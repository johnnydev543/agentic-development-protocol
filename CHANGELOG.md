# Changelog

## v0.6 — 2026-09-16

- Renamed the project to Agentic Development Protocol.
- Added an active-ledger/archive policy and reusable archiving script so stable FIXED findings do not consume normal session context.

## v0.5 — 2026-09-14

- Removed named-model mappings and `MODEL_REGISTRY.md`; model selection now lives outside repository policy.
- Redefined L0-L3 as task decision risk rather than model capability.
- Added mandatory per-session Role and Maximum authorized level, with an optional natural-language Task.
- Added a hard authorization boundary: classification above the maximum requires immediate escalation before planning, decomposition, design, or edits.
- Replaced the mandatory HANDOFF lifecycle with IMPLEMENT → REVIEW → IMPLEMENT corrections → REVIEW → COMPLETE and an optional narrowly scoped L3 DECISION session.
- Restored Git only as an optional reproducible review checkpoint, not a model handoff prerequisite.
- Added `FIXED-PENDING-REVIEW`; a fresh REVIEW finalizes high-risk corrections as `FIXED`.
- Added optional PLAN and PLAN-REVIEW roles with `PLN-###` findings and a two-revision stop rule for structural plan rejection.
- Allowed PLAN-REVIEW to amend and approve plans directly, and added REVIEW-AND-FIX for verified localized low-risk defects; independent re-review remains mandatory for defined high-risk categories.
- Integrated verification into REVIEW and REVIEW-AND-FIX instead of retaining a separate VERIFY role. Review authorization may reach L3, and independent verification is risk-based rather than an unconditional full-suite rerun.
- Enforced one fixed role per session, merged FIX into IMPLEMENT and RE-REVIEW into REVIEW, and made normal review/finding scopes inferable from repository state.
- Simplified session input to Role, Maximum authorized level, and an optional natural-language Task; the session reports its inferred required level and effective scope.
- Allowed REVIEW-AND-FIX to review and correct through L3 while limiting final self-approval to eligible L0-L2 findings; its L3 corrections require fresh REVIEW and unresolved decisions route to DECISION.

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
