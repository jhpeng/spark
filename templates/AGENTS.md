# Formats and language rules

Read this guide before creating, editing, translating, moving, removing, or retconning content in any directory, and before changing templates. Agent instruction files (`AGENTS.md`) are shared operational guidance, outside the content translation pairs below; maintain one authoritative rule set in English and use routing files where needed. Rule comments embedded in translated templates also remain in English.

## Formats and links

- Slugs are lowercase-kebab. Link content with Obsidian-style `[[slug]]` wikilinks, using vault-relative paths to disambiguate language versions as described below.
- Use [entry.md](entry.md) for wiki entries, [story.md](story.md) for stories, and [session.md](session.md) for session logs. Their `-tw.md` counterparts supply translated templates.
- For forecast node records, use the minimum record in the [forecast guide](../forecasts/AGENTS.md).
- For wiki classification, short drafts, and entry lifecycle, follow the [wiki guide](../wiki/AGENTS.md); template sections are used according to that guide.
- When changing a template, read the corresponding [wiki](../wiki/AGENTS.md), [story](../stories/AGENTS.md), or [session](../sessions/AGENTS.md) guide; preserve the [canon guide's](../canon/AGENTS.md) status and branch meanings.

## English and Taiwan Traditional Chinese

Keep these file pairs synchronized in both directions. When creating, editing, moving, splitting, merging, removing, or retconning either version, apply the same operation to its counterpart in the same change. Create a missing counterpart for retained content as part of that work.

| English | Taiwan Traditional Chinese |
|---|---|
| `wiki/<path>.md` | `wiki-tw/<path>.md` |
| `stories/<path>.md` | `stories-tw/<path>.md` |
| `forecasts/<path>.md` | `forecasts-tw/<path>.md` |
| `canon/<name>.md` | `canon/<name>-tw.md` |
| `templates/<name>.md` | `templates/<name>-tw.md` |
| `open-questions.md` | `open-questions-tw.md` |

- Use Taiwan Traditional Chinese and Taiwan usage. Mirror wiki, story, and forecast subfolders and filenames exactly; translate titles and prose.
- Keep meaning, calculations, citations, and metadata consistent. Retain English metadata keys and controlled values such as `kind`, `status`, and `grounding`; translate human-readable values such as titles. Approval or retcon status applies to both versions of an entry; translation alone does not promote a draft to canon.
- Keep branch identifiers identical across languages; translate their descriptions and preserve their scope and assumptions.
- Link to the matching language version where one exists. Use vault-relative wikilinks when filenames are shared, such as `[[wiki/concepts/orbital-transportation-network]]` and `[[wiki-tw/concepts/orbital-transportation-network]]`.
- After moving, splitting, merging, or removing content, repair inbound links and `depends_on` references in both languages, update affected open questions and timeline references, and verify that retained claims still have the premises they need. Preserve historical session statements; redirect their links to an appropriate successor or replace obsolete links with plain text when none exists. Do not silently drop a dependency that an argument still requires.
- Keep `sessions/` English-only. `templates/session-tw.md` is a translated reference template; actual session logs use English headings and content. Both languages link to the same English session log.
- Before completing the change, verify that every retained affected pair exists at matching paths, conveys the same information, and has working links; removed pairs must leave no dangling references.
