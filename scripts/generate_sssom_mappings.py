#!/usr/bin/env python3
"""
Generate SSSOM Mapping File from CultureMech Normalized YAML

Creates SSSOM-compliant TSV file from existing CHEBI term assignments
in normalized_yaml recipes. Can optionally include unmapped ingredients
as candidates for future curation.

SSSOM Specification: https://mapping-commons.github.io/sssom/

Usage:
    uv run python scripts/generate_sssom_mappings.py [options]
"""

import argparse
import sys
import yaml
import re
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, Set
from collections import Counter

import pandas as pd


def create_curie(ingredient_name: str) -> str:
    """
    Create a valid CURIE from ingredient name.

    Args:
        ingredient_name: Human-readable ingredient name

    Returns:
        CURIE like "culturemech:Distilled_water"
    """
    # Replace spaces and special characters with underscores
    safe_name = re.sub(r'[^\w\-]', '_', ingredient_name)
    # Remove consecutive underscores
    safe_name = re.sub(r'_+', '_', safe_name)
    # Remove leading/trailing underscores
    safe_name = safe_name.strip('_')

    return f"culturemech:{safe_name}"


def extract_mapping_tool(curation_history: list) -> str:
    """
    Extract mapping tool from curation history.

    Args:
        curation_history: List of curation events

    Returns:
        Mapping tool identifier (e.g., "MicrobeMediaParam|v1.0")
    """
    for event in curation_history:
        if 'chebi' in event.get('curator', '').lower():
            notes = event.get('notes', '')
            if 'MicrobeMediaParam' in notes:
                return 'MicrobeMediaParam|v1.0'
            elif 'MediaDive' in notes:
                return 'MediaDive|v1.0'

    return 'CultureMech|manual'


def generate_sssom_mappings(
    normalized_dir: Path,
    confidence_threshold: float = 0.0,
    include_unmapped: bool = False,
    verbose: bool = False
) -> pd.DataFrame:
    """
    Generate SSSOM mapping DataFrame from normalized YAML files.

    Args:
        normalized_dir: Path to normalized_yaml directory
        confidence_threshold: Minimum confidence score
        include_unmapped: Include unmapped ingredients (for future curation)
        verbose: Show progress messages

    Returns:
        DataFrame with SSSOM columns
    """
    mappings = []
    unmapped_candidates = {}  # Track unmapped ingredients
    seen_pairs = set()  # Track (subject_id, object_id) to avoid duplicates

    total_files = sum(1 for _ in normalized_dir.rglob('*.yaml'))
    processed_files = 0

    if verbose:
        print(f"\nProcessing {total_files} YAML files...")
        if include_unmapped:
            print("Including unmapped ingredients as future mapping candidates")
        print("=" * 70)

    for yaml_file in normalized_dir.rglob('*.yaml'):
        try:
            # Load recipe
            with open(yaml_file) as f:
                recipe = yaml.safe_load(f)

            if not recipe:
                continue

            # Extract mapping tool from curation history
            mapping_tool = extract_mapping_tool(recipe.get('curation_history', []))

            # Process direct ingredients
            for ingredient in recipe.get('ingredients', []):
                preferred_term = ingredient.get('preferred_term', '').strip()
                if not preferred_term:
                    continue

                term = ingredient.get('term', {})

                if term and term.get('id'):
                    # Has mapping - create normal SSSOM entry
                    subject_id = create_curie(preferred_term)
                    object_id = term['id']

                    # Skip duplicates
                    pair_key = (subject_id, object_id)
                    if pair_key in seen_pairs:
                        continue
                    seen_pairs.add(pair_key)

                    # Determine confidence based on source
                    confidence = 0.95  # High confidence for curated sources

                    if confidence < confidence_threshold:
                        continue

                    mappings.append({
                        'subject_id': subject_id,
                        'subject_label': preferred_term,
                        'predicate_id': 'skos:exactMatch',
                        'object_id': object_id,
                        'object_label': term.get('label', ''),
                        'mapping_justification': 'semapv:ManualMappingCuration',
                        'confidence': confidence,
                        'mapping_tool': mapping_tool,
                        'mapping_date': datetime.now(timezone.utc).isoformat(),
                        'comment': 'Curated from MicrobeMediaParam and MediaDive chemical mappings'
                    })
                else:
                    # No mapping - track for unmapped list
                    if include_unmapped:
                        subject_id = create_curie(preferred_term)
                        if subject_id not in unmapped_candidates:
                            unmapped_candidates[subject_id] = {
                                'label': preferred_term,
                                'count': 0
                            }
                        unmapped_candidates[subject_id]['count'] += 1

            # Process solution compositions
            for solution in recipe.get('solutions', []):
                for ingredient in solution.get('composition', []):
                    preferred_term = ingredient.get('preferred_term', '').strip()
                    if not preferred_term:
                        continue

                    term = ingredient.get('term', {})

                    if term and term.get('id'):
                        # Has mapping
                        subject_id = create_curie(preferred_term)
                        object_id = term['id']

                        pair_key = (subject_id, object_id)
                        if pair_key in seen_pairs:
                            continue
                        seen_pairs.add(pair_key)

                        confidence = 0.95

                        if confidence < confidence_threshold:
                            continue

                        mappings.append({
                            'subject_id': subject_id,
                            'subject_label': preferred_term,
                            'predicate_id': 'skos:exactMatch',
                            'object_id': object_id,
                            'object_label': term.get('label', ''),
                            'mapping_justification': 'semapv:ManualMappingCuration',
                            'confidence': confidence,
                            'mapping_tool': mapping_tool,
                            'mapping_date': datetime.now(timezone.utc).isoformat(),
                            'comment': 'Curated from MicrobeMediaParam and MediaDive chemical mappings'
                        })
                    else:
                        # No mapping - track for unmapped list
                        if include_unmapped:
                            subject_id = create_curie(preferred_term)
                            if subject_id not in unmapped_candidates:
                                unmapped_candidates[subject_id] = {
                                    'label': preferred_term,
                                    'count': 0
                                }
                            unmapped_candidates[subject_id]['count'] += 1

            processed_files += 1

            if verbose and processed_files % 1000 == 0:
                print(f"Progress: {processed_files}/{total_files} "
                      f"({processed_files/total_files*100:.1f}%) - "
                      f"Found {len(mappings)} mappings, {len(unmapped_candidates)} unmapped")

        except Exception as e:
            if verbose:
                print(f"Error processing {yaml_file}: {e}")
            continue

    # Add unmapped candidates if requested
    if include_unmapped and unmapped_candidates:
        for subject_id, info in unmapped_candidates.items():
            mappings.append({
                'subject_id': subject_id,
                'subject_label': info['label'],
                'predicate_id': 'semapv:Unmapped',
                'object_id': '',  # Empty - no mapping exists
                'object_label': '',
                'mapping_justification': 'semapv:Unreviewed',
                'confidence': 0.0,  # No mapping
                'mapping_tool': 'CultureMech|unmapped_detection',
                'mapping_date': datetime.now(timezone.utc).isoformat(),
                'comment': f'Unmapped ingredient (appears in {info["count"]} recipes) - candidate for future curation'
            })

    if verbose:
        print(f"\nCompleted: {processed_files} files processed")
        print(f"Generated {len(mappings)} total entries:")
        mapped_count = sum(1 for m in mappings if m.get('confidence', 0) > 0)
        unmapped_count = len(mappings) - mapped_count
        print(f"  - Mapped: {mapped_count}")
        print(f"  - Unmapped candidates: {unmapped_count}")

    return pd.DataFrame(mappings)


