"""Fetch MediaDive media compositions from REST API.

Fetches detailed composition data from MediaDive REST API individual
endpoints (/rest/medium/:id) instead of relying on PDF parsing.

Expected to achieve ~100% composition coverage vs 54.7% from PDF parsing.
"""

import json
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
import requests

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MediaDiveAPIFetcher:
    """
    Fetch MediaDive media recipes from REST API with rate limiting.

    API Documentation: https://mediadive.dsmz.de/doc/
    Base URL: https://mediadive.dsmz.de/rest

    Key Endpoints:
    - GET /media - Bulk list (metadata only)
    - GET /medium/:id - Individual medium (WITH compositions!)
    - GET /solution/:id - Solution recipe details
    """

    BASE_URL = "https://mediadive.dsmz.de/rest"
    DEFAULT_DELAY = 0.25  # 4 requests/second (conservative)

    def __init__(
        self,
        output_dir: Path,
        delay: float = DEFAULT_DELAY,
        timeout: float = 30.0
    ):
        """
        Initialize MediaDive API fetcher.

        Args:
            output_dir: Directory to save fetched data
            delay: Seconds to wait between API calls (default: 0.25)
            timeout: Request timeout in seconds (default: 30)
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.delay = delay
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "User-Agent": "CultureMech/0.1.0 (github.com/KG-Hub/CultureMech)"
        })

    def fetch_all(self, limit: Optional[int] = None):
        """
        Main orchestration: fetch all media with compositions.

        Steps:
        1. Fetch media list (IDs)
        2. Fetch detailed composition for each medium
        3. Extract unique solutions
        4. Extract unique ingredients
        5. Export to JSON files
        6. Save statistics

        Args:
            limit: Optional limit for testing (default: None = all media)
        """
        logger.info("=" * 60)
        logger.info("MediaDive API Fetcher")
        logger.info("=" * 60)

        # Step 1: Fetch media list
        logger.info("\n[1/5] Fetching media list...")
        media_ids = self._fetch_media_list()
        logger.info(f"  ✓ Retrieved {len(media_ids)} media IDs")

        if limit:
            media_ids = media_ids[:limit]
            logger.info(f"  (Limited to {limit} for testing)")

        # Step 2: Fetch detailed compositions
        logger.info(f"\n[2/5] Fetching detailed compositions for {len(media_ids)} media...")
        media_details = self._fetch_all_media_details(media_ids)
        logger.info(f"  ✓ Successfully fetched {len(media_details)} media")
        logger.info(f"  ✗ Failed: {len(media_ids) - len(media_details)}")

        # Step 3: Extract solutions
        logger.info("\n[3/5] Extracting solutions...")
        solutions = self._extract_solutions(media_details)
        logger.info(f"  ✓ Found {len(solutions)} unique solutions")

        # Step 4: Extract ingredients
        logger.info("\n[4/5] Extracting ingredients...")
        ingredients = self._extract_ingredients(media_details, solutions)
        logger.info(f"  ✓ Found {len(ingredients)} unique ingredients")

        # Step 5: Export data
        logger.info("\n[5/5] Exporting data...")
        self._export_data(media_details, solutions, ingredients, len(media_ids))

        logger.info("\n" + "=" * 60)
        logger.info("✓ Fetch complete!")
        logger.info(f"  Media fetched: {len(media_details)}/{len(media_ids)}")
        logger.info(f"  Solutions: {len(solutions)}")
        logger.info(f"  Ingredients: {len(ingredients)}")
        logger.info(f"  Output: {self.output_dir}")
        logger.info("=" * 60)

    def _fetch_media_list(self) -> List[int]:
        """Fetch list of all media IDs from bulk endpoint."""
        url = f"{self.BASE_URL}/media"
        response = self.session.get(url, timeout=self.timeout)
        response.raise_for_status()
        data = response.json()

        # Extract IDs from data array
        media_ids = [m["id"] for m in data.get("data", [])]
        return media_ids

    def _fetch_medium_details(self, medium_id: int) -> Optional[Dict[str, Any]]:
        """
        Fetch detailed composition for a single medium.

        Endpoint: GET /medium/:id
        Returns: Full medium with solutions and recipes
        """
        url = f"{self.BASE_URL}/medium/{medium_id}"

        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            if data.get("status") == 200 and "data" in data:
                return data["data"]
            else:
                logger.warning(f"  Medium {medium_id}: No data (status {data.get('status')})")
                return None

        except requests.RequestException as e:
            logger.warning(f"  Medium {medium_id}: Request failed - {e}")
            return None

    def _fetch_all_media_details(
        self,
        media_ids: List[int]
    ) -> List[Dict[str, Any]]:
        """
        Fetch detailed compositions for all media with rate limiting.

        Args:
            media_ids: List of media IDs to fetch

        Returns:
            List of successfully fetched media details
        """
        media_details = []
        failed = []

        for i, medium_id in enumerate(media_ids, 1):
            # Progress indicator
            if i % 100 == 0 or i == len(media_ids):
                logger.info(f"  Progress: {i}/{len(media_ids)} ({i/len(media_ids)*100:.1f}%)")

            # Fetch medium
            details = self._fetch_medium_details(medium_id)

            if details:
                media_details.append(details)
            else:
                failed.append(medium_id)

            # Rate limiting (skip for last item)
            if i < len(media_ids):
                time.sleep(self.delay)

        return media_details

    def _extract_solutions(
        self,
        media_details: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Extract unique solutions from media details.

        Each medium has 'solutions' array with solution details.
        """
        solutions_by_id = {}

        for medium in media_details:
            for solution in medium.get("solutions", []):
                sol_id = solution.get("id")
                if sol_id and sol_id not in solutions_by_id:
                    solutions_by_id[sol_id] = solution

        return list(solutions_by_id.values())

    def _extract_ingredients(
        self,
        media_details: List[Dict[str, Any]],
        solutions: List[Dict[str, Any]]
    ) -> List[Dict[str, Any]]:
        """
        Extract unique ingredients from solutions.

        Recipe items have 'compound_id' for ingredients.
        """
        ingredients_by_id = {}

        # Extract from solutions
        for solution in solutions:
            for item in solution.get("recipe", []):
                comp_id = item.get("compound_id")
                if comp_id and comp_id not in ingredients_by_id:
                    ingredients_by_id[comp_id] = {
                        "id": comp_id,
                        "name": item.get("compound", ""),
                        # Note: Full ingredient details would require
                        # separate /ingredient/:id API calls
                    }

        return list(ingredients_by_id.values())

    def _export_data(
        self,
        media_details: List[Dict[str, Any]],
        solutions: List[Dict[str, Any]],
        ingredients: List[Dict[str, Any]],
        total_attempted: int
    ):
        """Export all data to JSON files with statistics."""

        # Export media details
        media_path = self.save_json(
            {"count": len(media_details), "data": media_details},
            "mediadive_api_media.json"
        )
        logger.info(f"  ✓ Saved {media_path.name}")

        # Export solutions
        solutions_path = self.save_json(
            {"count": len(solutions), "data": solutions},
            "mediadive_api_solutions.json"
        )
        logger.info(f"  ✓ Saved {solutions_path.name}")

        # Export ingredients
        ingredients_path = self.save_json(
            {"count": len(ingredients), "data": ingredients},
            "mediadive_api_ingredients.json"
        )
        logger.info(f"  ✓ Saved {ingredients_path.name}")

        # Export statistics
        stats = {
            "fetch_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "source": "MediaDive REST API",
            "base_url": self.BASE_URL,
            "total_attempted": total_attempted,
            "total_fetched": len(media_details),
            "success_rate": len(media_details) / total_attempted * 100 if total_attempted > 0 else 0,
            "total_solutions": len(solutions),
            "total_ingredients": len(ingredients),
            "api_delay": self.delay,
            "estimated_time_minutes": (total_attempted * self.delay) / 60
        }
        stats_path = self.save_json(stats, "fetch_stats.json")
        logger.info(f"  ✓ Saved {stats_path.name}")

    def save_json(self, data: Any, filename: str) -> Path:
        """Save data as pretty-printed JSON."""
        output_path = self.output_dir / filename
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        return output_path


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Fetch MediaDive media compositions from REST API"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default=Path("raw/mediadive_api"),
        help="Output directory (default: raw/mediadive_api)"
    )
    parser.add_argument(
        "-l", "--limit",
        type=int,
        help="Limit number of media to fetch (for testing)"
    )
    parser.add_argument(
        "-d", "--delay",
        type=float,
        default=0.25,
        help="Delay between API calls in seconds (default: 0.25)"
    )

    args = parser.parse_args()

    fetcher = MediaDiveAPIFetcher(
        output_dir=args.output,
        delay=args.delay
    )

    fetcher.fetch_all(limit=args.limit)


if __name__ == "__main__":
    main()
