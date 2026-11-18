# Open questions

Unresolved evidence, feasibility checks, and decisions within branches. Each question names the entries it affects and the investigation needed. Viable alternative futures remain in wiki entries; their coexistence is not itself a blocker. Remove a question once a session settles it, and link the entry that settled it.

<!-- Format:
## <question>
- Blocks: [[entry]], ...
- Scope: <affected branch identifiers, when applicable>
- Options: ...
- Raised: [[sessions/YYYY-MM-DD-topic]]
-->

## What magnetic interaction makes independent accelerator modules practical?

- Blocks: [[wiki/tech/modular-orbital-accelerator]], [[wiki/concepts/orbital-transportation-network]]
- Options: short interaction regions with many modules; longer or overlapping regions if field strength, coil mass, and ship coupling permit. Determine ship interface, aperture, force, structural loads, and useful interaction range before selecting a design; the illustrative 1 km range is unvalidated.
- Raised: [[sessions/2026-11-18-orbital-acceleration-network]]

## What passenger and cargo service limits should the network meet?

- Blocks: [[wiki/tech/modular-orbital-accelerator]], [[wiki/concepts/orbital-transportation-network]]
- Options: sufficient active distance for equal passenger/cargo boosts; smaller passenger boosts on shorter formations; different scheduled formations using the same modules. Specify ship mass, arrival speed, departure velocity, acceleration, pulse duration, and jerk. The 1 g and 100 g examples are not approved load limits.
- Raised: [[sessions/2026-11-18-orbital-acceleration-network]]

## How should accelerator formations be scheduled and controlled?

- Blocks: [[wiki/tech/modular-orbital-accelerator]], [[wiki/concepts/orbital-transportation-network]]
- Options: recurring corridors with limited repositioning; more extensive reconfiguration for individual arrivals. Quantify orbital drift, alignment tolerances, communication delay, repositioning time and propellant, and safe trajectories after missed or failed encounters.
- Raised: [[sessions/2026-11-18-orbital-acceleration-network]]

## What supplies launch power and handles waste heat?

- Blocks: [[wiki/tech/modular-orbital-accelerator]], [[wiki/concepts/orbital-transportation-network]]
- Options: continuous generation with stored launch energy; generation closer to instantaneous demand; independent module power or shared supply where transmission is feasible. Choose an energy source and model efficiency, storage mass, coil cooling, radiator temperature and area, and launch cadence. No fusion capability or 90% system efficiency is assumed established.
- Raised: [[sessions/2026-11-18-orbital-acceleration-network]]

## How do modules recover their orbits and obtain resources?

- Blocks: [[wiki/tech/modular-orbital-accelerator]], [[wiki/concepts/orbital-transportation-network]]
- Options: recovery propulsion supplied by local extraction and processing; imported resources; partial impulse recovery from compatible incoming traffic. Select exhaust velocity, module mass, resource source, and logistics; calculate propellant, energy, and recovery time. Opposing traffic does not automatically cancel orbital changes.
- Raised: [[sessions/2026-11-18-orbital-acceleration-network]]

## Where would the first network operate, and why would customers use it?

- Blocks: [[wiki/tech/modular-orbital-accelerator]], [[wiki/concepts/orbital-transportation-network]]
- Options: retain Jupiter as the initial candidate or compare another location once routes and demand are defined. Select orbits, destinations, resource access, and passenger/cargo volumes; calculate radiation dose and shielding, tidal effects, full trip times, arrival braking, and cost per delivered payload against onboard propulsion and tugs. No deployment date or profitability is established.
- Raised: [[sessions/2026-11-18-orbital-acceleration-network]]

## Which end-user services sustain paying demand for greater industrial capacity?

- Blocks: [[wiki/concepts/ai-driven-industrial-demand]], [[wiki/concepts/space-expansion-motives]], [[wiki/concepts/earth-development-limits]]
- Scope: `ai-industrial-expansion`, `climate-adaptation-pressure`, `earth-development-limits`; comparison with `earth-centered-development`.
- Options: quantify household assistance, care, housing, interactive experiences, and physical projects separately; identify private or public payers, affordability, price response, saturation, sharing, and efficiency gains. Test whether adoption increases total computation or material stocks rather than assuming unlimited demand or that infrastructure purchases are final demand.
- Raised: [[sessions/2026-11-19-drivers-of-space-expansion]]

## What physical automation and manufacturing capabilities can support expansion?

- Blocks: [[wiki/concepts/ai-driven-industrial-demand]], [[wiki/concepts/orbital-data-centers]], [[wiki/concepts/climate-adaptation-pressure]], [[wiki/concepts/earth-development-limits]]
- Scope: `ai-industrial-expansion`, `climate-adaptation-pressure`, `earth-development-limits`, and off-Earth extensions of `state-funded-expansion`.
- Options: specify which tasks machines can perform reliably, with what maintenance, human intervention, and supply dependencies. Separate extraction, refining, fabrication, memory, packaging, and equipment bottlenecks; test repair and recycling assumptions rather than treating improved AI or more ore as a complete manufacturing chain.
- Raised: [[sessions/2026-11-19-drivers-of-space-expansion]]

## Can a specified orbital computing service compete over its full lifecycle?

- Blocks: [[wiki/concepts/orbital-data-centers]], [[wiki/concepts/ai-driven-industrial-demand]], [[wiki/concepts/earth-development-limits]], [[wiki/concepts/state-funded-space-industry]]
- Scope: orbital-computing implementations of `ai-industrial-expansion`, `earth-development-limits`, `climate-adaptation-pressure`, or `state-funded-expansion`; none automatically inherits another's premises.
- Options: select workload, orbit, availability target, communications architecture, radiation tolerance, shielding, thermal design, hardware lifetime, replacement schedule, and launch/retirement plan. Measure delivered useful computation and compare full costs, financing, reliability, and latency with permitted terrestrial or local-device alternatives. The 10 MW example only bounds idealized collection and radiating areas.
- Raised: [[sessions/2026-11-19-drivers-of-space-expansion]]

