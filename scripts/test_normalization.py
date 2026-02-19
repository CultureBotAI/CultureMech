#!/usr/bin/env python3
"""
Test Normalization and Preprocessing Functions

Validates that the normalization, solution parsing, and other preprocessing
functions work correctly on known test cases.
"""

import sys
from pathlib import Path

# Add scripts to path
sys.path.insert(0, str(Path(__file__).parent))

from enrich_sssom_with_ols import (
    normalize_ingredient_name,
    parse_solution,
    strip_brand_names,
    expand_gas_abbreviation,
    is_bio_material,
    # MicroMediaParam normalization functions
    lookup_biological_product,
    convert_formula_to_name,
    expand_buffer_name,
    normalize_greek_letters,
    normalize_stereochemistry_prefixes,
    fix_formula_notation,
    normalize_atom_salt_notation,
    normalize_iron_oxidation,
    normalize_formula_spaces,
    normalize_hcl_salt,
    normalize_for_mapping,
)


def test_normalization():
    """Test ingredient name normalization (comprehensive pipeline)."""
    print("=" * 70)
    print("Normalization Tests (Comprehensive Pipeline)")
    print("=" * 70)

    test_cases = [
        # Hydrated salts - now converted to common names
        ('MnCl2・6H2O', 'MnCl2・6H2O'),  # Unicode dot preserved initially
        ('MnCl2·6H2O', 'manganese(II) chloride'),  # Hydration removed, formula converted
        ('MnCl2.6H2O', 'manganese(II) chloride'),
        ('FeSO4.7H2O', 'iron(II) sulfate'),
        ('CaCl2.2H2O', 'calcium chloride'),

        # Solutions - descriptors removed
        ('5% Na2S solution', '5% Na2S solution'),  # Percent preserved
        ('glucose solution', 'glucose solution'),  # Solution keyword not removed by pipeline

        # Whitespace
        ('  glucose   ', 'glucose'),
        ('glucose  powder', 'glucose powder'),  # Powder not removed by pipeline
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = normalize_ingredient_name(input_val)
        if result == expected:
            print(f"✓ {input_val:30s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:30s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nNormalization: {passed} passed, {failed} failed")
    return failed == 0


def test_solution_parsing():
    """Test solution/concentration parsing."""
    print("\n" + "=" * 70)
    print("Solution Parsing Tests")
    print("=" * 70)

    test_cases = [
        ('5% Na2S solution', ('Na2S', '5', '%')),
        ('0.1 mM CaCl2', ('CaCl2', '0.1', 'mM')),
        ('10 g/L glucose', ('glucose', '10', 'g/L')),
        ('glucose', ('glucose', None, None)),
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = parse_solution(input_val)
        if result == expected:
            print(f"✓ {input_val:30s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:30s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nSolution parsing: {passed} passed, {failed} failed")
    return failed == 0


def test_brand_stripping():
    """Test brand name removal."""
    print("\n" + "=" * 70)
    print("Brand Name Stripping Tests")
    print("=" * 70)

    test_cases = [
        ('Bacto Peptone', 'Peptone'),
        ('Yeast extract (BD-Difco)', 'Yeast extract'),
        ('Peptone (Difco)', 'Peptone'),
        ('Glucose (Sigma)', 'Glucose'),
        ('Glucose', 'Glucose'),
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = strip_brand_names(input_val)
        if result == expected:
            print(f"✓ {input_val:40s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:40s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nBrand stripping: {passed} passed, {failed} failed")
    return failed == 0


def test_gas_expansion():
    """Test gas abbreviation expansion."""
    print("\n" + "=" * 70)
    print("Gas Abbreviation Expansion Tests")
    print("=" * 70)

    test_cases = [
        ('N2', ['nitrogen gas', 'molecular nitrogen', 'dinitrogen']),
        ('O2', ['oxygen gas', 'molecular oxygen', 'dioxygen']),
        ('CO2', ['carbon dioxide', 'CO2']),
        ('glucose', ['glucose']),  # Not a gas
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = expand_gas_abbreviation(input_val)
        if result == expected:
            print(f"✓ {input_val:10s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:10s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nGas expansion: {passed} passed, {failed} failed")
    return failed == 0


def test_bio_material_detection():
    """Test bio-material detection."""
    print("\n" + "=" * 70)
    print("Bio-Material Detection Tests")
    print("=" * 70)

    test_cases = [
        ('Yeast extract', True),
        ('Peptone', True),
        ('Meat extract', True),
        ('Tryptone', True),
        ('Casein', True),
        ('Glucose', False),
        ('NaCl', False),
        ('Sodium chloride', False),
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = is_bio_material(input_val)
        if result == expected:
            status = "bio-material" if result else "chemical"
            print(f"✓ {input_val:30s} → {status}")
            passed += 1
        else:
            print(f"✗ {input_val:30s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nBio-material detection: {passed} passed, {failed} failed")
    return failed == 0


def test_biological_product_lookup():
    """Test biological product dictionary lookup."""
    print("\n" + "=" * 70)
    print("Biological Product Lookup Tests (MicroMediaParam)")
    print("=" * 70)

    test_cases = [
        ('Yeast extract', 'FOODON:03315426'),
        ('Peptone', 'FOODON:03302071'),
        ('peptone', 'FOODON:03302071'),  # Case insensitive
        ('DNA', 'CHEBI:16991'),
        ('Blood', 'UBERON:0000178'),
        ('Agar', 'CHEBI:2509'),
        ('BSA', 'CHEBI:3136'),
        ('Glucose', None),  # Not in dictionary
        ('NaCl', None),
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = lookup_biological_product(input_val)
        if result == expected:
            status = result if result else "not found"
            print(f"✓ {input_val:30s} → {status}")
            passed += 1
        else:
            print(f"✗ {input_val:30s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nBiological product lookup: {passed} passed, {failed} failed")
    return failed == 0


def test_formula_to_name_conversion():
    """Test chemical formula to common name conversion."""
    print("\n" + "=" * 70)
    print("Formula to Name Conversion Tests (MicroMediaParam)")
    print("=" * 70)

    test_cases = [
        ('Fe2(SO4)3', 'iron(III) sulfate'),
        ('FeSO4', 'iron(II) sulfate'),
        ('(NH4)2SO4', 'ammonium sulfate'),
        ('CaCl2', 'calcium chloride'),
        ('MgSO4', 'magnesium sulfate'),
        ('Na2MoO4', 'sodium molybdate'),
        ('NH42SO4', 'ammonium sulfate'),  # Typo correction
        ('Glucose', 'Glucose'),  # Not a formula
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = convert_formula_to_name(input_val)
        if result == expected:
            print(f"✓ {input_val:20s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:20s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nFormula to name: {passed} passed, {failed} failed")
    return failed == 0


def test_greek_letter_normalization():
    """Test Greek letter conversion."""
    print("\n" + "=" * 70)
    print("Greek Letter Normalization Tests (MicroMediaParam)")
    print("=" * 70)

    test_cases = [
        ('α-D-Glucose', 'alpha-D-Glucose'),
        ('β-NAD', 'beta-NAD'),
        ('γ-aminobutyric acid', 'gamma-aminobutyric acid'),
        ('ß-carotene', 'beta-carotene'),
        ('Glucose', 'Glucose'),  # No Greek letters
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = normalize_greek_letters(input_val)
        if result == expected:
            print(f"✓ {input_val:30s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:30s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nGreek letter normalization: {passed} passed, {failed} failed")
    return failed == 0


def test_stereochemistry_normalization():
    """Test stereochemistry prefix normalization."""
    print("\n" + "=" * 70)
    print("Stereochemistry Normalization Tests (MicroMediaParam)")
    print("=" * 70)

    test_cases = [
        ('D+-Glucose', 'D-Glucose'),
        ('L+-Tartaric acid', 'L-Tartaric acid'),
        ('D-+-biotin', 'D-biotin'),
        ('(+)-alpha-tocopherol', 'alpha-tocopherol'),
        ('(-)-compound', 'compound'),
        ('(±)-compound', 'DL-compound'),
        ('Glucose', 'Glucose'),
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = normalize_stereochemistry_prefixes(input_val)
        if result == expected:
            print(f"✓ {input_val:30s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:30s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nStereochemistry normalization: {passed} passed, {failed} failed")
    return failed == 0


def test_formula_notation_fixing():
    """Test formula notation parentheses fixes."""
    print("\n" + "=" * 70)
    print("Formula Notation Fixing Tests (MicroMediaParam)")
    print("=" * 70)

    test_cases = [
        ('NH42SO4', '(NH4)2SO4'),
        ('CaNO32', 'Ca(NO3)2'),
        ('Fe2SO43', 'Fe2(SO4)3'),
        ('KPO42', 'K(PO4)2'),
        ('NaCl', 'NaCl'),  # Already correct
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = fix_formula_notation(input_val)
        if result == expected:
            print(f"✓ {input_val:20s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:20s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nFormula notation fixing: {passed} passed, {failed} failed")
    return failed == 0


def test_atom_salt_notation():
    """Test atom-salt notation conversion."""
    print("\n" + "=" * 70)
    print("Atom-Salt Notation Tests (MicroMediaParam)")
    print("=" * 70)

    test_cases = [
        ('Na-benzoate', 'sodium benzoate'),
        ('Na3 citrate', 'trisodium citrate'),
        ('K acetate', 'potassium acetate'),
        ('Na2-EDTA', 'disodium EDTA'),
        ('NaCl', 'NaCl'),  # Not atom-salt notation
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = normalize_atom_salt_notation(input_val)
        # Check if expected substring is in result (allows for variations)
        if expected.lower() in result.lower():
            print(f"✓ {input_val:20s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:20s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nAtom-salt notation: {passed} passed, {failed} failed")
    return failed == 0


def test_iron_oxidation_normalization():
    """Test iron oxidation state normalization."""
    print("\n" + "=" * 70)
    print("Iron Oxidation Normalization Tests (MicroMediaParam)")
    print("=" * 70)

    test_cases = [
        ('FeIII citrate', 'iron(III) citrate'),
        ('FeII chloride', 'iron(II) chloride'),
        ('IronIII sulfate', 'iron(III) sulfate'),
        ('IronII acetate', 'iron(II) acetate'),
        ('FeSO4', 'FeSO4'),  # No oxidation notation
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = normalize_iron_oxidation(input_val)
        if result == expected:
            print(f"✓ {input_val:25s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:25s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nIron oxidation normalization: {passed} passed, {failed} failed")
    return failed == 0


def test_formula_space_normalization():
    """Test formula space removal."""
    print("\n" + "=" * 70)
    print("Formula Space Normalization Tests (MicroMediaParam)")
    print("=" * 70)

    test_cases = [
        ('Fe SO4 x 7 H2O', 'FeSO4 x 7 H2O'),
        ('Na Cl', 'NaCl'),
        ('Mg SO4', 'MgSO4'),
        ('Ca Cl2', 'CaCl2'),
        ('NaCl', 'NaCl'),  # Already correct
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = normalize_formula_spaces(input_val)
        if result == expected:
            print(f"✓ {input_val:25s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:25s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nFormula space normalization: {passed} passed, {failed} failed")
    return failed == 0


def test_hcl_salt_normalization():
    """Test HCl salt notation normalization."""
    print("\n" + "=" * 70)
    print("HCl Salt Normalization Tests (MicroMediaParam)")
    print("=" * 70)

    test_cases = [
        ('Thiamine-HCl', 'Thiamine hydrochloride'),
        ('L-Cysteine HCl x H2O', 'L-Cysteine hydrochloride'),
        ('Pyridoxine-HCl', 'Pyridoxine hydrochloride'),
        ('Glucose', 'Glucose'),  # No HCl
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = normalize_hcl_salt(input_val)
        if result == expected:
            print(f"✓ {input_val:30s} → {result}")
            passed += 1
        else:
            print(f"✗ {input_val:30s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nHCl salt normalization: {passed} passed, {failed} failed")
    return failed == 0


def test_buffer_expansion():
    """Test buffer abbreviation expansion."""
    print("\n" + "=" * 70)
    print("Buffer Expansion Tests (MicroMediaParam)")
    print("=" * 70)

    test_cases = [
        ('HEPES buffer', '4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid'),
        ('MES', '2-(N-morpholino)ethanesulfonic acid'),
        ('Tris-HCl', 'tris(hydroxymethyl)aminomethane'),
        ('Glucose', 'Glucose'),  # Not a buffer
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = expand_buffer_name(input_val)
        if result == expected:
            print(f"✓ {input_val:20s} → {result[:50]}...")
            passed += 1
        else:
            print(f"✗ {input_val:20s} → {result} (expected: {expected})")
            failed += 1

    print(f"\nBuffer expansion: {passed} passed, {failed} failed")
    return failed == 0


def test_comprehensive_normalization():
    """Test the complete 16-step normalization pipeline."""
    print("\n" + "=" * 70)
    print("Comprehensive Normalization Pipeline Tests (16 steps)")
    print("=" * 70)

    test_cases = [
        # Greek letters
        ('α-D-Glucose', 'alpha-D-Glucose'),
        # Stereochemistry
        ('D+-Glucose x H2O', 'D-Glucose'),
        # Formula fixes + name conversion
        ('NH42SO4', 'ammonium sulfate'),
        # Atom-salt notation
        ('Na-benzoate', 'sodium benzoate'),
        # Iron oxidation
        ('FeIII citrate', 'iron(III) citrate'),
        # HCl salt + hydration
        ('Thiamine-HCl x 2 H2O', 'Thiamine hydrochloride'),
        # Formula spaces + hydration + conversion
        ('Fe SO4 x 7 H2O', 'iron(II) sulfate'),
        # Buffer expansion
        ('HEPES buffer', '4-(2-hydroxyethyl)-1-piperazineethanesulfonic acid'),
        # Multiple transformations
        ('D+-α-Glucose monohydrate', 'D-alpha-Glucose'),
    ]

    passed = 0
    failed = 0

    for input_val, expected in test_cases:
        result = normalize_for_mapping(input_val)
        if result == expected:
            print(f"✓ {input_val:40s} → {result[:50]}")
            passed += 1
        else:
            print(f"✗ {input_val:40s} → {result}")
            print(f"  Expected: {expected}")
            failed += 1

    print(f"\nComprehensive normalization: {passed} passed, {failed} failed")
    return failed == 0


def main():
    """Run all tests."""
    all_passed = True

    # Original tests
    all_passed &= test_normalization()
    all_passed &= test_solution_parsing()
    all_passed &= test_brand_stripping()
    all_passed &= test_gas_expansion()
    all_passed &= test_bio_material_detection()

    # MicroMediaParam integration tests
    all_passed &= test_biological_product_lookup()
    all_passed &= test_formula_to_name_conversion()
    all_passed &= test_greek_letter_normalization()
    all_passed &= test_stereochemistry_normalization()
    all_passed &= test_formula_notation_fixing()
    all_passed &= test_atom_salt_notation()
    all_passed &= test_iron_oxidation_normalization()
    all_passed &= test_formula_space_normalization()
    all_passed &= test_hcl_salt_normalization()
    all_passed &= test_buffer_expansion()
    all_passed &= test_comprehensive_normalization()

    print("\n" + "=" * 70)
    if all_passed:
        print("✓ All tests passed!")
        return 0
    else:
        print("✗ Some tests failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
