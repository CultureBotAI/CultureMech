#!/usr/bin/env python3
"""
Check CHEBI IDs in normalized YAML files for validity

Scans all normalized YAML files and reports on CHEBI ID statistics
and potential issues.

Usage:
    uv run python scripts/check_chebi_ids.py
"""

import yaml
from pathlib import Path
from collections import Counter, defaultdict
import re


def is_valid_chebi_format(chebi_id: str) -> bool:
    """Check if CHEBI ID has valid format."""
    if not chebi_id.startswith('CHEBI:'):
        return False

    try:
        num = int(chebi_id.split(':')[1])
        # CHEBI IDs should be positive and reasonable (< 10 million)
        return 0 < num < 10000000
    except (ValueError, IndexError):
        return False


def extract_chebi_ids(yaml_dir: Path):
    """Extract all CHEBI IDs from YAML files."""
    chebi_ids = []
    invalid_ids = []
    suspicious_ids = []

    for yaml_file in yaml_dir.rglob('*.yaml'):
        try:
            with open(yaml_file) as f:
                recipe = yaml.safe_load(f)

            if not recipe:
                continue

            # Check ingredients
            for ingredient in recipe.get('ingredients', []):
                term = ingredient.get('term', {})
                if term and term.get('id'):
                    chebi_id = term['id']

                    if is_valid_chebi_format(chebi_id):
                        chebi_ids.append(chebi_id)

                        # Check for suspicious patterns
                        num = int(chebi_id.split(':')[1])
                        if num > 999999:  # 7+ digits
                            suspicious_ids.append((chebi_id, str(yaml_file)))
                    else:
                        invalid_ids.append((chebi_id, str(yaml_file)))

            # Check solutions
            for solution in recipe.get('solutions', []):
                for ingredient in solution.get('composition', []):
                    term = ingredient.get('term', {})
                    if term and term.get('id'):
                        chebi_id = term['id']

                        if is_valid_chebi_format(chebi_id):
                            chebi_ids.append(chebi_id)

                            num = int(chebi_id.split(':')[1])
                            if num > 999999:
                                suspicious_ids.append((chebi_id, str(yaml_file)))
                        else:
                            invalid_ids.append((chebi_id, str(yaml_file)))

        except Exception as e:
            print(f"Error processing {yaml_file}: {e}")
            continue

    return chebi_ids, invalid_ids, suspicious_ids


def main():
    yaml_dir = Path('data/normalized_yaml')

    if not yaml_dir.exists():
        print(f"Error: {yaml_dir} not found")
        return

    print("Scanning YAML files for CHEBI IDs...")
    print("=" * 70)

    chebi_ids, invalid_ids, suspicious_ids = extract_chebi_ids(yaml_dir)

    # Statistics
    print(f"\nTotal CHEBI IDs found: {len(chebi_ids)}")
    print(f"Unique CHEBI IDs: {len(set(chebi_ids))}")
    print(f"Invalid format: {len(invalid_ids)}")
    print(f"Suspicious (7+ digits): {len(suspicious_ids)}")

    # Most common IDs
    print("\nTop 10 most common CHEBI IDs:")
    counter = Counter(chebi_ids)
    for chebi_id, count in counter.most_common(10):
        print(f"  {chebi_id}: {count}")

    # Invalid IDs
    if invalid_ids:
        print(f"\n❌ Invalid CHEBI IDs found ({len(invalid_ids)}):")
        for chebi_id, file_path in invalid_ids[:20]:
            print(f"  {chebi_id} in {Path(file_path).name}")

        if len(invalid_ids) > 20:
            print(f"  ... and {len(invalid_ids) - 20} more")

    # Suspicious IDs
    if suspicious_ids:
        print(f"\n⚠️  Suspicious CHEBI IDs (7+ digits) found ({len(suspicious_ids)}):")
        for chebi_id, file_path in suspicious_ids[:20]:
            print(f"  {chebi_id} in {Path(file_path).name}")

        if len(suspicious_ids) > 20:
            print(f"  ... and {len(suspicious_ids) - 20} more")

    # CHEBI number distribution
    print("\nCHEBI number digit distribution:")
    digit_counts = defaultdict(int)
    for chebi_id in chebi_ids:
        try:
            num_str = chebi_id.split(':')[1]
            digit_counts[len(num_str)] += 1
        except:
            pass

    for digits in sorted(digit_counts.keys()):
        count = digit_counts[digits]
        pct = count / len(chebi_ids) * 100 if chebi_ids else 0
        print(f"  {digits} digit(s): {count} ({pct:.1f}%)")

    print("\n" + "=" * 70)

    # Recommendations
    if invalid_ids or suspicious_ids:
        print("\n💡 Recommendations:")
        if invalid_ids:
            print("  - Fix invalid CHEBI ID formats")
            print("    Run: grep -r '<invalid_id>' data/normalized_yaml/")
        if suspicious_ids:
            print("  - Review suspicious CHEBI IDs (7+ digits)")
            print("    These may be concatenated numbers or typos")
            print("    Example: CHEBI:10716816 might be two IDs: 107 + 16816")


if __name__ == "__main__":
    main()
