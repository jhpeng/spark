---
title: "Lunar industrialization & factory scaling: 25-year roadmap (2031–2051)"
id: "lunar-industrial-mid-term"
period: "2026-11-24/2051-12-31"
evidence_cutoff: "2026-11-24"
updated: "2026-11-24"
lifecycle: "active"
---

# Lunar industrialization & factory scaling: 25-year roadmap (2031–2051)

Baseline: [forecasts/index](./index.md) · 5-year near-term tree: [forecasts/lunar-outpost-near-term](./lunar-outpost-near-term.md) · 125-year long-term tree: [forecasts/lunar-expansion](./lunar-expansion.md)

This medium-term thematic tree covers the **5-year-step (`Y0+5` to `Y0+25`: `2031`, `2036`, `2041`, `2046`, `2051`)** tier of the rolling 125-year forecast grid. It bridges the government-led South Pole outpost buildup (`2027–2031`) into the actual **industrial factory transition**: testing whether an exogenous paying demand driver (such as `ai-industrial-expansion` → orbital computing, `earth-development-limits`, or sustained public industrial subsidies) appears by `2036`, whether "Factory #0" civil works and pilot ISRU work by `2041`, and whether humanity crosses the 40 kW → 1 MWe nuclear/hybrid industrial-park threshold by `2046–2051` ([wiki/tech/lunar-south-pole-industrial-power](../wiki/tech/lunar-south-pole-industrial-power.md)).

## Tree overview

Percentages show `(conditional probability | cumulative path probability)` under the 2026-11-24 evidence cutoff. All 10 active leaves (`*`) sum to exactly **100.0%** (both exact products and rounded display values). Across all histories, achieving shared lunar services by `2036` totals **65.0%** (`33.0% + 18.0% + 14.0%`), matching the shared-service baseline across the repository.

```text
2026 baseline (index)
├── 2031 · Initial South Pole utility & 2032–2036 service contracts locked in: outpost-utilities-2031 (60% | path 60.0%) [pending]
│   ├── 2036 · Shared lunar services operating + industrial demand funded: services-and-demand-2036 (55% | path 33.0%) [pending]
│   │   ├── 2041 · Factory #0 pads, ≥40–100 kWe power & ≥1 t/yr pilot ISRU: pilot-factory-2041 (60% | path 19.8%) [pending]
│   │   │   ├── 2046 · MW-class South Pole nuclear/hybrid park & ≥10 t/yr plant: mw-industrial-park-2046 (55% | path 10.9%) [pending]
│   │   │   │   ├── 2051 · Multi-MW manufacturing & cislunar supply (or Mare annex): scaled-lunar-industry-2051 (55% | path 6.0%) [pending] *
│   │   │   │   └── 2051 · Local-supply factory persists (~1–2 MWe), no wider export: local-supply-cap-2051 (45% | path 4.9%) [pending] *
│   │   │   └── 2046 · Stays sub-MW pilot scale without MW industrial park: sub-mw-plateau-2046 (45% | path 8.9%) [pending] *
│   │   └── 2041 · Pilot ISRU or 40–100 kWe power misses 2041 target: pilot-delayed-2041 (40% | path 13.2%) [pending]
│   │       ├── 2046 · Pilot ISRU & Factory #0 recovered by 2046 (5-yr slip): late-pilot-2046 (55% | path 7.3%) [pending] *
│   │       └── 2046 · Cheap Earth launch or dust/thermal wear defeats local ISRU: isru-economics-fail-2046 (45% | path 5.9%) [pending] *
│   ├── 2036 · Shared lunar services operating, science/geopolitics only: services-science-only-2036 (30% | path 18.0%) [pending]
│   │   ├── 2046 · Late AI/orbital demand triggers pilot factory by 2046: late-industrial-pivot-2046 (35% | path 6.3%) [pending] *
│   │   └── 2046 · Remains a shared science outpost without factories: permanent-science-outpost-2046 (65% | path 11.7%) [pending] *
│   └── 2036 · Early utilities stall before 3-year shared services: services-stalled-2036 (15% | path 9.0%) [pending] *
└── 2031 · No initial South Pole utility or shared commitment by 2031: no-outpost-utilities-2031 (40% | path 40.0%) [pending]
    ├── 2036 · Late recovery achieves shared lunar services by 2036: delayed-services-2036 (35% | path 14.0%) [pending] *
    └── 2036 · Still no shared lunar services by 2036: no-services-2036 (65% | path 26.0%) [pending] *
```

