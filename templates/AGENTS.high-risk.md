# AGENTS.md — High Risk

## Core Principles

- Never invent authoritative values, business rules, mappings, source facts, or domain semantics.
- Preserve source/provenance and historical records.
- Inspect existing code, schemas, tests, and specifications before editing.
- Prefer the smallest correct change.
- Separate diagnosis from implementation when root cause is uncertain.
- Do not weaken validation or tests merely to obtain a passing run.

## Routing

Classify substantial work as L0/L1/L2/L3 using the shared routing policy.

Route directly to L3 when work requires architecture, ambiguous domain semantics, provenance interpretation, information timing/ordering decisions, or high-impact data-model decisions.

Known solutions should be implemented by an appropriate lower-cost level.

## Escalation

After 2 materially different unsuccessful fixes for the same failure, STOP. No third speculative modification.

Stop immediately when the next change would require guessing:

- authoritative values,
- identity or category mappings,
- timestamps or ordering,
- source meaning,
- business/domain rules,
- or other semantics not established by a source/specification.

Produce the standard escalation package and hand off to the appropriate next level, clarification, or independent review.

## Data Integrity

Clearly distinguish:

- raw source data,
- parsed data,
- normalized data,
- derived metrics,
- model-generated interpretation.

Model-generated interpretation must not be persisted or presented as authoritative source data unless the specification explicitly defines it as model-derived.

Historical records must not be silently overwritten when history is part of the domain model.

## Review Gate

Independent review is required or strongly preferred for changes affecting:

- domain calculations,
- extraction/normalization semantics,
- identity/mapping logic,
- timestamps or information cutoffs,
- source provenance,
- historical mutation/versioning,
- database schema for critical data,
- cross-module architecture.

Prefer a fresh reviewer with a different model perspective when practical.

The reviewer must receive the task, specification, project rules, git diff, and verification output and classify findings as Blocker/Major/Minor/Suggestion.

## Efficiency

Strong models resolve uncertainty. Lower-cost models execute known solutions. Cost optimization never justifies inventing or weakening domain truth.
