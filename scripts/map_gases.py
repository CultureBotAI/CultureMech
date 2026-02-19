#!/usr/bin/env python3
"""
Map Gas Ingredients to CHEBI

Identifies gas-related ingredients and maps them to their CHEBI chemical IDs.
"""

import pandas as pd
import sys
from pathlib import Path
from datetime import datetime, timezone

sys.path.insert(0, str(Path(__file__).parent))
from enrich_sssom_with_ols import create_mapping, load_sssom_file, extract_sssom_metadata, save_sssom_file


# Gas mappings to CHEBI IDs
GAS_MAPPINGS = {
    # Common gases
    'Carbon dioxide gas': ('CHEBI:16526', 'carbon dioxide'),
    'CO2 gas': ('CHEBI:16526', 'carbon dioxide'),
    'Carbon dioxide': ('CHEBI:16526', 'carbon dioxide'),
    'CO2': ('CHEBI:16526', 'carbon dioxide'),

    'Nitrogen gas': ('CHEBI:17997', 'dinitrogen'),
    'N2 gas': ('CHEBI:17997', 'dinitrogen'),
    'N2': ('CHEBI:17997', 'dinitrogen'),
    'Nitrogen': ('CHEBI:17997', 'dinitrogen'),

    'Hydrogen gas': ('CHEBI:18276', 'dihydrogen'),
    'H2 gas': ('CHEBI:18276', 'dihydrogen'),
    'H2': ('CHEBI:18276', 'dihydrogen'),
    'Hydrogen': ('CHEBI:18276', 'dihydrogen'),

    'Oxygen gas': ('CHEBI:15379', 'dioxygen'),
    'O2 gas': ('CHEBI:15379', 'dioxygen'),
    'O2': ('CHEBI:15379', 'dioxygen'),
    'Oxygen': ('CHEBI:15379', 'dioxygen'),

    'Methane gas': ('CHEBI:16183', 'methane'),
    'CH4 gas': ('CHEBI:16183', 'methane'),
    'CH4': ('CHEBI:16183', 'methane'),
    'Methane': ('CHEBI:16183', 'methane'),

    'Argon gas': ('CHEBI:49475', 'argon atom'),
    'Argon': ('CHEBI:49475', 'argon atom'),
    'Ar': ('CHEBI:49475', 'argon atom'),

    'Helium gas': ('CHEBI:33681', 'helium atom'),
    'Helium': ('CHEBI:33681', 'helium atom'),
    'He': ('CHEBI:33681', 'helium atom'),

    'Carbon monoxide gas': ('CHEBI:17245', 'carbon monoxide'),
    'CO gas': ('CHEBI:17245', 'carbon monoxide'),
    'CO': ('CHEBI:17245', 'carbon monoxide'),

    'Hydrogen sulfide gas': ('CHEBI:16136', 'hydrogen sulfide'),
    'H2S gas': ('CHEBI:16136', 'hydrogen sulfide'),
    'H2S': ('CHEBI:16136', 'hydrogen sulfide'),

    'Ammonia gas': ('CHEBI:16134', 'ammonia'),
    'NH3 gas': ('CHEBI:16134', 'ammonia'),
    'NH3': ('CHEBI:16134', 'ammonia'),

    'Nitrous oxide gas': ('CHEBI:17045', 'nitrous oxide'),
    'N2O gas': ('CHEBI:17045', 'nitrous oxide'),
    'N2O': ('CHEBI:17045', 'nitrous oxide'),
}


def find_gas_ingredients(unmapped_file: Path):
    """Find all gas-related ingredients in unmapped list."""
    df = pd.read_csv(unmapped_file, sep='\t')

    # Case-insensitive search for gas-related terms
    gas_pattern = r'(?i)(gas|air|CO2|N2|O2|H2|CH4|NH3|H2S|N2O|Ar|He)\b'
    potential_gases = df[df['ingredient'].str.contains(gas_pattern, na=False, regex=True)]

    return potential_gases


