---
title: Orbital data centers
kind: tech
era: null
status: draft
grounding: speculative
depends_on:
  - "[canon/laws](../../canon/laws.md)"
---

# Orbital data centers

## Summary

Orbital data centers combine computing hardware, power collection, heat rejection, and communications to serve paying customers on Earth from orbit. This candidate engineering architecture could provide early demand for space transport, assembly, and maintenance without first requiring a large off-world population. Competitive lifetime cost, scalable engineering, and a suitable workload have not been established for the proposed industrial scale.

## Reasoning

### Scope and branches

The physical accounting below applies wherever this architecture is considered; no branch assumes that it is deployed automatically. Large-scale deployment remains `speculative` in each of these conditional applications:

- `ai-industrial-expansion`: customers in [wiki/concepts/ai-driven-industrial-demand](../concepts/ai-driven-industrial-demand.md) purchase enough useful computing to justify orbital investment after terrestrial and local-device alternatives are compared.
- `earth-development-limits`: [wiki/concepts/earth-development-limits](../concepts/earth-development-limits.md) constrains additional terrestrial environmental loads while explicitly permitting qualifying off-world facilities. Policy must count Earth-side manufacturing, launch, replacement, and disposal rather than merely moving the operating address.
- `climate-adaptation-pressure`: the demand described in [wiki/concepts/climate-adaptation-pressure](../concepts/climate-adaptation-pressure.md) may include computing services, but adaptation needs do not by themselves establish an orbital advantage.
- `state-funded-expansion`: public procurement in [wiki/society/state-funded-space-industry](../society/state-funded-space-industry.md) could fund early services or research. Continuing subsidy and independent commercial demand are distinct possibilities.

These applications are optional combinations, not inherited premises across branches. `earth-centered-development`, discussed in [wiki/concepts/space-expansion-motives](../concepts/space-expansion-motives.md), remains possible if terrestrial efficiency, supply, or changed consumption removes the advantage.

### Customer and business case

Cloud operators or specialist providers would finance facilities using investment and customer contracts; governments could be early purchasers. Customers buy applications or useful compute, not necessarily knowledge of the servers' location. Sending information rather than bulk physical products back to Earth may suit this business, provided communication capacity, latency, reliability, and data-handling requirements are met.

The comparison is lifetime cost per delivered useful workload, including financing, power and thermal equipment, launch, communications, radiation-related faults, maintenance, hardware replacement, and disposal. Earlier availability could have value where terrestrial capacity is delayed, but faster orbital construction is itself an unverified assumption. Cheap compute alone does not establish superior models, software, or customer service.

Repeat orders might support assembly and repair services, then selected local material production. Such a supply chain must retain an external paying purpose; a mine and transport operator cannot justify each other solely by exchanging orders. Advanced processors could continue to come from Earth even if some bulky structures are eventually made elsewhere.

## Validation

### Physics: power and heat

Use an illustrative **10 MW computing load**, not an approved specification. At Earth's solar distance, incident sunlight normal to the rays is approximately **1,361 W/m²**. Assuming **30% electrical conversion efficiency**, uninterrupted illumination, and no other losses:

**A_solar = 10,000,000 / (1,361 × 0.30) ≈ 24,500 m².**

This is effective illuminated panel area. It excludes auxiliary loads, power conversion losses, storage, degradation, shadowing, pointing losses, and backup capacity. Continuous sunlight is an orbit-dependent design choice, not a general property of orbit. [NASA: solar irradiance](https://data.giss.nasa.gov/modelforce/solar.irradiance/)

Assume approximately **10 MW becomes onboard waste heat**, radiator temperature **350 K** (about **77°C**), emissivity **0.9**, and an unobstructed view of a cold sink with negligible incident heat. The idealized radiation balance is **P = εσAT⁴**, with **σ = 5.670374419 × 10⁻⁸ W m⁻² K⁻⁴**:

**A_radiator = 10,000,000 / (0.9 × 5.670374419 × 10⁻⁸ × 350⁴) ≈ 13,100 m².**

This is total effective emitting surface area, not planar footprint. Both faces count only if both actually radiate under the assumed thermal and view conditions. Real design must include absorbed sunlight and Earth radiation, view factors, transport of heat from processors, temperature differences, auxiliary heat, redundancy, and degradation. Vacuum provides no external air for convective heat rejection; a complete thermal system remains necessary. The area calculation does not establish deployable mass or reliability. [NASA: thermal control](https://www.nasa.gov/smallsat-institute/sst-soa/thermal-control/), [NIST: Stefan–Boltzmann constant](https://physics.nist.gov/cgi-bin/cuu/Value?sigma)

No orbit, shielding, communications architecture, or maintenance route is selected. Radiation exposure, full latency, collision risk, power interruptions, and transport budgets therefore remain unquantified rather than passed checks.

### Engineering precedents and limits

Google's November 2025 Project Suncatcher describes research into solar-powered TPU satellites connected by optical links, including a near-continuously illuminated dawn–dusk sun-synchronous orbit as a candidate. This is a research architecture, not evidence of economical industrial deployment. Starcloud reports H100-based orbital computing and AI demonstrations on Starcloud-1; a demonstration does not validate the economics or reliability of a large computing fleet. These are proponents' reports, not independent commercial-performance audits. [Google: Project Suncatcher](https://research.google/blog/exploring-a-space-based-scalable-ai-infrastructure-system-design/), [Starcloud-1](https://www.starcloud.com/starcloud-1)

### Consistency and environmental accounting

During [sessions/2026-11-19-drivers-of-space-expansion](../../sessions/2026-11-19-drivers-of-space-expansion.md), checked [canon/laws](../../canon/laws.md), [canon/timeline](../../canon/timeline.md), and related repository entries. Energy conservation, radiative cooling, light-speed limits, and orbital transport costs are retained; no canon deployment or date is added. The existing [wiki/tech/orbital-transportation-network](./orbital-transportation-network.md) and [wiki/tech/modular-orbital-accelerator](./modular-orbital-accelerator.md) remain independent speculative proposals, not required infrastructure or proven cost reductions.

Moving operation off Earth does not eliminate Earth-side emissions or licensing. For example, US satellite rules include orbital-debris and end-of-mission requirements. A branch claiming environmental benefit must compare complete lifecycles and define where energy is used and waste heat is rejected. [FCC: satellite rules](https://docs.fcc.gov/public/attachments/FCC-25-69A1.pdf)

## Consequences

- Recurring demand could finance transport, assembly, repair, and selected material production, if their full costs are competitive.
- Large unmanned facilities can coexist with very small human populations. Permanent settlement requires a separate motive and support system.
- Early operators may gain customer relationships and operational experience; competitors, standardization, or stranded investment remain possible. Policy-driven competition is developed in [wiki/concepts/earth-development-limits](../concepts/earth-development-limits.md).
- Ground-based efficiency, local inference, improved power supply, or weaker demand can leave computing primarily on Earth.

## Open questions

- For the applicable branches above, which paying workloads tolerate orbital communications, and what utilization and contracts support investment?
- Which orbit, power, thermal, shielding, fault-recovery, and servicing design meets the required availability and hardware replacement cycle?
- Does lifetime cost per useful workload beat terrestrial upgrades, local computing, and legally available alternative capacity?
- Under `earth-development-limits`, what is the complete lifecycle environmental burden and how is it counted against the agreement?
- Which services or materials could be supplied locally at a genuine advantage, without assuming the existing accelerator proposal works?

These unresolved checks are tracked in [open-questions](../../open-questions.md).
