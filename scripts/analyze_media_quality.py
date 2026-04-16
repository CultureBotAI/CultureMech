#!/usr/bin/env python3
"""
Analyze media recipe data quality and prioritize records needing review.

Generates a prioritized list of media with quality issues for Edison deep research review.
"""

import argparse
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any
import json


def load_yaml_recipe(yaml_path: Path) -> Dict[str, Any]:
    """Load a YAML recipe file."""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def calculate_completeness_score(recipe: Dict[str, Any]) -> Dict[str, Any]:
    """
    Calculate completeness score and identify missing/problematic fields.

    Returns dict with:
    - score: 0-100 completeness score
    - missing_fields: list of missing critical fields
    - issues: list of data quality issues
    """
    score = 100
    missing_fields = []
    issues = []

    # Critical fields (10 points each)
    critical_fields = {
        'description': 'No description provided',
        'medium_type': 'Medium type not specified',
        'physical_state': 'Physical state not specified',
        'ingredients': 'No ingredients listed',
    }

    for field, issue in critical_fields.items():
        if not recipe.get(field):
            score -= 10
            missing_fields.append(field)
            issues.append(issue)

    # Important fields (5 points each)
    important_fields = {
        'target_organisms': 'No target organisms specified',
        'ph_value': 'pH value not specified',
        'category': 'No category assigned',
    }

    for field, issue in important_fields.items():
        if not recipe.get(field):
            score -= 5
            missing_fields.append(field)
            issues.append(issue)

    # Check ingredient quality
    ingredients = recipe.get('ingredients', [])
    if ingredients:
        # Check for unmapped ingredients (no CHEBI)
        unmapped_count = 0
        missing_amounts = 0

        for ing in ingredients:
            if not ing.get('ingredient_term'):
                unmapped_count += 1
                issues.append(f"Unmapped ingredient: {ing.get('name', 'unknown')}")

            if not ing.get('amount') and not ing.get('concentration'):
                missing_amounts += 1

        # Penalize unmapped ingredients
        if unmapped_count > 0:
            penalty = min(15, unmapped_count * 2)
            score -= penalty
            issues.append(f"{unmapped_count} unmapped ingredients (no CHEBI)")

        # Penalize missing amounts
        if missing_amounts > len(ingredients) * 0.5:  # More than 50% missing
            score -= 10
            issues.append(f"{missing_amounts}/{len(ingredients)} ingredients missing amounts")

    # Check for solutions
    solutions = recipe.get('solutions', [])
    if solutions:
        for sol in solutions:
            sol_ings = sol.get('ingredients', [])
            if not sol_ings:
                score -= 5
                issues.append(f"Solution '{sol.get('name', 'unknown')}' has no ingredients")

    # Check target organisms quality
    target_organisms = recipe.get('target_organisms', [])
    if target_organisms:
        unmapped_organisms = sum(1 for org in target_organisms if not org.get('organism_term'))
        if unmapped_organisms > 0:
            score -= min(10, unmapped_organisms * 3)
            issues.append(f"{unmapped_organisms} unmapped organisms (no NCBITaxon)")

    # Check for media_term (provenance)
    if not recipe.get('media_term'):
        score -= 5
        missing_fields.append('media_term')
        issues.append('No source database reference')

    # Ensure score doesn't go negative
    score = max(0, score)

    return {
        'score': score,
        'missing_fields': missing_fields,
        'issues': issues,
        'has_description': bool(recipe.get('description')),
        'has_ph': bool(recipe.get('ph_value') or recipe.get('ph_range')),
        'has_organisms': bool(recipe.get('target_organisms')),
        'ingredient_count': len(ingredients),
        'unmapped_ingredient_count': sum(1 for ing in ingredients if not ing.get('ingredient_term')),
        'solution_count': len(solutions),
    }


