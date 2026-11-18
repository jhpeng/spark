# Formats and language rules

Read this guide before creating, editing, translating, renaming, or retconning content in any directory, and before changing templates. Agent instruction files (`AGENTS.md`) are shared operational guidance, outside the content translation pairs below; maintain one authoritative rule set and use routing files where needed.

## Formats and links

- Slugs are lowercase-kebab. Link content with Obsidian-style `[[slug]]` wikilinks, using vault-relative paths to disambiguate language versions as described below.
- Use [entry.md](entry.md) for wiki entries, [story.md](story.md) for stories, and [session.md](session.md) for session logs. Their `-tw.md` counterparts supply translated templates.
- When changing a template, read the corresponding [wiki](../wiki/AGENTS.md), [story](../stories/AGENTS.md), or [session](../sessions/AGENTS.md) guide; preserve the [canon guide's](../canon/AGENTS.md) status and branch meanings.

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
- Keep branch identifiers identical across languages; translate their descriptions and preserve their scope and assumptions.
- Link to the matching language version where one exists. Use vault-relative wikilinks when filenames are shared, such as `[[wiki/concepts/orbital-transportation-network]]` and `[[wiki-tw/concepts/orbital-transportation-network|軌道運輸網路]]`. Update affected links when renaming either version.
- Keep `sessions/` English-only. `templates/session-tw.md` is a translated reference template; actual session logs use English headings and content. Both languages link to the same English session log.
- Before completing the change, verify that every affected pair exists at matching paths, conveys the same information, and has working links.
