# 0000 Document Index Template

Copy this file to `docs/0000_DOCUMENT_INDEX.md` when adopting `policies/DOCUMENT_NAMING.md`.

```text
# Document Index

Document ID: DOC-0000
Type: INDEX
Status: ACTIVE
Created: <YYYY-MM-DD>
Updated: <YYYY-MM-DD>

| ID | Filename | Type | Status | Supersedes | Summary |
|---|---|---|---|---|---|
| DOC-0001 | `0001_SPEC_EXAMPLE.md` | SPEC | DRAFT | — | Example specification |

## Stable-Path Exceptions

| Path | Reason |
|---|---|
| `implementation-handoff.md` | Well-known path used by architecture and implementation prompts |
| `review-findings.md` | Well-known cross-session findings ledger |
```

Before allocating the next number, compare this index with numbered files already present on the target branch. Resolve concurrent allocation collisions before merge.
