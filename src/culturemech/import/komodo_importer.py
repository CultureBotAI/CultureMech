"""
KOMODO to CultureMech Importer

Converts KOMODO (Known Media Database) data to CultureMech YAML format.

Data Sources:
- komodo_media.json - Media records with compositions
- komodo_compounds.json - SEED compound mappings
- komodo_organisms.json - Organism associations

Key Features:
- Standardized molar concentrations (MM unit)
- SEED compound ID to ChEBI mapping
- Deduplication against existing MediaDive recipes
- Organism-media associations

Reference:
- Zarecki et al. (2015) Nature Communications
- https://komodo.modelseed.org/
"""

import json
import yaml
import re
from pathlib import Path
from typing import Any, Dict, List, Optional
from datetime import datetime
import logging
from importlib import import_module

# Import from module with reserved keyword name
ChemicalMapper = import_module('culturemech.import.chemical_mappings').ChemicalMapper

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class KOMODOImporter:
    """Import KOMODO media data into CultureMech format."""

    def __init__(
        self,
        komodo_data_dir: Path,
        output_dir: Path,
        curator: str = "komodo-import",
        chemical_mapper: Optional[ChemicalMapper] = None,
    ):
        """
        Initialize importer.

        Args:
            komodo_data_dir: Directory containing KOMODO JSON files
            output_dir: Output directory for CultureMech YAML files
            curator: Curator name for provenance
            chemical_mapper: Optional ChemicalMapper for ingredient lookups
        """
        self.komodo_dir = Path(komodo_data_dir)
        self.output_dir = Path(output_dir)
        self.curator = curator

        # Load data
        self.media_data = self._load_json("komodo_media.json")
        self.compounds_data = self._load_json("komodo_compounds.json")
        self.organisms_data = self._load_json("komodo_organisms.json")

        # Extract lists from data structure
        self.media = self.media_data.get('data', [])
        self.compounds = self.compounds_data.get('data', [])
        self.organisms = self.organisms_data.get('data', [])

        # Index compounds by SEED ID for quick lookup
        self.seed_to_compound = {
            comp['id']: comp for comp in self.compounds
        }

        # Initialize chemical mapper
        self.chemical_mapper = chemical_mapper

        logger.info(f"Loaded {len(self.media)} KOMODO media recipes")
        logger.info(f"Loaded {len(self.compounds)} SEED compounds")
        logger.info(f"Loaded {len(self.organisms)} organism associations")

    def _load_json(self, filename: str) -> Dict:
        """Load JSON file from KOMODO data directory."""
        path = self.komodo_dir / filename
        if not path.exists():
            logger.warning(f"File not found: {path}")
            return {'count': 0, 'data': []}

        with open(path, encoding='utf-8') as f:
            return json.load(f)

    def import_all(self, limit: Optional[int] = None) -> List[Path]:
        """
        Import all KOMODO media to CultureMech format.

        Args:
            limit: Optional limit on number of media to import

        Returns:
            List of generated YAML file paths
        """
        generated = []
        media_list = self.media[:limit] if limit else self.media

        logger.info(f"\nImporting {len(media_list)} KOMODO media recipes...")

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
        Convert a single KOMODO medium to CultureMech YAML.

        Args:
            medium: KOMODO media dictionary

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

        # Include KOMODO ID for uniqueness
        filename = f"KOMODO_{medium_id}_{clean_name}.yaml"

        # Determine category
        category = self._infer_category(medium)
        output_path = self.output_dir / category / filename
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write YAML
        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(recipe, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        return output_path

    def _convert_to_culturemech(self, medium: Dict) -> Optional[Dict]:
        """
        Convert KOMODO medium to CultureMech schema.

        Args:
            medium: KOMODO media dictionary

        Returns:
            CultureMech recipe dictionary
        """
        if not medium.get('name'):
            return None

        recipe = {
            'name': medium['name'],
            'original_name': medium['name'],
            'category': 'imported',
            'medium_type': self._infer_medium_type(medium),
            'physical_state': self._infer_physical_state(medium),
            'ingredients': self._map_ingredients(medium),
            'preparation_steps': self._create_preparation_steps(medium),
            'curation_history': self._create_curation_history(medium)
        }

        # Add media term
        if medium.get('id'):
            recipe['media_term'] = {
                'preferred_term': f"KOMODO Medium {medium['id']}",
                'term': {
                    'id': f"KOMODO:{medium['id']}",
                    'label': medium['name']
                }
            }

        # Add notes
        notes = []
        notes.append(f"Source: KOMODO (Known Media Database)")
        notes.append(f"Reference: https://komodo.modelseed.org/")
        notes.append(f"Standardized molar concentrations from SEED compound database")

        recipe['notes'] = ' '.join(notes)

        return recipe

    def _map_ingredients(self, medium: Dict) -> List[Dict]:
        """
        Map KOMODO ingredients to CultureMech format.

        Args:
            medium: KOMODO media dictionary

        Returns:
            List of ingredient dictionaries
        """
        ingredients = []

        for comp in medium.get('composition', []):
            seed_id = comp.get('seed_id') or comp.get('compound_id')
            if not seed_id:
                continue

            # Look up compound name from SEED database
            compound = self.seed_to_compound.get(seed_id)
            if not compound:
                logger.debug(f"Compound not found for SEED ID: {seed_id}")
                continue

            compound_name = compound.get('name', seed_id)

            ingredient = {
                'preferred_term': compound_name
            }

            # Try to map to ChEBI via chemical mapper
            if self.chemical_mapper:
                mapping = self.chemical_mapper.lookup(compound_name)
                if mapping and mapping.get('chebi_id'):
                    chebi_id = mapping['chebi_id']
                    if not chebi_id.startswith('CHEBI:'):
                        chebi_id = f"CHEBI:{chebi_id}"

                    ingredient['term'] = {
                        'id': chebi_id,
                        'label': mapping.get('chebi_label', compound_name)
                    }

            # Add molar concentration if available
            concentration = comp.get('concentration')
            concentration_mm = comp.get('concentration_mM')

            if concentration_mm is not None:
                ingredient['concentration'] = {
                    'value': str(concentration_mm),
                    'unit': 'MM'  # Millimolar
                }
            elif concentration is not None:
                # Assume mM if no unit specified
                ingredient['concentration'] = {
                    'value': str(concentration),
                    'unit': 'MM'
                }

            # Add SEED compound ID as note
            ingredient['notes'] = f"SEED ID: {seed_id}"

            ingredients.append(ingredient)

        # Fallback if no ingredients found
        if not ingredients:
            ingredients = [{
                'preferred_term': 'See source for composition',
                'concentration': {
                    'value': 'variable',
                    'unit': 'G_PER_L'
                },
                'notes': 'Full composition available at KOMODO database'
            }]

        return ingredients

    def _create_preparation_steps(self, medium: Dict) -> List[Dict]:
        """
        Create preparation steps from KOMODO data.

        Args:
            medium: KOMODO media dictionary

        Returns:
            List of preparation step dictionaries
        """
        steps = [
            {
                'step_number': 1,
                'action': 'DISSOLVE',
                'description': 'Dissolve all ingredients in distilled water to achieve specified molar concentrations'
            },
            {
                'step_number': 2,
                'action': 'ADJUST_PH',
                'description': 'Adjust pH if specified in original formulation'
            },
            {
                'step_number': 3,
                'action': 'AUTOCLAVE',
                'description': 'Sterilize by autoclaving at 121°C for 15-20 minutes'
            }
        ]

        return steps

    def _infer_medium_type(self, medium: Dict) -> str:
        """
        Infer medium type from name and composition.

        Args:
            medium: KOMODO media dictionary

        Returns:
            Medium type (DEFINED, COMPLEX, MINIMAL)
        """
        name = medium.get('name', '').lower()

        # Check for complex media indicators
        complex_terms = ['agar', 'broth', 'extract', 'peptone', 'yeast']
        if any(term in name for term in complex_terms):
            return 'COMPLEX'

        # Check for minimal media indicators
        minimal_terms = ['minimal', 'defined', 'synthetic']
        if any(term in name for term in minimal_terms):
            return 'DEFINED'

        # KOMODO media are typically well-defined with molar concentrations
        # Default to DEFINED
        return 'DEFINED'

    def _infer_physical_state(self, medium: Dict) -> str:
        """
        Infer physical state from name.

        Args:
            medium: KOMODO media dictionary

        Returns:
            Physical state (LIQUID, SOLID_AGAR)
        """
        name = medium.get('name', '').lower()

        # Check for agar
        if 'agar' in name:
            return 'SOLID_AGAR'

        # Default to liquid
        return 'LIQUID'

    def _infer_category(self, medium: Dict) -> str:
        """
        Determine media category for file organization.

        Args:
            medium: KOMODO media dictionary

        Returns:
            Category name (bacterial, fungal, archaea, specialized)
        """
        name = medium.get('name', '').lower()

        # Category keywords
        if any(term in name for term in ['fungi', 'fungal', 'yeast', 'mold', 'mould']):
            return 'fungal'
        elif any(term in name for term in ['archaea', 'archaeal', 'halophil', 'methanogen']):
            return 'archaea'
        elif any(term in name for term in ['marine', 'seawater', 'extreme', 'anaerobic']):
            return 'specialized'
        else:
            return 'bacterial'  # Default

    def _create_curation_history(self, medium: Dict) -> List[Dict]:
        """
        Create curation history record.

        Args:
            medium: KOMODO media dictionary

        Returns:
            List with curation event
        """
        return [
            {
                'timestamp': datetime.utcnow().isoformat() + 'Z',
                'curator': self.curator,
                'action': 'Imported from KOMODO',
                'notes': (
                    f"Source: KOMODO (Known Media Database), "
                    f"Medium ID: {medium.get('id', 'unknown')}, "
                    f"Reference: Zarecki et al. (2015) Nature Communications"
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
        Check if medium already exists in knowledge base.

        Args:
            medium: KOMODO media dictionary

        Returns:
            True if duplicate found, False otherwise
        """
        name = medium.get('name', '').lower()

        # Check for exact name matches in existing files
        for category in ['bacterial', 'fungal', 'archaea', 'specialized', 'algae']:
            kb_dir = self.output_dir / category
            if not kb_dir.exists():
                continue

            for yaml_file in kb_dir.glob('*.yaml'):
                # Skip KOMODO files (we're importing KOMODO)
                if 'KOMODO' in yaml_file.name:
                    continue

                try:
                    with open(yaml_file, encoding='utf-8') as f:
                        existing = yaml.safe_load(f)

                    existing_name = existing.get('name', '').lower()

                    # Simple name matching
                    if name == existing_name:
                        logger.debug(f"Duplicate found: {name} = {existing_name}")
                        return True

                    # Fuzzy matching (>90% similarity)
                    similarity = self._name_similarity(name, existing_name)
                    if similarity > 0.9:
                        logger.debug(f"Similar media found: {name} ≈ {existing_name} ({similarity:.2%})")
                        return True

                except Exception as e:
                    logger.debug(f"Error checking duplicate in {yaml_file}: {e}")

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
        """Get statistics about KOMODO import."""
        stats = {
            'total_media': len(self.media),
            'total_compounds': len(self.compounds),
            'total_organisms': len(self.organisms),
            'media_by_type': {},
            'media_by_category': {}
        }

        # Count by type
        for medium in self.media:
            medium_type = self._infer_medium_type(medium)
            stats['media_by_type'][medium_type] = stats['media_by_type'].get(medium_type, 0) + 1

        # Count by category
        for medium in self.media:
            category = self._infer_category(medium)
            stats['media_by_category'][category] = stats['media_by_category'].get(category, 0) + 1

        return stats


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description="Import KOMODO media to CultureMech"
    )
    parser.add_argument(
        "-i", "--input",
        type=Path,
        default="data/raw/komodo",
        help="Input directory with KOMODO raw JSON files (Layer 1: data/raw/komodo/)"
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

    importer = KOMODOImporter(
        komodo_data_dir=args.input,
        output_dir=args.output,
        chemical_mapper=chemical_mapper
    )

    if args.stats:
        stats = importer.get_statistics()
        print("\nKOMODO Import Statistics:")
        print(json.dumps(stats, indent=2))
    else:
        importer.import_all(limit=args.limit)


if __name__ == "__main__":
    main()