def generate_sssom_metadata(include_unmapped: bool = False) -> str:
    """
    Generate SSSOM metadata header in YAML format.

    Args:
        include_unmapped: Whether unmapped ingredients are included

    Returns:
        YAML metadata header as string
    """
    description = (
        'Mappings between CultureMech culture media ingredients and '
        'CHEBI chemical entity ontology terms'
    )
    if include_unmapped:
        description += '. Includes unmapped ingredients (confidence=0.0) as candidates for future curation.'

    metadata = {
        'curie_map': {
            'CHEBI': 'http://purl.obolibrary.org/obo/CHEBI_',
            'culturemech': 'https://w3id.org/culturemech/ingredient/',
            'skos': 'http://www.w3.org/2004/02/skos/core#',
            'semapv': 'https://w3id.org/semapv/vocab/'
        },
        'mapping_set_id': 'https://w3id.org/culturemech/mappings/chebi/v1.0',
        'mapping_set_title': 'CultureMech to CHEBI Ingredient Mappings',
        'mapping_set_description': description,
        'license': 'https://creativecommons.org/publicdomain/zero/1.0/',
        'mapping_provider': 'https://github.com/KG-Hub/KG-Microbe/CultureMech',
        'mapping_date': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
        'comment': 'Predicates: skos:exactMatch (mapped), semapv:Unmapped (no mapping found). Justifications: semapv:ManualMappingCuration (curated), semapv:Unreviewed (not yet reviewed).'
    }

    # Convert to YAML with comment markers
    yaml_str = yaml.dump(metadata, default_flow_style=False, sort_keys=False)
    # Add comment markers to each line
    commented = '\n'.join(f"# {line}" for line in yaml_str.split('\n'))

    return commented


def save_sssom_file(df: pd.DataFrame, output_path: Path, include_unmapped: bool = False):
    """
    Save DataFrame as SSSOM-compliant TSV file with metadata header.

    Args:
        df: SSSOM DataFrame
        output_path: Output file path
        include_unmapped: Whether unmapped ingredients are included
    """
    # Generate metadata header
    metadata = generate_sssom_metadata(include_unmapped)

    # Create output directory
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Write file with metadata header
    with open(output_path, 'w') as f:
        # Write metadata
        f.write(metadata)
        f.write('\n')

        # Write TSV data
        df.to_csv(f, sep='\t', index=False)


