#!/usr/bin/env python3
"""
Extract Unique Ingredients from CultureMech YAML Files

Scans all YAML recipe files and extracts a comprehensive, non-redundant list
of ingredient names with frequency and provenance tracking.

Usage:
    uv run python scripts/extract_unique_ingredients.py [options]
"""

import argparse
import sys
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, Set

import pandas as pd


def extract_source_from_path(yaml_file: Path) -> str:
    """
    Extract data source from file path.

    Examples:
        KOMODO_1-10037_... -> KOMODO
        JCM_J530_... -> JCM
        DSMZ_44_... -> DSMZ
        TOGO_M3236_... -> TOGO
        CCAP_C10_... -> CCAP
    """
    filename = yaml_file.stem

    # Common source prefixes
    sources = ['KOMODO', 'JCM', 'DSMZ', 'TOGO', 'CCAP', 'SAG', 'UTEX',
               'ATCC', 'NCIT', 'BACDIVE', 'MediaDive']

    for source in sources:
        if filename.startswith(source):
            return source

    # Check parent directory for category
    category = yaml_file.parent.name
    if category in ['algae', 'bacterial', 'fungal', 'archaea', 'specialized']:
        return category.upper()

    return 'UNKNOWN'


def extract_ingredients_from_recipe(recipe: Dict) -> Set[str]:
    """
    Extract all ingredient names from a recipe.

    Args:
        recipe: Parsed YAML recipe dictionary

    Returns:
        Set of ingredient preferred_term values
    """
    ingredients = set()

    # Direct ingredients
    for ing in recipe.get('ingredients', []):
        preferred_term = ing.get('preferred_term', '').strip()
        if preferred_term:
            ingredients.add(preferred_term)

    # Solution compositions
    for solution in recipe.get('solutions', []):
        for ing in solution.get('composition', []):
            preferred_term = ing.get('preferred_term', '').strip()
            if preferred_term:
                ingredients.add(preferred_term)

    return ingredients


def extract_unique_ingredients(
    data_dirs: list[Path],
    verbose: bool = False
) -> pd.DataFrame:
    """
    Extract all unique ingredient names from YAML files.

    Args:
        data_dirs: List of directories to scan (raw_yaml, normalized_yaml)
        verbose: Show progress messages

    Returns:
        DataFrame with columns: ingredient_name, frequency, has_chebi_mapping,
                                chebi_id, sources
    """
    ingredient_stats = defaultdict(lambda: {
        'frequency': 0,
        'sources': set(),
        'chebi_id': None,
        'has_chebi_mapping': False
    })

    total_files = 0
    processed_files = 0

    # Count total files first
    for data_dir in data_dirs:
        total_files += sum(1 for _ in data_dir.rglob('*.yaml'))

    if verbose:
        print(f"\nScanning {total_files} YAML files across {len(data_dirs)} directories...")
        print("=" * 70)

    # Process all YAML files
    for data_dir in data_dirs:
        for yaml_file in data_dir.rglob('*.yaml'):
            try:
                # Load recipe
                with open(yaml_file) as f:
                    recipe = yaml.safe_load(f)

                if not recipe:
                    continue

                # Extract source
                source = extract_source_from_path(yaml_file)

                # Extract ingredients
                ingredients = extract_ingredients_from_recipe(recipe)

                # Update stats for each ingredient
                for ing_name in ingredients:
                    ingredient_stats[ing_name]['frequency'] += 1
                    ingredient_stats[ing_name]['sources'].add(source)

                    # Check for CHEBI mapping in normalized_yaml files
                    if 'normalized_yaml' in str(yaml_file):
                        # Find this ingredient in the recipe to check for term
                        for ing in recipe.get('ingredients', []) + \
                                   [i for s in recipe.get('solutions', [])
                                    for i in s.get('composition', [])]:
                            if ing.get('preferred_term', '').strip() == ing_name:
                                term = ing.get('term', {})
                                if term and term.get('id'):
                                    ingredient_stats[ing_name]['chebi_id'] = term['id']
                                    ingredient_stats[ing_name]['has_chebi_mapping'] = True
                                    break

                processed_files += 1

                if verbose and processed_files % 1000 == 0:
                    print(f"Progress: {processed_files}/{total_files} "
                          f"({processed_files/total_files*100:.1f}%) - "
                          f"Found {len(ingredient_stats)} unique ingredients")

            except Exception as e:
                if verbose:
                    print(f"Error processing {yaml_file}: {e}")
                continue

    if verbose:
        print(f"\nCompleted: {processed_files} files processed")
        print(f"Found {len(ingredient_stats)} unique ingredients")

    # Convert to DataFrame
    df = pd.DataFrame([
        {
            'ingredient_name': name,
            'frequency': stats['frequency'],
            'has_chebi_mapping': stats['has_chebi_mapping'],
            'chebi_id': stats['chebi_id'] or '',
            'sources': '|'.join(sorted(stats['sources']))
        }
        for name, stats in ingredient_stats.items()
    ]).sort_values('frequency', ascending=False).reset_index(drop=True)

    return df


