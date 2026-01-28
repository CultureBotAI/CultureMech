"""
NBRC to CultureMech Importer

Converts NBRC (NITE Biological Resource Center) media data to CultureMech YAML.

Data Sources:
- nbrc_media.json - Scraped media recipes from NBRC website

Integration Strategy:
- Import Japanese BRC media not in TogoMedium
- ~50% overlap with TOGO expected
- ~200 new unique recipes expected
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


class NBRCImporter:
    """Import NBRC media data into CultureMech format."""

    def __init__(
        self,
        raw_data_dir: Path,
        output_dir: Path,
        curator: str = "nbrc-import",
    ):
        """
        Initialize importer.

        Args:
            raw_data_dir: Directory containing NBRC JSON files
            output_dir: Output directory for CultureMech YAML files
            curator: Curator name for provenance
        """
        self.raw_dir = Path(raw_data_dir)
        self.output_dir = Path(output_dir)
        self.curator = curator

        # Load data
        self.media = self._load_json("nbrc_media.json")
        self.stats = self._load_json("scrape_stats.json")

        logger.info(f"Loaded {len(self.media)} NBRC media recipes")

    def _load_json(self, filename: str) -> Any:
        """Load JSON file from raw data directory."""
        path = self.raw_dir / filename
        if not path.exists():
            logger.warning(f"File not found: {path}")
            return [] if "media" in filename else {}

        with open(path, encoding="utf-8") as f:
            return json.load(f)

    def import_all(self, limit: Optional[int] = None) -> List[Path]:
        """
        Import all NBRC media to CultureMech format.

        Args:
            limit: Optional limit on number of media to import

        Returns:
            List of generated YAML file paths
        """
        generated = []
        media_list = self.media[:limit] if limit else self.media

        logger.info(f"\nImporting {len(media_list)} NBRC media recipes...")

        for medium in media_list:
            try:
                yaml_path = self.import_medium(medium)
                if yaml_path:
                    generated.append(yaml_path)
                    logger.info(f"✓ Imported {yaml_path.name}")
            except Exception as e:
                logger.error(
                    f"✗ Error importing {medium.get('media_name', 'Unknown')}: {e}"
                )

        logger.info(f"\n✓ Imported {len(generated)}/{len(media_list)} media")
        return generated

    def import_medium(self, medium: Dict) -> Optional[Path]:
        """
        Convert a single NBRC medium to CultureMech YAML.

        Args:
            medium: NBRC media dictionary

        Returns:
            Path to generated YAML file
        """
        # Create CultureMech recipe
        recipe = {
            "name": medium.get("media_name", "Unknown"),
            "original_name": medium.get("media_name", "Unknown"),
            "category": "imported",
            "description": self._create_description(medium),
            "medium_type": self._infer_medium_type(medium),
            "physical_state": self._infer_physical_state(medium),
            "ingredients": self._map_ingredients(medium),
            "preparation_steps": self._map_preparation_steps(medium),
            "curation_history": self._create_curation_history(medium),
        }

        # Add notes if present
        if medium.get("notes"):
            recipe["notes"] = medium["notes"]

        # Determine output category
        category = self._determine_category(medium)

        # Save to YAML
        output_path = self._get_output_path(recipe, category)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            yaml.dump(recipe, f, default_flow_style=False, sort_keys=False)

        return output_path

    def _create_recipe_id(self, medium: Dict) -> str:
        """Create CultureMech recipe ID from NBRC media."""
        media_number = medium.get("media_number", "")

        # Clean media number (e.g., "No. 802" -> "802")
        number = re.sub(r"[^\d]", "", media_number)

        if number:
            return f"NBRC_{number}"
        else:
            # Fallback: sanitize name
            name = medium.get("media_name", "UNKNOWN")
            sanitized = re.sub(r"[^A-Z0-9]", "_", name.upper())
            return f"NBRC_{sanitized[:30]}"

    def _create_description(self, medium: Dict) -> str:
        """Create description from NBRC media info."""
        parts = []

        media_name = medium.get("media_name", "")
        if media_name:
            parts.append(media_name)

        media_number = medium.get("media_number", "")
        if media_number:
            parts.append(f"NBRC {media_number}")

        if not parts:
            parts.append("NBRC culture medium")

        description = ". ".join(parts) + "."

        return description

    def _infer_medium_type(self, medium: Dict) -> str:
        """
        Infer medium type from name and composition.

        Args:
            medium: NBRC media dictionary

        Returns:
            Medium type (DEFINED, COMPLEX, MINIMAL)
        """
        name = medium.get("media_name", "").lower()
        ingredients = medium.get("ingredients", [])

        # Check for complex media indicators
        complex_terms = ["agar", "broth", "extract", "peptone", "yeast"]
        if any(term in name for term in complex_terms):
            return "COMPLEX"

        # Check ingredients
        complex_ingredients = ["yeast extract", "peptone", "beef extract", "malt"]
        for ing in ingredients:
            ing_name = ing.get("name", "").lower()
            if any(term in ing_name for term in complex_ingredients):
                return "COMPLEX"

        # If all ingredients have chemical formulas, likely defined
        has_formulas = any("(" in ing.get("name", "") for ing in ingredients)
        if has_formulas and len(ingredients) > 0:
            return "DEFINED"

        # Default to complex for unknown
        return "COMPLEX"

    def _infer_physical_state(self, medium: Dict) -> str:
        """
        Infer physical state from ingredients.

        Args:
            medium: NBRC media dictionary

        Returns:
            Physical state (LIQUID, SOLID_AGAR)
        """
        ingredients = medium.get("ingredients", [])

        # Check if agar is present
        for ing in ingredients:
            ing_name = ing.get("name", "").lower()
            if "agar" in ing_name:
                return "SOLID_AGAR"

        # Default to liquid
        return "LIQUID"

    def _map_ingredients(self, medium: Dict) -> List[Dict]:
        """
        Map NBRC ingredients to CultureMech format.

        Args:
            medium: NBRC media dictionary

        Returns:
            List of ingredient dictionaries
        """
        cm_ingredients = []

        for ing in medium.get("ingredients", []):
            ingredient = {"preferred_term": ing.get("name", "")}

            # Map quantity and unit to concentration
            quantity = ing.get("quantity", "")
            unit = ing.get("unit", "")

            if quantity:
                # Map units to standard format
                unit_map = {
                    "g": "G_PER_L",
                    "mg": "MG_PER_L",
                    "ml": "ML_PER_L",
                    "μl": "UL_PER_L",
                    "μg": "UG_PER_L",
                }
                standard_unit = unit_map.get(unit.lower(), "G_PER_L")

                ingredient["concentration"] = {
                    "value": str(quantity),
                    "unit": standard_unit,
                }

            cm_ingredients.append(ingredient)

        return cm_ingredients

    def _map_preparation_steps(self, medium: Dict) -> List[Dict]:
        """
        Map NBRC preparation steps to CultureMech format.

        Args:
            medium: NBRC media dictionary

        Returns:
            List of preparation step dictionaries
        """
        preparation_text = medium.get("preparation", [])

        if not preparation_text:
            # Create basic steps from ingredients
            if medium.get("ingredients"):
                preparation_text = [
                    "Dissolve ingredients in distilled water",
                    "Adjust pH if needed",
                    "Sterilize by autoclaving",
                ]

        # Convert to PreparationStep format
        steps = []
        for i, desc in enumerate(preparation_text, 1):
            # Infer action from description
            action = "DISSOLVE"
            if "autoclave" in desc.lower():
                action = "AUTOCLAVE"
            elif "filter" in desc.lower():
                action = "FILTER_STERILIZE"
            elif "adjust" in desc.lower() or "ph" in desc.lower():
                action = "ADJUST_PH"
            elif "add" in desc.lower():
                action = "ADD"

            steps.append(
                {"step_number": i, "action": action, "description": desc}
            )

        return steps

    def _determine_category(self, medium: Dict) -> str:
        """
        Determine media category for file organization.

        Args:
            medium: NBRC media dictionary

        Returns:
            Category name (bacterial, fungal, etc.)
        """
        name = medium.get("media_name", "").lower()

        # Category keywords
        if any(
            term in name for term in ["fungi", "fungal", "yeast", "mold", "mould"]
        ):
            return "fungal"
        elif any(term in name for term in ["archaea", "archaeal"]):
            return "archaeal"
        elif any(term in name for term in ["marine", "seawater"]):
            return "marine"
        else:
            return "bacterial"  # Default

    def _create_curation_history(self, medium: Dict) -> List[Dict]:
        """
        Create curation history record.

        Args:
            medium: NBRC media dictionary

        Returns:
            List with curation event
        """
        return [
            {
                "timestamp": datetime.now().isoformat() + "Z",
                "curator": self.curator,
                "action": "Imported from NBRC",
                "notes": (
                    f"Source: NBRC, Media No. {medium.get('media_number', '')}, "
                    f"URL: {medium.get('url', '')}. "
                    "Imported via ethical web scraping."
                ),
            }
        ]

    def _get_output_path(self, recipe: Dict, category: str) -> Path:
        """
        Determine output file path.

        Args:
            recipe: Recipe dictionary
            category: Media category

        Returns:
            Output file path
        """
        # Create filename from media number (e.g., "YPG Medium" -> "NBRC_YPG_MEDIUM.yaml")
        name = recipe['name']
        sanitized = re.sub(r'[^A-Z0-9_]', '_', name.upper())
        filename = f"NBRC_{sanitized}.yaml"
        return self.output_dir / category / filename

    def print_stats(self):
        """Print import statistics."""
        logger.info("\n=== NBRC Import Statistics ===")
        logger.info(f"Scrape date: {self.stats.get('scrape_date', 'Unknown')}")
        logger.info(f"Total media: {len(self.media)}")

        # Count by category
        categories = {}
        for medium in self.media:
            cat = self._determine_category(medium)
            categories[cat] = categories.get(cat, 0) + 1

        logger.info("\nBy category:")
        for cat, count in sorted(categories.items()):
            logger.info(f"  {cat}: {count}")


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Import NBRC media to CultureMech")
    parser.add_argument(
        "-i",
        "--input",
        type=Path,
        default="raw/nbrc",
        help="Input directory with NBRC raw JSON files (Layer 1: raw/nbrc/)",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default="normalized_yaml",
        help="Output directory for normalized YAML files (Layer 3: normalized_yaml/)",
    )
    parser.add_argument(
        "-l", "--limit", type=int, help="Limit number of media to import"
    )
    parser.add_argument(
        "--stats", action="store_true", help="Print statistics only (no import)"
    )

    args = parser.parse_args()

    importer = NBRCImporter(raw_data_dir=args.input, output_dir=args.output)

    if args.stats:
        importer.print_stats()
    else:
        importer.import_all(limit=args.limit)


if __name__ == "__main__":
    main()