def map_gases_to_chebi(ingredients_df: pd.DataFrame):
    """Map gas ingredients to CHEBI IDs."""
    mappings = []

    for _, row in ingredients_df.iterrows():
        ingredient_name = row['ingredient']

        # Check exact matches first
        if ingredient_name in GAS_MAPPINGS:
            chebi_id, label = GAS_MAPPINGS[ingredient_name]
            mapping = create_mapping(
                ingredient_name=ingredient_name,
                chebi_id=chebi_id,
                label=label,
                confidence=0.98,
                predicate='exactMatch',
                tool='GasDict|manual',
                comment=f'Curated gas mapping',
                mapping_method='curated_dictionary'
            )
            mappings.append(mapping)
            print(f"✓ {ingredient_name:40s} → {chebi_id} ({label})")
        else:
            # Check case-insensitive matches
            for gas_name, (chebi_id, label) in GAS_MAPPINGS.items():
                if ingredient_name.lower() == gas_name.lower():
                    mapping = create_mapping(
                        ingredient_name=ingredient_name,
                        chebi_id=chebi_id,
                        label=label,
                        confidence=0.98,
                        predicate='exactMatch',
                        tool='GasDict|manual',
                        comment=f'Curated gas mapping',
                        mapping_method='curated_dictionary'
                    )
                    mappings.append(mapping)
                    print(f"✓ {ingredient_name:40s} → {chebi_id} ({label})")
                    break

    return pd.DataFrame(mappings)


def main():
    print("=" * 70)
    print("Map Gas Ingredients to CHEBI")
    print("=" * 70)
    print()

    # Find gas ingredients
    unmapped_file = Path('output/truly_unmapped_ingredients.tsv')
    print(f"Searching for gases in: {unmapped_file}")
    potential_gases = find_gas_ingredients(unmapped_file)
    print(f"Found {len(potential_gases)} potential gas ingredients")
    print()

    # Map to CHEBI
    print("Mapping gases to CHEBI:")
    print("-" * 70)
    gas_mappings_df = map_gases_to_chebi(potential_gases)
    print("-" * 70)
    print(f"Mapped {len(gas_mappings_df)} gases to CHEBI")
    print()

    if len(gas_mappings_df) == 0:
        print("No new gas mappings to add.")
        return

    # Load existing SSSOM
    sssom_file = Path('output/culturemech_chebi_mappings_final.sssom.tsv')
    print(f"Loading existing SSSOM: {sssom_file}")
    existing_df = load_sssom_file(sssom_file)
    metadata = extract_sssom_metadata(sssom_file)
    print(f"  Existing mappings: {len(existing_df)}")
    print()

    # Merge
    print("Merging gas mappings with existing SSSOM...")
    merged_df = pd.concat([existing_df, gas_mappings_df], ignore_index=True)

    # Remove duplicates (prefer higher confidence)
    merged_df = merged_df.sort_values('confidence', ascending=False)
    merged_df = merged_df.drop_duplicates(subset=['subject_id'], keep='first')

    print(f"  Total mappings after merge: {len(merged_df)}")
    print()

    # Save
    output_file = Path('output/culturemech_chebi_mappings_with_gases.sssom.tsv')
    save_sssom_file(merged_df, output_file, metadata)
    print(f"Saved to: {output_file}")
    print()

    # Summary
    print("=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Original SSSOM entries: {len(existing_df)}")
    print(f"New gas mappings: {len(gas_mappings_df)}")
    print(f"Final SSSOM entries: {len(merged_df)}")
    print(f"Net new mappings: {len(merged_df) - len(existing_df)}")
    print()

    # Show what was mapped
    print("Mapped gases:")
    for _, row in gas_mappings_df.iterrows():
        print(f"  {row['subject_label']:40s} → {row['object_id']}")
    print()
    print("=" * 70)


if __name__ == "__main__":
    main()
