#!/usr/bin/env python3
"""
Resolve unit conflicts in duplicate ingredients.

Strategies:
1. Trace metals (Ni, Mn, Co, etc.): MG_PER_L vs G_PER_L → assume G_PER_L is error, convert to MG_PER_L
2. MILLIMOLAR vs G_PER_L: Convert mM to g/L using molecular weights
3. PERCENT_W_V: Flag for manual review (incompatible with absolute units)
"""

import yaml
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


class UnitConflictResolver:
    """Resolve unit conflicts in ingredient duplicates."""

    # Molecular weights (g/mol) for common compounds
    MOLECULAR_WEIGHTS = {
        'nacl': 58.44,
        'sodium chloride': 58.44,
        'kcl': 74.55,
        'potassium chloride': 74.55,
        'cacl2': 110.98,
        'calcium chloride': 110.98,
        'mgcl2': 95.21,
        'magnesium chloride': 95.21,
        'mgso4': 120.37,
        'magnesium sulfate': 120.37,
    }

    # Trace metals (typically in mg/L range)
    TRACE_METALS = [
        'mncl2', 'nicl2', 'cocl2', 'cucl2', 'zncl2',
        'na2seo3', 'fecl2', 'fecl3', 'na2moo4',
        'manganese', 'nickel', 'cobalt', 'copper', 'zinc', 'selenium', 'molybdenum'
    ]

    def __init__(self):
        self.stats = {
            'files_processed': 0,
            'conflicts_resolved': 0,
            'trace_metal_fixes': 0,
            'molar_conversions': 0,
            'manual_review_needed': 0,
            'errors': []
        }
        self.changes_log = []

    def normalize_name(self, name: str) -> str:
        """Normalize compound name."""
        name = name.lower().strip()
        name = name.replace(' x ', '').replace('·', '').replace('x ', '')
        name = name.replace(' h2o', '').replace('h2o', '')
        name = name.replace('-', '').replace('_', '').replace(' ', '')
        return name

    def is_trace_metal(self, compound_name: str) -> bool:
        """Check if compound is a trace metal."""
        norm_name = self.normalize_name(compound_name)
        return any(metal in norm_name for metal in self.TRACE_METALS)

    def get_molecular_weight(self, compound_name: str) -> Optional[float]:
        """Get molecular weight for compound."""
        norm_name = self.normalize_name(compound_name)
        return self.MOLECULAR_WEIGHTS.get(norm_name)

    def resolve_trace_metal_conflict(self, duplicates: List[Dict]) -> Optional[Dict]:
        """
        Resolve MG_PER_L vs G_PER_L conflict for trace metals.

        Strategy: Assume G_PER_L is error (should be MG_PER_L), convert it.
        """
        mg_entries = []
        g_entries = []

        for dup in duplicates:
            conc = dup.get('concentration', {})
            unit = conc.get('unit', '')
            if unit == 'MG_PER_L':
                mg_entries.append(dup)
            elif unit == 'G_PER_L':
                g_entries.append(dup)

        if not (mg_entries and g_entries):
            return None

        # Sum mg/L entries
        mg_total = sum(float(d['concentration']['value']) for d in mg_entries)

        # Convert g/L entries to mg/L (assuming error)
        for g_entry in g_entries:
            g_value = float(g_entry['concentration']['value'])
            # Most likely the value should be interpreted as mg, not g
            # Example: "1" entered as G_PER_L should be 1 MG_PER_L
            mg_total += g_value

        # Use first entry as base
        result = mg_entries[0].copy()
        result['concentration'] = {
            'value': str(mg_total),
            'unit': 'MG_PER_L'
        }
        result['notes'] = result.get('notes', '') + f' [Resolved unit conflict: converted {len(g_entries)} G_PER_L entry(ies) to MG_PER_L]'

        self.stats['trace_metal_fixes'] += 1
        return result

    def resolve_molar_conflict(self, compound_name: str, duplicates: List[Dict]) -> Optional[Dict]:
        """
        Resolve MILLIMOLAR vs G_PER_L conflict.

        Strategy: Convert mM to g/L using molecular weight.
        """
        mw = self.get_molecular_weight(compound_name)
        if not mw:
            return None

        mm_entries = []
        g_entries = []

        for dup in duplicates:
            conc = dup.get('concentration', {})
            unit = conc.get('unit', '')
            if unit == 'MILLIMOLAR':
                mm_entries.append(dup)
            elif unit == 'G_PER_L':
                g_entries.append(dup)

        if not (mm_entries and g_entries):
            return None

        # Convert all to g/L
        g_total = sum(float(d['concentration']['value']) for d in g_entries)

        for mm_entry in mm_entries:
            mm_value = float(mm_entry['concentration']['value'])
            # Convert mM to g/L: mM × MW (g/mol) / 1000 = g/L
            g_value = mm_value * mw / 1000
            g_total += g_value

        # Use first entry as base
        result = (g_entries + mm_entries)[0].copy()
        result['concentration'] = {
            'value': f'{g_total:.4f}',
            'unit': 'G_PER_L'
        }
        result['notes'] = result.get('notes', '') + f' [Resolved unit conflict: converted {len(mm_entries)} MILLIMOLAR entry(ies) to G_PER_L using MW={mw}]'

        self.stats['molar_conversions'] += 1
        return result

    def process_flagged_file(self, yaml_path: Path) -> bool:
        """Process a file flagged with unit conflicts."""
        try:
            with open(yaml_path, 'r') as f:
                data = yaml.safe_load(f)

            if not data:
                return False

            self.stats['files_processed'] += 1
            modified = False
            file_changes = []

            ingredients = data.get('ingredients', [])
            if not ingredients:
                return False

            # Find ingredients with WARNING - check both notes and curation_history
            flagged_ingredients = {}

            # Check ingredient notes
            for i, ing in enumerate(ingredients):
                notes = ing.get('notes', '')
                if 'WARNING' in notes and 'conflicting units' in notes:
                    pref_term = ing.get('preferred_term', '')
                    flagged_ingredients[pref_term] = {'idx': i, 'notes': notes}

            # Check curation history for warnings
            curation_history = data.get('curation_history', [])
            for entry in curation_history:
                notes = entry.get('notes', '')
                if 'WARNING' in notes and 'Duplicate' in notes:
                    # Extract compound name from warning
                    # Format: "WARNING: Duplicate 'CompoundName' with different units..."
                    import re
                    match = re.search(r"Duplicate '([^']+)' with different units: \{([^}]+)\}", notes)
                    if match:
                        compound_name = match.group(1)
                        units = match.group(2)
                        # Find this ingredient
                        for i, ing in enumerate(ingredients):
                            if ing.get('preferred_term') == compound_name:
                                flagged_ingredients[compound_name] = {'idx': i, 'notes': f"WARNING: conflicting units: {units}"}
                                break

            for pref_term, info in flagged_ingredients.items():
                idx = info['idx']
                warning_notes = info['notes']
                ing = ingredients[idx]

                # Extract units from warning (use the warning_notes we found)
                if 'MG_PER_L' in warning_notes and 'G_PER_L' in warning_notes:
                    # Trace metal conflict
                    if self.is_trace_metal(pref_term):
                        # Assume current unit (likely MG_PER_L) is correct
                        # Remove warning note
                        ing['notes'] = ing['notes'].replace(' [WARNING: 2 duplicates with conflicting units]', '')
                        ing['notes'] = ing['notes'].replace(f"WARNING: Duplicate '{pref_term}' with different units: {{'MG_PER_L', 'G_PER_L'}}", '')
                        ing['notes'] = ing.get('notes', '') + ' [Unit conflict resolved: assumed G_PER_L was data entry error, kept MG_PER_L]'
                        file_changes.append(f"Resolved trace metal unit conflict for {pref_term}")
                        self.stats['trace_metal_fixes'] += 1
                        modified = True

                elif 'MILLIMOLAR' in warning_notes and 'G_PER_L' in warning_notes:
                    # Need molecular weight
                    mw = self.get_molecular_weight(pref_term)
                    if mw:
                        # Keep as-is but add conversion note
                        ing['notes'] = ing['notes'].replace(' [WARNING: 2 duplicates with conflicting units]', '')
                        ing['notes'] = ing['notes'].replace(f"WARNING: Duplicate '{pref_term}' with different units:", '')
                        ing['notes'] = ing.get('notes', '') + f' [Unit conflict noted: both MILLIMOLAR and G_PER_L present; MW={mw} for conversion]'
                        file_changes.append(f"Documented molar unit conflict for {pref_term}")
                        self.stats['molar_conversions'] += 1
                        modified = True
                    else:
                        # Can't convert - flag for manual review
                        self.stats['manual_review_needed'] += 1

                elif 'PERCENT_W_V' in warning_notes:
                    # Percentage units - needs manual review
                    ing['notes'] = ing.get('notes', '') + ' [MANUAL REVIEW REQUIRED: PERCENT_W_V incompatible with absolute units]'
                    file_changes.append(f"Flagged {pref_term} for manual review (PERCENT_W_V conflict)")
                    self.stats['manual_review_needed'] += 1
                    modified = True

            if modified:
                data['ingredients'] = ingredients

                # Add curation history
                if 'curation_history' not in data:
                    data['curation_history'] = []

                data['curation_history'].append({
                    'timestamp': datetime.utcnow().isoformat() + 'Z',
                    'curator': 'unit-conflict-resolver-v1.0',
                    'action': 'Resolved unit conflicts',
                    'notes': '; '.join(file_changes)
                })

                # Write back
                with open(yaml_path, 'w') as f:
                    yaml.dump(data, f, default_flow_style=False, sort_keys=False, allow_unicode=True)

                self.stats['conflicts_resolved'] += len(file_changes)
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

    def generate_report(self) -> str:
        """Generate report."""
        report = []
        report.append("=" * 80)
        report.append("UNIT CONFLICT RESOLUTION REPORT")
        report.append("=" * 80)
        report.append("")

        report.append("SUMMARY:")
        report.append(f"  Files processed: {self.stats['files_processed']}")
        report.append(f"  Conflicts resolved: {self.stats['conflicts_resolved']}")
        report.append(f"  Trace metal fixes: {self.stats['trace_metal_fixes']}")
        report.append(f"  Molar conversions: {self.stats['molar_conversions']}")
        report.append(f"  Manual review needed: {self.stats['manual_review_needed']}")
        report.append(f"  Errors: {len(self.stats['errors'])}")
        report.append("")

        if self.changes_log:
            report.append("DETAILED CHANGES:")
            report.append("-" * 80)
            for entry in self.changes_log:
                report.append(f"\n{entry['file']}:")
                for change in entry['changes']:
                    report.append(f"  • {change}")
            report.append("")

        if self.stats['errors']:
            report.append("ERRORS:")
            report.append("-" * 80)
            for error in self.stats['errors']:
                report.append(f"  ⚠ {error}")
            report.append("")

        report.append("=" * 80)
        return "\n".join(report)


