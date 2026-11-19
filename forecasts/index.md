---
title: "Lunar-led expansion: initial forecast tree"
id: "index"
parent: null
children: ["lunar-services-2036", "no-lunar-services-2036"]
period: "2026-11-19/3026-12-31"
evidence_cutoff: "2026-11-19"
updated: "2026-11-19"
conditional_probability: null
confidence: "low"
resolution: "pending"
lifecycle: "active"
---

# Lunar-led expansion: initial forecast tree

This is a **lunar-led subtree**, developed from the repository's existing scenarios. It forecasts shared services, local consumables, household residence, and demonstrated independence separately. Its probabilities do not cover every future for humanity: Mars, orbital industry, and other routes can develop under any lunar outcome.

## Baseline and evidence

Recorded and selectively checked on **2026-11-19**; this is the evidence cutoff, not a claim to have surveyed every event through that date. [[canon/timeline]] supplies the repository's 2026 starting setting; [[canon/laws]] binds every path. Future wiki scenarios remain assumptions, not observations.

| Dated evidence | Supported conclusion and limit |
|---|---|
| CNSA reported Chang'e 6's lunar far-side sample return on 2024-06-25. [Mission report](https://www.cnsa.gov.cn/n6758823/n6758844/n10518102/n10518147/c10565180/content.html) | Lunar return operations have been demonstrated; this does not establish routine industrial freight. |
| A 2025-04-25 interview with China's lunar-program chief designer, published by CNSA, described a basic research station before 2035 and expansion before 2045, with long autonomous operation and short human visits. [Station plan](https://www.cnsa.gov.cn/n6758823/n6758844/n10663475/n10663416/c10666366/content.html) | A stated program direction supports considering repeated operations; its dates and residence model are goals, not achieved capability. |
| NASA's 2026-11-07 release reported awards for miniCAST power-related components, with integration and testing still ahead. [NASA awards](https://www.nasa.gov/news-release/nasa-awards-moon-base-transportation-technology-science-projects/) | Procurement is more concrete than ambition, but component awards do not demonstrate a working shared service. |
| NASA's phases page, checked 2026-11-19, describes infrastructure deployment in 2029–2032 and outpost assembly from 2032. [NASA phases](https://www.nasa.gov/moonbase-phases/) | A published sequence helps define milestones; it does not warrant treating the schedule as certain. |

These references motivate a lunar starting point. Repository reasoning comes from [[wiki/concepts/geopolitical-drivers-of-space-expansion]], [[wiki/concepts/lunar-base-development]], and [[wiki/concepts/space-expansion-motives]]. Public scientific or strategic purchases are a candidate early payer; rivalry is optional. Continued funding, compatibility, reliability, and access for later users remain conditions.

## How to read the probabilities

Each number is an **initial subjective estimate**, conditional on the full path and this evidence set, expressed as a fraction in metadata and a percentage below. None is a measured frequency or calibrated model output. Low confidence means the number is easy to revise; it does not mean a low chance of the outcome. Long-horizon estimates have very low confidence.

Sibling branches are complements and sum to 100%; causes such as AI demand, public procurement, and environmental policy can coexist and are not competing outcomes. The tree keeps Earth-centered, delayed, and limited-development paths. An unexpanded leaf means **not yet modeled**, not zero probability of later expansion.

For example, early services → local consumables → households has path probability **0.65 × 0.55 × 0.40 = 14.3%** under this initial assessment. The 3026 branches below do not yield an all-path probability of lunar independence: several earlier leaves remain unexpanded.

## Observable milestones

These thresholds define forecast categories; they are **not validated engineering requirements or minimum viable population sizes**. Each question asks whether its milestone is operating at the specified deadline, with the required preceding record. Earlier milestones describe their own deadline windows; they need not remain true throughout intervening decades or centuries.

| Code | Criterion |
|---|---|
| **S — shared services** | At least one lunar-surface service system has supplied at least two independently funded customer programs with at least two of power, communications, cargo handling, or maintenance during each of the final three calendar years, and remains operating at the deadline. Separate programs may share a state sponsor; two instruments within one mission are not two programs. Ownership need not be commercial; occupancy is unnecessary. |
| **L — local consumables** | At least one lunar customer has actually used lunar-origin water or oxygen at ≥10 tonnes/year and ≥20% of its total consumption of that same product in each of the final three calendar years. Count a product consistently rather than counting water and its extracted oxygen twice. Imported machinery is allowed; sample extraction, earthworks, metals, and Earth exports alone do not satisfy L. |
| **H — household residence** | At least one lunar site has continuously housed ≥100 residents, including ≥10 households whose primary home is there rather than a work rotation, throughout the final ten years. A household means at least two people sharing domestic life; turnover is allowed while totals persist. This does not establish reproduction, safe childhood, or independence. |
| **I — demonstrated independence** | At least one lunar community remains operational after the final 30 consecutive years without Earth material deliveries or essential Earth-directed operations. Records must show locally sustained food, water, air, power, essential medicines and replacement equipment through actual maintenance cycles, plus locally born people reaching adulthood. Any off-Earth supplier must also satisfy the no-Earth-dependence test; dependence cannot be hidden behind an intermediary. Stockpiles alone do not qualify. This is finite demonstrated resilience, not proof of indefinite survival. |

Resolve a yes outcome only with adequate operational evidence; resolve its complement only when adequate evidence establishes failure to meet the criterion at the deadline. Missing reports or inaccessible records leave the pair **unresolved**, rather than proving failure. Until assessment, both siblings remain pending. Preserve and evaluate each dated forecast against its original criteria. A threshold change creates a dated new version, not a new scoring target for the old prediction.

## Navigation

| Horizon and inherited path | Next alternatives: conditional probability |
|---|---|
| 2036, from this baseline | [[forecasts/lunar-services-2036|S met: 65%]] · [[forecasts/no-lunar-services-2036|S not met: 35%]] |
| 2076, after S in 2036 | [[forecasts/local-consumables-2076|L met: 55%]] · [[forecasts/no-local-consumables-2076|L not met: 45%]] |
| 2076, after no S in 2036 | [[forecasts/delayed-lunar-services-2076|S met later: 45%]] · [[forecasts/still-no-lunar-services-2076|S still not met: 55%]] |
| 2126, after early S and L | [[forecasts/local-supply-households-2126|H met: 40%]] · [[forecasts/local-supply-no-households-2126|H not met: 60%]] |
| 2126, after early S but no L | [[forecasts/import-path-households-2126|H met: 15%]] · [[forecasts/import-path-no-households-2126|H not met: 85%]] |
| 3026, after early S, L, and H | [[forecasts/early-households-independent-3026|I met: 45%]] · [[forecasts/early-households-not-independent-3026|I not met: 55%]] |
| 3026, after early S and L but no H in 2126 | [[forecasts/later-households-independent-3026|I met later: 20%]] · [[forecasts/later-households-not-independent-3026|I not met: 80%]] |

## 2031 checkpoint and revision triggers

By **2031-12-31**, review operational deliveries, recurring paid contracts, cross-program use of power or communications, cancellation provisions, equipment failure and repair, and accessible resource surveys. These are five-year leading indicators, not an extra probability-bearing fork. Repeated delivery and multi-year use strengthen the early-services estimate; cancellations, incompatible isolated missions, or persistent failures weaken it. An announcement alone changes less than verified service performance. Reassess all affected siblings together without presuming the evidence will narrow uncertainty.

## Dependencies and unresolved validation

The long path draws on service demand, `lunar-local-supply`, residential motives, and the capability requirements of `civilization-backup` at their relevant nodes. Outcomes are defined by demonstrated capabilities; no single motive is required, including deliberate backup funding. [[wiki/concepts/ai-driven-industrial-demand]], [[wiki/concepts/earth-development-limits]], and [[wiki/concepts/climate-adaptation-pressure]] are optional demand mechanisms, not baseline assumptions of limitless consumption, global restrictions, or an uninhabitable Earth.

[[wiki/tech/orbital-data-centers]], [[wiki/concepts/lunar-earth-cargo]], and [[wiki/tech/orbital-transportation-network]] remain optional, unproven applications. The forecast assumes neither cheap Earth exports nor a modular accelerator. Neither fusion, mind uploading, nor unknown physics is required. No geopolitical winner or military-industrial branch is selected.

Physics checks are inherited only within their stated assumptions. For example, the lunar-base entry's hypothetical 30/(10−2) = 3.75-year imported-mass offset does not establish financial payback or equipment lifetime. No complete production, radiation, thermal, food, manufacturing, or transport budget has been closed here. Relevant checks remain in [[open-questions]]; each node identifies which ones constrain its estimate. [[canon/laws]] and [[canon/timeline]] contain no approved future industrial sequence that this tree changes.

Initial creation and estimate provenance: [[sessions/2026-11-19-initial-forecast-tree]]. The root is a baseline, not a pending future outcome; its null probability and pending resolution are administrative placeholders.
