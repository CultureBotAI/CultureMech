"""
BacDive API fetcher.

Fetches cultivation data from BacDive (Bacterial Diversity Metadatabase).
BacDive contains 100,000+ bacterial strains with 66,570+ cultivation datasets.

API Documentation: https://bacdive.dsmz.de/api/bacdive/
Python Client: https://github.com/DSMZ-de/bacdive
"""

import argparse
import json
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# BacDive requires API credentials - install with: pip install bacdive
try:
    import bacdive
except ImportError:
    logger.error("BacDive client not installed. Install with: pip install bacdive")
    bacdive = None


class BacDiveFetcher:
    """
    Fetch cultivation data from BacDive API.

    BacDive provides:
    - 100,000+ bacterial and archaeal strains
    - 66,570+ cultivation datasets
    - Growth conditions and media references
    - Links to DSMZ media (overlaps with MediaDive)
    """

    def __init__(
        self,
        output_dir: Path,
        email: Optional[str] = None,
        password: Optional[str] = None,
    ):
        """
        Initialize BacDive fetcher.

        Args:
            output_dir: Directory to save fetched data
            email: BacDive account email (or set BACDIVE_EMAIL env var)
            password: BacDive account password (or set BACDIVE_PASSWORD env var)

        Note:
            Free registration required at https://bacdive.dsmz.de/
        """
        if bacdive is None:
            raise ImportError(
                "BacDive client not installed. "
                "Install with: pip install bacdive"
            )

        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize BacDive client
        # Credentials can be provided directly or via environment variables
        self.client = bacdive.BacdiveClient(email, password)
        logger.info("✓ BacDive client initialized")

    def fetch_all_strain_ids(self) -> List[Dict[str, Any]]:
        """
        Fetch IDs of all strains in BacDive.

        Returns:
            List of strain metadata (ID, name, type culture)
        """
        logger.info("Fetching all strain IDs from BacDive...")
        logger.info("Note: This may take several minutes for 100,000+ strains")

        all_strains = []

        try:
            # Search for all strains (no filters)
            # BacDive API returns paginated results
            query = self.client.search()

            for strain_id in query:
                # Query returns iterator of strain IDs
                all_strains.append({"bacdive_id": strain_id})

                if len(all_strains) % 1000 == 0:
                    logger.info(f"  Retrieved {len(all_strains)} strain IDs...")

            logger.info(f"✓ Fetched {len(all_strains)} strain IDs")
            return all_strains

        except Exception as e:
            logger.error(f"Error fetching strain IDs: {e}")
            return []

    def fetch_strain_details(self, strain_id: int) -> Optional[Dict]:
        """
        Fetch detailed information for a single strain.

        Args:
            strain_id: BacDive strain ID

        Returns:
            Complete strain data including cultivation conditions
        """
        try:
            strain_data = self.client.retrieve(strain_id)
            return strain_data
        except Exception as e:
            logger.warning(f"  Error fetching strain {strain_id}: {e}")
            return None

    def fetch_cultivation_data(
        self, strain_ids: List[int], limit: Optional[int] = None
    ) -> List[Dict[str, Any]]:
        """
        Fetch cultivation data for list of strains.

        Args:
            strain_ids: List of BacDive strain IDs
            limit: Optional limit for testing

        Returns:
            List of strains with cultivation data
        """
        if limit:
            strain_ids = strain_ids[:limit]
            logger.info(f"Limiting to {limit} strains for testing")

        logger.info(f"Fetching cultivation data for {len(strain_ids)} strains...")

        cultivation_data = []
        strains_with_media = 0
        failed = []

        for i, strain_id_obj in enumerate(strain_ids, 1):
            strain_id = strain_id_obj.get("bacdive_id")

            if i % 100 == 0:
                logger.info(
                    f"  Progress: {i}/{len(strain_ids)} "
                    f"({strains_with_media} with cultivation data)"
                )

            strain_data = self.fetch_strain_details(strain_id)

            if strain_data:
                # Extract cultivation conditions
                if self._has_cultivation_data(strain_data):
                    cultivation_data.append(strain_data)
                    strains_with_media += 1
            else:
                failed.append(strain_id)

            # Rate limiting
            time.sleep(0.1)  # 10 requests/second

        logger.info(f"\n✓ Fetched cultivation data:")
        logger.info(f"  Total strains: {len(strain_ids)}")
        logger.info(f"  With cultivation data: {strains_with_media}")
        logger.info(f"  Failed: {len(failed)}")

        return cultivation_data

    def _has_cultivation_data(self, strain_data: Dict) -> bool:
        """
        Check if strain has cultivation/media information.

        Args:
            strain_data: Complete strain data from BacDive

        Returns:
            True if strain has cultivation conditions
        """
        # BacDive structure: cultivation data in multiple sections
        cultivation_keys = [
            "culture and growth conditions",
            "culture_collection_no",
            "isolation",
        ]

        for key in cultivation_keys:
            if key in strain_data:
                data = strain_data[key]
                if data and len(data) > 0:
                    return True
        return False

    def extract_media_references(
        self, cultivation_data: List[Dict]
    ) -> Dict[str, Dict]:
        """
        Extract unique media recipes referenced in cultivation data.

        Args:
            cultivation_data: List of strains with cultivation data

        Returns:
            Dictionary of media_id -> media_info
        """
        logger.info("Extracting unique media references...")

        media_refs = {}

        for strain in cultivation_data:
            # Extract media from cultivation sections
            cult_data = strain.get("culture and growth conditions", {})

            if isinstance(cult_data, list):
                for condition in cult_data:
                    media_info = self._extract_media_from_condition(condition)
                    if media_info:
                        media_id = media_info.get("media_id")
                        if media_id and media_id not in media_refs:
                            media_refs[media_id] = media_info

        logger.info(f"✓ Extracted {len(media_refs)} unique media references")
        return media_refs

    def _extract_media_from_condition(self, condition: Dict) -> Optional[Dict]:
        """
        Extract media information from cultivation condition.

        Args:
            condition: Cultivation condition object

        Returns:
            Media information or None
        """
        # BacDive often references DSMZ media numbers
        # Example: "DSMZ Medium 1", "DSM 1", etc.

        media_name = condition.get("medium", "")
        if not media_name:
            return None

        # Extract DSMZ media number if present
        media_id = None
        if "DSMZ" in media_name or "DSM" in media_name:
            # Parse media number
            import re

            match = re.search(r"(?:DSMZ|DSM)\s*(?:Medium\s*)?(\d+)", media_name)
            if match:
                media_id = f"DSMZ_{match.group(1)}"

        return {
            "media_id": media_id or media_name.replace(" ", "_"),
            "media_name": media_name,
            "growth_temperature": condition.get("temp", ""),
            "growth_ph": condition.get("pH", ""),
            "growth_time": condition.get("time", ""),
        }

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
        logger.info(f"✓ Saved to {output_path}")
        return output_path

    def fetch_all(self, media_limit: Optional[int] = None):
        """
        Fetch all BacDive cultivation data.

        Two-stage process:
        1. Fetch all strain IDs (~100,000+)
        2. Fetch cultivation data for strains with media info (~66,570)

        Args:
            media_limit: Optional limit on strains to fetch (for testing)
        """
        logger.info("=" * 60)
        logger.info("BacDive Cultivation Data Fetcher")
        logger.info("=" * 60)

        # Stage 1: Get all strain IDs
        # Note: This is a full search and may take time
        logger.info("\n=== Stage 1: Fetching strain IDs ===")
        # For testing, we can skip this and use a smaller set
        if media_limit and media_limit < 1000:
            logger.info("Skipping full strain ID fetch for small test")
            # Use first N IDs from a range
            strain_ids = [{"bacdive_id": i} for i in range(1, media_limit + 1)]
        else:
            strain_ids = self.fetch_all_strain_ids()

        self.save_json(strain_ids, "bacdive_strain_ids.json")

        # Stage 2: Fetch cultivation data
        logger.info("\n=== Stage 2: Fetching cultivation data ===")
        cultivation_data = self.fetch_cultivation_data(strain_ids, limit=media_limit)
        self.save_json(cultivation_data, "bacdive_cultivation.json")

        # Extract unique media
        logger.info("\n=== Stage 3: Extracting media references ===")
        media_refs = self.extract_media_references(cultivation_data)
        self.save_json(media_refs, "bacdive_media_refs.json")

        # Save statistics
        stats = {
            "fetch_date": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "total_strain_ids": len(strain_ids),
            "strains_with_cultivation": len(cultivation_data),
            "unique_media_refs": len(media_refs),
        }
        self.save_json(stats, "fetch_stats.json")

        logger.info("\n" + "=" * 60)
        logger.info("✓ Fetch complete!")
        logger.info(f"  Total strains: {len(strain_ids)}")
        logger.info(f"  With cultivation data: {len(cultivation_data)}")
        logger.info(f"  Unique media refs: {len(media_refs)}")
        logger.info(f"  Output: {self.output_dir}")
        logger.info("=" * 60)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Fetch cultivation data from BacDive API"
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="raw/bacdive",
        help="Output directory for fetched data",
    )
    parser.add_argument(
        "-e",
        "--email",
        help="BacDive account email (or set BACDIVE_EMAIL env var)",
    )
    parser.add_argument(
        "-p",
        "--password",
        help="BacDive account password (or set BACDIVE_PASSWORD env var)",
    )
    parser.add_argument(
        "-l",
        "--limit",
        type=int,
        help="Limit number of strains to fetch (for testing)",
    )

    args = parser.parse_args()

    try:
        fetcher = BacDiveFetcher(
            output_dir=args.output, email=args.email, password=args.password
        )
        fetcher.fetch_all(media_limit=args.limit)
    except ImportError as e:
        logger.error(str(e))
        logger.info("\nTo install BacDive client:")
        logger.info("  pip install bacdive")
        logger.info("\nOr with uv:")
        logger.info("  uv pip install bacdive")
        exit(1)
    except Exception as e:
        logger.error(f"Error: {e}")
        logger.info("\nMake sure you have:")
        logger.info("1. Registered at https://bacdive.dsmz.de/")
        logger.info("2. Provided credentials via --email/--password or env vars")
        exit(1)


if __name__ == "__main__":
    main()
