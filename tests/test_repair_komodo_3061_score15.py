from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_3061_score15.py"
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
    return _load_script(SCRIPT, "repair_komodo_3061_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_3061")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": "Trace element solution (630)",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 6.8,
        "notes": (
            "pH buffer: KOH | Source: KOMODO ModelSEED | ID: 3061 | "
            "DSMZ Medium: 3061 (mediadive.medium:3061)"
        ),
        "media_term": {
            "preferred_term": "KOMODO Medium 3061",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "Trace element solution (630)",
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


def test_repair_expands_komodo_3061_metabolite_table(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"]) == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repaired["record_kind"] == "SOLUTION"
    assert repaired["ph_value"] == 6.8
    assert set(ingredients) == {
        name for name, _value, _unit in repair_module.FINAL_INGREDIENT_SIGNATURE
    }
    assert "KOH" not in ingredients
    assert "NaOH" not in ingredients
    assert ingredients["H2SO4"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_all_disclosed_components(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    for name, (identifier, label) in repair_module.GROUNDINGS.items():
        assert ingredients[name]["term"] == {"id": identifier, "label": label}
        assert ingredients[name]["mediaingredientmech_chebi_term"] == {
            "id": identifier,
            "label": label,
        }

    assert ingredients["NiCl2 x 6 H2O"]["term"] == {
        "id": "CHEBI:53542",
        "label": "nickel chloride hexahydrate",
    }
    assert ingredients["CoCl2 x 4 H2O"]["term"] == {
        "id": "CHEBI:35696",
        "label": "cobalt dichloride",
    }


def test_repair_preserves_ph_adjusters_as_process_context_only(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    ph_step = repaired["preparation_steps"][1]["description"]
    assert "pH 6.8" in ph_step
    assert "KOH" in ph_step
    assert "NaOH" in ph_step
    assert "KOH" in repaired["curation_history"][-1]["notes"]
    assert "NaOH" in repaired["curation_history"][-1]["notes"]


def test_repair_adds_reference_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert once["references"] == [{"reference": repair_module.KOMODO_3061}]
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


def test_plan_repairs_target_record(repair_module) -> None:
    target_path = repair_module.NORMALIZED / repair_module.TARGET
    expected_target = repair_module.repair_record(
        yaml.safe_load(target_path.read_text(encoding="utf-8"))
    )

    assert repair_module.plan_repairs() == {target_path: expected_target}


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "komodo.medium:3062"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["preferred_term"] = "NaOH"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [
        {
            "preferred_term": "Trace element solution",
            "concentration": {"value": "1", "unit": "ML_PER_L"},
        }
    ]

    with pytest.raises(ValueError, match="unexpected solutions"):
        repair_module.repair_record(doc)