## Observable milestones

```spark-visual
{
  "type": "phase-progression",
  "id": "lunar-mid-term-progression",
  "title": "Lunar Base to MW-Class Factory Milestones (2031–2051)",
  "scale_mode": "schematic",
  "caption": "Schematic (not to scale): Five 5-year checkpoints spanning 2031 to 2051. Transitioning from a shared science outpost (2036) to a MW-class factory (2046–2051) requires an explicit paying industrial demand driver.",
  "params": {
    "stages": [
      {
        "code": "2031",
        "label": "Initial Utilities & Contracts",
        "metric": "≥1 utility · 2032–2036 funded",
        "summary": "Initial kW-class South Pole power/comms/mobility is deployed and multi-year budgets commit ≥2 programs to shared operations."
      },
      {
        "code": "2036",
        "label": "Shared Services + Demand",
        "metric": "≥2 programs (3 yr) + buyer",
        "summary": "Shared South Pole services operate for 3 consecutive years AND an explicit paying industrial demand driver funds pilot production."
      },
      {
        "code": "2041",
        "label": "Factory #0 & Pilot ISRU",
        "metric": "≥40–100 kWe · ≥1 t/yr O2/H2O",
        "summary": "Sintered landing pads/berms, ≥40–100 kWe continuous nuclear/hybrid power, and ≥1 tonne/year verified lunar O2/water production operate."
      },
      {
        "code": "2046",
        "label": "MW Industrial Park",
        "metric": "≥0.5–1 MWe · ≥10 t/yr output",
        "summary": "A MW-class South Pole nuclear/hybrid power park (plus optional PSR laser/HVDC feed) supports ≥10 tonnes/year of lunar consumables or structures."
      },
      {
        "code": "2051",
        "label": "Scaled Cislunar Industry",
        "metric": "Multi-MW · orbital/Mare scale",
        "summary": "Lunar factories scale past local base needs into recurring cislunar/orbital supply or initiate a flat high-titanium mare heavy-industry annex."
      }
    ]
  }
}
```

All outcomes follow the shared resolution policy in [forecasts/index](./index.md); missing evidence leaves a fork `unresolved`.

| Year | Milestone | Criterion |
|---|---|---|
| **2031** | **Initial utilities & shared contracts** | At least one dedicated kW-class South Pole utility (power, comms, or mobility) is operating AND funded multi-year contracts commit ≥2 independent programs to shared 2032–2036 operations (or recover within 2031). |
| **2036** | **Shared services + funded industrial demand** | Shared lunar services meet the 3-year threshold (≥2 independent programs, ≥2 utility types across 2034–2036) AND at least one paying industrial buyer or public industrial program funds a ≥1 tonne/year lunar pilot plant (distinguishing industrial pull from science-only outposts). |
| **2041** | **Factory #0 & pilot ISRU operating** | Sintered/stabilized landing pads and blast berms support recurring heavy landings, a ≥40–100 kWe continuous nuclear/hybrid power node operates ≥180 days/year, AND pilot ISRU produces ≥1 tonne/year of verified lunar oxygen, water, or sintered structural parts. |
| **2046** | **MW-class industrial park operating** | A ≥0.5–1 MWe continuous surface nuclear/hybrid power park operates at the lunar South Pole (with optional ELFO laser beaming or HVDC feed to PSRs) AND local production reaches ≥10 tonnes/year of accepted consumables or bulk materials. |
| **2051** | **Scaled multi-MW industry & external supply** | Lunar industrial capacity exceeds ≥2 MWe continuous AND either delivers recurring propellant/structural mass to cislunar/orbital customers (e.g., orbital computing or depots) OR initiates a second automated heavy-industry annex on a flat high-titanium mare plain. |

