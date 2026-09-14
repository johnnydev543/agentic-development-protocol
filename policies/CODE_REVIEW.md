# Code Review Policy

Verification and review are risk-based. Do not spend expensive independent review on every trivial change.

## Standard Verification

For ordinary changes, complete the relevant subset of:

1. Unit tests.
2. Integration tests, if available.
3. Lint checks, if configured.
4. Type checks, if configured.
5. Build/import/startup smoke checks when relevant.

## Independent Review

Independent review is required or strongly preferred for high-risk changes, including:

- Financial or safety-critical calculations.
- Domain-semantic extraction or normalization.
- Consensus/revision logic.
- Historical data mutation rules.
- Database schema changes affecting important data.
- Identity/mapping logic.
- Timestamp/information-cutoff logic.
- Source provenance logic.
- Backtesting logic.
- Cross-module architecture changes.
- Large refactors affecting domain behavior.

Prefer a fresh-context reviewer different from the implementation model when practical.

## Reviewer Input

The reviewer should receive:

- Original task or task ID.
- Authoritative specification.
- Relevant project rules (`AGENTS.md`).
- Relevant recorded architecture or decision constraints, if present.
- Explicitly named changed files and review scope.
- Test/lint/type-check output.

## Finding Severity

Classify findings as:

- Blocker
- Major
- Minor
- Suggestion

Each actionable finding should also have a stable ID such as `RVW-001` and include affected files/symbols, the observed problem, why it matters, required correction, and required verification.

The reviewer must not silently rewrite domain semantics. Any finding that changes authoritative business/domain meaning must be supported by a source/specification or escalated for clarification.

## Persist Findings Across Sessions

When review and repair happen in different sessions, do not depend on chat history. Persist actionable findings in `docs/review-findings.md`.

If a standalone review report is needed, name it `NNNN_REVIEW_SCOPE.md` and register the next unused review document number in `docs/0000_DOCUMENT_INDEX.md`. This numbering applies only to standalone review reports; the findings ledger keeps its stable filename and separate `RVW-###` IDs.

Recommended format:

```text
## RVW-001 — Major
Status: OPEN
Task: TASK-003
Files:
- src/...

Finding:
...

Required fix:
...

Verification:
- ...
```

After repair, keep the original finding and update it:

```text
Status: FIXED-PENDING-REVIEW
Fix summary: ...
Verification: ...
```

A separate fixer normally uses `FIXED-PENDING-REVIEW`. A `REVIEW-AND-FIX` session may set `FIXED` after resolving a localized, unambiguous, low-risk finding and passing verification. If the finding is invalid, use `NEEDS-REVIEW` with evidence.

## Who Should Fix Review Findings?

Do not automatically use the review model to implement its findings.

Use an L0-L2-authorized FIX session when the finding is localized, explicit, pattern-following, supported by existing architecture/semantics, and testable without a new design decision.

Require an L3-authorized FIX or DECISION session when the finding exposes:

- an architecture flaw;
- an interface or schema decision that must change;
- unsupported domain/provenance/timing semantics;
- uncertain cross-module root cause;
- another high-risk decision not settled by the specification.

The session authorization, not the selected model's name, controls whether that work may proceed.

## Fix Completion

A finding is not resolved merely because code changed.

Fresh RE-REVIEW is mandatory for Blocker/Major findings, L3 work, architecture/interface/schema changes, security or safety-critical behavior, domain/provenance/timing semantics, uncertain root cause, or an explicit reviewer request. Verified localized low-risk fixes may be closed in REVIEW-AND-FIX without creating an endless reviewer chain.

## Cross-Model Review

Cross-model review is useful for independent error detection, not automatic deference to a supposedly stronger model. Prefer diversity of model perspective when the change is high-risk or when the implementer may have anchored on a flawed assumption.
