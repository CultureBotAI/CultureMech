#!/usr/bin/env python3
"""
Enrich CultureMech recipes with KG-Microbe exact matches.

Finds recipes that exactly match KG-Microbe mediadive media (by ingredient composition)
and adds the kg_microbe_match field to the YAML files.

Usage:
    python scripts/enrich_with_kg_microbe_matches.py \
        --kg-microbe-dir /path/to/kg-microbe \
        --recipe-dir data/normalized_yaml/bacterial \
        [--dry-run] \
        [--limit N]
"""

import argparse
import logging
from pathlib import Path
import yaml
from datetime import datetime, timezone
from typing import Dict, Any

from culturemech.match import KGMediaMatcher

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


def enrich_recipe_with_kg_match(
    recipe_file: Path,
    matcher: KGMediaMatcher,
    dry_run: bool = False
) -> Dict[str, Any]:
    """
    Enrich a single recipe with kg_microbe_match field.

    Args:
        recipe_file: Path to recipe YAML
        matcher: KGMediaMatcher instance
        dry_run: If True, don't write changes

    Returns:
        Dict with operation results
    """
    result = {
        'file': str(recipe_file),
        'had_match_before': False,
        'exact_match_found': False,
        'match_id': None,
        'match_name': None,
        'ingredient_count': 0,
        'updated': False
    }

    # Load recipe
    with open(recipe_file) as f:
        data = yaml.safe_load(f)

    # Check if already has kg_microbe_match
    result['had_match_before'] = 'kg_microbe_match' in data

    # Extract ingredients
    recipe_ingredients = matcher.extract_recipe_ingredients(recipe_file)
    result['ingredient_count'] = len(recipe_ingredients)

    if not recipe_ingredients:
        logger.debug(f"No ingredients in {recipe_file.name}, skipping")
        return result

    # Find exact match
    exact_match_id = matcher.find_exact_match(recipe_ingredients)

    if exact_match_id:
        result['exact_match_found'] = True
        result['match_id'] = f"mediadive.medium:{exact_match_id}"
        result['match_name'] = matcher.get_medium_name(exact_match_id)

        # Update recipe YAML
        if data.get('kg_microbe_match') != result['match_id']:
            data['kg_microbe_match'] = result['match_id']

            # Add curation history entry
            if 'curation_history' not in data:
                data['curation_history'] = []

            data['curation_history'].append({
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'curator': 'kg-microbe-matcher-v1.0',
                'action': 'Added KG-Microbe exact match',
                'notes': f"Matched to {result['match_name']} ({result['match_id']}) based on ingredient composition"
            })

            if not dry_run:
                # Write updated YAML
                with open(recipe_file, 'w') as f:
                    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

                result['updated'] = True
                logger.info(f"✓ {recipe_file.name} → {result['match_name']} ({result['match_id']})")
            else:
                result['updated'] = True  # Would have been updated
                logger.info(f"[DRY RUN] {recipe_file.name} → {result['match_name']} ({result['match_id']})")

    return result


def main():
    """Main enrichment pipeline."""
    parser = argparse.ArgumentParser(
        description='Enrich CultureMech recipes with KG-Microbe exact matches'
    )
    parser.add_argument(
        '--kg-microbe-dir',
        type=Path,
        required=True,
        help='Path to kg-microbe repository root'
    )
    parser.add_argument(
        '--recipe-dir',
        type=Path,
        default=Path('data/normalized_yaml/bacterial'),
        help='Directory containing recipe YAML files (default: data/normalized_yaml/bacterial)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print changes without writing files'
    )
    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of recipes to process (for testing)'
    )

    args = parser.parse_args()

    # Validate paths
    if not args.kg_microbe_dir.exists():
        logger.error(f"KG-Microbe directory not found: {args.kg_microbe_dir}")
        return 1

    if not args.recipe_dir.exists():
        logger.error(f"Recipe directory not found: {args.recipe_dir}")
        return 1

    logger.info(f"Loading KG-Microbe data from {args.kg_microbe_dir}")
    matcher = KGMediaMatcher(args.kg_microbe_dir)

    # Find all recipe YAML files
    recipe_files = list(args.recipe_dir.glob('*.yaml'))

    if not recipe_files:
        logger.warning(f"No YAML files found in {args.recipe_dir}")
        return 0

    if args.limit:
        recipe_files = recipe_files[:args.limit]
        logger.info(f"Limited to {args.limit} recipes")

    logger.info(f"Processing {len(recipe_files)} recipes...")
    if args.dry_run:
        logger.info("DRY RUN MODE - no files will be modified")

    # Statistics
    stats = {
        'total': 0,
        'had_match_before': 0,
        'exact_match_found': 0,
        'updated': 0,
        'no_ingredients': 0
    }

    # Process each recipe
    for recipe_file in recipe_files:
        result = enrich_recipe_with_kg_match(recipe_file, matcher, dry_run=args.dry_run)

        stats['total'] += 1
        if result['had_match_before']:
            stats['had_match_before'] += 1
        if result['exact_match_found']:
            stats['exact_match_found'] += 1
        if result['updated']:
            stats['updated'] += 1
        if result['ingredient_count'] == 0:
            stats['no_ingredients'] += 1

    # Print summary
    print()
    print("=" * 80)
    print("ENRICHMENT SUMMARY")
    print("=" * 80)
    print()
    print(f"Total recipes processed:      {stats['total']}")
    print(f"Already had match:            {stats['had_match_before']}")
    print(f"Exact matches found:          {stats['exact_match_found']}")
    print(f"Recipes updated:              {stats['updated']}")
    print(f"Recipes without ingredients:  {stats['no_ingredients']}")
    print()

    if args.dry_run:
        print("NOTE: This was a dry run. No files were modified.")
        print("      Run without --dry-run to apply changes.")
        print()

    if stats['updated'] > 0 and not args.dry_run:
        print(f"✓ Successfully enriched {stats['updated']} recipes with kg_microbe_match")
    elif stats['exact_match_found'] == 0:
        print("⚠ No exact matches found in KG-Microbe for any recipes")

    return 0


if __name__ == '__main__':
    exit(main())
