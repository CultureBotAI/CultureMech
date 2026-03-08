#!/usr/bin/env python3
"""
Aggregate Unmapped Media Ingredients

This script scans all media YAML files, identifies unmapped ingredients,
and outputs a structured YAML file conforming to the unmapped_ingredients_schema.

Unmapped ingredients are identified by:
- Numeric placeholder IDs (e.g., '1', '2', '3')
- Generic placeholders like 'See source for composition'
- Empty or missing preferred_term values

Usage:
    python scripts/aggregate_unmapped_ingredients.py [options]

Options:
    --output PATH       Output file path (default: output/unmapped_ingredients.yaml)
    --input-dir PATH    Input directory with media YAML files (default: data/normalized_yaml)
    --min-occurrences N Only include ingredients appearing at least N times (default: 1)
    --verbose           Enable verbose logging
"""

import argparse
import glob
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Set, Tuple

import yaml


class UnmappedIngredientAggregator:
    """Aggregates unmapped ingredients from media YAML files."""

    def __init__(self, input_dir: str = "data/normalized_yaml", min_occurrences: int = 1, verbose: bool = False):
        self.input_dir = Path(input_dir)
        self.min_occurrences = min_occurrences
        self.verbose = verbose

        # Data structures for aggregation
        self.unmapped_ingredients: Dict[str, Dict] = defaultdict(lambda: {
            'placeholder_id': '',
            'raw_ingredient_text': set(),
            'occurrence_count': 0,
            'media_occurrences': [],
            'concentration_info': []
        })

        self.category_stats = defaultdict(lambda: {
            'media_with_unmapped': set(),
            'total_unmapped_instances': 0,
            'unique_unmapped': set()
        })

        self.total_media_processed = 0
        self.media_with_unmapped = set()

    def is_unmapped_ingredient(self, preferred_term: str) -> bool:
        """Check if an ingredient is unmapped based on its preferred_term."""
        if not preferred_term or preferred_term.strip() == '':
            return True

        # Numeric placeholders
        if preferred_term.isdigit():
            return True

        # Generic placeholders
        generic_placeholders = [
            'See source for composition',
            'variable',
            'See source',
            'Not specified',
            'Unknown'
        ]

        if any(placeholder.lower() in preferred_term.lower() for placeholder in generic_placeholders):
            return True

        return False

    def extract_chemical_name(self, notes: str) -> str:
        """Extract chemical name from notes field."""
        if not notes:
            return ""

        # Try to extract from "Original amount: <chemical>" pattern
        match = re.search(r'Original amount:\s*([^\(]+)', notes)
        if match:
            chemical = match.group(1).strip()
            # Remove any trailing numbers or special chars
            chemical = re.sub(r'\s*[\d.]+\s*$', '', chemical)
            return chemical

        # Try to extract before parentheses
        match = re.search(r'^([^\(]+)', notes)
        if match:
            return match.group(1).strip()

        return notes.strip()

    def process_medium_file(self, file_path: Path) -> None:
        """Process a single medium YAML file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            if not data or 'ingredients' not in data:
                return

            medium_name = data.get('name', file_path.stem)
            medium_category = data.get('category', 'UNKNOWN').upper()

            has_unmapped = False

            for idx, ingredient in enumerate(data['ingredients']):
                preferred_term = ingredient.get('preferred_term', '')

                if self.is_unmapped_ingredient(preferred_term):
                    # Skip completely empty ingredients (data quality issue)
                    notes = ingredient.get('notes', '')
                    if not preferred_term and not notes:
                        if self.verbose:
                            print(f"Skipping empty ingredient at index {idx} in {medium_name}", file=sys.stderr)
                        continue

                    has_unmapped = True

                    # Use placeholder ID as key
                    placeholder_id = preferred_term if preferred_term else f'empty_{idx}'

                    # Extract information
                    chemical_name = self.extract_chemical_name(notes)

                    # Add to aggregation
                    ing_data = self.unmapped_ingredients[placeholder_id]
                    ing_data['placeholder_id'] = placeholder_id

                    if notes:
                        ing_data['raw_ingredient_text'].add(notes)
                    if chemical_name:
                        if 'parsed_chemical_names' not in ing_data:
                            ing_data['parsed_chemical_names'] = set()
                        ing_data['parsed_chemical_names'].add(chemical_name)

                    ing_data['occurrence_count'] += 1

                    # Add media occurrence
                    ing_data['media_occurrences'].append({
                        'medium_name': medium_name,
                        'medium_category': medium_category,
                        'medium_file_path': str(file_path.relative_to(self.input_dir.parent)),
                        'ingredient_index': idx
                    })

                    # Add concentration info
                    if 'concentration' in ingredient:
                        conc = ingredient['concentration']
                        conc_info = {
                            'value': str(conc.get('value', 'variable')),
                            'unit': conc.get('unit', 'VARIABLE'),
                            'notes': notes
                        }
                        ing_data['concentration_info'].append(conc_info)

                    # Update category stats
                    self.category_stats[medium_category]['media_with_unmapped'].add(medium_name)
                    self.category_stats[medium_category]['total_unmapped_instances'] += 1
                    self.category_stats[medium_category]['unique_unmapped'].add(placeholder_id)

            if has_unmapped:
                self.media_with_unmapped.add(medium_name)

            self.total_media_processed += 1

            if self.verbose and self.total_media_processed % 100 == 0:
                print(f"Processed {self.total_media_processed} media files...", file=sys.stderr)

        except Exception as e:
            if self.verbose:
                print(f"Error processing {file_path}: {e}", file=sys.stderr)

    def scan_all_media(self) -> None:
        """Scan all media YAML files in the input directory."""
        if not self.input_dir.exists():
            raise ValueError(f"Input directory not found: {self.input_dir}")

        pattern = str(self.input_dir / "**/*.yaml")
        media_files = glob.glob(pattern, recursive=True)

        if self.verbose:
            print(f"Found {len(media_files)} media files to process", file=sys.stderr)

        for file_path in media_files:
            self.process_medium_file(Path(file_path))

        if self.verbose:
            print(f"Completed processing {self.total_media_processed} media files", file=sys.stderr)

    def generate_output(self) -> Dict:
        """Generate the structured output conforming to the schema."""
        # Filter by minimum occurrences
        filtered_ingredients = {
            k: v for k, v in self.unmapped_ingredients.items()
            if v['occurrence_count'] >= self.min_occurrences
        }

        # Convert sets to lists and prepare output
        unmapped_list = []
        for placeholder_id, data in sorted(filtered_ingredients.items(),
                                          key=lambda x: x[1]['occurrence_count'],
                                          reverse=True):
            ingredient_entry = {
                'placeholder_id': placeholder_id,
                'raw_ingredient_text': sorted(data['raw_ingredient_text']),
                'occurrence_count': data['occurrence_count'],
                'media_occurrences': data['media_occurrences'],
                'mapping_status': 'UNMAPPED'
            }

            # Add parsed chemical name if available
            if 'parsed_chemical_names' in data and data['parsed_chemical_names']:
                # Use the most common one or first one
                ingredient_entry['parsed_chemical_name'] = sorted(data['parsed_chemical_names'])[0]

            # Add unique concentration info
            unique_conc = []
            seen_conc = set()
            for conc in data['concentration_info']:
                key = (conc['value'], conc['unit'])
                if key not in seen_conc:
                    seen_conc.add(key)
                    unique_conc.append(conc)
            ingredient_entry['concentration_info'] = unique_conc[:10]  # Limit to 10 examples

            unmapped_list.append(ingredient_entry)

        # Prepare category summary
        summary_list = []
        for category, stats in sorted(self.category_stats.items()):
            summary_list.append({
                'category': category,
                'media_with_unmapped': len(stats['media_with_unmapped']),
                'total_unmapped_instances': stats['total_unmapped_instances'],
                'unique_unmapped_count': len(stats['unique_unmapped'])
            })

        # Build final output
        output = {
            'generation_date': datetime.now().isoformat(),
            'total_unmapped_count': len(filtered_ingredients),
            'media_count': len(self.media_with_unmapped),
            'unmapped_ingredients': unmapped_list,
            'summary_by_category': summary_list
        }

        return output

    def save_output(self, output_path: str) -> None:
        """Save the aggregated output to a YAML file."""
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)

        output_data = self.generate_output()

        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(output_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

        if self.verbose:
            print(f"\nOutput saved to: {output_path}", file=sys.stderr)
            print(f"Total unmapped ingredients: {output_data['total_unmapped_count']}", file=sys.stderr)
            print(f"Media with unmapped ingredients: {output_data['media_count']}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description='Aggregate unmapped media ingredients into structured YAML',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        '--output',
        default='output/unmapped_ingredients.yaml',
        help='Output file path (default: output/unmapped_ingredients.yaml)'
    )

    parser.add_argument(
        '--input-dir',
        default='data/normalized_yaml',
        help='Input directory with media YAML files (default: data/normalized_yaml)'
    )

    parser.add_argument(
        '--min-occurrences',
        type=int,
        default=1,
        help='Only include ingredients appearing at least N times (default: 1)'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Enable verbose logging'
    )

    args = parser.parse_args()

    try:
        aggregator = UnmappedIngredientAggregator(
            input_dir=args.input_dir,
            min_occurrences=args.min_occurrences,
            verbose=args.verbose
        )

        aggregator.scan_all_media()
        aggregator.save_output(args.output)

        print(f"✅ Successfully aggregated unmapped ingredients to {args.output}")

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
