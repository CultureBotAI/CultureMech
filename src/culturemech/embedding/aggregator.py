"""
Media vector aggregator for deriving and extracting media embeddings.

Aggregates ingredient and organism embeddings to create media-level vectors.
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


class MediaVectorAggregator:
    """Aggregate node embeddings into media-level embeddings."""

    def __init__(self, embeddings_dict: Dict[str, np.ndarray], solution_mapping_path: Optional[Path] = None):
        """
        Initialize aggregator with embeddings dictionary.

        Args:
            embeddings_dict: Dictionary mapping node IDs to embedding vectors
            solution_mapping_path: Path to solution→CHEBI mapping JSON file
        """
        self.embeddings = embeddings_dict

        # Load solution→CHEBI mapping from KG
        self.solution_to_chebi = {}
        if solution_mapping_path and solution_mapping_path.exists():
            with open(solution_mapping_path) as f:
                self.solution_to_chebi = json.load(f)
            print(f"✓ Loaded {len(self.solution_to_chebi)} solution→CHEBI mappings from KG")
        else:
            # Try default location
            default_path = Path("data/solution_to_chebi_mapping.json")
            if default_path.exists():
                with open(default_path) as f:
                    self.solution_to_chebi = json.load(f)
                print(f"✓ Loaded {len(self.solution_to_chebi)} solution→CHEBI mappings from KG (default path)")

    def aggregate_derived_embeddings(
        self, media_yamls: List[Path], min_coverage: float = 0.5
    ) -> Dict[str, MediaEmbedding]:
        """
        Aggregate derived media embeddings from ingredients and organisms.

        For each medium:
        1. Extract CHEBI IDs from ingredients[].term.id
        2. Extract NCBITaxon IDs from target_organisms[].term.id
        3. Lookup embeddings for found IDs
        4. Mean pool: media_vector = weighted_mean([ingredient_vecs, organism_vecs])
        5. Track coverage % (found / total)

        Args:
            media_yamls: List of paths to media YAML files
            min_coverage: Minimum coverage threshold (0-1) to include medium

        Returns:
            Dictionary mapping medium names to MediaEmbedding objects
        """
        media_embeddings = {}

        for yaml_path in tqdm(media_yamls, desc="Aggregating derived embeddings"):
            try:
                with open(yaml_path, "r") as f:
                    media_data = yaml.safe_load(f)

                if not media_data:
                    continue

                # Extract components
                ingredient_ids = self._extract_ingredient_ids(media_data)
                organism_ids = self._extract_organism_ids(media_data)

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
        return media_embeddings

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
                ingredient_ids = self._extract_ingredient_ids(media_data)
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

    def _extract_ingredient_ids(self, media_data: dict) -> List[str]:
        """
        Extract CHEBI/FOODON/mediadive.ingredient IDs.

        For solutions, uses KG-Microbe edges to map mediadive.solution → CHEBI.

        Processes:
        - ingredients[] array (for media files)
        - composition[] array (for solution files)
        - solutions[].composition[] arrays (for media with solutions)

        This ensures both media ingredients and solution components are included.
        """
        ingredient_ids = []

        # Check if this is a solution file (solutions use 'term', media use 'media_term')
        solution_term = media_data.get("term") or media_data.get("media_term", {}).get("term")
        if solution_term and isinstance(solution_term, dict) and "id" in solution_term:
            solution_id = solution_term["id"]
            # If this is a solution, use KG mappings to get CHEBI ingredients
            if solution_id.startswith("mediadive.solution:"):
                chebi_ids = self.solution_to_chebi.get(solution_id, [])
                if chebi_ids:
                    ingredient_ids.extend(chebi_ids)
                    # Return early - solutions use KG mappings, not YAML composition
                    return ingredient_ids

        # Extract from main ingredients (media files)
        ingredients = media_data.get("ingredients", [])

        # Also check composition (for solution files without media_term)
        if not ingredients:
            ingredients = media_data.get("composition", [])

        for ing in ingredients:
            if not isinstance(ing, dict):
                continue

            # First try to get explicit term ID
            if "term" in ing:
                term = ing["term"]
                if isinstance(term, dict) and "id" in term:
                    term_id = term["id"]
                    if term_id.startswith(("CHEBI:", "FOODON:", "mediadive.ingredient:")):
                        ingredient_ids.append(term_id)
                        continue

            # Fallback: try to extract chemical name from notes and map to mediadive.ingredient
            if "notes" in ing and isinstance(ing["notes"], str):
                chem_name = self._extract_chemical_from_notes(ing["notes"])
                if chem_name:
                    # Try to find matching mediadive.ingredient embedding
                    # Look for exact match or normalized match
                    ingredient_id = self._find_mediadive_ingredient(chem_name)
                    if ingredient_id:
                        ingredient_ids.append(ingredient_id)

        # Extract from solutions referenced in media
        solutions = media_data.get("solutions", [])
        for solution in solutions:
            if not isinstance(solution, dict):
                continue

            # Try to get solution ID from term
            if "term" in solution:
                term = solution["term"]
                if isinstance(term, dict) and "id" in term:
                    solution_id = term["id"]
                    # Use KG mappings to get CHEBI ingredients for this solution
                    if solution_id.startswith("mediadive.solution:"):
                        chebi_ids = self.solution_to_chebi.get(solution_id, [])
                        ingredient_ids.extend(chebi_ids)
                        continue

            # Fallback: process composition within solution (for solutions without term ID)
            composition = solution.get("composition", [])
            for comp in composition:
                if not isinstance(comp, dict):
                    continue

                # Extract term ID from solution ingredient
                if "term" in comp:
                    term = comp["term"]
                    if isinstance(term, dict) and "id" in term:
                        term_id = term["id"]
                        if term_id.startswith(("CHEBI:", "FOODON:", "mediadive.ingredient:")):
                            ingredient_ids.append(term_id)
                            continue

                # Fallback: extract from notes
                if "notes" in comp and isinstance(comp["notes"], str):
                    chem_name = self._extract_chemical_from_notes(comp["notes"])
                    if chem_name:
                        ingredient_id = self._find_mediadive_ingredient(chem_name)
                        if ingredient_id:
                            ingredient_ids.append(ingredient_id)

        return ingredient_ids

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


    def _find_mediadive_ingredient(self, chem_name: str) -> Optional[str]:
        """
        Find mediadive.ingredient embedding ID by chemical name.

        Args:
            chem_name: Chemical name/formula extracted from notes

        Returns:
            mediadive.ingredient ID if found, None otherwise
        """
        # Normalize chemical name (remove spaces, lowercase for comparison)
        chem_normalized = chem_name.replace(" ", "").lower()

        # Try exact match first
        for embedding_id in self.embeddings.keys():
            if embedding_id.startswith("mediadive.ingredient:"):
                # Extract the ingredient name from the ID
                ingredient_name = embedding_id.split(":", 1)[1]
                ingredient_normalized = ingredient_name.replace(" ", "").replace("_", "").lower()

                # Check for exact match or substring match
                if (chem_normalized == ingredient_normalized or
                    chem_normalized in ingredient_normalized or
                    ingredient_normalized in chem_normalized):
                    return embedding_id

        return None

    def _extract_chemical_from_notes(self, notes: str) -> Optional[str]:
        """
        Extract chemical name from notes field.

        Examples:
            "NaNO3(Fisher BP360-500)" -> "NaNO3"
            "Original amount: K2HPO4(Sigma P 3786)" -> "K2HPO4"
            "CaCl2•2H2O(Sigma C-3881)" -> "CaCl2•2H2O"

        Args:
            notes: Notes field text from ingredient

        Returns:
            Extracted chemical name/formula or None
        """
        # Remove "Original amount:" prefix if present
        notes = re.sub(r'^Original amount:\s*', '', notes, flags=re.IGNORECASE)

        # Extract chemical formula before parenthesis (vendor info)
        match = re.match(r'^([A-Za-z0-9•·\s-]+?)[\(]', notes)
        if match:
            chem_name = match.group(1).strip()
            # Clean up bullet characters
            chem_name = re.sub(r'[•·]', '', chem_name).strip()
            return chem_name if chem_name else None

        return None

    def _aggregate_components(
        self,
        ingredient_ids: List[str],
        organism_ids: List[str],
        ingredient_weight: float = 0.6,
        organism_weight: float = 0.4,
    ) -> tuple[Optional[np.ndarray], float]:
        """
        Aggregate ingredient and organism embeddings with weighting.

        Args:
            ingredient_ids: List of ingredient term IDs
            organism_ids: List of organism term IDs
            ingredient_weight: Weight for ingredient embeddings (default 0.6)
            organism_weight: Weight for organism embeddings (default 0.4)

        Returns:
            Tuple of (aggregated_embedding, coverage)
        """
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
            # Both available - use weighted average
            aggregated = (
                ingredient_weight * ingredient_mean + organism_weight * organism_mean
            )
        elif ingredient_mean is not None:
            # Only ingredients available
            aggregated = ingredient_mean
        elif organism_mean is not None:
            # Only organisms available
            aggregated = organism_mean
        else:
            return None, 0.0

        return aggregated, coverage
