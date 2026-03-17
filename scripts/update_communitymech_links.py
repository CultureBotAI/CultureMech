#!/usr/bin/env python3
"""Update CommunityMech YAMLs with CultureMech IDs for bidirectional linking.

This script reads the import log from import_from_communitymech.py and updates
the corresponding CommunityMech growth_media entries with culturemech_id and
culturemech_url fields.

Usage:
    python scripts/update_communitymech_links.py \\
        --import-log data/import_tracking/communitymech_imports.json \\
        --communitymech-repo ../CommunityMech/CommunityMech \\
        --dry-run  # Optional: preview only
"""

import argparse
import json
import yaml
from pathlib import Path
from typing import Dict, List, Any


def generate_culturemech_url(culturemech_id: str) -> str:
    """Generate GitHub URL for a CultureMech ID."""
    return f"https://github.com/CultureBotAI/CultureMech/tree/main/kb/media/{culturemech_id}"


def update_communitymech_yaml(
    yaml_path: Path,
    media_name: str,
    culturemech_id: str,
    dry_run: bool = False
) -> bool:
    """Add culturemech_id to a growth_media entry.

    Returns:
        True if update was successful, False otherwise
    """
    try:
        with open(yaml_path) as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"  ✗ Error loading {yaml_path}: {e}")
        return False

    if not data or 'growth_media' not in data:
        print(f"  ✗ No growth_media section in {yaml_path}")
        return False

    # Find and update the medium
    updated = False
    for medium in data.get('growth_media', []):
        if medium.get('name') == media_name:
            # Check if already has culturemech_id
            if 'culturemech_id' in medium:
                print(f"  ⚠ Already has culturemech_id: {medium['culturemech_id']}")
                if medium['culturemech_id'] != culturemech_id:
                    print(f"    WARNING: Mismatch! Existing: {medium['culturemech_id']}, New: {culturemech_id}")
                return False

            # Add CultureMech ID and URL
            medium['culturemech_id'] = culturemech_id
            medium['culturemech_url'] = generate_culturemech_url(culturemech_id)
            updated = True
            break

    if not updated:
        print(f"  ✗ Could not find medium '{media_name}' in {yaml_path}")
        return False

    if dry_run:
        print(f"  [DRY RUN] Would update {yaml_path}")
        print(f"    Adding: culturemech_id: {culturemech_id}")
        print(f"    Adding: culturemech_url: {generate_culturemech_url(culturemech_id)}")
        return True

    # Write back to file
    try:
        with open(yaml_path, 'w') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
        print(f"  ✓ Updated {yaml_path}")
        return True
    except Exception as e:
        print(f"  ✗ Error writing {yaml_path}: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description='Update CommunityMech YAMLs with CultureMech IDs for backlinking'
    )
    parser.add_argument(
        '--import-log',
        type=Path,
        required=True,
        help='Path to import log JSON from import_from_communitymech.py'
    )
    parser.add_argument(
        '--communitymech-repo',
        type=Path,
        required=True,
        help='Path to CommunityMech repository root'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview only, do not write files'
    )

    args = parser.parse_args()

    # Load import log
    print(f"Loading import log: {args.import_log}")
    with open(args.import_log) as f:
        import_log = json.load(f)

    print(f"Found {len(import_log)} imported media\n")

    # Update each CommunityMech file
    success_count = 0
    for i, entry in enumerate(import_log, 1):
        media_name = entry['media_name']
        culturemech_id = entry['culturemech_id']
        source_files = entry['source_files']

        print(f"[{i}/{len(import_log)}] {media_name}")
        print(f"  CultureMech ID: {culturemech_id}")

        # Update each source file (a medium can appear in multiple communities)
        for source_file in source_files:
            full_path = args.communitymech_repo / source_file
            print(f"  Updating: {source_file}")

            if update_communitymech_yaml(full_path, media_name, culturemech_id, args.dry_run):
                success_count += 1

        print()

    print(f"{'=' * 60}")
    print(f"Update complete: {success_count} file updates")
    if args.dry_run:
        print("(DRY RUN - no files were written)")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    main()
