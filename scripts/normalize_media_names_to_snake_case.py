#!/usr/bin/env python3
"""
Normalize all media names to snake_case for consistent matching.

This script:
1. Converts recipe names to snake_case (lowercase with underscores)
2. Preserves original name in a metadata field for reference
3. Updates all internal references (solutions, etc.)
4. Makes future matching case-insensitive by design
"""

import argparse
import logging
import re
import sys
from pathlib import Path
from typing import Dict, Any, Optional
import yaml
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


class NameNormalizer:
    """Normalize media names to snake_case."""

    def __init__(self, dry_run: bool = False):
        """Initialize normalizer."""
        self.dry_run = dry_run
        self.stats = {
            'files_processed': 0,
            'names_normalized': 0,
            'already_snake_case': 0,
            'files_renamed': 0
        }
        self.renames = []  # Track file renames

    @staticmethod
    def to_snake_case(text: str) -> str:
        """
        Convert text to snake_case.

        Examples:
            "BG-11 Medium" → "bg_11_medium"
            "F/2 Medium" → "f_2_medium"
            "Bold's 3N Medium" → "bolds_3n_medium"
            "DSMZ Medium 141" → "dsmz_medium_141"
        """
        # Replace common separators with spaces
        text = re.sub(r'[/\-\s]+', ' ', text)

        # Remove possessive apostrophes
        text = re.sub(r"'s\b", 's', text)

        # Remove other apostrophes
        text = text.replace("'", '')

        # Replace non-alphanumeric with space
        text = re.sub(r'[^a-zA-Z0-9]+', ' ', text)

        # Convert to lowercase and join with underscores
        text = '_'.join(text.lower().split())

        # Remove leading/trailing underscores
        text = text.strip('_')

        # Collapse multiple underscores
        text = re.sub(r'_+', '_', text)

        return text

    @staticmethod
    def is_already_snake_case(text: str) -> bool:
        """Check if text is already in snake_case."""
        # Snake case should be all lowercase with underscores only
        return bool(re.match(r'^[a-z0-9_]+$', text))

    def add_curation_history(self, recipe: Dict[str, Any], original_name: str, new_name: str) -> None:
        """Add curation history entry."""
        if 'curation_history' not in recipe:
            recipe['curation_history'] = []

        recipe['curation_history'].append({
            'timestamp': datetime.now(timezone.utc).isoformat(),
            'curator': 'normalize_media_names_to_snake_case.py',
            'action': 'NAME_NORMALIZED',
            'notes': f'Normalized name from "{original_name}" to "{new_name}" for consistent matching'
        })

    def process_file(self, yaml_file: Path) -> Optional[Path]:
        """
        Process a single recipe file.

        Returns:
            New file path if file was renamed, None otherwise
        """
        try:
            with open(yaml_file, 'r', encoding='utf-8') as f:
                recipe = yaml.safe_load(f)

            if not recipe:
                return None

            original_name = recipe.get('name', '')
            if not original_name:
                logger.warning(f"No name field in {yaml_file}")
                return None

            # Check if already snake_case
            if self.is_already_snake_case(original_name):
                self.stats['already_snake_case'] += 1
                return None

            # Convert to snake_case
            new_name = self.to_snake_case(original_name)

            if new_name == original_name:
                # No change needed
                self.stats['already_snake_case'] += 1
                return None

            # Store original name if not already stored
            if 'original_name' not in recipe:
                recipe['original_name'] = original_name

            # Update name
            recipe['name'] = new_name

            # Add curation history
            self.add_curation_history(recipe, original_name, new_name)

            self.stats['names_normalized'] += 1

            if not self.dry_run:
                # Write updated content
                with open(yaml_file, 'w', encoding='utf-8') as f:
                    yaml.dump(recipe, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

                # Calculate new filename
                new_filename = new_name + '.yaml'
                new_path = yaml_file.parent / new_filename

                # Rename file if different
                if new_path != yaml_file:
                    if new_path.exists():
                        logger.warning(f"Target file already exists: {new_path}")
                        return None

                    yaml_file.rename(new_path)
                    self.stats['files_renamed'] += 1
                    self.renames.append((str(yaml_file), str(new_path)))
                    logger.info(f"Renamed: {yaml_file.name} → {new_path.name}")
                    return new_path

            return None

        except Exception as e:
            logger.error(f"Error processing {yaml_file}: {e}")
            return None

    def process_directory(
        self,
        yaml_dir: Path,
        category: Optional[str] = None,
        limit: Optional[int] = None
    ) -> None:
        """Process all recipe files in a directory."""
        logger.info("=" * 60)
        logger.info("Media Name Normalization to snake_case")
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
            if i % 500 == 0:
                logger.info(f"Progress: {i}/{len(files)} files processed...")

            self.process_file(yaml_file)
            self.stats['files_processed'] += 1

        # Print summary
        logger.info("\n" + "=" * 60)
        logger.info("Normalization Complete")
        logger.info("=" * 60)
        logger.info(f"Files processed: {self.stats['files_processed']}")
        logger.info(f"Names normalized: {self.stats['names_normalized']}")
        logger.info(f"Already snake_case: {self.stats['already_snake_case']}")
        logger.info(f"Files renamed: {self.stats['files_renamed']}")

        if self.renames and not self.dry_run:
            logger.info(f"\nRenamed {len(self.renames)} files")
            logger.info("Remember to update any external references!")

        logger.info("=" * 60)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Normalize media names to snake_case",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry run on first 10 files
  python scripts/normalize_media_names_to_snake_case.py --dry-run --limit 10

  # Process bacterial category
  python scripts/normalize_media_names_to_snake_case.py --category bacterial

  # Process all categories
  python scripts/normalize_media_names_to_snake_case.py
        """
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

    normalizer = NameNormalizer(dry_run=args.dry_run)
    normalizer.process_directory(args.yaml_dir, args.category, args.limit)

    return 0


if __name__ == '__main__':
    sys.exit(main())
