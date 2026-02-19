#!/usr/bin/env python3
"""
Extract Truly Unmapped Ingredients

Uses subject_id matching (not exact label matching) to identify ingredients
that don't have any mapping in the SSSOM file.
"""

import pandas as pd
import re
from pathlib import Path


def create_subject_id(name):
    """Create subject_id from ingredient name."""
    subject_id = re.sub(r'[^\w\-]', '_', str(name))
    subject_id = re.sub(r'_+', '_', subject_id).strip('_')
    return f"culturemech:{subject_id}"


def main():
    print("=" * 70)
    print("Extract Truly Unmapped Ingredients (by subject_id)")
    print("=" * 70)
    print()

    # Load SSSOM
    print("Loading SSSOM file...")
    df_sssom = pd.read_csv('output/culturemech_chebi_mappings_final.sssom.tsv',
                           sep='\t', comment='#')
    sssom_ids = set(df_sssom['subject_id'])
    print(f"  Loaded {len(df_sssom)} SSSOM entries")
    print(f"  Unique subject_ids: {len(sssom_ids)}")
    print()

    # Load ingredients
    print("Loading ingredients list...")
    df_ing = pd.read_csv('output/ingredients_unique.tsv', sep='\t')
    # Rename columns for consistency
    df_ing = df_ing.rename(columns={
        'ingredient_name': 'ingredient',
        'frequency': 'count',
        'has_chebi_mapping': 'mapped',
        'chebi_id': 'collection'
    })
    print(f"  Loaded {len(df_ing)} ingredients")
    print()

    # Create subject_ids and check mappings
    print("Matching by subject_id...")
    df_ing['subject_id'] = df_ing['ingredient'].apply(create_subject_id)
    df_ing['has_mapping'] = df_ing['subject_id'].isin(sssom_ids)

    mapped = df_ing[df_ing['has_mapping']]
    unmapped = df_ing[~df_ing['has_mapping']].sort_values('count', ascending=False)

    print(f"  Mapped ingredients: {len(mapped)}")
    print(f"  Unmapped ingredients: {len(unmapped)}")
    print(f"  Coverage: {len(mapped)/len(df_ing)*100:.1f}%")
    print()

    # Save unmapped
    output_file = Path('output/truly_unmapped_ingredients.tsv')
    unmapped[['ingredient', 'count', 'sources']].to_csv(output_file, sep='\t', index=False)
    print(f"Saved to: {output_file}")
    print()

    # Show top 20
    print("=" * 70)
    print(f"Top 20 Unmapped Ingredients (by recipe frequency)")
    print("=" * 70)
    for i, (_, row) in enumerate(unmapped.head(20).iterrows(), 1):
        count_val = row['count']
        # Handle both numeric and string values
        if isinstance(count_val, str):
            count_str = count_val
        else:
            count_str = f"{int(count_val):4d}"
        print(f"{i:2d}. {row['ingredient']:50s} ({count_str} recipes)")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()
