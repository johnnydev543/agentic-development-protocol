# Review Fix Prompt Template

Use this when review findings were produced in another session or by another model.

```text
Fix the OPEN findings assigned to this session in docs/review-findings.md.

Before editing, read:
- AGENTS.md
- docs/review-findings.md
- docs/implementation-handoff.md if present
- the authoritative specification
- the files/tests referenced by the selected findings

For each finding:
1. Confirm that the requested fix is consistent with the authoritative specification and architecture invariants.
2. Make the smallest correct change that resolves the finding.
3. Add or update a regression test when appropriate.
4. Run the verification requested by the finding plus relevant lint/type checks.
5. Do not broaden the fix into unrelated refactoring.

If a finding requires a new architecture, interface/schema decision, unsupported domain interpretation, or uncertain cross-module semantic change, do not guess. Leave the finding OPEN and report that it requires higher-level review/architecture work.

After a successful fix, update the original finding in docs/review-findings.md instead of deleting it:

Status: FIXED
Fixed by commit: <sha if available>
Fix summary: <concise description>
Verification: <commands/results>

If the finding is not actually valid, do not silently close it. Mark it as NEEDS-REVIEW and explain the evidence.

Do not mark a finding FIXED merely because code was changed. Verification must pass.
```
