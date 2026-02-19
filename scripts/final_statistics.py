#!/usr/bin/env python3
"""
Final SSSOM Mapping Statistics

Shows comprehensive statistics for the final enriched SSSOM file.
"""

import pandas as pd
from pathlib import Path


def main():
    # Load SSSOM file
    df = pd.read_csv('output/culturemech_chebi_mappings_final.sssom.tsv',
                     sep='\t', comment='#')
    mapped = df[df['confidence'] > 0]

    # Load ingredients to calculate true coverage
    df_ing = pd.read_csv('output/ingredients_unique.tsv', sep='\t')
    total_ingredients = len(df_ing)
    sssom_subject_ids = set(df['subject_id'])

    # Calculate true coverage by subject_id matching
    def create_subject_id(name):
        import re
        subject_id = re.sub(r'[^\w\-]', '_', str(name))
        subject_id = re.sub(r'_+', '_', subject_id).strip('_')
        return f"culturemech:{subject_id}"

    df_ing['subject_id'] = df_ing['ingredient_name'].apply(create_subject_id)
    mapped_ingredients = df_ing['subject_id'].isin(sssom_subject_ids).sum()
    coverage_pct = mapped_ingredients / total_ingredients * 100

    print("=" * 70)
    print("Final SSSOM Mapping Statistics")
    print("=" * 70)
    print(f"Total entries: {len(df)}")
    print(f"Mapped entries (confidence > 0): {len(mapped)}")
    print(f"Unique subject_ids: {df['subject_id'].nunique()}")
    print()

    print("Mapping method breakdown:")
    for method, count in mapped['mapping_method'].value_counts().items():
        pct = count / len(mapped) * 100
        print(f"  {method:30s}: {count:4d} ({pct:5.1f}%)")
    print()

    print("Confidence distribution:")
    bins = [0, 0.5, 0.8, 0.9, 1.0]
    for label, group in mapped.groupby(pd.cut(mapped['confidence'], bins=bins)):
        print(f"  {label}: {len(group)}")
    print()

    print("Top ontologies:")
    ontology_counts = {}
    for obj_id in mapped['object_id']:
        if pd.notna(obj_id) and ':' in str(obj_id):
            ontology = str(obj_id).split(':')[0]
            ontology_counts[ontology] = ontology_counts.get(ontology, 0) + 1

    for ontology, count in sorted(ontology_counts.items(), key=lambda x: -x[1])[:5]:
        pct = count / len(mapped) * 100
        print(f"  {ontology:15s}: {count:4d} ({pct:5.1f}%)")
    print()

    print(f"True coverage (by subject_id matching): {coverage_pct:.1f}% ({mapped_ingredients} / {total_ingredients})")
    print("=" * 70)


if __name__ == "__main__":
    main()
