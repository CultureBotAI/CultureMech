#!/usr/bin/env python3
"""Fix validation errors in CultureMech recipe files.

Applies progressive fixing strategies:
1. YAML parsing fixes (escape sequences, quotes)
2. Schema defaults (missing required fields)
3. Enum normalization
4. Type coercion

Usage:
    python scripts/fix_validation_errors.py [OPTIONS]

Options:
    --dry-run              Show what would be fixed without writing files
    --categories CATS      Comma-separated list: yaml,schema,types,all (default: all)
    --limit N              Process only first N recipes
    --report-only          Generate validation report without fixing
    --input-dir DIR        Directory with normalized recipes (default: data/normalized_yaml)
    --verbose              Show detailed progress
"""

import argparse
import logging
import sys
from pathlib import Path
from typing import List, Set

import yaml

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from culturemech.validation import YAMLFixer, SchemaDefaulter, RecipeValidator


logger = logging.getLogger(__name__)


class ValidationFixer:
    """Batch validation error fixer."""

    def __init__(self, dry_run: bool = False, verbose: bool = False):
        """Initialize the fixer.

        Args:
            dry_run: If True, don't write fixed files
            verbose: Show detailed progress
        """
        self.dry_run = dry_run
        self.verbose = verbose

        self.yaml_fixer = YAMLFixer()
        self.schema_defaulter = SchemaDefaulter()
        self.validator = RecipeValidator()

        # Statistics
        self.stats = {
            'total': 0,
            'skipped': 0,
            'yaml_fixed': 0,
            'schema_fixed': 0,
            'unfixable': 0,
            'already_valid': 0,
        }

    def fix_directory(
        self,
        input_dir: Path,
        categories: Set[str],
        limit: int = None
    ) -> List[Path]:
        """Fix all recipes in a directory.

        Args:
            input_dir: Directory containing recipe YAML files
            categories: Set of fix categories to apply
            limit: Maximum number of recipes to process

        Returns:
            List of paths that were fixed
        """
        fixed_files = []

        # Find all YAML files
        yaml_files = sorted(input_dir.rglob('*.yaml'))

        if limit:
            yaml_files = yaml_files[:limit]

        self.stats['total'] = len(yaml_files)

        logger.info(f"Processing {len(yaml_files)} recipe files...")

        for i, recipe_path in enumerate(yaml_files, 1):
            if self.verbose or i % 100 == 0:
                logger.info(f"[{i}/{len(yaml_files)}] Processing {recipe_path.name}")

            try:
                fixed = self.fix_file(recipe_path, categories)
                if fixed:
                    fixed_files.append(recipe_path)
            except Exception as e:
                logger.error(f"Error processing {recipe_path}: {e}")
                self.stats['unfixable'] += 1

        return fixed_files

    def fix_file(self, recipe_path: Path, categories: Set[str]) -> bool:
        """Fix a single recipe file.

        Args:
            recipe_path: Path to recipe YAML file
            categories: Set of fix categories to apply

        Returns:
            True if file was fixed and written
        """
        # Step 1: Try to load YAML (with fixes if needed)
        try:
            with open(recipe_path, 'r', encoding='utf-8', errors='replace') as f:
                original_content = f.read()

            # Try simple load first
            try:
                recipe = yaml.safe_load(original_content)
                yaml_was_fixed = False
                content = original_content
                warnings = []
            except yaml.YAMLError:
                # Need YAML fixes
                if 'yaml' not in categories and 'all' not in categories:
                    self.stats['skipped'] += 1
                    return False

                # Apply YAML fixes
                content, warnings = self.yaml_fixer.fix_yaml_content(original_content)
                recipe = yaml.safe_load(content)
                yaml_was_fixed = True
                self.stats['yaml_fixed'] += 1

                if self.verbose:
                    logger.info(f"  Fixed YAML errors: {', '.join(warnings)}")

        except Exception as e:
            logger.error(f"  Cannot load YAML: {e}")
            self.stats['unfixable'] += 1
            return False

        if not isinstance(recipe, dict):
            logger.error(f"  Recipe is not a dictionary")
            self.stats['unfixable'] += 1
            return False

        # Step 2: Apply schema defaults if needed
        schema_was_fixed = False
        if 'schema' in categories or 'all' in categories:
            original_recipe = recipe.copy()

            # Apply defaults
            recipe = self.schema_defaulter.apply_defaults(recipe)

            # Check if anything changed
            if recipe != original_recipe:
                schema_was_fixed = True
                self.stats['schema_fixed'] += 1

                if self.verbose:
                    changes = self.schema_defaulter.changes_made
                    logger.info(f"  Applied schema defaults: {len(changes)} changes")

        # Step 3: Normalize enums and coerce types
        types_was_fixed = False
        if 'types' in categories or 'all' in categories:
            original_recipe = recipe.copy()

            # Normalize enums
            recipe = self.schema_defaulter.normalize_enums(recipe)

            # Coerce types
            recipe = self.schema_defaulter.coerce_types(recipe)

            if recipe != original_recipe:
                types_was_fixed = True

                if self.verbose:
                    logger.info(f"  Normalized types and enums")

        # Step 4: Write fixed file if changes were made
        any_fixes = yaml_was_fixed or schema_was_fixed or types_was_fixed

        if not any_fixes:
            self.stats['already_valid'] += 1
            return False

        if not self.dry_run:
            # Write fixed content
            with open(recipe_path, 'w', encoding='utf-8') as f:
                yaml.safe_dump(recipe, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

            if self.verbose:
                logger.info(f"  ✓ Fixed and saved")

        else:
            if self.verbose:
                logger.info(f"  Would fix (dry-run)")

        return True

    def print_stats(self):
        """Print statistics summary."""
        print("\n" + "="*60)
        print("FIXING STATISTICS")
        print("="*60)
        print(f"Total recipes:        {self.stats['total']}")
        print(f"Already valid:        {self.stats['already_valid']}")
        print(f"Fixed:")
        print(f"  - YAML parsing:     {self.stats['yaml_fixed']}")
        print(f"  - Schema defaults:  {self.stats['schema_fixed']}")
        print(f"Skipped:              {self.stats['skipped']}")
        print(f"Unfixable:            {self.stats['unfixable']}")
        print(f"\nTotal fixed:          {self.stats['yaml_fixed'] + self.stats['schema_fixed']}")
        print("="*60 + "\n")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Fix validation errors in recipe files',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Show what would be fixed without writing files'
    )

    parser.add_argument(
        '--categories',
        default='all',
        help='Comma-separated list: yaml,schema,types,all (default: all)'
    )

    parser.add_argument(
        '--limit',
        type=int,
        help='Process only first N recipes'
    )

    parser.add_argument(
        '--report-only',
        action='store_true',
        help='Generate validation report without fixing'
    )

    parser.add_argument(
        '--input-dir',
        type=Path,
        default=Path('data/normalized_yaml'),
        help='Directory with normalized recipes (default: data/normalized_yaml)'
    )

    parser.add_argument(
        '--verbose',
        action='store_true',
        help='Show detailed progress'
    )

    args = parser.parse_args()

    # Setup logging
    logging.basicConfig(
        level=logging.INFO if args.verbose else logging.WARNING,
        format='%(message)s'
    )

    # Parse categories
    if args.categories == 'all':
        categories = {'yaml', 'schema', 'types', 'all'}
    else:
        categories = set(args.categories.split(','))

    # Validate input directory
    if not args.input_dir.exists():
        logger.error(f"Input directory not found: {args.input_dir}")
        sys.exit(1)

    # Report-only mode: just validate and report
    if args.report_only:
        logger.info("Generating validation report...")
        validator = RecipeValidator()

        yaml_files = sorted(args.input_dir.rglob('*.yaml'))
        if args.limit:
            yaml_files = yaml_files[:args.limit]

        reports = []
        for i, recipe_path in enumerate(yaml_files, 1):
            if args.verbose or i % 100 == 0:
                logger.info(f"[{i}/{len(yaml_files)}] Validating {recipe_path.name}")

            report = validator.validate_file(recipe_path)
            reports.append(report)

        summary = validator.generate_summary(reports)
        validator.print_summary(summary)

        return

    # Fix mode
    logger.info(f"Fix categories: {', '.join(sorted(categories))}")
    if args.dry_run:
        logger.info("DRY RUN MODE - no files will be modified")

    fixer = ValidationFixer(dry_run=args.dry_run, verbose=args.verbose)

    fixed_files = fixer.fix_directory(
        args.input_dir,
        categories=categories,
        limit=args.limit
    )

    fixer.print_stats()

    if args.dry_run:
        print(f"Would fix {len(fixed_files)} files")
    else:
        print(f"Fixed {len(fixed_files)} files")


if __name__ == '__main__':
    main()
