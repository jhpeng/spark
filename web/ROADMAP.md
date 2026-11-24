# Spark 網頁化開發藍圖（Web Presentation Roadmap）

> **適用分支**：`web-portal`（未來成熟後併入 `main`）  
> **目標讀者**：專案維護者與所有後續接手的 AI Agents  
> **最高原則**：保留現有 Markdown 作為「單一真相來源（Single Source of Truth）」，透過固定的設計系統、確定性建置管線與宣告式視覺元件，確保跨 Agent、跨 Model 的網頁風格 100% 一致。

---

## 1. 技術與視覺定案（Architecture & Design Decisions）

所有後續實作必須遵守以下定案，未經專案維護者明確同意不得更換：

1. **單一真相來源（Single Source of Truth）**
   - 所有世界觀、物理驗證、預測樹、故事、討論紀錄與待解問題，皆持續維護於既有 Markdown 目錄（`canon/`、`wiki/`、`wiki-tw/`、`forecasts/`、`forecasts-tw/`、`stories/`、`stories-tw/`、`sessions/`、`open-questions*.md`）。
   - 網頁層（`web/`）只負責讀取 Markdown 與結構化資料並建置靜態網站至 `dist/`。**禁止任何 Agent 直接手改 `dist/` 產物。**
2. **技術路線（方案 A：Python 零依賴靜態建置器）**
   - 建置工具：`Python 3` 標準函式庫（可選極少數純 Python 解析依賴，但**不引入 Node.js / npm / React / Tailwind 等重型前端框架**），確保環境零依賴漂移、極易被不同模型理解與維護。
   - 前端技術：語意化 HTML5 + 集中式 CSS Design Tokens（`web/tokens.css`）+ 原生 ES Modules JS + SVG / Canvas 視覺化引擎。
   - 數學公式：KaTeX（用於呈現 `## Validation / 驗證` 中的物理公式與質量／能量平衡計算）。
3. **視覺路線（天文台編輯美學 — Editorial Observatory）**
   - **預設深色主題（Obsidian & Warm Starlight）**：中性深碳黑底色搭配暖白紙墨文字、太陽琥珀金作為主視覺與活躍路徑強調色；標題採襯線編輯字體（`Newsreader` / `Noto Serif TC`）搭配高可讀性無襯線長文字體與等寬數據字體，去除廉價深藍格線與早期 AI 後台感。
   - **可切換淺色主題（Archival Paper）**：溫暖典藏紙白底色搭配深炭墨與古銅金強調色，全由 CSS Variables 驅動。
   - **預測樹強制採互動心智圖（Interactive Mind-Map）**：以平滑貝茲曲線（線寬對應累計路徑機率）搭配可點擊高亮路徑的節點卡片與即時檢視器呈現，禁止以純文字 ASCII 樹顯示。
4. **跨 Agent 一致性護欄**
   - 規則權威：`web/AGENTS.md`（英文撰寫，符合 [templates/AGENTS.md](../templates/AGENTS.md) 規範，並於根目錄 [AGENTS.md](../AGENTS.md) 註冊）。
   - 強制驗證：`web/check.py` 作為所有變更的必過關卡（檢查連結、雙語同步、Token 違規、元件 Schema、圖說與比例標註）。

---

## 2. 目標目錄結構（Target Layout）

```text
spark/
├── AGENTS.md                  # 根目錄規則索引（新增 web/AGENTS.md 入口）
├── assets/
│   └── media/                 # 受風格規範管制的靜態插圖與技術圖表（依 slug 分資料夾）
│       └── <slug>/
├── web/
│   ├── ROADMAP.md             # 本文件：分階段開發藍圖與進度追蹤
│   ├── AGENTS.md              # 網頁呈現與視覺一致性權威規則（英文）
│   ├── COMPONENTS.md          # 核准元件、版型與宣告式動畫白名單及 JSON Schema
│   ├── tokens.css             # 全站唯一 Design Tokens（色彩、字體、間距、狀態色）
│   ├── styles/                # 模組化樣式（layout.css, prose.css, science.css, components.css）
│   ├── templates/             # 6 種標準頁面版型（Page Archetypes）
│   ├── i18n/
│   │   ├── en.json            # 英文 UI 字串
│   │   └── zh-tw.json         # 台灣繁體中文 UI 字串
│   ├── js/
│   │   ├── app.js             # 導覽、雙語切換、TOC 高亮、主題控制
│   │   ├── search.js          # 全站離線搜尋
│   │   ├── forecast-tree.js   # 互動式預測樹引擎
│   │   ├── knowledge-graph.js # 全站依賴與分支知識圖譜
│   │   └── animations/        # 宣告式物理／工程動畫引擎集合
│   ├── build.py               # 確定性靜態網站建置腳本（輸出至 dist/）
│   └── check.py               # 自動化一致性與品質驗證腳本
└── dist/                      # 建置產物（列入 .gitignore，可直接部署 GitHub Pages）
```

