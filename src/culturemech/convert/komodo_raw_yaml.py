"""Convert KOMODO JSON to raw YAML format.

Performs direct 1:1 conversion of KOMODO media database exports to YAML
without any normalization or LinkML validation.

Input: raw/komodo/*.json
Output: raw_yaml/komodo/*.yaml
"""

import argparse
import logging
from pathlib import Path

from culturemech.convert.base import JSONToRawYAMLConverter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Convert KOMODO JSON to raw YAML format (no normalization)"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default="raw/komodo",
        help="Input directory with KOMODO JSON files (default: raw/komodo)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default="raw_yaml/komodo",
        help="Output directory for raw YAML files (default: raw_yaml/komodo)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    logger.info(f"Converting KOMODO JSON to raw YAML")
    logger.info(f"  Input: {args.input}")
    logger.info(f"  Output: {args.output}")

    converter = JSONToRawYAMLConverter(verbose=args.verbose)
    converter.convert_directory(args.input, args.output, pattern="*.json")

    logger.info("Conversion complete")


if __name__ == "__main__":
    main()
