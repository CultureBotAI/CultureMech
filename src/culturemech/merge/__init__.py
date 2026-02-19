"""Recipe deduplication and merging module.

This module provides functionality for:
- Fingerprinting recipes based on ingredient sets
- Matching duplicate recipes with identical ingredients
- Merging duplicate recipes into canonical records
- Preserving provenance and synonyms
"""

from culturemech.merge.fingerprint import RecipeFingerprinter
from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merger import RecipeMerger

__all__ = ["RecipeFingerprinter", "RecipeMatcher", "RecipeMerger"]
