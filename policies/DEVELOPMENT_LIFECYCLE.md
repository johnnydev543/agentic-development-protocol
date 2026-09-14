# Authorized Development Lifecycle

Use this workflow after the controlling specification is sufficiently settled:

```text
[optional PLAN → PLAN-REVIEW]
                 ↓
IMPLEMENT → implementation checkpoint → REVIEW → FIX → fix checkpoint → RE-REVIEW → VERIFY
```

There is no mandatory HANDOFF phase or implementation-handoff document. A separate DECISION session is used only when an unresolved L3 question blocks implementation.

## Optional PLAN Gate

Use PLAN when the implementation scope must be subdivided before coding.

- **L2 PLAN:** mechanically divides work under already-settled module boundaries, interfaces, schemas, semantics, dependencies, and acceptance criteria.
- **L3 PLAN:** chooses or changes those boundaries or resolves another high-impact decision. Use L3 authorization or first run a focused DECISION session.

Each planned task must be independently executable, name its files/components, inputs/outputs, do-not-change boundaries, acceptance criteria, and tests. PLAN must not implement code.

PLAN-REVIEW evaluates the plan rather than production code. When authority is sufficient, it should directly amend task boundaries, dependencies, acceptance criteria, and tests, then return `PLAN_APPROVED` in the same session. Plan edits do not require another reviewer. Use stable `PLN-###` findings only when an unresolved decision or missing authority prevents direct resolution. After two materially different revisions fail for the same structural reason, escalate instead of cycling.

## 1. IMPLEMENT

The session must include the authorization header from `templates/SESSION_AUTHORIZATION.md` and an explicit scope. L0-L2 covers even large or multi-file work when architecture, interfaces, schemas, domain semantics, and acceptance criteria are already settled.

If required work exceeds the session maximum, stop before planning, decomposition, design, or edits and emit the escalation package. Do not turn an unresolved L3 decision into apparently routine subtasks.

Complete only the named scope, add the required tests, and record verification. When practical, create an implementation checkpoint commit after checks pass. The commit freezes the review target; it is not a model-handoff requirement.

## 2. REVIEW

Use a fresh session for meaningful changes. Provide the controlling specification, project rules, explicit change scope, implementation checkpoint when available, and verification output.

The reviewer records actionable findings with stable `RVW-###` IDs. REVIEW is diagnosis-only. REVIEW-AND-FIX may directly resolve a localized, unambiguous, low-risk defect within its authorization, run verification, and set it `FIXED` in the same session. A checkpoint commit makes the reviewed snapshot reproducible, but review may use an explicitly named working-tree scope.

## 3. FIX

Authorize a FIX session for specific `RVW-###` entries.

- Explicit, localized, pattern-following correction under settled decisions: L0-L2.
- Architecture, interface/schema, domain/provenance/timing decision, or uncertain root cause: L3.

After checks pass, a separate FIX session normally sets `FIXED-PENDING-REVIEW`. It may set `FIXED` directly only when the finding is localized, unambiguous, low risk, and independent re-review is not required by the rules below.

## 4. RE-REVIEW

Fresh RE-REVIEW is required for Blocker/Major findings, L3 work, architecture/interface/schema changes, security or safety-critical behavior, domain/provenance/timing semantics, uncertain root cause, or when explicitly requested. It is optional for verified localized low-risk fixes.

For each finding:

- correction and verification pass → `FIXED`;
- correction fails or regresses behavior → `OPEN` with evidence;
- finding conflicts with authoritative requirements → `NEEDS-REVIEW`;
- a distinct new defect → allocate a new `RVW-###` ID.

Do not rewrite or delete the original finding.

## 5. VERIFY

Run the risk-relevant tests, lint, type checks, build/import/startup checks, and regression checks. Verification evidence belongs with the task/finding. Passing commands do not override unresolved semantic or provenance doubt.

## Optional L3 DECISION Session

When implementation discovers an unauthorized L3 question, open a separate session scoped only to that decision. Its output should state:

- decision;
- authoritative constraints;
- required implementation behavior;
- acceptance criteria.

It should not broaden into unrelated implementation. After the decision is authoritative, return to a newly authorized IMPLEMENT or FIX session.

## Checkpoint Rule

Git checkpoints are recommended for reproducible review targets, not mandatory phase handoffs. Agents must not refuse work solely because the working tree lacks a phase-specific commit. Never overwrite unrelated local changes to manufacture a clean checkpoint.
