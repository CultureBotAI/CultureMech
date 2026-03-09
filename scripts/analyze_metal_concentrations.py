#!/usr/bin/env python3
"""
Analyze metal and REE concentrations across all culture media.

Computes distributions and identifies high-metal and high-REE media.
"""

import re
import yaml
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Tuple
import statistics

# Define metals and REEs based on common culture media components
METALS = {
    # Essential trace metals
    'Fe': ['Fe', 'Iron', 'Ferric', 'Ferrous', 'FeCl', 'FeSO4', 'Fe2(SO4)3', 'FeNH4', 'FeSO', 'FeEDTA'],
    'Cu': ['Cu', 'Copper', 'Cupric', 'Cuprous', 'CuCl', 'CuSO4', 'CuEDTA'],
    'Zn': ['Zn', 'Zinc', 'ZnCl', 'ZnSO4', 'ZnEDTA'],
    'Mn': ['Mn', 'Manganese', 'MnCl', 'MnSO4', 'MnEDTA'],
    'Co': ['Co', 'Cobalt', 'CoCl', 'CoSO4', 'CoCl2', 'CoEDTA'],
    'Ni': ['Ni', 'Nickel', 'NiCl', 'NiSO4', 'NiEDTA'],
    'Mo': ['Mo', 'Molybdenum', 'MoO', 'Na2MoO4', 'MoCl', 'MoEDTA', 'Molybdate'],
    'Se': ['Se', 'Selenium', 'SeO', 'Na2SeO', 'Selenite', 'Selenate'],
    'W': ['W', 'Tungsten', 'Na2WO4', 'Tungstate'],
    'V': ['V', 'Vanadium', 'VO', 'Vanadate'],
    'Cr': ['Cr', 'Chromium', 'CrCl', 'Chromate'],
    'Ca': ['Ca', 'Calcium', 'CaCl', 'CaSO4', 'CaCO3'],
    'Mg': ['Mg', 'Magnesium', 'MgCl', 'MgSO4'],
    'K': ['K', 'Potassium', 'KCl', 'K2HPO4', 'KH2PO4'],
    'Na': ['Na', 'Sodium', 'NaCl', 'NaHCO3', 'Na2CO3'],
}

# Rare Earth Elements (REEs) - Lanthanides + Sc + Y
REES = {
    'La': ['La', 'Lanthanum', 'LaCl'],
    'Ce': ['Ce', 'Cerium', 'CeCl'],
    'Pr': ['Pr', 'Praseodymium', 'PrCl'],
    'Nd': ['Nd', 'Neodymium', 'NdCl'],
    'Pm': ['Pm', 'Promethium', 'PmCl'],
    'Sm': ['Sm', 'Samarium', 'SmCl'],
    'Eu': ['Eu', 'Europium', 'EuCl'],
    'Gd': ['Gd', 'Gadolinium', 'GdCl'],
    'Tb': ['Tb', 'Terbium', 'TbCl'],
    'Dy': ['Dy', 'Dysprosium', 'DyCl'],
    'Ho': ['Ho', 'Holmium', 'HoCl'],
    'Er': ['Er', 'Erbium', 'ErCl'],
    'Tm': ['Tm', 'Thulium', 'TmCl'],
    'Yb': ['Yb', 'Ytterbium', 'YbCl'],
    'Lu': ['Lu', 'Lutetium', 'LuCl'],
    'Sc': ['Sc', 'Scandium', 'ScCl'],
    'Y': ['Y', 'Yttrium', 'YCl'],
}


def extract_concentration_value(ingredient: dict) -> float:
    """
    Extract numerical concentration value from ingredient.

    Returns concentration in mM (millimolar) for comparison.
    """
    if 'concentration' not in ingredient:
        return 0.0

    conc = ingredient['concentration']
    if not isinstance(conc, dict) or 'value' not in conc or 'unit' not in conc:
        return 0.0

    value = conc['value']
    unit = conc['unit']

    # Handle string values
    try:
        value = float(value) if isinstance(value, str) else value
    except (ValueError, TypeError):
        return 0.0

    # Convert to mM for standardization
    conversions = {
        'mM': 1.0,
        'M': 1000.0,
        'uM': 0.001,
        'μM': 0.001,
        'nM': 0.000001,
        'g/L': 1.0,  # Approximate, depends on molecular weight
        'mg/L': 0.001,
        'ug/L': 0.000001,
        'µg/L': 0.000001,
    }

    return value * conversions.get(unit, 1.0)


