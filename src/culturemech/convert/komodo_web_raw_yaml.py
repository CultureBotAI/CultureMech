"""Convert KOMODO web scrape JSON to raw YAML format.

Performs direct 1:1 conversion of KOMODO web scraping exports to YAML
without any normalization or LinkML validation.

Input: raw/komodo_web/*.json
Output: raw_yaml/komodo_web/*.yaml
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
        description="Convert KOMODO web JSON to raw YAML format (no normalization)"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default="data/raw/komodo_web",
        help="Input directory with KOMODO web JSON files (default: raw/komodo_web)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default="data/raw_yaml/komodo_web",
        help="Output directory for raw YAML files (default: raw_yaml/komodo_web)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    logger.info(f"Converting KOMODO web JSON to raw YAML")
    logger.info(f"  Input: {args.input}")
    logger.info(f"  Output: {args.output}")

    converter = JSONToRawYAMLConverter(verbose=args.verbose)
    converter.convert_directory(args.input, args.output, pattern="*.json")

    logger.info("Conversion complete")


if __name__ == "__main__":
    main()
