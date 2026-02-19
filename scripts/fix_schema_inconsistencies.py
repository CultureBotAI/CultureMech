#!/usr/bin/env python3
"""Fix schema inconsistencies in normalized recipes.

This script identifies and fixes recipes that don't conform to the LinkML schema,
particularly algae recipes that use agent_term/amount instead of preferred_term/concentration.
"""

import argparse
import sys
from pathlib import Path
from typing import Dict, List

import yaml


def fix_ingredient_schema(ingredient: Dict) -> Dict:
    """Fix ingredient to match LinkML schema.

    Converts:
    - agent_term.preferred_term -> preferred_term
    - amount -> concentration (as best effort)

    Args:
        ingredient: Ingredient dictionary

    Returns:
        Fixed ingredient dictionary
    """
    fixed = {}

    # Fix preferred_term
    if 'preferred_term' in ingredient:
        # Already correct
        fixed['preferred_term'] = ingredient['preferred_term']
    elif 'agent_term' in ingredient and isinstance(ingredient['agent_term'], dict):
        # Extract from agent_term
        agent_term = ingredient['agent_term']
        if 'preferred_term' in agent_term:
            fixed['preferred_term'] = agent_term['preferred_term']

            # Copy term if it exists
            if 'term' in agent_term:
                fixed['term'] = agent_term['term']
    else:
        # No valid preferred_term found
        return None

    # Fix concentration
    if 'concentration' in ingredient:
        # Already correct
        fixed['concentration'] = ingredient['concentration']
    elif 'amount' in ingredient:
        # Convert amount to concentration (placeholder)
        amount_str = str(ingredient['amount'])
        fixed['concentration'] = {
            'value': 'variable',
            'unit': 'G_PER_L'
        }
        # Add note about original amount
        fixed['notes'] = f'Original amount: {amount_str}'
    else:
        # No concentration - add placeholder
        fixed['concentration'] = {
            'value': 'variable',
            'unit': 'G_PER_L'
        }

    # Copy other fields
    for key in ['term', 'notes', 'role', 'chemical_formula', 'molecular_weight']:
        if key in ingredient and key not in fixed:
            fixed[key] = ingredient[key]

    return fixed


def fix_recipe_schema(recipe: Dict) -> tuple[Dict, List[str]]:
    """Fix recipe schema inconsistencies.

    Args:
        recipe: Recipe dictionary

    Returns:
        Tuple of (fixed_recipe, list_of_issues_found)
    """
    issues = []
    fixed = recipe.copy()

    # Fix ingredients
    if 'ingredients' in recipe:
        original_ingredients = recipe['ingredients']
        fixed_ingredients = []

        for i, ing in enumerate(original_ingredients):
            if not isinstance(ing, dict):
                issues.append(f"Ingredient {i} is not a dictionary")
                continue

            # Check if needs fixing
            needs_fix = False
            if 'agent_term' in ing:
                needs_fix = True
                issues.append(f"Ingredient {i} has agent_term instead of preferred_term")
            if 'amount' in ing and 'concentration' not in ing:
                needs_fix = True
                issues.append(f"Ingredient {i} has amount instead of concentration")

            if needs_fix:
                fixed_ing = fix_ingredient_schema(ing)
                if fixed_ing:
                    fixed_ingredients.append(fixed_ing)
                else:
                    issues.append(f"Ingredient {i} could not be fixed (skipped)")
            else:
                fixed_ingredients.append(ing)

        if fixed_ingredients:
            fixed['ingredients'] = fixed_ingredients
        else:
            issues.append("No valid ingredients after fixing")

    return fixed, issues


def fix_recipe_file(recipe_path: Path, dry_run: bool = False) -> tuple[bool, List[str]]:
    """Fix a single recipe file.

    Args:
        recipe_path: Path to recipe YAML file
        dry_run: If True, don't write changes

    Returns:
        Tuple of (was_fixed, list_of_issues)
    """
    try:
        # Load recipe
        with open(recipe_path, 'r', encoding='utf-8') as f:
            recipe = yaml.safe_load(f)

        if not isinstance(recipe, dict):
            return False, ["Recipe is not a dictionary"]

        # Fix schema
        fixed_recipe, issues = fix_recipe_schema(recipe)

        if not issues:
            # No issues found
            return False, []

        # Write fixed recipe
        if not dry_run:
            with open(recipe_path, 'w', encoding='utf-8') as f:
                yaml.dump(fixed_recipe, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        return True, issues

    except Exception as e:
        return False, [f"Error processing file: {e}"]


def main():
    parser = argparse.ArgumentParser(
        description='Fix schema inconsistencies in normalized recipes'
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
        help='Show what would be fixed without writing files'
    )

    parser.add_argument(
        '--category',
        type=str,
        help='Only fix specific category (e.g., algae)'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed issues for each file'
    )

    args = parser.parse_args()

    if not args.normalized_dir.exists():
        print(f"Error: Directory not found: {args.normalized_dir}", file=sys.stderr)
        return 1

    print("=" * 70)
    print("Schema Inconsistency Fixer")
    print("=" * 70)
    print()

    if args.dry_run:
        print("DRY RUN MODE - no files will be modified")
        print()

    # Find recipes to process
    if args.category:
        category_dir = args.normalized_dir / args.category
        if not category_dir.exists():
            print(f"Error: Category directory not found: {category_dir}", file=sys.stderr)
            return 1
        recipe_files = list(category_dir.glob('*.yaml'))
    else:
        recipe_files = list(args.normalized_dir.rglob('*.yaml'))

    print(f"Found {len(recipe_files)} recipes to check")
    print()

    # Process recipes
    fixed_count = 0
    error_count = 0
    issue_summary = {}

    for recipe_path in recipe_files:
        was_fixed, issues = fix_recipe_file(recipe_path, dry_run=args.dry_run)

        if issues:
            if was_fixed:
                fixed_count += 1

                if args.verbose:
                    print(f"Fixed: {recipe_path.name}")
                    for issue in issues:
                        print(f"  - {issue}")
                    print()

                # Track issue types
                for issue in issues:
                    issue_type = issue.split(':')[0] if ':' in issue else issue
                    issue_summary[issue_type] = issue_summary.get(issue_type, 0) + 1
            else:
                error_count += 1
                print(f"Error: {recipe_path.name}")
                for issue in issues:
                    print(f"  - {issue}")
                print()

    # Summary
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total recipes checked: {len(recipe_files)}")
    print(f"Recipes fixed: {fixed_count}")
    print(f"Recipes with errors: {error_count}")
    print()

    if issue_summary:
        print("Issue types found:")
        for issue_type, count in sorted(issue_summary.items(), key=lambda x: x[1], reverse=True):
            print(f"  {issue_type}: {count}")
        print()

    if args.dry_run and fixed_count > 0:
        print("Run without --dry-run to apply fixes")
    elif fixed_count > 0:
        print(f"✓ Successfully fixed {fixed_count} recipes")
    else:
        print("✓ No schema issues found")

    return 0


if __name__ == '__main__':
    sys.exit(main())
