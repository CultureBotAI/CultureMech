"""Import ingredient hierarchy from MediaIngredientMech repository."""

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional
import yaml

logger = logging.getLogger(__name__)


class MediaIngredientMechHierarchyImporter:
    """Import ingredient hierarchy from MediaIngredientMech."""

    def __init__(self, repo_path: Optional[Path] = None):
        """
        Initialize the hierarchy importer.

        Args:
            repo_path: Path to MediaIngredientMech repository
        """
        self.repo_path = repo_path
        self.hierarchy: Dict[str, Any] = {}
        self.lookup_index: Dict[str, Any] = {}

    def load_hierarchy(self, mim_repo_path: Optional[Path] = None) -> Dict[str, Any]:
        """
        Load hierarchy from MediaIngredientMech YAML files.

        Args:
            mim_repo_path: Path to MediaIngredientMech repo (overrides instance path)

        Returns:
            Dictionary containing:
                - families: Parent-child relationships
                - roles: Role assignments
                - merges: Merge mappings
        """
        repo_path = mim_repo_path or self.repo_path
        if not repo_path:
            raise ValueError("MediaIngredientMech repository path not provided")

        if not repo_path.exists():
            raise FileNotFoundError(f"Repository not found at {repo_path}")

        logger.info(f"Loading hierarchy from {repo_path}...")

        # Look for hierarchy/family files
        hierarchy_data = {
            'families': [],
            'roles': {},
            'merges': {},
            'variants': {}
        }

        # Load ingredient families (parent-child relationships)
        families_file = repo_path / "ingredient_families.yaml"
        if families_file.exists():
            logger.info(f"Loading families from {families_file}...")
            with open(families_file, 'r', encoding='utf-8') as f:
                families_data = yaml.safe_load(f)
                if families_data:
                    hierarchy_data['families'] = families_data.get('families', [])
                    logger.info(f"  Loaded {len(hierarchy_data['families'])} families")

        # Load role assignments
        roles_file = repo_path / "ingredient_roles.yaml"
        if roles_file.exists():
            logger.info(f"Loading roles from {roles_file}...")
            with open(roles_file, 'r', encoding='utf-8') as f:
                roles_data = yaml.safe_load(f)
                if roles_data:
                    hierarchy_data['roles'] = roles_data.get('roles', {})
                    logger.info(f"  Loaded roles for {len(hierarchy_data['roles'])} ingredients")

        # Load merge mappings
        merges_file = repo_path / "ingredient_merges.yaml"
        if merges_file.exists():
            logger.info(f"Loading merges from {merges_file}...")
            with open(merges_file, 'r', encoding='utf-8') as f:
                merges_data = yaml.safe_load(f)
                if merges_data:
                    hierarchy_data['merges'] = merges_data.get('merges', {})
                    logger.info(f"  Loaded {len(hierarchy_data['merges'])} merge mappings")

        # Load variant information
        variants_file = repo_path / "ingredient_variants.yaml"
        if variants_file.exists():
            logger.info(f"Loading variants from {variants_file}...")
            with open(variants_file, 'r', encoding='utf-8') as f:
                variants_data = yaml.safe_load(f)
                if variants_data:
                    hierarchy_data['variants'] = variants_data.get('variants', {})
                    logger.info(f"  Loaded {len(hierarchy_data['variants'])} variant definitions")

        self.hierarchy = hierarchy_data
        self._build_lookup_index()

        return hierarchy_data

    def _build_lookup_index(self):
        """
        Build fast lookup index for hierarchy queries.

        Creates indexes by:
        - CHEBI ID → canonical ingredient
        - Name → canonical ingredient
        - MediaIngredientMech ID → ingredient info
        """
        logger.info("Building hierarchy lookup index...")

        self.lookup_index = {
            'by_chebi': {},
            'by_name': {},
            'by_mim_id': {},
            'by_synonym': {},
            'parent_of': {},  # child_id → parent_id
            'children_of': {}  # parent_id → [child_ids]
        }

        # Index families (parent-child relationships)
        for family in self.hierarchy.get('families', []):
            parent_id = family.get('parent_id')
            parent_name = family.get('parent_name')
            parent_chebi = family.get('parent_chebi')
            children = family.get('children', [])

            # Index parent
            if parent_id:
                self.lookup_index['by_mim_id'][parent_id] = {
                    'id': parent_id,
                    'name': parent_name,
                    'chebi_id': parent_chebi,
                    'is_parent': True
                }

                if parent_chebi:
                    self.lookup_index['by_chebi'][parent_chebi] = parent_id

                if parent_name:
                    normalized_name = self._normalize_name(parent_name)
                    self.lookup_index['by_name'][normalized_name] = parent_id

            # Index children
            if parent_id:
                self.lookup_index['children_of'][parent_id] = []

            for child in children:
                child_id = child.get('id')
                child_name = child.get('name')
                child_chebi = child.get('chebi_id')
                variant_type = child.get('variant_type')

                if child_id:
                    self.lookup_index['by_mim_id'][child_id] = {
                        'id': child_id,
                        'name': child_name,
                        'chebi_id': child_chebi,
                        'parent_id': parent_id,
                        'parent_name': parent_name,
                        'variant_type': variant_type
                    }

                    if parent_id:
                        self.lookup_index['parent_of'][child_id] = parent_id
                        self.lookup_index['children_of'][parent_id].append(child_id)

                    if child_chebi:
                        self.lookup_index['by_chebi'][child_chebi] = child_id

                    if child_name:
                        normalized_name = self._normalize_name(child_name)
                        self.lookup_index['by_name'][normalized_name] = child_id

        logger.info(
            f"  Index built: "
            f"{len(self.lookup_index['by_mim_id'])} MIM IDs, "
            f"{len(self.lookup_index['by_chebi'])} CHEBI IDs, "
            f"{len(self.lookup_index['by_name'])} names, "
            f"{len(self.lookup_index['parent_of'])} parent relationships"
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

    def get_parent(self, mim_id: str) -> Optional[Dict[str, Any]]:
        """
        Get parent ingredient for a given MediaIngredientMech ID.

        Args:
            mim_id: MediaIngredientMech ID

        Returns:
            Parent ingredient info or None if no parent
        """
        parent_id = self.lookup_index['parent_of'].get(mim_id)
        if parent_id:
            return self.lookup_index['by_mim_id'].get(parent_id)
        return None

    def get_children(self, mim_id: str) -> List[Dict[str, Any]]:
        """
        Get child ingredients for a given MediaIngredientMech ID.

        Args:
            mim_id: MediaIngredientMech ID

        Returns:
            List of child ingredient info dicts
        """
        child_ids = self.lookup_index['children_of'].get(mim_id, [])
        return [
            self.lookup_index['by_mim_id'][child_id]
            for child_id in child_ids
            if child_id in self.lookup_index['by_mim_id']
        ]

    def get_variant_type(self, mim_id: str) -> Optional[str]:
        """
        Get variant type for a given MediaIngredientMech ID.

        Args:
            mim_id: MediaIngredientMech ID

        Returns:
            Variant type (HYDRATE, SALT_FORM, etc.) or None
        """
        ingredient_info = self.lookup_index['by_mim_id'].get(mim_id)
        if ingredient_info:
            return ingredient_info.get('variant_type')
        return None

    def get_roles(self, mim_id: str) -> List[str]:
        """
        Get functional roles for a given MediaIngredientMech ID.

        Args:
            mim_id: MediaIngredientMech ID

        Returns:
            List of role strings (e.g., ['MINERAL', 'SALT'])
        """
        return self.hierarchy.get('roles', {}).get(mim_id, [])

    def find_by_chebi(self, chebi_id: str) -> Optional[str]:
        """
        Find MediaIngredientMech ID by CHEBI ID.

        Args:
            chebi_id: CHEBI ID (with or without prefix)

        Returns:
            MediaIngredientMech ID or None
        """
        # Normalize CHEBI ID format
        if not chebi_id.startswith('CHEBI:'):
            chebi_id = f"CHEBI:{chebi_id}"

        return self.lookup_index['by_chebi'].get(chebi_id)

    def find_by_name(self, name: str) -> Optional[str]:
        """
        Find MediaIngredientMech ID by name.

        Args:
            name: Ingredient name

        Returns:
            MediaIngredientMech ID or None
        """
        normalized_name = self._normalize_name(name)
        return self.lookup_index['by_name'].get(normalized_name)

    def get_ingredient_info(self, mim_id: str) -> Optional[Dict[str, Any]]:
        """
        Get full ingredient information by MediaIngredientMech ID.

        Args:
            mim_id: MediaIngredientMech ID

        Returns:
            Ingredient info dict or None
        """
        return self.lookup_index['by_mim_id'].get(mim_id)

    def get_stats(self) -> Dict[str, int]:
        """
        Get statistics about loaded hierarchy.

        Returns:
            Dictionary with counts of various hierarchy elements
        """
        return {
            'total_ingredients': len(self.lookup_index['by_mim_id']),
            'parents': sum(
                1 for info in self.lookup_index['by_mim_id'].values()
                if info.get('is_parent')
            ),
            'children': len(self.lookup_index['parent_of']),
            'families': len(self.hierarchy.get('families', [])),
            'roles_assigned': len(self.hierarchy.get('roles', {})),
            'merges': len(self.hierarchy.get('merges', {})),
            'variants': len(self.hierarchy.get('variants', {}))
        }
