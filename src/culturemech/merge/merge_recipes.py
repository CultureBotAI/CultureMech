#!/usr/bin/env python3
"""Main CLI script for merging recipes with identical ingredient sets.

This script identifies and merges recipes that have the same base formulation
(same chemicals) regardless of concentration, pH, temperature, or other parameters.

Process:
1. Scans normalized_yaml/ for all recipes
2. Groups recipes by ingredient fingerprint (CHEBI IDs + names)
3. Merges groups into canonical records with synonym tracking
4. Writes merged recipes to merge_yaml/merged/
5. Generates merge statistics

IMPORTANT: Matching is based on INGREDIENT IDENTITY only. Recipes with the same
chemicals but different concentrations are considered duplicates and will be merged.
This is useful for identifying that "LB Medium" exists across multiple databases
even with formulation variations.
"""

import argparse
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

from culturemech.merge.fingerprint import RecipeFingerprinter
from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merger import RecipeMerger


def find_all_recipes(normalized_dir: Path) -> list[Path]:
    """Find all recipe YAML files in normalized_yaml directory.

    Args:
        normalized_dir: Path to normalized_yaml directory

    Returns:
        List of recipe file paths
    """
    recipes = []
    for category_dir in normalized_dir.iterdir():
        if category_dir.is_dir():
            recipes.extend(category_dir.glob('*.yaml'))

    return sorted(recipes)


def progress_bar(current: int, total: int, prefix: str = '') -> None:
    """Display progress bar.

    Args:
        current: Current progress
        total: Total items
        prefix: Optional prefix message
    """
    bar_length = 50
    percent = current / total
    filled = int(bar_length * percent)
    bar = '█' * filled + '░' * (bar_length - filled)
    print(f'\r{prefix} [{bar}] {current}/{total} ({percent*100:.1f}%)', end='', flush=True)
    if current == total:
        print()  # Newline when complete


