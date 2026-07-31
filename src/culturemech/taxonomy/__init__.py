"""Media similarity and unit-conversion utilities.

Provides tools for:
- Calculating similarity between media recipes (Bray-Curtis, Jaccard, etc.)
- Converting concentration units to molar

`TaxonomyClassifier` was removed here (#154). It wrote a `taxonomy:` block whose
class was never added to the schema, so its output could not validate; and its
single-axis `domain` conflated what #148 split into orthogonal composition /
nutritional-class / functional-role axes. Reviving it means designing that schema
class against the three axes first — a feature, not a repair.
"""

from .similarity import SimilarityCalculator
from .unit_converter import UnitConverter

__all__ = [
    'SimilarityCalculator',
    'UnitConverter',
]
