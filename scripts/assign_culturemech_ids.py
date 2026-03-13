#!/usr/bin/env python3
"""
Assign CultureMech IDs to all media and solution records.

Creates stable, sequential identifiers in the format CultureMech:NNNNNN
where NNNNNN is a zero-padded 6-digit number.

Strategy:
1. Scan all existing YAML files to find highest ID if any exist
2. Assign IDs sequentially to files without IDs
3. Sort by filename for deterministic ordering
4. Update YAML files with new 'id' field
5. Generate ID registry file for tracking

Usage:
    python scripts/assign_culturemech_ids.py [--start-id 1] [--dry-run]
"""

import argparse
import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from collections import defaultdict


class CultureMechIDAssigner:
    """Assign stable CultureMech IDs to media records."""

    def __init__(self, start_id: int = 1, dry_run: bool = False):
        self.start_id = start_id
        self.dry_run = dry_run
        self.current_id = start_id
        self.stats = {
            'files_scanned': 0,
            'files_with_id': 0,
            'files_assigned': 0,
            'highest_existing_id': 0,
            'errors': []
        }
        self.id_registry = {}  # Maps CultureMech ID → file path

    def format_id(self, id_number: int) -> str:
        """Format ID as CultureMech:NNNNNN."""
        return f"CultureMech:{id_number:06d}"

    def parse_id(self, id_string: str) -> Optional[int]:
        """Parse CultureMech ID string to integer."""
        if not id_string or not id_string.startswith('CultureMech:'):
            return None
        try:
            return int(id_string.split(':')[1])
        except (IndexError, ValueError):
            return None

    def scan_existing_ids(self, base_dir: Path) -> int:
        """
        Scan all YAML files to find existing IDs.

        Returns:
            Highest existing ID number (0 if none found)
        """
        print(f"🔍 Scanning for existing CultureMech IDs in {base_dir}...")

        yaml_files = list(base_dir.rglob('*.yaml'))
        highest_id = 0

        for yaml_path in yaml_files:
            try:
                with open(yaml_path, 'r') as f:
                    data = yaml.safe_load(f)

                if not data:
                    continue

                self.stats['files_scanned'] += 1

                # Check for existing ID
                existing_id = data.get('id')
                if existing_id:
                    id_num = self.parse_id(existing_id)
                    if id_num:
                        self.stats['files_with_id'] += 1
                        highest_id = max(highest_id, id_num)
                        self.id_registry[existing_id] = str(yaml_path)

            except Exception as e:
                self.stats['errors'].append(f"Error scanning {yaml_path.name}: {e}")
                continue

        self.stats['highest_existing_id'] = highest_id
        print(f"✓ Scanned {self.stats['files_scanned']} files")
        print(f"  - Files with IDs: {self.stats['files_with_id']}")
        print(f"  - Highest ID: {self.format_id(highest_id) if highest_id > 0 else 'None'}")

        return highest_id

    def assign_ids(self, base_dir: Path):
        """Assign IDs to all files without them."""
        print(f"\n📝 Assigning CultureMech IDs...")

        # Get all YAML files, sorted by path for deterministic ordering
        yaml_files = sorted(base_dir.rglob('*.yaml'))

        # Separate files with and without IDs
        files_needing_ids = []

        for yaml_path in yaml_files:
            try:
                with open(yaml_path, 'r') as f:
                    data = yaml.safe_load(f)

                if not data:
                    continue

                # Check if already has ID
                if not data.get('id'):
                    files_needing_ids.append(yaml_path)

            except Exception as e:
                self.stats['errors'].append(f"Error checking {yaml_path.name}: {e}")
                continue

        print(f"  - Files needing IDs: {len(files_needing_ids)}")

        # Assign IDs sequentially
        for yaml_path in files_needing_ids:
            success = self._assign_id_to_file(yaml_path)
            if success:
                self.stats['files_assigned'] += 1

    def _assign_id_to_file(self, yaml_path: Path) -> bool:
        """Assign ID to a single file."""
        try:
            with open(yaml_path, 'r') as f:
                data = yaml.safe_load(f)

            if not data:
                return False

            # Generate new ID
            new_id = self.format_id(self.current_id)

            # Check for conflicts (shouldn't happen but be safe)
            if new_id in self.id_registry:
                self.stats['errors'].append(f"ID conflict: {new_id} already exists!")
                return False

            # Add ID field at the top
            data['id'] = new_id

            # Add curation history entry
            if 'curation_history' not in data:
                data['curation_history'] = []

            data['curation_history'].append({
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'curator': 'culturemech-id-assigner-v1.0',
                'action': 'Assigned CultureMech ID',
                'notes': f'Assigned stable identifier: {new_id}'
            })

            # Write back (if not dry run)
            if not self.dry_run:
                # Preserve order: id first, then rest
                ordered_data = {'id': new_id}
                ordered_data.update({k: v for k, v in data.items() if k != 'id'})

                with open(yaml_path, 'w') as f:
                    yaml.dump(ordered_data, f, default_flow_style=False,
                             sort_keys=False, allow_unicode=True)

            # Update registry
            self.id_registry[new_id] = str(yaml_path)
            self.current_id += 1

            return True

        except Exception as e:
            self.stats['errors'].append(f"Error assigning ID to {yaml_path.name}: {e}")
            return False

    def save_registry(self, output_path: Path):
        """Save ID registry to TSV file."""
        print(f"\n💾 Saving ID registry to {output_path}...")

        with open(output_path, 'w') as f:
            f.write("culturemech_id\tfile_path\n")
            for cm_id in sorted(self.id_registry.keys(),
                              key=lambda x: self.parse_id(x) or 0):
                f.write(f"{cm_id}\t{self.id_registry[cm_id]}\n")

        print(f"✓ Registry saved ({len(self.id_registry)} entries)")

    def generate_report(self) -> str:
        """Generate summary report."""
        report = []
        report.append("=" * 80)
        report.append("CULTUREMECH ID ASSIGNMENT REPORT")
        report.append("=" * 80)
        report.append("")

        if self.dry_run:
            report.append("*** DRY RUN MODE - NO FILES MODIFIED ***")
            report.append("")

        report.append("SUMMARY:")
        report.append(f"  Files scanned:        {self.stats['files_scanned']}")
        report.append(f"  Files with IDs:       {self.stats['files_with_id']}")
        report.append(f"  Files assigned IDs:   {self.stats['files_assigned']}")
        report.append(f"  Highest existing ID:  {self.format_id(self.stats['highest_existing_id']) if self.stats['highest_existing_id'] > 0 else 'None'}")
        report.append(f"  Next available ID:    {self.format_id(self.current_id)}")
        report.append(f"  Total IDs in registry: {len(self.id_registry)}")
        report.append(f"  Errors:               {len(self.stats['errors'])}")
        report.append("")

        if self.stats['errors']:
            report.append("ERRORS:")
            report.append("-" * 80)
            for error in self.stats['errors'][:20]:  # Show first 20
                report.append(f"  ⚠ {error}")
            if len(self.stats['errors']) > 20:
                report.append(f"  ... and {len(self.stats['errors']) - 20} more errors")
            report.append("")

        report.append("ID RANGE:")
        if self.id_registry:
            ids = sorted([self.parse_id(cm_id) for cm_id in self.id_registry.keys()
                         if self.parse_id(cm_id)])
            if ids:
                report.append(f"  First ID: {self.format_id(ids[0])}")
                report.append(f"  Last ID:  {self.format_id(ids[-1])}")
        report.append("")

        report.append("=" * 80)
        return "\n".join(report)


