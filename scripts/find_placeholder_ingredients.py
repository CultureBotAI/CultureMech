#!/usr/bin/env python3
"""Find recipes with placeholder ingredients."""

from pathlib import Path
from collections import Counter
import yaml
import re

normalized_dir = Path("data/normalized_yaml")
recipes = list(normalized_dir.rglob("*.yaml"))

placeholder_patterns = [
    r'see\s+source',
    r'refer\s+to',
    r'available\s+at',
    r'contact\s+source',
    r'not\s+specified',
    r'unknown',
    r'medium\s+no\.',
]

placeholder_recipes = []
ingredient_name_counts = Counter()

for recipe_path in recipes[:2000]:  # Sample first 2000
    try:
        with open(recipe_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Fix escape sequences
            content = re.sub(r'\\x[0-9A-Fa-f]{2}', '°', content)
            recipe = yaml.safe_load(content)

        if not isinstance(recipe, dict):
            continue

        ingredients = recipe.get('ingredients', [])
        if not ingredients or len(ingredients) == 0:
            continue

        # Check if all ingredients are placeholders
        all_placeholder = True
        for ing in ingredients:
            preferred_term = ing.get('preferred_term', '').lower()

            # Track ingredient names
            ingredient_name_counts[preferred_term] += 1

            # Check if placeholder
            is_placeholder = any(
                re.search(pattern, preferred_term, re.IGNORECASE)
                for pattern in placeholder_patterns
            )

            if not is_placeholder:
                all_placeholder = False

        if all_placeholder and len(ingredients) > 0:
            placeholder_recipes.append({
                'path': recipe_path.name,
                'name': recipe.get('name', 'Unknown'),
                'ingredient': ingredients[0].get('preferred_term', 'Unknown')
            })

    except Exception as e:
        continue

print(f"Analyzed {min(2000, len(recipes))} recipes")
print(f"Found {len(placeholder_recipes)} recipes with only placeholder ingredients")
print()

print("Top 10 most common ingredient names:")
for name, count in ingredient_name_counts.most_common(10):
    print(f"  {count:4d}x {name[:60]}")

print()
print("Sample placeholder recipes:")
for recipe in placeholder_recipes[:10]:
    print(f"  {recipe['name']}")
    print(f"    File: {recipe['path']}")
    print(f"    Ingredient: {recipe['ingredient']}")
    print()
