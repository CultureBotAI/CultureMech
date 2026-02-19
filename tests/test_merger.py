"""Unit tests for recipe merging."""

import tempfile
from pathlib import Path

import pytest
import yaml

from culturemech.merge.merger import RecipeMerger


class TestRecipeMerger:
    """Test RecipeMerger class."""

    def setup_method(self):
        """Set up test fixtures."""
        self.merger = RecipeMerger()
        self.temp_dir = tempfile.mkdtemp()

    def create_temp_recipe(self, recipe_dict: dict, filename: str) -> Path:
        """Create a temporary recipe file.

        Args:
            recipe_dict: Recipe dictionary
            filename: Filename (with .yaml extension)

        Returns:
            Path to created file
        """
        path = Path(self.temp_dir) / filename
        with open(path, 'w', encoding='utf-8') as f:
            yaml.dump(recipe_dict, f)
        return path

    def test_merge_single_recipe(self):
        """Test merging a single recipe (no duplicates)."""
        recipe = {
            'name': 'LB Medium',
            'category': 'bacterial',
            'medium_type': 'COMPLEX',
            'physical_state': 'LIQUID',
            'ingredients': [
                {'preferred_term': 'Tryptone', 'term': {'id': 'CHEBI:36316'}},
                {'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}
            ],
            'media_term': {
                'term': {'id': 'TOGO:M001', 'label': 'LB Medium'}
            }
        }

        path = self.create_temp_recipe(recipe, 'LB_Medium.yaml')
        merged = self.merger.merge_group([path])

        # Should preserve recipe
        assert merged['name'] == 'LB Medium'
        assert 'merge_fingerprint' in merged
        assert merged['merged_from'] == ['LB_Medium']

    def test_merge_duplicate_recipes(self):
        """Test merging duplicate recipes."""
        recipe1 = {
            'name': 'LB Medium',
            'category': 'bacterial',
            'medium_type': 'COMPLEX',
            'physical_state': 'LIQUID',
            'ingredients': [
                {'preferred_term': 'Tryptone', 'term': {'id': 'CHEBI:36316'}},
                {'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}
            ],
            'media_term': {
                'term': {'id': 'TOGO:M001', 'label': 'LB Medium'}
            }
        }

        recipe2 = {
            'name': 'LB Broth',
            'category': 'bacterial',
            'medium_type': 'COMPLEX',
            'physical_state': 'LIQUID',
            'ingredients': [
                {'preferred_term': 'Tryptone', 'term': {'id': 'CHEBI:36316'}},
                {'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}
            ],
            'media_term': {
                'term': {'id': 'mediadive.medium:123', 'label': 'LB Broth'}
            }
        }

        path1 = self.create_temp_recipe(recipe1, 'TOGO_M001_LB_Medium.yaml')
        path2 = self.create_temp_recipe(recipe2, 'MediaDive_123_LB_Broth.yaml')

        merged = self.merger.merge_group([path1, path2])

        # Should have merged fields
        assert 'synonyms' in merged
        assert len(merged['synonyms']) == 1
        assert merged['merged_from'] == ['TOGO_M001_LB_Medium', 'MediaDive_123_LB_Broth']
        assert 'merge_fingerprint' in merged

    def test_canonical_name_selection_by_frequency(self):
        """Test canonical name is selected by frequency."""
        recipe1 = {'name': 'LB Medium', 'ingredients': [{'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}]}
        recipe2 = {'name': 'LB Medium', 'ingredients': [{'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}]}
        recipe3 = {'name': 'LB Broth', 'ingredients': [{'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}]}

        path1 = self.create_temp_recipe(recipe1, 'recipe1.yaml')
        path2 = self.create_temp_recipe(recipe2, 'recipe2.yaml')
        path3 = self.create_temp_recipe(recipe3, 'recipe3.yaml')

        merged = self.merger.merge_group([path1, path2, path3])

        # 'LB Medium' appears 2x, 'LB Broth' 1x
        assert merged['name'] == 'LB Medium'

    def test_canonical_name_selection_by_source_priority(self):
        """Test canonical name tie-breaking by source priority."""
        recipe_togo = {
            'name': 'Medium A',
            'ingredients': [{'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}],
            'media_term': {'term': {'id': 'TOGO:M001', 'label': 'Medium A'}}
        }

        recipe_mediadive = {
            'name': 'Medium B',
            'ingredients': [{'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}],
            'media_term': {'term': {'id': 'mediadive.medium:123', 'label': 'Medium B'}}
        }

        path1 = self.create_temp_recipe(recipe_togo, 'togo.yaml')
        path2 = self.create_temp_recipe(recipe_mediadive, 'mediadive.yaml')

        merged = self.merger.merge_group([path1, path2])

        # TOGO has higher priority than MediaDive
        assert merged['name'] == 'Medium A'

    def test_synonym_building(self):
        """Test synonym list construction."""
        recipe1 = {
            'name': 'LB Medium',
            'category': 'bacterial',
            'ingredients': [{'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}],
            'media_term': {'term': {'id': 'TOGO:M001', 'label': 'LB Medium'}}
        }

        recipe2 = {
            'name': 'LB Broth',
            'category': 'specialized',
            'ingredients': [{'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}],
            'media_term': {'term': {'id': 'mediadive.medium:123', 'label': 'LB Broth'}}
        }

        path1 = self.create_temp_recipe(recipe1, 'togo.yaml')
        path2 = self.create_temp_recipe(recipe2, 'mediadive.yaml')

        merged = self.merger.merge_group([path1, path2])

        # Check synonyms
        assert 'synonyms' in merged
        synonyms = merged['synonyms']

        # Should have 1 synonym (non-canonical name)
        assert len(synonyms) == 1

        # Check synonym structure
        synonym = synonyms[0]
        assert 'name' in synonym
        assert 'source' in synonym
        assert 'source_id' in synonym
        assert 'original_category' in synonym

    def test_category_merging(self):
        """Test categories are merged from multiple recipes."""
        recipe1 = {
            'name': 'LB Medium',
            'category': 'bacterial',
            'ingredients': [{'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}]
        }

        recipe2 = {
            'name': 'LB Medium',
            'category': 'specialized',
            'ingredients': [{'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}]
        }

        path1 = self.create_temp_recipe(recipe1, 'recipe1.yaml')
        path2 = self.create_temp_recipe(recipe2, 'recipe2.yaml')

        merged = self.merger.merge_group([path1, path2])

        # Should have both categories
        assert 'categories' in merged
        categories = merged['categories']
        assert set(categories) == {'bacterial', 'specialized'}

    def test_curation_history_added(self):
        """Test curation history entry is added."""
        recipe1 = {
            'name': 'LB Medium',
            'ingredients': [{'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}],
            'curation_history': [
                {'timestamp': '2024-01-01T00:00:00Z', 'curator': 'togo-import', 'action': 'Imported'}
            ]
        }

        recipe2 = {
            'name': 'LB Broth',
            'ingredients': [{'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710'}}]
        }

        path1 = self.create_temp_recipe(recipe1, 'recipe1.yaml')
        path2 = self.create_temp_recipe(recipe2, 'recipe2.yaml')

        merged = self.merger.merge_group([path1, path2])

        # Should have curation history
        assert 'curation_history' in merged
        history = merged['curation_history']

        # Should have original entry plus merge entry
        assert len(history) >= 1

        # Last entry should be merge
        merge_entry = history[-1]
        assert merge_entry['curator'] == 'recipe-merger'
        assert 'Merged' in merge_entry['action']

    def test_most_complete_ingredients(self):
        """Test that most complete ingredient annotations are used."""
        # Recipe with minimal annotations
        recipe1 = {
            'name': 'LB Medium',
            'ingredients': [
                {'preferred_term': 'Glucose'},
                {'preferred_term': 'NaCl'}
            ]
        }

        # Recipe with CHEBI IDs
        recipe2 = {
            'name': 'LB Medium',
            'ingredients': [
                {'preferred_term': 'Glucose', 'term': {'id': 'CHEBI:17234', 'label': 'glucose'}},
                {'preferred_term': 'NaCl', 'term': {'id': 'CHEBI:26710', 'label': 'sodium chloride'}}
            ]
        }

        path1 = self.create_temp_recipe(recipe1, 'recipe1.yaml')
        path2 = self.create_temp_recipe(recipe2, 'recipe2.yaml')

        merged = self.merger.merge_group([path1, path2])

        # Should use recipe2's ingredients (more complete)
        assert len(merged['ingredients']) == 2
        for ingredient in merged['ingredients']:
            assert 'term' in ingredient
            assert 'id' in ingredient['term']
            assert ingredient['term']['id'].startswith('CHEBI:')

    def test_extract_source(self):
        """Test source extraction from media_term."""
        recipe_togo = {
            'media_term': {'term': {'id': 'TOGO:M001', 'label': 'Test'}}
        }
        assert self.merger._extract_source(recipe_togo) == 'TOGO'

        recipe_mediadive = {
            'media_term': {'term': {'id': 'mediadive.medium:123', 'label': 'Test'}}
        }
        assert self.merger._extract_source(recipe_mediadive) == 'MediaDive'

        recipe_unknown = {
            'media_term': {'term': {'id': 'OTHER:123', 'label': 'Test'}}
        }
        assert self.merger._extract_source(recipe_unknown) == 'unknown'

    def test_merge_empty_list(self):
        """Test merging empty list raises error."""
        with pytest.raises(ValueError, match="empty recipe list"):
            self.merger.merge_group([])
