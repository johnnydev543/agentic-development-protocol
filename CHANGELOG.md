# Changelog

## v0.2.1 — 2026-09-12

- Restored self-contained phase prompts after the context-deduplication experiment caused unreliable tool-driven reading in some model integrations.
- Removed the repository-wide durable-document numbering policy; stable `RVW-###` review finding IDs remain.
- Temporarily disabled Git-based phase handoff. Tasks, explicit change scope, review findings, and verification results are the handoff record.
- Retained lightweight four-digit numbering only for optional standalone review reports; `RVW-###` remains the independent actionable-finding sequence.

## v0.2 — 2026-09-12

- Added staged development lifecycle: SPEC FINAL → ARCHITECT → HANDOFF → IMPLEMENT → REVIEW → FIX → VERIFY.
- Added explicit separation between task level (L0-L3) and development phase.
- Added architecture-pass guidance so strong models establish module boundaries, interfaces, schemas, dependency direction, high-risk core logic, and reference implementations without consuming all repetitive implementation work.
- Added `docs/implementation-handoff.md` conventions for architecture invariants and task-by-task delegation.
- Added one-task-at-a-time implementation rules for Flash/lower-cost models.
- Added cross-session review persistence through `docs/review-findings.md` and stable `RVW-*` finding IDs.
- Added review-fix routing: explicit/local findings go to lower-cost models; architecture/schema/domain uncertainty routes back to strong models.
- Added fix-status conventions requiring verification before a finding can be marked FIXED.
- Added Git baseline/commit guidance for architecture, implementation, review, and fix phases.
- Added reusable prompt templates for architecture pass, delegated implementation, independent review, and review fix.
- Updated model registry with phase-based role mapping and cache/session considerations.
- Updated standard and high-risk `AGENTS.md` templates to include staged routing, handoff, review-fix, and Git discipline.

## v0.1 — 2026-09-05

- Added model-agnostic L0-L3 routing policy.
- Added two-attempt escalation threshold and structured handoff.
- Added risk-based code review policy.
- Added separate model registry for fast-changing model assignments.
- Added minimal, standard, and high-risk AGENTS templates.
- Added financial-project example.
