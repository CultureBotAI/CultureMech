#!/usr/bin/env python3
"""
Validate ingredient hierarchy integration in CultureMech recipes.

Usage:
    python scripts/validate_hierarchy_integration.py \
        --mim-repo /path/to/MediaIngredientMech \
        --yaml-dir data/normalized_yaml \
        --report-output validation_report.yaml
"""

import argparse
import logging
import sys
import time
from collections import defaultdict
from pathlib import Path
from typing import Any, Dict, List, Set

import yaml

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from culturemech.enrich.hierarchy_importer import MediaIngredientMechHierarchyImporter

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class HierarchyValidator:
    """Validate hierarchy integration in CultureMech recipes."""

    def __init__(self, hierarchy_importer: MediaIngredientMechHierarchyImporter):
        """
        Initialize validator.

        Args:
            hierarchy_importer: MediaIngredientMechHierarchyImporter with loaded data
        """
        self.importer = hierarchy_importer
        self.issues: List[Dict[str, Any]] = []
        self.stats = {
            'files_checked': 0,
            'ingredients_checked': 0,
            'ingredients_with_hierarchy': 0,
            'ingredients_with_roles': 0,
            'valid_parent_refs': 0,
            'invalid_parent_refs': 0,
            'orphaned_refs': 0,
            'circular_refs': 0,
            'valid_variant_types': 0,
            'invalid_variant_types': 0,
            'valid_roles': 0,
            'invalid_roles': 0,
            'errors': 0
        }

        # Valid variant types from schema
        self.valid_variant_types = {
            'HYDRATE', 'SALT_FORM', 'ANHYDROUS',
            'NAMED_HYDRATE', 'CHEMICAL_VARIANT'
        }

        # Valid roles from schema
        self.valid_roles = {
            'CARBON_SOURCE', 'NITROGEN_SOURCE', 'MINERAL',
            'TRACE_ELEMENT', 'BUFFER', 'VITAMIN_SOURCE',
            'SALT', 'PROTEIN_SOURCE', 'AMINO_ACID_SOURCE',
            'SOLIDIFYING_AGENT', 'ENERGY_SOURCE',
            'ELECTRON_ACCEPTOR', 'ELECTRON_DONOR',
            'COFACTOR_PROVIDER'
        }

    def validate_ingredient(
        self,
        ingredient: Dict[str, Any],
        recipe_name: str
    ) -> List[Dict[str, Any]]:
        """
        Validate single ingredient's hierarchy fields.

        Args:
            ingredient: Ingredient descriptor dict
            recipe_name: Name of containing recipe

        Returns:
            List of validation issues found
        """
        issues = []
        self.stats['ingredients_checked'] += 1

        ingredient_name = ingredient.get('preferred_term', 'unknown')

        # Check parent_ingredient field
        if 'parent_ingredient' in ingredient:
            self.stats['ingredients_with_hierarchy'] += 1
            parent_ingredient = ingredient['parent_ingredient']

            # Validate structure
            if not isinstance(parent_ingredient, dict):
                issues.append({
                    'type': 'invalid_parent_structure',
                    'recipe': recipe_name,
                    'ingredient': ingredient_name,
                    'message': 'parent_ingredient must be a dict'
                })
            else:
                # Check required fields
                if 'preferred_term' not in parent_ingredient:
                    issues.append({
                        'type': 'missing_parent_name',
                        'recipe': recipe_name,
                        'ingredient': ingredient_name,
                        'message': 'parent_ingredient missing preferred_term'
                    })

                parent_id = parent_ingredient.get('mediaingredientmech_id')
                if not parent_id:
                    issues.append({
                        'type': 'missing_parent_id',
                        'recipe': recipe_name,
                        'ingredient': ingredient_name,
                        'message': 'parent_ingredient missing mediaingredientmech_id'
                    })
                elif parent_id:
                    # Validate parent exists in hierarchy
                    parent_info = self.importer.get_ingredient_info(parent_id)
                    if parent_info:
                        self.stats['valid_parent_refs'] += 1

                        # Check for circular references
                        if self._has_circular_reference(ingredient, parent_id):
                            issues.append({
                                'type': 'circular_reference',
                                'recipe': recipe_name,
                                'ingredient': ingredient_name,
                                'parent_id': parent_id,
                                'message': 'Circular parent-child relationship detected'
                            })
                            self.stats['circular_refs'] += 1
                    else:
                        issues.append({
                            'type': 'orphaned_parent_reference',
                            'recipe': recipe_name,
                            'ingredient': ingredient_name,
                            'parent_id': parent_id,
                            'message': f'Parent ID {parent_id} not found in MediaIngredientMech'
                        })
                        self.stats['orphaned_refs'] += 1
                        self.stats['invalid_parent_refs'] += 1

        # Check variant_type field
        if 'variant_type' in ingredient:
            variant_type = ingredient['variant_type']

            if variant_type not in self.valid_variant_types:
                issues.append({
                    'type': 'invalid_variant_type',
                    'recipe': recipe_name,
                    'ingredient': ingredient_name,
                    'variant_type': variant_type,
                    'message': f'Invalid variant_type: {variant_type}',
                    'valid_values': list(self.valid_variant_types)
                })
                self.stats['invalid_variant_types'] += 1
            else:
                self.stats['valid_variant_types'] += 1

        # Check role field
        if 'role' in ingredient:
            self.stats['ingredients_with_roles'] += 1
            roles = ingredient['role']

            if not isinstance(roles, list):
                issues.append({
                    'type': 'invalid_role_structure',
                    'recipe': recipe_name,
                    'ingredient': ingredient_name,
                    'message': 'role must be a list'
                })
            else:
                for role in roles:
                    if role not in self.valid_roles:
                        issues.append({
                            'type': 'invalid_role_value',
                            'recipe': recipe_name,
                            'ingredient': ingredient_name,
                            'role': role,
                            'message': f'Invalid role: {role}',
                            'valid_values': list(self.valid_roles)
                        })
                        self.stats['invalid_roles'] += 1
                    else:
                        self.stats['valid_roles'] += 1

        return issues

    def _has_circular_reference(
        self,
        ingredient: Dict[str, Any],
        parent_id: str,
        visited: Optional[Set[str]] = None
    ) -> bool:
        """
        Check for circular parent-child references.

        Args:
            ingredient: Ingredient descriptor dict
            parent_id: Parent MediaIngredientMech ID
            visited: Set of visited IDs (for recursion)

        Returns:
            True if circular reference detected
        """
        if visited is None:
            visited = set()

        # Get ingredient's MIM ID
        mim_term = ingredient.get('mediaingredientmech_term')
        if not mim_term:
            return False

        mim_id = mim_term.get('id') if isinstance(mim_term, dict) else None
        if not mim_id:
            return False

        # Check if we've seen this ID before (circular)
        if mim_id in visited:
            return True

        visited.add(mim_id)

        # Check if parent is in visited set
        if parent_id in visited:
            return True

        return False

    def validate_recipe(self, recipe_path: Path) -> List[Dict[str, Any]]:
        """
        Validate all ingredients in a recipe.

        Args:
            recipe_path: Path to recipe YAML file

        Returns:
            List of validation issues found
        """
        try:
            with open(recipe_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)

            if not data:
                return []

            recipe_name = data.get('name', recipe_path.stem)
            issues = []

            # Validate direct ingredients
            ingredients = data.get('ingredients', [])
            if isinstance(ingredients, list):
                for ingredient in ingredients:
                    if isinstance(ingredient, dict):
                        issues.extend(self.validate_ingredient(ingredient, recipe_name))

            # Validate solution ingredients
            solutions = data.get('solutions', [])
            if isinstance(solutions, list):
                for solution in solutions:
                    if isinstance(solution, dict):
                        composition = solution.get('composition', [])
                        if isinstance(composition, list):
                            for ingredient in composition:
                                if isinstance(ingredient, dict):
                                    issues.extend(
                                        self.validate_ingredient(ingredient, recipe_name)
                                    )

            self.stats['files_checked'] += 1
            return issues

        except Exception as e:
            logger.error(f"  ✗ Failed to validate {recipe_path.name}: {e}")
            self.stats['errors'] += 1
            return [{
                'type': 'file_error',
                'recipe': str(recipe_path),
                'message': str(e)
            }]

    def run_validation(
        self,
        yaml_dir: Path,
        category: Optional[str] = None,
        limit: Optional[int] = None
    ) -> Dict[str, Any]:
        """
        Validate all recipes in directory.

        Args:
            yaml_dir: Directory containing normalized YAML files
            category: Optional category filter
            limit: Optional limit on number of files

        Returns:
            Dictionary with validation results
        """
        logger.info("=" * 60)
        logger.info("Hierarchy Integration Validation")
        logger.info("=" * 60)

        # Find recipe files
        if category:
            pattern = f"{category}/**/*.yaml"
            logger.info(f"Validating category: {category}")
        else:
            pattern = "**/*.yaml"
            logger.info("Validating all categories")

        yaml_files = list(yaml_dir.glob(pattern))
        logger.info(f"Found {len(yaml_files)} recipe files")

        if limit:
            yaml_files = yaml_files[:limit]
            logger.info(f"Limited to {limit} files for testing")

        # Validate files
        all_issues = []
        for i, yaml_file in enumerate(yaml_files, 1):
            if i % 100 == 0:
                logger.info(f"Progress: {i}/{len(yaml_files)} files validated...")

            issues = self.validate_recipe(yaml_file)
            all_issues.extend(issues)

        self.issues = all_issues

        # Print summary
        logger.info("\n" + "=" * 60)
        logger.info("Validation Complete")
        logger.info("=" * 60)
        logger.info(f"Files checked: {self.stats['files_checked']}")
        logger.info(f"Ingredients checked: {self.stats['ingredients_checked']}")
        logger.info(f"Ingredients with hierarchy: {self.stats['ingredients_with_hierarchy']}")
        logger.info(f"Ingredients with roles: {self.stats['ingredients_with_roles']}")
        logger.info("")
        logger.info(f"Valid parent references: {self.stats['valid_parent_refs']}")
        logger.info(f"Invalid parent references: {self.stats['invalid_parent_refs']}")
        logger.info(f"Orphaned references: {self.stats['orphaned_refs']}")
        logger.info(f"Circular references: {self.stats['circular_refs']}")
        logger.info("")
        logger.info(f"Valid variant types: {self.stats['valid_variant_types']}")
        logger.info(f"Invalid variant types: {self.stats['invalid_variant_types']}")
        logger.info("")
        logger.info(f"Valid roles: {self.stats['valid_roles']}")
        logger.info(f"Invalid roles: {self.stats['invalid_roles']}")

        if self.stats['errors'] > 0:
            logger.warning(f"File errors: {self.stats['errors']}")

        # Calculate coverage
        if self.stats['ingredients_checked'] > 0:
            hierarchy_coverage = (
                self.stats['ingredients_with_hierarchy'] /
                self.stats['ingredients_checked']
            ) * 100
            role_coverage = (
                self.stats['ingredients_with_roles'] /
                self.stats['ingredients_checked']
            ) * 100

            logger.info("")
            logger.info(f"Hierarchy coverage: {hierarchy_coverage:.1f}%")
            logger.info(f"Role coverage: {role_coverage:.1f}%")

        # Determine overall status
        total_issues = len(all_issues)
        if total_issues == 0:
            logger.info("\n✓ All validations passed!")
        else:
            logger.warning(f"\n✗ Found {total_issues} validation issues")

        logger.info("=" * 60)

        return {
            'stats': self.stats,
            'issues': all_issues,
            'issue_counts': self._count_issues_by_type(all_issues)
        }

    def _count_issues_by_type(self, issues: List[Dict[str, Any]]) -> Dict[str, int]:
        """Count issues by type."""
        counts = defaultdict(int)
        for issue in issues:
            counts[issue.get('type', 'unknown')] += 1
        return dict(counts)

    def generate_report(self, output_path: Path):
        """
        Generate validation report.

        Args:
            output_path: Path to save report YAML
        """
        report = {
            'generation_date': time.strftime("%Y-%m-%dT%H:%M:%S.000000Z", time.gmtime()),
            'stats': self.stats,
            'issue_counts': self._count_issues_by_type(self.issues),
            'issues': self.issues[:100],  # First 100 issues for review
            'hierarchy_stats': self.importer.get_stats()
        }

        with open(output_path, 'w', encoding='utf-8') as f:
            yaml.dump(report, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

        logger.info(f"Validation report saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Validate hierarchy integration in CultureMech recipes",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        "--mim-repo",
        type=Path,
        required=True,
        help="Path to MediaIngredientMech repository"
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
        help="Validate only specific category"
    )

    parser.add_argument(
        "--limit",
        type=int,
        help="Limit number of files to validate (for testing)"
    )

    parser.add_argument(
        "--report-output",
        type=Path,
        help="Path to save validation report YAML"
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
    if not args.mim_repo.exists():
        logger.error(f"MediaIngredientMech repository not found: {args.mim_repo}")
        return 1

    if not args.yaml_dir.exists():
        logger.error(f"YAML directory not found: {args.yaml_dir}")
        return 1

    try:
        # Load hierarchy
        logger.info("Loading MediaIngredientMech hierarchy...")
        importer = MediaIngredientMechHierarchyImporter(args.mim_repo)
        importer.load_hierarchy()

        # Create validator
        validator = HierarchyValidator(importer)

        # Run validation
        result = validator.run_validation(
            yaml_dir=args.yaml_dir,
            category=args.category,
            limit=args.limit
        )

        # Save report if requested
        if args.report_output:
            validator.generate_report(args.report_output)

        # Return exit code based on issues
        total_issues = len(result['issues'])
        if total_issues > 0:
            logger.warning(f"Validation completed with {total_issues} issues")
            return 1

        logger.info("Validation completed successfully")
        return 0

    except Exception as e:
        logger.error(f"Validation failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
