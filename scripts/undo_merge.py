#!/usr/bin/env python3
"""Undo problematic merges and restore original recipes.

Provides capability to:
1. Undo specific merge by recipe ID
2. Undo all merges matching filter criteria (e.g., variant_contamination)
3. Dry-run mode to preview changes

Restores original recipes from normalized_yaml directory.
"""

import argparse
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional

import yaml


def find_all_recipes(directory: Path) -> List[Path]:
    """Find all recipe YAML files."""
    return sorted(directory.rglob('*.yaml'))


def load_recipe(path: Path) -> Dict:
    """Load recipe from YAML file."""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def find_recipe_by_id(merge_dir: Path, recipe_id: str) -> Optional[Path]:
    """Find merged recipe file by ID.

    Args:
        merge_dir: Path to merged recipes directory
        recipe_id: Recipe ID to find

    Returns:
        Path to recipe file or None
    """
    # Try exact match first
    for path in find_all_recipes(merge_dir):
        recipe = load_recipe(path)
        if recipe_id in recipe.get('merged_from', []):
            return path

    # Try fuzzy match by filename
    for path in find_all_recipes(merge_dir):
        if recipe_id.lower() in path.stem.lower():
            return path

    return None


def get_original_recipes(
    merged_recipe: Dict,
    normalized_dir: Path
) -> List[Path]:
    """Get paths to original recipes that were merged.

    Args:
        merged_recipe: Merged recipe dictionary
        normalized_dir: Path to normalized recipes directory

    Returns:
        List of paths to original recipe files
    """
    merged_from = merged_recipe.get('merged_from', [])

    original_paths = []

    for recipe_id in merged_from:
        # Search in all category directories
        found = False

        for category_dir in normalized_dir.iterdir():
            if not category_dir.is_dir():
                continue

            recipe_path = category_dir / f"{recipe_id}.yaml"
            if recipe_path.exists():
                original_paths.append(recipe_path)
                found = True
                break

        if not found:
            print(f"  Warning: Original recipe not found: {recipe_id}", file=sys.stderr)

    return original_paths


def undo_merge(
    merged_path: Path,
    normalized_dir: Path,
    output_dir: Path,
    dry_run: bool = False,
    log_events: bool = True
) -> Dict:
    """Undo a merge and restore original recipes.

    Args:
        merged_path: Path to merged recipe file
        normalized_dir: Path to normalized recipes directory
        output_dir: Output directory for restored recipes
        dry_run: If True, don't actually perform changes
        log_events: If True, log undo events

    Returns:
        Result dictionary with statistics
    """
    # Load merged recipe
    merged_recipe = load_recipe(merged_path)
    merged_from = merged_recipe.get('merged_from', [])

    print(f"\nUndoing merge: {merged_path.name}")
    print(f"  Canonical name: {merged_recipe.get('name')}")
    print(f"  Merged from {len(merged_from)} recipes")

    # Find original recipes
    original_paths = get_original_recipes(merged_recipe, normalized_dir)

    if not original_paths:
        print(f"  Error: No original recipes found")
        return {
            'success': False,
            'reason': 'no_originals_found',
        }

    print(f"  Found {len(original_paths)} original recipes")

    if dry_run:
        print("  [DRY RUN] Would restore:")
        for path in original_paths:
            print(f"    - {path.name}")
        print(f"  [DRY RUN] Would remove: {merged_path.name}")

        return {
            'success': True,
            'dry_run': True,
            'restored_count': len(original_paths),
        }

    # Restore original recipes
    output_dir.mkdir(parents=True, exist_ok=True)

    restored = []
    for original_path in original_paths:
        dest_path = output_dir / original_path.name

        try:
            shutil.copy2(original_path, dest_path)
            restored.append(dest_path)
            print(f"  Restored: {dest_path.name}")
        except Exception as e:
            print(f"  Error copying {original_path.name}: {e}", file=sys.stderr)

    # Remove merged recipe
    try:
        merged_path.unlink()
        print(f"  Removed: {merged_path.name}")
    except Exception as e:
        print(f"  Error removing {merged_path.name}: {e}", file=sys.stderr)

    # Log event
    if log_events:
        log_undo_event(merged_path, original_paths, output_dir)

    return {
        'success': True,
        'restored_count': len(restored),
        'removed_merge': merged_path.name,
    }


