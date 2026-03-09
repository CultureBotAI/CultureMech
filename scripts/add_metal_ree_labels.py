#!/usr/bin/env python3
"""
Add high_metal and high_ree labels to media YAML files based on analysis.
"""

import yaml
from pathlib import Path


def add_labels_to_media():
    """Add high_metal and high_ree labels to media files."""

    # Load analysis results
    analysis_file = Path("data/metal_ree_analysis.yaml")
    with open(analysis_file) as f:
        analysis = yaml.safe_load(f)

    high_metal_media = set(analysis['high_metal_media'])
    high_ree_media = set(analysis['high_ree_media'])

    print(f"📋 Loaded analysis results:")
    print(f"   - {len(high_metal_media)} high-metal media")
    print(f"   - {len(high_ree_media)} high-REE media\n")

    updated_count = 0
    media_dir = Path("data/normalized_yaml")

    # Process all media YAML files
    for category_dir in media_dir.iterdir():
        if not category_dir.is_dir():
            continue

        for yaml_file in category_dir.glob("*.yaml"):
            try:
                with open(yaml_file) as f:
                    media_data = yaml.safe_load(f)

                if not media_data:
                    continue

                media_name = yaml_file.stem
                modified = False

                # Add high_metal label
                if media_name in high_metal_media:
                    if media_data.get('high_metal') != True:
                        media_data['high_metal'] = True
                        modified = True
                else:
                    if 'high_metal' in media_data:
                        del media_data['high_metal']
                        modified = True

                # Add high_ree label
                if media_name in high_ree_media:
                    if media_data.get('high_ree') != True:
                        media_data['high_ree'] = True
                        modified = True
                else:
                    if 'high_ree' in media_data:
                        del media_data['high_ree']
                        modified = True

                # Write back if modified
                if modified:
                    with open(yaml_file, 'w') as f:
                        yaml.dump(media_data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)
                    updated_count += 1

            except Exception as e:
                print(f"⚠ Error processing {yaml_file.name}: {e}")
                continue

    print(f"✓ Updated {updated_count} media files with metal/REE labels")


if __name__ == "__main__":
    add_labels_to_media()
