"""Pipeline for enriching CultureMech recipes with MediaIngredientMech identifiers."""

import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
import yaml

from .mediaingredientmech_loader import MediaIngredientMechLoader

logger = logging.getLogger(__name__)


class MediaIngredientMechLinker:
    """Link CultureMech ingredients to MediaIngredientMech identifiers."""

    def __init__(self, loader: MediaIngredientMechLoader):
        """
        Initialize linker with a loaded MediaIngredientMech dataset.

        Args:
            loader: MediaIngredientMechLoader with data loaded
        """
        self.loader = loader
        self.stats = {
            "files_processed": 0,
            "ingredients_matched": 0,
            "solutions_matched": 0,
            "no_match": 0,
            "already_linked": 0,
            "errors": 0,
            "match_methods": {}
        }
        self.unmatched_ingredients: List[Dict[str, str]] = []

    def enrich_ingredient(self, ingredient: Dict[str, Any]) -> bool:
        """
        Add mediaingredientmech_term to an ingredient if match found.

        Args:
            ingredient: Ingredient descriptor dict

        Returns:
            True if match found and added, False otherwise
        """
        # Skip if already has MediaIngredientMech link
        if 'mediaingredientmech_term' in ingredient:
            self.stats['already_linked'] += 1
            return False

        # Get ingredient name and CHEBI ID
        name = ingredient.get('preferred_term', '')
        chebi_id = None

        if 'term' in ingredient and isinstance(ingredient['term'], dict):
            chebi_id = ingredient['term'].get('id')

        # Find match
        match = self.loader.find_match(name, chebi_id)

        if match:
            mim_id = match.get('id')
            mim_name = match.get('name', name)
            match_method = match.get('match_method', 'unknown')

            # Add MediaIngredientMech term
            ingredient['mediaingredientmech_term'] = {
                'id': mim_id,
                'label': mim_name
            }

            # Track statistics
            self.stats['ingredients_matched'] += 1
            if match_method not in self.stats['match_methods']:
                self.stats['match_methods'][match_method] = 0
            self.stats['match_methods'][match_method] += 1

            return True
        else:
            # Track unmatched
            self.stats['no_match'] += 1
            self.unmatched_ingredients.append({
                'name': name,
                'chebi_id': chebi_id or 'N/A'
            })
            return False

    def enrich_solution(self, solution: Dict[str, Any]) -> int:
        """
        Add mediaingredientmech_term to solution composition ingredients.

        Args:
            solution: Solution descriptor dict

        Returns:
            Number of ingredients matched
        """
        matched_count = 0

        # Skip if already has MediaIngredientMech link at solution level
        if 'mediaingredientmech_term' in solution:
            self.stats['already_linked'] += 1

        # Process composition ingredients
        composition = solution.get('composition', [])
        if isinstance(composition, list):
            for ingredient in composition:
                if isinstance(ingredient, dict):
                    if self.enrich_ingredient(ingredient):
                        matched_count += 1

        if matched_count > 0:
            self.stats['solutions_matched'] += 1

        return matched_count

    def enrich_recipe(
        self,
        yaml_file: Path,
        dry_run: bool = False
    ) -> bool:
        """
        Process a single recipe YAML file and add MediaIngredientMech links.

        Args:
            yaml_file: Path to recipe YAML file
            dry_run: If True, don't save changes

        Returns:
            True if file was modified, False otherwise
        """
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            if not data:
                return False

            modified = False

            # Enrich direct ingredients
            ingredients = data.get('ingredients', [])
            if isinstance(ingredients, list):
                for ingredient in ingredients:
                    if isinstance(ingredient, dict):
                        if self.enrich_ingredient(ingredient):
                            modified = True

            # Enrich solution ingredients
            solutions = data.get('solutions', [])
            if isinstance(solutions, list):
                for solution in solutions:
                    if isinstance(solution, dict):
                        if self.enrich_solution(solution) > 0:
                            modified = True

            # Add curation history if modified
            if modified and not dry_run:
                if 'curation_history' not in data:
                    data['curation_history'] = []

                data['curation_history'].append({
                    'timestamp': time.strftime("%Y-%m-%dT%H:%M:%S.000000Z", time.gmtime()),
                    'curator': 'mediaingredientmech-enrichment-v1.0',
                    'action': 'Added MediaIngredientMech links',
                    'notes': f'Linked ingredients to MediaIngredientMech identifiers'
                })

                # Save updated file
                with open(yaml_file, 'w', encoding='utf-8') as f:
                    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

                logger.debug(f"  ✓ Updated {yaml_file.name}")

            if modified:
                self.stats['files_processed'] += 1

            return modified

        except Exception as e:
            logger.error(f"  ✗ Failed to process {yaml_file.name}: {e}")
            self.stats['errors'] += 1
            return False

    def run_pipeline(
        self,
        yaml_dir: Path,
        category: Optional[str] = None,
        limit: Optional[int] = None,
        dry_run: bool = False
    ) -> Dict[str, Any]:
        """
        Run enrichment pipeline on all recipe files.

        Args:
            yaml_dir: Directory containing normalized YAML files
            category: Optional category filter (bacterial, fungal, etc.)
            limit: Optional limit on number of files to process
            dry_run: If True, don't save changes

        Returns:
            Statistics dictionary
        """
        logger.info("=" * 60)
        logger.info("MediaIngredientMech Enrichment Pipeline")
        logger.info("=" * 60)

        if dry_run:
            logger.info("DRY RUN MODE - no files will be modified")

        # Find recipe files
        if category:
            pattern = f"{category}/**/*.yaml"
            logger.info(f"Processing category: {category}")
        else:
            pattern = "**/*.yaml"
            logger.info("Processing all categories")

        yaml_files = list(yaml_dir.glob(pattern))
        logger.info(f"Found {len(yaml_files)} recipe files")

        if limit:
            yaml_files = yaml_files[:limit]
            logger.info(f"Limited to {limit} files for testing")

        # Process files
        for i, yaml_file in enumerate(yaml_files, 1):
            if i % 100 == 0:
                logger.info(f"Progress: {i}/{len(yaml_files)} files processed...")

            self.enrich_recipe(yaml_file, dry_run)

        # Print summary
        logger.info("\n" + "=" * 60)
        logger.info("Enrichment Complete")
        logger.info("=" * 60)
        logger.info(f"Files processed: {self.stats['files_processed']}")
        logger.info(f"Ingredients matched: {self.stats['ingredients_matched']}")
        logger.info(f"Solutions with matched ingredients: {self.stats['solutions_matched']}")
        logger.info(f"Already linked (skipped): {self.stats['already_linked']}")
        logger.info(f"No match found: {self.stats['no_match']}")

        if self.stats['match_methods']:
            logger.info("\nMatch methods breakdown:")
            for method, count in sorted(self.stats['match_methods'].items()):
                logger.info(f"  {method}: {count}")

        if self.stats['errors'] > 0:
            logger.warning(f"Errors: {self.stats['errors']}")

        logger.info("=" * 60)

        return {
            'stats': self.stats,
            'unmatched_ingredients': self.unmatched_ingredients
        }
