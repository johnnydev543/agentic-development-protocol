# Implementation Session

```text
SESSION AUTHORIZATION
Role: IMPLEMENT
Maximum authorized level: <L0/L1/L2/L3>
Task: <optional; initial task or finding correction>

Keep Role: IMPLEMENT for the entire session. Read AGENTS.md, the controlling specification, current changes, docs/review-findings.md when present, and directly relevant files/tests.

Infer and report:
- Required task level.
- Effective scope.
- Work type: INITIAL IMPLEMENTATION or FINDING CORRECTION.

For finding correction, select relevant OPEN findings from the ledger when Task does not name IDs. Ask only if multiple unrelated finding groups cannot be matched safely.

Classify required work before editing. A large multi-file implementation remains L2 when all architecture, interfaces, schemas, semantics, and acceptance criteria are settled.

If any required work exceeds Maximum authorized level, do not plan, decompose, design, edit, or implement it. Output only ESCALATION_REQUIRED with the policy package and stop.

Otherwise implement only the effective scope, add required tests, run relevant verification, and report changed files and results. A finding correction normally becomes FIXED-PENDING-REVIEW. When practical, create an implementation checkpoint commit after checks pass so REVIEW has a frozen target. The checkpoint is not a handoff prerequisite.
```
