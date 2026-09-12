# Review Fix Prompt Template

Use this when review findings were produced in another session or by another model.

```text
Fix the OPEN findings assigned to this session in docs/review-findings.md.

Before editing, read:
- AGENTS.md
- policies/CODE_REVIEW.md
- docs/review-findings.md
- docs/implementation-handoff.md if present
- the authoritative specification
- the files/tests referenced by the selected findings

For each finding, confirm the requested fix against the authoritative specification and recorded invariants. Make the smallest correct change, add a regression test when appropriate, and run the requested verification. Do not broaden the fix into unrelated refactoring.

If a finding requires a new architecture, interface/schema decision, unsupported domain interpretation, or uncertain cross-module semantic change, do not guess. Leave the finding OPEN and report that it requires higher-level review/architecture work.

After a successful fix, retain and update the original finding using the status and completion fields in `policies/CODE_REVIEW.md`. Invalid or conflicting findings become `NEEDS-REVIEW` with evidence. Code changes alone do not justify `FIXED`; verification must pass.
```
