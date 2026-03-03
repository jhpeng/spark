# Agent Instructions

Any agent must read this file before making changes in this repository.

## Repository Goal

Store knowledge in a structured, efficient format and retrieve it quickly.

## Core Concepts

- **Knowledge Unit**: A single note, fact, or concept.
- **Metadata**: Fields used for filtering and indexing.
- **Index**: Lookup data used to find knowledge units fast.

## Knowledge Storage Rules

1. Store each knowledge unit in a separate file.
2. Keep each file atomic: one primary idea per file.
3. Use consistent front matter metadata.
4. Add relevant tags for discoverability.
5. Update index data when adding or modifying knowledge.

### Standard Knowledge File Template

```md
---
id: unique-id
title: Short title
tags: [topic-a, topic-b]
source: URL or reference
created_at: YYYY-MM-DD
updated_at: YYYY-MM-DD
---

## Summary
One-paragraph summary.

## Details
Main knowledge content.

## Related
- related-id-1
- related-id-2
```

## Search Process

1. Filter by metadata (`tags`, `source`, date range).
2. Search titles and summaries with keyword or phrase matching.
3. Rank by relevance:
   - exact match
   - partial match
   - related tags
4. Run full-content search only when necessary.
5. Follow `Related` links to expand context.

## Suggested Repository Layout

```text
.
├── README.md
├── AGENTS.md
├── knowledge/
│   ├── topic-a/
│   └── topic-b/
└── index/
    ├── tags.json
    └── ids.json
```

## Maintenance

- Keep metadata schema stable.
- Prefer additive updates to avoid breaking search/index tools.
- Ensure new knowledge is indexed before considering the update complete.
