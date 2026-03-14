"""Test MediaIngredientMech enrichment functionality."""

import tempfile
from pathlib import Path
import yaml

from culturemech.enrich.mediaingredientmech_loader import MediaIngredientMechLoader
from culturemech.enrich.mediaingredientmech_linker import MediaIngredientMechLinker


def test_mediaingredientmech_loader():
    """Test loading MediaIngredientMech data."""
    # Create a temporary directory with sample data
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir)

        # Create sample unmapped_ingredients.yaml
        sample_data = [
            {
                'id': 'MediaIngredientMech:000001',
                'name': 'Glucose',
                'chebi_id': 'CHEBI:17234',
                'synonyms': ['D-Glucose', 'Dextrose']
            },
            {
                'id': 'MediaIngredientMech:000002',
                'name': 'Yeast Extract',
                'synonyms': ['Yeast extract powder']
            },
            {
                'id': 'MediaIngredientMech:000003',
                'name': 'Sodium chloride',
                'chebi_id': 'CHEBI:26710',
                'synonyms': ['NaCl', 'Table salt']
            }
        ]

        yaml_file = repo_path / 'unmapped_ingredients.yaml'
        with open(yaml_file, 'w') as f:
            yaml.dump(sample_data, f)

        # Test loader
        loader = MediaIngredientMechLoader(repo_path=repo_path)

        assert len(loader.ingredients) == 3
        assert len(loader.by_chebi) == 2
        assert len(loader.by_name) == 3

        # Test matching
        match = loader.find_match('Glucose', 'CHEBI:17234')
        assert match is not None
        assert match['id'] == 'MediaIngredientMech:000001'
        assert match['match_method'] == 'chebi_id'

        match = loader.find_match('D-Glucose')
        assert match is not None
        assert match['id'] == 'MediaIngredientMech:000001'
        assert match['match_method'] == 'synonym'

        match = loader.find_match('NaCl')
        assert match is not None
        assert match['id'] == 'MediaIngredientMech:000003'
        assert match['match_method'] == 'synonym'


def test_mediaingredientmech_linker():
    """Test linking ingredients to MediaIngredientMech IDs."""
    # Create sample loader with test data
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir)

        sample_data = [
            {
                'id': 'MediaIngredientMech:000001',
                'name': 'Glucose',
                'chebi_id': 'CHEBI:17234',
                'synonyms': ['D-Glucose']
            }
        ]

        yaml_file = repo_path / 'unmapped_ingredients.yaml'
        with open(yaml_file, 'w') as f:
            yaml.dump(sample_data, f)

        loader = MediaIngredientMechLoader(repo_path=repo_path)
        linker = MediaIngredientMechLinker(loader)

        # Test enriching an ingredient
        ingredient = {
            'preferred_term': 'Glucose',
            'term': {
                'id': 'CHEBI:17234',
                'label': 'glucose'
            },
            'concentration': {
                'value': '10',
                'unit': 'G_PER_L'
            }
        }

        result = linker.enrich_ingredient(ingredient)

        assert result is True
        assert 'mediaingredientmech_term' in ingredient
        assert ingredient['mediaingredientmech_term']['id'] == 'MediaIngredientMech:000001'
        assert linker.stats['ingredients_matched'] == 1


def test_mediaingredientmech_linker_solution():
    """Test linking solution composition ingredients."""
    with tempfile.TemporaryDirectory() as tmpdir:
        repo_path = Path(tmpdir)

        sample_data = [
            {
                'id': 'MediaIngredientMech:000001',
                'name': 'Glucose',
                'chebi_id': 'CHEBI:17234'
            }
        ]

        yaml_file = repo_path / 'unmapped_ingredients.yaml'
        with open(yaml_file, 'w') as f:
            yaml.dump(sample_data, f)

        loader = MediaIngredientMechLoader(repo_path=repo_path)
        linker = MediaIngredientMechLinker(loader)

        # Test enriching a solution with composition
        solution = {
            'preferred_term': 'Sugar Solution',
            'composition': [
                {
                    'preferred_term': 'Glucose',
                    'term': {
                        'id': 'CHEBI:17234',
                        'label': 'glucose'
                    },
                    'concentration': {
                        'value': '100',
                        'unit': 'G_PER_L'
                    }
                }
            ]
        }

        matched = linker.enrich_solution(solution)

        assert matched == 1
        assert 'mediaingredientmech_term' in solution['composition'][0]
        assert solution['composition'][0]['mediaingredientmech_term']['id'] == 'MediaIngredientMech:000001'


if __name__ == '__main__':
    test_mediaingredientmech_loader()
    print("✓ Loader tests passed")

    test_mediaingredientmech_linker()
    print("✓ Linker ingredient tests passed")

    test_mediaingredientmech_linker_solution()
    print("✓ Linker solution tests passed")

    print("\nAll tests passed!")
