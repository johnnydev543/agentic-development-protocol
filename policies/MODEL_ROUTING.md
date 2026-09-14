# Task Routing and Session Authorization

## Separation of Concerns

L0-L3 classifies the task's decision risk. It is not a model ranking and does not claim that a named model can complete that level efficiently.

Model names, providers, product tiers, and reasoning-effort labels must not grant authority. Each session receives its authority explicitly.

## Task Levels

- **L0 — Mechanical:** search, renames, localized text/config edits, simple tests, and deterministic transformations with no semantic decision.
- **L1 — Routine implementation:** explicit local behavior, ordinary endpoints/adapters, straightforward fixes, and tests under settled contracts.
- **L2 — Complex implementation:** difficult debugging, dependency tracing, large or multi-file implementation where architecture, interfaces, schemas, and domain semantics are already authoritative.
- **L3 — Decision work:** architecture, interface/schema decisions, ambiguous or conflicting requirements, unsupported domain/provenance/timing interpretation, uncertain cross-module root cause, or another high-impact choice.

Repository size and file count do not by themselves make work L3. A large settled implementation may be L2; a ten-line semantic decision may be L3.

## Session Authorization

Every working session must state:

```text
Role: <PLAN / PLAN-REVIEW / IMPLEMENT / REVIEW / REVIEW-AND-FIX / DECISION>
Maximum authorized level: <L0 / L1 / L2 / L3>
Task: <optional natural-language scope; infer from repository state when omitted>
```

The role is fixed for the whole session. A new phase requires a new session; an IMPLEMENT session never turns itself into REVIEW. The maximum authorized level is an execution boundary, not an estimate of model intelligence. The agent infers and reports the required task level after inspecting the task and repository.

Model capability is a separate user selection. A highly capable model may perform L0 work, though it may cost more than necessary. Granting a weaker model L3 authority does not make it suitable for L3 decisions.

An agent may classify work above its maximum. Detection does not grant permission to perform it. If any required work exceeds the maximum authorized level, the agent must:

1. stop before planning, architectural decomposition, design, file edits, or implementation;
2. output only `ESCALATION_REQUIRED` and the package in `policies/ESCALATION.md`;
3. identify the unresolved decision that requires the higher level;
4. end the task.

It must not silently downgrade the task, create implementation tasks whose boundaries require unresolved L3 decisions, or continue merely because it believes itself capable.

Mechanical subdivision is allowed below L3 only when boundaries, interfaces, schemas, semantics, and acceptance criteria are already authoritative. Architectural decomposition is L3 decision work.

## Phase Routing

- **PLAN:** L2 when mechanically subdividing settled work; L3 when task boundaries require architecture, interface/schema, or domain decisions.
- **PLAN-REVIEW:** verify each task and directly amend the plan to an approvable form when authority is sufficient. Plan edits do not require another independent review.
- **IMPLEMENT:** handles both initial task work and correction of `RVW-###` findings. Normally L0-L2; L3 only with explicit authorization.
- **REVIEW:** authorize up to L3 according to change risk. Review includes independent, risk-based verification.
- **REVIEW-AND-FIX:** may review and correct up to L3 within session authorization. It may self-close only eligible localized L0-L2 findings. An L3 correction remains `FIXED-PENDING-REVIEW` for fresh REVIEW; an unresolved L3 decision routes to DECISION before correction.
- **DECISION:** resolve only the named L3 question and produce constraints plus acceptance criteria. Do not broaden into unrelated implementation.

Specialization may influence which model the user selects, but selection is external to this policy. Current model preferences belong in user/session configuration, not the repository.

## Scope Inference

Users should not have to copy commit hashes or finding IDs during a normal linear workflow. When `Task` is omitted, infer scope and state it before work:

- IMPLEMENT: use relevant `OPEN` findings when present; otherwise use the user request and current task state.
- REVIEW: use relevant `FIXED-PENDING-REVIEW` findings and their correction diff when present; otherwise review current working-tree changes, or the current branch/checkpoint change when the tree is clean.
- REVIEW-AND-FIX: infer the same scope as REVIEW.

Ask for scope only when multiple unrelated change groups exist, the base cannot be determined safely, findings cannot be matched to changes, or inference would materially broaden the task.
