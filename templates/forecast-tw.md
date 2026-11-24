---
title: "<主題預測樹名稱>"
id: "<topic-slug>"
period: "<YYYY-MM-DD/YYYY-MM-DD>"
evidence_cutoff: "<YYYY-MM-DD>"
updated: "<YYYY-MM-DD>"
lifecycle: "active"
---

<!-- Authoring guidance: follow ../forecasts/AGENTS.md for tree structure, probabilities, resolution, and revision rules. Keep one thematic tree per file; split a deep subtree into a child file only when this file becomes unwieldy or evolves into an independent theme. Define shared criteria once below rather than repeating boilerplate in every fork. Remove this comment from forecast files. -->

# <主題預測樹名稱>

基準：[forecasts-tw/index](./index.md)

<用 2–3 句說明：這棵預測樹預測什麼、未涵蓋什麼，以及借用了哪些世界觀設定作為假設而非現實觀測。>

## 樹狀總覽

```text
<YYYY> 基準
├── <YYYY> <結果 A> (<條件機率>% | 路徑 <路徑機率>%) [pending]
│   ├── <YYYY> <結果 A1> (<條件機率>% | 路徑 <路徑機率>%) [pending]
│   └── <YYYY> <結果 A2> (<條件機率>% | 路徑 <路徑機率>%) [pending]
└── <YYYY> <結果 B> (<條件機率>% | 路徑 <路徑機率>%) [pending]
```

## 可觀察的里程碑

<說明如何依明訂標準與期限判定結果，並註明證據不足時整組維持 `unresolved`。>

| 代碼 | 判定標準 |
|---|---|
| **<代碼>** | <具體、可觀察的判定標準與所需的運作時間窗。> |

## 分岔

### <YYYY> — <問題標題>

- **前置路徑**：`index`（或 `<parent-outcome-id>`）
- **問題**：<單一互斥且窮盡的問題。>
- **期限**：`<YYYY-MM-DD>` · **證據截點**：`<YYYY-MM-DD>`

| 結果 ID | 結果 | 條件機率 | 路徑機率 | 信心度 | 判定狀態 | 生命週期 |
|---|---|---:|---:|---|---|---|
| `<outcome-a-id>` | <結果 A> | 0% | 0.0% | `low` | `pending` | `active` |
| `<outcome-b-id>` | <結果 B> | 0% | 0.0% | `low` | `pending` | `active` |

- **推論與情境**：
  - **`<outcome-a-id>`**：<新增條件、後果與估計理由。>
  - **`<outcome-b-id>`**：<補集涵蓋範圍與估計理由。>
- **驗證與修訂訊號**：<可觀察的領先指標、相關 [wiki 條目](../wiki-tw/concepts/example.md) 與 [待解問題](../open-questions-tw.md)。>

## 檢查點與修訂訊號

<選用：近期的領先指標與檢視日期，不額外建立帶機率的分岔。>

## 依賴與尚未完成的驗證

<借用的世界觀前提、未作為基準假設的可選機制，以及保留於 [open-questions-tw](../open-questions-tw.md) 的物理或經濟檢查。>

## 修訂紀錄

- `<YYYY-MM-DD>`：<初次建立或重大修訂摘要；退役結果與原因集中記錄於此。>（[session](../sessions/YYYY-MM-DD-topic.md)）
