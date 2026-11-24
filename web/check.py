#!/usr/bin/env python3
"""
Spark Automated Web & Consistency Quality Gate (web/check.py)

Enforces web/AGENTS.md, web/COMPONENTS.md, and templates/AGENTS.md across all
agents and models. Returns exit code 0 on pass, 1 on any violation.

Checks performed:
  1. Frontmatter metadata & enum validation (wiki entries & forecast trees)
  2. Bilingual 1:1 file synchronization & UI i18n key parity
  3. Design token discipline (zero hardcoded colors in styles/JS; zero inline styles in templates)
  4. Declarative `spark-visual` JSON schema & bilingual visual parity; no raw <script>/<style>/<canvas> in Markdown
  5. Image alt-text and local asset existence checks
  6. Clean deterministic build (web/build.py) + zero unresolved placeholders + zero broken internal links
"""

from __future__ import annotations

import json
import posixpath
import re
import sys
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
WEB_DIR = REPO_ROOT / "web"
DIST_DIR = REPO_ROOT / "dist"

sys.path.insert(0, str(WEB_DIR))
import build as spark_build  # noqa: E402

VALID_KINDS = {"concept", "tech", "society", "place", "era"}
VALID_STATUSES = {"draft", "canon", "retconned"}
VALID_GROUNDINGS = {"established", "plausible", "speculative"}
VALID_LIFECYCLES = {"active", "retired"}
APPROVED_VISUAL_TYPES = spark_build.APPROVED_VISUAL_TYPES
APPROVED_SCALE_MODES = spark_build.APPROVED_SCALE_MODES

COLOR_RE = re.compile(r"(#[0-9a-fA-F]{3,8}\b|\brgba?\s*\(|\bhsla?\s*\()")
INLINE_STYLE_RE = re.compile(r"\bstyle\s*=")
RAW_EMBED_RE = re.compile(r"<\s*(script|style|canvas)\b", re.IGNORECASE)
VISUAL_BLOCK_RE = re.compile(r"```spark-visual\s*\n(.*?)\n```", re.DOTALL)
MD_IMAGE_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
PLACEHOLDER_RE = re.compile(r"\{\{[a-zA-Z0-9_]+\}\}")
HREF_OR_SRC_RE = re.compile(r'(?:href|src)="([^"]+)"')


def validate_visual_spec(raw_json: str, src_rel: str) -> tuple[list[str], tuple[str, str, str] | None]:
    """Validate a single `spark-visual` JSON block against web/COMPONENTS.md schemas."""
    errs: list[str] = []
    try:
        spec = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        return [f"{src_rel}: invalid spark-visual JSON: {exc}"], None

    if not isinstance(spec, dict):
        return [f"{src_rel}: spark-visual block must be a JSON object"], None

    vtype = spec.get("type")
    vid = spec.get("id")
    vtitle = spec.get("title")
    scale_mode = spec.get("scale_mode")
    caption = spec.get("caption")
    params = spec.get("params")

    if vtype not in APPROVED_VISUAL_TYPES:
        errs.append(f"{src_rel}: unapproved spark-visual type '{vtype}' (allowed: {sorted(APPROVED_VISUAL_TYPES)})")
    if not isinstance(vid, str) or not re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", vid):
        errs.append(f"{src_rel}: invalid spark-visual id '{vid}' (must be lowercase-kebab)")
    if not isinstance(vtitle, str) or not vtitle.strip():
        errs.append(f"{src_rel}: missing non-empty spark-visual title")
    if scale_mode not in APPROVED_SCALE_MODES:
        errs.append(f"{src_rel}: invalid spark-visual scale_mode '{scale_mode}' (allowed: {sorted(APPROVED_SCALE_MODES)})")
    if not isinstance(caption, str) or not caption.strip():
        errs.append(f"{src_rel}: missing non-empty spark-visual caption")
    if not isinstance(params, dict):
        errs.append(f"{src_rel}: spark-visual 'params' must be an object")
        return errs, None

    # Engine-specific parameter checks
    if vtype == "orbital-transfer":
        for req in ("origin_label", "target_label", "delta_v_km_s", "payload_mass_t"):
            if req not in params:
                errs.append(f"{src_rel} ({vid}): orbital-transfer missing param '{req}'")
        if isinstance(params.get("delta_v_km_s"), (int, float)) and params["delta_v_km_s"] <= 0:
            errs.append(f"{src_rel} ({vid}): delta_v_km_s must be > 0")
        if isinstance(params.get("payload_mass_t"), (int, float)) and params["payload_mass_t"] <= 0:
            errs.append(f"{src_rel} ({vid}): payload_mass_t must be > 0")
    elif vtype == "energy-budget":
        for req in ("mass_t", "delta_v_km_s", "efficiency", "cadence_per_day"):
            if req not in params:
                errs.append(f"{src_rel} ({vid}): energy-budget missing param '{req}'")
        eff = params.get("efficiency")
        if not isinstance(eff, (int, float)) or not (0 < eff <= 1):
            errs.append(f"{src_rel} ({vid}): efficiency must be in (0, 1]")
    elif vtype == "phase-progression":
        stages = params.get("stages")
        if not isinstance(stages, list) or not (2 <= len(stages) <= 6):
            errs.append(f"{src_rel} ({vid}): phase-progression 'stages' must be a list of 2..6 objects")
        else:
            for idx, st in enumerate(stages):
                if not isinstance(st, dict) or not all(isinstance(st.get(k), str) and st.get(k).strip() for k in ("code", "label", "summary")):
                    errs.append(f"{src_rel} ({vid}): stage[{idx}] must have non-empty strings 'code', 'label', 'summary'")

    sig = (str(vid), str(vtype), str(scale_mode)) if not errs else None
    return errs, sig


