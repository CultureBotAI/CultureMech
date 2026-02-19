#!/usr/bin/env python3
"""Test loading a problematic YAML file."""

from pathlib import Path
import re
import yaml

recipe_path = Path("data/normalized_yaml/bacterial/TOGO_M1745_Hydrogen-using_methanogen_medium.yaml")

print("Attempting to load:", recipe_path)
print()

try:
    with open(recipe_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Raw content (first 500 chars):")
    print(content[:500])
    print()

    # Try fixing
    fixed_content = re.sub(r'\\x[0-9A-Fa-f]{2}', '°', content)

    print("Fixed content (first 500 chars):")
    print(fixed_content[:500])
    print()

    recipe = yaml.safe_load(fixed_content)
    print("✓ Successfully loaded!")
    print(f"Name: {recipe.get('name')}")

except Exception as e:
    print(f"✗ Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
