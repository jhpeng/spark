---
title: "Lunar South Pole outpost buildup: 5-year annual roadmap (2027–2031)"
id: "lunar-outpost-near-term"
period: "2026-11-24/2031-12-31"
evidence_cutoff: "2026-11-24"
updated: "2026-11-24"
lifecycle: "active"
---

# Lunar South Pole outpost buildup: 5-year annual roadmap (2027–2031)

Baseline: [forecasts/index](./index.md) · Long-horizon companion tree: [forecasts/lunar-expansion](./lunar-expansion.md)

This near-term thematic tree populates the **annual (`Y0+1` to `Y0+5`: `2027–2031`)** tier of the rolling 100-year forecast grid. Crucially, **2027–2031 is NOT a lunar factory era**: real-world 2026 schedules (NASA's 2029–2032 initial infrastructure phase, PROMISE late-2028 recon rover, China's pre-2030 crewed goal and 2035 basic station) and current demand drivers (`state-funded-expansion` and geopolitical competition, not commercial industrial off-take) only support **landing reliability, polar reconnaissance, lunar-night survival, and initial government-funded utilities** in this 5-year window. Industrial factories belong to the **2036–2051+** medium/long-term horizons, conditional on an exogenous paying demand driver (such as `ai-industrial-expansion` → orbital computing, `earth-development-limits`, or sustained public subsidy) actually materializing.

## Tree overview

Percentages show `(conditional probability | cumulative path probability)` under the 2026-11-24 evidence cutoff. All 10 active leaves (`*`) sum to exactly **100.0%** (both exact products and rounded display values). On-schedule shared-service contract lock-in by 2031 is **10.6%**, while 2-year slip-and-recover paths total **53.1%** (combined **63.7%**, consistent with reaching [lunar-services-2036](./lunar-expansion.md) at ~65%), and stall / isolated flags-and-footprints paths total **36.3%** (consistent with `no-lunar-services-2036` at ~35%).

```text
2026 baseline (index)
├── 2027 · Repeatable uncrewed South Pole landings & relay established: south-pole-access-2027 (60% | path 60.0%) [pending]
│   ├── 2028 · Crewed lunar return or polar recon rover launched: crewed-or-recon-2028 (70% | path 42.0%) [pending]
│   │   ├── 2029 · In-situ polar volatile survey & basic night survival: polar-survey-night-survival-2029 (65% | path 27.3%) [pending]
│   │   │   ├── 2030 · First initial surface utility deployed (power/comms/mobility): initial-utility-deployed-2030 (60% | path 16.4%) [pending]
│   │   │   │   ├── 2031 · Multi-year shared utility contracts locked in: shared-service-contracts-2031 (65% | path 10.6%) [pending] *
│   │   │   │   └── 2031 · Missions stay isolated without shared contracts: isolated-missions-only-2031 (35% | path 5.7%) [pending] *
│   │   │   └── 2030 · No initial surface utility deployed by 2030: no-initial-utility-2030 (40% | path 10.9%) [pending]
│   │   │       ├── 2031 · Initial surface utility recovered by 2031: delayed-utility-2031 (60% | path 6.6%) [pending] *
│   │   │       └── 2031 · Return to short flags-and-footprints visits only: flags-and-footprints-only-2031 (40% | path 4.4%) [pending] *
│   │   └── 2029 · Polar volatile survey or night-survival demo missed: no-polar-survey-2029 (35% | path 14.7%) [pending]
│   │       ├── 2031 · Polar survey & night survival recovered by 2031: delayed-survey-2031 (60% | path 8.8%) [pending] *
│   │       └── 2031 · Persistent polar-operations bottleneck through 2031: polar-ops-bottleneck-2031 (40% | path 5.9%) [pending] *
│   └── 2028 · Neither crewed return nor polar recon rover launched: no-crewed-or-recon-2028 (30% | path 18.0%) [pending]
│       ├── 2030 · Crewed return or polar recon recovered by 2030: delayed-crewed-or-recon-2030 (65% | path 11.7%) [pending] *
│       └── 2030 · Major program stretch-out or cancellation through 2030: program-stretchout-2030 (35% | path 6.3%) [pending] *
└── 2027 · No reliable South Pole landings or relay by 2027: no-south-pole-access-2027 (40% | path 40.0%) [pending]
    ├── 2029 · Uncrewed South Pole access recovered by 2029 (2-yr slip): delayed-access-recovery-2029 (65% | path 26.0%) [pending] *
    └── 2029 · Chronic landing/funding stall through 2029: chronic-access-stall-2029 (35% | path 14.0%) [pending] *
```

