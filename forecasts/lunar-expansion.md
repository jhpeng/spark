---
title: "Lunar-led expansion: 125-year long-term forecast tree (2051–2151)"
id: "lunar-expansion"
period: "2026-11-19/2151-12-31"
evidence_cutoff: "2026-11-24"
updated: "2026-11-24"
lifecycle: "active"
---

# Lunar-led expansion: 125-year long-term forecast tree (2051–2151)

Baseline: [forecasts/index](./index.md) · 5-year near-term tree: [forecasts/lunar-outpost-near-term](./lunar-outpost-near-term.md) · 25-year mid-term tree: [forecasts/lunar-industrial-mid-term](./lunar-industrial-mid-term.md)

This long-horizon **lunar-led tree** covers the **25-year-step (`Y0+25` to `Y0+125`: `2051`, `2076`, `2101`, `2126`, `2151`)** tier of the rolling 125-year forecast grid. It tracks five quarter-century milestones from sustained shared lunar services (`2051`) through routine local water/oxygen (`2076`), a multi-site lunar industrial network (`2101`), sustained lunar household residence (`2126`), and multi-year resilient lunar society (`2151`). Its probabilities do not cover every future for humanity: Mars, orbital industry, and other routes can develop under any lunar outcome. Repository reasoning draws on [wiki/concepts/geopolitical-drivers-of-space-expansion](../wiki/concepts/geopolitical-drivers-of-space-expansion.md), [wiki/concepts/lunar-base-development](../wiki/concepts/lunar-base-development.md), [wiki/tech/lunar-south-pole-industrial-power](../wiki/tech/lunar-south-pole-industrial-power.md), and [wiki/concepts/space-expansion-motives](../wiki/concepts/space-expansion-motives.md).

## Tree overview

Percentages show `(conditional probability | cumulative path probability)` under the 2026-11-24 evidence cutoff. All 8 active leaves (`*`) sum to exactly **100.0%** (exact products; rounded display values sum to 100.1%); unexpanded leaves (`*`) are not yet modeled, not zero probability of later expansion.

```text
2026 baseline (index)
├── 2051 · Sustained shared lunar services operating: lunar-services-2051 (65% | path 65.0%) [pending]
│   ├── 2076 · Routine lunar water/O2 in use: local-consumables-2076 (55% | path 35.8%) [pending]
│   │   ├── 2101 · Multi-site lunar industrial network operating: multi-site-industry-2101 (55% | path 19.7%) [pending]
│   │   │   ├── 2126 · Lunar households established (industrial path): local-supply-households-2126 (45% | path 8.8%) [pending]
│   │   │   │   ├── 2151 · Resilient multi-year-autonomous lunar society: resilient-lunar-society-2151 (40% | path 3.5%) [pending] *
│   │   │   │   └── 2151 · Lunar households remain Earth-resupply dependent: earth-dependent-households-2151 (60% | path 5.3%) [pending] *
│   │   │   └── 2126 · Automated/rotational industry without households: local-supply-no-households-2126 (55% | path 10.8%) [pending] *
│   │   └── 2101 · Single-hub local supply only (no multi-site network): single-hub-industry-2101 (45% | path 16.1%) [pending] *
│   └── 2076 · No routine lunar water/O2: no-local-consumables-2076 (45% | path 29.3%) [pending]
│       ├── 2126 · Lunar households established (import/late path): import-path-households-2126 (15% | path 4.4%) [pending] *
│       └── 2126 · No lunar households (import path): import-path-no-households-2126 (85% | path 24.9%) [pending] *
└── 2051 · No sustained shared lunar services by 2051: no-lunar-services-2051 (35% | path 35.0%) [pending]
    ├── 2076 · Delayed shared lunar services operating: delayed-lunar-services-2076 (45% | path 15.8%) [pending] *
    └── 2076 · Still no shared lunar services: still-no-lunar-services-2076 (55% | path 19.3%) [pending] *
```

## Observable milestones

