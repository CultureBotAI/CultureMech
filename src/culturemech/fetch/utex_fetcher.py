"""Fetch algae media recipes from UTEX Culture Collection.

UTEX (Culture Collection of Algae at the University of Texas at Austin)
provides extensive algal culture media recipes for both freshwater and
saltwater organisms.

Website: https://utex.org/
Media recipes: https://utex.org/pages/algal-culture-media
Collection size: 3,000+ strains

This fetcher:
1. Fetches the media index page
2. Extracts recipe URLs
3. Fetches each recipe detail page
4. Extracts structured recipe data
5. Saves to JSON files

Data source: Web scraping (no public API available)
"""

import argparse
import json
import logging
import time
from datetime import datetime
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# UTEX composition tables are headed
# `# | Component | Amount | Stock Solution Concentration | Final Concentration`.
# The leading `#` is a row ordinal, not data. Reading fixed column positions
# instead of the header is what produced the corpus-wide defect where every
# UTEX ingredient was named "1", "2", "3"... and its *name* was stored as the
# amount: `cols[0]` is the ordinal and `cols[1]` is the component, so the real
# Amount column was never read at all. Map by header text, never by position.
_COMPONENT_HEADERS = {"component", "ingredient", "chemical", "compound"}
_COLUMN_ALIASES = {
    "amount": "amount",
    "quantity": "amount",
    "stock solution concentration": "stock_concentration",
    "stock concentration": "stock_concentration",
    "final concentration": "final_concentration",
    "concentration": "final_concentration",
}


def _header_map(cells: list[str]) -> dict[str, int] | None:
    """Column name -> index, or None when this row is not a composition header.

    Returning None for an unrecognized table is deliberate: UTEX product pages
    carry several layout tables (cart widgets, badges) that a positional reader
    happily mistakes for data.
    """
    mapping: dict[str, int] = {}
    for index, cell in enumerate(cells):
        key = cell.strip().lower()
        if key in _COMPONENT_HEADERS:
            mapping["component"] = index
        elif key in _COLUMN_ALIASES:
            mapping.setdefault(_COLUMN_ALIASES[key], index)
    return mapping if "component" in mapping else None


def parse_composition_table(rows: list[list[str]]) -> list[dict[str, str]]:
    """Rows of a UTEX composition table -> composition entries.

    `rows` is the table as text cells, header included. An entry always carries
    `ingredient` and `amount` (the keys the importer reads) and carries the two
    concentration columns only when the page filled them in.
    """
    if not rows:
        return []
    columns = _header_map(rows[0])
    if columns is None:
        return []

    entries: list[dict[str, str]] = []
    for cells in rows[1:]:
        component_index = columns["component"]
        if component_index >= len(cells):
            continue
        name = cells[component_index].strip()
        if not name:
            continue
        entry = {"ingredient": name, "amount": ""}
        for field in ("amount", "stock_concentration", "final_concentration"):
            index = columns.get(field)
            if index is not None and index < len(cells):
                value = cells[index].strip()
                if value:
                    entry[field] = value
        entries.append(entry)
    return entries


