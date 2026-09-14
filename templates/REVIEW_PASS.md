# Independent Review and Re-review Session

```text
SESSION AUTHORIZATION
Role: <REVIEW / REVIEW-AND-FIX / RE-REVIEW>
Assigned execution level: <L0/L1/L2/L3>
Maximum authorized level: <L0/L1/L2/L3>
Review scope: <checkpoint commit or explicit changed files/components>
Finding scope for RE-REVIEW: <RVW-### IDs or N/A>

Read AGENTS.md, policies/CODE_REVIEW.md, the controlling specification, the explicit review scope, relevant tests, and verification output. Use fresh context for meaningful changes.

Verification is part of this review. Inspect the implementer or fixer's recorded evidence, independently rerun the risk-relevant targeted checks, and add adversarial, regression, or domain-semantic cases when coverage is insufficient. A full-suite rerun is required only when the risk, affected surface, missing evidence, or low execution cost justifies it. Review authorization may reach L3.

REVIEW diagnoses only. REVIEW-AND-FIX may record, directly correct, verify, and close a localized, unambiguous, low-risk finding in this session. It must not use that mode for Blocker/Major, L3, architecture/interface/schema, security/safety, domain/provenance/timing, or uncertain-root-cause work.

RE-REVIEW checks the selected findings and fix scope. For each finding:
- pass → Status: FIXED with evidence;
- fail/regression → Status: OPEN with evidence;
- conflict with authoritative requirements → Status: NEEDS-REVIEW;
- distinct new defect → allocate a new RVW-###.

Do not delete or rewrite original findings. Report `Review result: CLEAN` or `FINDINGS`, `Verification: PASS`, `FAIL`, or `BLOCKED`, checks independently run, and residual verification limits. A clean review states that no Blocker/Major/Minor findings were found.

Optional standalone reports use the next NNNN_REVIEW_SCOPE.md number in docs/0000_DOCUMENT_INDEX.md; this sequence is independent of RVW-###.
```
