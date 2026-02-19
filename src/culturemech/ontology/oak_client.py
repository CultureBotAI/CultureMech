#!/usr/bin/env python3
"""
Ontology Access Kit (OAK) Client for Multi-Ontology Search

Provides unified interface to search across multiple ontologies (CHEBI, FOODON, NCBITaxon, etc.)
using the Ontology Access Kit library. Complements OLS client with comprehensive synonym matching
and multi-ontology support.

Depends on:
    oaklib>=0.5.0
"""

import logging
from pathlib import Path
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


@dataclass
class OAKResult:
    """Result from OAK search"""
    curie: str
    label: str
    matched_term: str  # The term that matched (label or synonym)
    is_exact_match: bool
    ontology: str


class OAKClient:
    """
    Ontology Access Kit client for multi-ontology search.

    Provides unified interface to CHEBI, FOODON, NCBITaxon, and other ontologies
    via OAK's adapter system.
    """

    # OLS-based ontology sources (requires network)
    OLS_SOURCES = {
        'chebi': 'sqlite:obo:chebi',
        'foodon': 'sqlite:obo:foodon',
        'ncbitaxon': 'sqlite:obo:ncbitaxon',
        'envo': 'sqlite:obo:envo',
    }

    def __init__(self, cache_dir: Optional[Path] = None):
        """
        Initialize OAK client.

        Args:
            cache_dir: Directory for caching ontology data (default: ~/.cache/culturemech/oak)
        """
        self.cache_dir = cache_dir or Path.home() / ".cache" / "culturemech" / "oak"
        self.cache_dir.mkdir(parents=True, exist_ok=True)

        self.adapters = {}
        self.stats = {
            'searches': 0,
            'exact_matches': 0,
            'synonym_matches': 0,
            'no_matches': 0,
            'errors': 0
        }

    def get_adapter(self, ontology: str):
        """
        Get or create adapter for ontology.

        Args:
            ontology: Ontology name (e.g., 'chebi', 'foodon')

        Returns:
            OAK adapter instance
        """
        if ontology not in self.adapters:
            try:
                from oaklib import get_adapter

                source = self.OLS_SOURCES.get(ontology)
                if not source:
                    logger.warning(f"Unknown ontology: {ontology}")
                    return None

                logger.debug(f"Creating OAK adapter for {ontology}: {source}")
                adapter = get_adapter(source)
                self.adapters[ontology] = adapter

            except Exception as e:
                logger.error(f"Failed to create OAK adapter for {ontology}: {e}")
                self.stats['errors'] += 1
                return None

        return self.adapters[ontology]

    def exact_search(
        self,
        query: str,
        ontology: str = "chebi"
    ) -> List[OAKResult]:
        """
        Exact label search using OAK.

        Args:
            query: Search term
            ontology: Ontology to search (default: chebi)

        Returns:
            List of OAKResult objects
        """
        self.stats['searches'] += 1
        adapter = self.get_adapter(ontology)
        if not adapter:
            return []

        try:
            results = []

            # Search for entities matching the query
            for curie in adapter.basic_search(query):
                label = adapter.label(curie)

                # Check if it's an exact match
                if label and label.lower() == query.lower():
                    results.append(OAKResult(
                        curie=curie,
                        label=label,
                        matched_term=label,
                        is_exact_match=True,
                        ontology=ontology
                    ))
                    self.stats['exact_matches'] += 1

            if not results:
                self.stats['no_matches'] += 1

            return results

        except Exception as e:
            logger.error(f"OAK exact search failed for '{query}' in {ontology}: {e}")
            self.stats['errors'] += 1
            return []

    def synonym_search(
        self,
        query: str,
        ontology: str = "chebi"
    ) -> List[OAKResult]:
        """
        Search including synonyms using OAK's entity_aliases interface.

        Args:
            query: Search term
            ontology: Ontology to search

        Returns:
            List of OAKResult objects with synonym matches
        """
        self.stats['searches'] += 1
        adapter = self.get_adapter(ontology)
        if not adapter:
            return []

        try:
            results = []
            query_lower = query.lower()

            # Search for terms
            for curie in adapter.basic_search(query):
                label = adapter.label(curie)

                # Check label first
                if label and label.lower() == query_lower:
                    results.append(OAKResult(
                        curie=curie,
                        label=label,
                        matched_term=label,
                        is_exact_match=True,
                        ontology=ontology
                    ))
                    self.stats['exact_matches'] += 1
                    continue

                # Check synonyms
                try:
                    synonyms = list(adapter.entity_aliases(curie))
                    for syn in synonyms:
                        if syn and syn.lower() == query_lower:
                            results.append(OAKResult(
                                curie=curie,
                                label=label or curie,
                                matched_term=syn,
                                is_exact_match=True,
                                ontology=ontology
                            ))
                            self.stats['synonym_matches'] += 1
                            break
                except Exception:
                    # entity_aliases may not be supported by all adapters
                    pass

            if not results:
                self.stats['no_matches'] += 1

            return results

        except Exception as e:
            logger.error(f"OAK synonym search failed for '{query}' in {ontology}: {e}")
            self.stats['errors'] += 1
            return []

    def multi_ontology_search(
        self,
        query: str,
        ontologies: Optional[List[str]] = None,
        include_synonyms: bool = True
    ) -> Dict[str, List[OAKResult]]:
        """
        Search across multiple ontologies.

        Args:
            query: Search term
            ontologies: List of ontology names (default: ['chebi', 'foodon'])
            include_synonyms: Include synonym matching (default: True)

        Returns:
            Dict mapping ontology name to list of results
        """
        if ontologies is None:
            ontologies = ['chebi', 'foodon']

        results = {}
        search_func = self.synonym_search if include_synonyms else self.exact_search

        for ontology in ontologies:
            try:
                results[ontology] = search_func(query, ontology)
            except Exception as e:
                logger.error(f"Search failed in {ontology}: {e}")
                results[ontology] = []

        return results

    def get_statistics(self) -> Dict:
        """Get client usage statistics."""
        return {
            **self.stats,
            'success_rate': (
                (self.stats['exact_matches'] + self.stats['synonym_matches']) /
                self.stats['searches']
                if self.stats['searches'] > 0
                else 0.0
            )
        }


