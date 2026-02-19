#!/usr/bin/env python3
"""
Extract Unmapped Ingredients to SSSOM

Creates a new SSSOM file containing only unmapped ingredients after enrichment.
Useful for tracking curation progress and identifying remaining gaps.

Usage:
    uv run python scripts/extract_unmapped_sssom.py \\
        --enriched-sssom output/culturemech_chebi_mappings_exact.sssom.tsv \\
        --ingredients output/ingredients_unique.tsv \\
        --output output/unmapped_ingredients.sssom.tsv
"""

import argparse
import sys
import re
from pathlib import Path
from datetime import datetime, timezone
from typing import Set

import pandas as pd


def load_sssom_file(sssom_path: Path) -> pd.DataFrame:
    """Load SSSOM TSV file, skipping metadata header."""
    with open(sssom_path) as f:
        for i, line in enumerate(f):
            if not line.startswith('#'):
                skip_rows = i
                break
        else:
            raise ValueError("No data found in SSSOM file (all lines are comments)")

    return pd.read_csv(sssom_path, sep='\t', skiprows=skip_rows)


def extract_sssom_metadata(sssom_path: Path) -> str:
    """Extract metadata header from SSSOM file."""
    metadata_lines = []

    with open(sssom_path) as f:
        for line in f:
            if line.startswith('#'):
                metadata_lines.append(line.rstrip())
            else:
                break

    return '\n'.join(metadata_lines)


def get_mapped_ingredients(sssom_df: pd.DataFrame) -> Set[str]:
    """
    Get set of ingredient names that have mappings.

    Args:
        sssom_df: SSSOM DataFrame

    Returns:
        Set of mapped ingredient names (subject_label values)
    """
    # Filter out unmapped entries (if any exist in the SSSOM)
    # Consider mapped if:
    # - predicate_id is not 'semapv:Unmapped' AND not empty/NaN
    # - confidence is greater than 0.0
    # - object_id is not empty (has an actual mapping target)

    mapped = sssom_df[
        (sssom_df['predicate_id'].notna()) &
        (sssom_df['predicate_id'] != '') &
        (sssom_df['predicate_id'] != 'semapv:Unmapped') &
        (sssom_df['confidence'] > 0.0) &
        (sssom_df['object_id'].notna()) &
        (sssom_df['object_id'] != '')
    ]

    return set(mapped['subject_label'].unique())


def create_unmapped_entry(ingredient_name: str, occurrence_count: int = 0) -> dict:
    """
    Create an unmapped SSSOM entry for an ingredient.

    Args:
        ingredient_name: Ingredient name
        occurrence_count: Number of times ingredient appears in recipes

    Returns:
        SSSOM mapping dictionary
    """
    # Create CURIE for subject
    subject_id = re.sub(r'[^\w\-]', '_', ingredient_name)
    subject_id = re.sub(r'_+', '_', subject_id).strip('_')
    subject_id = f"culturemech:{subject_id}"

    return {
        'subject_id': subject_id,
        'subject_label': ingredient_name,
        'predicate_id': 'semapv:Unmapped',
        'object_id': '',
        'object_label': '',
        'mapping_justification': '',
        'confidence': 0.0,
        'mapping_tool': '',
        'mapping_date': datetime.now(timezone.utc).isoformat(),
        'comment': f"Unmapped ingredient (occurs {occurrence_count} times in recipes)" if occurrence_count > 0 else "Unmapped ingredient"
    }


