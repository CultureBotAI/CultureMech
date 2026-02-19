#!/usr/bin/env python3
"""
Remove Invalid CHEBI IDs from Normalized YAML Files

Identifies and removes CHEBI IDs that are invalid or suspicious,
leaving the preferred_term intact but removing the term.id field.

Usage:
    uv run python scripts/remove_invalid_chebi_ids.py [--dry-run] [--verbose]
"""

import argparse
import yaml
from pathlib import Path
from datetime import datetime, timezone
from collections import defaultdict


def is_valid_chebi_id(chebi_id: str) -> tuple[bool, str]:
    """
    Check if CHEBI ID is valid.

    Returns:
        (is_valid, reason)
    """
    if not isinstance(chebi_id, str):
        return False, "not a string"

    if not chebi_id.startswith('CHEBI:'):
        return False, "missing CHEBI: prefix"

    try:
        num = int(chebi_id.split(':')[1])
    except (ValueError, IndexError):
        return False, "invalid numeric part"

    if num <= 0:
        return False, "negative or zero"

    # CHEBI IDs should be reasonable (< 10 million)
    # Valid range is typically 1-6 digits (1 to 999,999)
    # 7+ digits are suspicious
    if num > 9999999:
        return False, "8+ digits (clearly invalid)"

    if num > 999999:
        return False, "7 digits (suspicious)"

    return True, "valid"


def remove_invalid_chebi_from_recipe(recipe: dict) -> tuple[dict, list]:
    """
    Remove invalid CHEBI IDs from a recipe.

    Returns:
        (modified_recipe, list_of_removed_ids)
    """
    removed_ids = []

    # Process direct ingredients
    for ingredient in recipe.get('ingredients', []):
        term = ingredient.get('term', {})
        if term and term.get('id'):
            chebi_id = term['id']
            is_valid, reason = is_valid_chebi_id(chebi_id)

            if not is_valid:
                removed_ids.append({
                    'chebi_id': chebi_id,
                    'ingredient': ingredient.get('preferred_term', 'unknown'),
                    'reason': reason,
                    'location': 'ingredients'
                })
                # Remove the entire term field
                del ingredient['term']

    # Process solutions
    for solution in recipe.get('solutions', []):
        for ingredient in solution.get('composition', []):
            term = ingredient.get('term', {})
            if term and term.get('id'):
                chebi_id = term['id']
                is_valid, reason = is_valid_chebi_id(chebi_id)

                if not is_valid:
                    removed_ids.append({
                        'chebi_id': chebi_id,
                        'ingredient': ingredient.get('preferred_term', 'unknown'),
                        'reason': reason,
                        'location': f"solutions/{solution.get('preferred_term', 'unknown')}"
                    })
                    # Remove the entire term field
                    del ingredient['term']

    return recipe, removed_ids


def add_curation_event(recipe: dict, removed_count: int):
    """Add curation event documenting the removal of invalid CHEBI IDs."""
    if 'curation_history' not in recipe:
        recipe['curation_history'] = []

    recipe['curation_history'].append({
        'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
        'curator': 'invalid-chebi-removal',
        'action': f'Removed {removed_count} invalid CHEBI ID(s)',
        'notes': 'Removed CHEBI IDs with invalid format (7+ digits) from MicrobeMediaParam source data'
    })


def process_yaml_file(
    yaml_file: Path,
    dry_run: bool = False,
    verbose: bool = False
) -> dict:
    """
    Process a single YAML file to remove invalid CHEBI IDs.

    Returns:
        Statistics dict
    """
    try:
        with open(yaml_file) as f:
            recipe = yaml.safe_load(f)

        if not recipe:
            return {'error': 'empty file'}

        # Remove invalid CHEBI IDs
        modified_recipe, removed_ids = remove_invalid_chebi_from_recipe(recipe)

        if removed_ids:
            if verbose:
                print(f"\n📝 {yaml_file.name}")
                for item in removed_ids:
                    print(f"   Removing {item['chebi_id']} from '{item['ingredient']}' - {item['reason']}")

            # Add curation event
            add_curation_event(modified_recipe, len(removed_ids))

            # Write back to file
            if not dry_run:
                with open(yaml_file, 'w') as f:
                    yaml.dump(modified_recipe, f, default_flow_style=False,
                             sort_keys=False, allow_unicode=True)

            return {
                'modified': True,
                'removed_count': len(removed_ids),
                'removed_ids': removed_ids
            }

        return {'modified': False}

    except Exception as e:
        print(f"❌ Error processing {yaml_file}: {e}")
        return {'error': str(e)}