def contains_metal(ingredient_name: str, metal_patterns: List[str]) -> bool:
    """Check if ingredient name contains any metal pattern."""
    name_upper = ingredient_name.upper()
    for pattern in metal_patterns:
        # Match pattern at word boundaries or with common prefixes
        if re.search(rf'\b{re.escape(pattern.upper())}', name_upper):
            return True
        # Also check in formula-like patterns
        if pattern.upper() in name_upper:
            return True
    return False


def analyze_media_metals(media_dir: Path) -> Dict:
    """
    Analyze metal and REE concentrations across all media.

    Returns dict with:
    - metal_concentrations: {media_name: {metal: concentration}}
    - ree_concentrations: {media_name: {ree: concentration}}
    - distributions: statistical distributions
    """
    metal_concentrations = defaultdict(lambda: defaultdict(float))
    ree_concentrations = defaultdict(lambda: defaultdict(float))

    # Scan all media YAML files
    for category_dir in media_dir.iterdir():
        if not category_dir.is_dir():
            continue

        for yaml_file in category_dir.glob("*.yaml"):
            try:
                with open(yaml_file) as f:
                    media_data = yaml.safe_load(f)

                if not media_data or 'ingredients' not in media_data:
                    continue

                media_name = yaml_file.stem

                # Analyze each ingredient
                for ingredient in media_data['ingredients']:
                    if not isinstance(ingredient, dict):
                        continue

                    # Get ingredient name
                    ing_name = ""
                    if 'term' in ingredient and isinstance(ingredient['term'], dict):
                        ing_name = ingredient['term'].get('label', '')
                    if not ing_name and 'preferred_term' in ingredient:
                        ing_name = str(ingredient['preferred_term'])

                    if not ing_name:
                        continue

                    concentration = extract_concentration_value(ingredient)

                    # Check for metals
                    for metal_symbol, patterns in METALS.items():
                        if contains_metal(ing_name, patterns):
                            metal_concentrations[media_name][metal_symbol] += concentration

                    # Check for REEs
                    for ree_symbol, patterns in REES.items():
                        if contains_metal(ing_name, patterns):
                            ree_concentrations[media_name][ree_symbol] += concentration

            except Exception as e:
                print(f"⚠ Error processing {yaml_file.name}: {e}")
                continue

    # Compute distributions
    all_metal_totals = []
    all_ree_totals = []

    for media_name in metal_concentrations:
        total_metal = sum(metal_concentrations[media_name].values())
        if total_metal > 0:
            all_metal_totals.append(total_metal)

    for media_name in ree_concentrations:
        total_ree = sum(ree_concentrations[media_name].values())
        if total_ree > 0:
            all_ree_totals.append(total_ree)

    distributions = {
        'metal': compute_distribution_stats(all_metal_totals),
        'ree': compute_distribution_stats(all_ree_totals),
    }

    return {
        'metal_concentrations': dict(metal_concentrations),
        'ree_concentrations': dict(ree_concentrations),
        'distributions': distributions,
    }


def compute_distribution_stats(values: List[float]) -> Dict:
    """Compute statistical distribution of values."""
    if not values:
        return {
            'count': 0,
            'mean': 0,
            'median': 0,
            'stdev': 0,
            'min': 0,
            'max': 0,
            'p75': 0,
            'p90': 0,
            'p95': 0,
        }

    sorted_values = sorted(values)
    n = len(sorted_values)

    return {
        'count': n,
        'mean': statistics.mean(sorted_values),
        'median': statistics.median(sorted_values),
        'stdev': statistics.stdev(sorted_values) if n > 1 else 0,
        'min': sorted_values[0],
        'max': sorted_values[-1],
        'p75': sorted_values[int(n * 0.75)] if n > 0 else 0,
        'p90': sorted_values[int(n * 0.90)] if n > 0 else 0,
        'p95': sorted_values[int(n * 0.95)] if n > 0 else 0,
    }


