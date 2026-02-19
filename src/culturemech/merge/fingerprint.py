"""Recipe fingerprinting module for ingredient set matching.

Generates SHA256 fingerprints from ingredient sets for matching recipes with
the same base formulation (same chemicals, regardless of amounts).

Fingerprints are based on:
- CHEBI IDs (preferred) or normalized ingredient names
- Includes both direct ingredients and solution compositions
- Order-independent (sorted before hashing)
- Concentration-independent (ignores amounts, pH, temperature, etc.)

IMPORTANT: This identifies recipes with the same INGREDIENT SET, not identical
recipes. Two recipes with the same chemicals but different concentrations will
have the same fingerprint and be considered duplicates.
"""

import hashlib
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Set

import yaml


@dataclass
class IngredientSignature:
    """A normalized identifier for an ingredient.

    Attributes:
        identifier: CHEBI ID (preferred) or normalized name
        source: 'chebi' or 'name'
    """
    identifier: str
    source: str

    def __str__(self) -> str:
        return self.identifier

    def __hash__(self) -> int:
        return hash(self.identifier)

    def __eq__(self, other) -> bool:
        if not isinstance(other, IngredientSignature):
            return False
        return self.identifier == other.identifier


class RecipeFingerprinter:
    """Generate fingerprints from recipe ingredient sets.

    A fingerprint is a SHA256 hash of the sorted, unique ingredient identifiers.
    This enables exact SET matching of recipes with identical ingredients,
    regardless of order or concentration.
    """

    # Patterns that indicate placeholder/invalid ingredients
    PLACEHOLDER_PATTERNS = [
        r'see\s+source',
        r'refer\s+to',
        r'available\s+at',
        r'contact\s+source',
        r'not\s+specified',
        r'unknown',
        r'medium\s+no\.',
        r'composition\s+not\s+available',
        r'proprietary',
    ]

    def __init__(self):
        """Initialize the fingerprinter."""
        pass

    def fingerprint(self, recipe: Dict) -> Optional[str]:
        """Generate SHA256 fingerprint from recipe ingredient set.

        Args:
            recipe: Recipe dictionary with 'ingredients' and optional 'solutions'

        Returns:
            SHA256 hex digest of sorted ingredient identifiers, or None if no valid ingredients

        Raises:
            ValueError: If recipe has no ingredients list
        """
        if 'ingredients' not in recipe:
            raise ValueError("Recipe has no ingredients list")

        ingredients = recipe.get('ingredients', [])

        # Check for empty ingredients list
        if not ingredients or len(ingredients) == 0:
            raise ValueError("Recipe has empty ingredients list")

        signatures = self._extract_signatures(recipe)

        if not signatures:
            # Recipe has ingredients but none are valid (e.g., malformed data, placeholders)
            return None

        # Sort for order-independence
        sorted_ids = sorted([str(sig) for sig in signatures])

        # Generate hash
        combined = '|'.join(sorted_ids)
        fingerprint = hashlib.sha256(combined.encode('utf-8')).hexdigest()

        return fingerprint

    def _extract_signatures(self, recipe: Dict) -> Set[IngredientSignature]:
        """Extract ingredient signatures from recipe.

        Processes:
        1. Direct ingredients
        2. Solution compositions (if present)

        Args:
            recipe: Recipe dictionary

        Returns:
            Set of unique IngredientSignature objects
        """
        signatures = set()

        # Process direct ingredients
        for ingredient in recipe.get('ingredients', []):
            sig = self._extract_identifier(ingredient)
            if sig:
                signatures.add(sig)

        # Process solutions (recursive)
        for solution in recipe.get('solutions', []):
            for ingredient in solution.get('composition', []):
                sig = self._extract_identifier(ingredient)
                if sig:
                    signatures.add(sig)

        return signatures

    def _extract_identifier(self, ingredient: Dict) -> Optional[IngredientSignature]:
        """Extract CHEBI ID or normalized name from ingredient.

        Priority:
        1. CHEBI ID from term.id field
        2. Normalized preferred_term (if not a placeholder)

        Args:
            ingredient: Ingredient dictionary

        Returns:
            IngredientSignature or None if ingredient is invalid or placeholder
        """
        # Priority 1: CHEBI ID
        term = ingredient.get('term')
        if term and isinstance(term, dict):
            chebi_id = term.get('id')
            if chebi_id and chebi_id.startswith('CHEBI:'):
                return IngredientSignature(
                    identifier=chebi_id,
                    source='chebi'
                )

        # Priority 2: Normalized name (if not placeholder)
        preferred_term = ingredient.get('preferred_term')
        if preferred_term:
            # Check if this is a placeholder ingredient
            if self._is_placeholder(preferred_term):
                return None

            normalized = self._normalize_name(preferred_term)
            if normalized:
                return IngredientSignature(
                    identifier=normalized,
                    source='name'
                )

        return None

    def _is_placeholder(self, name: str) -> bool:
        """Check if ingredient name is a placeholder.

        Placeholder ingredients like "See source for composition" should not
        be used for fingerprinting as they don't represent actual ingredients.

        Args:
            name: Ingredient name to check

        Returns:
            True if name matches a placeholder pattern
        """
        name_lower = name.lower()
        for pattern in self.PLACEHOLDER_PATTERNS:
            if re.search(pattern, name_lower, re.IGNORECASE):
                return True
        return False

    def _normalize_name(self, name: str) -> str:
        """Normalize ingredient name for matching.

        Normalization:
        - Convert to lowercase
        - Remove hydration markers (·nH2O, .nH2O, xnH2O, x n H2O)
        - Remove extra whitespace
        - Trim

        Args:
            name: Raw ingredient name

        Returns:
            Normalized name
        """
        normalized = name.lower()

        # Remove hydration patterns
        # Matches: ·7H2O, .7H2O, x7H2O, x 7 H2O, (7H2O), etc.
        hydration_patterns = [
            r'[·\.x]?\s*\d+\s*h2o',    # ·7H2O, .7H2O, x7H2O, 7H2O
            r'\(\s*\d+\s*h2o\s*\)',    # (7H2O)
            r'x\s+\d+\s+h\s*2\s*o',    # x 7 H2O
        ]

        for pattern in hydration_patterns:
            normalized = re.sub(pattern, '', normalized, flags=re.IGNORECASE)

        # Remove extra whitespace
        normalized = re.sub(r'\s+', ' ', normalized)

        # Trim
        normalized = normalized.strip()

        return normalized

    def fingerprint_file(self, recipe_path: Path) -> str:
        """Generate fingerprint from recipe file.

        Args:
            recipe_path: Path to recipe YAML file

        Returns:
            SHA256 hex digest

        Raises:
            FileNotFoundError: If file doesn't exist
            ValueError: If recipe has no ingredients or is invalid YAML
        """
        if not recipe_path.exists():
            raise FileNotFoundError(f"Recipe file not found: {recipe_path}")

        try:
            with open(recipe_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()

            # Fix common YAML escape sequence issues
            # These are from malformed string escapes in the source data
            # Replace any \xNN sequences with degree symbol as placeholder
            content = re.sub(r'\\x[0-9A-Fa-f]{2}', '°', content)

            recipe = yaml.safe_load(content)
        except (yaml.YAMLError, yaml.scanner.ScannerError) as e:
            raise ValueError(f"Invalid YAML in {recipe_path}: {e}")

        if not isinstance(recipe, dict):
            raise ValueError(f"Recipe is not a dictionary: {recipe_path}")

        return self.fingerprint(recipe)
