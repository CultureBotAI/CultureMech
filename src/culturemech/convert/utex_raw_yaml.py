"""Convert UTEX JSON to raw YAML format.

Performs direct 1:1 conversion of UTEX fetched data to YAML
without any normalization or LinkML validation.

Input: raw/utex/utex_media.json
Output: raw_yaml/utex/*.yaml
"""

import argparse
import json
import logging
from pathlib import Path

import yaml

from culturemech.convert.base import RawYAMLConverter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UTEXRawYAMLConverter(RawYAMLConverter):
    """Convert UTEX JSON to raw YAML."""

    def convert_file(self, input_file: Path, output_dir: Path):
        """Convert UTEX JSON file to raw YAML files.

        Args:
            input_file: Path to utex_media.json
            output_dir: Directory to write raw YAML files
        """
        output_dir.mkdir(parents=True, exist_ok=True)

        with open(input_file) as f:
            data = json.load(f)

        # Extract recipes array
        recipes = data.get('recipes', [])

        if not recipes:
            self.log(f"No recipes found in {input_file}")
            return

        self.log(f"  Found {len(recipes)} recipe(s)")

        for i, recipe in enumerate(recipes):
            # Add source metadata
            recipe = self.add_source_metadata(recipe, input_file)

            # Generate output filename
            recipe_id = recipe.get('id', f'utex_{i:04d}')
            filename = f"{recipe_id}.yaml"

            output_file = output_dir / filename

            # Write YAML preserving structure
            with open(output_file, 'w') as f:
                yaml.dump(recipe, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

        self.log(f"  Wrote {len(recipes)} raw YAML file(s)")

    def convert_directory(self, input_dir: Path, output_dir: Path, pattern: str = "utex_media.json"):
        """Convert UTEX media JSON to raw YAML.

        Args:
            input_dir: Input directory containing utex_media.json
            output_dir: Output directory for raw YAML files
            pattern: Filename pattern (default: utex_media.json)
        """
        input_dir = Path(input_dir)
        output_dir = Path(output_dir)

        if not input_dir.exists():
            raise FileNotFoundError(f"Input directory not found: {input_dir}")

        output_dir.mkdir(parents=True, exist_ok=True)

        # Look for utex_media.json
        input_file = input_dir / pattern

        if not input_file.exists():
            self.log(f"No {pattern} found in {input_dir}", force=True)
            self.log(f"Run 'just fetch-utex' first to download data", force=True)
            return

        self.log(f"Converting: {input_file.name}", force=True)
        try:
            self.convert_file(input_file, output_dir)
        except Exception as e:
            self.log(f"Error converting {input_file}: {e}", force=True)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Convert UTEX JSON to raw YAML format (no normalization)"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default="raw/utex",
        help="Input directory with UTEX JSON files (default: raw/utex)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default="raw_yaml/utex",
        help="Output directory for raw YAML files (default: raw_yaml/utex)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    logger.info(f"Converting UTEX JSON to raw YAML")
    logger.info(f"  Input: {args.input}")
    logger.info(f"  Output: {args.output}")

    converter = UTEXRawYAMLConverter(verbose=args.verbose)
    converter.convert_directory(args.input, args.output)

    logger.info("Conversion complete")


if __name__ == "__main__":
    main()
