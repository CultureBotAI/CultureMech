"""
BacDive to CultureMech Importer

Converts BacDive cultivation data to CultureMech YAML format.

Data Sources:
- bacdive_cultivation.json - Cultivation datasets for strains
- bacdive_media_refs.json - Unique media extracted from cultivation data
- bacdive_strain_ids.json - All strain IDs (metadata)

Integration Strategy:
- Primary value: Organism→media associations (66,000+ links)
- Secondary value: New media recipes not in MediaDive (~500)
- Many BacDive media reference DSMZ media (overlap with MediaDive)
"""

import json
import yaml
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class BacDiveImporter:
    """Import BacDive cultivation data into CultureMech format."""

    def __init__(
        self,
        raw_data_dir: Path,
        output_dir: Path,
        curator: str = "bacdive-import",
    ):
        """
        Initialize importer.

        Args:
            raw_data_dir: Directory containing BacDive JSON files
            output_dir: Output directory for CultureMech YAML files
            curator: Curator name for provenance
        """
        self.raw_dir = Path(raw_data_dir)
        self.output_dir = Path(output_dir)
        self.curator = curator

        # Load data
        self.cultivation_data = self._load_json("bacdive_cultivation.json")
        self.media_refs = self._load_json("bacdive_media_refs.json")
        self.stats = self._load_json("fetch_stats.json")

        logger.info(f"Loaded {len(self.cultivation_data)} cultivation datasets")
        logger.info(f"Loaded {len(self.media_refs)} unique media references")

    def _load_json(self, filename: str) -> Any:
        """Load JSON file from raw data directory."""
        path = self.raw_dir / filename
        if not path.exists():
            logger.warning(f"File not found: {path}")
            return [] if "cultivation" in filename or "strain" in filename else {}

        with open(path) as f:
            return json.load(f)

    def import_all(self, limit: Optional[int] = None) -> List[Path]:
        """
        Import all BacDive media to CultureMech format.

        Args:
            limit: Optional limit on number of media to import (for testing)

        Returns:
            List of generated YAML file paths
        """
        generated = []
        media_list = list(self.media_refs.items())

        if limit:
            media_list = media_list[:limit]
            logger.info(f"Limiting to {limit} media for testing")

        logger.info(f"\nImporting {len(media_list)} media recipes...")

        for media_id, media_info in media_list:
            try:
                yaml_path = self.import_medium(media_id, media_info)
                if yaml_path:
                    generated.append(yaml_path)
                    logger.info(f"✓ Imported {yaml_path.name}")
            except Exception as e:
                logger.error(f"✗ Error importing {media_id}: {e}")

        logger.info(f"\n✓ Imported {len(generated)}/{len(media_list)} media")
        return generated

    def import_medium(self, media_id: str, media_info: Dict) -> Optional[Path]:
        """
        Convert a single BacDive media reference to CultureMech YAML.

        Args:
            media_id: Media identifier
            media_info: Media information dictionary

        Returns:
            Path to generated YAML file
        """
        # Check if this is a DSMZ media reference
        is_dsmz_ref = media_id.startswith("DSMZ_")

        if is_dsmz_ref:
            # This media likely already exists from MediaDive import
            # Instead of creating new recipe, we should enrich the existing one
            # For now, log and skip (enrichment will be separate step)
            logger.debug(
                f"Skipping {media_id} - DSMZ media "
                "(should exist from MediaDive import)"
            )
            return None

        # Create CultureMech recipe for non-DSMZ media
        recipe = {
            "name": media_info.get("media_name", media_id),
            "original_name": media_info.get("media_name", media_id),
            "category": "imported",
            "description": self._create_description(media_info),
            "medium_type": "COMPLEX",  # Default assumption for unknown media
            "physical_state": "LIQUID",  # Default assumption
            "ingredients": self._create_minimal_ingredients(),
            "preparation_steps": self._extract_preparation_steps(media_info),
            "notes": self._create_notes(media_info),
            "curation_history": self._create_curation_history(media_id, media_info),
        }

        # Determine output category (default to bacterial)
        category = "bacterial"

        # Save to YAML
        output_path = self._get_output_path(recipe, category)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w") as f:
            yaml.dump(recipe, f, default_flow_style=False, sort_keys=False)

        return output_path

    def _create_recipe_id(self, media_id: str) -> str:
        """
        Create CultureMech recipe ID from BacDive media ID.

        Args:
            media_id: BacDive media identifier

        Returns:
            CultureMech-compliant ID
        """
        # Format: BACDIVE_{sanitized_id}
        sanitized = re.sub(r"[^A-Z0-9_]", "_", media_id.upper())
        return f"BACDIVE_{sanitized}"

    def _create_description(self, media_info: Dict) -> str:
        """Create description from media info."""
        parts = [f"Media: {media_info.get('media_name', 'Unknown')}"]

        if media_info.get("growth_temperature"):
            parts.append(f"Growth temperature: {media_info['growth_temperature']}")

        if media_info.get("growth_ph"):
            parts.append(f"pH: {media_info['growth_ph']}")

        return ". ".join(parts) + "."

    def _create_minimal_ingredients(self) -> List[Dict]:
        """Create minimal ingredient entry (BacDive provides references, not full recipes)."""
        return [
            {
                "preferred_term": "See source for composition",
                "concentration": {"value": "variable", "unit": "G_PER_L"},
                "notes": "Full composition available at source database",
            }
        ]

    def _extract_preparation_steps(self, media_info: Dict) -> List[Dict]:
        """
        Extract preparation steps from media info.

        Note: BacDive typically only provides media references,
        not detailed preparation protocols.
        """
        steps = []

        media_name = media_info.get("media_name", "")
        if media_name:
            steps.append(
                {
                    "step_number": 1,
                    "action": "DISSOLVE",
                    "description": f"Prepare {media_name} according to standard protocol",
                }
            )

        return steps

    def _create_notes(self, media_info: Dict) -> str:
        """Create notes from media info including growth conditions."""
        parts = []

        parts.append("Imported from BacDive cultivation data.")
        parts.append("Media reference extracted from strain growth conditions.")

        if media_info.get("growth_temperature"):
            parts.append(f"Growth temperature: {media_info['growth_temperature']}")

        if media_info.get("growth_ph"):
            parts.append(f"pH: {media_info['growth_ph']}")

        if media_info.get("growth_time"):
            parts.append(f"Growth time: {media_info['growth_time']}")

        return " ".join(parts)

    def _create_curation_history(self, media_id: str, media_info: Dict) -> List[Dict]:
        """
        Create curation history record.

        Args:
            media_id: Media identifier
            media_info: Media information

        Returns:
            List with curation event
        """
        return [
            {
                "timestamp": datetime.now().isoformat() + "Z",
                "curator": self.curator,
                "action": "Imported from BacDive",
                "notes": f"Source: BacDive, Media ID: {media_id}",
            }
        ]

    def _get_output_path(self, recipe: Dict, category: str) -> Path:
        """
        Determine output file path.

        Args:
            recipe: Recipe dictionary
            category: Media category (bacterial, fungal, etc.)

        Returns:
            Output file path
        """
        # Sanitize name for filename
        name = recipe['name']
        sanitized = re.sub(r'[^A-Z0-9_]', '_', name.upper())
        filename = f"BACDIVE_{sanitized}.yaml"
        return self.output_dir / category / filename

    def export_organism_media_associations(
        self, output_path: Optional[Path] = None
    ) -> Path:
        """
        Export organism→media associations for enriching existing recipes.

        This is the primary value of BacDive data: linking organisms to media.

        Args:
            output_path: Optional output path (default: processed dir)

        Returns:
            Path to associations file
        """
        if output_path is None:
            output_path = Path("data/processed/bacdive_organism_media.json")

        output_path.parent.mkdir(parents=True, exist_ok=True)

        logger.info("Extracting organism→media associations...")

        associations = []

        for strain in self.cultivation_data:
            organism_name = self._extract_organism_name(strain)
            media_refs = self._extract_media_from_strain(strain)

            for media_ref in media_refs:
                associations.append(
                    {
                        "organism": organism_name,
                        "strain_id": strain.get("BacDive-ID"),
                        "media_name": media_ref.get("media_name"),
                        "media_id": media_ref.get("media_id"),
                        "growth_conditions": {
                            "temperature": media_ref.get("growth_temperature"),
                            "ph": media_ref.get("growth_ph"),
                            "time": media_ref.get("growth_time"),
                        },
                    }
                )

        with open(output_path, "w") as f:
            json.dump(associations, f, indent=2)

        logger.info(f"✓ Exported {len(associations)} organism→media associations")
        logger.info(f"  Saved to: {output_path}")

        return output_path

    def _extract_organism_name(self, strain: Dict) -> str:
        """Extract organism name from strain data."""
        # BacDive structure: taxonomy info in 'Name and taxonomic classification'
        taxonomy = strain.get("Name and taxonomic classification", {})
        if isinstance(taxonomy, dict):
            return taxonomy.get("species", "Unknown organism")
        return "Unknown organism"

    def _extract_media_from_strain(self, strain: Dict) -> List[Dict]:
        """Extract all media references from a strain."""
        media_refs = []

        cult_data = strain.get("culture and growth conditions", {})
        if isinstance(cult_data, list):
            for condition in cult_data:
                media_info = self._extract_media_from_condition(condition)
                if media_info:
                    media_refs.append(media_info)

        return media_refs

    def _extract_media_from_condition(self, condition: Dict) -> Optional[Dict]:
        """Extract media information from cultivation condition."""
        media_name = condition.get("medium", "")
        if not media_name:
            return None

        # Extract DSMZ media number if present
        media_id = None
        if "DSMZ" in media_name or "DSM" in media_name:
            match = re.search(r"(?:DSMZ|DSM)\s*(?:Medium\s*)?(\d+)", media_name)
            if match:
                media_id = f"DSMZ_{match.group(1)}"

        return {
            "media_id": media_id or media_name.replace(" ", "_"),
            "media_name": media_name,
            "growth_temperature": condition.get("temp", ""),
            "growth_ph": condition.get("pH", ""),
            "growth_time": condition.get("time", ""),
        }

    def print_stats(self):
        """Print import statistics."""
        logger.info("\n=== BacDive Import Statistics ===")
        logger.info(f"Fetch date: {self.stats.get('fetch_date', 'Unknown')}")
        logger.info(f"Total strains: {self.stats.get('total_strain_ids', 0)}")
        logger.info(
            f"Strains with cultivation data: "
            f"{self.stats.get('strains_with_cultivation', 0)}"
        )
        logger.info(f"Unique media refs: {self.stats.get('unique_media_refs', 0)}")
        logger.info(
            f"DSMZ media refs: "
            f"{sum(1 for m in self.media_refs if m.startswith('DSMZ_'))}"
        )
        logger.info(
            f"Non-DSMZ media: "
            f"{sum(1 for m in self.media_refs if not m.startswith('DSMZ_'))}"
        )


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Import BacDive media to CultureMech")
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default="raw/bacdive",
        help="Input directory with BacDive raw JSON files (Layer 1: raw/bacdive/)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="normalized_yaml",
        help="Output directory for normalized YAML files (Layer 3: normalized_yaml/)",
    )
    parser.add_argument(
        "-l", "--limit", type=int, help="Limit number of media to import (for testing)"
    )
    parser.add_argument(
        "--stats", action="store_true", help="Print statistics only (no import)"
    )
    parser.add_argument(
        "--export-associations",
        action="store_true",
        help="Export organism→media associations",
    )

    args = parser.parse_args()

    importer = BacDiveImporter(raw_data_dir=args.input, output_dir=args.output)

    if args.stats:
        importer.print_stats()
    elif args.export_associations:
        importer.export_organism_media_associations()
    else:
        importer.import_all(limit=args.limit)


if __name__ == "__main__":
    main()
