# Spark — rule index

Read the applicable guides before starting the task; directory placement alone does not load rules for discussion or work in another directory. Each guide owns its rules; follow its pointers when the task crosses domains.

| When | Read | Rules owned there |
|---|---|---|
| Discussing, validating, or changing worldbuilding; approving or retconning content | [canon/AGENTS.md](canon/AGENTS.md) | Project purpose, physics, branches, validation, status, approval, timelines |
| Discussing ideas or recording a session | [sessions/AGENTS.md](sessions/AGENTS.md) | When to write, session logs, open questions, commits |
| Constructing or updating forecasts; recording a session that affects existing forecasts | [forecasts/AGENTS.md](forecasts/AGENTS.md) | Prediction trees, conditional probabilities, evidence, autonomous revision |
| Discussing wiki classification; creating, revising, reorganizing, or removing entries in `wiki/` or `wiki-tw/` | [wiki/AGENTS.md](wiki/AGENTS.md) | Classification, draft lifecycle, entry layout, branch presentation, grounding |
| Writing or changing stories in `stories/` or `stories-tw/` | [stories/AGENTS.md](stories/AGENTS.md) | Story scope and links to worldbuilding |
| Creating, editing, translating, moving, removing, or retconning content; changing templates | [templates/AGENTS.md](templates/AGENTS.md) | Formats, links, bilingual synchronization |
| Building, styling, or modifying web presentation, visual components, animations, or media in `web/` or `assets/media/` | [web/AGENTS.md](web/AGENTS.md) | Single source of truth, design tokens, page archetypes, component whitelist, visual checks |

**Before committing:** Whenever you change repository content (`canon/`, `forecasts/`, `forecasts-tw/`, `wiki/`, `wiki-tw/`, `stories/`, `stories-tw/`, `sessions/`, `open-questions*.md`), `web/`, or `assets/media/`, run `python3 web/check.py` and confirm exit code `0`. Enable the local Git hook once per clone with `git config core.hooksPath .githooks` so `.githooks/pre-commit` runs this check automatically on every commit.

These guides are agent instructions, not wiki entries, stories, or canon claims. They share one authoritative rule set across languages; `wiki-tw/AGENTS.md`, `stories-tw/AGENTS.md`, and `forecasts-tw/AGENTS.md` route to the corresponding guides.
