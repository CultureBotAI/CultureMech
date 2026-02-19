#!/usr/bin/env python3
"""
Unit tests for OLS API Client
"""

import unittest
from unittest.mock import Mock, patch, MagicMock
from pathlib import Path
import json
import tempfile

import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from culturemech.ontology.ols_client import OLSClient


class TestOLSClient(unittest.TestCase):
    """Test OLS API client functionality."""

    def setUp(self):
        """Set up test fixtures."""
        # Create temporary cache directory
        self.temp_dir = tempfile.mkdtemp()
        self.cache_dir = Path(self.temp_dir) / "ols_cache"

        # Initialize client with test cache
        self.client = OLSClient(
            cache_dir=self.cache_dir,
            rate_limit=0,  # Disable rate limiting for tests
            timeout=5
        )

    def tearDown(self):
        """Clean up test fixtures."""
        import shutil
        shutil.rmtree(self.temp_dir, ignore_errors=True)

    @patch('culturemech.ontology.ols_client.requests.get')
    def test_search_chebi(self, mock_get):
        """Test CHEBI search functionality."""
        # Mock API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'response': {
                'docs': [
                    {
                        'iri': 'http://purl.obolibrary.org/obo/CHEBI_15377',
                        'short_form': 'CHEBI:15377',
                        'label': 'water',
                        'description': ['An oxygen hydride...'],
                        'synonym': ['H2O', 'aqua'],
                        'score': 42.5
                    }
                ]
            }
        }
        mock_get.return_value = mock_response

        # Test search
        results = self.client.search_chebi('water', exact=True)

        # Assertions
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['chebi_id'], 'CHEBI:15377')
        self.assertEqual(results[0]['label'], 'water')
        self.assertIn('H2O', results[0]['synonyms'])

        # Verify API call
        mock_get.assert_called_once()
        call_args = mock_get.call_args
        self.assertIn('water', str(call_args))

    @patch('culturemech.ontology.ols_client.requests.get')
    def test_verify_chebi_id(self, mock_get):
        """Test CHEBI ID verification."""
        # Mock API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'iri': 'http://purl.obolibrary.org/obo/CHEBI_15377',
            'label': 'water',
            'description': ['An oxygen hydride consisting of two hydrogens...'],
            'synonyms': ['H2O', 'aqua', 'oxidane'],
            'annotation': {
                'formula': ['H2O'],
                'inchi': ['InChI=1S/H2O/h1H2']
            }
        }
        mock_get.return_value = mock_response

        # Test verification
        term = self.client.verify_chebi_id('CHEBI:15377')

        # Assertions
        self.assertIsNotNone(term)
        self.assertEqual(term['chebi_id'], 'CHEBI:15377')
        self.assertEqual(term['label'], 'water')
        self.assertEqual(term['formula'], 'H2O')
        self.assertIn('H2O', term['synonyms'])

    @patch('culturemech.ontology.ols_client.requests.get')
    def test_verify_invalid_chebi_id(self, mock_get):
        """Test verification of invalid CHEBI ID."""
        # Mock 404 response
        mock_response = Mock()
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = Exception("404 Not Found")
        mock_get.return_value = mock_response

        # Test verification
        term = self.client.verify_chebi_id('CHEBI:99999999')

        # Should return None for invalid ID
        self.assertIsNone(term)

    def test_cache_functionality(self):
        """Test response caching."""
        # Create mock response
        cache_key = "test_key"
        test_data = {'result': 'test_value'}

        # Save to cache
        self.client._save_to_cache(cache_key, test_data)

        # Retrieve from cache
        cached_data = self.client._get_from_cache(cache_key)

        # Assertions
        self.assertIsNotNone(cached_data)
        self.assertEqual(cached_data['result'], 'test_value')

        # Check statistics
        stats = self.client.get_statistics()
        self.assertEqual(stats['cache_hits'], 1)

    @patch('culturemech.ontology.ols_client.requests.get')
    def test_suggest_mapping(self, mock_get):
        """Test suggestion API."""
        # Mock API response
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'response': {
                'docs': [
                    {
                        'iri': 'http://purl.obolibrary.org/obo/CHEBI_17234',
                        'autosuggest': 'glucose'
                    }
                ]
            }
        }
        mock_get.return_value = mock_response

        # Test suggestions
        suggestions = self.client.suggest_mapping('glucose')

        # Assertions
        self.assertEqual(len(suggestions), 1)
        self.assertEqual(suggestions[0]['chebi_id'], 'CHEBI:17234')
        self.assertEqual(suggestions[0]['label'], 'glucose')

    def test_statistics_tracking(self):
        """Test statistics tracking."""
        initial_stats = self.client.get_statistics()

        # Simulate cache hit
        self.client._get_from_cache('nonexistent_key')

        # Simulate cache miss
        stats = self.client.get_statistics()
        self.assertEqual(stats['cache_misses'], 1)


class TestOLSClientIntegration(unittest.TestCase):
    """Integration tests with real OLS API (optional - requires network)."""

    @unittest.skip("Skip by default - requires network access")
    def test_real_api_search(self):
        """Test real API search (network required)."""
        client = OLSClient(rate_limit=1)

        # Search for water
        results = client.search_chebi('water', exact=True)

        # Should find water
        self.assertTrue(len(results) > 0)
        # First result should be water
        self.assertIn('water', results[0]['label'].lower())

    @unittest.skip("Skip by default - requires network access")
    def test_real_api_verification(self):
        """Test real API verification (network required)."""
        client = OLSClient(rate_limit=1)

        # Verify water CHEBI ID
        term = client.verify_chebi_id('CHEBI:15377')

        # Should return valid term
        self.assertIsNotNone(term)
        self.assertEqual(term['label'], 'water')
        self.assertEqual(term['formula'], 'H2O')


if __name__ == '__main__':
    unittest.main()
