#!/usr/bin/env python3
"""
Import MediaDive API Solutions to CultureMech YAML Format

Converts MediaDive API solutions (from mediadive_api_solutions.json) into
individual SolutionDescriptor YAML files for reuse across media recipes.

Input:
- data/raw/mediadive_api/mediadive_api_solutions.json (5,399 solutions)

Output:
- data/normalized_yaml/solutions/mediadive/*.yaml (individual solution files)
- data/normalized_yaml/solutions/mediadive_index.json (lookup index)

Usage:
    python scripts/import_mediadive_solutions.py [--limit N] [--dry-run]
"""

import json
import yaml
import re
from pathlib import Path
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from collections import Counter
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)


class MediaDiveSolutionImporter:
    """Import MediaDive API solutions into CultureMech SolutionDescriptor format."""

    # Unit mapping from MediaDive to CultureMech schema
    # Only includes units that exist in ConcentrationUnitEnum
    UNIT_MAP = {
        'g': 'G_PER_L',
        'g/l': 'G_PER_L',
        'mg': 'MG_PER_L',
        'mg/l': 'MG_PER_L',
        'mg/ml': 'G_PER_L',  # mg/ml = g/L
        'µg': 'MICROG_PER_L',
        'µg/l': 'MICROG_PER_L',
        'ug': 'MICROG_PER_L',
        'ug/l': 'MICROG_PER_L',
        'ml': 'PERCENT_V_V',  # mL per L is volume/volume
        'ml/l': 'PERCENT_V_V',
        'mL': 'PERCENT_V_V',
        'µl': 'PERCENT_V_V',  # μL per L (very small volume fraction)
        'μl': 'PERCENT_V_V',  # Different Unicode
        'ul': 'PERCENT_V_V',
        'M': 'MOLAR',
        'mM': 'MILLIMOLAR',
        'µM': 'MICROMOLAR',
        'μM': 'MICROMOLAR',  # Different Unicode
        'uM': 'MICROMOLAR',
        '%': 'PERCENT_W_V',
        '%(v/v)': 'PERCENT_V_V',
        '%(w/v)': 'PERCENT_W_V',
        # Special units that don't map cleanly - use VARIABLE
        'Units': 'VARIABLE',  # International Units (enzyme activity)
        'piece': 'VARIABLE',  # Counted items (e.g., tablets)
        'drops': 'VARIABLE',  # Imprecise volume measure
    }

    def __init__(
        self,
        input_file: Path,
        output_dir: Path,
        dry_run: bool = False
    ):
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)
        self.dry_run = dry_run

        self.stats = {
            'total_solutions': 0,
            'solutions_written': 0,
            'solutions_with_composition': 0,
            'solutions_skipped': 0,
            'total_ingredients': 0,
            'unit_conversions': Counter(),
        }

        # Load solution data
        with open(self.input_file) as f:
            data = json.load(f)
            self.solutions = data.get('data', [])
            self.stats['total_solutions'] = len(self.solutions)

        logger.info(f"Loaded {len(self.solutions)} solutions from {self.input_file}")

    def _sanitize_filename(self, name: str) -> str:
        """
        Convert solution name to safe filename.

        Examples:
            "Main sol. 1" -> "Main_sol_1"
            "Trace metal solution (SL-6)" -> "Trace_metal_solution_SL_6"
        """
        # Replace problematic characters with underscore
        name = re.sub(r'[^\w\s\-]', '_', name)
        # Replace whitespace with underscore
        name = re.sub(r'\s+', '_', name)
        # Remove consecutive underscores
        name = re.sub(r'_+', '_', name)
        # Remove leading/trailing underscores
        name = name.strip('_')
        # Limit length
        if len(name) > 100:
            name = name[:100]
        return name

    def _convert_unit(self, unit: str, volume_ml: float = 1000.0) -> str:
        """
        Convert MediaDive unit to CultureMech ConcentrationUnitEnum.

        MediaDive units are per solution volume (e.g., "5g per 1000ml").
        CultureMech units are normalized per liter.

        Args:
            unit: MediaDive unit string (e.g., "g", "mg", "ml")
            volume_ml: Solution volume in mL (default 1000)

        Returns:
            CultureMech unit enum value
        """
        unit_clean = unit.strip() if unit else 'g'

        # Direct mapping if available
        if unit_clean in self.UNIT_MAP:
            self.stats['unit_conversions'][unit_clean] += 1
            return self.UNIT_MAP[unit_clean]

        # Default to G_PER_L
        logger.warning(f"Unknown unit '{unit}', defaulting to G_PER_L")
        self.stats['unit_conversions']['unknown'] += 1
        return 'G_PER_L'

    def _normalize_concentration(
        self,
        amount: float,
        unit: str,
        volume_ml: float = 1000.0
    ) -> float:
        """
        Normalize concentration to per-liter basis.

        Args:
            amount: Amount in solution
            unit: Unit string
            volume_ml: Solution volume in mL

        Returns:
            Normalized amount per liter
        """
        # Handle edge case of zero or invalid volume
        if volume_ml <= 0:
            logger.warning(f"Invalid volume {volume_ml} mL, using default 1000 mL")
            volume_ml = 1000.0

        # Convert to per-liter if solution volume != 1L
        if volume_ml != 1000.0:
            amount = amount * (1000.0 / volume_ml)

        return amount

    def _convert_ingredient(
        self,
        recipe_item: dict,
        solution_volume_ml: float
    ) -> Optional[dict]:
        """
        Convert MediaDive recipe item to CultureMech IngredientDescriptor.

        MediaDive format:
        {
          "recipe_order": 1,
          "compound": "Peptone",
          "compound_id": 1,
          "amount": 5,
          "unit": "g",
          "g_l": 5,
          "condition": "for solid medium",
          "optional": 0
        }

        CultureMech format:
        {
          "preferred_term": "Peptone",
          "concentration": {
            "value": "5",
            "unit": "G_PER_L"
          },
          "notes": "for solid medium",
          "term": {
            "id": "mediadive.compound:1",
            "label": "Peptone"
          }
        }
        """
        if not recipe_item.get('compound'):
            return None

        # Normalize concentration if needed
        amount = recipe_item.get('amount', 0)
        unit = recipe_item.get('unit', 'g')

        # Use g_l if available (already normalized)
        if recipe_item.get('g_l') is not None:
            amount = recipe_item['g_l']
            unit = 'g'
        else:
            # Normalize to per-liter
            amount = self._normalize_concentration(
                amount, unit, solution_volume_ml
            )

        ingredient = {
            'preferred_term': recipe_item['compound']
        }

        # Add concentration
        if amount > 0:
            ingredient['concentration'] = {
                'value': str(amount),
                'unit': self._convert_unit(unit, solution_volume_ml)
            }

        # Add notes (condition)
        notes_parts = []
        if recipe_item.get('condition'):
            notes_parts.append(recipe_item['condition'])
        if recipe_item.get('optional') == 1:
            notes_parts.append('optional')
        if notes_parts:
            ingredient['notes'] = '; '.join(notes_parts)

        # Add term reference
        if recipe_item.get('compound_id'):
            ingredient['term'] = {
                'id': f"mediadive.compound:{recipe_item['compound_id']}",
                'label': recipe_item['compound']
            }

        return ingredient

    def _convert_solution(self, solution: dict) -> Optional[dict]:
        """
        Convert MediaDive solution to CultureMech SolutionDescriptor.

        MediaDive format:
        {
          "id": 1,
          "name": "Main sol. 1",
          "volume": 1000,
          "recipe": [...],
          "steps": [...]
        }

        CultureMech SolutionDescriptor format:
        {
          "preferred_term": "Main sol. 1",
          "term": {
            "id": "mediadive.solution:1",
            "label": "Main sol. 1"
          },
          "composition": [...],
          "preparation_notes": "...",
          "storage_conditions": null,
          "shelf_life": null
        }
        """
        if not solution.get('name') or not solution.get('recipe'):
            return None

        solution_id = solution['id']
        name = solution['name']
        volume_ml = solution.get('volume', 1000.0)

        # Handle invalid volumes
        if not volume_ml or volume_ml <= 0:
            logger.warning(f"Solution {solution_id} has invalid volume {volume_ml}, using 1000 mL")
            volume_ml = 1000.0

        # Convert ingredients
        composition = []
        for recipe_item in solution['recipe']:
            ingredient = self._convert_ingredient(recipe_item, volume_ml)
            if ingredient:
                composition.append(ingredient)
                self.stats['total_ingredients'] += 1

        if not composition:
            logger.warning(f"Solution {solution_id} '{name}' has no valid ingredients")
            return None

        # Build SolutionDescriptor
        descriptor = {
            'preferred_term': name,
            'term': {
                'id': f'mediadive.solution:{solution_id}',
                'label': name
            },
            'composition': composition
        }

        # Add preparation notes from steps
        if solution.get('steps'):
            steps_text = '\n'.join([
                step.get('step', '') for step in solution['steps']
                if step.get('step')
            ])
            if steps_text:
                descriptor['preparation_notes'] = steps_text

        # Add volume note if not standard 1L
        if volume_ml != 1000.0:
            volume_note = f"Original volume: {volume_ml} mL"
            if descriptor.get('preparation_notes'):
                descriptor['preparation_notes'] += f"\n\n{volume_note}"
            else:
                descriptor['preparation_notes'] = volume_note

        return descriptor

    def import_solutions(self, limit: Optional[int] = None):
        """
        Import all solutions to YAML files.

        Args:
            limit: Maximum number of solutions to import (for testing)
        """
        logger.info(f"Importing solutions to {self.output_dir}")

        if not self.dry_run:
            self.output_dir.mkdir(parents=True, exist_ok=True)

        # Index for fast lookups
        solution_index = {}

        # Process solutions
        for idx, solution in enumerate(self.solutions[:limit] if limit else self.solutions):
            if (idx + 1) % 100 == 0:
                logger.info(f"Processed {idx + 1}/{len(self.solutions)} solutions...")

            # Convert to SolutionDescriptor
            descriptor = self._convert_solution(solution)
            if not descriptor:
                self.stats['solutions_skipped'] += 1
                continue

            self.stats['solutions_with_composition'] += 1

            # Generate filename
            solution_id = solution['id']
            safe_name = self._sanitize_filename(solution['name'])
            filename = f"mediadive_{solution_id}_{safe_name}.yaml"

            # Add to index
            solution_index[f"mediadive.solution:{solution_id}"] = {
                'id': f"mediadive.solution:{solution_id}",
                'name': solution['name'],
                'filename': filename,
                'ingredient_count': len(descriptor['composition'])
            }

            # Write YAML
            if not self.dry_run:
                output_path = self.output_dir / filename
                with open(output_path, 'w') as f:
                    yaml.dump(
                        descriptor,
                        f,
                        default_flow_style=False,
                        sort_keys=False,
                        allow_unicode=True
                    )
                self.stats['solutions_written'] += 1
            else:
                logger.debug(f"Would write: {filename}")

        # Write index file
        index_path = self.output_dir.parent / 'mediadive_solution_index.json'
        if not self.dry_run:
            with open(index_path, 'w') as f:
                json.dump(
                    {
                        'generated': datetime.now(timezone.utc).isoformat(),
                        'source': str(self.input_file),
                        'count': len(solution_index),
                        'solutions': solution_index
                    },
                    f,
                    indent=2
                )
            logger.info(f"Wrote solution index to {index_path}")

        return solution_index

    def print_stats(self):
        """Print import statistics."""
        logger.info("\n" + "=" * 60)
        logger.info("MediaDive Solution Import Statistics")
        logger.info("=" * 60)
        logger.info(f"Total solutions loaded:      {self.stats['total_solutions']}")
        logger.info(f"Solutions with composition:  {self.stats['solutions_with_composition']}")
        logger.info(f"Solutions skipped:           {self.stats['solutions_skipped']}")
        logger.info(f"Solutions written:           {self.stats['solutions_written']}")
        logger.info(f"Total ingredients:           {self.stats['total_ingredients']}")
        logger.info("")
        logger.info("Unit conversions:")
        for unit, count in self.stats['unit_conversions'].most_common():
            logger.info(f"  {unit:15s} → {count:5d}")
        logger.info("=" * 60)