## Observable milestones

```spark-visual
{
  "type": "phase-progression",
  "id": "lunar-outpost-near-term-progression",
  "title": "South Pole Outpost Buildup Annual Milestones (2027–2031)",
  "scale_mode": "schematic",
  "caption": "Schematic (not to scale): Realistic 2027–2031 exploration and initial-infrastructure milestones grounded in 2026 NASA/CNSA schedules. No commercial lunar factory is expected in this 5-year window.",
  "params": {
    "stages": [
      {
        "code": "2027",
        "label": "Uncrewed Access & Relay",
        "metric": "≥2 landings · ≥500 kg · ≥1 relay",
        "summary": "At least two successful uncrewed South Pole soft landings (≥500 kg cumulative in 2026–2027) plus an operational communications/navigation relay."
      },
      {
        "code": "2028",
        "label": "Crewed Return / Recon Launch",
        "metric": "Crewed landing OR polar rover",
        "summary": "Either a crewed lunar landing succeeds OR a dedicated polar resource-prospecting rover (PROMISE/Chang'e-7 class) launches toward the South Pole."
      },
      {
        "code": "2029",
        "label": "Volatile Survey & Night Survival",
        "metric": "In-situ data · ≥1 lunar night",
        "summary": "Direct in-situ South Pole regolith/volatile measurements are returned AND a surface asset survives at least one full lunar night/eclipse."
      },
      {
        "code": "2030",
        "label": "First Initial Surface Utility",
        "metric": "≥1 power/comms/mobility node",
        "summary": "At least one dedicated multi-mission surface utility element (small kW-class power, comms hub, or pressurized/cargo mobility) is deployed at the South Pole."
      },
      {
        "code": "2031",
        "label": "Shared Utility Contracts",
        "metric": "≥2 programs · funded 2032–2036",
        "summary": "Recurring multi-year contracts commit ≥2 independent programs to share South Pole power, comms, or cargo services, setting up the 2036 milestone."
      }
    ]
  }
}
```

All outcomes are evaluated against stated criteria and deadlines under the shared resolution policy in [forecasts/index](./index.md); missing or unverifiable records leave a sibling pair `unresolved`. Milestones apply to any national, international, or commercial actor operating at the lunar South Pole (NASA/Artemis, CNSA/ILRS, or private operators).

### Real-world 2027–2031 agency & commercial manifest (checked 2026-11-24)

These are **dated published targets and commercial plans**, not guaranteed deliveries. Almost all funded 2027–2031 revenue is "picks-and-shovels" logistics, communications, and mobility purchased by governments (not heavy lunar factories):

