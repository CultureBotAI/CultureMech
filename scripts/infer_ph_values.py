#!/usr/bin/env python3
"""
Extract and infer pH values for CultureMech recipes.

This script:
1. Extracts pH from notes/description fields using regex patterns
2. Applies safe category-based defaults when no pH found
3. Tags inferred values with curation flags for transparency
"""

import argparse
import logging
import re
import sys
from pathlib import Path
from typing import Dict, Any, Optional
import yaml
from datetime import datetime, timezone

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


class pHInferrer:
    """Extract and infer pH values for culture media recipes."""

    # pH patterns to search for in text
    PH_PATTERNS = [
        r'ph[:\s=]+(\d+\.?\d*)',
        r'adjusted\s+to\s+ph\s+(\d+\.?\d*)',
        r'final\s+ph\s+(\d+\.?\d*)',
        r'ph\s+(\d+\.?\d*)',
        r'ph=(\d+\.?\d*)',
    ]

    # Safe pH defaults by organism category
    PH_DEFAULTS = {
        'bacterial': 7.0,    # Neutral
        'fungal': 5.5,       # Slightly acidic
        'archaea': 7.2,      # Near-neutral
        'algae': 7.5,        # Photosynthetic optimal
        'specialized': 7.0,  # Neutral default
    }

    def __init__(self, dry_run: bool = False):
        """Initialize inferrer."""
        self.dry_run = dry_run
        self.stats = {
            'files_processed': 0,
            'ph_added': 0,
            'already_has_ph': 0,
            'extraction_methods': {
                'extracted_from_text': 0,
                'category_default': 0,
                'no_inference': 0
            }
        }

    def extract_ph_from_text(self, recipe: Dict[str, Any]) -> Optional[float]:
        """Extract pH value from notes/description fields."""
        # Combine all text fields
        text = ' '.join([
            recipe.get('notes', ''),
            recipe.get('description', ''),
            recipe.get('name', '')
        ]).lower()

        # Try each pattern
        for pattern in self.PH_PATTERNS:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                try:
                    ph = float(match.group(1))
                    # Sanity check - pH should be in valid range
                    if 0.0 <= ph <= 14.0:
                        # Most culture media are between 4-10
                        if 4.0 <= ph <= 10.0:
                            return ph
                        # Allow wider range but log warning
                        elif 0.0 < ph < 14.0:
                            logger.warning(f"Unusual pH {ph} in {recipe.get('name', 'unknown')}")
                            return ph
                except (ValueError, IndexError):
                    continue

        return None

    def infer_ph_default(self, recipe: Dict[str, Any]) -> Optional[float]:
        """Apply safe pH default based on organism category."""
        category = recipe.get('category', '')

        # Get default for category
        default_ph = self.PH_DEFAULTS.get(category)

        if default_ph:
            return default_ph

        # No safe default available
        return None

    def add_curation_history(self, recipe: Dict[str, Any], action: str, notes: str) -> None:
        """Add curation history entry."""
        if 'curation_history' not in recipe:
            recipe['curation_history'] = []

        recipe['curation_history'].append({
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'curator': 'infer_ph_values.py',
            'action': action,
            'notes': notes
        })

    def process_file(self, yaml_file: Path) -> bool:
        """Process a single recipe file."""
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                recipe = yaml.safe_load(f)

            if not recipe:
                return False

            # Skip if already has pH
            if recipe.get('ph_value') or recipe.get('ph'):
                self.stats['already_has_ph'] += 1
                return False

            modified = False

            # Try to extract from text first
            extracted_ph = self.extract_ph_from_text(recipe)

            if extracted_ph:
                if not self.dry_run:
                    recipe['ph_value'] = extracted_ph
                    self.add_curation_history(
                        recipe,
                        'PH_EXTRACTED',
                        f'Extracted pH {extracted_ph} from text fields'
                    )

                self.stats['extraction_methods']['extracted_from_text'] += 1
                self.stats['ph_added'] += 1
                modified = True

            else:
                # Fall back to category default
                default_ph = self.infer_ph_default(recipe)

                if default_ph:
                    if not self.dry_run:
                        recipe['ph_value'] = default_ph

                        # Add curation flags to indicate this is inferred
                        if 'data_quality_flags' not in recipe:
                            recipe['data_quality_flags'] = []
                        if 'ph_inferred' not in recipe['data_quality_flags']:
                            recipe['data_quality_flags'].append('ph_inferred')

                        category = recipe.get('category', 'unknown')
                        self.add_curation_history(
                            recipe,
                            'PH_INFERRED',
                            f'Inferred default pH {default_ph} for {category} media'
                        )

                    self.stats['extraction_methods']['category_default'] += 1
                    self.stats['ph_added'] += 1
                    modified = True
                else:
                    self.stats['extraction_methods']['no_inference'] += 1

            # Write back if modified
            if modified and not self.dry_run:
                with open(yaml_file, 'w', encoding='utf-8') as f:
                    yaml.dump(recipe, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

            return modified

        except Exception as e:
            logger.error(f"Error processing {yaml_file}: {e}")
            return False

    def process_directory(
        self,
        yaml_dir: Path,
        category: Optional[str] = None,
        limit: Optional[int] = None
    ) -> None:
        """Process all recipe files in a directory."""
        logger.info("=" * 60)
        logger.info("pH Value Extraction and Inference")
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
        logger.info("pH Inference Complete")
        logger.info("=" * 60)
        logger.info(f"Files processed: {self.stats['files_processed']}")
        logger.info(f"pH values added: {self.stats['ph_added']}")
        logger.info(f"Already has pH: {self.stats['already_has_ph']}")
        logger.info("\nExtraction methods breakdown:")
        for method, count in self.stats['extraction_methods'].items():
            if count > 0:
                logger.info(f"  {method}: {count}")
        logger.info("=" * 60)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Extract and infer pH values for CultureMech recipes"
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

    inferrer = pHInferrer(dry_run=args.dry_run)
    inferrer.process_directory(args.yaml_dir, args.category, args.limit)

    return 0


if __name__ == '__main__':
    sys.exit(main())
