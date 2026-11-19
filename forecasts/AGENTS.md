# Forecast tree rules

Use `forecasts/` for evidence-based predictions and `forecasts-tw/` for their translations. Read [canon rules](../canon/AGENTS.md) for physical validation, [session rules](../sessions/AGENTS.md) for recording, and [format rules](../templates/AGENTS.md) for language and links.

1. **Dated baseline.** Start at `index.md`, the root: record the evidence cutoff, observed conditions, sources, and unknowns. The preceding five to ten years may inform the baseline. Give future nodes explicit years or periods, from five or ten years ahead to fifty, one hundred, or one thousand; intervals need not be uniform.
2. **One node per file.** Use a stable lowercase-kebab ID, one parent except at the root, and reciprocal links to all children. Keep the tree connected and acyclic. Each child inherits its entire ancestral scenario and adds its own conditions and consequences; dependencies outside that path must be explicit. Similar outcomes under different histories remain separate nodes.
3. **One question per fork.** State the question, deadline, observable outcome criteria, and enabling or blocking conditions. Sibling outcomes must be mutually exclusive and collectively exhaustive; include an explicit residual outcome when needed. Events that can coexist require successive forks or joint outcomes. Expand leaves when useful, rather than filling every possible future.
4. **Conditional probabilities.** Every non-root node gives the probability of its outcome given its full ancestral scenario and current evidence. Active siblings sum to 100% for the same question, deadline, and evidence cutoff. A path's probability is the product of its conditional probabilities; this does not assume independence. Recalculate affected siblings and descendants together.
5. **Evidence and confidence.** Separate observations, assumptions, and deductions. Cite dated sources and explain each estimate, including subjective judgments when data are scarce. Record confidence separately from probability; use coarse estimates and broader outcomes for distant horizons. Scenario assumptions from wiki or canon are not observations of the real world.
6. **Autonomous revision.** At each relevant session, update existing forecasts from discussion and new evidence without human approval; nodes may be added, revised, split, or retired. Retain the prior dated baseline, estimates, criteria, and reasons for material changes in the session log or linked repository history. Repair links and translations. Keep retired nodes reachable through revision links, outside the active tree; represent any still-possible outcomes in the active alternatives.
7. **Resolution and convergence.** Use `resolution: pending | occurred | not-occurred | unresolved`; use `lifecycle: active | retired` separately. Resolve outcomes only against their stated criteria and deadlines; missing evidence remains unresolved. Advance the baseline and recondition surviving forecasts as events become known, preserving the old forecast and its evaluation. New evidence may widen uncertainty or introduce branches; convergence is not mandatory.
8. **Scope and authority.** Forecasts follow known physics and declare the scope of borrowed worldbuilding premises. These forecast lifecycle rules govern forecast files instead of the canon approval statuses. Forecast revisions neither promote content to canon nor change approved claims or the canon timeline; those changes follow the canon guide.

## Minimum node record

- ID, parent, children; forecast period and evidence cutoff; last updated date.
- Scenario, added conditions, consequences, and explicit dependencies.
- Conditional probability, confidence, and estimation rationale (root: probability not applicable).
- Observable criteria and deadline; resolution and lifecycle.
- Dated sources, assumptions, and links to sessions or prior revisions.

The root carries the baseline rather than a forecast outcome. Before completing an update, check tree links, inherited assumptions, sibling probability totals, affected descendants, revision provenance, and bilingual synchronization.
