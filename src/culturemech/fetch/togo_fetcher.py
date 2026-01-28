"""
TOGO Medium API fetcher.

Fetches microbial culture media data from TogoMedium REST API.
Implements rate limiting, caching, and error handling.
"""

import argparse
import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


class TogoFetcher:
    """Fetch data from TogoMedium API."""

    BASE_URL = "https://togomedium.org/sparqlist/api"

    def __init__(self, output_dir: Path, delay: float = 0.5):
        """
        Initialize fetcher.

        Args:
            output_dir: Directory to save fetched data
            delay: Delay between API requests in seconds (default 0.5)
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.delay = delay

        # Session with retry strategy
        self.session = requests.Session()
        retries = Retry(
            total=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        self.session.mount("https://", HTTPAdapter(max_retries=retries))

    def fetch_media_list(self, limit: int = 100, offset: int = 0) -> List[Dict]:
        """
        Fetch paginated list of media.

        Args:
            limit: Number of results per page
            offset: Starting offset

        Returns:
            List of media objects
        """
        url = f"{self.BASE_URL}/list_media"
        params = {"limit": limit, "offset": offset}

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            # API returns: {"total": 2917, "offset": 0, "contents": [...], ...}
            if isinstance(data, dict) and "contents" in data:
                return data["contents"]
            elif isinstance(data, list):
                return data
            return []
        except requests.RequestException as e:
            print(f"Error fetching media list (offset={offset}): {e}")
            return []

    def fetch_all_media_ids(self) -> List[Dict[str, Any]]:
        """
        Fetch all media IDs with pagination.

        Returns:
            List of all media objects with IDs and names
        """
        print("Fetching media list from TOGO API...")
        all_media = []
        offset = 0
        limit = 100

        while True:
            print(f"  Fetching batch at offset {offset}...")
            batch = self.fetch_media_list(limit=limit, offset=offset)

            if not batch:
                break

            all_media.extend(batch)
            print(f"    Retrieved {len(batch)} media (total: {len(all_media)})")

            if len(batch) < limit:
                # Last page
                break

            offset += limit
            time.sleep(self.delay)

        print(f"✓ Fetched {len(all_media)} media IDs")
        return all_media

    def fetch_medium_details(self, gm_id: str) -> Optional[Dict]:
        """
        Fetch detailed information for a single medium.

        Args:
            gm_id: Medium ID (e.g., "M443")

        Returns:
            Medium details or None if error
        """
        url = f"{self.BASE_URL}/gmdb_medium_by_gmid"
        params = {"gm_id": gm_id}

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            data = response.json()

            # API returns array, take first element
            if isinstance(data, list) and len(data) > 0:
                return data[0]
            elif isinstance(data, dict):
                return data
            return None

        except requests.RequestException as e:
            print(f"  Error fetching {gm_id}: {e}")
            return None

    def fetch_all_media_details(
        self, limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Fetch detailed information for all media.

        Args:
            limit: Optional limit on number of media to fetch (for testing)

        Returns:
            List of complete media objects
        """
        # Get list of all media IDs
        media_list = self.fetch_all_media_ids()

        if limit:
            media_list = media_list[:limit]
            print(f"Limiting to first {limit} media for testing")

        # Fetch details for each medium
        print(f"\nFetching details for {len(media_list)} media...")
        all_details = []
        failed = []

        for i, medium in enumerate(media_list, 1):
            # Extract gm_id from nested structure
            # Format: {"media_id": {"label": "M3006", "href": "/medium/M3006"}, ...}
            gm_id = None
            if isinstance(medium, dict):
                media_id_obj = medium.get("media_id")
                if isinstance(media_id_obj, dict):
                    gm_id = media_id_obj.get("label")
                elif isinstance(media_id_obj, str):
                    gm_id = media_id_obj

            if not gm_id:
                print(f"  [{i}/{len(media_list)}] Skipping (no ID)")
                continue

            print(f"  [{i}/{len(media_list)}] Fetching {gm_id}...", end="")

            details = self.fetch_medium_details(gm_id)
            if details:
                all_details.append(details)
                print(" ✓")
            else:
                failed.append(gm_id)
                print(" ✗")

            time.sleep(self.delay)

        print(f"\n✓ Fetched {len(all_details)} media details")
        if failed:
            print(f"✗ Failed to fetch {len(failed)} media: {', '.join(failed[:10])}")

        return all_details

    def fetch_components_list(self) -> List[Dict[str, Any]]:
        """
        Fetch list of all components (ingredients).

        Returns:
            List of component objects
        """
        url = f"{self.BASE_URL}/list_components"

        try:
            print("Fetching components list...")
            response = self.session.get(url, timeout=60)
            response.raise_for_status()
            components = response.json()
            print(f"✓ Fetched {len(components)} components")
            return components

        except requests.RequestException as e:
            print(f"Error fetching components: {e}")
            return []

    def save_json(self, data: Any, filename: str) -> Path:
        """
        Save data as JSON file.

        Args:
            data: Data to save
            filename: Output filename

        Returns:
            Path to saved file
        """
        output_path = self.output_dir / filename
        with open(output_path, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"✓ Saved to {output_path}")
        return output_path

    def fetch_all(self, media_limit: Optional[int] = None):
        """
        Fetch all available TOGO data.

        Args:
            media_limit: Optional limit on media (for testing)
        """
        print("=" * 60)
        print("TOGO Medium Data Fetcher")
        print("=" * 60)

        # Fetch media details
        media = self.fetch_all_media_details(limit=media_limit)
        if media:
            self.save_json(media, "togo_media.json")

        # Fetch components
        components = self.fetch_components_list()
        if components:
            self.save_json(components, "togo_components.json")

        # Save statistics
        stats = {
            "fetch_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "media_count": len(media),
            "components_count": len(components),
            "api_delay": self.delay,
        }
        self.save_json(stats, "fetch_stats.json")

        print("\n" + "=" * 60)
        print(f"✓ Fetch complete!")
        print(f"  Media: {len(media)}")
        print(f"  Components: {len(components)}")
        print(f"  Output: {self.output_dir}")
        print("=" * 60)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch media data from TogoMedium API"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="data/raw/togo",
        help="Output directory for fetched data",
    )
    parser.add_argument(
        "-d",
        "--delay",
        type=float,
        default=0.5,
        help="Delay between API requests in seconds (default: 0.5)",
    )
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        help="Limit number of media to fetch (for testing)",
    )
    parser.add_argument(
        "--media-only",
        action="store_true",
        help="Fetch only media data (skip components)",
    )
    parser.add_argument(
        "--components-only",
        action="store_true",
        help="Fetch only components data (skip media)",
    )

    args = parser.parse_args()

    fetcher = TogoFetcher(output_dir=args.output, delay=args.delay)

    if args.components_only:
        components = fetcher.fetch_components_list()
        fetcher.save_json(components, "togo_components.json")
    elif args.media_only:
        media = fetcher.fetch_all_media_details(limit=args.limit)
        fetcher.save_json(media, "togo_media.json")
    else:
        fetcher.fetch_all(media_limit=args.limit)


if __name__ == "__main__":
    main()
