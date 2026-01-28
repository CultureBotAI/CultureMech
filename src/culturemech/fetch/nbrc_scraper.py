"""
NBRC Media Scraper

Ethical web scraper for NITE Biological Resource Center media recipes.
NBRC provides 400+ media recipes publicly on their website.

Important: This scraper follows ethical guidelines:
- Checks robots.txt before scraping
- Implements 2-second delays between requests
- Caches pages locally to minimize server load
- Provides proper attribution

URL: https://www.nite.go.jp/en/nbrc/cultures/media/culture-list-e.html
"""

import argparse
import json
import time
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    logger.error("Required libraries not installed")
    logger.info("Install with: pip install requests beautifulsoup4")
    requests = None
    BeautifulSoup = None


class NBRCScraper:
    """
    Ethical web scraper for NBRC media recipes.

    NBRC (NITE Biological Resource Center) is a Japanese culture collection
    providing 400+ freely accessible media recipes.
    """

    BASE_URL = "https://www.nite.go.jp"
    MEDIA_LIST_URL = (
        "https://www.nite.go.jp/en/nbrc/cultures/media/culture-list-e.html"
    )

    def __init__(
        self,
        output_dir: Path,
        delay: float = 2.0,
        cache_html: bool = True,
    ):
        """
        Initialize scraper with ethical defaults.

        Args:
            output_dir: Directory to save scraped data
            delay: Delay between requests in seconds (default: 2.0 for ethics)
            cache_html: Whether to cache HTML pages locally
        """
        if requests is None or BeautifulSoup is None:
            raise ImportError(
                "Required libraries not installed. "
                "Install with: pip install requests beautifulsoup4"
            )

        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.delay = delay
        self.cache_html = cache_html

        if self.cache_html:
            self.cache_dir = self.output_dir / "scraped"
            self.cache_dir.mkdir(exist_ok=True)

        # Set user agent for transparency
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": (
                    "CultureMech/0.1.0 (Research Project; "
                    "https://github.com/KG-Hub/CultureMech) "
                    "Python/requests"
                )
            }
        )

        logger.info("✓ NBRC scraper initialized")
        logger.info(f"  Delay: {delay}s between requests")
        logger.info(f"  Caching: {'enabled' if cache_html else 'disabled'}")

    def check_robots_txt(self) -> bool:
        """
        Check robots.txt for scraping permissions.

        Returns:
            True if scraping is allowed
        """
        robots_url = f"{self.BASE_URL}/robots.txt"
        try:
            response = self.session.get(robots_url, timeout=10)
            if response.status_code == 200:
                logger.info("✓ robots.txt checked")
                # Simple check: if no specific disallow, proceed
                # For production, use robotparser module
                if "Disallow: /en/nbrc" in response.text:
                    logger.warning("robots.txt may restrict access")
                    return False
                return True
            else:
                logger.info("No robots.txt found - proceeding cautiously")
                return True
        except Exception as e:
            logger.warning(f"Could not fetch robots.txt: {e}")
            return True  # Assume allowed if can't check

    def fetch_page(self, url: str, cache_name: Optional[str] = None) -> Optional[str]:
        """
        Fetch a web page with caching and rate limiting.

        Args:
            url: URL to fetch
            cache_name: Optional cache filename

        Returns:
            HTML content or None
        """
        # Check cache first
        if cache_name and self.cache_html:
            cache_path = self.cache_dir / cache_name
            if cache_path.exists():
                logger.debug(f"  Loading from cache: {cache_name}")
                return cache_path.read_text(encoding="utf-8")

        # Fetch from web
        try:
            logger.debug(f"  Fetching: {url}")
            response = self.session.get(url, timeout=30)
            response.raise_for_status()
            html = response.text

            # Cache if enabled
            if cache_name and self.cache_html:
                cache_path = self.cache_dir / cache_name
                cache_path.write_text(html, encoding="utf-8")

            # Ethical delay
            time.sleep(self.delay)

            return html

        except requests.RequestException as e:
            logger.error(f"  Error fetching {url}: {e}")
            return None

    def scrape_media_list(self) -> List[Dict[str, str]]:
        """
        Scrape the main media list page.

        Returns:
            List of media with IDs and names
        """
        logger.info("Scraping media list...")

        html = self.fetch_page(self.MEDIA_LIST_URL, "media_list.html")
        if not html:
            logger.error("Failed to fetch media list")
            return []

        soup = BeautifulSoup(html, "html.parser")
        media_list = []

        # NBRC media list structure (may need adjustment based on actual HTML)
        # Typical structure: table with media number, name, and link

        # Find all media entries (adjust selector based on actual HTML structure)
        # This is a placeholder - actual structure needs to be verified
        tables = soup.find_all("table")

        for table in tables:
            rows = table.find_all("tr")
            for row in rows[1:]:  # Skip header row
                cells = row.find_all("td")
                if len(cells) >= 2:
                    # Extract media number and name
                    media_number = cells[0].get_text(strip=True)
                    media_name = cells[1].get_text(strip=True)

                    # Find link if available
                    link = row.find("a")
                    media_url = None
                    if link and link.get("href"):
                        media_url = urljoin(self.BASE_URL, link["href"])

                    if media_number and media_name:
                        media_list.append(
                            {
                                "media_number": media_number,
                                "media_name": media_name,
                                "url": media_url,
                            }
                        )

        logger.info(f"✓ Found {len(media_list)} media recipes")
        return media_list

    def scrape_media_details(self, media_item: Dict) -> Optional[Dict]:
        """
        Scrape detailed recipe for a single medium.

        Args:
            media_item: Media item from list

        Returns:
            Complete media recipe
        """
        if not media_item.get("url"):
            logger.warning(f"  No URL for {media_item.get('media_name')}")
            return None

        media_number = media_item["media_number"]
        cache_name = f"media_{media_number.replace(' ', '_')}.html"

        html = self.fetch_page(media_item["url"], cache_name)
        if not html:
            return None

        soup = BeautifulSoup(html, "html.parser")

        # Extract recipe components
        # This is a placeholder - actual structure needs verification
        recipe = {
            "media_number": media_number,
            "media_name": media_item["media_name"],
            "url": media_item["url"],
            "ingredients": self._extract_ingredients(soup),
            "preparation": self._extract_preparation(soup),
            "notes": self._extract_notes(soup),
        }

        return recipe

    def _extract_ingredients(self, soup: BeautifulSoup) -> List[Dict]:
        """Extract ingredients from media page."""
        ingredients = []

        # Look for ingredient table/list
        # Typical structure: ingredient name, amount, unit
        # This is a placeholder - adjust based on actual HTML

        tables = soup.find_all("table")
        for table in tables:
            # Check if this is the ingredients table
            if "ingredient" in str(table).lower() or "composition" in str(
                table
            ).lower():
                rows = table.find_all("tr")
                for row in rows[1:]:  # Skip header
                    cells = row.find_all("td")
                    if len(cells) >= 2:
                        name = cells[0].get_text(strip=True)
                        amount = cells[1].get_text(strip=True)

                        # Parse amount and unit
                        match = re.match(r"([\d.]+)\s*(\w+)", amount)
                        if match:
                            quantity = match.group(1)
                            unit = match.group(2)
                        else:
                            quantity = amount
                            unit = ""

                        ingredients.append(
                            {"name": name, "quantity": quantity, "unit": unit}
                        )

        return ingredients

    def _extract_preparation(self, soup: BeautifulSoup) -> List[str]:
        """Extract preparation steps."""
        steps = []

        # Look for preparation section
        prep_section = soup.find(string=re.compile("preparation", re.I))
        if prep_section:
            # Get parent element and extract text
            parent = prep_section.find_parent()
            if parent:
                # Find ordered/unordered list
                ol = parent.find_next("ol")
                ul = parent.find_next("ul")

                list_elem = ol or ul
                if list_elem:
                    items = list_elem.find_all("li")
                    steps = [item.get_text(strip=True) for item in items]

        return steps

    def _extract_notes(self, soup: BeautifulSoup) -> str:
        """Extract notes/remarks."""
        notes = ""

        # Look for notes section
        notes_section = soup.find(string=re.compile("note|remark", re.I))
        if notes_section:
            parent = notes_section.find_parent()
            if parent:
                notes = parent.get_text(strip=True)

        return notes

    def scrape_all(self, limit: Optional[int] = None) -> List[Dict]:
        """
        Scrape all NBRC media recipes.

        Args:
            limit: Optional limit for testing

        Returns:
            List of complete media recipes
        """
        logger.info("=" * 60)
        logger.info("NBRC Media Scraper")
        logger.info("=" * 60)

        # Check robots.txt
        if not self.check_robots_txt():
            logger.warning("Robots.txt check failed - aborting")
            return []

        # Get media list
        media_list = self.scrape_media_list()
        if not media_list:
            return []

        if limit:
            media_list = media_list[:limit]
            logger.info(f"Limiting to {limit} media for testing")

        # Scrape details for each medium
        logger.info(f"\nScraping details for {len(media_list)} media...")
        all_recipes = []
        failed = []

        for i, media_item in enumerate(media_list, 1):
            logger.info(
                f"  [{i}/{len(media_list)}] {media_item['media_name']}...",
                end="",
            )

            recipe = self.scrape_media_details(media_item)
            if recipe:
                all_recipes.append(recipe)
                logger.info(" ✓")
            else:
                failed.append(media_item["media_name"])
                logger.info(" ✗")

        logger.info(f"\n✓ Scraped {len(all_recipes)} media recipes")
        if failed:
            logger.warning(f"Failed to scrape {len(failed)} media")

        return all_recipes

    def save_json(self, data: Any, filename: str) -> Path:
        """Save data as JSON file."""
        output_path = self.output_dir / filename
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info(f"✓ Saved to {output_path}")
        return output_path


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Ethical scraper for NBRC media recipes"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="data/raw/nbrc",
        help="Output directory",
    )
    parser.add_argument(
        "-d",
        "--delay",
        type=float,
        default=2.0,
        help="Delay between requests (seconds, default: 2.0)",
    )
    parser.add_argument(
        "-l", "--limit", type=int, help="Limit number of media (for testing)"
    )
    parser.add_argument(
        "--no-cache", action="store_true", help="Disable HTML caching"
    )

    args = parser.parse_args()

    try:
        scraper = NBRCScraper(
            output_dir=args.output,
            delay=args.delay,
            cache_html=not args.no_cache,
        )

        recipes = scraper.scrape_all(limit=args.limit)
        if recipes:
            scraper.save_json(recipes, "nbrc_media.json")

            # Save statistics
            stats = {
                "scrape_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "media_count": len(recipes),
                "delay_seconds": args.delay,
            }
            scraper.save_json(stats, "scrape_stats.json")

    except Exception as e:
        logger.error(f"Error: {e}")
        import traceback

        traceback.print_exc()
        exit(1)


if __name__ == "__main__":
    main()
