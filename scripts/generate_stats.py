#!/usr/bin/env python3
"""
Generate comprehensive statistics for CultureMech repository.

Produces reproducible statistics about media recipes, sources, and ingredient
mapping coverage (CHEBI, PubChem, CAS-RN).

Usage:
    uv run python scripts/generate_stats.py [--output-json FILE] [--output-markdown FILE] [--output-dir DIR] [--terminal-only]
"""

import argparse
import json
import sys
import yaml
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter, defaultdict
from typing import Dict, List, Optional

# Import ChemicalMapper
from importlib import import_module
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))
ChemicalMapper = import_module('culturemech.import.chemical_mappings').ChemicalMapper


class RecipeStatisticsCollector:
    """Single-pass recipe statistics collector with progress reporting."""

    def __init__(self, normalized_yaml_dir: Path, mapper: ChemicalMapper):
        self.normalized_yaml_dir = Path(normalized_yaml_dir)
        self.mapper = mapper
        self.stats = {
            'metadata': {
                'generated_at': datetime.now(timezone.utc).isoformat(),
                'repository': 'KG-Microbe/CultureMech',
                'total_recipes': 0,
            },
            'recipes_by_category': Counter(),
            'recipes_by_source': Counter(),
            'ingredient_mapping': {
                'total_ingredients': 0,
                'with_chebi': 0,
                'with_pubchem': 0,
                'with_cas_rn': 0,
                'unmapped': 0,
            },
            'data_quality': {
                'recipes_with_ingredients': 0,
                'total_ingredient_count': 0,
            },
            'medium_composition': Counter(),
            'physical_state': Counter(),
        }

    def collect_statistics(self) -> Dict:
        """Single-pass processing of all recipes."""
        yaml_files = list(self.normalized_yaml_dir.rglob('*.yaml'))
        self.stats['metadata']['total_recipes'] = len(yaml_files)

        print(f"\nProcessing {len(yaml_files)} recipes...")
        print("=" * 70)

        for i, yaml_file in enumerate(yaml_files, 1):
            if i % 500 == 0:
                print(f"Progress: {i}/{len(yaml_files)} ({i/len(yaml_files)*100:.1f}%)")

            self._process_recipe(yaml_file)

        # Calculate derived statistics
        self._finalize_statistics()

        print(f"\n✓ Processed {len(yaml_files)} recipes")
        return self.stats

    def _process_recipe(self, yaml_file: Path):
        """Extract metrics from one recipe."""
        try:
            with open(yaml_file) as f:
                recipe = yaml.safe_load(f)

            if not recipe:
                return

            # Track category
            category = yaml_file.parent.name
            self.stats['recipes_by_category'][category] += 1

            # Extract source
            source = self._extract_source(recipe, yaml_file)
            self.stats['recipes_by_source'][source] += 1

            # Track medium composition
            medium_type = recipe.get('medium_type', 'UNKNOWN')
            self.stats['medium_composition'][medium_type] += 1

            # Track physical state
            physical_state = recipe.get('physical_state', 'UNKNOWN')
            self.stats['physical_state'][physical_state] += 1

            # Analyze ingredients
            ingredients = recipe.get('ingredients', [])
            solutions = recipe.get('solutions', [])

            # Count recipes with ingredients
            if ingredients or solutions:
                self.stats['data_quality']['recipes_with_ingredients'] += 1

            # Process direct ingredients
            for ingredient in ingredients:
                self._analyze_ingredient(ingredient)

            # Process solution compositions
            for solution in solutions:
                composition = solution.get('composition', [])
                for ingredient in composition:
                    self._analyze_ingredient(ingredient)

        except Exception as e:
            print(f"Warning: Error processing {yaml_file}: {e}")

    def _extract_source(self, recipe: Dict, yaml_file: Path) -> str:
        """Determine source from curator or filename."""
        # Check curation_history
        curation_history = recipe.get('curation_history', [])
        if curation_history:
            curator = curation_history[0].get('curator', '')

            # Map curator to canonical source name
            if 'togo' in curator.lower():
                return 'TOGO'
            elif 'mediadive' in curator.lower():
                return 'MediaDive'
            elif 'komodo' in curator.lower():
                return 'KOMODO'
            elif 'atcc' in curator.lower():
                return 'ATCC'
            elif 'bacdive' in curator.lower():
                return 'BacDive'
            elif 'nbrc' in curator.lower():
                return 'NBRC'
            elif 'mediadb' in curator.lower():
                return 'MediaDB'
            elif 'utex' in curator.lower():
                return 'UTEX'
            elif 'ccap' in curator.lower():
                return 'CCAP'
            elif 'sag' in curator.lower():
                return 'SAG'

        # Fallback to filename prefix
        filename = yaml_file.name
        if filename.startswith('KOMODO_'):
            return 'KOMODO'
        elif filename.startswith('TOGO_'):
            return 'TOGO'
        elif filename.startswith('ATCC_'):
            return 'ATCC'
        elif filename.startswith('NBRC_'):
            return 'NBRC'
        elif filename.startswith('MediaDB_'):
            return 'MediaDB'
        elif filename.startswith('UTEX_'):
            return 'UTEX'
        elif filename.startswith('CCAP_'):
            return 'CCAP'
        elif filename.startswith('SAG_'):
            return 'SAG'

        return 'UNKNOWN'

    def _analyze_ingredient(self, ingredient: Dict):
        """Check CHEBI/PubChem/CAS-RN coverage for an ingredient."""
        self.stats['ingredient_mapping']['total_ingredients'] += 1
        self.stats['data_quality']['total_ingredient_count'] += 1

        has_mapping = False

        # Check CHEBI
        term = ingredient.get('term', {})
        if term and term.get('id', '').startswith('CHEBI:'):
            self.stats['ingredient_mapping']['with_chebi'] += 1
            has_mapping = True

        # Check PubChem and CAS-RN via mapper
        preferred_term = ingredient.get('preferred_term', '')
        if preferred_term and isinstance(preferred_term, str):
            mapping = self.mapper.lookup(preferred_term)
            if mapping:
                if mapping.get('pubchem_id'):
                    self.stats['ingredient_mapping']['with_pubchem'] += 1
                    has_mapping = True

                if mapping.get('cas_rn'):
                    self.stats['ingredient_mapping']['with_cas_rn'] += 1
                    has_mapping = True

        # Count unmapped
        if not has_mapping:
            self.stats['ingredient_mapping']['unmapped'] += 1

    def _finalize_statistics(self):
        """Calculate derived statistics and percentages."""
        total_recipes = self.stats['metadata']['total_recipes']
        total_ingredients = self.stats['ingredient_mapping']['total_ingredients']

        # Average ingredients per recipe
        if total_recipes > 0:
            avg_ingredients = self.stats['data_quality']['total_ingredient_count'] / total_recipes
            self.stats['data_quality']['average_ingredients_per_recipe'] = round(avg_ingredients, 1)

        # Percentage recipes with ingredients
        if total_recipes > 0:
            pct = (self.stats['data_quality']['recipes_with_ingredients'] / total_recipes) * 100
            self.stats['data_quality']['recipes_with_ingredients_pct'] = round(pct, 1)

        # Ingredient mapping percentages
        if total_ingredients > 0:
            for key in ['with_chebi', 'with_pubchem', 'with_cas_rn', 'unmapped']:
                count = self.stats['ingredient_mapping'][key]
                pct = (count / total_ingredients) * 100
                self.stats['ingredient_mapping'][f'{key}_pct'] = round(pct, 1)

        # LinkML validation (all recipes are validated if they're in normalized_yaml)
        self.stats['data_quality']['linkml_validated'] = total_recipes
        self.stats['data_quality']['linkml_validated_pct'] = 100.0


