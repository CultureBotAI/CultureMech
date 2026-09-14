from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m8_tomato_juice_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
PLACEHOLDER_INGREDIENTS = (("See source for composition", "variable", "VARIABLE"),)


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m8_tomato_juice_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_m8")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _medium_doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "tomato_juice_agar",
        "original_name": "Tomato Juice Agar",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": "source medium",
            "term": {"id": target.source_term, "label": target.source_name},
        },
        "notes": "Source",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition", "resolved_reference"],
        "kg_microbe_match": "mediadive.medium:12",
    }


def _solution_doc(record_id: str, composition: tuple) -> dict:
    return {
        "id": record_id,
        "preferred_term": "Main sol. J15",
        "term": {
            "id": "mediadive.solution:3636",
            "label": "Main sol. J15",
        },
        "composition": [
            _ingredient(name, value, unit)
            for name, value, unit in composition
        ],
        "preparation_notes": "Adjust pH to 7.2.",
        "curation_history": [],
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in PLACEHOLDER_INGREDIENTS
        ],
        "data_quality_flags": ["incomplete_composition"],
        "category": "bacterial",
    }


def _repair_medium(repair_module, path: Path) -> dict:
    target = next(target for target in repair_module.TARGETS if target.path == path)
    return repair_module.repair_medium_record(_medium_doc(target), target)


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_mediadive_j15_becomes_canonical_parent(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.MEDIADIVE_J15_PATH)

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.DIRECT_COMPOSITION
    assert repaired["ph_value"] == 7.2
    assert repaired["variant_children"] == [repair_module.M8_CHILD]
    assert "parent_media" not in repaired
    assert "kg_microbe_match" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed(
        [("bacterial/tomato_juice_agar.yaml", repaired)]
    ) == []


def test_togo_m8_links_to_j15_source_duplicate(
    repair_module,
    scorer_module,
) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M8_PATH)

    assert repaired["parent_media"] == repair_module.J15_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [repair_module.M8_CHILD["notes"]]
    assert "variant_children" not in repaired
    assert "kg_microbe_match" not in repaired
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed(
        [("bacterial/TOGO_M8_Tomato_Juice_Agar.yaml", repaired)]
    ) == []


def test_repair_corrects_units_and_groundings(repair_module) -> None:
    repaired = _repair_medium(repair_module, repair_module.TOGO_M8_PATH)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "800.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Tomato juice"]["concentration"] == {
        "value": "200.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Tomato juice"]["term"] == {
        "id": "FOODON:03301454",
        "label": "Tomato juice",
    }
    assert ingredients["Agar"]["physicochemical_roles"] == ["SOLIDIFYING_AGENT"]
    assert ingredients["Yeast extract (BD-Difco)"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert ingredients["Tryptone (BD-Difco)"]["term"] == {
        "id": "MICRO:0000182",
        "label": "Tryptone",
    }


def test_solution_3636_corrects_false_percent_rows(repair_module) -> None:
    doc = _solution_doc(
        "CultureMech:012716",
        repair_module.IMPORTED_SOLUTION_3636_COMPOSITION,
    )
    repaired = repair_module.repair_solution_record(doc)
    composition = _by_name(repaired["composition"])

    assert "ingredients" not in repaired
    assert repair_module._signature(
        repaired["composition"],
        "composition",
    ) == repair_module.SOLUTION_3636_COMPOSITION
    assert composition["Tryptone (BD-Difco)"]["term"] == {
        "id": "MICRO:0000182",
        "label": "Tryptone",
    }
    assert composition["Tomato juice"]["concentration"] == {
        "value": "200.0",
        "unit": "ML_PER_L",
    }
    assert composition["Distilled water"]["concentration"] == {
        "value": "800.0",
        "unit": "ML_PER_L",
    }
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]


def test_repair_adds_references_flags_and_event_once(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M8_PATH
    )
    once = repair_module.repair_medium_record(_medium_doc(target), target)
    twice = repair_module.repair_medium_record(once, target)

    assert twice == once
    assert once["references"] == [
        {"reference": reference} for reference in target.references
    ]
    assert once["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR
        and event.get("action") == target.action
    ]
    assert len(matching_events) == 1
    assert repair_module.TOGO_M8 in matching_events[0]["source"]
    assert "tomato juice" in matching_events[0]["notes"]


def test_repair_rejects_wrong_medium_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _medium_doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_medium_ingredient_drift(repair_module) -> None:
    target = next(
        target for target in repair_module.TARGETS if target.path == repair_module.TOGO_M8_PATH
    )
    doc = _medium_doc(target)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_medium_record(doc, target)


def test_repair_rejects_solution_composition_drift(repair_module) -> None:
    doc = _solution_doc(
        "CultureMech:012716",
        repair_module.IMPORTED_SOLUTION_3636_COMPOSITION,
    )
    doc["composition"].pop()

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_solution_record(doc)
