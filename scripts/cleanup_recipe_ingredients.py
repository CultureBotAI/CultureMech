#!/usr/bin/env python3
"""Clean up data quality issues within individual recipes.

Fixes:
1. Duplicate ingredient entries (e.g., water appearing multiple times)
2. Missing pH buffers mentioned in notes
3. Inconsistent concentration formats
4. Other within-recipe data quality issues

This runs BEFORE merging to ensure clean input data.
"""

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml


def find_all_recipes(directory: Path) -> List[Path]:
    """Find all recipe YAML files."""
    recipes = []
    for category_dir in directory.iterdir():
        if category_dir.is_dir():
            recipes.extend(category_dir.glob('*.yaml'))
    return sorted(recipes)


def load_recipe(path: Path) -> Dict:
    """Load recipe from YAML file."""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def save_recipe(recipe: Dict, path: Path) -> None:
    """Save recipe to YAML file."""
    with open(path, 'w', encoding='utf-8') as f:
        yaml.dump(recipe, f, default_flow_style=False, allow_unicode=True, sort_keys=False)


def merge_duplicate_ingredients(recipe: Dict) -> Tuple[Dict, List[str]]:
    """Merge duplicate ingredient entries within a recipe.

    Args:
        recipe: Recipe dictionary

    Returns:
        Tuple of (modified_recipe, list_of_changes)
    """
    changes = []

    if 'ingredients' not in recipe:
        return recipe, changes

    # Group ingredients by normalized name
    ingredient_groups = defaultdict(list)

    for ingredient in recipe['ingredients']:
        name = ingredient.get('preferred_term', '').strip().lower()
        if name:
            ingredient_groups[name].append(ingredient)

    # Find duplicates
    duplicates = {name: ings for name, ings in ingredient_groups.items() if len(ings) > 1}

    if not duplicates:
        return recipe, changes

    # Merge duplicates
    merged_ingredients = []
    processed_names = set()

    for ingredient in recipe['ingredients']:
        name = ingredient.get('preferred_term', '').strip().lower()

        if name in processed_names:
            continue  # Already merged

        if name in duplicates:
            # Merge all instances
            group = duplicates[name]
            merged = merge_ingredient_group(group)
            merged_ingredients.append(merged)
            processed_names.add(name)

            changes.append(
                f"Merged {len(group)} duplicate entries of '{ingredient.get('preferred_term')}'"
            )
        else:
            # No duplicates, keep as-is
            merged_ingredients.append(ingredient)
            processed_names.add(name)

    recipe['ingredients'] = merged_ingredients

    return recipe, changes


def merge_ingredient_group(ingredients: List[Dict]) -> Dict:
    """Merge multiple instances of the same ingredient.

    Strategy:
    - Keep first instance as base
    - If concentrations differ, keep the first non-zero one
    - Combine notes/comments
    - Prefer most complete annotations

    Args:
        ingredients: List of duplicate ingredient dicts

    Returns:
        Merged ingredient dict
    """
    if len(ingredients) == 1:
        return ingredients[0]

    # Start with first ingredient
    merged = ingredients[0].copy()

    # Collect all concentrations
    concentrations = [
        ing.get('concentration')
        for ing in ingredients
        if ing.get('concentration')
    ]

    # If we have multiple different concentrations, note this as a warning
    unique_concs = set(str(c) for c in concentrations if c)
    if len(unique_concs) > 1:
        merged['data_quality_flags'] = merged.get('data_quality_flags', [])
        if 'merged_duplicate_concentrations' not in merged['data_quality_flags']:
            merged['data_quality_flags'].append('merged_duplicate_concentrations')

        # Add note about which concentrations were merged
        note = f"Merged duplicate entries with concentrations: {', '.join(unique_concs)}"
        if 'notes' in merged:
            merged['notes'] = f"{merged['notes']}. {note}"
        else:
            merged['notes'] = note

    # Prefer ingredient with CHEBI term if available
    for ing in ingredients:
        if ing.get('term', {}).get('id', '').startswith('CHEBI:'):
            merged['term'] = ing['term']
            break

    return merged


