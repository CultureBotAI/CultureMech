"""
Media vector aggregator using YAML as source of truth.

Extracts CHEBI terms from enriched YAML files with fallback to KG mappings.
"""

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import yaml
from tqdm import tqdm


@dataclass
class MediaEmbedding:
    """Container for media embedding with metadata."""

    medium_id: str
    embedding: np.ndarray
    coverage: float  # Fraction of components with embeddings
    num_ingredients: int
    num_organisms: int
    source: str  # 'derived' or 'direct'


class MediaVectorAggregatorYAML:
    """
    Aggregate node embeddings into media-level embeddings.

    Uses YAML composition as primary source, with KG fallback.
    """

    def __init__(
        self,
        embeddings_dict: Dict[str, np.ndarray],
        solution_mapping_path: Optional[Path] = None,
        name_mapping_path: Optional[Path] = None
    ):
        """
        Initialize aggregator with embeddings dictionary.

        Args:
            embeddings_dict: Dictionary mapping node IDs to embedding vectors
            solution_mapping_path: Path to solution→CHEBI mapping JSON (KG fallback)
            name_mapping_path: Path to chemical name→CHEBI mapping JSON (name fallback)
        """
        self.embeddings = embeddings_dict

        # Load KG fallback mappings
        self.solution_to_chebi = {}
        if solution_mapping_path and solution_mapping_path.exists():
            with open(solution_mapping_path) as f:
                self.solution_to_chebi = json.load(f)
            print(f"✓ Loaded {len(self.solution_to_chebi)} solution→CHEBI mappings (KG fallback)")
        elif Path("data/solution_to_chebi_mapping.json").exists():
            with open("data/solution_to_chebi_mapping.json") as f:
                self.solution_to_chebi = json.load(f)
            print(f"✓ Loaded {len(self.solution_to_chebi)} solution→CHEBI mappings (KG fallback, default path)")

        # Load name-based fallback
        self.name_to_chebi = {}
        if name_mapping_path and name_mapping_path.exists():
            with open(name_mapping_path) as f:
                self.name_to_chebi = json.load(f)
            print(f"✓ Loaded {len(self.name_to_chebi)} name→CHEBI mappings (name fallback)")

    def aggregate_derived_embeddings(
        self, media_yamls: List[Path], min_coverage: float = 0.5
    ) -> Dict[str, MediaEmbedding]:
        """
        Aggregate derived media embeddings from YAML composition.

        Extraction priority:
        1. chebi_term.id from YAML (enriched)
        2. term.id from YAML if CHEBI
        3. name→CHEBI fallback mapping
        4. solution→CHEBI KG fallback (for solutions only)

        Args:
            media_yamls: List of paths to media/solution YAML files
            min_coverage: Minimum coverage threshold (0-1) to include medium

        Returns:
            Dictionary mapping medium names to MediaEmbedding objects
        """
        media_embeddings = {}
        extraction_stats = {
            'yaml_chebi_term': 0,
            'yaml_term_chebi': 0,
            'name_fallback': 0,
            'kg_fallback': 0,
            'not_found': 0
        }

        for yaml_path in tqdm(media_yamls, desc="Aggregating derived embeddings"):
            try:
                with open(yaml_path, "r") as f:
                    media_data = yaml.safe_load(f)

                if not media_data:
                    continue

                # Extract components using YAML-first approach
                ingredient_ids, stats = self._extract_ingredient_ids_yaml_source(media_data)
                organism_ids = self._extract_organism_ids(media_data)

                # Update extraction stats
                for key in stats:
                    extraction_stats[key] = extraction_stats.get(key, 0) + stats[key]

                # Aggregate embeddings
                embedding, coverage = self._aggregate_components(
                    ingredient_ids, organism_ids, ingredient_weight=0.6, organism_weight=0.4
                )

                # Skip if coverage too low
                if coverage < min_coverage or embedding is None:
                    continue

                medium_name = yaml_path.stem
                media_embeddings[medium_name] = MediaEmbedding(
                    medium_id=medium_name,
                    embedding=embedding,
                    coverage=coverage,
                    num_ingredients=len(ingredient_ids),
                    num_organisms=len(organism_ids),
                    source="derived",
                )

            except Exception as e:
                print(f"⚠ Error processing {yaml_path.name}: {e}")
                continue

        print(f"✓ Aggregated {len(media_embeddings):,} derived media embeddings")
        print(f"\nExtraction source breakdown:")
        total = sum(extraction_stats.values())
        for source, count in sorted(extraction_stats.items(), key=lambda x: -x[1]):
            pct = (count / total * 100) if total > 0 else 0
            print(f"  {source:20s}: {count:5d} ({pct:5.1f}%)")

        return media_embeddings

    def _extract_ingredient_ids_yaml_source(self, media_data: dict) -> tuple[List[str], dict]:
        """
        Extract CHEBI IDs from YAML composition using YAML-first approach.

        Returns:
            (ingredient_ids, extraction_stats)
        """
        ingredient_ids = []
        stats = {
            'yaml_chebi_term': 0,
            'yaml_term_chebi': 0,
            'name_fallback': 0,
            'kg_fallback': 0,
            'not_found': 0
        }

        # Check if this is a solution file (solutions use KG fallback as last resort)
        is_solution = False
        solution_term = media_data.get("term") or media_data.get("media_term", {}).get("term")
        if solution_term and isinstance(solution_term, dict) and "id" in solution_term:
            solution_id = solution_term["id"]
            is_solution = solution_id.startswith("mediadive.solution:")

        # Extract from main ingredients or composition
        ingredients = media_data.get("ingredients", []) or media_data.get("composition", [])

        for ing in ingredients:
            if not isinstance(ing, dict):
                continue

            chebi_id = None

            # Priority 1: chebi_term.id (from enriched YAML)
            if "chebi_term" in ing:
                chebi_term = ing["chebi_term"]
                if isinstance(chebi_term, dict) and "id" in chebi_term:
                    chebi_id = chebi_term["id"]
                    if chebi_id.startswith("CHEBI:"):
                        ingredient_ids.append(chebi_id)
                        stats['yaml_chebi_term'] += 1
                        continue

            # Priority 2: term.id if CHEBI
            if "term" in ing:
                term = ing["term"]
                if isinstance(term, dict) and "id" in term:
                    term_id = term["id"]
                    if term_id.startswith(("CHEBI:", "FOODON:")):
                        ingredient_ids.append(term_id)
                        stats['yaml_term_chebi'] += 1
                        continue

            # Priority 3: Name-based fallback
            preferred_term = ing.get("preferred_term", "")
            if preferred_term and preferred_term in self.name_to_chebi:
                chebi_ids = self.name_to_chebi[preferred_term]
                if chebi_ids:
                    ingredient_ids.append(chebi_ids[0])  # Take first match
                    stats['name_fallback'] += 1
                    continue

            stats['not_found'] += 1

        # Extract from solutions (similar logic)
        solutions = media_data.get("solutions", [])
        for solution in solutions:
            if not isinstance(solution, dict):
                continue

            # Try to get solution ID for KG fallback
            if "term" in solution:
                term = solution["term"]
                if isinstance(term, dict) and "id" in term:
                    sol_id = term["id"]
                    if sol_id.startswith("mediadive.solution:") and sol_id in self.solution_to_chebi:
                        # KG fallback for whole solution
                        chebi_ids = self.solution_to_chebi[sol_id]
                        ingredient_ids.extend(chebi_ids)
                        stats['kg_fallback'] += len(chebi_ids)
                        continue

            # Otherwise process solution composition
            composition = solution.get("composition", [])
            for comp in composition:
                if not isinstance(comp, dict):
                    continue

                # Same extraction logic as ingredients
                if "chebi_term" in comp:
                    chebi_term = comp["chebi_term"]
                    if isinstance(chebi_term, dict) and "id" in chebi_term:
                        chebi_id = chebi_term["id"]
                        if chebi_id.startswith("CHEBI:"):
                            ingredient_ids.append(chebi_id)
                            stats['yaml_chebi_term'] += 1
                            continue

                if "term" in comp:
                    term = comp["term"]
                    if isinstance(term, dict) and "id" in term:
                        term_id = term["id"]
                        if term_id.startswith(("CHEBI:", "FOODON:")):
                            ingredient_ids.append(term_id)
                            stats['yaml_term_chebi'] += 1
                            continue

                stats['not_found'] += 1

        # Final fallback: If this is a solution with no ingredients extracted, use KG
        if is_solution and not ingredient_ids and solution_id in self.solution_to_chebi:
            chebi_ids = self.solution_to_chebi[solution_id]
            ingredient_ids.extend(chebi_ids)
            stats['kg_fallback'] += len(chebi_ids)

        return ingredient_ids, stats

    def _extract_organism_ids(self, media_data: dict) -> List[str]:
        """Extract NCBITaxon IDs from target organisms."""
        organism_ids = []

        organisms = media_data.get("target_organisms", [])
        for org in organisms:
            if isinstance(org, dict) and "term" in org:
                term = org["term"]
                if isinstance(term, dict) and "id" in term:
                    term_id = term["id"]
                    if term_id.startswith("NCBITaxon:"):
                        organism_ids.append(term_id)

        return organism_ids

    def _aggregate_components(
        self,
        ingredient_ids: List[str],
        organism_ids: List[str],
        ingredient_weight: float = 0.6,
        organism_weight: float = 0.4,
    ) -> tuple[Optional[np.ndarray], float]:
        """Aggregate ingredient and organism embeddings with weighting."""
        # Collect ingredient embeddings
        ingredient_vectors = []
        for term_id in ingredient_ids:
            if term_id in self.embeddings:
                ingredient_vectors.append(self.embeddings[term_id])

        # Collect organism embeddings
        organism_vectors = []
        for term_id in organism_ids:
            if term_id in self.embeddings:
                organism_vectors.append(self.embeddings[term_id])

        # Calculate coverage
        total_components = len(ingredient_ids) + len(organism_ids)
        found_components = len(ingredient_vectors) + len(organism_vectors)

        if total_components == 0 or found_components == 0:
            return None, 0.0

        coverage = found_components / total_components

        # Mean pool each component type
        ingredient_mean = (
            np.mean(ingredient_vectors, axis=0) if ingredient_vectors else None
        )
        organism_mean = np.mean(organism_vectors, axis=0) if organism_vectors else None

        # Weighted combination
        if ingredient_mean is not None and organism_mean is not None:
            aggregated = (
                ingredient_weight * ingredient_mean + organism_weight * organism_mean
            )
        elif ingredient_mean is not None:
            aggregated = ingredient_mean
        elif organism_mean is not None:
            aggregated = organism_mean
        else:
            return None, 0.0

        return aggregated, coverage

    def get_direct_embeddings(self, media_yamls: List[Path]) -> Dict[str, MediaEmbedding]:
        """
        Extract direct media embeddings from mediadive.medium nodes.

        For MediaDive media:
        1. Extract media_term.term.id (e.g., DSMZ:123)
        2. Map to mediadive.medium:DSMZ_123
        3. Lookup embedding directly

        Args:
            media_yamls: List of paths to media YAML files

        Returns:
            Dictionary mapping medium names to MediaEmbedding objects
        """
        media_embeddings = {}

        for yaml_path in tqdm(media_yamls, desc="Extracting direct embeddings"):
            try:
                with open(yaml_path, "r") as f:
                    media_data = yaml.safe_load(f)

                if not media_data:
                    continue

                # Extract media term ID
                media_term_id = self._extract_media_term_id(media_data)
                if not media_term_id:
                    continue

                # Map to embedding node ID
                embedding_node_id = self._map_to_embedding_node_id(media_term_id)
                if not embedding_node_id or embedding_node_id not in self.embeddings:
                    continue

                # Get embedding
                embedding = self.embeddings[embedding_node_id]

                # Count components for metadata
                ingredient_ids, _ = self._extract_ingredient_ids_yaml_source(media_data)
                organism_ids = self._extract_organism_ids(media_data)

                medium_name = yaml_path.stem
                media_embeddings[medium_name] = MediaEmbedding(
                    medium_id=medium_name,
                    embedding=embedding,
                    coverage=1.0,  # Direct embedding has full coverage
                    num_ingredients=len(ingredient_ids),
                    num_organisms=len(organism_ids),
                    source="direct",
                )

            except Exception as e:
                print(f"⚠ Error processing {yaml_path.name}: {e}")
                continue

        print(f"✓ Extracted {len(media_embeddings):,} direct media embeddings")
        return media_embeddings

    def _extract_media_term_id(self, media_data: dict) -> Optional[str]:
        """Extract media term ID from media_term field."""
        media_term = media_data.get("media_term")
        if isinstance(media_term, dict) and "term" in media_term:
            term = media_term["term"]
            if isinstance(term, dict) and "id" in term:
                return term["id"]
        return None

    def _map_to_embedding_node_id(self, media_term_id: str) -> Optional[str]:
        """
        Map media/solution term ID to embedding node ID.

        Examples:
            mediadive.medium:123 -> mediadive.medium:123 (direct match)
            mediadive.solution:456 -> mediadive.solution:456 (direct match)
            komodo.medium:123 -> None (not in embeddings)
            TOGO:123 -> None (not in embeddings)
        """
        # MediaDive medium and solution IDs are already in the correct format
        if media_term_id.startswith(("mediadive.medium:", "mediadive.solution:")):
            return media_term_id
        return None
