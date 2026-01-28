"""Import KOMODO media metadata to CultureMech YAML format.

Converts KOMODO web table data into CultureMech YAML files with:
- KOMODO IDs (komodo.medium:ID format for kg-microbe compatibility)
- Medium metadata (pH, type, aerobic classification)
- DSMZ recipe mapping (for future composition merge)
- Filename sanitization
- Duplicate detection
"""

import json
import logging
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class KomodoWebImporter:
    """
    Import KOMODO media from web table data to CultureMech YAML format.

    Creates YAML files with KOMODO metadata that can later be merged
    with DSMZ composition data using the DSMZ medium number mappings.
    """

    def __init__(
        self,
        input_dir: Path,
        output_dir: Path,
        limit: Optional[int] = None
    ):
        """
        Initialize KOMODO web importer.

        Args:
            input_dir: Directory with komodo_web_media.json
            output_dir: Root directory for kb/media/
            limit: Optional limit for testing (default: None = all media)
        """
        self.input_dir = Path(input_dir)
        self.output_dir = Path(output_dir)
        self.limit = limit

        # Load source data
        self.media_file = self.input_dir / "komodo_web_media.json"
        if not self.media_file.exists():
            raise FileNotFoundError(f"KOMODO media file not found: {self.media_file}")

        with open(self.media_file) as f:
            data = json.load(f)
            self.media_records = data.get("data", [])

        # Tracking
        self.generated_filenames = {}  # {filename: [medium_id1, ...]}
        self.duplicate_count = 0
        self.import_count = 0
        self.skip_count = 0

    def import_all(self):
        """
        Import all KOMODO media to YAML files.

        Steps:
        1. Process each medium
        2. Convert to CultureMech format
        3. Write YAML files
        4. Report statistics
        """
        logger.info("=" * 60)
        logger.info("KOMODO Web Table Importer")
        logger.info("=" * 60)

        total = len(self.media_records)
        if self.limit:
            total = min(total, self.limit)
            logger.info(f"Limiting to {self.limit} media for testing")

        logger.info(f"\nProcessing {total} KOMODO media...")
        logger.info("")

        for i, record in enumerate(self.media_records[:total], 1):
            if i % 50 == 0 or i == total:
                logger.info(f"  Progress: {i}/{total} ({i/total*100:.1f}%)")

            self._import_medium(record)

        # Report duplicates
        self._report_duplicates()

        # Final statistics
        logger.info("\n" + "=" * 60)
        logger.info("✓ Import complete!")
        logger.info(f"  Imported: {self.import_count}/{total}")
        logger.info(f"  Skipped: {self.skip_count}")
        logger.info(f"  Duplicates: {self.duplicate_count}")
        logger.info(f"  Output: {self.output_dir}")
        logger.info("=" * 60)

    def _import_medium(self, record: Dict[str, Any]):
        """Import a single KOMODO medium to YAML."""
        komodo_id = record.get('id')
        if not komodo_id:
            logger.warning("Skipping record with no ID")
            self.skip_count += 1
            return

        # Convert to CultureMech format
        recipe = self._convert_to_culturemech(record)

        # Determine category (default to bacterial for now)
        category = self._infer_category(record)

        # Generate filename
        filename = self._generate_filename(record, category)
        full_filename = f"{category}/{filename}"

        # Check for duplicate filenames
        if full_filename in self.generated_filenames:
            self.duplicate_count += 1
            existing_ids = ", ".join(self.generated_filenames[full_filename])
            logger.warning(
                f"⚠️  DUPLICATE FILENAME: {filename}\n"
                f"   Category: {category}\n"
                f"   Current medium: KOMODO:{komodo_id} ('{record.get('name')}')\n"
                f"   Previous medium(s): {existing_ids}\n"
                f"   File will be OVERWRITTEN!"
            )

        # Track filename
        if full_filename not in self.generated_filenames:
            self.generated_filenames[full_filename] = []
        self.generated_filenames[full_filename].append(f"KOMODO:{komodo_id}")

        # Write YAML file
        category_dir = self.output_dir / category
        category_dir.mkdir(parents=True, exist_ok=True)

        output_path = category_dir / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(recipe, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        self.import_count += 1

    def _convert_to_culturemech(self, record: Dict[str, Any]) -> Dict[str, Any]:
        """
        Convert KOMODO record to CultureMech YAML format.

        Creates a media recipe with KOMODO metadata, preserving DSMZ
        mapping for future composition merge.
        """
        komodo_id = record['id']
        name = record['name']

        recipe = {
            "name": name,
            "original_name": name,
            "category": "imported"
        }

        # Medium type
        if record.get('is_complex'):
            recipe['medium_type'] = "COMPLEX"
        else:
            recipe['medium_type'] = "DEFINED"

        # Physical state (unknown from KOMODO data, default to LIQUID)
        recipe['physical_state'] = "LIQUID"

        # pH information
        if record.get('ph_value'):
            recipe['ph_value'] = float(record['ph_value'])
        elif record.get('ph_range'):
            recipe['ph_range'] = record['ph_range']

        if record.get('ph_buffer'):
            if 'notes' in recipe:
                recipe['notes'] += f" | pH buffer: {record['ph_buffer']}"
            else:
                recipe['notes'] = f"pH buffer: {record['ph_buffer']}"

        # Media term (KOMODO ID for kg-microbe compatibility)
        recipe['media_term'] = {
            "preferred_term": f"KOMODO Medium {komodo_id}",
            "term": {
                "id": f"komodo.medium:{komodo_id}",
                "label": name
            }
        }

        # Add source notes with DSMZ mapping (for future merge)
        source_notes = f"Source: KOMODO ModelSEED | ID: {komodo_id}"
        if record.get('dsmz_medium_number'):
            source_notes += f" | DSMZ Medium: {record['dsmz_medium_number']} (mediadive.medium:{record['dsmz_medium_number']})"
        if record.get('is_aerobic') is not None:
            source_notes += f" | Aerobic: {'Yes' if record['is_aerobic'] else 'No'}"
        if record.get('is_submedium'):
            source_notes += " | SubMedium: Yes"

        if 'notes' in recipe:
            recipe['notes'] += f" | {source_notes}"
        else:
            recipe['notes'] = source_notes

        # Placeholder ingredients (required by schema, will be populated during DSMZ merge)
        # The DSMZ merge step will add composition data using the DSMZ medium number
        recipe['ingredients'] = []

        # Applications
        recipe['applications'] = ["Microbial cultivation"]

        # Curation history
        recipe['curation_history'] = [{
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.%fZ", time.gmtime()),
            "curator": "komodo-web-import",
            "action": "Imported from KOMODO web table",
            "notes": f"Source: KOMODO, ID: {komodo_id}"
        }]

        return recipe

    def _infer_category(self, record: Dict[str, Any]) -> str:
        """
        Infer category from KOMODO record.

        For now, default to 'bacterial' since most KOMODO media
        are bacterial. This can be refined during DSMZ merge.
        """
        # Could add logic here based on medium name keywords
        # For now, use bacterial as default
        return "bacterial"

    def _generate_filename(self, record: Dict[str, Any], category: str) -> str:
        """
        Generate sanitized filename for KOMODO medium.

        Format: KOMODO_{ID}_{SANITIZED_NAME}.yaml

        Args:
            record: KOMODO medium record
            category: Medium category

        Returns:
            Sanitized filename
        """
        komodo_id = record['id']
        name = record['name']

        # Sanitize ID (replace dots, underscores with hyphens for consistency)
        sanitized_id = komodo_id.replace('.', '-').replace('_', '-')

        # Sanitize name
        sanitized_name = self._sanitize_filename(name)

        # Truncate long names (max 80 chars for filename)
        if len(sanitized_name) > 80:
            sanitized_name = sanitized_name[:80]

        filename = f"KOMODO_{sanitized_id}_{sanitized_name}.yaml"

        return filename

    def _sanitize_filename(self, name: str) -> str:
        r"""
        Sanitize media name for use as a filename.

        REPLACES ALL PROBLEMATIC CHARACTERS WITH UNDERSCORE (_)

        Problematic characters replaced (ALL become '_'):
        1. Shell metacharacters: / \ : * ? " < > | ' ` ; & $ ! # % @ ^ ~ [ ] { } ( )
        2. CSV/data problematic: , (comma) and spaces
        3. Special symbols: + =
        4. Non-ASCII: ° ´ and all other non-ASCII characters

        KEEPS ONLY: a-z, A-Z, 0-9, -, .
        """
        clean_name = ''
        for char in name:
            if char.isalnum() or char in ['-', '.']:
                clean_name += char
            else:
                clean_name += '_'

        # Collapse multiple consecutive underscores
        while '__' in clean_name:
            clean_name = clean_name.replace('__', '_')

        return clean_name.strip('_')

    def _report_duplicates(self):
        """Report duplicate filename statistics."""
        if self.duplicate_count == 0:
            logger.info("\n✓ No duplicate filenames detected - all files are unique")
            return

        # Find duplicates
        duplicates = {
            fname: ids for fname, ids in self.generated_filenames.items()
            if len(ids) > 1
        }

        logger.warning(f"\n⚠️  DUPLICATE FILENAME SUMMARY")
        logger.warning("=" * 60)
        logger.warning(f"Total duplicate events: {self.duplicate_count}")
        logger.warning(f"Unique filenames with duplicates: {len(duplicates)}")
        logger.warning("")
        logger.warning("Files that were OVERWRITTEN:")
        logger.warning("-" * 60)

        for filename, medium_ids in sorted(duplicates.items()):
            logger.warning(f"Filename: {filename}")
            logger.warning(f"  Conflicts: {len(medium_ids)} media mapped to same file")
            for i, med_id in enumerate(medium_ids, 1):
                logger.warning(f"    {i}. {med_id}")
            logger.warning(f"  → Only the LAST one ({medium_ids[-1]}) was saved!")
            logger.warning("")

        logger.warning("=" * 60)
        logger.warning(f"⚠️  {len(duplicates)} file(s) were overwritten!")
        logger.warning(f"⚠️  Data loss: {sum(len(ids) - 1 for ids in duplicates.values())} media lost")
        logger.warning("=" * 60)


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Import KOMODO media from web table to CultureMech YAML"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default=Path("raw/komodo_web"),
        help="Input directory with KOMODO web raw JSON files (Layer 1: raw/komodo_web/)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("normalized_yaml"),
        help="Output directory for normalized YAML files (Layer 3: normalized_yaml/)"
    )
    parser.add_argument(
        "-l", "--limit",
        type=int,
        help="Limit number of media to import (for testing)"
    )

    args = parser.parse_args()

    importer = KomodoWebImporter(
        input_dir=args.input,
        output_dir=args.output,
        limit=args.limit
    )

    importer.import_all()


if __name__ == "__main__":
    main()
