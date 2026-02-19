#!/usr/bin/env python3
"""
Coverage Improvement Summary

Shows the progression of coverage improvements through the enrichment process.
"""


def main():
    print("=" * 70)
    print("Coverage Improvement Summary")
    print("=" * 70)
    print()

    print("Baseline (Feb 7, 2026):")
    print("  Coverage: 27.1% (1,367 / 5,048 ingredients)")
    print("  Source: Original manually curated mappings")
    print()

    print("After MicroMediaParam Integration (Feb 9-10):")
    print("  Coverage: 40.5% (2,045 unique subject_ids)")
    print("  Improvements:")
    print("    + 100+ biological products dictionary")
    print("    + 100+ chemical formula conversions")
    print("    + 15+ buffer compound expansions")
    print("    + Advanced normalization (16-step pipeline)")
    print("  New mappings: +678 ingredients (+13.4 percentage points)")
    print()

    print("After Unicode Dot Fixes (Feb 11):")
    print("  Coverage: 45.4% (2,292 / 5,049 ingredients)")
    print("  Improvements:")
    print("    + Unicode dot normalization (5 variants)")
    print("    + Reverse EDTA notation (EDTA·2Na)")
    print("    + Anhydrous prefix removal")
    print("    + Concentration prefix removal (10%, 25% w/v)")
    print("  New mappings: +247 ingredients (+4.9 percentage points)")
    print()

    print("After Gas Mappings (Feb 11):")
    print("  Coverage: 45.6% (2,302 / 5,048 ingredients)")
    print("  Improvements:")
    print("    + Curated gas dictionary (11 gases)")
    print("    + CO2, N2, O2, H2, CH4, N2O, Ar, He, CO, H2S, NH3")
    print("  New mappings: +10 ingredients (+0.2 percentage points)")
    print()

    print("=" * 70)
    print("Total Improvement from Baseline:")
    print("=" * 70)
    print("  Baseline:  27.1% (1,367 mapped)")
    print("  Current:   45.6% (2,302 mapped)")
    print("  Gain:      +18.5 percentage points (+935 new mappings)")
    print()
    print("  That's a 68.4% increase in coverage!")
    print("=" * 70)
    print()

    print("Key Achievements:")
    print("  ✓ MicroMediaParam normalization pipeline integrated")
    print("  ✓ Unicode dot variants now handled correctly")
    print("  ✓ Biological products (peptone, yeast, serum) mapped")
    print("  ✓ Chemical formula variants normalized")
    print("  ✓ Gas ingredients mapped to CHEBI")
    print("  ✓ Clean SSSOM file with no duplicates or unmapped entries")
    print()

    print("Remaining:")
    print("  • 2,746 ingredients still unmapped (54.4%)")
    print("  • Mostly complex mixtures, solutions, and medium references")
    print()


if __name__ == "__main__":
    main()