def main():
    """Main execution."""
    parser = argparse.ArgumentParser(
        description="Assign CultureMech IDs to media and solution records"
    )
    parser.add_argument(
        '--start-id',
        type=int,
        default=1,
        help='Starting ID number (default: 1)'
    )
    parser.add_argument(
        '--input-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Input directory with YAML files (default: data/normalized_yaml)'
    )
    parser.add_argument(
        '--registry-output',
        type=Path,
        default=Path('data/culturemech_id_registry.tsv'),
        help='Output path for ID registry (default: data/culturemech_id_registry.tsv)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Dry run mode - no files will be modified'
    )

    args = parser.parse_args()

    print("=" * 80)
    print("CULTUREMECH ID ASSIGNMENT")
    print("=" * 80)
    print()

    if not args.input_dir.exists():
        print(f"❌ Input directory not found: {args.input_dir}")
        return 1

    # Initialize assigner
    assigner = CultureMechIDAssigner(
        start_id=args.start_id,
        dry_run=args.dry_run
    )

    # Step 1: Scan for existing IDs
    highest_existing = assigner.scan_existing_ids(args.input_dir)

    # Step 2: Set starting ID to next available
    if highest_existing > 0:
        assigner.current_id = highest_existing + 1
        print(f"\n✓ Will start assigning from {assigner.format_id(assigner.current_id)}")
    else:
        print(f"\n✓ No existing IDs found, starting from {assigner.format_id(assigner.start_id)}")

    # Step 3: Assign IDs to files without them
    assigner.assign_ids(args.input_dir)

    # Step 4: Save registry
    if not args.dry_run:
        assigner.save_registry(args.registry_output)

    # Step 5: Generate report
    report = assigner.generate_report()
    print("\n" + report)

    # Save report
    if not args.dry_run:
        report_path = Path('data/culturemech_id_assignment_report.txt')
        with open(report_path, 'w') as f:
            f.write(report)
        print(f"✓ Report saved to: {report_path}")

    return 0


if __name__ == '__main__':
    exit(main())