```spark-visual
{
  "type": "phase-progression",
  "id": "lunar-milestones-progression",
  "title": "Lunar Expansion Long-Term Milestones (2051–2151)",
  "scale_mode": "schematic",
  "caption": "Schematic (not to scale): Five quarter-century classification thresholds across the 125-year long-term horizon (2051–2151). Thresholds define observable criteria rather than validated engineering minimums.",
  "params": {
    "stages": [
      {
        "code": "2051",
        "label": "Sustained Shared Services",
        "metric": "≥2 programs · ≥2 utilities · 3 yr",
        "summary": "At least one lunar-surface system supplies power, communications, cargo handling, or maintenance to ≥2 independent programs across 2049–2051."
      },
      {
        "code": "2076",
        "label": "Routine Local Water/O2",
        "metric": "≥10 t/yr · ≥20% local · 3 yr",
        "summary": "At least one lunar customer uses ≥10 tonnes/year of lunar-derived water or oxygen accounting for ≥20% of its consumption for 3 consecutive years."
      },
      {
        "code": "2101",
        "label": "Multi-Site Industry",
        "metric": "≥2 sites · ≥100 t/yr output",
        "summary": "At least two distinct lunar industrial sites (e.g., South Pole + Mare annex) produce ≥100 tonnes/year of propellant, metals, or structural materials."
      },
      {
        "code": "2126",
        "label": "Lunar Household Residence",
        "metric": "≥100 residents · ≥10 households · 10 yr",
        "summary": "At least one lunar site continuously houses ≥100 residents including ≥10 households treating it as their primary home for 10 consecutive years."
      },
      {
        "code": "2151",
        "label": "Resilient Lunar Society",
        "metric": "≥1,000 residents OR ≥5-yr autonomy",
        "summary": "Lunar settlements either house ≥1,000 continuous residents with broad local manufacturing OR demonstrate ≥5-year critical-supply autonomy from Earth."
      }
    ]
  }
}
```

These thresholds define forecast categories; they are **not validated engineering requirements or minimum viable population sizes**. All outcomes follow the shared resolution policy in [forecasts/index](./index.md): inadequate evidence leaves a sibling pair `unresolved`, not failed.

| Year | Milestone | Criterion |
|---|---|---|
| **2051** | **Sustained shared lunar services** | At least one lunar-surface service system has supplied ≥2 independently funded customer programs with at least two of power, communications, cargo handling, or maintenance during 2049–2051, and remains operating at the deadline. Bridges both early-2036 and delayed-2040s paths from [forecasts/lunar-industrial-mid-term](./lunar-industrial-mid-term.md). |
| **2076** | **Routine local water/oxygen** | At least one lunar customer has actually used lunar-origin water or oxygen at ≥10 tonnes/year and ≥20% of its total consumption of that same product across 2074–2076. Imported machinery is allowed; sample extraction, earthworks, metals, and Earth exports alone do not qualify. |
| **2101** | **Multi-site lunar industrial network** | At least two geographically distinct lunar industrial sites (e.g., a South Pole water/logistics hub plus a high-titanium mare metallurgy/manufacturing annex) operate concurrently and produce ≥100 tonnes/year combined of verified propellant, refined metals, or structural/energy components for lunar or orbital customers. |
| **2126** | **Sustained lunar households** | At least one lunar site has continuously housed ≥100 residents, including ≥10 households whose primary home is there rather than a work rotation, throughout 2117–2126. Turnover is allowed while totals persist; this does not establish reproduction, safe childhood, or independence. |
| **2151** | **Resilient multi-year-autonomous lunar society** | Lunar habitation and industry either continuously sustain ≥1,000 residents with local food/structural/repair supply chains OR credibly demonstrate ≥5 years of survival without Earth resupply for life support, power, and critical maintenance ("vitamins" buffered or locally substituted). |

## Forks

### 2051 — Sustained shared lunar services operating

- **Inherited path**: `index` (2026 baseline; aggregates the 25-year mid-term tree [forecasts/lunar-industrial-mid-term](./lunar-industrial-mid-term.md))
- **Question**: Are sustained shared lunar services operating continuously across 2049–2051?
- **Deadline**: `2051-12-31` · **Period**: `2026-11-24/2051-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `lunar-services-2051` | Sustained shared lunar services operating | 65% | 65.0% | `low` | `pending` | `active` |
| `no-lunar-services-2051` | No sustained shared lunar services by 2051 | 35% | 35.0% | `low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`lunar-services-2051` (65%)**: Gives 25 years for NASA/Artemis, CNSA/ILRS, and commercial logistics providers to establish at least one multi-customer utility hub (whether by 2036 or after a 2040s recovery). Does not require permanent residents, profitability, or MW-class factories.
  - **`no-lunar-services-2051` (35%)**: Missions remain isolated national sorties, budgets contract after symbolic crewed landings, or terrestrial alternatives keep lunar infrastructure unfunded (`earth-centered-development`).
- **Validation & revision signals**: Recondition directly from the `2036–2051` outcomes in [forecasts/lunar-industrial-mid-term](./lunar-industrial-mid-term.md).

