---
title: "以月球為起點的擴張：預測樹"
id: "lunar-expansion"
period: "2026-11-19/3026-12-31"
evidence_cutoff: "2026-11-19"
updated: "2026-11-24"
lifecycle: "active"
---

# 以月球為起點的擴張：預測樹

基準：[forecasts-tw/index](./index.md)

這是依據 repo 現有情境建立的**月球發展子樹**，分別預測共用服務（`S`）、在地耗材（`L`）、家戶居住（`H`）與經驗證的自主維持能力（`I`）。機率並未涵蓋人類所有未來：火星、軌道產業或其他路徑，都可能在不同月球結果下發展。repo 的推論來自 [wiki-tw/concepts/geopolitical-drivers-of-space-expansion](../wiki-tw/concepts/geopolitical-drivers-of-space-expansion.md)、[wiki-tw/concepts/lunar-base-development](../wiki-tw/concepts/lunar-base-development.md) 與 [wiki-tw/concepts/space-expansion-motives](../wiki-tw/concepts/space-expansion-motives.md)。

## 樹狀總覽

括號內為 2026-11-19 證據截點下的 `（條件機率 | 累計路徑機率）`。目前所有葉節點（標註 `*`）合計 100.0%；尚未展開的葉節點表示尚未建模，不代表後續擴張機率為零。下方的 3026 年分支不能用來計算涵蓋全部路徑的月球自主機率，因為較早的若干葉節點尚未展開。

```text
2026 基準 (index)
├── 2036 達成 S：lunar-services-2036 (65% | 路徑 65.0%) [pending]
│   ├── 2076 達成 L：local-consumables-2076 (55% | 路徑 35.8%) [pending]
│   │   ├── 2126 達成 H：local-supply-households-2126 (40% | 路徑 14.3%) [pending]
│   │   │   ├── 3026 達成 I：early-households-independent-3026 (45% | 路徑 6.4%) [pending] *
│   │   │   └── 3026 未達 I：early-households-not-independent-3026 (55% | 路徑 7.9%) [pending] *
│   │   └── 2126 未達 H：local-supply-no-households-2126 (60% | 路徑 21.5%) [pending]
│   │       ├── 3026 達成 I：later-households-independent-3026 (20% | 路徑 4.3%) [pending] *
│   │       └── 3026 未達 I：later-households-not-independent-3026 (80% | 路徑 17.2%) [pending] *
│   └── 2076 未達 L：no-local-consumables-2076 (45% | 路徑 29.3%) [pending]
│       ├── 2126 達成 H：import-path-households-2126 (15% | 路徑 4.4%) [pending] *
│       └── 2126 未達 H：import-path-no-households-2126 (85% | 路徑 24.9%) [pending] *
└── 2036 未達 S：no-lunar-services-2036 (35% | 路徑 35.0%) [pending]
    ├── 2076 較晚達成 S：delayed-lunar-services-2076 (45% | 路徑 15.8%) [pending] *
    └── 2076 仍未達 S：still-no-lunar-services-2076 (55% | 路徑 19.3%) [pending] *
```

## 可觀察的里程碑

以下門檻用來定義預測分類，**不是經驗證的工程規格或最低可存續人口**。每個問題都要求在指定期限仍符合里程碑，並具備所需的先前運作紀錄。較早的里程碑只描述其自身期限的時間窗，不要求在中間數十年或數百年一直成立。所有結果皆依 [forecasts-tw/index](./index.md) 的共用判定原則評估：證據不足時整組維持 `unresolved`，不視為失敗。

