#!/usr/bin/env python3
"""
CLI script to enrich CultureMech recipes with MediaIngredientMech identifiers.

This script:
1. Clones the MediaIngredientMech repository from GitHub
2. Loads ingredient data from unmapped_ingredients.yaml
3. Matches CultureMech ingredients to MediaIngredientMech IDs
4. Adds mediaingredientmech_term fields to recipe YAML files
5. Generates a JSON report with statistics
"""

import argparse
import json
import logging
import sys
import tempfile
from pathlib import Path

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from culturemech.enrich.mediaingredientmech_loader import MediaIngredientMechLoader
from culturemech.enrich.mediaingredientmech_linker import MediaIngredientMechLinker

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Enrich CultureMech recipes with MediaIngredientMech identifiers",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Dry run on first 10 files
  python scripts/enrich_with_mediaingredientmech.py --dry-run --limit 10

  # Process all bacterial media
  python scripts/enrich_with_mediaingredientmech.py --category bacterial

  # Process with custom MediaIngredientMech repo location
  python scripts/enrich_with_mediaingredientmech.py --mim-repo /path/to/MediaIngredientMech

  # Generate detailed report
  python scripts/enrich_with_mediaingredientmech.py --report-output enrichment_report.json
        """
    )

    parser.add_argument(
        '--yaml-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Directory containing normalized recipe YAML files (default: data/normalized_yaml)'
    )

    parser.add_argument(
        '--mim-repo',
        type=Path,
        help='Path to existing MediaIngredientMech repository (if not provided, will clone from GitHub)'
    )

    parser.add_argument(
        '--category',
        choices=['bacterial', 'fungal', 'archaea', 'algae', 'specialized', 'imported'],
        help='Process only files in specified category'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of files to process (useful for testing)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be done without modifying files'
    )

    parser.add_argument(
        '--report-output',
        type=Path,
        help='Path to save JSON report with statistics and unmatched ingredients'
    )

    parser.add_argument(
        '--fuzzy-threshold',
        type=float,
        default=0.95,
        help='Fuzzy matching threshold (0.0-1.0, default: 0.95)'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Validate inputs
    if not args.yaml_dir.exists():
        logger.error(f"YAML directory not found: {args.yaml_dir}")
        return 1

    # Step 1: Get or clone MediaIngredientMech repository
    if args.mim_repo:
        if not args.mim_repo.exists():
            logger.error(f"MediaIngredientMech repo not found: {args.mim_repo}")
            return 1
        repo_path = args.mim_repo
        temp_dir = None
        logger.info(f"Using existing MediaIngredientMech repo: {repo_path}")
    else:
        # Clone into temporary directory
        temp_dir = tempfile.mkdtemp(prefix='mediaingredientmech_')
        repo_path = Path(temp_dir) / 'MediaIngredientMech'
        try:
            MediaIngredientMechLoader.clone_repo(repo_path)
        except Exception as e:
            logger.error(f"Failed to clone MediaIngredientMech repository: {e}")
            return 1

    try:
        # Step 2: Load MediaIngredientMech data
        logger.info("Loading MediaIngredientMech data...")
        loader = MediaIngredientMechLoader(repo_path=repo_path)

        if not loader.ingredients:
            logger.error("No ingredients loaded from MediaIngredientMech repository")
            return 1

        # Step 3: Create linker and run pipeline
        linker = MediaIngredientMechLinker(loader)

        result = linker.run_pipeline(
            yaml_dir=args.yaml_dir,
            category=args.category,
            limit=args.limit,
            dry_run=args.dry_run
        )

        # Step 4: Generate report if requested
        if args.report_output:
            report = {
                'parameters': {
                    'yaml_dir': str(args.yaml_dir),
                    'category': args.category,
                    'limit': args.limit,
                    'dry_run': args.dry_run,
                    'fuzzy_threshold': args.fuzzy_threshold
                },
                'statistics': result['stats'],
                'unmatched_ingredients': result['unmatched_ingredients']
            }

            with open(args.report_output, 'w', encoding='utf-8') as f:
                json.dump(report, f, indent=2, ensure_ascii=False)

            logger.info(f"\nReport saved to: {args.report_output}")

            # Print unmatched ingredients summary
            if result['unmatched_ingredients']:
                logger.info(f"\nFound {len(result['unmatched_ingredients'])} unmatched ingredients")
                logger.info("See report for full list")

        logger.info("\nEnrichment complete!")
        return 0

    finally:
        # Cleanup temporary directory if created
        if temp_dir:
            import shutil
            shutil.rmtree(temp_dir, ignore_errors=True)
            logger.debug(f"Cleaned up temporary directory: {temp_dir}")


if __name__ == '__main__':
    sys.exit(main())
