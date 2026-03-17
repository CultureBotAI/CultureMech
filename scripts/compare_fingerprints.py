#!/usr/bin/env python3
"""Compare fingerprinting modes to analyze merge behavior differences.

Generates all three fingerprint types (original, chemical, variant) for
each recipe and analyzes how merge groups would differ between modes.

Outputs:
- Comparison statistics
- Recipes that would merge differently
- Variant pair analysis
- Mode comparison matrix
"""

import argparse
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Set, Tuple

import yaml

from culturemech.enrich.hierarchy_importer import MediaIngredientMechHierarchyImporter
from culturemech.merge.fingerprint import RecipeFingerprinter
from culturemech.merge.hierarchy_fingerprint import HierarchyAwareFingerprinter


def find_all_recipes(normalized_dir: Path) -> List[Path]:
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


def load_recipe(path: Path) -> Dict:
    """Load recipe from YAML file.

    Args:
        path: Path to recipe YAML file

    Returns:
        Recipe dictionary
    """
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        return yaml.safe_load(f)


def fingerprint_all_modes(
    recipe_paths: List[Path],
    hierarchy: MediaIngredientMechHierarchyImporter,
    limit: int = None
) -> Dict[str, Dict[str, str]]:
    """Generate fingerprints in all modes for each recipe.

    Args:
        recipe_paths: List of recipe file paths
        hierarchy: Hierarchy importer instance
        limit: Optional limit on number of recipes to process

    Returns:
        Dictionary mapping recipe_id -> {mode -> fingerprint}
    """
    print(f"\nGenerating fingerprints for {len(recipe_paths)} recipes...")

    # Initialize fingerprinters
    original_fp = RecipeFingerprinter()
    chemical_fp = HierarchyAwareFingerprinter(hierarchy, mode='chemical')
    variant_fp = HierarchyAwareFingerprinter(hierarchy, mode='variant')

    results = {}

    if limit:
        recipe_paths = recipe_paths[:limit]

    for i, path in enumerate(recipe_paths, 1):
        try:
            recipe = load_recipe(path)
            recipe_id = path.stem

            fingerprints = {}

            # Generate all fingerprints
            try:
                fingerprints['original'] = original_fp.fingerprint(recipe)
            except (ValueError, Exception):
                fingerprints['original'] = None

            try:
                fingerprints['chemical'] = chemical_fp.fingerprint(recipe)
            except (ValueError, Exception):
                fingerprints['chemical'] = None

            try:
                fingerprints['variant'] = variant_fp.fingerprint(recipe)
            except (ValueError, Exception):
                fingerprints['variant'] = None

            results[recipe_id] = fingerprints

            if i % 1000 == 0:
                print(f"  Progress: {i}/{len(recipe_paths)} recipes processed")

        except Exception as e:
            print(f"  Warning: Failed to process {path}: {e}", file=sys.stderr)

    print(f"  Completed: {len(results)} recipes fingerprinted")
    return results


def group_by_fingerprint(
    fingerprints: Dict[str, Dict[str, str]]
) -> Dict[str, Dict[str, List[str]]]:
    """Group recipes by fingerprint for each mode.

    Args:
        fingerprints: Recipe fingerprints by mode

    Returns:
        Dictionary mapping mode -> {fingerprint -> [recipe_ids]}
    """
    groups = {
        'original': defaultdict(list),
        'chemical': defaultdict(list),
        'variant': defaultdict(list)
    }

    for recipe_id, fps in fingerprints.items():
        for mode, fp in fps.items():
            if fp:  # Skip None fingerprints
                groups[mode][fp].append(recipe_id)

    return groups


def analyze_differences(
    groups: Dict[str, Dict[str, List[str]]],
    fingerprints: Dict[str, Dict[str, str]]
) -> Dict:
    """Analyze differences between fingerprinting modes.

    Args:
        groups: Recipe groups by mode
        fingerprints: Recipe fingerprints by mode

    Returns:
        Analysis dictionary with statistics and examples
    """
    print("\nAnalyzing differences between modes...")

    # Count groups by mode
    mode_stats = {}
    for mode, fp_groups in groups.items():
        # Only count groups with valid fingerprints
        valid_groups = {fp: ids for fp, ids in fp_groups.items() if fp}
        total_recipes = sum(len(ids) for ids in valid_groups.values())

        mode_stats[mode] = {
            'total_groups': len(valid_groups),
            'total_recipes': total_recipes,
            'singleton_groups': sum(1 for ids in valid_groups.values() if len(ids) == 1),
            'duplicate_groups': sum(1 for ids in valid_groups.values() if len(ids) >= 2),
            'largest_group': max((len(ids) for ids in valid_groups.values()), default=0),
        }

    # Find recipes that merge differently
    different_original_chemical = 0
    different_original_variant = 0
    different_chemical_variant = 0

    for recipe_id, fps in fingerprints.items():
        orig = fps.get('original')
        chem = fps.get('chemical')
        var = fps.get('variant')

        if orig and chem and orig != chem:
            different_original_chemical += 1

        if orig and var and orig != var:
            different_original_variant += 1

        if chem and var and chem != var:
            different_chemical_variant += 1

    analysis = {
        'mode_statistics': mode_stats,
        'fingerprint_differences': {
            'original_vs_chemical': different_original_chemical,
            'original_vs_variant': different_original_variant,
            'chemical_vs_variant': different_chemical_variant,
        },
    }

    return analysis