def generate_merge_stats(
    input_count: int,
    output_count: int,
    groups: dict,
    recipes_by_group: dict
) -> dict:
    """Generate merge statistics.

    Args:
        input_count: Number of input recipes
        output_count: Number of output recipes
        groups: Dictionary of fingerprint -> recipe paths
        recipes_by_group: Dictionary of fingerprint -> loaded recipe dicts

    Returns:
        Statistics dictionary
    """
    reduction = input_count - output_count
    reduction_pct = (reduction / input_count * 100) if input_count > 0 else 0

    # Find largest group
    largest_group_size = max((len(paths) for paths in groups.values()), default=0)

    # Count cross-category merges
    cross_category_count = 0
    for fp, paths in groups.items():
        if len(paths) > 1:
            recipes = recipes_by_group.get(fp, [])
            categories = set(r.get('category') for r in recipes if r.get('category'))
            if len(categories) > 1:
                cross_category_count += 1

    # Find top duplicates (groups with most recipes)
    top_duplicates = []
    duplicate_groups = [(fp, paths) for fp, paths in groups.items() if len(paths) >= 2]
    duplicate_groups.sort(key=lambda x: len(x[1]), reverse=True)

    for fp, paths in duplicate_groups[:10]:  # Top 10
        recipes = recipes_by_group.get(fp, [])
        if not recipes:
            continue

        # Get canonical name (most common)
        name_counts = Counter(r['name'] for r in recipes)
        canonical_name = name_counts.most_common(1)[0][0]

        # Get sources
        sources = set()
        for recipe in recipes:
            media_term = recipe.get('media_term', {})
            if isinstance(media_term, dict):
                term = media_term.get('term', {})
                if isinstance(term, dict):
                    term_id = term.get('id', '')
                    if 'TOGO:' in term_id:
                        sources.add('TOGO')
                    elif 'mediadive.medium:' in term_id:
                        sources.add('MediaDive')
                    elif 'komodo.medium:' in term_id:
                        sources.add('KOMODO')
                    elif 'DSMZ' in term_id:
                        sources.add('DSMZ')

        # Get categories
        categories = sorted(set(r.get('category') for r in recipes if r.get('category')))

        top_duplicates.append({
            'name': canonical_name,
            'count': len(paths),
            'sources': sorted(sources),
            'categories': categories,
        })

    stats = {
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'input_recipes': input_count,
        'output_recipes': output_count,
        'reduction': reduction,
        'reduction_percentage': round(reduction_pct, 1),
        'cross_category_merges': cross_category_count,
        'largest_group_size': largest_group_size,
        'top_duplicates': top_duplicates,
    }

    return stats


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Merge duplicate recipes from normalized_yaml to merge_yaml',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
  # Dry run to see what would be merged
  python -m culturemech.merge.merge_recipes --dry-run

  # Show statistics only
  python -m culturemech.merge.merge_recipes --stats-only

  # Perform actual merge
  python -m culturemech.merge.merge_recipes

  # Merge only groups with 3+ recipes
  python -m culturemech.merge.merge_recipes --min-group-size 3

  # Process only first 1000 recipes (for testing)
  python -m culturemech.merge.merge_recipes --limit 1000
        '''
    )

    parser.add_argument(
        '--normalized-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Path to normalized_yaml directory (default: data/normalized_yaml)'
    )

    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('data/merge_yaml/merged'),
        help='Path to output directory (default: data/merge_yaml/merged)'
    )

    parser.add_argument(
        '--stats-file',
        type=Path,
        default=Path('data/merge_yaml/merge_stats.json'),
        help='Path to statistics output file (default: data/merge_yaml/merge_stats.json)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be merged without writing files'
    )

    parser.add_argument(
        '--stats-only',
        action='store_true',
        help='Generate statistics without merging recipes'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Process only first N recipes (for testing)'
    )

    parser.add_argument(
        '--min-group-size',
        type=int,
        default=1,
        help='Minimum group size to process (default: 1, set to 2 to only merge duplicates)'
    )

    args = parser.parse_args()

    # Validate paths
    if not args.normalized_dir.exists():
        print(f"Error: Normalized directory not found: {args.normalized_dir}", file=sys.stderr)
        return 1

    print("=" * 70)
    print("Recipe Merge Tool - Ingredient Set Matching")
    print("=" * 70)
    print()
    print("NOTE: Recipes are matched by INGREDIENT SET only.")
    print("Concentration, pH, temperature, and preparation differences are IGNORED.")
    print("This identifies recipes with the same base formulation (same chemicals).")
    print()

    # Find all recipes
    print(f"Scanning {args.normalized_dir} for recipes...")
    all_recipes = find_all_recipes(args.normalized_dir)

    if args.limit:
        all_recipes = all_recipes[:args.limit]

    print(f"Found {len(all_recipes)} recipes")
    print()

    # Initialize matcher
    matcher = RecipeMatcher()

    # Group recipes by fingerprint
    print("Grouping recipes by ingredient fingerprint...")

    def progress_callback(current, total):
        progress_bar(current, total, prefix="Progress:")

    groups = matcher.group_recipes(
        all_recipes,
        min_group_size=args.min_group_size,
        progress_callback=progress_callback
    )

    print()
    print(f"Found {len(groups)} unique recipe groups")

    # Show skip statistics if available
    if hasattr(matcher, '_last_skip_stats'):
        stats = matcher._last_skip_stats
        skipped_total = stats['skipped_no_fingerprint'] + stats['skipped_error']

        if skipped_total > 0:
            print()
            print(f"⚠ Skipped {skipped_total} recipes:")
            for reason, count in stats['reasons'].items():
                print(f"  - {reason}: {count}")
            print()
            print(f"Successfully fingerprinted: {stats['successfully_fingerprinted']} recipes")
    print()

    # Load recipes for each group (for stats)
    print("Loading recipes for analysis...")
    recipes_by_group = {}
    for fp, paths in groups.items():
        recipes = []
        for path in paths:
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    recipe = yaml.safe_load(f)
                    recipes.append(recipe)
            except Exception as e:
                print(f"Warning: Failed to load {path}: {e}", file=sys.stderr)
        recipes_by_group[fp] = recipes

    print()

    # Generate statistics
    output_count = len(groups)
    stats = generate_merge_stats(
        input_count=len(all_recipes),
        output_count=output_count,
        groups=groups,
        recipes_by_group=recipes_by_group
    )

    # Display statistics
    print("=" * 70)
    print("Merge Statistics")
    print("=" * 70)
    print(f"Input recipes:          {stats['input_recipes']:,}")
    print(f"Output recipes:         {stats['output_recipes']:,}")
    print(f"Reduction:              {stats['reduction']:,} recipes ({stats['reduction_percentage']}%)")
    print(f"Cross-category merges:  {stats['cross_category_merges']}")
    print(f"Largest group size:     {stats['largest_group_size']}")
    print()

    if stats['top_duplicates']:
        print("Top duplicate groups:")
        for i, dup in enumerate(stats['top_duplicates'][:5], 1):
            sources_str = ', '.join(dup['sources']) if dup['sources'] else 'unknown'
            categories_str = ', '.join(dup['categories']) if dup['categories'] else 'none'
            print(f"  {i}. {dup['name']}")
            print(f"     Count: {dup['count']}, Sources: {sources_str}, Categories: {categories_str}")
        print()

    # If stats-only, stop here
    if args.stats_only:
        print("Statistics generated (use --dry-run or omit --stats-only to perform merge)")
        return 0

    # If dry-run, show what would be merged
    if args.dry_run:
        print("=" * 70)
        print("Dry Run - Recipe Groups (showing first 10 duplicate groups)")
        print("=" * 70)
        duplicate_groups = [(fp, paths) for fp, paths in groups.items() if len(paths) >= 2]
        duplicate_groups.sort(key=lambda x: len(x[1]), reverse=True)

        for i, (fp, paths) in enumerate(duplicate_groups[:10], 1):
            recipes = recipes_by_group.get(fp, [])
            names = [r['name'] for r in recipes]
            print(f"\n{i}. Group of {len(paths)} recipes:")
            for name in names:
                print(f"   - {name}")

        print()
        print(f"Would write {len(groups)} merged recipes to {args.output_dir}")
        print("Run without --dry-run to perform actual merge")
        return 0

    # Perform actual merge
    print("=" * 70)
    print("Merging Recipes")
    print("=" * 70)
    print()

    # Create output directory
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Initialize merger
    merger = RecipeMerger()

    # Merge each group
    print("Merging and writing recipes...")
    for i, (fp, paths) in enumerate(groups.items(), 1):
        try:
            # Merge group
            merged_recipe = merger.merge_group(paths, fingerprint=fp)

            # Generate output filename (use canonical name)
            filename = merged_recipe['name'].replace('/', '_').replace(' ', '_') + '.yaml'
            output_path = args.output_dir / filename

            # Write merged recipe
            with open(output_path, 'w', encoding='utf-8') as f:
                yaml.dump(merged_recipe, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

            if i % 500 == 0:
                progress_bar(i, len(groups), prefix="Progress:")

        except Exception as e:
            print(f"\nError merging group {fp}: {e}", file=sys.stderr)
            continue

    progress_bar(len(groups), len(groups), prefix="Progress:")
    print()

    # Write statistics
    print(f"Writing statistics to {args.stats_file}...")
    args.stats_file.parent.mkdir(parents=True, exist_ok=True)
    with open(args.stats_file, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2)

    print()
    print("=" * 70)
    print("Merge Complete!")
    print("=" * 70)
    print(f"Merged recipes written to: {args.output_dir}")
    print(f"Statistics written to: {args.stats_file}")
    print()
    print(f"Summary: {stats['input_recipes']:,} → {stats['output_recipes']:,} recipes")
    print(f"Reduction: {stats['reduction']:,} recipes ({stats['reduction_percentage']}%)")
    print()

    return 0


if __name__ == '__main__':
    sys.exit(main())
