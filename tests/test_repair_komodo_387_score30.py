from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_387_score30.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "thermophilic_methanosaeta_medium",
        "original_name": "THERMOPHILIC METHANOSAETA MEDIUM",
        "category": "archaea",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.5,
        "media_term": {
            "preferred_term": "KOMODO Medium 387",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "THERMOPHILIC METHANOSAETA MEDIUM",
            },
        },
        "notes": "Source: KOMODO ModelSEED | ID: 387 | DSMZ Medium: 387",
        "ingredients": [],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


@pytest.fixture
def repair():
    return _load_script(SCRIPT, "repair_komodo_387_score30")


@pytest.fixture
def scorer():
    return _load_script(SCORER, "score_review_need_for_komodo_387")


def test_repair_record_expands_thermophilic_methanosaeta_medium(
    repair,
    scorer,
) -> None:
    once = repair.repair_record(_doc(repair))
    twice = repair.repair_record(once)

    assert once == twice
    assert scorer.score_record(twice) == (0, [])
    assert once["medium_type"] == "DEFINED"
    assert once["composition_type"] == "DEFINED"
    assert once["ph_value"] == 6.5
    assert len(once["ingredients"]) == 36


def test_repair_record_scales_base_and_trace_components(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "NH4Cl")["concentration"] == {
        "value": "0.492611",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Na2SeO3 x 5 H2O")["concentration"] == {
        "value": "0.000002956",
        "unit": "G_PER_L",
    }
    assert (
        "1015 mL final formulation"
        in _ingredient(
            repaired,
            "MgSO4 x 7 H2O",
        )["notes"]
    )


def test_repair_record_combines_calcium_and_adds_coenzyme_m(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "CaCl2 x 2 H2O")["concentration"] == {
        "value": "0.099507",
        "unit": "G_PER_L",
    }
    assert _ingredient(repaired, "Coenzyme M")["term"] == {
        "id": "CHEBI:17905",
        "label": "coenzyme M",
    }
    assert _ingredient(repaired, "Coenzyme M")["concentration"] == {
        "value": "0.139901",
        "unit": "G_PER_L",
    }


def test_repair_record_uses_dsmz_387_gas_notes(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert _ingredient(repaired, "N2")["source"] == repair.SOURCE_387
    assert _ingredient(repaired, "CO2")["source"] == repair.SOURCE_387
    assert "30% CO2" in _ingredient(repaired, "CO2")["notes"]


def test_repair_record_adds_references_and_flags(repair) -> None:
    repaired = repair.repair_record(_doc(repair))

    assert repaired["references"] == [
        {"reference": repair.KOMODO_387_URL},
        {"reference": repair.DSMZ_387_URL},
        {"reference": repair.DSMZ_141_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert "mediaingredientmech_chebi_term" in _ingredient(repaired, "Coenzyme M")


def test_repair_record_rejects_wrong_id(repair) -> None:
    doc = _doc(repair)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected immutable id CultureMech:005164"):
        repair.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair) -> None:
    doc = _doc(repair)
    doc["media_term"]["term"]["id"] = "komodo.medium:141"

    with pytest.raises(ValueError, match="missing expected media term komodo.medium:387"):
        repair.repair_record(doc)