## Which off-Earth resource chain has a paying customer and a cost advantage?

- Blocks: [[wiki/concepts/space-expansion-motives]], [[wiki/concepts/ai-driven-industrial-demand]], [[wiki/concepts/orbital-data-centers]], [[wiki/concepts/earth-development-limits]], [[wiki/concepts/state-funded-space-industry]]
- Scope: resource-supply extensions of `ai-industrial-expansion`, `earth-development-limits`, `climate-adaptation-pressure`, and `state-funded-expansion`.
- Options: identify resource concentration, location, extraction and processing yields, energy, equipment imports, repair, transport, output quality, throughput, and final payer. Compare supply for existing space users with Earth imports, recycling, substitutes, and terrestrial production; evaluate exports to Earth separately. Determine which initial capabilities still require terrestrial manufacturing and how rising in-use stocks affect recycling supply.
- Raised: [[sessions/2026-11-19-drivers-of-space-expansion]]

## What environmental accounting supports a particular development limit?

- Blocks: [[wiki/concepts/earth-development-limits]], [[wiki/concepts/orbital-data-centers]], [[wiki/concepts/climate-adaptation-pressure]]
- Scope: `earth-development-limits`, with environmental comparisons relevant to `climate-adaptation-pressure` and `earth-centered-development`.
- Options: define separate emissions, land, water, ecosystem, and any radiative-impact metrics, baselines, locations, and time horizons. Compare photovoltaic land-cover effects with displaced generation and alternative siting; the hypothetical planetary-albedo change is not a deployment forecast. Include Earth-based manufacture, launches, replacements, communications, and disposal in space-service accounting and avoid double-counting sunlight and electrical waste heat.
- Raised: [[sessions/2026-11-19-drivers-of-space-expansion]]

## What makes coordinated limits and the transition to space supply institutionally workable?

- Blocks: [[wiki/concepts/earth-development-limits]], [[wiki/concepts/state-funded-space-industry]]
- Scope: `earth-development-limits`; optional public support from `state-funded-expansion` must be explicitly adopted.
- Options: specify agreement coverage, compliance and verification, national implementation, treatment of trade and overseas production, transition material and emissions budgets, civilian necessities, financing, and allocation between incumbents and later developers. Explain why off-Earth activity qualifies under the chosen rules while remaining supervised, and whether policy credibility lasts long enough for capital recovery.
- Raised: [[sessions/2026-11-19-drivers-of-space-expansion]]

## When does adaptation increase total environmental pressure and justify off-Earth production?

- Blocks: [[wiki/concepts/climate-adaptation-pressure]], [[wiki/concepts/ai-driven-industrial-demand]]
- Scope: `climate-adaptation-pressure`; compare with `earth-centered-development` without requiring either future to replace the other.
- Options: choose regional climate, crop, water, cooling, power-supply, and emissions assumptions. Compare adaptation, mitigation, crop changes, controlled-environment production, terrestrial relocation, and any proposed off-Earth service on equal terms. Determine costs and payers, including whether crisis erodes investment capacity; do not infer planetary uninhabitability or indoor staple-crop viability from local stress.
- Raised: [[sessions/2026-11-19-drivers-of-space-expansion]]

## What supports permanent residence or an independently surviving settlement?

- Blocks: [[wiki/concepts/space-expansion-motives]], [[wiki/concepts/state-funded-space-industry]], [[wiki/concepts/earth-development-limits]]
- Scope: `community-led-settlement`, `civilization-backup`, and explicitly chosen settlement extensions of the industrial branches.
- Options: compare automated operations, rotation, and permanent residence; specify health, radiation, gravity, food, water, repair, medical care, family life, rights, affordability, and return options. A backup settlement additionally needs a credible industrial and biological supply chain after loss of Earth support; the 98% water-recovery example proves neither ecosystem closure nor independence.
- Raised: [[sessions/2026-11-19-drivers-of-space-expansion]]

## What public purpose and commitments sustain state-funded infrastructure?

- Blocks: [[wiki/concepts/state-funded-space-industry]]
- Scope: `state-funded-expansion`; separately, `lunar-military-industrialization`.
- Options: identify the public objective, purchaser, budget duration, fallback on withdrawal, and alternatives. For the separate lunar military hypothesis, establish the assumed treaty situation, political consequences, public rationale, and full industrial costs at a non-operational level. Cheapness and strategic superiority remain unproven; no weapon design, targeting, or performance optimization is required to record this uncertainty.
- Raised: [[sessions/2026-11-19-drivers-of-space-expansion]]

## When does early space capacity confer durable commercial advantage?

- Blocks: [[wiki/concepts/earth-development-limits]], [[wiki/concepts/space-expansion-motives]], [[wiki/concepts/state-funded-space-industry]]
- Scope: `earth-development-limits` and explicitly combined commercial/public-support scenarios.
- Options: model capital recovery, utilization, learning, contracts, interoperability, switching costs, access to logistics, and competing terrestrial efficiency gains. Distinguish production cost from sale price and market power. Identify conditions for durable concentration, open competition, or excess capacity; these outcomes remain viable alternatives rather than decisions that must be resolved to one future.
- Raised: [[sessions/2026-11-19-drivers-of-space-expansion]]
