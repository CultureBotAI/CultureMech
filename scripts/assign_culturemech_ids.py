#!/usr/bin/env python3
"""
Assign CultureMech IDs to all media and solution records.

Creates stable, sequential identifiers in the format CultureMech:NNNNNN
where NNNNNN is a zero-padded 6-digit number.

Strategy:
1. Scan all existing YAML files and validate their IDs
2. Reserve every ID in the active registry, lifecycle catalog, and tombstones
3. Assign above the all-time issued high-water mark to files without IDs
4. Sort by filename for deterministic ordering
5. Update YAML files with new 'id' field
6. Regenerate the active compatibility registry

Usage:
    python scripts/assign_culturemech_ids.py [--start-id 1] [--dry-run]
"""

import argparse
import csv
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import yaml
from build_recipe_id_catalog import (
    DEFAULT_OUT as DEFAULT_CATALOG,
)
from build_recipe_id_catalog import (
    DEFAULT_TOMBSTONES,
    id_number,
    read_tombstones,
)


class CultureMechIDAssigner:
    """Assign stable CultureMech IDs to media records."""

    def __init__(
        self,
        start_id: int = 1,
        dry_run: bool = False,
        issued_ids: set[str] | None = None,
    ):
        self.start_id = start_id
        self.dry_run = dry_run
        self.current_id = start_id
        self.stats = {
            "files_scanned": 0,
            "files_with_id": 0,
            "files_assigned": 0,
            "highest_existing_id": 0,
            "errors": [],
        }
        self.id_registry = {}  # Maps CultureMech ID → file path
        self.issued_ids = set(issued_ids or ())
        # Maps CultureMech ID → list of file paths (only populated when >1).
        # Used by --check to detect cross-file ID collisions.
        self.duplicates: dict[str, list[str]] = defaultdict(list)

    def format_id(self, id_number: int) -> str:
        """Format ID as CultureMech:NNNNNN."""
        if not 1 <= id_number <= 999_999:
            raise ValueError("CultureMech ID space is limited to 000001 through 999999")
        return f"CultureMech:{id_number:06d}"

    def parse_id(self, id_string: str) -> int | None:
        """Parse CultureMech ID string to integer."""
        return id_number(id_string)

    def scan_existing_ids(self, base_dir: Path) -> int:
        """
        Scan all YAML files to find existing IDs.

        Returns:
            Highest existing ID number (0 if none found)
        """
        print(f"🔍 Scanning for existing CultureMech IDs in {base_dir}...")

        yaml_files = list(base_dir.rglob("*.yaml"))
        highest_id = 0

        for yaml_path in yaml_files:
            try:
                with open(yaml_path) as f:
                    data = yaml.safe_load(f)

                if not data:
                    continue

                self.stats["files_scanned"] += 1

                # Check for existing ID
                existing_id = data.get("id")
                if existing_id:
                    id_num = self.parse_id(existing_id)
                    if id_num is not None:
                        self.stats["files_with_id"] += 1
                        highest_id = max(highest_id, id_num)
                        if existing_id in self.id_registry:
                            # Cross-file duplicate. Remember both sides.
                            entry = self.duplicates[existing_id]
                            if not entry:
                                entry.append(self.id_registry[existing_id])
                            entry.append(str(yaml_path))
                        else:
                            self.id_registry[existing_id] = str(yaml_path)
                    else:
                        self.stats["errors"].append(
                            f"Malformed ID in {yaml_path}: {existing_id!r}; "
                            "expected CultureMech:NNNNNN"
                        )

            except Exception as e:
                self.stats["errors"].append(f"Error scanning {yaml_path.name}: {e}")
                continue

        self.stats["highest_existing_id"] = highest_id
        print(f"✓ Scanned {self.stats['files_scanned']} files")
        print(f"  - Files with IDs: {self.stats['files_with_id']}")
        print(f"  - Highest ID: {self.format_id(highest_id) if highest_id > 0 else 'None'}")

        return highest_id

    def assign_ids(self, base_dir: Path):
        """Assign IDs to all files without them."""
        print("\n📝 Assigning CultureMech IDs...")

        # Get all YAML files, sorted by path for deterministic ordering
        yaml_files = sorted(base_dir.rglob("*.yaml"))

        # Separate files with and without IDs
        files_needing_ids = []

        for yaml_path in yaml_files:
            try:
                with open(yaml_path) as f:
                    data = yaml.safe_load(f)

                if not data:
                    continue

                # Check if already has ID
                if not data.get("id"):
                    files_needing_ids.append(yaml_path)

            except Exception as e:
                self.stats["errors"].append(f"Error checking {yaml_path.name}: {e}")
                continue

        print(f"  - Files needing IDs: {len(files_needing_ids)}")

        # Assign IDs sequentially
        for yaml_path in files_needing_ids:
            success = self._assign_id_to_file(yaml_path)
            if success:
                self.stats["files_assigned"] += 1

    def _assign_id_to_file(self, yaml_path: Path) -> bool:
        """Assign ID to a single file."""
        try:
            with open(yaml_path) as f:
                data = yaml.safe_load(f)

            if not data:
                return False

            # Generate new ID
            new_id = self.format_id(self.current_id)

            # Check for conflicts (shouldn't happen but be safe)
            if new_id in self.id_registry or new_id in self.issued_ids:
                self.stats["errors"].append(f"ID conflict: {new_id} was already issued!")
                return False

            # Add ID field at the top
            data["id"] = new_id

            # Add curation history entry
            if "curation_history" not in data:
                data["curation_history"] = []

            data["curation_history"].append(
                {
                    "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                    "curator": "culturemech-id-assigner-v1.0",
                    "action": "Assigned CultureMech ID",
                    "notes": f"Assigned stable identifier: {new_id}",
                }
            )

            # Write back (if not dry run)
            if not self.dry_run:
                # Preserve order: id first, then rest
                ordered_data = {"id": new_id}
                ordered_data.update({k: v for k, v in data.items() if k != "id"})

                with open(yaml_path, "w") as f:
                    yaml.dump(
                        ordered_data,
                        f,
                        default_flow_style=False,
                        sort_keys=False,
                        allow_unicode=True,
                    )

            # Update registry
            self.id_registry[new_id] = str(yaml_path)
            self.issued_ids.add(new_id)
            self.current_id += 1

            return True

        except Exception as e:
            self.stats["errors"].append(f"Error assigning ID to {yaml_path.name}: {e}")
            return False

    def save_registry(self, output_path: Path):
        """Save ID registry to TSV file."""
        print(f"\n💾 Saving ID registry to {output_path}...")

        with open(output_path, "w") as f:
            f.write("culturemech_id\tfile_path\n")
            for cm_id in sorted(self.id_registry.keys(), key=lambda x: self.parse_id(x) or 0):
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
        report.append(
            f"  Highest existing ID:  {self.format_id(self.stats['highest_existing_id']) if self.stats['highest_existing_id'] > 0 else 'None'}"
        )
        next_id = self.format_id(self.current_id) if self.current_id <= 999_999 else "EXHAUSTED"
        report.append(f"  Next available ID:    {next_id}")
        report.append(f"  Total IDs in registry: {len(self.id_registry)}")
        report.append(f"  Errors:               {len(self.stats['errors'])}")
        report.append("")

        if self.stats["errors"]:
            report.append("ERRORS:")
            report.append("-" * 80)
            for error in self.stats["errors"][:20]:  # Show first 20
                report.append(f"  ⚠ {error}")
            if len(self.stats["errors"]) > 20:
                report.append(f"  ... and {len(self.stats['errors']) - 20} more errors")
            report.append("")

        report.append("ID RANGE:")
        if self.id_registry:
            ids = sorted(
                [self.parse_id(cm_id) for cm_id in self.id_registry.keys() if self.parse_id(cm_id)]
            )
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
    parser.add_argument("--start-id", type=int, default=1, help="Starting ID number (default: 1)")
    parser.add_argument(
        "--input-dir",
        type=Path,
        default=Path("data/normalized_yaml"),
        help="Input directory with YAML files (default: data/normalized_yaml)",
    )
    parser.add_argument(
        "--registry-output",
        type=Path,
        default=Path("data/culturemech_id_registry.tsv"),
        help="Output path for ID registry (default: data/culturemech_id_registry.tsv)",
    )
    parser.add_argument(
        "--catalog",
        type=Path,
        default=DEFAULT_CATALOG,
        help="Published lifecycle catalog used as the issued-ID high-water ledger",
    )
    parser.add_argument(
        "--tombstones",
        type=Path,
        default=DEFAULT_TOMBSTONES,
        help="Retired-ID ledger whose identifiers must never be reused",
    )
    parser.add_argument(
        "--dry-run", action="store_true", help="Dry run mode - no files will be modified"
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Scan-only: detect cross-file ID collisions and exit non-zero if any found. "
        "No files modified. Use this as a pre-commit / CI gate.",
    )

    args = parser.parse_args()

    if not 1 <= args.start_id <= 999_999:
        print("❌ --start-id must be between 1 and 999999")
        return 2

    print("=" * 80)
    print("CULTUREMECH ID ASSIGNMENT")
    print("=" * 80)
    print()

    if not args.input_dir.exists():
        print(f"❌ Input directory not found: {args.input_dir}")
        return 1

    issued_ids: set[str] = set()
    for ledger in (args.registry_output, args.catalog):
        if not ledger.is_file():
            continue
        try:
            with ledger.open(encoding="utf-8", newline="") as stream:
                reader = csv.DictReader(stream, delimiter="\t")
                if "culturemech_id" not in (reader.fieldnames or ()):
                    print(f"❌ Issued-ID ledger has no culturemech_id column: {ledger}")
                    return 2
                for line_number, row in enumerate(reader, start=2):
                    culturemech_id = (row.get("culturemech_id") or "").strip()
                    if id_number(culturemech_id) is None:
                        print(
                            f"❌ Malformed issued ID at {ledger}:{line_number}: "
                            f"{culturemech_id!r}"
                        )
                        return 2
                    issued_ids.add(culturemech_id)
        except (OSError, csv.Error) as exc:
            print(f"❌ Cannot read issued-ID ledger {ledger}: {exc}")
            return 2

    tombstones, tombstone_errors = read_tombstones(args.tombstones)
    if tombstone_errors:
        print(f"❌ Invalid tombstone ledger {args.tombstones}:")
        for error in tombstone_errors[:20]:
            print(f"  - {error}")
        return 2
    issued_ids.update(tombstones)

    # Initialize assigner. The catalog and tombstone ledger reserve every ID
    # ever issued, including records that no longer exist in the live corpus.
    assigner = CultureMechIDAssigner(
        start_id=args.start_id,
        dry_run=args.dry_run,
        issued_ids=issued_ids,
    )

    # Step 1: Scan for existing IDs
    highest_existing = assigner.scan_existing_ids(args.input_dir)

    # Collision detection — applies in --check mode and is also a pre-flight
    # check before any new assignment runs.
    if assigner.duplicates:
        print(f"\n❌ {len(assigner.duplicates)} duplicate CultureMech ID(s) detected:")
        for id_str, paths in sorted(assigner.duplicates.items()):
            print(f"  {id_str}: {len(paths)} files")
            for p in paths:
                print(f"    - {p}")
        return 2
    if assigner.stats["errors"]:
        print(f"\n❌ {len(assigner.stats['errors'])} corpus scan error(s):")
        for error in assigner.stats["errors"][:20]:
            print(f"  - {error}")
        return 2
    reused = sorted(set(assigner.id_registry) & set(tombstones))
    if reused:
        print("\n❌ Retired CultureMech ID(s) were reused by live records:")
        for culturemech_id in reused[:20]:
            print(f"  - {culturemech_id}: {assigner.id_registry[culturemech_id]}")
        return 2
    if args.check:
        missing_count = assigner.stats["files_scanned"] - assigner.stats["files_with_id"]
        if missing_count:
            print(
                f"\n❌ {missing_count} record(s) have no CultureMech ID; "
                "mint them with `just assign-ids`."
            )
            return 2
        print("\n✓ Every record has one canonical, unique, unreused CultureMech ID.")
        return 0

    # Step 2: Set starting ID to next available
    highest_issued = max(
        (id_number(culturemech_id) or 0 for culturemech_id in issued_ids),
        default=0,
    )
    high_water = max(highest_existing, highest_issued)
    missing_count = assigner.stats["files_scanned"] - assigner.stats["files_with_id"]
    next_number = high_water + 1 if high_water else assigner.start_id
    if missing_count and next_number + missing_count - 1 > 999_999:
        print(
            f"\n❌ CultureMech ID space has room for {max(0, 1_000_000 - next_number)} "
            f"record(s), but {missing_count} need IDs; no files were changed."
        )
        return 2
    assigner.current_id = next_number
    if missing_count:
        print(f"\n✓ Will start assigning from {assigner.format_id(assigner.current_id)}")
    elif next_number > 999_999:
        print("\n✓ ID space is full; every record is already assigned.")
    elif high_water:
        print(f"\n✓ Next available ID is {assigner.format_id(assigner.current_id)}")
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
        report_path = Path("data/culturemech_id_assignment_report.txt")
        with open(report_path, "w") as f:
            f.write(report)
        print(f"✓ Report saved to: {report_path}")

    return 0


if __name__ == "__main__":
    exit(main())
