#!/usr/bin/env python3
"""
Apply Edison deep research results to CultureMech recipe files.

Usage:
    python apply_edison_results.py --results edison_results.json --dry-run
    python apply_edison_results.py --results edison_results.json
"""

import argparse
import sys
import yaml
import json
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

sys.path.insert(0, str(Path(__file__).resolve().parent))
from record_io import write_record  # noqa: E402


def load_recipe(file_path: Path) -> Dict[str, Any]:
    """Load a YAML recipe file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)


def save_recipe(file_path: Path, recipe: Dict[str, Any], dry_run: bool = False):
    """Save updated recipe to YAML file."""
    if dry_run:
        print(f"[DRY RUN] Would write to: {file_path}")
        return

    # Shared writer: `width=120` re-wrapped every long scalar in the file, so half
    # of PR #140's diff was churn in untouched `notes:` (#141).
    write_record(file_path, recipe)


def apply_description(recipe: Dict[str, Any], description: str) -> List[str]:
    """Apply description from Edison results."""
    if not recipe.get('description'):
        recipe['description'] = description
        return ['description']
    return []


def apply_ph_value(recipe: Dict[str, Any], ph_value: float) -> List[str]:
    """Apply pH value from Edison results."""
    if not recipe.get('ph_value') and not recipe.get('ph_range'):
        recipe['ph_value'] = float(ph_value)
        return ['ph_value']
    return []


def apply_target_organisms(recipe: Dict[str, Any], organisms: List[Dict[str, str]]) -> List[str]:
    """Apply target organisms from Edison results."""
    if not recipe.get('target_organisms'):
        recipe['target_organisms'] = []

        for org in organisms:
            organism_entry = {
                'name': org['name']
            }

            # Add NCBITaxon ID if provided
            if 'ncbitaxon_id' in org and org['ncbitaxon_id']:
                organism_entry['organism_term'] = {
                    'id': org['ncbitaxon_id'],
                    'label': org['name']
                }

            recipe['target_organisms'].append(organism_entry)

        return ['target_organisms']
    return []


def apply_ingredient_mappings(recipe: Dict[str, Any], mappings: Dict[str, str]) -> List[str]:
    """Apply CHEBI mappings to ingredients."""
    fields_changed = []

    for ing in recipe.get('ingredients', []):
        ing_name = ing.get('name', '').lower()

        # Check if Edison provided CHEBI mapping for this ingredient
        for mapped_name, chebi_id in mappings.items():
            if mapped_name.lower() in ing_name or ing_name in mapped_name.lower():
                # Only add if not already mapped
                if not ing.get('ingredient_term'):
                    ing['ingredient_term'] = {
                        'id': chebi_id,
                        'label': mapped_name
                    }
                    if 'ingredients' not in fields_changed:
                        fields_changed.append('ingredients')
                break

    # Also check solution ingredients
    for sol in recipe.get('solutions', []):
        for ing in sol.get('ingredients', []):
            ing_name = ing.get('name', '').lower()

            for mapped_name, chebi_id in mappings.items():
                if mapped_name.lower() in ing_name or ing_name in mapped_name.lower():
                    if not ing.get('ingredient_term'):
                        ing['ingredient_term'] = {
                            'id': chebi_id,
                            'label': mapped_name
                        }
                        if 'solutions' not in fields_changed:
                            fields_changed.append('solutions')
                    break

    return fields_changed


def add_curation_event(recipe: Dict[str, Any], fields_changed: List[str],
                      notes: str = None):
    """Add curation history event."""
    if not fields_changed:
        return

    if 'curation_history' not in recipe:
        recipe['curation_history'] = []

    event = {
        'timestamp': datetime.now().isoformat() + 'Z',
        'curator': 'edison-deep-research',
        'action': 'ENRICHED',
        'fields_changed': fields_changed
    }

    if notes:
        event['notes'] = notes
    else:
        event['notes'] = 'Enriched with Edison deep research findings from peer-reviewed literature'

    recipe['curation_history'].append(event)


def apply_edison_result(recipe_file: Path, edison_result: Dict[str, Any],
                       yaml_dir: Path, dry_run: bool = False) -> bool:
    """
    Apply Edison research results to a recipe file.

    Returns True if any changes were made.
    """
    # Load recipe
    try:
        recipe = load_recipe(yaml_dir / recipe_file)
    except FileNotFoundError:
        print(f"ERROR: Recipe file not found: {yaml_dir / recipe_file}")
        return False
    except Exception as e:
        print(f"ERROR loading {recipe_file}: {e}")
        return False

    fields_changed = []

    # Apply description
    if 'description' in edison_result and edison_result['description']:
        fields_changed.extend(apply_description(recipe, edison_result['description']))

    # Apply pH value
    if 'ph_value' in edison_result and edison_result['ph_value']:
        try:
            fields_changed.extend(apply_ph_value(recipe, edison_result['ph_value']))
        except (ValueError, TypeError):
            print(f"WARNING: Invalid pH value for {recipe_file}: {edison_result['ph_value']}")

    # Apply target organisms
    if 'target_organisms' in edison_result and edison_result['target_organisms']:
        fields_changed.extend(apply_target_organisms(recipe, edison_result['target_organisms']))

    # Apply ingredient mappings
    if 'ingredient_mappings' in edison_result and edison_result['ingredient_mappings']:
        fields_changed.extend(apply_ingredient_mappings(recipe, edison_result['ingredient_mappings']))

    # Add curation event if any changes were made
    if fields_changed:
        notes = edison_result.get('notes', None)
        add_curation_event(recipe, fields_changed, notes)

        # Save updated recipe
        save_recipe(yaml_dir / recipe_file, recipe, dry_run)

        print(f"✓ Updated {recipe_file}: {', '.join(fields_changed)}")
        return True
    else:
        print(f"○ No changes for {recipe_file}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Apply Edison deep research results to CultureMech recipes"
    )
    parser.add_argument('--results', type=Path, required=True,
                       help='JSON file with Edison research results')
    parser.add_argument('--yaml-dir', type=Path, default=Path('data/normalized_yaml'),
                       help='Directory containing recipe YAML files')
    parser.add_argument('--dry-run', action='store_true',
                       help='Preview changes without writing files')

    args = parser.parse_args()

    # Load Edison results
    print("Loading Edison results...")
    with open(args.results, 'r') as f:
        edison_results = json.load(f)

    print(f"Found {len(edison_results)} Edison result entries")

    if args.dry_run:
        print("\n[DRY RUN MODE] - No files will be modified\n")

    # Process each result
    updates_made = 0
    no_changes = 0
    errors = 0

    for result in edison_results:
        recipe_file = result.get('file_path')
        if not recipe_file:
            print("WARNING: Result missing 'file_path', skipping")
            errors += 1
            continue

        try:
            changed = apply_edison_result(
                Path(recipe_file),
                result,
                args.yaml_dir,
                args.dry_run
            )

            if changed:
                updates_made += 1
            else:
                no_changes += 1

        except Exception as e:
            print(f"ERROR processing {recipe_file}: {e}")
            errors += 1
            continue

    # Summary
    print("\n" + "=" * 70)
    print("Summary")
    print("=" * 70)
    print(f"Total recipes processed: {len(edison_results)}")
    print(f"  Updated: {updates_made}")
    print(f"  No changes: {no_changes}")
    print(f"  Errors: {errors}")

    if args.dry_run:
        print("\n[DRY RUN] No files were modified. Run without --dry-run to apply changes.")
    else:
        print(f"\nSuccessfully updated {updates_made} recipe files.")
        print("\nNext steps:")
        print("1. Validate updated recipes: just validate-recipes")
        print("2. Review changes: git diff data/normalized_yaml/")
        print("3. Re-run quality analysis to verify improvements")
        print("4. Commit changes: git commit -m 'Enrich recipes with Edison results'")


if __name__ == '__main__':
    main()
