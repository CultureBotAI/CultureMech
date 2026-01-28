"""UTEX importer for CultureMech.

Converts UTEX Culture Collection media recipes to CultureMech LinkML YAML format.

UTEX (University of Texas Culture Collection of Algae) provides ~99 algae media recipes
for freshwater and marine organisms.
"""

import argparse
import json
import re
import yaml
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


class UTEXImporter:
    """Import UTEX media data to CultureMech format."""

    def __init__(self, raw_data_dir: Path, output_dir: Path):
        """Initialize importer.

        Args:
            raw_data_dir: Directory containing utex_media.json
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
        """Load UTEX media JSON."""
        media_file = self.raw_data_dir / "utex_media.json"
        if not media_file.exists():
            print(f"✗ Media file not found: {media_file}")
            print(f"  Run: just fetch-utex")
            return []

        with open(media_file) as f:
            data = json.load(f)

        recipes = data.get("recipes", [])
        if not recipes:
            print(f"✗ No recipes found in {media_file}")
            return []

        print(f"Found {len(recipes)} UTEX recipes")
        return recipes

    def _sanitize_filename(self, name: str) -> str:
        """Sanitize filename for filesystem compatibility."""
        # Replace problematic characters with underscore
        safe = re.sub(r'[<>:"/\\|?*\',;()%#&@!\[\]{}]', '_', name)
        # Replace multiple underscores/spaces with single underscore
        safe = re.sub(r'[_\s]+', '_', safe)
        # Remove leading/trailing underscores
        safe = safe.strip('_')
        # Limit length
        if len(safe) > 200:
            safe = safe[:200]
        return safe

    def _determine_salinity_type(self, recipe: Dict) -> str:
        """Determine if media is freshwater, saltwater, or brackish."""
        name = recipe.get('name', '').lower()
        category = recipe.get('category', '').lower()

        # Saltwater indicators
        saltwater_keywords = ['seawater', 'marine', 'f/2', 'f2', 'erdschreiber',
                               'ocean', 'saltwater', 'nacl', 'sea salt']
        if any(kw in name for kw in saltwater_keywords) or category == 'saltwater':
            return 'saltwater'

        # Freshwater indicators
        freshwater_keywords = ['freshwater', 'bold', 'bg-11', 'bg11', 'bristol',
                                'tap', 'soil', 'chu']
        if any(kw in name for kw in freshwater_keywords) or category == 'freshwater':
            return 'freshwater'

        # Default to freshwater for algae
        return 'freshwater'

    def convert_recipe(self, recipe: Dict) -> Dict[str, Any]:
        """Convert UTEX recipe to CultureMech format."""
        utex_id = recipe.get('id', '')
        name = recipe.get('name', 'Unknown Medium')

        # Sanitize filename
        safe_name = self._sanitize_filename(name)

        # Determine salinity
        salinity_type = self._determine_salinity_type(recipe)

        # Build CultureMech recipe
        cm_recipe = {
            'name': name,
            'category': 'algae',
            'medium_type': 'defined' if 'defined' in name.lower() else 'complex',
            'physical_state': 'liquid',  # Most UTEX media are liquid
        }

        # Add description
        desc = recipe.get('description')
        if desc:
            cm_recipe['description'] = desc
        else:
            cm_recipe['description'] = f"Algae culture medium from UTEX Culture Collection. " \
                                         f"Suitable for {salinity_type} algae cultivation."

        # Add ingredients
        ingredients = []
        composition = recipe.get('composition', [])
        for item in composition:
            ingredient_name = item.get('ingredient', '')
            amount = item.get('amount', '')

            # Skip header rows or empty entries
            if not ingredient_name or ingredient_name in ['#', 'Component', 'Ingredient']:
                continue

            ingredient = {
                'agent_term': {
                    'preferred_term': ingredient_name
                }
            }

            # Add amount if present
            if amount and amount not in ['Amount', 'Quantity']:
                ingredient['amount'] = amount

            ingredients.append(ingredient)

        if ingredients:
            cm_recipe['ingredients'] = ingredients

        # Add preparation steps
        prep = recipe.get('preparation')
        if prep:
            # Split preparation into steps
            steps = self._parse_preparation(prep)
            if steps:
                cm_recipe['preparation_steps'] = [{'step_number': i+1, 'instruction': step}
                                                    for i, step in enumerate(steps)]

        # Add notes
        notes = recipe.get('notes')
        if notes:
            cm_recipe['notes'] = notes

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
        cm_recipe['applications'] = ['Algae cultivation', 'Phytoplankton culture',
                                       'Microalgae research']

        # Add curation metadata
        cm_recipe['curation_history'] = [
            {
                'curator': 'utex-import',
                'date': datetime.now(timezone.utc).strftime('%Y-%m-%d'),
                'action': f'Imported from UTEX Culture Collection',
                'notes': f'Source ID: {utex_id}, URL: {recipe.get("url", "")}'
            }
        ]

        # Add cross-references
        xrefs = []
        if utex_id:
            xrefs.append(f"UTEX:{utex_id}")
        if recipe.get('url'):
            xrefs.append(recipe['url'])
        if xrefs:
            cm_recipe['references'] = [{'reference_id': xref} for xref in xrefs]

        return cm_recipe, safe_name

    def _parse_preparation(self, prep_text: str) -> List[str]:
        """Parse preparation text into discrete steps."""
        if not prep_text:
            return []

        # Split by common separators
        steps = []

        # Try numbered lists first (1., 2., etc.)
        numbered = re.split(r'\d+\.\s*', prep_text)
        if len(numbered) > 2:  # Found numbered list
            steps = [s.strip() for s in numbered if s.strip()]
        else:
            # Try sentence splitting
            sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', prep_text)
            steps = [s.strip() for s in sentences if len(s.strip()) > 10]

        # If still no good steps, use whole text as single step
        if not steps:
            steps = [prep_text.strip()]

        return steps[:10]  # Limit to 10 steps

    def import_all(self, limit: Optional[int] = None):
        """Import all UTEX recipes.

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
                output_file = self.algae_dir / f"{filename}.yaml"
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
        print("UTEX Import Summary")
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
        description="Import UTEX media recipes into CultureMech"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default="data/raw/utex",
        help="Input directory with UTEX raw JSON files (Layer 1: data/raw/utex/)"
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
    print("UTEX to CultureMech Importer")
    print("=" * 60)
    print(f"Input:  {args.input}")
    print(f"Output: {args.output}")
    print()

    importer = UTEXImporter(args.input, args.output)

    if args.stats:
        recipes = importer.load_media_data()
        print(f"\nFound {len(recipes)} recipes")
        print("\nRun without --stats to import")
        return

    importer.import_all(limit=args.limit)


if __name__ == "__main__":
    main()
