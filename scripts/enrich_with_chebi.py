#!/usr/bin/env python3
"""
Enrich normalized YAML recipes with CHEBI ontology terms.

Applies chemical mappings to all normalized_yaml files, adding CHEBI terms
to ingredients based on the MicrobeMediaParam and MediaDive mappings.

Usage:
    uv run python scripts/enrich_with_chebi.py [--dry-run] [--limit N]
"""

import argparse
import sys
import yaml
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter

# Import ChemicalMapper using importlib to handle 'import' keyword issue
from importlib import import_module
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

ChemicalMapper = import_module('culturemech.import.chemical_mappings').ChemicalMapper


class RecipeEnricher:
    """Enrich recipe YAML files with CHEBI ontology terms."""

    def __init__(self, mapper: ChemicalMapper, dry_run: bool = False):
        self.mapper = mapper
        self.dry_run = dry_run
        self.stats = {
            'total_recipes': 0,
            'recipes_modified': 0,
            'total_ingredients': 0,
            'ingredients_enriched': 0,
            'ingredients_already_had_term': 0,
            'ingredients_no_mapping': 0,
            'ingredients_updated': 0,
            'by_category': Counter(),
            'by_source': Counter(),
        }

    def enrich_ingredient(self, ingredient: dict) -> bool:
        """
        Enrich a single ingredient with CHEBI term.

        Returns:
            True if ingredient was modified, False otherwise
        """
        preferred_term = ingredient.get('preferred_term', '')

        # Convert to string if it's not already (handle edge cases)
        if not isinstance(preferred_term, str):
            preferred_term = str(preferred_term)

        preferred_term = preferred_term.strip()
        if not preferred_term:
            return False

        self.stats['total_ingredients'] += 1

        # Check if already has a term
        existing_term = ingredient.get('term')
        if existing_term and existing_term.get('id'):
            self.stats['ingredients_already_had_term'] += 1
            # Could optionally verify/update existing term
            return False

        # Look up mapping
        chebi_term = self.mapper.get_chebi_term(preferred_term)

        if not chebi_term:
            self.stats['ingredients_no_mapping'] += 1
            return False

        # Add CHEBI term
        ingredient['term'] = chebi_term
        self.stats['ingredients_enriched'] += 1
        return True

    def enrich_solution(self, solution: dict) -> bool:
        """
        Enrich a solution's composition with CHEBI terms.

        Returns:
            True if solution was modified, False otherwise
        """
        composition = solution.get('composition', [])
        if not composition:
            return False

        modified = False
        for ingredient in composition:
            if self.enrich_ingredient(ingredient):
                modified = True

        return modified

    def enrich_recipe(self, recipe: dict) -> bool:
        """
        Enrich a recipe with CHEBI terms for all ingredients.

        Returns:
            True if recipe was modified, False otherwise
        """
        modified = False

        # Enrich direct ingredients
        ingredients = recipe.get('ingredients', [])
        for ingredient in ingredients:
            if self.enrich_ingredient(ingredient):
                modified = True

        # Enrich solution compositions
        solutions = recipe.get('solutions', [])
        for solution in solutions:
            if self.enrich_solution(solution):
                modified = True

        return modified

    def enrich_file(self, yaml_file: Path) -> bool:
        """
        Enrich a single YAML file with CHEBI terms.

        Returns:
            True if file was modified, False otherwise
        """
        try:
            # Load recipe
            with open(yaml_file) as f:
                recipe = yaml.safe_load(f)

            if not recipe:
                return False

            # Track category
            category = yaml_file.parent.name
            self.stats['by_category'][category] += 1

            # Enrich recipe
            modified = self.enrich_recipe(recipe)

            if modified:
                self.stats['recipes_modified'] += 1

                if not self.dry_run:
                    # Add curation event
                    curation_history = recipe.get('curation_history', [])
                    curation_history.append({
                        'timestamp': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
                        'curator': 'chebi-enrichment',
                        'action': 'Added CHEBI ontology terms to ingredients',
                        'notes': 'Enriched using MicrobeMediaParam and MediaDive chemical mappings'
                    })
                    recipe['curation_history'] = curation_history

                    # Write back to file
                    with open(yaml_file, 'w') as f:
                        yaml.dump(recipe, f, default_flow_style=False, sort_keys=False,
                                  allow_unicode=True)

            return modified

        except Exception as e:
            print(f"Error processing {yaml_file}: {e}")
            return False

    def enrich_all(self, normalized_yaml_dir: Path, limit: int = None):
        """Enrich all YAML files in the normalized_yaml directory."""
        yaml_files = list(normalized_yaml_dir.rglob('*.yaml'))

        if limit:
            yaml_files = yaml_files[:limit]
            print(f"Limiting to {limit} files")

        self.stats['total_recipes'] = len(yaml_files)

        print(f"\n{'DRY RUN - ' if self.dry_run else ''}Enriching {len(yaml_files)} recipes...")
        print("=" * 70)

        for i, yaml_file in enumerate(yaml_files, 1):
            if i % 100 == 0:
                print(f"Progress: {i}/{len(yaml_files)} ({i/len(yaml_files)*100:.1f}%)")
                print(f"  Modified: {self.stats['recipes_modified']}, "
                      f"Enriched: {self.stats['ingredients_enriched']}, "
                      f"No mapping: {self.stats['ingredients_no_mapping']}")

            self.enrich_file(yaml_file)

        self.print_summary()

    def print_summary(self):
        """Print enrichment statistics."""
        print("\n" + "=" * 70)
        print(f"{'DRY RUN - ' if self.dry_run else ''}Enrichment Summary")
        print("=" * 70)
        print(f"Total recipes:           {self.stats['total_recipes']}")
        print(f"Recipes modified:        {self.stats['recipes_modified']} "
              f"({self.stats['recipes_modified']/self.stats['total_recipes']*100:.1f}%)")
        print()
        print(f"Total ingredients:       {self.stats['total_ingredients']}")
        print(f"  Already had term:      {self.stats['ingredients_already_had_term']} "
              f"({self.stats['ingredients_already_had_term']/self.stats['total_ingredients']*100:.1f}%)")
        print(f"  Newly enriched:        {self.stats['ingredients_enriched']} "
              f"({self.stats['ingredients_enriched']/self.stats['total_ingredients']*100:.1f}%)")
        print(f"  No mapping found:      {self.stats['ingredients_no_mapping']} "
              f"({self.stats['ingredients_no_mapping']/self.stats['total_ingredients']*100:.1f}%)")
        print()
        print("By category:")
        for cat, count in sorted(self.stats['by_category'].items()):
            print(f"  {cat}: {count}")
        print("=" * 70)