def analyze_directory(yaml_dir: Path) -> List[Dict[str, Any]]:
    """Analyze all recipes in directory and return prioritized list."""
    results = []

    # Find all YAML files
    yaml_files = list(yaml_dir.rglob("*.yaml"))
    print(f"Analyzing {len(yaml_files)} recipe files...")

    for yaml_file in yaml_files:
        try:
            recipe = load_yaml_recipe(yaml_file)
            quality = calculate_completeness_score(recipe)

            # Get recipe metadata
            result = {
                'file_path': str(yaml_file.relative_to(yaml_dir)),
                'name': recipe.get('name', 'Unknown'),
                'category': recipe.get('category', 'unknown'),
                'source': recipe.get('media_term', {}).get('id', 'unknown') if isinstance(recipe.get('media_term'), dict) else 'unknown',
                'completeness_score': quality['score'],
                'missing_fields': quality['missing_fields'],
                'issues': quality['issues'],
                'metadata': {
                    'has_description': quality['has_description'],
                    'has_ph': quality['has_ph'],
                    'has_organisms': quality['has_organisms'],
                    'ingredient_count': quality['ingredient_count'],
                    'unmapped_ingredients': quality['unmapped_ingredient_count'],
                    'solution_count': quality['solution_count'],
                }
            }

            results.append(result)

        except Exception as e:
            print(f"Error processing {yaml_file}: {e}")
            continue

    # Sort by completeness score (lowest first = highest priority)
    results.sort(key=lambda x: x['completeness_score'])

    return results


def generate_report(results: List[Dict[str, Any]], output_file: Path, top_n: int = None):
    """Generate prioritized report for Edison review."""

    if top_n:
        results = results[:top_n]

    # Summary statistics
    total_recipes = len(results)
    avg_score = sum(r['completeness_score'] for r in results) / total_recipes if total_recipes > 0 else 0

    # Count by quality tier
    critical = sum(1 for r in results if r['completeness_score'] < 50)
    needs_work = sum(1 for r in results if 50 <= r['completeness_score'] < 70)
    good = sum(1 for r in results if 70 <= r['completeness_score'] < 90)
    excellent = sum(1 for r in results if r['completeness_score'] >= 90)

    # Group issues by type
    issue_counts = defaultdict(int)
    for r in results:
        for issue in r['issues']:
            # Normalize issue text for counting
            if 'unmapped ingredient' in issue.lower():
                issue_counts['Unmapped ingredients'] += 1
            elif 'description' in issue.lower():
                issue_counts['Missing description'] += 1
            elif 'ph' in issue.lower():
                issue_counts['Missing pH'] += 1
            elif 'organism' in issue.lower():
                issue_counts['Missing/unmapped organisms'] += 1
            elif 'amount' in issue.lower():
                issue_counts['Missing amounts'] += 1

    # Write report
    with open(output_file, 'w') as f:
        f.write("# CultureMech Media Quality Analysis Report\n\n")
        f.write(f"**Generated**: {Path.cwd()}\n")
        f.write(f"**Total Recipes Analyzed**: {total_recipes:,}\n")
        f.write(f"**Average Completeness Score**: {avg_score:.1f}/100\n\n")

        f.write("## Quality Distribution\n\n")
        f.write(f"- 🔴 **Critical** (< 50): {critical:,} recipes ({100*critical/total_recipes:.1f}%)\n")
        f.write(f"- 🟡 **Needs Work** (50-69): {needs_work:,} recipes ({100*needs_work/total_recipes:.1f}%)\n")
        f.write(f"- 🟢 **Good** (70-89): {good:,} recipes ({100*good/total_recipes:.1f}%)\n")
        f.write(f"- ⭐ **Excellent** (≥ 90): {excellent:,} recipes ({100*excellent/total_recipes:.1f}%)\n\n")

        f.write("## Common Issues\n\n")
        for issue, count in sorted(issue_counts.items(), key=lambda x: x[1], reverse=True):
            f.write(f"- **{issue}**: {count:,} occurrences\n")
        f.write("\n")

        f.write("## Top Priority Recipes for Edison Review\n\n")
        f.write("These recipes have the lowest completeness scores and would benefit most from deep research:\n\n")

        # Top priority recipes
        for i, r in enumerate(results[:50], 1):  # Top 50
            f.write(f"### {i}. {r['name']} (Score: {r['completeness_score']}/100)\n\n")
            f.write(f"- **File**: `{r['file_path']}`\n")
            f.write(f"- **Category**: {r['category']}\n")
            f.write(f"- **Source**: {r['source']}\n")
            f.write(f"- **Ingredients**: {r['metadata']['ingredient_count']} total, "
                   f"{r['metadata']['unmapped_ingredients']} unmapped\n")

            if r['issues']:
                f.write(f"\n**Issues** ({len(r['issues'])}):\n")
                for issue in r['issues'][:10]:  # Limit to 10 issues per recipe
                    f.write(f"  - {issue}\n")

            f.write("\n**Recommended Edison Queries**:\n")

            # Suggest specific queries based on issues
            if not r['metadata']['has_description']:
                f.write(f"  - \"What is {r['name']} culture medium used for? What organisms does it grow?\"\n")

            if not r['metadata']['has_ph']:
                f.write(f"  - \"What is the pH of {r['name']} medium?\"\n")

            if not r['metadata']['has_organisms']:
                f.write(f"  - \"What organisms are cultivated using {r['name']} medium?\"\n")

            if r['metadata']['unmapped_ingredients'] > 0:
                f.write(f"  - \"What are the chemical identities (CHEBI IDs) of ingredients in {r['name']}?\"\n")

            f.write("\n---\n\n")

    print(f"\nReport written to: {output_file}")
    print(f"\nSummary:")
    print(f"  Total recipes: {total_recipes:,}")
    print(f"  Average score: {avg_score:.1f}/100")
    print(f"  Critical priority: {critical:,} recipes")
    print(f"  Top issues: {', '.join(list(issue_counts.keys())[:3])}")


