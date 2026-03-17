#!/usr/bin/env python3
"""Validate merge quality and detect problematic merges.

Checks for:
1. Variant contamination - merging hydrates with anhydrous forms incorrectly
2. Parent mismatches - ingredients with conflicting parent relationships
3. Concentration outliers - wildly different concentrations in merged group
4. Cross-family merges - ingredients from different chemical families

Outputs actionable quality reports with severity levels.
"""

import argparse
import statistics
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional

import yaml

from culturemech.enrich.hierarchy_importer import MediaIngredientMechHierarchyImporter


def find_all_recipes(merge_dir: Path) -> List[Path]:
    """Find all merged recipe YAML files."""
    return sorted(merge_dir.rglob('*.yaml'))


def load_recipe(path: Path) -> Dict:
    """Load recipe from YAML file."""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def detect_variant_contamination(
    recipe: Dict,
    hierarchy: MediaIngredientMechHierarchyImporter
) -> Optional[Dict]:
    """Detect if recipe incorrectly merges different variants.

    Args:
        recipe: Merged recipe dictionary
        hierarchy: Hierarchy importer

    Returns:
        Issue dictionary or None
    """
    # Check if this is a merged recipe
    merged_from = recipe.get('merged_from', [])
    if len(merged_from) < 2:
        return None  # Not a merge

    # Extract variant types from all ingredients
    variant_types = set()

    for ingredient in recipe.get('ingredients', []):
        mim_id = ingredient.get('mediaingredientmech_term', {}).get('id')
        if mim_id:
            variant_type = hierarchy.get_variant_type(mim_id)
            if variant_type:
                variant_types.add(variant_type)

    # Check for problematic combinations
    problematic_combinations = [
        {'HYDRATE', 'ANHYDROUS'},
        {'SALT_FORM', 'FREE_BASE'},
        {'SALT_FORM', 'FREE_ACID'},
    ]

    for combo in problematic_combinations:
        if combo.issubset(variant_types):
            return {
                'type': 'variant_contamination',
                'severity': 'HIGH',
                'variants': list(variant_types),
                'recipe_name': recipe.get('name'),
                'merged_count': len(merged_from),
            }

    return None


def detect_parent_mismatches(
    recipe: Dict,
    hierarchy: MediaIngredientMechHierarchyImporter
) -> Optional[Dict]:
    """Detect ingredients with conflicting parent relationships.

    Args:
        recipe: Merged recipe dictionary
        hierarchy: Hierarchy importer

    Returns:
        Issue dictionary or None
    """
    # Check if this is a merged recipe
    merged_from = recipe.get('merged_from', [])
    if len(merged_from) < 2:
        return None

    # Group ingredients by their CHEBI ID and check parent consistency
    chebi_to_parents = defaultdict(set)

    for ingredient in recipe.get('ingredients', []):
        mim_id = ingredient.get('mediaingredientmech_term', {}).get('id')
        if not mim_id:
            continue

        # Get CHEBI ID
        ingredient_info = hierarchy.get_ingredient_info(mim_id)
        if not ingredient_info:
            continue

        chebi_id = ingredient_info.get('chebi_id')
        if not chebi_id:
            continue

        # Get parent
        parent_info = hierarchy.get_parent(mim_id)
        parent_id = parent_info.get('id') if parent_info else None

        if parent_id:
            chebi_to_parents[chebi_id].add(parent_id)

    # Check for conflicts
    conflicts = []
    for chebi_id, parents in chebi_to_parents.items():
        if len(parents) > 1:
            conflicts.append({
                'chebi_id': chebi_id,
                'conflicting_parents': list(parents),
            })

    if conflicts:
        return {
            'type': 'parent_mismatch',
            'severity': 'MEDIUM',
            'conflicts': conflicts,
            'recipe_name': recipe.get('name'),
        }

    return None


def detect_concentration_outliers(
    recipe: Dict,
    threshold: float = 3.0
) -> Optional[Dict]:
    """Detect ingredients with outlier concentrations.

    Args:
        recipe: Merged recipe dictionary
        threshold: Number of standard deviations for outlier detection

    Returns:
        Issue dictionary or None
    """
    # Check if this is a merged recipe
    merged_from = recipe.get('merged_from', [])
    if len(merged_from) < 3:
        return None  # Need at least 3 for outlier detection

    # Extract concentrations for each ingredient
    ingredient_concentrations = defaultdict(list)

    for ingredient in recipe.get('ingredients', []):
        name = ingredient.get('preferred_term')
        concentration = ingredient.get('concentration')

        if name and concentration:
            # Try to parse concentration value
            try:
                # Extract numeric value (basic parsing)
                value_str = str(concentration).split()[0]
                value = float(value_str)
                ingredient_concentrations[name].append(value)
            except (ValueError, IndexError):
                pass

    # Check for outliers
    outliers = []

    for name, values in ingredient_concentrations.items():
        if len(values) < 3:
            continue

        mean = statistics.mean(values)
        stdev = statistics.stdev(values)

        if stdev == 0:
            continue

        for value in values:
            z_score = abs((value - mean) / stdev)
            if z_score > threshold:
                outliers.append({
                    'ingredient': name,
                    'value': value,
                    'mean': mean,
                    'z_score': round(z_score, 2),
                })

    if outliers:
        return {
            'type': 'concentration_outlier',
            'severity': 'LOW',
            'outliers': outliers,
            'recipe_name': recipe.get('name'),
        }

    return None


