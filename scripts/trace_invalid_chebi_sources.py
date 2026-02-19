#!/usr/bin/env python3
"""
Trace Invalid CHEBI IDs to Source Mapping Files

Identifies which MicrobeMediaParam/MediaDive mapping files contain
invalid CHEBI IDs and reports them for correction.

Usage:
    uv run python scripts/trace_invalid_chebi_sources.py
"""

import csv
from pathlib import Path
from collections import defaultdict
import json


def is_valid_chebi_id(chebi_id: str) -> tuple[bool, str]:
    """Check if CHEBI ID is valid."""
    if not isinstance(chebi_id, str):
        return False, "not a string"

    # Handle different CHEBI ID formats
    chebi_str = str(chebi_id).strip()

    # Check for CHEBI: prefix
    if chebi_str.startswith('CHEBI:'):
        num_str = chebi_str.split(':')[1]
    else:
        # Might be just the number
        num_str = chebi_str

    try:
        num = int(num_str)
    except ValueError:
        return False, "invalid numeric part"

    if num <= 0:
        return False, "negative or zero"

    if num > 9999999:
        return False, "8+ digits (clearly invalid)"

    if num > 999999:
        return False, "7 digits (suspicious)"

    return True, "valid"


def scan_microbe_media_param(data_dir: Path) -> dict:
    """Scan MicrobeMediaParam TSV files for invalid CHEBI IDs."""
    results = defaultdict(list)

    if not data_dir.exists():
        print(f"⚠️  MicrobeMediaParam directory not found: {data_dir}")
        return results

    print(f"\n🔍 Scanning MicrobeMediaParam files in {data_dir}...")

    for tsv_file in data_dir.glob('*.tsv'):
        print(f"   Checking {tsv_file.name}...")

        try:
            with open(tsv_file) as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row_num, row in enumerate(reader, 2):  # Start at 2 (header is row 1)
                    # Check for CHEBI ID in various columns
                    chebi_id = None

                    # Try different column names
                    for col in ['chebi_id', 'mapped', 'CHEBI', 'chebi']:
                        if col in row and row[col]:
                            potential_id = row[col].strip()
                            # Extract CHEBI ID if it's a full term
                            if 'CHEBI:' in potential_id or 'chebi:' in potential_id:
                                chebi_id = potential_id
                                break
                            elif potential_id.isdigit():
                                chebi_id = f"CHEBI:{potential_id}"
                                break

                    if chebi_id:
                        is_valid, reason = is_valid_chebi_id(chebi_id)
                        if not is_valid:
                            results[tsv_file.name].append({
                                'row': row_num,
                                'chebi_id': chebi_id,
                                'reason': reason,
                                'ingredient': row.get('original', row.get('normalized_compound', 'unknown')),
                                'original_value': row.get('mapped', row.get('chebi_id', ''))
                            })

        except Exception as e:
            print(f"   ❌ Error reading {tsv_file.name}: {e}")

    return results


def scan_mediadive(data_dir: Path) -> dict:
    """Scan MediaDive JSON files for invalid CHEBI IDs."""
    results = defaultdict(list)

    if not data_dir.exists():
        print(f"⚠️  MediaDive directory not found: {data_dir}")
        return results

    print(f"\n🔍 Scanning MediaDive files in {data_dir}...")

    ingredients_file = data_dir / "mediadive_ingredients.json"
    if ingredients_file.exists():
        print(f"   Checking {ingredients_file.name}...")

        try:
            with open(ingredients_file) as f:
                data = json.load(f)

            # Handle both array and object formats
            ingredients = data.get('data', data) if isinstance(data, dict) else data

            if isinstance(ingredients, dict):
                ingredients = list(ingredients.values())

            for idx, ingredient in enumerate(ingredients):
                chebi_id = ingredient.get('ChEBI') or ingredient.get('chebi_id')
                if chebi_id:
                    is_valid, reason = is_valid_chebi_id(str(chebi_id))
                    if not is_valid:
                        results[ingredients_file.name].append({
                            'index': idx,
                            'chebi_id': str(chebi_id),
                            'reason': reason,
                            'ingredient': ingredient.get('name', 'unknown')
                        })

        except Exception as e:
            print(f"   ❌ Error reading {ingredients_file.name}: {e}")

    return results


def main():
    print("=" * 70)
    print("Tracing Invalid CHEBI IDs to Source Files")
    print("=" * 70)

    # Paths
    microbe_media_param_dir = Path('data/raw/microbe-media-param')
    mediadive_dir = Path('data/raw/mediadive')

    # Scan source files
    mmp_results = scan_microbe_media_param(microbe_media_param_dir)
    mediadive_results = scan_mediadive(mediadive_dir)

    # Report results
    print("\n" + "=" * 70)
    print("Results")
    print("=" * 70)

    total_invalid = 0

    # MicrobeMediaParam results
    if mmp_results:
        print("\n📊 MicrobeMediaParam Files with Invalid CHEBI IDs:")
        for filename, issues in sorted(mmp_results.items()):
            print(f"\n  📄 {filename}")
            print(f"     {len(issues)} invalid ID(s) found")

            # Group by CHEBI ID
            by_id = defaultdict(list)
            for issue in issues:
                by_id[issue['chebi_id']].append(issue)

            for chebi_id, occurrences in sorted(by_id.items(), key=lambda x: -len(x[1])):
                print(f"\n     ⚠️  {chebi_id} ({occurrences[0]['reason']})")
                print(f"        Occurrences: {len(occurrences)}")
                print(f"        Ingredients: {', '.join(set(o['ingredient'] for o in occurrences[:5]))}")

                # Show first few row numbers
                rows = [str(o['row']) for o in occurrences[:5]]
                print(f"        Rows: {', '.join(rows)}")
                if len(occurrences) > 5:
                    print(f"        ... and {len(occurrences) - 5} more rows")

            total_invalid += len(issues)
    else:
        print("\n✅ No invalid CHEBI IDs found in MicrobeMediaParam files")

    # MediaDive results
    if mediadive_results:
        print("\n📊 MediaDive Files with Invalid CHEBI IDs:")
        for filename, issues in sorted(mediadive_results.items()):
            print(f"\n  📄 {filename}")
            print(f"     {len(issues)} invalid ID(s) found")

            for issue in issues[:10]:
                print(f"     ⚠️  {issue['chebi_id']} for '{issue['ingredient']}' ({issue['reason']})")

            if len(issues) > 10:
                print(f"     ... and {len(issues) - 10} more")

            total_invalid += len(issues)
    else:
        print("\n✅ No invalid CHEBI IDs found in MediaDive files")

    # Summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total invalid CHEBI IDs in source files: {total_invalid}")

    if total_invalid > 0:
        print("\n📌 Recommendations:")
        print("\n1. Create corrected mapping files:")
        print("   - Copy the TSV files to a new location")
        print("   - Manually fix the invalid CHEBI IDs")
        print("   - Replace the original files")

        print("\n2. Report to upstream maintainers:")
        print("   - MicrobeMediaParam: https://github.com/KG-Hub/KG-Microbe/MicrobeMediaParam")
        print("   - MediaDive: https://mediadive.dsmz.de/")

        print("\n3. Remove invalid IDs from normalized_yaml:")
        print("   uv run python scripts/remove_invalid_chebi_ids.py --dry-run")
        print("   uv run python scripts/remove_invalid_chebi_ids.py")

        print("\n4. Re-run enrichment after fixes:")
        print("   just enrich-with-chebi")
        print("   just sssom-pipeline")

    print("\n" + "=" * 70)


if __name__ == "__main__":
    main()
