# AI Agent Routing

[繁體中文](#繁體中文) · [English](#english)

<a id="繁體中文"></a>
## 繁體中文

一套供 AI 程式代理使用、與特定模型無關（model-agnostic）的任務路由、升級、交接與程式碼審查政策。

> 核心原則：用強模型消除不確定性、做高決策密度工作；用成本較低的模型執行已知解法與明確 task。

這個專案不是模型排行榜。它提供一套穩定的工作方法，依據任務的**不確定性、風險、影響範圍、開發階段與專業需求**選擇處理層級；實際模型名稱集中在獨立 registry，方便隨能力、價格、供應與快取狀況調整。

### 專案目的

- 避免所有工作都一律交給最昂貴的模型。
- 避免複雜或高風險問題從低階層級反覆試錯。
- 讓強模型專注架構、介面、schema、跨模組與不確定性決策。
- 讓 Flash／較低成本模型接手已定義、可測試、pattern-following 的實作。
- 為失敗嘗試設定明確停止條件與交接格式。
- 讓 review 與 review-fix 可以跨 session、跨模型可靠傳遞。
- 讓高風險修改接受 fresh-context／cross-model 獨立審查。
- 用 Git diff、handoff files 與 task IDs 作為 agent 之間的共同狀態。
- 將長期穩定的 routing 原則與快速變動的模型映射分開維護。
- 提供可直接放入新專案的 `AGENTS.md` 與 prompt 範本。

### 兩個 routing 維度

這套方法同時看兩件事：

1. **L0–L3 task level**：目前這個問題需要多少推理、判斷與風險承擔。
2. **Development phase**：目前處於 ARCHITECT、IMPLEMENT、REVIEW、FIX 還是 VERIFY。

因此「程式很多」不等於一定要用最強模型；如果 architecture、schema、interface 與 acceptance criteria 已經定案，大量 implementation 仍可交給較便宜模型。反過來，一個只改幾行的 schema／provenance／domain semantics 變更也可能直接需要 L3。

### L0–L3 任務路由

| 層級 | 定位 | 適合的工作 | 目前主要模型 |
|---|---|---|---|
| L0 | 快速／機械式 | 搜尋、重新命名、局部文字或設定修改、簡單測試、無領域語意變更的機械式重構 | GPT-5.6 Luna、DeepSeek V4 Flash |
| L1 | 日常實作 | 依明確規格開發、CRUD／API、schema、語意已定義的 adapter、直接的錯誤修正、一般前後端工作 | GLM-5.3 Flash、GPT-5.6 Terra |
| L2 | 複雜工程 | 多檔修改、相依關係追蹤、有證據的困難除錯、repo 規模實作、可靠性／效能工作 | GLM-5.3、DeepSeek V4 Pro；視情況使用 GPT-5.6 Terra |
| L3 | 架構／高度不確定 | 架構設計、衝突或模糊需求、跨模組根因分析、領域解讀、來源／資料血緣語意、高影響資料模型決策 | GPT-5.6 Sol |

不要強迫每項任務從 L0 開始。若工作一開始就涉及架構判斷、未定義的領域語意、資料來源歧義、關鍵時序或其他高風險決策，應直接路由到 L3。反之，若解法已明確，只剩實作，優先交由 L0–L2 執行。

完整定義見 [`policies/MODEL_ROUTING.md`](policies/MODEL_ROUTING.md)。

### 規格定案後的多模型開發流程

當 spec 已 sufficiently final，可以採用：

```text
SPEC FINAL
    ↓
ARCHITECT
    ↓
HANDOFF
    ↓
IMPLEMENT
    ↓
REVIEW
    ↓
FIX
    ↓
VERIFY
```

核心分工：

> Pro／Sol 決定 pattern；Flash／較低成本模型依照 pattern 執行。

#### ARCHITECT

強模型負責：

- module/package boundaries
- domain model、interface、protocol、schema、type
- dependency direction
- bootstrap / dependency injection
- shared config / logging / error handling
- repository/service/provider abstraction
- 高耦合或高風險核心邏輯
- 至少一個完整 reference implementation
- smoke / architecture tests

強模型**不應為了完整而把所有 CRUD、adapter、provider、edge case、boilerplate tests 全部寫完**。

停止條件是：剩餘工作已經可以被拆成低不確定性的 implementation tasks，而不是「產品已 feature-complete」。

#### HANDOFF

架構完成後建立：

`docs/implementation-handoff.md`

至少記錄：

- Architecture completed
- Architecture invariants
- Remaining implementation tasks
- High-risk remaining work

每個 task 應有 task ID、相關檔案、goal、implementation notes、不可變更範圍、acceptance criteria、tests。

#### IMPLEMENT

Flash／較低成本模型一次只做一個 task。不要下「把剩下的全部完成」這種模糊指令。

若 task 必須改 architecture、interface、schema 或 domain semantics 才能完成，implementer 應停止並回報 blocker，而不是自行重設計。

#### REVIEW

重要變更使用 fresh-context reviewer，能跨模型時優先跨模型。Reviewer 應看原始 task、spec、`AGENTS.md`、handoff invariants、Git diff 與 verification output。

Finding 分為 Blocker / Major / Minor / Suggestion，並使用穩定 ID，例如 `RVW-003`。

#### FIX

Review finding 不代表一定要由原 review 強模型修。

- 明確、局部、pattern-following、可直接測試 → Flash／較低成本模型。
- 暴露 architecture flaw、schema/interface 決策、domain/provenance ambiguity、uncertain root cause → 回到強模型。

跨 session 時將 finding 寫入：

`docs/review-findings.md`

修正後保留原 finding，更新為 `FIXED` 並記錄 fix summary、verification、commit SHA（若可得）。不要只因「有改 code」就標記完成。

#### VERIFY

task／finding 的完成條件是驗證通過，而不是 code 已修改。依風險執行 unit test、integration test、lint、type check、build/import/startup smoke test 與 regression test。

完整流程見 [`policies/DEVELOPMENT_LIFECYCLE.md`](policies/DEVELOPMENT_LIFECYCLE.md)。

### Git 是 handoff backbone

建議 sequence：

```text
architecture baseline commit
        ↓
TASK-001 commit
        ↓
TASK-002 commit
        ↓
review findings
        ↓
review-fix commit(s)
        ↓
verification
```

例如：

```text
arch: establish core application architecture
feat: implement TASK-001 report ingestion
fix: resolve RVW-003 provider normalization issue
```

這讓 reviewer 可以看「architecture baseline vs Flash implementation」或「review finding vs fix」，而不是面對一次混在一起的大型 diff。

### Escalation：兩次失敗規則

對同一個尚未解決的失敗，若已嘗試 **兩種實質不同的修法**仍未成功：

1. 立即停止 speculative editing，不做第三次猜測式修改。
2. L0／L1 的工程或除錯問題建議升至 L2。
3. 架構、領域語意、provenance、時序或其他高風險決策直接建議 L3。
4. L2 若仍失敗，應升至 L3 進行更深入的根因、架構或領域判斷。
5. 已在 L3 時，不要只因問題困難而再次建議 L3；缺少權威語意、必要資料或需求互相衝突時，應要求釐清或獨立審查。
6. 產出包含原始任務、觀察到的失敗、已嘗試方法與結果、證據支持的根因假設、相關檔案／測試、限制與下一個精確問題的 escalation package。

詳見 [`policies/ESCALATION.md`](policies/ESCALATION.md)。

### Cross-model review

一般修改依風險執行相關 unit test、integration test、lint 與 type check。財務或安全關鍵計算、領域語意轉換、歷史資料規則、重要 schema、identity／mapping、timestamp／information cutoff、provenance、backtesting、跨模組架構與大型領域重構等高風險變更，應要求或強烈建議獨立審查。

Cross-model review 的目的不是盲從「更強」模型，而是用 fresh context 與不同模型 perspective 找出 implementer 的盲點。詳見 [`policies/CODE_REVIEW.md`](policies/CODE_REVIEW.md)。

### Prompt templates

可直接使用：

- [`templates/ARCHITECTURE_PASS.md`](templates/ARCHITECTURE_PASS.md) — 叫強模型建立主架構、刻意留下可委派工作。
- [`templates/IMPLEMENT_TASK.md`](templates/IMPLEMENT_TASK.md) — 叫 Flash／較低成本模型只執行指定 task。
- [`templates/REVIEW_PASS.md`](templates/REVIEW_PASS.md) — fresh-context review，產出可持久化 findings。
- [`templates/REVIEW_FIX.md`](templates/REVIEW_FIX.md) — 在另一個 session 依 finding 修復並標記驗證結果。

### 為什麼 policy 與 MODEL_REGISTRY 分開？

`policies/*.md` 定義長期穩定的工作流程；`models/MODEL_REGISTRY.md` 定義目前哪些模型適合扮演 L0–L3、ARCHITECT、IMPLEMENT、REVIEW、FIX、VERIFY 等角色。

因此，新模型出現時先更新 registry；只有底層 workflow 原則改變時才修改 policy。模型 mapping 是操作指引，不是永久 benchmark 排名。

### 目前模型角色

目前預設方向：

- ARCHITECT：GPT-5.6 Sol；部分 conventional architecture 可考慮 GLM-5.3。
- IMPLEMENT：GLM-5.3 Flash、GPT-5.6 Terra；機械工作可用 Luna / DeepSeek V4 Flash。
- REVIEW：Sol、GLM-5.3、DeepSeek V4 Pro 或 OpenRouter 上經驗證的獨立強模型。
- REVIEW FIX：一般 finding 優先 Flash / Terra；architecture/domain finding 回強模型。
- VERIFY：使用能可靠執行並解讀測試的最低成本模型/harness。

Frontend/UI specialist 目前為 Kimi K3。完整 mapping 見 [`models/MODEL_REGISTRY.md`](models/MODEL_REGISTRY.md)。

### 目錄結構

```text
.
├── README.md
├── policies/
│   ├── MODEL_ROUTING.md
│   ├── DEVELOPMENT_LIFECYCLE.md
│   ├── ESCALATION.md
│   └── CODE_REVIEW.md
├── models/
│   └── MODEL_REGISTRY.md
├── templates/
│   ├── AGENTS.minimal.md
│   ├── AGENTS.standard.md
│   ├── AGENTS.high-risk.md
│   ├── ARCHITECTURE_PASS.md
│   ├── IMPLEMENT_TASK.md
│   ├── REVIEW_PASS.md
│   └── REVIEW_FIX.md
├── examples/
│   └── financial-project/
│       └── AGENTS.md
└── CHANGELOG.md
```

### 在新專案中使用

1. 選擇 `AGENTS.minimal.md`、`AGENTS.standard.md` 或 `AGENTS.high-risk.md`，複製成專案根目錄 `AGENTS.md`。
2. 加入技術棧、測試指令、權威規格、禁止事項與 domain constraints。
3. 規格定案後，以 `ARCHITECTURE_PASS.md` 讓強模型建立 architecture skeleton。
4. 要求 architect 寫出 `docs/implementation-handoff.md`。
5. 用 `IMPLEMENT_TASK.md` 一次派一個 task 給 Flash／較低成本模型。
6. 每個 task 使用獨立 Git commit 或至少保留清楚 baseline。
7. 重要變更用 `REVIEW_PASS.md` 做 fresh-context review。
8. 跨 session findings 寫入 `docs/review-findings.md`，再使用 `REVIEW_FIX.md` 修復。
9. 若 finding 只是明確實作問題，不必浪費 review 強模型做修復；只有 architecture/domain uncertainty 才升回高階模型。

---

<a id="english"></a>
## English

A model-agnostic routing, escalation, handoff, and review policy for AI coding agents.

### Principle

> Use strong models to resolve uncertainty and make high-decision-density choices; use lower-cost models to execute known solutions.

### Two routing dimensions

1. **L0-L3 task level** — reasoning, uncertainty, risk, and blast radius.
2. **Development phase** — SPEC FINAL → ARCHITECT → HANDOFF → IMPLEMENT → REVIEW → FIX → VERIFY.

A large task can still be delegated when architecture and semantics are explicit. A small change can require L3 when it changes architecture, schema, provenance, or domain meaning.

### Recommended staged workflow

```text
SPEC FINAL
    ↓
ARCHITECT
    ↓
HANDOFF
    ↓
IMPLEMENT
    ↓
REVIEW
    ↓
FIX
    ↓
VERIFY
```

The architect establishes boundaries, contracts, reference patterns, high-risk core logic, and a verified skeleton, then creates `docs/implementation-handoff.md` and stops before repetitive implementation is exhausted.

Lower-cost models execute one explicit task at a time. Review uses fresh context when appropriate. Cross-session findings are persisted in `docs/review-findings.md`. Straightforward findings can be fixed by lower-cost models; architecture/domain findings route back upward.

### Structure

- `policies/MODEL_ROUTING.md` — L0-L3 and phase-aware routing.
- `policies/DEVELOPMENT_LIFECYCLE.md` — architecture-to-delegation lifecycle.
- `policies/ESCALATION.md` — stop conditions and escalation package.
- `policies/CODE_REVIEW.md` — review, persisted findings, and review-fix routing.
- `models/MODEL_REGISTRY.md` — current model-to-level and model-to-phase mapping.
- `templates/AGENTS.*.md` — project agent policies.
- `templates/ARCHITECTURE_PASS.md` — architecture prompt.
- `templates/IMPLEMENT_TASK.md` — delegated implementation prompt.
- `templates/REVIEW_PASS.md` — independent review prompt.
- `templates/REVIEW_FIX.md` — cross-session fix prompt.

### Core routing rule

Do not force every task to start at L0. Route directly to L3 when architecture or unsupported semantic judgment is required. Once decisions are explicit, route implementation downward.

Do not automatically use the reviewer to implement its findings. Use a lower-cost model for explicit localized fixes; route architecture/interface/schema/domain uncertainty back to a strong model.

### Status

v0.2 — staged multi-model development workflow.
