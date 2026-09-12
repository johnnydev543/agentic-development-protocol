# Document Naming and Identity Policy

Project documents should have stable identities that remain useful across sessions, models, reviews, and Git history.

## Default Filename

Use a repository-wide, zero-padded four-digit sequence for new specifications, plans, architecture decisions, review artifacts, reports, and similar durable documents:

```text
NNNN_TYPE_SCOPE.md
```

Examples:

```text
0001_SPEC_REPORT_INGESTION.md
0002_PLAN_REPORT_INGESTION_PHASE1.md
0003_REVIEW_REPORT_INGESTION_PHASE1.md
0004_ADR_SOURCE_VERSIONING.md
```

- `NNNN` is the next unused repository-wide document number, starting at `0001`.
- `TYPE` describes the document role, such as `SPEC`, `PLAN`, `ARCH`, `ADR`, `REVIEW`, `REPORT`, or `RUNBOOK`.
- `SCOPE` is a short, stable, uppercase snake-case subject. Add `PHASE1`, `PHASE2`, and similar terms only when the phase is part of the document's durable identity.

Do not reuse a number after a document is deleted, superseded, or abandoned.

## Dates and Mutable State

Do not include a date in new numbered filenames by default. Dates, status, version, ownership, and Git baselines are metadata and may change without changing the document's identity or breaking links.

Use this header near the top of a numbered document:

```text
Document ID: DOC-0001
Type: SPEC
Status: DRAFT
Created: 2026-09-12
Updated: 2026-09-12
Git baseline: <commit SHA or N/A>
Supersedes: <DOC-NNNN or none>
Related: <TASK/RVW/document IDs or none>
```

Use ISO `YYYY-MM-DD` dates. The filename remains unchanged when `Updated`, `Status`, or the reviewed commit changes.

Create a new numbered document when the new artifact has a distinct purpose or intentionally supersedes an earlier decision. Ordinary corrections and status updates should update the existing document and its metadata.

## Document Index and Number Allocation

Projects adopting this policy should maintain:

```text
docs/0000_DOCUMENT_INDEX.md
```

Reserve `0000` for this index. Record every allocated document ID, filename, type, status, and relationship to superseded documents.

Before creating a document:

1. Read the index and scan existing numbered filenames.
2. Select the next unused number.
3. Add the new allocation to the index in the same commit as the document.
4. Before merging, rebase or refresh against the target branch and check for a collision.
5. If another branch claimed the same number first, renumber only the still-unmerged document and update its links/index entry.

The index is the registry, but existing filenames remain the final collision check.

## Stable-Path Exceptions

Keep conventional or tool-addressed entry points unnumbered when agents, automation, packaging, or common tooling must locate them without consulting the index. Examples include:

- `README.md`;
- `AGENTS.md`;
- `CHANGELOG.md`;
- `docs/implementation-handoff.md`;
- `docs/review-findings.md`;
- repository policy and reusable template filenames.

The stable `docs/review-findings.md` ledger may reference separately numbered review artifacts. A standalone review report should use a numbered filename even though actionable cross-session findings are also recorded in the stable ledger.

Document an additional exception in `docs/0000_DOCUMENT_INDEX.md`; do not create ad hoc unnumbered files merely for convenience.

## Existing Repositories

Apply this policy prospectively. Do not mass-rename existing documents solely to add numbers because that can break links, Git references, external bookmarks, prompts, and review provenance.

Rename legacy documents only as a dedicated migration with a complete link/reference update and redirect or compatibility plan where appropriate.

## Relationship to Task and Finding IDs

Document IDs, implementation task IDs, and review finding IDs identify different things:

- `DOC-0007` — durable document identity;
- `TASK-014` — implementation unit in the handoff ledger;
- `RVW-006` — actionable review finding.

Do not derive one sequence from another and do not substitute filenames for task or finding IDs.