## Forks

### 2031 — Initial South Pole utilities and 2032–2036 contracts locked in

- **Inherited path**: `index` (2026 baseline; aggregates the 5-year tree [forecasts/lunar-outpost-near-term](./lunar-outpost-near-term.md))
- **Question**: Are initial South Pole utilities deployed and multi-year 2032–2036 shared commitments locked in by `2031-12-31`?
- **Deadline**: `2031-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `outpost-utilities-2031` | Initial South Pole utility & 2032–2036 service contracts locked in | 60% | 60.0% | `low` | `pending` | `active` |
| `no-outpost-utilities-2031` | No initial South Pole utility or shared commitment by 2031 | 40% | 40.0% | `low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`outpost-utilities-2031` (60%)**: Captures both on-time and minor-slip 2027–2031 histories where NASA (CLPS 2 / Artemis Moon Base Phase I) and/or CNSA (ILRS basic elements) put initial kW-class utilities on the ground and fund 2032–2036 operations.
  - **`no-outpost-utilities-2031` (40%)**: Captures heavy-lander delays (Starship/Blue Moon), chronic landing failures, or post-landing political fatigue reverting to flags-and-footprints visits.
- **Validation & revision signals**: Recondition directly from the annual outcomes of [forecasts/lunar-outpost-near-term](./lunar-outpost-near-term.md).

---

### 2036 (Recovery fork) — Shared lunar services after missing 2031

- **Inherited path**: `index` → `no-outpost-utilities-2031`
- **Question**: After missing the 2031 utility gate, do delayed programs still achieve 3-year shared lunar services by `2036-12-31`?
- **Deadline**: `2036-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `delayed-services-2036` | Late recovery achieves shared lunar services by 2036 | 35% | 14.0% | `low` | `pending` | `active` |
| `no-services-2036` | Still no shared lunar services by 2036 | 65% | 26.0% | `low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`delayed-services-2036` (35%)**: A rapid 2032–2033 deployment wave (e.g., ILRS 2035 basic station or recovered NASA Moon Base Phase I) still meets the 2034–2036 shared-service window.
  - **`no-services-2036` (65%)**: Missing 2031 leaves only 2 years to build and start a 3-year operating record by 2034, making a 2036 miss likely.
- **Validation & revision signals**: Track 2032–2034 utility deployments and multi-program access contracts.

---

### 2036 — Shared lunar services AND external industrial demand signal

- **Inherited path**: `index` → `outpost-utilities-2031`
- **Question**: By `2036-12-31`, are shared lunar services operating with a funded industrial pilot demand driver, operating for science/geopolitics only, or stalled?
- **Deadline**: `2036-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `services-and-demand-2036` | Shared lunar services operating + industrial demand funded | 55% | 33.0% | `low` | `pending` | `active` |
| `services-science-only-2036` | Shared lunar services operating, science/geopolitics only | 30% | 18.0% | `low` | `pending` | `active` |
| `services-stalled-2036` | Early utilities stall before 3-year shared services | 15% | 9.0% | `low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`services-and-demand-2036` (55%)**: The critical **motive gate** — either `ai-industrial-expansion` (e.g., commercially viable orbital compute placing cislunar supply/propellant orders), `earth-development-limits`, or sustained `state-funded-expansion` strategic logistics funds a real ≥1 t/yr pilot factory.
  - **`services-science-only-2036` (30%)**: The South Pole works well as an Antarctica-like research and geopolitical hub, but terrestrial AI/energy efficiency and cheap Earth launch leave **no commercial case for lunar factories**.
  - **`services-stalled-2036` (15%)**: Budget reversals, hardware attrition, or geopolitical fragmentation prevent a 3-year continuous shared-service record.