def check_css_and_templates(errors: list[str]) -> None:
    """Enforce design token discipline: no hardcoded colors or ad-hoc inline styles."""
    tokens_path = WEB_DIR / "tokens.css"
    if not tokens_path.is_file():
        errors.append("Missing web/tokens.css")
    else:
        t_text = tokens_path.read_text(encoding="utf-8")
        if t_text.count("{") != t_text.count("}"):
            errors.append("Unbalanced braces in web/tokens.css")

    for css_file in sorted((WEB_DIR / "styles").glob("*.css")):
        hits = COLOR_RE.findall(css_file.read_text(encoding="utf-8"))
        if hits:
            errors.append(f"{css_file.relative_to(REPO_ROOT).as_posix()}: hardcoded color(s) forbidden outside tokens.css: {hits[:5]}")

    for js_file in sorted((WEB_DIR / "js").rglob("*.js")):
        hits = COLOR_RE.findall(js_file.read_text(encoding="utf-8"))
        if hits:
            errors.append(f"{js_file.relative_to(REPO_ROOT).as_posix()}: hardcoded color(s) forbidden in JS: {hits[:5]}")

    for tpl_file in sorted((WEB_DIR / "templates").glob("*.html")):
        hits = INLINE_STYLE_RE.findall(tpl_file.read_text(encoding="utf-8"))
        if hits:
            errors.append(f"{tpl_file.relative_to(REPO_ROOT).as_posix()}: inline style attribute forbidden in templates")


def check_i18n(errors: list[str]) -> int:
    """Verify web/i18n/en.json and web/i18n/zh-tw.json have 100% symmetric keys."""
    def flatten(obj: dict[str, Any], prefix: str = "") -> set[str]:
        out: set[str] = set()
        for k, v in obj.items():
            full = f"{prefix}.{k}" if prefix else k
            if isinstance(v, dict):
                out |= flatten(v, full)
            else:
                if not isinstance(v, str) or not v.strip():
                    errors.append(f"Empty or non-string i18n value at '{full}'")
                out.add(full)
        return out

    en_data = json.loads((WEB_DIR / "i18n" / "en.json").read_text(encoding="utf-8"))
    tw_data = json.loads((WEB_DIR / "i18n" / "zh-tw.json").read_text(encoding="utf-8"))
    en_k, tw_k = flatten(en_data), flatten(tw_data)
    if en_k != tw_k:
        if en_k - tw_k:
            errors.append(f"i18n keys missing in zh-tw.json: {sorted(en_k - tw_k)}")
        if tw_k - en_k:
            errors.append(f"i18n keys missing in en.json: {sorted(tw_k - en_k)}")
    return len(en_k)


