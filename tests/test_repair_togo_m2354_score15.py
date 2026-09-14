from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2354_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
CONCENTRATION_AUDIT = REPO / "scripts" / "audit_concentration_plausibility.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m2354_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2354")


@pytest.fixture(scope="module")
def concentration_module():
    return _load_script(CONCENTRATION_AUDIT, "concentration_audit_for_togo_m2354")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "medium_for_erythrobacter_longus",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2354",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "medium_for_erythrobacter_longus",
        "original_name": "MEDIUM FOR ERYTHROBACTER LONGUS",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.5,
        "media_term": {
            "preferred_term": "DSMZ Medium 695",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "MEDIUM FOR ERYTHROBACTER LONGUS",
            },
        },
        "notes": "Source: DSMZ",
        "ingredients": [],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "variant_children": [
            {
                "path": (
                    "data/normalized_yaml/bacterial/"
                    "KOMODO_695_medium_FOR_ERYTHROBACTER_LONGUS.yaml"
                ),
                "relationship": "SOURCE_DUPLICATE",
                "id": "CultureMech:006313",
                "name": "medium_for_erythrobacter_longus",
            },
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_volume_rows_and_adds_fe_citrate_stock(
    repair_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "UNDEFINED"
    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_value"] == 7.5
    assert repair_module._component_signature(
        repaired["ingredients"], "ingredients"
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert repair_module._solution_signature(
        repaired["solutions"]
    ) == repair_module.FINAL_SOLUTION_SIGNATURE
    assert ingredients["Artificial seawater"]["concentration"] == {
        "value": "700.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "300.0",
        "unit": "ML_PER_L",
    }
    assert solutions["5% Fe(III) citrate"]["concentration"] == {
        "value": "2.0",
        "unit": "ML_PER_L",
    }


def test_repair_grounds_disclosed_unambiguous_components(
    repair_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    fe_citrate = repaired["solutions"][0]["composition"][0]

    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["Peptone (BBL 11910)"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Bacto peptone",
    }
    assert ingredients["Proteose peptone no.3 (Difco)"]["term"] == {
        "id": "MICRO:0000180",
        "label": "Proteose Peptone",
    }
    assert ingredients["Soytone (Difco)"]["term"] == {
        "id": "FOODON:03315720",
        "label": "Soy peptone",
    }
    assert ingredients["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert fe_citrate["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:144421",
        "label": "iron(III) citrate",
    }


def test_repair_keeps_artificial_seawater_unmapped(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))
    artificial_seawater = _by_name(repaired["ingredients"])["Artificial seawater"]

    assert "term" not in artificial_seawater
    assert "mediaingredientmech_chebi_term" not in artificial_seawater
    assert "retained without a single-compound ontology grounding" in artificial_seawater[
        "notes"
    ]


def test_repair_adds_ph_adjustment_without_inventing_sterilization(
    repair_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 7.5.",
        }
    ]
    assert "sterilization" not in repaired
    assert "ph_range" not in repaired
    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired


def test_repair_links_togo_record_to_dsmz_parent(repair_module) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert repaired["parent_media"] == repair_module.PARENT_MEDIA
    assert repaired["variant_relationship"] == "SOURCE_DUPLICATE"
    assert repaired["variant_modifications"] == [
        repair_module.VARIANT_MODIFICATION,
    ]


def test_repair_record_drops_out_of_review_and_concentration_reports(
    repair_module,
    scorer_module,
    concentration_module,
) -> None:
    repaired = repair_module.repair_target(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert concentration_module.audit_parsed(
        [(repair_module.NORMALIZED / repair_module.TARGET, repaired)]
    ) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_target(_doc(repair_module))
    twice = repair_module.repair_target(once)

    assert twice["references"] == [
        {"reference": url} for url in repair_module.REFERENCES
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
    assert "5% Fe(III) citrate" in matching_events[0]["notes"]


def test_repair_parent_adds_togo_child_once(repair_module) -> None:
    once = repair_module.repair_parent(_parent_doc(repair_module))
    twice = repair_module.repair_parent(once)

    assert twice["variant_children"] == [
        {
            "path": (
                "data/normalized_yaml/bacterial/"
                "KOMODO_695_medium_FOR_ERYTHROBACTER_LONGUS.yaml"
            ),
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:006313",
            "name": "medium_for_erythrobacter_longus",
        },
        repair_module.TOGO_CHILD,
    ]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.LINK_ACTION
        )
    ]
    assert len(matching_events) == 1


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_target(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_target(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("5% Fe(III) citrate", "2", "ML_PER_L")

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_target(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"] = [
        {
            "preferred_term": "5% Fe(III) citrate",
            "concentration": {"value": "2.0", "unit": "ML_PER_L"},
            "composition": [],
        }
    ]

    with pytest.raises(ValueError, match="composition signature drifted"):
        repair_module.repair_target(doc)


def test_repair_parent_rejects_wrong_parent_id(repair_module) -> None:
    doc = _parent_doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_PARENT_ID):
        repair_module.repair_parent(doc)


def test_target_record_matches_togo_m2354_repair_contract(
    repair_module,
) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert (
        repair_module._component_signature(doc["ingredients"], "ingredients"),
        repair_module._solution_signature(doc.get("solutions")),
    ) in (
        (repair_module.IMPORTED_INGREDIENT_SIGNATURE, ()),
        (
            repair_module.FINAL_INGREDIENT_SIGNATURE,
            repair_module.FINAL_SOLUTION_SIGNATURE,
        ),
    )
