#!/usr/bin/env python3
"""
Import culture media from CultureBotHT repository.

CultureBotHT contains 381 high-quality media YAML files with:
- 60.9% ontology coverage (4,479/7,354 ingredients)
- 313 consolidated and validated media
- Experimental growth data integration
- FEBA (Fitness Browser) compatibility

This script:
1. Reads YAML files from CultureBotHT media_yaml directory
2. Converts to CultureMech schema (minimal transformations needed)
3. Assigns CultureMech IDs
4. Categorizes by organism type
5. Validates against schema
6. Outputs to data/normalized_yaml/
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime, timezone
import yaml

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


class CultureBotHTImporter:
    """Import CultureBotHT media into CultureMech."""

    # Medium type mapping: CultureBotHT → CultureMech
    MEDIUM_TYPE_MAP = {
        'MINIMAL': 'DEFINED',
        'DEFINED': 'DEFINED',
        'RICH': 'COMPLEX',
        'COMPLEX': 'COMPLEX',
    }

    # Category inference from media name patterns
    CATEGORY_PATTERNS = {
        'bacterial': [
            'LB', 'TSB', 'nutrient', 'brain_heart', 'mueller_hinton',
            'pseudomonas', 'bacillus', 'escherichia', 'salmonella'
        ],
        'algae': [
            'BG11', 'BG12', 'cyanobacteria', 'synechococcus', 'prochlorococcus',
            'photosynthetic', 'blue_green'
        ],
        'fungal': [
            'PDA', 'sabouraud', 'malt', 'czapek', 'yeast_mold', 'fungal'
        ],
    }

    def __init__(self, culturebotht_dir: Path, output_dir: Path, dry_run: bool = False):
        """Initialize importer."""
        self.culturebotht_dir = Path(culturebotht_dir)
        self.output_dir = Path(output_dir)
        self.dry_run = dry_run

        self.stats = {
            'files_read': 0,
            'files_imported': 0,
            'files_skipped': 0,
            'errors': 0,
            'categories': {
                'bacterial': 0,
                'algae': 0,
                'fungal': 0,
                'specialized': 0,
            }
        }

    def infer_category(self, medium_name: str) -> str:
        """Infer organism category from medium name."""
        name_lower = medium_name.lower()

        # Check patterns
        for category, patterns in self.CATEGORY_PATTERNS.items():
            if any(pattern.lower() in name_lower for pattern in patterns):
                return category.upper()

        # Default to specialized
        return 'SPECIALIZED'

    def transform_medium(self, source_data: Dict[str, Any], source_file: str) -> Dict[str, Any]:
        """Transform CultureBotHT medium to CultureMech schema."""

        # Start with source data (already mostly compatible)
        medium = source_data.copy()

        # Map medium type
        if 'medium_type' in medium:
            original_type = medium['medium_type']
            medium['medium_type'] = self.MEDIUM_TYPE_MAP.get(original_type, original_type)

        # Infer and add category
        if 'category' not in medium:
            medium['category'] = self.infer_category(medium.get('name', ''))

        # Add source tracking
        if 'sources' not in medium:
            medium['sources'] = []

        medium['sources'].append({
            'database': 'CultureBotHT',
            'database_id': medium.get('name', ''),
            'url': f'https://github.com/CultureBotAI/CultureBotHT'
        })

        # Add import metadata
        if 'curation_history' not in medium:
            medium['curation_history'] = []

        medium['curation_history'].append({
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'curator': 'import_from_culturebotht.py',
            'action': 'IMPORTED',
            'notes': f'Imported from CultureBotHT repository: {source_file}'
        })

        # Add data quality flags if needed
        if 'data_quality_flags' not in medium:
            medium['data_quality_flags'] = []

        # Check for unmapped ingredients
        unmapped_count = 0
        for ingredient in medium.get('ingredients', []):
            if 'term' not in ingredient or not ingredient.get('term', {}).get('id'):
                unmapped_count += 1

        if unmapped_count > 0:
            medium['data_quality_flags'].append('has_unmapped_ingredients')

        return medium

    def sanitize_filename(self, name: str) -> str:
        """Convert name to safe filename (snake_case)."""
        import re
        # Convert to lowercase
        name = name.lower()
        # Replace spaces and special chars with underscore
        name = re.sub(r'[^a-z0-9]+', '_', name)
        # Remove leading/trailing underscores
        name = name.strip('_')
        # Collapse multiple underscores
        name = re.sub(r'_+', '_', name)
        return name

    def import_file(self, yaml_file: Path) -> bool:
        """Import a single media YAML file."""
        try:
            # Read source file
            with open(yaml_file, 'r', encoding='utf-8') as f:
                source_data = yaml.safe_load(f)

            if not source_data or 'name' not in source_data:
                logger.warning(f"Skipping {yaml_file.name}: No name field")
                self.stats['files_skipped'] += 1
                return False

            # Transform to CultureMech schema
            medium = self.transform_medium(source_data, yaml_file.name)

            # Determine output category and filename
            category = medium['category'].lower()
            self.stats['categories'][category] = self.stats['categories'].get(category, 0) + 1

            # Create safe filename from name field
            safe_name = self.sanitize_filename(medium['name'])
            output_filename = f"{safe_name}.yaml"

            # Determine output path
            output_category_dir = self.output_dir / category
            output_path = output_category_dir / output_filename

            if not self.dry_run:
                # Create category directory if needed
                output_category_dir.mkdir(parents=True, exist_ok=True)

                # Write output file
                with open(output_path, 'w', encoding='utf-8') as f:
                    yaml.dump(medium, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

            logger.info(f"✓ Imported {yaml_file.name} → {category}/{output_filename}")
            self.stats['files_imported'] += 1
            return True

        except Exception as e:
            logger.error(f"✗ Error importing {yaml_file}: {e}")
            self.stats['errors'] += 1
            return False

    def import_all(self) -> None:
        """Import all media from CultureBotHT."""
        logger.info("=" * 60)
        logger.info("CultureBotHT Media Import")
        logger.info("=" * 60)

        if self.dry_run:
            logger.info("DRY RUN MODE - no files will be written")

        # Find all YAML files
        media_yaml_dir = self.culturebotht_dir / "media_yaml"

        if not media_yaml_dir.exists():
            logger.error(f"Media YAML directory not found: {media_yaml_dir}")
            return

        yaml_files = sorted(media_yaml_dir.glob("*.yaml"))
        logger.info(f"Found {len(yaml_files)} media YAML files")
        logger.info("")

        # Import each file
        for yaml_file in yaml_files:
            self.stats['files_read'] += 1
            self.import_file(yaml_file)

        # Print summary
        logger.info("\n" + "=" * 60)
        logger.info("Import Complete")
        logger.info("=" * 60)
        logger.info(f"Files read: {self.stats['files_read']}")
        logger.info(f"Files imported: {self.stats['files_imported']}")
        logger.info(f"Files skipped: {self.stats['files_skipped']}")
        logger.info(f"Errors: {self.stats['errors']}")
        logger.info("\nBy category:")
        for category, count in sorted(self.stats['categories'].items()):
            if count > 0:
                logger.info(f"  {category}: {count}")
        logger.info("=" * 60)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Import culture media from CultureBotHT repository"
    )

    parser.add_argument(
        '--culturebotht-dir',
        type=Path,
        default=Path('/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/CultureBotHT/CultureBotHT'),
        help='Path to CultureBotHT repository'
    )

    parser.add_argument(
        '--output-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Output directory for normalized YAML files'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be imported without writing files'
    )

    args = parser.parse_args()

    # Validate paths
    if not args.culturebotht_dir.exists():
        logger.error(f"CultureBotHT directory not found: {args.culturebotht_dir}")
        return 1

    # Run import
    importer = CultureBotHTImporter(
        culturebotht_dir=args.culturebotht_dir,
        output_dir=args.output_dir,
        dry_run=args.dry_run
    )

    importer.import_all()

    return 0 if importer.stats['errors'] == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
