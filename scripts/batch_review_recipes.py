#!/usr/bin/env python3
"""
Batch review recipes for quality assurance.

Validates all recipes against P1-P4 validation rules and generates reports.
"""

import argparse
import json
import yaml
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from collections import defaultdict
import re

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


class RecipeValidator:
    """Validate recipes against quality rules."""

    def __init__(self, mediaingredientmech_repo: Optional[Path] = None):
        self.mediaingredientmech_repo = mediaingredientmech_repo
        self.mediaing_ids = self._load_mediaingredientmech_ids()

    def _validate_solution(self, solution: Dict, solution_path: Path) -> Dict:
        """Validate a solution file (uses SolutionDescriptor schema)."""
        issues = []

        # Solution-specific validation
        # Required: preferred_term, composition
        if 'preferred_term' not in solution:
            issues.append({
                'rule': 'P1.3',
                'priority': 'P1',
                'description': 'Missing required field: preferred_term (for solutions)'
            })

        if 'composition' not in solution:
            issues.append({
                'rule': 'P1.3',
                'priority': 'P1',
                'description': 'Missing required field: composition (for solutions)'
            })

        # Check composition ingredients
        composition = solution.get('composition', [])
        total_ingredients = len(composition)
        linked_ingredients = sum(
            1 for ing in composition
            if isinstance(ing, dict) and ing.get('mediaingredientmech_term', {}).get('id')
        )

        coverage = (linked_ingredients / total_ingredients * 100) if total_ingredients > 0 else 0

        # Solutions should have >80% MediaIngredientMech coverage
        if coverage < 80 and total_ingredients > 0:
            issues.append({
                'rule': 'P3.2',
                'priority': 'P3',
                'description': f'Low MediaIngredientMech coverage: {coverage:.1f}% (threshold: 80% for solutions)'
            })

        # Check for invalid MediaIngredientMech IDs
        for idx, ing in enumerate(composition):
            if isinstance(ing, dict):
                mediaing_id = ing.get('mediaingredientmech_term', {}).get('id')
                if mediaing_id and self.mediaing_ids and mediaing_id not in self.mediaing_ids:
                    issues.append({
                        'rule': 'P2.1',
                        'priority': 'P2',
                        'description': f'Invalid MediaIngredientMech ID: {mediaing_id} (ingredient: {ing.get("preferred_term", "unknown")})'
                    })

        return {
            'path': str(solution_path),
            'id': solution.get('id', 'N/A'),
            'name': solution.get('preferred_term', 'N/A'),
            'category': 'solution',
            'medium_type': 'SOLUTION',
            'total_ingredients': total_ingredients,
            'linked_ingredients': linked_ingredients,
            'coverage': coverage,
            'issues': issues,
            'valid': len([i for i in issues if i['priority'] == 'P1']) == 0
        }

    def _load_mediaingredientmech_ids(self) -> set:
        """Load all valid MediaIngredientMech IDs."""
        ids = set()
        if not self.mediaingredientmech_repo:
            # Try default location
            default_path = Path(__file__).parent.parent.parent / "MediaIngredientMech"
            if default_path.exists():
                self.mediaingredientmech_repo = default_path

        if self.mediaingredientmech_repo:
            mapped_file = self.mediaingredientmech_repo / "data" / "curated" / "mapped_ingredients.yaml"
            if mapped_file.exists():
                with open(mapped_file) as f:
                    data = yaml.safe_load(f)
                    for item in data.get('ingredients', []):
                        if 'id' in item:
                            ids.add(item['id'])
        return ids

    def validate_recipe(self, recipe_path: Path) -> Dict:
        """Validate a single recipe and return issues."""
        issues = []

        try:
            with open(recipe_path) as f:
                recipe = yaml.safe_load(f)
        except Exception as e:
            return {
                'path': str(recipe_path),
                'valid': False,
                'issues': [{
                    'rule': 'P1.1',
                    'priority': 'P1',
                    'description': f'Failed to parse YAML: {e}'
                }]
            }

        # P1.1: Schema validation (basic check)
        if not isinstance(recipe, dict):
            issues.append({
                'rule': 'P1.1',
                'priority': 'P1',
                'description': 'Recipe is not a valid dictionary'
            })
            return {'path': str(recipe_path), 'valid': False, 'issues': issues}

        # Detect if this is a solution (not a media recipe)
        is_solution = (
            'solutions' in str(recipe_path) or
            ('preferred_term' in recipe and 'composition' in recipe and 'name' not in recipe)
        )

        # Solutions use SolutionDescriptor schema, skip MediaRecipe validation
        if is_solution:
            return self._validate_solution(recipe, recipe_path)

        # P1.2: Invalid CultureMech ID
        culturemech_id = recipe.get('id', '')
        if not re.match(r'^CultureMech:\d{6}$', culturemech_id):
            issues.append({
                'rule': 'P1.2',
                'priority': 'P1',
                'description': f'Invalid CultureMech ID format: {culturemech_id}'
            })

        # P1.3: Missing required fields
        required_fields = ['name', 'medium_type', 'physical_state']
        for field in required_fields:
            if field not in recipe:
                issues.append({
                    'rule': 'P1.3',
                    'priority': 'P1',
                    'description': f'Missing required field: {field}'
                })

        # P1.4: Invalid enum values (basic check)
        # These are the actual values from the schema - DO NOT hardcode, derive from schema
        valid_medium_types = ['DEFINED', 'COMPLEX', 'SEMI_DEFINED', 'MINIMAL', 'UNDEFINED']
        valid_physical_states = ['LIQUID', 'SOLID_AGAR', 'SEMISOLID', 'BIPHASIC']

        if recipe.get('medium_type') and recipe['medium_type'] not in valid_medium_types:
            issues.append({
                'rule': 'P1.4',
                'priority': 'P1',
                'description': f'Invalid medium_type: {recipe.get("medium_type")}'
            })

        if recipe.get('physical_state') and recipe['physical_state'] not in valid_physical_states:
            issues.append({
                'rule': 'P1.4',
                'priority': 'P1',
                'description': f'Invalid physical_state: {recipe.get("physical_state")}'
            })

        # P2.1: Invalid MediaIngredientMech ID
        ingredients = recipe.get('ingredients', []) + recipe.get('composition', [])
        for idx, ing in enumerate(ingredients):
            if isinstance(ing, dict):
                mediaing_id = ing.get('mediaingredientmech_term', {}).get('id')
                if mediaing_id and self.mediaing_ids and mediaing_id not in self.mediaing_ids:
                    issues.append({
                        'rule': 'P2.1',
                        'priority': 'P2',
                        'description': f'Invalid MediaIngredientMech ID: {mediaing_id} (ingredient: {ing.get("preferred_term", "unknown")})'
                    })

        # P3.1: Placeholder text
        placeholder_patterns = [
            r'see source',
            r'original amount:',
            r'unknown',
            r'\bTBD\b',
            r'to be determined',
            r'check source',
            r'refer to'
        ]

        def check_placeholders(text: str) -> bool:
            if not isinstance(text, str):
                return False
            text_lower = text.lower()
            return any(re.search(pattern, text_lower) for pattern in placeholder_patterns)

        # Check notes
        if check_placeholders(recipe.get('notes', '')):
            issues.append({
                'rule': 'P3.1',
                'priority': 'P3',
                'description': 'Placeholder text found in notes field'
            })

        # Check ingredients
        for idx, ing in enumerate(ingredients):
            if isinstance(ing, dict):
                if check_placeholders(ing.get('notes', '')):
                    issues.append({
                        'rule': 'P3.1',
                        'priority': 'P3',
                        'description': f'Placeholder text in ingredient notes: {ing.get("preferred_term", "unknown")}'
                    })

        # P3.2: Missing MediaIngredientMech linkage
        total_ingredients = len(ingredients)
        linked_ingredients = sum(
            1 for ing in ingredients
            if isinstance(ing, dict) and ing.get('mediaingredientmech_term', {}).get('id')
        )

        coverage = (linked_ingredients / total_ingredients * 100) if total_ingredients > 0 else 0

        # For solutions, expect >80% coverage; for media, >50%
        is_solution = 'solutions' in str(recipe_path)
        threshold = 80 if is_solution else 50

        if coverage < threshold and total_ingredients > 0:
            issues.append({
                'rule': 'P3.2',
                'priority': 'P3',
                'description': f'Low MediaIngredientMech coverage: {coverage:.1f}% (threshold: {threshold}%)'
            })

        # P3.4: Missing preparation steps for complex media
        if recipe.get('medium_type') == 'COMPLEX' and not recipe.get('preparation_steps'):
            issues.append({
                'rule': 'P3.4',
                'priority': 'P3',
                'description': 'Missing preparation_steps for COMPLEX medium'
            })

        # P3.5: Sterilization not specified
        if not recipe.get('sterilization'):
            issues.append({
                'rule': 'P3.5',
                'priority': 'P3',
                'description': 'Sterilization method not specified'
            })

        # P3.6: pH not specified for defined/semi-defined media
        if recipe.get('medium_type') in ['DEFINED', 'SEMI_DEFINED'] and not recipe.get('ph_value'):
            issues.append({
                'rule': 'P3.6',
                'priority': 'P3',
                'description': 'pH not specified for DEFINED/SEMI_DEFINED medium'
            })

        # P4.2: Missing target organisms
        if not recipe.get('target_organisms'):
            issues.append({
                'rule': 'P4.2',
                'priority': 'P4',
                'description': 'No target_organisms specified'
            })

        # P4.3: Missing references
        if not recipe.get('references'):
            issues.append({
                'rule': 'P4.3',
                'priority': 'P4',
                'description': 'No source references'
            })

        return {
            'path': str(recipe_path),
            'id': recipe.get('id', 'N/A'),
            'name': recipe.get('name', 'N/A'),
            'category': recipe_path.parent.name,
            'medium_type': recipe.get('medium_type', 'N/A'),
            'total_ingredients': total_ingredients,
            'linked_ingredients': linked_ingredients,
            'coverage': coverage,
            'issues': issues,
            'valid': len([i for i in issues if i['priority'] == 'P1']) == 0
        }