def classify_media(
    metal_concentrations: Dict,
    ree_concentrations: Dict,
    distributions: Dict
) -> Tuple[set, set]:
    """
    Classify media as high-metal or high-REE based on distributions.

    Uses 90th percentile as threshold for "high".
    """
    metal_threshold = distributions['metal']['p90']
    ree_threshold = distributions['ree']['p90']

    high_metal_media = set()
    high_ree_media = set()

    # Classify by metal concentration
    for media_name, metals in metal_concentrations.items():
        total_metal = sum(metals.values())
        if total_metal >= metal_threshold:
            high_metal_media.add(media_name)

    # Classify by REE concentration
    for media_name, rees in ree_concentrations.items():
        total_ree = sum(rees.values())
        if total_ree >= ree_threshold:
            high_ree_media.add(media_name)

    return high_metal_media, high_ree_media


def main():
    """Main analysis workflow."""
    media_dir = Path("data/normalized_yaml")

    print("🔬 Analyzing metal and REE concentrations across media...\n")

    # Analyze concentrations
    results = analyze_media_metals(media_dir)

    metal_conc = results['metal_concentrations']
    ree_conc = results['ree_concentrations']
    distributions = results['distributions']

    # Print distributions
    print("📊 Metal Concentration Distribution:")
    print(f"  Media with metals: {distributions['metal']['count']}")
    print(f"  Mean: {distributions['metal']['mean']:.2f} mM")
    print(f"  Median: {distributions['metal']['median']:.2f} mM")
    print(f"  90th percentile: {distributions['metal']['p90']:.2f} mM")
    print(f"  95th percentile: {distributions['metal']['p95']:.2f} mM")
    print(f"  Max: {distributions['metal']['max']:.2f} mM")

    print("\n📊 REE Concentration Distribution:")
    print(f"  Media with REEs: {distributions['ree']['count']}")
    print(f"  Mean: {distributions['ree']['mean']:.6f} mM")
    print(f"  Median: {distributions['ree']['median']:.6f} mM")
    print(f"  90th percentile: {distributions['ree']['p90']:.6f} mM")
    print(f"  95th percentile: {distributions['ree']['p95']:.6f} mM")
    print(f"  Max: {distributions['ree']['max']:.6f} mM")

    # Classify media
    high_metal_media, high_ree_media = classify_media(
        metal_conc, ree_conc, distributions
    )

    print(f"\n✓ Classified {len(high_metal_media)} high-metal media")
    print(f"✓ Classified {len(high_ree_media)} high-REE media")

    # Show top 10 high-metal media
    print("\n🥇 Top 10 High-Metal Media:")
    metal_totals = {name: sum(metals.values()) for name, metals in metal_conc.items()}
    for i, (media_name, total) in enumerate(sorted(metal_totals.items(), key=lambda x: x[1], reverse=True)[:10], 1):
        print(f"  {i}. {media_name}: {total:.2f} mM")

    # Show top 10 high-REE media (if any)
    if ree_conc:
        print("\n🥇 Top 10 High-REE Media:")
        ree_totals = {name: sum(rees.values()) for name, rees in ree_conc.items()}
        for i, (media_name, total) in enumerate(sorted(ree_totals.items(), key=lambda x: x[1], reverse=True)[:10], 1):
            print(f"  {i}. {media_name}: {total:.6f} mM")

    # Save results
    output_file = Path("data/metal_ree_analysis.yaml")
    with open(output_file, 'w') as f:
        yaml.dump({
            'distributions': distributions,
            'high_metal_media': sorted(high_metal_media),
            'high_ree_media': sorted(high_ree_media),
            'metal_concentrations': {k: dict(v) for k, v in metal_conc.items()},
            'ree_concentrations': {k: dict(v) for k, v in ree_conc.items()},
        }, f, default_flow_style=False, sort_keys=False)

    print(f"\n✓ Results saved to {output_file}")


if __name__ == "__main__":
    main()
