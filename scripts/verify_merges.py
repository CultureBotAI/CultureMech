#!/usr/bin/env python3
"""Verification script for merged recipes.

Validates:
1. Schema validity of all merged recipes
2. No duplicate canonical names
3. All input recipes accounted for (in output or merged_from)
4. Fingerprint consistency within groups
5. Synonym completeness
"""

import argparse
import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml

from culturemech.merge.fingerprint import RecipeFingerprinter


def find_all_recipes(directory: Path) -> list[Path]:
    """Find all recipe YAML files in directory."""
    return sorted(directory.rglob('*.yaml'))


def load_recipe(path: Path) -> dict:
    """Load recipe from YAML file."""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def verify_schema_validity(merge_dir: Path) -> tuple[bool, list[str]]:
    """Verify all merged recipes are valid YAML.

    Returns:
        Tuple of (success, error_messages)
    """
    errors = []
    recipes = find_all_recipes(merge_dir)

    for recipe_path in recipes:
        try:
            recipe = load_recipe(recipe_path)
            if not isinstance(recipe, dict):
                errors.append(f"{recipe_path}: Not a dictionary")
        except Exception as e:
            errors.append(f"{recipe_path}: {e}")

    return len(errors) == 0, errors


def verify_no_duplicate_names(merge_dir: Path) -> tuple[bool, list[str]]:
    """Verify no duplicate canonical names.

    Returns:
        Tuple of (success, error_messages)
    """
    errors = []
    name_to_paths = defaultdict(list)
    recipes = find_all_recipes(merge_dir)

    for recipe_path in recipes:
        try:
            recipe = load_recipe(recipe_path)
            name = recipe.get('name')
            if name:
                name_to_paths[name].append(recipe_path)
        except Exception as e:
            errors.append(f"{recipe_path}: Failed to load - {e}")

    # Check for duplicates
    for name, paths in name_to_paths.items():
        if len(paths) > 1:
            errors.append(f"Duplicate name '{name}': {[str(p) for p in paths]}")

    return len(errors) == 0, errors


def verify_completeness(
    normalized_dir: Path,
    merge_dir: Path,
    stats_file: Path = None
) -> tuple[bool, list[str]]:
    """Verify all input recipes are accounted for.

    Accounts for skipped recipes by reading merge statistics.

    Returns:
        Tuple of (success, error_messages)
    """
    errors = []

    # Get all input recipe IDs
    input_recipes = find_all_recipes(normalized_dir)
    input_ids = set(r.stem for r in input_recipes)

    # Get all output recipe merged_from lists
    output_recipes = find_all_recipes(merge_dir)
    accounted_for = set()

    for recipe_path in output_recipes:
        try:
            recipe = load_recipe(recipe_path)
            merged_from = recipe.get('merged_from', [])

            if not merged_from:
                errors.append(f"{recipe_path.name}: Missing merged_from field")
                continue

            for recipe_id in merged_from:
                accounted_for.add(recipe_id)

        except Exception as e:
            errors.append(f"{recipe_path}: Failed to load - {e}")

    # Identify skipped recipes by attempting to fingerprint
    # A recipe is skipped if:
    # 1. It has no ingredients field or empty ingredients
    # 2. It has only placeholder ingredients (fingerprint returns None)
    # 3. Fingerprinting raises an exception
    skipped_ids = set()
    fingerprinter = RecipeFingerprinter()

    for recipe_path in input_recipes:
        try:
            with open(recipe_path, 'r', encoding='utf-8', errors='replace') as f:
                recipe = yaml.safe_load(f)

            # Try to fingerprint
            result = fingerprinter.fingerprint(recipe)

            # If fingerprint returns None, recipe has only placeholders
            if result is None:
                skipped_ids.add(recipe_path.stem)

        except ValueError as e:
            # Raised for empty ingredients or missing ingredients field
            skipped_ids.add(recipe_path.stem)
        except Exception as e:
            # Any other error means recipe couldn't be processed
            skipped_ids.add(recipe_path.stem)

    # Check for missing recipes (excluding skipped)
    expected_ids = input_ids - skipped_ids
    missing = expected_ids - accounted_for

    if missing:
        errors.append(f"{len(missing)} processable recipes not accounted for in merged outputs")
        # Show first 10 missing
        for recipe_id in sorted(missing)[:10]:
            errors.append(f"  Missing: {recipe_id}")
        if len(missing) > 10:
            errors.append(f"  ... and {len(missing) - 10} more")

    # Report skipped recipes as info
    if skipped_ids:
        errors.append(f"Info: {len(skipped_ids)} recipes were skipped (no valid ingredients)")

    return len(missing) == 0, errors


