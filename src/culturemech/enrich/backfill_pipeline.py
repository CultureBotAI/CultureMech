"""Systematic backfill pipeline for applying enrichments to existing recipes.

Applies available enrichments systematically:
1. ATCC cross-references
2. CHEBI term mappings (SSSOM)
3. Preparation steps
4. Organism data (from curation)
"""

import json
import logging
import time
from pathlib import Path
from typing import Any, Dict, List, Optional
import yaml

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EnrichmentBackfillPipeline:
    """Apply enrichments systematically to recipe files."""

    def __init__(self):
        """Initialize backfill pipeline."""
        self.stats = {
            "files_processed": 0,
            "atcc_refs_added": 0,
            "prep_steps_added": 0,
            "organism_data_added": 0,
            "errors": 0
        }

    def apply_atcc_crossrefs(
        self,
        yaml_dir: Path,
        crossref_file: Path,
        dry_run: bool = False
    ):
        """
        Add ATCC cross-references to DSMZ files.

        Args:
            yaml_dir: Directory containing YAML files
            crossref_file: Path to atcc_crossref.json
            dry_run: If True, only show what would be done
        """
        if not crossref_file.exists():
            logger.warning(f"ATCC crossref file not found: {crossref_file}")
            return

        with open(crossref_file, 'r') as f:
            crossrefs = json.load(f)

        logger.info(f"Applying ATCC cross-references from {len(crossrefs)} entries...")

        for atcc_id, ref_data in crossrefs.items():
            dsmz_id = ref_data.get("dsmz")
            if not dsmz_id:
                continue

            # Find matching DSMZ file
            dsmz_files = list(yaml_dir.glob(f"**/DSMZ_{dsmz_id}_*.yaml"))
            if not dsmz_files:
                logger.debug(f"  No DSMZ file found for ID {dsmz_id}")
                continue

            for yaml_file in dsmz_files:
                if dry_run:
                    logger.info(f"  Would add ATCC:{atcc_id} to {yaml_file.name}")
                    continue

                try:
                    with open(yaml_file, 'r', encoding='utf-8') as f:
                        data = yaml.safe_load(f)

                    # Check if already has ATCC reference
                    notes = data.get("notes", "")
                    if f"ATCC:{atcc_id}" in notes or f"ATCC {atcc_id}" in notes:
                        logger.debug(f"  {yaml_file.name} already has ATCC:{atcc_id}")
                        continue

                    # Add ATCC cross-reference to notes
                    atcc_note = f"Cross-reference: ATCC:{atcc_id} ({ref_data['name']})"
                    if notes:
                        data["notes"] = f"{notes}\n\n{atcc_note}"
                    else:
                        data["notes"] = atcc_note

                    # Add to curation history
                    if "curation_history" not in data:
                        data["curation_history"] = []

                    data["curation_history"].append({
                        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.000000Z", time.gmtime()),
                        "curator": "atcc-crossref-backfill",
                        "action": "Added ATCC cross-reference",
                        "notes": f"ATCC:{atcc_id} verified equivalent (verified {ref_data.get('verification_date', 'unknown')})"
                    })

                    # Save updated file
                    with open(yaml_file, 'w', encoding='utf-8') as f:
                        yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

                    logger.info(f"  ✓ Added ATCC:{atcc_id} to {yaml_file.name}")
                    self.stats["atcc_refs_added"] += 1

                except Exception as e:
                    logger.error(f"  ✗ Failed to update {yaml_file.name}: {e}")
                    self.stats["errors"] += 1

    def apply_organism_data(
        self,
        yaml_dir: Path,
        organism_file: Path,
        dry_run: bool = False,
        limit: Optional[int] = None
    ):
        """
        Add curated organism data to recipe files.

        Args:
            yaml_dir: Directory containing YAML files
            organism_file: Path to organism_candidates.json
            dry_run: If True, only show what would be done
            limit: Optional limit for testing
        """
        if not organism_file.exists():
            logger.warning(f"Organism data file not found: {organism_file}")
            return

        with open(organism_file, 'r') as f:
            organisms = json.load(f)

        logger.info(f"Applying organism data from {len(organisms)} entries...")

        count = 0
        skipped_invalid = 0
        for filepath, org_data in organisms.items():
            if limit and count >= limit:
                break

            # Skip invalid organism names
            organism_name = org_data.get("organism_name", "")
            if not organism_name or organism_name in ["Strain", "Medium", "Agar", "Broth"]:
                skipped_invalid += 1
                continue

            # Find the actual file (filepath in JSON may be relative)
            yaml_file = Path(filepath)
            if not yaml_file.exists():
                # Try as relative to yaml_dir
                yaml_file = yaml_dir / filepath
                if not yaml_file.exists():
                    # Try just the filename
                    yaml_file = yaml_dir / Path(filepath).name
                    if not yaml_file.exists():
                        continue

            if dry_run:
                logger.info(f"  Would add organism data to {yaml_file.name}")
                count += 1
                continue

            try:
                with open(yaml_file, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)

                # Check if already has target_organisms
                if data.get("target_organisms"):
                    logger.debug(f"  {yaml_file.name} already has organism data")
                    continue

                # Add organism culture type
                culture_type = org_data.get("culture_type")
                if culture_type:
                    data["organism_culture_type"] = culture_type

                # Add target organisms
                organism_name = org_data.get("organism_name")
                if organism_name:
                    organism_entry = {
                        "preferred_term": organism_name
                    }

                    # Add NCBI taxon ID if available
                    ncbi_id = org_data.get("ncbi_taxon_id")
                    if ncbi_id:
                        organism_entry["term"] = {
                            "id": f"NCBITaxon:{ncbi_id}",
                            "label": organism_name
                        }

                    # Add strain if available
                    strain = org_data.get("strain")
                    if strain:
                        organism_entry["strain"] = strain

                    data["target_organisms"] = [organism_entry]

                # Add to curation history
                if "curation_history" not in data:
                    data["curation_history"] = []

                data["curation_history"].append({
                    "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S.000000Z", time.gmtime()),
                    "curator": "organism-data-backfill",
                    "action": "Added curated organism data",
                    "notes": f"Added organism: {organism_name}, culture_type: {culture_type}"
                })

                # Save updated file
                with open(yaml_file, 'w', encoding='utf-8') as f:
                    yaml.dump(data, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

                logger.info(f"  ✓ Added organism data to {yaml_file.name}")
                self.stats["organism_data_added"] += 1
                count += 1

            except Exception as e:
                logger.error(f"  ✗ Failed to update {yaml_file.name}: {e}")
                self.stats["errors"] += 1

        if skipped_invalid > 0:
            logger.info(f"  Skipped {skipped_invalid} entries with invalid organism names")

    def run_full_pipeline(
        self,
        yaml_dir: Path,
        atcc_crossref_file: Optional[Path] = None,
        organism_file: Optional[Path] = None,
        dry_run: bool = False
    ):
        """
        Run complete enrichment backfill pipeline.

        Args:
            yaml_dir: Directory containing YAML files
            atcc_crossref_file: Path to ATCC cross-references
            organism_file: Path to organism curation data
            dry_run: If True, only show what would be done
        """
        logger.info("=" * 60)
        logger.info("Enrichment Backfill Pipeline")
        logger.info("=" * 60)
        if dry_run:
            logger.info("DRY RUN MODE - no files will be modified")
        logger.info("")

        # Step 1: ATCC cross-references
        if atcc_crossref_file:
            logger.info("[1/2] Applying ATCC cross-references...")
            self.apply_atcc_crossrefs(yaml_dir, atcc_crossref_file, dry_run)
        else:
            logger.info("[1/2] Skipping ATCC cross-references (no file provided)")

        # Step 2: Organism data
        if organism_file:
            logger.info("\n[2/2] Applying organism data...")
            self.apply_organism_data(yaml_dir, organism_file, dry_run)
        else:
            logger.info("\n[2/2] Skipping organism data (no file provided)")

        # Print summary
        logger.info("\n" + "=" * 60)
        logger.info("Backfill Complete")
        logger.info("=" * 60)
        logger.info(f"ATCC cross-references added: {self.stats['atcc_refs_added']}")
        logger.info(f"Organism data added: {self.stats['organism_data_added']}")
        if self.stats['errors'] > 0:
            logger.warning(f"Errors: {self.stats['errors']}")
        logger.info("=" * 60)


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Systematic enrichment backfill pipeline"
    )
    parser.add_argument(
        "yaml_dir",
        type=Path,
        help="Directory containing YAML files to enrich"
    )
    parser.add_argument(
        "--atcc-crossrefs",
        type=Path,
        default=Path("data/raw/atcc/atcc_crossref.json"),
        help="ATCC cross-reference file"
    )
    parser.add_argument(
        "--organism-data",
        type=Path,
        default=Path("data/curation/organism_candidates.json"),
        help="Organism curation data file"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be done without modifying files"
    )

    args = parser.parse_args()

    pipeline = EnrichmentBackfillPipeline()
    pipeline.run_full_pipeline(
        args.yaml_dir,
        atcc_crossref_file=args.atcc_crossrefs if args.atcc_crossrefs.exists() else None,
        organism_file=args.organism_data if args.organism_data.exists() else None,
        dry_run=args.dry_run
    )


if __name__ == "__main__":
    main()