def main():
    parser = argparse.ArgumentParser(
        description="Extract unmapped ingredients to SSSOM file"
    )
    parser.add_argument(
        '--enriched-sssom',
        type=Path,
        required=True,
        help="Input enriched SSSOM file (with exact matches)"
    )
    parser.add_argument(
        '--ingredients',
        type=Path,
        required=True,
        help="Input ingredients_unique.tsv file"
    )
    parser.add_argument(
        '--output',
        type=Path,
        required=True,
        help="Output SSSOM file with only unmapped ingredients"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Show progress messages"
    )

    args = parser.parse_args()

    # Check input files exist
    if not args.enriched_sssom.exists():
        print(f"Error: Enriched SSSOM file not found: {args.enriched_sssom}")
        sys.exit(1)

    if not args.ingredients.exists():
        print(f"Error: Ingredients file not found: {args.ingredients}")
        sys.exit(1)

    print("=" * 70)
    print("Extract Unmapped Ingredients to SSSOM")
    print("=" * 70)
    print(f"Enriched SSSOM: {args.enriched_sssom}")
    print(f"Ingredients:    {args.ingredients}")
    print(f"Output:         {args.output}")
    print()

    # Load enriched SSSOM file
    if args.verbose:
        print("Loading enriched SSSOM file...")

    sssom_df = load_sssom_file(args.enriched_sssom)
    metadata_header = extract_sssom_metadata(args.enriched_sssom)

    if args.verbose:
        print(f"Loaded {len(sssom_df)} mappings")

    # Get mapped ingredients
    mapped_ingredients = get_mapped_ingredients(sssom_df)

    if args.verbose:
        print(f"Found {len(mapped_ingredients)} mapped ingredients")

    # Load all ingredients
    if args.verbose:
        print(f"\nLoading ingredients list...")

    ingredients_df = pd.read_csv(args.ingredients, sep='\t')

    if args.verbose:
        print(f"Loaded {len(ingredients_df)} unique ingredients")

    # Find unmapped ingredients
    unmapped_ingredients = ingredients_df[
        ~ingredients_df['ingredient_name'].isin(mapped_ingredients)
    ]

    if args.verbose:
        print(f"\nIdentified {len(unmapped_ingredients)} unmapped ingredients")

    # Create unmapped entries
    unmapped_entries = []
    for _, row in unmapped_ingredients.iterrows():
        entry = create_unmapped_entry(
            row['ingredient_name'],
            row.get('occurrence_count', 0)
        )
        unmapped_entries.append(entry)

    # Create DataFrame
    unmapped_df = pd.DataFrame(unmapped_entries)

    # Sort by occurrence count (descending) if available
    if 'comment' in unmapped_df.columns:
        # Extract occurrence count from comment
        unmapped_df['_sort_key'] = unmapped_df['comment'].str.extract(r'occurs (\d+) times')[0].fillna(0).astype(int)
        unmapped_df = unmapped_df.sort_values('_sort_key', ascending=False)
        unmapped_df = unmapped_df.drop('_sort_key', axis=1)

    # Update metadata header
    updated_metadata = metadata_header.replace(
        'CultureMech CHEBI Mappings',
        'CultureMech Unmapped Ingredients'
    )
    updated_metadata += f"\n# Extracted: {datetime.now(timezone.utc).isoformat()}"
    updated_metadata += f"\n# Total unmapped: {len(unmapped_df)}"

    # Save output
    if args.verbose:
        print(f"\nSaving unmapped SSSOM file: {args.output}")

    args.output.parent.mkdir(parents=True, exist_ok=True)

    with open(args.output, 'w') as f:
        f.write(updated_metadata)
        f.write('\n')
        unmapped_df.to_csv(f, sep='\t', index=False)

    # Print summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total ingredients:     {len(ingredients_df)}")
    print(f"Mapped ingredients:    {len(mapped_ingredients)}")
    print(f"Unmapped ingredients:  {len(unmapped_df)}")
    print(f"Coverage:              {len(mapped_ingredients)/len(ingredients_df)*100:.1f}%")

    # Show top unmapped by frequency
    if len(unmapped_df) > 0:
        print("\nTop 20 unmapped ingredients (by frequency):")
        print("-" * 70)
        for _, row in unmapped_df.head(20).iterrows():
            print(f"  {row['subject_label']}")

    print()
    print(f"Output saved to: {args.output}")
    print("=" * 70)


if __name__ == "__main__":
    main()
