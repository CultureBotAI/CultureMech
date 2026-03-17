#!/usr/bin/env python3
"""
Enrich CultureMech recipes with ingredient hierarchy from MediaIngredientMech.

Usage:
    python scripts/enrich_with_hierarchy.py \
        --mim-repo /path/to/MediaIngredientMech \
        --yaml-dir data/normalized_yaml \
        --category bacterial \
        --dry-run \
        --limit 10 \
        --report-output hierarchy_enrichment_report.yaml
"""

import argparse
import logging
import subprocess
import sys
import tempfile
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from culturemech.enrich.hierarchy_importer import MediaIngredientMechHierarchyImporter
from culturemech.enrich.hierarchy_enricher import HierarchyEnricher

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def clone_mim_repo(target_dir: Path) -> Path:
    """
    Clone MediaIngredientMech repository.

    Args:
        target_dir: Directory to clone into

    Returns:
        Path to cloned repository
    """
    repo_url = "https://github.com/microbe-mech/MediaIngredientMech.git"
    logger.info(f"Cloning MediaIngredientMech from {repo_url}...")

    try:
        subprocess.run(
            ["git", "clone", "--depth", "1", repo_url, str(target_dir)],
            check=True,
            capture_output=True,
            text=True
        )
        logger.info(f"Repository cloned to {target_dir}")
        return target_dir
    except subprocess.CalledProcessError as e:
        logger.error(f"Failed to clone repository: {e.stderr}")
        raise


def main():
    parser = argparse.ArgumentParser(
        description="Enrich CultureMech recipes with MediaIngredientMech hierarchy",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "--mim-repo",
        type=Path,
        help="Path to MediaIngredientMech repository (will clone if not provided)"
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
        "--report-output",
        type=Path,
        help="Path to save enrichment report YAML"
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

    # Resolve yaml_dir
    if not args.yaml_dir.exists():
        logger.error(f"YAML directory not found: {args.yaml_dir}")
        return 1

    # Handle MediaIngredientMech repository
    temp_dir = None
    try:
        if args.mim_repo:
            mim_repo_path = args.mim_repo
            if not mim_repo_path.exists():
                logger.error(f"MediaIngredientMech repository not found: {mim_repo_path}")
                return 1
        else:
            # Clone to temporary directory
            temp_dir = tempfile.mkdtemp(prefix="mim_repo_")
            mim_repo_path = clone_mim_repo(Path(temp_dir))

        # Load hierarchy
        logger.info("Loading MediaIngredientMech hierarchy...")
        importer = MediaIngredientMechHierarchyImporter(mim_repo_path)
        importer.load_hierarchy()

        # Print hierarchy stats
        stats = importer.get_stats()
        logger.info(f"Hierarchy loaded successfully:")
        logger.info(f"  Total ingredients: {stats['total_ingredients']}")
        logger.info(f"  Parents: {stats['parents']}")
        logger.info(f"  Children: {stats['children']}")
        logger.info(f"  Families: {stats['families']}")

        # Create enricher
        enricher = HierarchyEnricher(importer)

        # Run pipeline
        result = enricher.run_pipeline(
            yaml_dir=args.yaml_dir,
            category=args.category,
            limit=args.limit,
            dry_run=args.dry_run
        )

        # Save report if requested
        if args.report_output:
            enricher.generate_report(args.report_output)

        # Print summary
        logger.info("\n" + "=" * 60)
        logger.info("Summary")
        logger.info("=" * 60)

        enrichment_stats = result['stats']
        if enrichment_stats['files_modified'] > 0:
            logger.info(f"✓ Successfully enriched {enrichment_stats['ingredients_enriched']} ingredients "
                       f"in {enrichment_stats['files_modified']} files")
        else:
            logger.info("✗ No files were modified")

        if enrichment_stats['no_mim_id'] > 0:
            logger.warning(f"  {enrichment_stats['no_mim_id']} ingredients missing MediaIngredientMech ID")

        if enrichment_stats['no_parent_found'] > 0:
            logger.info(f"  {enrichment_stats['no_parent_found']} ingredients have no parent "
                       "(likely already canonical)")

        return 0

    except Exception as e:
        logger.error(f"Pipeline failed: {e}", exc_info=True)
        return 1

    finally:
        # Cleanup temporary directory
        if temp_dir:
            import shutil
            try:
                shutil.rmtree(temp_dir)
                logger.debug(f"Cleaned up temporary directory: {temp_dir}")
            except Exception as e:
                logger.warning(f"Failed to cleanup temp directory: {e}")


if __name__ == "__main__":
    sys.exit(main())