---

## 3. 分階段執行藍圖（Phased Execution Plan）

後續 Agent 請依序推進各階段。每完成一個階段，必須執行驗收條件並更新本文件的勾選狀態。

### Phase 1：治理規範與設計系統基礎（Governance & Design System）
- **狀態**：`[x] 已完成`
- **目標**：在寫任何頁面程式之前，先把規則、設計變數與版型契約鎖定，讓所有後續工作有唯一標準可循。
- **交付物**：
  1. `web/AGENTS.md`（英文權威規則）：明定 Single Source of Truth、Design Tokens 使用規範、禁止事項（禁止手改 `dist/`、禁止硬編碼色碼與 inline style、禁止私自發明版型）、雙語同步要求、插圖標註規範、提交前必跑驗證指令。
  2. 更新根目錄 [AGENTS.md](../AGENTS.md)，在規則索引表加入 `web/AGENTS.md`。
  3. `web/tokens.css`：完整定義「深色航太技術藍圖風」的設計變數：
     - 表面層級（背景、卡片、側欄、程式碼／公式區塊、格線色）
     - 文字層級（主文、次要說明、等寬數據、超連結）
     - 語意狀態色：`status`（`canon` / `draft` / `retconned`）、`grounding`（`established` / `plausible` / `speculative`）、`resolution`（`pending` / `occurred` / `not-occurred` / `unresolved`）
     - 字體階層、行高、最大閱讀寬度（適合長文閱讀）、間距刻度、圓角與邊框。
  4. `web/COMPONENTS.md`：定義 6 種標準頁面版型（首頁總覽、Wiki 條目頁、預測樹頁、正史與時間軸頁、故事頁、待解問題／討論紀錄頁）與元件白名單契約。
  5. `web/i18n/en.json` 與 `web/i18n/zh-tw.json` 基礎介面字典。
  6. 更新 `.gitignore`，排除 `dist/` 與 Python 快取檔。
- **Agent 護欄**：不可在此階段引入外部前端框架或寫死頁面內容；所有視覺數值都必須抽象成 CSS Custom Properties。
- **驗收條件**：
  - `AGENTS.md` 正確連結至 `web/AGENTS.md`。
  - `web/tokens.css` 涵蓋所有 Spark 狀態值與雙語長文排版變數。
  - `web/i18n/en.json` 與 `web/i18n/zh-tw.json` 鍵值 100% 一致。

---

### Phase 2：確定性建置管線與核心長文閱讀器（Deterministic SSG & Long-form Reader）
- **狀態**：`[x] 已完成`
- **目標**：將目前 repo 內所有雙語 Markdown 完整編譯為可瀏覽、可搜尋、架構清晰的三欄式靜態網站。
- **交付物**：
  1. `web/build.py`：
     - 解析 YAML frontmatter 與 Markdown 內文（支援標題、表格、清單、程式碼區塊、引用、註腳）。
     - 自動轉換相對 `.md` 內部連結為正確的靜態網頁路由（保留錨點）。
     - 自動建立 `depends_on` 依賴關係與全站反向連結（Backlinks）。
     - 自動配對雙語版本（如 `wiki/...` ↔ `wiki-tw/...`、`canon/laws.md` ↔ `canon/laws-tw.md`）。
     - 產生離線搜尋索引 `dist/search-index-en.json` 與 `dist/search-index-zh-tw.json`。
  2. `web/templates/` 與 `web/styles/`：實作 6 種標準版型與三欄式閱讀架構：
     - **左欄**：可摺疊分類導覽樹（Canon / Forecasts / Wiki 5 大類 / Stories / Open Questions / Sessions）+ 狀態篩選。
     - **中欄**：條目標頭 Metadata 卡片 + 結構化長文內容 + 上一篇／下一篇或相關條目。
     - **右欄**：頁內目錄（Sticky TOC）+ 依賴條目（`depends_on`）+ 反向引用（Backlinks）。
  3. `web/js/app.js` 與 `web/js/search.js`：繁中／EN 同頁面切換、鍵盤快捷搜尋（`/` 或 `Cmd/Ctrl+K`）、行動裝置響應式側欄。
