---
title: "<Topic forecast tree>"
id: "<topic-slug>"
period: "<YYYY-MM-DD/YYYY-MM-DD>"
evidence_cutoff: "<YYYY-MM-DD>"
updated: "<YYYY-MM-DD>"
lifecycle: "active"
---

<!-- Authoring guidance: follow ../forecasts/AGENTS.md for tree structure, rolling 100-year tiered horizon cadence (Y0+1..+5 annual, Y0+10..+25 every 5 yr, Y0+25..+100 every 25 yr; capped at Y0+100 and rolled forward annually), probabilities, resolution, and revision rules. Keep one thematic tree per file; split a deep subtree into a child file only when this file becomes unwieldy or evolves into an independent theme. Define shared criteria once below rather than repeating boilerplate in every fork. Remove this comment from forecast files. -->

# <Topic forecast tree>

Baseline: [forecasts/index](./index.md)

<2–3 sentences: what this tree forecasts, what it leaves out, and which worldbuilding premises are borrowed as assumptions rather than observations.>

## Tree overview

```text
<YYYY> baseline (index)
├── <YYYY> · <Event A achieved>: <outcome-a-id> (<cond>% | path <path>%) [pending]
│   ├── <YYYY> · <Downstream event A1>: <outcome-a1-id> (<cond>% | path <path>%) [pending] *
│   └── <YYYY> · <Downstream event A2 not met>: <outcome-a2-id> (<cond>% | path <path>%) [pending] *
└── <YYYY> · <Event A not achieved>: <outcome-b-id> (<cond>% | path <path>%) [pending] *
```

## Observable milestones

<State how outcomes are evaluated against stated criteria and deadlines, and note that missing evidence leaves a pair `unresolved`. Use plain-language milestone names rather than single-letter codes.>

| Milestone | Criterion |
|---|---|
| **<Plain-language milestone name>** | <Concrete, observable criterion and required operating window.> |

## Forks

### <YYYY> — <Plain-language event or milestone title>

- **Inherited path**: `index` (or `<parent-outcome-id>`)
- **Question**: <Single mutually exclusive, collectively exhaustive question in plain language.>
- **Deadline**: `<YYYY-MM-DD>` · **Evidence cutoff**: `<YYYY-MM-DD>`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `<outcome-a-id>` | <Plain-language event achieved> | 0% | 0.0% | `low` | `pending` | `active` |
| `<outcome-b-id>` | <Plain-language event not achieved> | 0% | 0.0% | `low` | `pending` | `active` |

- **Rationale & scenarios**:
  - **`<outcome-a-id>`**: <Added conditions, consequences, and estimation rationale.>
  - **`<outcome-b-id>`**: <Complement scope and estimation rationale.>
- **Validation & revision signals**: <Observable leading indicators, linked [wiki entries](../wiki/concepts/example.md), and relevant [open questions](../open-questions.md).>

## Checkpoints and revision triggers

<Optional near-term leading indicators and review dates without adding an extra probability-bearing fork.>

## Dependencies and unresolved validation

<Borrowed worldbuilding premises, optional mechanisms not assumed as baseline, and unresolved physical/economic checks in [open-questions](../open-questions.md).>

## Revision history

- `<YYYY-MM-DD>`: <Summary of creation or material revision; record retired outcomes here with reasons.> ([session](../sessions/YYYY-MM-DD-topic.md))
