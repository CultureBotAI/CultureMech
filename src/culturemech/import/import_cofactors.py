"""
Import cofactor hierarchy from PFASCommunityAgents.
Creates cofactor reference data and ingredient mappings.
"""

import yaml
from pathlib import Path
import sys

PFAS_REPO = Path("/Users/marcin/Documents/VIMSS/ontology/PFAS/PFASCommunityAgents")
COFACTOR_FILE = PFAS_REPO / "data/reference/cofactor_hierarchy.yaml"
MAPPING_FILE = PFAS_REPO / "data/reference/ingredient_cofactor_mapping.csv"

CATEGORY_MAPPING = {
    "vitamins": "VITAMINS",
    "metals": "METALS",
    "nucleotides": "NUCLEOTIDES",
    "energy_transfer": "ENERGY_TRANSFER",
    "other_specialized": "OTHER_SPECIALIZED",
}


def import_cofactor_hierarchy():
    """Convert PFAS cofactor hierarchy to CultureMech format."""
    if not COFACTOR_FILE.exists():
        print(f"Error: PFAS cofactor file not found at {COFACTOR_FILE}")
        return []

    with open(COFACTOR_FILE) as f:
        pfas_data = yaml.safe_load(f)

    cofactors = []

    for cat_key, cat_data in pfas_data.get('cofactor_hierarchy', {}).items():
        category_enum = CATEGORY_MAPPING.get(cat_key, "OTHER_SPECIALIZED")

        for cofactor_key, cofactor_data in cat_data.get('cofactors', {}).items():
            cofactor = {
                'preferred_term': cofactor_data.get('names', [cofactor_key])[0],
                'category': category_enum,
            }

            # Add CHEBI term
            if 'id' in cofactor_data:
                cofactor['term'] = {
                    'id': cofactor_data['id'],
                    'label': cofactor['preferred_term'],
                }

            # Add precursor
            if 'precursor' in cofactor_data:
                cofactor['precursor'] = cofactor_data['precursor']
                if 'precursor_id' in cofactor_data:
                    cofactor['precursor_term'] = {
                        'id': cofactor_data['precursor_id'],
                        'label': cofactor_data['precursor'],
                    }

            # Add EC associations
            if 'ec_associations' in cofactor_data:
                cofactor['ec_associations'] = cofactor_data['ec_associations']

            # Add KEGG pathways
            if 'kegg_pathways' in cofactor_data:
                cofactor['kegg_pathways'] = cofactor_data['kegg_pathways']

            # Add enzyme examples
            if 'enzyme_examples' in cofactor_data:
                cofactor['enzyme_examples'] = cofactor_data['enzyme_examples']

            # Add biosynthesis genes
            if 'biosynthesis_genes' in cofactor_data:
                cofactor['biosynthesis_genes'] = cofactor_data['biosynthesis_genes']

            # Add bioavailability
            if 'bioavailability' in cofactor_data:
                cofactor['bioavailability'] = cofactor_data['bioavailability']

            # Add notes
            if 'notes' in cofactor_data:
                cofactor['notes'] = cofactor_data['notes']

            cofactors.append(cofactor)

    print(f"Imported {len(cofactors)} cofactors from PFAS data")
    return cofactors


def write_cofactor_reference(cofactors: list, output_dir: Path):
    """Write cofactors to reference file."""
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "cofactors.yaml"

    with open(output_file, 'w') as f:
        yaml.dump({'cofactors': cofactors}, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    print(f"✓ Wrote {len(cofactors)} cofactors to {output_file}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Import cofactor hierarchy from PFAS data")
    parser.add_argument("--output-dir", type=Path, default=Path("data/reference"),
                        help="Output directory for cofactor reference (default: data/reference)")

    args = parser.parse_args()

    cofactors = import_cofactor_hierarchy()
    if not cofactors:
        print("No cofactors imported. Exiting.")
        sys.exit(1)

    write_cofactor_reference(cofactors, args.output_dir)

    # Print summary by category
    print("\nCofactors by category:")
    by_category = {}
    for cofactor in cofactors:
        cat = cofactor.get('category', 'UNKNOWN')
        by_category[cat] = by_category.get(cat, 0) + 1

    for cat, count in sorted(by_category.items()):
        print(f"  {cat}: {count}")


if __name__ == "__main__":
    main()
