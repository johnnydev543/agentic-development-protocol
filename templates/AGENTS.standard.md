# AGENTS.md — Standard

## Core Principles

- Inspect relevant existing code before editing.
- Follow the authoritative specification and existing project conventions.
- Prefer the smallest correct change over broad refactoring.
- Add or update tests when behavior changes.
- Run relevant tests and configured lint/type checks.
- Do not silently reinterpret requirements.
- Do not invent missing domain rules, mappings, timestamps, or values.
- Use strong models for decisions; use lower-cost models for execution once the decision is explicit.

## Task Routing

Before substantial work, classify the task internally:

- L0 — fast/mechanical.
- L1 — routine implementation.
- L2 — complex engineering.
- L3 — architecture/high uncertainty.

Do not force every task to start at L0/L1. Route directly to L3 when architecture or unsupported domain interpretation is already required.

If the solution is specified and only implementation remains, prefer L0-L2.

The agent must not claim that it switched models unless the environment actually did so.

## Development Phase

Also identify the current phase:

- SPEC FINAL
- ARCHITECT
- HANDOFF
- IMPLEMENT
- REVIEW
- FIX
- VERIFY

Task level and phase are separate. A large IMPLEMENT task may still belong to L1/L2 if architecture is settled; a small FIX may require L3 if it changes architecture or semantics.

### Architecture pass

When acting as architect, establish module boundaries, interfaces, schemas, dependency direction, shared infrastructure, high-risk core logic, and representative reference implementations.

Do not continue into repetitive implementation merely to make the product feature-complete.

Create/update `docs/implementation-handoff.md` with architecture completed, architecture invariants, remaining implementation tasks, and high-risk remaining work.

### Delegated implementation

When implementing from `docs/implementation-handoff.md`:

- execute one selected task at a time;
- follow existing architecture/reference patterns;
- stay within scope;
- add required tests;
- stop instead of redesigning architecture when blocked;
- mark the task DONE only after verification passes;
- do not automatically begin the next task.

## Escalation

At L0/L1, after 2 materially different unsuccessful fixes for the same failure, STOP and recommend L2 (or L3 for architecture/domain uncertainty).

At L2, after 2 materially different unsuccessful fixes, STOP and recommend L3 when deeper reasoning is required.

At L3, do not recommend L3 again merely because the task is hard. Stop for missing authoritative semantics/data, conflicting requirements, or when independent review is needed.

Never make a third speculative modification after the two-attempt threshold.

### Escalation Output

Include:

- Current routing level.
- Recommended next level.
- Suggested model, if model selection exists.
- Reason.
- Current task.
- Exact observed failure.
- Materially different attempts and outcomes.
- Evidence-supported suspected root cause.
- Relevant files/tests.
- Important constraints.
- Precise next question.

## Review Gate

Ordinary changes: run the relevant unit/integration tests and configured lint/type checks.

High-risk changes: prefer fresh-context independent review, ideally by a different model. The reviewer receives the task, specification, project rules, architecture/handoff constraints, git diff, and verification output.

Review findings should be classified as Blocker, Major, Minor, or Suggestion and should use stable finding IDs such as `RVW-001`.

Persist cross-session findings in `docs/review-findings.md` rather than relying on chat history.

A reviewer must not silently redefine domain semantics.

## Review Fix

Do not assume the reviewer must perform the fix.

Use a lower-cost model for a localized, explicit, pattern-following fix covered by existing architecture and tests.

Escalate the fix to L3 when the finding exposes an architecture flaw, interface/schema decision, unsupported domain meaning, uncertain root cause, or high-risk cross-module semantic change.

After fixing, update the original finding rather than deleting it:

- `Status: FIXED`
- concise fix summary
- verification performed
- commit SHA if available

A finding is not FIXED merely because code changed; verification must pass.

## Git Discipline

Use Git as the handoff backbone.

Prefer clear phase/task commits such as:

- `arch: establish core application architecture`
- `feat: implement TASK-001 ...`
- `fix: resolve RVW-003 ...`

Review against the correct baseline/diff rather than an undifferentiated repository snapshot.

## Document Identity

For new specifications, plans, architecture records, standalone reviews, reports, and similar durable artifacts, follow `policies/DOCUMENT_NAMING.md`.

- Allocate the next repository-wide four-digit ID.
- Use `NNNN_TYPE_SCOPE.md` and register it in `docs/0000_DOCUMENT_INDEX.md`.
- Keep created/updated dates, status, version, and Git baseline inside the document rather than the filename.
- Do not renumber or mass-rename existing documents as part of unrelated work.
- Preserve stable well-known paths such as `README.md`, `AGENTS.md`, `docs/implementation-handoff.md`, and `docs/review-findings.md`.

## Efficiency

Use strong models to resolve uncertainty and lower-cost models to execute known solutions.

Do not escalate merely because a task is large. Escalate because uncertainty, risk, repeated failure, or domain judgment exceeds the current level.
