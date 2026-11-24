# Web presentation and design consistency rules

Applies to `web/`, `assets/media/`, and any visual or interactive presentation of repository content. Read [templates/AGENTS.md](../templates/AGENTS.md) for bilingual synchronization and link rules, [canon/AGENTS.md](../canon/AGENTS.md) for status and branch meanings, [wiki/AGENTS.md](../wiki/AGENTS.md) for entry metadata, and [forecasts/AGENTS.md](../forecasts/AGENTS.md) for forecast tree structure. For phased implementation milestones, see [web/ROADMAP.md](ROADMAP.md).

## Core principles

1. **Markdown is the single source of truth.** All worldbuilding, physical validation, forecast trees, stories, session logs, and open questions live in their existing Markdown directories. `web/build.py` deterministically compiles Markdown into static files under `dist/`. Never hand-edit `dist/`, and never duplicate or fork worldbuilding prose inside HTML templates or JavaScript.
2. **Zero-dependency Python SSG stack.** Build tooling uses Python 3 (standard library first). Frontend output uses semantic HTML5, modular CSS driven by `web/tokens.css`, vanilla ES Modules, SVG/Canvas visualizations, and KaTeX for math. Do not introduce Node.js, npm, React, Tailwind, or alternative CSS/JS frameworks without explicit maintainer approval.
3. **English for code and rules.** Keep agent guides, component specs, code, identifiers, comments, and schemas in English. User-facing UI strings live exclusively in `web/i18n/en.json` and `web/i18n/zh-tw.json`.

## Design tokens and styling discipline

The visual identity is **Editorial Observatory**: a high-craft scientific publication meets precision observatory instrument. Default dark mode uses **Obsidian & Warm Starlight** (neutral carbon-ink surfaces, warm alabaster typography, solar amber focal accents, editorial serif display titles paired with clean sans-serif prose and tabular monospace telemetry); optional light mode uses **Archival Paper**. Avoid generic dark-navy/neon-cyan dashboard tropes, full-page background grid clutter, and plain-text ASCII visualizations.

- **`web/tokens.css` is authoritative.** All colors, typography, spacing, borders, radii, shadows, z-index layers, and semantic badge colors (`status`, `grounding`, `resolution`, `lifecycle`, `kind`) are defined in `web/tokens.css`.
- **No hardcoded colors.** Do not write hex (`#...`), `rgb()`, `rgba()`, `hsl()`, or named colors in `web/styles/*.css`, `web/templates/*`, or `web/js/*`. Always reference CSS custom properties (`var(--...)`). Canvas and SVG scripts must read active token values via `getComputedStyle(document.documentElement)`.
- **No ad-hoc inline styles.** Do not add inline `style="..."` attributes in templates or Markdown. Only registered visualization engines may set computed geometric properties (e.g., coordinates, dimensions, transforms).
- **Theme extensibility.** Preserve token-driven light-mode readiness; never assume dark-only raw values inside components.

## Page archetypes and component whitelist

- **Fixed page archetypes.** Every generated page must use one of the six approved archetypes defined in [web/COMPONENTS.md](COMPONENTS.md): `home`, `wiki-entry`, `forecast-tree`, `canon-doc`, `story`, or `index-log`. Do not create bespoke one-off layouts for individual Markdown entries.
- **Approved components only.** Markdown entries may embed only the declarative visual blocks (`spark-visual`) and UI components registered in [web/COMPONENTS.md](COMPONENTS.md). Never embed raw `<script>`, custom `<style>`, or arbitrary `<canvas>` tags inside Markdown content.
- **Adding a new component or animation engine.** Before using a new component or animation type:
  1. Document its purpose, props/JSON schema, and accessibility behavior in [web/COMPONENTS.md](COMPONENTS.md).
  2. Implement it under `web/js/` using only `web/tokens.css` tokens and respecting `prefers-reduced-motion`.
  3. Register its schema in `web/check.py`.

## Scientific evidence and reasoning integrity

- **Preserve rigor.** Rendering must preserve all calculations, assumptions, citations, branch scopes, and unresolved checks. Never silently omit, simplify, or hide caveats in ways that make `draft` or `speculative` material appear established or canon.
- **Mandatory metadata badges.**
  - Wiki entries must prominently display `kind`, `status` (`canon` | `draft` | `retconned`), and `grounding` (`established` | `plausible` | `speculative`).
  - Forecast trees must prominently display `evidence_cutoff`, `updated`, `lifecycle`, and per-outcome conditional probability, cumulative path probability, confidence, and `resolution`.
- **Structured validation sections.** Recognize standard `## Validation` / `## 驗證` subsections (`Physics` / `物理`, `Consistency` / `一致性`, `Motive` / `動機`) and render them with clear visual distinction while keeping the underlying Markdown unchanged.

## Static media and diagrams (`assets/media/`)

- Store static illustrations and diagrams in `assets/media/<slug>/` with lowercase-kebab filenames (e.g., `assets/media/lunar-resource-utilization/ice-extraction-flow.svg`). Prefer clean vector `.svg` for diagrams and compressed `.webp`/`.png` for editorial illustrations (aspect ratio `16:9` or `3:2`).
- Match the **Editorial Observatory** visual style: calm neutral carbon-ink (`#0b0c0f`) or transparent backgrounds, warm alabaster (`#f2efe9`) linework, solar amber (`#e2a856`) focal highlights, and understated scientific clarity — avoid neon cyberpunk glows, cluttered lens flares, or cartoon styling.
- Every embedded image must include:
  - Descriptive `alt` text and caption in the page's language (synchronized across English and Taiwan Traditional Chinese).
  - Explicit scale disclosure in the caption or `alt` text: **Schematic (not to scale)** / **示意圖（非等比例）** or **To scale** / **等比例圖**.
  - Physical consistency with [canon/laws.md](../canon/laws.md).

## Bilingual UI synchronization

- Never hardcode user-visible UI labels in templates or JS. Add every UI key to both `web/i18n/en.json` and `web/i18n/zh-tw.json` in the same change.
- Language switching must link exact bilingual counterparts (`wiki/` ↔ `wiki-tw/`, `forecasts/` ↔ `forecasts-tw/`, `stories/` ↔ `stories-tw/`, `canon/<name>.md` ↔ `canon/<name>-tw.md`, `open-questions.md` ↔ `open-questions-tw.md`) and clearly label English-only `sessions/` logs.

## Verification gate

Before committing any web, visual, or content change affecting the portal:
1. Run `python3 web/check.py` — this executes all static quality gates (frontmatter & enum validation, bilingual 1:1 file and i18n symmetry, zero hardcoded colors in `web/styles/` and `web/js/`, zero inline styles in `web/templates/`, `spark-visual` JSON schema & bilingual parity, image `alt` & path checks) AND runs `python3 web/build.py` to verify zero unresolved placeholders and zero broken internal links in `dist/`.
2. Confirm exit code `0` (`SPARK WEB CHECK PASSED`).
3. For any visual, layout, or visualization change, visually verify the rendered result (e.g., capture a screenshot via headless Chrome and inspect it directly) to confirm no text clipping, alignment skew, or broken layout before reporting done.
4. Enable the repository pre-commit hook once per local clone via `git config core.hooksPath .githooks` so [.githooks/pre-commit](../.githooks/pre-commit) runs `python3 web/check.py` automatically before every commit.
5. For local preview: `python3 -m http.server 8001 -d dist`.
6. Deployment to GitHub Pages is automated via [.github/workflows/deploy-web.yml](../.github/workflows/deploy-web.yml) on push to `main` (or manual `workflow_dispatch`), gated on `python3 web/check.py`.