- **Agent 護欄**：所有頁面必須由 `web/build.py` 統一套版生成；不允許為單一 Markdown 檔案客製獨立 HTML。
- **驗收條件**：
  - 執行 `python3 web/build.py` 零錯誤產出 `dist/`。
  - 現有所有英文與繁中檔案皆可正確瀏覽、無斷鏈、雙語切換對應正確。
  - 以 `python3 -m http.server -d dist` 本機開啟後，三欄版型與搜尋運作正常。

---

### Phase 3：科學證據、推論結構與公式呈現（Scientific Evidence & Reasoning UI）
- **狀態**：`[x] 已完成`
- **目標**：讓 Spark 最核心的價值——物理驗證、估算過程、來源引用、分支前提與待解檢查——在網頁上具備極高可讀性與可追溯性。
- **交付物**：
  1. **科學驗證專區渲染（`web/styles/science.css` + `build.py` 區塊辨識）**：
     - 自動辨識 `## Validation` / `## 驗證` 下的三個標準子區（`Physics / 物理`、`Consistency / 一致性`、`Motive / 動機`），渲染為帶圖示與語意邊框的結構化驗證卡片。
     - 自動彙整文內外部來源連結（NASA / ESA / OpenStax / 論文）為清晰的引用清單。
     - 標記「假設前提（Scope / Assumptions）」與「待解問題（Open Questions）」區塊，並提供直接跳轉至全站待解清單對應項目的錨點。
  2. **數學公式支援**：整合 KaTeX 渲染行內與區塊公式，確保能量、動量、質量平衡與機率公式以學術級排版顯示。
  3. **正史與時間軸視圖**：針對 `canon/laws*.md` 呈現定律編號卡片；針對 `canon/timeline*.md` 呈現可依「共用前提 / 特定分支」篩選的結構化時間軸。
- **Agent 護欄**：不得改寫或刪減原始 Markdown 的任何科學論述或計算細節；強化呈現只能基於既有標準章節名稱與語意規則。
- **驗收條件**：
  - [orbital-transportation-network.md](../wiki-tw/tech/orbital-transportation-network.md) 與 [lunar-resource-utilization.md](../wiki-tw/tech/lunar-resource-utilization.md) 的物理估算、公式與來源引用清晰呈現。
  - `canon/laws*.md` 與 `canon/timeline*.md` 均能正確套用專屬結構化視圖。

---

### Phase 4：互動式預測樹與全站知識圖譜（Interactive Forecast Trees & Knowledge Graph）
- **狀態**：`[x] 已完成`
- **目標**：將純文字的條件機率預測樹與跨條目依賴網，升級為可探索、可篩選的資料驅動視覺化介面。
- **交付物**：
  1. **互動式預測樹引擎（`web/js/forecast-tree.js`）**：
     - 由 `web/build.py` 解析 `forecasts/*.md` 與 `forecasts-tw/*.md` 中的樹狀結構、里程碑定義、各分岔表格（條件機率、累計路徑機率、信心度、判定狀態、生命週期）與推論文字，輸出結構化 JSON。
     - 前端渲染可縮放／拖曳的互動節點樹：點擊任一結果節點即可高亮「從基準線到該節點的完整繼承路徑」，並在詳情面板顯示該分岔的推論、驗證與修訂訊號。
     - 支援顯示累計路徑機率總和校驗、篩選 `pending / occurred / not-occurred / unresolved`。
  2. **全站知識依賴圖譜（`web/js/knowledge-graph.js`）**：
     - 讀取建置期輸出的 `graph.json`，視覺化呈現 `canon`、`wiki`（依 `kind` 分色）、`forecasts` 與 `stories` 之間的 `depends_on` 與引用關係。
     - 支援依分類、`status`、`grounding` 過濾，點選節點可預覽摘要並跳轉條目。
- **Agent 護欄**：視覺化顏色與字體必須透過 `getComputedStyle` 讀取 `web/tokens.css` 變數，確保主題一致。
- **驗收條件**：
  - [forecasts-tw/lunar-expansion.md](../forecasts-tw/lunar-expansion.md) 與英文版皆完整呈現為互動預測樹，且所有機率數字與原 Markdown 100% 吻合。
  - 全站知識圖譜正確顯示所有現有條目與依賴連線。

---

