---
title: "Forecasts: dated baseline and active trees"
id: "index"
period: "2026-11-19/3026-12-31"
evidence_cutoff: "2026-11-19"
updated: "2026-11-24"
lifecycle: "active"
---

# Forecasts: dated baseline and active trees

This directory holds evidence-based prediction trees built from the repository's worldbuilding scenarios. Each thematic tree lives in its own file under `forecasts/` (with a synchronized counterpart in `forecasts-tw/`). Rules live in [forecasts/AGENTS.md](./AGENTS.md).

## Active forecast trees

| Tree | Horizon | Evidence cutoff | Lifecycle | Scope |
|---|---|---|---|---|
| [Lunar-led expansion](./lunar-expansion.md) | 2026–3026 | 2026-11-19 | `active` | Shared lunar services (`S`), local consumables (`L`), household residence (`H`), and demonstrated independence (`I`). Does not exhaust Mars, orbital industry, or other routes. |

## Dated baseline and evidence

Recorded and selectively checked on **2026-11-19**; this is the evidence cutoff, not a claim to have surveyed every event through that date. [canon/timeline](../canon/timeline.md) supplies the repository's 2026 starting setting; [canon/laws](../canon/laws.md) binds every path. Future wiki scenarios remain assumptions, not observations of the real world.

| Dated evidence | Supported conclusion and limit |
|---|---|
| CNSA reported Chang'e 6's lunar far-side sample return on 2024-06-25. [Mission report](https://www.cnsa.gov.cn/n6758823/n6758844/n10518102/n10518147/c10565180/content.html) | Lunar return operations have been demonstrated; this does not establish routine industrial freight. |
| A 2025-04-25 interview with China's lunar-program chief designer, published by CNSA, described a basic research station before 2035 and expansion before 2045, with long autonomous operation and short human visits. [Station plan](https://www.cnsa.gov.cn/n6758823/n6758844/n10663475/n10663416/c10666366/content.html) | A stated program direction supports considering repeated operations; its dates and residence model are goals, not achieved capability. |
| NASA's 2026-11-07 release reported awards for miniCAST power-related components, with integration and testing still ahead. [NASA awards](https://www.nasa.gov/news-release/nasa-awards-moon-base-transportation-technology-science-projects/) | Procurement is more concrete than ambition, but component awards do not demonstrate a working shared service. |
| NASA's phases page, checked 2026-11-19, describes infrastructure deployment in 2029–2032 and outpost assembly from 2032. [NASA phases](https://www.nasa.gov/moonbase-phases/) | A published sequence helps define milestones; it does not warrant treating the schedule as certain. |

## Shared conventions

- **Conditional and path probabilities**: Each outcome gives its **conditional probability** given its full ancestral path and current evidence, and its **cumulative path probability** (the product of conditional probabilities along the path; this does not assume independence). Sibling outcomes for the same question and deadline are mutually exclusive and collectively exhaustive, summing to 100%.
- **Subjective estimates and confidence**: Initial numbers are uncalibrated subjective estimates, not measured frequencies or calibrated model outputs. **Confidence** (`high`, `medium`, `low`, `very-low`) is recorded separately from probability: low confidence means an estimate is easy to revise, not that the outcome is unlikely.
- **Unexpanded leaves**: An unexpanded leaf means **not yet modeled**, not zero probability of later development.
- **Resolution and lifecycle**: `resolution` (`pending | occurred | not-occurred | unresolved`) and `lifecycle` (`active | retired`) are tracked separately. Resolve an outcome only against its stated criteria and deadline; missing reports or inaccessible records leave the sibling pair `unresolved`, rather than proving failure. Changing a threshold creates a dated new version rather than retroactively changing the scoring target of an old forecast.
- **Scope and authority**: Forecast revisions neither promote content to canon nor alter approved claims in `canon/`.

## Revision history

- `2026-11-24`: Reorganized `forecasts/` from one-node-per-file into one-tree-per-topic-file; moved the lunar-led tree into [lunar-expansion.md](./lunar-expansion.md) without changing probabilities, criteria, or evidence cutoff.
- `2026-11-19`: Initial baseline and lunar-led forecast tree created ([sessions/2026-11-19-initial-forecast-tree](../sessions/2026-11-19-initial-forecast-tree.md)).
