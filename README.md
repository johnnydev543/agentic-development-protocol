# Agentic Development Protocol

A model-agnostic policy for authorized coding sessions, review checkpoints, escalation, and verified repair.

## Core Principle

L0-L3 describes the task's decision risk, not a permanent ranking of models. Model names, providers, product tiers, and reasoning-effort labels are intentionally absent from repository policy.

Every session receives an explicit role and execution ceiling:

```text
Role: IMPLEMENT
Maximum authorized level: L2
Task: <optional natural-language scope>
```

One session keeps one role from beginning to end. Starting REVIEW means starting a new session; IMPLEMENT does not switch itself into REVIEW. The agent infers and reports the required level and effective scope. If required work exceeds the maximum, recognizing the higher level does not authorize the agent to perform it.

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
| `IMPLEMENT` | Implement a new task or correct existing `RVW-###` findings | Normally L0-L2; L3 only with explicit authorization |
| `REVIEW` | Review initial implementation or corrected findings, independently verify, and update `RVW-###` records without modifying production code | Up to L3, matching the reviewed change's risk |
| `REVIEW-AND-FIX` | Review and correct up to L3 within authorization; only eligible localized L0-L2 findings may be self-closed | Review/correction up to L3; final self-approval up to L2 |

Every session must explicitly provide:

```text
Role
Maximum authorized level
Task (optional when repository state is unambiguous)
```

These fields are authorization, not a claim about the selected model's inherent capability. A highly capable model can perform L0 work; granting a weaker model L3 authority does not make it capable of reliable L3 decisions.

## Development Workflow

```text
[optional PLAN → PLAN-REVIEW]
                 ↓
IMPLEMENT
   ↓ implementation checkpoint
REVIEW
   ↓ RVW-### findings
IMPLEMENT finding corrections
   ↓ correction checkpoint / FIXED-PENDING-REVIEW
REVIEW
   ↓ FIXED, OPEN, or NEEDS-REVIEW
COMPLETE
```

There is no separate FIX or RE-REVIEW role: IMPLEMENT also corrects findings, and REVIEW also reviews corrections. There is no mandatory HANDOFF phase or `docs/implementation-handoff.md`. If implementation encounters an unresolved L3 question, use a narrowly scoped DECISION session, then return to IMPLEMENT.

When a complex implementation must first be split, use PLAN rather than IMPLEMENT. PLAN is L2 if it only subdivides settled work, and L3 if task boundaries require architecture/interface/schema/domain decisions. A PLAN-REVIEW session either approves it or records `PLN-###` findings; after two failed structural revisions, escalate instead of looping.

Git commits are optional reproducible review checkpoints, not model handoffs. A reviewer may receive a checkpoint commit or an explicitly named working-tree scope. Agents must not require phase-specific commits before proceeding or overwrite unrelated changes to manufacture a clean tree.

Verification is not a separate final role. IMPLEMENT submits affected-scope evidence for initial work and corrections. REVIEW and REVIEW-AND-FIX independently inspect it and rerun or extend checks according to risk. They need not rerun the full suite when targeted evidence is sufficient.

### Scope without manual bookkeeping

In a normal linear workflow, `Task` may be omitted. The new session infers and reports scope from the user request, current diff, branch/checkpoint state, and `docs/review-findings.md`:

- IMPLEMENT prefers relevant `OPEN` findings when correcting reviewed work.
- REVIEW prefers relevant `FIXED-PENDING-REVIEW` findings and their correction diff; otherwise it reviews current implementation changes.
- Ask the user only when multiple unrelated change groups or an unsafe base ambiguity prevents reliable inference.

### Fast path

REVIEW-AND-FIX is useful when the result is not known in advance. It reviews first, then routes each result:

```text
IMPLEMENT → REVIEW-AND-FIX
                 ├─ CLEAN → COMPLETE
                 ├─ eligible L0-L2 finding → correct + verify → FIXED
                 ├─ settled L3 finding → correct + verify → FIXED-PENDING-REVIEW
                 └─ unresolved L3 decision → OPEN → separate DECISION
```

