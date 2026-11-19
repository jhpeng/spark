---
title: Modular orbital accelerator
kind: tech
era: null
status: draft
grounding: speculative
depends_on:
  - "[canon/laws](../../canon/laws.md)"
---

# Modular orbital accelerator

## Summary

A station composed of separate, free-flying electromagnetic accelerator modules gives passing spacecraft successive velocity changes. Modules arrange their encounter positions and timing around the incoming trajectory, requested departure trajectory, and permitted acceleration. The same infrastructure is intended to serve passengers and cargo within a [wiki/tech/orbital-transportation-network](./orbital-transportation-network.md).

## Reasoning

### Scope

This is a candidate technology that a branch may explicitly adopt, not an existing facility or a shared premise of space expansion. Its illustrative specifications do not constrain unrelated transport architectures; routes and deployment depend on a separately justified [wiki/tech/orbital-transportation-network](./orbital-transportation-network.md).

### Design rationale

The user proposes moving heavy propulsion infrastructure from individual ships into reusable stations. Independent modules avoid a single continuous supporting structure and allow incremental construction and replacement. Each module supplies a small part of the total velocity change, receives the opposite impulse, and subsequently restores its operating orbit using propulsion and supplied resources.

Both passenger and cargo service are design intentions. Force and timing must be controlled to meet each vehicle's acceleration limit; adjusting electrical power alone does not specify a safe force profile. Formations must be planned in advance: repositioning modules takes time and changes their orbits. Jupiter is the original candidate location, but no orbit, resource source, or deployment date has been selected.

This is speculative engineering, not speculative physics. Electromagnetic acceleration and precision formation flying have precedents, but their combination at the required mass, speed, interaction range, and scale has not been demonstrated. Economics and a complete engineering path remain unresolved.

## Validation

### Physics: acceleration, energy, and power

