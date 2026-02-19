"""DSMZ composition resolution for KOMODO recipes.

Resolves empty KOMODO recipes by copying ingredient compositions from
corresponding DSMZ/MediaDive recipes.
"""

import logging
import re
from copy import deepcopy
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import yaml

logger = logging.getLogger(__name__)


class DSMZCompositionResolver:
    """Resolve KOMODO empty recipes with DSMZ compositions.

    KOMODO web importer creates placeholder recipes with empty ingredients
    for recipes that reference DSMZ media. This resolver:
    1. Extracts DSMZ medium numbers from KOMODO recipe notes
    2. Finds matching DSMZ/MediaDive recipes in normalized_yaml
    3. Copies ingredients and solutions to KOMODO recipes
    4. Adds enrichment provenance to curation_history
    """

    def __init__(self, normalized_dir: Path):
        """Initialize the resolver.

        Args:
            normalized_dir: Path to normalized_yaml directory
        """
        self.normalized_dir = Path(normalized_dir)

        # Build index of DSMZ recipes by medium number
        self.dsmz_index = self._build_dsmz_index()

        logger.info(f"Indexed {len(self.dsmz_index)} DSMZ media")

    def _build_dsmz_index(self) -> Dict[str, Path]:
        """Build index of DSMZ medium numbers to recipe files.

        Returns:
            Dictionary mapping DSMZ medium numbers (e.g., "457") to file paths
        """
        index = {}

        # Find all DSMZ recipe files
        dsmz_files = list(self.normalized_dir.rglob("DSMZ_*.yaml"))

        for recipe_path in dsmz_files:
            try:
                with open(recipe_path, 'r', encoding='utf-8') as f:
                    recipe = yaml.safe_load(f)

                # Extract medium number from media_term.term.id
                # Format: mediadive.medium:457
                if 'media_term' in recipe and isinstance(recipe['media_term'], dict):
                    term = recipe['media_term'].get('term', {})
                    if isinstance(term, dict):
                        medium_id = term.get('id', '')
                        if medium_id.startswith('mediadive.medium:'):
                            # Extract number after colon
                            medium_num = medium_id.split(':')[1]
                            # Remove variant suffixes (457b -> 457)
                            base_num = re.sub(r'[a-z].*$', '', medium_num)
                            index[base_num] = recipe_path
                            logger.debug(f"Indexed DSMZ medium {base_num}: {recipe_path.name}")

            except Exception as e:
                logger.warning(f"Could not index {recipe_path}: {e}")

        return index

    def extract_dsmz_id(self, recipe: Dict) -> Optional[str]:
        """Extract DSMZ medium number from KOMODO recipe notes.

        Args:
            recipe: KOMODO recipe dictionary

        Returns:
            DSMZ medium number (e.g., "457") or None
        """
        notes = recipe.get('notes', '')
        if not notes:
            return None

        # Pattern: "DSMZ Medium: 457 (mediadive.medium:457)"
        match = re.search(r'DSMZ Medium:\s*(\d+[a-z]?)\s*\(mediadive\.medium:(\d+[a-z]?)\)', notes)
        if match:
            medium_num = match.group(1)
            # Remove variant suffixes
            base_num = re.sub(r'[a-z].*$', '', medium_num)
            return base_num

        return None

    def find_dsmz_recipe(self, dsmz_id: str) -> Optional[Path]:
        """Find DSMZ recipe file by medium number.

        Args:
            dsmz_id: DSMZ medium number (e.g., "457")

        Returns:
            Path to recipe file or None
        """
        return self.dsmz_index.get(dsmz_id)

    def merge_composition(
        self,
        target_recipe: Dict,
        source_recipe: Dict,
        source_id: str
    ) -> Dict:
        """Copy ingredients and solutions from source to target recipe.

        Args:
            target_recipe: KOMODO recipe to enrich
            source_recipe: DSMZ recipe with composition
            source_id: DSMZ medium number for provenance

        Returns:
            Enriched recipe
        """
        target = deepcopy(target_recipe)

        # Copy ingredients (excluding placeholders)
        if 'ingredients' in source_recipe:
            ingredients = source_recipe['ingredients']

            # Filter out placeholder ingredients
            real_ingredients = [
                ing for ing in ingredients
                if not self._is_placeholder(ing.get('preferred_term', ''))
            ]

            if real_ingredients:
                target['ingredients'] = real_ingredients
                logger.info(f"Copied {len(real_ingredients)} ingredients from DSMZ {source_id}")
            else:
                logger.warning(f"DSMZ {source_id} has only placeholder ingredients")

        # Copy solutions if present
        if 'solutions' in source_recipe and source_recipe['solutions']:
            target['solutions'] = deepcopy(source_recipe['solutions'])
            logger.info(f"Copied {len(source_recipe['solutions'])} solutions from DSMZ {source_id}")

        # Copy pH if available and not already set
        if 'ph_value' in source_recipe and 'ph_value' not in target:
            target['ph_value'] = source_recipe['ph_value']

        # Copy physical_state if available and target is not set properly
        if 'physical_state' in source_recipe:
            target['physical_state'] = source_recipe['physical_state']

        # Copy medium_type if available
        if 'medium_type' in source_recipe:
            target['medium_type'] = source_recipe['medium_type']

        # Add enrichment metadata
        self._add_enrichment_metadata(target, source_id)

        return target

    def _is_placeholder(self, ingredient_name: str) -> bool:
        """Check if ingredient is a placeholder.

        Args:
            ingredient_name: Ingredient preferred_term

        Returns:
            True if placeholder
        """
        if not ingredient_name:
            return False

        placeholder_patterns = [
            r'see\s+source',
            r'refer\s+to',
            r'available\s+at',
            r'not\s+specified',
            r'unknown',
        ]

        name_lower = ingredient_name.lower()
        for pattern in placeholder_patterns:
            if re.search(pattern, name_lower):
                return True

        return False

    def _add_enrichment_metadata(self, recipe: Dict, source_id: str):
        """Add curation history entry for enrichment.

        Args:
            recipe: Recipe to update
            source_id: DSMZ medium number
        """
        if 'curation_history' not in recipe:
            recipe['curation_history'] = []

        entry = {
            'timestamp': datetime.now().isoformat(),
            'curator': 'dsmz-resolver-v1.0',
            'action': 'Enriched with DSMZ composition',
            'notes': f'Copied ingredients from DSMZ Medium {source_id}'
        }

        recipe['curation_history'].append(entry)

    def resolve_recipe(
        self,
        recipe_path: Path
    ) -> Tuple[Optional[Dict], Optional[str]]:
        """Resolve a single KOMODO recipe.

        Args:
            recipe_path: Path to KOMODO recipe file

        Returns:
            Tuple of (enriched_recipe, error_message)
            If successful, returns (recipe, None)
            If failed, returns (None, error_message)
        """
        try:
            # Load recipe
            with open(recipe_path, 'r', encoding='utf-8') as f:
                recipe = yaml.safe_load(f)

            # Check if it's a KOMODO recipe with empty ingredients
            if not recipe_path.name.startswith('KOMODO_'):
                return None, "Not a KOMODO recipe"

            if 'ingredients' not in recipe:
                return None, "No ingredients field"

            if len(recipe.get('ingredients', [])) > 0:
                return None, "Already has ingredients"

            # Extract DSMZ ID
            dsmz_id = self.extract_dsmz_id(recipe)
            if not dsmz_id:
                return None, "Could not extract DSMZ medium number"

            # Find DSMZ recipe
            dsmz_path = self.find_dsmz_recipe(dsmz_id)
            if not dsmz_path:
                return None, f"DSMZ medium {dsmz_id} not found"

            # Load DSMZ recipe
            with open(dsmz_path, 'r', encoding='utf-8') as f:
                dsmz_recipe = yaml.safe_load(f)

            # Check if DSMZ recipe has ingredients
            if not dsmz_recipe.get('ingredients'):
                return None, f"DSMZ medium {dsmz_id} has no ingredients"

            # Merge compositions
            enriched = self.merge_composition(recipe, dsmz_recipe, dsmz_id)

            return enriched, None

        except Exception as e:
            return None, f"Error resolving recipe: {e}"

    def resolve_directory(
        self,
        dry_run: bool = False
    ) -> Dict[str, int]:
        """Resolve all KOMODO recipes with empty ingredients.

        Args:
            dry_run: If True, don't write files

        Returns:
            Dictionary of statistics
        """
        stats = {
            'total_komodo': 0,
            'empty_ingredients': 0,
            'resolved': 0,
            'failed': 0,
            'already_complete': 0,
            'failures': []
        }

        # Find all KOMODO recipes
        komodo_files = list(self.normalized_dir.rglob("KOMODO_*.yaml"))
        stats['total_komodo'] = len(komodo_files)

        logger.info(f"Found {len(komodo_files)} KOMODO recipes")

        for recipe_path in komodo_files:
            try:
                # Load and check recipe
                with open(recipe_path, 'r', encoding='utf-8') as f:
                    recipe = yaml.safe_load(f)

                # Skip if not empty
                if recipe.get('ingredients') and len(recipe['ingredients']) > 0:
                    stats['already_complete'] += 1
                    continue

                stats['empty_ingredients'] += 1

                # Try to resolve
                enriched, error = self.resolve_recipe(recipe_path)

                if enriched:
                    stats['resolved'] += 1

                    if not dry_run:
                        # Write enriched recipe
                        with open(recipe_path, 'w', encoding='utf-8') as f:
                            yaml.safe_dump(
                                enriched,
                                f,
                                default_flow_style=False,
                                allow_unicode=True,
                                sort_keys=False
                            )
                        logger.info(f"✓ Resolved {recipe_path.name}")
                    else:
                        logger.info(f"Would resolve {recipe_path.name}")

                else:
                    stats['failed'] += 1
                    stats['failures'].append({
                        'file': recipe_path.name,
                        'error': error
                    })
                    logger.debug(f"✗ Could not resolve {recipe_path.name}: {error}")

            except Exception as e:
                stats['failed'] += 1
                stats['failures'].append({
                    'file': recipe_path.name,
                    'error': str(e)
                })
                logger.error(f"Error processing {recipe_path}: {e}")

        return stats
