# Finding Correction Session

```text
SESSION AUTHORIZATION
Role: IMPLEMENT
Maximum authorized level: <L0/L1/L2/L3>
Task: <optional RVW-### IDs; infer relevant OPEN findings when omitted>

Keep Role: IMPLEMENT for the whole session. Read AGENTS.md, OPEN findings in docs/review-findings.md, the controlling specification, and referenced files/tests. Infer and report the relevant finding scope; ask only when unrelated OPEN groups cannot be matched safely.

If a required correction exceeds Maximum authorized level, do not plan, architecturally decompose, design, or edit. Output only ESCALATION_REQUIRED and stop.

Otherwise make the smallest correct fix, add regression coverage, and run every verification named by the finding plus relevant checks. Avoid unrelated refactoring.

After checks pass, set Status: FIXED-PENDING-REVIEW and record Fix summary and Verification result. A fresh Role: REVIEW session performs the finding review when required.
```
