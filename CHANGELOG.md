# Changelog

## v0.4 — 2026-09-12

- Assigned one canonical source to routing, lifecycle, escalation, review, document identity, handoff tasks, and review findings.
- Added a minimum context matrix for ARCHITECT, IMPLEMENT, REVIEW, FIX, and VERIFY.
- Explicitly prohibited preloading all policies, templates, specifications, historical reviews, or model-selection material for every task.
- Reduced duplicated review/fix schema and implementation rules in phase prompts by referring to their canonical policy or ledger.
- Clarified that project/domain invariants belong in `AGENTS.md` while task-specific invariants belong in the handoff.

## v0.3 — 2026-09-12

- Added stable repository-wide document IDs using `NNNN_TYPE_SCOPE.md` for new specifications, plans, architecture records, standalone reviews, reports, and runbooks.
- Moved dates, status, version, and Git baselines into document metadata so routine updates do not rename files or break links.
- Reserved `docs/0000_DOCUMENT_INDEX.md` as the allocation registry and added a reusable index template.
- Defined stable-path exceptions for conventional and tool-addressed files such as `README.md`, `AGENTS.md`, implementation handoff, and review findings ledgers.
- Made the policy prospective to avoid unsafe mass-renaming of existing documents.
- Added concurrent-branch collision handling and clarified that document, task, and review-finding IDs use separate sequences.

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
