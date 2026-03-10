#!/usr/bin/env python3
"""
Build fast compound→CHEBI mapping using:
1. Exact synonym matching (fast)
2. KG fallback for unmapped compounds

Skips expensive fuzzy matching for speed.
"""

import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml
from tqdm import tqdm

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def normalize_name(name: str) -> str:
    """Normalize chemical name for matching."""
    name = name.lower().strip()
    # Remove common prefixes
    name = re.sub(r'^(d|l|dl)-', '', name)
    name = re.sub(r'\s*\(.*?\)\s*', '', name)  # Remove parentheses
    name = name.replace('-', '').replace('_', '').replace(' ', '')
    return name


def load_chebi_synonyms(nodes_file: Path) -> tuple[dict, dict]:
    """Load CHEBI labels and synonyms."""
    print("Loading CHEBI synonyms from KG...")
    chebi_labels = {}
    chebi_synonyms = defaultdict(list)

    with open(nodes_file) as f:
        next(f)  # Skip header
        for line in tqdm(f, desc="Parsing nodes"):
            parts = line.strip().split('\t')
            if len(parts) < 7:
                continue

            node_id = parts[0]
            if not node_id.startswith('CHEBI:'):
                continue

            primary_name = parts[2]
            chebi_labels[node_id] = primary_name.strip()

            synonyms_str = parts[6] if len(parts) > 6 else ""
            if synonyms_str:
                synonyms = synonyms_str.split('|')
                all_names = [primary_name] + synonyms
                for syn in all_names:
                    if syn:
                        normalized = normalize_name(syn)
                        if normalized and node_id not in chebi_synonyms[normalized]:
                            chebi_synonyms[normalized].append(node_id)

    print(f"✓ Loaded {len(chebi_labels):,} CHEBI labels")
    print(f"✓ Indexed {len(chebi_synonyms):,} unique synonyms")
    return chebi_labels, dict(chebi_synonyms)


def build_fast_mapping(
    solutions_dir: Path,
    solution_to_chebi: dict,
    chebi_labels: dict,
    chebi_synonyms: dict
) -> tuple[dict, dict, dict]:
    """Build fast compound mapping using exact matching + KG fallback."""
    compound_to_chebi = {}
    name_to_chebi = defaultdict(set)

    stats = {
        'exact_match': 0,
        'synonym_match_ambiguous': 0,
        'kg_fallback': 0,
        'unmapped': 0
    }

    for yaml_path in tqdm(sorted(solutions_dir.glob("*.yaml")), desc="Processing solutions"):
        try:
            with open(yaml_path) as f:
                data = yaml.safe_load(f)

            term = data.get('term', {})
            solution_id = term.get('id')
            if not solution_id or not solution_id.startswith('mediadive.solution:'):
                continue

            composition = data.get('composition', [])
            comp_items = [(item.get('preferred_term', ''), item.get('term', {}).get('id', ''))
                         for item in composition if isinstance(item, dict)]

            # Filter to only mediadive.compound items
            comp_items = [(n, cid) for n, cid in comp_items if cid.startswith('mediadive.compound:')]

            # Track which compounds get matched
            matched = set()

            # Step 1: Exact synonym matching
            for name, compound_id in comp_items:
                if not name:
                    continue

                normalized = normalize_name(name)
                if normalized in chebi_synonyms:
                    chebi_ids = chebi_synonyms[normalized]
                    if len(chebi_ids) == 1:
                        compound_to_chebi[compound_id] = {
                            'chebi_id': chebi_ids[0],
                            'confidence': 1.0,
                            'match_type': 'exact_match',
                            'source_name': name
                        }
                        name_to_chebi[name].add(chebi_ids[0])
                        stats['exact_match'] += 1
                        matched.add(compound_id)
                    else:
                        # Ambiguous - take first
                        compound_to_chebi[compound_id] = {
                            'chebi_id': chebi_ids[0],
                            'confidence': 0.9,
                            'match_type': 'synonym_match_ambiguous',
                            'source_name': name
                        }
                        name_to_chebi[name].add(chebi_ids[0])
                        stats['synonym_match_ambiguous'] += 1
                        matched.add(compound_id)

            # Step 2: KG fallback for unmapped
            unmapped = [cid for _, cid in comp_items if cid not in matched]
            if unmapped and solution_id in solution_to_chebi:
                kg_chebi_ids = solution_to_chebi[solution_id]
                for i, comp_id in enumerate(unmapped):
                    if i < len(kg_chebi_ids):
                        compound_to_chebi[comp_id] = {
                            'chebi_id': kg_chebi_ids[i],
                            'confidence': 0.7,
                            'match_type': 'kg_fallback',
                            'source_name': ''
                        }
                        stats['kg_fallback'] += 1
                        matched.add(comp_id)

            # Count unmapped
            for _, comp_id in comp_items:
                if comp_id not in matched:
                    stats['unmapped'] += 1

        except Exception as e:
            print(f"⚠ Error processing {yaml_path.name}: {e}")
            continue

    return compound_to_chebi, dict(name_to_chebi), stats


def main():
    solutions_dir = Path("data/normalized_yaml/solutions/mediadive")
    solution_mapping_path = Path("data/solution_to_chebi_mapping.json")
    nodes_file = Path("data/kgm/merged-kg_nodes.tsv")
    output_path = Path("data/compound_to_chebi_mapping_enhanced.json")
    name_mapping_path = Path("data/chemical_name_to_chebi_mapping_enhanced.json")

    # Load data
    with open(solution_mapping_path) as f:
        solution_to_chebi = json.load(f)

    chebi_labels, chebi_synonyms = load_chebi_synonyms(nodes_file)

    # Build mappings
    print("\nBuilding fast compound→CHEBI mapping...")
    compound_to_chebi, name_to_chebi, stats = build_fast_mapping(
        solutions_dir, solution_to_chebi, chebi_labels, chebi_synonyms
    )

    # Save mappings
    with open(output_path, 'w') as f:
        json.dump(compound_to_chebi, f, indent=2)

    with open(name_mapping_path, 'w') as f:
        name_to_chebi_lists = {k: list(v) for k, v in name_to_chebi.items()}
        json.dump(name_to_chebi_lists, f, indent=2)

    # Print statistics
    print(f"\n{'='*70}")
    print("MAPPING STATISTICS")
    print(f"{'='*70}")
    print(f"Total compound mappings: {len(compound_to_chebi):,}")
    print(f"Total name mappings: {len(name_to_chebi):,}")
    print(f"\nMatch type breakdown:")
    total = sum(stats.values())
    for match_type, count in sorted(stats.items(), key=lambda x: -x[1]):
        pct = (count / total * 100) if total > 0 else 0
        print(f"  {match_type:30s}: {count:5d} ({pct:5.1f}%)")

    print(f"\n✓ Saved to {output_path}")
    print(f"✓ Saved name mapping to {name_mapping_path}")


if __name__ == "__main__":
    main()
