"""Tests for the cross-category filename collision triage (#116).

The classifier's whole value is the EQUIVALENT class: by exact ingredient tuples
almost every collision looks DIFFERENT, but most of those differences are
ingestion artefacts (label variants, a spurious water row, the same ingredient
grounded to two CHEBI ids) rather than genuinely distinct media. If normalization
is too weak the report is useless; if it is too aggressive it will recommend
merging media that differ for real.
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
def afc():
    return _load("audit_filename_collisions")


def _doc(*ings):
    return {"ingredients": [
        {"preferred_term": n, "term": ({"id": i} if i else None),
         "concentration": {"value": v, "unit": "G_PER_L"}}
        for n, v, i in ings
    ]}


# --- label normalization --------------------------------------------------


@pytest.mark.parametrize("a,b", [
    ("MgSO4・7H2O", "MgSO4 x 7 H2O"),
    ("MgSO4·7H2O", "MgSO4 x 7 H2O"),
    ("Soluble starch", "Starch"),
    ("Glucose", "glucose"),
])
def test_ingestion_label_variants_fold_together(afc, a, b):
    assert afc.normalize_name(a) == afc.normalize_name(b)


@pytest.mark.parametrize("a,b", [
    ("MgSO4 x 7 H2O", "MgCl2 x 7 H2O"),
    ("Glucose", "Galactose"),
    ("KH2PO4", "K2HPO4"),
])
def test_genuinely_different_ingredients_stay_apart(afc, a, b):
    """Normalization must not be so aggressive that distinct chemicals collide."""
    assert afc.normalize_name(a) != afc.normalize_name(b)


# --- classification -------------------------------------------------------


def test_identical_compositions(afc):
    d = _doc(("Glucose", "4", "CHEBI:17234"), ("Agar", "20", "CHEBI:2509"))
    assert afc.classify([d, d])[0] == "IDENTICAL"


def test_label_variant_only_is_equivalent(afc):
    a = _doc(("MgSO4・7H2O", "1", "CHEBI:31795"))
    b = _doc(("MgSO4 x 7 H2O", "1", "CHEBI:31795"))
    assert afc.classify([a, b])[0] == "EQUIVALENT"


def test_spurious_water_row_is_ignored(afc):
    """One ingestion path adds a water row (often implausibly, see #118)."""
    a = _doc(("Distilled water", "1", "CHEBI:15377"), ("Agar", "20", "CHEBI:2509"))
    b = _doc(("Agar", "20", "CHEBI:2509"))
    assert afc.classify([a, b])[0] == "EQUIVALENT"


def test_same_ingredient_grounded_to_two_chebi_ids_is_equivalent(afc):
    """The real 1_10_sabourauds_agar case: labels agree, groundings disagree."""
    a = _doc(("Glucose", "4", "CHEBI:42758"))
    b = _doc(("Glucose", "4", "CHEBI:17234"))
    assert afc.classify([a, b])[0] == "EQUIVALENT"


def test_differing_concentration_is_not_equivalent(afc):
    """Concentration is load-bearing — cf. Pfennig's medium in #127."""
    a = _doc(("NaCl", "10", "CHEBI:26710"))
    b = _doc(("NaCl", "30", "CHEBI:26710"))
    assert afc.classify([a, b])[0] == "DIFFERENT"


def test_extra_non_water_ingredient_is_not_equivalent(afc):
    a = _doc(("Glucose", "4", "CHEBI:17234"), ("Yeast extract", "2", None))
    b = _doc(("Glucose", "4", "CHEBI:17234"))
    assert afc.classify([a, b])[0] == "DIFFERENT"


def test_disjoint_compositions_report_zero_overlap(afc):
    a = _doc(("Glucose", "4", "CHEBI:17234"))
    b = _doc(("Peptone", "5", None))
    cls, evidence = afc.classify([a, b])
    assert cls == "DIFFERENT"
    assert evidence.startswith("0/")


# --- the real corpus ------------------------------------------------------


def test_the_eleven_methano_collisions_from_issue_116_are_resolved():
    """#116 listed 11 methano* files present in BOTH bacterial/ and archaea/.

    #120 resolved them; this pins that they do not come back.
    """
    names = [
        "marine_methanogenic_medium", "methanogen_high_salt_medium",
        "methanogenium_cv_medium", "methanogenium_medium",
        "methanogenium_medium_h2_co2", "methanogens_saline_water_medium",
        "methanohalophilus_euhalobius_medium", "methanohalophilus_halophilus_medium",
        "methanohalophilus_medium", "modified_balchs_methanogen_medium_1_b",
        "modified_methanohalophilus_medium",
    ]
    normalized = REPO_ROOT / "data" / "normalized_yaml"
    still_colliding = [
        n for n in names
        if (normalized / "bacterial" / f"{n}.yaml").is_file()
        and (normalized / "archaea" / f"{n}.yaml").is_file()
    ]
    assert not still_colliding, f"re-introduced bacterial/archaea collisions: {still_colliding}"
