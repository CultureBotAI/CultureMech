#!/usr/bin/env python3
"""Compare frozen/current unmapped TSV rows for release tracker #687 (2026-11-13).

Inputs: named pairs of local TSVs and optional explicit literal key columns.
Output: JSON on stdout with byte digests, exact row multiset changes, and key changes.
CSV quoting is honored; cells are not normalized. No source mutations or identity
inference. Literal key tuples describe source observations, not scientific entities.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path


def read_tsv(path: Path) -> tuple[dict, list[str], list[tuple[str, ...]]]:
    before = path.stat()
    raw = path.read_bytes()
    after = path.stat()
    if (before.st_ino, before.st_size, before.st_mtime_ns) != (
        after.st_ino,
        after.st_size,
        after.st_mtime_ns,
    ):
        raise ValueError(f"file changed during read: {path}")
    parsed = list(
        csv.reader(io.StringIO(raw.decode("utf-8"), newline=""), delimiter="\t", strict=True)
    )
    if not parsed or not parsed[0] or len(set(parsed[0])) != len(parsed[0]):
        raise ValueError(f"missing or duplicate header: {path}")
    columns = parsed[0]
    rows = []
    for number, row in enumerate(parsed[1:], start=2):
        if len(row) != len(columns):
            raise ValueError(f"row {number} has {len(row)} cells, expected {len(columns)}: {path}")
        rows.append(tuple(row))
    source = {"path": str(path), "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw)}
    return source, columns, rows


def counted_rows(counts: Counter, columns: list[str]) -> list[dict]:
    return [
        {"values": dict(zip(columns, row, strict=True)), "count": count}
        for row, count in sorted(counts.items())
    ]


def compare_pair(label: str, frozen: Path, current: Path, keys: list[str]) -> dict:
    frozen_source, columns, frozen_rows = read_tsv(frozen)
    current_source, current_columns, current_rows = read_tsv(current)
    if columns != current_columns:
        raise ValueError(f"{label}: ordered headers differ; do not infer corresponding columns")
    if any(key not in columns for key in keys) or len(set(keys)) != len(keys):
        raise ValueError(f"{label}: key columns must be distinct explicit header names")
    old, new = Counter(frozen_rows), Counter(current_rows)
    removed, added = old - new, new - old
    report = {
        "label": label,
        "sources": {"frozen": frozen_source, "current": current_source},
        "columns": columns,
        "ordered_rows_equal": frozen_rows == current_rows,
        "row_multisets_equal": old == new,
        "counts": {
            "frozen_rows": len(frozen_rows),
            "current_rows": len(current_rows),
            "unchanged_rows": sum((old & new).values()),
            "removed_rows": sum(removed.values()),
            "added_rows": sum(added.values()),
        },
        "removed_rows": counted_rows(removed, columns),
        "added_rows": counted_rows(added, columns),
    }
    if keys:
        indices = [columns.index(key) for key in keys]
        old_by_key, new_by_key = defaultdict(Counter), defaultdict(Counter)
        for rows, grouped in ((frozen_rows, old_by_key), (current_rows, new_by_key)):
            for row in rows:
                grouped[tuple(row[index] for index in indices)][row] += 1
        removed_keys = old_by_key.keys() - new_by_key.keys()
        added_keys = new_by_key.keys() - old_by_key.keys()
        common_keys = old_by_key.keys() & new_by_key.keys()
        changed_keys = sorted(key for key in common_keys if old_by_key[key] != new_by_key[key])
        report["literal_keys"] = {
            "columns": keys,
            "scope": "Exact column tuples only; not stable ontology IDs or scientific identities.",
            "counts": {
                "frozen_distinct": len(old_by_key),
                "current_distinct": len(new_by_key),
                "removed_distinct": len(removed_keys),
                "added_distinct": len(added_keys),
                "common_with_changed_rows": len(changed_keys),
                "frozen_keys_with_multiple_rows": sum(
                    sum(rows.values()) > 1 for rows in old_by_key.values()
                ),
                "current_keys_with_multiple_rows": sum(
                    sum(rows.values()) > 1 for rows in new_by_key.values()
                ),
            },
            "removed": [dict(zip(keys, key, strict=True)) for key in sorted(removed_keys)],
            "added": [dict(zip(keys, key, strict=True)) for key in sorted(added_keys)],
            "common_with_changed_rows": [
                {
                    "key": dict(zip(keys, key, strict=True)),
                    "frozen": counted_rows(old_by_key[key], columns),
                    "current": counted_rows(new_by_key[key], columns),
                }
                for key in changed_keys
            ],
        }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--pair", nargs=3, action="append", required=True, metavar=("NAME", "FROZEN", "CURRENT")
    )
    parser.add_argument("--key-column", action="append", default=[])
    args = parser.parse_args()
    report = {
        "schema_version": 1,
        "observed_at": datetime.now(timezone.utc).isoformat(),
        "scope": "Exact TSV row multisets and optional literal source-column tuples only.",
        "comparisons": [
            compare_pair(label, Path(frozen), Path(current), args.key_column)
            for label, frozen, current in args.pair
        ],
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