def log_undo_event(
    merged_path: Path,
    original_paths: List[Path],
    output_dir: Path
) -> None:
    """Log undo event for audit trail.

    Args:
        merged_path: Path to merged recipe that was removed
        original_paths: Paths to original recipes that were restored
        output_dir: Output directory
    """
    log_file = output_dir.parent / 'undo_log.yaml'

    event = {
        'merged_recipe': merged_path.name,
        'original_recipes': [p.name for p in original_paths],
        'timestamp': Path.ctime(merged_path) if merged_path.exists() else None,
    }

    # Append to log
    events = []
    if log_file.exists():
        with open(log_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
            events = data.get('undo_events', []) if data else []

    events.append(event)

    with open(log_file, 'w', encoding='utf-8') as f:
        yaml.dump({'undo_events': events}, f, default_flow_style=False, allow_unicode=True)


def undo_by_filter(
    merge_dir: Path,
    normalized_dir: Path,
    output_dir: Path,
    quality_report_path: Path,
    filter_type: str,
    dry_run: bool = False
) -> Dict:
    """Undo all merges matching filter criteria.

    Args:
        merge_dir: Path to merged recipes directory
        normalized_dir: Path to normalized recipes directory
        output_dir: Output directory for restored recipes
        quality_report_path: Path to quality report YAML
        filter_type: Issue type to filter by (e.g., 'variant_contamination')
        dry_run: If True, don't actually perform changes

    Returns:
        Result dictionary with statistics
    """
    # Load quality report
    if not quality_report_path.exists():
        print(f"Error: Quality report not found: {quality_report_path}", file=sys.stderr)
        return {'success': False, 'reason': 'no_quality_report'}

    with open(quality_report_path, 'r', encoding='utf-8') as f:
        report = yaml.safe_load(f)

    # Get issues of specified type
    issues = report.get('issues', {}).get(filter_type, [])

    if not issues:
        print(f"No issues found of type: {filter_type}")
        return {'success': True, 'undone_count': 0}

    print(f"\nFound {len(issues)} issues of type '{filter_type}'")

    # Undo each merge
    undone_count = 0

    for issue in issues:
        recipe_file = issue.get('recipe_file')
        if not recipe_file:
            continue

        merged_path = merge_dir / recipe_file

        if not merged_path.exists():
            print(f"  Warning: File not found: {recipe_file}", file=sys.stderr)
            continue

        result = undo_merge(
            merged_path,
            normalized_dir,
            output_dir,
            dry_run=dry_run,
            log_events=True
        )

        if result.get('success'):
            undone_count += 1

    return {
        'success': True,
        'undone_count': undone_count,
        'filter_type': filter_type,
    }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Undo problematic merges and restore original recipes'
    )

    parser.add_argument(
        '--merged-dir',
        type=Path,
        required=True,
        help='Path to merged recipes directory'
    )

    parser.add_argument(
        '--normalized-dir',
        type=Path,
        required=True,
        help='Path to normalized recipes directory'
    )

    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('data/merge_yaml/restored'),
        help='Output directory for restored recipes'
    )

    parser.add_argument(
        '--recipe-id',
        type=str,
        help='Specific recipe ID to undo'
    )

    parser.add_argument(
        '--filter',
        type=str,
        choices=['variant_contamination', 'parent_mismatch', 'concentration_outlier'],
        help='Undo all merges with this issue type'
    )

    parser.add_argument(
        '--quality-report',
        type=Path,
        default=Path('reports/merge_quality.yaml'),
        help='Path to quality report (required with --filter)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without actually performing them'
    )

    args = parser.parse_args()

    # Validate arguments
    if not args.recipe_id and not args.filter:
        print("Error: Must specify either --recipe-id or --filter", file=sys.stderr)
        return 1

    if args.filter and not args.quality_report.exists():
        print(f"Error: Quality report required with --filter: {args.quality_report}", file=sys.stderr)
        return 1

    print("=" * 70)
    print("Undo Merge Tool")
    print("=" * 70)

    if args.dry_run:
        print("\n*** DRY RUN MODE - No changes will be made ***\n")

    # Undo specific recipe
    if args.recipe_id:
        merged_path = find_recipe_by_id(args.merged_dir, args.recipe_id)

        if not merged_path:
            print(f"Error: Recipe not found: {args.recipe_id}", file=sys.stderr)
            return 1

        result = undo_merge(
            merged_path,
            args.normalized_dir,
            args.output_dir,
            dry_run=args.dry_run
        )

        if result.get('success'):
            print(f"\nSuccess: Restored {result.get('restored_count', 0)} recipes")
            return 0
        else:
            print(f"\nFailed: {result.get('reason', 'unknown')}")
            return 1

    # Undo by filter
    if args.filter:
        result = undo_by_filter(
            args.merged_dir,
            args.normalized_dir,
            args.output_dir,
            args.quality_report,
            args.filter,
            dry_run=args.dry_run
        )

        if result.get('success'):
            print(f"\nSuccess: Undone {result.get('undone_count', 0)} merges")
            return 0
        else:
            print(f"\nFailed: {result.get('reason', 'unknown')}")
            return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