class UTEXFetcher:
    """Fetch media recipes from UTEX Culture Collection."""

    BASE_URL = "https://utex.org"
    MEDIA_INDEX_URL = f"{BASE_URL}/pages/algal-culture-media"

    def __init__(self, output_dir: Path, rate_limit: float = 1.0):
        """Initialize fetcher.

        Args:
            output_dir: Directory to save fetched data
            rate_limit: Seconds to wait between requests (default: 1.0)
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.rate_limit = rate_limit
        self.session = requests.Session()
        self.session.headers.update(
            {"User-Agent": "CultureMech/1.0 (Scientific Research; contact: info@culturemech.org)"}
        )

    def fetch_media_index(self) -> list[dict[str, str]]:
        """Fetch media index page and extract recipe URLs.

        Returns:
            List of dicts with 'name' and 'url' for each recipe
        """
        logger.info(f"Fetching media index from {self.MEDIA_INDEX_URL}")

        response = self.session.get(self.MEDIA_INDEX_URL)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        recipes = []

        # Find all media links
        # UTEX uses product links like /products/bg-11-medium
        for link in soup.find_all("a", href=True):
            href = link.get("href", "")
            if "/products/" in href and "medium" in href.lower():
                name = link.get_text(strip=True)
                if name and len(name) > 3:  # Filter out short/empty links
                    url = href if href.startswith("http") else f"{self.BASE_URL}{href}"
                    recipes.append({"name": name, "url": url})

        # Deduplicate by URL
        seen_urls = set()
        unique_recipes = []
        for recipe in recipes:
            if recipe["url"] not in seen_urls:
                seen_urls.add(recipe["url"])
                unique_recipes.append(recipe)

        logger.info(f"Found {len(unique_recipes)} unique media recipes")
        return unique_recipes

    def fetch_recipe_details(self, recipe_url: str, recipe_name: str) -> dict[str, Any] | None:
        """Fetch detailed recipe information from recipe page.

        Args:
            recipe_url: URL of recipe detail page
            recipe_name: Name of the recipe

        Returns:
            Dict with recipe details or None if fetch fails
        """
        try:
            time.sleep(self.rate_limit)  # Rate limiting

            logger.info(f"Fetching: {recipe_name}")
            response = self.session.get(recipe_url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            # Extract recipe details
            # UTEX stores recipes in product description format
            recipe_data = {
                "id": recipe_url.split("/")[-1],  # e.g., 'bg-11-medium'
                "name": recipe_name,
                "url": recipe_url,
                "source": "UTEX",
                "category": self._determine_category(recipe_name),
                "description": None,
                "composition": [],
                "preparation": None,
                "notes": None,
                "fetched_date": datetime.now().isoformat(),
            }

            # Extract description
            desc_elem = soup.find("div", class_="product-description")
            if desc_elem:
                recipe_data["description"] = desc_elem.get_text(strip=True)

            # Extract composition/ingredients by header, not by column position
            # (see `parse_composition_table`).
            for table in soup.find_all("table"):
                rows = [
                    [cell.get_text(strip=True) for cell in row.find_all(["td", "th"])]
                    for row in table.find_all("tr")
                ]
                recipe_data["composition"].extend(parse_composition_table(rows))

            if not recipe_data["composition"] and soup.find("table"):
                logger.warning(
                    f"{recipe_url}: has tables but no recognizable composition header; "
                    f"no ingredients captured"
                )

            # There is deliberately no <ul>/<ol> fallback. One existed, splitting
            # every list item on ':' or '-', and it read the site's navigation
            # menu as a recipe: bbm-boron-stock-solution came back with 18
            # "ingredients" including {'RGB': 'LED Lighting Platform'} and
            # {'Media Kits & Add': 'Ins'}. It never contributed a real
            # ingredient — all 99 media pages carry a proper table — so it was
            # pure downside. A page whose composition is prose (that boron page
            # states it in a sentence) is reported as uncaptured rather than
            # guessed at.

            # Extract preparation/notes
            # Look for sections with keywords
            for elem in soup.find_all(["div", "p", "section"]):
                text = elem.get_text(strip=True)
                lower_text = text.lower()
                if "preparation" in lower_text or "instruction" in lower_text:
                    recipe_data["preparation"] = text
                elif "note" in lower_text or "remark" in lower_text:
                    recipe_data["notes"] = text

            return recipe_data

        except Exception as e:
            logger.error(f"Error fetching {recipe_name}: {e}")
            return None

    def _determine_category(self, name: str) -> str:
        """Determine if recipe is for freshwater or saltwater.

        Args:
            name: Recipe name

        Returns:
            'freshwater', 'saltwater', or 'general'
        """
        name_lower = name.lower()

        saltwater_keywords = ["seawater", "marine", "erdschreiber", "saltwater", "f/2", "ocean"]
        freshwater_keywords = ["freshwater", "bold", "bg-11", "bristol", "tap", "soil"]

        if any(kw in name_lower for kw in saltwater_keywords):
            return "saltwater"
        elif any(kw in name_lower for kw in freshwater_keywords):
            return "freshwater"
        else:
            return "general"

    def fetch_all(self, limit: int | None = None) -> dict[str, Any]:
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
            recipe_data = self.fetch_recipe_details(recipe_info["url"], recipe_info["name"])
            if recipe_data:
                recipes.append(recipe_data)

        # Create output data
        output_data = {
            "source": "UTEX",
            "source_url": self.MEDIA_INDEX_URL,
            "fetched_date": datetime.now().isoformat(),
            "count": len(recipes),
            "recipes": recipes,
        }

        # Save to file
        output_file = self.output_dir / "utex_media.json"
        with open(output_file, "w") as f:
            json.dump(output_data, f, indent=2)

        logger.info(f"Saved {len(recipes)} recipes to {output_file}")

        # Save statistics
        stats = {
            "fetch_date": datetime.now().isoformat(),
            "total_recipes": len(recipes),
            "categories": {},
            "source_url": self.MEDIA_INDEX_URL,
        }

        for recipe in recipes:
            cat = recipe.get("category", "unknown")
            stats["categories"][cat] = stats["categories"].get(cat, 0) + 1

        stats_file = self.output_dir / "fetch_stats.json"
        with open(stats_file, "w") as f:
            json.dump(stats, f, indent=2)

        return output_data


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Fetch media recipes from UTEX Culture Collection")
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="data/raw/utex",
        help="Output directory for fetched data (default: raw/utex)",
    )
    parser.add_argument(
        "-l", "--limit", type=int, help="Limit number of recipes to fetch (for testing)"
    )
    parser.add_argument(
        "--rate-limit",
        type=float,
        default=1.0,
        help="Seconds to wait between requests (default: 1.0)",
    )

    args = parser.parse_args()

    logger.info("UTEX Media Fetcher")
    logger.info(f"Output: {args.output}")
    if args.limit:
        logger.info(f"Limit: {args.limit} recipes")

    fetcher = UTEXFetcher(args.output, rate_limit=args.rate_limit)
    fetcher.fetch_all(limit=args.limit)

    logger.info("Fetch complete")


if __name__ == "__main__":
    main()
