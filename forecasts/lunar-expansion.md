---
title: "Lunar-led expansion: forecast tree"
id: "lunar-expansion"
period: "2026-11-19/3026-12-31"
evidence_cutoff: "2026-11-19"
updated: "2026-11-24"
lifecycle: "active"
---

# Lunar-led expansion: forecast tree

Baseline: [forecasts/index](./index.md)

This is a **lunar-led subtree**, developed from the repository's existing scenarios. It forecasts shared services (`S`), local consumables (`L`), household residence (`H`), and demonstrated independence (`I`) separately. Its probabilities do not cover every future for humanity: Mars, orbital industry, and other routes can develop under any lunar outcome. Repository reasoning draws on [wiki/concepts/geopolitical-drivers-of-space-expansion](../wiki/concepts/geopolitical-drivers-of-space-expansion.md), [wiki/concepts/lunar-base-development](../wiki/concepts/lunar-base-development.md), and [wiki/concepts/space-expansion-motives](../wiki/concepts/space-expansion-motives.md).

## Tree overview

Percentages show `(conditional probability | cumulative path probability)` under the 2026-11-19 evidence cutoff. Leaf frontier totals 100.0%; unexpanded leaves (`*`) are not yet modeled, not zero probability of later expansion. The 3026 branches below do not yield an all-path probability of lunar independence because several earlier leaves remain unexpanded.

```text
2026 baseline (index)
├── 2036 S met: lunar-services-2036 (65% | path 65.0%) [pending]
│   ├── 2076 L met: local-consumables-2076 (55% | path 35.8%) [pending]
│   │   ├── 2126 H met: local-supply-households-2126 (40% | path 14.3%) [pending]
│   │   │   ├── 3026 I met: early-households-independent-3026 (45% | path 6.4%) [pending] *
│   │   │   └── 3026 I not met: early-households-not-independent-3026 (55% | path 7.9%) [pending] *
│   │   └── 2126 H not met: local-supply-no-households-2126 (60% | path 21.5%) [pending]
│   │       ├── 3026 I met: later-households-independent-3026 (20% | path 4.3%) [pending] *
│   │       └── 3026 I not met: later-households-not-independent-3026 (80% | path 17.2%) [pending] *
│   └── 2076 L not met: no-local-consumables-2076 (45% | path 29.3%) [pending]
│       ├── 2126 H met: import-path-households-2126 (15% | path 4.4%) [pending] *
│       └── 2126 H not met: import-path-no-households-2126 (85% | path 24.9%) [pending] *
└── 2036 S not met: no-lunar-services-2036 (35% | path 35.0%) [pending]
    ├── 2076 S met later: delayed-lunar-services-2076 (45% | path 15.8%) [pending] *
    └── 2076 S still not met: still-no-lunar-services-2076 (55% | path 19.3%) [pending] *
```

## Observable milestones

```spark-visual
{
  "type": "phase-progression",
  "id": "lunar-milestones-progression",
  "title": "Lunar Expansion Milestone Progression (S → L → H → I)",
  "scale_mode": "schematic",
  "caption": "Schematic (not to scale): Ordered classification thresholds used in this forecast tree. Thresholds define observable criteria rather than validated engineering minimums.",
  "params": {
    "stages": [
      {
        "code": "S · 2036",
        "label": "Shared Services",
        "metric": "≥2 programs · ≥2 services · 3 yr",
        "summary": "At least one lunar-surface system supplies power, communications, cargo handling, or maintenance to ≥2 independently funded customer programs across 3 consecutive calendar years."
      },
      {
        "code": "L · 2076",
        "label": "Local Consumables",
        "metric": "≥10 t/yr · ≥20% local · 3 yr",
        "summary": "At least one lunar customer uses ≥10 tonnes/year of lunar-derived water or oxygen accounting for ≥20% of its total consumption of that product for 3 consecutive years."
      },
      {
        "code": "H · 2126",
        "label": "Household Residence",
        "metric": "≥100 residents · ≥10 households · 10 yr",
        "summary": "At least one lunar site continuously houses ≥100 residents including ≥10 households treating it as their primary home rather than a rotational work post for 10 consecutive years."
      },
      {
        "code": "I · 3026",
        "label": "Verified Independence",
        "metric": "30 yr no-Earth resupply",
        "summary": "At least one lunar community sustains food, water, air, power, medicines, equipment maintenance cycles, and generational maturity for 30 consecutive years without Earth resupply."
      }
    ]
  }
}
```