def find_variant_pairs(
    groups: Dict[str, Dict[str, List[str]]],
    normalized_dir: Path
) -> List[Dict]:
    """Find examples of variant pairs that merge differently.

    Args:
        groups: Recipe groups by mode
        normalized_dir: Path to normalized recipes

    Returns:
        List of variant pair examples
    """
    print("\nFinding variant pair examples...")

    examples = []

    # Find groups that merge in chemical mode but not in variant mode
    chemical_groups = groups['chemical']
    variant_groups = groups['variant']

    for chem_fp, chem_recipes in chemical_groups.items():
        if len(chem_recipes) < 2:
            continue  # Skip singletons

        # Check if these recipes have different variant fingerprints
        variant_fps = set()
        for recipe_id in chem_recipes:
            # Find this recipe's variant fingerprint
            for var_fp, var_recipes in variant_groups.items():
                if recipe_id in var_recipes:
                    variant_fps.add(var_fp)
                    break

        if len(variant_fps) > 1:
            # These recipes merge in chemical mode but not variant mode
            # This indicates variant pairs (hydrates, salts, etc.)
            examples.append({
                'chemical_fingerprint': chem_fp,
                'recipe_count': len(chem_recipes),
                'variant_count': len(variant_fps),
                'recipe_ids': chem_recipes[:5],  # First 5 examples
            })

            if len(examples) >= 20:
                break  # Limit to 20 examples

    print(f"  Found {len(examples)} variant pair examples")
    return examples


def generate_report(
    analysis: Dict,
    variant_examples: List[Dict],
    output_path: Path
) -> None:
    """Generate comparison report.

    Args:
        analysis: Analysis results
        variant_examples: Variant pair examples
        output_path: Path to output YAML file
    """
    report = {
        'fingerprint_comparison': {
            'modes_compared': ['original', 'chemical', 'variant'],
            'mode_statistics': analysis['mode_statistics'],
            'fingerprint_differences': analysis['fingerprint_differences'],
        },
        'variant_pair_examples': variant_examples,
        'summary': {
            'original_groups': analysis['mode_statistics']['original']['total_groups'],
            'chemical_groups': analysis['mode_statistics']['chemical']['total_groups'],
            'variant_groups': analysis['mode_statistics']['variant']['total_groups'],
            'reduction_original': round(
                (1 - analysis['mode_statistics']['original']['total_groups'] /
                 analysis['mode_statistics']['original']['total_recipes']) * 100, 1
            ) if analysis['mode_statistics']['original']['total_recipes'] > 0 else 0,
            'reduction_chemical': round(
                (1 - analysis['mode_statistics']['chemical']['total_groups'] /
                 analysis['mode_statistics']['chemical']['total_recipes']) * 100, 1
            ) if analysis['mode_statistics']['chemical']['total_recipes'] > 0 else 0,
            'reduction_variant': round(
                (1 - analysis['mode_statistics']['variant']['total_groups'] /
                 analysis['mode_statistics']['variant']['total_recipes']) * 100, 1
            ) if analysis['mode_statistics']['variant']['total_recipes'] > 0 else 0,
        }
    }

    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(report, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\nReport written to: {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Compare fingerprinting modes'
    )

    parser.add_argument(
        '--normalized-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Path to normalized_yaml directory'
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
        default=Path('reports/fingerprint_comparison.yaml'),
        help='Path to output report'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of recipes to process (for testing)'
    )

    args = parser.parse_args()

    # Validate paths
    if not args.normalized_dir.exists():
        print(f"Error: Normalized directory not found: {args.normalized_dir}", file=sys.stderr)
        return 1

    if not args.mim_repo.exists():
        print(f"Error: MediaIngredientMech repo not found: {args.mim_repo}", file=sys.stderr)
        return 1

    print("=" * 70)
    print("Fingerprint Mode Comparison")
    print("=" * 70)

    # Load hierarchy
    print(f"\nLoading MediaIngredientMech hierarchy from {args.mim_repo}...")
    hierarchy = MediaIngredientMechHierarchyImporter(args.mim_repo)
    hierarchy.load_hierarchy()

    stats = hierarchy.get_stats()
    print(f"  Loaded hierarchy: {stats['total_ingredients']} ingredients, "
          f"{stats['families']} families")

    # Find all recipes
    print(f"\nFinding recipes in {args.normalized_dir}...")
    recipe_paths = find_all_recipes(args.normalized_dir)
    print(f"  Found {len(recipe_paths)} recipes")

    # Generate fingerprints in all modes
    fingerprints = fingerprint_all_modes(recipe_paths, hierarchy, limit=args.limit)

    # Group by fingerprint
    groups = group_by_fingerprint(fingerprints)

    # Analyze differences
    analysis = analyze_differences(groups, fingerprints)

    # Find variant examples
    variant_examples = find_variant_pairs(groups, args.normalized_dir)

    # Generate report
    generate_report(analysis, variant_examples, args.output)

    # Print summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    stats = analysis['mode_statistics']
    print(f"Original mode:  {stats['original']['total_groups']:,} groups "
          f"({stats['original']['duplicate_groups']:,} duplicates)")
    print(f"Chemical mode:  {stats['chemical']['total_groups']:,} groups "
          f"({stats['chemical']['duplicate_groups']:,} duplicates)")
    print(f"Variant mode:   {stats['variant']['total_groups']:,} groups "
          f"({stats['variant']['duplicate_groups']:,} duplicates)")
    print()
    print(f"Variant pair groups found: {len(variant_examples)}")
    print()

    return 0


if __name__ == '__main__':
    sys.exit(main())
