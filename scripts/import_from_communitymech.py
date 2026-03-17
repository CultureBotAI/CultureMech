#!/usr/bin/env python3
"""Import media records from CommunityMech to CultureMech.

This script converts CommunityMech growth_media records into CultureMech MediaRecipe YAMLs,
preserving MediaIngredientMech mappings, evidence, and provenance tracking.

Usage:
    python scripts/import_from_communitymech.py \\
        --manifest data/import_tracking/unmapped_media_manifest.yaml \\
        --communitymech-repo ../CommunityMech/CommunityMech \\
        --output-dir data/normalized_yaml \\
        --assign-ids \\
        --dry-run  # Optional: preview only
"""

import argparse
import json
import yaml
import sys
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Any, Optional

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from culturemech.utils.id_utils import mint_next_id, generate_xmech_id


# Field mapping from CommunityMech to CultureMech
FIELD_MAPPING = {
    'name': 'name',
    'ph': 'ph_value',
    'temperature': 'temperature_value',
    'temperature_unit': 'temperature_unit',
    'atmosphere': 'incubation_atmosphere',
    'preparation_notes': 'notes',
}

# Unit conversion mapping
UNIT_CONVERSION = {
    'g/L': 'G_PER_L',
    'G/L': 'G_PER_L',
    'mg/L': 'MG_PER_L',
    'MG/L': 'MG_PER_L',
    'µg/L': 'MICROG_PER_L',
    'ug/L': 'MICROG_PER_L',
    'M': 'MOLAR',
    'mM': 'MILLIMOLAR',
    'µM': 'MICROMOLAR',
    'μM': 'MICROMOLAR',  # Alternative mu character
    'uM': 'MICROMOLAR',
    '% (w/v)': 'PERCENT_W_V',
    '% (v/v)': 'PERCENT_V_V',
    '%': 'PERCENT_W_V',  # Default % to w/v
    'x (half-strength)': 'VARIABLE',  # Special case for dilutions
    'degrees Celsius': 'CELSIUS',
    '°C': 'CELSIUS',
    'C': 'CELSIUS',
}


def load_manifest(manifest_path: Path) -> Dict[str, Any]:
    """Load the unmapped media manifest."""
    with open(manifest_path) as f:
        return yaml.safe_load(f)


def load_communitymech_yaml(yaml_path: Path) -> Dict[str, Any]:
    """Load a CommunityMech YAML file."""
    with open(yaml_path) as f:
        return yaml.safe_load(f)


def extract_growth_media(data: Dict[str, Any], media_name: str) -> Optional[Dict[str, Any]]:
    """Extract a specific growth medium from CommunityMech data."""
    for medium in data.get('growth_media', []):
        if medium.get('name') == media_name:
            return medium
    return None


def infer_category(media_dict: Dict[str, Any], community_dict: Dict[str, Any]) -> str:
    """Infer CultureMech category from CommunityMech metadata."""
    comm_category = community_dict.get('community_category', '')
    media_name = media_dict.get('name', '').lower()

    # DIET communities → specialized
    if 'DIET' in comm_category or 'diet' in media_name:
        return 'specialized'

    # Plant growth media → specialized
    if any(keyword in media_name for keyword in ['plant', 'arabidopsis', 'lotus', 'soybean', 'murashige']):
        return 'specialized'

    # Thermophilic (>55°C) → archaea
    try:
        temp = float(media_dict.get('temperature', 0))
        if temp >= 55:
            return 'archaea'
    except (ValueError, TypeError):
        pass

    # Default to bacterial
    return 'bacterial'


def convert_unit(unit_str: str) -> str:
    """Convert CommunityMech unit string to CultureMech ConcentrationUnitEnum."""
    if not unit_str:
        return 'VARIABLE'

    # Direct mapping
    if unit_str in UNIT_CONVERSION:
        return UNIT_CONVERSION[unit_str]

    # Fallback: keep original if not recognized
    print(f"  Warning: Unrecognized unit '{unit_str}', using VARIABLE")
    return 'VARIABLE'


def convert_temperature_unit(unit_str: str) -> str:
    """Convert temperature unit string to TemperatureUnitEnum."""
    if not unit_str:
        return 'CELSIUS'

    if unit_str in UNIT_CONVERSION:
        return UNIT_CONVERSION[unit_str]

    return 'CELSIUS'  # Default


