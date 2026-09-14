from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_oatmeal_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_jcm_oatmeal_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_oatmeal")


def _minimal_doc(repair_module, path: str) -> dict:
    ingredients = [
        {
            "preferred_term": repair_module.OATMEAL,
            "concentration": {"value": "30", "unit": "G_PER_L"},
        },
        {
            "preferred_term": repair_module.AGAR,
            "concentration": {"value": "20", "unit": "G_PER_L"},
        },
    ]
    if path == repair_module.TOGO:
        ingredients.insert(
            0,
            {
                "preferred_term": repair_module.WATER,
                "concentration": {"value": "1", "unit": "G_PER_L"},
            },
        )

    return {
        "id": repair_module.EXPECTED_IDS[path],
        "name": "oatmeal_agar",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "term": {"id": repair_module.EXPECTED_SOURCE_TERMS[path]},
        },
        "ingredients": ingredients,
        "curation_history": [],
    }


def _component(rows: list[dict], preferred_term: str) -> dict:
    return next(row for row in rows if row["preferred_term"] == preferred_term)


def _target(repair_module, path: str):
    return next(target for target in repair_module.TARGETS if target.path == path)


def test_repair_jcm_adds_missing_water_and_source_steps(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.JCM)
    repaired = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.JCM),
        target,
    )

    ingredients = {row["preferred_term"]: row for row in repaired["ingredients"]}
    assert list(ingredients) == [
        repair_module.OATMEAL,
        repair_module.AGAR,
        repair_module.WATER,
    ]
    assert ingredients[repair_module.WATER]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert repaired["preparation_steps"][0]["action"] == "HEAT"
    assert repaired["preparation_steps"][1] == {
        "step_number": 2,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 15 min.",
    }
    assert scorer_module.score_record(repaired)[1] == ["no pH and no temperature"]


def test_repair_jcm_accepts_pre_repair_oatmeal_label(repair_module) -> None:
    target = _target(repair_module, repair_module.JCM)
    doc = _minimal_doc(repair_module, repair_module.JCM)
    doc["ingredients"][0]["preferred_term"] = repair_module.IMPORTED_OATMEAL

    repaired = repair_module.repair_document(doc, target)

    assert repaired["ingredients"][0]["preferred_term"] == repair_module.OATMEAL


def test_repair_togo_normalizes_water_unit_and_links_parent(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.TOGO)
    repaired = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.TOGO),
        target,
    )

    water = _component(repaired["ingredients"], repair_module.WATER)
    assert water["concentration"] == {"value": "1000", "unit": "ML_PER_L"}
    assert water["term"] == {"id": "CHEBI:15377", "label": "water"}
    assert repaired["parent_media"] == repair_module.JCM_PARENT
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert scorer_module.score_record(repaired)[1] == ["no pH and no temperature"]


def test_repair_adds_flags_references_history_and_duplicate_child(
    repair_module,
) -> None:
    target = _target(repair_module, repair_module.JCM)
    repaired = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.JCM),
        target,
    )

    assert repaired["variant_children"] == [repair_module.TOGO_CHILD]
    assert repaired["references"] == [{"reference": repair_module.JCM_URL}]
    assert repaired["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert repaired["curation_history"][-1]["action"] == repair_module.ACTION


def test_repair_document_is_idempotent(repair_module) -> None:
    for target in repair_module.TARGETS:
        once = repair_module.repair_document(
            _minimal_doc(repair_module, target.path),
            target,
        )
        twice = repair_module.repair_document(once, target)

        matching_events = [
            event
            for event in twice["curation_history"]
            if (
                event.get("curator") == repair_module.CURATOR
                and event.get("action") == repair_module.ACTION
            )
        ]
        assert len(matching_events) == 1
        assert once == twice


def test_repair_document_rejects_wrong_id(repair_module) -> None:
    target = _target(repair_module, repair_module.JCM)
    doc = _minimal_doc(repair_module, repair_module.JCM)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:002506'"):
        repair_module.repair_document(doc, target)


def test_repair_document_rejects_wrong_source_term(repair_module) -> None:
    target = _target(repair_module, repair_module.TOGO)
    doc = _minimal_doc(repair_module, repair_module.TOGO)
    doc["media_term"]["term"]["id"] = "TOGO:M42"

    with pytest.raises(ValueError, match="expected 'TOGO:M139'"):
        repair_module.repair_document(doc, target)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    target = _target(repair_module, repair_module.JCM)
    doc = _minimal_doc(repair_module, repair_module.JCM)
    doc["ingredients"][0]["preferred_term"] = "Rolled oats"

    with pytest.raises(ValueError, match="missing Oatmeal Agar core ingredient"):
        repair_module.repair_document(doc, target)


def test_target_records_are_expected_jcm_148_recipes(repair_module) -> None:
    expected_names = [row["preferred_term"] for row in repair_module.INGREDIENTS]

    for target in repair_module.TARGETS:
        doc = yaml.safe_load((repair_module.NORMALIZED / target.path).read_text(encoding="utf-8"))
        repaired = repair_module.repair_document(doc, target)

        assert doc["id"] == repair_module.EXPECTED_IDS[target.path]
        assert [row["preferred_term"] for row in repaired["ingredients"]] == expected_names