### Phase 5：宣告式物理動畫引擎與靜態插圖規範（Declarative Animations & Media）
- **狀態**：`[x] 已完成`
- **目標**：在不犧牲跨 Agent 一致性的前提下，為複雜的物理概念與工程架構提供直覺的動畫與圖表。
- **交付物**：
  1. **宣告式視覺區塊語法（```` ```spark-visual ````）**：
     - 在 Markdown 中透過 JSON 區塊宣告動畫類型、物理參數、雙語標籤與比例說明（`scale_mode: "schematic" | "to-scale"`）。
     - 在 `web/COMPONENTS.md` 註冊完整 Schema，禁止 Agent 在文章中直接插入 `<script>` 或自訂 Canvas 程式碼。
  2. **首批標準物理動畫引擎（`web/js/animations/`）**：
     - `orbital-transfer`：軌道加速、動量反衝與軌跡轉移示意（具播放／暫停／重播控制列）。
     - `energy-budget`：功率、儲能與發射頻率互動計算視覺化（具參數滑桿，即時連動顯示物理公式結果，如 $E = \frac{1}{2}mv^2$ 與 $P_{\text{avg}} = E/t$）。
     - `phase-progression`：太空基礎設施階段演進（如月球 `S → L → H → I` 里程碑演化）。
  3. **示範套用**：於 [modular-orbital-accelerator.md](../wiki-tw/tech/modular-orbital-accelerator.md)、[orbital-transportation-network.md](../wiki-tw/tech/orbital-transportation-network.md)（含英文對應檔）加入首批示範動畫。
  4. **靜態插圖與技術圖表規範**：於 `web/AGENTS.md` 補齊 `assets/media/<slug>/` 命名規則、統一風格指南、必填雙語圖說與 `alt` 文字，以及強制標註「示意圖 / 比例圖」。
- **Agent 護欄**：所有動畫皆須支援 `prefers-reduced-motion`（減少動態效果無障礙設定），且一律套用 `web/tokens.css` 色票與字體。
- **驗收條件**：
  - `spark-visual` 區塊在雙語頁面皆正確渲染並具互動控制。
  - 若提供未在白名單內的元件類型或缺少必填欄位，`web/check.py` 會直接報錯。

---

### Phase 6：自動化驗證關卡與部署流程（Quality Gates & Deployment）
- **狀態**：`[x] 已完成`
- **目標**：建立「無人值守也能維持高品質與風格一致」的自動化防線與靜態部署流程。
- **交付物**：
  1. **完整版 `web/check.py` 檢查套件**：
     - YAML frontmatter 必填欄位與合法枚舉值檢查（對齊 `wiki/AGENTS.md` 與 `forecasts/AGENTS.md`）。
     - 雙語檔案 1:1 對應與內部相對連結／錨點無斷鏈檢查。
     - `web/styles/` 靜態掃描：禁止在 `tokens.css` 以外出現硬編碼 hex/rgb 色碼，禁止未核准的 inline style。
     - `spark-visual` JSON Schema 驗證與圖片路徑、`alt`、比例標註檢查。
     - 執行 `web/build.py` 驗證建置無錯誤且無未解析的模板變數。
  2. **部署與預覽文件**：
     - 提供一鍵本機建置與預覽指令。
     - 建立可選的 GitHub Actions workflow（`.github/workflows/deploy-web.yml`），在推送到指定分支時自動跑 `check.py` → `build.py` 並部署 `dist/` 至 GitHub Pages。
- **驗收條件**：
  - `python3 web/check.py` 在乾淨狀態下回傳 exit code `0`；刻意植入斷鏈、違規色碼或錯誤元件參數時能準確攔截。

---

## 4. 給後續 Agent 的交接指引（Agent Handoff Protocol）

任何 Agent 在 `web-portal`（或後續網頁維護任務）開工前，請遵守以下流程：

1. **開工必讀**：先讀根目錄 [AGENTS.md](../AGENTS.md) → `web/AGENTS.md`（Phase 1 建立後）→ 本文件 `web/ROADMAP.md` → `web/COMPONENTS.md`。
2. **單階段推進**：每次聚焦完成一個 Phase（或明確拆分的小里程碑），不要跨階段混雜未經設計的臨時程式碼。
3. **驗證後才算完成**：完成修改後，務必執行 `python3 web/build.py` 與 `python3 web/check.py`（Phase 2/6 起適用），並在確認無誤後更新本文件對應 Phase 的狀態標記（`[x] 已完成`）與備註。
4. **嚴格禁止事項**：
   - 不得將 Markdown 內容改為手寫 HTML 維護。
   - 不得繞過 `web/tokens.css` 自行發明配色、字體或排版風格。
   - 不得在未更新 `web/COMPONENTS.md` 與 `web/AGENTS.md` 的情況下私自新增動畫引擎或頁面版型。