| 代碼 | 判定標準 |
|---|---|
| **S — 共用服務** | 至少一套月面服務系統，在最後三個曆年的每一年，為至少兩個各自有經費來源的客戶計畫提供電力、通訊、貨物處理或維修中的至少兩類服務，且到期限時仍運作。不同計畫可以由同一國家資助；同一次任務的兩件儀器不算兩個計畫。無須商業所有權或有人居住。 |
| **L — 在地耗材** | 至少一個月球客戶，在最後三個曆年的每一年，實際使用月球來源的水或氧氣達每年 10 公噸以上，且占自身同種產品總消耗量至少 20%。須一致計算同一產品，不重複計入水及從該水分離的氧。允許進口機械；只有採樣、土方、金屬或對地出口不符合 L。 |
| **H — 家戶居住** | 至少一個月球地點，在最後十年持續住有至少 100 位居民，其中至少 10 個家戶將當地作為主要住所，而非輪班工作地。家戶指至少兩人共同過日常生活；人員可替換，但總數須持續達標。這不代表已驗證生育、兒童健康或自主維持。 |
| **I — 經驗證的自主維持** | 至少一個月球社群，在最後連續 30 年沒有地球物資運補或不可缺少的地球端操作下，仍維持運作。紀錄須顯示在地維持食物、水、空氣、能源、必要藥物與替換設備，經歷實際維修週期，並有當地出生者成長至成年。任何地外供應方也須符合不依賴地球的檢驗，不能把依賴藏在中介供應商之後。只靠庫存不符合。這是有限期間的韌性驗證，不是無限期存續的證明。 |

## 分岔

### 2036 — 共用月面服務（`S`）

- **前置路徑**：`index`（2026 基準）
- **問題**：2034–2036 年間是否達成 **S**（共用月面服務）？
- **期限**：`2036-12-31` · **期間**：`2026-11-20/2036-12-31` · **證據截點**：`2026-11-19`

| 結果 ID | 結果 | 條件機率 | 路徑機率 | 信心度 | 判定狀態 | 生命週期 |
|---|---|---:|---:|---|---|---|
| `lunar-services-2036` | **達成 S** — 共用月面服務運作 | 65% | 65.0% | `low` | `pending` | `active` |
| `no-lunar-services-2036` | **未達 S** — 無符合標準的共用服務 | 35% | 35.0% | `low` | `pending` | `active` |

- **推論與情境**：
  - **`lunar-services-2036`（65%）**：已有明確採購與多項基礎設施計畫，使十年內至少出現一套運作中共用系統的可能性高於完全沒有，但仍為進度延宕、整合、使用權與經費風險保留相當權重。依 [wiki-tw/society/state-funded-space-industry](../wiki-tw/society/state-funded-space-industry.md)，公共科研或戰略採購是可能的早期付費者；商業或混合出資也符合。無須常駐居民、在地生產、對所有國家開放或商業獲利。
  - **`no-lunar-services-2036`（35%）**：探測任務、獨立設施、私人基礎設施與短期造訪仍可發生，這與[以地球為中心的發展](../wiki-tw/concepts/space-expansion-motives.md)相容，只是未達共用服務門檻。公告可能比預算持久，各國計畫可能重複建置而不共用，硬體挫折或重大干擾也可能使三年紀錄無法成立。
- **驗證與修訂訊號**：追蹤重複付費合約、跨計畫使用率、實際供電／通訊表現、停機時間、維修能力與計畫取消。[wiki-tw/concepts/geopolitical-drivers-of-space-expansion](../wiki-tw/concepts/geopolitical-drivers-of-space-expansion.md) 說明政治競爭雖可支撐出資，卻也可能限制使用權；[wiki-tw/concepts/lunar-base-development](../wiki-tw/concepts/lunar-base-development.md) 與 [open-questions-tw](../open-questions-tw.md) 仍保留公共承諾、客戶存取與質量／電力／散熱預算的待解檢查。

---

### 2076 — 早期 `S` 之後的常態在地耗材（`L`）

- **前置路徑**：`index` → `lunar-services-2036`
- **問題**：2074–2076 年間是否達成 **L**（常態使用月球來源水或氧氣）？
- **期限**：`2076-12-31` · **期間**：`2037-01-01/2076-12-31` · **證據截點**：`2026-11-19`

