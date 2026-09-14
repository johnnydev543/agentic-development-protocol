# Agent Rules

## Authority

Use authoritative specifications, project rules, existing architecture, and tests. Do not invent domain semantics or broaden scope.

## Routing and Authorization

L0-L3 classifies task decision risk, not model capability. Every session must declare:

- Role: PLAN, PLAN-REVIEW, IMPLEMENT, REVIEW, REVIEW-AND-FIX, or DECISION.
- Maximum authorized level.
- Optional Task when repository state does not make scope unambiguous.

The role is fixed for the whole session. Infer and report the required level and effective scope. If any required work exceeds the maximum, stop before planning, architectural decomposition, design, file edits, or implementation. Output only `ESCALATION_REQUIRED` and the package from `policies/ESCALATION.md`. Detecting L3 does not authorize L3 work.

Large multi-file implementation may remain L2 when architecture, interfaces, schemas, semantics, and acceptance criteria are settled. Architectural decomposition is L3; mechanical subdivision under settled boundaries is not.

## Workflow

Use `IMPLEMENT → REVIEW → IMPLEMENT finding corrections → REVIEW → COMPLETE`. IMPLEMENT covers initial work and corrections; REVIEW covers initial and finding review. Verification is part of their evidence. There is no mandatory HANDOFF phase or handoff document.

Use optional PLAN → PLAN-REVIEW when implementation needs subdivision. L2 PLAN only divides settled work; task boundaries requiring architecture, interface/schema, or domain decisions are L3. Two failed structural revisions trigger escalation rather than another review loop.

Git checkpoints are recommended when they provide a reproducible review target, but they are not model handoffs or prerequisites. Do not overwrite unrelated changes to create one.

## Failure and Review

After two materially different unsuccessful fixes for the same failure, stop. Persist stable `RVW-###` findings. REVIEW-AND-FIX may review and correct to L3 but self-closes only eligible L0-L2 findings. Blocker/Major, L3, architecture/schema, security/safety, domain/provenance/timing, and uncertain-root-cause corrections require fresh REVIEW.

Run the tests, lint, type checks, and smoke checks appropriate to the scope and risk.
