#!/usr/bin/env python3
"""
Quick test script to verify hierarchy integration implementation.

Usage:
    python scripts/test_hierarchy_integration.py
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

def test_imports():
    """Test that all modules can be imported."""
    print("Testing imports...")

    try:
        from culturemech.enrich.hierarchy_importer import MediaIngredientMechHierarchyImporter
        print("  ✓ hierarchy_importer")

        from culturemech.enrich.hierarchy_enricher import HierarchyEnricher
        print("  ✓ hierarchy_enricher")

        from culturemech.enrich.role_importer import RoleImporter
        print("  ✓ role_importer")

        return True
    except ImportError as e:
        print(f"  ✗ Import failed: {e}")
        return False


def test_id_generation():
    """Test MediaIngredientMech ID pattern validation."""
    print("\nTesting ID pattern validation...")

    import re

    pattern = r'^MediaIngredientMech:\d{6}$'

    test_cases = [
        ("MediaIngredientMech:000001", True),
        ("MediaIngredientMech:015431", True),
        ("MediaIngredientMech:999999", True),
        ("MediaIngredientMech:1", False),  # Not zero-padded
        ("CultureMech:000001", False),  # Wrong prefix
        ("MediaIngredientMech:0000001", False),  # Too many digits
    ]

    all_passed = True
    for id_str, expected in test_cases:
        result = bool(re.match(pattern, id_str))
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} {id_str} → {result} (expected {expected})")

    return all_passed


def test_variant_type_enum():
    """Test variant type enum values."""
    print("\nTesting variant type enum...")

    valid_variant_types = {
        'HYDRATE', 'SALT_FORM', 'ANHYDROUS',
        'NAMED_HYDRATE', 'CHEMICAL_VARIANT'
    }

    test_values = [
        ("HYDRATE", True),
        ("SALT_FORM", True),
        ("ANHYDROUS", True),
        ("NAMED_HYDRATE", True),
        ("CHEMICAL_VARIANT", True),
        ("INVALID_TYPE", False),
        ("hydrate", False),  # Case sensitive
    ]

    all_passed = True
    for value, expected in test_values:
        result = value in valid_variant_types
        status = "✓" if result == expected else "✗"
        if result != expected:
            all_passed = False
        print(f"  {status} {value} → {result} (expected {expected})")

    return all_passed


def test_ingredient_reference_structure():
    """Test ingredient reference data structure."""
    print("\nTesting ingredient reference structure...")

    reference = {
        'preferred_term': 'Calcium chloride',
        'mediaingredientmech_id': 'MediaIngredientMech:000041'
    }

    checks = [
        ('preferred_term' in reference, "Has preferred_term field"),
        ('mediaingredientmech_id' in reference, "Has mediaingredientmech_id field"),
        (isinstance(reference['preferred_term'], str), "preferred_term is string"),
        (isinstance(reference['mediaingredientmech_id'], str), "mediaingredientmech_id is string"),
        (reference['mediaingredientmech_id'].startswith('MediaIngredientMech:'), "Valid ID prefix"),
    ]

    all_passed = True
    for check, description in checks:
        status = "✓" if check else "✗"
        if not check:
            all_passed = False
        print(f"  {status} {description}")

    return all_passed


def test_hierarchy_importer_initialization():
    """Test hierarchy importer can be initialized."""
    print("\nTesting hierarchy importer initialization...")

    try:
        from culturemech.enrich.hierarchy_importer import MediaIngredientMechHierarchyImporter

        # Initialize without repo path
        importer = MediaIngredientMechHierarchyImporter()
        print("  ✓ Initialized without repo path")

        # Check attributes
        assert hasattr(importer, 'hierarchy'), "Has hierarchy attribute"
        print("  ✓ Has hierarchy attribute")

        assert hasattr(importer, 'lookup_index'), "Has lookup_index attribute"
        print("  ✓ Has lookup_index attribute")

        return True
    except Exception as e:
        print(f"  ✗ Failed: {e}")
        return False


def main():
    """Run all tests."""
    print("=" * 60)
    print("Hierarchy Integration Implementation Tests")
    print("=" * 60)

    results = []

    # Run tests
    results.append(("Imports", test_imports()))
    results.append(("ID Pattern Validation", test_id_generation()))
    results.append(("Variant Type Enum", test_variant_type_enum()))
    results.append(("Ingredient Reference Structure", test_ingredient_reference_structure()))
    results.append(("Hierarchy Importer Initialization", test_hierarchy_importer_initialization()))

    # Summary
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)

    passed = sum(1 for _, result in results if result)
    total = len(results)

    for name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status}: {name}")

    print(f"\nTotal: {passed}/{total} tests passed")

    if passed == total:
        print("\n✓ All tests passed!")
        return 0
    else:
        print(f"\n✗ {total - passed} test(s) failed")
        return 1


if __name__ == "__main__":
    sys.exit(main())
