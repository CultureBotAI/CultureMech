"""
Import ingredient roles from PFASCommunityAgents TSV.
Enriches existing media recipes with role annotations.
"""

import csv
from pathlib import Path
import yaml
import sys

PFAS_REPO = Path("/Users/marcin/Documents/VIMSS/ontology/PFAS/PFASCommunityAgents")
INGREDIENT_FILE = PFAS_REPO / "data/sheets_pfas/PFAS_Data_for_AI_media_ingredients_extended.tsv"

# Map PFAS roles to CultureMech IngredientRoleEnum values
ROLE_MAPPING = {
    "carbon source": "CARBON_SOURCE",
    "nitrogen source": "NITROGEN_SOURCE",
    "mineral": "MINERAL",
    "buffer": "BUFFER",
    "trace element": "TRACE_ELEMENT",
    "vitamin source": "VITAMIN_SOURCE",
    "salt": "SALT",
    "protein source": "PROTEIN_SOURCE",
    "amino acid source": "AMINO_ACID_SOURCE",
    "solidifying agent": "SOLIDIFYING_AGENT",
}


def load_ingredient_roles():
    """Load ingredient roles from PFAS TSV."""
    if not INGREDIENT_FILE.exists():
        print(f"Warning: PFAS data file not found at {INGREDIENT_FILE}")
        return {}

    roles_db = {}

    with open(INGREDIENT_FILE) as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            chebi_id = row.get('ontology_id', '').strip()
            role_raw = row.get('role', '').strip()
            role_enum = ROLE_MAPPING.get(role_raw)

            if chebi_id and role_enum:
                if chebi_id not in roles_db:
                    roles_db[chebi_id] = []
                if role_enum not in roles_db[chebi_id]:
                    roles_db[chebi_id].append(role_enum)

    print(f"Loaded {len(roles_db)} ingredient role mappings")
    return roles_db


def enrich_recipe_with_roles(recipe_path: Path, roles_db: dict, dry_run: bool = False):
    """Add role annotations to ingredients in a recipe."""
    with open(recipe_path) as f:
        recipe = yaml.safe_load(f)

    modified = False
    changes = []

    for ingredient in recipe.get('ingredients', []):
        term = ingredient.get('term', {})
        chebi_id = term.get('id')

        if chebi_id in roles_db and 'role' not in ingredient:
            ingredient['role'] = roles_db[chebi_id]
            modified = True
            changes.append(f"  Added roles {roles_db[chebi_id]} to {ingredient.get('preferred_term', 'unknown')}")

    if modified:
        if not dry_run:
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
    parser.add_argument("--kb-dir", type=Path, default=Path("kb/media"),
                        help="Knowledge base directory (default: kb/media)")
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