def main():
    parser = argparse.ArgumentParser(
        description="Remove invalid CHEBI IDs from normalized YAML files"
    )
    parser.add_argument(
        '--normalized-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help="Path to normalized_yaml directory"
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help="Show what would be removed without modifying files"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Show detailed information about each removal"
    )

    args = parser.parse_args()

    if not args.normalized_dir.exists():
        print(f"❌ Error: {args.normalized_dir} not found")
        return 1

    print("=" * 70)
    print("Invalid CHEBI ID Removal")
    print("=" * 70)
    print(f"Directory: {args.normalized_dir}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'LIVE (will modify files)'}")
    print()

    # Statistics
    stats = {
        'total_files': 0,
        'modified_files': 0,
        'total_removed': 0,
        'by_reason': defaultdict(int),
        'by_chebi_id': defaultdict(int),
        'errors': 0
    }

    # Track all unique invalid IDs
    all_invalid_ids = defaultdict(lambda: {
        'count': 0,
        'ingredients': set(),
        'files': set(),
        'reason': None
    })

    # Process all YAML files
    yaml_files = list(args.normalized_dir.rglob('*.yaml'))
    stats['total_files'] = len(yaml_files)

    print(f"Processing {len(yaml_files)} YAML files...")
    if args.dry_run:
        print("⚠️  DRY RUN MODE - No files will be modified\n")

    for yaml_file in yaml_files:
        result = process_yaml_file(yaml_file, args.dry_run, args.verbose)

        if 'error' in result:
            stats['errors'] += 1
            continue

        if result.get('modified'):
            stats['modified_files'] += 1
            stats['total_removed'] += result['removed_count']

            # Track individual removals
            for item in result['removed_ids']:
                chebi_id = item['chebi_id']
                reason = item['reason']
                ingredient = item['ingredient']

                stats['by_reason'][reason] += 1
                stats['by_chebi_id'][chebi_id] += 1

                all_invalid_ids[chebi_id]['count'] += 1
                all_invalid_ids[chebi_id]['ingredients'].add(ingredient)
                all_invalid_ids[chebi_id]['files'].add(yaml_file.name)
                all_invalid_ids[chebi_id]['reason'] = reason

    # Print summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total files processed: {stats['total_files']}")
    print(f"Files modified: {stats['modified_files']}")
    print(f"Total invalid IDs removed: {stats['total_removed']}")
    print(f"Errors: {stats['errors']}")

    if stats['total_removed'] > 0:
        print("\n📊 Removals by reason:")
        for reason, count in sorted(stats['by_reason'].items(), key=lambda x: -x[1]):
            print(f"  {reason:30s}: {count:4d}")

        print("\n🔢 Most common invalid CHEBI IDs removed:")
        sorted_ids = sorted(stats['by_chebi_id'].items(), key=lambda x: -x[1])
        for chebi_id, count in sorted_ids[:10]:
            print(f"  {chebi_id}: {count} occurrences")

        print("\n📋 Detailed breakdown of top invalid IDs:")
        for chebi_id, count in sorted_ids[:5]:
            info = all_invalid_ids[chebi_id]
            print(f"\n  {chebi_id} ({info['reason']})")
            print(f"    Occurrences: {info['count']}")
            print(f"    Files: {len(info['files'])}")
            print(f"    Ingredients: {', '.join(list(info['ingredients'])[:5])}")
            if len(info['ingredients']) > 5:
                print(f"      ... and {len(info['ingredients']) - 5} more")

    print("\n" + "=" * 70)

    if args.dry_run:
        print("\n⚠️  This was a DRY RUN. No files were modified.")
        print("To apply changes, run without --dry-run")
    else:
        print(f"\n✅ Successfully removed {stats['total_removed']} invalid CHEBI IDs")
        print(f"   from {stats['modified_files']} files")

        # Suggest next steps
        if stats['total_removed'] > 0:
            print("\n📌 Next steps:")
            print("  1. Review changes: git diff data/normalized_yaml/")
            print("  2. Verify results: uv run python scripts/check_chebi_ids.py")
            print("  3. Regenerate SSSOM: just sssom-pipeline")

    return 0


if __name__ == "__main__":
    exit(main())
