"""Tests for the concentration-plausibility audit (#118).

The risk with a magnitude heuristic is both directions: too loose and it misses
the stock-solution values that motivated the issue; too tight and it drowns a
curator in false positives on legitimately concentrated media. These tests pin
the three confirmed real-world cases from #118 as must-detect, and pin ordinary
final-medium concentrations as must-not-detect.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def acp():
    return _load("audit_concentration_plausibility")


def _ing(name, value, unit="G_PER_L", ident=None):
    return {"preferred_term": name, "term": ({"id": ident} if ident else None),
            "concentration": {"value": value, "unit": unit}}


# --- must detect: the confirmed cases from #118 ---------------------------


def test_water_at_preparation_volume(acp):
    """sulfolobus_medium_for_dsm_9790 carries 'Distilled water 2000 G_PER_L'."""
    hit = acp.check_ingredient(_ing("Distilled water", "2000", ident="CHEBI:15377"))
    assert hit and hit[0] == "WATER_AS_VOLUME"


@pytest.mark.parametrize("name,value", [
    ("MnCl2 x 4 H2O", "180"),
    ("Na2B4O7 x 10 H2O", "450"),
    ("ZnSO4 x 7 H2O", "22"),
    ("CuCl2 x 2 H2O", "5"),
    ("Na2MoO4 x 2 H2O", "3"),
])
def test_trace_salts_at_stock_magnitude(acp, name, value):
    hit = acp.check_ingredient(_ing(name, value))
    assert hit and hit[0] == "TRACE_SALT_AS_STOCK", f"{name} {value} not flagged"


def test_resazurin_unit_slip(acp):
    """TOGO_M1796_Desulfovibrio_medium stores Resazurin at 1 G_PER_L (~1000x)."""
    hit = acp.check_ingredient(_ing("Resazurin", "1"))
    assert hit and hit[0] == "INDICATOR_UNIT_SLIP"


# --- must NOT detect: ordinary final-medium values ------------------------


@pytest.mark.parametrize("name,value", [
    ("NaCl", "10"),               # bulk salt, ordinary
    ("Glucose", "20"),            # carbon source
    ("Yeast extract", "5"),
    ("Agar", "15"),
    ("Distilled water", "1"),     # implausible in another way, but not a volume
    ("MgSO4 x 7 H2O", "0.5"),     # not a trace element
])
def test_ordinary_concentrations_are_not_flagged(acp, name, value):
    assert acp.check_ingredient(_ing(name, value)) is None


def test_trace_salt_below_threshold_is_not_flagged(acp):
    """Trace elements at genuine final-medium magnitude must pass."""
    assert acp.check_ingredient(_ing("MnCl2 x 4 H2O", "0.005")) is None


def test_vitamin_at_final_medium_magnitude_is_not_flagged(acp):
    assert acp.check_ingredient(_ing("Biotin", "0.00002")) is None


def test_non_gpl_units_are_out_of_scope(acp):
    """Only G_PER_L is checked; a molar-basis check needs molecular weights."""
    assert acp.check_ingredient(_ing("Resazurin", "1", unit="MG_PER_L")) is None
    assert acp.check_ingredient(_ing("MnCl2", "180", unit="MILLIMOLAR")) is None


def test_unparseable_and_nonpositive_values_are_skipped(acp):
    assert acp.check_ingredient(_ing("Resazurin", "n/a")) is None
    assert acp.check_ingredient(_ing("Resazurin", None)) is None
    assert acp.check_ingredient(_ing("Resazurin", "0")) is None


def test_hydrate_suffix_does_not_defeat_matching(acp):
    """Labels arrive with several hydrate separators."""
    for label in ("MnCl2·4H2O", "MnCl2 x 4 H2O", "MnCl2・4H2O", "MnCl2"):
        hit = acp.check_ingredient(_ing(label, "180"))
        assert hit and hit[0] == "TRACE_SALT_AS_STOCK", label


# --- cocktail roll-up -----------------------------------------------------


def test_flattened_cocktail_requires_no_solutions_block(acp, tmp_path):
    """A record that already nests its stock under `solutions:` is correct."""
    rec = tmp_path / "bacterial"
    rec.mkdir()
    import yaml
    (rec / "x.yaml").write_text(yaml.dump({
        "id": "CultureMech:1", "solutions": [{"preferred_term": "vitamins"}],
        "ingredients": [],
    }))
    rows = [{"finding": "INDICATOR_UNIT_SLIP", "file_path": "bacterial/x.yaml",
             "record_id": "CultureMech:1"} for _ in range(5)]
    [summary] = acp.summarize_records(rows, tmp_path)
    assert summary["has_solutions_block"] == "yes"
    assert summary["flattened_cocktail"] == "no"


def test_flattened_cocktail_detected_without_solutions_block(acp, tmp_path):
    rec = tmp_path / "bacterial"
    rec.mkdir()
    import yaml
    (rec / "y.yaml").write_text(yaml.dump({"id": "CultureMech:2", "ingredients": []}))
    rows = [{"finding": "INDICATOR_UNIT_SLIP", "file_path": "bacterial/y.yaml",
             "record_id": "CultureMech:2"} for _ in range(3)]
    [summary] = acp.summarize_records(rows, tmp_path)
    assert summary["flattened_cocktail"] == "yes"


def test_single_flagged_row_is_not_a_cocktail(acp, tmp_path):
    rec = tmp_path / "bacterial"
    rec.mkdir()
    import yaml
    (rec / "z.yaml").write_text(yaml.dump({"id": "CultureMech:3", "ingredients": []}))
    rows = [{"finding": "INDICATOR_UNIT_SLIP", "file_path": "bacterial/z.yaml",
             "record_id": "CultureMech:3"}]
    [summary] = acp.summarize_records(rows, tmp_path)
    assert summary["flattened_cocktail"] == "no"


# --- corpus ---------------------------------------------------------------


def test_the_three_records_named_in_issue_118_are_flagged(acp):
    """Regression: the cases that motivated the issue must stay detected."""
    rows = acp.audit()
    flagged = {r["file_path"] for r in rows}
    for expected in (
        "archaea/sulfolobus_medium_for_dsm_9790.yaml",
        "bacterial/TOGO_M1791_Pelobacter_acetylenicus_Medium.yaml",
        "bacterial/TOGO_M1796_Desulfovibrio_medium.yaml",
    ):
        assert expected in flagged, f"{expected} no longer flagged"


def test_stock_solution_records_are_excluded(acp):
    """High magnitudes are correct in a stock-solution record by definition.

    Without this exclusion the audit would flag thousands of the ~4,784 MediaDive
    solution records that live in bacterial/ (#124).
    """
    from record_kinds import is_solution_record
    import yaml as _yaml

    rows = acp.audit()
    normalized = REPO_ROOT / "data" / "normalized_yaml"
    for r in rows[:400]:
        doc = _yaml.safe_load((normalized / r["file_path"]).read_text())
        assert not is_solution_record(doc), f"solution record flagged: {r['file_path']}"
