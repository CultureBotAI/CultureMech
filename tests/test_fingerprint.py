"""Unit tests for recipe fingerprinting."""

import pytest

from culturemech.merge.fingerprint import RecipeFingerprinter


class TestRecipeFingerprinter:
    """Test RecipeFingerprinter class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.fingerprinter = RecipeFingerprinter()

    def test_fingerprint_basic(self):
        """Test basic fingerprinting with CHEBI IDs."""
        recipe = {
            'name': 'Test Medium',
            'ingredients': [
                {
                    'preferred_term': 'Glucose',
                    'term': {'id': 'CHEBI:17234', 'label': 'glucose'},
                    'concentration': {'value': '10', 'unit': 'G_PER_L'}
                },
                {
                    'preferred_term': 'NaCl',
                    'term': {'id': 'CHEBI:26710', 'label': 'sodium chloride'},
                    'concentration': {'value': '5', 'unit': 'G_PER_L'}
                }
            ]
        }

        fingerprint = self.fingerprinter.fingerprint(recipe)

        # Should be a valid SHA256 hex digest
        assert len(fingerprint) == 64
        assert all(c in '0123456789abcdef' for c in fingerprint)

    def test_fingerprint_order_independence(self):
        """Test that ingredient order doesn't affect fingerprint."""
        recipe1 = {
            'ingredients': [
                {'preferred_term': 'Glucose', 'term': {'id': 'CHEBI:17234'}},
                {'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}
            ]
        }

        recipe2 = {
            'ingredients': [
                {'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}},
                {'preferred_term': 'Glucose', 'term': {'id': 'CHEBI:17234'}}
            ]
        }

        fp1 = self.fingerprinter.fingerprint(recipe1)
        fp2 = self.fingerprinter.fingerprint(recipe2)

        assert fp1 == fp2

    def test_fingerprint_concentration_independence(self):
        """Test that concentration doesn't affect fingerprint."""
        recipe1 = {
            'ingredients': [
                {
                    'preferred_term': 'Glucose',
                    'term': {'id': 'CHEBI:17234'},
                    'concentration': {'value': '10', 'unit': 'G_PER_L'}
                }
            ]
        }

        recipe2 = {
            'ingredients': [
                {
                    'preferred_term': 'Glucose',
                    'term': {'id': 'CHEBI:17234'},
                    'concentration': {'value': '20', 'unit': 'G_PER_L'}
                }
            ]
        }

        fp1 = self.fingerprinter.fingerprint(recipe1)
        fp2 = self.fingerprinter.fingerprint(recipe2)

        assert fp1 == fp2

    def test_fingerprint_without_chebi(self):
        """Test fingerprinting with normalized names (no CHEBI IDs)."""
        recipe = {
            'ingredients': [
                {'preferred_term': 'Glucose'},
                {'preferred_term': 'Sodium Chloride'}
            ]
        }

        fingerprint = self.fingerprinter.fingerprint(recipe)

        assert len(fingerprint) == 64

    def test_fingerprint_with_solutions(self):
        """Test fingerprinting includes solution compositions."""
        recipe = {
            'ingredients': [
                {'preferred_term': 'Glucose', 'term': {'id': 'CHEBI:17234'}}
            ],
            'solutions': [
                {
                    'preferred_term': 'Trace Metal Solution',
                    'composition': [
                        {'preferred_term': 'FeCl3', 'term': {'id': 'CHEBI:30808'}},
                        {'preferred_term': 'ZnCl2', 'term': {'id': 'CHEBI:49976'}}
                    ]
                }
            ]
        }

        fingerprint = self.fingerprinter.fingerprint(recipe)

        # Should include solution ingredients
        assert len(fingerprint) == 64

        # Verify it's different from recipe without solutions
        recipe_no_solution = {
            'ingredients': [
                {'preferred_term': 'Glucose', 'term': {'id': 'CHEBI:17234'}}
            ]
        }

        fp_no_solution = self.fingerprinter.fingerprint(recipe_no_solution)
        assert fingerprint != fp_no_solution

    def test_normalize_name(self):
        """Test name normalization."""
        # Test hydration removal
        assert self.fingerprinter._normalize_name('MgSO4·7H2O') == 'mgso4'
        assert self.fingerprinter._normalize_name('CaCl2.2H2O') == 'cacl2'
        assert self.fingerprinter._normalize_name('NaCl x 6H2O') == 'nacl'
        assert self.fingerprinter._normalize_name('FeSO4 x 7 H2O') == 'feso4'

        # Test lowercase
        assert self.fingerprinter._normalize_name('Glucose') == 'glucose'

        # Test whitespace
        assert self.fingerprinter._normalize_name('  NaCl  ') == 'nacl'
        assert self.fingerprinter._normalize_name('Na  Cl') == 'na cl'

    def test_fingerprint_empty_ingredients(self):
        """Test that fingerprinting raises error for empty ingredients."""
        recipe = {
            'name': 'Empty Recipe',
            'ingredients': []
        }

        with pytest.raises(ValueError, match="no ingredients"):
            self.fingerprinter.fingerprint(recipe)

    def test_extract_identifier_priority(self):
        """Test that CHEBI ID takes priority over name."""
        ingredient_with_chebi = {
            'preferred_term': 'Some Chemical',
            'term': {'id': 'CHEBI:12345', 'label': 'chemical'}
        }

        sig = self.fingerprinter._extract_identifier(ingredient_with_chebi)

        assert sig.identifier == 'CHEBI:12345'
        assert sig.source == 'chebi'

        # Without CHEBI ID
        ingredient_without_chebi = {
            'preferred_term': 'Some Chemical'
        }

        sig = self.fingerprinter._extract_identifier(ingredient_without_chebi)

        assert sig.identifier == 'some chemical'
        assert sig.source == 'name'

    def test_duplicate_ingredient_handling(self):
        """Test that duplicate ingredients are handled correctly."""
        recipe = {
            'ingredients': [
                {'preferred_term': 'Glucose', 'term': {'id': 'CHEBI:17234'}},
                {'preferred_term': 'Glucose', 'term': {'id': 'CHEBI:17234'}},
                {'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}
            ]
        }

        # Should use SET semantics (duplicates ignored)
        signatures = self.fingerprinter._extract_signatures(recipe)

        # Should only have 2 unique ingredients
        assert len(signatures) == 2

    def test_fingerprint_deterministic(self):
        """Test that fingerprinting is deterministic."""
        recipe = {
            'ingredients': [
                {'preferred_term': 'Glucose', 'term': {'id': 'CHEBI:17234'}},
                {'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}
            ]
        }

        fp1 = self.fingerprinter.fingerprint(recipe)
        fp2 = self.fingerprinter.fingerprint(recipe)
        fp3 = self.fingerprinter.fingerprint(recipe)

        assert fp1 == fp2 == fp3
