"""Generate human-reviewable curation candidates and apply approved curations."""

import json
import csv
import logging
from pathlib import Path
from typing import Dict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CurationValidator:
    """Generate human-reviewable curation candidates."""

    @staticmethod
    def generate_review_csv(extractions_json: Path, output_csv: Path) -> None:
        """Create CSV with extracted organism data for human review.

        Args:
            extractions_json: Input JSON file with organism candidates
            output_csv: Output CSV file path
        """
        # Load extractions
        with open(extractions_json, 'r') as f:
            extractions = json.load(f)

        # Prepare CSV data
        fieldnames = [
            'filename',
            'medium_name',
            'extracted_organism',
            'ncbi_taxon_id',
            'ncbi_taxon_label',
            'strain',
            'culture_type',
            'confidence',
            'extraction_pattern',
            'approve'
        ]

        output_csv.parent.mkdir(parents=True, exist_ok=True)

        with open(output_csv, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()

            for filename, data in sorted(extractions.items()):
                # Extract medium name from filename
                medium_name = Path(filename).stem.replace('_', ' ')

                row = {
                    'filename': filename,
                    'medium_name': medium_name,
                    'extracted_organism': data.get('organism_name', ''),
                    'ncbi_taxon_id': data.get('ncbi_taxon_id', ''),
                    'ncbi_taxon_label': data.get('ncbi_taxon_label', ''),
                    'strain': data.get('strain', ''),
                    'culture_type': data.get('culture_type', ''),
                    'confidence': data.get('confidence', ''),
                    'extraction_pattern': data.get('extraction_pattern', ''),
                    'approve': 'TRUE'  # Default to approved, curator can change
                }
                writer.writerow(row)

        logger.info(f"Generated review CSV with {len(extractions)} entries: {output_csv}")
        logger.info(f"\nNext steps:")
        logger.info(f"1. Open {output_csv} in a spreadsheet editor")
        logger.info(f"2. Review each row and set 'approve' to TRUE or FALSE")
        logger.info(f"3. Save the file")
        logger.info(f"4. Run yaml_updater.py with the approved CSV")

    @staticmethod
    def load_approved_curations(approved_csv: Path) -> Dict:
        """Load approved curations from CSV.

        Args:
            approved_csv: CSV file with approve column

        Returns:
            Dictionary mapping filenames to approved organism data
        """
        approved = {}

        with open(approved_csv, 'r') as f:
            reader = csv.DictReader(f)

            for row in reader:
                # Only include approved rows
                if row['approve'].strip().upper() != 'TRUE':
                    continue

                filename = row['filename']
                approved[filename] = {
                    'organism_name': row['extracted_organism'],
                    'ncbi_taxon_id': row['ncbi_taxon_id'],
                    'ncbi_taxon_label': row['ncbi_taxon_label'],
                    'strain': row['strain'],
                    'culture_type': row['culture_type'],
                    'confidence': row['confidence']
                }

        logger.info(f"Loaded {len(approved)} approved curations from {approved_csv}")
        return approved


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Generate review CSV from organism extraction results'
    )
    parser.add_argument(
        '--input',
        type=Path,
        default=Path('data/curation/organism_candidates.json'),
        help='Input JSON file with organism candidates'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('data/curation/organism_review.csv'),
        help='Output CSV file for review'
    )

    args = parser.parse_args()

    validator = CurationValidator()
    validator.generate_review_csv(args.input, args.output)


if __name__ == '__main__':
    main()
