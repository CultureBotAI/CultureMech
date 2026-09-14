from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2310_reactivation_464a_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2310_reactivation_464a")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2310")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _target_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "reactivation_with_liquid_medium_464_plate_count_agar",
        "original_name": "Reactivation With Liquid Medium 464 (Plate Count Agar)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "TOGO Medium M2310",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": "Reactivation With Liquid Medium 464 (Plate Count Agar)",
            },
        },
        "notes": "Source: TOGO",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "reactivation_with_liquid_medium_464",
        "original_name": "REACTIVATION WITH LIQUID MEDIUM 464",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 7.0,
        "media_term": {
            "preferred_term": "DSMZ Medium 464a",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "REACTIVATION WITH LIQUID MEDIUM 464",
            },
        },
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.PARENT_INGREDIENT_SIGNATURE
        ],
        "variant_children": [
            {
                "path": (
                    "data/normalized_yaml/bacterial/"
                    "KOMODO_464a_REACTIVATION_WITH_LIQUID_medium_464.yaml"
                ),
                "relationship": "SOURCE_DUPLICATE",
                "id": "CultureMech:005520",
                "name": "reactivation_with_liquid_medium_464",
                "notes": (
                    "Same ingredient and concentration signature; KOMODO record "
                    "copied from the matching DSMZ medium source."
                ),
            },
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_restores_dsmz_formula_and_leaves_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_target(_target_doc(repair_module))

    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert repaired["ph_value"] == 7.0
    assert repaired["preparation_steps"] == list(repair_module.PREPARATION_STEPS)
    assert "solutions" not in repaired
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_grounds_every_dsmz_component(repair_module) -> None:
    repaired = repair_module.repair_target(_target_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "Yeast extract",
    }
    assert ingredients["Dextrose"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17634",
        "label": "D-glucose",
    }
    assert ingredients["Agar, if required"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["Tryptone"]["term"] == {
        "id": "MICRO:0000182",
        "label": "tryptone",
    }


def test_repair_links_source_duplicate_once(repair_module) -> None:
    once = repair_module.repair_target(_target_doc(repair_module))
    twice = repair_module.repair_target(once)
    parent_once = repair_module.repair_parent(_parent_doc(repair_module))
    parent_twice = repair_module.repair_parent(parent_once)

    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert twice["parent_media"] == repair_module.PARENT_MEDIA
    assert twice["variant_relationship"] == "SOURCE_DUPLICATE"
    assert twice["variant_modifications"] == [repair_module.VARIANT_MODIFICATIONS]
    assert parent_twice["variant_children"][-1] == repair_module.VARIANT_CHILD

    target_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    parent_events = [
        event
        for event in parent_twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.LINK_ACTION
        )
    ]
    assert len(target_events) == 1
    assert len(parent_events) == 1


def test_plan_repairs_target_and_parent(repair_module) -> None:
    plans = repair_module.plan_repairs()

    assert set(plans) == {
        repair_module.NORMALIZED / repair_module.PARENT,
        repair_module.NORMALIZED / repair_module.TARGET,
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:008897"):
        repair_module.repair_target(doc)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2311"

    with pytest.raises(ValueError, match="expected media term TOGO:M2310"):
        repair_module.repair_target(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _target_doc(repair_module)
    doc["ingredients"][0] = _ingredient("Distilled water", "1.0", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_target(doc)


def test_parent_rejects_wrong_id(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:001584"):
        repair_module.repair_parent(doc)


def test_corpus_records_match_repair_contract(repair_module) -> None:
    target_doc = yaml.safe_load(
        (repair_module.NORMALIZED / repair_module.TARGET).read_text(encoding="utf-8")
    )
    parent_doc = yaml.safe_load(
        (repair_module.NORMALIZED / repair_module.PARENT).read_text(encoding="utf-8")
    )

    assert target_doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(target_doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(target_doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    assert parent_doc["id"] == repair_module.EXPECTED_PARENT_ID
    assert repair_module._source_term_id(parent_doc) == (
        repair_module.EXPECTED_PARENT_MEDIA_TERM
    )
    assert repair_module._signature(parent_doc["ingredients"], "ingredients") == (
        repair_module.PARENT_INGREDIENT_SIGNATURE
    )
