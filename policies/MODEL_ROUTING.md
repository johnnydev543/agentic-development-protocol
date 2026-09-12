# Model Routing Policy

## Core Rule

Use strong models to resolve uncertainty and lower-cost models to execute known solutions.

Routing is based on task uncertainty, risk, blast radius, and specialization—not model prestige.

## Two Dimensions of Routing

Use both dimensions together:

1. **Task level (L0-L3)** — how much reasoning capacity and judgment this task requires.
2. **Development phase** — whether the repository is currently in architecture, delegated implementation, review, review-fix, or verification.

A large implementation task does not automatically require a strong model if architecture and semantics are already settled. Conversely, a small-looking change may require L3 if it changes an interface, schema, provenance rule, or other high-impact semantic decision.

See `policies/DEVELOPMENT_LIFECYCLE.md` for the staged workflow.

## Levels

### L0 — Fast / Mechanical
Use for repository search, explanation, renames, localized config/text changes, simple logging, simple tests, and mechanical refactors with no domain-semantic change.

### L1 — Routine Implementation
Use for implementation from an explicit specification, CRUD/API work, schemas, adapters with already-defined semantics, straightforward bug fixes, routine frontend/backend work, and normal tests.

### L2 — Complex Engineering
Use for non-trivial multi-file changes, dependency tracing, difficult debugging with evidence, repo-scale implementation, reliability/performance work, and large tasks whose architecture and semantics are already defined.

### L3 — Architecture / High Uncertainty
Use for architecture design, conflicting or ambiguous specifications, difficult cross-module root-cause analysis, domain interpretation, source/provenance semantics, and high-impact data-model decisions.

## Phase-Aware Routing

### Architecture pass

Prefer L3 for decisions that define:

- module/package boundaries;
- interfaces/protocols/contracts;
- schemas and dependency direction;
- shared infrastructure patterns;
- cross-module orchestration;
- high-risk core logic.

The architecture model should establish reference patterns and then stop before repetitive implementation is exhausted.

### Delegated implementation

Once architecture, semantics, and acceptance criteria are explicit, prefer L0-L2 depending on task size and coupling. Pattern-following work should not remain on L3 merely because L3 created the architecture.

### Review

Review capacity should reflect risk rather than implementation cost. High-risk or cross-module changes should receive fresh-context independent review, preferably with a different model perspective.

### Review fix

Do not automatically use the review model to implement its own findings.

Prefer L0-L2 when a finding is localized, explicit, and testable under existing architecture. Route the fix to L3 when the finding exposes an architecture flaw, schema/interface decision, ambiguous semantics, uncertain root cause, or other high-risk judgment.

## Direct Routing

Do not force every task to start at L0 or L1.

Route directly to L3 when the task already requires architectural judgment, unsupported domain interpretation, ambiguous provenance, high-risk timing/ordering semantics, or another decision not settled by an authoritative specification.

If the solution is already specified and only implementation remains, prefer L0-L2 execution.

## Specialist Routing

Specialization may override generic level selection. Frontend/UI-heavy work, security review, formal methods, data engineering, or other specialized workloads may use a specialist model appropriate to that domain.

## Model Identity

The agent must not claim that it switched models unless the execution environment actually performed the switch. If switching is unavailable, recommend the next routing level and provide a handoff package.