def generate_edison_batch_file(results: List[Dict[str, Any]], output_file: Path, batch_size: int = 100):
    """Generate a batch file for Edison processing."""

    batch = results[:batch_size]

    edison_tasks = []
    for r in batch:
        task = {
            'recipe_name': r['name'],
            'file_path': r['file_path'],
            'completeness_score': r['completeness_score'],
            'priority': 'HIGH' if r['completeness_score'] < 50 else 'MEDIUM' if r['completeness_score'] < 70 else 'LOW',
            'queries': []
        }

        # Generate specific queries based on missing data
        if not r['metadata']['has_description']:
            task['queries'].append({
                'field': 'description',
                'query': f"What is {r['name']} culture medium? What is its composition and what organisms does it cultivate? Provide a concise 2-3 sentence description."
            })

        if not r['metadata']['has_ph']:
            task['queries'].append({
                'field': 'ph_value',
                'query': f"What is the pH value of {r['name']} culture medium? Provide numeric value."
            })

        if not r['metadata']['has_organisms']:
            task['queries'].append({
                'field': 'target_organisms',
                'query': f"What microorganisms are commonly cultivated using {r['name']} medium? Provide species names and NCBITaxon IDs if possible."
            })

        if r['metadata']['unmapped_ingredients'] > 0:
            task['queries'].append({
                'field': 'ingredient_mapping',
                'query': f"What are the chemical identities (CHEBI IDs) and exact compositions of ingredients in {r['name']} medium?"
            })

        edison_tasks.append(task)

    with open(output_file, 'w') as f:
        json.dump(edison_tasks, f, indent=2)

    print(f"Edison batch file written to: {output_file}")
    print(f"  Tasks: {len(edison_tasks)}")
    print(f"  Total queries: {sum(len(t['queries']) for t in edison_tasks)}")


def main():
    parser = argparse.ArgumentParser(description="Analyze media recipe quality and prioritize for review")
    parser.add_argument('--yaml-dir', type=Path, default=Path('data/normalized_yaml'),
                       help='Directory containing recipe YAML files')
    parser.add_argument('--output', type=Path, default=Path('data/import_tracking/reports/quality_analysis.md'),
                       help='Output report file')
    parser.add_argument('--edison-batch', type=Path,
                       default=Path('data/import_tracking/reports/edison_batch.json'),
                       help='Output Edison batch file')
    parser.add_argument('--top-n', type=int, default=None,
                       help='Limit report to top N recipes')
    parser.add_argument('--batch-size', type=int, default=100,
                       help='Number of recipes in Edison batch')

    args = parser.parse_args()

    print("=" * 70)
    print("CultureMech Media Quality Analysis")
    print("=" * 70)

    # Analyze all recipes
    results = analyze_directory(args.yaml_dir)

    # Generate report
    args.output.parent.mkdir(parents=True, exist_ok=True)
    generate_report(results, args.output, args.top_n)

    # Generate Edison batch file
    args.edison_batch.parent.mkdir(parents=True, exist_ok=True)
    generate_edison_batch_file(results, args.edison_batch, args.batch_size)

    print("\n" + "=" * 70)
    print("Analysis complete!")
    print("=" * 70)
    print(f"\nNext steps:")
    print(f"1. Review report: {args.output}")
    print(f"2. Process batch with Edison: {args.edison_batch}")
    print(f"3. Use Edison deep research to fill gaps and correct errors")
    print(f"4. Update recipe YAML files with Edison results")


if __name__ == '__main__':
    main()
