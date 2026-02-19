"""Schema field defaulting and normalization for CultureMech recipes.

Handles missing required fields, enum normalization, and type coercion
to maximize successful schema validation.
"""

import logging
from copy import deepcopy
from datetime import datetime
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class SchemaDefaulter:
    """Apply defaults and normalizations to recipe data for schema compliance.

    Strategies:
    1. Add missing required fields with sensible defaults
    2. Normalize enum values (case conversion)
    3. Coerce common type mismatches
    4. Track all changes in curation_history
    """

    # Valid enum values from schema
    CONCENTRATION_UNITS = {
        'G_PER_L', 'MG_PER_L', 'UG_PER_L', 'PERCENT', 'MOLAR', 'MILLIMOLAR',
        'MICROMOLAR', 'ML_PER_L', 'DROPS', 'TO_1L', 'GRAINS', 'TABLETS',
        'TRACE', 'VARIABLE'
    }

    CATEGORY_ENUM = {
        'BACTERIA', 'ARCHAEA', 'FUNGI', 'ALGAE', 'PROTOZOA', 'VIRUS',
        'GENERAL', 'UNKNOWN'
    }

    MODIFIER_ENUM = {
        'INCREASED', 'DECREASED', 'OMITTED', 'SUBSTITUTED'
    }

    STERILIZATION_METHODS = {
        'AUTOCLAVE', 'FILTER', 'PASTEURIZE', 'UV', 'CHEMICAL', 'NONE'
    }

    def __init__(self):
        """Initialize the schema defaulter."""
        self.changes_made = []

    def apply_defaults(self, recipe: Dict) -> Dict:
        """Apply defaults for missing required fields.

        Args:
            recipe: Recipe dictionary

        Returns:
            Recipe with defaults applied
        """
        recipe = deepcopy(recipe)
        self.changes_made = []

        # If ingredients field is completely missing, add placeholder
        if 'ingredients' not in recipe:
            recipe['ingredients'] = [{
                'preferred_term': 'See source for composition',
                'concentration': {
                    'value': 'variable',
                    'unit': 'VARIABLE'
                }
            }]
            self.changes_made.append("Added placeholder ingredients for missing composition")
        elif isinstance(recipe['ingredients'], list):
            # Ensure ingredients have required concentration field
            recipe['ingredients'] = [
                self._fix_ingredient(ing) for ing in recipe['ingredients']
            ]

        # Fix solutions if present
        if 'solutions' in recipe:
            recipe['solutions'] = [
                self._fix_solution(sol) for sol in recipe['solutions']
            ]

        # Add curation history entry if changes were made
        if self.changes_made:
            self._add_curation_entry(recipe)

        return recipe

    def _fix_ingredient(self, ingredient: Dict) -> Dict:
        """Fix a single ingredient to meet schema requirements.

        Args:
            ingredient: Ingredient dictionary

        Returns:
            Fixed ingredient
        """
        ingredient = deepcopy(ingredient)

        # Ensure concentration field exists (required)
        if 'concentration' not in ingredient:
            # Check if there's a raw concentration string we can parse
            ingredient['concentration'] = {
                'value': 'variable',
                'unit': 'VARIABLE'
            }
            self.changes_made.append(
                f"Added default concentration for ingredient: {ingredient.get('preferred_term', 'unknown')}"
            )
        elif isinstance(ingredient['concentration'], dict):
            # Fix concentration subfields
            conc = ingredient['concentration']

            if 'value' not in conc:
                conc['value'] = 'variable'
                self.changes_made.append(
                    f"Added default concentration value for: {ingredient.get('preferred_term', 'unknown')}"
                )

            if 'unit' not in conc:
                conc['unit'] = 'VARIABLE'
                self.changes_made.append(
                    f"Added default concentration unit for: {ingredient.get('preferred_term', 'unknown')}"
                )
            else:
                # Normalize unit enum
                conc['unit'] = self._normalize_enum(conc['unit'], self.CONCENTRATION_UNITS)

        # Ensure preferred_term exists (required)
        if 'preferred_term' not in ingredient:
            ingredient['preferred_term'] = 'Unknown ingredient'
            self.changes_made.append("Added default preferred_term")

        return ingredient

    def _fix_solution(self, solution: Dict) -> Dict:
        """Fix a solution to meet schema requirements.

        Args:
            solution: Solution dictionary

        Returns:
            Fixed solution
        """
        solution = deepcopy(solution)

        # Fix composition ingredients
        if 'composition' in solution:
            solution['composition'] = [
                self._fix_ingredient(ing) for ing in solution['composition']
            ]

        # Ensure name exists
        if 'name' not in solution:
            solution['name'] = 'Unknown solution'
            self.changes_made.append("Added default solution name")

        return solution

    def _normalize_enum(self, value: str, valid_values: set) -> str:
        """Normalize enum value to match schema.

        Args:
            value: Raw enum value
            valid_values: Set of valid enum values

        Returns:
            Normalized enum value
        """
        if not isinstance(value, str):
            return str(value).upper()

        # Try uppercase match
        upper_value = value.upper()
        if upper_value in valid_values:
            return upper_value

        # Try replacing spaces/hyphens with underscores
        normalized = upper_value.replace(' ', '_').replace('-', '_')
        if normalized in valid_values:
            self.changes_made.append(f"Normalized enum '{value}' to '{normalized}'")
            return normalized

        # Return original if no match found
        logger.warning(f"Could not normalize enum value: {value}")
        return value

    def normalize_enums(self, recipe: Dict) -> Dict:
        """Normalize all enum values in recipe.

        Args:
            recipe: Recipe dictionary

        Returns:
            Recipe with normalized enums
        """
        recipe = deepcopy(recipe)
        self.changes_made = []

        # Normalize category
        if 'category' in recipe:
            recipe['category'] = self._normalize_enum(
                recipe['category'],
                self.CATEGORY_ENUM
            )

        # Normalize categories (multivalued)
        if 'categories' in recipe:
            recipe['categories'] = [
                self._normalize_enum(cat, self.CATEGORY_ENUM)
                for cat in recipe['categories']
            ]

        # Normalize ingredient modifiers
        if 'ingredients' in recipe:
            for ing in recipe['ingredients']:
                if 'modifier' in ing:
                    ing['modifier'] = self._normalize_enum(
                        ing['modifier'],
                        self.MODIFIER_ENUM
                    )

        # Normalize sterilization method
        if 'sterilization' in recipe and isinstance(recipe['sterilization'], dict):
            if 'method' in recipe['sterilization']:
                recipe['sterilization']['method'] = self._normalize_enum(
                    recipe['sterilization']['method'],
                    self.STERILIZATION_METHODS
                )

        # Add curation history if changes were made
        if self.changes_made:
            self._add_curation_entry(recipe)

        return recipe

    def coerce_types(self, recipe: Dict) -> Dict:
        """Coerce common type mismatches.

        Args:
            recipe: Recipe dictionary

        Returns:
            Recipe with type corrections
        """
        recipe = deepcopy(recipe)
        self.changes_made = []

        # Ensure name is string
        if 'name' in recipe and not isinstance(recipe['name'], str):
            recipe['name'] = str(recipe['name'])
            self.changes_made.append("Coerced name to string")

        # Ensure pH is float if present
        if 'ph' in recipe and recipe['ph'] is not None:
            try:
                if isinstance(recipe['ph'], str):
                    # Remove common prefixes/suffixes
                    ph_str = recipe['ph'].replace('pH', '').replace('~', '').strip()
                    recipe['ph'] = float(ph_str)
                    self.changes_made.append(f"Coerced pH to float: {recipe['ph']}")
            except (ValueError, AttributeError):
                logger.warning(f"Could not coerce pH value: {recipe['ph']}")

        # Ensure temperature_value is float if present
        if 'temperature_value' in recipe and recipe['temperature_value'] is not None:
            try:
                recipe['temperature_value'] = float(recipe['temperature_value'])
            except (ValueError, TypeError):
                logger.warning(f"Could not coerce temperature_value: {recipe['temperature_value']}")

        # Add curation history if changes were made
        if self.changes_made:
            self._add_curation_entry(recipe)

        return recipe

    def _add_curation_entry(self, recipe: Dict):
        """Add curation history entry for changes made.

        Args:
            recipe: Recipe dictionary to update
        """
        if 'curation_history' not in recipe:
            recipe['curation_history'] = []

        entry = {
            'curator': 'schema-defaulter-v1.0',
            'date': datetime.now().isoformat(),
            'action': 'Applied schema defaults and normalizations',
            'notes': '; '.join(self.changes_made)
        }

        recipe['curation_history'].append(entry)
