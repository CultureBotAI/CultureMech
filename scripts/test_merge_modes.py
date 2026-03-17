#!/usr/bin/env python3
"""Test different merge modes and compare results.

Runs merge pipeline with different modes (conservative, aggressive, variant-aware)
and generates comparison reports.

Usage:
    python scripts/test_merge_modes.py --modes conservative,aggressive,variant-aware
    python scripts/test_merge_modes.py --modes all
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path
from typing import Dict, List

import yaml

from culturemech.enrich.hierarchy_importer import MediaIngredientMechHierarchyImporter
from culturemech.merge.fingerprint import RecipeFingerprinter
from culturemech.merge.hierarchy_fingerprint import HierarchyAwareFingerprinter
from culturemech.merge.merge_rules import MergeRuleEngine


def find_all_recipes(normalized_dir: Path) -> List[Path]:
    """Find all recipe YAML files."""
    recipes = []
    for category_dir in normalized_dir.iterdir():
        if category_dir.is_dir():
            recipes.extend(category_dir.glob('*.yaml'))
    return sorted(recipes)


def load_recipe(path: Path) -> Dict:
    """Load recipe from YAML file."""
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        return yaml.safe_load(f)


def test_mode(
    mode: str,
    recipe_paths: List[Path],
    hierarchy: MediaIngredientMechHierarchyImporter,
    fingerprint_mode: str = 'chemical',
    limit: int = None
) -> Dict:
    """Test a specific merge mode.

    Args:
        mode: Merge mode to test
        recipe_paths: List of recipe file paths
        hierarchy: Hierarchy importer
        fingerprint_mode: Fingerprinting mode
        limit: Optional limit on recipes

    Returns:
        Results dictionary with statistics
    """
    print(f"\nTesting mode: {mode} (fingerprint: {fingerprint_mode})")

    if limit:
        recipe_paths = recipe_paths[:limit]

    # Initialize components
    fingerprinter = HierarchyAwareFingerprinter(hierarchy, mode=fingerprint_mode)
    rule_engine = MergeRuleEngine(hierarchy, mode=mode)

    # Group recipes by fingerprint
    groups = defaultdict(list)
    skipped = 0

    for i, path in enumerate(recipe_paths, 1):
        try:
            recipe = load_recipe(path)
            fp = fingerprinter.fingerprint(recipe)

            if fp:
                groups[fp].append(path)
            else:
                skipped += 1

            if i % 1000 == 0:
                print(f"  Progress: {i}/{len(recipe_paths)}")

        except Exception as e:
            skipped += 1

    print(f"  Processed: {len(recipe_paths)} recipes")
    print(f"  Skipped: {skipped} recipes")
    print(f"  Groups: {len(groups)}")

    # Analyze groups
    group_sizes = [len(paths) for paths in groups.values()]
    duplicate_groups = [size for size in group_sizes if size >= 2]

    # Apply merge rules to check confidence
    high_confidence = 0
    medium_confidence = 0
    low_confidence = 0

    for fp, paths in groups.items():
        if len(paths) < 2:
            continue

        # Load first two recipes to test rule engine
        try:
            recipe1 = load_recipe(paths[0])
            recipe2 = load_recipe(paths[1])

            should_merge, reason, confidence = rule_engine.should_merge(
                recipe1, recipe2, fingerprint_match=True
            )

            if confidence >= 0.9:
                high_confidence += 1
            elif confidence >= 0.7:
                medium_confidence += 1
            else:
                low_confidence += 1

        except Exception:
            pass

    results = {
        'mode': mode,
        'fingerprint_mode': fingerprint_mode,
        'total_recipes': len(recipe_paths),
        'total_groups': len(groups),
        'skipped_recipes': skipped,
        'singleton_groups': sum(1 for size in group_sizes if size == 1),
        'duplicate_groups': len(duplicate_groups),
        'largest_group': max(group_sizes, default=0),
        'reduction': len(recipe_paths) - len(groups),
        'reduction_percentage': round(
            (1 - len(groups) / len(recipe_paths)) * 100, 1
        ) if len(recipe_paths) > 0 else 0,
        'confidence_distribution': {
            'high': high_confidence,
            'medium': medium_confidence,
            'low': low_confidence,
        }
    }

    return results


def compare_modes(results_by_mode: Dict[str, Dict]) -> Dict:
    """Compare results across modes.

    Args:
        results_by_mode: Dictionary mapping mode -> results

    Returns:
        Comparison dictionary
    """
    comparison = {
        'modes': list(results_by_mode.keys()),
        'summary': {},
        'differences': {}
    }

    # Summary statistics
    for mode, results in results_by_mode.items():
        comparison['summary'][mode] = {
            'groups': results['total_groups'],
            'reduction': results['reduction'],
            'reduction_pct': results['reduction_percentage'],
            'largest_group': results['largest_group'],
        }

    # Find differences
    modes = list(results_by_mode.keys())
    if len(modes) >= 2:
        for i in range(len(modes)):
            for j in range(i + 1, len(modes)):
                mode1, mode2 = modes[i], modes[j]
                r1, r2 = results_by_mode[mode1], results_by_mode[mode2]

                diff_key = f"{mode1}_vs_{mode2}"
                comparison['differences'][diff_key] = {
                    'group_count_diff': r1['total_groups'] - r2['total_groups'],
                    'reduction_diff_pct': round(
                        r1['reduction_percentage'] - r2['reduction_percentage'], 1
                    ),
                }

    return comparison


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Test and compare merge modes'
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
        '--modes',
        type=str,
        default='all',
        help='Comma-separated list of modes to test (or "all")'
    )

    parser.add_argument(
        '--fingerprint-mode',
        type=str,
        default='chemical',
        choices=['chemical', 'variant', 'original'],
        help='Fingerprinting mode to use'
    )

    parser.add_argument(
        '--output',
        type=Path,
        default=Path('reports/mode_comparison.yaml'),
        help='Output report path'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of recipes (for testing)'
    )

    args = parser.parse_args()

    # Parse modes
    if args.modes.lower() == 'all':
        modes = ['conservative', 'aggressive', 'variant-aware']
    else:
        modes = [m.strip() for m in args.modes.split(',')]

    # Validate paths
    if not args.normalized_dir.exists():
        print(f"Error: {args.normalized_dir} not found", file=sys.stderr)
        return 1

    if not args.mim_repo.exists():
        print(f"Error: {args.mim_repo} not found", file=sys.stderr)
        return 1

    print("=" * 70)
    print("Merge Mode Comparison")
    print("=" * 70)

    # Load hierarchy
    print(f"\nLoading hierarchy from {args.mim_repo}...")
    hierarchy = MediaIngredientMechHierarchyImporter(args.mim_repo)
    hierarchy.load_hierarchy()

    stats = hierarchy.get_stats()
    print(f"  Loaded: {stats['total_ingredients']} ingredients, "
          f"{stats['families']} families")

    # Find recipes
    print(f"\nFinding recipes in {args.normalized_dir}...")
    recipe_paths = find_all_recipes(args.normalized_dir)
    print(f"  Found {len(recipe_paths)} recipes")

    # Test each mode
    results_by_mode = {}

    for mode in modes:
        results = test_mode(
            mode,
            recipe_paths,
            hierarchy,
            fingerprint_mode=args.fingerprint_mode,
            limit=args.limit
        )
        results_by_mode[mode] = results

    # Compare results
    comparison = compare_modes(results_by_mode)

    # Generate report
    report = {
        'test_configuration': {
            'fingerprint_mode': args.fingerprint_mode,
            'modes_tested': modes,
            'total_recipes': len(recipe_paths),
        },
        'results_by_mode': results_by_mode,
        'comparison': comparison,
    }

    # Write report
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, 'w', encoding='utf-8') as f:
        yaml.dump(report, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\n\nReport written to: {args.output}")

    # Print summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)

    for mode, results in results_by_mode.items():
        print(f"\n{mode.upper()}:")
        print(f"  Groups: {results['total_groups']:,}")
        print(f"  Reduction: {results['reduction']:,} recipes ({results['reduction_percentage']}%)")
        print(f"  Largest group: {results['largest_group']}")
        conf = results['confidence_distribution']
        print(f"  Confidence: High={conf['high']}, Med={conf['medium']}, Low={conf['low']}")

    print()
    return 0


if __name__ == '__main__':
    sys.exit(main())
