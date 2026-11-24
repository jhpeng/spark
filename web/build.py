#!/usr/bin/env python3
"""
Spark Deterministic Static Site Generator (web/build.py)

Compiles repository Markdown files into a bilingual static website under dist/
using only Python 3 standard library modules.

Follows web/AGENTS.md and web/COMPONENTS.md:
- Markdown files remain the single source of truth.
- All generated pages use the six approved archetypes in web/templates/.
- All UI labels come from web/i18n/{en,zh-tw}.json.
- Outputs offline search indices and dependency graph JSON.
"""

from __future__ import annotations

import hashlib
import html
import json
import os
import posixpath
import re
import shutil
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

REPO_ROOT = Path(__file__).resolve().parent.parent
WEB_DIR = REPO_ROOT / "web"
DIST_DIR = REPO_ROOT / "dist"
TEMPLATES_DIR = WEB_DIR / "templates"
I18N_DIR = WEB_DIR / "i18n"

CONTENT_ROOTS = [
    "canon",
    "forecasts",
    "forecasts-tw",
    "wiki",
    "wiki-tw",
    "stories",
    "stories-tw",
    "sessions",
]
ROOT_DOCS = ["open-questions.md", "open-questions-tw.md"]


@dataclass
class DocPage:
    src_rel: str            # e.g. "wiki/tech/orbital-transportation-network.md"
    out_rel: str            # e.g. "wiki/tech/orbital-transportation-network.html"
    lang: str               # "en" | "zh-tw"
    archetype: str          # one of the 6 approved archetypes
    section: str            # "canon" | "forecasts" | "wiki" | "stories" | "sessions" | "open-questions"
    subsection: str         # e.g. "tech", "concepts", "society", ""
    title: str
    meta: dict[str, Any]
    body_md: str
    excerpt: str = ""
    plain_text: str = ""
    toc: list[tuple[int, str, str]] = field(default_factory=list)
    depends_on_rels: list[str] = field(default_factory=list)
    body_links_rels: list[str] = field(default_factory=list)
    backlinks: list[str] = field(default_factory=list)
    citations: list[tuple[int, str, str, str]] = field(default_factory=list)
    counterpart_out: str = ""
    forecast_tree_data: dict[str, Any] | None = None


# ---------------------------------------------------------------------------
# Frontmatter & Slug Utilities
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict[str, Any], str]:
    """Parse simple YAML frontmatter without external dependencies."""
    if not text.startswith("---\n") and not text.startswith("---\r\n"):
        return {}, text
    lines = text.splitlines()
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return {}, text

    meta: dict[str, Any] = {}
    current_list_key: str | None = None
    for raw in lines[1:end_idx]:
        if not raw.strip() or raw.strip().startswith("#"):
            continue
        if re.match(r"^\s*-\s+", raw) and current_list_key:
            item = re.sub(r"^\s*-\s+", "", raw).strip()
            meta[current_list_key].append(_unquote(item))
            continue
        m = re.match(r"^([A-Za-z0-9_-]+)\s*:\s*(.*)$", raw)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val == "":
                meta[key] = []
                current_list_key = key
            elif val.startswith("[") and val.endswith("]"):
                inner = val[1:-1].strip()
                meta[key] = [_unquote(x.strip()) for x in inner.split(",") if x.strip()] if inner else []
                current_list_key = None
            elif val.lower() == "null":
                meta[key] = None
                current_list_key = None
            else:
                meta[key] = _unquote(val)
                current_list_key = None
    body = "\n".join(lines[end_idx + 1 :]).lstrip("\n")
    return meta, body


def _unquote(val: str) -> str:
    if len(val) >= 2 and ((val[0] == '"' and val[-1] == '"') or (val[0] == "'" and val[-1] == "'")):
        return val[1:-1]
    return val


def slugify(text: str) -> str:
    """Create a deterministic heading ID supporting ASCII and CJK headings."""
    cleaned = re.sub(r"[`*_~()\[\]{}:.,!?/\\|\"'「」『』（）—–·]+", " ", text).strip().lower()
    cleaned = re.sub(r"\s+", "-", cleaned)
    cleaned = unicodedata.normalize("NFKC", cleaned)
    return cleaned or "section"


def extract_first_h1(md: str) -> str | None:
    for line in md.splitlines():
        m = re.match(r"^#\s+(.+)$", line.strip())
        if m:
            return m.group(1).strip()
    return None


def strip_markdown_inline(text: str) -> str:
    text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[`*_~]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def resolve_md_target(from_src_rel: str, href: str) -> tuple[str | None, str]:
    """Resolve a relative .md href to a repo-relative .md path and optional #anchor."""
    if href.startswith(("http://", "https://", "mailto:", "#")):
        return None, ""
    if "#" in href:
        path_part, anchor = href.split("#", 1)
        anchor = "#" + anchor
    else:
        path_part, anchor = href, ""
    if not path_part.endswith(".md"):
        return None, anchor
    base_dir = posixpath.dirname(from_src_rel)
    resolved = posixpath.normpath(posixpath.join(base_dir, path_part))
    return resolved, anchor


def rel_href(from_out_rel: str, to_out_rel: str) -> str:
    from_dir = posixpath.dirname(from_out_rel)
    rel = posixpath.relpath(to_out_rel, from_dir or ".")
    return rel


def asset_prefix_for(out_rel: str) -> str:
    depth = out_rel.count("/")
    return "../" * depth


# ---------------------------------------------------------------------------
# Forecast Indented Tree Parser (for Interactive Mind-Map)
# ---------------------------------------------------------------------------

def _parse_fork_details(md: str) -> dict[str, dict[str, str]]:
    """Extract per-outcome fork question, deadline, confidence, rationale, signals, and anchor ID."""
    details: dict[str, dict[str, str]] = {}
    fork_chunks = re.split(r"(?m)^(?=###\s+)", md)
    for chunk in fork_chunks:
        hm = re.match(r"^###\s+(.+)$", chunk.splitlines()[0] if chunk.splitlines() else "")
        if not hm:
            continue
        heading_raw = hm.group(1).strip()
        heading_id = slugify(heading_raw)

        q_m = re.search(r"-\s*\*\*(?:Question|問題)\*\*[:：]\s*(.+)", chunk)
        question = strip_markdown_inline(q_m.group(1)) if q_m else strip_markdown_inline(heading_raw)

        dl_m = re.search(r"\*\*(?:Deadline|期限)\*\*[:：]\s*`?([0-9-]+)`?", chunk)
        deadline = dl_m.group(1) if dl_m else ""

        sig_m = re.search(r"-\s*\*\*(?:Validation(?:\s*(?:&|and)\s*revision)?\s*signals?|驗證與修訂訊號)\*\*[:：]\s*(.+)", chunk)
        signals = strip_markdown_inline(sig_m.group(1)) if sig_m else ""

        # Parse per-outcome table rows
        for line in chunk.splitlines():
            s = line.strip()
            if not s.startswith("|") or "`" not in s:
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) < 6:
                continue
            id_m = re.match(r"^`([a-z0-9-]+)`$", cells[0])
            if not id_m:
                continue
            oid = id_m.group(1)
            details[oid] = {
                "fork_heading": strip_markdown_inline(heading_raw),
                "fork_anchor": heading_id,
                "question": question,
                "deadline": deadline,
                "outcome_desc": strip_markdown_inline(cells[1]),
                "confidence": cells[4].strip("` "),
                "resolution": cells[5].strip("` "),
                "lifecycle": cells[6].strip("` ") if len(cells) > 6 else "active",
                "rationale": "",
                "signals": signals,
            }

        # Parse per-outcome rationale bullets: - **`outcome-id` (65%)**: ...
        for rm in re.finditer(r"^\s*-\s*\*\*`([a-z0-9-]+)`[^*]*\*\*[:：]\s*(.+)$", chunk, re.MULTILINE):
            oid = rm.group(1)
            if oid in details:
                details[oid]["rationale"] = strip_markdown_inline(rm.group(2))

    return details