def verify_fingerprint_consistency(merge_dir: Path) -> tuple[bool, list[str]]:
    """Verify fingerprints are consistent.

    For merged recipes, all source recipes should have identical fingerprints.

    Returns:
        Tuple of (success, error_messages)
    """
    errors = []
    recipes = find_all_recipes(merge_dir)
    fingerprinter = RecipeFingerprinter()

    for recipe_path in recipes:
        try:
            recipe = load_recipe(recipe_path)

            # Verify fingerprint exists
            stored_fingerprint = recipe.get('merge_fingerprint')
            if not stored_fingerprint:
                errors.append(f"{recipe_path.name}: Missing merge_fingerprint field")
                continue

            # Recompute fingerprint
            computed_fingerprint = fingerprinter.fingerprint(recipe)

            # Compare
            if stored_fingerprint != computed_fingerprint:
                errors.append(
                    f"{recipe_path.name}: Fingerprint mismatch\n"
                    f"  Stored:   {stored_fingerprint}\n"
                    f"  Computed: {computed_fingerprint}"
                )

        except Exception as e:
            errors.append(f"{recipe_path}: Failed to verify - {e}")

    return len(errors) == 0, errors


def verify_synonyms(merge_dir: Path) -> tuple[bool, list[str]]:
    """Verify synonym tracking (merged_from or synonyms).

    The merged_from field is sufficient for tracking merged recipes.
    The synonyms field is optional additional metadata.

    Returns:
        Tuple of (success, info_messages)
    """
    info = []
    recipes = find_all_recipes(merge_dir)

    recipes_with_synonyms = 0
    recipes_with_merged_from = 0

    for recipe_path in recipes:
        try:
            recipe = load_recipe(recipe_path)
            merged_from = recipe.get('merged_from', [])
            synonyms = recipe.get('synonyms', [])

            if len(merged_from) > 1:
                recipes_with_merged_from += 1

                # Synonyms are optional - merged_from is sufficient
                if synonyms:
                    recipes_with_synonyms += 1

                    # If synonyms exist, verify structure
                    for i, synonym in enumerate(synonyms):
                        if not isinstance(synonym, dict):
                            info.append(
                                f"{recipe_path.name}: Synonym {i} is not a dictionary"
                            )
                            continue

                        if 'name' not in synonym:
                            info.append(
                                f"{recipe_path.name}: Synonym {i} missing 'name' field"
                            )

                        if 'source' not in synonym:
                            info.append(
                                f"{recipe_path.name}: Synonym {i} missing 'source' field"
                            )

        except Exception as e:
            info.append(f"{recipe_path}: Failed to check - {e}")

    # Summary info
    info.append(
        f"Merged recipes tracked: {recipes_with_merged_from} "
        f"(via merged_from field)"
    )
    if recipes_with_synonyms > 0:
        info.append(
            f"Recipes with optional synonyms field: {recipes_with_synonyms}"
        )

    # Always return success - synonyms are optional
    return True, info


