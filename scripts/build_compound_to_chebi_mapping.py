#!/usr/bin/env python3
"""
Build mapping from mediadive.compound names to CHEBI IDs using KG knowledge.

Strategy:
1. Load solution→CHEBI mappings from KG edges
2. Load CHEBI node labels from KG nodes
3. For each solution YAML:
   - Match composition items (by name) to CHEBI terms
   - Build mediadive.compound:X → CHEBI:Y mapping
4. Save mapping for YAML enrichment
"""

import json
import sys
from collections import defaultdict
from pathlib import Path

import yaml
from tqdm import tqdm

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))


def load_solution_to_chebi_mapping(mapping_path: Path) -> dict:
    """Load pre-extracted solution→CHEBI mappings."""
    with open(mapping_path) as f:
        return json.load(f)


def load_chebi_labels(nodes_file: Path) -> dict:
    """Load CHEBI node labels from KG nodes file."""
    print("Loading CHEBI labels from KG nodes...")
    chebi_labels = {}

    with open(nodes_file) as f:
        # Skip header
        next(f)

        for line in tqdm(f, desc="Parsing nodes"):
            parts = line.strip().split('\t')
            if len(parts) < 3:
                continue

            node_id = parts[0]
            if node_id.startswith('CHEBI:'):
                # Column 3 (index 2) is the name
                label = parts[2] if len(parts) > 2 else ""
                chebi_labels[node_id] = label.lower().strip()

    print(f"✓ Loaded {len(chebi_labels):,} CHEBI labels")
    return chebi_labels


def normalize_name(name: str) -> str:
    """Normalize chemical name for matching."""
    return name.lower().strip().replace('-', '').replace(' ', '')


def match_composition_to_chebi(
    composition_names: list[str],
    solution_chebi_ids: list[str],
    chebi_labels: dict
) -> dict:
    """
    Match composition item names to CHEBI IDs.

    Args:
        composition_names: List of chemical names from YAML composition
        solution_chebi_ids: List of CHEBI IDs for this solution from KG
        chebi_labels: Mapping of CHEBI ID → label

    Returns:
        Mapping of composition_name → CHEBI_ID
    """
    mapping = {}

    # Normalize composition names
    norm_comp_names = {normalize_name(name): name for name in composition_names}

    # Try to match each CHEBI to a composition name
    for chebi_id in solution_chebi_ids:
        chebi_label = chebi_labels.get(chebi_id, "")
        norm_label = normalize_name(chebi_label)

        # Try exact match
        if norm_label in norm_comp_names:
            original_name = norm_comp_names[norm_label]
            mapping[original_name] = chebi_id
            continue

        # Try substring match (for cases like "sodium chloride" vs "NaCl")
        matched = False
        for norm_comp, original_name in norm_comp_names.items():
            if norm_label in norm_comp or norm_comp in norm_label:
                mapping[original_name] = chebi_id
                matched = True
                break

    return mapping


def build_compound_to_chebi_mapping(
    solutions_dir: Path,
    solution_to_chebi: dict,
    chebi_labels: dict
) -> dict:
    """
    Build mapping from mediadive.compound:X to CHEBI:Y.

    Returns:
        Mapping of mediadive.compound:X → CHEBI:Y
    """
    compound_to_chebi = {}
    name_to_chebi = defaultdict(set)  # Track all CHEBI IDs for each chemical name

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

            # Get CHEBI IDs for this solution from KG
            solution_chebi_ids = solution_to_chebi.get(solution_id, [])
            if not solution_chebi_ids:
                continue

            # Extract composition names and compound IDs
            composition = data.get('composition', [])
            comp_items = []
            for item in composition:
                name = item.get('preferred_term', '')
                item_term = item.get('term', {})
                compound_id = item_term.get('id', '')

                if name and compound_id.startswith('mediadive.compound:'):
                    comp_items.append((name, compound_id))

            # Match names to CHEBI IDs
            comp_names = [name for name, _ in comp_items]
            name_mapping = match_composition_to_chebi(
                comp_names, solution_chebi_ids, chebi_labels
            )

            # Build compound→CHEBI mapping
            for name, compound_id in comp_items:
                if name in name_mapping:
                    chebi_id = name_mapping[name]
                    compound_to_chebi[compound_id] = chebi_id
                    name_to_chebi[name].add(chebi_id)

        except Exception as e:
            print(f"⚠ Error processing {yaml_path.name}: {e}")
            continue

    return compound_to_chebi, dict(name_to_chebi)


def main():
    # Paths
    solutions_dir = Path("data/normalized_yaml/solutions/mediadive")
    solution_mapping_path = Path("data/solution_to_chebi_mapping.json")
    nodes_file = Path("data/kgm/merged-kg_nodes.tsv")
    output_path = Path("data/compound_to_chebi_mapping.json")
    name_mapping_path = Path("data/chemical_name_to_chebi_mapping.json")

    # Load data
    solution_to_chebi = load_solution_to_chebi_mapping(solution_mapping_path)
    chebi_labels = load_chebi_labels(nodes_file)

    # Build mappings
    print("\nBuilding compound→CHEBI mapping...")
    compound_to_chebi, name_to_chebi = build_compound_to_chebi_mapping(
        solutions_dir, solution_to_chebi, chebi_labels
    )

    # Save mappings
    with open(output_path, 'w') as f:
        json.dump(compound_to_chebi, f, indent=2)

    with open(name_mapping_path, 'w') as f:
        # Convert sets to lists for JSON serialization
        name_to_chebi_lists = {k: list(v) for k, v in name_to_chebi.items()}
        json.dump(name_to_chebi_lists, f, indent=2)

    print(f"\n✓ Built {len(compound_to_chebi):,} compound→CHEBI mappings")
    print(f"✓ Built {len(name_to_chebi):,} name→CHEBI mappings")
    print(f"✓ Saved to {output_path}")
    print(f"✓ Saved name mapping to {name_mapping_path}")


if __name__ == "__main__":
    main()
