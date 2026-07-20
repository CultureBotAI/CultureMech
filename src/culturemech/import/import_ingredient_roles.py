"""
Import ingredient roles from PFASCommunityAgents TSV.
Enriches existing media recipes with role annotations.
"""

import csv
from pathlib import Path
import yaml
import sys

from culturemech.curate.curation_event import record_curation_event

PFAS_REPO = Path("/Users/marcin/Documents/VIMSS/ontology/PFAS/PFASCommunityAgents")
INGREDIENT_FILE = PFAS_REPO / "data/sheets_pfas/PFAS_Data_for_AI_media_ingredients_extended.tsv"

# Map PFAS role tokens (lowercase source values) to CultureMech faceted role
# assignments. Each entry is (slot_name, enum_value_token) — the writer
# below buckets assignments by slot when populating an IngredientDescriptor.
#
# Facet decisions:
# - carbon/nitrogen/vitamin/protein/amino-acid → NutritionalRoleEnum values
#   (nutritional_roles slot).
# - buffer/solidifying → PhysicochemicalRoleEnum values (physicochemical_roles).
# - "mineral" has no direct NutritionalRoleEnum equivalent; mapped to
#   TRACE_ELEMENT as the broadest catch-all. Curators should refine to
#   PHOSPHATE_SOURCE / IRON_SOURCE / SULFUR_SOURCE where applicable.
# - "salt" has no NutritionalRoleEnum equivalent (salts contribute ionic
#   strength / osmotic pressure, not elemental supply); mapped to
#   PhysicochemicalRoleEnum.OSMOTIC_AGENT.
ROLE_MAPPING = {
    "carbon source":      ("nutritional_roles",     "CARBON_SOURCE"),
    "nitrogen source":    ("nutritional_roles",     "NITROGEN_SOURCE"),
    "mineral":            ("nutritional_roles",     "TRACE_ELEMENT"),
    "trace element":      ("nutritional_roles",     "TRACE_ELEMENT"),
    "vitamin source":     ("nutritional_roles",     "VITAMIN_SOURCE"),
    "protein source":     ("nutritional_roles",     "PROTEIN_SOURCE"),
    "amino acid source":  ("nutritional_roles",     "AMINO_ACID_SOURCE"),
    "buffer":             ("physicochemical_roles", "BUFFER"),
    "salt":               ("physicochemical_roles", "OSMOTIC_AGENT"),
    "solidifying agent":  ("physicochemical_roles", "SOLIDIFYING_AGENT"),
}


def load_ingredient_roles():
    """Load ingredient roles from PFAS TSV.

    Returns:
        dict[chebi_id, dict[slot_name, list[enum_value]]] — a per-CHEBI
        bucket keyed by faceted-slot name.
    """
    if not INGREDIENT_FILE.exists():
        print(f"Warning: PFAS data file not found at {INGREDIENT_FILE}")
        return {}

    roles_db: dict[str, dict[str, list[str]]] = {}

    with open(INGREDIENT_FILE) as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            chebi_id = row.get('ontology_id', '').strip()
            role_raw = row.get('role', '').strip()
            mapping = ROLE_MAPPING.get(role_raw)

            if chebi_id and mapping:
                slot, enum_value = mapping
                slot_bucket = roles_db.setdefault(chebi_id, {})
                slot_bucket.setdefault(slot, [])
                if enum_value not in slot_bucket[slot]:
                    slot_bucket[slot].append(enum_value)

    print(f"Loaded facet role mappings for {len(roles_db)} ingredients")
    return roles_db


def enrich_recipe_with_roles(recipe_path: Path, roles_db: dict, dry_run: bool = False):
    """Add faceted role annotations to ingredients in a recipe.

    Writes to `nutritional_roles` / `physicochemical_roles` per the ROLE_MAPPING
    facet assignment. Skips an ingredient's slot if the slot is already set on
    that ingredient (never overwrites curator assignments).
    """
    with open(recipe_path) as f:
        recipe = yaml.safe_load(f)

    modified = False
    changes = []

    for ingredient in recipe.get('ingredients', []):
        term = ingredient.get('term', {})
        chebi_id = term.get('id')

        if chebi_id in roles_db:
            for slot, enum_values in roles_db[chebi_id].items():
                if slot in ingredient:
                    continue  # never overwrite existing assignments
                ingredient[slot] = list(enum_values)
                modified = True
                changes.append(
                    f"  Added {slot}={enum_values} to {ingredient.get('preferred_term', 'unknown')}"
                )

    if modified:
        if not dry_run:
            record_curation_event(
                recipe,
                curator="import_ingredient_roles.py",
                action="ENRICHED_INGREDIENT_ROLES",
                notes=f"roles_added_to={len(changes)} ingredients",
                source="PFAS_Data_for_AI_media_ingredients_extended.tsv",
                skip_if_recent=True,
            )
            with open(recipe_path, 'w') as f:
                yaml.dump(recipe, f, default_flow_style=False, allow_unicode=True, sort_keys=False)
            print(f"✓ Updated {recipe_path.name}")
        else:
            print(f"Would update {recipe_path.name}:")

        for change in changes:
            print(change)

    return modified


def enrich_all_recipes(kb_dir: Path, roles_db: dict, dry_run: bool = False):
    """Enrich all recipes in the knowledge base."""
    recipe_files = list(kb_dir.glob("**/*.yaml"))
    print(f"Found {len(recipe_files)} recipe files")

    updated_count = 0
    for recipe_path in recipe_files:
        try:
            if enrich_recipe_with_roles(recipe_path, roles_db, dry_run=dry_run):
                updated_count += 1
        except Exception as e:
            print(f"Error processing {recipe_path}: {e}")

    print(f"\n✓ {'Would update' if dry_run else 'Updated'} {updated_count} recipes with ingredient roles")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Import ingredient roles from PFAS data")
    parser.add_argument("--kb-dir", type=Path, default=Path("data/normalized_yaml"),
                        help="Knowledge base directory (default: data/normalized_yaml)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be changed without modifying files")

    args = parser.parse_args()

    if not args.kb_dir.exists():
        print(f"Error: Knowledge base directory not found: {args.kb_dir}")
        sys.exit(1)

    roles_db = load_ingredient_roles()
    if not roles_db:
        print("No ingredient roles loaded. Exiting.")
        sys.exit(1)

    enrich_all_recipes(args.kb_dir, roles_db, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