def validate_sssom_format(df: pd.DataFrame) -> bool:
    """
    Validate SSSOM DataFrame has required columns.

    Args:
        df: DataFrame to validate

    Returns:
        True if valid, False otherwise
    """
    required_columns = [
        'subject_id',
        'predicate_id',
        'object_id',
        'mapping_justification'
    ]

    missing = set(required_columns) - set(df.columns)

    if missing:
        print(f"Error: Missing required SSSOM columns: {missing}")
        return False

    # Check for valid CURIEs in subject_id
    if not df['subject_id'].str.contains(':').all():
        print("Error: Not all subject_id values are valid CURIEs")
        return False

    # Check for valid CURIEs in object_id (allowing empty for unmapped)
    # Unmapped entries have predicate_id = 'semapv:Unmapped' and empty object_id
    mapped_entries = df[df['predicate_id'] != 'semapv:Unmapped']
    if len(mapped_entries) > 0:
        if not mapped_entries['object_id'].str.contains(':').all():
            print("Error: Not all mapped object_id values are valid CURIEs")
            return False

    # Verify unmapped entries have empty object_id
    unmapped_entries = df[df['predicate_id'] == 'semapv:Unmapped']
    if len(unmapped_entries) > 0:
        if not (unmapped_entries['object_id'] == '').all():
            print("Error: Unmapped entries should have empty object_id")
            return False

    return True


def main():
    parser = argparse.ArgumentParser(
        description="Generate SSSOM mapping file from normalized YAML"
    )
    parser.add_argument(
        '--normalized-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help="Path to normalized_yaml directory"
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('output/culturemech_chebi_mappings.sssom.tsv'),
        help="Output SSSOM file path"
    )
    parser.add_argument(
        '--confidence-threshold',
        type=float,
        default=0.0,
        help="Minimum confidence score (0.0-1.0)"
    )
    parser.add_argument(
        '--include-unmapped',
        action='store_true',
        help="Include unmapped ingredients as future mapping candidates"
    )
    parser.add_argument(
        '--validate',
        action='store_true',
        help="Validate SSSOM format after generation"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Show progress messages"
    )

    args = parser.parse_args()

    if not args.normalized_dir.exists():
        print(f"Error: normalized_yaml directory not found: {args.normalized_dir}")
        sys.exit(1)

    print("=" * 70)
    print("CultureMech SSSOM Mapping Generator")
    print("=" * 70)
    print(f"Input: {args.normalized_dir}")
    print(f"Output: {args.output}")
    print(f"Confidence threshold: {args.confidence_threshold}")
    print(f"Include unmapped: {args.include_unmapped}")
    print()

    # Generate mappings
    df = generate_sssom_mappings(
        args.normalized_dir,
        confidence_threshold=args.confidence_threshold,
        include_unmapped=args.include_unmapped,
        verbose=args.verbose
    )

    # Validate format
    if args.validate:
        if args.verbose:
            print("\nValidating SSSOM format...")

        if not validate_sssom_format(df):
            print("Error: SSSOM validation failed")
            sys.exit(1)

        if args.verbose:
            print("SSSOM format validation passed")

    # Save to file
    save_sssom_file(df, args.output, args.include_unmapped)

    # Print summary
    print("\n" + "=" * 70)
    print("SSSOM Generation Summary")
    print("=" * 70)
    print(f"Total entries: {len(df)}")
    print(f"Unique subjects: {df['subject_id'].nunique()}")

    # Count mapped vs unmapped
    mapped = df[df['confidence'] > 0.0]
    unmapped = df[df['confidence'] == 0.0]

    print(f"\nMapped ingredients: {len(mapped)}")
    print(f"  Unique subjects: {mapped['subject_id'].nunique()}")
    print(f"  Unique CHEBI terms: {mapped['object_id'].nunique()}")

    if len(unmapped) > 0:
        print(f"\nUnmapped ingredients (future candidates): {len(unmapped)}")
        print(f"  These can be prioritized for manual curation or OLS discovery")

    print("\nConfidence distribution:")
    for conf in sorted(df['confidence'].unique(), reverse=True):
        count = len(df[df['confidence'] == conf])
        print(f"  {conf:.2f}: {count} ({count/len(df)*100:.1f}%)")
    print()
    print("Mapping tool distribution:")
    for tool, count in df['mapping_tool'].value_counts().items():
        print(f"  {tool}: {count}")

    if len(unmapped) > 0:
        print("\n📊 Top 10 unmapped ingredients by frequency:")
        unmapped_sorted = unmapped.sort_values('comment', ascending=False)
        for _, row in unmapped_sorted.head(10).iterrows():
            # Extract frequency from comment
            freq = row['comment'].split('(appears in ')[1].split(' recipes)')[0]
            print(f"  {row['subject_label']:40s} - {freq} recipes")

    print()
    print(f"Output saved to: {args.output}")
    print("=" * 70)


if __name__ == "__main__":
    main()
