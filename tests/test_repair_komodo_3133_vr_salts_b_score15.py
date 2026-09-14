from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_3133_vr_salts_b_score15.py"
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
    return _load_script(SCRIPT, "repair_komodo_3133_vr_salts_b_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_3133_vr_salts_b")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": "VR salts B",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.0,
        "notes": (
            "pH buffer: NaOH | Source: KOMODO ModelSEED | ID: 3133 | "
            "DSMZ Medium: 3133 (mediadive.medium:3133) | SubMedium: Yes"
        ),
        "media_term": {
            "preferred_term": "KOMODO Medium 3133",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "VR salts B",
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


def test_repair_expands_vr_salts_b_stock(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"]) == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repaired["record_kind"] == "SOLUTION"
    assert "ph_value" not in repaired
    assert set(ingredients) == {
        name for name, _value, _unit in repair_module.FINAL_INGREDIENT_SIGNATURE
    }
    assert ingredients["MgSO4 x 7 H2O"]["concentration"] == {
        "value": "24.0",
        "unit": "G_PER_L",
    }
    assert ingredients["CuSO4 x 5 H2O"]["concentration"] == {
        "value": "0.125",
        "unit": "G_PER_L",
    }
    assert ingredients["HCl"]["concentration"] == {
        "value": "2.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["NaOH"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_all_except_exact_vso4_hydrate(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    for name, (identifier, label) in repair_module.GROUNDINGS.items():
        assert ingredients[name]["term"] == {"id": identifier, "label": label}
        assert ingredients[name]["mediaingredientmech_chebi_term"] == {
            "id": identifier,
            "label": label,
        }

    assert "term" not in ingredients["VSO4 x 7 H2O"]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_source_preparation_steps(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    steps = repaired["preparation_steps"]

    assert [step["action"] for step in steps] == [
        "MIX",
        "ADJUST_PH",
        "MIX",
        "MIX",
        "FILTER",
        "STORE",
    ]
    assert "2 ml HCl" in steps[0]["description"]
    assert "7.0 to 7.4" in steps[1]["description"]
    assert "Refrigerate" in steps[-1]["description"]


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert {row["reference"] for row in once["references"]} == {
        repair_module.ROGOSA_1969,
        repair_module.ROGOSA_1969_DOI,
    }

    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1


def test_plan_repairs_targets_record(repair_module) -> None:
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
    doc["media_term"]["term"]["id"] = "komodo.medium:510"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["preferred_term"] = "HCl"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [
        {
            "preferred_term": "VR salts A",
            "concentration": {"value": "30", "unit": "ML_PER_L"},
        }
    ]

    with pytest.raises(ValueError, match="unexpected solutions"):
        repair_module.repair_record(doc)
