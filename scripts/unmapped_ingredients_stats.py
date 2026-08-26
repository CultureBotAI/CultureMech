#!/usr/bin/env python3
"""Generate a human-readable report from the #337 unresolved summary."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml


def load_unmapped_data(file_path: str | Path) -> dict[str, Any]:
    """Load one deterministic unmapped-ingredients YAML view."""

    with Path(file_path).open(encoding="utf-8") as stream:
        value = yaml.safe_load(stream)
    if not isinstance(value, dict):
        raise ValueError("unmapped ingredient report root must be a mapping")
    return value


def print_summary(data: dict[str, Any]) -> None:
    """Print high-level summary statistics."""

    print("=" * 70)
    print("UNMAPPED INGREDIENTS SUMMARY")
    print("=" * 70)
    print(f"Total unresolved groups: {data['total_unmapped_count']}")
    print(f"Total direct occurrences: {data['total_instances']}")
    print(f"Recipes with unresolved ingredients: {data['recipe_count']}")
    print()


def print_category_breakdown(data: dict[str, Any]) -> None:
    """Print category-wise breakdown."""

    print("BREAKDOWN BY CATEGORY")
    print("-" * 70)
    print(f"{'Category':<15} {'Recipes':<10} {'Instances':<12} {'Unique':<10}")
    print("-" * 70)
    for category in data["summary_by_category"]:
        print(
            f"{category['category']:<15} "
            f"{category['recipes_with_unmapped']:<10} "
            f"{category['total_unmapped_instances']:<12} "
            f"{category['unique_unmapped_count']:<10}"
        )
    print()


def print_top_unmapped(data: dict[str, Any], top_n: int = 20) -> None:
    """Print the most frequent unresolved groups."""

    print(f"TOP {top_n} MOST FREQUENT UNMAPPED INGREDIENTS")
    print("-" * 70)
    for index, ingredient in enumerate(data["unmapped_ingredients"][:top_n], 1):
        placeholder = ingredient["placeholder_id"]
        count = ingredient["occurrence_count"]
        parsed = ingredient.get("parsed_chemical_name") or "N/A"
        print(f"{index}. Placeholder: '{placeholder}' (occurs {count} times)")
        if parsed != "N/A":
            print(f"   Parsed name: {parsed}")
        raw_texts = ingredient.get("raw_ingredient_text") or []
        if raw_texts:
            first_raw = str(raw_texts[0])
            if len(first_raw) > 80:
                first_raw = first_raw[:77] + "..."
            print(f"   Raw text: {first_raw}")
        print()


def print_mapping_coverage(data: dict[str, Any]) -> None:
    """Print occurrence-frequency statistics for unresolved groups."""

    print("MAPPING COVERAGE ANALYSIS")
    print("-" * 70)
    total_groups = int(data["total_unmapped_count"])
    total_instances = int(data["total_instances"])
    frequency_ranges = {"1-5": 0, "6-20": 0, "21-50": 0, "51-100": 0, "100+": 0}
    for ingredient in data["unmapped_ingredients"]:
        count = int(ingredient["occurrence_count"])
        if count <= 5:
            frequency_ranges["1-5"] += 1
        elif count <= 20:
            frequency_ranges["6-20"] += 1
        elif count <= 50:
            frequency_ranges["21-50"] += 1
        elif count <= 100:
            frequency_ranges["51-100"] += 1
        else:
            frequency_ranges["100+"] += 1

    average = total_instances / total_groups if total_groups else 0.0
    print(f"Total unresolved groups: {total_groups}")
    print(f"Total direct occurrences: {total_instances}")
    print(f"Average occurrences per group: {average:.1f}")
    print()
    print("Frequency distribution:")
    for range_name, count in frequency_ranges.items():
        percentage = count / total_groups * 100 if total_groups else 0.0
        print(f"  {range_name} occurrences: {count} groups ({percentage:.1f}%)")
    print()


def print_category_priorities(data: dict[str, Any]) -> None:
    """Suggest mapping priorities by complete direct-occurrence count."""

    print("MAPPING PRIORITY RECOMMENDATIONS")
    print("-" * 70)
    categories = sorted(
        data["summary_by_category"],
        key=lambda value: (-value["total_unmapped_instances"], value["category"]),
    )
    print("Priority order based on direct-occurrence count:")
    for index, category in enumerate(categories, 1):
        name = category["category"]
        instances = category["total_unmapped_instances"]
        unique = category["unique_unmapped_count"]
        recipes = category["recipes_with_unmapped"]
        print(f"{index}. {name}: {instances} occurrences across {recipes} recipes")
        print(f"   ({unique} unresolved groups to map)")
    print()


def generate_report(input_file: str | Path, top_n: int = 20) -> int:
    """Generate the complete report, returning a process exit code."""

    try:
        data = load_unmapped_data(input_file)
        print_summary(data)
        print_category_breakdown(data)
        print_top_unmapped(data, top_n)
        print_mapping_coverage(data)
        print_category_priorities(data)
        print("=" * 70)
        print("For detailed data, see:", input_file)
        print("=" * 70)
    except (OSError, KeyError, TypeError, ValueError, yaml.YAMLError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--input",
        default="output/unmapped_ingredients.yaml",
        help="Input unmapped ingredients YAML file",
    )
    parser.add_argument(
        "--top",
        type=int,
        default=20,
        help="Number of top unresolved groups to show (default: 20)",
    )
    args = parser.parse_args(argv)
    return generate_report(args.input, args.top)


if __name__ == "__main__":
    raise SystemExit(main())
