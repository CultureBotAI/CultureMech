from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_2110_hutners_salts_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_komodo_2110_hutners_salts_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_2110")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": "Hutner's salts (medium 590)",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.8,
        "notes": "pH buffer: NaOH | Source: KOMODO ModelSEED",
        "media_term": {
            "preferred_term": "KOMODO Medium 2110",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "Hutner's salts (medium 590)",
            },
        },
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_expands_hutners_salts_and_metals_44(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    metals = repaired["solutions"][0]
    metals_components = _by_name(metals["composition"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repair_module._solution_signature(repaired["solutions"], "solutions") == (
        repair_module.FINAL_SOLUTION_SIGNATURE
    )
    assert repaired["ph_value"] == 6.8
    assert ingredients["Nitrilotriacetic acid"]["term"] == {
        "id": "CHEBI:44557",
        "label": "nitrilotriacetic acid",
    }
    assert ingredients["(NH4)6Mo7O24 x 4 H2O"]["concentration"] == {
        "value": "9.25",
        "unit": "MG_PER_L",
    }
    assert not {"KOH", "NaOH", "H2SO4"} & set(ingredients)
    assert metals["preferred_term"] == '"Metals 44"'
    assert metals_components["Na-EDTA"]["concentration"] == {
        "value": "250.0",
        "unit": "MG_PER_L",
    }
    assert metals_components["Co(NO3)2 x 6 H2O"]["term"] == {
        "id": "CHEBI:86214",
        "label": "cobalt dinitrate hexahydrate",
    }
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_adds_preparation_flags_references_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert once["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert once["references"] == [
        {"reference": repair_module.MEDIADIVE_590},
        {"reference": repair_module.DSMZ_590},
    ]
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "komodo.medium:9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["preferred_term"] = "KOH"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = repair_module.repair_record(_doc(repair_module))
    doc["solutions"][0]["concentration"] = {"value": "5.0", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)
