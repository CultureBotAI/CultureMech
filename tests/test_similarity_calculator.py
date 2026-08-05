"""Tests for media similarity calculator."""

import pytest

from culturemech.taxonomy.similarity import SimilarityCalculator
from culturemech.taxonomy.unit_converter import UnitConverter


class TestUnitConverter:
    """Test unit conversion functionality."""

    def test_molar_to_molar(self):
        """Test that molar values pass through unchanged."""
        converter = UnitConverter()
        ing = {'term': {'id': 'CHEBI:26710'}}  # NaCl

        result = converter.to_molar(1.0, 'MOLAR', ing)
        assert result == 1.0

    def test_millimolar_to_molar(self):
        """Test millimolar conversion."""
        converter = UnitConverter()
        ing = {'term': {'id': 'CHEBI:26710'}}

        result = converter.to_molar(1000.0, 'MILLIMOLAR', ing)
        assert result == 1.0

    def test_variable_returns_none(self):
        """Test that variable concentrations return None."""
        converter = UnitConverter()
        ing = {'term': {'id': 'CHEBI:26710'}}

        result = converter.to_molar(1.0, 'VARIABLE', ing)
        assert result is None


class TestSimilarityCalculator:
    """Test similarity calculation."""

    def test_identical_recipes(self):
        """Test that identical recipes have similarity 1.0."""
        calc = SimilarityCalculator(metric='bray_curtis')

        recipe = {
            'ingredients': [
                {
                    'preferred_term': 'Sodium chloride',
                    'term': {'id': 'CHEBI:26710'},
                    'concentration': {'value': '5', 'unit': 'G_PER_L'}
                },
                {
                    'preferred_term': 'Glucose',
                    'term': {'id': 'CHEBI:17234'},
                    'concentration': {'value': '10', 'unit': 'G_PER_L'}
                }
            ]
        }

        similarity = calc.calculate_similarity(recipe, recipe)
        assert similarity == 1.0

    def test_completely_different_recipes(self):
        """Test that recipes with no shared ingredients have low similarity."""
        calc = SimilarityCalculator(metric='bray_curtis')

        recipe_a = {
            'ingredients': [
                {
                    'preferred_term': 'Sodium chloride',
                    'term': {'id': 'CHEBI:26710'},
                    'concentration': {'value': '5', 'unit': 'G_PER_L'}
                }
            ]
        }

        recipe_b = {
            'ingredients': [
                {
                    'preferred_term': 'Glucose',
                    'term': {'id': 'CHEBI:17234'},
                    'concentration': {'value': '10', 'unit': 'G_PER_L'}
                }
            ]
        }

        similarity = calc.calculate_similarity(recipe_a, recipe_b)
        assert similarity == 0.0  # No overlap

    def test_jaccard_index(self):
        """Test Jaccard index calculation (presence/absence)."""
        calc = SimilarityCalculator(metric='jaccard')

        recipe_a = {
            'ingredients': [
                {'term': {'id': 'CHEBI:26710'}, 'concentration': {'value': '5', 'unit': 'G_PER_L'}},
                {'term': {'id': 'CHEBI:17234'}, 'concentration': {'value': '10', 'unit': 'G_PER_L'}},
                {'term': {'id': 'CHEBI:32815'}, 'concentration': {'value': '2', 'unit': 'G_PER_L'}}
            ]
        }

        recipe_b = {
            'ingredients': [
                {'term': {'id': 'CHEBI:26710'}, 'concentration': {'value': '5', 'unit': 'G_PER_L'}},
                {'term': {'id': 'CHEBI:17234'}, 'concentration': {'value': '10', 'unit': 'G_PER_L'}},
                {'term': {'id': 'CHEBI:32815'}, 'concentration': {'value': '2', 'unit': 'G_PER_L'}},
                {'term': {'id': 'CHEBI:29108'}, 'concentration': {'value': '1', 'unit': 'G_PER_L'}},  # Extra ingredient
            ]
        }

        similarity = calc.calculate_similarity(recipe_a, recipe_b)
        # Jaccard = 3 / 4 = 0.75
        assert similarity == 0.75

    def test_presence_absence_fallback(self):
        """Test fallback to presence/absence when conversions fail."""
        calc = SimilarityCalculator(metric='bray_curtis')

        recipe_a = {
            'ingredients': [
                {'preferred_term': 'Unknown compound A', 'concentration': {'value': 'variable', 'unit': 'VARIABLE'}},
                {'preferred_term': 'Unknown compound B', 'concentration': {'value': 'variable', 'unit': 'VARIABLE'}}
            ]
        }

        recipe_b = {
            'ingredients': [
                {'preferred_term': 'Unknown compound A', 'concentration': {'value': 'variable', 'unit': 'VARIABLE'}},
                {'preferred_term': 'Unknown compound B', 'concentration': {'value': 'variable', 'unit': 'VARIABLE'}}
            ]
        }

        # Should still work with presence/absence
        similarity = calc.calculate_similarity(recipe_a, recipe_b)
        assert similarity == 1.0

    def test_calculate_all_metrics(self):
        """Test calculating all metrics at once."""
        calc = SimilarityCalculator()

        recipe = {
            'ingredients': [
                {'term': {'id': 'CHEBI:26710'}, 'concentration': {'value': '5', 'unit': 'G_PER_L'}}
            ]
        }

        metrics = calc.calculate_all_metrics(recipe, recipe)

        assert 'bray_curtis' in metrics
        assert 'jaccard' in metrics
        assert 'cosine' in metrics
        assert 'sorensen' in metrics

        # All should be 1.0 for identical recipes
        assert metrics['bray_curtis'] == 1.0
        assert metrics['jaccard'] == 1.0
        assert metrics['cosine'] == 1.0
        assert metrics['sorensen'] == 1.0

    def test_concentration_vector_stats(self):
        """Test concentration vector statistics."""
        calc = SimilarityCalculator()

        recipe = {
            'ingredients': [
                {'term': {'id': 'CHEBI:26710'}, 'concentration': {'value': '5', 'unit': 'G_PER_L'}},
                {'term': {'id': 'CHEBI:17234'}, 'concentration': {'value': '10', 'unit': 'G_PER_L'}},
                {'term': {'id': 'CHEBI:32815'}, 'concentration': {'value': 'variable', 'unit': 'VARIABLE'}}
            ]
        }

        stats = calc.get_concentration_vector_stats(recipe)

        assert stats['total_ingredients'] == 3
        assert 'convertible' in stats
        assert 'conversion_rate' in stats
        assert 'ingredient_ids' in stats
        assert len(stats['ingredient_ids']) == 3


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
