"""Extract preparation steps from MediaDive API solution data.

Parses MediaDive solution steps and recipe data into CultureMech
PreparationStep objects with appropriate PreparationActionEnum values.
"""

import json
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
import requests
import time
import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PreparationStepsExtractor:
    """Extract and enrich preparation steps from MediaDive API."""

    BASE_URL = "https://mediadive.dsmz.de/rest"
    DEFAULT_DELAY = 0.3  # Conservative rate limiting

    # Mapping of keywords to PreparationActionEnum
    ACTION_PATTERNS = [
        (r'\b(dissolve|add.*to.*water|suspend)\b', 'DISSOLVE'),
        (r'\b(mix|stir|shake|combine)\b', 'MIX'),
        (r'\b(heat|warm|boil)\b', 'HEAT'),
        (r'\b(cool|chill)\b', 'COOL'),
        (r'\b(autoclave|sterilize.*pressure)\b', 'AUTOCLAVE'),
        (r'\b(filter|sterilize.*filter|0\.22|0\.2\s*μ?m)\b', 'FILTER_STERILIZE'),
        (r'\b(adjust.*ph|ph.*to)\b', 'ADJUST_PH'),
        (r'\b(add.*agar|agar.*for solid)\b', 'ADD_AGAR'),
        (r'\b(pour.*plate|dispense.*petri)\b', 'POUR_PLATES'),
        (r'\b(aliquot|divide|distribute)\b', 'ALIQUOT'),
        (r'\b(store|storage|keep at)\b', 'STORE'),
    ]

    def __init__(self, delay: float = DEFAULT_DELAY, timeout: float = 30.0):
        """
        Initialize extractor.

        Args:
            delay: Seconds between API calls
            timeout: Request timeout in seconds
        """
        self.delay = delay
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json",
            "User-Agent": "CultureMech/0.1.0 (github.com/KG-Hub/CultureMech)"
        })

    def fetch_medium_details(self, medium_id: int) -> Optional[Dict[str, Any]]:
        """
        Fetch detailed medium data from MediaDive API.

        Args:
            medium_id: MediaDive medium ID

        Returns:
            Medium data dict or None if failed
        """
        url = f"{self.BASE_URL}/medium/{medium_id}"

        try:
            response = self.session.get(url, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            if data.get("status") == 200 and "data" in data:
                return data["data"]
            else:
                logger.warning(f"Medium {medium_id}: No data (status {data.get('status')})")
                return None

        except requests.RequestException as e:
            logger.warning(f"Medium {medium_id}: Request failed - {e}")
            return None

    def extract_preparation_steps(
        self,
        medium_data: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        """
        Extract preparation steps from medium data.

        Args:
            medium_data: Full medium data from API

        Returns:
            List of PreparationStep dicts
        """
        steps = []
        step_number = 1

        # Extract from all solutions
        for solution in medium_data.get("solutions", []):
            # First, add ingredient dissolution step if we have a recipe
            recipe = solution.get("recipe", [])
            if recipe:
                # Check if ingredients need dissolving
                ingredients = [item.get("compound", "") for item in recipe]
                if ingredients:
                    steps.append({
                        "step_number": step_number,
                        "action": "DISSOLVE",
                        "description": f"Dissolve all ingredients in distilled water to specified concentrations"
                    })
                    step_number += 1

            # Parse solution steps
            for step_data in solution.get("steps", []):
                step_text = step_data.get("step", "").strip()
                if not step_text:
                    continue

                # Determine action from text
                action = self._classify_action(step_text)

                step_dict = {
                    "step_number": step_number,
                    "action": action,
                    "description": step_text
                }

                # Extract temperature if mentioned
                temp = self._extract_temperature(step_text)
                if temp:
                    step_dict["temperature"] = temp

                # Extract duration if mentioned
                duration = self._extract_duration(step_text)
                if duration:
                    step_dict["duration"] = duration

                steps.append(step_dict)
                step_number += 1

        # Add default sterilization step if not already present
        if steps and not any("AUTOCLAVE" in s.get("action", "") or "FILTER_STERILIZE" in s.get("action", "") for s in steps):
            # Check if medium has agar (solid)
            has_agar = any(
                any("agar" in item.get("compound", "").lower()
                    for item in sol.get("recipe", []))
                for sol in medium_data.get("solutions", [])
            )

            if has_agar:
                steps.append({
                    "step_number": step_number,
                    "action": "AUTOCLAVE",
                    "description": "Sterilize by autoclaving (121°C, 15 psi, 15-20 min)"
                })
            else:
                steps.append({
                    "step_number": step_number,
                    "action": "FILTER_STERILIZE",
                    "description": "Sterilize by filtration (0.22 μm) to preserve heat-sensitive components"
                })

        return steps

    def _classify_action(self, step_text: str) -> str:
        """
        Classify step text into PreparationActionEnum.

        Args:
            step_text: Step description

        Returns:
            Action enum value (defaults to "MIX" if unclear)
        """
        text_lower = step_text.lower()

        for pattern, action in self.ACTION_PATTERNS:
            if re.search(pattern, text_lower):
                return action

        # Default to MIX for unclassified steps
        return "MIX"

    def _extract_temperature(self, text: str) -> Optional[Dict[str, Any]]:
        """
        Extract temperature value from text.

        Args:
            text: Step description

        Returns:
            TemperatureValue dict or None
        """
        # Match patterns like "121°C", "15°C", "37 degrees"
        temp_pattern = r'(\d+)\s*°?[CcFf]'
        match = re.search(temp_pattern, text)

        if match:
            value = float(match.group(1))
            # Assume Celsius unless Fahrenheit explicitly mentioned
            unit = "CELSIUS" if "F" not in match.group(0).upper() else "FAHRENHEIT"
            return {
                "value": value,
                "unit": unit
            }

        return None

    def _extract_duration(self, text: str) -> Optional[str]:
        """
        Extract duration from text.

        Args:
            text: Step description

        Returns:
            Duration string or None
        """
        # Match patterns like "15 min", "20 minutes", "overnight", "1 hour"
        duration_patterns = [
            r'\d+\s*min(?:ute)?s?',
            r'\d+\s*h(?:ou)?r?s?',
            r'\d+\s*sec(?:ond)?s?',
            r'overnight',
            r'\d+\s*day?s?'
        ]

        for pattern in duration_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(0)

        return None

    def enrich_yaml_file(
        self,
        yaml_path: Path,
        medium_id: Optional[int] = None,
        dry_run: bool = False
    ) -> bool:
        """
        Add preparation steps to a YAML file.

        Args:
            yaml_path: Path to YAML file
            medium_id: MediaDive medium ID (extracted from filename if None)
            dry_run: If True, only print what would be done

        Returns:
            True if successful, False otherwise
        """
        # Load existing YAML
        with open(yaml_path, 'r', encoding='utf-8') as f:
            recipe_data = yaml.safe_load(f)

        # Extract medium ID from filename or media_term if not provided
        if medium_id is None:
            # First try filename pattern: MEDIADB_123_Name.yaml
            match = re.search(r'MEDIADB[_\s](\d+)', yaml_path.stem)
            if match:
                medium_id = int(match.group(1))
            # Then try DSMZ pattern: DSMZ_123_Name.yaml
            elif re.search(r'DSMZ[_\s](\d+)', yaml_path.stem):
                match = re.search(r'DSMZ[_\s](\d+)', yaml_path.stem)
                medium_id = int(match.group(1))
            # Finally try extracting from media_term field
            elif recipe_data.get("media_term", {}).get("term", {}).get("id"):
                term_id = recipe_data["media_term"]["term"]["id"]
                # Pattern: mediadive.medium:123
                match = re.search(r'mediadive\.medium:(\d+)', term_id)
                if match:
                    medium_id = int(match.group(1))

        if medium_id is None:
            logger.warning(f"Could not extract medium ID from {yaml_path.name}")
            return False

        # Check if already has preparation steps
        if recipe_data.get("preparation_steps"):
            logger.info(f"  Skipping {yaml_path.name} (already has preparation steps)")
            return True

        # Fetch medium details from API
        medium_data = self.fetch_medium_details(medium_id)
        if not medium_data:
            logger.warning(f"  Failed to fetch medium {medium_id} for {yaml_path.name}")
            return False

        # Extract preparation steps
        prep_steps = self.extract_preparation_steps(medium_data)
        if not prep_steps:
            logger.info(f"  No preparation steps found for {yaml_path.name}")
            return True

        if dry_run:
            logger.info(f"  Would add {len(prep_steps)} steps to {yaml_path.name}")
            return True

        # Add preparation steps to recipe
        recipe_data["preparation_steps"] = prep_steps

        # Add curation history entry
        if "curation_history" not in recipe_data:
            recipe_data["curation_history"] = []

        recipe_data["curation_history"].append({
            "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.000000Z", time.gmtime()),
            "curator": "preparation-steps-enrichment",
            "action": "Added preparation steps from MediaDive API",
            "notes": f"Extracted {len(prep_steps)} preparation steps from solution data"
        })

        # Save updated YAML
        with open(yaml_path, 'w', encoding='utf-8') as f:
            yaml.dump(recipe_data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        logger.info(f"  ✓ Added {len(prep_steps)} steps to {yaml_path.name}")
        return True

    def enrich_all_mediadb_files(
        self,
        yaml_dir: Path,
        limit: Optional[int] = None,
        dry_run: bool = False
    ):
        """
        Enrich all MediaDive (MEDIADB and DSMZ) YAML files with preparation steps.

        Args:
            yaml_dir: Directory containing YAML files
            limit: Optional limit for testing
            dry_run: If True, only print what would be done
        """
        # Find all MediaDive files (MEDIADB and DSMZ)
        mediadb_files = list(yaml_dir.glob("**/MEDIADB_*.yaml"))
        dsmz_files = list(yaml_dir.glob("**/DSMZ_*.yaml"))
        all_files = sorted(mediadb_files + dsmz_files)

        if limit:
            all_files = all_files[:limit]

        logger.info(f"Found {len(all_files)} MediaDive files (MEDIADB + DSMZ)")
        if dry_run:
            logger.info("DRY RUN - no files will be modified")

        success_count = 0
        skip_count = 0
        fail_count = 0

        for i, yaml_path in enumerate(all_files, 1):
            if i % 50 == 0:
                logger.info(f"Progress: {i}/{len(all_files)} ({i/len(all_files)*100:.1f}%)")

            result = self.enrich_yaml_file(yaml_path, dry_run=dry_run)

            if result:
                success_count += 1
            else:
                fail_count += 1

            # Rate limiting
            if i < len(all_files):
                time.sleep(self.delay)

        logger.info(f"\nResults:")
        logger.info(f"  ✓ Success: {success_count}")
        logger.info(f"  ✗ Failed: {fail_count}")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Extract preparation steps from MediaDive API"
    )
    parser.add_argument(
        "yaml_dir",
        type=Path,
        help="Directory containing YAML files to enrich"
    )
    parser.add_argument(
        "-l", "--limit",
        type=int,
        help="Limit number of files to process (for testing)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without modifying files"
    )
    parser.add_argument(
        "-d", "--delay",
        type=float,
        default=0.3,
        help="Delay between API calls in seconds (default: 0.3)"
    )

    args = parser.parse_args()

    extractor = PreparationStepsExtractor(delay=args.delay)
    extractor.enrich_all_mediadb_files(
        yaml_dir=args.yaml_dir,
        limit=args.limit,
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()
