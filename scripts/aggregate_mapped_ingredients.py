#!/usr/bin/env python3
"""
Aggregate Mapped Media Ingredients

This script scans all media YAML files, identifies ingredients with proper ontology
mappings, and outputs a structured YAML file conforming to the mapped_ingredients_schema.

Mapped ingredients are identified by having a term.id field with an ontology reference
(e.g., CHEBI:12345, FOODON:00001234).

Usage:
    python scripts/aggregate_mapped_ingredients.py [options]

Options:
    --output PATH       Output file path (default: output/mapped_ingredients.yaml)
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


class MappedIngredientAggregator:
    """Aggregates mapped ingredients from media YAML files."""

    def __init__(self, input_dir: str = "data/normalized_yaml", min_occurrences: int = 1, verbose: bool = False):
        self.input_dir = Path(input_dir)
        self.min_occurrences = min_occurrences
        self.verbose = verbose

        # Data structures for aggregation
        self.mapped_ingredients: Dict[str, Dict] = defaultdict(lambda: {
            'preferred_term': '',
            'ontology_id': '',
            'ontology_label': '',
            'ontology_source': '',
            'occurrence_count': 0,
            'media_occurrences': [],
            'concentration_info': [],
            'synonyms': set()
        })

        self.category_stats = defaultdict(lambda: {
            'media_with_mapped': set(),
            'total_mapped_instances': 0,
            'unique_mapped': set()
        })

        self.ontology_stats = defaultdict(lambda: {
            'unique_terms': set(),
            'total_instances': 0
        })

        self.total_media_processed = 0
        self.total_ingredients_processed = 0
        self.media_with_mapped = set()

    def extract_ontology_source(self, term_id: str) -> str:
        """Extract ontology source from term ID."""
        if not term_id:
            return "OTHER"

        if term_id.startswith("CHEBI:"):
            return "CHEBI"
        elif term_id.startswith("FOODON:"):
            return "FOODON"
        elif term_id.startswith("NCIT:"):
            return "NCIT"
        elif term_id.startswith("MESH:"):
            return "MESH"
        elif term_id.startswith("UBERON:"):
            return "UBERON"
        elif term_id.startswith("ENVO:"):
            return "ENVO"
        else:
            return "OTHER"

    def is_mapped_ingredient(self, ingredient: dict) -> bool:
        """Check if an ingredient has proper ontology mapping."""
        # Check for term.id field
        if 'term' in ingredient and isinstance(ingredient['term'], dict):
            term_id = ingredient['term'].get('id', '')
            if term_id and ':' in term_id:
                return True

        # Alternative: agent_term.id field
        if 'agent_term' in ingredient and isinstance(ingredient['agent_term'], dict):
            if 'term' in ingredient['agent_term'] and isinstance(ingredient['agent_term']['term'], dict):
                term_id = ingredient['agent_term']['term'].get('id', '')
                if term_id and ':' in term_id:
                    return True

        return False

    def extract_term_info(self, ingredient: dict) -> Tuple[str, str, str]:
        """Extract term ID, label, and preferred term from ingredient."""
        term_id = ""
        term_label = ""
        preferred_term = ""

        # Check term structure
        if 'term' in ingredient and isinstance(ingredient['term'], dict):
            term_id = ingredient['term'].get('id', '')
            term_label = ingredient['term'].get('label', '')

        # Check agent_term structure
        if 'agent_term' in ingredient and isinstance(ingredient['agent_term'], dict):
            preferred_term = ingredient['agent_term'].get('preferred_term', '')
            if 'term' in ingredient['agent_term'] and isinstance(ingredient['agent_term']['term'], dict):
                term_id = ingredient['agent_term']['term'].get('id', '')
                term_label = ingredient['agent_term']['term'].get('label', '')

        # Fallback to preferred_term at root level
        if not preferred_term:
            preferred_term = ingredient.get('preferred_term', term_label)

        return term_id, term_label, preferred_term

    def process_medium_file(self, file_path: Path) -> None:
        """Process a single medium YAML file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            if not data or 'ingredients' not in data:
                return

            medium_name = data.get('name', file_path.stem)
            medium_category = data.get('category', 'UNKNOWN').upper()

            has_mapped = False

            for idx, ingredient in enumerate(data['ingredients']):
                self.total_ingredients_processed += 1

                if self.is_mapped_ingredient(ingredient):
                    has_mapped = True

                    term_id, term_label, preferred_term = self.extract_term_info(ingredient)

                    if not preferred_term:
                        preferred_term = term_label or term_id

                    ontology_source = self.extract_ontology_source(term_id)

                    # Use preferred_term as key for aggregation
                    key = preferred_term

                    # Add to aggregation
                    ing_data = self.mapped_ingredients[key]
                    ing_data['preferred_term'] = preferred_term
                    ing_data['ontology_id'] = term_id
                    ing_data['ontology_label'] = term_label
                    ing_data['ontology_source'] = ontology_source
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
                            'notes': ingredient.get('notes', '')
                        }
                        ing_data['concentration_info'].append(conc_info)

                    # Track synonyms
                    notes = ingredient.get('notes', '')
                    if notes:
                        ing_data['synonyms'].add(notes[:100])  # Limit length

                    # Update category stats
                    self.category_stats[medium_category]['media_with_mapped'].add(medium_name)
                    self.category_stats[medium_category]['total_mapped_instances'] += 1
                    self.category_stats[medium_category]['unique_mapped'].add(key)

                    # Update ontology stats
                    self.ontology_stats[ontology_source]['unique_terms'].add(term_id)
                    self.ontology_stats[ontology_source]['total_instances'] += 1

            if has_mapped:
                self.media_with_mapped.add(medium_name)

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
            print(f"Total ingredients processed: {self.total_ingredients_processed}", file=sys.stderr)

    def generate_output(self) -> Dict:
        """Generate the structured output conforming to the schema."""
        # Filter by minimum occurrences
        filtered_ingredients = {
            k: v for k, v in self.mapped_ingredients.items()
            if v['occurrence_count'] >= self.min_occurrences
        }

        # Convert sets to lists and prepare output
        mapped_list = []
        for preferred_term, data in sorted(filtered_ingredients.items(),
                                          key=lambda x: x[1]['occurrence_count'],
                                          reverse=True):
            ingredient_entry = {
                'preferred_term': preferred_term,
                'ontology_id': data['ontology_id'],
                'ontology_label': data['ontology_label'],
                'ontology_source': data['ontology_source'],
                'occurrence_count': data['occurrence_count'],
                'media_occurrences': data['media_occurrences'][:50],  # Limit to 50 examples
                'mapping_quality': 'DIRECT_MATCH'  # Default assumption
            }

            # Add unique concentration info
            unique_conc = []
            seen_conc = set()
            for conc in data['concentration_info']:
                key = (conc['value'], conc['unit'])
                if key not in seen_conc:
                    seen_conc.add(key)
                    unique_conc.append(conc)
            ingredient_entry['concentration_info'] = unique_conc[:10]  # Limit to 10 examples

            # Add synonyms if any
            if data['synonyms']:
                ingredient_entry['synonyms'] = sorted(data['synonyms'])[:5]  # Limit to 5

            mapped_list.append(ingredient_entry)

        # Prepare category summary
        category_summary = []
        for category, stats in sorted(self.category_stats.items()):
            category_summary.append({
                'category': category,
                'media_with_mapped': len(stats['media_with_mapped']),
                'total_mapped_instances': stats['total_mapped_instances'],
                'unique_mapped_count': len(stats['unique_mapped'])
            })

        # Prepare ontology summary
        total_instances = sum(stats['total_instances'] for stats in self.ontology_stats.values())
        ontology_summary = []
        for ontology, stats in sorted(self.ontology_stats.items(),
                                     key=lambda x: x[1]['total_instances'],
                                     reverse=True):
            coverage_pct = (stats['total_instances'] / total_instances * 100) if total_instances > 0 else 0
            ontology_summary.append({
                'ontology_source': ontology,
                'unique_terms_count': len(stats['unique_terms']),
                'total_instances': stats['total_instances'],
                'coverage_percentage': round(coverage_pct, 2)
            })

        # Calculate total instances
        total_instances_count = sum(ing['occurrence_count'] for ing in mapped_list)

        # Build final output
        output = {
            'generation_date': datetime.now().isoformat(),
            'total_mapped_count': len(filtered_ingredients),
            'total_instances': total_instances_count,
            'media_count': len(self.media_with_mapped),
            'mapped_ingredients': mapped_list,
            'summary_by_category': category_summary,
            'summary_by_ontology': ontology_summary
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
            print(f"Total mapped ingredients: {output_data['total_mapped_count']}", file=sys.stderr)
            print(f"Total instances: {output_data['total_instances']}", file=sys.stderr)
            print(f"Media with mapped ingredients: {output_data['media_count']}", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(
        description='Aggregate mapped media ingredients into structured YAML',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    parser.add_argument(
        '--output',
        default='output/mapped_ingredients.yaml',
        help='Output file path (default: output/mapped_ingredients.yaml)'
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
        aggregator = MappedIngredientAggregator(
            input_dir=args.input_dir,
            min_occurrences=args.min_occurrences,
            verbose=args.verbose
        )

        aggregator.scan_all_media()
        aggregator.save_output(args.output)

        print(f"✅ Successfully aggregated mapped ingredients to {args.output}")

    except Exception as e:
        print(f"❌ Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
