#!/usr/bin/env python3
"""
Assign ingredient roles from MediaIngredientMech to CultureMech recipes.

Usage:
    python scripts/assign_ingredient_roles.py \
        --mim-repo /path/to/MediaIngredientMech \
        --yaml-dir data/normalized_yaml \
        --category bacterial \
        --dry-run \
        --limit 10
"""

import argparse
import logging
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from culturemech.enrich.role_importer import RoleImporter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Assign ingredient roles from MediaIngredientMech",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "--mim-repo",
        type=Path,
        required=True,
        help="Path to MediaIngredientMech repository"
    )

    parser.add_argument(
        "--yaml-dir",
        type=Path,
        default=Path("data/normalized_yaml"),
        help="Directory containing normalized YAML files (default: data/normalized_yaml)"
    )

    parser.add_argument(
        "--category",
        type=str,
        choices=["bacterial", "fungal", "archaea", "specialized", "algae"],
        help="Process only specific category"
    )

    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of files to process (for testing)"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't modify files, just show what would be done"
    )

    parser.add_argument(
        "--no-inherit",
        action="store_true",
        help="Don't inherit roles from parent ingredients"
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Validate paths
    if not args.mim_repo.exists():
        logger.error(f"MediaIngredientMech repository not found: {args.mim_repo}")
        return 1

    if not args.yaml_dir.exists():
        logger.error(f"YAML directory not found: {args.yaml_dir}")
        return 1

    try:
        # Create role importer
        logger.info("Initializing role importer...")
        importer = RoleImporter(args.mim_repo)

        # Load roles
        importer.load_roles()

        # Run pipeline
        result = importer.run_pipeline(
            yaml_dir=args.yaml_dir,
            category=args.category,
            limit=args.limit,
            dry_run=args.dry_run,
            inherit_from_parent=not args.no_inherit
        )

        # Print summary
        stats = result['stats']
        logger.info("\n" + "=" * 60)
        logger.info("Summary")
        logger.info("=" * 60)

        if stats['files_modified'] > 0:
            logger.info(f"✓ Successfully assigned roles to {stats['ingredients_assigned']} ingredients "
                       f"in {stats['files_modified']} files")
        else:
            logger.info("✗ No files were modified")

        if stats['no_mim_id'] > 0:
            logger.warning(f"  {stats['no_mim_id']} ingredients missing MediaIngredientMech ID")

        if stats['no_roles_found'] > 0:
            logger.info(f"  {stats['no_roles_found']} ingredients have no role assignments")

        return 0

    except Exception as e:
        logger.error(f"Pipeline failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