def main():
    import argparse

    parser = argparse.ArgumentParser(
        description="Import MediaDive API solutions to CultureMech YAML format"
    )
    parser.add_argument(
        '--input',
        type=Path,
        default=Path('data/raw/mediadive_api/mediadive_api_solutions.json'),
        help='Input MediaDive solutions JSON file'
    )
    parser.add_argument(
        '--output',
        type=Path,
        default=Path('data/normalized_yaml/solutions/mediadive'),
        help='Output directory for solution YAML files'
    )
    parser.add_argument(
        '--limit',
        type=int,
        help='Limit number of solutions to import (for testing)'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview without writing files'
    )

    args = parser.parse_args()

    # Verify input file exists
    if not args.input.exists():
        logger.error(f"Input file not found: {args.input}")
        return 1

    # Create importer
    importer = MediaDiveSolutionImporter(
        input_file=args.input,
        output_dir=args.output,
        dry_run=args.dry_run
    )

    # Import solutions
    solution_index = importer.import_solutions(limit=args.limit)

    # Print statistics
    importer.print_stats()

    if args.dry_run:
        logger.info("\n🔍 DRY RUN - No files were written")
    else:
        logger.info(f"\n✓ Import complete! Solutions saved to {args.output}")

    return 0


if __name__ == '__main__':
    exit(main())