| 結果 ID | 結果 | 條件機率 | 路徑機率 | 信心度 | 判定狀態 | 生命週期 |
|---|---|---:|---:|---|---|---|
| `local-consumables-2076` | **達成 L** — 常態使用在地水／氧氣 | 55% | 35.8% | `very-low` | `pending` | `active` |
| `no-local-consumables-2076` | **未達 L** — 無符合標準的在地耗材 | 45% | 29.3% | `very-low` | `pending` | `active` |

- **推論與情境**：
  - **`local-consumables-2076`（55%）**：明確採用 `lunar-local-supply`：已辨識的客戶重複使用月球水或氧氣。早期服務基地提供客戶與運作經驗，之後四十年也允許反覆試驗。允許進口機械與公共採購；此里程碑不證明商業競爭力、完整製造鏈或對地出口。
  - **`no-local-consumables-2076`（45%）**：反映萃取不可靠、礦源貧乏、使用率低、合約過短或地球低成本補給占優勢等可能。既有服務可能持續靠進口運作、規模縮小或萎縮；土方、金屬加工或小型試驗皆可存在而不符合 `L`。對 2076 年後的在地生產不做定論。
- **驗證與修訂訊號**：[wiki-tw/tech/lunar-resource-utilization](../wiki-tw/tech/lunar-resource-utilization.md) 要求實測原料、回收率、電力、散熱、耗材、維修與實際採用產量（其假想 `1/(0.05×0.8) = 25` 公噸原料產 1 公噸水僅為質量平衡）。合約須來自獨立用途，而非供應商循環自購。比較實際年交付量與進口成本；追蹤 [open-questions-tw](../open-questions-tw.md) 中的選址／製程與地外客戶問題。

---

### 2076 — 2036 年未達 `S` 之後的延後共用服務（`S`）

- **前置路徑**：`index` → `no-lunar-services-2036`
- **問題**：錯過 2036 年里程碑後，2074–2076 年間是否達成 **S**？
- **期限**：`2076-12-31` · **期間**：`2037-01-01/2076-12-31` · **證據截點**：`2026-11-19`

| 結果 ID | 結果 | 條件機率 | 路徑機率 | 信心度 | 判定狀態 | 生命週期 |
|---|---|---:|---:|---|---|---|
| `delayed-lunar-services-2076` | **較晚達成 S** — 延後建立共用服務（葉節點） | 45% | 15.8% | `very-low` | `pending` | `active` |
| `still-no-lunar-services-2076` | **仍未達 S** — 仍無符合標準的共用服務（葉節點） | 55% | 19.3% | `very-low` | `pending` | `active` |

- **推論與情境**：
  - **`delayed-lunar-services-2076`（45%）**：多出的四十年讓計畫有機會從進度延宕中恢復，透過新一輪經費週期、提升交付可靠度或建立相容客戶計畫達成 `S`。這是不同於早期服務的歷史路徑，不與 `lunar-services-2036` 合併。
  - **`still-no-lunar-services-2076`（55%）**：略微偏向早期失敗後仍有結構性阻礙：地球替代方案可能持續足夠、獨立客戶未能成形，或使用權仍碎片化。涵蓋間歇任務、單一計畫基地、縮編或重大中斷（不預設中斷為預期原因），亦不排除軌道或火星活動成功。
- **驗證與修訂訊號**：觀察是否出現新出資的獨立客戶、多年運作紀錄、系統相容性，以及先前失敗原因是否已修正。[wiki-tw/society/state-funded-space-industry](../wiki-tw/society/state-funded-space-industry.md)、[wiki-tw/concepts/geopolitical-drivers-of-space-expansion](../wiki-tw/concepts/geopolitical-drivers-of-space-expansion.md)、[wiki-tw/concepts/lunar-base-development](../wiki-tw/concepts/lunar-base-development.md) 與 [wiki-tw/concepts/space-expansion-motives](../wiki-tw/concepts/space-expansion-motives.md) 提供可能機制與地球中心替代路徑；良好科研成果可與 `S` 未達並存。

---

### 2126 — 早期 `S` 與 `L` 之後的家戶居住（`H`）

