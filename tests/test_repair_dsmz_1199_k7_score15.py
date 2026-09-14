from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_1199_k7_score15.py"
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
    return _load_script(SCRIPT, "repair_dsmz_1199_k7_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_1199")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "k7_medium",
        "original_name": "K7 MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "DSMZ Medium 1199",
            "term": {"id": repair_module.EXPECTED_PARENT_TERM, "label": "K7 MEDIUM"},
        },
        "notes": "Source: DSMZ",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "variant_children": [],
    }


def _child_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_CHILD_ID,
        "name": "k7_medium",
        "original_name": "K7 medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 1199",
            "term": {"id": repair_module.EXPECTED_CHILD_TERM, "label": "K7 medium"},
        },
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.KOMODO_CHILD_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "parent_media": {
            "path": "data/normalized_yaml/bacterial/k7_medium.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": repair_module.EXPECTED_PARENT_ID,
            "name": "k7_medium",
            "notes": "stale exact-signature note",
        },
        "variant_modifications": [
            "KOMODO record is an exact source duplicate of DSMZ Medium 1199."
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_adds_dsmz_water_and_yeast_extract_grounding(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_parent(_parent_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert ingredients["Glucose"]["term"] == {"id": "CHEBI:17234", "label": "glucose"}
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert "term" not in ingredients["Peptone"]
    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.PARENT), repaired)]) == []


def test_repair_updates_source_duplicate_link_and_is_idempotent(
    repair_module,
) -> None:
    parent_once = repair_module.repair_parent(_parent_doc(repair_module))
    parent_twice = repair_module.repair_parent(parent_once)
    child_once = repair_module.repair_child(_child_doc(repair_module))
    child_twice = repair_module.repair_child(child_once)

    assert parent_twice == parent_once
    assert child_twice == child_once
    assert parent_once["variant_children"] == [repair_module.KOMODO_CHILD_ENTRY]
    assert child_once["parent_media"] == repair_module.KOMODO_PARENT_MEDIA
    assert child_once["variant_modifications"] == [
        "KOMODO records distilled water with a variable concentration where DSMZ Medium 1199 lists 1000.0 ml/L."
    ]
    assert parent_once["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert parent_once["references"] == [
        {"reference": repair_module.MEDIADIVE_1199},
        {"reference": repair_module.DSMZ_1199},
    ]


def test_repair_rejects_wrong_parent_id(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_PARENT_ID):
        repair_module.repair_parent(doc)


def test_repair_rejects_wrong_parent_media_term(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["media_term"]["term"]["id"] = "mediadive.medium:9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_PARENT_TERM):
        repair_module.repair_parent(doc)


def test_repair_rejects_parent_ingredient_drift(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["ingredients"][0]["concentration"] = {"value": "2", "unit": "G_PER_L"}

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_parent(doc)


def test_repair_rejects_child_ingredient_drift(repair_module) -> None:
    doc = _child_doc(repair_module)
    doc["ingredients"][1]["concentration"] = {"value": "1000", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_child(doc)
