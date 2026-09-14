# Independent Review Session

```text
SESSION AUTHORIZATION
Role: <REVIEW / REVIEW-AND-FIX>
Maximum authorized level: <L0/L1/L2/L3>
Task: <optional natural-language scope>

Keep the selected role for the entire session. Read AGENTS.md, policies/CODE_REVIEW.md, the controlling specification, current changes, checkpoint/branch state, docs/review-findings.md, relevant tests, and submitted verification. Use fresh context for meaningful changes.

Infer and report:
- Required review level.
- Effective review scope.
- Review type: INITIAL REVIEW or FINDING REVIEW.
- Findings in scope, if any.

When Task omits scope, prefer relevant FIXED-PENDING-REVIEW findings and their correction diff; otherwise review the current working tree or current branch/checkpoint change. Ask only when multiple unrelated change groups or an unsafe base ambiguity prevents reliable inference.

Verification is part of this review. Inspect the implementing session's recorded evidence, independently rerun the risk-relevant targeted checks, and add adversarial, regression, or domain-semantic cases when coverage is insufficient. A full-suite rerun is required only when the risk, affected surface, missing evidence, or low execution cost justifies it. Review authorization may reach L3.

REVIEW diagnoses only. REVIEW-AND-FIX may review and correct up to L3 when authorized. It may self-close only localized, unambiguous L0-L2 findings. Set an L3 correction to FIXED-PENDING-REVIEW for a fresh REVIEW session. Leave an unresolved L3 decision OPEN for a separate DECISION session.

For a FINDING REVIEW:
- pass → Status: FIXED with evidence;
- fail/regression → Status: OPEN with evidence;
- conflict with authoritative requirements → Status: NEEDS-REVIEW;
- distinct new defect → allocate a new RVW-###.

Do not delete or rewrite original findings. Report `Review result: CLEAN` or `FINDINGS`, `Verification: PASS`, `FAIL`, or `BLOCKED`, checks independently run, and residual verification limits. A clean review states that no Blocker/Major/Minor findings were found.

Optional standalone reports use the next NNNN_REVIEW_SCOPE.md number in docs/0000_DOCUMENT_INDEX.md; this sequence is independent of RVW-###.
```
