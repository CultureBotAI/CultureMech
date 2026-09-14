from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_1203_fastidious_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_1203_fastidious_score20")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_fastidious")


def _minimal_doc(repair_module, path: str) -> dict:
    ingredients = [
        {
            "preferred_term": repair_module.IMPORTED_FASTIDIOUS,
            "concentration": {"value": "45.7", "unit": "G_PER_L"},
            "term": {"id": "CHEBI:2509", "label": "agar"},
            "mediaingredientmech_chebi_term": {"id": "CHEBI:2509", "label": "agar"},
        },
        {
            "preferred_term": repair_module.IMPORTED_HORSE_BLOOD,
            "concentration": {"value": "100", "unit": "G_PER_L"},
        },
    ]
    if path == repair_module.KOMODO_3136:
        ingredients.append({"preferred_term": repair_module.WATER})

    return {
        "id": repair_module.EXPECTED_IDS[path],
        "name": "fastidious_anaerobe_agar",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "term": {"id": repair_module.EXPECTED_SOURCE_TERMS[path]},
        },
        "ingredients": ingredients,
        "curation_history": [],
    }


def _target(repair_module, path: str):
    return next(target for target in repair_module.TARGETS if target.path == path)


def _component(rows: list[dict], preferred_term: str) -> dict:
    return next(row for row in rows if row["preferred_term"] == preferred_term)


def test_repair_rebuilds_dsmz_formula(repair_module, scorer_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_3136)

    repaired = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.KOMODO_3136),
        target,
    )

    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        repair_module.FASTIDIOUS,
        repair_module.WATER,
        repair_module.HORSE_BLOOD,
    ]
    assert _component(repaired["ingredients"], repair_module.WATER)["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert _component(repaired["ingredients"], repair_module.HORSE_BLOOD)["concentration"] == {
        "value": "5-10",
        "unit": "PERCENT_V_V",
    }
    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ph_range"] == repair_module.PH_RANGE
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert repaired["sterilization"] == repair_module.STERILIZATION
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_removes_false_fastidious_agar_grounding(repair_module) -> None:
    target = _target(repair_module, repair_module.DSMZ)

    repaired = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.DSMZ),
        target,
    )
    product = repaired["ingredients"][0]

    assert "term" not in product
    assert "mediaingredientmech_chebi_term" not in product


def test_repair_keeps_blood_out_of_chebi_only_slot(repair_module) -> None:
    target = _target(repair_module, repair_module.DSMZ)

    repaired = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.DSMZ),
        target,
    )
    blood = _component(repaired["ingredients"], repair_module.HORSE_BLOOD)

    assert blood["term"] == {"id": "UBERON:0000178", "label": "blood"}
    assert "mediaingredientmech_chebi_term" not in blood


def test_repair_links_duplicates(repair_module) -> None:
    dsmz = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.DSMZ),
        _target(repair_module, repair_module.DSMZ),
    )
    komodo = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.KOMODO_1203),
        _target(repair_module, repair_module.KOMODO_1203),
    )

    assert dsmz["variant_children"] == [
        repair_module.SOURCE_DUPLICATES[repair_module.KOMODO_1203],
        repair_module.SOURCE_DUPLICATES[repair_module.KOMODO_3136],
    ]
    assert komodo["parent_media"] == repair_module.DSMZ_PARENT
    assert komodo["variant_relationship"] == "SOURCE_DUPLICATE"


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_3136)

    repaired = repair_module.repair_document(
        _minimal_doc(repair_module, repair_module.KOMODO_3136),
        target,
    )

    assert repaired["references"] == [{"reference": repair_module.DSMZ_URL}]
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
    target = _target(repair_module, repair_module.DSMZ)
    doc = _minimal_doc(repair_module, repair_module.DSMZ)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected 'CultureMech:000653'"):
        repair_module.repair_document(doc, target)


def test_repair_document_rejects_wrong_source_term(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_3136)
    doc = _minimal_doc(repair_module, repair_module.KOMODO_3136)
    doc["media_term"]["term"]["id"] = "komodo.medium:1203"

    with pytest.raises(ValueError, match="expected 'komodo.medium:3136'"):
        repair_module.repair_document(doc, target)


def test_repair_document_rejects_ingredient_drift(repair_module) -> None:
    target = _target(repair_module, repair_module.DSMZ)
    doc = _minimal_doc(repair_module, repair_module.DSMZ)
    doc["ingredients"][0]["preferred_term"] = "Fastidious Anaerobe Broth"

    with pytest.raises(ValueError, match="missing Fastidious Anaerobe Agar"):
        repair_module.repair_document(doc, target)


def test_target_records_are_expected_dsmz_1203_recipes(repair_module) -> None:
    expected_names = [row["preferred_term"] for row in repair_module.INGREDIENTS]

    for target in repair_module.TARGETS:
        doc = yaml.safe_load((repair_module.NORMALIZED / target.path).read_text(encoding="utf-8"))
        repaired = repair_module.repair_document(doc, target)

        assert doc["id"] == repair_module.EXPECTED_IDS[target.path]
        assert [row["preferred_term"] for row in repaired["ingredients"]] == expected_names
