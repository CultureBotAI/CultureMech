"""Convert SAG JSON metadata to raw YAML format.

SAG recipes are in PDF format. This converter:
1. Reads the metadata JSON (recipe names, URLs)
2. Optionally extracts text from PDFs if downloaded
3. Creates raw YAML files with available data

Input: raw/sag/sag_media.json (and optionally raw/sag/pdfs/*.pdf)
Output: raw_yaml/sag/*.yaml
"""

import argparse
import json
import logging
from pathlib import Path
from typing import Optional

import yaml

from culturemech.convert.base import RawYAMLConverter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SAGRawYAMLConverter(RawYAMLConverter):
    """Convert SAG JSON metadata to raw YAML."""

    def __init__(self, verbose: bool = False, extract_pdfs: bool = False):
        """Initialize converter.

        Args:
            verbose: Enable verbose logging
            extract_pdfs: Extract text from PDF files if available
        """
        super().__init__(verbose)
        self.extract_pdfs = extract_pdfs

        if extract_pdfs:
            try:
                import pdfplumber
                self.pdfplumber = pdfplumber
                self.log("PDF extraction enabled (using pdfplumber)", force=True)
            except ImportError:
                self.log("Warning: pdfplumber not installed, PDF extraction disabled", force=True)
                self.log("Install with: uv pip install pdfplumber", force=True)
                self.extract_pdfs = False
                self.pdfplumber = None

    def extract_pdf_text(self, pdf_path: Path) -> Optional[str]:
        """Extract text from PDF file.

        Args:
            pdf_path: Path to PDF file

        Returns:
            Extracted text or None if extraction fails
        """
        if not self.extract_pdfs or self.pdfplumber is None:
            return None

        try:
            with self.pdfplumber.open(pdf_path) as pdf:
                text = ""
                for page in pdf.pages:
                    text += page.extract_text() or ""
                return text.strip() if text else None
        except Exception as e:
            self.log(f"  Error extracting PDF {pdf_path.name}: {e}")
            return None

    def convert_file(self, input_file: Path, output_dir: Path):
        """Convert SAG JSON file to raw YAML files.

        Args:
            input_file: Path to sag_media.json
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

        # Get PDF directory if it exists
        pdf_dir = input_file.parent / 'pdfs'
        has_pdfs = pdf_dir.exists() and self.extract_pdfs

        for i, recipe in enumerate(recipes):
            # Add source metadata
            recipe = self.add_source_metadata(recipe, input_file)

            # Try to extract PDF text if available
            if has_pdfs and recipe.get('pdf_downloaded'):
                pdf_filename = f"{recipe['id']}.pdf"
                pdf_path = pdf_dir / pdf_filename
                if pdf_path.exists():
                    self.log(f"  Extracting: {pdf_filename}")
                    pdf_text = self.extract_pdf_text(pdf_path)
                    if pdf_text:
                        recipe['pdf_extracted_text'] = pdf_text
                        recipe['pdf_extraction_success'] = True
                    else:
                        recipe['pdf_extraction_success'] = False

            # Generate output filename
            recipe_id = recipe.get('id', f'sag_{i:04d}')
            filename = f"{recipe_id}.yaml"

            output_file = output_dir / filename

            # Write YAML preserving structure
            with open(output_file, 'w') as f:
                yaml.dump(recipe, f, sort_keys=False, allow_unicode=True, default_flow_style=False)

        self.log(f"  Wrote {len(recipes)} raw YAML file(s)")

    def convert_directory(self, input_dir: Path, output_dir: Path, pattern: str = "sag_media.json"):
        """Convert SAG media JSON to raw YAML.

        Args:
            input_dir: Input directory containing sag_media.json
            output_dir: Output directory for raw YAML files
            pattern: Filename pattern (default: sag_media.json)
        """
        input_dir = Path(input_dir)
        output_dir = Path(output_dir)

        if not input_dir.exists():
            raise FileNotFoundError(f"Input directory not found: {input_dir}")

        output_dir.mkdir(parents=True, exist_ok=True)

        # Look for sag_media.json
        input_file = input_dir / pattern

        if not input_file.exists():
            self.log(f"No {pattern} found in {input_dir}", force=True)
            self.log(f"Run 'just fetch-sag' first to download data", force=True)
            return

        self.log(f"Converting: {input_file.name}", force=True)
        try:
            self.convert_file(input_file, output_dir)
        except Exception as e:
            self.log(f"Error converting {input_file}: {e}", force=True)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Convert SAG JSON to raw YAML format (no normalization)"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default="raw/sag",
        help="Input directory with SAG JSON files (default: raw/sag)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default="raw_yaml/sag",
        help="Output directory for raw YAML files (default: raw_yaml/sag)"
    )
    parser.add_argument(
        "--extract-pdfs",
        action="store_true",
        help="Extract text from PDF files if available (requires pdfplumber)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    logger.info(f"Converting SAG JSON to raw YAML")
    logger.info(f"  Input: {args.input}")
    logger.info(f"  Output: {args.output}")
    if args.extract_pdfs:
        logger.info(f"  PDF extraction: enabled")

    converter = SAGRawYAMLConverter(verbose=args.verbose, extract_pdfs=args.extract_pdfs)
    converter.convert_directory(args.input, args.output)

    logger.info("Conversion complete")


if __name__ == "__main__":
    main()