def extract_ph_buffers(recipe: Dict) -> Tuple[Dict, List[str]]:
    """Extract pH buffers mentioned in notes and add as ingredients.

    Args:
        recipe: Recipe dictionary

    Returns:
        Tuple of (modified_recipe, list_of_changes)
    """
    changes = []

    notes = recipe.get('notes', '')
    if not notes:
        return recipe, changes

    # Common pH buffer patterns
    ph_buffer_patterns = [
        (r'pH\s+buffer:\s*([A-Za-z0-9\(\)]+)', 'pH buffer'),
        (r'adjust(?:ed)?\s+(?:pH\s+)?(?:to|with)\s+([A-Za-z0-9\(\)]+)', 'pH adjustment'),
        (r'using\s+([A-Za-z0-9\(\)]+)\s+(?:for\s+)?pH', 'pH control'),
    ]

    buffers_found = set()

    for pattern, context in ph_buffer_patterns:
        matches = re.finditer(pattern, notes, re.IGNORECASE)
        for match in matches:
            buffer_name = match.group(1).strip()

            # Clean up common variations
            buffer_name = buffer_name.replace('_', ' ')

            # Skip if already in ingredients
            existing_names = {
                ing.get('preferred_term', '').lower()
                for ing in recipe.get('ingredients', [])
            }

            if buffer_name.lower() not in existing_names:
                buffers_found.add((buffer_name, context))

    # Add buffers as ingredients
    if buffers_found:
        if 'ingredients' not in recipe:
            recipe['ingredients'] = []

        for buffer_name, context in buffers_found:
            ingredient = {
                'preferred_term': buffer_name,
                'notes': f'Extracted from recipe notes ({context})',
                'data_quality_flags': ['extracted_from_notes']
            }
            recipe['ingredients'].append(ingredient)

            changes.append(
                f"Added pH buffer '{buffer_name}' from notes"
            )

    return recipe, changes


def normalize_concentrations(recipe: Dict) -> Tuple[Dict, List[str]]:
    """Normalize concentration formats for consistency.

    Args:
        recipe: Recipe dictionary

    Returns:
        Tuple of (modified_recipe, list_of_changes)
    """
    changes = []

    for ingredient in recipe.get('ingredients', []):
        conc = ingredient.get('concentration')
        if not conc:
            continue

        # Already normalized if it's a dict with value and unit
        if isinstance(conc, dict):
            continue

        # Try to parse string concentration
        if isinstance(conc, str):
            parsed = parse_concentration(conc)
            if parsed:
                old_conc = conc
                ingredient['concentration'] = parsed
                changes.append(
                    f"Normalized '{ingredient.get('preferred_term')}' concentration: "
                    f"'{old_conc}' → {parsed}"
                )

    return recipe, changes


def parse_concentration(conc_str: str) -> Optional[Dict]:
    """Parse concentration string into structured format.

    Args:
        conc_str: Concentration string (e.g., "10 g/L", "5%")

    Returns:
        Dict with value and unit, or None if can't parse
    """
    # Common patterns
    patterns = [
        (r'([\d.]+)\s*([gm])/[Ll]', lambda m: {'value': float(m[1]), 'unit': f'{m[2].upper()}_PER_L'}),
        (r'([\d.]+)\s*%', lambda m: {'value': float(m[1]), 'unit': 'PERCENT'}),
        (r'([\d.]+)\s*([mµ]?[MgL])', lambda m: {'value': float(m[1]), 'unit': m[2]}),
    ]

    for pattern, parser in patterns:
        match = re.match(pattern, conc_str.strip())
        if match:
            try:
                return parser(match)
            except (ValueError, IndexError):
                pass

    return None


