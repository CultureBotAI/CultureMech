#!/usr/bin/env python3
"""
Infer sterilization methods for CultureMech recipes using rule-based heuristics.

This script adds sterilization descriptors when missing, using:
1. Solid agar media → AUTOCLAVE (high confidence)
2. Heat-sensitive ingredients → FILTER (high confidence)
3. Existing preparation steps → Extract autoclave info
4. Liquid media without heat-sensitive → AUTOCLAVE (medium confidence)
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Dict, Any, Optional, List
import yaml
from datetime import datetime, timezone

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


class SterilizationInferrer:
    """Infer sterilization methods for culture media recipes."""

    # Heat-sensitive ingredients that indicate filter sterilization
    HEAT_SENSITIVE_KEYWORDS = [
        'vitamin', 'antibiotic', 'serum', 'blood', 'enzyme',
        'protein', 'peptide', 'growth factor', 'hormone',
        'thiamine', 'biotin', 'cobalamin', 'folic acid',
        'penicillin', 'streptomycin', 'ampicillin', 'kanamycin'
    ]

    def __init__(self, dry_run: bool = False):
        """Initialize inferrer."""
        self.dry_run = dry_run
        self.stats = {
            'files_processed': 0,
            'sterilization_added': 0,
            'already_has_sterilization': 0,
            'inference_methods': {
                'solid_agar_autoclave': 0,
                'heat_sensitive_filter': 0,
                'prep_steps_autoclave': 0,
                'liquid_default_autoclave': 0,
                'no_inference': 0
            }
        }

    def has_heat_sensitive_ingredients(self, recipe: Dict[str, Any]) -> bool:
        """Check if recipe contains heat-sensitive ingredients."""
        ingredients_text = ' '.join([
            ing.get('preferred_term', '').lower()
            for ing in recipe.get('ingredients', [])
        ])

        # Also check solution names
        for solution in recipe.get('solutions', []):
            ingredients_text += ' ' + solution.get('name', '').lower()
            for ing in solution.get('ingredients', []):
                ingredients_text += ' ' + ing.get('preferred_term', '').lower()

        return any(keyword in ingredients_text for keyword in self.HEAT_SENSITIVE_KEYWORDS)

    def extract_from_prep_steps(self, recipe: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """Extract sterilization info from preparation steps."""
        for step in recipe.get('preparation_steps', []):
            action = step.get('action', '').upper()
            if 'AUTOCLAVE' in action or 'STERILIZE' in action:
                return {
                    'method': 'AUTOCLAVE',
                    'notes': 'Extracted from preparation steps',
                    'curation_flags': ['extracted_from_prep_steps']
                }
            elif 'FILTER' in action:
                return {
                    'method': 'FILTER',
                    'pore_size': '0.22',
                    'pore_size_unit': 'MICROMETER',
                    'notes': 'Extracted from preparation steps',
                    'curation_flags': ['extracted_from_prep_steps']
                }
        return None

    def infer_sterilization(self, recipe: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """
        Infer sterilization method using rule-based logic.

        Returns:
            Sterilization descriptor dict, or None if no safe inference
        """
        # Rule 1: Check preparation steps first
        from_prep = self.extract_from_prep_steps(recipe)
        if from_prep:
            self.stats['inference_methods']['prep_steps_autoclave'] += 1
            return from_prep

        # Rule 2: Solid agar → AUTOCLAVE (high confidence)
        if recipe.get('physical_state') == 'SOLID_AGAR':
            self.stats['inference_methods']['solid_agar_autoclave'] += 1
            return {
                'method': 'AUTOCLAVE',
                'temperature': 121,
                'temperature_unit': 'CELSIUS',
                'duration': '15-20 min',
                'pressure': '15 psi',
                'notes': 'Inferred from solid agar medium (high confidence)',
                'curation_flags': ['inferred', 'high_confidence']
            }

        # Rule 3: Heat-sensitive ingredients → FILTER (high confidence)
        if self.has_heat_sensitive_ingredients(recipe):
            self.stats['inference_methods']['heat_sensitive_filter'] += 1
            return {
                'method': 'FILTER',
                'pore_size': '0.22',
                'pore_size_unit': 'MICROMETER',
                'notes': 'Inferred from heat-sensitive ingredients (high confidence)',
                'curation_flags': ['inferred', 'high_confidence']
            }

        # Rule 4: Liquid media → AUTOCLAVE (medium confidence)
        if recipe.get('physical_state') == 'LIQUID':
            self.stats['inference_methods']['liquid_default_autoclave'] += 1
            return {
                'method': 'AUTOCLAVE',
                'temperature': 121,
                'temperature_unit': 'CELSIUS',
                'duration': '15-20 min',
                'notes': 'Inferred default for liquid medium (medium confidence)',
                'curation_flags': ['inferred', 'medium_confidence']
            }

        # No safe inference
        self.stats['inference_methods']['no_inference'] += 1
        return None

    def add_curation_history(self, recipe: Dict[str, Any], action: str) -> None:
        """Add curation history entry."""
        if 'curation_history' not in recipe:
            recipe['curation_history'] = []

        recipe['curation_history'].append({
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'curator': 'infer_sterilization_method.py',
            'action': action,
            'notes': 'Automated sterilization method inference'
        })

    def process_file(self, yaml_file: Path) -> bool:
        """Process a single recipe file."""
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                recipe = yaml.safe_load(f)

            if not recipe:
                return False

            # Skip if already has sterilization
            if recipe.get('sterilization'):
                self.stats['already_has_sterilization'] += 1
                return False

            # Infer sterilization
            sterilization = self.infer_sterilization(recipe)

            if sterilization:
                if not self.dry_run:
                    recipe['sterilization'] = sterilization
                    self.add_curation_history(recipe, 'STERILIZATION_INFERRED')

                    # Write back
                    with open(yaml_file, 'w', encoding='utf-8') as f:
                        yaml.dump(recipe, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

                self.stats['sterilization_added'] += 1
                return True

            return False

        except Exception as e:
            logger.error(f"Error processing {yaml_file}: {e}")
            return False

    def process_directory(self, yaml_dir: Path, category: Optional[str] = None, limit: Optional[int] = None) -> None:
        """Process all recipe files in a directory."""
        logger.info("=" * 60)
        logger.info("Sterilization Method Inference")
        logger.info("=" * 60)

        if self.dry_run:
            logger.info("DRY RUN MODE - no files will be modified")

        # Find files
        if category:
            pattern = f"{category}/*.yaml"
            logger.info(f"Processing category: {category}")
        else:
            pattern = "*/*.yaml"
            logger.info("Processing all categories")

        files = sorted(yaml_dir.glob(pattern))
        logger.info(f"Found {len(files)} recipe files")

        if limit:
            files = files[:limit]
            logger.info(f"Limited to {limit} files for testing")

        # Process files
        for i, yaml_file in enumerate(files, 1):
            if i % 100 == 0:
                logger.info(f"Progress: {i}/{len(files)} files processed...")

            self.process_file(yaml_file)
            self.stats['files_processed'] += 1

        # Print summary
        logger.info("\n" + "=" * 60)
        logger.info("Inference Complete")
        logger.info("=" * 60)
        logger.info(f"Files processed: {self.stats['files_processed']}")
        logger.info(f"Sterilization added: {self.stats['sterilization_added']}")
        logger.info(f"Already has sterilization: {self.stats['already_has_sterilization']}")
        logger.info("\nInference methods breakdown:")
        for method, count in self.stats['inference_methods'].items():
            if count > 0:
                logger.info(f"  {method}: {count}")
        logger.info("=" * 60)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Infer sterilization methods for CultureMech recipes"
    )

    parser.add_argument(
        '--yaml-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Directory containing recipe YAML files'
    )

    parser.add_argument(
        '--category',
        choices=['bacterial', 'fungal', 'archaea', 'algae', 'specialized', 'imported'],
        help='Process only specified category'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of files (for testing)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without modifying files'
    )

    args = parser.parse_args()

    if not args.yaml_dir.exists():
        logger.error(f"Directory not found: {args.yaml_dir}")
        return 1

    inferrer = SterilizationInferrer(dry_run=args.dry_run)
    inferrer.process_directory(args.yaml_dir, args.category, args.limit)

    return 0


if __name__ == '__main__':
    sys.exit(main())
