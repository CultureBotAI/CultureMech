#!/usr/bin/env python3
"""Create new CultureMech recipe YAML from input data.

Helper script for the create-recipe skill to generate properly formatted
recipe YAML files from various input formats.
"""

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional

import yaml


def sanitize_filename(name: str) -> str:
    """Convert recipe name to safe filename.

    Args:
        name: Recipe name

    Returns:
        Sanitized filename (without .yaml extension)
    """
    # Replace spaces and special chars with underscores
    safe = re.sub(r'[^\w\s-]', '', name)
    safe = re.sub(r'[-\s]+', '_', safe)
    return safe.strip('_')


def parse_concentration(conc_str: str) -> Dict:
    """Parse concentration string to structured format.

    Args:
        conc_str: Concentration string like "10 g/L" or "5%"

    Returns:
        Dictionary with value and unit
    """
    # Common patterns
    patterns = [
        (r'([\d.]+)\s*g/[Ll]', lambda m: {'value': float(m[1]), 'unit': 'G_PER_L'}),
        (r'([\d.]+)\s*mg/[Ll]', lambda m: {'value': float(m[1]), 'unit': 'MG_PER_L'}),
        (r'([\d.]+)\s*%', lambda m: {'value': float(m[1]), 'unit': 'PERCENT'}),
        (r'([\d.]+)\s*[Mm][Mm]', lambda m: {'value': float(m[1]), 'unit': 'MM'}),
        (r'([\d.]+)\s*[Mm]', lambda m: {'value': float(m[1]), 'unit': 'M'}),
    ]

    for pattern, parser in patterns:
        match = re.match(pattern, conc_str.strip())
        if match:
            try:
                return parser(match)
            except (ValueError, IndexError):
                pass

    # Fallback: return as string
    return conc_str


def create_ingredient(name: str, concentration: str = None) -> Dict:
    """Create ingredient dictionary.

    Args:
        name: Ingredient name
        concentration: Concentration string (optional)

    Returns:
        Ingredient dictionary
    """
    ingredient = {
        'preferred_term': name.strip()
    }

    if concentration:
        parsed = parse_concentration(concentration)
        if isinstance(parsed, dict):
            # Structured concentration
            ingredient['concentration'] = parsed
        else:
            # Keep as string
            ingredient['concentration'] = concentration

    return ingredient


def create_recipe_template(
    name: str,
    ingredients: List[Dict],
    recipe_id: str = None,
    category: str = 'bacterial',
    medium_type: str = 'COMPLEX',
    physical_state: str = 'LIQUID',
    ph_value: float = None,
    notes: str = None
) -> Dict:
    """Create recipe YAML template.

    Args:
        name: Recipe name
        ingredients: List of ingredient dictionaries
        recipe_id: CultureMech ID (optional)
        category: Recipe category
        medium_type: Medium type enum value
        physical_state: Physical state enum value
        ph_value: pH value (optional)
        notes: Additional notes (optional)

    Returns:
        Recipe dictionary
    """
    recipe = {
        'name': name,
        'original_name': name,
        'category': category,
        'medium_type': medium_type,
        'physical_state': physical_state,
        'ingredients': ingredients,
    }

    # Add optional fields
    if recipe_id:
        recipe['id'] = recipe_id

    if ph_value:
        recipe['ph_value'] = ph_value

    if notes:
        recipe['notes'] = notes

    # Add curation history
    recipe['curation_history'] = [{
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'curator': 'create-recipe-skill',
        'action': 'Created new recipe from input data',
    }]

    return recipe


def parse_json_input(json_data: Dict) -> Dict:
    """Parse JSON input to recipe template.

    Args:
        json_data: JSON dictionary

    Returns:
        Recipe dictionary
    """
    name = json_data.get('name')
    if not name:
        raise ValueError("JSON must include 'name' field")

    # Parse ingredients
    ingredients = []
    for ing in json_data.get('ingredients', []):
        if isinstance(ing, dict):
            ingredient = create_ingredient(
                ing.get('name', ''),
                ing.get('concentration') or ing.get('amount')
            )
            ingredients.append(ingredient)
        elif isinstance(ing, str):
            # Just a name
            ingredients.append(create_ingredient(ing))

    if not ingredients:
        raise ValueError("JSON must include 'ingredients' list")

    # Map JSON fields to recipe fields
    medium_type = json_data.get('type', 'COMPLEX').upper()
    if medium_type == 'DEFINED':
        medium_type = 'DEFINED'
    elif medium_type == 'COMPLEX':
        medium_type = 'COMPLEX'

    physical_state = json_data.get('state', 'LIQUID').upper()

    return create_recipe_template(
        name=name,
        ingredients=ingredients,
        category=json_data.get('category', 'bacterial'),
        medium_type=medium_type,
        physical_state=physical_state,
        ph_value=json_data.get('ph'),
        notes=json_data.get('notes')
    )


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Create CultureMech recipe YAML from input'
    )

    parser.add_argument(
        '--json',
        type=Path,
        help='JSON file with recipe data'
    )

    parser.add_argument(
        '--name',
        type=str,
        help='Recipe name'
    )

    parser.add_argument(
        '--ingredients',
        type=str,
        help='Ingredients as JSON string'
    )

    parser.add_argument(
        '--category',
        type=str,
        default='bacterial',
        choices=['bacterial', 'algae', 'archaea', 'fungal', 'specialized', 'solutions'],
        help='Recipe category'
    )

    parser.add_argument(
        '--output',
        type=Path,
        help='Output file path (default: auto-generate in normalized_yaml)'
    )

    parser.add_argument(
        '--id',
        type=str,
        help='CultureMech ID (default: auto-assign)'
    )

    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Print YAML without saving'
    )

    args = parser.parse_args()

    try:
        # Parse input
        if args.json:
            with open(args.json, 'r') as f:
                json_data = json.load(f)
            recipe = parse_json_input(json_data)

        elif args.name and args.ingredients:
            # Parse ingredients from JSON string
            ingredients_data = json.loads(args.ingredients)
            ingredients = []
            for ing in ingredients_data:
                if isinstance(ing, dict):
                    ingredients.append(create_ingredient(
                        ing.get('name', ''),
                        ing.get('concentration')
                    ))

            recipe = create_recipe_template(
                name=args.name,
                ingredients=ingredients,
                recipe_id=args.id,
                category=args.category
            )

        else:
            print("Error: Must provide either --json or --name + --ingredients", file=sys.stderr)
            return 1

        # Generate YAML
        yaml_str = yaml.dump(recipe, default_flow_style=False, allow_unicode=True, sort_keys=False)

        if args.dry_run:
            print(yaml_str)
            return 0

        # Determine output path
        if args.output:
            output_path = args.output
        else:
            # Auto-generate path
            filename = sanitize_filename(recipe['name']) + '.yaml'
            output_path = Path(f"data/normalized_yaml/{args.category}/{filename}")

        # Create directory if needed
        output_path.parent.mkdir(parents=True, exist_ok=True)

        # Write file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(yaml_str)

        print(f"✅ Recipe created: {output_path}")
        print(f"   Name: {recipe['name']}")
        print(f"   Category: {args.category}")
        print(f"   Ingredients: {len(recipe['ingredients'])}")

        if args.id:
            print(f"   ID: {args.id}")

        return 0

    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
