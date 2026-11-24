---
title: "<Topic forecast tree>"
id: "<topic-slug>"
period: "<YYYY-MM-DD/YYYY-MM-DD>"
evidence_cutoff: "<YYYY-MM-DD>"
updated: "<YYYY-MM-DD>"
lifecycle: "active"
---

<!-- Authoring guidance: follow ../forecasts/AGENTS.md for tree structure, probabilities, resolution, and revision rules. Keep one thematic tree per file; split a deep subtree into a child file only when this file becomes unwieldy or evolves into an independent theme. Define shared criteria once below rather than repeating boilerplate in every fork. Remove this comment from forecast files. -->

# <Topic forecast tree>

Baseline: [forecasts/index](./index.md)

<2–3 sentences: what this tree forecasts, what it leaves out, and which worldbuilding premises are borrowed as assumptions rather than observations.>

## Tree overview

```text
<YYYY> baseline
├── <YYYY> <Outcome A> (<cond>% | path <path>%) [pending]
│   ├── <YYYY> <Outcome A1> (<cond>% | path <path>%) [pending]
│   └── <YYYY> <Outcome A2> (<cond>% | path <path>%) [pending]
└── <YYYY> <Outcome B> (<cond>% | path <path>%) [pending]
```

## Observable milestones

<State how outcomes are evaluated against stated criteria and deadlines, and note that missing evidence leaves a pair `unresolved`.>

| Code | Criterion |
|---|---|
| **<Code>** | <Concrete, observable criterion and required operating window.> |

## Forks

### <YYYY> — <Question title>

- **Inherited path**: `index` (or `<parent-outcome-id>`)
- **Question**: <Single mutually exclusive, collectively exhaustive question.>
- **Deadline**: `<YYYY-MM-DD>` · **Evidence cutoff**: `<YYYY-MM-DD>`

| Outcome ID | Outcome | Cond. prob. | Path prob. | Confidence | Resolution | Lifecycle |
|---|---|---:|---:|---|---|---|
| `<outcome-a-id>` | <Outcome A> | 0% | 0.0% | `low` | `pending` | `active` |
| `<outcome-b-id>` | <Outcome B> | 0% | 0.0% | `low` | `pending` | `active` |

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
