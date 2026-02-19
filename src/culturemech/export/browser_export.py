"""
Browser data exporter for CultureMech.

Generates JavaScript data file for the faceted search browser.
Extracts searchable fields and facets from YAML recipes.
"""

import json
import argparse
from pathlib import Path
from typing import Any, Optional
import yaml


class BrowserExporter:
    """Export recipes to browser-friendly JavaScript format."""

    def __init__(self, kb_dir: Path):
        self.kb_dir = Path(kb_dir)
        self.recipes = []

    def load_recipes(self) -> None:
        """Load all recipe YAML files."""
        for recipe_file in self.kb_dir.rglob("*.yaml"):
            try:
                with open(recipe_file) as f:
                    recipe_data = yaml.safe_load(f)
                    # Enrich with metadata
                    recipe_data["_source_file"] = str(recipe_file.relative_to(self.kb_dir))
                    recipe_data["_category"] = recipe_file.parent.name
                    self.recipes.append(recipe_data)
            except Exception as e:
                print(f"Error loading {recipe_file}: {e}")

    def extract_browser_data(self) -> list[dict[str, Any]]:
        """Extract flattened data for browser consumption."""
        browser_data = []

        for recipe in self.recipes:
            item = {
                "name": recipe.get("name", "Unknown"),
                "category": recipe.get("category", recipe.get("_category", "unknown")),
                "description": recipe.get("description", "").strip(),
                "medium_type": recipe.get("medium_type", ""),
                "physical_state": recipe.get("physical_state", ""),

                # Organisms (extract names for faceting)
                "target_organism_names": self._extract_organism_names(recipe),
                "organism_culture_type": recipe.get("organism_culture_type", ""),
                "organism_ids": self._extract_organism_ids(recipe),

                # Ingredients (extract names for faceting)
                "ingredient_names": self._extract_ingredient_names(recipe),

                # Applications
                "applications": recipe.get("applications", []),

                # Sterilization
                "sterilization_method": self._extract_sterilization_method(recipe),

                # Media database
                "media_database": self._extract_media_database(recipe),
                "media_database_id": self._extract_media_database_id(recipe),

                # Counts
                "num_ingredients": len(recipe.get("ingredients", [])),
                "num_solutions": len(recipe.get("solutions", [])),
                "num_preparation_steps": len(recipe.get("preparation_steps", [])),

                # Links
                "source_file": recipe.get("_source_file", ""),
                "html_page": self._sanitize_filename(recipe.get('name', 'Unknown')) + ".html",

                # pH
                "ph_value": recipe.get("ph_value"),
                "ph_range": recipe.get("ph_range", ""),
            }

            browser_data.append(item)

        return browser_data

    def _extract_organism_names(self, recipe: dict) -> list[str]:
        """Extract organism names from target_organisms."""
        names = []
        for org in recipe.get("target_organisms", []):
            preferred_term = org.get("preferred_term")
            if preferred_term:
                names.append(preferred_term)
        return names

    def _extract_organism_ids(self, recipe: dict) -> list[str]:
        """Extract NCBITaxon and GTDB IDs from target_organisms."""
        ids = []
        for org in recipe.get("target_organisms", []):
            term = org.get("term") or {}
            if term.get("id"):
                ids.append(term["id"])
            gtdb = org.get("gtdb_term") or {}
            if gtdb.get("id"):
                ids.append(gtdb["id"])
        return ids

    def _extract_ingredient_names(self, recipe: dict) -> list[str]:
        """Extract ingredient names."""
        names = []
        for ing in recipe.get("ingredients", []):
            preferred_term = ing.get("preferred_term")
            if preferred_term:
                names.append(preferred_term)
        return names

    def _extract_sterilization_method(self, recipe: dict) -> Optional[str]:
        """Extract sterilization method."""
        sterilization = recipe.get("sterilization")
        if sterilization and isinstance(sterilization, dict):
            return sterilization.get("method")
        return None

    def _extract_media_database(self, recipe: dict) -> Optional[str]:
        """Extract media database source (DSMZ, TOGO, etc.)."""
        media_term = recipe.get("media_term", {})
        if isinstance(media_term, dict):
            term = media_term.get("term", {})
            if isinstance(term, dict):
                term_id = term.get("id", "")
                if ":" in term_id:
                    return term_id.split(":")[0]
        return None

    def _extract_media_database_id(self, recipe: dict) -> Optional[str]:
        """Extract full media database ID."""
        media_term = recipe.get("media_term", {})
        if isinstance(media_term, dict):
            term = media_term.get("term", {})
            if isinstance(term, dict):
                return term.get("id")
        return None

    def _sanitize_filename(self, name: str) -> str:
        """Sanitize filename for filesystem compatibility."""
        import re
        sanitized = name.replace(' ', '_')
        sanitized = re.sub(r'[/\\:*?"<>|,\']', '_', sanitized)
        sanitized = re.sub(r'_+', '_', sanitized)
        sanitized = sanitized.strip('_')
        return sanitized

    def export(self, output_path: Path) -> None:
        """Export to JavaScript data file."""
        browser_data = self.extract_browser_data()

        # Generate JavaScript file
        js_content = "// CultureMech Browser Data\n"
        js_content += "// Auto-generated - do not edit manually\n\n"
        js_content += f"window.culturemechData = {json.dumps(browser_data, indent=2)};\n\n"
        js_content += "// Dispatch event to notify that data is ready\n"
        js_content += "dispatchEvent(new CustomEvent('culturemechDataReady'));\n"

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(js_content)

        print(f"✓ Exported {len(browser_data)} recipes to {output_path}")


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Export CultureMech recipes to browser data format"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default="data/normalized_yaml",
        help="Input directory containing normalized recipe YAML files (Layer 3)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default="app/data.js",
        help="Output JavaScript file"
    )

    args = parser.parse_args()

    exporter = BrowserExporter(args.input)
    exporter.load_recipes()
    exporter.export(args.output)


if __name__ == "__main__":
    main()