def generate_tsv_report(results: List[Dict], output_path: Path):
    """Generate TSV report of validation results."""
    with open(output_path, 'w') as f:
        # Header
        f.write('\t'.join([
            'CultureMech ID',
            'Recipe Name',
            'Category',
            'Medium Type',
            'Valid',
            'P1 Critical',
            'P2 High',
            'P3 Medium',
            'P4 Low',
            'Total Ingredients',
            'Linked Ingredients',
            'Coverage %',
            'Issues',
            'File Path'
        ]) + '\n')

        # Data rows
        for result in results:
            issues_by_priority = defaultdict(list)
            for issue in result['issues']:
                issues_by_priority[issue['priority']].append(issue['description'])

            p1_count = len(issues_by_priority['P1'])
            p2_count = len(issues_by_priority['P2'])
            p3_count = len(issues_by_priority['P3'])
            p4_count = len(issues_by_priority['P4'])

            all_issues = '; '.join([
                f"{issue['rule']}: {issue['description']}"
                for issue in result['issues']
            ])

            f.write('\t'.join([
                result.get('id', 'N/A'),
                result.get('name', 'N/A'),
                result.get('category', 'N/A'),
                result.get('medium_type', 'N/A'),
                'Yes' if result['valid'] else 'No',
                str(p1_count),
                str(p2_count),
                str(p3_count),
                str(p4_count),
                str(result.get('total_ingredients', 0)),
                str(result.get('linked_ingredients', 0)),
                f"{result.get('coverage', 0):.1f}",
                all_issues,
                result['path']
            ]) + '\n')


