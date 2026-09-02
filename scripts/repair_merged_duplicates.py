#!/usr/bin/env python3
"""Undo the summed-duplicate merge where the pre-merge value is unambiguous (#394).

`cleanup_media_quality.py` collapsed duplicate ingredient rows by **adding**
their concentrations, and left the parts behind in a note:

    - preferred_term: Methanol
      concentration: {value: '1584.0', unit: G_PER_L}
      notes: '[Merged 2 duplicates: 792.0, 792.0]'

792 g/L is the density of methanol, so the source listed neat solvent twice and
the merge invented 1584. Summing was the wrong operation: duplicate rows almost
always mean the importer transcribed one addition twice, not that the medium
receives the ingredient twice.

## What this repairs, and what it refuses to

Only rows where **every merged part is the same value**. Then the pre-merge
value is that value, there is exactly one possibility, and the repair is
arithmetic-free.

It refuses rows whose parts differ — `15.0, 15.0, 20.0`. Picking 15 or 20 is a
question about the source recipe, and a plausible guess that round-trips is
still false chemistry. Those stay for source curation and keep failing the
audit.

The note is rewritten from `Merged` to `Collapsed ... identical duplicates` so
the record still says what happened and the audit stops reporting the row,
without the evidence being erased.

Preview by default. `--apply` writes.
"""

from __future__ import annotations

import argparse
import sys
from collections import Counter

# `timezone.utc`, not `datetime.UTC`: the latter is 3.11+ and this project
# supports >=3.10.
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_merged_duplicates import MERGE_NOTE, classify  # noqa: E402
from record_io import write_record  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RECORDS = REPO_ROOT / "data" / "normalized_yaml"

CURATOR = "repair_merged_duplicates.py"
ACTION = "REPAIRED_SUMMED_DUPLICATE_MERGE"


def repair_ingredient(ingredient: dict[str, Any]) -> tuple[str, str] | None:
    """Collapse one summed row. Returns (before, after) or None if not eligible."""
    verdict = classify(ingredient)
    if not verdict:
        return None
    finding, parts = verdict
    if finding != "IDENTICAL_PARTS":
        return None

    concentration = ingredient.get("concentration") or {}
    before = str(concentration.get("value"))
    after = str(parts[0])
    if before == after:
        return None

    concentration["value"] = after
    ingredient["concentration"] = concentration

    notes = str(ingredient.get("notes") or "")
    listed = ", ".join(str(p) for p in parts)
    ingredient["notes"] = MERGE_NOTE.sub(
        f"[Collapsed {len(parts)} identical duplicates: {listed}]", notes, count=1
    ).strip()
    return before, after


def repair_record(record: dict[str, Any]) -> list[tuple[str, str, str]]:
    """Every collapse made in this record: (ingredient, before, after)."""
    changed: list[tuple[str, str, str]] = []

    def walk(items: Any) -> None:
        for ingredient in items or []:
            if not isinstance(ingredient, dict):
                continue
            outcome = repair_ingredient(ingredient)
            if outcome:
                changed.append((str(ingredient.get("preferred_term", "")), *outcome))
            walk(ingredient.get("composition"))

    walk(record.get("ingredients"))
    walk(record.get("solutions"))
    return changed


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--records-dir", type=Path, default=DEFAULT_RECORDS)
    parser.add_argument("--apply", action="store_true", help="Write. Default is preview.")
    parser.add_argument("--limit", type=int, default=0, help="Stop after N records (0 = all).")
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    stats: Counter = Counter()
    by_ingredient: Counter = Counter()
    failures: list[str] = []

    for path in sorted(args.records_dir.glob("*/*.yaml")):
        record = yaml.safe_load(path.read_text())
        if not isinstance(record, dict):
            continue

        changed = repair_record(record)
        if not changed:
            continue

        for name, before, after in changed:
            by_ingredient[(name, before, after)] += 1
        stats["rows_collapsed"] += len(changed)
        stats["records_repaired"] += 1

        record.setdefault("curation_history", []).append(
            {
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "curator": CURATOR,
                "action": ACTION,
                "notes": (
                    f"Collapsed {len(changed)} ingredient row(s) whose concentration was the "
                    f"SUM of identical duplicate values written by cleanup_media_quality.py. "
                    f"Every merged part was the same value, so the pre-merge value is "
                    f"unambiguous and no source lookup was needed. Rows whose merged parts "
                    f"differ were left untouched."
                ),
            }
        )
        if args.apply:
            write_record(path, record)
        if args.limit and stats["records_repaired"] >= args.limit:
            break

    verb = "Collapsed" if args.apply else "Would collapse"
    print(f"\n{verb} {stats['rows_collapsed']} row(s) across {stats['records_repaired']} record(s)")
    if by_ingredient:
        print("\nmost affected:")
        for (name, before, after), count in by_ingredient.most_common(12):
            print(f"  {count:5d}  {name!r}: {before} -> {after}")
    if failures:
        print(f"\n{len(failures)} left untouched:", file=sys.stderr)
        for line in failures:
            print(f"  {line}", file=sys.stderr)
    if not args.apply:
        print("\nPreview only. Re-run with --apply to write.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
