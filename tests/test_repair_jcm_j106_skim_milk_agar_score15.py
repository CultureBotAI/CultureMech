from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_j106_skim_milk_agar_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_j106_skim_milk_agar")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_j106")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(
    name: str,
    value: str,
    unit: str,
    composition: tuple[tuple[str, str, str], ...],
) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "composition": [
            _ingredient(component_name, component_value, component_unit)
            for component_name, component_value, component_unit in composition
        ],
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": repair_module.TARGET.stem,
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 7.0,
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "JCM Medium J106",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: JCM",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_replaces_flat_components_with_jcm_solutions(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ph_value"] == 7.0
    assert repaired["ingredients"] == []
    assert repair_module._solution_signatures(repaired) == (repair_module.FINAL_SOLUTION_SIGNATURES)
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_agar_and_water_inside_solutions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solution_a = _by_name(repaired["solutions"])["Solution A"]
    solution_b = _by_name(repaired["solutions"])["Solution B"]
    solution_a_components = _by_name(solution_a["composition"])
    solution_b_components = _by_name(solution_b["composition"])

    assert solution_a["concentration"] == {"value": "500.0", "unit": "ML_PER_L"}
    assert solution_b["concentration"] == {"value": "500.0", "unit": "ML_PER_L"}
    assert solution_a_components["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert solution_b_components["Agar"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert solution_b_components["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }


def test_repair_keeps_bd_difco_skim_milk_opaque(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    skim_milk = _by_name(_by_name(repaired["solutions"])["Solution A"]["composition"])[
        "Skim milk (BD-Difco)"
    ]

    assert skim_milk == {
        "preferred_term": "Skim milk (BD-Difco)",
        "concentration": {"value": "50.0", "unit": "G_PER_L"},
        "source": repair_module.SOURCE,
        "notes": (
            "JCM Medium 106 lists 25.0 g Skim milk (BD-Difco) in the "
            "500 ml Solution A stock; this complex milk product is retained "
            "as an opaque component."
        ),
    }


def test_repair_preserves_source_stated_separate_autoclaving(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert repaired["sterilization"] == repair_module.STERILIZATION


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["kg_microbe_match"] == "mediadive.medium:12"
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "nested Solution A and Solution B" in matching_events[0]["notes"]


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "mediadive.medium:J107"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Skim milk (BD-Difco)", "50", "G_PER_L")

    with pytest.raises(ValueError, match="recipe signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc.pop("ingredients")
    doc["solutions"] = [
        _solution(name, value, unit, composition)
        for name, value, unit, composition in repair_module.FINAL_SOLUTION_SIGNATURES
    ]
    doc["solutions"][0]["composition"][0]["concentration"]["value"] = "25.0"

    with pytest.raises(ValueError, match="recipe signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_jcm_j106_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert (
        repair_module._signature(doc.get("ingredients"), "ingredients"),
        repair_module._solution_signatures(doc),
    ) in (
        (repair_module.IMPORTED_INGREDIENT_SIGNATURE, ()),
        (
            repair_module.FINAL_INGREDIENT_SIGNATURE,
            repair_module.FINAL_SOLUTION_SIGNATURES,
        ),
    )