An L3-authorized REVIEW-AND-FIX session may diagnose and correct L3 work within settled authority. It cannot finally approve its own L3 correction: the result remains `FIXED-PENDING-REVIEW` for a fresh REVIEW session. If the correction requires an unresolved architecture, schema, domain, provenance, or timing decision, leave it `OPEN` and route the decision to a separate DECISION session.

### L3 decision path

When any role detects unauthorized L3 work:

```text
current role
    ↓ ESCALATION_REQUIRED
DECISION
    ↓ authoritative decision and acceptance criteria
return to PLAN or IMPLEMENT
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

Use REVIEW-AND-FIX to close eligible localized L0-L2 defects in one verified session. Blocker/Major, L3, architecture/schema, security/safety, domain/provenance/timing, and uncertain-root-cause corrections require a fresh REVIEW session. New defects receive new IDs.

Optional standalone review reports use `NNNN_REVIEW_SCOPE.md` and the lightweight `docs/0000_DOCUMENT_INDEX.md`. This document-number sequence is independent of `RVW-###` and does not apply to specs, plans, architecture records, or policies.

Stable `FIXED` findings move out of the active ledger into numbered files under `docs/review-archive/`. Active sessions do not read archives by default. See `policies/REVIEW_ARCHIVE.md` and `scripts/archive_review_findings.py`.

## Failure Rule

After two materially different unsuccessful fixes for the same failure, stop. Do not attempt a third speculative change. Return the evidence package in `policies/ESCALATION.md`.

## Session Examples

Each block below starts a separate session. The role never changes inside a block.

### Session A — initial implementation

```text
Role: IMPLEMENT
Maximum authorized level: L2

Complete the current development task.
```

The session reports its inferred task level and scope, implements, tests, and leaves reviewable changes.

### Session B — initial review

```text
Role: REVIEW
Maximum authorized level: L3

Review the previous implementation session's result.
```

The session infers the current change scope, performs risk-based verification, and returns `CLEAN` or records `RVW-###` findings.

### Session C — finding correction

```text
Role: IMPLEMENT
Maximum authorized level: L3

Correct the current open review findings.
```

The session infers the relevant `OPEN` findings, corrects only that scope, records verification, and changes them to `FIXED-PENDING-REVIEW`.

### Session D — review corrected findings

```text
Role: REVIEW
Maximum authorized level: L3

Review the previous correction session's result.
```

The session infers relevant `FIXED-PENDING-REVIEW` findings and their diff, then sets each to `FIXED`, `OPEN`, or `NEEDS-REVIEW`. This is ordinary REVIEW, not a separate RE-REVIEW role.

### Optional explicit scope

Add `Task` only when the repository contains multiple unrelated targets:

```text
Role: REVIEW
Maximum authorized level: L3
Task: Review RVW-012 and RVW-014 in the ingestion pipeline only.
```

## Repository Structure

```text
policies/
  MODEL_ROUTING.md
  DEVELOPMENT_LIFECYCLE.md
  ESCALATION.md
  CODE_REVIEW.md
  REVIEW_ARCHIVE.md
templates/
  SESSION_AUTHORIZATION.md
  PLAN_TASKS.md
  DECISION_PASS.md
  IMPLEMENT_TASK.md
  REVIEW_PASS.md
  FINDING_CORRECTION.md
  REVIEW_DOCUMENT_INDEX.md
  AGENTS.minimal.md
  AGENTS.standard.md
  AGENTS.high-risk.md
examples/
  financial-project/AGENTS.md
scripts/
  archive_review_findings.py
```

## Adoption

1. Copy the suitable `AGENTS.*.md` template into the project as `AGENTS.md`.
2. Add project-specific authority, domain constraints, and verification commands.
3. Start each working session with `SESSION_AUTHORIZATION.md`.
4. If needed, use `PLAN_TASKS.md` to split and approve complex implementation work.
5. Use `IMPLEMENT_TASK.md`, then a fresh `REVIEW_PASS.md` session.
6. Correct findings in a new IMPLEMENT session using `FINDING_CORRECTION.md`, then start another REVIEW session with `REVIEW_PASS.md`.
7. Keep personal model preferences outside the repository and change them as empirical performance changes.
