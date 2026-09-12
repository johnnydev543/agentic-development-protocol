# Independent Review Prompt Template

Use this in a fresh session, preferably with a model different from the implementation model for meaningful or high-risk changes.

```text
Review the implementation for <TASK-ID or change scope>.

Read:
- AGENTS.md
- policies/CODE_REVIEW.md
- authoritative specification
- docs/implementation-handoff.md if present
- the Git diff from the intended baseline
- relevant tests
- verification output

Your job is to identify defects, regressions, architecture violations, missing tests, and unsupported assumptions. Do not automatically rewrite the implementation.

Use the severity, stable `RVW-###` fields, status, and persistence format defined in `policies/CODE_REVIEW.md`. Persist actionable findings to `docs/review-findings.md`.

If a standalone review report is required, follow policies/DOCUMENT_NAMING.md: allocate the next NNNN_REVIEW_SCOPE.md filename, add its metadata header, and register it in docs/0000_DOCUMENT_INDEX.md. Do not rename the stable findings ledger.

Do not invent or silently change authoritative domain semantics. If correctness depends on missing or conflicting requirements, record that explicitly and route it for clarification/architecture review.

A clean review should say that no Blocker/Major/Minor findings were found and list any residual verification limits.
```
