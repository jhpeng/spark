# Canon and worldbuilding rules

Spark is a hard-science forecasting and worldbuilding workspace exploring possible futures for humanity's spread across the universe, grounded in real physics, material conditions, and human society, with sci-fi stories set in those futures. You act as an **active co-researcher**, not a passive scribe: bring your own hypotheses, extrapolate forward beyond the user's starting premises, **validate** every claim against physics, and **record** assumptions, branches, and consequences. The repository preserves multiple possibilities rather than selecting one inevitable history.

Read this guide before discussing, extrapolating, or validating ideas, or changing worldbuilding in any directory. For discussion, autonomous draft writing, and recording, also read [the session workflow](../sessions/AGENTS.md). For content edits, read [format and language rules](../templates/AGENTS.md).

For prediction trees in `forecasts/` and `forecasts-tw/`, read [forecast rules](../forecasts/AGENTS.md); that guide owns their probability, autonomous extension, revision, and lifecycle rules.

## The one hard rule

Everything obeys known physics. [canon/laws.md](laws.md) lists the laws; read it before validating anything. An idea that breaks a law is rejected or reworked until it fits — say which law it breaks and propose a physics-respecting alternative. Unknown engineering is fine; unknown physics is not.

## Independent extrapolation

Known physics is the boundary; the user's current prompt is a starting point, not a ceiling.

- **Push causal chains forward.** Actively derive second- and third-order technological, economic, geopolitical, and social consequences from real-world conditions, user premises, and existing entries. Surface unasked alternative paths, counterintuitive risks, bottlenecks, and `speculative` long-horizon branches whenever they obey [canon/laws.md](laws.md).
- **Separate epistemic provenance.** Clearly distinguish **real-world observations** (dated evidence), **user premises** (ideas or assumptions supplied by the user), and **agent extrapolations** (your own hypotheses, mechanisms, or extended branches). Label speculative leaps and grade their `grounding` honestly.
- **Challenge without overwriting.** You may fork new `draft` branches or forecast subtrees that test, compete with, or offer alternatives to existing `canon` premises, leaving the original `canon` intact within its own scope.

## Branches and possible futures

- Explore ideas conditionally: under which assumptions could this happen, what would follow, and what would prevent it? Several motives may coexist; compare their consequences without requiring the user to choose one cause or outcome.
- Preserve mutually exclusive futures as separate branches. Stories may occupy different branches or parallel timelines. These are ways to organize alternative settings, not a claim that physical parallel universes or travel between them exist. The same known physics binds every branch.
- When recording alternatives, give each branch a stable lowercase-kebab identifier and state its assumptions, divergence, consequences, and dependencies.
- State whether each claim is shared across branches or conditional on named branches. Branches inherit only explicitly shared premises and declared dependencies. For existing entries without a scope, preserve their status and identify the applicable scope before using them to constrain a new branch; shared physical laws always apply.
- Different outcomes across branches are expected. Contradictions within a branch or with its shared premises require resolution. Creating an alternative does not replace or retcon the original branch.
- Keep viable alternatives under exploration in wiki entries; apply the [wiki lifecycle rules](../wiki/AGENTS.md) when retiring drafts. Use [open-questions.md](../open-questions.md) for missing evidence, unresolved feasibility, or decisions needed within a branch, identifying which branches they affect. An intentional fork may remain open indefinitely without blocking work on its alternatives.

## Status

- `draft` — working content open for autonomous agent authoring and revision, including agent-originated extrapolations and new branches. It may be brief, incomplete, or awaiting validation; follow the [wiki lifecycle rules](../wiki/AGENTS.md) for revision and removal.
- `canon` — core premises the user approved within a stated scope. Approval anchors a premise within its scope without making one branch the universal future or blocking competing `draft` branches. Only the user promotes to canon.
- `retconned` — previously approved content replaced within its stated scope. Keep the page, add a `## Retcon` section saying what replaced it and why, and link the successor. Ordinary draft revision or removal does not require a retcon. A different branch alone is not a replacement.

## Validating an idea

Run all three checks on both user premises and your own extrapolations, reporting results as you go:

1. **Physics** — back-of-envelope with real numbers: energy, mass, travel time, signal delay, radiation dose, heat rejection. Show the calculation in the entry's `## Validation` section and cite sources (papers, NASA/ESA, textbooks) for every constant or claim that is not common knowledge.
2. **Consistency** — check every relevant `canon` page (via `depends_on`, the timeline, and a grep for related terms), distinguishing shared premises from branch-specific claims. Flag conflicts within the applicable scope. Preserve a different premise or outcome as an explicitly separate branch when appropriate (including competing alternatives to `canon`); changing existing canon within its scope requires the user's choice to revise the idea or approve a retcon.
3. **Motive and consequences** — identify who acts, who pays, and under what economic, political, survival, or cultural conditions they would do so. Compare the outcomes of different motives and assumptions, including coexistence, failure, or no expansion where relevant. Distinguish physical feasibility from adoption and persistence; mark likelihood judgments as conditional and explain their evidence.

A check that cannot be settled yet is flagged during discussion and recorded in `open-questions.md` at session end. Record useful drafts before all checks are complete, distinguishing observations, user premises, agent extrapolations, and unresolved checks. Apply quantitative checks to relevant physical claims; an institutional description does not need an invented calculation. Explicit scenario assumptions may support conditional exploration while their feasibility remains unresolved; identify which conclusions depend on them. A known violation of physical law must still be rejected or reworked.

## Approval and timelines

- User approval is required only to promote content to `canon` or substantively replace or withdraw approved claims within their scope. Authoring and extending `draft` entries, opening new branches (including competing alternatives to `canon`), creating or updating `forecasts/`, and editorial maintenance that preserves approved meaning, scope, and status (including classification, formatting, clarification, splitting, and merging) require no prior approval. When reorganizing approved material, preserve its provenance and timeline references; keep new unapproved claims separate. Check affected dependencies before proposing a substantive canon change.
- **On approval**: set `status: canon` for the approved content and scope, add its dated events to the appropriate shared or branch section of `canon/timeline.md`, and commit. If only part of a draft is approved, separate the approved and draft content before assigning page-level status.

Approved dated events go in [timeline.md](timeline.md), grouped into explicitly shared or named-branch sections; alternative histories remain separate. Read the relevant entries before changing their timeline events. Apply the [session commit rule](../sessions/AGENTS.md) when committing approved work.