---

### 2076 — Routine local water/oxygen use after sustained shared services

- **Inherited path**: `index` → `lunar-services-2051`
- **Question**: Is routine lunar-origin water or oxygen use achieved across 2074–2076?
- **Deadline**: `2076-12-31` · **Period**: `2052-01-01/2076-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `local-consumables-2076` | Routine lunar water/O2 in use | 55% | 35.8% | `very-low` | `pending` | `active` |
| `no-local-consumables-2076` | No routine lunar water/O2 | 45% | 29.3% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`local-consumables-2076` (55%)**: Explicitly adopts `lunar-local-supply` with a paying customer (state logistics, cislunar depots, or orbital computing). Imported machinery and public purchasing remain allowed; this proves neither commercial profitability nor Earth exports.
  - **`no-local-consumables-2076` (45%)**: Captures poor deposits, high dust/thermal wear, short contracts, or ultra-cheap reusable Earth launch outcompeting local extraction.
- **Validation & revision signals**: Track measured feedstock, equipment MTBF, power/thermal budgets, and actual annual accepted output ([wiki/tech/lunar-resource-utilization](../wiki/tech/lunar-resource-utilization.md)).

---

### 2076 — Delayed shared lunar services after missing 2051

- **Inherited path**: `index` → `no-lunar-services-2051`
- **Question**: Are shared lunar services operating across 2074–2076 after missing the 2051 milestone?
- **Deadline**: `2076-12-31` · **Period**: `2052-01-01/2076-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `delayed-lunar-services-2076` | Delayed shared lunar services operating | 45% | 15.8% | `very-low` | `pending` | `active` |
| `still-no-lunar-services-2076` | Still no shared lunar services | 55% | 19.3% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`delayed-lunar-services-2076` (45%)**: An additional quarter-century allows new funding cycles, improved robotics, or late orbital demand to revive shared lunar infrastructure.
  - **`still-no-lunar-services-2076` (55%)**: Persistent structural lack of paying demand or geopolitical fragmentation keeps the Moon limited to isolated visits; does not exclude orbital or Martian activity.
- **Validation & revision signals**: Look for newly funded independent customers and multi-year utility contracts after 2051.

---

### 2101 — Multi-site lunar industrial network after routine local consumables

- **Inherited path**: `index` → `lunar-services-2051` → `local-consumables-2076`
- **Question**: Is a multi-site lunar industrial network (≥2 distinct sites, ≥100 tonnes/year combined output) operating by `2101-12-31`?
- **Deadline**: `2101-12-31` · **Period**: `2077-01-01/2101-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `multi-site-industry-2101` | Multi-site lunar industrial network operating | 55% | 19.7% | `very-low` | `pending` | `active` |
| `single-hub-industry-2101` | Single-hub local supply only (no multi-site network) | 45% | 16.1% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`multi-site-industry-2101` (55%)**: Reflects the long-term South Pole saturation fork in [wiki/tech/lunar-south-pole-industrial-power](../wiki/tech/lunar-south-pole-industrial-power.md) — once local propellant and logistics mature, heavy metallurgy, mass-multiplier manufacturing (metals, basalt fibers, local solar), and potential mass drivers expand onto flat high-titanium mare plains alongside the South Pole hub.
  - **`single-hub-industry-2101` (45%)**: Local water/oxygen production remains viable for one polar base without sufficient cislunar or Earth-export demand to justify opening a second industrial site.
- **Validation & revision signals**: Track total MW-scale lunar power deployment, non-volatile metal/structural output, and multi-site surface/suborbital logistics.

---

### 2126 — Sustained lunar households after multi-site lunar industry

- **Inherited path**: `index` → `lunar-services-2051` → `local-consumables-2076` → `multi-site-industry-2101`
- **Question**: Is sustained lunar household residence (≥100 residents, ≥10 households across 2117–2126) achieved by `2126-12-31`?
- **Deadline**: `2126-12-31` · **Period**: `2102-01-01/2126-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `local-supply-households-2126` | Lunar households established (industrial path) | 45% | 8.8% | `very-low` | `pending` | `active` |
| `local-supply-no-households-2126` | Automated/rotational industry without households | 55% | 10.8% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`local-supply-households-2126` (45%)**: A mature multi-site industrial network lowers housing and supply barriers, enabling employment-led or community-led permanent residence if health, partial gravity, rights, and exit options work ([wiki/society/community-led-settlement](../wiki/society/community-led-settlement.md), [wiki/society/migration-contracts-and-resident-rights](../wiki/society/migration-contracts-and-resident-rights.md)).
  - **`local-supply-no-households-2126` (55%)**: Because Earth–Moon round-trip light delay is only ~2.56 seconds, teleoperated robotics and rotating crews can run a large lunar industrial economy with zero permanent families.