- **Validation & revision signals**: Track commercial orbital-compute economics ([wiki/tech/orbital-data-centers](../wiki/tech/orbital-data-centers.md)), AI energy/supply trends ([wiki/concepts/ai-driven-industrial-demand](../wiki/concepts/ai-driven-industrial-demand.md)), and binding ISRU off-take contracts.

---

### 2046 (Demand-pivot fork) — Late industrial pivot from a science-only outpost

- **Inherited path**: `index` → `outpost-utilities-2031` → `services-science-only-2036`
- **Question**: If the 2036 outpost is science-only, does exogenous industrial demand (e.g., AI/orbital compute or Earth limits) emerge to launch a pilot factory by `2046-12-31`?
- **Deadline**: `2046-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `late-industrial-pivot-2046` | Late AI/orbital demand triggers pilot factory by 2046 | 35% | 6.3% | `very-low` | `pending` | `active` |
| `permanent-science-outpost-2046` | Remains a shared science outpost without factories | 65% | 11.7% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`late-industrial-pivot-2046` (35%)**: A decade of AI/orbital scaling or policy shifts in the 2040s finally creates paying cislunar customers, leveraging the mature South Pole science hub.
  - **`permanent-science-outpost-2046` (65%)**: Fits `earth-centered-development`: Earth manufacturing and reusable launch remain cheaper, so the Moon stays a permanent scientific/geopolitical outpost without heavy industry.
- **Validation & revision signals**: Monitor Earth-to-orbit launch cost vs. cislunar propellant demand in the 2040s.

---

### 2041 — Factory #0 civil works, ≥40–100 kWe power, and ≥1 t/yr pilot ISRU

- **Inherited path**: `index` → `outpost-utilities-2031` → `services-and-demand-2036`
- **Question**: Are sintered landing pads/berms, ≥40–100 kWe continuous nuclear/hybrid power, and ≥1 tonne/year verified lunar ISRU operating by `2041-12-31`?
- **Deadline**: `2041-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `pilot-factory-2041` | Factory #0 pads, ≥40–100 kWe power & ≥1 t/yr pilot ISRU | 60% | 19.8% | `very-low` | `pending` | `active` |
| `pilot-delayed-2041` | Pilot ISRU or 40–100 kWe power misses 2041 target | 40% | 13.2% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`pilot-factory-2041` (60%)**: Given funded 2036 industrial demand, five years allow deploying a 40–100 kWe fission unit, paving sintered pads to stop 1–2 km/s plume ejecta, and proving tonne-scale oxygen/water extraction ([wiki/tech/lunar-resource-utilization](../wiki/tech/lunar-resource-utilization.md)).
  - **`pilot-delayed-2041` (40%)**: Nuclear launch-safety bottlenecks, abrasive dust jamming excavation, or high-temperature crucible/electrode failures delay pilot output past 2041.
- **Validation & revision signals**: Track 40 kWe FSP flight operations, sintered pad durability under heavy landings, and sustained ISRU reactor run-hours.

---

### 2046 (Recovery fork) — Consequences of missing 2041 pilot ISRU

