"""
Fix unnamed media and detect physical state from ingredients.

Issues to fix:
1. Recipes with "(Unnamed medium)" should use their database ID as the name
2. Physical state should be SOLID_AGAR if agar is in ingredients
"""

import logging
from pathlib import Path
import yaml
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MediaFixer:
    """Fix unnamed media and physical state detection."""

    def __init__(self, dry_run: bool = False):
        """
        Initialize fixer.

        Args:
            dry_run: If True, only report what would be changed
        """
        self.dry_run = dry_run
        self.stats = {
            "files_processed": 0,
            "unnamed_fixed": 0,
            "physical_state_fixed": 0,
            "errors": 0
        }

    def has_agar_ingredient(self, recipe: dict) -> bool:
        """
        Check if recipe has agar as an ingredient.

        Args:
            recipe: Recipe dict

        Returns:
            True if agar found in ingredients
        """
        ingredients = recipe.get("ingredients", [])

        for ingredient in ingredients:
            preferred_term = ingredient.get("preferred_term", "").lower()

            # Check for agar variants
            if "agar" in preferred_term:
                return True

            # Also check alternative_terms
            alt_terms = ingredient.get("alternative_terms", [])
            for term in alt_terms:
                if "agar" in term.lower():
                    return True

        return False

    def extract_database_id(self, recipe: dict) -> tuple[str, str]:
        """
        Extract database name and ID from media_term.

        Args:
            recipe: Recipe dict

        Returns:
            Tuple of (database, id) e.g., ("TOGO", "M1466")
        """
        media_term = recipe.get("media_term", {})
        if isinstance(media_term, dict):
            term = media_term.get("term", {})
            if isinstance(term, dict):
                term_id = term.get("id", "")
                if ":" in term_id:
                    parts = term_id.split(":", 1)
                    return (parts[0], parts[1])

        return (None, None)

    def fix_file(self, yaml_path: Path) -> bool:
        """
        Fix a single YAML file.

        Args:
            yaml_path: Path to YAML file

        Returns:
            True if file was modified, False otherwise
        """
        try:
            with open(yaml_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            if not isinstance(data, dict):
                logger.warning(f"Skipping {yaml_path}: not a dict")
                return False

            modified = False
            changes = []

            # Fix 1: Unnamed media
            name = data.get("name", "")
            if name in ["(Unnamed medium)", "Unnamed medium", "(unnamed medium)", "unnamed medium"]:
                database, db_id = self.extract_database_id(data)

                if database and db_id:
                    new_name = f"{database} Medium {db_id}"
                    data["name"] = new_name

                    # Also update media_term label if it's unnamed
                    if "media_term" in data:
                        media_term = data["media_term"]
                        if isinstance(media_term, dict):
                            term = media_term.get("term", {})
                            if isinstance(term, dict) and term.get("label") in [
                                "(Unnamed medium)", "Unnamed medium", "(unnamed medium)", "unnamed medium"
                            ]:
                                term["label"] = new_name

                    modified = True
                    self.stats["unnamed_fixed"] += 1
                    changes.append(f"name: {name} → {new_name}")

            # Fix 2: Physical state based on agar
            if self.has_agar_ingredient(data):
                current_state = data.get("physical_state", "")

                # Only update if currently LIQUID or empty
                if current_state in ["LIQUID", "liquid", ""]:
                    data["physical_state"] = "SOLID_AGAR"
                    modified = True
                    self.stats["physical_state_fixed"] += 1
                    changes.append(f"physical_state: {current_state or 'empty'} → SOLID_AGAR (agar detected)")

            if modified:
                logger.info(f"{'[DRY RUN] ' if self.dry_run else ''}Modified {yaml_path.name}")
                for change in changes:
                    logger.info(f"  - {change}")

                if not self.dry_run:
                    # Write back to file
                    with open(yaml_path, 'w', encoding='utf-8') as f:
                        yaml.dump(
                            data,
                            f,
                            default_flow_style=False,
                            allow_unicode=True,
                            sort_keys=False,
                            width=100
                        )

            self.stats["files_processed"] += 1
            return modified

        except Exception as e:
            logger.error(f"Error processing {yaml_path}: {e}")
            self.stats["errors"] += 1
            return False

    def fix_directory(self, directory: Path):
        """
        Fix all YAML files in a directory recursively.

        Args:
            directory: Root directory to search
        """
        logger.info(f"Scanning {directory} for YAML files...")

        yaml_files = list(directory.rglob("*.yaml"))
        logger.info(f"Found {len(yaml_files)} YAML files")

        files_modified = 0
        for yaml_file in yaml_files:
            if self.fix_file(yaml_file):
                files_modified += 1

        # Print summary
        logger.info("\n" + "="*60)
        logger.info("FIX SUMMARY")
        logger.info("="*60)
        logger.info(f"Files processed: {self.stats['files_processed']}")
        logger.info(f"Files modified: {files_modified}")
        logger.info(f"  - Unnamed media fixed: {self.stats['unnamed_fixed']}")
        logger.info(f"  - Physical state fixed: {self.stats['physical_state_fixed']}")
        logger.info(f"Errors: {self.stats['errors']}")

        if self.dry_run:
            logger.info("\nDRY RUN - No files were modified")
        else:
            logger.info(f"\n✓ Updated {files_modified} files")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Fix unnamed media and detect physical state from ingredients"
    )
    parser.add_argument(
        "directory",
        type=Path,
        nargs="?",
        default=Path("data/normalized_yaml"),
        help="Directory containing YAML files (default: data/normalized_yaml)"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying files"
    )

    args = parser.parse_args()

    if not args.directory.exists():
        logger.error(f"Directory not found: {args.directory}")
        return

    fixer = MediaFixer(dry_run=args.dry_run)
    fixer.fix_directory(args.directory)


if __name__ == "__main__":
    main()
