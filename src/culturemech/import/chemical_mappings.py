"""
Chemical Mappings Loader

Loads and provides lookup for chemical/ingredient mappings from:
1. MicrobeMediaParam compound_mappings_strict_final.tsv
2. MicrobeMediaParam compound_mappings_strict_final_hydrate.tsv
3. MediaDive mediadive_ingredients.json

Provides unified interface for retrieving CHEBI terms, formulas, and metadata
for media ingredients across all sources.

Integration:
- MicrobeMediaParam: ~3,000+ ingredient mappings with CHEBI IDs
- MediaDive: 1,235 ingredients with ChEBI, CAS-RN, PubChem IDs
- Merge strategy: Prefer high-confidence MicrobeMediaParam mappings
"""

import csv
import json
from pathlib import Path
from typing import Optional, Dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChemicalMapper:
    """Unified chemical/ingredient mapping lookup."""

    def __init__(
        self,
        microbe_media_param_dir: Optional[Path] = None,
        mediadive_data_dir: Optional[Path] = None
    ):
        """
        Initialize chemical mapper with data sources.

        Args:
            microbe_media_param_dir: Path to MicrobeMediaParam/pipeline_output/merge_mappings/
            mediadive_data_dir: Path to MediaDive JSON files
        """
        self.mappings = {}
        self.sources = {}

        # Load MicrobeMediaParam mappings
        if microbe_media_param_dir:
            self._load_microbe_media_param(microbe_media_param_dir)

        # Load MediaDive ingredients
        if mediadive_data_dir:
            self._load_mediadive_ingredients(mediadive_data_dir)

        logger.info(f"Loaded {len(self.mappings)} chemical mappings")

    def _load_microbe_media_param(self, data_dir: Path):
        """Load MicrobeMediaParam compound mappings."""
        data_dir = Path(data_dir)

        # Try both files
        for filename in [
            "compound_mappings_strict_final.tsv",
            "compound_mappings_strict_final_hydrate.tsv",
            "high_confidence_compound_mappings.tsv"
        ]:
            file_path = data_dir / filename
            if not file_path.exists():
                continue

            logger.info(f"Loading {filename}...")
            with open(file_path) as f:
                reader = csv.DictReader(f, delimiter='\t')
                for row in reader:
                    self._add_mapping_from_microbe_media_param(row)

    def _add_mapping_from_microbe_media_param(self, row: dict):
        """Add mapping from MicrobeMediaParam TSV row."""
        # Normalize ingredient name
        original = row.get('original', '').lower().strip()
        if not original:
            return

        # Build mapping entry
        mapping = {
            'preferred_term': row.get('original'),
            'normalized': row.get('normalized_compound', original),
            'chebi_id': None,
            'chebi_label': None,
            'chebi_formula': None,
            'mapped_name': row.get('mapped'),
            'concentration_unit': row.get('unit'),
            'confidence': row.get('match_confidence'),
            'quality': row.get('mapping_quality'),
            'hydration_state': row.get('hydration_state'),
            'source': 'MicrobeMediaParam'
        }

        # Extract CHEBI ID
        chebi_id = row.get('chebi_id') or row.get('mapped')
        if chebi_id and ('CHEBI:' in chebi_id or 'chebi:' in chebi_id):
            # Extract ID
            if ':' in chebi_id:
                mapping['chebi_id'] = chebi_id.split(':', 1)[1] if not chebi_id.startswith('CHEBI:') else chebi_id
            else:
                mapping['chebi_id'] = f"CHEBI:{chebi_id}"

            mapping['chebi_label'] = row.get('chebi_label')
            mapping['chebi_formula'] = row.get('chebi_formula')

        # For hydrated compounds, prefer hydrated CHEBI
        if row.get('hydrated_chebi_id'):
            mapping['hydrated_chebi_id'] = row['hydrated_chebi_id']
            mapping['hydrated_chebi_label'] = row.get('hydrated_chebi_label')

        # Store mapping (don't overwrite if already exists with higher confidence)
        if original not in self.mappings or self._is_better_mapping(mapping, self.mappings[original]):
            self.mappings[original] = mapping
            self.sources[original] = 'MicrobeMediaParam'

    def _load_mediadive_ingredients(self, data_dir: Path):
        """Load MediaDive ingredient mappings."""
        data_dir = Path(data_dir)
        ingredients_file = data_dir / "mediadive_ingredients.json"

        if not ingredients_file.exists():
            logger.warning(f"MediaDive ingredients not found: {ingredients_file}")
            return

        logger.info("Loading mediadive_ingredients.json...")
        with open(ingredients_file) as f:
            data = json.load(f)

        for ing in data.get('data', []):
            name = ing.get('name', '').lower().strip()
            if not name:
                continue

            # Build mapping entry
            mapping = {
                'preferred_term': ing.get('name'),
                'normalized': name,
                'chebi_id': ing.get('ChEBI'),
                'chebi_label': ing.get('name'),
                'cas_rn': ing.get('CAS-RN'),
                'pubchem_id': ing.get('PubChem'),
                'formula': ing.get('formula'),
                'molecular_weight': ing.get('mass'),
                'source': 'MediaDive'
            }

            # Only add if not already present (prefer MicrobeMediaParam)
            if name not in self.mappings:
                self.mappings[name] = mapping
                self.sources[name] = 'MediaDive'

    def _is_better_mapping(self, new: dict, existing: dict) -> bool:
        """Determine if new mapping is better than existing."""
        # Prefer high confidence over low
        conf_order = {'high': 3, 'medium': 2, 'low': 1, None: 0}
        new_conf = conf_order.get(new.get('confidence'), 0)
        existing_conf = conf_order.get(existing.get('confidence'), 0)

        if new_conf > existing_conf:
            return True

        # If same confidence, prefer one with more data
        new_score = sum([
            bool(new.get('chebi_id')),
            bool(new.get('chebi_formula')),
            bool(new.get('chebi_label')),
        ])
        existing_score = sum([
            bool(existing.get('chebi_id')),
            bool(existing.get('chebi_formula')),
            bool(existing.get('chebi_label')),
        ])

        return new_score > existing_score

    def lookup(self, ingredient_name: str) -> Optional[Dict]:
        """
        Look up chemical mapping for an ingredient.

        Args:
            ingredient_name: Ingredient name (case-insensitive)

        Returns:
            Mapping dict with CHEBI ID, label, formula, etc., or None
        """
        normalized = ingredient_name.lower().strip()
        return self.mappings.get(normalized)

    def get_chebi_term(self, ingredient_name: str) -> Optional[Dict]:
        """
        Get CHEBI term for ingredient suitable for CultureMech schema.

        Returns:
            {
                "id": "CHEBI:17234",
                "label": "D-glucose"
            }
        """
        mapping = self.lookup(ingredient_name)
        if not mapping or not mapping.get('chebi_id'):
            return None

        chebi_id = mapping['chebi_id']
        # Ensure proper CURIE format
        if not chebi_id.startswith('CHEBI:'):
            chebi_id = f"CHEBI:{chebi_id}"

        return {
            'id': chebi_id,
            'label': mapping.get('chebi_label', ingredient_name)
        }

    def get_statistics(self) -> dict:
        """Get statistics about loaded mappings."""
        stats = {
            'total_mappings': len(self.mappings),
            'with_chebi_id': sum(1 for m in self.mappings.values() if m.get('chebi_id')),
            'sources': {}
        }

        # Count by source
        for source in self.sources.values():
            stats['sources'][source] = stats['sources'].get(source, 0) + 1

        # Count by confidence
        stats['confidence'] = {}
        for m in self.mappings.values():
            conf = m.get('confidence', 'unknown')
            stats['confidence'][conf] = stats['confidence'].get(conf, 0) + 1

        return stats