- **前置路徑**：`index` → `lunar-services-2036` → `local-consumables-2076`
- **問題**：2117–2126 年間是否達成 **H**（持續的月球家戶居住）？
- **期限**：`2126-12-31` · **期間**：`2077-01-01/2126-12-31` · **證據截點**：`2026-11-19`

| 結果 ID | 結果 | 條件機率 | 路徑機率 | 信心度 | 判定狀態 | 生命週期 |
|---|---|---:|---:|---|---|---|
| `local-supply-households-2126` | **達成 H** — 在地供應後的家戶居住 | 40% | 14.3% | `very-low` | `pending` | `active` |
| `local-supply-no-households-2126` | **未達 H** — 在地供應路徑但未達家戶門檻 | 60% | 21.5% | `very-low` | `pending` | `active` |

- **推論與情境**：
  - **`local-supply-households-2126`（40%）**：早期服務與耗材降低部分補給門檻，但本身不會自動產生舉家遷居的動機。明確加入居住動機（就業、社群自治、公共韌性支出或混合因素，不假設特定合約或政體）。100 人門檻只是分類邊界，不是可存續人口結論。
  - **`local-supply-no-households-2126`（60%）**：反映工業用途與家庭移居偏好之間的落差。自動化與輪班人力可在極少居民下維持產出，而健康、費用、住房、權利或撤資都可能阻礙 `H`。此結果與技術成功相容，不必然代表工業失敗，也不排除更晚出現居住社群。
- **驗證與修訂訊號**：[wiki-tw/society/community-led-settlement](../wiki-tw/society/community-led-settlement.md) 與 [wiki-tw/society/migration-contracts-and-resident-rights](../wiki-tw/society/migration-contracts-and-resident-rights.md) 要求有資金支撐的生活成本、權利、醫療與可行退場機制。[wiki-tw/concepts/ai-driven-industrial-demand](../wiki-tw/concepts/ai-driven-industrial-demand.md) 僅將自動化視為可選產出助力，而非移居證明。須將居住紀錄與工作崗位分開查核；輻射、低重力健康、食物、維修與贊助方撤出後的延續性仍保留於 [open-questions-tw](../open-questions-tw.md)。

---

### 2126 — 早期 `S` 但 2076 年未達 `L` 之後的家戶居住（`H`）

- **前置路徑**：`index` → `lunar-services-2036` → `no-local-consumables-2076`
- **問題**：即使未達 2076 年耗材里程碑，2117–2126 年間是否達成 **H**？
- **期限**：`2126-12-31` · **期間**：`2077-01-01/2126-12-31` · **證據截點**：`2026-11-19`

| 結果 ID | 結果 | 條件機率 | 路徑機率 | 信心度 | 判定狀態 | 生命週期 |
|---|---|---:|---:|---|---|---|
| `import-path-households-2126` | **達成 H** — 未達 L 後仍達成家戶居住（葉節點） | 15% | 4.4% | `very-low` | `pending` | `active` |
| `import-path-no-households-2126` | **未達 H** — 未達 L 後亦未達家戶門檻（葉節點） | 85% | 24.9% | `very-low` | `pending` | `active` |

- **推論與情境**：
  - **`import-path-households-2126`（15%）**：為高度有意願且資金充足的家戶保留路徑，可由進口、補貼、社群財富或 2076 年後補上的在地生產支撐（「進口路徑」僅標示先前歷史，不強制永久依賴進口）。權重低於在地供應路徑反映已驗證的促成條件較少，而非物理定律或因果效應估計。
  - **`import-path-no-households-2126`（85%）**：反映這條歷史上累積的經費、健康、補給與居住偏好阻礙，屬於寬廣補集，而非預測 85% 會廢棄或文明衰退。月球仍可能保留科研、機器人活動、輪班人員、小型社群或 2076 年後的在地生產。
