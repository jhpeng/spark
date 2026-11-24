# Spark Web Components & Page Archetypes Registry

This file is the authoritative whitelist of page layouts, UI components, data-driven visualizations, and declarative animation blocks (`spark-visual`) for the Spark web portal. Read [web/AGENTS.md](AGENTS.md) before modifying this registry.

Any component, archetype, or animation engine not listed here is **unapproved** and must not be emitted by `web/build.py` or embedded in Markdown.

---

## 1. Approved Page Archetypes

Every generated HTML page in `dist/` must use one of these six templates under `web/templates/`.

| Archetype ID | Source Paths | Purpose & Required Regions |
|---|---|---|
| `home` | Generated root (`/`, `/zh-tw/`) | Project overview, entry reading map, quick links to Canon, active Forecast Trees, Wiki categories, Knowledge Graph launcher, and repository stats (`canon` vs `draft` counts). |
| `wiki-entry` | `wiki/<kind>/*.md`, `wiki-tw/<kind>/*.md` | Three-column long-form reader: Left nav tree, Center header metadata card (`kind`, `status`, `grounding`, `era`) + structured prose + Validation evidence cards + Open Questions links, Right sticky TOC + `depends_on` + Backlinks. |
| `forecast-tree` | `forecasts/*.md`, `forecasts-tw/*.md` | Forecast overview metadata (`id`, `period`, `evidence_cutoff`, `updated`, `lifecycle`), interactive probability tree canvas, milestone criteria table, and structured fork cards with conditional/cumulative probabilities and revision history. |
| `canon-doc` | `canon/laws*.md`, `canon/timeline*.md` | Authoritative reference layout: numbered physical-law cards (for `laws`) or filterable shared/branch timeline view (for `timeline`), plus cross-references to dependent entries. |
| `story` | `stories/*.md`, `stories-tw/*.md` | Distraction-minimized narrative reading column paired with a collapsible "Worldbuilding Basis" panel listing `uses` dependencies, branch scope, and canon/draft status of referenced entries. |
| `index-log` | `open-questions*.md`, `sessions/*.md`, Knowledge Graph page | Filterable registry or archival log view: filter controls (by branch, category, or date) + structured table/list view. English-only `sessions/` pages display an explicit language notice when viewed from the `zh-tw` UI. |

---

## 2. Core UI Components

All components must consume CSS custom properties exclusively from `web/tokens.css` and user-visible labels exclusively from `web/i18n/{en,zh-tw}.json`.

| Component | Class Prefix | Contract |
|---|---|---|
| Global Header | `.sp-header` | Brand link, search trigger (`/` or `Ctrl/Cmd+K`), exact 1:1 language switcher (`EN` / `繁中`), theme toggle (when enabled), mobile nav drawer button. |
| Navigation Tree | `.sp-nav` | Collapsible groups matching repository taxonomy (`Canon`, `Forecasts`, `Wiki` → `Concepts / Tech / Society / Places / Eras`, `Stories`, `Open Questions`, `Sessions`). Supports filtering by `status` and `grounding`. |
| Metadata Strip | `.sp-meta` | Displays frontmatter key-value pairs as semantic badges (`status`, `grounding`, `kind`, `lifecycle`, `evidence_cutoff`, `updated`). |
| Validation Evidence Card | `.sp-validation` | Automatically wraps `## Validation` / `## 驗證` subsections (`Physics` / `物理`, `Consistency` / `一致性`, `Motive` / `動機`) with distinct accent borders (`--val-*-accent`), monospace calculation highlights, and an aggregated citation list. |
| Dependency & Backlink Panel | `.sp-relations` | Renders outbound `depends_on` / `uses` links and build-computed inbound backlinks with each target's `status` and `grounding` indicator. |
| Open Questions Callout | `.sp-open-q` | Highlights unresolved checks at the end of an entry and links directly to `open-questions.md` / `open-questions-tw.md`. |
| Citation List | `.sp-citations` | Deduplicated list of external scientific/institutional sources cited in the page. |
| Search Modal | `.sp-search` | Client-side instant search over `search-index-{en,zh-tw}.json` with keyboard navigation (`ArrowUp`/`ArrowDown`/`Enter`/`Esc`). |

---

