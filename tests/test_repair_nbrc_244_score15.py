from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_nbrc_244_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
sys.path.insert(0, str(REPO / "src"))
from culturemech.ingredients import resolve_ingredient  # noqa: E402


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_nbrc_244_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_nbrc_244")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "togo_medium_m1466",
        "original_name": "(Unnamed medium)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in repair_module.LEGACY_INGREDIENTS
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1466",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "TOGO Medium M1466",
            },
        },
        "notes": "Source: NBRC - NBRC_M244",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "245",
        "original_name": "245",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 7.6,
        "media_term": {
            "preferred_term": "NBRC Medium 244",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "NBRC Medium 244",
            },
        },
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in repair_module.FINAL_INGREDIENTS
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_formula_and_exits_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["ph_value"] == 7.6
    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENTS
    )
    assert ingredients["Seawater"]["concentration"] == {
        "value": "750",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "250",
        "unit": "ML_PER_L",
    }
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_all_components(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert ingredients["Malt extract"]["term"] == {
        "id": "FOODON:03301056",
        "label": "Malt extract",
    }
    assert ingredients["Seawater"]["term"] == {
        "id": "ENVO:00002149",
        "label": "Seawater",
    }
    assert ingredients["Glucose"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17234",
        "label": "glucose",
    }
    assert ingredients["Agar (if needed)"]["physicochemical_roles"] == [
        "SOLIDIFYING_AGENT",
    ]

    unresolved = {
        ingredient["preferred_term"]
        for ingredient in repaired["ingredients"]
        if not resolve_ingredient(ingredient).is_resolved
    }
    assert unresolved == set()


def test_repair_links_togo_record_to_nbrc_parent(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["parent_media"] == repair_module.PARENT_MEDIA
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [
        repair_module.VARIANT_MODIFICATIONS,
    ]


def test_repair_parent_links_togo_child_once(repair_module) -> None:
    once = repair_module.repair_parent(_parent_doc(repair_module))
    twice = repair_module.repair_parent(once)

    assert twice["variant_children"] == [repair_module.TOGO_CHILD]

    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.LINK_ACTION
        )
    ]
    assert matching_events == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.LINK_ACTION,
            "source": "; ".join(repair_module.TARGET_REFERENCES),
            "notes": "Linked TOGO M1466 as a source duplicate of NBRC Medium 244.",
        }
    ]


def test_repair_target_adds_preparation_references_flags_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_target(_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.TARGET_REFERENCES
    ]
    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
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
    assert "corrected Seawater and Distilled water" in matching_events[0]["notes"]


def test_plan_repairs_target_and_parent_records(repair_module) -> None:
    target_path = repair_module.NORMALIZED / repair_module.TARGET
    parent_path = repair_module.NORMALIZED / repair_module.PARENT

    assert repair_module.plan_repairs() == {
        target_path: repair_module.repair_target(
            yaml.safe_load(target_path.read_text(encoding="utf-8"))
        ),
        parent_path: repair_module.repair_parent(
            yaml.safe_load(parent_path.read_text(encoding="utf-8"))
        ),
    }


def test_repair_rejects_wrong_target_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_parent_id(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_PARENT_ID):
        repair_module.repair_parent(doc)


def test_repair_rejects_wrong_target_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1453"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_parent_media_term(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["media_term"]["term"]["id"] = "nbrc.medium:245"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_PARENT_MEDIA_TERM):
        repair_module.repair_parent(doc)


def test_repair_rejects_target_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][1] = _ingredient("Yeast extract", "5", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(doc)


def test_repair_rejects_parent_ingredient_drift(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["ingredients"][3] = _ingredient("Seawater", "750", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_parent(doc)


def test_corpus_parent_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.PARENT
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_PARENT_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_PARENT_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") == (
        repair_module.FINAL_INGREDIENTS
    )


def test_corpus_target_record_matches_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in {
        repair_module.LEGACY_INGREDIENTS,
        repair_module.FINAL_INGREDIENTS,
    }
