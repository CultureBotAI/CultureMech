"""
ATCC Media importer for CultureMech.

Converts ATCC media data to CultureMech LinkML YAML format.
Handles manually curated JSON and cross-references to existing imports.
"""

import argparse
import json
import re
import yaml
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


class ATCCImporter:
    """Import ATCC media data to CultureMech format."""

    def __init__(self, raw_data_dir: Path, output_dir: Path):
        """
        Initialize importer.

        Args:
            raw_data_dir: Directory containing ATCC JSON files
            output_dir: Root kb/media directory
        """
        self.raw_data_dir = Path(raw_data_dir)
        self.output_dir = Path(output_dir)

        # Create category directories
        self.categories = {
            "bacterial": self.output_dir / "bacterial",
            "fungal": self.output_dir / "fungal",
            "archaea": self.output_dir / "archaea",
            "specialized": self.output_dir / "specialized",
            "algae": self.output_dir / "algae",
        }

        for cat_dir in self.categories.values():
            cat_dir.mkdir(parents=True, exist_ok=True)

        self.stats = {
            "total": 0,
            "success": 0,
            "failed": 0,
            "by_category": {cat: 0 for cat in self.categories.keys()},
            "cross_referenced": 0,
        }

    def load_manual_media(self) -> List[Dict]:
        """Load manually curated ATCC media JSON."""
        media_file = self.raw_data_dir / "atcc_media_manual.json"
        if not media_file.exists():
            print(f"⚠ Manual media file not found: {media_file}")
            return []

        with open(media_file) as f:
            data = json.load(f)

        if isinstance(data, list):
            return data
        return []

    def load_extracted_media(self) -> List[Dict]:
        """Load extracted media from MicroMediaParam."""
        extracted_dir = self.raw_data_dir / "extracted"
        if not extracted_dir.exists():
            return []

        media_list = []
        for json_file in extracted_dir.glob("atcc_*.json"):
            with open(json_file) as f:
                data = json.load(f)
                media_list.append(data)

        return media_list

    def load_crossref_database(self) -> Dict:
        """Load ATCC cross-reference database."""
        crossref_file = self.raw_data_dir / "atcc_crossref.json"
        if not crossref_file.exists():
            return {}

        with open(crossref_file) as f:
            return json.load(f)

    def _sanitize_filename(self, name: str) -> str:
        """Sanitize filename for filesystem compatibility."""
        sanitized = name.replace(" ", "_")
        sanitized = re.sub(r'[/\\:*?"<>|,\']', "_", sanitized)
        sanitized = re.sub(r"_+", "_", sanitized)
        sanitized = sanitized.strip("_")
        return sanitized

    def _infer_category(self, medium: Dict) -> str:
        """
        Infer category from medium name or metadata.

        Args:
            medium: ATCC medium object

        Returns:
            Category name
        """
        name = medium.get("name", "").lower()

        # Fungal keywords
        if any(kw in name for kw in ["yeast", "malt", "potato", "sabouraud"]):
            return "fungal"

        # Archaea keywords
        if any(kw in name for kw in ["halophil", "methanogen", "archae"]):
            return "archaea"

        # Specialized keywords
        if any(kw in name for kw in ["anaerobic", "marine", "extreme"]):
            return "specialized"

        # Default to bacterial
        return "bacterial"

    def _parse_unit(self, unit_str: str) -> str:
        """
        Parse unit string to CultureMech enum value.

        Args:
            unit_str: Unit string (e.g., "g/L", "mg/L")

        Returns:
            CultureMech ConcentrationUnitEnum value
        """
        unit_lower = unit_str.lower().replace(" ", "")

        unit_map = {
            "g/l": "G_PER_L",
            "g": "G_PER_L",
            "mg/l": "MG_PER_L",
            "mg": "MG_PER_L",
            "μg/l": "MICROG_PER_L",
            "mcg/l": "MICROG_PER_L",
            "μg": "MICROG_PER_L",
            "mcg": "MICROG_PER_L",
            "ml/l": "G_PER_L",  # Approximate for solutions
            "ml": "G_PER_L",
            "m": "MOLAR",
            "mm": "MILLIMOLAR",
            "%": "PERCENT_W_V",
        }

        return unit_map.get(unit_lower, "G_PER_L")

    def _convert_manual_to_culturemech(self, medium: Dict) -> Optional[Dict]:
        """
        Convert manually curated ATCC medium to CultureMech schema.

        Args:
            medium: Manual ATCC medium object

        Returns:
            CultureMech recipe dict or None if invalid
        """
        atcc_id = medium.get("atcc_id")
        name = medium.get("name")

        if not name or not atcc_id:
            return None

        # Base recipe
        recipe = {
            "name": name,
            "category": "imported",
            "medium_type": medium.get("medium_type", "COMPLEX"),
            "physical_state": medium.get("physical_state", "LIQUID"),
        }

        # Description
        description = medium.get("description")
        if description:
            recipe["description"] = description

        # pH
        ph = medium.get("ph")
        if ph:
            recipe["ph_value"] = float(ph)

        # Ingredients
        ingredients = []
        for ing in medium.get("ingredients", []):
            ingredient = {"preferred_term": ing["name"]}

            # Concentration
            concentration = ing.get("concentration")
            unit = ing.get("unit", "g/L")
            if concentration:
                ingredient["concentration"] = {
                    "value": str(concentration),
                    "unit": self._parse_unit(unit),
                }

            # ChEBI term if available
            chebi_id = ing.get("chebi_id")
            if chebi_id:
                if not chebi_id.startswith("CHEBI:"):
                    chebi_id = f"CHEBI:{chebi_id}"
                ingredient["term"] = {
                    "id": chebi_id,
                    "label": ing["name"],
                }

            # Notes
            notes = ing.get("notes")
            if notes:
                ingredient["notes"] = notes

            ingredients.append(ingredient)

        recipe["ingredients"] = ingredients

        # Media term (ATCC database reference)
        recipe["media_term"] = {
            "preferred_term": f"ATCC Medium {atcc_id}",
            "term": {"id": f"ATCC:{atcc_id}", "label": name},
        }

        # Notes with source and cross-references
        notes_parts = []
        source = medium.get("source")
        if source:
            notes_parts.append(f"Source: {source}")

        cross_refs = medium.get("cross_references", {})
        if cross_refs:
            refs_str = ", ".join(
                [f"{db.upper()}:{id}" for db, id in cross_refs.items()]
            )
            notes_parts.append(f"Cross-references: {refs_str}")

        extra_notes = medium.get("notes")
        if extra_notes:
            notes_parts.append(extra_notes)

        if notes_parts:
            recipe["notes"] = "\n".join(notes_parts)

        # Applications
        applications = medium.get("applications", [])
        if applications:
            recipe["applications"] = applications
        else:
            recipe["applications"] = ["Microbial cultivation"]

        # Curation history
        recipe["curation_history"] = [
            {
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "curator": "atcc-import",
                "action": "Imported from ATCC data",
                "notes": f"Source: ATCC {atcc_id}",
            }
        ]

        return recipe

    def _convert_extracted_to_culturemech(self, medium: Dict) -> Optional[Dict]:
        """
        Convert MicroMediaParam extracted ATCC medium to CultureMech schema.

        Args:
            medium: Extracted ATCC medium object

        Returns:
            CultureMech recipe dict or None if invalid
        """
        medium_id = medium.get("medium_id", "")
        name = medium.get("medium_name", "Unknown")

        # Extract ATCC ID from medium_id if possible
        atcc_id = medium_id.replace("atcc_", "")

        # Clean up corrupted name (dotted line parsing artifacts)
        if "………" in name:
            # This is corrupted, use ID instead
            name = f"ATCC Medium {atcc_id}"

        # Base recipe
        recipe = {
            "name": name,
            "category": "imported",
            "medium_type": "COMPLEX",  # Default
            "physical_state": "LIQUID",  # Default
        }

        # Ingredients
        ingredients = []
        for comp in medium.get("composition", []):
            ingredient = {"preferred_term": comp.get("name", "Unknown")}

            # Concentration
            concentration = comp.get("concentration")
            unit = comp.get("unit", "g")
            if concentration:
                ingredient["concentration"] = {
                    "value": str(concentration),
                    "unit": self._parse_unit(unit),
                }

            ingredients.append(ingredient)

        if ingredients:
            recipe["ingredients"] = ingredients
        else:
            # Placeholder
            recipe["ingredients"] = [
                {
                    "preferred_term": "See source for composition",
                    "concentration": {"value": "variable", "unit": "G_PER_L"},
                }
            ]

        # Media term
        recipe["media_term"] = {
            "preferred_term": f"ATCC Medium {atcc_id}",
            "term": {"id": f"ATCC:{atcc_id}", "label": name},
        }

        # Notes
        recipe["notes"] = f"Source: MicroMediaParam extraction from ATCC PDF"

        # Applications
        recipe["applications"] = ["Microbial cultivation"]

        # Curation history
        recipe["curation_history"] = [
            {
                "timestamp": datetime.now(timezone.utc)
                .isoformat()
                .replace("+00:00", "Z"),
                "curator": "atcc-import",
                "action": "Imported from MicroMediaParam extraction",
                "notes": f"Source: {medium_id}",
            }
        ]

        return recipe

    def import_all(self, limit: Optional[int] = None) -> Dict:
        """
        Import all ATCC media.

        Args:
            limit: Optional limit on number of media to import

        Returns:
            Statistics dict
        """
        print("=" * 60)
        print("ATCC Media Importer")
        print("=" * 60)

        # Load all data sources
        manual_media = self.load_manual_media()
        extracted_media = self.load_extracted_media()
        crossref_db = self.load_crossref_database()

        print(f"Found {len(manual_media)} manually curated media")
        print(f"Found {len(extracted_media)} extracted media")
        print(f"Found {len(crossref_db)} cross-references")

        all_media = []

        # Process manual media (priority)
        for medium in manual_media:
            medium["_source"] = "manual"
            all_media.append(medium)

        # Process extracted media
        for medium in extracted_media:
            medium["_source"] = "extracted"
            all_media.append(medium)

        self.stats["total"] = len(all_media)
        self.stats["cross_referenced"] = len(crossref_db)

        if limit:
            all_media = all_media[:limit]
            print(f"Limiting to first {limit} media")

        # Import each medium
        for i, medium in enumerate(all_media, 1):
            source = medium.get("_source")
            if source == "manual":
                atcc_id = medium.get("atcc_id", "unknown")
                name = medium.get("name", "Unknown")
            else:
                atcc_id = medium.get("medium_id", "unknown").replace("atcc_", "")
                name = medium.get("medium_name", "Unknown")[:50]

            print(f"[{i}/{len(all_media)}] Importing ATCC {atcc_id}: {name}...", end="")

            try:
                if source == "manual":
                    recipe = self._convert_manual_to_culturemech(medium)
                else:
                    recipe = self._convert_extracted_to_culturemech(medium)

                if not recipe:
                    print(" ✗ (invalid)")
                    self.stats["failed"] += 1
                    continue

                # Determine category
                category = self._infer_category(recipe)
                output_dir = self.categories[category]

                # Generate filename
                filename = self._sanitize_filename(recipe["name"]) + ".yaml"
                output_path = output_dir / filename

                # Write YAML
                with open(output_path, "w") as f:
                    yaml.dump(
                        recipe,
                        f,
                        default_flow_style=False,
                        allow_unicode=True,
                        sort_keys=False,
                    )

                self.stats["success"] += 1
                self.stats["by_category"][category] += 1

                print(f" ✓ ({category})")

            except Exception as e:
                print(f" ✗ Error: {e}")
                self.stats["failed"] += 1

        # Print summary
        print("\n" + "=" * 60)
        print("Import Summary")
        print("=" * 60)
        print(f"Total: {self.stats['total']}")
        print(f"Success: {self.stats['success']}")
        print(f"Failed: {self.stats['failed']}")
        if self.stats["total"] > 0:
            print(
                f"Success rate: {self.stats['success']/self.stats['total']*100:.1f}%"
            )
        print(f"Cross-references available: {self.stats['cross_referenced']}")
        print("\nBy category:")
        for cat, count in self.stats["by_category"].items():
            if count > 0:
                print(f"  {cat:12s}: {count:4d}")
        print("=" * 60)

        return self.stats


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(description="Import ATCC media data to CultureMech")
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default="data/raw/atcc",
        help="Input directory with ATCC raw JSON files (Layer 1: data/raw/atcc/)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="data/normalized_yaml",
        help="Output directory for normalized recipe YAML files (Layer 3: data/normalized_yaml/)",
    )
    parser.add_argument(
        "-l", "--limit", type=int, help="Limit number of media to import (for testing)"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show statistics only (dry run)",
    )

    args = parser.parse_args()

    importer = ATCCImporter(raw_data_dir=args.input, output_dir=args.output)

    if args.stats:
        manual_media = importer.load_manual_media()
        extracted_media = importer.load_extracted_media()
        crossref_db = importer.load_crossref_database()
        print(f"Manually curated media: {len(manual_media)}")
        print(f"Extracted media: {len(extracted_media)}")
        print(f"Cross-references: {len(crossref_db)}")
        print(f"Total media: {len(manual_media) + len(extracted_media)}")
    else:
        importer.import_all(limit=args.limit)


if __name__ == "__main__":
    main()