def convert_ingredients(composition: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """Convert CommunityMech composition to CultureMech ingredients."""
    ingredients = []

    for item in composition:
        ingredient = {
            'preferred_term': item.get('name', 'Unknown'),
        }

        # Add concentration if present (as STRING per CultureMech schema)
        if 'concentration' in item and 'unit' in item:
            try:
                concentration_value = str(float(item['concentration']))
                ingredient['concentration'] = {
                    'value': concentration_value,
                    'unit': convert_unit(item['unit'])
                }
            except (ValueError, TypeError):
                print(f"  Warning: Could not convert concentration for {item.get('name')}")

        # Preserve MediaIngredientMech ID if present
        if 'media_ingredient_mech_id' in item:
            ingredient['mediaingredientmech_term'] = {
                'id': item['media_ingredient_mech_id'],
            }
            # Note: Do not include URL - not in CultureMech schema

        # Add CHEBI term if present (use 'term' not 'chemical' per schema)
        if 'chebi_term' in item and isinstance(item['chebi_term'], dict):
            chebi_term = item['chebi_term']
            if 'term' in chebi_term:
                ingredient['term'] = {
                    'id': chebi_term['term'].get('id', ''),
                    'label': chebi_term['term'].get('label', ''),
                }

        ingredients.append(ingredient)

    return ingredients


def convert_to_culturemech(
    media_dict: Dict[str, Any],
    community_dict: Dict[str, Any],
    community_ids: List[str],
    culturemech_id: Optional[str] = None
) -> Dict[str, Any]:
    """Convert CommunityMech growth_media to CultureMech MediaRecipe format."""

    # Base recipe structure
    recipe = {
        'name': media_dict.get('name', 'Unknown Medium'),
        'original_name': media_dict.get('name', 'Unknown Medium'),
        'category': infer_category(media_dict, community_dict),
        'medium_type': 'DEFINED',  # Most CommunityMech media are defined
        'physical_state': 'LIQUID',  # Default, can be overridden
    }

    # Add CultureMech ID if provided
    if culturemech_id:
        recipe['id'] = culturemech_id

    # Convert ingredients
    if 'composition' in media_dict:
        recipe['ingredients'] = convert_ingredients(media_dict['composition'])

    # Map simple fields
    if 'ph' in media_dict:
        try:
            recipe['ph_value'] = float(media_dict['ph'])
        except (ValueError, TypeError):
            pass

    # Temperature (use temperature_value, not incubation_temperature structure)
    if 'temperature' in media_dict:
        try:
            temp_value = float(media_dict['temperature'])
            recipe['temperature_value'] = temp_value
            # Note: CultureMech uses temperature_value (float) not incubation_temperature (object)
        except (ValueError, TypeError):
            pass

    # Atmosphere
    if 'atmosphere' in media_dict:
        atmosphere = media_dict['atmosphere'].upper()
        if atmosphere in ['AEROBIC', 'ANAEROBIC', 'MICROAEROPHILIC']:
            recipe['incubation_atmosphere'] = atmosphere

    # Build notes from multiple fields
    notes_parts = []

    if 'headspace_gas' in media_dict:
        notes_parts.append(f"Headspace gas: {media_dict['headspace_gas']}")

    if 'vessel_type' in media_dict:
        notes_parts.append(f"Vessel type: {media_dict['vessel_type']}")

    if 'light_regime' in media_dict:
        notes_parts.append(f"Light regime: {media_dict['light_regime']}")

    if 'light_intensity' in media_dict:
        notes_parts.append(f"Light intensity: {media_dict['light_intensity']}")

    if 'incubation_time' in media_dict:
        time_val = media_dict['incubation_time']
        time_unit = media_dict.get('incubation_time_unit', '')
        notes_parts.append(f"Incubation time: {time_val} {time_unit}")

    if 'inoculum_source' in media_dict:
        notes_parts.append(f"Inoculum source: {media_dict['inoculum_source']}")

    if 'preparation_notes' in media_dict:
        notes_parts.append(f"\n{media_dict['preparation_notes']}")

    if notes_parts:
        recipe['notes'] = '\n'.join(notes_parts)

    # Source data (provenance)
    recipe['source_data'] = {
        'origin': 'CommunityMech',
        'community_ids': community_ids,
        'import_date': datetime.now().date().isoformat(),
        'notes': f"Imported from CommunityMech {', '.join(community_ids)}"
    }

    # Preserve evidence (filter to only CultureMech schema fields)
    if 'evidence' in media_dict and isinstance(media_dict['evidence'], list):
        filtered_evidence = []
        for ev in media_dict['evidence']:
            # Only include fields that exist in CultureMech EvidenceItem schema
            culturemech_ev = {}
            if 'reference' in ev:
                culturemech_ev['reference'] = ev['reference']
            if 'supports' in ev:
                culturemech_ev['supports'] = ev['supports']
            if 'snippet' in ev:
                culturemech_ev['snippet'] = ev['snippet']
            if 'explanation' in ev:
                culturemech_ev['explanation'] = ev['explanation']
            # Skip: evidence_source (not in CultureMech schema)
            if culturemech_ev:  # Only add if has at least one field
                filtered_evidence.append(culturemech_ev)

        if filtered_evidence:
            recipe['source_data']['evidence'] = filtered_evidence

    # Curation history
    recipe['curation_history'] = [
        {
            'timestamp': datetime.now().isoformat() + 'Z',
            'curator': 'communitymech-importer-v1.0',
            'action': 'Imported from CommunityMech',
            'notes': f"Created from {', '.join(community_ids)} growth_media record"
        }
    ]

    return recipe


def sanitize_filename(name: str) -> str:
    """Convert media name to safe filename."""
    # Replace problematic characters
    safe = name.replace('/', '_')
    safe = safe.replace(':', '')
    safe = safe.replace(' ', '_')
    safe = safe.replace('-', '_')
    safe = safe.replace('(', '')
    safe = safe.replace(')', '')
    safe = safe.replace(',', '')
    safe = safe.replace('.', '_')

    # Remove consecutive underscores
    while '__' in safe:
        safe = safe.replace('__', '_')

    return safe.strip('_')


def save_recipe(
    recipe: Dict[str, Any],
    output_dir: Path,
    dry_run: bool = False
) -> Path:
    """Save recipe to appropriate category directory."""
    category = recipe['category']
    category_dir = output_dir / category

    # Create filename from recipe name
    filename = sanitize_filename(recipe['name']) + '.yaml'
    output_path = category_dir / filename

    if dry_run:
        print(f"  [DRY RUN] Would save to: {output_path}")
        print(f"  Content preview:")
        print(yaml.dump(recipe, default_flow_style=False, sort_keys=False)[:500])
        print("  ...")
        return output_path

    # Create directory if needed
    category_dir.mkdir(parents=True, exist_ok=True)

    # Write YAML
    with open(output_path, 'w') as f:
        yaml.dump(recipe, f, default_flow_style=False, sort_keys=False)

    print(f"  ✓ Saved to: {output_path}")
    return output_path


def main():
    parser = argparse.ArgumentParser(
        description='Import media records from CommunityMech to CultureMech'
    )
    parser.add_argument(
        '--manifest',
        type=Path,
        required=True,
        help='Path to unmapped media manifest YAML'
    )
    parser.add_argument(
        '--communitymech-repo',
        type=Path,
        required=True,
        help='Path to CommunityMech repository root'
    )
    parser.add_argument(
        '--output-dir',
        type=Path,
        required=True,
        help='Output directory for CultureMech YAMLs'
    )
    parser.add_argument(
        '--assign-ids',
        action='store_true',
        help='Assign CultureMech IDs to new records'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Preview only, do not write files'
    )

    args = parser.parse_args()

    # Load manifest
    print(f"Loading manifest: {args.manifest}")
    manifest = load_manifest(args.manifest)

    # Find highest existing CultureMech ID if assigning IDs
    next_id_num = None
    if args.assign_ids:
        from culturemech.utils.id_utils import find_highest_id_multi_file
        highest = find_highest_id_multi_file(args.output_dir, 'CultureMech')
        next_id_num = highest + 1
        print(f"Highest existing ID: CultureMech:{highest:06d}")
        print(f"Next ID will be: CultureMech:{next_id_num:06d}\n")

    # Process each medium
    import_log = []

    for i, media_entry in enumerate(manifest['media'], 1):
        media_name = media_entry['name']
        community_ids = media_entry['community_ids']
        source_files = media_entry['source_files']

        print(f"\n[{i}/{len(manifest['media'])}] Processing: {media_name}")
        print(f"  Community IDs: {', '.join(community_ids)}")

        # Load first source file (primary source)
        primary_source = args.communitymech_repo / source_files[0]
        print(f"  Loading: {primary_source}")

        try:
            community_data = load_communitymech_yaml(primary_source)
        except Exception as e:
            print(f"  ✗ Error loading {primary_source}: {e}")
            continue

        # Extract growth medium
        media_dict = extract_growth_media(community_data, media_name)
        if not media_dict:
            print(f"  ✗ Could not find medium '{media_name}' in {primary_source}")
            continue

        # Assign CultureMech ID if requested
        culturemech_id = None
        if args.assign_ids:
            culturemech_id = generate_xmech_id('CultureMech', next_id_num)
            print(f"  Assigned ID: {culturemech_id}")
            next_id_num += 1

        # Convert to CultureMech format
        recipe = convert_to_culturemech(
            media_dict,
            community_data,
            community_ids,
            culturemech_id
        )

        # Save recipe
        output_path = save_recipe(recipe, args.output_dir, args.dry_run)

        # Log import
        import_log.append({
            'media_name': media_name,
            'culturemech_id': culturemech_id,
            'community_ids': community_ids,
            'source_files': source_files,
            'output_path': str(output_path),
            'category': recipe['category'],
            'import_timestamp': datetime.now().isoformat()
        })

    # Save import log
    if not args.dry_run:
        log_path = args.output_dir.parent / 'import_tracking' / 'communitymech_imports.json'
        log_path.parent.mkdir(parents=True, exist_ok=True)

        with open(log_path, 'w') as f:
            json.dump(import_log, f, indent=2)

        print(f"\n✓ Import log saved to: {log_path}")

    print(f"\n{'=' * 60}")
    print(f"Import complete: {len(import_log)} media processed")
    if args.dry_run:
        print("(DRY RUN - no files were written)")
    print(f"{'=' * 60}")


if __name__ == '__main__':
    main()
