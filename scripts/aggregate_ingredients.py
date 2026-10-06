#!/usr/bin/env python3
"""Build CultureMech's lossless direct ingredient-occurrence artifacts."""

from __future__ import annotations

import argparse
from pathlib import Path

from ingredient_occurrences import default_list_output, run_aggregation


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("data/normalized_yaml"),
        help="Directory containing normalized recipe YAML files.",
    )
    parser.add_argument(
        "--occurrences-output",
        type=Path,
        default=Path("output/ingredient_occurrences.tsv"),
        help="Canonical uncapped occurrence TSV.",
    )
    parser.add_argument(
        "--mapped-output",
        type=Path,
        default=Path("output/mapped_ingredients.yaml"),
        help="Mapped compatibility-view YAML.",
    )
    parser.add_argument(
        "--unmapped-output",
        type=Path,
        default=Path("output/unmapped_ingredients.yaml"),
        help="Unmapped compatibility-view YAML.",
    )
    parser.add_argument(
        "--errors-output",
        type=Path,
        default=Path("output/ingredient_aggregation_errors.tsv"),
        help="Machine-readable input error report.",
    )
    parser.add_argument(
        "--list-output",
        type=Path,
        default=None,
        help="Ingredient list TSV (default: ingredients_list.tsv beside --occurrences-output).",
    )
    parser.add_argument(
        "--min-occurrences",
        type=int,
        default=1,
        help="Minimum group size retained in YAML views; TSV is always complete.",
    )
    parser.add_argument("--verbose", action="store_true", help="Print a compact summary.")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.list_output is None:
        args.list_output = default_list_output(args.occurrences_output)
    return run_aggregation(
        input_dir=args.input_dir,
        occurrences_output=args.occurrences_output,
        mapped_output=args.mapped_output,
        unmapped_output=args.unmapped_output,
        errors_output=args.errors_output,
        list_output=args.list_output,
        min_occurrences=args.min_occurrences,
        verbose=args.verbose,
    )


if __name__ == "__main__":
    raise SystemExit(main())
