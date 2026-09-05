# Model Routing Policy

## Core Rule

Use strong models to resolve uncertainty and lower-cost models to execute known solutions.

Routing is based on task uncertainty, risk, blast radius, and specialization—not model prestige.

## Levels

### L0 — Fast / Mechanical
Use for repository search, explanation, renames, localized config/text changes, simple logging, simple tests, and mechanical refactors with no domain-semantic change.

### L1 — Routine Implementation
Use for implementation from an explicit specification, CRUD/API work, schemas, adapters with already-defined semantics, straightforward bug fixes, routine frontend/backend work, and normal tests.

### L2 — Complex Engineering
Use for non-trivial multi-file changes, dependency tracing, difficult debugging with evidence, repo-scale implementation, reliability/performance work, and large tasks whose architecture and semantics are already defined.

### L3 — Architecture / High Uncertainty
Use for architecture design, conflicting or ambiguous specifications, difficult cross-module root-cause analysis, domain interpretation, source/provenance semantics, and high-impact data-model decisions.

## Direct Routing

Do not force every task to start at L0 or L1.

Route directly to L3 when the task already requires architectural judgment, unsupported domain interpretation, ambiguous provenance, high-risk timing/ordering semantics, or another decision not settled by an authoritative specification.

If the solution is already specified and only implementation remains, prefer L0-L2 execution.

## Specialist Routing

Specialization may override generic level selection. Frontend/UI-heavy work, security review, formal methods, data engineering, or other specialized workloads may use a specialist model appropriate to that domain.

## Model Identity

The agent must not claim that it switched models unless the execution environment actually performed the switch. If switching is unavailable, recommend the next routing level and provide a handoff package.