def cleanup_recipe(
    recipe_path: Path,
    dry_run: bool = False,
    verbose: bool = False
) -> Dict:
    """Clean up a single recipe.

    Args:
        recipe_path: Path to recipe file
        dry_run: If True, don't save changes
        verbose: If True, print all changes

    Returns:
        Dictionary with cleanup statistics
    """
    recipe = load_recipe(recipe_path)
    all_changes = []

    # 1. Merge duplicate ingredients
    recipe, changes = merge_duplicate_ingredients(recipe)
    all_changes.extend(changes)

    # 2. Extract pH buffers from notes
    recipe, changes = extract_ph_buffers(recipe)
    all_changes.extend(changes)

    # 3. Normalize concentrations
    recipe, changes = normalize_concentrations(recipe)
    all_changes.extend(changes)

    # Save if changes were made
    if all_changes and not dry_run:
        save_recipe(recipe, recipe_path)

    # Report
    if verbose and all_changes:
        print(f"\n{recipe_path.name}:")
        for change in all_changes:
            print(f"  • {change}")

    return {
        'file': recipe_path.name,
        'changes': len(all_changes),
        'change_list': all_changes,
    }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Clean up data quality issues within recipes'
    )

    parser.add_argument(
        '--normalized-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Path to normalized_yaml directory'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be changed without modifying files'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed changes for each recipe'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of recipes to process (for testing)'
    )

    parser.add_argument(
        '--report',
        type=Path,
        help='Write cleanup report to file'
    )

    args = parser.parse_args()

    # Validate paths
    if not args.normalized_dir.exists():
        print(f"Error: {args.normalized_dir} not found", file=sys.stderr)
        return 1

    print("=" * 70)
    print("Recipe Ingredient Cleanup")
    print("=" * 70)

    if args.dry_run:
        print("\n*** DRY RUN MODE - No files will be modified ***\n")

    # Find all recipes
    print(f"\nScanning {args.normalized_dir}...")
    recipe_paths = find_all_recipes(args.normalized_dir)

    if args.limit:
        recipe_paths = recipe_paths[:args.limit]

    print(f"Found {len(recipe_paths)} recipes")
    print()

    # Process recipes
    print("Processing recipes...")
    results = []

    for i, path in enumerate(recipe_paths, 1):
        try:
            result = cleanup_recipe(path, dry_run=args.dry_run, verbose=args.verbose)
            results.append(result)

            if i % 500 == 0:
                print(f"  Processed {i}/{len(recipe_paths)} recipes...")

        except Exception as e:
            print(f"  Error processing {path}: {e}", file=sys.stderr)

    print(f"Completed: {len(results)} recipes processed")
    print()

    # Generate summary
    total_changes = sum(r['changes'] for r in results)
    recipes_modified = sum(1 for r in results if r['changes'] > 0)

    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Recipes processed:  {len(results)}")
    print(f"Recipes modified:   {recipes_modified}")
    print(f"Total changes:      {total_changes}")

    if total_changes > 0:
        print()
        print("Change breakdown:")

        # Count change types
        change_types = defaultdict(int)
        for result in results:
            for change in result['change_list']:
                if 'Merged' in change:
                    change_types['Duplicate ingredients merged'] += 1
                elif 'Added pH buffer' in change:
                    change_types['pH buffers extracted'] += 1
                elif 'Normalized' in change:
                    change_types['Concentrations normalized'] += 1

        for change_type, count in sorted(change_types.items()):
            print(f"  {change_type}: {count}")

    # Write report
    if args.report:
        report_data = {
            'summary': {
                'recipes_processed': len(results),
                'recipes_modified': recipes_modified,
                'total_changes': total_changes,
            },
            'changes_by_recipe': [
                {
                    'file': r['file'],
                    'changes': r['change_list']
                }
                for r in results if r['changes'] > 0
            ]
        }

        args.report.parent.mkdir(parents=True, exist_ok=True)
        with open(args.report, 'w', encoding='utf-8') as f:
            yaml.dump(report_data, f, default_flow_style=False, allow_unicode=True)

        print()
        print(f"Report written to: {args.report}")

    print()

    if args.dry_run:
        print("DRY RUN: No files were modified. Run without --dry-run to apply changes.")
    elif total_changes > 0:
        print(f"✓ {recipes_modified} recipes cleaned up successfully!")
    else:
        print("✓ No cleanup needed - all recipes are clean!")

    return 0


if __name__ == '__main__':
    sys.exit(main())
