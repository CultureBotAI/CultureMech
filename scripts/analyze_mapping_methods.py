#!/usr/bin/env python3
"""
Analyze Mapping Methods in SSSOM File

Shows breakdown of mapping methods to distinguish:
- Curated dictionary mappings (BioProductDict)
- Ontology-based exact matches (OLS/OAK)
- Ontology-based fuzzy matches
- Manual curation

Usage:
    uv run python scripts/analyze_mapping_methods.py [sssom_file]
"""

import sys
import argparse
from pathlib import Path
import pandas as pd


def load_sssom_file(sssom_path: Path) -> pd.DataFrame:
    """Load SSSOM TSV file, skipping metadata header."""
    # Find where data starts (after metadata comments)
    with open(sssom_path) as f:
        for i, line in enumerate(f):
            if not line.startswith('#'):
                skip_rows = i
                break
        else:
            raise ValueError("No data found in SSSOM file (all lines are comments)")

    # Load TSV data
    df = pd.read_csv(sssom_path, sep='\t', skiprows=skip_rows)
    return df


def analyze_mapping_methods(df: pd.DataFrame):
    """Analyze and display mapping method breakdown."""
    print("=" * 70)
    print("Mapping Method Analysis")
    print("=" * 70)
    print()

    # Total mappings
    print(f"Total mappings: {len(df)}")
    print()

    # Check if mapping_method column exists
    if 'mapping_method' not in df.columns:
        print("⚠️  Warning: 'mapping_method' column not found in SSSOM file")
        print("   This column was added in the MicroMediaParam integration (2026-02-09)")
        print("   Please re-run enrichment to add this column.")
        print()

        # Show mapping_tool breakdown instead
        if 'mapping_tool' in df.columns:
            print("Mapping tool breakdown (legacy):")
            print("-" * 70)
            tool_counts = df['mapping_tool'].value_counts()
            for tool, count in tool_counts.items():
                pct = count / len(df) * 100
                print(f"  {tool:40s}: {count:5d} ({pct:5.1f}%)")
        return

    # Mapping method breakdown
    print("Mapping Method Breakdown:")
    print("-" * 70)

    method_counts = df['mapping_method'].value_counts()
    method_labels = {
        'curated_dictionary': 'Curated Dictionary (BioProductDict)',
        'ontology_exact': 'Ontology Exact Match (OLS/OAK)',
        'ontology_fuzzy': 'Ontology Fuzzy Match (OLS/OAK)',
        'manual_curation': 'Manual Curation (Original)'
    }

    # Display in order
    total_ontology = 0
    for method in ['curated_dictionary', 'ontology_exact', 'ontology_fuzzy', 'manual_curation']:
        count = method_counts.get(method, 0)
        if count > 0:
            label = method_labels.get(method, method)
            pct = count / len(df) * 100
            print(f"  {label:45s}: {count:5d} ({pct:5.1f}%)")

            if method in ['ontology_exact', 'ontology_fuzzy']:
                total_ontology += count

    print()
    print(f"Total ontology-based (OAK/OLS):          {total_ontology:5d} ({total_ontology/len(df)*100:5.1f}%)")
    print(f"Total non-ontology (curated + manual):   {len(df) - total_ontology:5d} ({(len(df) - total_ontology)/len(df)*100:5.1f}%)")
    print()

    # Detailed breakdown by mapping_tool for each method
    print("Detailed Breakdown by Tool:")
    print("-" * 70)

    for method in ['curated_dictionary', 'ontology_exact', 'ontology_fuzzy', 'manual_curation']:
        method_df = df[df['mapping_method'] == method]
        if len(method_df) > 0:
            label = method_labels.get(method, method)
            print(f"\n{label}:")
            if 'mapping_tool' in df.columns:
                tool_counts = method_df['mapping_tool'].value_counts()
                for tool, count in tool_counts.items():
                    pct = count / len(method_df) * 100
                    print(f"    {tool:40s}: {count:5d} ({pct:5.1f}%)")

    # Confidence distribution by method
    print()
    print("Confidence Distribution by Method:")
    print("-" * 70)

    for method in ['curated_dictionary', 'ontology_exact', 'ontology_fuzzy', 'manual_curation']:
        method_df = df[df['mapping_method'] == method]
        if len(method_df) > 0:
            label = method_labels.get(method, method)
            avg_conf = method_df['confidence'].mean()
            min_conf = method_df['confidence'].min()
            max_conf = method_df['confidence'].max()
            print(f"  {label:45s}: avg={avg_conf:.2f}, min={min_conf:.2f}, max={max_conf:.2f}")


def main():
    parser = argparse.ArgumentParser(
        description="Analyze mapping methods in SSSOM file"
    )
    parser.add_argument(
        'sssom_file',
        type=Path,
        nargs='?',
        default=Path('output/culturemech_chebi_mappings_exact.sssom.tsv'),
        help="SSSOM file to analyze (default: output/culturemech_chebi_mappings_exact.sssom.tsv)"
    )

    args = parser.parse_args()

    if not args.sssom_file.exists():
        print(f"Error: File not found: {args.sssom_file}")
        sys.exit(1)

    print(f"Analyzing: {args.sssom_file}")
    print()

    df = load_sssom_file(args.sssom_file)
    analyze_mapping_methods(df)

    print()
    print("=" * 70)


if __name__ == "__main__":
    main()
