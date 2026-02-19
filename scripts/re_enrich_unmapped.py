#!/usr/bin/env python3
"""
Re-enrich Previously Unmapped Entries

Takes low-confidence/unmapped entries from an SSSOM file and re-runs
them through the enrichment pipeline with MicroMediaParam normalization.

Usage:
    uv run python scripts/re_enrich_unmapped.py --verbose
"""

import argparse
import sys
from pathlib import Path
import pandas as pd

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
sys.path.insert(0, str(Path(__file__).parent))

from culturemech.ontology.ols_client import OLSClient
from culturemech.ontology.oak_client import OAKClient
from enrich_sssom_with_ols import (
    load_sssom_file,
    extract_sssom_metadata,
    save_sssom_file,
    lookup_biological_product,
    normalize_for_mapping,
    create_mapping,
)


def re_enrich_unmapped(
    sssom_path: Path,
    output_path: Path,
    ols_client: OLSClient,
    oak_client: OAKClient = None,
    confidence_threshold: float = 0.5,
    verbose: bool = False
):
    """Re-enrich unmapped/low-confidence entries."""

    # Load SSSOM file
    df = load_sssom_file(sssom_path)
    metadata = extract_sssom_metadata(sssom_path)

    if verbose:
        print(f"Loaded {len(df)} entries from {sssom_path}")

    # Find low-confidence entries
    low_conf = df[df['confidence'] < confidence_threshold]

    if verbose:
        print(f"Found {len(low_conf)} low-confidence entries (< {confidence_threshold})")
        print()

    # Re-process each low-confidence entry
    updated_count = 0
    stats = {
        'bio_product': 0,
        'oak_synonym': 0,
        'ols_exact': 0,
        'ols_fuzzy': 0,
        'still_unmapped': 0,
    }

    for idx, row in low_conf.iterrows():
        ingredient_name = row['subject_label']

        if verbose and (updated_count % 100 == 0):
            print(f"Progress: {updated_count}/{len(low_conf)} - Updated {updated_count}")

        # Stage 0: Bio product dictionary
        bio_id = lookup_biological_product(ingredient_name)
        if bio_id:
            df.at[idx, 'object_id'] = bio_id
            df.at[idx, 'object_label'] = ingredient_name
            df.at[idx, 'confidence'] = 0.98
            df.at[idx, 'mapping_method'] = 'curated_dictionary'
            df.at[idx, 'mapping_tool'] = 'BioProductDict'
            df.at[idx, 'predicate_id'] = 'skos:exactMatch'
            df.at[idx, 'comment'] = 'Re-enriched via BioProductDict'
            updated_count += 1
            stats['bio_product'] += 1
            continue

        # Normalize
        normalized = normalize_for_mapping(ingredient_name)

        # Stage 1: OAK synonym search
        if oak_client:
            try:
                oak_results = oak_client.synonym_search(normalized, 'chebi')
                if oak_results:
                    result = oak_results[0]
                    df.at[idx, 'object_id'] = result.curie
                    df.at[idx, 'object_label'] = result.label
                    df.at[idx, 'confidence'] = 0.92
                    df.at[idx, 'mapping_method'] = 'ontology_exact'
                    df.at[idx, 'mapping_tool'] = 'OAK|synonym'
                    df.at[idx, 'predicate_id'] = 'skos:exactMatch'
                    df.at[idx, 'comment'] = f'Re-enriched via OAK: {result.matched_term}'
                    updated_count += 1
                    stats['oak_synonym'] += 1
                    continue
            except Exception as e:
                if verbose:
                    print(f"  OAK error for '{ingredient_name}': {e}")

        # Stage 2: OLS exact
        try:
            exact_results = ols_client.search_chebi(normalized, exact=True)
            if exact_results and exact_results[0].get('score', 0) > 80:
                best = exact_results[0]
                df.at[idx, 'object_id'] = best['chebi_id']
                df.at[idx, 'object_label'] = best['label']
                df.at[idx, 'confidence'] = 0.95
                df.at[idx, 'mapping_method'] = 'ontology_exact'
                df.at[idx, 'mapping_tool'] = 'EBI_OLS_API|exact'
                df.at[idx, 'predicate_id'] = 'skos:exactMatch'
                df.at[idx, 'comment'] = 'Re-enriched via OLS exact'
                updated_count += 1
                stats['ols_exact'] += 1
                continue
        except Exception as e:
            if verbose:
                print(f"  OLS error for '{ingredient_name}': {e}")

        # Stage 3: OLS fuzzy
        try:
            fuzzy_results = ols_client.search_chebi(normalized, exact=False)
            if fuzzy_results and fuzzy_results[0].get('score', 0) > 50:
                best = fuzzy_results[0]
                conf = min(best.get('score', 50) / 100.0, 0.85)
                if conf >= 0.6:  # Only use if decent confidence
                    df.at[idx, 'object_id'] = best['chebi_id']
                    df.at[idx, 'object_label'] = best['label']
                    df.at[idx, 'confidence'] = conf
                    df.at[idx, 'mapping_method'] = 'ontology_fuzzy'
                    df.at[idx, 'mapping_tool'] = 'EBI_OLS_API|fuzzy'
                    df.at[idx, 'predicate_id'] = 'skos:closeMatch'
                    df.at[idx, 'comment'] = f'Re-enriched via OLS fuzzy (score: {best.get("score", 0):.1f})'
                    updated_count += 1
                    stats['ols_fuzzy'] += 1
                    continue
        except Exception as e:
            if verbose:
                print(f"  OLS fuzzy error for '{ingredient_name}': {e}")

        stats['still_unmapped'] += 1

    if verbose:
        print()
        print("Re-enrichment complete!")
        print(f"Updated: {updated_count}/{len(low_conf)}")
        print()
        print("Breakdown:")
        print(f"  Bio product dict:  {stats['bio_product']}")
        print(f"  OAK synonym:       {stats['oak_synonym']}")
        print(f"  OLS exact:         {stats['ols_exact']}")
        print(f"  OLS fuzzy:         {stats['ols_fuzzy']}")
        print(f"  Still unmapped:    {stats['still_unmapped']}")

    # Save
    save_sssom_file(df, output_path, metadata)

    if verbose:
        print()
        print(f"Saved to: {output_path}")

    return updated_count