All masses, speeds, acceleration limits, and efficiencies below are illustrative assumptions, not approved specifications. Use a 100-tonne ship (100,000 kg), approximately 1 g = 9.81 m/s², and a common initial station frame. These straight-line estimates neglect orbital gravity and small module motions; a real Jovian formation needs orbital simulation. Standard gravity is 9.80665 m/s². [NIST conversion factors](https://www.nist.gov/pml/special-publication-811/nist-guide-si-appendix-b-conversion-factors/nist-guide-si-appendix-b9)

For constant along-track acceleration, L = (v_f² − v_i²)/(2a) and t = (v_f − v_i)/a. [OpenStax: constant acceleration](https://openstax.org/books/university-physics-volume-1/pages/3-4-motion-with-constant-acceleration)

| Illustrative encounter | Active acceleration distance | Time under thrust |
|---|---|---|
| 0 → 10 km/s at 1 g | 10,000² / (2 × 9.81) ≈ 5,100 km | 10,000 / 9.81 ≈ 1,019 s |
| 0 → 10 km/s at 100 g | 10,000² / (2 × 981) ≈ 51 km | 10,000 / 981 ≈ 10.2 s |
| 10 → 20 km/s at 1 g | (20,000² − 10,000²) / (2 × 9.81) ≈ 15,300 km | 10,000 / 9.81 ≈ 1,019 s |

The 100 g case assumes specially engineered cargo, not a general cargo tolerance. Passenger acceleration limits, pulse duration, and jerk remain to be specified.

Ship kinetic-energy gain is ΔK = m(v_f² − v_i²)/2: 5 TJ for 0 → 10 km/s and 15 TJ for 10 → 20 km/s. These are ship-energy figures in the stated frame, not complete electrical or orbital-recovery budgets. [OpenStax: kinetic energy](https://openstax.org/books/university-physics-volume-1/pages/7-2-kinetic-energy)

For the first case, average mechanical power is 5 × 10¹² / 1,019 ≈ 4.9 GW. At constant acceleration, instantaneous ship power P = Fv = mav rises to about 9.81 GW at exit. The 100 g case transfers the same ship energy in one hundredth the time, requiring roughly 100 times the mechanical power. Electrical input must also cover losses and module dynamics. [OpenStax: power](https://openstax.org/books/university-physics-volume-1/pages/7-4-power)

### Physics: separate modules and recoil

Assume, without claiming feasibility, a module can push over a 1 km interaction region. At 10 km/s, transit lasts approximately 1,000 / 10,000 = 0.1 s; at 1 g it adds only about 9.81 × 0.1 = 0.98 m/s. Small velocity increments can still imply high acceleration if applied briefly. Coasting gaps add no electromagnetic work; under the common-frame approximation, the active lengths must still sum to the required acceleration distance. Moving modules and gravity require a more complete calculation.

Momentum exchange gives module recoil ΔV = −mΔv/M. A 100-tonne ship receiving 1 m/s transfers 100,000 N·s; a 1,000-tonne module recoils by 0.1 m/s. Across a 10 km/s boost, the ship receives 10⁹ N·s. Each free module must handle its own share; the formation's total mass does not mechanically spread an individual module's recoil. [OpenStax: momentum conservation](https://openstax.org/books/university-physics-volume-1/pages/9-3-conservation-of-linear-momentum)

Recovery propulsion still obeys [canon/laws](../../canon/laws.md) and the rocket equation. Matching incoming and outgoing impulses could reduce recovery demand only where encounter directions, locations, and timing permit; cancellation is not assumed.

### Physics: heat, control, and environment

As an illustrative conversion budget, delivering 5 TJ at 90% electrical-to-mechanical efficiency consumes 5 / 0.9 ≈ 5.56 TJ and leaves about 0.56 TJ of losses to account for. If ultimately rejected as heat over one day, that is 0.56 × 10¹² / 86,400 ≈ 6.4 MW on average, excluding generator losses, refrigeration, and recovery propulsion. Actual loss locations, thermal storage, radiator temperatures, and area are unresolved. Radiative cooling obeys P = εσA(T⁴ − T_env⁴) in the simple enclosure approximation. [OpenStax: heat transfer](https://openstax.org/books/university-physics-volume-2/pages/1-6-mechanisms-of-heat-transfer)

A 15,300 km formation has an end-to-end one-way light time of about 15.3 × 10⁶ / 299,792,458 ≈ 0.051 s. Timing must therefore account for communication delay; local sensing and advance scheduling are candidate controls. The speed of light is exact in SI. [NIST: speed of light](https://physics.nist.gov/cuu/Constants/Value/c.html)

Radiation dose, tidal effects, collision margins, and full route travel times cannot yet be calculated: the Jovian orbit, shielding, formation geometry, and destinations are unspecified. These block location-specific validation.

### Engineering precedents and their limits

A NASA-hosted 1979 report describes construction and initial testing of a 2.5 m electromagnetic mass driver with timed drive coils. This supports the acceleration mechanism, not spacecraft-scale performance. [NASA: mass-driver prototype](https://ntrs.nasa.gov/citations/19800026231)

ESA reports that Proba-3 maintained millimetre-precision formation at 150 m separation for hours. This supports precision formation control, not operation during large accelerator impulses. [ESA: Proba-3 formation flight](https://www.esa.int/articles/proba-3-achieves-precise-formation-flying)

### Consistency and motive

Checked [canon/laws](../../canon/laws.md), [canon/timeline](../../canon/timeline.md), and repository terms for stations, Jupiter, acceleration, and propulsion when recording [sessions/2026-11-18-orbital-acceleration-network](../../sessions/2026-11-18-orbital-acceleration-network.md). No conflicting canon infrastructure exists. Momentum, energy, heat, and light-delay constraints are retained; no new physics is required.

The proposed motive is sharing costly power and propulsion equipment across repeated journeys. Modularity could support incremental investment and maintenance. Whether that outweighs formation control, recovery propellant, and construction costs compared with onboard propulsion is unresolved, so this is a candidate technology rather than an established prediction.

## Consequences

- The [wiki/tech/orbital-transportation-network](./orbital-transportation-network.md) sells trajectory changes subject to vehicle load limits and station availability.
- Compatible ship hardware for electromagnetic coupling is required; its design remains open.
- Passenger service requires enough cumulative interaction distance at acceptable acceleration, even when modules are widely separated.
- Ships and modules need procedures for a missed or failed encounter; these are not yet designed.

## Open questions

- What magnetic coupling and module geometry provide a useful interaction length and force?
- What passenger and cargo load limits, vehicle masses, and velocity changes define the service?
- How are formations scheduled, aligned, reconfigured, and kept safe during module failures?
- What supplies electrical energy, stores launch energy, and rejects heat?
- How do modules restore their orbits, and where do recovery resources originate?
- Which location and routes justify the system, and how do its costs compare with alternatives?

These unresolved checks are tracked in [open-questions](../../open-questions.md).
