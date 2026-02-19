#!/usr/bin/env python3
"""
Remove Unmapped Entries from SSSOM File

This script removes unmapped entries (confidence 0.0, predicate semapv:Unmapped)
from an SSSOM file so they can be re-processed through enrichment with improved
normalization.

Usage:
    uv run python scripts/remove_unmapped_from_sssom.py \\
        --input output/culturemech_chebi_mappings_exact.sssom.tsv \\
        --output output/culturemech_chebi_mappings_mapped_only.sssom.tsv
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from enrich_sssom_with_ols import load_sssom_file, extract_sssom_metadata, save_sssom_file


def remove_unmapped_entries(input_path: Path, output_path: Path, verbose: bool = False):
    """Remove unmapped entries from SSSOM file."""

    # Load SSSOM file
    df = load_sssom_file(input_path)
    metadata = extract_sssom_metadata(input_path)

    if verbose:
        print(f"Loaded {len(df)} entries from {input_path}")
        print()

    # Find unmapped entries
    unmapped = df[
        (df['predicate_id'] == 'semapv:Unmapped') |
        (df['confidence'] == 0.0)
    ]

    if verbose:
        print(f"Found {len(unmapped)} unmapped entries")
        print()

    # Remove unmapped entries
    mapped_only = df[
        (df['predicate_id'] != 'semapv:Unmapped') &
        (df['confidence'] > 0.0)
    ]

    if verbose:
        print(f"Keeping {len(mapped_only)} mapped entries")
        print()

    # Save
    save_sssom_file(mapped_only, output_path, metadata)

    if verbose:
        print(f"Saved to: {output_path}")
        print()

    return len(unmapped), len(mapped_only)


def main():
    parser = argparse.ArgumentParser(
        description="Remove unmapped entries from SSSOM file"
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
        default=Path('output/culturemech_chebi_mappings_mapped_only.sssom.tsv'),
        help="Output SSSOM file (mapped entries only)"
    )
    parser.add_argument(
        '--verbose',
        action='store_true',
        help="Show progress"
    )

    args = parser.parse_args()

    print("=" * 70)
    print("Remove Unmapped Entries from SSSOM")
    print("=" * 70)
    print(f"Input:  {args.input}")
    print(f"Output: {args.output}")
    print()

    unmapped_count, mapped_count = remove_unmapped_entries(
        args.input,
        args.output,
        args.verbose
    )

    print()
    print("=" * 70)
    print(f"✓ Removed {unmapped_count} unmapped entries")
    print(f"✓ Kept {mapped_count} mapped entries")
    print("=" * 70)


if __name__ == "__main__":
    main()
