"""SAG importer for CultureMech.

Converts SAG (Sammlung von Algenkulturen Göttingen) media recipes to CultureMech LinkML YAML format.

SAG provides ~30 algae media recipes, primarily in PDF format.
"""

import argparse
import json
import re
import yaml
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


class SAGImporter:
    """Import SAG media data to CultureMech format."""

    def __init__(self, raw_data_dir: Path, output_dir: Path):
        """Initialize importer.

        Args:
            raw_data_dir: Directory containing sag_media.json
            output_dir: Root normalized_yaml directory
        """
        self.raw_data_dir = Path(raw_data_dir)
        self.output_dir = Path(output_dir)

        # Create algae category directory
        self.algae_dir = self.output_dir / "algae"
        self.algae_dir.mkdir(parents=True, exist_ok=True)

        self.stats = {
            "total": 0,
            "success": 0,
            "failed": 0,
            "by_category": {"algae": 0},
        }

    def load_media_data(self) -> List[Dict]:
        """Load SAG media JSON."""
        media_file = self.raw_data_dir / "sag_media.json"
        if not media_file.exists():
            print(f"✗ Media file not found: {media_file}")
            print(f"  Run: just fetch-sag")
            return []

        with open(media_file) as f:
            data = json.load(f)

        recipes = data.get("recipes", [])
        if not recipes:
            print(f"✗ No recipes found in {media_file}")
            return []

        print(f"Found {len(recipes)} SAG recipes")
        return recipes

    def _sanitize_filename(self, name: str) -> str:
        """Sanitize filename for filesystem compatibility."""
        # Replace problematic characters with underscore (including forward slash!)
        safe = re.sub(r'[<>:"/\\|?*,;()%#&@!\[\]{}]', '_', name)
        # Replace multiple underscores/spaces with single underscore
        safe = re.sub(r'[_\\s]+', '_', safe)
        # Remove leading/trailing underscores and dots
        safe = safe.strip('_.')
        # Ensure it's not empty
        if not safe or safe == '_':
            # Use a hash of the original name
            import hashlib
            safe = f"recipe_{hashlib.md5(name.encode()).hexdigest()[:8]}"
        # Limit length
        if len(safe) > 200:
            safe = safe[:200]
        return safe

    def _determine_salinity_type(self, recipe: Dict) -> str:
        """Determine if media is freshwater, saltwater, or brackish."""
        name = recipe.get('name', '').lower()
        recipe_id = recipe.get('id', '').lower()

        # Saltwater indicators
        saltwater_keywords = [
            'seawater', 'marine', 'f/2', 'f2', 'erdschreiber',
            'ocean', 'saltwater', 'sw', 'swes'
        ]
        if any(kw in name for kw in saltwater_keywords):
            return 'saltwater'
        if any(kw in recipe_id for kw in saltwater_keywords):
            return 'saltwater'

        # SAG-specific saltwater media
        saltwater_ids = ['f/2', 'swes', 'diat', 'porph']
        if recipe_id in saltwater_ids:
            return 'saltwater'

        # Freshwater indicators
        freshwater_keywords = [
            'freshwater', 'bold', 'bg 11', 'bg11', 'bristol',
            'tap', 'soil', 'chu', 'mbb+v', '3nbbm'
        ]
        if any(kw in name for kw in freshwater_keywords):
            return 'freshwater'

        # SAG-specific freshwater media
        freshwater_ids = ['bg 11', 'b', '3nbbm+v', 'mbb+v']
        if recipe_id in freshwater_ids:
            return 'freshwater'

        # Default to freshwater
        return 'freshwater'

    def _expand_sag_name(self, sag_id: str) -> str:
        """Expand SAG abbreviated names to full names."""
        expansions = {
            'BG 11': 'BG-11 Medium',
            'bg 11': 'BG-11 Medium',
            '3NBBM+V': '3N Bold Basal Medium with Vitamins',
            'f/2': 'f/2 Medium',
            'B': 'Bold\'s Basal Medium',
            'Diat': 'Diatom Medium',
            'SWES': 'Seawater Enriched with Soil Extract',
            'MBB+V': 'Modified Bold\'s Basal Medium with Vitamins',
            'Spirul': 'Spirulina Medium',
            'WC': 'Woods Hole MBL Medium',
            'Porph': 'Porphyridium Medium',
            'Pol': 'Polytoma Medium',
            'Ochr': 'Ochromonas Medium',
            'Chilo': 'Chilomonas Medium',
        }

        return expansions.get(sag_id, sag_id)

    def convert_recipe(self, recipe: Dict) -> Dict[str, Any]:
        """Convert SAG recipe to CultureMech format."""
        sag_id = recipe.get('id', '')
        name = recipe.get('name', sag_id)

        # Expand abbreviated name
        expanded_name = self._expand_sag_name(sag_id) if sag_id else name

        # Sanitize filename
        safe_name = self._sanitize_filename(expanded_name)
        if not safe_name or safe_name == '_':
            safe_name = sag_id.replace('/', '_').replace(':', '_')

        # Determine salinity
        salinity_type = self._determine_salinity_type(recipe)

        # Build CultureMech recipe
        cm_recipe = {
            'name': expanded_name,
            'category': 'algae',
            'medium_type': 'complex',  # Most SAG media are complex
            'physical_state': 'liquid',
        }

        # Add description
        desc_parts = []
        desc_parts.append(f"Algae culture medium from SAG Culture Collection (Göttingen)")
        desc_parts.append(f"Suitable for {salinity_type} algae cultivation")

        # Add format note
        pdf_url = recipe.get('pdf_url', '')
        if pdf_url:
            desc_parts.append(f"Recipe available in PDF format")

        cm_recipe['description'] = '. '.join(desc_parts) + '.'

        # Add PDF text if available
        pdf_text = recipe.get('pdf_text')
        if pdf_text and len(pdf_text.strip()) > 50:
            # Try to extract ingredients from PDF text
            ingredients = self._extract_ingredients_from_text(pdf_text)
            if ingredients:
                cm_recipe['ingredients'] = ingredients

            # Try to extract preparation steps
            prep_steps = self._extract_preparation_from_text(pdf_text)
            if prep_steps:
                cm_recipe['preparation_steps'] = prep_steps

            # Store full PDF text in notes
            cm_recipe['notes'] = f"PDF content: {pdf_text[:1000]}"  # First 1000 chars

        # If no ingredients extracted, add placeholder
        if 'ingredients' not in cm_recipe:
            cm_recipe['notes'] = f"Full recipe available at {pdf_url}" if pdf_url else "Recipe details in PDF format"

        # Add salinity info for marine media
        if salinity_type == 'saltwater':
            cm_recipe['salinity'] = 'marine (natural seawater or artificial seawater)'
        elif salinity_type == 'brackish':
            cm_recipe['salinity'] = 'brackish (reduced seawater concentration)'

        # Add light recommendations (typical for algae)
        cm_recipe['light_intensity'] = 'Varies by species; typically 50-100 µmol photons m⁻² s⁻¹'
        cm_recipe['light_cycle'] = 'Varies by species; commonly 12:12 or 16:8 light:dark'

        # Add temperature (typical for algae)
        cm_recipe['temperature_range'] = '15-30°C depending on species'

        # Add applications
        cm_recipe['applications'] = [
            'Algae cultivation',
            'Phytoplankton culture',
            'Microalgae research'
        ]

        # Add curation metadata
        cm_recipe['curation_history'] = [
            {
                'curator': 'sag-import',
                'date': datetime.now(timezone.utc).strftime('%Y-%m-%d'),
                'action': f'Imported from SAG Culture Collection',
                'notes': f'Source ID: {sag_id}, PDF URL: {pdf_url}'
            }
        ]

        # Add cross-references
        xrefs = []
        if sag_id:
            xrefs.append(f"SAG:{sag_id}")
        if pdf_url:
            xrefs.append(pdf_url)
        if xrefs:
            cm_recipe['references'] = [{'reference_id': xref} for xref in xrefs]

        return cm_recipe, safe_name

    def _extract_ingredients_from_text(self, text: str) -> List[Dict]:
        """Try to extract ingredients from PDF text."""
        ingredients = []

        # Look for common ingredient patterns
        lines = text.split('\n')
        in_ingredients_section = False

        for line in lines:
            # Look for section headers
            if re.search(r'(ingredient|component|composition|stock solution)', line, re.I):
                in_ingredients_section = True
                continue

            if in_ingredients_section:
                # Look for lines with chemical formulas and amounts
                match = re.search(r'([A-Z][a-z]?[A-Z0-9().·•]+)\s+([\d.]+\s*[a-zA-Z/]+)', line)
                if match:
                    ingredient_name = match.group(1)
                    amount = match.group(2)
                    ingredients.append({
                        'agent_term': {'preferred_term': ingredient_name},
                        'amount': amount
                    })

                # Stop if we hit a new section
                if re.search(r'(preparation|method|note|reference)', line, re.I):
                    break

        return ingredients[:20]  # Limit to 20 ingredients

    def _extract_preparation_from_text(self, text: str) -> List[Dict]:
        """Try to extract preparation steps from PDF text."""
        steps = []

        lines = text.split('\n')
        in_prep_section = False
        step_num = 1

        for line in lines:
            # Look for preparation section
            if re.search(r'(preparation|method|procedure|protocol)', line, re.I):
                in_prep_section = True
                continue

            if in_prep_section and line.strip():
                # Add as a step if it looks like an instruction
                if len(line.strip()) > 20 and not line.strip().startswith('#'):
                    steps.append({
                        'step_number': step_num,
                        'instruction': line.strip()
                    })
                    step_num += 1

                # Stop after reasonable number of steps
                if step_num > 10:
                    break

        return steps

    def import_all(self, limit: Optional[int] = None):
        """Import all SAG recipes.

        Args:
            limit: Optional limit on number of recipes to import
        """
        recipes = self.load_media_data()
        if not recipes:
            return

        if limit:
            recipes = recipes[:limit]
            print(f"Limiting import to {limit} recipes")

        self.stats['total'] = len(recipes)

        for idx, recipe in enumerate(recipes, 1):
            try:
                print(f"[{idx}/{len(recipes)}] Importing: {recipe.get('name', 'Unknown')}")

                cm_recipe, filename = self.convert_recipe(recipe)

                # Write YAML file
                output_file = self.algae_dir / f"SAG_{filename}.yaml"
                with open(output_file, 'w') as f:
                    yaml.dump(cm_recipe, f, default_flow_style=False, sort_keys=False,
                              allow_unicode=True)

                self.stats['success'] += 1
                self.stats['by_category']['algae'] += 1

            except Exception as e:
                print(f"  ✗ Error: {e}")
                self.stats['failed'] += 1

        self.print_summary()

    def print_summary(self):
        """Print import statistics."""
        print("\n" + "=" * 60)
        print("SAG Import Summary")
        print("=" * 60)
        print(f"Total recipes:    {self.stats['total']}")
        print(f"Successfully imported: {self.stats['success']}")
        print(f"Failed:          {self.stats['failed']}")
        print(f"\nBy category:")
        for cat, count in self.stats['by_category'].items():
            print(f"  {cat}: {count}")
        print("=" * 60)


def main():
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Import SAG media recipes into CultureMech"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default="data/raw/sag",
        help="Input directory with SAG raw JSON files (Layer 1: data/raw/sag/)"
    )
    parser.add_argument(
        "-o", "--output",
        type=Path,
        default="data/normalized_yaml",
        help="Output directory for normalized YAML files (Layer 3: data/normalized_yaml/)"
    )
    parser.add_argument(
        "-l", "--limit",
        type=int,
        help="Limit number of media to import (for testing)"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show statistics only (dry run)"
    )

    args = parser.parse_args()

    print("=" * 60)
    print("SAG to CultureMech Importer")
    print("=" * 60)
    print(f"Input:  {args.input}")
    print(f"Output: {args.output}")
    print()

    importer = SAGImporter(args.input, args.output)

    if args.stats:
        recipes = importer.load_media_data()
        print(f"\nFound {len(recipes)} recipes")
        print("\nRun without --stats to import")
        return

    importer.import_all(limit=args.limit)


if __name__ == "__main__":
    main()
