"""
TOGO Medium importer for CultureMech.

Converts TOGO Medium JSON data to CultureMech LinkML YAML format.
"""

import argparse
import json
import re
import yaml
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


class TogoImporter:
    """Import TOGO Medium data to CultureMech format."""

    def __init__(self, raw_data_dir: Path, output_dir: Path):
        """
        Initialize importer.

        Args:
            raw_data_dir: Directory containing togo_media.json
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
            "by_source": {},
        }

    def load_media_data(self) -> List[Dict]:
        """Load TOGO media JSON."""
        media_file = self.raw_data_dir / "togo_media.json"
        if not media_file.exists():
            print(f"✗ Media file not found: {media_file}")
            print(f"  Run: just fetch-togo-raw")
            return []

        with open(media_file) as f:
            data = json.load(f)

        if isinstance(data, list):
            return data
        elif isinstance(data, dict) and "data" in data:
            return data["data"]
        return []

    def _sanitize_filename(self, name: str) -> str:
        """
        Sanitize filename for filesystem compatibility.

        Replaces ALL non-alphanumeric characters (except dash and dot) with underscore.
        This ensures filenames are safe for:
        - All operating systems (Windows, macOS, Linux)
        - Shell commands (no metacharacters)
        - CSV exports (no commas)
        - URLs (URL-safe characters only)

        Problematic characters replaced with '_':
        - Shell metacharacters: / \ : * ? " < > | ' ` ; & $ ! # % @ ^ ~ [ ] { } ( )
        - Separators: , (causes CSV issues)
        - Special symbols: + = (can cause issues in some contexts)
        - Non-ASCII: ° ´ and other accented/special characters
        - Whitespace: space, tab, newline

        Allowed characters: a-z A-Z 0-9 _ - .
        """
        clean_name = ''
        for char in name:
            if char.isalnum() or char in ['-', '.']:
                clean_name += char
            else:
                clean_name += '_'

        # Collapse multiple consecutive underscores
        while '__' in clean_name:
            clean_name = clean_name.replace('__', '_')

        # Remove leading/trailing underscores
        clean_name = clean_name.strip('_')

        return clean_name

    def _infer_category(self, medium: Dict) -> str:
        """
        Infer category from medium name or metadata.

        Args:
            medium: TOGO medium object

        Returns:
            Category name (bacterial/fungal/archaea/specialized/algae)
        """
        name = medium.get("name", "").lower()

        # Fungal keywords
        if any(
            kw in name
            for kw in [
                "yeast",
                "malt",
                "potato dextrose",
                "sabouraud",
                "czapek",
                "fungal",
                "fungi",
            ]
        ):
            return "fungal"

        # Archaea keywords
        if any(
            kw in name
            for kw in ["halophil", "methanogen", "archae", "thermophil", "sulfolobus"]
        ):
            return "archaea"

        # Algae keywords
        if any(
            kw in name for kw in ["algae", "algal", "phyto", "chlorella", "spirulina"]
        ):
            return "algae"

        # Specialized keywords
        if any(
            kw in name
            for kw in [
                "anaerobic",
                "marine",
                "extreme",
                "thermophil",
                "acidophil",
                "alkalophil",
            ]
        ):
            return "specialized"

        # Default to bacterial
        return "bacterial"

    def _extract_source_info(self, medium: Dict) -> Dict[str, str]:
        """
        Extract source information from medium.

        Args:
            medium: TOGO medium object

        Returns:
            Dict with source, original_id, url, gm_id
        """
        meta = medium.get("meta", {})

        # Extract gm_id from URL like "http://togomedium.org/medium/M3006"
        gm_url = meta.get("gm", "")
        gm_id = gm_url.split("/")[-1] if gm_url else ""

        original_id = meta.get("original_media_id", "")
        src_url = meta.get("src_url", "")

        # Extract source from original_media_id (e.g., "JCM_M1331" -> "JCM")
        source = ""
        if original_id and "_" in original_id:
            source = original_id.split("_")[0]

        # Build URL to TOGO page
        url = f"https://togomedium.org/medium/{gm_id}"

        return {
            "source": source or "TOGO",
            "original_id": original_id or gm_id,
            "url": url,
            "gm_id": gm_id,
            "src_url": src_url,
        }

    def _extract_ingredients(self, medium: Dict) -> List[Dict]:
        """
        Extract ingredients from medium.

        Args:
            medium: TOGO medium object

        Returns:
            List of ingredient descriptors
        """
        ingredients = []
        components = medium.get("components", [])

        if not components:
            # Placeholder ingredient if no composition
            return [
                {
                    "preferred_term": "See source for composition",
                    "concentration": {"value": "variable", "unit": "G_PER_L"},
                    "notes": "Full composition available at source database",
                }
            ]

        # TOGO has nested structure: components -> items
        for comp_section in components:
            items = comp_section.get("items", [])
            for item in items:
                component_name = item.get("component_name", "Unknown")

                ingredient = {"preferred_term": component_name}

                # Concentration
                volume = item.get("volume")
                unit = item.get("unit", "")
                if volume:
                    # Try to parse unit
                    concentration_unit = self._parse_unit(unit)
                    ingredient["concentration"] = {
                        "value": str(volume),
                        "unit": concentration_unit,
                    }

                # GMO component ID (could potentially map to ChEBI)
                gmo_id = item.get("gmo_id")
                label = item.get("label")

                # For now, we don't have direct ChEBI mappings in TOGO data
                # But we have GMO IDs which are ontology terms

                # Role/notes from TOGO properties and roles
                notes_parts = []

                roles = item.get("roles", [])
                if roles:
                    role_labels = [r.get("label") for r in roles if r.get("label")]
                    if role_labels:
                        notes_parts.append(f"Role: {', '.join(role_labels)}")

                properties = item.get("properties", [])
                if properties:
                    prop_labels = [p.get("label") for p in properties if p.get("label")]
                    if prop_labels:
                        notes_parts.append(f"Properties: {', '.join(prop_labels)}")

                if notes_parts:
                    ingredient["notes"] = "; ".join(notes_parts)

                ingredients.append(ingredient)

        return ingredients if ingredients else [
            {
                "preferred_term": "See source for composition",
                "concentration": {"value": "variable", "unit": "G_PER_L"},
                "notes": "Full composition available at source database",
            }
        ]

    def _parse_unit(self, unit_str: str) -> str:
        """
        Parse unit string to CultureMech enum value.

        Args:
            unit_str: Unit string from TOGO (e.g., "g/L", "mg/L")

        Returns:
            CultureMech ConcentrationUnitEnum value
        """
        unit_lower = unit_str.lower().replace(" ", "")

        unit_map = {
            "g/l": "G_PER_L",
            "g/liter": "G_PER_L",
            "mg/l": "MG_PER_L",
            "mg/liter": "MG_PER_L",
            "μg/l": "MICROG_PER_L",
            "ug/l": "MICROG_PER_L",
            "m": "MOLAR",
            "mm": "MILLIMOLAR",
            "μm": "MICROMOLAR",
            "um": "MICROMOLAR",
            "%w/v": "PERCENT_W_V",
            "%v/v": "PERCENT_V_V",
            "%": "PERCENT_W_V",
        }

        return unit_map.get(unit_lower, "G_PER_L")

    def _extract_ph(self, medium: Dict) -> Dict:
        """
        Extract pH information.

        Args:
            medium: TOGO medium object

        Returns:
            Dict with ph_value or ph_range
        """
        ph_info = {}

        # TOGO may have pH as single value or range
        ph = medium.get("ph")
        if ph is not None:
            if isinstance(ph, (int, float)):
                ph_info["ph_value"] = float(ph)
            elif isinstance(ph, str):
                # Try to parse range like "7.0-7.5"
                if "-" in ph:
                    ph_info["ph_range"] = ph
                else:
                    try:
                        ph_info["ph_value"] = float(ph)
                    except ValueError:
                        pass

        return ph_info

    def _convert_to_culturemech(self, medium: Dict) -> Optional[Dict]:
        """
        Convert TOGO medium to CultureMech schema.

        Args:
            medium: TOGO medium object

        Returns:
            CultureMech recipe dict or None if invalid
        """
        meta = medium.get("meta", {})
        name = meta.get("name")

        if not name:
            return None

        # Extract source info (includes gm_id)
        source_info = self._extract_source_info(medium)
        gm_id = source_info["gm_id"]

        # Base recipe
        recipe = {
            "name": name,
            "original_name": name,  # Store original name with all special characters
            "category": "imported",
            "medium_type": "COMPLEX",  # Default, could be refined
            "physical_state": "LIQUID",  # Default
        }

        # Description (if available)
        description = medium.get("description")
        if description:
            recipe["description"] = description

        # pH (if available)
        ph_info = self._extract_ph(medium)
        recipe.update(ph_info)

        # Ingredients
        ingredients = self._extract_ingredients(medium)
        if ingredients:
            recipe["ingredients"] = ingredients

        # Media term (TOGO database reference)
        recipe["media_term"] = {
            "preferred_term": f"TOGO Medium {gm_id}",
            "term": {"id": f"TOGO:{gm_id}", "label": name},
        }

        # Notes with source info
        notes_parts = [f"Source: {source_info['url']}"]
        if source_info["source"] and source_info["source"] != "TOGO":
            notes_parts.append(
                f"Original source: {source_info['source']} - {source_info['original_id']}"
            )
        if source_info.get("src_url"):
            notes_parts.append(f"Original URL: {source_info['src_url']}")
        recipe["notes"] = "\n".join(notes_parts)

        # Applications
        recipe["applications"] = ["Microbial cultivation"]

        # Curation history
        recipe["curation_history"] = [
            {
                "timestamp": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
                "curator": "togo-import",
                "action": "Imported from TOGO Medium",
                "notes": f"Source: {source_info['source']}, ID: {gm_id}",
            }
        ]

        return recipe

    def import_all(self, limit: Optional[int] = None) -> Dict:
        """
        Import all TOGO media.

        Args:
            limit: Optional limit on number of media to import

        Returns:
            Statistics dict
        """
        print("=" * 60)
        print("TOGO Medium Importer")
        print("=" * 60)

        # Load data
        media_data = self.load_media_data()
        if not media_data:
            print("✗ No media data found")
            return self.stats

        self.stats["total"] = len(media_data)
        print(f"Found {len(media_data)} media in TOGO data")

        if limit:
            media_data = media_data[:limit]
            print(f"Limiting to first {limit} media")

        # Import each medium
        for i, medium in enumerate(media_data, 1):
            meta = medium.get("meta", {})
            name = meta.get("name", "Unknown")

            # Extract gm_id from URL
            gm_url = meta.get("gm", "")
            gm_id = gm_url.split("/")[-1] if gm_url else "unknown"

            print(f"[{i}/{len(media_data)}] Importing {gm_id}: {name[:50]}...", end="")

            try:
                recipe = self._convert_to_culturemech(medium)
                if not recipe:
                    print(" ✗ (invalid)")
                    self.stats["failed"] += 1
                    continue

                # Determine category
                category = self._infer_category(medium)
                output_dir = self.categories[category]

                # Generate unique filename with source and ID
                source_info = self._extract_source_info(medium)
                source = source_info["source"]
                gm_id = source_info["gm_id"]

                # Sanitize name for filename
                clean_name = self._sanitize_filename(name)

                # Include source and ID for uniqueness (like MediaDive format)
                filename = f"TOGO_{gm_id}_{clean_name}.yaml"
                output_path = output_dir / filename

                # Write YAML
                with open(output_path, "w") as f:
                    yaml.dump(
                        recipe, f, default_flow_style=False, allow_unicode=True, sort_keys=False
                    )

                self.stats["success"] += 1
                self.stats["by_category"][category] += 1

                # Track by source
                source = self._extract_source_info(medium)["source"]
                self.stats["by_source"][source] = (
                    self.stats["by_source"].get(source, 0) + 1
                )

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
        print(f"Success rate: {self.stats['success']/self.stats['total']*100:.1f}%")
        print("\nBy category:")
        for cat, count in self.stats["by_category"].items():
            if count > 0:
                print(f"  {cat:12s}: {count:4d}")
        print("\nBy source:")
        for source, count in sorted(
            self.stats["by_source"].items(), key=lambda x: x[1], reverse=True
        ):
            print(f"  {source:12s}: {count:4d}")
        print("=" * 60)

        return self.stats


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Import TOGO Medium data to CultureMech"
    )
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default="data/raw/togo",
        help="Input directory with TOGO raw JSON files (Layer 1: data/raw/togo/)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="data/normalized_yaml",
        help="Output directory for normalized YAML files (Layer 3: data/normalized_yaml/)",
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

    importer = TogoImporter(raw_data_dir=args.input, output_dir=args.output)

    if args.stats:
        media_data = importer.load_media_data()
        print(f"Total media: {len(media_data)}")
        print(f"Raw data: {args.input}")
    else:
        importer.import_all(limit=args.limit)


if __name__ == "__main__":
    main()