## 3. Data-Driven Visualizations (Auto-Generated)

These engines consume build-time JSON emitted by `web/build.py`. Authors do not hand-code them in Markdown.

| Engine | Script | Input Data | Behavior |
|---|---|---|---|
| Interactive Forecast Mind-Map | `web/js/forecast-tree.js` | Embedded per-tree JSON parsed from `forecasts/*.md` | Renders an interactive horizontal mind-map (never a raw ASCII text dump) with smooth curved Bézier connectors weighted by cumulative path probability; clicking any node illuminates its full ancestral path from baseline and updates an attached fork inspector showing conditional & cumulative probabilities, milestone criteria, rationale, and revision signals. |
| Knowledge Dependency Graph | `web/js/knowledge-graph.js` | `dist/graph.json` | Interactive graph of all entries and `depends_on` / `uses` edges, filterable by `kind`, `status`, and `grounding`, with node preview and click-to-navigate. |
| Structured Timeline | `web/js/timeline.js` | Parsed `canon/timeline*.md` | Filterable view separating shared premises from named-branch timelines. |

---

## 4. Declarative Visual & Animation Blocks (`spark-visual`)

Authors and agents may embed approved physics/engineering animations in Markdown using a fenced code block with language tag `spark-visual` containing valid JSON.

### 4.1 Common Envelope Schema (Required for All Types)

```json
{
  "type": "orbital-transfer | energy-budget | phase-progression",
  "id": "lowercase-kebab-unique-within-page",
  "title": "Human-readable title in the page's language",
  "scale_mode": "schematic | to-scale",
  "caption": "Short explanation including explicit scale/assumption note",
  "params": {}
}
```

Validation rules enforced by `web/check.py`:
- `type` must be one of the approved engine IDs in Section 4.2.
- `id` must be lowercase-kebab and unique within the page (matching across EN and ZH-TW counterparts).
- `scale_mode` is mandatory (`"schematic"` or `"to-scale"`); the renderer automatically displays a visible scale badge from `web/i18n/`.
- `title` and `caption` must be non-empty strings localized to the file's language.
- All animation engines must provide Play / Pause / Reset controls and honor `@media (prefers-reduced-motion: reduce)` by rendering a clear static keyframe state by default.

### 4.2 Approved Animation Engines

#### `orbital-transfer`
- **Script**: `web/js/animations/orbital-transfer.js`
- **Use case**: Illustrating orbital acceleration, momentum recoil, flyby/rendezvous geometry, and lunar-Earth cargo trajectories.
- **Required `params`**:
  - `origin_label` (string), `target_label` (string)
  - `delta_v_km_s` (number > 0)
  - `payload_mass_t` (number > 0)
  - `show_recoil` (boolean) — highlights equal-and-opposite impulse on the accelerator/station.

#### `energy-budget`
- **Script**: `web/js/animations/energy-budget.js`
- **Use case**: Interactive physics calculator & animated flow showing kinetic energy ($E = \frac{1}{2}mv^2$), conversion efficiency, average power ($P_{\text{avg}} = E/t$), and storage buffering.
- **Required `params`**:
  - `mass_t` (number > 0), `mass_range_t` (`[min, max]`)
  - `delta_v_km_s` (number > 0), `delta_v_range_km_s` (`[min, max]`)
  - `efficiency` (number in `(0, 1]`)
  - `cadence_per_day` (number > 0)

#### `phase-progression`
- **Script**: `web/js/animations/phase-progression.js`
- **Use case**: Step-by-step progression of infrastructure milestones (e.g., lunar `S → L → H → I` or modular base expansion).
- **Required `params`**:
  - `stages` (array of 2–6 objects, each with `code`, `label`, `summary`, and optional `metric`).

---

## 5. Procedure for Adding New Components or Engines

1. Propose and document the new archetype, UI component, or `spark-visual` engine in this file (`web/COMPONENTS.md`) with its exact schema and accessibility behavior.
2. Implement styles using only `web/tokens.css` variables; never hardcode colors or inline styles.
3. Add all new UI labels to both `web/i18n/en.json` and `web/i18n/zh-tw.json`.
4. Add schema validation rules to `web/check.py`.
5. Verify with `python3 web/build.py` and `python3 web/check.py`.