- **驗證與修訂訊號**：依實際 `H` 居住紀錄判定，不可因缺乏在地氧氣就直接推論沒有家戶。[wiki-tw/society/community-led-settlement](../wiki-tw/society/community-led-settlement.md)、[wiki-tw/society/migration-contracts-and-resident-rights](../wiki-tw/society/migration-contracts-and-resident-rights.md)、[wiki-tw/concepts/lunar-base-development](../wiki-tw/concepts/lunar-base-development.md) 與 [wiki-tw/concepts/space-expansion-motives](../wiki-tw/concepts/space-expansion-motives.md) 界定居住動機、可執行補給／退場條款與地球中心選項。不假設對地出口產業、廉價軌道運輸或無限期維生系統。

---

### 3026 — 早期 `S`、`L` 與 `H` 之後的自主維持（`I`）

- **前置路徑**：`index` → `lunar-services-2036` → `local-consumables-2076` → `local-supply-households-2126`
- **問題**：2997–3026 年間是否達成 **I**（有限期間的經驗證月球自主維持）？
- **期限**：`3026-12-31` · **期間**：`2127-01-01/3026-12-31` · **證據截點**：`2026-11-19`

| 結果 ID | 結果 | 條件機率 | 路徑機率 | 信心度 | 判定狀態 | 生命週期 |
|---|---|---:|---:|---|---|---|
| `early-households-independent-3026` | **達成 I** — 早期家戶後達成自主維持（葉節點） | 45% | 6.4% | `very-low` | `pending` | `active` |
| `early-households-not-independent-3026` | **未達 I** — 早期家戶後未達自主維持（葉節點） | 55% | 7.9% | `very-low` | `pending` | `active` |

- **推論與情境**：
  - **`early-households-independent-3026`（45%）**：套用 `civilization-backup` 能力檢驗，不論動機為何（刻意為備援出資只是選項之一）。九個世紀加上先前家戶與生產基礎允許大量學習；早期社群可變遷、遷移或由後續符合標準的月球社群接續。這不主張無限期存續、大規模移民或星際擴張。
  - **`early-households-not-independent-3026`（55%）**：略偏向至少一項關鍵依賴持續存在，或未能通過連續 30 年檢驗。涵蓋繁榮但依賴地球的聚落、選擇分工貿易的社群、製造瓶頸、健康限制、人口縮小或月球居住中斷。未達 `I` 不等於滅絕，也允許月球以外的地外文明。
- **驗證與修訂訊號**：查核食物與養分閉環、替換工具與零件、必要藥物、能源／散熱預算，以及出生至成年的健康紀錄；僅靠庫存無法通過 `I`。若未通過，須辨識具體失敗條件。[wiki-tw/concepts/space-expansion-motives](../wiki-tw/concepts/space-expansion-motives.md) 與 [wiki-tw/society/community-led-settlement](../wiki-tw/society/community-led-settlement.md) 區分備援能力與自治動機。無須加速器或未知物理；各項關鍵預算仍列於 [open-questions-tw](../open-questions-tw.md)。

---

### 3026 — 早期 `S` 與 `L` 但 2126 年未達 `H` 之後的自主維持（`I`）

- **前置路徑**：`index` → `lunar-services-2036` → `local-consumables-2076` → `local-supply-no-households-2126`
- **問題**：2126 年未達家戶門檻後，2997–3026 年間是否達成 **I**？
- **期限**：`3026-12-31` · **期間**：`2127-01-01/3026-12-31` · **證據截點**：`2026-11-19`

| 結果 ID | 結果 | 條件機率 | 路徑機率 | 信心度 | 判定狀態 | 生命週期 |
|---|---|---:|---:|---|---|---|
| `later-households-independent-3026` | **後來達成 I** — 未達早期 H 後達成自主維持（葉節點） | 20% | 4.3% | `very-low` | `pending` | `active` |
| `later-households-not-independent-3026` | **未達 I** — 未達早期 H 後仍未自主維持（葉節點） | 80% | 17.2% | `very-low` | `pending` | `active` |

