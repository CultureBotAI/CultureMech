"""Apply approved curations to YAML files."""

import logging
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime, timezone
import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class YAMLUpdater:
    """Update YAML files with approved organism data."""

    @staticmethod
    def create_organism_descriptor(organism_data: Dict) -> Optional[Dict]:
        """Create an OrganismDescriptor from organism data.

        Args:
            organism_data: Dictionary with organism information

        Returns:
            OrganismDescriptor dict or None if no organism name
        """
        organism_name = organism_data.get('organism_name', '').strip()
        if not organism_name:
            return None

        descriptor = {
            'preferred_term': organism_name
        }

        # Add NCBI taxon term if available
        ncbi_id = organism_data.get('ncbi_taxon_id', '').strip()
        ncbi_label = organism_data.get('ncbi_taxon_label', '').strip()

        if ncbi_id and ncbi_label:
            descriptor['term'] = {
                'id': ncbi_id,
                'label': ncbi_label
            }

        # Add strain if available
        strain = organism_data.get('strain', '').strip()
        if strain:
            descriptor['strain'] = strain

        return descriptor

    @staticmethod
    def update_yaml_file(yaml_path: Path, organism_data: Dict, dry_run: bool = True) -> bool:
        """Update a YAML file with organism data.

        Args:
            yaml_path: Path to YAML file
            organism_data: Dictionary with organism information
            dry_run: If True, don't actually write changes

        Returns:
            True if file was updated, False otherwise
        """
        try:
            # Load existing YAML
            with open(yaml_path, 'r') as f:
                data = yaml.safe_load(f)

            # Check if already has target_organisms or organism_culture_type
            has_target_organisms = bool(data.get('target_organisms'))
            has_culture_type = 'organism_culture_type' in data

            if has_target_organisms or has_culture_type:
                logger.warning(f"Skipping {yaml_path.name}: already has organism data")
                return False

            # Create organism descriptor
            descriptor = YAMLUpdater.create_organism_descriptor(organism_data)
            if not descriptor:
                logger.warning(f"Skipping {yaml_path.name}: no organism name in data")
                return False

            # Add target_organisms
            data['target_organisms'] = [descriptor]

            # Add organism_culture_type
            culture_type = organism_data.get('culture_type', '').strip()
            if culture_type in ['isolate', 'community']:
                data['organism_culture_type'] = culture_type

            # Add curation history entry
            if 'curation_history' not in data:
                data['curation_history'] = []

            curation_entry = {
                'timestamp': datetime.now(timezone.utc).isoformat(),
                'curator': 'organism-extractor',
                'action': 'Added organism data from pattern extraction',
                'notes': f"Pattern: {organism_data.get('extraction_pattern', 'unknown')}, Confidence: {organism_data.get('confidence', 'unknown')}"
            }
            data['curation_history'].append(curation_entry)

            # Write back to YAML
            if not dry_run:
                with open(yaml_path, 'w') as f:
                    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
                logger.info(f"Updated {yaml_path.name}")
            else:
                logger.info(f"[DRY RUN] Would update {yaml_path.name}")

            return True

        except Exception as e:
            logger.error(f"Error updating {yaml_path}: {e}")
            return False

    @staticmethod
    def process_approved_curations(approved_curations: Dict, yaml_dir: Path,
                                   dry_run: bool = True) -> int:
        """Process all approved curations and update YAML files.

        Args:
            approved_curations: Dictionary mapping filenames to organism data
            yaml_dir: Root directory containing YAML files
            dry_run: If True, preview changes without writing

        Returns:
            Number of files updated
        """
        updated_count = 0

        for filename, organism_data in approved_curations.items():
            yaml_path = yaml_dir / filename

            if not yaml_path.exists():
                logger.warning(f"File not found: {yaml_path}")
                continue

            if YAMLUpdater.update_yaml_file(yaml_path, organism_data, dry_run):
                updated_count += 1

        return updated_count


def main():
    """Main entry point."""
    import argparse
    from .curation_validator import CurationValidator

    parser = argparse.ArgumentParser(
        description='Update YAML files with approved organism curations'
    )
    parser.add_argument(
        '--input',
        type=Path,
        required=True,
        help='Input CSV file with approved curations'
    )
    parser.add_argument(
        '--yaml-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Directory containing YAML files'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without writing to files'
    )

    args = parser.parse_args()

    # Load approved curations
    validator = CurationValidator()
    approved = validator.load_approved_curations(args.input)

    if not approved:
        logger.warning("No approved curations found!")
        return

    # Process curations
    updater = YAMLUpdater()
    updated_count = updater.process_approved_curations(
        approved,
        args.yaml_dir,
        args.dry_run
    )

    if args.dry_run:
        logger.info(f"\n[DRY RUN] Would update {updated_count} files")
        logger.info("Remove --dry-run to apply changes")
    else:
        logger.info(f"\nUpdated {updated_count} YAML files")


if __name__ == '__main__':
    main()