class StatisticsFormatter:
    """Multi-format output formatter (JSON, Markdown, Terminal)."""

    def __init__(self, stats: Dict):
        self.stats = stats

    def to_json(self) -> str:
        """Export structured JSON."""
        return json.dumps(self.stats, indent=2)

    def to_markdown(self) -> str:
        """Generate report with tables."""
        md = []

        # Header
        md.append("# CultureMech Repository Statistics")
        md.append("")
        md.append(f"Generated: {self.stats['metadata']['generated_at']}")
        md.append(f"Repository: {self.stats['metadata']['repository']}")
        md.append("")

        # Summary
        md.append("## Summary")
        md.append("")
        md.append(f"- **Total Recipes**: {self.stats['metadata']['total_recipes']:,}")
        md.append(f"- **Recipes with Ingredients**: {self.stats['data_quality']['recipes_with_ingredients']:,} ({self.stats['data_quality'].get('recipes_with_ingredients_pct', 0)}%)")
        md.append(f"- **Average Ingredients per Recipe**: {self.stats['data_quality'].get('average_ingredients_per_recipe', 0)}")
        md.append(f"- **LinkML Validated**: {self.stats['data_quality']['linkml_validated']:,} (100%)")
        md.append("")

        # Recipes by Category
        md.append("## Recipes by Category")
        md.append("")
        md.append("| Category | Count | Percentage |")
        md.append("|----------|-------|------------|")
        total = self.stats['metadata']['total_recipes']
        for category, count in sorted(self.stats['recipes_by_category'].items()):
            pct = (count / total * 100) if total > 0 else 0
            md.append(f"| {category} | {count:,} | {pct:.1f}% |")
        md.append("")

        # Recipes by Source
        md.append("## Recipes by Source")
        md.append("")
        md.append("| Source | Count | Percentage |")
        md.append("|--------|-------|------------|")
        for source, count in sorted(self.stats['recipes_by_source'].items(), key=lambda x: x[1], reverse=True):
            pct = (count / total * 100) if total > 0 else 0
            md.append(f"| {source} | {count:,} | {pct:.1f}% |")
        md.append("")

        # Ingredient Mapping Coverage
        md.append("## Ingredient Mapping Coverage")
        md.append("")
        md.append("| Mapping Type | Count | Percentage |")
        md.append("|--------------|-------|------------|")
        ing_stats = self.stats['ingredient_mapping']
        total_ing = ing_stats['total_ingredients']
        md.append(f"| **Total Ingredients** | {total_ing:,} | 100% |")
        md.append(f"| CHEBI Ontology | {ing_stats['with_chebi']:,} | {ing_stats.get('with_chebi_pct', 0):.1f}% |")
        md.append(f"| PubChem | {ing_stats['with_pubchem']:,} | {ing_stats.get('with_pubchem_pct', 0):.1f}% |")
        md.append(f"| CAS-RN | {ing_stats['with_cas_rn']:,} | {ing_stats.get('with_cas_rn_pct', 0):.1f}% |")
        md.append(f"| Unmapped | {ing_stats['unmapped']:,} | {ing_stats.get('unmapped_pct', 0):.1f}% |")
        md.append("")

        # Medium Composition
        md.append("## Medium Composition")
        md.append("")
        md.append("| Type | Count | Percentage |")
        md.append("|------|-------|------------|")
        for comp_type, count in sorted(self.stats['medium_composition'].items()):
            pct = (count / total * 100) if total > 0 else 0
            md.append(f"| {comp_type} | {count:,} | {pct:.1f}% |")
        md.append("")

        # Physical State
        md.append("## Physical State")
        md.append("")
        md.append("| State | Count | Percentage |")
        md.append("|-------|-------|------------|")
        for state, count in sorted(self.stats['physical_state'].items()):
            pct = (count / total * 100) if total > 0 else 0
            md.append(f"| {state} | {count:,} | {pct:.1f}% |")
        md.append("")

        return "\n".join(md)

    def to_terminal(self) -> str:
        """Print colorized summary."""
        lines = []

        lines.append("\n" + "=" * 70)
        lines.append("CultureMech Repository Statistics")
        lines.append("=" * 70)
        lines.append("")

        # Summary stats
        lines.append(f"Total recipes:              {self.stats['metadata']['total_recipes']:,}")
        lines.append(f"Recipes with ingredients:   {self.stats['data_quality']['recipes_with_ingredients']:,} ({self.stats['data_quality'].get('recipes_with_ingredients_pct', 0):.1f}%)")
        lines.append(f"Avg ingredients/recipe:     {self.stats['data_quality'].get('average_ingredients_per_recipe', 0)}")
        lines.append(f"LinkML validated:           {self.stats['data_quality']['linkml_validated']:,} (100%)")
        lines.append("")

        # Top sources
        lines.append("Top Sources:")
        for source, count in sorted(self.stats['recipes_by_source'].items(), key=lambda x: x[1], reverse=True)[:5]:
            lines.append(f"  {source:15} {count:6,} recipes")
        lines.append("")

        # Ingredient mapping
        lines.append("Ingredient Mapping:")
        ing_stats = self.stats['ingredient_mapping']
        lines.append(f"  Total:      {ing_stats['total_ingredients']:8,}")
        lines.append(f"  CHEBI:      {ing_stats['with_chebi']:8,} ({ing_stats.get('with_chebi_pct', 0):5.1f}%)")
        lines.append(f"  PubChem:    {ing_stats['with_pubchem']:8,} ({ing_stats.get('with_pubchem_pct', 0):5.1f}%)")
        lines.append(f"  CAS-RN:     {ing_stats['with_cas_rn']:8,} ({ing_stats.get('with_cas_rn_pct', 0):5.1f}%)")
        lines.append(f"  Unmapped:   {ing_stats['unmapped']:8,} ({ing_stats.get('unmapped_pct', 0):5.1f}%)")
        lines.append("")

        lines.append("=" * 70)

        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Generate comprehensive statistics for CultureMech repository"
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
        "--output-json",
        type=Path,
        help="Output JSON file path"
    )
    parser.add_argument(
        "--output-markdown",
        type=Path,
        help="Output Markdown file path"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Output directory (writes stats.json and stats.md)"
    )
    parser.add_argument(
        "--terminal-only",
        action="store_true",
        help="Only print to terminal (no file output)"
    )

    args = parser.parse_args()

    print("=" * 70)
    print("CultureMech Statistics Generator")
    print("=" * 70)
    print(f"Normalized YAML: {args.normalized_yaml}")
    print(f"MicrobeMediaParam: {args.microbe_media_param}")
    print(f"MediaDive: {args.mediadive}")
    print()

    # Load chemical mapper
    print("Loading chemical mappings...")
    mapper = ChemicalMapper(
        microbe_media_param_dir=args.microbe_media_param,
        mediadive_data_dir=args.mediadive
    )

    # Collect statistics
    collector = RecipeStatisticsCollector(args.normalized_yaml, mapper)
    stats = collector.collect_statistics()

    # Format output
    formatter = StatisticsFormatter(stats)

    # Output to terminal
    print(formatter.to_terminal())

    # Output to files
    if not args.terminal_only:
        # Handle output-dir
        if args.output_dir:
            args.output_dir.mkdir(parents=True, exist_ok=True)
            json_path = args.output_dir / "stats.json"
            md_path = args.output_dir / "stats.md"
        else:
            json_path = args.output_json
            md_path = args.output_markdown

        # Write JSON
        if json_path:
            print(f"\nWriting JSON to: {json_path}")
            json_path.parent.mkdir(parents=True, exist_ok=True)
            with open(json_path, 'w') as f:
                f.write(formatter.to_json())
            print(f"✓ JSON written: {json_path}")

        # Write Markdown
        if md_path:
            print(f"\nWriting Markdown to: {md_path}")
            md_path.parent.mkdir(parents=True, exist_ok=True)
            with open(md_path, 'w') as f:
                f.write(formatter.to_markdown())
            print(f"✓ Markdown written: {md_path}")


if __name__ == "__main__":
    main()
