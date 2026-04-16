#!/usr/bin/env python3
"""Assign taxonomy classifications to CultureMech media recipes.

Processes media recipes and assigns 4-level taxonomy:
- Level 1: Functional Domain
- Level 2: Environmental Context
- Level 3: Nutritional Profile
- Level 4: Specific Formulation

Usage:
    python scripts/assign_taxonomy.py --dry-run
    python scripts/assign_taxonomy.py --sample 100
    python scripts/assign_taxonomy.py  # Process all
"""

import argparse
import yaml
from pathlib import Path
from collections import Counter

# Add src to path for imports
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from culturemech.taxonomy import TaxonomyClassifier


def assign_taxonomy_to_recipes(
    data_dir: Path,
    dry_run: bool = True,
    sample_size: int = None
) -> dict:
    """
    Assign taxonomy to all recipes in data directory.

    Args:
        data_dir: Path to normalized_yaml directory
        dry_run: If True, don't write changes
        sample_size: If set, only process this many recipes

    Returns:
        Statistics dict
    """
    classifier = TaxonomyClassifier()

    stats = {
        'total_processed': 0,
        'domains': Counter(),
        'contexts': Counter(),
        'carbon_sources': Counter(),
        'nitrogen_sources': Counter(),
        'avg_confidence': 0.0
    }

    yaml_files = list(data_dir.glob('**/*.yaml'))

    if sample_size:
        yaml_files = yaml_files[:sample_size]

    print(f"Processing {len(yaml_files)} recipes...")

    confidences = []

    for yaml_file in yaml_files:
        try:
            with open(yaml_file) as f:
                recipe = yaml.safe_load(f)

            if not recipe or 'ingredients' not in recipe:
                continue

            # Assign taxonomy
            taxonomy = classifier.classify_recipe(recipe)

            # Update stats
            stats['total_processed'] += 1
            stats['domains'][taxonomy['domain']] += 1

            for context in taxonomy['context']:
                stats['contexts'][context] += 1

            for carbon in taxonomy['profile']['carbon_sources']:
                stats['carbon_sources'][carbon] += 1

            for nitrogen in taxonomy['profile']['nitrogen_sources']:
                stats['nitrogen_sources'][nitrogen] += 1

            confidences.append(taxonomy['confidence_score'])

            # Write back if not dry-run
            if not dry_run:
                recipe['taxonomy'] = taxonomy

                with open(yaml_file, 'w') as f:
                    yaml.dump(recipe, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

            # Print progress
            if stats['total_processed'] % 100 == 0:
                print(f"  Processed {stats['total_processed']} recipes...")

        except Exception as e:
            print(f"⚠️  Error processing {yaml_file}: {e}")

    # Calculate average confidence
    if confidences:
        stats['avg_confidence'] = sum(confidences) / len(confidences)

    return stats


def print_statistics(stats: dict):
    """Print taxonomy assignment statistics."""
    print("\n" + "="*80)
    print("TAXONOMY ASSIGNMENT STATISTICS")
    print("="*80)

    print(f"\nTotal recipes processed: {stats['total_processed']}")
    print(f"Average confidence: {stats['avg_confidence']:.2f}")

    print("\n" + "-"*80)
    print("DOMAIN DISTRIBUTION (Level 1)")
    print("-"*80)
    for domain, count in stats['domains'].most_common():
        pct = (count / stats['total_processed']) * 100
        print(f"  {domain:20s}: {count:5d} ({pct:5.1f}%)")

    print("\n" + "-"*80)
    print("ENVIRONMENTAL CONTEXT (Level 2)")
    print("-"*80)
    for context, count in stats['contexts'].most_common(10):
        pct = (count / stats['total_processed']) * 100
        print(f"  {context:20s}: {count:5d} ({pct:5.1f}%)")

    print("\n" + "-"*80)
    print("CARBON SOURCES (Level 3)")
    print("-"*80)
    for carbon, count in stats['carbon_sources'].most_common(8):
        pct = (count / stats['total_processed']) * 100
        print(f"  {carbon:25s}: {count:5d} ({pct:5.1f}%)")

    print("\n" + "-"*80)
    print("NITROGEN SOURCES (Level 3)")
    print("-"*80)
    for nitrogen, count in stats['nitrogen_sources'].most_common(6):
        pct = (count / stats['total_processed']) * 100
        print(f"  {nitrogen:25s}: {count:5d} ({pct:5.1f}%)")

    print("\n" + "="*80)


def main():
    parser = argparse.ArgumentParser(
        description='Assign taxonomy to CultureMech media recipes'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview changes without writing files'
    )
    parser.add_argument(
        '--sample',
        type=int,
        help='Process only N recipes (for testing)'
    )
    parser.add_argument(
        '--data-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Path to normalized_yaml directory'
    )

    args = parser.parse_args()

    if args.dry_run:
        print("⚠️  DRY RUN MODE - No files will be modified\n")

    # Assign taxonomy
    stats = assign_taxonomy_to_recipes(
        args.data_dir,
        dry_run=args.dry_run,
        sample_size=args.sample
    )

    # Print statistics
    print_statistics(stats)

    if args.dry_run:
        print("\n⚠️  DRY RUN - No files were modified")
        print("Run without --dry-run to apply taxonomy assignments")
    else:
        print(f"\n✓ Taxonomy assigned to {stats['total_processed']} recipes")


if __name__ == '__main__':
    main()
