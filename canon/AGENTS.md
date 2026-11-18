# Canon and worldbuilding rules

Spark is a hard-science wiki exploring possible futures for humanity's spread across the universe, with sci-fi stories set in those futures. The user brings ideas; you discuss them, **validate** them against physics, and **record** their assumptions and consequences. The repository preserves multiple possibilities rather than selecting one inevitable history.

Read this guide before discussing or validating ideas, or changing worldbuilding in any directory. For discussion and recording, also read [the session workflow](../sessions/AGENTS.md). For content edits, read [format and language rules](../templates/AGENTS.md).

## The one hard rule

Everything obeys known physics. [canon/laws.md](laws.md) lists the laws; read it before validating anything. An idea that breaks a law is rejected or reworked until it fits — say which law it breaks and propose a physics-respecting alternative. Unknown engineering is fine; unknown physics is not.

## Branches and possible futures

- Explore ideas conditionally: under which assumptions could this happen, what would follow, and what would prevent it? Several motives may coexist; compare their consequences without requiring the user to choose one cause or outcome.
- Preserve mutually exclusive futures as separate branches. Stories may occupy different branches or parallel timelines. These are ways to organize alternative settings, not a claim that physical parallel universes or travel between them exist. The same known physics binds every branch.
- When recording alternatives, give each branch a stable lowercase-kebab identifier and state its assumptions, divergence, consequences, and dependencies.
- State whether each claim is shared across branches or conditional on named branches. Branches inherit only explicitly shared premises and declared dependencies. For existing entries without a scope, preserve their status and identify the applicable scope before using them to constrain a new branch; shared physical laws always apply.
- Different outcomes across branches are expected. Contradictions within a branch or with its shared premises require resolution. Creating an alternative does not replace or retcon the original branch.
- Keep viable alternatives in wiki entries. Use [open-questions.md](../open-questions.md) for missing evidence, unresolved feasibility, or decisions needed within a branch, identifying which branches they affect. An intentional fork may remain open indefinitely without blocking work on its alternatives.

## Status

- `draft` — recorded from a session, not yet approved.
- `canon` — the user approved it within its stated scope. An approved entry may describe multiple conditional alternatives; approval does not make one branch the universal future. Only the user promotes to canon.
- `retconned` — replaced within its stated scope. Keep the page, add a `## Retcon` section saying what replaced it and why, and link the successor. A different branch alone is not a replacement.

## Validating an idea

Run all three checks during discussion and report results as you go:

1. **Physics** — back-of-envelope with real numbers: energy, mass, travel time, signal delay, radiation dose, heat rejection. Show the calculation in the entry's `## Validation` section and cite sources (papers, NASA/ESA, textbooks) for every constant or claim that is not common knowledge.
2. **Consistency** — check every relevant `canon` page (via `depends_on`, the timeline, and a grep for related terms), distinguishing shared premises from branch-specific claims. Flag conflicts within the applicable scope. Preserve a different premise or outcome as an explicitly separate branch when appropriate; changing existing canon within its scope requires the user's choice to revise the idea or approve a retcon.
3. **Motive and consequences** — identify who acts, who pays, and under what economic, political, survival, or cultural conditions they would do so. Compare the outcomes of different motives and assumptions, including coexistence, failure, or no expansion where relevant. Distinguish physical feasibility from adoption and persistence; mark likelihood judgments as conditional and explain their evidence.

A check that cannot be settled yet is flagged during discussion and recorded in `open-questions.md` at session end. Explicit scenario assumptions may support conditional exploration while their feasibility remains unresolved; identify which conclusions depend on them.

## Approval and timelines

- **On approval**: set `status: canon` for the approved content and scope, add its dated events to the appropriate shared or branch section of `canon/timeline.md`, and commit. If only part of a draft is approved, separate the approved and draft content before assigning page-level status.

Approved dated events go in [timeline.md](timeline.md), grouped into explicitly shared or named-branch sections; alternative histories remain separate. Read the relevant entries before changing their timeline events. Apply the [session commit rule](../sessions/AGENTS.md) when committing approved work.
