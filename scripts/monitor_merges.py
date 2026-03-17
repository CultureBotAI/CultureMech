#!/usr/bin/env python3
"""Monitoring dashboard for merge quality.

Generates comprehensive quality reports with:
- Overall merge statistics
- Issue detection and severity levels
- Recommended actions
- Trend analysis (if historical data available)

Outputs actionable YAML reports for decision-making.
"""

import argparse
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List

import yaml

from culturemech.enrich.hierarchy_importer import MediaIngredientMechHierarchyImporter


def find_all_recipes(directory: Path) -> List[Path]:
    """Find all recipe YAML files."""
    return sorted(directory.rglob('*.yaml'))


def load_recipe(path: Path) -> Dict:
    """Load recipe from YAML file."""
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def collect_merge_statistics(merge_dir: Path) -> Dict:
    """Collect overall merge statistics.

    Args:
        merge_dir: Path to merged recipes directory

    Returns:
        Statistics dictionary
    """
    print(f"\nCollecting merge statistics from {merge_dir}...")

    recipe_paths = find_all_recipes(merge_dir)

    stats = {
        'total_recipes': len(recipe_paths),
        'merged_recipes': 0,
        'singleton_recipes': 0,
        'merge_group_sizes': [],
        'largest_merge_group': 0,
        'total_source_recipes': 0,
    }

    for path in recipe_paths:
        try:
            recipe = load_recipe(path)
            merged_from = recipe.get('merged_from', [])

            if len(merged_from) > 1:
                stats['merged_recipes'] += 1
                stats['merge_group_sizes'].append(len(merged_from))
                stats['largest_merge_group'] = max(
                    stats['largest_merge_group'],
                    len(merged_from)
                )
            else:
                stats['singleton_recipes'] += 1

            stats['total_source_recipes'] += len(merged_from)

        except Exception as e:
            print(f"  Warning: Failed to process {path}: {e}", file=sys.stderr)

    # Calculate averages
    if stats['merge_group_sizes']:
        stats['average_merge_group_size'] = round(
            sum(stats['merge_group_sizes']) / len(stats['merge_group_sizes']),
            2
        )
    else:
        stats['average_merge_group_size'] = 0

    # Calculate reduction
    if stats['total_source_recipes'] > 0:
        stats['reduction_count'] = stats['total_source_recipes'] - stats['total_recipes']
        stats['reduction_percentage'] = round(
            (stats['reduction_count'] / stats['total_source_recipes']) * 100,
            1
        )
    else:
        stats['reduction_count'] = 0
        stats['reduction_percentage'] = 0

    print(f"  Processed {stats['total_recipes']} recipes")

    return stats


def analyze_categories(merge_dir: Path) -> Dict:
    """Analyze category distribution and cross-category merges.

    Args:
        merge_dir: Path to merged recipes directory

    Returns:
        Category analysis dictionary
    """
    print("\nAnalyzing categories...")

    recipe_paths = find_all_recipes(merge_dir)

    category_counts = Counter()
    cross_category_merges = []

    for path in recipe_paths:
        try:
            recipe = load_recipe(path)
            categories = recipe.get('categories', [])

            if not categories:
                # Try singular category field
                category = recipe.get('category')
                if category:
                    categories = [category]

            # Count categories
            for cat in categories:
                category_counts[cat] += 1

            # Check for cross-category merge
            if len(categories) > 1:
                merged_from = recipe.get('merged_from', [])
                cross_category_merges.append({
                    'name': recipe.get('name'),
                    'categories': categories,
                    'merged_count': len(merged_from),
                })

        except Exception as e:
            pass

    analysis = {
        'category_distribution': dict(category_counts),
        'cross_category_merge_count': len(cross_category_merges),
        'cross_category_examples': cross_category_merges[:10],  # First 10
    }

    print(f"  Found {len(category_counts)} categories")
    print(f"  Cross-category merges: {len(cross_category_merges)}")

    return analysis


