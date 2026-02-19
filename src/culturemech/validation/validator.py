"""Recipe validation with LinkML schema and error categorization.

Validates recipes against the CultureMech schema and categorizes validation
errors for reporting and fixing prioritization.
"""

import logging
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

import yaml

logger = logging.getLogger(__name__)


@dataclass
class ValidationReport:
    """Report of validation results for a single recipe.

    Attributes:
        recipe_path: Path to recipe file
        is_valid: Whether recipe passes validation
        yaml_error: YAML parsing error if present
        schema_errors: List of schema validation errors
        fixable: Whether errors can be automatically fixed
        error_category: Primary error category
        warnings: Non-fatal warnings
    """
    recipe_path: Path
    is_valid: bool = False
    yaml_error: Optional[str] = None
    schema_errors: List[str] = field(default_factory=list)
    fixable: bool = False
    error_category: str = "unknown"
    warnings: List[str] = field(default_factory=list)


class RecipeValidator:
    """Validate recipes against CultureMech schema.

    Provides:
    - YAML parsing validation
    - Schema validation (when LinkML available)
    - Error categorization
    - Fixability assessment
    """

    # Error categories and their fixability
    ERROR_CATEGORIES = {
        'yaml_parse': {'fixable_rate': 0.85, 'description': 'YAML parsing errors'},
        'missing_required': {'fixable_rate': 0.90, 'description': 'Missing required fields'},
        'invalid_enum': {'fixable_rate': 0.95, 'description': 'Invalid enum values'},
        'type_mismatch': {'fixable_rate': 0.80, 'description': 'Type mismatches'},
        'empty_ingredients': {'fixable_rate': 0.0, 'description': 'Empty ingredients list'},
        'placeholder': {'fixable_rate': 0.0, 'description': 'Placeholder ingredients'},
        'structural': {'fixable_rate': 0.30, 'description': 'Structural problems'},
        'unknown': {'fixable_rate': 0.20, 'description': 'Unknown errors'},
    }

    def __init__(self, schema_path: Optional[Path] = None):
        """Initialize validator.

        Args:
            schema_path: Path to LinkML schema file (optional)
        """
        self.schema_path = schema_path
        self.schema_validator = None

        # Try to load LinkML validator if available
        if schema_path and schema_path.exists():
            try:
                # Import LinkML if available
                from linkml.validators import JsonschemaValidator
                from linkml_runtime.loaders import yaml_loader

                self.schema_validator = JsonschemaValidator(str(schema_path))
                logger.info(f"Loaded LinkML schema: {schema_path}")
            except ImportError:
                logger.warning("LinkML not available, schema validation disabled")
            except Exception as e:
                logger.warning(f"Could not load schema: {e}")

    def validate_file(self, recipe_path: Path) -> ValidationReport:
        """Validate a recipe file.

        Args:
            recipe_path: Path to recipe YAML file

        Returns:
            ValidationReport with results
        """
        report = ValidationReport(recipe_path=recipe_path)

        # Step 1: Try to load YAML
        try:
            with open(recipe_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()

            # Try to parse
            try:
                recipe = yaml.safe_load(content)
            except yaml.YAMLError as e:
                report.yaml_error = str(e)
                report.error_category = 'yaml_parse'
                report.fixable = True  # YAML errors are often fixable
                return report

            # Validate that it's a dict
            if not isinstance(recipe, dict):
                report.yaml_error = "Recipe is not a dictionary"
                report.error_category = 'structural'
                report.fixable = False
                return report

        except FileNotFoundError:
            report.yaml_error = "File not found"
            report.error_category = 'unknown'
            report.fixable = False
            return report
        except Exception as e:
            report.yaml_error = str(e)
            report.error_category = 'unknown'
            report.fixable = False
            return report

        # Step 2: Basic structural checks
        structural_errors = self._check_structure(recipe)
        if structural_errors:
            report.schema_errors.extend(structural_errors)
            report.error_category = self._categorize_errors(structural_errors)
            report.fixable = self._assess_fixability(report.error_category)
            return report

        # Step 3: Schema validation (if available)
        if self.schema_validator:
            schema_errors = self._validate_schema(recipe)
            if schema_errors:
                report.schema_errors.extend(schema_errors)
                report.error_category = self._categorize_errors(schema_errors)
                report.fixable = self._assess_fixability(report.error_category)
                return report

        # All checks passed
        report.is_valid = True
        return report

    def _check_structure(self, recipe: Dict) -> List[str]:
        """Check basic recipe structure.

        Args:
            recipe: Recipe dictionary

        Returns:
            List of error messages
        """
        errors = []

        # Check required top-level fields
        if 'name' not in recipe:
            errors.append("Missing required field: name")

        if 'ingredients' not in recipe:
            errors.append("Missing required field: ingredients")
        elif not isinstance(recipe['ingredients'], list):
            errors.append("Field 'ingredients' must be a list")
        elif len(recipe['ingredients']) == 0:
            errors.append("Empty ingredients list")

        # Check ingredient structure
        if 'ingredients' in recipe and isinstance(recipe['ingredients'], list):
            for i, ing in enumerate(recipe['ingredients']):
                if not isinstance(ing, dict):
                    errors.append(f"Ingredient {i} is not a dictionary")
                    continue

                if 'preferred_term' not in ing:
                    errors.append(f"Ingredient {i}: missing preferred_term")

                if 'concentration' not in ing:
                    errors.append(f"Ingredient {i}: missing required field 'concentration'")
                elif isinstance(ing['concentration'], dict):
                    conc = ing['concentration']
                    if 'value' not in conc:
                        errors.append(f"Ingredient {i}: concentration missing 'value'")
                    if 'unit' not in conc:
                        errors.append(f"Ingredient {i}: concentration missing 'unit'")

        return errors

    def _validate_schema(self, recipe: Dict) -> List[str]:
        """Validate recipe against LinkML schema.

        Args:
            recipe: Recipe dictionary

        Returns:
            List of validation errors
        """
        if not self.schema_validator:
            return []

        errors = []
        try:
            # Validate using LinkML
            self.schema_validator.validate(recipe)
        except Exception as e:
            # Parse validation errors
            error_msg = str(e)
            # Split into individual errors if multiple
            if '\n' in error_msg:
                errors.extend(error_msg.split('\n'))
            else:
                errors.append(error_msg)

        return errors

    def _categorize_errors(self, errors: List[str]) -> str:
        """Categorize error messages.

        Args:
            errors: List of error messages

        Returns:
            Primary error category
        """
        if not errors:
            return 'unknown'

        # Check for specific patterns
        error_text = ' '.join(errors).lower()

        if 'empty ingredients' in error_text:
            return 'empty_ingredients'
        elif 'placeholder' in error_text or 'see source' in error_text:
            return 'placeholder'
        elif 'missing required' in error_text or 'missing' in error_text:
            return 'missing_required'
        elif 'enum' in error_text or 'not in permissible' in error_text:
            return 'invalid_enum'
        elif 'type' in error_text or 'expected' in error_text:
            return 'type_mismatch'
        elif 'parse' in error_text or 'yaml' in error_text:
            return 'yaml_parse'
        elif 'structure' in error_text or 'dict' in error_text:
            return 'structural'
        else:
            return 'unknown'

    def _assess_fixability(self, category: str) -> bool:
        """Assess if error category is likely fixable.

        Args:
            category: Error category

        Returns:
            True if likely fixable automatically
        """
        if category in self.ERROR_CATEGORIES:
            fixable_rate = self.ERROR_CATEGORIES[category]['fixable_rate']
            return fixable_rate >= 0.5
        return False

    def generate_summary(self, reports: List[ValidationReport]) -> Dict:
        """Generate summary statistics from validation reports.

        Args:
            reports: List of validation reports

        Returns:
            Dictionary of summary statistics
        """
        summary = {
            'total': len(reports),
            'valid': 0,
            'invalid': 0,
            'fixable': 0,
            'unfixable': 0,
            'by_category': {},
        }

        for report in reports:
            if report.is_valid:
                summary['valid'] += 1
            else:
                summary['invalid'] += 1

                if report.fixable:
                    summary['fixable'] += 1
                else:
                    summary['unfixable'] += 1

                # Count by category
                category = report.error_category
                if category not in summary['by_category']:
                    summary['by_category'][category] = {
                        'count': 0,
                        'fixable': 0,
                        'description': self.ERROR_CATEGORIES.get(
                            category, {}
                        ).get('description', 'Unknown')
                    }
                summary['by_category'][category]['count'] += 1
                if report.fixable:
                    summary['by_category'][category]['fixable'] += 1

        return summary

    def print_summary(self, summary: Dict):
        """Print formatted summary statistics.

        Args:
            summary: Summary dictionary from generate_summary()
        """
        print("\n" + "="*60)
        print("VALIDATION SUMMARY")
        print("="*60)
        print(f"Total recipes:      {summary['total']}")
        print(f"Valid:              {summary['valid']} ({100*summary['valid']/summary['total']:.1f}%)")
        print(f"Invalid:            {summary['invalid']} ({100*summary['invalid']/summary['total']:.1f}%)")
        print(f"  - Fixable:        {summary['fixable']} ({100*summary['fixable']/summary['total']:.1f}%)")
        print(f"  - Unfixable:      {summary['unfixable']} ({100*summary['unfixable']/summary['total']:.1f}%)")

        print("\nErrors by category:")
        print("-"*60)
        for category, stats in sorted(summary['by_category'].items(),
                                       key=lambda x: x[1]['count'],
                                       reverse=True):
            print(f"{category:20s} {stats['count']:5d} ({stats['fixable']:5d} fixable) - {stats['description']}")

        print("="*60 + "\n")