def main():
    parser = argparse.ArgumentParser(
        description="Re-enrich previously unmapped SSSOM entries"
    )
    parser.add_argument(
        '--input',
        type=Path,
        default=Path('output/culturemech_chebi_mappings_exact.sssom.tsv'),
        help="Input SSSOM file"
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('output/culturemech_chebi_mappings_re_enriched.sssom.tsv'),
        help="Output SSSOM file"
    )
    parser.add_argument(
        '--confidence-threshold',
        type=float,
        default=0.5,
        help="Re-process entries below this confidence"
    )
    parser.add_argument(
        '--use-oak',
        action='store_true',
        default=True,
        help="Enable OAK for searching"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Show progress"
    )

    args = parser.parse_args()

    print("=" * 70)
    print("Re-enrich Previously Unmapped Entries")
    print("=" * 70)
    print(f"Input:  {args.input}")
    print(f"Output: {args.output}")
    print(f"Confidence threshold: {args.confidence_threshold}")
    print()

    # Initialize clients
    ols_client = OLSClient()
    oak_client = None
    if args.use_oak:
        try:
            oak_client = OAKClient()
            print("✓ OAK client initialized")
        except Exception as e:
            print(f"⚠ OAK client failed: {e}")

    print()

    # Re-enrich
    updated = re_enrich_unmapped(
        args.input,
        args.output,
        ols_client,
        oak_client,
        args.confidence_threshold,
        args.verbose
    )

    print()
    print("=" * 70)
    print(f"✓ Re-enriched {updated} previously unmapped entries")
    print("=" * 70)


if __name__ == "__main__":
    main()
