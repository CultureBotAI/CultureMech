from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_2076_2077_score15.py"
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
    return _load_script(SCRIPT, "repair_komodo_2076_2077_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_2076_2077")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module, target: Path) -> dict:
    expected = repair_module.TARGETS[target]
    return {
        "id": expected["id"],
        "name": target.stem,
        "original_name": expected["name"],
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": repair_module.PH_VALUES.get(target),
        "notes": f"Source: KOMODO ModelSEED | ID: {expected['media_term'].split(':')[1]}",
        "media_term": {
            "preferred_term": repair_module.SOURCE_LABELS[target],
            "term": {"id": expected["media_term"], "label": expected["name"]},
        },
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURES[target]
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_expands_empty_komodo_2076_record(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(
        repair_module.MEDIUM_1121_TARGET,
        _doc(repair_module, repair_module.MEDIUM_1121_TARGET),
    )
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"]) == (
        repair_module.FINAL_INGREDIENT_SIGNATURES[repair_module.MEDIUM_1121_TARGET]
    )
    assert "ph_value" not in repaired
    assert "KAI(SO4)2" in ingredients["KAl(SO4)2 x 12 H2O"]["notes"]
    assert "MnSO4 x X H2O" in ingredients["MnSO4 x 2 H2O"]["notes"]
    assert "Fe2(SO4)3 x xH2O" in ingredients["Fe2(SO4)3 x n H2O"]["notes"]
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.MEDIUM_1121_TARGET), repaired)]) == []


def test_repair_expands_komodo_2077_record(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(
        repair_module.MEDIUM_1146_TARGET,
        _doc(repair_module, repair_module.MEDIUM_1146_TARGET),
    )
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"]) == (
        repair_module.FINAL_INGREDIENT_SIGNATURES[repair_module.MEDIUM_1146_TARGET]
    )
    assert repaired["ph_value"] == 3.0
    assert ingredients["Na2SeO3"]["term"] == {"id": "CHEBI:48843", "label": "disodium selenite"}
    assert "NaSeO3" in ingredients["Na2SeO3"]["notes"]
    assert "H3BO" in ingredients["H3BO3"]["notes"]
    assert "Ni2SO4 x 6 H2O" in ingredients["NiSO4 x 6 H2O"]["notes"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.MEDIUM_1146_TARGET), repaired)]) == []


def test_repair_grounds_all_disclosed_components(repair_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(target, _doc(repair_module, target))
        ingredients = _by_name(repaired["ingredients"])

        for name in ingredients:
            identifier, label = repair_module.GROUNDINGS[name]
            assert ingredients[name]["term"] == {"id": identifier, "label": label}
            assert ingredients[name]["mediaingredientmech_chebi_term"] == {
                "id": identifier,
                "label": label,
            }


def test_repair_adds_reference_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(
        repair_module.MEDIUM_1146_TARGET,
        _doc(repair_module, repair_module.MEDIUM_1146_TARGET),
    )
    twice = repair_module.repair_record(repair_module.MEDIUM_1146_TARGET, once)

    assert twice == once
    assert once["references"] == [
        {"reference": repair_module.REFERENCES[repair_module.MEDIUM_1146_TARGET]}
    ]
    assert once["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
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


def test_plan_repairs_target_records(repair_module) -> None:
    expected_targets = {repair_module.NORMALIZED / target for target in repair_module.TARGETS}

    assert set(repair_module.plan_repairs()) == expected_targets


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module, repair_module.MEDIUM_1146_TARGET)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="CultureMech:004354"):
        repair_module.repair_record(repair_module.MEDIUM_1146_TARGET, doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module, repair_module.MEDIUM_1146_TARGET)
    doc["media_term"]["term"]["id"] = "komodo.medium:2070"

    with pytest.raises(ValueError, match="komodo.medium:2077"):
        repair_module.repair_record(repair_module.MEDIUM_1146_TARGET, doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.MEDIUM_1146_TARGET)
    doc["ingredients"][0]["preferred_term"] = "KOH"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(repair_module.MEDIUM_1146_TARGET, doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module, repair_module.MEDIUM_1146_TARGET)
    doc["solutions"] = [
        {
            "preferred_term": "Trace mineral solution",
            "concentration": {"value": "1", "unit": "ML_PER_L"},
        }
    ]

    with pytest.raises(ValueError, match="unexpected solutions"):
        repair_module.repair_record(repair_module.MEDIUM_1146_TARGET, doc)
