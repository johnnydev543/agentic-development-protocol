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
Role: <PLAN / PLAN-REVIEW / IMPLEMENT / REVIEW / REVIEW-AND-FIX / FIX / RE-REVIEW / DECISION>
Assigned execution level: <L0 / L1 / L2 / L3>
Maximum authorized level: <L0 / L1 / L2 / L3>
Task or review scope: <explicit scope>
```

The maximum authorized level is an execution boundary, not an estimate of model intelligence.

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
- **IMPLEMENT:** normally L0-L2. L3 implementation is allowed only when the session explicitly has L3 authority.
- **REVIEW:** authorize up to L3 according to change risk. Review includes independent, risk-based verification.
- **REVIEW-AND-FIX:** allowed for localized, unambiguous, low-risk corrections within the session maximum. Record the finding, fix it, run verification, and close it in one session.
- **FIX:** L0-L2 for an explicit localized correction; L3 for architecture, semantics, or uncertain root cause.
- **RE-REVIEW:** independently review and verify the selected findings and fix scope; authorization may reach L3.
- **DECISION:** resolve only the named L3 question and produce constraints plus acceptance criteria. Do not broaden into unrelated implementation.

Specialization may influence which model the user selects, but selection is external to this policy. Current model preferences belong in user/session configuration, not the repository.
