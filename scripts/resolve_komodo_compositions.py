#!/usr/bin/env python3
"""Resolve KOMODO recipes with empty ingredients using DSMZ compositions.

KOMODO web importer creates placeholder recipes with empty ingredients[]
for media that reference DSMZ numbers. This script:
1. Finds KOMODO recipes with empty ingredients
2. Extracts DSMZ medium numbers from notes field
3. Copies ingredients/solutions from matching DSMZ recipes
4. Adds enrichment provenance to curation_history

Usage:
    python scripts/resolve_komodo_compositions.py [OPTIONS]

Options:
    --dry-run              Show what would be resolved without writing
    --normalized-dir DIR   Directory with normalized recipes (default: data/normalized_yaml)
    --report-unresolved    List KOMODO recipes that couldn't be resolved
    --verbose              Show detailed progress
"""

import argparse
import logging
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from culturemech.enrich import DSMZCompositionResolver


logger = logging.getLogger(__name__)


def print_stats(stats: dict):
    """Print resolution statistics.

    Args:
        stats: Statistics dictionary from resolver
    """
    print("\n" + "="*60)
    print("KOMODO COMPOSITION RESOLUTION")
    print("="*60)
    print(f"Total KOMODO recipes:     {stats['total_komodo']}")
    print(f"Already complete:         {stats['already_complete']}")
    print(f"Empty ingredients:        {stats['empty_ingredients']}")
    print(f"  - Resolved:             {stats['resolved']}")
    print(f"  - Failed:               {stats['failed']}")
    print("="*60 + "\n")


def print_failures(stats: dict):
    """Print detailed failure information.

    Args:
        stats: Statistics dictionary with failures
    """
    if not stats['failures']:
        return

    print("\nFailed resolutions:")
    print("-"*60)

    # Group by error type
    error_groups = {}
    for failure in stats['failures']:
        error = failure['error']
        if error not in error_groups:
            error_groups[error] = []
        error_groups[error].append(failure['file'])

    for error, files in sorted(error_groups.items(), key=lambda x: len(x[1]), reverse=True):
        print(f"\n{error} ({len(files)} recipes):")
        for f in files[:5]:  # Show first 5
            print(f"  - {f}")
        if len(files) > 5:
            print(f"  ... and {len(files) - 5} more")

    print("-"*60 + "\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Resolve KOMODO empty recipes with DSMZ compositions',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be resolved without writing files'
    )

    parser.add_argument(
        '--normalized-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Directory with normalized recipes (default: data/normalized_yaml)'
    )

    parser.add_argument(
        '--report-unresolved',
        action='store_true',
        help='Show detailed report of unresolved recipes'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed progress'
    )

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format='%(message)s'
    )

    # Validate input directory
    if not args.normalized_dir.exists():
        logger.error(f"Normalized directory not found: {args.normalized_dir}")
        sys.exit(1)

    if args.dry_run:
        logger.info("DRY RUN MODE - no files will be modified\n")

    # Create resolver
    logger.info("Building DSMZ recipe index...")
    resolver = DSMZCompositionResolver(args.normalized_dir)

    # Resolve recipes
    logger.info("\nResolving KOMODO recipes...")
    stats = resolver.resolve_directory(dry_run=args.dry_run)

    # Print results
    print_stats(stats)

    if args.report_unresolved and stats['failed'] > 0:
        print_failures(stats)

    # Summary message
    if args.dry_run:
        print(f"Would resolve {stats['resolved']} recipes")
    else:
        print(f"Resolved {stats['resolved']} recipes")

        if stats['resolved'] > 0:
            print("\nNext steps:")
            print("  1. Run validation: just validation-stats")
            print("  2. Re-run merge: just merge-recipes")


if __name__ == '__main__':
    main()