def main():
    """CLI for testing chemical mappings."""
    import argparse

    parser = argparse.ArgumentParser(description="Test chemical mappings")
    parser.add_argument(
        "--microbe-media-param",
        type=Path,
        help="Path to MicrobeMediaParam/pipeline_output/merge_mappings/"
    )
    parser.add_argument(
        "--mediadive",
        type=Path,
        help="Path to MediaDive data directory"
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show statistics"
    )
    parser.add_argument(
        "ingredient",
        nargs="?",
        help="Ingredient to look up"
    )

    args = parser.parse_args()

    mapper = ChemicalMapper(
        microbe_media_param_dir=args.microbe_media_param,
        mediadive_data_dir=args.mediadive
    )

    if args.stats:
        stats = mapper.get_statistics()
        print("\nChemical Mapping Statistics:")
        print(json.dumps(stats, indent=2))
        return

    if args.ingredient:
        mapping = mapper.lookup(args.ingredient)
        if mapping:
            print(f"\nMapping for '{args.ingredient}':")
            print(json.dumps(mapping, indent=2))

            chebi_term = mapper.get_chebi_term(args.ingredient)
            if chebi_term:
                print("\nCHEBI Term:")
                print(json.dumps(chebi_term, indent=2))
        else:
            print(f"No mapping found for '{args.ingredient}'")


if __name__ == "__main__":
    main()