def load_quality_report(quality_report_path: Path) -> Dict:
    """Load quality validation report.

    Args:
        quality_report_path: Path to quality report YAML

    Returns:
        Quality report dictionary
    """
    if not quality_report_path.exists():
        print(f"  Warning: Quality report not found: {quality_report_path}", file=sys.stderr)
        return {}

    with open(quality_report_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def generate_recommendations(
    stats: Dict,
    category_analysis: Dict,
    quality_report: Dict
) -> List[str]:
    """Generate actionable recommendations.

    Args:
        stats: Merge statistics
        category_analysis: Category analysis
        quality_report: Quality validation report

    Returns:
        List of recommendation strings
    """
    recommendations = []

    # Check quality issues
    if quality_report:
        issues = quality_report.get('summary', {})

        variant_contamination = issues.get('variant_contamination', 0)
        if variant_contamination > 0:
            recommendations.append(
                f"URGENT: Undo {variant_contamination} merges with variant contamination "
                f"(use: scripts/undo_merge.py --filter variant_contamination)"
            )

        parent_mismatches = issues.get('parent_mismatch', 0)
        if parent_mismatches > 0:
            recommendations.append(
                f"Review {parent_mismatches} merges with parent mismatches manually"
            )

        concentration_outliers = issues.get('concentration_outlier', 0)
        if concentration_outliers > 10:
            recommendations.append(
                f"Investigate {concentration_outliers} merges with concentration outliers"
            )

    # Check cross-category merges
    cross_cat_count = category_analysis.get('cross_category_merge_count', 0)
    if cross_cat_count > 0:
        recommendations.append(
            f"INFO: {cross_cat_count} cross-category merges found (may be intentional)"
        )

    # Check reduction rate
    reduction_pct = stats.get('reduction_percentage', 0)
    if reduction_pct < 50:
        recommendations.append(
            f"Low reduction rate ({reduction_pct}%) - consider more aggressive merge mode"
        )
    elif reduction_pct > 95:
        recommendations.append(
            f"Very high reduction rate ({reduction_pct}%) - verify merge quality"
        )

    # If no issues, good job!
    if not recommendations:
        recommendations.append("No critical issues detected - merge quality looks good!")

    return recommendations


def generate_dashboard_report(
    merge_dir: Path,
    quality_report_path: Path,
    output_path: Path
) -> None:
    """Generate comprehensive monitoring dashboard report.

    Args:
        merge_dir: Path to merged recipes directory
        quality_report_path: Path to quality report
        output_path: Path to output dashboard report
    """
    print("=" * 70)
    print("Merge Quality Dashboard")
    print("=" * 70)

    # Collect statistics
    stats = collect_merge_statistics(merge_dir)

    # Analyze categories
    category_analysis = analyze_categories(merge_dir)

    # Load quality report
    quality_report = load_quality_report(quality_report_path)

    # Generate recommendations
    recommendations = generate_recommendations(
        stats,
        category_analysis,
        quality_report
    )

    # Build dashboard report
    report = {
        'generated_at': datetime.now().isoformat(),
        'merge_statistics': stats,
        'category_analysis': category_analysis,
        'quality_checks': quality_report.get('summary', {}),
        'recommendations': recommendations,
        'top_issues': {},
    }

    # Add top issues from quality report
    if quality_report and 'issues' in quality_report:
        for issue_type, issues in quality_report['issues'].items():
            if issues:
                report['top_issues'][issue_type] = {
                    'count': len(issues),
                    'examples': [
                        {
                            'recipe': issue.get('recipe_name'),
                            'file': issue.get('recipe_file'),
                            'severity': issue.get('severity'),
                        }
                        for issue in issues[:5]  # Top 5
                    ]
                }

    # Write report
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        yaml.dump(report, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"\nDashboard report written to: {output_path}")

    # Print summary
    print("\n" + "=" * 70)
    print("Dashboard Summary")
    print("=" * 70)
    print(f"Total merged recipes:    {stats['total_recipes']:,}")
    print(f"Merged groups:           {stats['merged_recipes']:,}")
    print(f"Singleton recipes:       {stats['singleton_recipes']:,}")
    print(f"Reduction:               {stats['reduction_count']:,} recipes ({stats['reduction_percentage']}%)")
    print(f"Largest merge group:     {stats['largest_merge_group']}")
    print()

    if quality_report:
        quality_summary = quality_report.get('summary', {})
        total_issues = quality_summary.get('total_issues', 0)

        print(f"Quality Issues:")
        print(f"  Variant contamination: {quality_summary.get('variant_contamination', 0)}")
        print(f"  Parent mismatches:     {quality_summary.get('parent_mismatch', 0)}")
        print(f"  Concentration outliers: {quality_summary.get('concentration_outlier', 0)}")
        print(f"  TOTAL:                 {total_issues}")
        print()

    print("Recommendations:")
    for i, rec in enumerate(recommendations, 1):
        print(f"  {i}. {rec}")
    print()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Generate merge quality monitoring dashboard'
    )

    parser.add_argument(
        '--merged-dir',
        type=Path,
        required=True,
        help='Path to merged recipes directory'
    )

    parser.add_argument(
        '--quality-report',
        type=Path,
        default=Path('reports/merge_quality.yaml'),
        help='Path to quality validation report'
    )

    parser.add_argument(
        '--output',
        type=Path,
        default=Path('reports/merge_dashboard.yaml'),
        help='Path to output dashboard report'
    )

    args = parser.parse_args()

    # Validate paths
    if not args.merged_dir.exists():
        print(f"Error: {args.merged_dir} not found", file=sys.stderr)
        return 1

    # Generate dashboard
    generate_dashboard_report(
        args.merged_dir,
        args.quality_report,
        args.output
    )

    return 0


if __name__ == '__main__':
    sys.exit(main())
