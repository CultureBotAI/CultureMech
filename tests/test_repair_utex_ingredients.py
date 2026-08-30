"""The UTEX ingredient repair must not invent a unit it was not given.

The defect being repaired invented one: `fix_schema_inconsistencies.py` wrote
`{value: variable, unit: G_PER_L}` onto every ingredient that had no amount,
asserting grams per litre for "4 drops" of vitamin cocktail. The repair is only
an improvement if it refuses to do the same thing.

Every literal in this file is copied from a real UTEX page or from the capture
in `data/raw/utex/utex_media.json`.
"""

from __future__ import annotations

from repair_utex_ingredients import (
    build_ingredient,
    parse_concentration,
    split_supplier,
    strip_vendor,
)

# --- names ---------------------------------------------------------------


def test_a_vendor_parenthetical_is_split_off_the_name():
    assert strip_vendor("NaNO3(Fisher BP360-500)") == ("NaNO3", "Fisher BP360-500", None)
    assert strip_vendor("K2HPO4(Sigma P 3786)") == ("K2HPO4", "Sigma P 3786", None)


def test_a_cas_parenthetical_is_not_mistaken_for_a_supplier():
    """UTEX switched from catalogue numbers to CAS after the January capture."""
    assert strip_vendor("MgSO4•7H2O(CAS: 10034-99-8)") == ("MgSO4•7H2O", None, "10034-99-8")


def test_a_chemical_parenthetical_is_kept():
    """`PABA(p-aminobenzoic acid)` is chemistry, not sourcing."""
    assert strip_vendor("PABA(p-aminobenzoic acid)")[0] == "PABA(p-aminobenzoic acid)"
    assert strip_vendor("CaCO3(optional)")[0] == "CaCO3(optional)"


def test_a_chemical_parenthetical_survives_a_trailing_vendor_one():
    base, supplier, _ = strip_vendor("PABA(p-aminobenzoic acid)(Sigma A 1174)")
    assert base == "PABA(p-aminobenzoic acid)"
    assert supplier == "Sigma A 1174"


def test_a_plain_name_is_left_alone():
    assert strip_vendor("Ferric Ammonium Citrate") == ("Ferric Ammonium Citrate", None, None)


def test_the_supplier_splits_into_vendor_and_catalog_number():
    assert split_supplier("Sigma P 3786") == {
        "supplier_name": "Sigma",
        "catalog_number": "P 3786",
    }
    assert split_supplier("Fisher BP360-500") == {
        "supplier_name": "Fisher",
        "catalog_number": "BP360-500",
    }


# --- concentrations ------------------------------------------------------


def test_a_per_litre_amount_maps_straight_across():
    assert parse_concentration("10 mL/L") == {"value": "10", "unit": "ML_PER_L"}
    assert parse_concentration("1 g/L") == {"value": "1", "unit": "G_PER_L"}


def test_a_molarity_is_read_as_a_molarity():
    assert parse_concentration("0.5 mM") == {"value": "0.5", "unit": "MILLIMOLAR"}
    assert parse_concentration("17.6 mM") == {"value": "17.6", "unit": "MILLIMOLAR"}
    assert parse_concentration("0.31 M") == {"value": "0.31", "unit": "MOLAR"}


def test_another_volume_basis_is_converted_onto_the_per_litre_convention():
    """`10 mL/3 L` and `0.01 g/500 mL` are real cells from the capture."""
    assert parse_concentration("10 mL/3 L")["unit"] == "ML_PER_L"
    assert parse_concentration("0.01 g/500 mL") == {"value": "0.02", "unit": "G_PER_L"}
    assert parse_concentration("1 mL/0.25 L") == {"value": "4", "unit": "ML_PER_L"}


def test_the_conversion_is_exact_rather_than_floating_point():
    """`0.1/1` in binary floating point is 0.1000000000000000055511151231257827."""
    assert parse_concentration("0.1 g/L")["value"] == "0.1"
    assert parse_concentration("0.0008 g/100 mL")["value"] == "0.008"


