#!/usr/bin/env python3
"""Generate index files for recipe collections.

Creates JSON index files that catalog all recipes with key metadata:
- Recipe name, ID, category
- Ingredient count
- Source databases
- File location
- Timestamps

Generates indexes at multiple levels:
1. Per-category indexes (algae, bacterial, etc.)
2. Master index (all recipes)
3. By-source indexes (TOGO, MediaDive, etc.)
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

import yaml


def find_all_recipes(directory: Path) -> List[Path]:
    """Find all recipe YAML files."""
    recipes = []
    for category_dir in directory.iterdir():
        if category_dir.is_dir():
            recipes.extend(category_dir.glob('*.yaml'))
    return sorted(recipes)


def load_recipe(path: Path) -> Optional[Dict]:
    """Load recipe from YAML file."""
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        print(f"  Warning: Failed to load {path}: {e}", file=sys.stderr)
        return None


def extract_recipe_metadata(recipe: Dict, filepath: Path) -> Dict:
    """Extract key metadata from recipe.

    Args:
        recipe: Recipe dictionary
        filepath: Path to recipe file

    Returns:
        Metadata dictionary
    """
    # Extract source
    source = 'unknown'
    source_id = None
    media_term = recipe.get('media_term', {})
    if isinstance(media_term, dict):
        term = media_term.get('term', {})
        if isinstance(term, dict):
            term_id = term.get('id', '')
            source_id = term_id
            if 'TOGO:' in term_id:
                source = 'TOGO'
            elif 'mediadive.medium:' in term_id:
                source = 'MediaDive'
            elif 'komodo.medium:' in term_id:
                source = 'KOMODO'
            elif 'DSMZ' in term_id:
                source = 'DSMZ'
            elif 'mediadive.solution:' in term_id:
                source = 'MediaDive-Solutions'

    # Get CultureMech ID if present
    culturemech_id = recipe.get('id')

    # Count ingredients
    ingredient_count = len(recipe.get('ingredients', []))
    solution_count = len(recipe.get('solutions', []))

    # Get categories
    categories = recipe.get('categories', [])
    if not categories:
        category = recipe.get('category')
        if category:
            categories = [category]

    # Check if merged
    merged_from = recipe.get('merged_from', [])
    is_merged = len(merged_from) > 1

    # Get organism culture type
    organism_culture_type = recipe.get('organism_culture_type')

    # Check for enrichment
    has_hierarchy = 'mediaingredientmech_term' in str(recipe.get('ingredients', []))

    metadata = {
        'name': recipe.get('name'),
        'filename': filepath.name,
        'ingredient_count': ingredient_count,
    }

    # Add optional fields
    if culturemech_id:
        metadata['id'] = culturemech_id

    if source_id:
        metadata['source_id'] = source_id

    metadata['source'] = source

    if solution_count > 0:
        metadata['solution_count'] = solution_count

    if categories:
        metadata['categories'] = categories

    if is_merged:
        metadata['merged_from_count'] = len(merged_from)
        metadata['merged_sources'] = list(set(
            mf.split('_')[0] for mf in merged_from if '_' in mf
        ))

    if organism_culture_type:
        metadata['organism_culture_type'] = organism_culture_type

    if has_hierarchy:
        metadata['has_hierarchy_enrichment'] = True

    return metadata


def generate_category_indexes(
    recipe_dir: Path,
    output_dir: Path
) -> Dict[str, Dict]:
    """Generate index file for each category.

    Args:
        recipe_dir: Directory containing recipe categories
        output_dir: Directory to write index files

    Returns:
        Dictionary mapping category -> category index
    """
    print(f"\nGenerating category indexes...")

    category_indexes = {}

    for category_dir in sorted(recipe_dir.iterdir()):
        if not category_dir.is_dir():
            continue

        category = category_dir.name
        print(f"  Processing {category}...")

        recipes = sorted(category_dir.glob('*.yaml'))

        category_index = {
            'generated': datetime.now(timezone.utc).isoformat(),
            'category': category,
            'count': len(recipes),
            'recipes': {}
        }

        for recipe_path in recipes:
            recipe = load_recipe(recipe_path)
            if not recipe:
                continue

            metadata = extract_recipe_metadata(recipe, recipe_path)

            # Use ID or source_id or filename as key
            key = (
                metadata.get('id') or
                metadata.get('source_id') or
                recipe_path.stem
            )

            category_index['recipes'][key] = metadata

        # Write category index
        output_file = output_dir / f"{category}_index.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(category_index, f, indent=2, ensure_ascii=False)

        print(f"    ✓ {len(recipes)} recipes indexed → {output_file.name}")

        category_indexes[category] = category_index

    return category_indexes


def generate_master_index(
    category_indexes: Dict[str, Dict],
    output_path: Path
) -> Dict:
    """Generate master index combining all categories.

    Args:
        category_indexes: Dictionary of category indexes
        output_path: Path to write master index

    Returns:
        Master index dictionary
    """
    print(f"\nGenerating master index...")

    total_recipes = sum(idx['count'] for idx in category_indexes.values())

    master_index = {
        'generated': datetime.now(timezone.utc).isoformat(),
        'description': 'Master index of all CultureMech recipes',
        'total_recipes': total_recipes,
        'categories': {},
        'recipes': {}
    }

    # Add category summaries
    for category, idx in category_indexes.items():
        master_index['categories'][category] = {
            'count': idx['count'],
            'index_file': f"{category}_index.json"
        }

        # Add all recipes
        for recipe_id, metadata in idx['recipes'].items():
            # Add category to metadata
            metadata_with_cat = metadata.copy()
            metadata_with_cat['category_dir'] = category

            master_index['recipes'][recipe_id] = metadata_with_cat

    # Write master index
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(master_index, f, indent=2, ensure_ascii=False)

    print(f"  ✓ {total_recipes} recipes indexed → {output_path.name}")

    return master_index


def generate_source_indexes(
    master_index: Dict,
    output_dir: Path
) -> Dict[str, Dict]:
    """Generate index files grouped by source database.

    Args:
        master_index: Master index dictionary
        output_dir: Directory to write index files

    Returns:
        Dictionary mapping source -> source index
    """
    print(f"\nGenerating source indexes...")

    # Group recipes by source
    recipes_by_source = defaultdict(dict)

    for recipe_id, metadata in master_index['recipes'].items():
        source = metadata.get('source', 'unknown')
        recipes_by_source[source][recipe_id] = metadata

    source_indexes = {}

    for source, recipes in sorted(recipes_by_source.items()):
        source_index = {
            'generated': datetime.now(timezone.utc).isoformat(),
            'source': source,
            'count': len(recipes),
            'recipes': recipes
        }

        # Write source index
        output_file = output_dir / f"by_source_{source.lower()}_index.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(source_index, f, indent=2, ensure_ascii=False)

        print(f"  ✓ {len(recipes)} {source} recipes → {output_file.name}")

        source_indexes[source] = source_index

    return source_indexes


def generate_statistics(master_index: Dict, output_path: Path) -> Dict:
    """Generate statistics summary.

    Args:
        master_index: Master index dictionary
        output_path: Path to write statistics

    Returns:
        Statistics dictionary
    """
    print(f"\nGenerating statistics...")

    recipes = master_index['recipes']

    # Count by source
    by_source = defaultdict(int)
    for metadata in recipes.values():
        by_source[metadata.get('source', 'unknown')] += 1

    # Count by category
    by_category = defaultdict(int)
    for metadata in recipes.values():
        categories = metadata.get('categories', [])
        if not categories:
            categories = [metadata.get('category_dir', 'unknown')]
        for cat in categories:
            by_category[cat] += 1

    # Count merged
    merged_count = sum(
        1 for m in recipes.values()
        if m.get('merged_from_count', 0) > 1
    )

    # Count with hierarchy
    hierarchy_count = sum(
        1 for m in recipes.values()
        if m.get('has_hierarchy_enrichment', False)
    )

    # Ingredient statistics
    ingredient_counts = [
        m['ingredient_count']
        for m in recipes.values()
        if 'ingredient_count' in m
    ]

    stats = {
        'generated': datetime.now(timezone.utc).isoformat(),
        'total_recipes': len(recipes),
        'by_source': dict(sorted(by_source.items())),
        'by_category': dict(sorted(by_category.items())),
        'merged_recipes': merged_count,
        'with_hierarchy_enrichment': hierarchy_count,
        'ingredient_statistics': {
            'min': min(ingredient_counts) if ingredient_counts else 0,
            'max': max(ingredient_counts) if ingredient_counts else 0,
            'avg': round(sum(ingredient_counts) / len(ingredient_counts), 1) if ingredient_counts else 0,
        }
    }

    # Write statistics
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)

    print(f"  ✓ Statistics → {output_path.name}")

    return stats


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate index files for recipe collections'
    )

    parser.add_argument(
        '--recipe-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Path to recipe directory (default: data/normalized_yaml)'
    )

    parser.add_argument(
        '--output-dir',
        type=Path,
        help='Output directory for indexes (default: same as recipe-dir)'
    )

    parser.add_argument(
        '--master-only',
        action='store_true',
        help='Generate only master index (skip per-category indexes)'
    )

    parser.add_argument(
        '--stats-only',
        action='store_true',
        help='Generate only statistics (skip indexes)'
    )

    args = parser.parse_args()

    # Validate paths
    if not args.recipe_dir.exists():
        print(f"Error: Recipe directory not found: {args.recipe_dir}", file=sys.stderr)
        return 1

    # Set output directory
    output_dir = args.output_dir or args.recipe_dir
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 70)
    print("Recipe Index Generator")
    print("=" * 70)
    print(f"Recipe directory: {args.recipe_dir}")
    print(f"Output directory: {output_dir}")

    if not args.stats_only:
        # Generate category indexes
        category_indexes = generate_category_indexes(args.recipe_dir, output_dir)

        # Generate master index
        master_index_path = output_dir / 'recipe_index.json'
        master_index = generate_master_index(category_indexes, master_index_path)

        # Generate source indexes
        generate_source_indexes(master_index, output_dir)

        # Generate statistics
        stats_path = output_dir / 'recipe_statistics.json'
        stats = generate_statistics(master_index, stats_path)

    else:
        # Load existing master index for stats
        master_index_path = output_dir / 'recipe_index.json'
        if not master_index_path.exists():
            print(f"Error: Master index not found: {master_index_path}", file=sys.stderr)
            print("Run without --stats-only first to generate indexes", file=sys.stderr)
            return 1

        with open(master_index_path, 'r', encoding='utf-8') as f:
            master_index = json.load(f)

        stats_path = output_dir / 'recipe_statistics.json'
        stats = generate_statistics(master_index, stats_path)

    # Print summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total recipes indexed: {master_index.get('total_recipes', stats.get('total_recipes', 0)):,}")
    print()
    print("Files generated:")
    print(f"  • recipe_index.json (master index)")
    print(f"  • recipe_statistics.json")

    if not args.master_only:
        print(f"  • {len(master_index.get('categories', {}))} category indexes")
        print(f"  • {len(set(m.get('source') for m in master_index['recipes'].values()))} source indexes")

    print()
    print(f"✓ Index generation complete!")
    print()

    return 0


if __name__ == '__main__':
    sys.exit(main())
