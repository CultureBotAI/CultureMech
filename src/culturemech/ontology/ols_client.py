#!/usr/bin/env python3
"""
EBI Ontology Lookup Service (OLS) API Client

Provides access to the EBI OLS API for CHEBI term lookup, verification, and search.
Includes caching and rate limiting for efficient API usage.

API Documentation: https://www.ebi.ac.uk/ols/docs/api
"""

import logging
import time
import json
import hashlib
from pathlib import Path
from typing import List, Dict, Optional
from urllib.parse import quote

import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class OLSClient:
    """Client for EBI Ontology Lookup Service API v4."""

    # Try OLS4 first, fallback to OLS3
    BASE_URLS = [
        "https://www.ebi.ac.uk/ols4/api",
        "https://www.ebi.ac.uk/ols/api"
    ]
    DEFAULT_CACHE_DIR = Path.home() / ".cache" / "culturemech" / "ols"

    def __init__(
        self,
        cache_dir: Optional[Path] = None,
        rate_limit: float = 5.0,
        timeout: int = 10
    ):
        """
        Initialize OLS client.

        Args:
            cache_dir: Directory for caching API responses (default: ~/.cache/culturemech/ols)
            rate_limit: Maximum requests per second (default: 5.0)
            timeout: Request timeout in seconds (default: 10)
        """
        self.cache_dir = cache_dir or self.DEFAULT_CACHE_DIR
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        self.rate_limit = rate_limit
        self.timeout = timeout
        self._last_request_time = 0

        # Try to detect which OLS version is available
        self.base_url = self._detect_ols_version()

        self.stats = {
            'requests': 0,
            'cache_hits': 0,
            'cache_misses': 0,
            'errors': 0,
            'invalid_ids': 0
        }

    def _detect_ols_version(self) -> str:
        """Detect which OLS API version is available."""
        for base_url in self.BASE_URLS:
            try:
                response = requests.get(f"{base_url}/ontologies/chebi", timeout=5)
                if response.status_code == 200:
                    logger.info(f"Using OLS API at {base_url}")
                    return base_url
            except Exception:
                continue

        # Default to OLS4 if detection fails
        logger.warning("Could not detect OLS version, defaulting to OLS4")
        return self.BASE_URLS[0]

    def _rate_limit_wait(self):
        """Enforce rate limiting between requests."""
        if self.rate_limit <= 0:
            return

        elapsed = time.time() - self._last_request_time
        min_interval = 1.0 / self.rate_limit

        if elapsed < min_interval:
            time.sleep(min_interval - elapsed)

        self._last_request_time = time.time()

    def _get_cache_path(self, cache_key: str) -> Path:
        """Get cache file path for a given key."""
        # Use hash to avoid filesystem issues with long URLs
        key_hash = hashlib.sha256(cache_key.encode()).hexdigest()
        return self.cache_dir / f"{key_hash}.json"

    def _get_from_cache(self, cache_key: str) -> Optional[Dict]:
        """Retrieve cached response if available."""
        cache_path = self._get_cache_path(cache_key)

        if cache_path.exists():
            try:
                with open(cache_path) as f:
                    self.stats['cache_hits'] += 1
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Cache read error: {e}")
                return None

        self.stats['cache_misses'] += 1
        return None

    def _save_to_cache(self, cache_key: str, data: Dict):
        """Save response to cache."""
        cache_path = self._get_cache_path(cache_key)

        try:
            with open(cache_path, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            logger.warning(f"Cache write error: {e}")

    def _make_request(self, url: str, params: Optional[Dict] = None, use_cache: bool = True) -> Optional[Dict]:
        """
        Make HTTP GET request to OLS API with caching and rate limiting.

        Args:
            url: API endpoint URL
            params: Query parameters
            use_cache: Whether to use cached responses

        Returns:
            Response JSON or None on error
        """
        # Generate cache key
        cache_key = f"{url}?{json.dumps(params, sort_keys=True)}" if params else url

        # Check cache first
        if use_cache:
            cached = self._get_from_cache(cache_key)
            if cached is not None:
                return cached

        # Rate limit
        self._rate_limit_wait()

        # Make request
        try:
            self.stats['requests'] += 1
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()

            data = response.json()

            # Cache successful response
            if use_cache:
                self._save_to_cache(cache_key, data)

            return data

        except requests.exceptions.HTTPError as e:
            self.stats['errors'] += 1
            if e.response.status_code == 404:
                # 404 is expected for invalid/deprecated IDs
                logger.debug(f"OLS API 404 (not found): {url}")
            else:
                logger.error(f"OLS API HTTP error: {e}")
            return None
        except requests.exceptions.RequestException as e:
            self.stats['errors'] += 1
            logger.error(f"OLS API request failed: {e}")
            return None

    def search_chebi(
        self,
        query: str,
        exact: bool = False,
        rows: int = 10
    ) -> List[Dict]:
        """
        Search CHEBI for matching terms.

        Args:
            query: Ingredient name to search
            exact: Require exact match (default: fuzzy search)
            rows: Maximum number of results to return

        Returns:
            List of matching terms with metadata:
            [
                {
                    'chebi_id': 'CHEBI:15377',
                    'label': 'water',
                    'iri': 'http://purl.obolibrary.org/obo/CHEBI_15377',
                    'description': 'An oxygen hydride...',
                    'synonyms': ['H2O', 'aqua', ...],
                    'score': 42.5
                },
                ...
            ]
        """
        params = {
            'q': query,
            'ontology': 'chebi',
            'exact': str(exact).lower(),
            'rows': rows,
            'fieldList': 'iri,label,short_form,description,synonym,score'
        }

        url = f"{self.base_url}/search"
        response = self._make_request(url, params)

        if not response:
            return []

        return self._parse_search_results(response)

    def _parse_search_results(self, response: Dict) -> List[Dict]:
        """Parse OLS search response into simplified term list."""
        docs = response.get('response', {}).get('docs', [])
        results = []

        for doc in docs:
            iri = doc.get('iri', '')
            short_form = doc.get('short_form', '')

            # Extract CHEBI ID from IRI or short_form
            chebi_id = None
            if 'CHEBI_' in iri:
                chebi_id = iri.split('CHEBI_')[-1]
                chebi_id = f"CHEBI:{chebi_id}"
            elif short_form:
                chebi_id = short_form

            if not chebi_id:
                continue

            results.append({
                'chebi_id': chebi_id,
                'label': doc.get('label', ''),
                'iri': iri,
                'description': doc.get('description', [''])[0] if doc.get('description') else '',
                'synonyms': doc.get('synonym', []),
                'score': doc.get('score', 0.0)
            })

        return results

    def verify_chebi_id(self, chebi_id: str) -> Optional[Dict]:
        """
        Verify a CHEBI ID exists and retrieve metadata.

        Args:
            chebi_id: CHEBI CURIE (e.g., "CHEBI:15377")

        Returns:
            Term metadata or None if not found:
            {
                'chebi_id': 'CHEBI:15377',
                'label': 'water',
                'iri': 'http://purl.obolibrary.org/obo/CHEBI_15377',
                'description': 'An oxygen hydride...',
                'synonyms': ['H2O', 'aqua', ...],
                'formula': 'H2O',
                'inchi': 'InChI=1S/H2O/h1H2'
            }
        """
        # Validate CHEBI ID format
        if not chebi_id.startswith('CHEBI:'):
            logger.warning(f"Invalid CHEBI ID format: {chebi_id}")
            self.stats['invalid_ids'] += 1
            return None

        # Extract numeric part
        chebi_number = chebi_id.split(':')[1]

        # Validate CHEBI number (should be 1-7 digits, rarely more than 6)
        try:
            num = int(chebi_number)
            if num <= 0 or num > 99999999:  # Sanity check
                logger.warning(f"Invalid CHEBI number (out of range): {chebi_id}")
                self.stats['invalid_ids'] += 1
                return None
            if num > 9999999:  # 8+ digits is suspicious
                logger.warning(f"Suspicious CHEBI number (very large): {chebi_id}")
                # Continue anyway, but log it
        except ValueError:
            logger.warning(f"Invalid CHEBI number (not numeric): {chebi_id}")
            self.stats['invalid_ids'] += 1
            return None

        # Convert CURIE to IRI
        iri = f"http://purl.obolibrary.org/obo/CHEBI_{chebi_number}"

        # URL-encode IRI (double encode for OLS)
        encoded_iri = quote(quote(iri, safe=''), safe='')

        url = f"{self.base_url}/ontologies/chebi/terms/{encoded_iri}"
        response = self._make_request(url)

        if not response:
            return None

        return self._parse_term_metadata(response, chebi_id)

    def _parse_term_metadata(self, response: Dict, chebi_id: str) -> Dict:
        """Parse OLS term response into simplified metadata."""
        label = response.get('label', '')
        iri = response.get('iri', '')
        description = response.get('description', [''])[0] if response.get('description') else ''

        # Extract synonyms
        synonyms = []
        if 'synonyms' in response:
            synonyms = response['synonyms']
        elif 'obo_synonym' in response.get('annotation', {}):
            synonyms = response['annotation']['obo_synonym']

        # Extract chemical properties from annotations
        annotation = response.get('annotation', {})
        formula = None
        inchi = None

        if 'formula' in annotation:
            formula = annotation['formula'][0] if annotation['formula'] else None
        if 'inchi' in annotation:
            inchi = annotation['inchi'][0] if annotation['inchi'] else None

        return {
            'chebi_id': chebi_id,
            'label': label,
            'iri': iri,
            'description': description,
            'synonyms': synonyms if isinstance(synonyms, list) else [synonyms] if synonyms else [],
            'formula': formula,
            'inchi': inchi
        }

    def suggest_mapping(self, ingredient_name: str) -> List[Dict]:
        """
        Get CHEBI suggestions for an ingredient name using OLS suggest API.

        Args:
            ingredient_name: Ingredient name to get suggestions for

        Returns:
            List of suggestions with labels and IRIs
        """
        params = {
            'q': ingredient_name,
            'ontology': 'chebi'
        }

        url = f"{self.base_url}/suggest"
        response = self._make_request(url, params)

        if not response:
            return []

        suggestions = []
        docs = response.get('response', {}).get('docs', [])

        for doc in docs:
            iri = doc.get('iri', '')
            if 'CHEBI_' in iri:
                chebi_id = iri.split('CHEBI_')[-1]
                chebi_id = f"CHEBI:{chebi_id}"

                suggestions.append({
                    'chebi_id': chebi_id,
                    'label': doc.get('autosuggest', ''),
                    'iri': iri
                })

        return suggestions

    def get_statistics(self) -> Dict:
        """Get client usage statistics."""
        return {
            **self.stats,
            'cache_hit_rate': (
                self.stats['cache_hits'] /
                (self.stats['cache_hits'] + self.stats['cache_misses'])
                if (self.stats['cache_hits'] + self.stats['cache_misses']) > 0
                else 0.0
            )
        }


def main():
    """CLI for testing OLS client."""
    import argparse

    parser = argparse.ArgumentParser(description="Test EBI OLS API client")
    parser.add_argument(
        '--search',
        type=str,
        help="Search CHEBI for ingredient name"
    )
    parser.add_argument(
        '--verify',
        type=str,
        help="Verify a CHEBI ID (e.g., CHEBI:15377)"
    )
    parser.add_argument(
        '--suggest',
        type=str,
        help="Get suggestions for ingredient name"
    )
    parser.add_argument(
        '--exact',
        action='store_true',
        help="Use exact matching (for search)"
    )
    parser.add_argument(
        '--no-cache',
        action='store_true',
        help="Disable caching"
    )
    parser.add_argument(
        '--stats',
        action='store_true',
        help="Show usage statistics"
    )

    args = parser.parse_args()

    # Initialize client
    client = OLSClient()

    if args.search:
        print(f"\nSearching CHEBI for: {args.search}")
        print("=" * 70)
        results = client.search_chebi(args.search, exact=args.exact)

        if results:
            for i, result in enumerate(results, 1):
                print(f"\n{i}. {result['label']} ({result['chebi_id']})")
                print(f"   Score: {result['score']:.2f}")
                if result['description']:
                    print(f"   Description: {result['description'][:100]}...")
                if result['synonyms']:
                    print(f"   Synonyms: {', '.join(result['synonyms'][:5])}")
        else:
            print("No results found")

    elif args.verify:
        print(f"\nVerifying CHEBI ID: {args.verify}")
        print("=" * 70)
        term = client.verify_chebi_id(args.verify)

        if term:
            print(f"\nLabel: {term['label']}")
            print(f"CHEBI ID: {term['chebi_id']}")
            print(f"IRI: {term['iri']}")
            if term['description']:
                print(f"Description: {term['description']}")
            if term['formula']:
                print(f"Formula: {term['formula']}")
            if term['synonyms']:
                print(f"Synonyms: {', '.join(term['synonyms'][:10])}")
        else:
            print("CHEBI ID not found or invalid")

    elif args.suggest:
        print(f"\nGetting suggestions for: {args.suggest}")
        print("=" * 70)
        suggestions = client.suggest_mapping(args.suggest)

        if suggestions:
            for i, sugg in enumerate(suggestions, 1):
                print(f"{i}. {sugg['label']} ({sugg['chebi_id']})")
        else:
            print("No suggestions found")

    if args.stats or not (args.search or args.verify or args.suggest):
        stats = client.get_statistics()
        print("\nOLS Client Statistics:")
        print("=" * 70)
        print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
