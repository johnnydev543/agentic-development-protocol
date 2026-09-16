#!/usr/bin/env python3
"""Move FIXED review findings from the active ledger into a numbered archive."""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

FINDING_RE = re.compile(r"^## (RVW-(\d{3})) — .+$")
STATUS_RE = re.compile(r"(?m)^Status: ([A-Z-]+)\s*$")


def parse_findings(text: str) -> tuple[list[tuple[int, str, str, str]], int]:
    lines = text.splitlines(keepends=True)
    headings: list[tuple[int, re.Match[str]]] = []
    in_fence = False
    for index, line in enumerate(lines):
        if line.lstrip().startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = FINDING_RE.match(line.rstrip("\n"))
        if match is not None:
            headings.append((index, match))

    findings: list[tuple[int, str, str, str]] = []
    for heading_index, (start, match) in enumerate(headings):
        end = len(lines)
        in_fence = False
        for index in range(start + 1, len(lines)):
            if lines[index].lstrip().startswith("```"):
                in_fence = not in_fence
                continue
            if not in_fence and lines[index].startswith("## "):
                end = index
                break
        block = "".join(lines[start:end]).strip() + "\n"
        status_match = STATUS_RE.search(block)
        if status_match is None:
            raise ValueError(f"{match.group(1)} has no Status line")
        findings.append((int(match.group(2)), match.group(1), status_match.group(1), block))
    first_start = headings[0][0] if headings else len(lines)
    return findings, first_start


def next_archive_path(archive_dir: Path, ids: list[int]) -> Path:
    existing = sorted(archive_dir.glob("[0-9][0-9][0-9][0-9]_FIXED_RVW-*.md"))
    number = int(existing[-1].name[:4]) + 1 if existing else 1
    return archive_dir / f"{number:04d}_FIXED_RVW-{min(ids):03d}-{max(ids):03d}.md"


def active_header(active_ids: list[str], next_id: int) -> str:
    active = ", ".join(active_ids) if active_ids else "none"
    return f"""# Review Findings Ledger

This is the active cross-session ledger. It contains only `OPEN`, `FIXED-PENDING-REVIEW`, and `NEEDS-REVIEW` findings. Stable `FIXED` entries live under `docs/review-archive/` and are not read by default.

Active findings: {active}
Next finding ID: `RVW-{next_id:03d}`

## ID and Status Rules

- Assign IDs monotonically and never reuse or renumber an ID.
- Allowed statuses are `OPEN`, `FIXED-PENDING-REVIEW`, `FIXED`, and `NEEDS-REVIEW`.
- Keep the original finding text when updating status.
- A separate IMPLEMENT correction normally sets `FIXED-PENDING-REVIEW`.
- REVIEW-AND-FIX may self-close only eligible L0-L2 findings.
- L3 and mandatory-independent-review corrections require a fresh REVIEW before `FIXED`.
- Archive only stable `FIXED` entries according to `policies/REVIEW_ARCHIVE.md`.

## Finding Template

```text
## RVW-### — <severity>
Status: OPEN
Task: <task or scope>
Files:
- ...

Finding:
...

Required fix:
...

Verification:
- ...

Fixed by commit: <sha if available>
Fix summary: <complete after correction>
Verification result: <commands and results>
```

---

"""


def archive_index_entry(path: Path, ids: list[str]) -> str:
    return f"| `{path.name}` | {', '.join(ids)} | {date.today().isoformat()} |\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ledger", type=Path, default=Path("docs/review-findings.md"))
    parser.add_argument("--archive-dir", type=Path, default=Path("docs/review-archive"))
    args = parser.parse_args()

    text = args.ledger.read_text(encoding="utf-8")
    findings, first_finding_line = parse_findings(text)
    original_preamble = "".join(text.splitlines(keepends=True)[:first_finding_line]).rstrip()
    if not findings:
        raise ValueError("ledger contains no findings")

    fixed = sorted((item for item in findings if item[2] == "FIXED"), key=lambda item: item[0])
    active = sorted((item for item in findings if item[2] != "FIXED"), key=lambda item: item[0])
    if not fixed:
        raise ValueError("ledger contains no FIXED findings to archive")

    args.archive_dir.mkdir(parents=True, exist_ok=True)
    archive_path = next_archive_path(args.archive_dir, [item[0] for item in fixed])
    archive_body = "\n".join(item[3].rstrip() for item in fixed) + "\n"
    archive_path.write_text(
        "# Archived Fixed Review Findings\n\n"
        f"Archived: {date.today().isoformat()}\n\n"
        "These entries are immutable historical records. Preserve their original RVW IDs.\n\n---\n\n"
        "## Original Ledger Preamble\n\n"
        + original_preamble
        + "\n\n---\n\n"
        + archive_body,
        encoding="utf-8",
    )

    max_id = max(item[0] for item in findings)
    active_body = "\n".join(item[3].rstrip() for item in active)
    args.ledger.write_text(
        active_header([item[1] for item in active], max_id + 1) + active_body + ("\n" if active_body else ""),
        encoding="utf-8",
    )

    index_path = args.archive_dir / "README.md"
    if index_path.exists():
        index = index_path.read_text(encoding="utf-8")
    else:
        index = (
            "# Review Finding Archive\n\n"
            "Do not read archive files by default. Search them only for an explicitly referenced historical finding, regression investigation, or decision evidence unavailable in the active ledger.\n\n"
            "| Archive | Finding IDs | Archived |\n"
            "|---|---|---|\n"
        )
    index = re.sub(r"\nNext finding ID: `RVW-\d{3}`\n?$", "\n", index)
    index += archive_index_entry(archive_path, [item[1] for item in fixed])
    index += f"\nNext finding ID: `RVW-{max_id + 1:03d}`\n"
    index_path.write_text(index, encoding="utf-8")

    print(f"archived {len(fixed)} findings to {archive_path}")
    print(f"kept {len(active)} active findings in {args.ledger}")


if __name__ == "__main__":
    main()
