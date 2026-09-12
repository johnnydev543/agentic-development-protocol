# AGENTS.md — Minimal

## Working Rules

- Inspect relevant existing code before editing.
- Prefer the smallest correct change.
- Follow authoritative specifications and project conventions.
- Add/update tests when behavior changes.
- Run relevant verification after implementation.
- Do not invent missing business/domain semantics.

## Routing

Classify substantial work as:

- L0: fast/mechanical.
- L1: routine implementation.
- L2: complex engineering.
- L3: architecture/high uncertainty.

Use the project's model registry when model selection is available.

Load policies, templates, specifications, and historical reviews only when the current phase/task requires them. Do not read the full documentation tree by default.

## Escalation

After 2 materially different unsuccessful fixes for the same failure, STOP. Do not make a third speculative modification.

Provide an escalation report containing the current level, recommended next level, failure, attempts, suspected root cause, relevant files/tests, constraints, and precise next question.

If the blocker requires unsupported domain assumptions or missing authoritative data, stop immediately and request clarification.

## Review

Use tests/lint/type checks as appropriate. High-risk changes should receive a fresh independent review when practical.

## Documents

Follow `policies/DOCUMENT_NAMING.md` for new durable specifications, plans, architecture records, standalone reviews, and reports. Allocate the next `NNNN_TYPE_SCOPE.md` ID in `docs/0000_DOCUMENT_INDEX.md`; keep dates and mutable status inside the document. Preserve conventional stable-path files and do not mass-rename legacy documents during unrelated work.