def generate_markdown_report(results: List[Dict], output_path: Path):
    """Generate markdown summary report."""
    total_recipes = len(results)
    valid_recipes = sum(1 for r in results if r['valid'])

    # Count issues by priority
    p1_recipes = sum(1 for r in results if any(i['priority'] == 'P1' for i in r['issues']))
    p2_recipes = sum(1 for r in results if any(i['priority'] == 'P2' for i in r['issues']))
    p3_recipes = sum(1 for r in results if any(i['priority'] == 'P3' for i in r['issues']))
    p4_recipes = sum(1 for r in results if any(i['priority'] == 'P4' for i in r['issues']))

    # Count total issues
    p1_total = sum(len([i for i in r['issues'] if i['priority'] == 'P1']) for r in results)
    p2_total = sum(len([i for i in r['issues'] if i['priority'] == 'P2']) for r in results)
    p3_total = sum(len([i for i in r['issues'] if i['priority'] == 'P3']) for r in results)
    p4_total = sum(len([i for i in r['issues'] if i['priority'] == 'P4']) for r in results)

    # Category breakdown
    by_category = defaultdict(list)
    for r in results:
        by_category[r.get('category', 'unknown')].append(r)

    # Coverage statistics
    total_ingredients = sum(r.get('total_ingredients', 0) for r in results)
    total_linked = sum(r.get('linked_ingredients', 0) for r in results)
    overall_coverage = (total_linked / total_ingredients * 100) if total_ingredients > 0 else 0

    # Issue frequency
    issue_counts = defaultdict(int)
    for r in results:
        for issue in r['issues']:
            issue_counts[issue['rule']] += 1

    with open(output_path, 'w') as f:
        f.write(f"# CultureMech Recipe Validation Report\n\n")
        f.write(f"**Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        f.write(f"## Summary Statistics\n\n")
        f.write(f"- **Total recipes:** {total_recipes:,}\n")
        f.write(f"- **Valid recipes (no P1 errors):** {valid_recipes:,} ({valid_recipes/total_recipes*100:.1f}%)\n")
        f.write(f"- **P1 Critical Errors:** {p1_total} issues in {p1_recipes} recipes ({p1_recipes/total_recipes*100:.1f}%)\n")
        f.write(f"- **P2 High Priority:** {p2_total} issues in {p2_recipes} recipes ({p2_recipes/total_recipes*100:.1f}%)\n")
        f.write(f"- **P3 Medium Priority:** {p3_total} issues in {p3_recipes} recipes ({p3_recipes/total_recipes*100:.1f}%)\n")
        f.write(f"- **P4 Low Priority:** {p4_total} issues in {p4_recipes} recipes ({p4_recipes/total_recipes*100:.1f}%)\n\n")

        f.write(f"## MediaIngredientMech Coverage\n\n")
        f.write(f"- **Total ingredient instances:** {total_ingredients:,}\n")
        f.write(f"- **Linked instances:** {total_linked:,}\n")
        f.write(f"- **Overall coverage:** {overall_coverage:.1f}%\n\n")

        f.write(f"## By Category\n\n")
        f.write(f"| Category | Recipes | Valid | P1 | P2 | P3 | P4 | Avg Coverage |\n")
        f.write(f"|----------|---------|-------|----|----|----|----|-------------|\n")

        for category in sorted(by_category.keys()):
            cat_results = by_category[category]
            cat_total = len(cat_results)
            cat_valid = sum(1 for r in cat_results if r['valid'])
            cat_p1 = sum(1 for r in cat_results if any(i['priority'] == 'P1' for i in r['issues']))
            cat_p2 = sum(1 for r in cat_results if any(i['priority'] == 'P2' for i in r['issues']))
            cat_p3 = sum(1 for r in cat_results if any(i['priority'] == 'P3' for i in r['issues']))
            cat_p4 = sum(1 for r in cat_results if any(i['priority'] == 'P4' for i in r['issues']))
            cat_coverage = sum(r.get('coverage', 0) for r in cat_results) / cat_total if cat_total > 0 else 0

            f.write(f"| {category} | {cat_total:,} | {cat_valid:,} | {cat_p1} | {cat_p2} | {cat_p3} | {cat_p4} | {cat_coverage:.1f}% |\n")

        f.write(f"\n## Most Frequent Issues\n\n")
        f.write(f"| Rule | Description | Count | Affected Recipes |\n")
        f.write(f"|------|-------------|-------|------------------|\n")

        rule_descriptions = {
            'P1.1': 'Schema validation failure',
            'P1.2': 'Invalid CultureMech ID',
            'P1.3': 'Missing required fields',
            'P1.4': 'Invalid enum values',
            'P2.1': 'Invalid MediaIngredientMech ID',
            'P3.1': 'Placeholder text',
            'P3.2': 'Low MediaIngredientMech coverage',
            'P3.4': 'Missing preparation steps',
            'P3.5': 'Sterilization not specified',
            'P3.6': 'pH not specified',
            'P4.2': 'Missing target organisms',
            'P4.3': 'Missing references',
        }

        for rule, count in sorted(issue_counts.items(), key=lambda x: x[1], reverse=True)[:20]:
            affected = sum(1 for r in results if any(i['rule'] == rule for i in r['issues']))
            desc = rule_descriptions.get(rule, 'Unknown')
            f.write(f"| {rule} | {desc} | {count:,} | {affected:,} |\n")

        if p1_total > 0:
            f.write(f"\n## P1 Critical Errors (Must Fix)\n\n")
            p1_recipes_list = [r for r in results if any(i['priority'] == 'P1' for i in r['issues'])]
            for r in p1_recipes_list[:20]:  # Show first 20
                f.write(f"### {r.get('name', 'Unknown')} ({r.get('id', 'N/A')})\n\n")
                f.write(f"**File:** `{r['path']}`\n\n")
                for issue in [i for i in r['issues'] if i['priority'] == 'P1']:
                    f.write(f"- **{issue['rule']}:** {issue['description']}\n")
                f.write(f"\n")

            if len(p1_recipes_list) > 20:
                f.write(f"\n*...and {len(p1_recipes_list) - 20} more recipes with P1 errors*\n")

        f.write(f"\n## Recommendations\n\n")

        if p1_total > 0:
            f.write(f"1. **CRITICAL:** Fix {p1_total} P1 errors in {p1_recipes} recipes before KG export\n")
        else:
            f.write(f"1. ✅ No P1 critical errors - ready for KG export\n")

        if p2_total > 0:
            f.write(f"2. **HIGH PRIORITY:** Review {p2_total} P2 issues in {p2_recipes} recipes\n")

        if p3_total > 0:
            f.write(f"3. **MEDIUM PRIORITY:** Auto-fix or review {p3_total} P3 issues\n")
            f.write(f"   - Run: `just fix-all-data-quality` to auto-correct safe issues\n")

        if overall_coverage < 80:
            f.write(f"4. **Coverage:** Improve MediaIngredientMech coverage from {overall_coverage:.1f}% to >80%\n")
            f.write(f"   - Run: `PYTHONPATH=src python scripts/enrich_with_mediaingredientmech.py`\n")


def main():
    parser = argparse.ArgumentParser(description='Batch review CultureMech recipes')
    parser.add_argument('--category', help='Specific category to review')
    parser.add_argument('--output', default='reports/validation', help='Output path prefix')
    parser.add_argument('--limit', type=int, help='Limit number of recipes')
    parser.add_argument('--mediaingredientmech-repo', type=Path, help='Path to MediaIngredientMech repo')
    parser.add_argument('--priority', help='Filter by priority (e.g., P1,P2)')

    args = parser.parse_args()

    # Find all recipe files
    data_dir = Path(__file__).parent.parent / "data" / "normalized_yaml"

    if args.category:
        pattern = f"{args.category}/*.yaml"
    else:
        pattern = "**/*.yaml"

    recipe_files = sorted(data_dir.glob(pattern))

    if args.limit:
        recipe_files = recipe_files[:args.limit]

    print(f"Found {len(recipe_files)} recipes to validate...")

    # Validate recipes
    validator = RecipeValidator(mediaingredientmech_repo=args.mediaingredientmech_repo)
    results = []

    for idx, recipe_file in enumerate(recipe_files, 1):
        if idx % 100 == 0:
            print(f"  Validated {idx}/{len(recipe_files)}...")

        result = validator.validate_recipe(recipe_file)

        # Filter by priority if specified
        if args.priority:
            priorities = args.priority.split(',')
            result['issues'] = [
                i for i in result['issues']
                if i['priority'] in priorities
            ]

        results.append(result)

    print(f"Validation complete. Generating reports...")

    # Create output directory
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Generate reports
    tsv_path = output_path.with_suffix('.tsv')
    md_path = output_path.with_suffix('.md')
    json_path = output_path.with_suffix('.json')

    generate_tsv_report(results, tsv_path)
    print(f"✅ TSV report: {tsv_path}")

    generate_markdown_report(results, md_path)
    print(f"✅ Markdown report: {md_path}")

    # JSON report
    with open(json_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"✅ JSON report: {json_path}")

    # Summary
    total = len(results)
    valid = sum(1 for r in results if r['valid'])
    p1_count = sum(len([i for i in r['issues'] if i['priority'] == 'P1']) for r in results)

    print(f"\n{'='*60}")
    print(f"SUMMARY: {valid}/{total} recipes valid ({valid/total*100:.1f}%)")
    if p1_count > 0:
        print(f"⚠️  {p1_count} P1 CRITICAL ERRORS - Must fix before export!")
    else:
        print(f"✅ No P1 errors - Ready for KG export")
    print(f"{'='*60}")


if __name__ == '__main__':
    main()