- **推論與情境**：
  - **`later-households-independent-3026`（20%）**：在九個世紀的尺度下保留明顯的晚起步可能，動機、技術與居住型態皆可演變。權重低於早期家戶路徑反映尚待完成的轉折更多，不表示錯過 2126 年就會在物理上封死定居。套用 `civilization-backup` 能力檢驗，不論動機；早期機器人生產本身不自動帶來居住或自主。
  - **`later-households-not-independent-3026`（80%）**：合併「居住始終未達標」與「後來形成家戶但未達工業與生物自主」兩種可能（不要求 2127–3026 年間一直沒有家戶）。涵蓋仍依賴地球的晚期聚落、機器人／輪班運作與廢棄，不是預測 80% 會發生災難、停滯或完全沒有太空文明。
- **驗證與修訂訊號**：追蹤後續家戶建立與留存率、必要進口庫存、實際零件替換與食物生產、人類生命週期健康，以及經查核的 30 年運作紀錄。[wiki-tw/society/community-led-settlement](../wiki-tw/society/community-led-settlement.md)、[wiki-tw/concepts/lunar-base-development](../wiki-tw/concepts/lunar-base-development.md) 與 [wiki-tw/concepts/space-expansion-motives](../wiki-tw/concepts/space-expansion-motives.md) 區分有用產業、定居動機、地球中心發展與備援檢驗。

## 2031 年檢查點與修訂訊號

至 **2031-12-31**，檢查實際交付、重複付費合約、跨計畫使用電力或通訊的情形、解約條款、設備故障與維修，以及可取得的資源調查。這些是五年尺度的領先指標，不是另一組帶機率的分岔。重複交付與多年使用會提高 `lunar-services-2036` 的估計；取消計畫、互不相容的獨立任務或反覆故障會降低估計。單純公告的影響應小於經驗證的服務表現。更新時一起重估受影響的同組分支與後續節點，不預設新證據一定會減少不確定性。

## 依賴與尚未完成的驗證

- **可選的需求機制**（不是無限消費、全球限制或地球無法居住的基準假設）：[wiki-tw/concepts/ai-driven-industrial-demand](../wiki-tw/concepts/ai-driven-industrial-demand.md)、[wiki-tw/concepts/earth-development-limits](../wiki-tw/concepts/earth-development-limits.md) 與 [wiki-tw/concepts/climate-adaptation-pressure](../wiki-tw/concepts/climate-adaptation-pressure.md)。
- **可選、尚未驗證的應用**（不假設便宜的對地出口或模組化加速器，也不依賴核融合、心智上傳、未知物理，且未選定地緣政治贏家或軍事工業分支）：[wiki-tw/tech/orbital-data-centers](../wiki-tw/tech/orbital-data-centers.md)、[wiki-tw/concepts/lunar-earth-cargo](../wiki-tw/concepts/lunar-earth-cargo.md) 與 [wiki-tw/tech/orbital-transportation-network](../wiki-tw/tech/orbital-transportation-network.md)。
- **物理與待解檢查**：物理檢查僅能在原本假設內沿用（例如月球基地條目的假想進口質量抵銷計算 `30/(10−2) = 3.75` 年，不能證明財務回本或設備壽命）。這裡尚未完成整體生產、輻射、散熱、食物、製造或運輸預算；相關檢查保留於 [open-questions-tw](../open-questions-tw.md)。[canon/laws-tw](../canon/laws-tw.md) 與 [canon/timeline-tw](../canon/timeline-tw.md) 並無被本樹更改的已核准未來工業順序。

## 修訂紀錄

- `2026-11-24`：依新版預測樹規則，將原本 14 份獨立結果節點檔整合為本主題預測樹檔案（`forecasts-tw/lunar-expansion.md`）；完整保留所有結果 ID、條件機率、判定標準、證據截點（`2026-11-19`）與推論依據。
- `2026-11-19`：初次建立以月球為起點的預測樹（[sessions/2026-11-19-initial-forecast-tree](../sessions/2026-11-19-initial-forecast-tree.md)）。
