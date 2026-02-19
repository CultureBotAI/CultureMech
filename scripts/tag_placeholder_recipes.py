#!/usr/bin/env python3
"""Tag recipes with placeholder ingredients for quality transparency.

Adds data_quality_flags to recipes that have placeholder ingredients
like "See source for composition". This provides transparency about
data quality limitations.

Usage:
    python scripts/tag_placeholder_recipes.py [OPTIONS]

Options:
    --normalized-dir DIR   Directory with normalized recipes (default: data/normalized_yaml)
    --dry-run              Show what would be tagged without writing
    --verbose              Show detailed progress
"""

import argparse
import logging
import re
import sys
from datetime import datetime
from pathlib import Path

import yaml

logger = logging.getLogger(__name__)


# Patterns that indicate placeholder ingredients
PLACEHOLDER_PATTERNS = [
    r'see\s+source',
    r'refer\s+to',
    r'available\s+at',
    r'contact\s+source',
    r'not\s+specified',
    r'unknown',
    r'composition\s+not\s+available',
]


def is_placeholder(ingredient_name: str) -> bool:
    """Check if ingredient name is a placeholder.

    Args:
        ingredient_name: Ingredient preferred_term

    Returns:
        True if placeholder
    """
    if not ingredient_name:
        return False

    name_lower = ingredient_name.lower()
    for pattern in PLACEHOLDER_PATTERNS:
        if re.search(pattern, name_lower):
            return True

    return False


def has_placeholder_ingredients(recipe: dict) -> bool:
    """Check if recipe has any placeholder ingredients.

    Args:
        recipe: Recipe dictionary

    Returns:
        True if has placeholders
    """
    ingredients = recipe.get('ingredients', [])

    for ing in ingredients:
        if isinstance(ing, dict):
            preferred_term = ing.get('preferred_term', '')
            if is_placeholder(preferred_term):
                return True

    return False


def tag_recipe(recipe: dict) -> bool:
    """Add data quality flag to recipe if needed.

    Args:
        recipe: Recipe dictionary

    Returns:
        True if tag was added
    """
    # Check if already tagged
    flags = recipe.get('data_quality_flags', [])
    if 'incomplete_composition' in flags:
        return False

    # Check if has placeholder ingredients
    if not has_placeholder_ingredients(recipe):
        return False

    # Add flag
    if 'data_quality_flags' not in recipe:
        recipe['data_quality_flags'] = []

    recipe['data_quality_flags'].append('incomplete_composition')

    # Add curation entry
    if 'curation_history' not in recipe:
        recipe['curation_history'] = []

    recipe['curation_history'].append({
        'timestamp': datetime.now().isoformat(),
        'curator': 'quality-tagger-v1.0',
        'action': 'Added data quality flag',
        'notes': 'Marked as incomplete_composition due to placeholder ingredients'
    })

    return True


def tag_directory(normalized_dir: Path, dry_run: bool = False, verbose: bool = False) -> dict:
    """Tag all recipes with placeholder ingredients.

    Args:
        normalized_dir: Directory with normalized recipes
        dry_run: If True, don't write files
        verbose: Show detailed progress

    Returns:
        Statistics dictionary
    """
    stats = {
        'total': 0,
        'tagged': 0,
        'already_tagged': 0,
        'no_placeholders': 0,
    }

    # Find all YAML files
    yaml_files = sorted(normalized_dir.rglob('*.yaml'))
    stats['total'] = len(yaml_files)

    logger.info(f"Processing {len(yaml_files)} recipe files...")

    for i, recipe_path in enumerate(yaml_files, 1):
        if verbose or i % 1000 == 0:
            logger.info(f"[{i}/{len(yaml_files)}] Processing {recipe_path.name}")

        try:
            # Load recipe
            with open(recipe_path, 'r', encoding='utf-8') as f:
                recipe = yaml.safe_load(f)

            if not isinstance(recipe, dict):
                continue

            # Check if already tagged
            flags = recipe.get('data_quality_flags', [])
            if 'incomplete_composition' in flags:
                stats['already_tagged'] += 1
                continue

            # Try to tag
            was_tagged = tag_recipe(recipe)

            if was_tagged:
                stats['tagged'] += 1

                if not dry_run:
                    # Write tagged recipe
                    with open(recipe_path, 'w', encoding='utf-8') as f:
                        yaml.safe_dump(
                            recipe,
                            f,
                            default_flow_style=False,
                            allow_unicode=True,
                            sort_keys=False
                        )

                    if verbose:
                        logger.info(f"  ✓ Tagged {recipe_path.name}")
                else:
                    if verbose:
                        logger.info(f"  Would tag {recipe_path.name}")
            else:
                stats['no_placeholders'] += 1

        except Exception as e:
            logger.error(f"Error processing {recipe_path}: {e}")

    return stats


def print_stats(stats: dict):
    """Print tagging statistics.

    Args:
        stats: Statistics dictionary
    """
    print("\n" + "="*60)
    print("QUALITY TAGGING STATISTICS")
    print("="*60)
    print(f"Total recipes:        {stats['total']}")
    print(f"Tagged:               {stats['tagged']}")
    print(f"Already tagged:       {stats['already_tagged']}")
    print(f"No placeholders:      {stats['no_placeholders']}")
    print("="*60 + "\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Tag recipes with placeholder ingredients',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--normalized-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Directory with normalized recipes (default: data/normalized_yaml)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be tagged without writing files'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed progress'
    )

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format='%(message)s'
    )

    # Validate input directory
    if not args.normalized_dir.exists():
        logger.error(f"Normalized directory not found: {args.normalized_dir}")
        sys.exit(1)

    if args.dry_run:
        logger.info("DRY RUN MODE - no files will be modified\n")

    # Tag recipes
    stats = tag_directory(args.normalized_dir, dry_run=args.dry_run, verbose=args.verbose)

    # Print results
    print_stats(stats)

    # Summary
    if args.dry_run:
        print(f"Would tag {stats['tagged']} recipes")
    else:
        print(f"Tagged {stats['tagged']} recipes with 'incomplete_composition' flag")


if __name__ == '__main__':
    main()
