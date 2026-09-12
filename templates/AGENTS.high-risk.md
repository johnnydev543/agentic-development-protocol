# AGENTS.md — High Risk

## Core Principles

- Never invent authoritative values, business rules, mappings, source facts, or domain semantics.
- Preserve source/provenance and historical records.
- Inspect existing code, schemas, tests, and specifications before editing.
- Prefer the smallest correct change.
- Separate diagnosis from implementation when root cause is uncertain.
- Do not weaken validation or tests merely to obtain a passing run.
- Use strong models for unresolved decisions; use lower-cost models only after semantics and architecture are explicit.

## Routing

Classify substantial work as L0/L1/L2/L3 using the shared routing policy.

Also identify the development phase: SPEC FINAL, ARCHITECT, HANDOFF, IMPLEMENT, REVIEW, FIX, or VERIFY.

Route directly to L3 when work requires architecture, ambiguous domain semantics, provenance interpretation, information timing/ordering decisions, or high-impact data-model decisions.

Known solutions should be implemented by an appropriate lower-cost level.

## Architecture and Handoff

For an architecture pass, establish the authoritative module boundaries, interfaces/schemas, dependency direction, source/provenance rules, shared infrastructure, high-risk core logic, and representative implementation patterns.

Do not consume strong-model time finishing repetitive implementation once lower-cost models can safely continue.

Persist the handoff in `docs/implementation-handoff.md`, including:

- architecture completed;
- architecture invariants;
- explicit remaining tasks with acceptance criteria and tests;
- high-risk remaining work that must not be delegated as routine implementation.

A delegated implementation agent must stop rather than silently change architecture or domain semantics to make a task easier.

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

The reviewer must receive the task, specification, project rules, architecture/handoff constraints, git diff, and verification output and classify findings as Blocker/Major/Minor/Suggestion.

Persist actionable cross-session findings in `docs/review-findings.md` with stable IDs such as `RVW-001`.

## Review Fix

A review finding does not automatically require the same strong model that found it.

Use a lower-cost model when the fix is explicit, localized, supported by existing semantics, and testable without architectural decisions.

Route back to L3 if the finding exposes an architecture flaw, schema/interface decision, ambiguous provenance/domain meaning, uncertain root cause, or another high-risk semantic decision.

After a successful fix, retain the original finding and mark it FIXED with a concise summary, verification evidence, and commit SHA when available. Never mark FIXED only because code changed.

## Git Discipline

Use explicit commits to preserve architecture and task baselines. Review the intended diff rather than the entire repository state whenever possible.

Recommended progression:

```text
architecture baseline → task commits → review findings → review-fix commits → verification
```

## Document Identity

Number new durable specifications, plans, architecture records, standalone review reports, and research/governance artifacts according to `policies/DOCUMENT_NAMING.md`.

Use the next repository-wide `NNNN_TYPE_SCOPE.md` identity and register it in `docs/0000_DOCUMENT_INDEX.md`. Keep dates, status, version, review provenance, and Git baselines inside the document. Never reuse an ID or mass-rename legacy documents during unrelated work. Stable tool-addressed files such as handoff and findings ledgers retain their fixed paths.

## Efficiency

Strong models resolve uncertainty. Lower-cost models execute known solutions. Cost optimization never justifies inventing or weakening domain truth.

Load only the policy, specification, task/finding, diff, and evidence required by the current phase. Do not preload all templates, historical reviews, or unrelated documents. Follow the minimum context matrix in `policies/DEVELOPMENT_LIFECYCLE.md`.
