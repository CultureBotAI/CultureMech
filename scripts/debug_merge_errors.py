#!/usr/bin/env python3
"""Debug merge errors to see what's actually failing."""

from pathlib import Path
from culturemech.merge.fingerprint import RecipeFingerprinter

normalized_dir = Path("data/normalized_yaml")
recipes = list(normalized_dir.rglob("*.yaml"))[:100]  # Sample 100

fingerprinter = RecipeFingerprinter()

error_counts = {}
success = 0

for recipe_path in recipes:
    try:
        fp = fingerprinter.fingerprint_file(recipe_path)
        if fp:
            success += 1
        else:
            print(f"None fingerprint: {recipe_path.name}")
    except Exception as e:
        error_type = type(e).__name__
        error_msg = str(e)[:80]
        key = f"{error_type}: {error_msg}"

        if key not in error_counts:
            error_counts[key] = {'count': 0, 'example': recipe_path.name}
        error_counts[key]['count'] += 1

print(f"\nSuccess: {success}")
print(f"\nError summary:")
for error, info in sorted(error_counts.items(), key=lambda x: x[1]['count'], reverse=True):
    print(f"  {info['count']:3d}x {error}")
    print(f"        Example: {info['example']}")