| Actor / Company | Business or program model | Published 2027–2031 targets | Who pays / main limit |
|---|---|---|---|
| **NASA (Artemis & CLPS 2)** | Public exploration & $10B ceiling commercial delivery framework | **2027**: Artemis III Earth-orbit docking test with Starship/Blue Moon; **2028**: Artemis IV crewed landing target & late-2028 PROMISE recon rover; **2029–2032**: Moon Base Phase I initial utilities. | US appropriations; heavy-lander readiness and schedule slips. |
| **CNSA (Chang'e & ILRS)** | State robotic recon, ISRU demo, crewed landing, and research station | **2027**: Chang'e 7 (orbiter, lander, rover, PSR water-ice hopper) & Long March 10 / Mengzhou / Lanyue tests; **2028**: Chang'e 8 (South Pole ISRU & regolith 3D-printing demo); **2029**: lunar-orbit docking rehearsal; **2030**: crewed landing → 2035 basic ILRS. | Chinese state funding; integration of heavy launcher and lander. |
| **SpaceX / Blue Origin** | Heavy multi-tonne cargo & human lunar landers | **2027**: Starship HLS uncrewed landing demo, Blue Moon Mk1 (~3 t) Flights 1–2 & Mk2 test; **2028+**: Starship commercial lunar cargo debut (~$100M/t commercial pricing) & Blue Moon Mk1 Flight 3 / Mk2 demos. | NASA HLS contracts + early commercial heavy payloads (e.g., Astrolab); LEO propellant transfer (Starship) and New Glenn cadence. |
| **Intuitive Machines / Firefly** | Medium robotic cargo, comms relay, and night-survival R&D | **2027–2029**: IM-3 (Reiner Gamma), IM-4 (South Pole), Blue Ghost 2/3 under CLPS 2; Intuitive Machines Stirling nuclear night-survival R&D (with AFRL) and lunar relay network. | NASA CLPS 2 & defense/agency R&D; commercial landing reliability. |
| **ispace** | Commercial landers & orbital communications/positioning | Mission 3 / Draper South Pole deliveries; targeting a ≥5-satellite **Lunar Connect** relay and positioning constellation by **2030**. | Government payloads & commercial lunar mission operators. |
| **Venturi Astrolab** | Multi-tonne surface logistics & astronaut rover (**FLEX**) | Contracted for Starship commercial lunar cargo delivery (NET **2028**) to provide surface transport and logistics. | NASA LTV competition + commercial payload customers; depends on Starship landing readiness. |
| **Interlune** | Niche Earth-return resource harvesting (**Helium-3** & volatiles) | Plans precursor robotic harvesting demos once 2027–2030 commercial landers mature, targeting high-value-per-gram quantum cooling / medical imaging markets rather than bulk lunar factories. | Venture capital & future niche off-takers; unproven extraction economics and transport cost. |

| Year | Milestone | Why this year (evidence anchor) | Criterion |
|---|---|---|---|
| **2027** | **Uncrewed South Pole access & relay** | Anchored to **Chang'e 7** (South Pole orbiter/lander/PSR hopper), **Blue Moon Mk1** Flights 1–2, **Starship HLS** uncrewed landing demo, **CLPS** (Griffin-1, IM-3/IM-4, Blue Ghost 2/3), and Artemis III LEO docking tests. | At least two successful uncrewed soft landings in the South Pole region (≥80°S) delivering ≥500 kg cumulative payload across 2026–2027, plus ≥1 operational lunar relay/navigation node. |
| **2028** | **Crewed return or polar recon launch** | Anchored to **Artemis IV** (late-2028 crewed target), **PROMISE** recon rover (late-2028), **Chang'e 8** (ISRU & regolith 3D-printing brick demo), **Starship** commercial cargo debut (**Astrolab FLEX**), and **Blue Moon Mk1** Flight 3. | Either a crewed lunar surface landing is completed, OR a dedicated polar volatile-prospecting / ISRU-demo rover/lander launches successfully on a trans-lunar trajectory. |
| **2029** | **In-situ polar survey & night survival** | Matches **PROMISE**'s 18-month mission window (late 2028 → 2029–2030), **Chang'e 7/8** surface data, **Mengzhou–Lanyue** lunar-orbit docking rehearsal, and Intuitive Machines/AFRL night-survival tech maturation. | Direct surface measurements of South Pole regolith/volatile composition are returned, AND at least one surface asset survives and resumes operations after a full lunar night or multi-day polar eclipse. |
| **2030** | **First initial surface utility deployed** | Matches NASA's 2029–2032 Moon Base Phase I initial power/comms/mobility window, China's **pre-2030 crewed landing** goal, and **ispace**'s 5-satellite **Lunar Connect** 2030 constellation target. | At least one dedicated multi-mission surface utility element (small kW-class power station, surface comms hub, or shared mobility/cargo asset) is deployed and operating at the South Pole. |
| **2031** | **Shared utility contracts locked in** | Matches the `+5 yr` (`2031`) leading-indicator checkpoint in [forecasts/lunar-expansion](./lunar-expansion.md) and **CLPS 2** multi-year service scaling, testing whether government competition converts into funded shared services for 2032–2036. | Funded multi-year contracts or appropriations commit ≥2 independent programs to use shared South Pole power, comms, or cargo handling across 2032–2036. (Does **not** require a factory or ISRU plant.) |

## Forks

### 2027 — Repeatable uncrewed South Pole landings and relay established

- **Inherited path**: `index` (2026 baseline)
- **Question**: Are repeatable uncrewed South Pole soft landings (≥2 landings, ≥500 kg) and an operational relay node established by `2027-12-31`?
- **Deadline**: `2027-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `south-pole-access-2027` | Repeatable uncrewed South Pole landings & relay established | 60% | 60.0% | `low` | `pending` | `active` |
| `no-south-pole-access-2027` | No reliable South Pole landings or relay by 2027 | 40% | 40.0% | `low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`south-pole-access-2027` (60%)**: Multiple scheduled 2026–2027 commercial and national uncrewed missions make two soft landings and one relay plausible if early guidance lessons are applied.
  - **`no-south-pole-access-2027` (40%)**: Polar terrain hazards, low-angle shadows, and commercial lander reliability still carry high failure and slip risk.
- **Validation & revision signals**: Track CLPS, Artemis prep, and Chang'e-7 landing outcomes, delivered mass, and relay uptime.

---

### 2029 (Recovery fork) — Consequences of missing 2027 uncrewed access

- **Inherited path**: `index` → `no-south-pole-access-2027`
- **Question**: If 2027 access is missed, is repeatable uncrewed South Pole access recovered by `2029-12-31`?
- **Deadline**: `2029-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `delayed-access-recovery-2029` | Uncrewed South Pole access recovered by 2029 (2-yr slip) | 65% | 26.0% | `low` | `pending` | `active` |
| `chronic-access-stall-2029` | Chronic landing/funding stall through 2029 | 35% | 14.0% | `low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`delayed-access-recovery-2029` (65%)**: Typical 2-year aerospace slip — hazard-avoidance and lander fixes restore polar delivery by 2029, delaying initial utilities into the early 2030s while keeping `lunar-services-2036` viable.
  - **`chronic-access-stall-2029` (35%)**: Repeated failures erode legislative and commercial support, shifting activity back toward isolated orbital/science missions (`earth-centered-development`).
- **Validation & revision signals**: Monitor lander failure reviews, contract renewals, and agency budget changes.

---

### 2028 — Crewed lunar return or polar reconnaissance rover launched

- **Inherited path**: `index` → `south-pole-access-2027`
- **Question**: Does either a crewed lunar landing succeed OR a dedicated polar resource-prospecting rover launch by `2028-12-31`?
- **Deadline**: `2028-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `crewed-or-recon-2028` | Crewed lunar return or polar recon rover launched | 70% | 42.0% | `low` | `pending` | `active` |
| `no-crewed-or-recon-2028` | Neither crewed return nor polar recon rover launched | 30% | 18.0% | `low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`crewed-or-recon-2028` (70%)**: Because either a crewed landing (NASA 2028 target) OR a robotic recon rover launch (PROMISE late-2028 target) satisfies the gate, the joint probability is relatively high once 2027 access works. Driven purely by public exploration and geopolitical commitments ([wiki/concepts/geopolitical-drivers-of-space-expansion](../wiki/concepts/geopolitical-drivers-of-space-expansion.md)).
  - **`no-crewed-or-recon-2028` (30%)**: Heavy-lander development delays (HLS) combined with rover payload slips can push both past 2028.
- **Validation & revision signals**: Track HLS uncrewed flight tests, Artemis crewed readiness, and PROMISE integration milestones ([wiki/concepts/lunar-base-development](../wiki/concepts/lunar-base-development.md)).

---

### 2030 (Recovery fork) — Consequences of missing 2028 crewed/recon gate

- **Inherited path**: `index` → `south-pole-access-2027` → `no-crewed-or-recon-2028`
- **Question**: After missing 2028, is crewed return or polar recon recovered by `2030-12-31`, or does the program suffer a major stretch-out/cancellation?
- **Deadline**: `2030-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `delayed-crewed-or-recon-2030` | Crewed return or polar recon recovered by 2030 | 65% | 11.7% | `low` | `pending` | `active` |
| `program-stretchout-2030` | Major program stretch-out or cancellation through 2030 | 35% | 6.3% | `low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`delayed-crewed-or-recon-2030` (65%)**: Parallel US and Chinese lunar programs create strong political incentives to recover within two years (matching China's pre-2030 crewed goal).
  - **`program-stretchout-2030` (35%)**: Major vehicle redesigns, budget austerity, or geopolitical de-prioritization stretch timelines into the mid-2030s.
- **Validation & revision signals**: Track US/China crewed lander test flights and multi-year appropriations.

---

### 2029 — In-situ polar volatile survey and basic lunar-night survival

- **Inherited path**: `index` → `south-pole-access-2027` → `crewed-or-recon-2028`
- **Question**: Are direct South Pole regolith/volatile measurements returned AND at least one surface asset survives a lunar night/eclipse by `2029-12-31`?
- **Deadline**: `2029-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `polar-survey-night-survival-2029` | In-situ polar volatile survey & basic night survival | 65% | 27.3% | `low` | `pending` | `active` |
| `no-polar-survey-2029` | Polar volatile survey or night-survival demo missed | 35% | 14.7% | `low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`polar-survey-night-survival-2029` (65%)**: Directly resolves the first real-world unknown flagged in [wiki/tech/lunar-resource-utilization](../wiki/tech/lunar-resource-utilization.md) — whether polar ice exists at usable concentrations/depths — while proving small-scale hardware can survive polar cold traps and dark periods.
  - **`no-polar-survey-2029` (35%)**: Extreme <40 K thermal environments, abrasive lunar dust, or short lander battery life can prevent night survival or volatile sampling.
- **Validation & revision signals**: Track PROMISE / polar rover telemetry, volatile assay papers, and post-eclipse wake-up records.

---

### 2031 (Recovery fork) — Consequences of missing 2029 survey or night survival

- **Inherited path**: `index` → `south-pole-access-2027` → `crewed-or-recon-2028` → `no-polar-survey-2029`
- **Question**: After missing 2029, are polar survey data and basic night survival recovered by `2031-12-31`, or do polar-operations bottlenecks persist?
- **Deadline**: `2031-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `delayed-survey-2031` | Polar survey & night survival recovered by 2031 | 60% | 8.8% | `very-low` | `pending` | `active` |
| `polar-ops-bottleneck-2031` | Persistent polar-operations bottleneck through 2031 | 40% | 5.9% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`delayed-survey-2031` (60%)**: Follow-on robotic missions recover volatile measurements and night survival ~2 years late, delaying infrastructure siting decisions into the early 2030s.
  - **`polar-ops-bottleneck-2031` (40%)**: Dust fouling and cryogenic mechanical failures keep polar assets short-lived, preventing transition from single sorties to persistent infrastructure.
- **Validation & revision signals**: Track robotic heater/RHU/battery night-survival rates and dust-mitigation test results.

---

### 2030 — First initial surface utility deployed (power, comms, or mobility)

- **Inherited path**: `index` → `south-pole-access-2027` → `crewed-or-recon-2028` → `polar-survey-night-survival-2029`
- **Question**: Is at least one dedicated multi-mission surface utility element (small kW-class power, comms hub, or shared mobility) deployed and operating at the South Pole by `2030-12-31`?
- **Deadline**: `2030-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `initial-utility-deployed-2030` | First initial surface utility deployed (power/comms/mobility) | 60% | 16.4% | `very-low` | `pending` | `active` |
| `no-initial-utility-2030` | No initial surface utility deployed by 2030 | 40% | 10.9% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`initial-utility-deployed-2030` (60%)**: Aligns with NASA's 2029–2032 initial infrastructure phase (e.g., miniCAST-derived power/comms node, vertical solar array, or pressurized rover) and early ILRS basic-station elements. Still exploration-scale (kW-class), not an industrial factory.
  - **`no-initial-utility-2030` (40%)**: Heavy cargo lander availability and integrated surface-power procurement can slip past 2030 even after successful reconnaissance.
- **Validation & revision signals**: Track integrated-power contract awards, pressurized rover delivery schedules, and heavy cargo lander flights.

---

### 2031 (Recovery fork) — Consequences of missing 2030 initial utility deployment

- **Inherited path**: `index` → `south-pole-access-2027` → `crewed-or-recon-2028` → `polar-survey-night-survival-2029` → `no-initial-utility-2030`
- **Question**: After missing 2030, is an initial surface utility deployed by `2031-12-31`, or do lunar missions revert to short flags-and-footprints visits only?
- **Deadline**: `2031-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `delayed-utility-2031` | Initial surface utility recovered by 2031 | 60% | 6.6% | `very-low` | `pending` | `active` |
| `flags-and-footprints-only-2031` | Return to short flags-and-footprints visits only | 40% | 4.4% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`delayed-utility-2031` (60%)**: A 1-year hardware/launch slip still places the first utility on the surface within NASA's 2029–2032 phase, preserving a path to `lunar-services-2036`.
  - **`flags-and-footprints-only-2031` (40%)**: After achieving symbolic crewed return milestones, political will shifts away from expensive surface infrastructure, leaving only brief scientific visits.
- **Validation & revision signals**: Distinguish crewed-landing publicity budgets from sustained surface-infrastructure line items.

---

### 2031 — Multi-year shared utility contracts locked in for 2032–2036

- **Inherited path**: `index` → `south-pole-access-2027` → `crewed-or-recon-2028` → `polar-survey-night-survival-2029` → `initial-utility-deployed-2030`
- **Question**: Are funded multi-year contracts committing ≥2 independent programs to shared South Pole utilities across 2032–2036 signed by `2031-12-31`?
- **Deadline**: `2031-12-31` · **Evidence cutoff**: `2026-11-24`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `shared-service-contracts-2031` | Multi-year shared utility contracts locked in | 65% | 10.6% | `very-low` | `pending` | `active` |
| `isolated-missions-only-2031` | Missions stay isolated without shared contracts | 35% | 5.7% | `very-low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`shared-service-contracts-2031` (65%)**: Directly operationalizes the `2031 checkpoint` in [forecasts/lunar-expansion](./lunar-expansion.md). Converts one-off exploration hardware into a shared South Pole beachhead (power, comms, cargo handling) for 2032–2036. Whether this beachhead later evolves into an **industrial factory (2036–2051+)** still depends on a separate external demand check: e.g., whether `ai-industrial-expansion` (such as commercially viable [orbital data centers](../wiki/tech/orbital-data-centers.md)) or `earth-development-limits` creates paying off-Earth industrial customers.
  - **`isolated-missions-only-2031` (35%)**: Geopolitical rivalry or security restrictions prevent cross-program sharing, forcing agencies to duplicate isolated equipment rather than building a shared base.
- **Validation & revision signals**: Track cross-program service agreements, interoperability standards, cancellation terms, and — separately for post-2031 industrial demand — whether Earth AI/energy trends and orbital-compute economics justify off-Earth supply ([wiki/concepts/ai-driven-industrial-demand](../wiki/concepts/ai-driven-industrial-demand.md)).

## Why factories are NOT placed in 2027–2031

1. **Schedule & hardware lead times**: As of 2026-11-24, NASA's own published phases reserve 2027–2029 for access/reconnaissance and 2029–2032 for *initial* exploration infrastructure, with longer-stay assembly starting only from 2032 ([wiki/concepts/lunar-base-development](../wiki/concepts/lunar-base-development.md)). China's basic research station targets 2035.
2. **Absence of commercial factory demand in 2027–2031**: As noted in [wiki/concepts/ai-driven-industrial-demand](../wiki/concepts/ai-driven-industrial-demand.md) (IEA 2026 projection: global data centers ~950 TWh or ~3% of electricity by 2030), terrestrial energy and manufacturing are nowhere near forcing commercial lunar factories within five years. Without an explosive new demand driver (such as commercial orbital compute or binding Earth development limits), there is no paying customer for a megawatt-class lunar factory in 2031.
3. **Where factories enter the grid**: Pilot civil works ("Factory #0") and small-scale ISRU demonstrations belong in the **2036–2051** medium-term grid (`Y0+10` to `Y0+25`), conditional on `lunar-services-2036` AND an explicit paying industrial motive; MW-class nuclear/hybrid factories ([wiki/tech/lunar-south-pole-industrial-power](../wiki/tech/lunar-south-pole-industrial-power.md)) follow only once that demand is funded.

## Dependencies and unresolved validation

- **Borrowed worldbuilding premises**: Relies on `state-funded-expansion` and geopolitical competition as the primary 2027–2031 payer ([wiki/concepts/geopolitical-drivers-of-space-expansion](../wiki/concepts/geopolitical-drivers-of-space-expansion.md)); does not assume `ai-industrial-expansion`, `earth-development-limits`, or commercial polar ice reserves are already established.
- **Open checks**: Polar deposit quality, shared-service contract continuity, and post-2031 industrial demand remain tracked in [open-questions](../open-questions.md).

## Revision history

- `2026-11-24`: Created realistic 5-year annual South Pole outpost buildup tree (`2027–2031`) grounded in 2026 NASA/CNSA schedules and state-funded exploration motives, explicitly deferring industrial factories to 2036–2051+ conditional on paying demand (such as AI/orbital compute).