These thresholds define forecast categories; they are **not validated engineering requirements or minimum viable population sizes**. Each question asks whether its milestone is operating at the specified deadline with the required preceding record. Earlier milestones describe their own deadline windows; they need not remain true throughout intervening decades or centuries. All outcomes follow the shared resolution policy in [forecasts/index](./index.md): inadequate evidence leaves a sibling pair `unresolved`, not failed.

| Code | Criterion |
|---|---|
| **S — shared services** | At least one lunar-surface service system has supplied at least two independently funded customer programs with at least two of power, communications, cargo handling, or maintenance during each of the final three calendar years, and remains operating at the deadline. Separate programs may share a state sponsor; two instruments within one mission are not two programs. Ownership need not be commercial; occupancy is unnecessary. |
| **L — local consumables** | At least one lunar customer has actually used lunar-origin water or oxygen at ≥10 tonnes/year and ≥20% of its total consumption of that same product in each of the final three calendar years. Count a product consistently rather than counting water and its extracted oxygen twice. Imported machinery is allowed; sample extraction, earthworks, metals, and Earth exports alone do not satisfy L. |
| **H — household residence** | At least one lunar site has continuously housed ≥100 residents, including ≥10 households whose primary home is there rather than a work rotation, throughout the final ten years. A household means at least two people sharing domestic life; turnover is allowed while totals persist. This does not establish reproduction, safe childhood, or independence. |
| **I — demonstrated independence** | At least one lunar community remains operational after the final 30 consecutive years without Earth material deliveries or essential Earth-directed operations. Records must show locally sustained food, water, air, power, essential medicines and replacement equipment through actual maintenance cycles, plus locally born people reaching adulthood. Any off-Earth supplier must also satisfy the no-Earth-dependence test; dependence cannot be hidden behind an intermediary. Stockpiles alone do not qualify. This is finite demonstrated resilience, not proof of indefinite survival. |

## Forks

### 2036 — Shared lunar services (`S`)

