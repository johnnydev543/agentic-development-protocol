# AI Agent Routing

A model-agnostic policy for authorized coding sessions, review checkpoints, escalation, and verified repair.

## Core Principle

L0-L3 describes the task's decision risk, not a permanent ranking of models. Model names, providers, product tiers, and reasoning-effort labels are intentionally absent from repository policy.

Every session receives an explicit role and execution ceiling:

```text
Role: IMPLEMENT
Assigned execution level: L1
Maximum authorized level: L2
Task scope: <explicit scope>
```

If required work exceeds the maximum, recognizing the higher level does not authorize the agent to perform it. It must stop before planning, architectural decomposition, design, or edits and return `ESCALATION_REQUIRED`.

## L0-L3

| Level | Meaning |
|---|---|
| L0 | Mechanical work with no semantic decision |
| L1 | Routine implementation under explicit contracts |
| L2 | Complex or repo-scale implementation with settled architecture and semantics |
| L3 | Architecture, interface/schema, ambiguous semantics, uncertain root cause, or another high-impact decision |

Complexity and risk are different. A large settled implementation can be L2; a small semantic change can be L3.

## Roles

| Role | Responsibility | Typical authorization |
|---|---|---|
| `PLAN` | Subdivide complex requirements into independently executable tasks without writing production code | L2 under settled boundaries; L3 when task boundaries require new decisions |
| `PLAN-REVIEW` | Review and, when authorized, directly amend a plan; return `PLAN_APPROVED` or blocking `PLN-###` findings | Usually L3 for plans involving architecture or domain risk |
| `DECISION` | Resolve one explicit architecture, interface/schema, domain-semantic, provenance, timing, or other high-impact question | L3 |
| `IMPLEMENT` | Implement an explicit scope under authoritative specifications and settled decisions | Normally L0-L2; L3 only with explicit authorization |
| `REVIEW` | Diagnose defects and independently perform risk-based verification; record stable `RVW-###` findings without modifying production code | Up to L3, matching the reviewed change's risk |
| `REVIEW-AND-FIX` | Review, directly correct, verify, and close localized, unambiguous, low-risk defects in one session | Normally L0-L2 |
| `FIX` | Correct only the selected `RVW-###` findings without reopening the entire review scope | L0-L2 for explicit fixes; L3 for decision-heavy or uncertain fixes |
| `RE-REVIEW` | Independently review and verify selected fixes, then set `FIXED`, `OPEN`, or `NEEDS-REVIEW` | Up to L3, matching the original finding's risk |

Every session must explicitly provide:

```text
Role
Assigned execution level
Maximum authorized level
Task or review scope
```

These fields are authorization, not a claim about the selected model's inherent capability.

## Development Workflow

```text
[optional PLAN → PLAN-REVIEW]
                 ↓
IMPLEMENT
   ↓ implementation checkpoint
REVIEW
   ↓ RVW-### findings
FIX
   ↓ fix checkpoint / FIXED-PENDING-REVIEW
RE-REVIEW
   ↓ FIXED, OPEN, or NEEDS-REVIEW
COMPLETE
```

There is no mandatory HANDOFF phase or `docs/implementation-handoff.md`. If implementation encounters an unresolved L3 question, use a narrowly scoped DECISION session, then return to IMPLEMENT or FIX.

When a complex implementation must first be split, use PLAN rather than IMPLEMENT. PLAN is L2 if it only subdivides settled work, and L3 if task boundaries require architecture/interface/schema/domain decisions. A PLAN-REVIEW session either approves it or records `PLN-###` findings; after two failed structural revisions, escalate instead of looping.

Git commits are optional reproducible review checkpoints, not model handoffs. A reviewer may receive a checkpoint commit or an explicitly named working-tree scope. Agents must not require phase-specific commits before proceeding or overwrite unrelated changes to manufacture a clean tree.

Verification is not a separate final role. IMPLEMENT and FIX submit their own affected-scope verification evidence. REVIEW, REVIEW-AND-FIX, and RE-REVIEW independently inspect that evidence and rerun or extend the checks required by risk. They need not rerun the full suite when targeted evidence is sufficient.

### Fast path

Use this only for localized, unambiguous, low-risk findings:

```text
IMPLEMENT → REVIEW-AND-FIX → COMPLETE
```

### L3 decision path

When any role detects unauthorized L3 work:

```text
current role
    ↓ ESCALATION_REQUIRED
DECISION
    ↓ authoritative decision and acceptance criteria
return to PLAN, IMPLEMENT, or FIX
```

The detecting agent must not perform the L3 decision merely because it classified the task correctly.

## Review Records

Persist actionable findings in `docs/review-findings.md`:

```text
## RVW-001 — Major
Status: OPEN
Review scope: <checkpoint or files/components>
Finding: ...
Required fix: ...
Verification required: ...
Fix summary: ...
Verification result: ...
```

Allowed states:

- `OPEN`
- `FIXED-PENDING-REVIEW`
- `FIXED`
- `NEEDS-REVIEW`

Use REVIEW-AND-FIX to close localized, unambiguous, low-risk defects in one verified session. Blocker/Major, L3, architecture/schema, security/safety, domain/provenance/timing, and uncertain-root-cause fixes require fresh RE-REVIEW. New defects receive new IDs.

Optional standalone review reports use `NNNN_REVIEW_SCOPE.md` and the lightweight `docs/0000_DOCUMENT_INDEX.md`. This document-number sequence is independent of `RVW-###` and does not apply to specs, plans, architecture records, or policies.

## Failure Rule

After two materially different unsuccessful fixes for the same failure, stop. Do not attempt a third speculative change. Return the evidence package in `policies/ESCALATION.md`.

## Repository Structure

```text
policies/
  MODEL_ROUTING.md
  DEVELOPMENT_LIFECYCLE.md
  ESCALATION.md
  CODE_REVIEW.md
templates/
  SESSION_AUTHORIZATION.md
  PLAN_TASKS.md
  DECISION_PASS.md
  IMPLEMENT_TASK.md
  REVIEW_PASS.md
  REVIEW_FIX.md
  REVIEW_DOCUMENT_INDEX.md
  AGENTS.minimal.md
  AGENTS.standard.md
  AGENTS.high-risk.md
examples/
  financial-project/AGENTS.md
```

## Adoption

1. Copy the suitable `AGENTS.*.md` template into the project as `AGENTS.md`.
2. Add project-specific authority, domain constraints, and verification commands.
3. Start each working session with `SESSION_AUTHORIZATION.md`.
4. If needed, use `PLAN_TASKS.md` to split and approve complex implementation work.
5. Use `IMPLEMENT_TASK.md`, then a fresh `REVIEW_PASS.md` session.
6. Fix selected findings with `REVIEW_FIX.md` and use `REVIEW_PASS.md` again as RE-REVIEW.
7. Keep personal model preferences outside the repository and change them as empirical performance changes.