def main():
    """CLI for testing OAK client."""
    import argparse

    parser = argparse.ArgumentParser(description="Test OAK client")
    parser.add_argument(
        '--search',
        type=str,
        help="Search for a term"
    )
    parser.add_argument(
        '--ontology',
        type=str,
        default='chebi',
        help="Ontology to search (default: chebi)"
    )
    parser.add_argument(
        '--synonyms',
        action='store_true',
        help="Include synonym search"
    )
    parser.add_argument(
        '--multi',
        action='store_true',
        help="Search across multiple ontologies"
    )
    parser.add_argument(
        '--stats',
        action='store_true',
        help="Show usage statistics"
    )

    args = parser.parse_args()

    # Initialize client
    client = OAKClient()

    if args.search:
        print(f"\nSearching for: {args.search}")
        print("=" * 70)

        if args.multi:
            results = client.multi_ontology_search(
                args.search,
                include_synonyms=args.synonyms
            )

            for ontology, ont_results in results.items():
                print(f"\n{ontology.upper()}:")
                if ont_results:
                    for result in ont_results:
                        print(f"  {result.curie}: {result.label}")
                        print(f"    Matched: {result.matched_term}")
                        print(f"    Exact: {result.is_exact_match}")
                else:
                    print("  No results")
        else:
            search_func = client.synonym_search if args.synonyms else client.exact_search
            results = search_func(args.search, args.ontology)

            if results:
                for result in results:
                    print(f"\n{result.curie}: {result.label}")
                    print(f"  Matched: {result.matched_term}")
                    print(f"  Exact: {result.is_exact_match}")
            else:
                print("No results found")

    if args.stats or not args.search:
        stats = client.get_statistics()
        print("\nOAK Client Statistics:")
        print("=" * 70)
        import json
        print(json.dumps(stats, indent=2))


if __name__ == "__main__":
    main()
