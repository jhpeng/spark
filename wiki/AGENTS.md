# Wiki rules

Applies to entries in both `wiki/` and `wiki-tw/`. Before creating or changing an entry, read [worldbuilding and validation rules](../canon/AGENTS.md), [the recording workflow](../sessions/AGENTS.md), and [format and language rules](../templates/AGENTS.md).

## Entries

- Use [the entry template](../templates/entry.md) and its [Taiwan Traditional Chinese counterpart](../templates/entry-tw.md).
- Eras, technologies, societies, and places live at `wiki/<kind>/<slug>.md`; concepts live at `wiki/concepts/<slug>.md` and use `kind: concept`. Mirror paths under `wiki-tw/`.
- Present alternatives in labeled branch sections; split them into linked entries when they need separate treatment. Follow the branch identifiers, assumptions, scope, consequences, and dependencies defined by the canon guide.
- Record validation calculations and sources in `## Validation`; record consequences and unresolved checks in their template sections. Keep viable alternatives in entries and track unresolved checks through the session workflow.

## Grounding

How far an entry rests on today's knowledge. Every physics-allowed idea fits one level:

- `established` — demonstrated science or engineering today.
- `plausible` — physics allows it and a credible engineering path exists.
- `speculative` — physics allows it, but the path is unknown (e.g. mind uploading).

Grade the weakest load-bearing claim: an entry is only as grounded as its shakiest dependency. For entries comparing branches, state each branch's grounding separately in the prose and use the weakest included branch for the entry metadata. Grounding measures scientific and engineering support, not how likely people are to choose that future.
