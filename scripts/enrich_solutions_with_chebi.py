#!/usr/bin/env python3
"""
Enrich solution YAML files with CHEBI terms.

Adds chebi_term field to composition items based on compound→CHEBI mapping.

Structure:
  composition:
  - preferred_term: Peptone
    term:
      id: mediadive.compound:1
      label: Peptone
    chebi_term:  # NEW
      id: CHEBI:XXXXX
      label: peptone
      confidence: 0.95
      match_type: exact_match
"""

import json
import sys
from pathlib import Path

import yaml
from tqdm import tqdm

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def load_compound_mapping(mapping_path: Path) -> dict:
    """Load compound→CHEBI mapping."""
    with open(mapping_path) as f:
        return json.load(f)


def load_chebi_labels(nodes_file: Path) -> dict:
    """Load CHEBI labels for enrichment."""
    print("Loading CHEBI labels...")
    chebi_labels = {}

    with open(nodes_file) as f:
        next(f)  # Skip header
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) < 3:
                continue
            node_id = parts[0]
            if node_id.startswith('CHEBI:'):
                label = parts[2] if len(parts) > 2 else ""
                chebi_labels[node_id] = label.strip()

    print(f"✓ Loaded {len(chebi_labels):,} CHEBI labels")
    return chebi_labels


def enrich_solution_yaml(
    yaml_path: Path,
    compound_mapping: dict,
    chebi_labels: dict,
    dry_run: bool = False
) -> tuple[int, int]:
    """
    Enrich a single solution YAML with CHEBI terms.

    Returns:
        (num_enriched, num_total_items)
    """
    with open(yaml_path) as f:
        data = yaml.safe_load(f)

    composition = data.get('composition', [])
    num_enriched = 0
    num_total = len(composition)

    for item in composition:
        # Get compound ID
        term = item.get('term', {})
        compound_id = term.get('id', '')

        if not compound_id.startswith('mediadive.compound:'):
            continue

        # Check if mapping exists
        if compound_id not in compound_mapping:
            continue

        # Get CHEBI mapping
        mapping = compound_mapping[compound_id]
        chebi_id = mapping['chebi_id']
        confidence = mapping['confidence']
        match_type = mapping['match_type']

        # Add chebi_term field
        if 'chebi_term' not in item:  # Only add if not already present
            item['chebi_term'] = {
                'id': chebi_id,
                'label': chebi_labels.get(chebi_id, ''),
                'confidence': confidence,
                'match_type': match_type
            }
            num_enriched += 1

    # Save enriched YAML
    if not dry_run and num_enriched > 0:
        with open(yaml_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

    return num_enriched, num_total


def enrich_all_solutions(
    solutions_dir: Path,
    compound_mapping: dict,
    chebi_labels: dict,
    dry_run: bool = False
) -> dict:
    """
    Enrich all solution YAML files.

    Returns:
        Statistics dictionary
    """
    stats = {
        'files_processed': 0,
        'files_enriched': 0,
        'items_enriched': 0,
        'items_total': 0,
        'match_type_counts': {}
    }

    solution_yamls = sorted(solutions_dir.glob("*.yaml"))

    for yaml_path in tqdm(solution_yamls, desc="Enriching solutions"):
        try:
            num_enriched, num_total = enrich_solution_yaml(
                yaml_path, compound_mapping, chebi_labels, dry_run
            )

            stats['files_processed'] += 1
            if num_enriched > 0:
                stats['files_enriched'] += 1

            stats['items_enriched'] += num_enriched
            stats['items_total'] += num_total

        except Exception as e:
            print(f"⚠ Error processing {yaml_path.name}: {e}")
            continue

    # Count match types
    for mapping in compound_mapping.values():
        match_type = mapping['match_type']
        stats['match_type_counts'][match_type] = stats['match_type_counts'].get(match_type, 0) + 1

    return stats


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Enrich solution YAML files with CHEBI terms"
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help="Show what would be enriched without modifying files"
    )
    args = parser.parse_args()

    # Paths
    solutions_dir = Path("data/normalized_yaml/solutions/mediadive")
    mapping_path = Path("data/compound_to_chebi_mapping_enhanced.json")
    nodes_file = Path("data/kgm/merged-kg_nodes.tsv")

    # Load data
    print("Loading mapping data...")
    compound_mapping = load_compound_mapping(mapping_path)
    chebi_labels = load_chebi_labels(nodes_file)

    # Enrich solutions
    print(f"\n{'='*70}")
    print(f"{'DRY RUN - ' if args.dry_run else ''}Enriching solution YAML files...")
    print(f"{'='*70}")

    stats = enrich_all_solutions(solutions_dir, compound_mapping, chebi_labels, args.dry_run)

    # Print statistics
    print(f"\n{'='*70}")
    print("ENRICHMENT STATISTICS")
    print(f"{'='*70}")
    print(f"Files processed: {stats['files_processed']:,}")
    print(f"Files enriched: {stats['files_enriched']:,}")
    print(f"Composition items enriched: {stats['items_enriched']:,} / {stats['items_total']:,}")
    enrichment_pct = (stats['items_enriched'] / stats['items_total'] * 100) if stats['items_total'] > 0 else 0
    print(f"Enrichment coverage: {enrichment_pct:.1f}%")

    print(f"\nMatch type distribution:")
    for match_type, count in sorted(stats['match_type_counts'].items(), key=lambda x: -x[1]):
        pct = (count / len(compound_mapping) * 100) if compound_mapping else 0
        print(f"  {match_type:30s}: {count:4d} ({pct:5.1f}%)")

    if args.dry_run:
        print(f"\n⚠ DRY RUN - No files were modified")
        print(f"Run without --dry-run to apply changes")
    else:
        print(f"\n✓ Solution YAML files enriched with CHEBI terms")


if __name__ == "__main__":
    main()
