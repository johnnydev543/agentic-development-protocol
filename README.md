# AI Agent Routing

[繁體中文](#繁體中文) · [English](#english)

<a id="繁體中文"></a>
## 繁體中文

一套供 AI 程式代理使用、與特定模型無關（model-agnostic）的任務路由、升級與程式碼審查政策。

> 核心原則：用強模型消除不確定性，用成本較低的模型執行已知解法。

這個專案不是模型排行榜。它提供一套穩定的工作方法，依據任務的**不確定性、風險、影響範圍與專業需求**選擇合適的處理層級；實際模型名稱則集中在獨立 registry，方便隨模型能力、價格與供應狀況調整。

### 專案目的

- 避免所有工作都一律交給最昂貴的模型。
- 避免複雜或高風險問題從低階層級反覆試錯。
- 為失敗嘗試設定明確停止條件與交接格式。
- 讓高風險修改接受 fresh-context／cross-model 獨立審查。
- 將長期穩定的 routing 原則與快速變動的模型映射分開維護。
- 提供可直接放入新專案的 `AGENTS.md` 範本。

### L0–L3 任務路由

| 層級 | 定位 | 適合的工作 | 目前主要模型 |
|---|---|---|---|
| L0 | 快速／機械式 | 搜尋、重新命名、局部文字或設定修改、簡單測試、無領域語意變更的機械式重構 | GPT-5.6 Luna、DeepSeek V4 Flash |
| L1 | 日常實作 | 依明確規格開發、CRUD／API、schema、語意已定義的 adapter、直接的錯誤修正、一般前後端工作 | GLM-5.3 Flash、GPT-5.6 Terra |
| L2 | 複雜工程 | 多檔修改、相依關係追蹤、有證據的困難除錯、repo 規模實作、可靠性／效能工作 | GLM-5.3、DeepSeek V4 Pro；視情況使用 GPT-5.6 Terra |
| L3 | 架構／高度不確定 | 架構設計、衝突或模糊需求、跨模組根因分析、領域解讀、來源／資料血緣語意、高影響資料模型決策 | GPT-5.6 Sol |

不要強迫每項任務從 L0 開始。若工作一開始就涉及架構判斷、未定義的領域語意、資料來源歧義、關鍵時序或其他高風險決策，應直接路由到 L3。反之，若解法已明確，只剩實作，優先交由 L0–L2 執行。

專業需求也可以覆蓋一般層級選擇。目前 frontend／UI specialist 為 Kimi K3；OpenRouter 可用於 second opinion、A/B 評估、專業模型與 provider fallback。完整對應請見 [`models/MODEL_REGISTRY.md`](models/MODEL_REGISTRY.md)。

### Escalation：兩次失敗規則

對同一個尚未解決的失敗，若已嘗試 **兩種實質不同的修法**仍未成功：

1. 立即停止 speculative editing，不做第三次猜測式修改。
2. L0／L1 的工程或除錯問題建議升至 L2。
3. 架構、領域語意、provenance、時序或其他高風險決策直接建議 L3。
4. L2 若仍失敗，應升至 L3 進行更深入的根因、架構或領域判斷。
5. 已在 L3 時，不要只因問題困難而再次建議 L3；缺少權威語意、必要資料或需求互相衝突時，應要求釐清或獨立審查。
6. 產出包含原始任務、觀察到的失敗、已嘗試方法與結果、證據支持的根因假設、相關檔案／測試、限制與下一個精確問題的 escalation package。

「兩次」指兩個**實質不同**的方法，不是把同一方法換個寫法重試。完整停止條件及交接範本請見 [`policies/ESCALATION.md`](policies/ESCALATION.md)。

### Cross-model review

一般修改依風險執行相關的 unit test、integration test、lint 與 type check。財務或安全關鍵計算、領域語意轉換、歷史資料規則、重要 schema、identity／mapping、timestamp／information cutoff、provenance、backtesting、跨模組架構與大型領域重構等高風險變更，應要求或強烈建議獨立審查。

可行時，審查者應：

- 使用 fresh context，避免繼承實作者的思考錨點。
- 採用不同於實作模型的模型，增加觀點多樣性。
- 取得原始任務、權威規格、專案規則、Git diff 與測試／lint／type-check 結果。
- 將發現分為 Blocker、Major、Minor、Suggestion。
- 不得在缺少規格或來源時自行改寫領域語意；這類問題應升級釐清。

Cross-model review 的目的是獨立找錯，而不是盲從被認為「更強」的模型。詳見 [`policies/CODE_REVIEW.md`](policies/CODE_REVIEW.md)。

### 為什麼 policy 與 MODEL_REGISTRY 分開？

`policies/MODEL_ROUTING.md` 定義「什麼類型的任務需要哪一級能力」，這些工作流程原則應保持穩定。`models/MODEL_REGISTRY.md` 則定義「目前由哪些模型扮演各層級與專業角色」，會隨模型供應、價格、延遲與實際表現頻繁變動。

因此，新模型出現時應先更新 registry；只有底層工作流程原則改變時，才修改 routing policy。registry 中的配置是可重新評估的操作指引，不是永久性的 benchmark 排名。

### 目錄結構

```text
.
├── README.md
├── policies/
│   ├── MODEL_ROUTING.md   # L0–L3 定義與 routing 規則
│   ├── ESCALATION.md      # 停止條件與交接格式
│   └── CODE_REVIEW.md     # 風險式驗證與獨立審查
├── models/
│   └── MODEL_REGISTRY.md  # 當前模型與角色映射
├── templates/
│   ├── AGENTS.minimal.md  # 輕量專案
│   ├── AGENTS.standard.md # 一般用途
│   └── AGENTS.high-risk.md# 高風險／資料敏感領域
├── examples/
│   └── financial-project/
│       └── AGENTS.md      # 金融／資料完整性範例
└── CHANGELOG.md
```

### 在新專案中使用

1. 依專案風險選擇範本：
   - `AGENTS.minimal.md`：小型、低風險或規則簡單的專案。
   - `AGENTS.standard.md`：大多數一般軟體專案。
   - `AGENTS.high-risk.md`：金融、安全關鍵、資料完整性或領域語意敏感專案。
2. 將範本複製到新專案根目錄並命名為 `AGENTS.md`。
3. 加入該專案的技術棧、測試指令、權威規格、禁止事項與領域限制。
4. 保留 L0–L3、兩次失敗停止規則與風險式審查的核心語意。
5. 依自己的可用模型、成本與 provider 更新 `models/MODEL_REGISTRY.md`，不要為了換模型而改動 routing policy。
6. 高風險專案可參考 `examples/financial-project/AGENTS.md` 的資料與領域完整性規則。

例如：

```text
請先依 AGENTS.md 判定 routing level。

任務：修正付款金額四捨五入造成的帳務差異。
限制：不得猜測會計規則；所有計算必須有測試。
驗證：執行 unit tests、integration tests 與 type check。
審查：金額計算變更需要 fresh-context cross-model review。
```

這項任務涉及財務計算與領域語意，應直接使用高風險流程；若規格沒有定義四捨五入方式，應要求釐清，而不是自行選擇規則。

---

<a id="english"></a>
## English

A model-agnostic routing, escalation, and review policy for AI coding agents.

## Principle

> Use strong models to resolve uncertainty and lower-cost models to execute known solutions.

## Structure

- `policies/MODEL_ROUTING.md` — task levels and routing rules.
- `policies/ESCALATION.md` — stop conditions and handoff protocol.
- `policies/CODE_REVIEW.md` — risk-based verification and independent review.
- `models/MODEL_REGISTRY.md` — current model-to-role mapping.
- `templates/AGENTS.minimal.md` — lightweight project template.
- `templates/AGENTS.standard.md` — general-purpose project template.
- `templates/AGENTS.high-risk.md` — domain/data-sensitive template.
- `examples/financial-project/AGENTS.md` — financial/data-integrity example.

## Routing levels

| Level | Meaning | Typical work |
|---|---|---|
| L0 | Fast / mechanical | search, rename, small edits, simple tests |
| L1 | Routine implementation | CRUD, schemas, adapters, straightforward fixes |
| L2 | Complex engineering | multi-file debugging, dependency tracing, repo-scale implementation |
| L3 | Architecture / high uncertainty | architecture, ambiguous requirements, domain semantics, difficult root cause |

## Escalation rule

For the same unresolved failure, after **two materially different unsuccessful fixes**, stop speculative editing and produce an escalation package.

Do not force every task to start at L0. High-risk or high-uncertainty tasks may route directly to L3.

## Usage

1. Copy the appropriate `templates/AGENTS.*.md` into a project as `AGENTS.md`.
2. Add project-specific rules.
3. Keep routing semantics stable.
4. Update `models/MODEL_REGISTRY.md` as models, price, or availability changes.

## Status

v0.1 — initial policy set.
