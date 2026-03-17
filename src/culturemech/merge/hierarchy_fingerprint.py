"""Hierarchy-aware recipe fingerprinting using MediaIngredientMech.

Extends RecipeFingerprinter with parent-based ingredient matching and
variant-aware fingerprinting modes.

Modes:
- 'chemical': Uses parent CHEBI IDs, merges variants together
  (CaCl₂·2H₂O and CaCl₂ get same fingerprint)
- 'variant': Uses parent + variant type, keeps variants separate
  (CaCl₂·2H₂O and CaCl₂ get different fingerprints)
"""

import hashlib
from pathlib import Path
from typing import Dict, List, Optional, Set

from culturemech.enrich.hierarchy_importer import MediaIngredientMechHierarchyImporter
from culturemech.merge.fingerprint import IngredientSignature, RecipeFingerprinter


class HierarchyAwareFingerprinter(RecipeFingerprinter):
    """Generate fingerprints using ingredient hierarchy from MediaIngredientMech.

    This fingerprinter leverages parent-child relationships to enable
    smarter recipe matching:

    1. Chemical mode: Treats variants as equivalent (merges hydrates, salts, etc.)
    2. Variant mode: Preserves variant distinctions (keeps hydrates separate)

    Uses MediaIngredientMech hierarchy for parent lookups and variant types.
    """

    VALID_MODES = ['chemical', 'variant', 'original']

    def __init__(
        self,
        hierarchy_importer: Optional[MediaIngredientMechHierarchyImporter] = None,
        mode: str = 'chemical'
    ):
        """Initialize hierarchy-aware fingerprinter.

        Args:
            hierarchy_importer: MediaIngredientMech hierarchy importer instance
                               If None, falls back to original fingerprinting
            mode: Fingerprinting mode:
                  - 'chemical': Use parent ingredients (variants merge)
                  - 'variant': Use parent + variant type (variants separate)
                  - 'original': Use original RecipeFingerprinter behavior

        Raises:
            ValueError: If mode is not valid
        """
        super().__init__()

        if mode not in self.VALID_MODES:
            raise ValueError(
                f"Invalid mode '{mode}'. Must be one of: {self.VALID_MODES}"
            )

        self.hierarchy = hierarchy_importer
        self.mode = mode

        # If no hierarchy or original mode, fall back to parent behavior
        if not hierarchy_importer or mode == 'original':
            self.mode = 'original'

    def fingerprint(self, recipe: Dict) -> Optional[str]:
        """Generate fingerprint from recipe ingredient set.

        Uses hierarchy-aware matching if available, otherwise falls back
        to original fingerprinting.

        Args:
            recipe: Recipe dictionary with 'ingredients' and optional 'solutions'

        Returns:
            SHA256 hex digest of sorted ingredient identifiers, or None if no valid ingredients
        """
        if self.mode == 'original':
            return super().fingerprint(recipe)

        # Use hierarchy-aware extraction
        if 'ingredients' not in recipe:
            raise ValueError("Recipe has no ingredients list")

        ingredients = recipe.get('ingredients', [])

        if not ingredients or len(ingredients) == 0:
            raise ValueError("Recipe has empty ingredients list")

        signatures = self._extract_signatures(recipe)

        if not signatures:
            return None

        # Sort for order-independence
        sorted_ids = sorted([str(sig) for sig in signatures])

        # Generate hash
        combined = '|'.join(sorted_ids)
        fingerprint = hashlib.sha256(combined.encode('utf-8')).hexdigest()

        return fingerprint

    def _extract_identifier(self, ingredient: Dict) -> Optional[IngredientSignature]:
        """Extract identifier using hierarchy when available.

        Priority (hierarchy-aware modes):
        1. Parent CHEBI ID from MediaIngredientMech (if available)
           - In 'chemical' mode: uses parent only
           - In 'variant' mode: uses parent + variant type
        2. Raw CHEBI ID (fallback)
        3. Normalized name (fallback)

        Args:
            ingredient: Ingredient dictionary

        Returns:
            IngredientSignature or None if ingredient is invalid or placeholder
        """
        if self.mode == 'original':
            return super()._extract_identifier(ingredient)

        # Try hierarchy-aware extraction
        if self.hierarchy:
            identifier = self._extract_hierarchy_identifier(ingredient)
            if identifier:
                return identifier

        # Fall back to original extraction
        return super()._extract_identifier(ingredient)

    def _extract_hierarchy_identifier(
        self,
        ingredient: Dict
    ) -> Optional[IngredientSignature]:
        """Extract identifier using MediaIngredientMech hierarchy.

        Args:
            ingredient: Ingredient dictionary

        Returns:
            IngredientSignature or None
        """
        # Get MediaIngredientMech ID from enrichment
        mim_id = ingredient.get('mediaingredientmech_term', {}).get('id')

        if not mim_id:
            # No MIM enrichment, fall back to original
            return None

        # Get ingredient info from hierarchy
        ingredient_info = self.hierarchy.get_ingredient_info(mim_id)

        if not ingredient_info:
            # Not in hierarchy, fall back to original
            return None

        # Check if this ingredient has a parent
        parent_info = self.hierarchy.get_parent(mim_id)

        if parent_info:
            # This is a variant with a parent
            parent_chebi = parent_info.get('chebi_id')

            if parent_chebi:
                if self.mode == 'variant':
                    # Include variant type to keep variants separate
                    variant_type = ingredient_info.get('variant_type', 'BASE')
                    identifier = f"{parent_chebi}|{variant_type}"
                else:  # chemical mode
                    # Use parent only to merge variants together
                    identifier = parent_chebi

                return IngredientSignature(
                    identifier=identifier,
                    source='hierarchy_parent'
                )
        else:
            # This ingredient is itself a parent (or has no parent)
            # Use its own CHEBI ID
            chebi_id = ingredient_info.get('chebi_id')

            if chebi_id:
                if self.mode == 'variant':
                    # Mark as BASE (parent ingredient)
                    identifier = f"{chebi_id}|BASE"
                else:  # chemical mode
                    identifier = chebi_id

                return IngredientSignature(
                    identifier=identifier,
                    source='hierarchy_base'
                )

        # No CHEBI ID available in hierarchy
        return None

    def get_fingerprint_mode(self) -> str:
        """Get current fingerprinting mode.

        Returns:
            Current mode string
        """
        return self.mode

    def get_fingerprint_version(self) -> str:
        """Get fingerprinting algorithm version.

        Returns:
            Version string for tracking algorithm changes
        """
        if self.mode == 'original':
            return 'original-v1.0'
        elif self.hierarchy:
            return f'hierarchy-{self.mode}-v1.0'
        else:
            return 'original-v1.0-fallback'
