"""
Normalize enum values in YAML files to match schema requirements.

Fixes:
1. medium_type: Convert to uppercase (COMPLEX, DEFINED, etc.)
2. physical_state: Convert to uppercase (LIQUID, SOLID_AGAR, etc.)
3. category: Convert to lowercase (bacterial, fungal, archaea, algae, specialized)
   - Replace "imported" with proper category based on directory structure
   - Fix "ALGAE" to "algae"
"""

import logging
from pathlib import Path
from typing import Dict, Any, Optional
import yaml
import re

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EnumNormalizer:
    """Normalize enum values in CultureMech YAML files."""

    # Valid enum values from schema
    VALID_MEDIUM_TYPES = {
        "DEFINED", "COMPLEX", "SELECTIVE", "DIFFERENTIAL", "ENRICHMENT", "MINIMAL"
    }

    VALID_PHYSICAL_STATES = {
        "LIQUID", "SOLID_AGAR", "SEMISOLID", "BIPHASIC"
    }

    VALID_CATEGORIES = {
        "bacterial", "fungal", "archaea", "specialized", "algae"
    }

    # Mapping for fixing common issues
    PHYSICAL_STATE_FIXES = {
        "SOLID": "SOLID_AGAR",  # Fix abbreviated form
        "solid": "SOLID_AGAR",
        "liquid": "LIQUID",
        "semisolid": "SEMISOLID",
        "biphasic": "BIPHASIC",
    }

    CATEGORY_FIXES = {
        "ALGAE": "algae",
        "BACTERIAL": "bacterial",
        "FUNGAL": "fungal",
        "ARCHAEA": "archaea",
        "SPECIALIZED": "specialized",
    }

    def __init__(self, dry_run: bool = False):
        """
        Initialize normalizer.

        Args:
            dry_run: If True, only report what would be changed
        """
        self.dry_run = dry_run
        self.stats = {
            "files_processed": 0,
            "files_modified": 0,
            "medium_type_fixed": 0,
            "physical_state_fixed": 0,
            "category_fixed": 0,
            "errors": 0
        }

    def infer_category_from_path(self, yaml_path: Path) -> Optional[str]:
        """
        Infer category from directory structure.

        Args:
            yaml_path: Path to YAML file

        Returns:
            Inferred category or None
        """
        # Check parent directory
        parent = yaml_path.parent.name.lower()

        if parent in self.VALID_CATEGORIES:
            return parent

        # Default: check for patterns in path
        path_str = str(yaml_path).lower()

        if "bacterial" in path_str:
            return "bacterial"
        elif "fungal" in path_str or "fungi" in path_str:
            return "fungal"
        elif "archaea" in path_str or "archaeal" in path_str:
            return "archaea"
        elif "algae" in path_str or "algal" in path_str:
            return "algae"
        elif "specialized" in path_str:
            return "specialized"

        # Default to bacterial if unclear
        logger.warning(f"Could not infer category from path: {yaml_path}, defaulting to 'bacterial'")
        return "bacterial"

    def normalize_medium_type(self, value: Any) -> Optional[str]:
        """
        Normalize medium_type to uppercase.

        Args:
            value: Current medium_type value

        Returns:
            Normalized value or None if invalid
        """
        if not value:
            return None

        normalized = str(value).upper().strip()

        if normalized in self.VALID_MEDIUM_TYPES:
            return normalized

        # Try to match partial strings
        for valid_type in self.VALID_MEDIUM_TYPES:
            if valid_type in normalized:
                return valid_type

        logger.warning(f"Unknown medium_type: {value}")
        return None

    def normalize_physical_state(self, value: Any) -> Optional[str]:
        """
        Normalize physical_state to uppercase.

        Args:
            value: Current physical_state value

        Returns:
            Normalized value or None if invalid
        """
        if not value:
            return None

        normalized = str(value).strip()

        # Check if it needs fixing
        if normalized in self.PHYSICAL_STATE_FIXES:
            return self.PHYSICAL_STATE_FIXES[normalized]

        # Already correct?
        normalized_upper = normalized.upper()
        if normalized_upper in self.VALID_PHYSICAL_STATES:
            return normalized_upper

        logger.warning(f"Unknown physical_state: {value}")
        return None

    def normalize_category(self, value: Any, yaml_path: Path) -> Optional[str]:
        """
        Normalize category to lowercase.

        Args:
            value: Current category value
            yaml_path: Path to YAML file (for inferring category if "imported")

        Returns:
            Normalized value or None if invalid
        """
        if not value:
            return None

        current = str(value).strip()

        # Handle "imported" - infer from path
        if current.lower() == "imported":
            return self.infer_category_from_path(yaml_path)

        # Fix capitalization
        if current in self.CATEGORY_FIXES:
            return self.CATEGORY_FIXES[current]

        # Already correct?
        if current.lower() in self.VALID_CATEGORIES:
            return current.lower()

        logger.warning(f"Unknown category: {value}")
        return None

    def normalize_file(self, yaml_path: Path) -> bool:
        """
        Normalize a single YAML file.

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

            # Normalize medium_type
            if "medium_type" in data:
                original = data["medium_type"]
                normalized = self.normalize_medium_type(original)

                if normalized and normalized != original:
                    data["medium_type"] = normalized
                    modified = True
                    self.stats["medium_type_fixed"] += 1
                    changes.append(f"medium_type: {original} → {normalized}")

            # Normalize physical_state
            if "physical_state" in data:
                original = data["physical_state"]
                normalized = self.normalize_physical_state(original)

                if normalized and normalized != original:
                    data["physical_state"] = normalized
                    modified = True
                    self.stats["physical_state_fixed"] += 1
                    changes.append(f"physical_state: {original} → {normalized}")

            # Normalize category
            if "category" in data:
                original = data["category"]
                normalized = self.normalize_category(original, yaml_path)

                if normalized and normalized != original:
                    data["category"] = normalized
                    modified = True
                    self.stats["category_fixed"] += 1
                    changes.append(f"category: {original} → {normalized}")

            # Also normalize categories (multivalued field)
            if "categories" in data and isinstance(data["categories"], list):
                original_categories = data["categories"][:]
                normalized_categories = []

                for cat in original_categories:
                    normalized = self.normalize_category(cat, yaml_path)
                    if normalized:
                        normalized_categories.append(normalized)

                if normalized_categories != original_categories:
                    data["categories"] = normalized_categories
                    modified = True
                    changes.append(f"categories: {original_categories} → {normalized_categories}")

            if modified:
                logger.info(f"{'[DRY RUN] ' if self.dry_run else ''}Modified {yaml_path.name}")
                for change in changes:
                    logger.info(f"  - {change}")

                if not self.dry_run:
                    # Write back to file, preserving formatting as much as possible
                    with open(yaml_path, 'w', encoding='utf-8') as f:
                        yaml.dump(
                            data,
                            f,
                            default_flow_style=False,
                            allow_unicode=True,
                            sort_keys=False,
                            width=100
                        )

                self.stats["files_modified"] += 1

            self.stats["files_processed"] += 1
            return modified

        except Exception as e:
            logger.error(f"Error processing {yaml_path}: {e}")
            self.stats["errors"] += 1
            return False

    def normalize_directory(self, directory: Path):
        """
        Normalize all YAML files in a directory recursively.

        Args:
            directory: Root directory to search
        """
        logger.info(f"Scanning {directory} for YAML files...")

        yaml_files = list(directory.rglob("*.yaml"))
        logger.info(f"Found {len(yaml_files)} YAML files")

        for yaml_file in yaml_files:
            self.normalize_file(yaml_file)

        # Print summary
        logger.info("\n" + "="*60)
        logger.info("NORMALIZATION SUMMARY")
        logger.info("="*60)
        logger.info(f"Files processed: {self.stats['files_processed']}")
        logger.info(f"Files modified: {self.stats['files_modified']}")
        logger.info(f"  - medium_type fixed: {self.stats['medium_type_fixed']}")
        logger.info(f"  - physical_state fixed: {self.stats['physical_state_fixed']}")
        logger.info(f"  - category fixed: {self.stats['category_fixed']}")
        logger.info(f"Errors: {self.stats['errors']}")

        if self.dry_run:
            logger.info("\nDRY RUN - No files were modified")
        else:
            logger.info(f"\n✓ Updated {self.stats['files_modified']} files")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Normalize enum values in CultureMech YAML files"
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

    normalizer = EnumNormalizer(dry_run=args.dry_run)
    normalizer.normalize_directory(args.directory)


if __name__ == "__main__":
    main()
