"""
MediaDB to CultureMech Importer

Converts MediaDB data to CultureMech YAML format.

Data Sources:
- mediadb_media.json - 65 chemically-defined media
- mediadb_compounds.json - Compound mappings (KEGG, BiGG, SEED, ChEBI, PubChem)
- mediadb_organisms.json - Organism associations

Key Features:
- High-quality defined media for model organisms
- Built-in ChEBI IDs (high confidence)
- All media tagged as DEFINED type
- Integration with metabolic modeling databases

Reference:
- Mazumdar et al. (2014) PLOS One
- https://mediadb.systemsbiology.net/
"""

import json
import yaml
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime, timezone
import logging
from importlib import import_module

# Import from module with reserved keyword name
ChemicalMapper = import_module('culturemech.import.chemical_mappings').ChemicalMapper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class MediaDBImporter:
    """Import MediaDB media data into CultureMech format."""

    def __init__(
        self,
        mediadb_data_dir: Path,
        output_dir: Path,
        curator: str = "mediadb-import",
        chemical_mapper: Optional[ChemicalMapper] = None,
    ):
        """
        Initialize importer.

        Args:
            mediadb_data_dir: Directory containing MediaDB JSON files
            output_dir: Output directory for CultureMech YAML files
            curator: Curator name for provenance
            chemical_mapper: Optional ChemicalMapper for ingredient lookups
        """
        self.mediadb_dir = Path(mediadb_data_dir)
        self.output_dir = Path(output_dir)
        self.curator = curator

        # Load data
        self.media_data = self._load_json("mediadb_media.json")
        self.compounds_data = self._load_json("mediadb_compounds.json")
        self.organisms_data = self._load_json("mediadb_organisms.json")

        # Extract lists from data structure
        self.media = self.media_data.get('data', [])
        self.compounds = self.compounds_data.get('data', [])
        self.organisms = self.organisms_data.get('data', [])

        # Index compounds by ID for quick lookup
        self.compounds_by_id = {
            comp['id']: comp for comp in self.compounds
        }

        # Initialize chemical mapper
        self.chemical_mapper = chemical_mapper

        # Cache existing media names for duplicate checking
        self.existing_media_names = self._load_existing_media_names()

        logger.info(f"Loaded {len(self.media)} MediaDB media recipes")
        logger.info(f"Loaded {len(self.compounds)} compounds")
        logger.info(f"Loaded {len(self.organisms)} organism associations")
        logger.info(f"Cached {len(self.existing_media_names)} existing media names for deduplication")

    def _load_json(self, filename: str) -> Dict:
        """Load JSON file from MediaDB data directory."""
        path = self.mediadb_dir / filename
        if not path.exists():
            logger.warning(f"File not found: {path}")
            return {'count': 0, 'data': []}

        with open(path, encoding='utf-8') as f:
            return json.load(f)

    def _load_existing_media_names(self) -> set:
        """Load existing media names from KB for duplicate checking."""
        existing_names = set()

        # Scan all categories
        for category in ['bacterial', 'fungal', 'archaea', 'specialized', 'algae']:
            kb_dir = self.output_dir / category
            if not kb_dir.exists():
                continue

            for yaml_file in kb_dir.glob('*.yaml'):
                # Skip MediaDB files (we're importing MediaDB)
                if 'MEDIADB' in yaml_file.name:
                    continue

                try:
                    with open(yaml_file, encoding='utf-8') as f:
                        existing = yaml.safe_load(f)

                    if existing and 'name' in existing:
                        existing_names.add(existing['name'].lower())
                except Exception as e:
                    logger.debug(f"Error loading {yaml_file}: {e}")

        return existing_names

    def import_all(self, limit: Optional[int] = None) -> List[Path]:
        """
        Import all MediaDB media to CultureMech format.

        Args:
            limit: Optional limit on number of media to import

        Returns:
            List of generated YAML file paths
        """
        generated = []
        media_list = self.media[:limit] if limit else self.media

        logger.info(f"\nImporting {len(media_list)} MediaDB media recipes...")

        duplicates = 0

        for medium in media_list:
            try:
                # Check for duplicates
                if self._check_duplicate(medium):
                    logger.debug(f"⊘ Skipped duplicate: {medium.get('name', 'Unknown')}")
                    duplicates += 1
                    continue

                yaml_path = self.import_medium(medium)
                if yaml_path:
                    generated.append(yaml_path)
                    logger.info(f"✓ Imported {yaml_path.name}")
            except Exception as e:
                logger.error(
                    f"✗ Error importing {medium.get('name', 'Unknown')}: {e}"
                )

        logger.info(f"\n✓ Imported {len(generated)}/{len(media_list)} media")
        logger.info(f"⊘ Skipped {duplicates} duplicates")
        return generated

    def import_medium(self, medium: Dict) -> Optional[Path]:
        """
        Convert a single MediaDB medium to CultureMech YAML.

        Args:
            medium: MediaDB media dictionary

        Returns:
            Path to generated YAML file
        """
        recipe = self._convert_to_culturemech(medium)

        if not recipe:
            return None

        # Generate unique filename
        medium_id = medium.get('id', 'unknown')
        name = recipe['name']

        # Sanitize name for filename
        clean_name = self._sanitize_filename(name)

        # Include MediaDB ID for uniqueness
        filename = f"MEDIADB_{medium_id}_{clean_name}.yaml"

        # Determine category (most MediaDB media are bacterial)
        category = self._infer_category(medium)
        output_path = self.output_dir / category / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write YAML
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(recipe, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        return output_path

    def _convert_to_culturemech(self, medium: Dict) -> Optional[Dict]:
        """
        Convert MediaDB medium to CultureMech schema.

        Args:
            medium: MediaDB media dictionary

        Returns:
            CultureMech recipe dictionary
        """
        if not medium.get('name'):
            return None

        recipe = {
            'name': medium['name'],
            'original_name': medium['name'],
            'category': 'imported',
            'medium_type': 'DEFINED',  # All MediaDB media are chemically defined
            'physical_state': self._infer_physical_state(medium),
            'ingredients': self._map_ingredients(medium),
            'preparation_steps': self._create_preparation_steps(medium),
            'curation_history': self._create_curation_history(medium)
        }

        # Add media term
        if medium.get('id'):
            recipe['media_term'] = {
                'preferred_term': f"MediaDB Medium {medium['id']}",
                'term': {
                    'id': f"MEDIADB:{medium['id']}",
                    'label': medium['name']
                }
            }

        # Add notes with organism associations
        notes = self._create_notes(medium)
        if notes:
            recipe['notes'] = notes

        # Add applications
        recipe['applications'] = [
            'Cultivation of genome-sequenced organisms',
            'Metabolic modeling',
            'Systems biology research'
        ]

        return recipe

    def _map_ingredients(self, medium: Dict) -> List[Dict]:
        """
        Map MediaDB ingredients to CultureMech format.

        Args:
            medium: MediaDB media dictionary

        Returns:
            List of ingredient dictionaries
        """
        ingredients = []

        for comp in medium.get('composition', []):
            compound_id = comp.get('compound_id')
            if not compound_id:
                continue

            # Look up compound details
            compound = self.compounds_by_id.get(compound_id)
            if not compound:
                logger.debug(f"Compound not found for ID: {compound_id}")
                continue

            # MediaDB uses KEGG IDs as 'name' field
            kegg_name = str(compound.get('name', compound_id))
            # The 'chebi_id' field actually contains compound common names, not numeric IDs
            common_name = str(compound.get('chebi_id', kegg_name))

            # Use common name as preferred term
            ingredient = {
                'preferred_term': common_name
            }

            # Try to get ChEBI ID from chemical mapper
            if self.chemical_mapper:
                mapping = self.chemical_mapper.lookup(common_name)
                if mapping and mapping.get('chebi_id'):
                    chebi_id = str(mapping['chebi_id'])
                    if not chebi_id.startswith('CHEBI:'):
                        chebi_id = f"CHEBI:{chebi_id}"

                    ingredient['term'] = {
                        'id': chebi_id,
                        'label': mapping.get('chebi_label', common_name)
                    }

            # Add concentration if available
            concentration = comp.get('concentration')
            unit = comp.get('unit')

            if concentration and unit:
                # Map unit to CultureMech enums
                unit_map = {
                    'g/L': 'G_PER_L',
                    'mg/L': 'MG_PER_L',
                    'ml/L': 'ML_PER_L',
                    'µg/L': 'MICROG_PER_L',
                    'μg/L': 'MICROG_PER_L',
                    'mM': 'MILLIMOLAR',
                    'µM': 'MICROMOLAR',
                    'μM': 'MICROMOLAR',
                    'M': 'MOLAR',
                    '%': 'PERCENT_W_V',
                    'g': 'G_PER_L',
                    'mg': 'MG_PER_L',
                    'ml': 'ML_PER_L',
                }
                standard_unit = unit_map.get(unit, 'G_PER_L')

                ingredient['concentration'] = {
                    'value': str(concentration),
                    'unit': standard_unit
                }

            # Add cross-references as notes
            xrefs = []
            if compound.get('kegg_id'):
                xrefs.append(f"KEGG:{compound['kegg_id']}")
            if compound.get('bigg_id'):
                xrefs.append(f"BiGG:{compound['bigg_id']}")
            if compound.get('seed_id'):
                xrefs.append(f"SEED:{compound['seed_id']}")
            if compound.get('pubchem_id'):
                xrefs.append(f"PubChem:{compound['pubchem_id']}")

            if xrefs:
                ingredient['notes'] = f"Cross-references: {', '.join(xrefs)}"

            ingredients.append(ingredient)

        # Fallback if no ingredients found
        if not ingredients:
            ingredients = [{
                'preferred_term': 'See source for composition',
                'concentration': {
                    'value': 'variable',
                    'unit': 'G_PER_L'
                },
                'notes': 'Full composition available at MediaDB'
            }]

        return ingredients

    def _create_preparation_steps(self, medium: Dict) -> List[Dict]:
        """
        Create preparation steps for defined media.

        Args:
            medium: MediaDB media dictionary

        Returns:
            List of preparation step dictionaries
        """
        steps = [
            {
                'step_number': 1,
                'action': 'DISSOLVE',
                'description': 'Dissolve all ingredients in distilled water to specified concentrations'
            },
            {
                'step_number': 2,
                'action': 'ADJUST_PH',
                'description': 'Adjust pH if specified in original formulation'
            },
            {
                'step_number': 3,
                'action': 'FILTER_STERILIZE',
                'description': 'Sterilize by filtration (0.22 μm) to preserve heat-sensitive components'
            }
        ]

        return steps

    def _infer_physical_state(self, medium: Dict) -> str:
        """
        Infer physical state from name.

        Args:
            medium: MediaDB media dictionary

        Returns:
            Physical state (LIQUID, SOLID_AGAR)
        """
        name = medium.get('name', '').lower()

        # Check for agar
        if 'agar' in name:
            return 'SOLID_AGAR'

        # Default to liquid for defined media
        return 'LIQUID'

    def _infer_category(self, medium: Dict) -> str:
        """
        Determine media category for file organization.

        Args:
            medium: MediaDB media dictionary

        Returns:
            Category name (bacterial, fungal, archaea, specialized)
        """
        name = medium.get('name', '').lower()

        # Category keywords
        if any(term in name for term in ['fungi', 'fungal', 'yeast', 'mold']):
            return 'fungal'
        elif any(term in name for term in ['archaea', 'archaeal']):
            return 'archaea'
        elif any(term in name for term in ['marine', 'seawater']):
            return 'specialized'
        else:
            return 'bacterial'  # Default (most MediaDB media are bacterial)

    def _create_notes(self, medium: Dict) -> str:
        """
        Create notes with organism associations and source info.

        Args:
            medium: MediaDB media dictionary

        Returns:
            Notes string
        """
        notes = []

        notes.append("Source: MediaDB (Chemically-defined media for genome-sequenced organisms)")
        notes.append("Reference: https://mediadb.systemsbiology.net/")

        # Add organism associations if available
        # Note: This would need to be populated during fetch if available
        if medium.get('organisms'):
            org_names = ', '.join(medium['organisms'])
            notes.append(f"Organisms: {org_names}")

        return ' '.join(notes)

    def _create_curation_history(self, medium: Dict) -> List[Dict]:
        """
        Create curation history record.

        Args:
            medium: MediaDB media dictionary

        Returns:
            List with curation event
        """
        return [
            {
                'timestamp': datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                'curator': self.curator,
                'action': 'Imported from MediaDB',
                'notes': (
                    f"Source: MediaDB (Institute for Systems Biology), "
                    f"Medium ID: {medium.get('id', 'unknown')}, "
                    f"Reference: Mazumdar et al. (2014) PLOS One"
                )
            }
        ]

    def _sanitize_filename(self, name: str) -> str:
        """
        Sanitize name for use in filename.

        Args:
            name: Original name

        Returns:
            Sanitized filename-safe string
        """
        # Replace non-alphanumeric characters with underscore
        clean_name = ''
        for char in name:
            if char.isalnum() or char in ['-', '.']:
                clean_name += char
            else:
                clean_name += '_'

        # Collapse multiple underscores
        while '__' in clean_name:
            clean_name = clean_name.replace('__', '_')

        # Remove leading/trailing underscores
        clean_name = clean_name.strip('_')

        # Limit length
        if len(clean_name) > 50:
            clean_name = clean_name[:50]

        return clean_name

    def _check_duplicate(self, medium: Dict) -> bool:
        """
        Check if medium already exists in knowledge base (cached version).

        Args:
            medium: MediaDB media dictionary

        Returns:
            True if duplicate found, False otherwise
        """
        name = medium.get('name', '').lower()

        # Check for exact name match
        if name in self.existing_media_names:
            logger.debug(f"Duplicate found: {name}")
            return True

        # Fuzzy matching (>90% similarity)
        for existing_name in self.existing_media_names:
            similarity = self._name_similarity(name, existing_name)
            if similarity > 0.9:
                logger.debug(f"Similar media found: {name} ≈ {existing_name} ({similarity:.2%})")
                return True

        return False

    def _name_similarity(self, name1: str, name2: str) -> float:
        """
        Calculate similarity between two names using Jaccard index.

        Args:
            name1: First name
            name2: Second name

        Returns:
            Similarity score (0-1)
        """
        # Convert to sets of words
        words1 = set(name1.lower().split())
        words2 = set(name2.lower().split())

        # Jaccard index
        intersection = words1 & words2
        union = words1 | words2

        if not union:
            return 0.0

        return len(intersection) / len(union)

    def get_statistics(self) -> Dict:
        """Get statistics about MediaDB import."""
        stats = {
            'total_media': len(self.media),
            'total_compounds': len(self.compounds),
            'total_organisms': len(self.organisms),
            'media_by_category': {}
        }

        # Count by category
        for medium in self.media:
            category = self._infer_category(medium)
            stats['media_by_category'][category] = stats['media_by_category'].get(category, 0) + 1

        # All MediaDB media are DEFINED
        stats['all_defined'] = True

        return stats


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Import MediaDB media to CultureMech"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default="data/raw/mediadb",
        help="Input directory with MediaDB raw JSON files (Layer 1: data/raw/mediadb/)"
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
        help="Limit number of media to import"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Print statistics only (no import)"
    )
    parser.add_argument(
        "--microbe-media-param",
        type=Path,
        help="Path to MicrobeMediaParam mappings for ChEBI lookup"
    )
    parser.add_argument(
        "--mediadive",
        type=Path,
        help="Path to MediaDive data for ChEBI lookup"
    )

    args = parser.parse_args()

    # Initialize chemical mapper if paths provided
    chemical_mapper = None
    if args.microbe_media_param or args.mediadive:
        chemical_mapper = ChemicalMapper(
            microbe_media_param_dir=args.microbe_media_param,
            mediadive_data_dir=args.mediadive
        )

    importer = MediaDBImporter(
        mediadb_data_dir=args.input,
        output_dir=args.output,
        chemical_mapper=chemical_mapper
    )

    if args.stats:
        stats = importer.get_statistics()
        print("\nMediaDB Import Statistics:")
        print(json.dumps(stats, indent=2))
    else:
        importer.import_all(limit=args.limit)


if __name__ == "__main__":
    main()
