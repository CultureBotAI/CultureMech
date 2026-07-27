"""Tests for KG-Microbe media matcher."""

import os

import pytest
from pathlib import Path
from culturemech.match import KGMediaMatcher, match_recipe_to_kg_microbe


# kg-microbe's checkout layout varies: the repo may sit directly at
# <workspace>/kg-microbe, or nested one level down at
# <workspace>/kg-microbe/kg-microbe when the outer directory is a workspace
# container. Probing beats hard-coding — the previous single hard-coded guess
# pointed at the container, so these tests silently skipped on a machine that
# had the data all along.
def _resolve_kg_microbe_dir() -> Path | None:
    """First candidate that actually holds the transformed mediadive tables."""
    env = os.environ.get("KG_MICROBE_DIR")
    workspace = Path(__file__).resolve().parent.parent.parent.parent
    candidates = [
        *( [Path(env)] if env else [] ),
        workspace / "kg-microbe" / "kg-microbe",
        workspace / "kg-microbe",
        Path(__file__).resolve().parent.parent.parent / "kg-microbe",
    ]
    for cand in candidates:
        mediadive = cand / "data" / "transformed" / "mediadive"
        if (mediadive / "edges.tsv").is_file() and (mediadive / "nodes.tsv").is_file():
            return cand
    return None


_KG_MICROBE_DIR = _resolve_kg_microbe_dir()
_SKIP_REASON = (
    "KG-Microbe mediadive data not found. Looked for "
    "data/transformed/mediadive/{edges,nodes}.tsv under $KG_MICROBE_DIR and the "
    "usual checkout layouts. Clone kg-microbe and run its transform, or set "
    "KG_MICROBE_DIR."
)



class TestKGMediaMatcher:
    """Tests for KGMediaMatcher class."""

    @pytest.fixture
    def kg_microbe_dir(self):
        """Path to the kg-microbe checkout holding the transformed mediadive tables."""
        if _KG_MICROBE_DIR is None:
            pytest.skip(_SKIP_REASON)
        return _KG_MICROBE_DIR

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
        """Test retrieving medium names.

        This used to assert only `isinstance(str)` and `len > 0`, which a
        biolink category string satisfies — and that is exactly what the loader
        was storing, having read the `category` column instead of `name`. Assert
        the actual name so the bug cannot come back silently.
        """
        if '514' in matcher.medium_names:
            name = matcher.get_medium_name('514')
            assert name == "BACTO MARINE BROTH DIFCO 2216"
            assert not name.startswith("biolink:"), "reading the category column again"

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
        """Test finding matches.

        Medium ids are NOT uniquely determined by their ingredient set: 514,
        760, 1173, 1517 and 1753 all share the same 17 ingredients (1173 is
        literally "MODIFIED MEDIUM 514"). So this asserts every perfect-Jaccard
        hit really is one, and that 514 is among them — not that it sorts first,
        which is an arbitrary tie-break.
        """
        if '514' in matcher.medium_ingredients:
            test_ingredients = matcher.get_medium_ingredients('514')

            matches = matcher.find_matches(test_ingredients, min_jaccard=1.0, max_results=5)

            # find_matches yields (medium_id, jaccard, shared, only_a, only_b).
            assert len(matches) > 0
            assert all(m[1] == 1.0 for m in matches)
            assert all(matcher.get_medium_ingredients(m[0]) == test_ingredients
                       for m in matches)
            assert '514' in {m[0] for m in matches}

    def test_find_exact_match(self, matcher):
        """Test finding exact matches.

        Returns *an* exact match, not a canonical one — see test_find_matches for
        why 514's ingredient set maps to five media.
        """
        if '514' in matcher.medium_ingredients:
            test_ingredients = matcher.get_medium_ingredients('514')

            exact_match = matcher.find_exact_match(test_ingredients)

            assert exact_match is not None
            assert matcher.get_medium_ingredients(exact_match) == test_ingredients

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
        """Path to the kg-microbe checkout holding the transformed mediadive tables."""
        if _KG_MICROBE_DIR is None:
            pytest.skip(_SKIP_REASON)
        return _KG_MICROBE_DIR

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
