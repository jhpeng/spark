---
title: Lunar–Earth cargo systems
kind: tech
era: null
status: draft
grounding: speculative
depends_on:
  - "[[canon/laws]]"
---

# Lunar–Earth cargo systems

## Summary

A lunar–Earth cargo system combines surface departure, transfer navigation, and Earth reentry and recovery. This entry compares rocket and fixed electromagnetic-launcher candidates, preserving demonstrated returns, illustrative energy checks, and unresolved engineering limits.

## Reasoning

### Scope

These are candidate technologies for `lunar-earth-export`, defined in [[wiki/concepts/lunar-earth-cargo]], which owns export demand and the staged development path. No architecture, export commodity, deployment date, or low-cost service is established here. Small returns are demonstrated; the complete industrial freight service remains `speculative`. Neither the military branch nor the free-flying orbital accelerator is inherited.

### The full service and launcher alternatives

| Segment | Required capability | Costs and limits to include |
|---|---|---|
| Surface departure | Put packaged cargo onto a suitable trajectory | Vehicle and propulsion, or fixed launcher construction, power, storage, cooling, maintenance, and compatible cargo interfaces. |
| Transfer toward Earth | Tracking, navigation, and any required corrections | Cargo carrier, control hardware, operations, transit time, and reliability. No orbit or transit duration is selected here. |
| Delivery to the surface | Controlled reentry, deceleration, protection, landing, and recovery | Thermal protection, load tolerance, recovery operations, losses, refurbishment, and any return or replacement of transport hardware. |

A fixed lunar electromagnetic launcher could retain heavy power and acceleration equipment at the site and reuse it. Recoil is transferred through its foundation to the Moon, unlike the free-flying modules in [[wiki/tech/modular-orbital-accelerator]]. Momentum remains conserved. The distinction removes the free-module orbit-recovery problem; it does not validate lunar construction, structural loads, alignment, dust resistance, wear, heat rejection, or payload acceleration tolerance.

At low traffic, rockets may avoid the fixed cost of a dedicated launcher. Greater, sustained throughput could favor more infrastructure, but the crossover remains unknown. Electromagnetic departure does not eliminate onboard guidance or Earth-arrival hardware. A direct return and a transfer involving an orbital service are alternatives to compare, not selected architectures. An advantage at one orbital destination does not establish an advantage delivering to low Earth orbit or Earth's surface.

## Validation

### Demonstrated return versus industrial scale

Apollo returned approximately **382 kg** of lunar material over six surface missions. This demonstrates physical return, not a freight price or an industrial production rate. [NASA: Apollo samples](https://science.nasa.gov/science-research/planetary-science/astrobiology/nasas-apollo-samples-yield-new-information-about-the-moon/)

A 1979 report describes construction and initial tests of a **2.5 m** electromagnetic mass-driver prototype. It supports the acceleration mechanism; it does not demonstrate a full-speed lunar export installation. [NASA technical report](https://ntrs.nasa.gov/citations/19800026231)

### Surface-departure energy scale

NASA lists lunar escape speed at approximately **2.38 km/s**, compared with **11.2 km/s** for Earth. Using the lunar value only as a reference scale, the kinetic energy per kilogram is:

**E/m = v²/2 = 2,380²/2 ≈ 2.83 MJ/kg ≈ 0.79 kWh/kg.**

This isolated-body escape-speed calculation is not a lunar-to-Earth trajectory solution, required mission delta-v, electricity bill, or delivered cost. A selected Earth–Moon trajectory must include both gravity fields and departure conditions. The estimate excludes carrier and packaging mass, propulsion or electrical losses, construction, maintenance, and operations. [NASA: Moon fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html), [OpenStax: kinetic energy](https://openstax.org/books/university-physics-volume-1/pages/7-2-kinetic-energy)

### Earth-arrival energy scale

Artemis I's lunar-return entry was approximately **11 km/s**. At that illustrative speed:

**E/m = 11,000²/2 = 60.5 MJ/kg ≈ 16.8 kWh/kg.**

This is kinetic energy per kilogram of the entering vehicle, not per kilogram of saleable product, and not heat all deposited into its shield or cargo. Much is transferred to the atmosphere during deceleration. Earth's gravity increases arrival speed; the different departure and arrival energy scales do not violate conservation. Atmospheric braking can save propellant, but thermal protection, guidance, deceleration loads, and recovery remain necessary. This is not a shield design or proof of economical bulk entry. [NASA: Artemis I mission results](https://ntrs.nasa.gov/api/citations/20230012789/downloads/IAC%202023Artemis%20I%20paper-FINALSTRIVES.pdf)

## Consequences

Departure, transfer, and arrival must be assessed as one service. A surface launcher's potential reduction in transported equipment does not replace navigation, cargo protection, or ground recovery; product form, tolerable loads, and traffic also affect architecture. Payers and investment scale are examined in [[wiki/concepts/lunar-earth-cargo]].

## Open questions

- Which departure, transfer, reentry, and recovery architecture meets the service requirement, including reusable versus replaceable hardware?
- What are the complete trajectory, trip duration, power and thermal budgets, cargo survival rate, and equipment lifetime?
- At what traffic and equipment life would fixed electromagnetic infrastructure improve on rocket service after construction, power, storage, thermal control, maintenance, and arrival costs?

These checks are tracked in [[open-questions]]. The proposal and existing calculations originate in [[sessions/2026-11-19-lunar-bases-and-cargo]].