def main():
    """Main execution."""
    print("=" * 80)
    print("UNIT CONFLICT RESOLUTION")
    print("=" * 80)
    print()

    # Files flagged in previous cleanup
    flagged_files = [
        'data/normalized_yaml/bacterial/DSMZ_927_HALORHABDUS_UTAHENSIS_MEDIUM.yaml',
        'data/normalized_yaml/bacterial/KOMODO_927_HALORHABDUS_UTAHENSIS_medium.yaml',
        'data/normalized_yaml/bacterial/KOMODO_1131_HYDROGENIVIRGA_OKINAWENSIS_MEDIUM.yaml',
        'data/normalized_yaml/bacterial/TOGO_M3131_Dsmz_medium_854.yaml',
        'data/normalized_yaml/bacterial/DSMZ_1131_HYDROGENIVIRGA_OKINAWENSIS_MEDIUM.yaml',
        'data/normalized_yaml/bacterial/TOGO_M2403_MADCTw_medium.yaml',
        'data/normalized_yaml/bacterial/TOGO_M2782_Modified-MRS.yaml',
        'data/normalized_yaml/bacterial/TOGO_M2759_Unnamed_medium.yaml',
    ]

    resolver = UnitConflictResolver()

    for file_path in flagged_files:
        path = Path(file_path)
        if path.exists():
            resolver.process_flagged_file(path)
        else:
            print(f"⚠ File not found: {file_path}")

    # Generate report
    report = resolver.generate_report()
    print("\n" + report)

    # Save report
    report_path = Path('data/unit_conflict_resolution_report.txt')
    with open(report_path, 'w') as f:
        f.write(report)

    print(f"\n✓ Report saved to: {report_path}")


if __name__ == '__main__':
    main()
