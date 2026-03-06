#!/usr/bin/env python3
"""
Generate statistics and reports from unmapped ingredients data.

Usage:
    python scripts/unmapped_ingredients_stats.py [--input FILE] [--top N]
"""

import argparse
import sys
from pathlib import Path

import yaml


def load_unmapped_data(file_path: str) -> dict:
    """Load the unmapped ingredients YAML file."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)


def print_summary(data: dict):
    """Print high-level summary statistics."""
    print("=" * 70)
    print("UNMAPPED INGREDIENTS SUMMARY")
    print("=" * 70)
    print(f"Generation Date: {data['generation_date']}")
    print(f"Total Unmapped Ingredients: {data['total_unmapped_count']}")
    print(f"Media with Unmapped: {data['media_count']}")
    print()


def print_category_breakdown(data: dict):
    """Print category-wise breakdown."""
    print("BREAKDOWN BY CATEGORY")
    print("-" * 70)
    print(f"{'Category':<15} {'Media':<10} {'Instances':<12} {'Unique':<10}")
    print("-" * 70)

    for cat in data['summary_by_category']:
        print(f"{cat['category']:<15} "
              f"{cat['media_with_unmapped']:<10} "
              f"{cat['total_unmapped_instances']:<12} "
              f"{cat['unique_unmapped_count']:<10}")

    print()


def print_top_unmapped(data: dict, top_n: int = 20):
    """Print top N most frequent unmapped ingredients."""
    print(f"TOP {top_n} MOST FREQUENT UNMAPPED INGREDIENTS")
    print("-" * 70)

    ingredients = data['unmapped_ingredients'][:top_n]

    for i, ing in enumerate(ingredients, 1):
        placeholder = ing['placeholder_id']
        count = ing['occurrence_count']
        parsed = ing.get('parsed_chemical_name', 'N/A')

        print(f"{i}. Placeholder: '{placeholder}' (occurs {count} times)")
        if parsed != 'N/A':
            print(f"   Parsed name: {parsed}")

        # Show first few raw texts
        if ing['raw_ingredient_text']:
            first_raw = ing['raw_ingredient_text'][0]
            if len(first_raw) > 80:
                first_raw = first_raw[:77] + "..."
            print(f"   Raw text: {first_raw}")

        print()


def print_mapping_coverage(data: dict):
    """Calculate and print mapping coverage statistics."""
    print("MAPPING COVERAGE ANALYSIS")
    print("-" * 70)

    total_ingredients = data['total_unmapped_count']
    total_instances = sum(ing['occurrence_count'] for ing in data['unmapped_ingredients'])

    # Calculate ingredients by occurrence frequency
    freq_ranges = {
        '1-5': 0,
        '6-20': 0,
        '21-50': 0,
        '51-100': 0,
        '100+': 0
    }

    for ing in data['unmapped_ingredients']:
        count = ing['occurrence_count']
        if count <= 5:
            freq_ranges['1-5'] += 1
        elif count <= 20:
            freq_ranges['6-20'] += 1
        elif count <= 50:
            freq_ranges['21-50'] += 1
        elif count <= 100:
            freq_ranges['51-100'] += 1
        else:
            freq_ranges['100+'] += 1

    print(f"Total unique unmapped: {total_ingredients}")
    print(f"Total instances: {total_instances}")
    print(f"Average occurrences per ingredient: {total_instances / total_ingredients:.1f}")
    print()
    print("Frequency distribution:")
    for range_name, count in freq_ranges.items():
        pct = (count / total_ingredients * 100) if total_ingredients > 0 else 0
        print(f"  {range_name} occurrences: {count} ingredients ({pct:.1f}%)")

    print()


def print_category_priorities(data: dict):
    """Suggest priorities for mapping efforts by category."""
    print("MAPPING PRIORITY RECOMMENDATIONS")
    print("-" * 70)

    categories = sorted(
        data['summary_by_category'],
        key=lambda x: x['total_unmapped_instances'],
        reverse=True
    )

    print("Priority order based on instance count:")
    for i, cat in enumerate(categories, 1):
        category = cat['category']
        instances = cat['total_unmapped_instances']
        unique = cat['unique_unmapped_count']
        media = cat['media_with_unmapped']

        print(f"{i}. {category}: {instances} instances across {media} media")
        print(f"   ({unique} unique ingredients to map)")

    print()


def generate_report(input_file: str, top_n: int = 20):
    """Generate complete statistics report."""
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

    except FileNotFoundError:
        print(f"Error: File not found: {input_file}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description='Generate statistics from unmapped ingredients data'
    )

    parser.add_argument(
        '--input',
        default='output/unmapped_ingredients.yaml',
        help='Input unmapped ingredients YAML file'
    )

    parser.add_argument(
        '--top',
        type=int,
        default=20,
        help='Number of top ingredients to show (default: 20)'
    )

    args = parser.parse_args()
    generate_report(args.input, args.top)


if __name__ == '__main__':
    main()