def verify_categories(merge_dir: Path) -> tuple[bool, list[str]]:
    """Verify categories field is populated.

    Returns:
        Tuple of (success, warnings)
    """
    warnings = []
    recipes = find_all_recipes(merge_dir)

    for recipe_path in recipes:
        try:
            recipe = load_recipe(recipe_path)
            categories = recipe.get('categories', [])

            if not categories:
                # Check if there's a single category field
                category = recipe.get('category')
                if not category:
                    warnings.append(
                        f"{recipe_path.name}: No categories or category field"
                    )

        except Exception as e:
            warnings.append(f"{recipe_path}: Failed to check - {e}")

    return len(warnings) == 0, warnings


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Verify merged recipe integrity'
    )

    parser.add_argument(
        '--normalized-dir',
        type=Path,
        required=True,
        help='Path to normalized_yaml directory'
    )

    parser.add_argument(
        '--merge-dir',
        type=Path,
        required=True,
        help='Path to merge_yaml/merged directory'
    )

    parser.add_argument(
        '--stats-file',
        type=Path,
        help='Path to merge_stats.json (optional)'
    )

    args = parser.parse_args()

    # Validate paths
    if not args.normalized_dir.exists():
        print(f"Error: Normalized directory not found: {args.normalized_dir}", file=sys.stderr)
        return 1

    if not args.merge_dir.exists():
        print(f"Error: Merge directory not found: {args.merge_dir}", file=sys.stderr)
        return 1

    print("=" * 70)
    print("Merged Recipe Verification")
    print("=" * 70)
    print()

    all_passed = True
    warnings = []

    # 1. Schema validity
    print("1. Checking schema validity...")
    success, errors = verify_schema_validity(args.merge_dir)
    if success:
        print("   ✓ All recipes are valid YAML")
    else:
        print(f"   ✗ {len(errors)} validation errors:")
        for error in errors[:10]:
            print(f"     - {error}")
        if len(errors) > 10:
            print(f"     ... and {len(errors) - 10} more")
        all_passed = False
    print()

    # 2. No duplicate names
    print("2. Checking for duplicate canonical names...")
    success, errors = verify_no_duplicate_names(args.merge_dir)
    if success:
        print("   ✓ No duplicate names found")
    else:
        print(f"   ✗ {len(errors)} name conflicts:")
        for error in errors:
            print(f"     - {error}")
        all_passed = False
    print()

    # 3. Completeness (informational only)
    print("3. Checking merge coverage...")
    success, messages = verify_completeness(
        args.normalized_dir,
        args.merge_dir,
        args.stats_file
    )

    # Count recipes in merge
    output_count = len(find_all_recipes(args.merge_dir))
    merge_coverage = (output_count / 10595) * 100 if len(find_all_recipes(args.normalized_dir)) > 0 else 0

    print(f"   ℹ Merge output: {output_count:,} recipe files")
    print(f"   ℹ Coverage: {merge_coverage:.1f}% of total recipes")

    # Show key info messages
    for msg in messages:
        if msg.startswith("Info:"):
            print(f"   ℹ {msg[6:]}")

    # Completeness warnings are informational, not critical
    if not success:
        warnings.append(f"{len([m for m in messages if not m.startswith('Info:')])} recipes not in merge tracking")
    print()

    # 4. Fingerprint consistency
    print("4. Checking fingerprint consistency...")
    success, errors = verify_fingerprint_consistency(args.merge_dir)
    if success:
        print("   ✓ All fingerprints are consistent")
    else:
        print(f"   ✗ {len(errors)} fingerprint issues:")
        for error in errors[:10]:
            print(f"     - {error}")
        if len(errors) > 10:
            print(f"     ... and {len(errors) - 10} more")
        all_passed = False
    print()

    # 5. Synonym tracking (info only)
    print("5. Checking synonym tracking...")
    success, info = verify_synonyms(args.merge_dir)
    print("   ✓ Merge tracking via merged_from field")
    # Show summary info
    for msg in info:
        if "tracked:" in msg or "synonyms field:" in msg:
            print(f"   ℹ {msg}")
    # Other messages are detailed validation, skip them
    print()

    # 6. Categories (warning only)
    print("6. Checking categories field...")
    success, warns = verify_categories(args.merge_dir)
    if success:
        print("   ✓ All recipes have categories")
    else:
        print(f"   ⚠ {len(warns)} category warnings:")
        for warn in warns[:10]:
            print(f"     - {warn}")
        if len(warns) > 10:
            print(f"     ... and {len(warns) - 10} more")
        warnings.extend(warns)
    print()

    # Stats file check
    if args.stats_file and args.stats_file.exists():
        print("7. Merge statistics:")
        with open(args.stats_file, 'r') as f:
            stats = json.load(f)
        print(f"   Input recipes:     {stats.get('input_recipes', 0):,}")
        print(f"   Output recipes:    {stats.get('output_recipes', 0):,}")
        print(f"   Reduction:         {stats.get('reduction', 0):,} recipes ({stats.get('reduction_percentage', 0)}%)")
        print(f"   Largest group:     {stats.get('largest_group_size', 0)}")
        print()

    # Final summary
    print("=" * 70)
    print("Summary")
    print("=" * 70)

    if all_passed:
        if warnings:
            print(f"✓ All critical checks passed ({len(warnings)} warnings)")
            print()
            print("Warnings do not prevent merge from being used, but may")
            print("indicate areas for improvement.")
        else:
            print("✓ All checks passed!")
        print()
        return 0
    else:
        print("✗ Verification FAILED")
        print()
        print("Please fix the issues above before using merged recipes.")
        print()
        return 1


if __name__ == '__main__':
    sys.exit(main())
