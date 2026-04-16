"""Tests for KG-Microbe media matcher."""

import pytest
from pathlib import Path
from culturemech.match import KGMediaMatcher, match_recipe_to_kg_microbe


class TestKGMediaMatcher:
    """Tests for KGMediaMatcher class."""

    @pytest.fixture
    def kg_microbe_dir(self):
        """Path to kg-microbe repository."""
        # Adjust this path based on your local setup
        kg_dir = Path(__file__).parent.parent.parent.parent / "kg-microbe"

        if not kg_dir.exists():
            pytest.skip(f"KG-Microbe not found at {kg_dir}")

        return kg_dir

    @pytest.fixture
    def matcher(self, kg_microbe_dir):
        """Create KGMediaMatcher instance."""
        return KGMediaMatcher(kg_microbe_dir)

    def test_initialization(self, matcher):
        """Test matcher initializes successfully."""
        assert matcher.medium_ingredients is not None
        assert matcher.medium_names is not None
        assert len(matcher.medium_ingredients) > 0
        assert len(matcher.medium_names) > 0

    def test_normalize_ontology_id(self, matcher):
        """Test ontology ID normalization."""
        assert matcher._normalize_ontology_id("CHEBI:0000178") == "CHEBI:178"
        assert matcher._normalize_ontology_id("CHEBI:178") == "CHEBI:178"
        assert matcher._normalize_ontology_id("FOODON:03302071") == "FOODON:3302071"
        assert matcher._normalize_ontology_id("FOODON:3302071") == "FOODON:3302071"
        assert matcher._normalize_ontology_id("UNKNOWN:123") == "UNKNOWN:123"

    def test_get_medium_name(self, matcher):
        """Test retrieving medium names."""
        # Test known medium
        if '514' in matcher.medium_names:
            name = matcher.get_medium_name('514')
            assert isinstance(name, str)
            assert len(name) > 0

        # Test unknown medium
        unknown_name = matcher.get_medium_name('99999999')
        assert unknown_name == "Medium 99999999"

    def test_get_medium_ingredients(self, matcher):
        """Test retrieving medium ingredients."""
        # Test known medium
        if '514' in matcher.medium_ingredients:
            ingredients = matcher.get_medium_ingredients('514')
            assert isinstance(ingredients, set)
            assert len(ingredients) > 0
            # All should be CHEBI or FOODON IDs
            for ing in ingredients:
                assert ing.startswith('CHEBI:') or ing.startswith('FOODON:')

        # Test unknown medium
        unknown_ingredients = matcher.get_medium_ingredients('99999999')
        assert unknown_ingredients == set()

    def test_compare_recipes(self, matcher):
        """Test recipe comparison."""
        recipe1 = {'CHEBI:1', 'CHEBI:2', 'CHEBI:3'}
        recipe2 = {'CHEBI:2', 'CHEBI:3', 'CHEBI:4'}

        jaccard, shared, only1, only2 = matcher.compare_recipes(recipe1, recipe2)

        assert jaccard == 0.5  # 2 shared / 4 total
        assert shared == {'CHEBI:2', 'CHEBI:3'}
        assert only1 == {'CHEBI:1'}
        assert only2 == {'CHEBI:4'}

    def test_compare_identical_recipes(self, matcher):
        """Test identical recipe comparison."""
        recipe = {'CHEBI:1', 'CHEBI:2'}

        jaccard, shared, only1, only2 = matcher.compare_recipes(recipe, recipe)

        assert jaccard == 1.0
        assert shared == recipe
        assert only1 == set()
        assert only2 == set()

    def test_compare_empty_recipes(self, matcher):
        """Test empty recipe comparison."""
        recipe1 = set()
        recipe2 = {'CHEBI:1'}

        jaccard, shared, only1, only2 = matcher.compare_recipes(recipe1, recipe2)

        assert jaccard == 0.0
        assert shared == set()
        assert only1 == set()
        assert only2 == {'CHEBI:1'}

    def test_find_matches(self, matcher):
        """Test finding matches."""
        # Use ingredients from a known medium if available
        if '514' in matcher.medium_ingredients:
            test_ingredients = matcher.get_medium_ingredients('514')

            matches = matcher.find_matches(test_ingredients, min_jaccard=1.0, max_results=5)

            assert len(matches) > 0
            # First match should be exact
            assert matches[0][0] == '514'
            assert matches[0][1] == 1.0  # Jaccard score

    def test_find_exact_match(self, matcher):
        """Test finding exact matches."""
        # Use ingredients from a known medium if available
        if '514' in matcher.medium_ingredients:
            test_ingredients = matcher.get_medium_ingredients('514')

            exact_match = matcher.find_exact_match(test_ingredients)

            assert exact_match == '514'

    def test_find_exact_match_no_match(self, matcher):
        """Test finding exact match when none exists."""
        fake_ingredients = {'CHEBI:999999', 'CHEBI:888888'}

        exact_match = matcher.find_exact_match(fake_ingredients)

        assert exact_match is None

    def test_generate_match_report(self, matcher, tmp_path):
        """Test match report generation."""
        # Create a simple test recipe
        test_recipe = tmp_path / "test_recipe.yaml"
        recipe_content = """
name: Test Recipe
ingredients:
  - preferred_term: Glucose
    term:
      id: CHEBI:42758
      label: D-glucose
  - preferred_term: NaCl
    term:
      id: CHEBI:26710
      label: sodium chloride
"""
        test_recipe.write_text(recipe_content)

        report = matcher.generate_match_report(test_recipe, top_n=5)

        assert 'recipe' in report
        assert 'ingredient_count' in report
        assert report['ingredient_count'] == 2
        assert 'top_matches' in report
        assert len(report['top_matches']) <= 5


class TestMatchRecipeToKGMicrobe:
    """Tests for convenience function."""

    @pytest.fixture
    def kg_microbe_dir(self):
        """Path to kg-microbe repository."""
        kg_dir = Path(__file__).parent.parent.parent.parent / "kg-microbe"

        if not kg_dir.exists():
            pytest.skip(f"KG-Microbe not found at {kg_dir}")

        return kg_dir

    def test_match_recipe_exact(self, kg_microbe_dir, tmp_path):
        """Test matching recipe with exact match."""
        # Create a test recipe with known ingredients
        test_recipe = tmp_path / "test_recipe.yaml"
        recipe_content = """
name: Test Recipe
ingredients:
  - preferred_term: Glucose
    term:
      id: CHEBI:42758
"""
        test_recipe.write_text(recipe_content)

        result = match_recipe_to_kg_microbe(
            test_recipe,
            kg_microbe_dir,
            min_jaccard=0.5
        )

        # May or may not find match depending on KG content
        assert result is None or result.startswith("mediadive.medium:")

    def test_match_recipe_no_ingredients(self, kg_microbe_dir, tmp_path):
        """Test matching recipe with no ingredients."""
        test_recipe = tmp_path / "empty_recipe.yaml"
        recipe_content = """
name: Empty Recipe
ingredients: []
"""
        test_recipe.write_text(recipe_content)

        result = match_recipe_to_kg_microbe(
            test_recipe,
            kg_microbe_dir,
            min_jaccard=1.0
        )

        assert result is None
