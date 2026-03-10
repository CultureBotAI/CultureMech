#!/usr/bin/env python3
"""
Build enhanced compound→CHEBI mapping using:
1. Exact name matching
2. Synonym matching
3. Fuzzy matching
4. KG fallback for unmapped compounds
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
    # Convert to lowercase
    name = name.lower().strip()
    # Remove common prefixes/suffixes
    name = re.sub(r'^(d|l|dl)-', '', name)
    name = re.sub(r'\s*\(.*?\)\s*', '', name)  # Remove parentheses content
    # Normalize separators
    name = name.replace('-', '').replace('_', '').replace(' ', '')
    return name


def load_chebi_data(nodes_file: Path) -> tuple[dict, dict]:
    """
    Load CHEBI labels and synonyms from KG nodes.

    Returns:
        (chebi_labels, chebi_synonyms)
        - chebi_labels: {CHEBI:ID -> primary_name}
        - chebi_synonyms: {normalized_synonym -> [CHEBI:IDs]}
    """
    print("Loading CHEBI data from KG nodes...")
    chebi_labels = {}
    chebi_synonyms = defaultdict(list)

    with open(nodes_file) as f:
        # Skip header
        next(f)

        for line in tqdm(f, desc="Parsing nodes"):
            parts = line.strip().split('\t')
            if len(parts) < 8:
                continue

            node_id = parts[0]
            if not node_id.startswith('CHEBI:'):
                continue

            # Column 3 (index 2) is the primary name
            primary_name = parts[2] if len(parts) > 2 else ""
            chebi_labels[node_id] = primary_name.strip()

            # Column 7 (index 6) is synonyms (pipe-separated)
            synonyms_str = parts[6] if len(parts) > 6 else ""
            if synonyms_str:
                synonyms = synonyms_str.split('|')
                # Index both primary name and all synonyms
                all_names = [primary_name] + synonyms
                for syn in all_names:
                    if syn:
                        normalized = normalize_name(syn)
                        if normalized and node_id not in chebi_synonyms[normalized]:
                            chebi_synonyms[normalized].append(node_id)

    print(f"✓ Loaded {len(chebi_labels):,} CHEBI labels")
    print(f"✓ Indexed {len(chebi_synonyms):,} unique synonyms")
    return chebi_labels, dict(chebi_synonyms)


def fuzzy_match_name(name: str, chebi_synonyms: dict, threshold: float = 0.85) -> list:
    """
    Optimized fuzzy match using substring matching (fast approximation).

    Returns list of (CHEBI_ID, confidence) tuples.
    """
    normalized = normalize_name(name)
    if not normalized or len(normalized) < 3:
        return []

    matches = []

    # Fast substring matching (much faster than SequenceMatcher)
    for syn, chebi_ids in chebi_synonyms.items():
        # Only check if lengths are similar (within 30%)
        if abs(len(syn) - len(normalized)) / max(len(syn), len(normalized)) > 0.3:
            continue

        # Check substring matches
        if normalized in syn or syn in normalized:
            for chebi_id in chebi_ids:
                # Confidence based on length similarity
                confidence = 1.0 - abs(len(syn) - len(normalized)) / max(len(syn), len(normalized))
                if confidence >= threshold:
                    matches.append((chebi_id, confidence, 'fuzzy_match'))

    # Sort by confidence descending
    matches.sort(key=lambda x: x[1], reverse=True)
    return matches[:3]  # Return top 3 matches


def match_composition_to_chebi_enhanced(
    composition_items: list[tuple[str, str]],  # [(name, compound_id), ...]
    solution_id: str,
    solution_to_chebi: dict,
    chebi_labels: dict,
    chebi_synonyms: dict
) -> dict:
    """
    Enhanced matching with exact, synonym, fuzzy, and KG fallback.

    Returns:
        {compound_id -> (CHEBI_ID, confidence, match_type)}
    """
    mappings = {}

    for name, compound_id in composition_items:
        if not name:
            continue

        normalized = normalize_name(name)

        # 1. Try exact match via synonyms (highest confidence)
        if normalized in chebi_synonyms:
            chebi_ids = chebi_synonyms[normalized]
            if len(chebi_ids) == 1:
                mappings[compound_id] = (chebi_ids[0], 1.0, 'exact_match')
                continue
            # Multiple matches - pick first (could be ambiguous)
            mappings[compound_id] = (chebi_ids[0], 0.95, 'synonym_match_ambiguous')
            continue

        # 2. Try fuzzy match
        fuzzy_matches = fuzzy_match_name(name, chebi_synonyms, threshold=0.85)
        if fuzzy_matches:
            chebi_id, confidence, match_type = fuzzy_matches[0]
            mappings[compound_id] = (chebi_id, confidence, match_type)
            continue

    # 3. KG fallback for unmapped compounds
    # Use KG solution→CHEBI edges for compounds we couldn't match by name
    unmapped = [comp_id for name, comp_id in composition_items if comp_id not in mappings]

    if unmapped and solution_id in solution_to_chebi:
        kg_chebi_ids = solution_to_chebi[solution_id]

        # Assign KG CHEBI IDs to unmapped compounds
        # This is heuristic - we don't know which compound maps to which CHEBI
        # But it's better than having no mapping at all
        for i, comp_id in enumerate(unmapped):
            if i < len(kg_chebi_ids):
                mappings[comp_id] = (kg_chebi_ids[i], 0.7, 'kg_fallback')

    return mappings


def build_enhanced_mapping(
    solutions_dir: Path,
    solution_to_chebi: dict,
    chebi_labels: dict,
    chebi_synonyms: dict
) -> tuple[dict, dict, dict]:
    """
    Build enhanced compound→CHEBI mapping.

    Returns:
        (compound_to_chebi, name_to_chebi, match_stats)
    """
    compound_to_chebi = {}  # {compound_id -> (CHEBI_ID, confidence, match_type)}
    name_to_chebi = defaultdict(set)  # {name -> set(CHEBI_IDs)}

    match_stats = {
        'exact_match': 0,
        'synonym_match_ambiguous': 0,
        'fuzzy_match': 0,
        'kg_fallback': 0,
        'unmapped': 0
    }

    solution_yamls = sorted(solutions_dir.glob("*.yaml"))

    for yaml_path in tqdm(solution_yamls, desc="Processing solutions"):
        try:
            with open(yaml_path) as f:
                data = yaml.safe_load(f)

            # Get solution ID
            term = data.get('term', {})
            solution_id = term.get('id')
            if not solution_id or not solution_id.startswith('mediadive.solution:'):
                continue

            # Extract composition
            composition = data.get('composition', [])
            comp_items = []
            for item in composition:
                name = item.get('preferred_term', '')
                item_term = item.get('term', {})
                compound_id = item_term.get('id', '')

                if name and compound_id.startswith('mediadive.compound:'):
                    comp_items.append((name, compound_id))

            # Match with enhanced algorithm
            mappings = match_composition_to_chebi_enhanced(
                comp_items, solution_id, solution_to_chebi, chebi_labels, chebi_synonyms
            )

            # Update results
            for name, compound_id in comp_items:
                if compound_id in mappings:
                    chebi_id, confidence, match_type = mappings[compound_id]
                    compound_to_chebi[compound_id] = {
                        'chebi_id': chebi_id,
                        'confidence': confidence,
                        'match_type': match_type,
                        'source_name': name
                    }
                    name_to_chebi[name].add(chebi_id)
                    match_stats[match_type] += 1
                else:
                    match_stats['unmapped'] += 1

        except Exception as e:
            print(f"⚠ Error processing {yaml_path.name}: {e}")
            continue

    return compound_to_chebi, dict(name_to_chebi), match_stats


def main():
    # Paths
    solutions_dir = Path("data/normalized_yaml/solutions/mediadive")
    solution_mapping_path = Path("data/solution_to_chebi_mapping.json")
    nodes_file = Path("data/kgm/merged-kg_nodes.tsv")
    output_path = Path("data/compound_to_chebi_mapping_enhanced.json")
    name_mapping_path = Path("data/chemical_name_to_chebi_mapping_enhanced.json")

    # Load data
    with open(solution_mapping_path) as f:
        solution_to_chebi = json.load(f)

    chebi_labels, chebi_synonyms = load_chebi_data(nodes_file)

    # Build enhanced mappings
    print("\nBuilding enhanced compound→CHEBI mapping...")
    compound_to_chebi, name_to_chebi, match_stats = build_enhanced_mapping(
        solutions_dir, solution_to_chebi, chebi_labels, chebi_synonyms
    )

    # Save mappings
    with open(output_path, 'w') as f:
        json.dump(compound_to_chebi, f, indent=2)

    with open(name_mapping_path, 'w') as f:
        # Convert sets to lists for JSON serialization
        name_to_chebi_lists = {k: list(v) for k, v in name_to_chebi.items()}
        json.dump(name_to_chebi_lists, f, indent=2)

    # Print statistics
    print(f"\n{'='*70}")
    print("MAPPING STATISTICS")
    print(f"{'='*70}")
    print(f"Total compound mappings: {len(compound_to_chebi):,}")
    print(f"Total name mappings: {len(name_to_chebi):,}")
    print(f"\nMatch type breakdown:")
    total_processed = sum(match_stats.values())
    for match_type, count in sorted(match_stats.items(), key=lambda x: -x[1]):
        pct = (count / total_processed * 100) if total_processed > 0 else 0
        print(f"  {match_type:30s}: {count:4d} ({pct:5.1f}%)")

    print(f"\n✓ Saved to {output_path}")
    print(f"✓ Saved name mapping to {name_mapping_path}")


if __name__ == "__main__":
    main()