- **Validation & revision signals**: Verify long-term household residency records separately from industrial tonnage or rotational worker headcount.

---

### 2126 — Sustained lunar households without routine 2076 local water/oxygen

- **Inherited path**: `index` → `lunar-services-2051` → `no-local-consumables-2076`
- **Question**: Is sustained lunar household residence achieved across 2117–2126 despite missing the 2076 local water/oxygen milestone?
- **Deadline**: `2126-12-31` · **Period**: `2077-01-01/2126-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `import-path-households-2126` | Lunar households established (import/late path) | 15% | 4.4% | `very-low` | `pending` | `active` |
| `import-path-no-households-2126` | No lunar households (import path) | 85% | 24.9% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`import-path-households-2126` (15%)**: Reserves a path for strongly funded community/state settlements supported by cheap Earth transport or post-2076 local production.
  - **`import-path-no-households-2126` (85%)**: Broad residual reflecting accumulated funding, health, and household-preference barriers without early local supply.
- **Validation & revision signals**: Evaluate via actual household residence records rather than treating absent 2076 local oxygen as proof of abandonment.

---

### 2151 — Resilient multi-year-autonomous lunar society

- **Inherited path**: `index` → `lunar-services-2051` → `local-consumables-2076` → `multi-site-industry-2101` → `local-supply-households-2126`
- **Question**: By `2151-12-31`, do lunar settlements reach ≥1,000 continuous residents with broad local manufacturing OR ≥5-year critical-supply autonomy from Earth?
- **Deadline**: `2151-12-31` · **Period**: `2127-01-01/2151-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `resilient-lunar-society-2151` | Resilient multi-year-autonomous lunar society | 40% | 3.5% | `very-low` | `pending` | `active` |
| `earth-dependent-households-2151` | Lunar households remain Earth-resupply dependent | 60% | 5.3% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`resilient-lunar-society-2151` (40%)**: Over 125 years, a populated multi-site lunar economy closes most of the material and agricultural loop (or maintains deep strategic reserves of Earth "vitamins" like chips, catalysts, and enriched fuel), approaching the `civilization-backup` objective without assuming 100% eternal autarky.
  - **`earth-dependent-households-2151` (60%)**: Even prosperous lunar towns remain economically integrated with Earth for advanced semiconductors, specialized medicine, volatile elements (C, N, Cu), and nuclear fuel — analogous to modern high-tech island economies rather than autarkic fortresses.
- **Validation & revision signals**: Track local closure of food, pharmaceuticals, electronics/spares, and nuclear fuel cycles, plus total permanent resident population.

## Dependencies and unresolved validation

- **Companion near/mid-term trees**: [forecasts/lunar-outpost-near-term](./lunar-outpost-near-term.md) (`2027–2031`) and [forecasts/lunar-industrial-mid-term](./lunar-industrial-mid-term.md) (`2031–2051`).
- **Physics and open checks**: Radiation, 1/6 g multigenerational health, full ecosystem closure, and industrial "vitamins" substitution remain unresolved in [open-questions](../open-questions.md). [canon/laws](../canon/laws.md) and [canon/timeline](../canon/timeline.md) remain unchanged.

## Revision history

- `2026-11-24`: Expanded the long-term tier to the 5-step quarter-century grid (`2051`, `2076`, `2101`, `2126`, `2151`; capped at `Y0+125`). Moved the early `2036` shared-services checkpoint into the dedicated 25-year mid-term tree ([forecasts/lunar-industrial-mid-term](./lunar-industrial-mid-term.md)), anchored the long-term root at `2051`, and added `2101` (multi-site industrial network) and `2151` (resilient multi-year-autonomous lunar society) while preserving the `2076` and `2126` milestones.
- `2026-11-24`: Replaced single-letter milestone variables (`S`, `L`, `H`) with plain-language event descriptions; retired the 1000-year (`3026`) forks (`early-households-independent-3026`, `early-households-not-independent-3026`, `later-households-independent-3026`, `later-households-not-independent-3026`).
- `2026-11-19`: Initial lunar-led forecast tree created ([sessions/2026-11-19-initial-forecast-tree](../sessions/2026-11-19-initial-forecast-tree.md)).
