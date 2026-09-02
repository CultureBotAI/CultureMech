#!/usr/bin/env python3
"""Find ingredient rows whose concentration is a summed merge artifact (#394).

`cleanup_media_quality.py` used to collapse duplicate ingredient rows by adding
their concentrations, and recorded what it did:

    - preferred_term: Agar
      concentration: {value: '50.0', unit: G_PER_L}
      notes: ' (for solid medium) [Merged 3 duplicates: 15.0, 15.0, 20.0]'

15 + 15 + 20 = 50, and agar sets at 15-20 g/L, so that medium cannot pour.
Duplicate rows almost always mean the importer listed one addition twice, not
that the medium receives the ingredient twice, so summing turned a
transcription artifact into a fabricated quantity.

The note is the evidence, which is what makes this recoverable at all: it
preserves the parts the merge consumed.

## Two populations, and only one is mechanical

`IDENTICAL_PARTS`
    Every merged part is the same value, so the pre-merge value is that value
    and nothing else. `Methanol 1584.0 = 792.0 + 792.0`; 792 g/L is the density
    of methanol, so the source meant neat solvent listed twice.
    Repairable with no judgement.

`DIFFERING_PARTS`
    The parts disagree — `15.0, 15.0, 20.0`. Which one the medium means is a
    curation question about the source recipe, not arithmetic. Reported only.

`COEXISTING_ROW`
    The merged row shares its record with another row of the same ingredient,
    so a consumer double-counts regardless of which value is right. Reported
    separately because it survives repairing the value.

Read-only. `scripts/repair_merged_duplicates.py` performs the repair.
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter, defaultdict
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_RECORDS = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_REPORT = REPO_ROOT / "data" / "import_tracking" / "reports" / "merged_duplicates.tsv"

# Both spellings: the original summing note, and the note the fixed mutator
# writes when it legitimately collapses identical duplicates.
MERGE_NOTE = re.compile(r"\[(?:Merged|Collapsed) (\d+) (?:identical )?duplicates: ([^\]]+)\]")

FINDINGS = ("IDENTICAL_PARTS", "DIFFERING_PARTS", "COEXISTING_ROW", "REPEATED_INGREDIENT")
HEADER = ["finding", "file_path", "record_id", "ingredient", "value", "unit", "parts", "detail"]


def merged_parts(notes: Any) -> list[Decimal] | None:
    """The concentrations a merge consumed, or None if this row records no merge."""
    match = MERGE_NOTE.search(str(notes or ""))
    if not match:
        return None
    parts: list[Decimal] = []
    for chunk in match.group(2).split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        try:
            parts.append(Decimal(chunk))
        except InvalidOperation:
            return None
    return parts or None


def _decimal(value: Any) -> Decimal | None:
    try:
        return Decimal(str(value))
    except (InvalidOperation, TypeError):
        return None


def classify(ingredient: dict[str, Any]) -> tuple[str, list[Decimal]] | None:
    """(finding, parts) for a summed row, or None when the row is sound.

    A row is sound when its value is not the sum of the parts — the fixed
    mutator writes the collapsed value, which equals one part rather than their
    total, so repaired rows stop being reported without needing the note
    stripped.
    """
    parts = merged_parts(ingredient.get("notes"))
    if not parts or len(parts) < 2:
        return None
    current = _decimal((ingredient.get("concentration") or {}).get("value"))
    if current is None or current != sum(parts):
        return None
    return ("IDENTICAL_PARTS" if len(set(parts)) == 1 else "DIFFERING_PARTS"), parts


def _collect(
    items: Any,
    by_name: dict[tuple[str, str], list[dict[str, Any]]],
    merged_names: set[tuple[str, str]],
    rows: list[dict[str, str]],
    stats: Counter,
    relative: str,
    identifier: str,
) -> None:
    """Walk one record's ingredient tree, accumulating findings.

    Module-level and explicitly parameterised rather than a closure inside
    `scan`'s loop: a closure over the loop variables is correct only while the
    call stays inside the same iteration, which is precisely the property that
    quietly stops holding when someone defers or parallelises it later.
    """
    for ingredient in items or []:
        if not isinstance(ingredient, dict):
            continue
        concentration = ingredient.get("concentration") or {}
        key = (str(ingredient.get("preferred_term", "")), str(concentration.get("unit", "")))
        by_name[key].append(ingredient)

        verdict = classify(ingredient)
        if verdict:
            finding, parts = verdict
            stats[finding] += 1
            merged_names.add(key)
            rows.append(
                {
                    "finding": finding,
                    "file_path": relative,
                    "record_id": identifier,
                    "ingredient": key[0],
                    "value": str(concentration.get("value")),
                    "unit": key[1],
                    "parts": ";".join(str(p) for p in parts),
                    "detail": (
                        "value is the sum of identical parts; the pre-merge value is unambiguous"
                        if finding == "IDENTICAL_PARTS"
                        else "value is the sum of differing parts; which one the medium "
                        "means needs the source recipe"
                    ),
                }
            )
        _collect(
            ingredient.get("composition"), by_name, merged_names, rows, stats, relative, identifier
        )


def scan(records_dir: Path) -> tuple[list[dict[str, str]], Counter]:
    rows: list[dict[str, str]] = []
    stats: Counter = Counter()

    for path in sorted(records_dir.glob("*/*.yaml")):
        record = yaml.safe_load(path.read_text())
        if not isinstance(record, dict):
            continue
        stats["records_scanned"] += 1
        relative = str(path.relative_to(REPO_ROOT))
        identifier = str(record.get("id") or "")

        by_name: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
        merged_names: set[tuple[str, str]] = set()
        for section in ("ingredients", "solutions"):
            _collect(record.get(section), by_name, merged_names, rows, stats, relative, identifier)

        # Repeated rows that carry NO merge note. `ucm.yaml` (#283) lists eight
        # ingredients twice at 1000x/100x apart — stock strength beside final
        # concentration — and never went through the merge, so COEXISTING_ROW
        # cannot see it. Reported whatever the ratio: two rows for one
        # ingredient in one recipe is a question either way.
        for key in sorted(by_name):
            if key in merged_names or len(by_name[key]) < 2:
                continue
            values = [_decimal((i.get("concentration") or {}).get("value")) for i in by_name[key]]
            numeric = [v for v in values if v is not None and v > 0]
            if len(numeric) < 2:
                continue
            stats["REPEATED_INGREDIENT"] += 1
            ratio = max(numeric) / min(numeric)
            rows.append(
                {
                    "finding": "REPEATED_INGREDIENT",
                    "file_path": relative,
                    "record_id": identifier,
                    "ingredient": key[0],
                    "value": ";".join(str(v) for v in values),
                    "unit": key[1],
                    "parts": "",
                    "detail": (
                        f"{len(by_name[key])} rows name this ingredient in one record, "
                        f"ratio {ratio:g}x"
                        + (
                            " — same value listed twice"
                            if ratio == 1
                            else (
                                " — a power of ten suggests stock strength beside a final "
                                "concentration"
                                if ratio in (Decimal(10), Decimal(100), Decimal(1000))
                                else ""
                            )
                        )
                    ),
                }
            )

        for key in sorted(merged_names):
            if len(by_name[key]) > 1:
                stats["COEXISTING_ROW"] += 1
                rows.append(
                    {
                        "finding": "COEXISTING_ROW",
                        "file_path": relative,
                        "record_id": identifier,
                        "ingredient": key[0],
                        "value": ";".join(
                            str((i.get("concentration") or {}).get("value")) for i in by_name[key]
                        ),
                        "unit": key[1],
                        "parts": "",
                        "detail": (
                            f"{len(by_name[key])} rows name this ingredient in one record, "
                            f"one of them a merge survivor — a consumer double-counts"
                        ),
                    }
                )
    return rows, stats


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--records-dir", type=Path, default=DEFAULT_RECORDS)
    parser.add_argument("--out", type=Path, default=DEFAULT_REPORT)
    parser.add_argument(
        "--max-identical",
        type=int,
        default=None,
        help="Fail if IDENTICAL_PARTS exceeds this. These are mechanically repairable.",
    )
    parser.add_argument(
        "--max-differing",
        type=int,
        default=None,
        help="Fail if DIFFERING_PARTS exceeds this. These need source curation.",
    )
    parser.add_argument(
        "--max-coexisting",
        type=int,
        default=None,
        help="Fail if COEXISTING_ROW exceeds this.",
    )
    parser.add_argument(
        "--max-repeated",
        type=int,
        default=None,
        help="Fail if REPEATED_INGREDIENT exceeds this (#283).",
    )
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    rows, stats = scan(args.records_dir)

    print(f"Scanned {stats['records_scanned']:,} records")
    for finding in FINDINGS:
        print(f"  {finding:16s} {stats[finding]:6d}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    print(f"\nWrote {args.out.relative_to(REPO_ROOT)}")

    # Per-detector baselines, deliberately not one total (#302): a total lets a
    # repair in one class pay for a regression in another.
    failures = []
    for finding, cap in (
        ("IDENTICAL_PARTS", args.max_identical),
        ("DIFFERING_PARTS", args.max_differing),
        ("COEXISTING_ROW", args.max_coexisting),
        ("REPEATED_INGREDIENT", args.max_repeated),
    ):
        if cap is not None and stats[finding] > cap:
            failures.append(f"{finding}: {stats[finding]} > baseline {cap}")
    if failures:
        print("\nFAIL:", file=sys.stderr)
        for line in failures:
            print(f"  {line}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