def parse_forecast_tree_block(md: str, title: str, i18n: dict[str, Any]) -> dict[str, Any] | None:
    """Parse the indented text tree and fork sections in forecasts/*.md into Mind-Map JSON."""
    m = re.search(r"```text\s*\n(.*?)\n```", md, re.DOTALL)
    if not m:
        return None
    lines = [ln.rstrip() for ln in m.group(1).splitlines() if ln.strip()]
    if not lines:
        return None

    fork_details = _parse_fork_details(md)
    nodes: list[dict[str, Any]] = []
    stack: list[tuple[int, str]] = []  # (depth, node_id)

    for idx, raw in enumerate(lines):
        if idx == 0:
            root_id = "index"
            nodes.append({
                "id": root_id,
                "parent": None,
                "eyebrow": "BASELINE",
                "label": raw.strip(),
                "short_label": raw.strip(),
                "cond": "100%",
                "cum": 100.0,
                "confidence": "baseline",
                "resolution": "active",
                "is_leaf": False,
                "question": title,
                "deadline": "",
                "rationale": "",
                "signals": "",
                "fork_anchor": "",
            })
            stack = [(0, root_id)]
            continue

        branch_m = re.search(r"(├──|└──)\s+(.+)$", raw)
        if not branch_m:
            continue
        prefix_len = branch_m.start()
        depth = (prefix_len // 4) + 1
        content = branch_m.group(2).strip()
        is_marked_leaf = content.endswith("*")

        res_m = re.search(r"\[(pending|occurred|not-occurred|unresolved)\]", content)
        resolution = res_m.group(1) if res_m else "pending"
        content_clean = re.sub(r"\s*\[(pending|occurred|not-occurred|unresolved)\]\s*\*?\s*$", "", content).strip()

        prob_m = re.search(r"\(([^|)]+)\|\s*(?:path|路徑)\s*([0-9.]+)%\)", content_clean)
        cond_str = prob_m.group(1).strip() if prob_m else "—"
        cum_val = float(prob_m.group(2)) if prob_m else 0.0
        if prob_m:
            content_clean = content_clean[: prob_m.start()].strip()

        split_m = re.split(r"[:：]\s*", content_clean, maxsplit=1)
        if len(split_m) == 2:
            eyebrow_part, node_id = split_m[0].strip(), split_m[1].strip()
        else:
            eyebrow_part, node_id = content_clean, slugify(content_clean)

        while stack and stack[-1][0] >= depth:
            stack.pop()
        parent_id = stack[-1][1] if stack else "index"

        fd = fork_details.get(node_id, {})
        nodes.append({
            "id": node_id,
            "parent": parent_id,
            "eyebrow": eyebrow_part,
            "label": fd.get("outcome_desc") or f"{eyebrow_part} — {node_id}",
            "short_label": eyebrow_part,
            "cond": cond_str,
            "cum": cum_val,
            "confidence": fd.get("confidence", "—"),
            "resolution": fd.get("resolution") or resolution,
            "is_leaf": is_marked_leaf,
            "question": fd.get("question", ""),
            "deadline": fd.get("deadline", ""),
            "rationale": fd.get("rationale", ""),
            "signals": fd.get("signals", ""),
            "fork_anchor": fd.get("fork_anchor", ""),
        })
        stack.append((depth, node_id))

    if len(nodes) < 2:
        return None

    parent_ids = {n["parent"] for n in nodes if n["parent"]}
    leaf_sum = round(sum(n["cum"] for n in nodes if n["id"] not in parent_ids), 1)

    return {
        "title": title,
        "leaf_sum": leaf_sum,
        "nodes": nodes,
        "labels": {
            "inherited_path": i18n["forecast"]["inherited_path"],
            "conditional_prob": i18n["forecast"]["conditional_prob"],
            "path_prob": i18n["forecast"]["path_prob"],
            "confidence": i18n["forecast"]["confidence"],
            "resolution": i18n["forecast"]["resolution"],
            "deadline": i18n["forecast"]["deadline"],
            "leaf_sum_check": i18n["forecast"]["leaf_sum_check"],
            "filter_all": i18n["forecast"]["filter_all"],
            "jump_to_fork": i18n["forecast"]["jump_to_fork"],
            "rationale_label": i18n["forecast"]["rationale_label"],
            "signals_label": i18n["forecast"]["signals_label"],
            "zoom_in": i18n["forecast"]["zoom_in"],
            "zoom_out": i18n["forecast"]["zoom_out"],
            "zoom_reset": i18n["forecast"]["zoom_reset"],
            "res_labels": i18n["resolution"],
        },
    }


# ---------------------------------------------------------------------------
# Markdown Renderer (Pure Python)
# ---------------------------------------------------------------------------

APPROVED_VISUAL_TYPES = {"orbital-transfer", "energy-budget", "phase-progression"}
APPROVED_SCALE_MODES = {"schematic", "to-scale"}


def render_spark_visual_block(raw_json: str, src_rel: str, i18n: dict[str, Any]) -> str:
    """Validate and render an approved declarative `spark-visual` JSON block."""
    try:
        spec = json.loads(raw_json)
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid spark-visual JSON in {src_rel}: {exc}") from exc

    if not isinstance(spec, dict):
        raise ValueError(f"spark-visual block in {src_rel} must be a JSON object")

    vtype = spec.get("type")
    vid = spec.get("id")
    vtitle = spec.get("title")
    scale_mode = spec.get("scale_mode")
    caption = spec.get("caption")
    params = spec.get("params")

    if vtype not in APPROVED_VISUAL_TYPES:
        raise ValueError(f"Unapproved spark-visual type '{vtype}' in {src_rel} (allowed: {sorted(APPROVED_VISUAL_TYPES)})")
    if not isinstance(vid, str) or not re.match(r"^[a-z0-9]+(?:-[a-z0-9]+)*$", vid):
        raise ValueError(f"Invalid spark-visual id '{vid}' in {src_rel} (must be lowercase-kebab)")
    if not isinstance(vtitle, str) or not vtitle.strip():
        raise ValueError(f"Missing spark-visual title in {src_rel}")
    if scale_mode not in APPROVED_SCALE_MODES:
        raise ValueError(f"Invalid spark-visual scale_mode '{scale_mode}' in {src_rel}")
    if not isinstance(caption, str) or not caption.strip():
        raise ValueError(f"Missing spark-visual caption in {src_rel}")
    if not isinstance(params, dict):
        raise ValueError(f"Missing spark-visual params object in {src_rel}")

    scale_label = i18n["visual"]["scale_to_scale"] if scale_mode == "to-scale" else i18n["visual"]["scale_schematic"]
    payload = {
        "type": vtype,
        "id": vid,
        "title": vtitle,
        "scale_mode": scale_mode,
        "params": params,
        "labels": i18n["visual"],
    }
    json_blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")

    return (
        f'<figure class="sp-visual-frame" id="visual-{html.escape(vid)}" '
        f'data-component="spark-visual" data-visual-type="{html.escape(vtype)}">'
        f'<div class="sp-visual-header">'
        f'<div><div class="sp-eyebrow">SPARK-VISUAL · {html.escape(vtype)}</div>'
        f'<div class="sp-visual-title">{html.escape(vtitle)}</div></div>'
        f'<div class="sp-visual-controls">'
        f'<span class="sp-badge">{html.escape(scale_label)}</span>'
        f"</div></div>"
        f'<script type="application/json" class="sp-visual-data">{json_blob}</script>'
        f'<div class="sp-visual-stage"></div>'
        f'<figcaption class="sp-visual-caption">{html.escape(caption)}</figcaption>'
        f"</figure>"
    )


def render_markdown(
    md: str,
    doc: DocPage,
    src_to_out: dict[str, str],
    i18n: dict[str, Any],
    strip_first_h1: bool = True,
    hide_ascii_tree: bool = False,
) -> tuple[str, list[tuple[int, str, str]], list[str], list[tuple[int, str, str, str]]]:
    """Convert Markdown to semantic HTML, returning (html, toc, resolved_md_links, citations)."""
    lines = md.splitlines()
    out: list[str] = []
    toc: list[tuple[int, str, str]] = []
    used_ids: set[str] = set()
    body_links: list[str] = []
    citations: list[tuple[int, str, str, str]] = []
    citation_url_to_idx: dict[str, int] = {}

    i = 0
    n = len(lines)
    skipped_h1 = False
    skipped_tree = False

    def unique_id(text: str) -> str:
        base = slugify(text)
        cand = base
        k = 2
        while cand in used_ids:
            cand = f"{base}-{k}"
            k += 1
        used_ids.add(cand)
        return cand

    def render_inline(text: str) -> str:
        # Protect inline code first
        code_tokens: list[str] = []

        def _save_code(match: re.Match[str]) -> str:
            idx = len(code_tokens)
            code_tokens.append(f"<code>{html.escape(match.group(1))}</code>")
            return f"\x00CODE{idx}\x00"

        text = re.sub(r"`([^`]+)`", _save_code, text)
        text = html.escape(text)

        # Images ![alt](src)
        text = re.sub(
            r"!\[([^\]]*)\]\(([^)]+)\)",
            lambda m: f'<img src="{m.group(2)}" alt="{m.group(1)}" loading="lazy">',
            text,
        )

        # Links [label](href)
        def _render_link(m: re.Match[str]) -> str:
            label = m.group(1)
            raw_href = html.unescape(m.group(2)).strip()
            if raw_href.startswith(("http://", "https://")):
                if raw_href not in citation_url_to_idx:
                    cite_num = len(citations) + 1
                    citation_url_to_idx[raw_href] = cite_num
                    domain = urlparse(raw_href).netloc.replace("www.", "")
                    citations.append((cite_num, html.unescape(label), raw_href, domain))
                else:
                    cite_num = citation_url_to_idx[raw_href]
                return (
                    f'<a class="sp-cite-link" href="{html.escape(raw_href)}" target="_blank" '
                    f'rel="noopener noreferrer">{label}<sup class="sp-cite-num">[{cite_num}]</sup></a>'
                )
            if raw_href.startswith("#"):
                return f'<a href="{html.escape(raw_href)}">{label}</a>'
            target_md, anchor = resolve_md_target(doc.src_rel, raw_href)
            if target_md == "README.md":
                home_target = "zh-tw/index.html" if doc.lang == "zh-tw" else "index.html"
                return f'<a href="{html.escape(rel_href(doc.out_rel, home_target))}">{label}</a>'
            if target_md and target_md in src_to_out:
                body_links.append(target_md)
                href_out = rel_href(doc.out_rel, src_to_out[target_md]) + anchor
                return f'<a href="{html.escape(href_out)}">{label}</a>'
            if target_md:
                return f'<code title="{html.escape(target_md)}">{label}</code>'
            return f'<a href="{html.escape(raw_href)}">{label}</a>'

        text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", _render_link, text)
        text = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", text)
        text = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", text)

        for idx, code_html in enumerate(code_tokens):
            text = text.replace(f"\x00CODE{idx}\x00", code_html)
        return text

    def flush_list(start_idx: int) -> tuple[str, int]:
        items: list[tuple[int, bool, str]] = []
        idx = start_idx
        while idx < n:
            ln = lines[idx]
            m_ul = re.match(r"^(\s*)[-*]\s+(.+)$", ln)
            m_ol = re.match(r"^(\s*)\d+\.\s+(.+)$", ln)
            if m_ul:
                items.append((len(m_ul.group(1)), False, m_ul.group(2)))
                idx += 1
            elif m_ol:
                items.append((len(m_ol.group(1)), True, m_ol.group(2)))
                idx += 1
            elif ln.strip() == "":
                # Peek ahead: if next non-empty line is indented list item, continue
                if idx + 1 < n and re.match(r"^\s+([-*]|\d+\.)\s+", lines[idx + 1]):
                    idx += 1
                    continue
                break
            else:
                break

        if not items:
            return "", start_idx

        html_parts: list[str] = []
        tag_stack: list[tuple[int, str]] = []  # (indent, "ul"|"ol")

        for indent, is_ol, content in items:
            tag = "ol" if is_ol else "ul"
            if not tag_stack:
                html_parts.append(f"<{tag}>")
                tag_stack.append((indent, tag))
            elif indent > tag_stack[-1][0]:
                html_parts.append(f"<{tag}>")
                tag_stack.append((indent, tag))
            else:
                while len(tag_stack) > 1 and indent < tag_stack[-1][0]:
                    _, closing = tag_stack.pop()
                    html_parts.append(f"</{closing}>")
                if tag_stack[-1][1] != tag:
                    _, closing = tag_stack.pop()
                    html_parts.append(f"</{closing}><{tag}>")
                    tag_stack.append((indent, tag))
            html_parts.append(f"<li>{render_inline(content)}</li>")

        while tag_stack:
            _, closing = tag_stack.pop()
            html_parts.append(f"</{closing}>")
        return "\n".join(html_parts), idx

    def flush_table(start_idx: int) -> tuple[str, int]:
        header_cells = [c.strip() for c in lines[start_idx].strip().strip("|").split("|")]
        idx = start_idx + 2  # skip separator row
        rows: list[list[str]] = []
        while idx < n and lines[idx].strip().startswith("|") and "|" in lines[idx].strip()[1:]:
            rows.append([c.strip() for c in lines[idx].strip().strip("|").split("|")])
            idx += 1

        ths = "".join(f"<th>{render_inline(c)}</th>" for c in header_cells)
        body_rows = []
        for r in rows:
            tds = "".join(f"<td>{render_inline(c)}</td>" for c in r)
            body_rows.append(f"<tr>{tds}</tr>")
        table_html = f"<table><thead><tr>{ths}</tr></thead><tbody>{''.join(body_rows)}</tbody></table>"
        return table_html, idx

    while i < n:
        line = lines[i]
        stripped = line.strip()

        if not stripped:
            i += 1
            continue

        # Fenced code block
        if stripped.startswith("```"):
            lang = stripped[3:].strip()
            code_lines: list[str] = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # consume closing ```
            if hide_ascii_tree and lang == "text" and not skipped_tree:
                skipped_tree = True
                continue
            if lang == "spark-visual":
                out.append(render_spark_visual_block("\n".join(code_lines), doc.src_rel, i18n))
                continue
            cls = f' class="language-{html.escape(lang)}"' if lang else ""
            out.append(f"<pre><code{cls}>{html.escape(chr(10).join(code_lines))}</code></pre>")
            continue

        # Headings
        hm = re.match(r"^(#{1,6})\s+(.+)$", stripped)
        if hm:
            level = len(hm.group(1))
            raw_title = hm.group(2).strip()
            if level == 1 and strip_first_h1 and not skipped_h1:
                skipped_h1 = True
                i += 1
                continue
            hid = unique_id(raw_title)
            if level in (2, 3):
                toc.append((level, hid, strip_markdown_inline(raw_title)))
            out.append(f'<h{level} id="{hid}">{render_inline(raw_title)}</h{level}>')
            i += 1
            continue

        # Horizontal rule
        if re.match(r"^[-*_]{3,}$", stripped):
            out.append("<hr>")
            i += 1
            continue

        # Table
        if stripped.startswith("|") and i + 1 < n and re.match(r"^\|[\s:|-]+\|$", lines[i + 1].strip()):
            tbl_html, i = flush_table(i)
            out.append(tbl_html)
            continue

        # Blockquote
        if stripped.startswith(">"):
            bq_lines: list[str] = []
            while i < n and lines[i].strip().startswith(">"):
                bq_lines.append(re.sub(r"^>\s?", "", lines[i].strip()))
                i += 1
            out.append(f"<blockquote><p>{render_inline(' '.join(bq_lines))}</p></blockquote>")
            continue

        # Lists
        if re.match(r"^\s*([-*]|\d+\.)\s+", line):
            list_html, i = flush_list(i)
            out.append(list_html)
            continue

        # Paragraph
        para_lines = [stripped]
        i += 1
        while i < n:
            nxt = lines[i].strip()
            if (
                not nxt
                or nxt.startswith(("#", "```", ">", "|"))
                or re.match(r"^[-*_]{3,}$", nxt)
                or re.match(r"^\s*([-*]|\d+\.)\s+", lines[i])
            ):
                break
            para_lines.append(nxt)
            i += 1
        out.append(f"<p>{render_inline(' '.join(para_lines))}</p>")

    return "\n".join(out), toc, body_links, citations


# ---------------------------------------------------------------------------
# Phase 3: Scientific Evidence, Citations & Canon Structured Views
# ---------------------------------------------------------------------------

def build_citations_html(citations: list[tuple[int, str, str, str]], i18n: dict[str, Any]) -> str:
    if not citations:
        return ""
    items = []
    for num, label, url, domain in citations:
        items.append(
            f'<li class="sp-citation-item">'
            f'<span class="sp-citation-idx">[{num}]</span>'
            f'<a href="{html.escape(url)}" target="_blank" rel="noopener noreferrer">{html.escape(label)}</a>'
            f'<span class="sp-citation-domain">{html.escape(domain)}</span>'
            f"</li>"
        )
    return (
        f'<section class="sp-citations" aria-label="{html.escape(i18n["science"]["citations"])}">'
        f'<h2 class="sp-citations-title">{html.escape(i18n["science"]["citations"])} ({len(citations)})</h2>'
        f'<ol class="sp-citations-list">{"".join(items)}</ol>'
        f"</section>"
    )


def _classify_validation_subsection(heading_text: str, i18n: dict[str, Any]) -> tuple[str, str]:
    low = heading_text.lower()
    if any(k in low for k in ("consistency", "一致性")):
        return "consistency", i18n["science"]["consistency"]
    if any(k in low for k in ("motive", "動機", "adoption", "採用")):
        return "motive", i18n["science"]["motive"]
    return "physics", i18n["science"]["physics"]


def enhance_wiki_html(body_html: str, i18n: dict[str, Any]) -> str:
    """Wrap standard Validation subsections, Branch blocks, and Open Questions in structured cards."""
    # Split body into H2 sections
    parts = re.split(r'(?=<h2\b[^>]*>)', body_html)
    enhanced: list[str] = []

    for part in parts:
        m_h2 = re.match(r'^<h2\b[^>]*>(.*?)</h2>(.*)$', part, re.DOTALL)
        if not m_h2:
            enhanced.append(part)
            continue

        h2_inner = m_h2.group(1)
        h2_plain = re.sub(r"<[^>]+>", "", h2_inner).strip().lower()
        h2_tag = part[: m_h2.start(2)]
        rest = m_h2.group(2)

        # 1. Validation / 驗證 -> wrap each H3 subsection in a structured .sp-validation-card
        if h2_plain in ("validation", "驗證"):
            subparts = re.split(r'(?=<h3\b[^>]*>)', rest)
            cards: list[str] = []
            lead = subparts[0].strip()
            if lead:
                cards.append(lead)
            for sp in subparts[1:]:
                m_h3 = re.match(r'^<h3\b[^>]*>(.*?)</h3>(.*)$', sp, re.DOTALL)
                if not m_h3:
                    cards.append(sp)
                    continue
                h3_plain = re.sub(r"<[^>]+>", "", m_h3.group(1)).strip()
                kind_cls, kind_label = _classify_validation_subsection(h3_plain, i18n)
                cards.append(
                    f'<div class="sp-validation-card sp-validation-card--{kind_cls}">'
                    f'<div class="sp-validation-label">{html.escape(kind_label)}</div>'
                    f"{sp}"
                    f"</div>"
                )
            enhanced.append(f'{h2_tag}<div class="sp-validation-grid">{"".join(cards)}</div>')
            continue

        # 2. Open questions / 待解問題 -> wrap in .sp-open-q callout
        if h2_plain in ("open questions", "待解問題"):
            enhanced.append(
                f'<section class="sp-open-q">'
                f'<div class="sp-validation-label">{html.escape(i18n["science"]["open_questions"])}</div>'
                f"{part}"
                f"</section>"
            )
            continue

        # 3. Reasoning / 推論 -> highlight ### Branch ... / ### 分支 ... blocks
        if h2_plain in ("reasoning", "推論"):
            subparts = re.split(r'(?=<h3\b[^>]*>)', rest)
            rebuilt = [subparts[0]]
            for sp in subparts[1:]:
                m_h3 = re.match(r'^<h3\b[^>]*>(.*?)</h3>(.*)$', sp, re.DOTALL)
                if m_h3:
                    h3_plain = re.sub(r"<[^>]+>", "", m_h3.group(1)).strip()
                    if re.match(r"^(branch|分支)\b", h3_plain, re.IGNORECASE) or h3_plain.startswith("分支"):
                        rebuilt.append(
                            f'<div class="sp-branch-card">'
                            f'<div class="sp-branch-eyebrow">{html.escape(i18n["science"]["branch_scope"])}</div>'
                            f"{sp}"
                            f"</div>"
                        )
                        continue
                rebuilt.append(sp)
            enhanced.append(h2_tag + "".join(rebuilt))
            continue

        enhanced.append(part)

    return "".join(enhanced)


def enhance_canon_laws_html(body_html: str, i18n: dict[str, Any]) -> str:
    """Wrap each H2 physical-law category in a numbered .sp-law-card."""
    parts = re.split(r'(?=<h2\b[^>]*>)', body_html)
    out: list[str] = []
    law_idx = 0
    for part in parts:
        m_h2 = re.match(r'^<h2\b[^>]*>(.*?)</h2>', part, re.DOTALL)
        if not m_h2:
            out.append(part)
            continue
        law_idx += 1
        title_plain = re.sub(r"<[^>]+>", "", m_h2.group(1)).strip().lower()
        is_spec = "speculative" in title_plain or "推測" in title_plain
        extra_cls = " sp-law-card--speculative" if is_spec else ""
        label = f'{i18n["science"]["law_principle"]} {law_idx:02d}'
        out.append(
            f'<section class="sp-law-card{extra_cls}">'
            f'<div class="sp-law-num">{html.escape(label)}</div>'
            f"{part}"
            f"</section>"
        )
    return "".join(out)


def enhance_canon_timeline_html(body_html: str, i18n: dict[str, Any]) -> str:
    """Convert canon timeline tables into a filterable vertical observatory timeline."""
    # Find all <table> blocks and any preceding H2/H3 branch heading
    sections = re.split(r'(?=<h[23]\b[^>]*>)', body_html)
    events: list[tuple[str, str, str, str, str]] = []  # (branch_key, branch_label, date, event_html, ref_html)
    intro_html: list[str] = []

    for sec in sections:
        m_h = re.match(r'^<h[23]\b[^>]*>(.*?)</h[23]>(.*)$', sec, re.DOTALL)
        if m_h:
            b_label = re.sub(r"<[^>]+>", "", m_h.group(1)).strip()
            b_key = slugify(b_label)
            chunk = m_h.group(2)
        else:
            b_label = i18n["science"]["timeline_shared"]
            b_key = "shared"
            chunk = sec

        m_tbl = re.search(r"<table>.*?<tbody>(.*?)</tbody></table>", chunk, re.DOTALL)
        if not m_tbl:
            intro_html.append(sec)
            continue

        before_tbl = chunk[: m_tbl.start()].strip()
        if before_tbl and not m_h:
            intro_html.append(before_tbl)

        for tr in re.findall(r"<tr>(.*?)</tr>", m_tbl.group(1), re.DOTALL):
            tds = re.findall(r"<td>(.*?)</td>", tr, re.DOTALL)
            if len(tds) >= 2:
                date_str = re.sub(r"<[^>]+>", "", tds[0]).strip()
                event_html = tds[1].strip()
                ref_html = tds[2].strip() if len(tds) >= 3 else ""
                events.append((b_key, b_label, date_str, event_html, ref_html))

    if not events:
        return body_html

    branches = list(dict.fromkeys((bk, bl) for bk, bl, _, _, _ in events))
    controls = [
        f'<button type="button" class="sp-btn sp-btn--active" data-timeline-filter="all">{html.escape(i18n["science"]["timeline_all"])}</button>'
    ]
    for bk, bl in branches:
        controls.append(
            f'<button type="button" class="sp-btn" data-timeline-filter="{html.escape(bk)}">{html.escape(bl)}</button>'
        )

    items_html = []
    for bk, bl, date_str, event_html, ref_html in events:
        ref_block = f'<div class="sp-timeline-ref">{ref_html}</div>' if ref_html and ref_html != "—" else ""
        items_html.append(
            f'<div class="sp-timeline-item" data-branch="{html.escape(bk)}">'
            f'<span class="sp-timeline-dot" aria-hidden="true"></span>'
            f'<div class="sp-timeline-head">'
            f'<span class="sp-timeline-date">{html.escape(date_str)}</span>'
            f'<span class="sp-badge">{html.escape(bl)}</span>'
            f"</div>"
            f'<p class="sp-timeline-event">{event_html}</p>'
            f"{ref_block}"
            f"</div>"
        )

    return (
        "".join(intro_html)
        + f'<div class="sp-timeline-controls" data-component="timeline-filter">{"".join(controls)}</div>'
        + f'<div class="sp-timeline">{"".join(items_html)}</div>'
    )


# ---------------------------------------------------------------------------
# Discovery & Bilingual Pairing
# ---------------------------------------------------------------------------

def classify_source(src_rel: str) -> tuple[str, str, str, str]:
    """Return (lang, archetype, section, subsection)."""
    parts = src_rel.split("/")
    if src_rel == "open-questions.md":
        return "en", "index-log", "open-questions", ""
    if src_rel == "open-questions-tw.md":
        return "zh-tw", "index-log", "open-questions", ""
    top = parts[0]
    if top == "canon":
        lang = "zh-tw" if src_rel.endswith("-tw.md") else "en"
        return lang, "canon-doc", "canon", ""
    if top == "forecasts":
        return "en", "forecast-tree", "forecasts", ""
    if top == "forecasts-tw":
        return "zh-tw", "forecast-tree", "forecasts", ""
    if top == "wiki":
        sub = parts[1] if len(parts) > 2 else ""
        return "en", "wiki-entry", "wiki", sub
    if top == "wiki-tw":
        sub = parts[1] if len(parts) > 2 else ""
        return "zh-tw", "wiki-entry", "wiki", sub
    if top == "stories":
        return "en", "story", "stories", ""
    if top == "stories-tw":
        return "zh-tw", "story", "stories", ""
    if top == "sessions":
        return "en", "index-log", "sessions", ""
    return "en", "index-log", "other", ""


def find_counterpart_src(src_rel: str) -> str | None:
    if src_rel == "open-questions.md":
        return "open-questions-tw.md"
    if src_rel == "open-questions-tw.md":
        return "open-questions.md"
    if src_rel.startswith("wiki/"):
        return "wiki-tw/" + src_rel[len("wiki/") :]
    if src_rel.startswith("wiki-tw/"):
        return "wiki/" + src_rel[len("wiki-tw/") :]
    if src_rel.startswith("forecasts/"):
        return "forecasts-tw/" + src_rel[len("forecasts/") :]
    if src_rel.startswith("forecasts-tw/"):
        return "forecasts/" + src_rel[len("forecasts-tw/") :]
    if src_rel.startswith("stories/"):
        return "stories-tw/" + src_rel[len("stories/") :]
    if src_rel.startswith("stories-tw/"):
        return "stories/" + src_rel[len("stories-tw/") :]
    if src_rel.startswith("canon/"):
        if src_rel.endswith("-tw.md"):
            return src_rel[: -len("-tw.md")] + ".md"
        return src_rel[: -len(".md")] + "-tw.md"
    return None


def discover_docs(i18n_map: dict[str, dict[str, Any]]) -> list[DocPage]:
    md_files: list[Path] = []
    for root_doc in ROOT_DOCS:
        p = REPO_ROOT / root_doc
        if p.is_file():
            md_files.append(p)
    for folder in CONTENT_ROOTS:
        d = REPO_ROOT / folder
        if d.is_dir():
            for p in sorted(d.rglob("*.md")):
                if p.name == "AGENTS.md":
                    continue
                md_files.append(p)

    docs: list[DocPage] = []
    for p in sorted(md_files):
        src_rel = p.relative_to(REPO_ROOT).as_posix()
        out_rel = src_rel[:-3] + ".html"
        lang, archetype, section, subsection = classify_source(src_rel)
        raw = p.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        title = str(meta.get("title") or extract_first_h1(body) or p.stem)
        plain = strip_markdown_inline(re.sub(r"```.*?```", " ", body, flags=re.DOTALL))
        excerpt = plain[:180].rstrip() + ("…" if len(plain) > 180 else "")

        doc = DocPage(
            src_rel=src_rel,
            out_rel=out_rel,
            lang=lang,
            archetype=archetype,
            section=section,
            subsection=subsection,
            title=title,
            meta=meta,
            body_md=body,
            excerpt=excerpt,
            plain_text=plain,
        )

        # Extract depends_on / uses links from frontmatter
        for field_name in ("depends_on", "uses"):
            vals = meta.get(field_name)
            if isinstance(vals, list):
                for entry in vals:
                    lm = re.search(r"\(([^)]+)\)", str(entry))
                    href = lm.group(1) if lm else str(entry)
                    target, _ = resolve_md_target(src_rel, href)
                    if target:
                        doc.depends_on_rels.append(target)

        if archetype == "forecast-tree":
            doc.forecast_tree_data = parse_forecast_tree_block(body, title, i18n_map[lang])

        docs.append(doc)
    return docs


# ---------------------------------------------------------------------------
# HTML Rendering Helpers
# ---------------------------------------------------------------------------

def render_template(name: str, context: dict[str, str]) -> str:
    tpl = (TEMPLATES_DIR / name).read_text(encoding="utf-8")
    for k, v in context.items():
        tpl = tpl.replace("{{" + k + "}}", v)
    return tpl


def build_top_nav_html(lang: str, current_out: str, active_section: str, i18n: dict[str, Any]) -> str:
    """Build top-right primary section navigation pills matching preview.html."""
    if lang == "zh-tw":
        items = [
            ("home", i18n["nav"]["home"], "zh-tw/index.html"),
            ("forecasts", i18n["nav"]["forecasts"], "forecasts-tw/lunar-expansion.html"),
            ("wiki", i18n["nav"]["wiki"], "wiki-tw/concepts/space-expansion-motives.html"),
            ("canon", i18n["nav"]["canon"], "canon/laws-tw.html"),
            ("graph", i18n["nav"]["knowledge_graph"], "zh-tw/graph.html"),
            ("open-questions", i18n["nav"]["open_questions"], "open-questions-tw.html"),
        ]
    else:
        items = [
            ("home", i18n["nav"]["home"], "index.html"),
            ("forecasts", i18n["nav"]["forecasts"], "forecasts/lunar-expansion.html"),
            ("wiki", i18n["nav"]["wiki"], "wiki/concepts/space-expansion-motives.html"),
            ("canon", i18n["nav"]["canon"], "canon/laws.html"),
            ("graph", i18n["nav"]["knowledge_graph"], "graph.html"),
            ("open-questions", i18n["nav"]["open_questions"], "open-questions.html"),
        ]
    links = []
    for sec_key, label, target_out in items:
        cls = "sp-btn sp-btn--active" if active_section == sec_key else "sp-btn"
        href = rel_href(current_out, target_out)
        links.append(f'<a class="{cls}" href="{html.escape(href)}">{html.escape(label)}</a>')
    return "\n".join(links)


def build_sidebar_html(docs: list[DocPage], lang: str, current_out: str, i18n: dict[str, Any]) -> str:
    lang_docs = [d for d in docs if d.lang == lang]
    sessions_docs = [d for d in docs if d.section == "sessions"]

    def link_item(d: DocPage) -> str:
        href = rel_href(current_out, d.out_rel)
        cls = "sp-nav-link sp-nav-link--active" if d.out_rel == current_out else "sp-nav-link"
        return f'<li><a class="{cls}" href="{html.escape(href)}">{html.escape(d.title)}</a></li>'

    groups: list[tuple[str, list[DocPage]]] = [
        (i18n["nav"]["canon"], [d for d in lang_docs if d.section == "canon"]),
        (i18n["nav"]["forecasts"], [d for d in lang_docs if d.section == "forecasts"]),
        (f'{i18n["nav"]["wiki"]} · {i18n["nav"]["concepts"]}', [d for d in lang_docs if d.section == "wiki" and d.subsection == "concepts"]),
        (f'{i18n["nav"]["wiki"]} · {i18n["nav"]["tech"]}', [d for d in lang_docs if d.section == "wiki" and d.subsection == "tech"]),
        (f'{i18n["nav"]["wiki"]} · {i18n["nav"]["society"]}', [d for d in lang_docs if d.section == "wiki" and d.subsection == "society"]),
        (f'{i18n["nav"]["wiki"]} · {i18n["nav"]["places"]}', [d for d in lang_docs if d.section == "wiki" and d.subsection == "places"]),
        (f'{i18n["nav"]["wiki"]} · {i18n["nav"]["eras"]}', [d for d in lang_docs if d.section == "wiki" and d.subsection == "eras"]),
        (i18n["nav"]["stories"], [d for d in lang_docs if d.section == "stories"]),
        (i18n["nav"]["open_questions"], [d for d in lang_docs if d.section == "open-questions"]),
        (i18n["nav"]["sessions"], sessions_docs),
    ]

    blocks: list[str] = []
    home_out = "zh-tw/index.html" if lang == "zh-tw" else "index.html"
    home_cls = "sp-nav-link sp-nav-link--active" if current_out == home_out else "sp-nav-link"
    blocks.append(
        f'<div class="sp-nav-group"><ul class="sp-nav-list">'
        f'<li><a class="{home_cls}" href="{html.escape(rel_href(current_out, home_out))}">{html.escape(i18n["nav"]["home"])}</a></li>'
        f"</ul></div>"
    )

    for heading, items in groups:
        if not items:
            continue
        is_active_group = any(d.out_rel == current_out for d in items)
        open_attr = " open" if is_active_group else ""
        lis = "\n".join(link_item(d) for d in items)
        blocks.append(
            f'<details class="sp-nav-group" name="sp-nav-accordion"{open_attr}>'
            f'<summary class="sp-nav-heading">'
            f'<span>{html.escape(heading)}</span>'
            f'<span class="sp-nav-meta"><span class="sp-nav-count">{len(items)}</span><span class="sp-nav-chevron" aria-hidden="true">›</span></span>'
            f"</summary>"
            f'<ul class="sp-nav-list">{lis}</ul>'
            f"</details>"
        )
    return "\n".join(blocks)


def build_meta_badges(doc: DocPage, i18n: dict[str, Any]) -> str:
    badges: list[str] = []
    meta = doc.meta
    if meta.get("kind"):
        k = str(meta["kind"])
        label = i18n["kind"].get(k, k)
        badges.append(f'<span class="sp-badge">{html.escape(i18n["meta"]["kind"])}: {html.escape(label)}</span>')
    if meta.get("status"):
        s = str(meta["status"])
        label = i18n["status"].get(s, s)
        badges.append(f'<span class="sp-badge sp-badge--{html.escape(s)}">{html.escape(i18n["meta"]["status"])}: {html.escape(label)}</span>')
    if meta.get("grounding"):
        g = str(meta["grounding"])
        label = i18n["grounding"].get(g, g)
        badges.append(f'<span class="sp-badge sp-badge--{html.escape(g)}">{html.escape(i18n["meta"]["grounding"])}: {html.escape(label)}</span>')
    if meta.get("evidence_cutoff"):
        badges.append(f'<span class="sp-badge">{html.escape(i18n["meta"]["evidence_cutoff"])}: {html.escape(str(meta["evidence_cutoff"]))}</span>')
    if meta.get("updated"):
        badges.append(f'<span class="sp-badge">{html.escape(i18n["meta"]["updated"])}: {html.escape(str(meta["updated"]))}</span>')
    if meta.get("lifecycle"):
        lc = str(meta["lifecycle"])
        label = i18n["lifecycle"].get(lc, lc)
        cls = "sp-badge--occurred" if lc == "active" else ""
        badges.append(f'<span class="sp-badge {cls}">{html.escape(i18n["meta"]["lifecycle"])}: {html.escape(label)}</span>')
    if not badges and doc.section == "canon":
        badges.append(f'<span class="sp-badge sp-badge--canon">{html.escape(i18n["status"]["canon"])}</span>')
    return "\n".join(badges)


def build_toc_html(toc: list[tuple[int, str, str]], i18n: dict[str, Any]) -> str:
    if not toc:
        return f'<p class="sp-mono">{html.escape(i18n["meta"]["none"])}</p>'
    lis = [f'<li><a href="#{html.escape(hid)}">{html.escape(label)}</a></li>' for _, hid, label in toc]
    return f'<ul class="sp-toc-list">{"".join(lis)}</ul>'


def build_relations_html(target_srcs: list[str], doc: DocPage, src_map: dict[str, DocPage], i18n: dict[str, Any]) -> str:
    unique_targets = list(dict.fromkeys(t for t in target_srcs if t in src_map and t != doc.src_rel))
    if not unique_targets:
        return f'<p class="sp-mono">{html.escape(i18n["meta"]["none"])}</p>'
    lis = []
    for t in unique_targets:
        target_doc = src_map[t]
        href = rel_href(doc.out_rel, target_doc.out_rel)
        lis.append(f'<li><a href="{html.escape(href)}">{html.escape(target_doc.title)}</a></li>')
    return f'<ul class="sp-rel-list">{"".join(lis)}</ul>'


# ---------------------------------------------------------------------------
# Main Build Pipeline
# ---------------------------------------------------------------------------

def compute_asset_version() -> str:
    """Compute a deterministic short hash of CSS & JS assets for browser cache busting."""
    h = hashlib.sha256()
    files = [WEB_DIR / "tokens.css"] + sorted((WEB_DIR / "styles").glob("*.css")) + sorted((WEB_DIR / "js").rglob("*.js"))
    for fp in files:
        if fp.is_file():
            h.update(fp.read_bytes())
    return h.hexdigest()[:8]


def build() -> None:
    asset_version = compute_asset_version()
    i18n_map = {
        "en": json.loads((I18N_DIR / "en.json").read_text(encoding="utf-8")),
        "zh-tw": json.loads((I18N_DIR / "zh-tw.json").read_text(encoding="utf-8")),
    }

    if DIST_DIR.exists():
        shutil.rmtree(DIST_DIR)
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    (DIST_DIR / ".nojekyll").write_text("", encoding="utf-8")

    # Copy static assets
    shutil.copy2(WEB_DIR / "tokens.css", DIST_DIR / "tokens.css")
    shutil.copytree(WEB_DIR / "styles", DIST_DIR / "styles")
    shutil.copytree(WEB_DIR / "js", DIST_DIR / "js")
    if (REPO_ROOT / "assets").is_dir():
        shutil.copytree(REPO_ROOT / "assets", DIST_DIR / "assets")

    docs = discover_docs(i18n_map)
    src_map = {d.src_rel: d for d in docs}
    src_to_out = {d.src_rel: d.out_rel for d in docs}

    # Resolve bilingual counterparts
    for d in docs:
        cp_src = find_counterpart_src(d.src_rel)
        if cp_src and cp_src in src_to_out:
            d.counterpart_out = src_to_out[cp_src]
        else:
            d.counterpart_out = "zh-tw/index.html" if d.lang == "en" else "index.html"

    # First pass: render Markdown body & collect body links for backlinks
    rendered_bodies: dict[str, str] = {}
    for d in docs:
        i18n = i18n_map[d.lang]
        body_html, toc, body_links, citations = render_markdown(
            d.body_md,
            d,
            src_to_out,
            i18n,
            strip_first_h1=True,
            hide_ascii_tree=(d.forecast_tree_data is not None),
        )
        if d.archetype == "wiki-entry":
            body_html = enhance_wiki_html(body_html, i18n)
        elif d.archetype == "canon-doc":
            if d.src_rel in ("canon/laws.md", "canon/laws-tw.md"):
                body_html = enhance_canon_laws_html(body_html, i18n)
            elif d.src_rel in ("canon/timeline.md", "canon/timeline-tw.md"):
                body_html = enhance_canon_timeline_html(body_html, i18n)
        rendered_bodies[d.src_rel] = body_html
        d.toc = toc
        d.body_links_rels = body_links
        d.citations = citations
        for target in set(d.depends_on_rels + body_links):
            if target in src_map and target != d.src_rel:
                src_map[target].backlinks.append(d.src_rel)

    # Second pass: emit all content HTML pages
    for d in docs:
        i18n = i18n_map[d.lang]
        prefix = asset_prefix_for(d.out_rel)
        home_out = "zh-tw/index.html" if d.lang == "zh-tw" else "index.html"
        nav_html = build_sidebar_html(docs, d.lang, d.out_rel, i18n)
        meta_badges = build_meta_badges(d, i18n)
        toc_html = build_toc_html(d.toc, i18n)
        depends_html = build_relations_html(d.depends_on_rels, d, src_map, i18n)
        backlinks_html = build_relations_html(sorted(set(d.backlinks)), d, src_map, i18n)
        extra_scripts = ""

        if d.archetype == "wiki-entry":
            kind_key = str(d.meta.get("kind") or d.subsection or "concept")
            eyebrow = f'{i18n["kind"].get(kind_key, kind_key)} · {d.src_rel}'
            shell_html = render_template("wiki-entry.html", {
                "nav_html": nav_html,
                "entry_kind_label": html.escape(eyebrow),
                "page_title": html.escape(d.title),
                "meta_badges_html": meta_badges,
                "content_html": rendered_bodies[d.src_rel],
                "citations_html": build_citations_html(d.citations, i18n),
                "toc_label": html.escape(i18n["meta"]["toc"]),
                "toc_html": toc_html,
                "depends_on_label": html.escape(i18n["meta"]["depends_on"]),
                "depends_on_html": depends_html,
                "backlinks_label": html.escape(i18n["meta"]["backlinks"]),
                "backlinks_html": backlinks_html,
            })
        elif d.archetype == "forecast-tree":
            if d.forecast_tree_data:
                json_blob = json.dumps(d.forecast_tree_data, ensure_ascii=False).replace("</", "<\\/")
                tree_fallback = f'<script type="application/json" class="sp-forecast-data">{json_blob}</script>'
                extra_scripts = f'<script type="module" src="{prefix}js/forecast-tree.js?v={asset_version}"></script>'
            else:
                tree_fallback = f'<p class="sp-mono">{html.escape(d.src_rel)}</p>'
            shell_html = render_template("forecast-tree.html", {
                "nav_html": nav_html,
                "forecast_eyebrow": html.escape(f'{i18n["nav"]["forecasts"]} · {d.src_rel}'),
                "page_title": html.escape(d.title),
                "meta_badges_html": meta_badges,
                "tree_id": html.escape(str(d.meta.get("id") or slugify(d.title))),
                "tree_overview_label": html.escape(i18n["nav"]["forecasts"]),
                "reset_selection_label": html.escape(i18n["forecast"]["reset_selection"]),
                "tree_fallback_html": tree_fallback,
                "content_html": rendered_bodies[d.src_rel] + build_citations_html(d.citations, i18n),
                "toc_label": html.escape(i18n["meta"]["toc"]),
                "toc_html": toc_html,
                "depends_on_label": html.escape(i18n["meta"]["depends_on"]),
                "depends_on_html": build_relations_html(d.depends_on_rels + d.body_links_rels, d, src_map, i18n),
            })
        elif d.archetype == "canon-doc":
            shell_html = render_template("canon-doc.html", {
                "nav_html": nav_html,
                "canon_eyebrow": html.escape(f'{i18n["nav"]["canon"]} · {d.src_rel}'),
                "page_title": html.escape(d.title),
                "meta_badges_html": meta_badges,
                "content_html": rendered_bodies[d.src_rel],
                "toc_label": html.escape(i18n["meta"]["toc"]),
                "toc_html": toc_html,
                "backlinks_label": html.escape(i18n["meta"]["backlinks"]),
                "backlinks_html": backlinks_html,
            })
        elif d.archetype == "story":
            shell_html = render_template("story.html", {
                "story_eyebrow": html.escape(f'{i18n["nav"]["stories"]} · {d.src_rel}'),
                "page_title": html.escape(d.title),
                "meta_badges_html": meta_badges,
                "content_html": rendered_bodies[d.src_rel],
                "depends_on_label": html.escape(i18n["meta"]["depends_on"]),
                "depends_on_html": depends_html,
                "toc_label": html.escape(i18n["meta"]["toc"]),
                "toc_html": toc_html,
            })
        else:
            notice = (
                f'<div class="sp-notice">{html.escape(i18n["meta"]["sessions_en_only"])}</div>'
                if d.section == "sessions"
                else ""
            )
            shell_html = render_template("index-log.html", {
                "nav_html": nav_html,
                "log_eyebrow": html.escape(f'{d.section} · {d.src_rel}'),
                "page_title": html.escape(d.title),
                "notice_html": notice,
                "filter_bar_html": "",
                "content_html": rendered_bodies[d.src_rel],
            })

        full_html = render_template("base.html", {
            "lang_code": d.lang,
            "page_title": html.escape(d.title),
            "site_name": html.escape(i18n["site"]["name"]),
            "asset_prefix": prefix,
            "asset_version": asset_version,
            "extra_head": "",
            "archetype": d.archetype,
            "menu_open_label": html.escape(i18n["nav"]["menu_open"]),
            "home_href": html.escape(rel_href(d.out_rel, home_out)),
            "rule_banner": html.escape(i18n["site"]["rule_banner"]),
            "top_nav_html": build_top_nav_html(d.lang, d.out_rel, d.section, i18n),
            "search_trigger": html.escape(i18n["search"]["trigger"]),
            "switch_lang_href": html.escape(rel_href(d.out_rel, d.counterpart_out)),
            "switch_lang_label": html.escape(i18n["site"]["switch_language"]),
            "theme_toggle_label": html.escape(i18n["site"]["theme_toggle"]),
            "body_shell": shell_html,
            "search_no_results": html.escape(i18n["search"]["no_results"]),
            "search_placeholder": html.escape(i18n["search"]["placeholder"]),
            "extra_scripts": extra_scripts,
        })

        out_path = DIST_DIR / d.out_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(full_html, encoding="utf-8")

    # Emit bilingual Home pages (dist/index.html and dist/zh-tw/index.html)
    for lang, out_rel, cp_out in (("en", "index.html", "zh-tw/index.html"), ("zh-tw", "zh-tw/index.html", "index.html")):
        i18n = i18n_map[lang]
        prefix = asset_prefix_for(out_rel)
        lang_docs = [d for d in docs if d.lang == lang]
        wiki_docs = [d for d in lang_docs if d.section == "wiki"]
        forecast_docs = [d for d in lang_docs if d.section == "forecasts"]
        canon_docs = [d for d in lang_docs if d.section == "canon"]

        forecast_href = rel_href(out_rel, "forecasts-tw/lunar-expansion.html" if lang == "zh-tw" else "forecasts/lunar-expansion.html")
        laws_href = rel_href(out_rel, "canon/laws-tw.html" if lang == "zh-tw" else "canon/laws.html")
        motives_href = rel_href(out_rel, "wiki-tw/concepts/space-expansion-motives.html" if lang == "zh-tw" else "wiki/concepts/space-expansion-motives.html")
        graph_href = rel_href(out_rel, "zh-tw/graph.html" if lang == "zh-tw" else "graph.html")

        hero_actions_html = "\n".join([
            f'<a class="sp-btn sp-btn--primary" href="{html.escape(forecast_href)}">{html.escape(i18n["nav"]["forecasts"])}</a>',
            f'<a class="sp-btn" href="{html.escape(graph_href)}">{html.escape(i18n["nav"]["knowledge_graph"])}</a>',
            f'<a class="sp-btn" href="{html.escape(motives_href)}">{html.escape(i18n["nav"]["wiki"])}</a>',
            f'<a class="sp-btn" href="{html.escape(laws_href)}">{html.escape(i18n["nav"]["laws"])}</a>',
        ])

        forecast_nodes_count = sum(
            len(fd.forecast_tree_data["nodes"])
            for fd in forecast_docs
            if fd.forecast_tree_data
        )
        stats_metrics_html = "\n".join([
            f'<div class="sp-metric"><div class="sp-metric-value">{len(wiki_docs)}</div><div class="sp-metric-label">{html.escape(i18n["nav"]["wiki"])}</div></div>',
            f'<div class="sp-metric"><div class="sp-metric-value">{forecast_nodes_count}</div><div class="sp-metric-label">{html.escape(i18n["nav"]["forecasts"])}</div></div>',
            f'<div class="sp-metric"><div class="sp-metric-value">{len(canon_docs)}</div><div class="sp-metric-label">{html.escape(i18n["nav"]["canon"])}</div></div>',
            f'<div class="sp-metric"><div class="sp-metric-value">EN / 繁中</div><div class="sp-metric-label">{html.escape(i18n["site"]["language_label"])}</div></div>',
        ])

        cards_html = "\n".join([
            f'<a class="sp-card" href="{html.escape(forecast_href)}"><div class="sp-eyebrow">01 · {html.escape(i18n["nav"]["forecasts"])}</div><div class="sp-card-title">{html.escape(i18n["nav"]["forecasts"])}</div><p>{html.escape(i18n["forecast"]["conditional_prob"])} &amp; {html.escape(i18n["forecast"]["path_prob"])}</p></a>',
            f'<a class="sp-card" href="{html.escape(laws_href)}"><div class="sp-eyebrow">02 · {html.escape(i18n["nav"]["canon"])}</div><div class="sp-card-title">{html.escape(i18n["nav"]["laws"])}</div><p>{html.escape(i18n["site"]["rule_banner"])}</p></a>',
            f'<a class="sp-card" href="{html.escape(motives_href)}"><div class="sp-eyebrow">03 · {html.escape(i18n["nav"]["wiki"])}</div><div class="sp-card-title">{html.escape(i18n["nav"]["concepts"])} &amp; {html.escape(i18n["nav"]["tech"])}</div><p>{html.escape(i18n["science"]["validation_heading"])}</p></a>',
        ])

        # Reading map table
        rows_html = []
        for wd in wiki_docs:
            k_key = str(wd.meta.get("kind") or wd.subsection)
            s_key = str(wd.meta.get("status") or "draft")
            g_key = str(wd.meta.get("grounding") or "")
            href = rel_href(out_rel, wd.out_rel)
            rows_html.append(
                f'<tr><td><a href="{html.escape(href)}">{html.escape(wd.title)}</a></td>'
                f'<td>{html.escape(i18n["kind"].get(k_key, k_key))}</td>'
                f'<td><span class="sp-badge sp-badge--{html.escape(s_key)}">{html.escape(i18n["status"].get(s_key, s_key))}</span></td>'
                f'<td><span class="sp-badge sp-badge--{html.escape(g_key)}">{html.escape(i18n["grounding"].get(g_key, g_key))}</span></td></tr>'
            )
        reading_map = (
            f'<h2>{html.escape(i18n["nav"]["wiki"])}</h2>'
            f'<table><thead><tr><th>{html.escape(i18n["nav"]["wiki"])}</th><th>{html.escape(i18n["meta"]["kind"])}</th>'
            f'<th>{html.escape(i18n["meta"]["status"])}</th><th>{html.escape(i18n["meta"]["grounding"])}</th></tr></thead>'
            f'<tbody>{"".join(rows_html)}</tbody></table>'
        )

        home_shell = render_template("home.html", {
            "home_eyebrow": html.escape(i18n["site"]["name"] + " · " + i18n["nav"]["home"]),
            "hero_headline": html.escape(i18n["site"]["hero_headline"]),
            "site_tagline": html.escape(i18n["site"]["tagline"]),
            "hero_actions_html": hero_actions_html,
            "stats_metrics_html": stats_metrics_html,
            "section_cards_html": cards_html,
            "reading_map_html": reading_map,
        })

        home_html = render_template("base.html", {
            "lang_code": lang,
            "page_title": html.escape(i18n["nav"]["home"]),
            "site_name": html.escape(i18n["site"]["name"]),
            "asset_prefix": prefix,
            "asset_version": asset_version,
            "extra_head": "",
            "archetype": "home",
            "menu_open_label": html.escape(i18n["nav"]["menu_open"]),
            "home_href": html.escape(rel_href(out_rel, out_rel)),
            "rule_banner": html.escape(i18n["site"]["rule_banner"]),
            "top_nav_html": build_top_nav_html(lang, out_rel, "home", i18n),
            "search_trigger": html.escape(i18n["search"]["trigger"]),
            "switch_lang_href": html.escape(rel_href(out_rel, cp_out)),
            "switch_lang_label": html.escape(i18n["site"]["switch_language"]),
            "theme_toggle_label": html.escape(i18n["site"]["theme_toggle"]),
            "body_shell": home_shell,
            "search_no_results": html.escape(i18n["search"]["no_results"]),
            "search_placeholder": html.escape(i18n["search"]["placeholder"]),
            "extra_scripts": "",
        })
        out_path = DIST_DIR / out_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(home_html, encoding="utf-8")

    # Emit offline search indices
    for lang, filename in (("en", "search-index-en.json"), ("zh-tw", "search-index-zh-tw.json")):
        records = [
            {
                "title": d.title,
                "url": d.out_rel,
                "section": d.section,
                "kind": d.meta.get("kind") or d.subsection,
                "status": d.meta.get("status") or "",
                "grounding": d.meta.get("grounding") or "",
                "excerpt": d.excerpt,
                "text": d.plain_text[:1500],
            }
            for d in docs
            if d.lang == lang or d.section == "sessions"
        ]
        (DIST_DIR / filename).write_text(json.dumps(records, ensure_ascii=False, indent=2), encoding="utf-8")

    # Emit dependency graph JSON (includes both depends_on and cross-reference links)
    graph_nodes = [
        {
            "id": d.src_rel,
            "title": d.title,
            "url": d.out_rel,
            "lang": d.lang,
            "section": d.section,
            "kind": d.meta.get("kind") or d.subsection or d.section,
            "status": d.meta.get("status") or ("canon" if d.section == "canon" else ""),
            "grounding": d.meta.get("grounding") or ("established" if d.section == "canon" else ""),
            "excerpt": d.excerpt,
        }
        for d in docs
    ]
    graph_edges = []
    seen_edges: set[tuple[str, str, str]] = set()
    for d in docs:
        for t in dict.fromkeys(d.depends_on_rels):
            if t in src_map and t != d.src_rel:
                key = (d.src_rel, t, "depends_on")
                if key not in seen_edges:
                    seen_edges.add(key)
                    graph_edges.append({"source": d.src_rel, "target": t, "type": "depends_on"})
        for t in dict.fromkeys(d.body_links_rels):
            if t in src_map and t != d.src_rel and (d.src_rel, t, "depends_on") not in seen_edges:
                key = (d.src_rel, t, "reference")
                if key not in seen_edges:
                    seen_edges.add(key)
                    graph_edges.append({"source": d.src_rel, "target": t, "type": "reference"})
    (DIST_DIR / "graph.json").write_text(
        json.dumps({"nodes": graph_nodes, "edges": graph_edges}, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    # Emit bilingual Knowledge Graph pages (dist/graph.html and dist/zh-tw/graph.html)
    for lang, out_rel, cp_out in (("en", "graph.html", "zh-tw/graph.html"), ("zh-tw", "zh-tw/graph.html", "graph.html")):
        i18n = i18n_map[lang]
        prefix = asset_prefix_for(out_rel)
        home_out = "zh-tw/index.html" if lang == "zh-tw" else "index.html"
        kg_config = {
            "lang": lang,
            "root": prefix,
            "labels": i18n["graph"],
            "nav_labels": i18n["nav"],
            "status_labels": i18n["status"],
            "grounding_labels": i18n["grounding"],
            "kind_labels": i18n["kind"],
        }
        kg_json = json.dumps(kg_config, ensure_ascii=False).replace("</", "<\\/")
        kg_body = (
            f'<p class="sp-lead">{html.escape(i18n["graph"]["subtitle"])}</p>'
            f'<section class="sp-viz-frame" data-component="knowledge-graph">'
            f'<script type="application/json" class="sp-kg-config">{kg_json}</script>'
            f'<div class="sp-kg-mount"></div>'
            f"</section>"
        )
        kg_shell = render_template("index-log.html", {
            "nav_html": build_sidebar_html(docs, lang, out_rel, i18n),
            "log_eyebrow": html.escape(f'{i18n["site"]["name"]} · {i18n["nav"]["knowledge_graph"]}'),
            "page_title": html.escape(i18n["graph"]["title"]),
            "notice_html": "",
            "filter_bar_html": "",
            "content_html": kg_body,
        })
        kg_html = render_template("base.html", {
            "lang_code": lang,
            "page_title": html.escape(i18n["graph"]["title"]),
            "site_name": html.escape(i18n["site"]["name"]),
            "asset_prefix": prefix,
            "asset_version": asset_version,
            "extra_head": "",
            "archetype": "index-log",
            "menu_open_label": html.escape(i18n["nav"]["menu_open"]),
            "home_href": html.escape(rel_href(out_rel, home_out)),
            "rule_banner": html.escape(i18n["site"]["rule_banner"]),
            "top_nav_html": build_top_nav_html(lang, out_rel, "graph", i18n),
            "search_trigger": html.escape(i18n["search"]["trigger"]),
            "switch_lang_href": html.escape(rel_href(out_rel, cp_out)),
            "switch_lang_label": html.escape(i18n["site"]["switch_language"]),
            "theme_toggle_label": html.escape(i18n["site"]["theme_toggle"]),
            "body_shell": kg_shell,
            "search_no_results": html.escape(i18n["search"]["no_results"]),
            "search_placeholder": html.escape(i18n["search"]["placeholder"]),
            "extra_scripts": f'<script type="module" src="{prefix}js/knowledge-graph.js?v={asset_version}"></script>',
        })
        out_path = DIST_DIR / out_rel
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(kg_html, encoding="utf-8")

    print(f"Built {len(docs) + 4} HTML pages, 2 search indices, and graph.json ({len(graph_edges)} edges) into {DIST_DIR}/")


if __name__ == "__main__":
    build()