def main():
    parser = argparse.ArgumentParser(
        description="Extract unique ingredients from CultureMech YAML files"
    )
    parser.add_argument(
        '--normalized-yaml',
        type=Path,
        default=Path('data/normalized_yaml'),
        help="Path to normalized_yaml directory"
    )
    parser.add_argument(
        '--raw-yaml',
        type=Path,
        help="Path to raw_yaml directory (optional)"
    )
    parser.add_argument(
        '--include-raw',
        action='store_true',
        help="Include raw_yaml directory in scan"
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('output/ingredients_unique.tsv'),
        help="Output TSV file path"
    )
    parser.add_argument(
        '--min-frequency',
        type=int,
        default=1,
        help="Minimum recipe frequency to include"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Show progress messages"
    )

    args = parser.parse_args()

    # Prepare data directories
    data_dirs = []

    if args.normalized_yaml.exists():
        data_dirs.append(args.normalized_yaml)
    else:
        print(f"Error: normalized_yaml directory not found: {args.normalized_yaml}")
        sys.exit(1)

    if args.include_raw:
        raw_yaml = args.raw_yaml or Path('data/raw_yaml')
        if raw_yaml.exists():
            data_dirs.append(raw_yaml)
        else:
            print(f"Warning: raw_yaml directory not found: {raw_yaml}")

    print("=" * 70)
    print("CultureMech Unique Ingredient Extractor")
    print("=" * 70)
    print(f"Scanning directories:")
    for d in data_dirs:
        print(f"  - {d}")
    print(f"Output: {args.output}")
    print(f"Min frequency: {args.min_frequency}")
    print()

    # Extract ingredients
    df = extract_unique_ingredients(data_dirs, verbose=args.verbose)

    # Filter by minimum frequency
    if args.min_frequency > 1:
        original_count = len(df)
        df = df[df['frequency'] >= args.min_frequency]
        filtered_count = original_count - len(df)
        if args.verbose:
            print(f"\nFiltered out {filtered_count} ingredients with frequency < {args.min_frequency}")

    # Create output directory
    args.output.parent.mkdir(parents=True, exist_ok=True)

    # Save to TSV
    df.to_csv(args.output, sep='\t', index=False)

    # Print summary
    print("\n" + "=" * 70)
    print("Extraction Summary")
    print("=" * 70)
    print(f"Total unique ingredients: {len(df)}")
    print(f"With CHEBI mapping: {df['has_chebi_mapping'].sum()} "
          f"({df['has_chebi_mapping'].sum()/len(df)*100:.1f}%)")
    print(f"Without CHEBI mapping: {(~df['has_chebi_mapping']).sum()} "
          f"({(~df['has_chebi_mapping']).sum()/len(df)*100:.1f}%)")
    print()
    print("Frequency distribution:")
    print(f"  1-5 recipes:    {len(df[df['frequency'] <= 5])}")
    print(f"  6-10 recipes:   {len(df[(df['frequency'] > 5) & (df['frequency'] <= 10)])}")
    print(f"  11-50 recipes:  {len(df[(df['frequency'] > 10) & (df['frequency'] <= 50)])}")
    print(f"  51-100 recipes: {len(df[(df['frequency'] > 50) & (df['frequency'] <= 100)])}")
    print(f"  >100 recipes:   {len(df[df['frequency'] > 100])}")
    print()
    print("Top 10 most frequent ingredients:")
    for _, row in df.head(10).iterrows():
        chebi = f" ({row['chebi_id']})" if row['chebi_id'] else " [NO CHEBI]"
        print(f"  {row['ingredient_name']:40s} {row['frequency']:5d}{chebi}")
    print()
    print(f"Output saved to: {args.output}")
    print("=" * 70)


if __name__ == "__main__":
    main()
