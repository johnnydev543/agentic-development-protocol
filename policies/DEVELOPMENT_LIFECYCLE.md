# Authorized Development Lifecycle

Use this workflow after the controlling specification is sufficiently settled:

```text
[optional PLAN → PLAN-REVIEW]
                 ↓
IMPLEMENT → implementation checkpoint → REVIEW → IMPLEMENT finding corrections → REVIEW → COMPLETE
```

There is no mandatory HANDOFF phase or implementation-handoff document. A separate DECISION session is used only when an unresolved L3 question blocks implementation.

## Optional PLAN Gate

Use PLAN when the implementation scope must be subdivided before coding.

- **L2 PLAN:** mechanically divides work under already-settled module boundaries, interfaces, schemas, semantics, dependencies, and acceptance criteria.
- **L3 PLAN:** chooses or changes those boundaries or resolves another high-impact decision. Use L3 authorization or first run a focused DECISION session.

Each planned task must be independently executable, name its files/components, inputs/outputs, do-not-change boundaries, acceptance criteria, and tests. PLAN must not implement code.

PLAN-REVIEW evaluates the plan rather than production code. When authority is sufficient, it should directly amend task boundaries, dependencies, acceptance criteria, and tests, then return `PLAN_APPROVED` in the same session. Plan edits do not require another reviewer. Use stable `PLN-###` findings only when an unresolved decision or missing authority prevents direct resolution. After two materially different revisions fail for the same structural reason, escalate instead of cycling.

## 1. IMPLEMENT

The session must include the authorization header from `templates/SESSION_AUTHORIZATION.md`. Its role remains fixed. L0-L2 covers even large or multi-file work when architecture, interfaces, schemas, domain semantics, and acceptance criteria are already settled.

If required work exceeds the session maximum, stop before planning, decomposition, design, or edits and emit the escalation package. Do not turn an unresolved L3 decision into apparently routine subtasks.

IMPLEMENT handles both initial task work and correction of review findings. Infer which applies from the request and repository state, report the inferred scope, complete only that scope, add the required tests, and record verification. Finding correction uses relevant `OPEN` entries and normally changes them to `FIXED-PENDING-REVIEW`. When practical, create a checkpoint commit after checks pass. The commit freezes the review target; it is not a model-handoff requirement.

## 2. REVIEW

Use a fresh session for meaningful changes. REVIEW handles both initial implementation review and review of corrected findings. Infer the mode and scope from relevant `FIXED-PENDING-REVIEW` findings, the current diff, checkpoint/branch state, and user request; report the inferred scope before proceeding. REVIEW may be authorized up to L3 according to risk.

The reviewer records actionable findings with stable `RVW-###` IDs. REVIEW is diagnosis-only, but verification is part of that diagnosis: inspect submitted evidence, independently rerun risk-relevant targeted checks, and add adversarial or regression cases when needed. For corrected findings, set `FIXED`, `OPEN`, or `NEEDS-REVIEW`; allocate a new ID for a distinct defect. Do not rerun the full suite merely to duplicate evidence unless risk, coverage, or execution cost justifies it.

## 3. REVIEW-AND-FIX

REVIEW-AND-FIX is a fixed composite role rather than a mid-session switch. It may review and correct up to L3 within session authorization. Its final self-approval is limited to L0-L2 findings that are localized, unambiguous, supported by settled decisions, and safe to verify in the same session.

- L0-L2 direct correction: record the finding, correct it, verify it, and set `FIXED` when no independent-review rule applies.
- L3 correction whose answer is authoritative: correct and verify it, but leave it `FIXED-PENDING-REVIEW`; the same session cannot finally approve it.
- Unresolved L3 architecture, interface/schema, domain/provenance/timing, or uncertain-root-cause decision: diagnose it and leave it `OPEN` for a separate DECISION session.

## 4. Review of Finding Corrections

There is no separate RE-REVIEW role. Start a fresh REVIEW session after IMPLEMENT corrects findings. Fresh independent REVIEW is required for Blocker/Major findings, L3 work, architecture/interface/schema changes, security or safety-critical behavior, domain/provenance/timing semantics, uncertain root cause, or when explicitly requested. It is optional for verified localized low-risk corrections closed by REVIEW-AND-FIX.

For each finding:

- correction and verification pass → `FIXED`;
- correction fails or regresses behavior → `OPEN` with evidence;
- finding conflicts with authoritative requirements → `NEEDS-REVIEW`;
- a distinct new defect → allocate a new `RVW-###` ID.

Do not rewrite or delete the original finding.

## Verification Inside Review

IMPLEMENT runs affected-scope checks before submitting initial work or finding corrections. REVIEW and REVIEW-AND-FIX independently assess that evidence and rerun or extend the checks needed for the reviewed risk. Record commands, results, uncovered limits, and any semantic or provenance uncertainty with the review. Passing commands do not override unresolved correctness doubt.

## Optional L3 DECISION Session

When implementation discovers an unauthorized L3 question, open a separate session scoped only to that decision. Its output should state:

- decision;
- authoritative constraints;
- required implementation behavior;
- acceptance criteria.

It should not broaden into unrelated implementation. After the decision is authoritative, return to a newly authorized IMPLEMENT session.

## Checkpoint Rule

Git checkpoints are recommended for reproducible review targets, not mandatory phase handoffs. Agents must not refuse work solely because the working tree lacks a phase-specific commit. Never overwrite unrelated local changes to manufacture a clean checkpoint.
