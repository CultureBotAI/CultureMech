"""Fetch algae media recipes from CCAP (Culture Collection of Algae and Protozoa).

CCAP is one of the world's largest collections of algae and protozoa,
based at the Scottish Association for Marine Science (SAMS) in Scotland.

Website: https://www.ccap.ac.uk/
Media recipes: https://www.ccap.ac.uk/index.php/media-recipes/
Collection: 3,000+ strains

This fetcher:
1. Fetches the media recipe index page
2. Extracts recipe names and PDF URLs
3. Downloads PDF files
4. Extracts structured data from PDFs (where possible)
5. Saves to JSON files

Data source: Web scraping + PDF extraction (no public API available)
"""

import argparse
import json
import logging
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class CCAPFetcher:
    """Fetch media recipes from CCAP."""

    BASE_URL = "https://www.ccap.ac.uk"
    MEDIA_INDEX_URL = f"{BASE_URL}/index.php/media-recipes/"

    def __init__(self, output_dir: Path, rate_limit: float = 1.0, download_pdfs: bool = False):
        """Initialize fetcher.

        Args:
            output_dir: Directory to save fetched data
            rate_limit: Seconds to wait between requests (default: 1.0)
            download_pdfs: Whether to download PDF files (default: False)
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.rate_limit = rate_limit
        self.download_pdfs = download_pdfs
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'CultureMech/1.0 (Scientific Research; contact: info@culturemech.org)'
        })

        if download_pdfs:
            self.pdf_dir = self.output_dir / 'pdfs'
            self.pdf_dir.mkdir(exist_ok=True)

    def fetch_media_index(self) -> List[Dict[str, str]]:
        """Fetch media index page and extract recipe URLs.

        Returns:
            List of dicts with 'name', 'pdf_url', and 'id' for each recipe
        """
        logger.info(f"Fetching media index from {self.MEDIA_INDEX_URL}")

        response = self.session.get(self.MEDIA_INDEX_URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        recipes = []

        # Find all PDF links
        # CCAP uses links like /wp-content/uploads/MR_<name>.pdf
        for link in soup.find_all('a', href=True):
            href = link.get('href', '')
            if '.pdf' in href and 'MR_' in href:
                name = link.get_text(strip=True)
                if name:
                    # Clean up name - remove extra whitespace and QA notes
                    name = re.sub(r'\s+', ' ', name).strip()
                    name = re.sub(r'\s*\(QA\)\s*$', '', name, flags=re.IGNORECASE)

                    # Build full URL
                    pdf_url = href if href.startswith('http') else f"{self.BASE_URL}{href}"

                    # Extract ID from filename
                    # e.g., MR_BG11.pdf -> BG11
                    match = re.search(r'MR_([^/]+)\.pdf', href)
                    recipe_id = match.group(1) if match else href.split('/')[-1].replace('.pdf', '')

                    recipes.append({
                        'id': recipe_id,
                        'name': name,
                        'pdf_url': pdf_url
                    })

        # Deduplicate by URL
        seen_urls = set()
        unique_recipes = []
        for recipe in recipes:
            if recipe['pdf_url'] not in seen_urls:
                seen_urls.add(recipe['pdf_url'])
                unique_recipes.append(recipe)

        logger.info(f"Found {len(unique_recipes)} unique media recipes")
        return unique_recipes

    def fetch_recipe_details(self, recipe_info: Dict[str, str]) -> Dict[str, Any]:
        """Process recipe information.

        For CCAP, recipes are in PDF format. We store metadata and optionally
        download the PDF for later processing.

        Args:
            recipe_info: Dict with recipe ID, name, and PDF URL

        Returns:
            Dict with recipe details
        """
        time.sleep(self.rate_limit)  # Rate limiting

        logger.info(f"Processing: {recipe_info['name']}")

        recipe_data = {
            'id': recipe_info['id'],
            'name': recipe_info['name'],
            'pdf_url': recipe_info['pdf_url'],
            'source': 'CCAP',
            'category': 'algae',
            'format': 'pdf',
            'fetched_date': datetime.now().isoformat(),
            'pdf_downloaded': False
        }

        # Optionally download PDF
        if self.download_pdfs:
            try:
                pdf_filename = f"{recipe_info['id']}.pdf"
                pdf_path = self.pdf_dir / pdf_filename

                logger.info(f"  Downloading PDF: {pdf_filename}")
                response = self.session.get(recipe_info['pdf_url'])
                response.raise_for_status()

                with open(pdf_path, 'wb') as f:
                    f.write(response.content)

                recipe_data['pdf_downloaded'] = True
                recipe_data['pdf_path'] = str(pdf_path)
                logger.info(f"  ✓ Downloaded: {pdf_path}")

            except Exception as e:
                logger.error(f"  Error downloading PDF: {e}")

        return recipe_data

    def fetch_all(self, limit: Optional[int] = None) -> Dict[str, Any]:
        """Fetch all media recipes.

        Args:
            limit: Optional limit on number of recipes to fetch

        Returns:
            Dict with metadata and list of recipes
        """
        # Get recipe index
        recipes_index = self.fetch_media_index()

        if limit:
            recipes_index = recipes_index[:limit]
            logger.info(f"Limiting to first {limit} recipes")

        # Fetch each recipe
        recipes = []
        for idx, recipe_info in enumerate(recipes_index, 1):
            logger.info(f"Progress: {idx}/{len(recipes_index)}")
            recipe_data = self.fetch_recipe_details(recipe_info)
            recipes.append(recipe_data)

        # Create output data
        output_data = {
            'source': 'CCAP',
            'source_url': self.MEDIA_INDEX_URL,
            'fetched_date': datetime.now().isoformat(),
            'count': len(recipes),
            'pdfs_downloaded': sum(1 for r in recipes if r.get('pdf_downloaded', False)),
            'recipes': recipes
        }

        # Save to file
        output_file = self.output_dir / 'ccap_media.json'
        with open(output_file, 'w') as f:
            json.dump(output_data, f, indent=2)

        logger.info(f"Saved {len(recipes)} recipes to {output_file}")

        # Save statistics
        stats = {
            'fetch_date': datetime.now().isoformat(),
            'total_recipes': len(recipes),
            'pdfs_downloaded': output_data['pdfs_downloaded'],
            'source_url': self.MEDIA_INDEX_URL
        }

        stats_file = self.output_dir / 'fetch_stats.json'
        with open(stats_file, 'w') as f:
            json.dump(stats, f, indent=2)

        return output_data


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch media recipes from CCAP (Culture Collection of Algae and Protozoa)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default="raw/ccap",
        help="Output directory for fetched data (default: raw/ccap)"
    )
    parser.add_argument(
        "-l", "--limit",
        type=int,
        help="Limit number of recipes to fetch (for testing)"
    )
    parser.add_argument(
        "--rate-limit",
        type=float,
        default=1.0,
        help="Seconds to wait between requests (default: 1.0)"
    )
    parser.add_argument(
        "--download-pdfs",
        action="store_true",
        help="Download PDF files (warning: can be large)"
    )

    args = parser.parse_args()

    logger.info("CCAP Media Fetcher")
    logger.info(f"Output: {args.output}")
    if args.limit:
        logger.info(f"Limit: {args.limit} recipes")
    if args.download_pdfs:
        logger.info("PDFs will be downloaded")

    fetcher = CCAPFetcher(args.output, rate_limit=args.rate_limit, download_pdfs=args.download_pdfs)
    fetcher.fetch_all(limit=args.limit)

    logger.info("Fetch complete")


if __name__ == "__main__":
    main()