def main():
    parser = argparse.ArgumentParser(
        description="Enrich normalized YAML recipes with CHEBI ontology terms"
    )
    parser.add_argument(
        "--normalized-yaml",
        type=Path,
        default="data/normalized_yaml",
        help="Path to normalized_yaml directory"
    )
    parser.add_argument(
        "--microbe-media-param",
        type=Path,
        default="data/raw/microbe-media-param",
        help="Path to MicrobeMediaParam mappings"
    )
    parser.add_argument(
        "--mediadive",
        type=Path,
        default="data/raw/mediadive",
        help="Path to MediaDive data"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Don't modify files, just show what would be done"
    )
    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of files to process (for testing)"
    )

    args = parser.parse_args()

    print("=" * 70)
    print("CHEBI Enrichment for CultureMech Recipes")
    print("=" * 70)
    print(f"Normalized YAML: {args.normalized_yaml}")
    print(f"MicrobeMediaParam: {args.microbe_media_param}")
    print(f"MediaDive: {args.mediadive}")
    print(f"Dry run: {args.dry_run}")
    print()

    # Load chemical mapper
    print("Loading chemical mappings...")
    mapper = ChemicalMapper(
        microbe_media_param_dir=args.microbe_media_param,
        mediadive_data_dir=args.mediadive
    )

    stats = mapper.get_statistics()
    print(f"Loaded {stats['total_mappings']} mappings "
          f"({stats['with_chebi_id']} with CHEBI IDs)")

    # Create enricher
    enricher = RecipeEnricher(mapper, dry_run=args.dry_run)

    # Enrich all recipes
    enricher.enrich_all(args.normalized_yaml, limit=args.limit)

    if args.dry_run:
        print("\nThis was a DRY RUN. No files were modified.")
        print("Run without --dry-run to apply changes.")


if __name__ == "__main__":
    main()
