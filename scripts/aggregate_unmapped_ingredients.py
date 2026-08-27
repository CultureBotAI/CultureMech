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
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)
    if args.min_occurrences < 1:
        parser.error("--min-occurrences must be at least 1")
    ensure_distinct_output_paths(args.output, args.occurrences_output, args.errors_output)

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
    )
    if args.verbose:
        print(
            f"Unmapped aggregation complete: {output['total_instances']} occurrences "
            f"across {output['total_unmapped_count']} unresolved groups"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