def check_markdown_content(errors: list[str]) -> dict[str, list[tuple[str, str, str]]]:
    """Validate frontmatter, bilingual pairs, spark-visual schemas, images, and raw HTML embeds."""
    content_paths: list[Path] = []
    for root_doc in spark_build.ROOT_DOCS:
        p = REPO_ROOT / root_doc
        if p.is_file():
            content_paths.append(p)
    for folder in spark_build.CONTENT_ROOTS:
        d = REPO_ROOT / folder
        if d.is_dir():
            for p in sorted(d.rglob("*.md")):
                if p.name != "AGENTS.md":
                    content_paths.append(p)

    rel_set = {p.relative_to(REPO_ROOT).as_posix() for p in content_paths}
    visuals_by_src: dict[str, list[tuple[str, str, str]]] = {}

    for p in content_paths:
        src_rel = p.relative_to(REPO_ROOT).as_posix()
        raw = p.read_text(encoding="utf-8")
        meta, body = spark_build.parse_frontmatter(raw)

        # 1. Bilingual 1:1 pair check
        cp = spark_build.find_counterpart_src(src_rel)
        if cp and cp not in rel_set:
            errors.append(f"{src_rel}: missing bilingual counterpart '{cp}'")

        # 2. Frontmatter checks for wiki entries
        if src_rel.startswith(("wiki/", "wiki-tw/")):
            if not meta.get("title"):
                errors.append(f"{src_rel}: missing frontmatter 'title'")
            if meta.get("kind") not in VALID_KINDS:
                errors.append(f"{src_rel}: invalid frontmatter 'kind'={meta.get('kind')!r}")
            if meta.get("status") not in VALID_STATUSES:
                errors.append(f"{src_rel}: invalid frontmatter 'status'={meta.get('status')!r}")
            if meta.get("grounding") not in VALID_GROUNDINGS:
                errors.append(f"{src_rel}: invalid frontmatter 'grounding'={meta.get('grounding')!r}")

        # 3. Frontmatter checks for thematic forecast trees
        if src_rel.startswith(("forecasts/", "forecasts-tw/")) and not src_rel.endswith("/index.md"):
            for req in ("title", "id", "period", "evidence_cutoff", "updated", "lifecycle"):
                if not meta.get(req):
                    errors.append(f"{src_rel}: missing forecast frontmatter '{req}'")
            if meta.get("lifecycle") and meta.get("lifecycle") not in VALID_LIFECYCLES:
                errors.append(f"{src_rel}: invalid forecast 'lifecycle'={meta.get('lifecycle')!r}")

        # 4. Disallow raw <script>, <style>, <canvas> in Markdown prose (outside fenced code blocks)
        body_no_fences = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
        if RAW_EMBED_RE.search(body_no_fences):
            errors.append(f"{src_rel}: raw <script>/<style>/<canvas> tags are forbidden in Markdown")

        # 5. Validate declarative `spark-visual` blocks
        seen_vids: set[str] = set()
        page_sigs: list[tuple[str, str, str]] = []
        for m in VISUAL_BLOCK_RE.finditer(body):
            v_errs, sig = validate_visual_spec(m.group(1), src_rel)
            errors.extend(v_errs)
            if sig:
                if sig[0] in seen_vids:
                    errors.append(f"{src_rel}: duplicate spark-visual id '{sig[0]}'")
                seen_vids.add(sig[0])
                page_sigs.append(sig)
        visuals_by_src[src_rel] = page_sigs

        # 6. Validate embedded Markdown images
        for im in MD_IMAGE_RE.finditer(body_no_fences):
            alt_text = im.group(1).strip()
            img_src = im.group(2).strip()
            if not alt_text:
                errors.append(f"{src_rel}: image '{img_src}' is missing descriptive alt text")
            if not img_src.startswith(("http://", "https://")):
                resolved = posixpath.normpath(posixpath.join(posixpath.dirname(src_rel), img_src))
                if not (REPO_ROOT / resolved).is_file():
                    errors.append(f"{src_rel}: image path not found '{img_src}' -> '{resolved}'")

    # 7. Bilingual parity of `spark-visual` blocks
    for src_rel, sigs in visuals_by_src.items():
        cp = spark_build.find_counterpart_src(src_rel)
        if cp and cp in visuals_by_src:
            if sigs != visuals_by_src[cp]:
                errors.append(f"{src_rel} <-> {cp}: mismatched spark-visual blocks ({sigs} vs {visuals_by_src[cp]})")

    return visuals_by_src


def check_built_dist(errors: list[str]) -> int:
    """Run web/build.py and verify zero broken links or unresolved placeholders in dist/."""
    try:
        spark_build.build()
    except Exception as exc:
        errors.append(f"web/build.py failed: {exc}")
        return 0

    html_files = sorted(DIST_DIR.rglob("*.html"))
    if not html_files:
        errors.append("dist/ contains no HTML files after build")
        return 0

    for hf in html_files:
        rel = hf.relative_to(DIST_DIR).as_posix()
        text = hf.read_text(encoding="utf-8")
        phs = PLACEHOLDER_RE.findall(text)
        if phs:
            errors.append(f"dist/{rel}: unresolved template placeholder(s): {phs[:5]}")
        for target in HREF_OR_SRC_RE.findall(text):
            if target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target_part = target.split("#", 1)[0].split("?", 1)[0]
            if not target_part:
                continue
            resolved = posixpath.normpath(posixpath.join(posixpath.dirname(rel), target_part))
            if not (DIST_DIR / resolved).exists():
                errors.append(f"dist/{rel}: broken internal link/asset '{target}' -> '{resolved}'")

    for json_name in ("search-index-en.json", "search-index-zh-tw.json", "graph.json"):
        jp = DIST_DIR / json_name
        if not jp.is_file():
            errors.append(f"Missing build artifact dist/{json_name}")
        else:
            try:
                json.loads(jp.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:
                errors.append(f"Invalid JSON in dist/{json_name}: {exc}")

    return len(html_files)


def main() -> int:
    errors: list[str] = []
    check_css_and_templates(errors)
    i18n_count = check_i18n(errors)
    visuals_by_src = check_markdown_content(errors)
    page_count = check_built_dist(errors)

    if errors:
        print(f"SPARK WEB CHECK FAILED ({len(errors)} violation(s)):", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    visual_total = sum(len(v) for v in visuals_by_src.values())
    print(
        f"SPARK WEB CHECK PASSED: {page_count} HTML pages, {i18n_count} i18n keys, "
        f"{visual_total} spark-visual blocks, 0 broken links, 0 token violations."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
