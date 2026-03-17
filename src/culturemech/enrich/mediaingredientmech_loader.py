"""Loader for MediaIngredientMech data from GitHub repository."""

import logging
import subprocess
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Optional
from rapidfuzz import fuzz
import yaml

logger = logging.getLogger(__name__)


class MediaIngredientMechLoader:
    """Load and index MediaIngredientMech data for ingredient matching."""

    def __init__(self, repo_path: Optional[Path] = None):
        """
        Initialize the loader.

        Args:
            repo_path: Path to existing MediaIngredientMech repo, or None to clone fresh
        """
        self.repo_path = repo_path
        self.ingredients: List[Dict[str, Any]] = []
        self.by_chebi: Dict[str, Dict[str, Any]] = {}
        self.by_name: Dict[str, Dict[str, Any]] = {}
        self.by_synonym: Dict[str, List[Dict[str, Any]]] = {}

        if self.repo_path:
            self.load_ingredients()

    @staticmethod
    def clone_repo(target_dir: Path) -> Path:
        """
        Clone MediaIngredientMech repository from GitHub.

        Args:
            target_dir: Directory to clone into

        Returns:
            Path to cloned repository
        """
        repo_url = "https://github.com/microbe-mech/MediaIngredientMech.git"
        logger.info(f"Cloning MediaIngredientMech from {repo_url}...")

        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, str(target_dir)],
            check=True,
            capture_output=True
        )

        logger.info(f"Repository cloned to {target_dir}")
        return target_dir

    def load_ingredients(self):
        """Load ingredients from mapped_ingredients.yaml."""
        if not self.repo_path:
            raise ValueError("repo_path not set - cannot load ingredients")

        # Try mapped_ingredients.yaml first (preferred - has CHEBI mappings)
        yaml_file = self.repo_path / "data" / "curated" / "mapped_ingredients.yaml"

        # Fallback to old location for backwards compatibility
        if not yaml_file.exists():
            yaml_file = self.repo_path / "unmapped_ingredients.yaml"

        if not yaml_file.exists():
            raise FileNotFoundError(f"mapped_ingredients.yaml not found at {yaml_file}")

        logger.info(f"Loading MediaIngredientMech data from {yaml_file}...")

        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        # The YAML structure should be a list of ingredient records
        if isinstance(data, list):
            self.ingredients = data
        elif isinstance(data, dict) and 'ingredients' in data:
            self.ingredients = data['ingredients']
        else:
            self.ingredients = []

        logger.info(f"Loaded {len(self.ingredients)} ingredients")

        # Build indexes
        self._build_indexes()

    def _build_indexes(self):
        """Build lookup indexes for efficient matching."""
        logger.info("Building lookup indexes...")

        for ingredient in self.ingredients:
            mim_id = ingredient.get('id')
            if not mim_id:
                continue

            # Index by CHEBI ID (try both field names for compatibility)
            chebi_id = ingredient.get('ontology_id') or ingredient.get('chebi_id')
            if chebi_id:
                # Normalize CHEBI ID format
                if not chebi_id.startswith('CHEBI:'):
                    chebi_id = f"CHEBI:{chebi_id}"
                self.by_chebi[chebi_id] = ingredient

            # Index by normalized name (try both field names)
            name = ingredient.get('preferred_term') or ingredient.get('name', '')
            name = name.strip()
            if name:
                normalized_name = self._normalize_name(name)
                self.by_name[normalized_name] = ingredient

            # Index by synonyms
            synonyms = ingredient.get('synonyms', [])
            if isinstance(synonyms, list):
                for syn in synonyms:
                    # Handle both string and dict formats
                    if isinstance(syn, str):
                        syn_text = syn
                    elif isinstance(syn, dict):
                        syn_text = syn.get('synonym_text', '')
                    else:
                        continue

                    if syn_text:
                        normalized_syn = self._normalize_name(syn_text)
                        if normalized_syn not in self.by_synonym:
                            self.by_synonym[normalized_syn] = []
                        self.by_synonym[normalized_syn].append(ingredient)

        logger.info(
            f"  CHEBI index: {len(self.by_chebi)} entries, "
            f"Name index: {len(self.by_name)} entries, "
            f"Synonym index: {len(self.by_synonym)} entries"
        )

    @staticmethod
    def _normalize_name(name: str) -> str:
        """
        Normalize ingredient name for matching.

        Args:
            name: Raw ingredient name

        Returns:
            Normalized name (lowercase, no extra whitespace)
        """
        return ' '.join(name.lower().strip().split())

    def find_match(
        self,
        name: str,
        chebi_id: Optional[str] = None,
        fuzzy_threshold: float = 0.95
    ) -> Optional[Dict[str, Any]]:
        """
        Find best matching MediaIngredientMech entry.

        Priority:
        1. CHEBI ID match (exact)
        2. Exact name match
        3. Synonym match
        4. Fuzzy name match (if score >= threshold)

        Args:
            name: Ingredient name to match
            chebi_id: Optional CHEBI ID
            fuzzy_threshold: Minimum fuzzy match score (0.0-1.0)

        Returns:
            Matching ingredient dict with 'match_method' key added, or None
        """
        # Priority 1: CHEBI ID
        if chebi_id:
            if not chebi_id.startswith('CHEBI:'):
                chebi_id = f"CHEBI:{chebi_id}"

            if chebi_id in self.by_chebi:
                match = self.by_chebi[chebi_id].copy()
                match['match_method'] = 'chebi_id'
                return match

        normalized_name = self._normalize_name(name)

        # Priority 2: Exact name match
        if normalized_name in self.by_name:
            match = self.by_name[normalized_name].copy()
            match['match_method'] = 'exact_name'
            return match

        # Priority 3: Synonym match
        if normalized_name in self.by_synonym:
            # Take first synonym match (could have multiple)
            match = self.by_synonym[normalized_name][0].copy()
            match['match_method'] = 'synonym'
            return match

        # Priority 4: Fuzzy match
        best_score = 0.0
        best_match = None

        for norm_name, ingredient in self.by_name.items():
            score = fuzz.ratio(normalized_name, norm_name) / 100.0
            if score > best_score:
                best_score = score
                best_match = ingredient

        if best_score >= fuzzy_threshold:
            match = best_match.copy()
            match['match_method'] = f'fuzzy_{best_score:.2f}'
            return match

        return None
