from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_middlebrook_hemin_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_jcm_middlebrook_hemin_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_middlebrook_hemin")


def _minimal_doc(repair_module, path: str) -> dict:
    return {
        "id": repair_module.EXPECTED_IDS[path],
        "name": "hemin_medium_for_mycobacterium",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID" if path == repair_module.JCM714 else "SOLID_AGAR",
        "media_term": {
            "term": {"id": repair_module.EXPECTED_SOURCE_TERMS[path]},
        },
        "ingredients": [
            {
                "preferred_term": repair_module.IMPORTED_MIDDLEBROOK,
                "concentration": {"value": "21.1111", "unit": "G_PER_L"},
                "term": {"id": "CHEBI:2509", "label": "agar"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:2509",
                    "label": "agar",
                },
            },
            {
                "preferred_term": repair_module.GLYCEROL,
                "concentration": {"value": "5", "unit": "G_PER_L"},
                "term": {"id": "CHEBI:17754", "label": "glycerol"},
                "mediaingredientmech_chebi_term": {
                    "id": "CHEBI:17754",
                    "label": "glycerol",
                },
            },
        ],
        "curation_history": [],
    }


def _target(repair_module, path: str):
    return next(target for target in repair_module.TARGETS if target.path == path)


def _component(rows: list[dict], preferred_term: str) -> dict:
    return next(row for row in rows if row["preferred_term"] == preferred_term)


def test_repair_jcm386_rebuilds_live_parent_formula(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.JCM386)

    repaired = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.JCM386),
        target,
    )

    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        repair_module.MIDDLEBROOK,
        repair_module.GLYCEROL,
        repair_module.WATER,
        repair_module.OADC,
    ]
    assert _component(repaired["ingredients"], repair_module.MIDDLEBROOK)[
        "concentration"
    ] == {"value": "19", "unit": "G_PER_L"}
    assert _component(repaired["ingredients"], repair_module.GLYCEROL)[
        "concentration"
    ] == {"value": "5", "unit": "ML_PER_L"}
    assert _component(repaired["ingredients"], repair_module.OADC)[
        "concentration"
    ] == {"value": "100", "unit": "ML_PER_L"}
    assert repaired["preparation_steps"] == list(repair_module.BASE_PREPARATION_STEPS)
    assert scorer_module.score_record(repaired)[1] == ["no pH and no temperature"]


def test_repair_jcm714_adds_hemin_and_parent_link(
    repair_module,
    scorer_module,
) -> None:
    target = _target(repair_module, repair_module.JCM714)

    repaired = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.JCM714),
        target,
    )

    hemin = _component(repaired["ingredients"], repair_module.HEMIN)

    assert repaired["physical_state"] == "SOLID_AGAR"
    assert hemin["concentration"] == {"value": "60", "unit": "MICROMOLAR"}
    assert hemin["term"] == {"id": "CHEBI:50385", "label": "hemin"}
    assert repaired["parent_media"] == repair_module.JCM386_PARENT
    assert repaired["variant_relationship"] == "SUPPLEMENTED_VARIANT"
    assert repaired["preparation_steps"] == list(repair_module.HEMIN_PREPARATION_STEPS)
    assert scorer_module.score_record(repaired)[1] == ["no pH and no temperature"]


def test_repair_removes_false_middlebrook_agar_grounding(repair_module) -> None:
    target = _target(repair_module, repair_module.JCM386)

    repaired = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.JCM386),
        target,
    )
    middlebrook = repaired["ingredients"][0]

    assert "term" not in middlebrook
    assert "mediaingredientmech_chebi_term" not in middlebrook


def test_repair_adds_flags_references_history_and_variant_child(
    repair_module,
) -> None:
    target = _target(repair_module, repair_module.JCM386)

    repaired = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.JCM386),
        target,
    )

    assert repaired["variant_children"] == [repair_module.JCM714_CHILD]
    assert repaired["references"] == [{"reference": repair_module.JCM386_URL}]
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
    target = _target(repair_module, repair_module.JCM714)
    doc = _minimal_doc(repair_module, repair_module.JCM714)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:003061'"):
        repair_module.repair_document(doc, target)


def test_repair_document_rejects_wrong_source_term(repair_module) -> None:
    target = _target(repair_module, repair_module.JCM386)
    doc = _minimal_doc(repair_module, repair_module.JCM386)
    doc["media_term"]["term"]["id"] = "mediadive.medium:J1"

    with pytest.raises(ValueError, match="expected 'mediadive.medium:J386'"):
        repair_module.repair_document(doc, target)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    target = _target(repair_module, repair_module.JCM386)
    doc = _minimal_doc(repair_module, repair_module.JCM386)
    doc["ingredients"][0]["preferred_term"] = "Middlebrook 7H11 agar"

    with pytest.raises(ValueError, match="missing Middlebrook 7H10 core ingredient"):
        repair_module.repair_document(doc, target)


def test_target_records_are_expected_jcm_386_714_recipes(repair_module) -> None:
    for target in repair_module.TARGETS:
        doc = yaml.safe_load(
            (repair_module.NORMALIZED / target.path).read_text(encoding="utf-8")
        )
        repaired = repair_module.repair_document(doc, target)

        assert doc["id"] == repair_module.EXPECTED_IDS[target.path]
        assert repaired["ingredients"][0]["preferred_term"] == repair_module.MIDDLEBROOK