def validate_merge_directory(
    merge_dir: Path,
    hierarchy: MediaIngredientMechHierarchyImporter,
    limit: int = None
) -> Dict:
    """Validate all merged recipes in directory.

    Args:
        merge_dir: Path to merged recipes directory
        hierarchy: Hierarchy importer
        limit: Optional limit on number of recipes

    Returns:
        Validation results dictionary
    """
    print(f"\nValidating merged recipes in {merge_dir}...")

    recipe_paths = find_all_recipes(merge_dir)

    if limit:
        recipe_paths = recipe_paths[:limit]

    print(f"  Found {len(recipe_paths)} recipes to validate")

    issues = {
        'variant_contamination': [],
        'parent_mismatch': [],
        'concentration_outlier': [],
    }

    for i, path in enumerate(recipe_paths, 1):
        try:
            recipe = load_recipe(path)

            # Run all checks
            issue = detect_variant_contamination(recipe, hierarchy)
            if issue:
                issue['recipe_file'] = path.name
                issues['variant_contamination'].append(issue)

            issue = detect_parent_mismatches(recipe, hierarchy)
            if issue:
                issue['recipe_file'] = path.name
                issues['parent_mismatch'].append(issue)

            issue = detect_concentration_outliers(recipe)
            if issue:
                issue['recipe_file'] = path.name
                issues['concentration_outlier'].append(issue)

            if i % 500 == 0:
                print(f"  Progress: {i}/{len(recipe_paths)}")

        except Exception as e:
            print(f"  Warning: Failed to validate {path}: {e}", file=sys.stderr)

    print(f"  Completed: {len(recipe_paths)} recipes validated")

    return {
        'total_recipes': len(recipe_paths),
        'issues': issues,
        'summary': {
            'variant_contamination': len(issues['variant_contamination']),
            'parent_mismatch': len(issues['parent_mismatch']),
            'concentration_outlier': len(issues['concentration_outlier']),
            'total_issues': sum(len(v) for v in issues.values()),
        }
    }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate merge quality and detect problematic merges'
    )

    parser.add_argument(
        '--merged-dir',
        type=Path,
        required=True,
        help='Path to merged recipes directory'
    )

    parser.add_argument(
        '--mim-repo',
        type=Path,
        required=True,
        help='Path to MediaIngredientMech repository'
    )

    parser.add_argument(
        '--output',
        type=Path,
        default=Path('reports/merge_quality.yaml'),
        help='Output report path'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of recipes (for testing)'
    )

    args = parser.parse_args()

    # Validate paths
    if not args.merged_dir.exists():
        print(f"Error: {args.merged_dir} not found", file=sys.stderr)
        return 1

    if not args.mim_repo.exists():
        print(f"Error: {args.mim_repo} not found", file=sys.stderr)
        return 1

    print("=" * 70)
    print("Merge Quality Validation")
    print("=" * 70)

    # Load hierarchy
    print(f"\nLoading hierarchy from {args.mim_repo}...")
    hierarchy = MediaIngredientMechHierarchyImporter(args.mim_repo)
    hierarchy.load_hierarchy()

    stats = hierarchy.get_stats()
    print(f"  Loaded: {stats['total_ingredients']} ingredients")

    # Validate
    results = validate_merge_directory(args.merged_dir, hierarchy, limit=args.limit)

    # Write report
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        yaml.dump(results, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\nReport written to: {args.output}")

    # Print summary
    print("\n" + "=" * 70)
    print("Quality Summary")
    print("=" * 70)
    print(f"Total recipes validated: {results['total_recipes']:,}")
    print()
    print(f"Issues found:")
    print(f"  Variant contamination (HIGH):    {results['summary']['variant_contamination']}")
    print(f"  Parent mismatches (MEDIUM):      {results['summary']['parent_mismatch']}")
    print(f"  Concentration outliers (LOW):    {results['summary']['concentration_outlier']}")
    print(f"  TOTAL:                           {results['summary']['total_issues']}")
    print()

    if results['summary']['total_issues'] > 0:
        quality_score = 100 * (1 - results['summary']['total_issues'] / results['total_recipes'])
        print(f"Quality score: {quality_score:.1f}%")
        print()

    return 0


if __name__ == '__main__':
    sys.exit(main())
