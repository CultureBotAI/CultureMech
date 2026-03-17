#!/usr/bin/env python3
"""
Generate human-readable hierarchy report for CultureMech ingredients.

Usage:
    python scripts/generate_hierarchy_report.py \
        --yaml-dir data/normalized_yaml \
        --output docs/ingredient_hierarchy.md
"""

import argparse
import logging
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Set

import yaml

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class HierarchyReporter:
    """Generate hierarchy report from CultureMech recipes."""

    def __init__(self):
        """Initialize reporter."""
        self.stats = {
            'files_analyzed': 0,
            'ingredients_analyzed': 0,
            'ingredients_with_hierarchy': 0,
            'ingredients_with_roles': 0,
            'unique_parents': set(),
            'variant_types': Counter(),
            'roles': Counter(),
            'ingredients_per_parent': defaultdict(list)
        }
        self.unmatched_ingredients: List[Dict[str, Any]] = []

    def analyze_ingredient(
        self,
        ingredient: Dict[str, Any],
        recipe_name: str
    ):
        """
        Analyze single ingredient for reporting.

        Args:
            ingredient: Ingredient descriptor dict
            recipe_name: Name of containing recipe
        """
        self.stats['ingredients_analyzed'] += 1

        ingredient_name = ingredient.get('preferred_term', 'unknown')
        mim_id = None

        # Get MIM ID
        mim_term = ingredient.get('mediaingredientmech_term')
        if mim_term and isinstance(mim_term, dict):
            mim_id = mim_term.get('id')

        # Check hierarchy fields
        if 'parent_ingredient' in ingredient:
            self.stats['ingredients_with_hierarchy'] += 1
            parent_ingredient = ingredient['parent_ingredient']

            if isinstance(parent_ingredient, dict):
                parent_name = parent_ingredient.get('preferred_term', 'unknown')
                parent_id = parent_ingredient.get('mediaingredientmech_id')

                if parent_id:
                    self.stats['unique_parents'].add(parent_id)
                    self.stats['ingredients_per_parent'][parent_id].append({
                        'name': ingredient_name,
                        'mim_id': mim_id,
                        'recipe': recipe_name
                    })

        # Track variant types
        if 'variant_type' in ingredient:
            variant_type = ingredient['variant_type']
            self.stats['variant_types'][variant_type] += 1

        # Track roles
        if 'role' in ingredient:
            self.stats['ingredients_with_roles'] += 1
            roles = ingredient['role']

            if isinstance(roles, list):
                for role in roles:
                    self.stats['roles'][role] += 1
        else:
            # Track unmatched ingredients
            if mim_id and 'parent_ingredient' not in ingredient:
                self.unmatched_ingredients.append({
                    'name': ingredient_name,
                    'mim_id': mim_id,
                    'recipe': recipe_name
                })

    def analyze_recipe(self, recipe_path: Path):
        """
        Analyze all ingredients in a recipe.

        Args:
            recipe_path: Path to recipe YAML file
        """
        try:
            with open(recipe_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            if not data:
                return

            recipe_name = data.get('name', recipe_path.stem)

            # Analyze direct ingredients
            ingredients = data.get('ingredients', [])
            if isinstance(ingredients, list):
                for ingredient in ingredients:
                    if isinstance(ingredient, dict):
                        self.analyze_ingredient(ingredient, recipe_name)

            # Analyze solution ingredients
            solutions = data.get('solutions', [])
            if isinstance(solutions, list):
                for solution in solutions:
                    if isinstance(solution, dict):
                        composition = solution.get('composition', [])
                        if isinstance(composition, list):
                            for ingredient in composition:
                                if isinstance(ingredient, dict):
                                    self.analyze_ingredient(ingredient, recipe_name)

            self.stats['files_analyzed'] += 1

        except Exception as e:
            logger.error(f"  ✗ Failed to analyze {recipe_path.name}: {e}")

    def run_analysis(
        self,
        yaml_dir: Path,
        category: str = None,
        limit: int = None
    ):
        """
        Analyze all recipes in directory.

        Args:
            yaml_dir: Directory containing normalized YAML files
            category: Optional category filter
            limit: Optional limit on number of files
        """
        logger.info("=" * 60)
        logger.info("Hierarchy Report Generation")
        logger.info("=" * 60)

        # Find recipe files
        if category:
            pattern = f"{category}/**/*.yaml"
            logger.info(f"Analyzing category: {category}")
        else:
            pattern = "**/*.yaml"
            logger.info("Analyzing all categories")

        yaml_files = list(yaml_dir.glob(pattern))
        logger.info(f"Found {len(yaml_files)} recipe files")

        if limit:
            yaml_files = yaml_files[:limit]
            logger.info(f"Limited to {limit} files for testing")

        # Analyze files
        for i, yaml_file in enumerate(yaml_files, 1):
            if i % 100 == 0:
                logger.info(f"Progress: {i}/{len(yaml_files)} files analyzed...")

            self.analyze_recipe(yaml_file)

        logger.info("\n" + "=" * 60)
        logger.info("Analysis Complete")
        logger.info("=" * 60)
        logger.info(f"Files analyzed: {self.stats['files_analyzed']}")
        logger.info(f"Ingredients analyzed: {self.stats['ingredients_analyzed']}")
        logger.info(f"Ingredients with hierarchy: {self.stats['ingredients_with_hierarchy']}")
        logger.info(f"Ingredients with roles: {self.stats['ingredients_with_roles']}")
        logger.info(f"Unique parent ingredients: {len(self.stats['unique_parents'])}")
        logger.info("=" * 60)

    def generate_markdown_report(self, output_path: Path):
        """
        Generate Markdown report.

        Args:
            output_path: Path to save Markdown report
        """
        logger.info(f"Generating Markdown report: {output_path}")

        with open(output_path, 'w', encoding='utf-8') as f:
            # Header
            f.write("# CultureMech Ingredient Hierarchy Report\n\n")
            f.write(f"*Generated: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}*\n\n")

            # Overview
            f.write("## Overview\n\n")
            f.write(f"- **Files analyzed**: {self.stats['files_analyzed']}\n")
            f.write(f"- **Total ingredients**: {self.stats['ingredients_analyzed']}\n")
            f.write(f"- **Ingredients with hierarchy**: {self.stats['ingredients_with_hierarchy']}\n")
            f.write(f"- **Ingredients with roles**: {self.stats['ingredients_with_roles']}\n")
            f.write(f"- **Unique parent ingredients**: {len(self.stats['unique_parents'])}\n\n")

            # Calculate coverage
            if self.stats['ingredients_analyzed'] > 0:
                hierarchy_coverage = (
                    self.stats['ingredients_with_hierarchy'] /
                    self.stats['ingredients_analyzed']
                ) * 100
                role_coverage = (
                    self.stats['ingredients_with_roles'] /
                    self.stats['ingredients_analyzed']
                ) * 100

                f.write(f"- **Hierarchy coverage**: {hierarchy_coverage:.1f}%\n")
                f.write(f"- **Role coverage**: {role_coverage:.1f}%\n\n")

            # Variant type distribution
            f.write("## Variant Type Distribution\n\n")
            if self.stats['variant_types']:
                f.write("| Variant Type | Count | Percentage |\n")
                f.write("|--------------|-------|------------|\n")

                total_variants = sum(self.stats['variant_types'].values())
                for variant_type, count in self.stats['variant_types'].most_common():
                    percentage = (count / total_variants) * 100
                    f.write(f"| {variant_type} | {count} | {percentage:.1f}% |\n")
                f.write("\n")
            else:
                f.write("*No variant type data available*\n\n")

            # Role distribution
            f.write("## Role Distribution\n\n")
            if self.stats['roles']:
                f.write("| Role | Count | Percentage |\n")
                f.write("|------|-------|------------|\n")

                total_roles = sum(self.stats['roles'].values())
                for role, count in self.stats['roles'].most_common():
                    percentage = (count / total_roles) * 100
                    f.write(f"| {role} | {count} | {percentage:.1f}% |\n")
                f.write("\n")
            else:
                f.write("*No role data available*\n\n")

            # Top ingredient families
            f.write("## Top Ingredient Families by Occurrence\n\n")
            if self.stats['ingredients_per_parent']:
                # Sort by number of children
                sorted_parents = sorted(
                    self.stats['ingredients_per_parent'].items(),
                    key=lambda x: len(x[1]),
                    reverse=True
                )

                f.write("| Parent ID | Number of Variants | Sample Variants |\n")
                f.write("|-----------|-------------------|----------------|\n")

                for parent_id, children in sorted_parents[:20]:  # Top 20
                    num_children = len(children)
                    sample_names = ', '.join(
                        child['name'] for child in children[:3]
                    )
                    if num_children > 3:
                        sample_names += f", ... ({num_children - 3} more)"

                    f.write(f"| {parent_id} | {num_children} | {sample_names} |\n")
                f.write("\n")
            else:
                f.write("*No family data available*\n\n")

            # Unmatched ingredients
            if self.unmatched_ingredients:
                f.write("## Unmatched Ingredients Needing Curation\n\n")
                f.write(f"*{len(self.unmatched_ingredients)} ingredients with MediaIngredientMech ID "
                       f"but no parent assignment*\n\n")

                if len(self.unmatched_ingredients) <= 50:
                    f.write("| Ingredient Name | MediaIngredientMech ID | Sample Recipe |\n")
                    f.write("|----------------|------------------------|---------------|\n")

                    for item in self.unmatched_ingredients:
                        f.write(f"| {item['name']} | {item['mim_id']} | {item['recipe']} |\n")
                    f.write("\n")
                else:
                    f.write("| Ingredient Name | MediaIngredientMech ID | Sample Recipe |\n")
                    f.write("|----------------|------------------------|---------------|\n")

                    for item in self.unmatched_ingredients[:50]:
                        f.write(f"| {item['name']} | {item['mim_id']} | {item['recipe']} |\n")
                    f.write(f"\n*Showing first 50 of {len(self.unmatched_ingredients)} unmatched ingredients*\n\n")

            # Footer
            f.write("---\n\n")
            f.write("*This report is automatically generated from CultureMech recipe data. ")
            f.write("Parent-child relationships and roles are imported from MediaIngredientMech.*\n")

        logger.info(f"Report saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate ingredient hierarchy report",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "--yaml-dir",
        type=Path,
        default=Path("data/normalized_yaml"),
        help="Directory containing normalized YAML files"
    )

    parser.add_argument(
        "--category",
        type=str,
        choices=["bacterial", "fungal", "archaea", "specialized", "algae"],
        help="Analyze only specific category"
    )

    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of files to analyze (for testing)"
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=Path("docs/ingredient_hierarchy.md"),
        help="Path to save Markdown report (default: docs/ingredient_hierarchy.md)"
    )

    parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Enable verbose logging"
    )

    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    # Validate paths
    if not args.yaml_dir.exists():
        logger.error(f"YAML directory not found: {args.yaml_dir}")
        return 1

    # Create output directory if needed
    args.output.parent.mkdir(parents=True, exist_ok=True)

    try:
        # Create reporter
        reporter = HierarchyReporter()

        # Run analysis
        reporter.run_analysis(
            yaml_dir=args.yaml_dir,
            category=args.category,
            limit=args.limit
        )

        # Generate report
        reporter.generate_markdown_report(args.output)

        logger.info("\n✓ Report generation completed successfully")
        return 0

    except Exception as e:
        logger.error(f"Report generation failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
