"""Apply MediaIngredientMech hierarchy to CultureMech recipes."""

import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
import yaml

from .hierarchy_importer import MediaIngredientMechHierarchyImporter

logger = logging.getLogger(__name__)


class HierarchyEnricher:
    """Enrich CultureMech recipes with hierarchy from MediaIngredientMech."""

    def __init__(self, hierarchy_importer: MediaIngredientMechHierarchyImporter):
        """
        Initialize enricher with loaded hierarchy.

        Args:
            hierarchy_importer: MediaIngredientMechHierarchyImporter with loaded data
        """
        self.importer = hierarchy_importer
        self.stats = {
            'files_processed': 0,
            'files_modified': 0,
            'ingredients_enriched': 0,
            'solutions_enriched': 0,
            'already_has_hierarchy': 0,
            'no_mim_id': 0,
            'no_parent_found': 0,
            'errors': 0
        }
        self.enrichment_details: List[Dict[str, Any]] = []

    def enrich_ingredient(self, ingredient: Dict[str, Any]) -> bool:
        """
        Add parent_ingredient and variant_type fields to an ingredient.

        Matches ingredient to MediaIngredientMech hierarchy:
        1. Check if ingredient has mediaingredientmech_term
        2. Look up parent in hierarchy
        3. Add parent_ingredient and variant_type if found

        Args:
            ingredient: Ingredient descriptor dict

        Returns:
            True if enriched, False otherwise
        """
        # Skip if already has hierarchy fields
        if 'parent_ingredient' in ingredient or 'variant_type' in ingredient:
            self.stats['already_has_hierarchy'] += 1
            return False

        # Check if ingredient has MediaIngredientMech ID
        mim_term = ingredient.get('mediaingredientmech_term')
        if not mim_term:
            self.stats['no_mim_id'] += 1
            return False

        mim_id = mim_term.get('id') if isinstance(mim_term, dict) else None
        if not mim_id:
            self.stats['no_mim_id'] += 1
            return False

        # Look up parent in hierarchy
        parent_info = self.importer.get_parent(mim_id)
        if not parent_info:
            self.stats['no_parent_found'] += 1
            return False

        # Get variant type
        variant_type = self.importer.get_variant_type(mim_id)

        # Add parent_ingredient field
        ingredient['parent_ingredient'] = {
            'preferred_term': parent_info.get('name', ''),
            'mediaingredientmech_id': parent_info.get('id')
        }

        # Add variant_type field if available
        if variant_type:
            ingredient['variant_type'] = variant_type

        self.stats['ingredients_enriched'] += 1

        # Track enrichment details
        self.enrichment_details.append({
            'ingredient_name': ingredient.get('preferred_term', ''),
            'mim_id': mim_id,
            'parent_name': parent_info.get('name', ''),
            'parent_id': parent_info.get('id'),
            'variant_type': variant_type
        })

        return True

    def enrich_solution(self, solution: Dict[str, Any]) -> int:
        """
        Add hierarchy to solution composition ingredients.

        Args:
            solution: Solution descriptor dict

        Returns:
            Number of ingredients enriched
        """
        enriched_count = 0

        # Process composition ingredients
        composition = solution.get('composition', [])
        if isinstance(composition, list):
            for ingredient in composition:
                if isinstance(ingredient, dict):
                    if self.enrich_ingredient(ingredient):
                        enriched_count += 1

        if enriched_count > 0:
            self.stats['solutions_enriched'] += 1

        return enriched_count

    def enrich_recipe(self, recipe_path: Path, dry_run: bool = False) -> bool:
        """
        Process single recipe file and add hierarchy.

        Args:
            recipe_path: Path to recipe YAML file
            dry_run: If True, don't save changes

        Returns:
            True if file was modified, False otherwise
        """
        try:
            with open(recipe_path, 'r', encoding='utf-8') as f:
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
                    'curator': 'hierarchy-enrichment-v1.0',
                    'action': 'Added ingredient hierarchy from MediaIngredientMech',
                    'notes': 'Added parent_ingredient and variant_type fields'
                })

                # Save updated file
                with open(recipe_path, 'w', encoding='utf-8') as f:
                    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

                logger.debug(f"  ✓ Updated {recipe_path.name}")

            if modified:
                self.stats['files_modified'] += 1

            self.stats['files_processed'] += 1
            return modified

        except Exception as e:
            logger.error(f"  ✗ Failed to process {recipe_path.name}: {e}")
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
        Process all recipes with hierarchy enrichment.

        Args:
            yaml_dir: Directory containing normalized YAML files
            category: Optional category filter (bacterial, fungal, etc.)
            limit: Optional limit on number of files to process
            dry_run: If True, don't save changes

        Returns:
            Dictionary with statistics and enrichment details
        """
        logger.info("=" * 60)
        logger.info("Ingredient Hierarchy Enrichment Pipeline")
        logger.info("=" * 60)

        if dry_run:
            logger.info("DRY RUN MODE - no files will be modified")

        # Get hierarchy stats
        hierarchy_stats = self.importer.get_stats()
        logger.info(f"Hierarchy loaded: {hierarchy_stats['total_ingredients']} ingredients, "
                   f"{hierarchy_stats['parents']} parents, "
                   f"{hierarchy_stats['children']} children")

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
        logger.info("Hierarchy Enrichment Complete")
        logger.info("=" * 60)
        logger.info(f"Files processed: {self.stats['files_processed']}")
        logger.info(f"Files modified: {self.stats['files_modified']}")
        logger.info(f"Ingredients enriched: {self.stats['ingredients_enriched']}")
        logger.info(f"Solutions with enriched ingredients: {self.stats['solutions_enriched']}")
        logger.info(f"Already has hierarchy (skipped): {self.stats['already_has_hierarchy']}")
        logger.info(f"No MediaIngredientMech ID: {self.stats['no_mim_id']}")
        logger.info(f"No parent found: {self.stats['no_parent_found']}")

        if self.stats['errors'] > 0:
            logger.warning(f"Errors: {self.stats['errors']}")

        # Calculate coverage
        total_potential = (
            self.stats['ingredients_enriched'] +
            self.stats['no_parent_found']
        )
        if total_potential > 0:
            coverage = (self.stats['ingredients_enriched'] / total_potential) * 100
            logger.info(f"Hierarchy coverage: {coverage:.1f}% "
                       f"({self.stats['ingredients_enriched']}/{total_potential})")

        logger.info("=" * 60)

        return {
            'stats': self.stats,
            'hierarchy_stats': hierarchy_stats,
            'enrichment_details': self.enrichment_details[:100]  # First 100 for review
        }

    def generate_report(self, output_path: Path):
        """
        Generate detailed enrichment report.

        Args:
            output_path: Path to save report YAML
        """
        report = {
            'generation_date': time.strftime("%Y-%m-%dT%H:%M:%S.000000Z", time.gmtime()),
            'stats': self.stats,
            'hierarchy_stats': self.importer.get_stats(),
            'sample_enrichments': self.enrichment_details[:50]
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(report, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        logger.info(f"Report saved to {output_path}")
