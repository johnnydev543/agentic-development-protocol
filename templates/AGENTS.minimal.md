# Agent Rules

Classify work using `policies/MODEL_ROUTING.md`. L0-L3 describes task decision risk, not model identity.

Every session must state Role, Assigned execution level, Maximum authorized level, and explicit scope. If required work exceeds the maximum, do not plan, decompose, design, edit, or implement it. Return only `ESCALATION_REQUIRED` with the policy package and stop.

Use `IMPLEMENT → REVIEW → FIX → RE-REVIEW → COMPLETE`. Verification is evidence inside implementation, fix, review, and re-review—not a separate role. Git checkpoints are optional review targets. After two materially different unsuccessful fixes, stop.

Persist stable `RVW-###` entries. REVIEW-AND-FIX may close verified localized low-risk findings; high-risk findings require fresh RE-REVIEW.
