# Independent Review Prompt Template

Use this in a fresh session, preferably with a model different from the implementation model for meaningful or high-risk changes.

```text
Review the implementation for <TASK-ID or change scope>.

Read:
- AGENTS.md
- authoritative specification
- docs/implementation-handoff.md if present
- the Git diff from the intended baseline
- relevant tests
- verification output

Your job is to identify defects, regressions, architecture violations, missing tests, and unsupported assumptions. Do not automatically rewrite the implementation.

Classify each finding as:
- Blocker
- Major
- Minor
- Suggestion

For every actionable finding, provide:
- Finding ID (RVW-###)
- Severity
- Affected files/symbols
- Observed problem
- Why it matters
- Required fix
- Verification needed

Persist actionable findings to docs/review-findings.md using this structure:

## RVW-001 — Major
Status: OPEN
Task: <TASK-ID>
Files:
- ...

Finding:
...

Required fix:
...

Verification:
- ...

Do not invent or silently change authoritative domain semantics. If correctness depends on missing or conflicting requirements, record that explicitly and route it for clarification/architecture review.

A clean review should say that no Blocker/Major/Minor findings were found and list any residual verification limits.
```
