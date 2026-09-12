# Staged Multi-Model Development Lifecycle

This workflow is for projects where the specification is already sufficiently settled and the goal is to spend strong-model tokens on high-decision-density work while delegating deterministic implementation to lower-cost models.

## Lifecycle

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

This lifecycle complements L0-L3 routing. The lifecycle answers **what phase the repository is in**; L0-L3 answers **how much reasoning capacity the current task requires**.

## 1. SPEC FINAL

Do not begin the architecture pass until the authoritative requirements are sufficiently stable for implementation.

If requirements are conflicting, materially incomplete, or require unsupported domain interpretation, route the unresolved decision to L3 before coding.

## 2. ARCHITECT

Use a strong model when the work determines architecture, interfaces, schemas, dependency direction, cross-module contracts, or other decisions that constrain later implementation.

The architect should normally complete:

- repository/module/package structure;
- core domain models, interfaces, protocols, schemas, and types;
- dependency direction and ownership boundaries;
- application bootstrap / dependency injection / entry points;
- shared configuration, logging, and error-handling foundations;
- repository/service/provider abstractions;
- high-risk or highly coupled core logic;
- at least one representative implementation for important extension patterns;
- smoke/architecture tests proving that the skeleton composes and starts.

The architect should normally **not** finish repetitive, localized, pattern-following work such as every CRUD route, every provider, every adapter, every edge case, broad boilerplate coverage, or UI polish.

### Stop condition

The architecture pass is complete when lower-cost models can implement the remaining tasks without needing to reinterpret the architecture.

Do not continue merely to make the product feature-complete.

## 3. HANDOFF

The architect creates or updates `docs/implementation-handoff.md`.

It should contain:

### Architecture completed

The decisions and foundational components that are now authoritative.

### Architecture invariants

Rules later agents must not silently change, such as:

- dependency direction;
- module ownership;
- public interfaces;
- schema boundaries;
- error-handling conventions;
- persistence access patterns;
- source/provenance rules;
- naming or extension patterns that matter to correctness.

### Remaining implementation tasks

Break work into small, independently executable tasks. Prefer tasks that affect roughly 1-3 modules and have explicit acceptance criteria.

Recommended format:

```text
#### TASK-001: <name>
Status: TODO
Files:
- ...

Goal:
...

Implementation notes:
...

Do not change:
...

Acceptance criteria:
- ...

Tests:
- ...
```

### High-risk remaining work

Any task that still requires architecture, domain judgment, or another high-uncertainty decision must be separated from ordinary implementation work and routed upward rather than disguised as a routine task.

## 4. IMPLEMENT

Lower-cost models should execute one well-scoped handoff task at a time.

Before editing, the implementer should read:

- `AGENTS.md`;
- `docs/implementation-handoff.md`;
- the selected task;
- the files and tests directly relevant to that task.

The implementer should:

1. Follow existing architecture and reference implementations.
2. Stay within task scope.
3. Add or update required tests.
4. Run the relevant test/lint/type-check subset.
5. Stop instead of redesigning architecture when the task cannot be completed under existing invariants.
6. Mark the task `DONE` only after verification passes, with a concise record of changed files and checks run.
7. Not automatically begin the next task unless explicitly instructed.

## 5. REVIEW

Review should use a fresh context for meaningful changes and preferably a different model from the implementer when practical.

The reviewer receives:

- original task or task ID;
- authoritative specification;
- `AGENTS.md`;
- relevant architecture/handoff rules;
- explicitly named changed files and review scope;
- test/lint/type-check results.

Findings must be concrete and classified as Blocker, Major, Minor, or Suggestion.

Each actionable finding should include:

- finding ID;
- affected file(s) / symbols;
- observed problem;
- why it matters;
- expected correction;
- verification needed.

Review is diagnosis, not automatic implementation. A reviewer may propose a fix but should not silently redefine architecture or domain semantics.

## 6. FIX

Do not assume every review finding requires the same model that performed the review.

Use a lower-cost implementation model when the finding is:

- localized;
- unambiguous;
- pattern-following;
- covered by existing interfaces/specification;
- testable without new architectural decisions.

Route back to a strong model when the finding exposes:

- an architecture flaw;
- an interface/schema decision that must change;
- cross-module semantic ambiguity;
- uncertain root cause;
- high-risk domain/provenance/timing logic.

### Cross-session review-fix handoff

When review and fix occur in different sessions, persist the findings in the repository rather than relying on chat history. Recommended file:

`docs/review-findings.md`

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

After fixing, the implementation agent should update the same entry:

```text
Status: FIXED
Fix summary: ...
Verification: ...
```

Do not delete or rewrite the original finding merely because it was fixed.

## 7. VERIFY

A task is not complete merely because code changed.

Verification should include the relevant subset of:

- unit tests;
- integration tests;
- lint;
- type checks;
- build/import/startup smoke tests;
- regression test for the reviewed defect.

For high-risk changes, run fresh-context review again if the fix materially changed architecture/domain behavior or if the original reviewer requested re-review.

## Temporary Handoff Rule

Git-based phase handoff is currently disabled. Use the selected `TASK-###`, explicitly named changed files/scope, `RVW-###` findings, and verification results as the cross-session handoff record. Normal version control may continue, but agents must not require phase-specific commits or Git baselines to proceed.

## Decision rule

Use the strong model for **decisions** and the cheaper model for **execution**.

A practical test:

- Changes architecture → strong model.
- Defines interface/schema/dependency semantics → strong model.
- High coupling / high uncertainty / high domain risk → strong model.
- Repetitive / localized / pattern-following → lower-cost model.
- Straightforward review fix with explicit finding → lower-cost model.
- Review fix that changes architecture or semantics → strong model.
