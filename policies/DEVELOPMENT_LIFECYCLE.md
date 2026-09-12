# Staged Multi-Model Development Lifecycle

Use this lifecycle when the authoritative specification is sufficiently settled:

```text
SPEC FINAL → ARCHITECT → HANDOFF → IMPLEMENT → REVIEW → FIX → VERIFY
```

The phase describes where work is in delivery. `policies/MODEL_ROUTING.md` separately determines the L0-L3 reasoning level. A large implementation can remain L1/L2 when decisions are settled; a small semantic or architecture change can require L3.

## Canonical Ownership

Avoid restating complete policies across prompts and handoff files:

| Concern | Canonical source |
|---|---|
| Project/domain invariants | Project `AGENTS.md` |
| L0-L3 and phase-aware routing | `policies/MODEL_ROUTING.md` |
| Lifecycle and phase transitions | This file |
| Escalation and two-attempt rule | `policies/ESCALATION.md` |
| Review findings and fix status | `policies/CODE_REVIEW.md` |
| Durable document identity | `policies/DOCUMENT_NAMING.md` |
| Current architecture/tasks | `docs/implementation-handoff.md` |
| Current actionable findings | `docs/review-findings.md` |

Other documents should summarize only what is needed to perform their role and link to the canonical source for full rules.

## Minimum Context by Phase

Do not instruct an agent to read every policy, template, specification, or historical review. Load only:

| Phase | Required governance context |
|---|---|
| ARCHITECT | `AGENTS.md`, this lifecycle, authoritative spec, relevant architecture/code/tests |
| IMPLEMENT | `AGENTS.md`, selected `TASK-###` in the handoff, controlling spec, affected code/tests |
| REVIEW | `AGENTS.md`, `CODE_REVIEW.md`, controlling spec, intended Git diff, verification output |
| FIX | `AGENTS.md`, selected `RVW-###`, controlling spec, affected code/tests |
| VERIFY | Acceptance criteria, requested verification, affected checks |

Read `MODEL_ROUTING.md` or the model registry only when classification/model selection is still required. Read `DOCUMENT_NAMING.md` only when creating a durable document. Templates are entry prompts for their own phase, not a set to load together.

## 1. SPEC FINAL

Identify the controlling specification and confirm it is stable enough to constrain implementation. Route unresolved, conflicting, or unsupported semantic decisions to L3 before coding.

## 2. ARCHITECT

A high-capability model establishes the decisions that constrain later work:

- module/package boundaries and dependency direction;
- core models, interfaces, protocols, schemas, and types;
- bootstrap and shared infrastructure patterns;
- repository/service/provider abstractions;
- high-risk or highly coupled core logic;
- representative implementation patterns;
- minimal smoke/architecture tests.

Stop when remaining work can be completed without reinterpreting architecture or domain semantics. Do not consume the architecture phase on repetitive adapters, endpoints, boilerplate, exhaustive edge cases, or polish.

## 3. HANDOFF

Create or update `docs/implementation-handoff.md` with:

- specification and architecture Git baselines;
- architecture completed;
- task-specific architecture invariants;
- remaining implementation tasks;
- high-risk remaining work.

Use this task structure:

```text
#### TASK-001: <name>
Status: TODO
Routing: <L0 / L1 / L2>
Baseline commit: <sha>
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

Prefer independently executable tasks affecting roughly one to three modules. Keep unresolved architecture/domain decisions under High-risk remaining work rather than disguising them as routine tasks.

## 4. IMPLEMENT

Execute one selected handoff task at a time under the recorded architecture. Stay in scope, add the requested tests, run relevant checks, and stop if completion requires changing an invariant or making an unsupported decision. Mark `DONE` only after verification and record changed files, results, and task commit SHA. Do not automatically begin the next task.

## 5. REVIEW

Use fresh context for meaningful changes and a different model perspective when practical. The reviewer receives the original task, controlling spec, project rules, intended baseline diff, and verification output.

Follow `policies/CODE_REVIEW.md` for severity, `RVW-###` fields, persistence, and fix status. Review diagnoses; it does not silently redefine architecture or domain semantics. Number a standalone review artifact according to `DOCUMENT_NAMING.md`.

## 6. FIX

Use L0-L2 for localized, explicit, pattern-following findings covered by existing decisions. Route architecture, interface/schema, domain/provenance/timing ambiguity, or uncertain cross-module causes to L3.

Update the original finding in `docs/review-findings.md`. Do not mark it `FIXED` until requested verification passes; use `NEEDS-REVIEW` with evidence when the finding conflicts with an authoritative source.

## 7. VERIFY

Run the subset required by the task and risk: unit/integration tests, lint, type checks, build/import/startup smoke checks, and defect regression tests. Re-review high-risk fixes when they materially change architecture/domain behavior or when requested by the reviewer.

## Git as the Handoff Backbone

```text
architecture baseline → TASK commits → review findings → RVW fix commits → verification
```

Review the intended Git range rather than an undifferentiated repository snapshot. Repository ledgers and Git history, not chat context alone, are the cross-session system of record.
