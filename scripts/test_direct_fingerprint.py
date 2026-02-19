#!/usr/bin/env python3
"""Test fingerprinting directly."""

from pathlib import Path

# Force reload
import sys
if 'culturemech.merge.fingerprint' in sys.modules:
    del sys.modules['culturemech.merge.fingerprint']

from culturemech.merge.fingerprint import RecipeFingerprinter

recipe_path = Path("data/normalized_yaml/bacterial/TOGO_M1745_Hydrogen-using_methanogen_medium.yaml")

fingerprinter = RecipeFingerprinter()

try:
    fp = fingerprinter.fingerprint_file(recipe_path)
    print(f"✓ Success! Fingerprint: {fp[:16]}...")
except Exception as e:
    print(f"✗ Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
