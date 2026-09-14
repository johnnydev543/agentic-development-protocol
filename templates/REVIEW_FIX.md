# Review Fix Session

```text
SESSION AUTHORIZATION
Role: FIX
Assigned execution level: <L0/L1/L2/L3>
Maximum authorized level: <L0/L1/L2/L3>
Finding scope: <RVW-### IDs>

Read AGENTS.md, the selected findings in docs/review-findings.md, the controlling specification, and referenced files/tests.

If a required correction exceeds Maximum authorized level, do not plan, architecturally decompose, design, or edit. Output only ESCALATION_REQUIRED and stop.

Otherwise make the smallest correct fix, add regression coverage, and run every verification named by the finding plus relevant checks. Avoid unrelated refactoring.

After checks pass, normally set Status: FIXED-PENDING-REVIEW. Set FIXED directly only for a localized, unambiguous, low-risk fix that does not trigger mandatory RE-REVIEW. Record Fix summary and Verification result.
```
