"""Merge rule engine for hierarchical recipe merging.

Implements three-level merge decision hierarchy:
1. Explicit merge rules from MediaIngredientMech (highest priority)
2. Hierarchy relationships (parent-child)
3. Fingerprint matching (baseline)

Supports multiple merge modes:
- conservative: Only merge with explicit rules or exact fingerprint match
- aggressive: Merge all variants with same parent
- variant-aware: Balanced approach, merge some variants but preserve important distinctions
"""

from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

from culturemech.enrich.hierarchy_importer import MediaIngredientMechHierarchyImporter


class MergeRuleEngine:
    """Apply hierarchical merge rules to recipe groups.

    Combines explicit merge rules, hierarchy relationships, and fingerprint
    matching to make smart merge decisions.
    """

    VALID_MODES = ['conservative', 'aggressive', 'variant-aware']

    def __init__(
        self,
        hierarchy_importer: MediaIngredientMechHierarchyImporter,
        mode: str = 'conservative',
        merge_rules_path: Optional[Path] = None
    ):
        """Initialize merge rule engine.

        Args:
            hierarchy_importer: MediaIngredientMech hierarchy importer
            mode: Merge mode ('conservative', 'aggressive', 'variant-aware')
            merge_rules_path: Optional path to explicit merge rules snapshot

        Raises:
            ValueError: If mode is not valid
        """
        if mode not in self.VALID_MODES:
            raise ValueError(
                f"Invalid mode '{mode}'. Must be one of: {self.VALID_MODES}"
            )

        self.hierarchy = hierarchy_importer
        self.mode = mode
        self.explicit_rules = {}

        # Load explicit merge rules if provided
        if merge_rules_path and merge_rules_path.exists():
            self._load_explicit_rules(merge_rules_path)

    def _load_explicit_rules(self, rules_path: Path) -> None:
        """Load explicit merge rules from MediaIngredientMech snapshot.

        Args:
            rules_path: Path to ingredient_merges.yaml snapshot
        """
        with open(rules_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)

        if not data or 'merges' not in data:
            return

        # Build synonym → canonical mapping
        merges = data.get('merges', {})

        for canonical_id, merge_info in merges.items():
            # Store canonical
            self.explicit_rules[canonical_id] = canonical_id

            # Store all synonyms pointing to canonical
            synonyms = merge_info.get('synonyms', [])
            for synonym_id in synonyms:
                self.explicit_rules[synonym_id] = canonical_id

    def should_merge(
        self,
        recipe1: Dict,
        recipe2: Dict,
        fingerprint_match: bool = False
    ) -> Tuple[bool, str, float]:
        """Determine if two recipes should merge.

        Applies three-level decision hierarchy:
        1. Check explicit merge rules
        2. Check hierarchy relationships
        3. Fall back to fingerprint match

        Args:
            recipe1: First recipe dictionary
            recipe2: Second recipe dictionary
            fingerprint_match: Whether recipes have identical fingerprints

        Returns:
            Tuple of (should_merge, reason, confidence)
            - should_merge: Boolean merge decision
            - reason: Human-readable explanation
            - confidence: Score 0.0-1.0 indicating decision confidence
        """
        # Level 1: Check explicit merge rules
        merge_decision = self._check_explicit_rules(recipe1, recipe2)
        if merge_decision:
            return merge_decision

        # Level 2: Check hierarchy relationships
        merge_decision = self._check_hierarchy_relationships(recipe1, recipe2)
        if merge_decision:
            return merge_decision

        # Level 3: Fall back to fingerprint match
        if fingerprint_match:
            return (True, "identical_fingerprint", 0.9)

        # No merge
        return (False, "no_match", 1.0)

    def _check_explicit_rules(
        self,
        recipe1: Dict,
        recipe2: Dict
    ) -> Optional[Tuple[bool, str, float]]:
        """Check if recipes should merge based on explicit rules.

        Args:
            recipe1: First recipe dictionary
            recipe2: Second recipe dictionary

        Returns:
            Merge decision tuple or None if no explicit rule applies
        """
        if not self.explicit_rules:
            return None

        # Extract ingredient MIM IDs from both recipes
        ingredients1 = self._extract_mim_ids(recipe1)
        ingredients2 = self._extract_mim_ids(recipe2)

        # Check if any ingredients have explicit merge rules
        canonical1 = set(
            self.explicit_rules.get(mim_id, mim_id)
            for mim_id in ingredients1
        )
        canonical2 = set(
            self.explicit_rules.get(mim_id, mim_id)
            for mim_id in ingredients2
        )

        # If canonical ingredient sets are identical, merge
        if canonical1 == canonical2 and canonical1:
            return (True, "explicit_merge_rule", 1.0)

        return None

    def _check_hierarchy_relationships(
        self,
        recipe1: Dict,
        recipe2: Dict
    ) -> Optional[Tuple[bool, str, float]]:
        """Check if recipes should merge based on hierarchy.

        Args:
            recipe1: First recipe dictionary
            recipe2: Second recipe dictionary

        Returns:
            Merge decision tuple or None if hierarchy doesn't apply
        """
        # Extract ingredient info
        ingredients1 = self._get_ingredient_hierarchy_info(recipe1)
        ingredients2 = self._get_ingredient_hierarchy_info(recipe2)

        if not ingredients1 or not ingredients2:
            return None

        # Different behavior by mode
        if self.mode == 'conservative':
            # Only merge if ingredients are identical (including variants)
            return None  # Let fingerprint handle it

        elif self.mode == 'aggressive':
            # Merge if parent ingredients match (ignore variant types)
            parents1 = set(info['parent_or_self'] for info in ingredients1)
            parents2 = set(info['parent_or_self'] for info in ingredients2)

            if parents1 == parents2 and parents1:
                return (True, "same_parent_ingredients", 0.8)

        elif self.mode == 'variant-aware':
            # Merge some variants but preserve important distinctions
            # Strategy: merge if difference is only hydration state
            parents1 = set(info['parent_or_self'] for info in ingredients1)
            parents2 = set(info['parent_or_self'] for info in ingredients2)

            if parents1 != parents2:
                return None  # Different base chemicals

            # Check variant types
            variants1 = set(info.get('variant_type') for info in ingredients1)
            variants2 = set(info.get('variant_type') for info in ingredients2)

            # Only hydration differences are allowed
            hydration_variants = {'HYDRATE', 'ANHYDROUS', None}

            if variants1.issubset(hydration_variants) and \
               variants2.issubset(hydration_variants):
                return (True, "hydration_variant_only", 0.7)

        return None

    def _extract_mim_ids(self, recipe: Dict) -> List[str]:
        """Extract MediaIngredientMech IDs from recipe.

        Args:
            recipe: Recipe dictionary

        Returns:
            List of MediaIngredientMech IDs
        """
        mim_ids = []

        # Process direct ingredients
        for ingredient in recipe.get('ingredients', []):
            mim_id = ingredient.get('mediaingredientmech_term', {}).get('id')
            if mim_id:
                mim_ids.append(mim_id)

        # Process solutions
        for solution in recipe.get('solutions', []):
            for ingredient in solution.get('composition', []):
                mim_id = ingredient.get('mediaingredientmech_term', {}).get('id')
                if mim_id:
                    mim_ids.append(mim_id)

        return mim_ids

    def _get_ingredient_hierarchy_info(self, recipe: Dict) -> List[Dict]:
        """Get hierarchy information for all ingredients in recipe.

        Args:
            recipe: Recipe dictionary

        Returns:
            List of ingredient info dictionaries with hierarchy data
        """
        ingredient_infos = []

        mim_ids = self._extract_mim_ids(recipe)

        for mim_id in mim_ids:
            info = self.hierarchy.get_ingredient_info(mim_id)

            if not info:
                continue

            # Get parent or use self
            parent_info = self.hierarchy.get_parent(mim_id)

            if parent_info:
                parent_id = parent_info.get('id')
                variant_type = info.get('variant_type')
            else:
                parent_id = mim_id
                variant_type = None

            ingredient_infos.append({
                'id': mim_id,
                'parent_or_self': parent_id,
                'variant_type': variant_type,
                'name': info.get('name'),
            })

        return ingredient_infos

    def get_merge_confidence(
        self,
        recipe1: Dict,
        recipe2: Dict,
        fingerprint_match: bool = False
    ) -> float:
        """Get confidence score for merge decision.

        Args:
            recipe1: First recipe dictionary
            recipe2: Second recipe dictionary
            fingerprint_match: Whether recipes have identical fingerprints

        Returns:
            Confidence score 0.0-1.0
        """
        should_merge, reason, confidence = self.should_merge(
            recipe1, recipe2, fingerprint_match
        )

        return confidence if should_merge else 0.0

    def get_mode(self) -> str:
        """Get current merge mode.

        Returns:
            Mode string
        """
        return self.mode
