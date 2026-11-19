# Wiki rules

Applies to entries in both `wiki/` and `wiki-tw/`, including classification and cleanup. Before creating, changing, or removing an entry, read [worldbuilding and validation rules](../canon/AGENTS.md), [the recording workflow](../sessions/AGENTS.md), and [format and language rules](../templates/AGENTS.md).

## Living wiki

The wiki is an evolving worldbuilding workspace. Create a draft as soon as an idea, assumption, question, or inference is useful to track, discuss, or cite independently. Short entries are welcome; complete engineering, institutions, economics, and validation are not prerequisites for recording.

Within authorized writing work, revise drafts as understanding changes. Split independently useful subjects, merge overlapping entries, reclassify when the main subject changes, and remove redundant, superseded, abandoned, or no-longer-useful drafts. Preserve alternatives still being explored; uncertainty alone is not a reason to discard them. Session logs preserve the discussion history; wiki entries present the current version and need not retain obsolete wording. Apply the canon guide when approved claims are affected and the format guide when paths or links change.

## Classification

Choose `kind` by the entry's main subject, independently of status, grounding, completeness, and branch. First state that subject in the summary, then use this table:

| Kind | Main question and scope | Directory |
|---|---|---|
| `era` | What changes during this historical period? Stages, sequences, defining conditions, and transitions. Identify a time span or boundary conditions; exact dates are optional. | `wiki/era/` |
| `tech` | How is a capability implemented, and what limits its operation? Devices, processes, engineering architectures, and infrastructure systems, including unbuilt proposals. | `wiki/tech/` |
| `society` | How do people organize, live together, decide, and distribute resources or power? Communities, organizations, governance, contracts, ownership, economic institutions, culture, and ways of life. A named polity or settled institutional design is optional. | `wiki/society/` |
| `place` | What is this particular location like? Celestial bodies, regions, sites, bases, and settlements, including their environment and layout. Identify a particular location; a proper name is optional. | `wiki/place/` |
| `concept` | Why does a phenomenon occur, or under what conditions does a development path hold? Causal mechanisms, motives, comparisons, tradeoffs, and analytical frameworks spanning subjects. | `wiki/concepts/` |

- Use one primary kind per entry. Supporting discussion of costs, politics, or engineering does not by itself change the kind.
- For `concept`, name the causal relationship or comparison being examined. Uncertainty, interdisciplinarity, and unfinished design are not classification criteria; concepts are durable subjects, not a staging area for other kinds.
- Classify a proposed orbital data-center architecture as `tech`, its ownership and access arrangements as `society`, and the mechanism by which computing demand drives space industry as `concept`.
- Classify a particular lunar base as `place`, a reusable base architecture as `tech`, its residents' institutions as `society`, and a comparison of base-development paths as `concept`.
- Split when a second subject is useful to discuss or reference independently, even if both resulting drafts are short. Otherwise retain supporting material in the primary entry. Link related entries rather than duplicating their definitions.

## Entries

- Use [the entry template](../templates/entry.md) and its [Taiwan Traditional Chinese counterpart](../templates/entry-tw.md).
- Use the directory for the chosen kind and a lowercase-kebab filename. Mirror paths under `wiki-tw/`.
- Keep metadata and a useful summary in short drafts. Treat template body sections as prompts: include what is useful now, mark relevant unknowns explicitly, and omit unused sections rather than inventing material to fill them. Record applicable unresolved checks even when validation is incomplete.
- Present alternatives in labeled branch sections; split them into linked entries when they need separate treatment. Follow the branch identifiers, assumptions, scope, consequences, and dependencies defined by the canon guide.
- Record available validation calculations and sources in `## Validation`; record consequences and unresolved checks in their template sections. Track unresolved checks through the session workflow.

## Grounding

How far an entry rests on today's knowledge. Every physics-allowed idea fits one level:

- `established` — demonstrated science or engineering today.
- `plausible` — physics allows it and a credible engineering path exists.
- `speculative` — physics allows it, but the path is unknown (e.g. mind uploading).

Grade the weakest load-bearing claim: an entry is only as grounded as its shakiest dependency. For entries comparing branches, state each branch's grounding separately in the prose and use the weakest included branch for the entry metadata. Grounding measures scientific and engineering support, not how likely people are to choose that future.
