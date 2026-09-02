#!/usr/bin/env python3
"""Report the ingredient rows the KGX export drops for want of an identity (#372).

`kgx_export` mints an edge only when the ingredient resolves:

    chem_id = _resolved_ingredient_id(ingredient, ingredient_resolver)
    if not chem_id:
        return None

Two call sites do this — `ingredient_to_edge` and the solution-composition
equivalent — and neither counts what it discarded. The rows leave no trace in
the output, no warning, and no report, so the export's node and edge totals look
complete when they are not.

This audit answers the same question from the corpus side, using the same
resolver, so it costs nothing in the export path and needs no koza run.

## Names, not rows

The headline is deliberately a **name** count. One grounding decision fixes
every row carrying that name, so a row count says how much output is missing
while a name count says how much work it takes to get it back — and the two
differ by more than an order of magnitude here. Both are reported; only the
name count is worth ratcheting.

Read-only.
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
from culturemech.ingredients import resolve_ingredient  # noqa: E402

DEFAULT_RECORDS = REPO_ROOT / "data" / "normalized_yaml"
DEFAULT_REPORT = REPO_ROOT / "data" / "import_tracking" / "reports" / "ungrounded_ingredients.tsv"
HEADER = [
    "ingredient",
    "kind",
    "rows",
    "records",
    "example_record",
    "has_local_term",
    "section",
]

# Why the classification matters: #372 proposes emitting these rows under
# kg-microbe's `INGREDIENT_CATEGORY`. Most of them are not ingredients. Minting
# 4,775 `biolink:ChemicalEntity` nodes called "See source for composition" would
# be worse than dropping them, so the split has to come before the decision.
_PLACEHOLDER = (
    "see source",
    "see recipe",
    "not specified",
    "unknown",
    "as required",
    "to be determined",
)
_CROSS_REFERENCE = ("see medium", "see m[", "medium [", "as in medium")
_SOLUTION_WORDS = ("solution", "stock", "cocktail", "elixir", "mixture", "buffer")


def classify_name(name: str) -> str:
    """What kind of thing this unresolvable string actually is."""
    lowered = name.strip().lower()
    if not lowered:
        return "EMPTY"
    if any(token in lowered for token in _PLACEHOLDER):
        return "PLACEHOLDER"
    if any(token in lowered for token in _CROSS_REFERENCE):
        return "CROSS_REFERENCE"
    if any(token in lowered for token in _SOLUTION_WORDS):
        return "SOLUTION_NAME"
    return "UNRESOLVED_CHEMICAL"


def _walk(items: Any, section: str, sink: list[tuple[str, str, dict[str, Any]]]) -> None:
    for ingredient in items or []:
        if not isinstance(ingredient, dict):
            continue
        name = str(ingredient.get("preferred_term") or "").strip()
        sink.append((name, section, ingredient))
        _walk(ingredient.get("composition"), f"{section}.composition", sink)


def scan(records_dir: Path) -> tuple[list[dict[str, Any]], Counter]:
    stats: Counter = Counter()
    rows_by_name: Counter = Counter()
    records_by_name: defaultdict[str, set[str]] = defaultdict(set)
    example: dict[str, str] = {}
    local_term: dict[str, bool] = {}
    section_of: dict[str, str] = {}

    for path in sorted(records_dir.glob("*/*.yaml")):
        record = yaml.safe_load(path.read_text())
        if not isinstance(record, dict):
            continue
        stats["records_scanned"] += 1
        identifier = str(record.get("id") or path.name)

        found: list[tuple[str, str, dict[str, Any]]] = []
        _walk(record.get("ingredients"), "ingredients", found)
        _walk(record.get("solutions"), "solutions", found)

        for name, section, ingredient in found:
            stats["rows_total"] += 1
            # The whole ingredient, not just its name: the resolver also reads a
            # record's own `term`, so a locally grounded row resolves without MIM
            # and passing the bare name would over-report.
            if resolve_ingredient(ingredient).is_resolved:
                stats["rows_resolved"] += 1
                continue
            stats["rows_ungrounded"] += 1
            rows_by_name[name] += 1
            records_by_name[name].add(identifier)
            example.setdefault(name, identifier)
            term = ingredient.get("term")
            local_term.setdefault(name, bool(isinstance(term, dict) and term.get("id")))
            section_of.setdefault(name, section)

    stats["names_ungrounded"] = len(rows_by_name)
    for name, count in rows_by_name.items():
        kind = classify_name(name)
        stats[f"names:{kind}"] += 1
        stats[f"rows:{kind}"] += count
    report = [
        {
            "ingredient": name,
            "kind": classify_name(name),
            "rows": count,
            "records": len(records_by_name[name]),
            "example_record": example[name],
            "has_local_term": "yes" if local_term[name] else "no",
            "section": section_of[name],
        }
        for name, count in rows_by_name.most_common()
    ]
    return report, stats


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--records-dir", type=Path, default=DEFAULT_RECORDS)
    parser.add_argument("--out", type=Path, default=DEFAULT_REPORT)
    parser.add_argument(
        "--max-names",
        type=int,
        default=None,
        help="Fail if the number of distinct unresolvable names exceeds this.",
    )
    args = parser.parse_args(argv if argv is not None else sys.argv[1:])

    report, stats = scan(args.records_dir)

    total = stats["rows_total"] or 1
    print(f"Scanned {stats['records_scanned']:,} records, {stats['rows_total']:,} ingredient rows")
    print(f"  resolved   : {stats['rows_resolved']:,}")
    print(
        f"  ungrounded : {stats['rows_ungrounded']:,} rows "
        f"({100 * stats['rows_ungrounded'] / total:.1f}%) "
        f"across {stats['names_ungrounded']:,} distinct names"
    )
    print("\nThese rows produce no edge in the KGX export and are reported nowhere else.")
    print("\nby kind (names / rows):")
    for kind in ("UNRESOLVED_CHEMICAL", "SOLUTION_NAME", "CROSS_REFERENCE", "PLACEHOLDER", "EMPTY"):
        if stats[f"names:{kind}"]:
            print(f"  {kind:22s} {stats[f'names:{kind}']:6,} / {stats[f'rows:{kind}']:7,}")
    if report:
        print("\nmost frequent:")
        for row in report[:10]:
            print(f"  {row['rows']:6d} rows / {row['records']:5d} records  {row['ingredient']!r}")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=HEADER, delimiter="\t")
        writer.writeheader()
        writer.writerows(report)
    print(f"\nWrote {args.out.relative_to(REPO_ROOT)}")

    if args.max_names is not None and stats["names_ungrounded"] > args.max_names:
        print(
            f"\nFAIL: {stats['names_ungrounded']} unresolvable names > baseline "
            f"{args.max_names}. A new import added ingredient names nothing can ground.",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
