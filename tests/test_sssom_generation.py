#!/usr/bin/env python3
"""
Integration tests for SSSOM pipeline
"""

import unittest
import tempfile
import yaml
from pathlib import Path
import pandas as pd

import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.extract_unique_ingredients import extract_unique_ingredients, extract_source_from_path
from scripts.generate_sssom_mappings import generate_sssom_mappings, create_curie, validate_sssom_format


class TestIngredientExtraction(unittest.TestCase):
    """Test ingredient extraction functionality."""

    def setUp(self):
        """Create temporary directory with test YAML files."""
        self.temp_dir = tempfile.mkdtemp()
        self.yaml_dir = Path(self.temp_dir) / "normalized_yaml" / "bacterial"
        self.yaml_dir.mkdir(parents=True)

        # Create test recipe
        test_recipe = {
            'name': 'Test Medium',
            'category': 'bacterial',
            'medium_type': 'DEFINED',
            'physical_state': 'LIQUID',
            'ingredients': [
                {
                    'preferred_term': 'Glucose',
                    'term': {
                        'id': 'CHEBI:17234',
                        'label': 'D-glucose'
                    },
                    'concentration': {'value': '10', 'unit': 'G_PER_L'}
                },
                {
                    'preferred_term': 'Yeast extract',
                    'concentration': {'value': '5', 'unit': 'G_PER_L'}
                }
            ],
            'solutions': [
                {
                    'preferred_term': 'Vitamin Solution',
                    'composition': [
                        {
                            'preferred_term': 'Thiamine',
                            'term': {
                                'id': 'CHEBI:18385',
                                'label': 'thiamine'
                            },
                            'concentration': {'value': '1', 'unit': 'MG_PER_L'}
                        }
                    ]
                }
            ]
        }

        # Save test recipe
        yaml_file = self.yaml_dir / "TOGO_M1234_Test_Medium.yaml"
        with open(yaml_file, 'w') as f:
            yaml.dump(test_recipe, f)

    def tearDown(self):
        """Clean up temporary directory."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    def test_extract_source_from_path(self):
        """Test source extraction from file path."""
        test_path = Path("/data/normalized_yaml/bacterial/TOGO_M1234_Test.yaml")
        source = extract_source_from_path(test_path)
        self.assertEqual(source, "TOGO")

        test_path2 = Path("/data/normalized_yaml/bacterial/KOMODO_1-123_Test.yaml")
        source2 = extract_source_from_path(test_path2)
        self.assertEqual(source2, "KOMODO")

    def test_ingredient_extraction(self):
        """Test extraction of unique ingredients."""
        data_dirs = [self.yaml_dir.parent.parent]  # Point to normalized_yaml
        df = extract_unique_ingredients(data_dirs, verbose=False)

        # Should find 3 ingredients
        self.assertEqual(len(df), 3)

        # Check ingredient names
        ingredient_names = set(df['ingredient_name'].values)
        self.assertIn('Glucose', ingredient_names)
        self.assertIn('Yeast extract', ingredient_names)
        self.assertIn('Thiamine', ingredient_names)

        # Check CHEBI mappings
        glucose_row = df[df['ingredient_name'] == 'Glucose'].iloc[0]
        self.assertTrue(glucose_row['has_chebi_mapping'])
        self.assertEqual(glucose_row['chebi_id'], 'CHEBI:17234')

        yeast_row = df[df['ingredient_name'] == 'Yeast extract'].iloc[0]
        self.assertFalse(yeast_row['has_chebi_mapping'])

        # Check frequency
        self.assertEqual(glucose_row['frequency'], 1)


class TestSSSOMGeneration(unittest.TestCase):
    """Test SSSOM mapping generation."""

    def test_create_curie(self):
        """Test CURIE creation from ingredient names."""
        # Simple name
        curie = create_curie("Glucose")
        self.assertEqual(curie, "culturemech:Glucose")

        # Name with spaces
        curie = create_curie("Yeast extract")
        self.assertEqual(curie, "culturemech:Yeast_extract")

        # Name with special characters
        curie = create_curie("D-Glucose (anhydrous)")
        self.assertEqual(curie, "culturemech:D-Glucose_anhydrous_")

    def test_validate_sssom_format(self):
        """Test SSSOM format validation."""
        # Valid DataFrame
        valid_df = pd.DataFrame([
            {
                'subject_id': 'culturemech:Glucose',
                'subject_label': 'Glucose',
                'predicate_id': 'skos:exactMatch',
                'object_id': 'CHEBI:17234',
                'object_label': 'D-glucose',
                'mapping_justification': 'semapv:ManualMappingCuration',
                'confidence': 0.95
            }
        ])

        self.assertTrue(validate_sssom_format(valid_df))

        # Missing required column
        invalid_df = pd.DataFrame([
            {
                'subject_id': 'culturemech:Glucose',
                'object_id': 'CHEBI:17234'
            }
        ])

        self.assertFalse(validate_sssom_format(invalid_df))

    def test_sssom_generation(self):
        """Test SSSOM generation from YAML files."""
        # Create temporary directory with test files
        temp_dir = tempfile.mkdtemp()
        yaml_dir = Path(temp_dir) / "normalized_yaml" / "bacterial"
        yaml_dir.mkdir(parents=True)

        # Create test recipe with CHEBI terms
        test_recipe = {
            'name': 'Test Medium',
            'category': 'bacterial',
            'medium_type': 'DEFINED',
            'physical_state': 'LIQUID',
            'ingredients': [
                {
                    'preferred_term': 'Glucose',
                    'term': {
                        'id': 'CHEBI:17234',
                        'label': 'D-glucose'
                    },
                    'concentration': {'value': '10', 'unit': 'G_PER_L'}
                }
            ],
            'curation_history': [
                {
                    'curator': 'chebi-enrichment',
                    'notes': 'Enriched using MicrobeMediaParam'
                }
            ]
        }

        yaml_file = yaml_dir / "TEST_001_Medium.yaml"
        with open(yaml_file, 'w') as f:
            yaml.dump(test_recipe, f)

        # Generate SSSOM mappings
        df = generate_sssom_mappings(yaml_dir.parent, verbose=False)

        # Should have 1 mapping
        self.assertEqual(len(df), 1)

        # Check mapping content
        mapping = df.iloc[0]
        self.assertEqual(mapping['subject_label'], 'Glucose')
        self.assertEqual(mapping['object_id'], 'CHEBI:17234')
        self.assertEqual(mapping['predicate_id'], 'skos:exactMatch')
        self.assertEqual(mapping['mapping_tool'], 'MicrobeMediaParam|v1.0')

        # Validate format
        self.assertTrue(validate_sssom_format(df))

        # Clean up
        import shutil
        shutil.rmtree(temp_dir, ignore_errors=True)


if __name__ == '__main__':
    unittest.main()
