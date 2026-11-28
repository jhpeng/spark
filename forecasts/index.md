---
title: "Forecasts: dated baseline and active trees"
id: "index"
period: "2026-11-19/2151-12-31"
evidence_cutoff: "2026-11-24"
updated: "2026-11-24"
lifecycle: "active"
---

# Forecasts: dated baseline and active trees

This directory holds evidence-based prediction trees built from the repository's worldbuilding scenarios. Each thematic tree lives in its own file under `forecasts/` (with a synchronized counterpart in `forecasts-tw/`). Rules live in [forecasts/AGENTS.md](./AGENTS.md).

## Active forecast trees

| Tree | Horizon (5 steps) | Evidence cutoff | Lifecycle | Scope |
|---|---|---|---|---|
| [Lunar South Pole outpost buildup (5-year)](./lunar-outpost-near-term.md) | 2027–2031 (every 1 yr) | 2026-11-24 | `active` | Near-term annual milestones anchored to 2026 NASA, CNSA, and commercial plans: uncrewed landings/relays, crewed return or recon launch, polar volatile survey & night survival, initial kW-class utilities, and 2032–2036 shared-service contracts. |
| [Lunar industrialization & factory scaling (25-year)](./lunar-industrial-mid-term.md) | 2031–2051 (every 5 yr) | 2026-11-24 | `active` | Medium-term 5-year milestones bridging outpost utilities (2031) to shared services + external demand (2036), Factory #0 & pilot ISRU (2041), MW-class nuclear/hybrid park (2046), and scaled cislunar industry / Mare annex (2051). |
| [Lunar-led expansion (125-year)](./lunar-expansion.md) | 2051–2151 (every 25 yr) | 2026-11-24 | `active` | Long-term quarter-century milestones: sustained shared services (2051), routine local water/O2 (2076), multi-site lunar industrial network (2101), sustained lunar households (2126), and resilient multi-year-autonomous lunar society (2151). |

## Dated baseline and evidence

Recorded and selectively checked on **2026-11-19**; this is the evidence cutoff, not a claim to have surveyed every event through that date. [canon/timeline](../canon/timeline.md) supplies the repository's 2026 starting setting; [canon/laws](../canon/laws.md) binds every path. Future wiki scenarios remain assumptions, not observations of the real world.

| Dated evidence | Supported conclusion and limit |
|---|---|
| CNSA reported Chang'e 6's lunar far-side sample return on 2024-06-25. [Mission report](https://www.cnsa.gov.cn/n6758823/n6758844/n10518102/n10518147/c10565180/content.html) | Lunar return operations have been demonstrated; this does not establish routine industrial freight. |
| A 2025-04-25 interview with China's lunar-program chief designer, published by CNSA, described a basic research station before 2035 and expansion before 2045, with long autonomous operation and short human visits. [Station plan](https://www.cnsa.gov.cn/n6758823/n6758844/n10663475/n10663416/c10666366/content.html) | A stated program direction supports considering repeated operations; its dates and residence model are goals, not achieved capability. |
| NASA's 2026-11-07 release reported awards for miniCAST power-related components, with integration and testing still ahead. [NASA awards](https://www.nasa.gov/news-release/nasa-awards-moon-base-transportation-technology-science-projects/) | Procurement is more concrete than ambition, but component awards do not demonstrate a working shared service. |
| NASA's phases page, checked 2026-11-19, describes infrastructure deployment in 2029–2032 and outpost assembly from 2032. [NASA phases](https://www.nasa.gov/moonbase-phases/) | A published sequence helps define milestones; it does not warrant treating the schedule as certain. |
| Agency and commercial lunar manifest reviewed 2026-11-24: NASA CLPS 2 ($10B ceiling), SpaceX Starship HLS/commercial cargo (NET 2028, ~$100M/t, Astrolab FLEX), Blue Origin Blue Moon Mk1/Mk2 (2027–2028), Intuitive Machines (IM-3/4, relay, Stirling night-survival R&D), Firefly (Blue Ghost), ispace (5-sat Lunar Connect by 2030), Interlune (He-3 precursor), and China's Chang'e 7 (2027) & Chang'e 8 (2028 regolith 3D-printing demo). | Confirms an active 2027–2031 commercial "picks-and-shovels" logistics/comms/mobility market funded mostly by governments, while heavy lunar factories remain post-2031 and contingent on external paying demand. |

## Shared conventions

- **Rolling 125-year horizon cadence (3 tiers × 5 steps)**: Relative to the current baseline year (`Y0`, currently `2026`), forks align to three dedicated 5-checkpoint views (6 points including `Y0`): **near term** (`Y0+1`–`Y0+5`, every 1 yr: `2027`–`2031`), **medium term** (`Y0+5`–`Y0+25`, every 5 yr: `2031`, `2036`, `2041`, `2046`, `2051`), and **long term** (`Y0+25`–`Y0+125`, every 25 yr: `2051`, `2076`, `2101`, `2126`, `2151`). Forecasts cap at `Y0+125`. Each new calendar year, advance `Y0` by 1 year, resolve due forks against their original deadlines/criteria, preserve prior forecasts in revision history, and shift every tier forward by 1 year.
- **Conditional and path probabilities**: Each outcome gives its **conditional probability** given its full ancestral path and current evidence, and its **cumulative path probability** (the product of conditional probabilities along the path; this does not assume independence). Sibling outcomes for the same question and deadline are mutually exclusive and collectively exhaustive, summing to 100%.
- **Subjective estimates and confidence**: Initial numbers are uncalibrated subjective estimates, not measured frequencies or calibrated model outputs. **Confidence** (`high`, `medium`, `low`, `very-low`) is recorded separately from probability: low confidence means an estimate is easy to revise, not that the outcome is unlikely.
- **Unexpanded leaves**: An unexpanded leaf means **not yet modeled**, not zero probability of later development.
- **Resolution and lifecycle**: `resolution` (`pending | occurred | not-occurred | unresolved`) and `lifecycle` (`active | retired`) are tracked separately. Resolve an outcome only against its stated criteria and deadline; missing reports or inaccessible records leave the sibling pair `unresolved`, rather than proving failure. Changing a threshold creates a dated new version rather than retroactively changing the scoring target of an old forecast.
- **Scope and authority**: Forecast revisions neither promote content to canon nor alter approved claims in `canon/`.

## Revision history

- `2026-11-24`: Adopted the tiered 100-year forecast cadence (`2027–2031` annual, `2036–2051` every 5 years, `2051–2126` every 25 years; capped at +100 years / `2126`) and retired the 1000-year (`3026`) horizon from active trees.
- `2026-11-24`: Reorganized `forecasts/` from one-node-per-file into one-tree-per-topic-file; moved the lunar-led tree into [lunar-expansion.md](./lunar-expansion.md) without changing probabilities, criteria, or evidence cutoff.
- `2026-11-19`: Initial baseline and lunar-led forecast tree created ([sessions/2026-11-19-initial-forecast-tree](../sessions/2026-11-19-initial-forecast-tree.md)).
