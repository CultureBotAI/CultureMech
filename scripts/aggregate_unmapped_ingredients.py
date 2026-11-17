#!/usr/bin/env python3
"""Compatibility CLI for the unresolved ingredient aggregation view.

The canonical ``aggregate-all-ingredients`` command scans once and writes both
partitions.  This wrapper keeps the historical command-line interface while
delegating traversal, validation, identity resolution, and counting to the
shared #337 occurrence collector.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from ingredient_occurrences import (
    build_unmapped_output,
    default_changes_output,
    default_holds_output,
    default_list_output,
    ensure_distinct_output_paths,
    scan_ingredient_occurrences,
    write_error_report,
    write_occurrences_and_yaml,
)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, default=Path("output/unmapped_ingredients.yaml"))
    parser.add_argument("--input-dir", type=Path, default=Path("data/normalized_yaml"))
    parser.add_argument("--min-occurrences", type=int, default=1)
    parser.add_argument(
        "--occurrences-output",
        type=Path,
        default=Path("output/ingredient_occurrences.tsv"),
    )
    parser.add_argument(
        "--errors-output",
        type=Path,
        default=Path("output/ingredient_aggregation_errors.tsv"),
    )
    parser.add_argument(
        "--list-output",
        type=Path,
        default=None,
        help="Ingredient list TSV (default: ingredients_list.tsv beside --occurrences-output).",
    )
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument(
        "--changes-output",
        type=Path,
        default=None,
        help="Lossless variant change TSV (default: beside occurrences).",
    )
    args = parser.parse_args(argv)
    if args.list_output is None:
        args.list_output = default_list_output(args.occurrences_output)
    if args.changes_output is None:
        args.changes_output = default_changes_output(args.occurrences_output)
    if args.min_occurrences < 1:
        parser.error("--min-occurrences must be at least 1")
    ensure_distinct_output_paths(
        args.output,
        args.occurrences_output,
        args.errors_output,
        args.list_output,
        args.changes_output,
        default_holds_output(args.occurrences_output),
    )

    result = scan_ingredient_occurrences(args.input_dir)
    write_error_report(args.errors_output, result.errors)
    if result.errors:
        if args.verbose:
            print(f"Unmapped aggregation failed with {len(result.errors)} input error(s)")
        return 1
    output = build_unmapped_output(result.occurrences, args.min_occurrences)
    write_occurrences_and_yaml(
        args.occurrences_output,
        result.occurrences,
        args.output,
        output,
        args.list_output,
        variant_changes=result.variant_changes,
        changes_path=args.changes_output,
        variant_mentions=result.variant_mentions,
    )
    if args.verbose:
        print(
            f"Unmapped aggregation complete: {output['total_instances']} occurrences "
            f"across {output['total_unmapped_count']} unresolved groups"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