- **Inherited path**: `index` (2026 baseline)
- **Question**: Is **S** (shared lunar services) met through 2034–2036?
- **Deadline**: `2036-12-31` · **Period**: `2026-11-20/2036-12-31` · **Evidence cutoff**: `2026-11-19`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `lunar-services-2036` | **S met** — shared lunar services operating | 65% | 65.0% | `low` | `pending` | `active` |
| `no-lunar-services-2036` | **S not met** — no qualifying shared services | 35% | 35.0% | `low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`lunar-services-2036` (65%)**: Dated procurement and multiple infrastructure ambitions make at least one functioning shared system more plausible than none over ten years, while reserving substantial weight for schedule, integration, access, and funding failures. Public science or strategic procurement is a plausible payer under [wiki/society/state-funded-space-industry](../wiki/society/state-funded-space-industry.md); commercial or mixed funding also qualifies. Does not require permanent residents, local production, open access to every country, or profitability.
  - **`no-lunar-services-2036` (35%)**: Missions, isolated facilities, private infrastructure, and short visits may still occur, fitting [Earth-centered development](../wiki/concepts/space-expansion-motives.md), without meeting the shared-service threshold. Announcements can outlast budgets, separate national programs can duplicate equipment instead of sharing, and hardware setbacks or serious disruption can prevent a three-year record.
- **Validation & revision signals**: Track recurring paid contracts, cross-program utilization, delivered power/communications, downtime, repair capability, and cancellations. [wiki/concepts/geopolitical-drivers-of-space-expansion](../wiki/concepts/geopolitical-drivers-of-space-expansion.md) explains why political competition may fund services yet restrict access; [wiki/concepts/lunar-base-development](../wiki/concepts/lunar-base-development.md) and [open-questions](../open-questions.md) keep public commitments, customer access, and mass/power/thermal budgets unresolved.

---

### 2076 — Recurring lunar consumables (`L`) after early `S`

- **Inherited path**: `index` → `lunar-services-2036`
- **Question**: Is **L** (recurring lunar-origin water or oxygen use) met through 2074–2076?
- **Deadline**: `2076-12-31` · **Period**: `2037-01-01/2076-12-31` · **Evidence cutoff**: `2026-11-19`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `local-consumables-2076` | **L met** — recurring local water/oxygen use | 55% | 35.8% | `very-low` | `pending` | `active` |
| `no-local-consumables-2076` | **L not met** — no qualifying local consumables | 45% | 29.3% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`local-consumables-2076` (55%)**: Explicitly adopts `lunar-local-supply`: an identified customer uses lunar water or oxygen repeatedly. An earlier service base supplies customers and operating experience, and four decades allow repeated trials. Imported machinery and public purchasing remain allowed; this proves neither commercial competitiveness, a complete manufacturing chain, nor exports to Earth.
  - **`no-local-consumables-2076` (45%)**: Captures unreliable extraction, weak deposits, low utilization, short contracts, or low-cost Earth supply. Services may persist on imports, operate at lower scale, or contract; earthworks, metalworking, or pilot experiments can exist without qualifying under `L`. Says nothing certain about post-2076 production.
- **Validation & revision signals**: [wiki/tech/lunar-resource-utilization](../wiki/tech/lunar-resource-utilization.md) requires measured feedstock, recovery, power, heat rejection, consumables, maintenance, and accepted output (its hypothetical `1/(0.05×0.8) = 25` tonnes feedstock per tonne of water is only a mass balance). Contracts must pay for independent uses rather than circular supplier demand. Compare actual annual accepted output and import prices against `L`; track site/production-process and off-Earth customer checks in [open-questions](../open-questions.md).

---

### 2076 — Delayed shared lunar services (`S`) after missed 2036 `S`

- **Inherited path**: `index` → `no-lunar-services-2036`
- **Question**: Is **S** met through 2074–2076 after missing the 2036 milestone?
- **Deadline**: `2076-12-31` · **Period**: `2037-01-01/2076-12-31` · **Evidence cutoff**: `2026-11-19`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `delayed-lunar-services-2076` | **S met later** — delayed shared services (leaf) | 45% | 15.8% | `very-low` | `pending` | `active` |
| `still-no-lunar-services-2076` | **S still not met** — no qualifying services (leaf) | 55% | 19.3% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`delayed-lunar-services-2076` (45%)**: Forty additional years permit recovery from schedule slips, new funding cycles, improved delivery reliability, or compatible customer programs. This is a distinct history from early services and is not merged into `lunar-services-2036`.
  - **`still-no-lunar-services-2076` (55%)**: Slightly favors persistent structural obstacles after the early miss: terrestrial alternatives may remain adequate, independent customers may not materialize, or access may stay fragmented. Includes intermittent missions, single-program bases, contraction, or catastrophic disruption (without asserting disruption as expected). Does not exclude successful orbital or Martian activity.
- **Validation & revision signals**: Look for newly funded independent customers, multi-year operating records, compatibility, and whether earlier failure causes were corrected. [wiki/society/state-funded-space-industry](../wiki/society/state-funded-space-industry.md), [wiki/concepts/geopolitical-drivers-of-space-expansion](../wiki/concepts/geopolitical-drivers-of-space-expansion.md), [wiki/concepts/lunar-base-development](../wiki/concepts/lunar-base-development.md), and [wiki/concepts/space-expansion-motives](../wiki/concepts/space-expansion-motives.md) frame candidate mechanisms and Earth-centered alternatives; good local science can coexist with failure of `S`.

---

### 2126 — Household residence (`H`) after early `S` and `L`

- **Inherited path**: `index` → `lunar-services-2036` → `local-consumables-2076`
- **Question**: Is **H** (sustained lunar household residence) met through 2117–2126?
- **Deadline**: `2126-12-31` · **Period**: `2077-01-01/2126-12-31` · **Evidence cutoff**: `2026-11-19`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `local-supply-households-2126` | **H met** — households after local supply | 40% | 14.3% | `very-low` | `pending` | `active` |
| `local-supply-no-households-2126` | **H not met** — local-supply history without H | 60% | 21.5% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`local-supply-households-2126` (40%)**: Earlier services and consumables lower some supply barriers, but do not by themselves create a household motive to move. Explicitly adds a residential motive (employment, community autonomy, public resilience spending, or a mix; no specific contract or government assumed). The 100-resident threshold is a category boundary, not a viability result.
  - **`local-supply-no-households-2126` (60%)**: Weights the separation between industrial usefulness and household preference. Automation and rotating staff can keep operations productive with few residents, while health, expense, housing, rights, or funding loss can prevent `H`. Compatible with technical success rather than necessarily industrial failure; does not forbid later residential communities.
- **Validation & revision signals**: [wiki/society/community-led-settlement](../wiki/society/community-led-settlement.md) and [wiki/society/migration-contracts-and-resident-rights](../wiki/society/migration-contracts-and-resident-rights.md) require funded living costs, rights, healthcare, and workable exit. [wiki/concepts/ai-driven-industrial-demand](../wiki/concepts/ai-driven-industrial-demand.md) makes automation an optional output aid, not proof of migration. Verify residency records separately from jobs; radiation, partial-gravity health, food, maintenance, and continuity after sponsor withdrawal remain open in [open-questions](../open-questions.md).

---

### 2126 — Household residence (`H`) after early `S` but missed 2076 `L`

- **Inherited path**: `index` → `lunar-services-2036` → `no-local-consumables-2076`
- **Question**: Is **H** met through 2117–2126 despite missing the 2076 consumables milestone?
- **Deadline**: `2126-12-31` · **Period**: `2077-01-01/2126-12-31` · **Evidence cutoff**: `2026-11-19`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `import-path-households-2126` | **H met** — households after missed L (leaf) | 15% | 4.4% | `very-low` | `pending` | `active` |
| `import-path-no-households-2126` | **H not met** — no households after missed L (leaf) | 85% | 24.9% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`import-path-households-2126` (15%)**: Reserves a path for strongly motivated and funded households supported by imports, subsidies, community wealth, or local production that catches up after 2076 ("import path" identifies the earlier history, not mandatory permanent import dependence). Lower weight than the local-supply history reflects fewer demonstrated enabling capabilities, not a physical law or causal-effect estimate.
  - **`import-path-no-households-2126` (85%)**: Broad residual reflecting accumulated funding, health, supply, and household-preference barriers on this history—not an 85% forecast of abandonment or civilizational decline. The Moon can retain research, robotic activity, rotating crews, smaller communities, or post-2076 local production without meeting `H`.
- **Validation & revision signals**: Evaluate via actual `H` residence records rather than treating absent local oxygen as proof of no households. [wiki/society/community-led-settlement](../wiki/society/community-led-settlement.md), [wiki/society/migration-contracts-and-resident-rights](../wiki/society/migration-contracts-and-resident-rights.md), [wiki/concepts/lunar-base-development](../wiki/concepts/lunar-base-development.md), and [wiki/concepts/space-expansion-motives](../wiki/concepts/space-expansion-motives.md) frame residence motives, enforceable supply/exit terms, and Earth-centered alternatives. No Earth export industry, cheap orbital transport, or indefinite life support is assumed.

---

### 3026 — Demonstrated independence (`I`) after early `S`, `L`, and `H`

- **Inherited path**: `index` → `lunar-services-2036` → `local-consumables-2076` → `local-supply-households-2126`
- **Question**: Is **I** (finite demonstrated lunar independence) met through 2997–3026?
- **Deadline**: `3026-12-31` · **Period**: `2127-01-01/3026-12-31` · **Evidence cutoff**: `2026-11-19`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `early-households-independent-3026` | **I met** — independence after early H (leaf) | 45% | 6.4% | `very-low` | `pending` | `active` |
| `early-households-not-independent-3026` | **I not met** — no independence after early H (leaf) | 55% | 7.9% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`early-households-independent-3026` (45%)**: Applies the `civilization-backup` capability test regardless of motive (deliberate backup funding is optional). Nine centuries and a prior household/production history allow substantial learning, while earlier communities may change, migrate, or be succeeded by a qualifying lunar community. Not a claim of infinite survival, mass migration, or interstellar expansion.
  - **`early-households-not-independent-3026` (55%)**: Slightly favors persistence of at least one essential dependency or failure to sustain the 30-year test. Includes prosperous Earth-dependent settlements, communities choosing specialization and trade, manufacturing bottlenecks, health limits, smaller populations, or loss of lunar habitation. Failure of `I` is not synonymous with extinction and allows off-Earth civilizations outside lunar scope.
- **Validation & revision signals**: Audit food/nutrient closure, replacement tools and components, essential medicines, energy/thermal budgets, and birth-to-adulthood health; reserves alone cannot pass `I`. Identify which requirement fails if `I` is not met. [wiki/concepts/space-expansion-motives](../wiki/concepts/space-expansion-motives.md) and [wiki/society/community-led-settlement](../wiki/society/community-led-settlement.md) distinguish backup capability from autonomy as a motive. No accelerator or new physics is required; all critical budgets remain open in [open-questions](../open-questions.md).

---

### 3026 — Demonstrated independence (`I`) after early `S` and `L`, no `H` in 2126

- **Inherited path**: `index` → `lunar-services-2036` → `local-consumables-2076` → `local-supply-no-households-2126`
- **Question**: Is **I** met through 2997–3026 after missing the 2126 household milestone?
- **Deadline**: `3026-12-31` · **Period**: `2127-01-01/3026-12-31` · **Evidence cutoff**: `2026-11-19`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `later-households-independent-3026` | **I met later** — independence after missed H (leaf) | 20% | 4.3% | `very-low` | `pending` | `active` |
| `later-households-not-independent-3026` | **I not met** — no independence after missed H (leaf) | 80% | 17.2% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`later-households-independent-3026` (20%)**: Preserves a substantial late-start possibility over nine centuries as motives, technology, and residence evolve. Lower weight than the early-household history reflects more uncompleted transitions, not a claim that missing 2126 makes settlement physically impossible. Applies the `civilization-backup` capability test regardless of motive; robotic production alone does not yield residence or independence.
  - **`later-households-not-independent-3026` (80%)**: Combines residence never meeting the test with failure to achieve industrial and biological independence even if later households form (does not require households to remain absent throughout 2127–3026). Includes dependent later settlements, robotic/rotating operations, and abandonment; not an 80% estimate of disaster, stagnation, or absence of all space civilization.
- **Validation & revision signals**: Track subsequent household adoption and retention, essential import inventories, actual component replacement and food production, human lifecycle health, and an audited 30-year operating record. [wiki/society/community-led-settlement](../wiki/society/community-led-settlement.md), [wiki/concepts/lunar-base-development](../wiki/concepts/lunar-base-development.md), and [wiki/concepts/space-expansion-motives](../wiki/concepts/space-expansion-motives.md) separate useful industry, settlement motives, Earth-centered development, and the backup test.

## 2031 checkpoint and revision triggers

By **2031-12-31**, review operational deliveries, recurring paid contracts, cross-program use of power or communications, cancellation provisions, equipment failure and repair, and accessible resource surveys. These are five-year leading indicators, not an extra probability-bearing fork. Repeated delivery and multi-year use strengthen `lunar-services-2036`; cancellations, incompatible isolated missions, or persistent failures weaken it. An announcement alone changes less than verified service performance. Reassess all affected siblings and descendants together without presuming new evidence will narrow uncertainty.

## Dependencies and unresolved validation

- **Optional demand mechanisms** (not baseline assumptions of limitless consumption, global restrictions, or an uninhabitable Earth): [wiki/concepts/ai-driven-industrial-demand](../wiki/concepts/ai-driven-industrial-demand.md), [wiki/concepts/earth-development-limits](../wiki/concepts/earth-development-limits.md), and [wiki/concepts/climate-adaptation-pressure](../wiki/concepts/climate-adaptation-pressure.md).
- **Optional, unproven applications** (neither cheap Earth exports nor a modular accelerator is assumed; no fusion, mind uploading, unknown physics, geopolitical winner, or military-industrial branch is selected): [wiki/tech/orbital-data-centers](../wiki/tech/orbital-data-centers.md), [wiki/concepts/lunar-earth-cargo](../wiki/concepts/lunar-earth-cargo.md), and [wiki/tech/orbital-transportation-network](../wiki/tech/orbital-transportation-network.md).
- **Physics and open checks**: Physics checks are inherited only within their stated assumptions (e.g., the lunar-base entry's hypothetical `30/(10−2) = 3.75`-year imported-mass offset does not establish financial payback or equipment lifetime). No complete production, radiation, thermal, food, manufacturing, or transport budget has been closed here; relevant checks remain in [open-questions](../open-questions.md). [canon/laws](../canon/laws.md) and [canon/timeline](../canon/timeline.md) contain no approved future industrial sequence that this tree changes.

## Revision history

- `2026-11-24`: Consolidated the 14 separate outcome node files into this single thematic tree file (`forecasts/lunar-expansion.md`) under the updated forecast tree rules; preserved all outcome IDs, conditional probabilities, criteria, evidence cutoff (`2026-11-19`), and rationale.
- `2026-11-19`: Initial lunar-led forecast tree created ([sessions/2026-11-19-initial-forecast-tree](../sessions/2026-11-19-initial-forecast-tree.md)).