- **Inherited path**: `index` → `outpost-utilities-2031` → `services-and-demand-2036` → `pilot-delayed-2041`
- **Question**: After missing 2041, is pilot ISRU recovered by `2046-12-31`, or do cheap Earth launch and lunar wear defeat local production?
- **Deadline**: `2046-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `late-pilot-2046` | Pilot ISRU & Factory #0 recovered by 2046 (5-yr slip) | 55% | 7.3% | `very-low` | `pending` | `active` |
| `isru-economics-fail-2046` | Cheap Earth launch or dust/thermal wear defeats local ISRU | 45% | 5.9% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`late-pilot-2046` (55%)**: Engineering redesigns overcome early dust and crucible wear, keeping the long-term `local-consumables-2076` path alive.
  - **`isru-economics-fail-2046` (45%)**: Imported "vitamins" (spares, seals, electrodes) and high maintenance make local production more expensive than flying supplies directly from Earth.
- **Validation & revision signals**: Measure full imported-spares ratio and delivered $/kg of lunar O₂ vs. Earth-launched LOX.

---

### 2046 — MW-class South Pole nuclear/hybrid industrial park operating

- **Inherited path**: `index` → `outpost-utilities-2031` → `services-and-demand-2036` → `pilot-factory-2041`
- **Question**: Does a ≥0.5–1 MWe continuous nuclear/hybrid power park support ≥10 tonnes/year of lunar consumables or bulk materials by `2046-12-31`?
- **Deadline**: `2046-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `mw-industrial-park-2046` | MW-class South Pole nuclear/hybrid park & ≥10 t/yr plant | 55% | 10.9% | `very-low` | `pending` | `active` |
| `sub-mw-plateau-2046` | Stays sub-MW pilot scale without MW industrial park | 45% | 8.9% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`mw-industrial-park-2046` (55%)**: Crosses the **40 kW → 1 MWe power gap** analyzed in [wiki/tech/lunar-south-pole-industrial-power](../wiki/tech/lunar-south-pole-industrial-power.md) using radial zoning, compact 650 K nuclear radiators (with waste-heat co-generation for ice baking/preheating), and optional ELFO orbital laser beaming or HVDC aluminum cables into PSRs.
  - **`sub-mw-plateau-2046` (45%)**: HALEU regulatory friction, polar ridge congestion, or insufficient recurring demand cap the site at sub-MW pilot scale.
- **Validation & revision signals**: Track MW-class space fission development, HALEU launch clearances, and multi-tonne annual ISRU output records.

---

### 2051 — Multi-MW manufacturing, cislunar supply, or High-Ti Mare annex

- **Inherited path**: `index` → `outpost-utilities-2031` → `services-and-demand-2036` → `pilot-factory-2041` → `mw-industrial-park-2046`
- **Question**: By `2051-12-31`, does lunar industry scale past ≥2 MWe into recurring cislunar/orbital supply (or initiate a flat high-titanium mare annex), or cap at local base supply?
- **Deadline**: `2051-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `scaled-lunar-industry-2051` | Multi-MW manufacturing & cislunar supply (or Mare annex) | 55% | 6.0% | `very-low` | `pending` | `active` |
| `local-supply-cap-2051` | Local-supply factory persists (~1–2 MWe), no wider export | 45% | 4.9% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`scaled-lunar-industry-2051` (55%)**: Begins Stage 2–3 mass multiplication (local metals, basalt fibers, lunar-made solar cells, orbital propellant/shielding deliveries) and confronts the South Pole topographic/Fe-Ti ceiling by opening a flat high-titanium mare heavy-industry annex.
  - **`local-supply-cap-2051` (45%)**: The 1–2 MWe South Pole plant profitably offsets local base imports, but orbital transport costs and Earth "vitamins" dependencies prevent wider export expansion.
- **Validation & revision signals**: Track cislunar propellant/structure deliveries, lunar-made PV/metal qualification, and site-selection commitments for mare plains ([wiki/tech/lunar-earth-cargo-system](../wiki/tech/lunar-earth-cargo-system.md)).

## Dependencies and unresolved validation

- **Core technical & economic dependencies**: [wiki/tech/lunar-south-pole-industrial-power](../wiki/tech/lunar-south-pole-industrial-power.md), [wiki/tech/lunar-resource-utilization](../wiki/tech/lunar-resource-utilization.md), [wiki/concepts/ai-driven-industrial-demand](../wiki/concepts/ai-driven-industrial-demand.md), and [wiki/concepts/earth-development-limits](../wiki/concepts/earth-development-limits.md).
- **Open checks**: HALEU launch approval, dust-wear MTBF, ELFO laser vs. HVDC crossover, and paying off-Earth demand remain tracked in [open-questions](../open-questions.md).

## Revision history

- `2026-11-24`: Created 25-year medium-term lunar industrialization tree (`2031–2051`, 5-year steps) bridging [forecasts/lunar-outpost-near-term](./lunar-outpost-near-term.md) (`2027–2031`) and [forecasts/lunar-expansion](./lunar-expansion.md) (`2051–2151`).
