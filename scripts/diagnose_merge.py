#!/usr/bin/env python3
"""Diagnostic script to analyze merge behavior."""

from pathlib import Path
from collections import Counter
import yaml

from culturemech.merge.fingerprint import RecipeFingerprinter


def main():
    normalized_dir = Path("data/normalized_yaml")

    # Find all recipes
    recipes = list(normalized_dir.rglob("*.yaml"))
    print(f"Total recipes found: {len(recipes)}")
    print()

    fingerprinter = RecipeFingerprinter()

    # Track statistics
    no_ingredients = 0
    no_valid_ingredients = 0
    has_chebi = 0
    only_names = 0
    fingerprint_counts = Counter()

    # Sample fingerprints for inspection
    fingerprint_samples = {}

    for recipe_path in recipes[:1000]:  # Sample first 1000
        try:
            with open(recipe_path, 'r') as f:
                recipe = yaml.safe_load(f)

            # Check ingredients
            ingredients = recipe.get('ingredients', [])

            if not ingredients:
                no_ingredients += 1
                continue

            # Check for CHEBI IDs
            has_chebi_in_recipe = False
            ingredient_names = []

            for ing in ingredients:
                preferred_term = ing.get('preferred_term', '')
                ingredient_names.append(preferred_term)

                term = ing.get('term')
                if term and isinstance(term, dict):
                    chebi_id = term.get('id', '')
                    if chebi_id and chebi_id.startswith('CHEBI:'):
                        has_chebi_in_recipe = True

            if has_chebi_in_recipe:
                has_chebi += 1
            else:
                only_names += 1

            # Generate fingerprint
            fp = fingerprinter.fingerprint(recipe)

            if fp is None:
                no_valid_ingredients += 1
            else:
                fingerprint_counts[fp] += 1

                # Store sample for top fingerprints
                if fp not in fingerprint_samples:
                    fingerprint_samples[fp] = {
                        'name': recipe.get('name', 'Unknown'),
                        'ingredients': ingredient_names[:5],  # First 5
                        'path': recipe_path.name
                    }

        except Exception as e:
            print(f"Error processing {recipe_path}: {e}")
            continue

    print("=" * 70)
    print("DIAGNOSIS RESULTS")
    print("=" * 70)
    print()
    print(f"Recipes analyzed: {len(recipes[:1000])}")
    print(f"No ingredients field: {no_ingredients}")
    print(f"No valid ingredients (fingerprint=None): {no_valid_ingredients}")
    print(f"With CHEBI IDs: {has_chebi}")
    print(f"Only names (no CHEBI): {only_names}")
    print()

    print(f"Unique fingerprints: {len(fingerprint_counts)}")
    print(f"Average recipes per fingerprint: {sum(fingerprint_counts.values()) / len(fingerprint_counts):.1f}")
    print()

    # Show top duplicates
    print("TOP 10 MOST COMMON FINGERPRINTS:")
    print("=" * 70)
    for fp, count in fingerprint_counts.most_common(10):
        sample = fingerprint_samples[fp]
        print(f"\nCount: {count}")
        print(f"  Example: {sample['name']}")
        print(f"  File: {sample['path']}")
        print(f"  Ingredients: {', '.join(sample['ingredients'])}")
        print(f"  Fingerprint: {fp[:16]}...")


if __name__ == '__main__':
    main()
