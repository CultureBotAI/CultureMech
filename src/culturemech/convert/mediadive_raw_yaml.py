"""Convert MediaDive JSON to raw YAML format.

Performs direct 1:1 conversion of MediaDive MongoDB exports to YAML
without any normalization or LinkML validation.

Input: raw/mediadive/*.json
Output: raw_yaml/mediadive/*.yaml
"""

import argparse
import json
import logging
from pathlib import Path

import yaml

from culturemech.convert.base import RawYAMLConverter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MediaDiveRawYAMLConverter(RawYAMLConverter):
    """Convert MediaDive JSON exports to raw YAML."""

    def convert_file(self, input_file: Path, output_dir: Path):
        """Convert MediaDive JSON file to raw YAML files.

        Args:
            input_file: Path to MediaDive JSON file
            output_dir: Directory to write raw YAML files
        """
        output_dir.mkdir(parents=True, exist_ok=True)

        with open(input_file) as f:
            data = json.load(f)

        # Handle both direct array and wrapped in 'data' key
        if isinstance(data, dict) and 'data' in data:
            records = data['data']
        elif isinstance(data, list):
            records = data
        else:
            records = [data]

        self.log(f"  Found {len(records)} record(s)")

        for i, record in enumerate(records):
            # Add source metadata
            record = self.add_source_metadata(record, input_file)

            # Determine output filename
            if '_id' in record:
                # MongoDB ObjectId format
                if isinstance(record['_id'], dict) and '$oid' in record['_id']:
                    record_id = record['_id']['$oid']
                else:
                    record_id = str(record['_id'])
                filename = f"{record_id}.yaml"
            elif 'id' in record:
                filename = f"{record['id']}.yaml"
            elif 'medium_id' in record:
                filename = f"{record['medium_id']}.yaml"
            else:
                filename = f"{input_file.stem}_{i:04d}.yaml"

            output_file = output_dir / filename

            # Write YAML preserving structure
            with open(output_file, 'w') as f:
                yaml.dump(record, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

        self.log(f"  Wrote {len(records)} raw YAML file(s)")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Convert MediaDive JSON to raw YAML format (no normalization)"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default="data/raw/mediadive",
        help="Input directory with MediaDive JSON files (default: raw/mediadive)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default="data/raw_yaml/mediadive",
        help="Output directory for raw YAML files (default: raw_yaml/mediadive)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    logger.info(f"Converting MediaDive JSON to raw YAML")
    logger.info(f"  Input: {args.input}")
    logger.info(f"  Output: {args.output}")

    converter = MediaDiveRawYAMLConverter(verbose=args.verbose)
    converter.convert_directory(args.input, args.output, pattern="*.json")

    logger.info("Conversion complete")


if __name__ == "__main__":
    main()
