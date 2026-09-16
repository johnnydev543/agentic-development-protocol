# Review Finding Archive Policy

Keep `docs/review-findings.md` as the active cross-session ledger. It contains only findings with these states:

- `OPEN`
- `FIXED-PENDING-REVIEW`
- `NEEDS-REVIEW`

Move stable `FIXED` entries to immutable numbered files under `docs/review-archive/`. Preserve every original `RVW-###` ID, finding body, fix summary, verification result, and referenced commit. Never renumber archived findings.

## Archive Gate

A finding may be archived only when:

1. its status is `FIXED`;
2. every required fresh REVIEW has completed;
3. its correction is part of a stable repository baseline;
4. no active finding requires its full body as current working context.

Archive at a completed milestone or whenever the active ledger exceeds 500 lines or 50 KB. Do not wait for the file to become a general project history.

## Archive Layout

```text
docs/
  review-findings.md
  review-archive/
    README.md
    0001_FIXED_RVW-001-052.md
    0002_FIXED_RVW-054-080.md
```

`docs/review-archive/README.md` records each archive file, included IDs, archive date, and the next available `RVW-###` ID. Archive document numbering is independent of standalone review-report numbering.

## Read Rules

IMPLEMENT, REVIEW, and REVIEW-AND-FIX read only relevant entries from the active ledger by default. Do not load archive files merely to reconstruct general history.

Search or read an archive only when:

- an active finding explicitly references an archived ID;
- the current task names a historical finding;
- a current change may regress a previously fixed defect;
- an authoritative decision or verification result exists only in the archived entry.

Read the matching entry or archive file, not the entire archive directory.

## Safe Archiving

Use `scripts/archive_review_findings.py` when the repository adopts the standard ledger format. Review its diff before committing. The script archives only entries whose current status is exactly `FIXED`; it leaves every other status active and preserves the monotonic next-ID sequence.
