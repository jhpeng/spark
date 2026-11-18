# Spark — agent guide

Spark is a hard-science wiki that predicts how humanity spreads civilization across the universe, with sci-fi stories set inside it. The user brings ideas; you discuss them, **validate** them against physics, and **record** them.

## The one hard rule

Everything obeys known physics. [canon/laws.md](canon/laws.md) lists the laws; read it before validating anything. An idea that breaks a law is rejected or reworked until it fits — say which law it breaks and propose a physics-respecting alternative. Unknown engineering is fine; unknown physics is not.

## Page types

| Kind | Lives in | Template |
|---|---|---|
| Wiki entry (era, tech, society, place) | `wiki/<kind>/<slug>.md` | [templates/entry.md](templates/entry.md) |
| Wiki entry (concept) | `wiki/concepts/<slug>.md` | [templates/entry.md](templates/entry.md) |
| Session log | `sessions/YYYY-MM-DD-<topic>.md` | [templates/session.md](templates/session.md) |
| Story | `stories/<slug>.md` | [templates/story.md](templates/story.md) |

Concept entries use `kind: concept` in metadata and the `concepts/` directory in both `wiki/` and `wiki-tw/`.

Slugs are lowercase-kebab. Link pages with `[[slug]]` (Obsidian-style wikilinks). Unresolved forks go in [open-questions.md](open-questions.md); dated events go in [canon/timeline.md](canon/timeline.md).

### Status

- `draft` — recorded from a session, not yet approved.
- `canon` — the user approved it. Only the user promotes to canon.
- `retconned` — replaced. Keep the page, add a `## Retcon` section saying what replaced it and why, and link the successor.

### Grounding

How far an entry rests on today's knowledge. Every physics-allowed idea fits one level:

- `established` — demonstrated science or engineering today.
- `plausible` — physics allows it and a credible engineering path exists.
- `speculative` — physics allows it, but the path is unknown (e.g. mind uploading).

Grade the weakest load-bearing claim: an entry is only as grounded as its shakiest dependency.

## English and Taiwan Traditional Chinese

Keep these file pairs synchronized in both directions. When creating, editing, renaming, or retconning either version, update its counterpart in the same change. Create a missing counterpart as part of that work.

| English | Taiwan Traditional Chinese |
|---|---|
| `wiki/<path>.md` | `wiki-tw/<path>.md` |
| `stories/<path>.md` | `stories-tw/<path>.md` |
| `canon/<name>.md` | `canon/<name>-tw.md` |
| `templates/<name>.md` | `templates/<name>-tw.md` |
| `open-questions.md` | `open-questions-tw.md` |

- Use Taiwan Traditional Chinese (繁體中文／台灣用語). Mirror wiki and story subfolders and filenames exactly; translate titles and prose.
- Keep meaning, calculations, citations, and metadata consistent. Retain English metadata keys and controlled values such as `kind`, `status`, and `grounding`; translate human-readable values such as titles. Approval or retcon status applies to both versions of an entry; translation alone does not promote a draft to canon.
- Link to the matching language version where one exists. Use vault-relative wikilinks when filenames are shared, such as `[[wiki/concepts/orbital-transportation-network]]` and `[[wiki-tw/concepts/orbital-transportation-network|軌道運輸網路]]`. Update affected links when renaming either version.
- Keep `sessions/` English-only. `templates/session-tw.md` is a translated reference template; actual session logs use English headings and content. Both languages link to the same English session log.
- Before completing the change, verify that every affected pair exists at matching paths, conveys the same information, and has working links.

## Validating an idea

Run all three checks during discussion and report results as you go:

1. **Physics** — back-of-envelope with real numbers: energy, mass, travel time, signal delay, radiation dose, heat rejection. Show the calculation in the entry's `## Validation` section and cite sources (papers, NASA/ESA, textbooks) for every constant or claim that is not common knowledge.
2. **Consistency** — check every `canon` page the idea touches (via `depends_on`, the timeline, and a grep for related terms). A conflict means either the idea changes or a canon page is proposed for retcon; the user picks.
3. **Motive** — why humans would actually do this: economics, politics, survival, culture. "Physically possible" alone does not make a prediction.

A check that cannot be settled yet becomes an entry in `open-questions.md`, not a silent assumption.

## Recording

- **During discussion**: talk; write nothing yet. Flag conflicts with canon the moment you see them.
- **End of session** (the user signals they are done, or the topic closes): write the session log, create or update every wiki entry the session produced as `draft`, add new forks to `open-questions.md`. Then list for the user every draft created or changed, so they can approve or reject each one.
- **On approval**: set `status: canon`, add the entry's dated events to `canon/timeline.md`, and commit.

Commit once per session, message `session: <topic>`. A story that invents a new technology, place, or institution spawns a draft wiki entry for it.
