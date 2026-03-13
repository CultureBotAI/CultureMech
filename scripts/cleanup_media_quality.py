#!/usr/bin/env python3
"""
Comprehensive media data quality cleanup script.

Fixes:
1. Duplicate ingredients (merges or flags conflicts)
2. Missing pH buffers (extracts from notes → ingredients)
3. Other data quality issues

Generates detailed report of all changes.
"""

import re
import yaml
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple, Optional


class MediaQualityFixer:
    """Fix data quality issues in media YAML files."""

    # Common pH buffers and their CHEBI IDs
    PH_BUFFERS = {
        'naoh': {'id': 'CHEBI:32145', 'label': 'sodium hydroxide', 'preferred': 'NaOH'},
        'sodium hydroxide': {'id': 'CHEBI:32145', 'label': 'sodium hydroxide', 'preferred': 'NaOH'},
        'hcl': {'id': 'CHEBI:17883', 'label': 'hydrochloric acid', 'preferred': 'HCl'},
        'hydrochloric acid': {'id': 'CHEBI:17883', 'label': 'hydrochloric acid', 'preferred': 'HCl'},
        'h2so4': {'id': 'CHEBI:26836', 'label': 'sulfuric acid', 'preferred': 'H2SO4'},
        'sulfuric acid': {'id': 'CHEBI:26836', 'label': 'sulfuric acid', 'preferred': 'H2SO4'},
        'koh': {'id': 'CHEBI:32035', 'label': 'potassium hydroxide', 'preferred': 'KOH'},
        'potassium hydroxide': {'id': 'CHEBI:32035', 'label': 'potassium hydroxide', 'preferred': 'KOH'},
        'na2co3': {'id': 'CHEBI:29377', 'label': 'sodium carbonate', 'preferred': 'Na2CO3'},
        'sodium carbonate': {'id': 'CHEBI:29377', 'label': 'sodium carbonate', 'preferred': 'Na2CO3'},
        'nahco3': {'id': 'CHEBI:32139', 'label': 'sodium hydrogen carbonate', 'preferred': 'NaHCO3'},
        'sodium bicarbonate': {'id': 'CHEBI:32139', 'label': 'sodium hydrogen carbonate', 'preferred': 'NaHCO3'},
        'sodium hydrogen carbonate': {'id': 'CHEBI:32139', 'label': 'sodium hydrogen carbonate', 'preferred': 'NaHCO3'},
    }

    def __init__(self):
        self.stats = {
            'files_processed': 0,
            'files_modified': 0,
            'duplicates_merged': 0,
            'duplicates_flagged': 0,
            'ph_buffers_added': 0,
            'errors': []
        }
        self.changes_log = []

    def normalize_name(self, name: str) -> str:
        """Normalize ingredient name for comparison."""
        name = name.lower().strip()
        # Remove common variations
        name = re.sub(r'\s+', ' ', name)
        name = re.sub(r'^(d|l|dl)-', '', name)
        return name

    def extract_ph_buffers_from_notes(self, notes: str) -> List[Dict]:
        """Extract pH buffers mentioned in notes."""
        if not notes:
            return []

        buffers = []
        notes_lower = notes.lower()

        # Pattern 1: "pH buffer: NaOH" or "pH adjusted with HCl"
        patterns = [
            r'ph\s+buffer:\s*([a-z0-9]+)',
            r'ph\s+adjusted\s+with\s+([a-z0-9]+)',
            r'adjusted\s+to\s+ph\s+[\d.]+\s+with\s+([a-z0-9]+)',
            r'ph\s+adjustment:\s*([a-z0-9]+)',
        ]

        for pattern in patterns:
            matches = re.finditer(pattern, notes_lower)
            for match in matches:
                buffer_name = match.group(1).strip()
                if buffer_name in self.PH_BUFFERS:
                    buffer_info = self.PH_BUFFERS[buffer_name]
                    buffers.append({
                        'preferred_term': buffer_info['preferred'],
                        'term': {
                            'id': buffer_info['id'],
                            'label': buffer_info['label']
                        },
                        'notes': 'pH adjustment (extracted from notes)'
                    })

        return buffers

    def merge_duplicate_ingredients(self, ingredients: List[Dict]) -> Tuple[List[Dict], List[str]]:
        """
        Merge duplicate ingredients.

        Returns:
            (merged_ingredients, warnings)
        """
        if not ingredients:
            return [], []

        # Group by normalized name
        groups = defaultdict(list)
        for ing in ingredients:
            norm_name = self.normalize_name(ing.get('preferred_term', ''))
            groups[norm_name].append(ing)

        merged = []
        warnings = []

        for norm_name, group in groups.items():
            if len(group) == 1:
                # No duplicates
                merged.append(group[0])
            else:
                # Has duplicates - try to merge
                merged_ing, warning = self._merge_ingredient_group(group)
                merged.append(merged_ing)
                if warning:
                    warnings.append(warning)

        return merged, warnings

    def _merge_ingredient_group(self, group: List[Dict]) -> Tuple[Dict, Optional[str]]:
        """Merge a group of duplicate ingredients."""
        # Use first as base
        base = group[0].copy()

        # Collect all concentrations
        concentrations = []
        units = set()

        for ing in group:
            if 'concentration' in ing and ing['concentration']:
                conc = ing['concentration']
                if 'value' in conc and 'unit' in conc:
                    try:
                        concentrations.append(float(conc['value']))
                        units.add(conc['unit'])
                    except (ValueError, TypeError):
                        pass

        warning = None

        if len(concentrations) > 1:
            if len(units) == 1:
                # Same unit - sum concentrations
                total = sum(concentrations)
                base['concentration'] = {
                    'value': str(total),
                    'unit': list(units)[0]
                }
                base['notes'] = base.get('notes', '') + f' [Merged {len(group)} duplicates: {", ".join(map(str, concentrations))}]'
                self.stats['duplicates_merged'] += 1
            else:
                # Different units - flag conflict
                warning = f"Duplicate '{base.get('preferred_term')}' with different units: {units}"
                base['notes'] = base.get('notes', '') + f' [WARNING: {len(group)} duplicates with conflicting units]'
                self.stats['duplicates_flagged'] += 1
        elif len(concentrations) == 1:
            # Multiple entries but only one has concentration
            self.stats['duplicates_merged'] += 1

        return base, warning

    def process_file(self, yaml_path: Path) -> bool:
        """
        Process a single YAML file.

        Returns:
            True if file was modified
        """
        try:
            with open(yaml_path, 'r') as f:
                data = yaml.safe_load(f)

            if not data:
                return False

            self.stats['files_processed'] += 1
            modified = False
            file_changes = []

            # Get ingredients
            ingredients = data.get('ingredients', [])
            if not ingredients:
                return False

            # 1. Merge duplicates
            original_count = len(ingredients)
            merged_ingredients, warnings = self.merge_duplicate_ingredients(ingredients)

            if len(merged_ingredients) < original_count:
                duplicates_removed = original_count - len(merged_ingredients)
                file_changes.append(f"Merged {duplicates_removed} duplicate ingredient(s)")
                modified = True

            if warnings:
                for warning in warnings:
                    file_changes.append(f"WARNING: {warning}")
                    self.stats['errors'].append(f"{yaml_path.name}: {warning}")

            # 2. Extract pH buffers from notes
            notes = data.get('notes', '')
            ph_buffers = self.extract_ph_buffers_from_notes(notes)

            if ph_buffers:
                # Check if already in ingredients
                existing_names = {self.normalize_name(ing.get('preferred_term', ''))
                                 for ing in merged_ingredients}

                for buffer in ph_buffers:
                    buffer_norm = self.normalize_name(buffer['preferred_term'])
                    if buffer_norm not in existing_names:
                        merged_ingredients.append(buffer)
                        file_changes.append(f"Added pH buffer: {buffer['preferred_term']}")
                        self.stats['ph_buffers_added'] += 1
                        modified = True

            # Update data if modified
            if modified:
                data['ingredients'] = merged_ingredients

                # Add curation history entry
                if 'curation_history' not in data:
                    data['curation_history'] = []

                data['curation_history'].append({
                    'timestamp': datetime.utcnow().isoformat() + 'Z',
                    'curator': 'data-quality-cleanup-v1.0',
                    'action': 'Data quality fixes',
                    'notes': '; '.join(file_changes)
                })

                # Write back to file
                with open(yaml_path, 'w') as f:
                    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

                self.stats['files_modified'] += 1
                self.changes_log.append({
                    'file': yaml_path.name,
                    'changes': file_changes
                })

            return modified

        except Exception as e:
            error_msg = f"Error processing {yaml_path.name}: {e}"
            self.stats['errors'].append(error_msg)
            print(f"⚠ {error_msg}")
            return False

    def process_directory(self, base_dir: Path):
        """Process all YAML files in directory tree."""
        yaml_files = list(base_dir.rglob('*.yaml'))

        print(f"🔍 Found {len(yaml_files)} YAML files to process\n")

        for yaml_path in yaml_files:
            self.process_file(yaml_path)

    def generate_report(self) -> str:
        """Generate detailed report of changes."""
        report = []
        report.append("=" * 80)
        report.append("MEDIA DATA QUALITY CLEANUP REPORT")
        report.append("=" * 80)
        report.append("")

        # Summary statistics
        report.append("SUMMARY:")
        report.append(f"  Files processed: {self.stats['files_processed']}")
        report.append(f"  Files modified:  {self.stats['files_modified']}")
        report.append(f"  Duplicates merged: {self.stats['duplicates_merged']}")
        report.append(f"  Duplicates flagged (conflicting units): {self.stats['duplicates_flagged']}")
        report.append(f"  pH buffers added: {self.stats['ph_buffers_added']}")
        report.append(f"  Errors: {len(self.stats['errors'])}")
        report.append("")

        # Detailed changes
        if self.changes_log:
            report.append("DETAILED CHANGES:")
            report.append("-" * 80)
            for entry in self.changes_log:
                report.append(f"\n{entry['file']}:")
                for change in entry['changes']:
                    report.append(f"  • {change}")
            report.append("")

        # Errors
        if self.stats['errors']:
            report.append("ERRORS/WARNINGS:")
            report.append("-" * 80)
            for error in self.stats['errors']:
                report.append(f"  ⚠ {error}")
            report.append("")

        report.append("=" * 80)
        return "\n".join(report)


def main():
    """Main execution."""
    print("=" * 80)
    print("MEDIA DATA QUALITY CLEANUP")
    print("=" * 80)
    print()

    # Initialize fixer
    fixer = MediaQualityFixer()

    # Process all media YAML files
    base_dir = Path('data/normalized_yaml')
    if not base_dir.exists():
        print(f"❌ Directory not found: {base_dir}")
        return

    fixer.process_directory(base_dir)

    # Generate and save report
    report = fixer.generate_report()
    print("\n" + report)

    # Save report to file
    report_path = Path('data/quality_cleanup_report.txt')
    with open(report_path, 'w') as f:
        f.write(report)

    print(f"\n✓ Report saved to: {report_path}")


if __name__ == '__main__':
    main()
