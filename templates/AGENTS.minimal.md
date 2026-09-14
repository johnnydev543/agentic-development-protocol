# Agent Rules

Classify work using `policies/MODEL_ROUTING.md`. L0-L3 describes task decision risk, not model identity.

Every session states Role and Maximum authorized level; Task is optional when repository state makes scope unambiguous. The role is fixed for the whole session. Infer and report required level and scope before acting. If required work exceeds the maximum, return only `ESCALATION_REQUIRED` with the policy package and stop.

Use `IMPLEMENT → REVIEW → IMPLEMENT corrections → REVIEW → COMPLETE`. IMPLEMENT covers task work and finding correction; REVIEW covers initial and finding review. Verification is evidence inside both roles. Git checkpoints are optional review targets. After two materially different unsuccessful fixes, stop.

Persist stable `RVW-###` entries. REVIEW-AND-FIX may review and correct to L3 but self-closes only eligible L0-L2 findings; high-risk corrections require fresh REVIEW.
