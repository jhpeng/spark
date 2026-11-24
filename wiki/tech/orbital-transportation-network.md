---
title: Orbital transportation network
kind: tech
era: null
status: draft
grounding: speculative
depends_on:
  - "[canon/laws](../../canon/laws.md)"
  - "[wiki/tech/modular-orbital-accelerator](./modular-orbital-accelerator.md)"
---

# Orbital transportation network

## Summary

A proposed network connects resource extraction, processing, depots, transport vehicles, and reusable acceleration services. Its distinctive component is the [wiki/tech/modular-orbital-accelerator](./modular-orbital-accelerator.md), which supplies velocity changes to passenger and cargo spacecraft while leaving much of the power and recovery machinery at the station.

## Reasoning

### Scope

This is an optional engineering architecture, not shared infrastructure inherited by other futures. A branch using it must explicitly adopt the accelerator and the resource, power, maintenance, and traffic assumptions needed for its routes. Ownership and operating institutions remain open; no particular society or deployment era is defined here.

### Operation and adoption

The user proposes that station modules reconfigure for incoming spacecraft and their requested acceleration. Repeated traffic could spread infrastructure costs across many trips, while local resources could supply station recovery propulsion. Jupiter was the starting example, not a settled first location.

The commercial hypothesis is a service priced around spacecraft mass, required trajectory change, acceleration limits, and scheduling. Regular freight could provide demand alongside passenger services, but no traffic volumes or economic advantage have been demonstrated. Extraction methods, ownership, power sources, and an era remain undecided.

## Validation

### Physics

```spark-visual
{
  "type": "energy-budget",
  "id": "network-power-budget",
  "title": "Departure Kinetic Energy & Daily Power Budget",
  "scale_mode": "schematic",
  "caption": "Schematic interactive calculator (illustrative parameters only): explores E = ½m(Δv)², electrical input at conversion efficiency η, daily mean power P_avg = E/t, and thermal losses.",
  "params": {
    "mass_t": 100,
    "mass_range_t": [20, 500],
    "delta_v_km_s": 10,
    "delta_v_range_km_s": [2, 25],
    "efficiency": 0.9,
    "cadence_per_day": 1
  }
}
```

The station estimates in [wiki/tech/modular-orbital-accelerator](./modular-orbital-accelerator.md) give 5 TJ of ship kinetic energy for a 100-tonne craft boosted from rest to 10 km/s in the station's initial frame. As a bookkeeping example, one such departure per day corresponds to 5 × 10¹² / 86,400 ≈ 58 MW of average useful power, despite gigawatt power during acceleration. Energy storage could separate generation rate from launch rate; its mass and feasibility remain unresolved. This uses P_average = E/t. [OpenStax: power](https://openstax.org/books/university-physics-volume-1/pages/7-4-power)

At the illustrative 90% conversion efficiency, electrical energy per departure is about 5.56 TJ = 1.54 million kWh. If electricity costs p currency units/kWh, that portion of a departure costs 1.54 million × p, before construction, maintenance, recovery, and financing. No electricity price or profitability is assumed.

The network does not eliminate reaction mass or momentum exchange: station modules receive opposite impulses and need recovery. Docking transfers require matching velocity with the depot or tanker; a passing acceleration encounter instead requires a compatible trajectory and precise timing. Gravity, arrival braking, resource transport, communication delay, and radiation shielding must be included in a complete route model. None has yet been selected well enough to calculate end-to-end service.

### Consistency

Checked [canon/laws](../../canon/laws.md), [canon/timeline](../../canon/timeline.md), and related repository terms during [sessions/2026-11-18-orbital-acceleration-network](../../sessions/2026-11-18-orbital-acceleration-network.md). No conflicting canon development exists. No deployment date or new timeline event is proposed. The grounding is speculative because the network depends on an unproven accelerator architecture and an unspecified supporting industrial system.

### Motive

The proposed economic benefit is reuse of heavy equipment across many journeys. Regular customers and reliable resource supply would be needed to justify the investment. Comparison with onboard propulsion, ordinary tugs, and other launch infrastructure remains open; physical possibility alone does not establish adoption.

## Consequences

- Travel becomes dependent on station schedules, compatible vehicle interfaces, and infrastructure availability.
- Resource production, station recovery, and passenger/cargo timetables become coupled operational requirements.
- Incoming traffic might assist momentum or energy recovery, but only after suitable routes and encounter geometry are demonstrated.

## Open questions

- Which locations, destinations, and traffic volumes justify the first service?
- What resource chain supports module recovery and maintenance?
- Which power and energy-storage systems can meet both average and launch demands?
- What service limits and recovery procedures make passenger and cargo operations practical?
- Does the full cost per delivered payload beat competing transport methods?

These unresolved checks are tracked in [open-questions](../../open-questions.md).
