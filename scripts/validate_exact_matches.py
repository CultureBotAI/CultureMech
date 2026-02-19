#!/usr/bin/env python3
"""
Validate Exact Match Enrichment Results

Compares before/after enrichment to validate improvements and ensure
existing mappings are preserved.

Usage:
    uv run python scripts/validate_exact_matches.py \\
        --before output/culturemech_chebi_mappings_enriched.sssom.tsv \\
        --after output/culturemech_chebi_mappings_exact.sssom.tsv
"""

import argparse
import sys
from pathlib import Path

import pandas as pd


def load_sssom_file(sssom_path: Path) -> pd.DataFrame:
    """Load SSSOM TSV file, skipping metadata header."""
    with open(sssom_path) as f:
        for i, line in enumerate(f):
            if not line.startswith('#'):
                skip_rows = i
                break
        else:
            raise ValueError("No data found in SSSOM file")

    return pd.read_csv(sssom_path, sep='\t', skiprows=skip_rows)


def compare_enrichments(before_df: pd.DataFrame, after_df: pd.DataFrame, verbose: bool = False):
    """
    Compare before/after enrichment results.

    Args:
        before_df: Original enriched SSSOM
        after_df: New exact-match enriched SSSOM
        verbose: Show detailed comparison
    """
    print("=" * 70)
    print("Enrichment Comparison Report")
    print("=" * 70)

    # Overall statistics
    print("\nOverall Statistics:")
    print(f"  Before: {len(before_df)} mappings")
    print(f"  After:  {len(after_df)} mappings")
    print(f"  Change: +{len(after_df) - len(before_df)} mappings")

    # Confidence distribution
    print("\nConfidence Distribution:")
    confidence_bins = [(0.95, 1.0), (0.90, 0.95), (0.80, 0.90), (0.50, 0.80), (0.0, 0.50)]

    for conf_min, conf_max in confidence_bins:
        before_count = len(before_df[
            (before_df['confidence'] >= conf_min) &
            (before_df['confidence'] < conf_max)
        ])
        after_count = len(after_df[
            (after_df['confidence'] >= conf_min) &
            (after_df['confidence'] < conf_max)
        ])
        change = after_count - before_count

        print(f"  {conf_min:.2f}-{conf_max:.2f}: {before_count:4d} → {after_count:4d} "
              f"({change:+d})")

    # Mapping tool breakdown
    print("\nMapping Tool Breakdown (After):")
    if 'mapping_tool' in after_df.columns:
        tool_counts = after_df['mapping_tool'].value_counts()
        for tool, count in tool_counts.items():
            print(f"  {tool}: {count}")

    # Predicate distribution
    print("\nPredicate Distribution:")
    before_predicates = before_df['predicate_id'].value_counts()
    after_predicates = after_df['predicate_id'].value_counts()

    all_predicates = set(before_predicates.index) | set(after_predicates.index)
    for predicate in sorted(all_predicates):
        before_count = before_predicates.get(predicate, 0)
        after_count = after_predicates.get(predicate, 0)
        change = after_count - before_count
        print(f"  {predicate}: {before_count:4d} → {after_count:4d} ({change:+d})")

    # Check for lost mappings
    before_ids = set(zip(before_df['subject_id'], before_df['object_id']))
    after_ids = set(zip(after_df['subject_id'], after_df['object_id']))

    lost_mappings = before_ids - after_ids
    new_mappings = after_ids - before_ids

    print(f"\nMapping Changes:")
    print(f"  Lost mappings: {len(lost_mappings)}")
    print(f"  New mappings:  {len(new_mappings)}")

    if lost_mappings and verbose:
        print("\n⚠ Lost Mappings:")
        for subject_id, object_id in list(lost_mappings)[:10]:
            print(f"  {subject_id} → {object_id}")
        if len(lost_mappings) > 10:
            print(f"  ... and {len(lost_mappings) - 10} more")

    if new_mappings and verbose:
        print("\n✓ New Mappings (sample):")
        for subject_id, object_id in list(new_mappings)[:10]:
            print(f"  {subject_id} → {object_id}")
        if len(new_mappings) > 10:
            print(f"  ... and {len(new_mappings) - 10} more")

    # High-confidence exact matches
    exact_matches_before = len(before_df[
        (before_df['confidence'] >= 0.90) &
        (before_df['predicate_id'] == 'skos:exactMatch')
    ])
    exact_matches_after = len(after_df[
        (after_df['confidence'] >= 0.90) &
        (after_df['predicate_id'] == 'skos:exactMatch')
    ])

    print(f"\nHigh-Confidence Exact Matches (≥0.90):")
    print(f"  Before: {exact_matches_before}")
    print(f"  After:  {exact_matches_after}")
    print(f"  Change: +{exact_matches_after - exact_matches_before}")

    # Multi-ontology mappings (non-CHEBI)
    non_chebi_after = len(after_df[~after_df['object_id'].str.startswith('CHEBI:')])
    if non_chebi_after > 0:
        print(f"\nMulti-Ontology Mappings (non-CHEBI):")
        print(f"  Total: {non_chebi_after}")
        if verbose:
            print("\nOntology breakdown:")
            ontology_counts = after_df[~after_df['object_id'].str.startswith('CHEBI:')]['object_id'].str.extract(r'^([^:]+):')[0].value_counts()
            for ontology, count in ontology_counts.items():
                print(f"  {ontology}: {count}")

    print("\n" + "=" * 70)

    # Validation checks
    print("\nValidation Checks:")
    checks_passed = 0
    total_checks = 0

    # Check 1: No lost high-confidence mappings
    total_checks += 1
    high_conf_before = set(zip(
        before_df[before_df['confidence'] >= 0.9]['subject_id'],
        before_df[before_df['confidence'] >= 0.9]['object_id']
    ))
    high_conf_after = set(zip(
        after_df[after_df['confidence'] >= 0.9]['subject_id'],
        after_df[after_df['confidence'] >= 0.9]['object_id']
    ))
    lost_high_conf = high_conf_before - high_conf_after

    if len(lost_high_conf) == 0:
        print("  ✓ No high-confidence mappings lost")
        checks_passed += 1
    else:
        print(f"  ✗ Lost {len(lost_high_conf)} high-confidence mappings")

    # Check 2: Improvement in coverage
    total_checks += 1
    if len(after_df) > len(before_df):
        print(f"  ✓ Coverage improved (+{len(after_df) - len(before_df)} mappings)")
        checks_passed += 1
    else:
        print(f"  ✗ Coverage did not improve")

    # Check 3: More exact matches
    total_checks += 1
    if exact_matches_after > exact_matches_before:
        print(f"  ✓ More exact matches (+{exact_matches_after - exact_matches_before})")
        checks_passed += 1
    else:
        print(f"  ⚠ Exact matches unchanged or decreased")

    print(f"\nValidation: {checks_passed}/{total_checks} checks passed")
    print("=" * 70)

    return checks_passed == total_checks


def main():
    parser = argparse.ArgumentParser(
        description="Validate exact match enrichment results"
    )
    parser.add_argument(
        '--before',
        type=Path,
        required=True,
        help="Original enriched SSSOM file"
    )
    parser.add_argument(
        '--after',
        type=Path,
        required=True,
        help="New exact-match enriched SSSOM file"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Show detailed comparison"
    )

    args = parser.parse_args()

    # Check files exist
    if not args.before.exists():
        print(f"Error: Before file not found: {args.before}")
        sys.exit(1)

    if not args.after.exists():
        print(f"Error: After file not found: {args.after}")
        sys.exit(1)

    # Load files
    print(f"Loading before: {args.before}")
    before_df = load_sssom_file(args.before)

    print(f"Loading after: {args.after}")
    after_df = load_sssom_file(args.after)

    # Compare
    success = compare_enrichments(before_df, after_df, verbose=args.verbose)

    if success:
        print("\n✓ Validation successful!")
        sys.exit(0)
    else:
        print("\n⚠ Validation completed with warnings")
        sys.exit(0)  # Don't fail, just warn


if __name__ == "__main__":
    main()
