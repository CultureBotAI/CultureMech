"""Similarity calculation for media recipes.

Implements multiple similarity metrics for comparing media based on
ingredient composition and concentrations:
- Bray-Curtis dissimilarity (concentration-aware, ecologically appropriate)
- Jaccard index (presence/absence)
- Cosine similarity (vector-based)
- Sørensen-Dice index
"""

from typing import Dict, Optional, Set, List
from collections import defaultdict
import math

from .unit_converter import UnitConverter


class SimilarityCalculator:
    """Calculate recipe similarity using multiple metrics."""

    def __init__(self, metric: str = 'bray_curtis', mw_cache_path: Optional[str] = None):
        """
        Initialize similarity calculator.

        Args:
            metric: Default metric to use ('bray_curtis', 'jaccard', 'cosine', 'sorensen')
            mw_cache_path: Path to ChEBI molecular weight cache
        """
        self.metric = metric
        self.unit_converter = UnitConverter(mw_cache_path)

    def calculate_similarity(
        self,
        recipe_a: Dict,
        recipe_b: Dict,
        metric: Optional[str] = None
    ) -> float:
        """
        Calculate similarity between two recipes.

        Args:
            recipe_a: First recipe dict with 'ingredients' field
            recipe_b: Second recipe dict with 'ingredients' field
            metric: Metric to use (overrides default if specified)

        Returns:
            Similarity score (0.0-1.0, higher = more similar)
            Returns None if calculation fails

        Examples:
            >>> calc = SimilarityCalculator()
            >>> recipe1 = {'ingredients': [{'term': {'id': 'CHEBI:26710'}, 'concentration': {'value': '5', 'unit': 'G_PER_L'}}]}
            >>> recipe2 = {'ingredients': [{'term': {'id': 'CHEBI:26710'}, 'concentration': {'value': '5', 'unit': 'G_PER_L'}}]}
            >>> calc.calculate_similarity(recipe1, recipe2)
            1.0  # Identical
        """
        metric = metric or self.metric

        # Build concentration vectors
        vec_a = self._build_concentration_vector(recipe_a)
        vec_b = self._build_concentration_vector(recipe_b)

        if not vec_a or not vec_b:
            return None

        # Calculate similarity based on metric
        if metric == 'bray_curtis':
            return self._bray_curtis_similarity(vec_a, vec_b)
        elif metric == 'jaccard':
            return self._jaccard_similarity(vec_a, vec_b)
        elif metric == 'cosine':
            return self._cosine_similarity(vec_a, vec_b)
        elif metric == 'sorensen':
            return self._sorensen_dice_similarity(vec_a, vec_b)
        else:
            raise ValueError(f"Unknown metric: {metric}")

    def _build_concentration_vector(self, recipe: Dict) -> Optional[Dict[str, float]]:
        """
        Extract normalized concentrations (molar) for all ingredients.

        Args:
            recipe: Recipe dict with 'ingredients' field

        Returns:
            Dict mapping ingredient_id -> molar_concentration
            Returns None if <80% of ingredients have concentrations

        Uses CHEBI ID as ingredient identifier when available,
        falls back to preferred_term for non-chemical ingredients.
        """
        ingredients = recipe.get('ingredients', [])
        if not ingredients:
            return None

        vector = {}
        convertible_count = 0
        total_with_conc = 0

        for ing in ingredients:
            # Get ingredient identifier (CHEBI ID preferred)
            ing_id = self._get_ingredient_id(ing)
            if not ing_id:
                continue

            # Get concentration
            conc = ing.get('concentration', {})
            value_str = conc.get('value', 'variable')
            unit = conc.get('unit', 'UNKNOWN')

            # Skip variable/unknown
            if value_str in ('variable', 'unknown', 'VARIABLE', 'UNKNOWN'):
                # Use presence/absence (concentration = 1.0 arbitrary unit)
                vector[ing_id] = 1.0
                continue

            try:
                value = float(value_str)
                total_with_conc += 1

                # Convert to molar
                molar = self.unit_converter.to_molar(value, unit, ing)

                if molar is not None:
                    vector[ing_id] = molar
                    convertible_count += 1
                else:
                    # Use presence/absence for non-convertible
                    vector[ing_id] = 1.0

            except (ValueError, TypeError):
                # Use presence/absence for invalid values
                vector[ing_id] = 1.0

        # Require at least 80% conversion success for quantitative comparison
        if total_with_conc > 0:
            conversion_rate = convertible_count / total_with_conc
            if conversion_rate < 0.80:
                # Fall back to presence/absence for all
                return {ing_id: 1.0 for ing_id in vector.keys()}

        return vector if vector else None

    def _get_ingredient_id(self, ingredient: Dict) -> Optional[str]:
        """
        Get unique identifier for ingredient.

        Priority:
            1. CHEBI ID (chemical entities)
            2. MediaIngredientMech ID (curated ingredients)
            3. Preferred term (fallback)

        Args:
            ingredient: Ingredient dict

        Returns:
            Unique identifier string
        """
        # Try CHEBI ID
        chebi_id = ingredient.get('term', {}).get('id')
        if chebi_id:
            return chebi_id

        # Try MediaIngredientMech ID
        mim_id = ingredient.get('mediaingredientmech_term', {}).get('id')
        if mim_id:
            return mim_id

        # Try CultureMech term (for solutions/media as ingredients)
        cm_id = ingredient.get('culturemech_term', {}).get('id')
        if cm_id:
            return cm_id

        # Fallback to normalized name
        name = ingredient.get('preferred_term', '')
        if name:
            return f"NAME:{name.lower().strip()}"

        return None

    def _bray_curtis_similarity(self, vec_a: Dict[str, float], vec_b: Dict[str, float]) -> float:
        """
        Calculate Bray-Curtis similarity (1 - dissimilarity).

        Formula:
            BC = Σ|c_i^A - c_i^B| / Σ(c_i^A + c_i^B)
            Similarity = 1 - BC

        Args:
            vec_a: Concentration vector for recipe A
            vec_b: Concentration vector for recipe B

        Returns:
            Similarity score (0.0-1.0, higher = more similar)
        """
        all_ingredients = set(vec_a.keys()) | set(vec_b.keys())

        numerator = 0.0
        denominator = 0.0

        for ing_id in all_ingredients:
            conc_a = vec_a.get(ing_id, 0.0)
            conc_b = vec_b.get(ing_id, 0.0)

            numerator += abs(conc_a - conc_b)
            denominator += (conc_a + conc_b)

        if denominator == 0:
            return 0.0

        dissimilarity = numerator / denominator
        return 1.0 - dissimilarity

    def _jaccard_similarity(self, vec_a: Dict[str, float], vec_b: Dict[str, float]) -> float:
        """
        Calculate Jaccard index (presence/absence).

        Formula:
            Jaccard = |A ∩ B| / |A ∪ B|

        Args:
            vec_a: Concentration vector for recipe A (only keys used)
            vec_b: Concentration vector for recipe B (only keys used)

        Returns:
            Similarity score (0.0-1.0)
        """
        set_a = set(vec_a.keys())
        set_b = set(vec_b.keys())

        intersection = len(set_a & set_b)
        union = len(set_a | set_b)

        if union == 0:
            return 0.0

        return intersection / union

    def _cosine_similarity(self, vec_a: Dict[str, float], vec_b: Dict[str, float]) -> float:
        """
        Calculate cosine similarity (vector-based).

        Formula:
            cosine = (A · B) / (||A|| * ||B||)

        Args:
            vec_a: Concentration vector for recipe A
            vec_b: Concentration vector for recipe B

        Returns:
            Similarity score (0.0-1.0)
        """
        all_ingredients = set(vec_a.keys()) | set(vec_b.keys())

        # Dot product
        dot_product = sum(
            vec_a.get(ing_id, 0.0) * vec_b.get(ing_id, 0.0)
            for ing_id in all_ingredients
        )

        # Magnitudes
        mag_a = math.sqrt(sum(c**2 for c in vec_a.values()))
        mag_b = math.sqrt(sum(c**2 for c in vec_b.values()))

        if mag_a == 0 or mag_b == 0:
            return 0.0

        return dot_product / (mag_a * mag_b)

    def _sorensen_dice_similarity(self, vec_a: Dict[str, float], vec_b: Dict[str, float]) -> float:
        """
        Calculate Sørensen-Dice index (weighted).

        Formula:
            Dice = 2 * Σ min(c_i^A, c_i^B) / (Σ c_i^A + Σ c_i^B)

        Args:
            vec_a: Concentration vector for recipe A
            vec_b: Concentration vector for recipe B

        Returns:
            Similarity score (0.0-1.0)
        """
        all_ingredients = set(vec_a.keys()) | set(vec_b.keys())

        intersection_sum = sum(
            min(vec_a.get(ing_id, 0.0), vec_b.get(ing_id, 0.0))
            for ing_id in all_ingredients
        )

        sum_a = sum(vec_a.values())
        sum_b = sum(vec_b.values())

        if sum_a + sum_b == 0:
            return 0.0

        return 2 * intersection_sum / (sum_a + sum_b)

    def calculate_all_metrics(self, recipe_a: Dict, recipe_b: Dict) -> Dict[str, float]:
        """
        Calculate all similarity metrics for comparison.

        Args:
            recipe_a: First recipe
            recipe_b: Second recipe

        Returns:
            Dict mapping metric_name -> similarity_score
        """
        metrics = {}

        for metric_name in ['bray_curtis', 'jaccard', 'cosine', 'sorensen']:
            try:
                similarity = self.calculate_similarity(recipe_a, recipe_b, metric=metric_name)
                metrics[metric_name] = similarity
            except Exception as e:
                metrics[metric_name] = None

        return metrics

    def get_concentration_vector_stats(self, recipe: Dict) -> Dict:
        """
        Get statistics about concentration vector for debugging.

        Args:
            recipe: Recipe dict

        Returns:
            Dict with stats: {
                'total_ingredients': int,
                'convertible': int,
                'conversion_rate': float,
                'total_concentration': float,
                'ingredient_ids': List[str]
            }
        """
        ingredients = recipe.get('ingredients', [])
        vec = self._build_concentration_vector(recipe)

        if not vec:
            return {
                'total_ingredients': len(ingredients),
                'convertible': 0,
                'conversion_rate': 0.0,
                'total_concentration': 0.0,
                'ingredient_ids': []
            }

        # Count convertible (molar values > 1.0 indicates actual concentration, not just presence)
        convertible = sum(1 for c in vec.values() if c != 1.0)

        return {
            'total_ingredients': len(ingredients),
            'convertible': convertible,
            'conversion_rate': convertible / len(ingredients) if len(ingredients) > 0 else 0.0,
            'total_concentration': sum(vec.values()),
            'ingredient_ids': list(vec.keys())
        }
