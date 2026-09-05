# AGENTS.md — Standard

## Core Principles

- Inspect relevant existing code before editing.
- Follow the authoritative specification and existing project conventions.
- Prefer the smallest correct change over broad refactoring.
- Add or update tests when behavior changes.
- Run relevant tests and configured lint/type checks.
- Do not silently reinterpret requirements.
- Do not invent missing domain rules, mappings, timestamps, or values.

## Task Routing

Before substantial work, classify the task internally:

- L0 — fast/mechanical.
- L1 — routine implementation.
- L2 — complex engineering.
- L3 — architecture/high uncertainty.

Do not force every task to start at L0/L1. Route directly to L3 when architecture or unsupported domain interpretation is already required.

If the solution is specified and only implementation remains, prefer L0-L2.

The agent must not claim that it switched models unless the environment actually did so.

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

High-risk changes: prefer fresh-context independent review, ideally by a different model. The reviewer receives the task, specification, project rules, git diff, and verification output.

Review findings should be classified as Blocker, Major, Minor, or Suggestion.

A reviewer must not silently redefine domain semantics.

## Efficiency

Use strong models to resolve uncertainty and lower-cost models to execute known solutions.

Do not escalate merely because a task is large. Escalate because uncertainty, risk, repeated failure, or domain judgment exceeds the current level.