def test_an_amount_with_no_volume_basis_yields_no_concentration():
    """The whole point. These are the cells that got a fabricated G_PER_L."""
    for cell in ("4 drops", "1 cc", "1 tsp", "90 mL", "1 per 200 mL", "40 mL of supernatant"):
        assert parse_concentration(cell) is None, cell


def test_an_empty_cell_yields_no_concentration():
    assert parse_concentration("") is None
    assert parse_concentration(None) is None


# --- the assembled ingredient -------------------------------------------


def test_an_unconvertible_amount_becomes_variable_not_a_guessed_unit():
    repaired = build_ingredient(
        {
            "preferred_term": "4",
            "concentration": {"value": "variable", "unit": "G_PER_L"},
            "notes": "Original amount: DAS Vitamin Cocktail",
        },
        {"ingredient": "DAS Vitamin Cocktail", "amount": "4 drops"},
    )
    assert repaired["preferred_term"] == "DAS Vitamin Cocktail"
    assert repaired["concentration"] == {"value": "variable", "unit": "VARIABLE"}
    assert repaired["notes"] == "UTEX lists: amount 4 drops"


def test_the_pages_own_final_concentration_beats_a_converted_amount():
    repaired = build_ingredient(
        {"preferred_term": "1", "notes": "Original amount: NaNO3(Fisher BP360-500)"},
        {
            "ingredient": "NaNO3(CAS: 7631-99-4)",
            "amount": "10 mL/L",
            "stock_concentration": "30 g/200 mL dH2O",
            "final_concentration": "17.6 mM",
        },
    )
    assert repaired["concentration"] == {"value": "17.6", "unit": "MILLIMOLAR"}


def test_every_source_cell_is_preserved_verbatim_in_the_note():
    """A converted value has to stay checkable against what UTEX printed."""
    repaired = build_ingredient(
        {"preferred_term": "1", "notes": "Original amount: NaNO3(Fisher BP360-500)"},
        {
            "ingredient": "NaNO3(CAS: 7631-99-4)",
            "amount": "10 mL/L",
            "stock_concentration": "30 g/200 mL dH2O",
            "final_concentration": "17.6 mM",
        },
    )
    assert repaired["notes"] == (
        "UTEX lists: amount 10 mL/L; stock 30 g/200 mL dH2O; final 17.6 mM; CAS 7631-99-4"
    )


def test_the_fabricated_original_amount_note_does_not_survive():
    repaired = build_ingredient(
        {"preferred_term": "2", "notes": "Original amount: Pea"},
        {"ingredient": "Pea", "amount": "1 per 200 mL"},
    )
    assert "Original amount" not in repaired["notes"]


def test_a_curated_note_is_kept_rather_than_overwritten():
    repaired = build_ingredient(
        {"preferred_term": "1", "notes": "Add after autoclaving."},
        {"ingredient": "Vitamin B12", "amount": "1 mL/L"},
    )
    assert repaired["notes"].startswith("Add after autoclaving.")
    assert "UTEX lists: amount 1 mL/L" in repaired["notes"]


def test_the_supplier_lands_in_the_field_meant_for_it():
    repaired = build_ingredient(
        {"preferred_term": "2", "notes": "Original amount: K2HPO4(Sigma P 3786)"},
        {"ingredient": "K2HPO4(Sigma P 3786)", "amount": "10 mL/L"},
    )
    assert repaired["supplier_catalog"] == {
        "supplier_name": "Sigma",
        "catalog_number": "P 3786",
    }


def test_fields_the_repair_does_not_own_are_left_untouched():
    repaired = build_ingredient(
        {
            "preferred_term": "1",
            "notes": "Original amount: Glucose",
            "term": {"id": "CHEBI:17234", "label": "glucose"},
            "nutritional_roles": ["CARBON_SOURCE"],
        },
        {"ingredient": "Glucose", "amount": "10 g/L"},
    )
    assert repaired["term"] == {"id": "CHEBI:17234", "label": "glucose"}
    assert repaired["nutritional_roles"] == ["CARBON_SOURCE"]
