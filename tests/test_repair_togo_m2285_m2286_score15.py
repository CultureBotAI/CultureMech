from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2285_m2286_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2285_m2286_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2285_m2286")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.expected_id,
        "name": target.path.stem,
        "original_name": "Vibrio Natriegens Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_signature
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {target.expected_media_term.removeprefix('TOGO:')}",
            "term": {"id": target.expected_media_term, "label": "Vibrio Natriegens Medium"},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_distilled_water_and_manganese_units(
    repair_module,
) -> None:
    expected = (
        (
            repair_module.TARGET_M2285,
            repair_module.M2285_FINAL_INGREDIENT_SIGNATURE,
            False,
        ),
        (
            repair_module.TARGET_M2286,
            repair_module.M2286_FINAL_INGREDIENT_SIGNATURE,
            True,
        ),
    )

    for target, signature, has_manganese in expected:
        repaired = repair_module.repair_record(_doc(target), target)
        ingredients = _by_name(repaired["ingredients"])

        assert repaired["medium_type"] == "COMPLEX"
        assert repaired["composition_type"] == "UNDEFINED"
        assert repaired["physical_state"] == "SOLID_AGAR"
        assert repaired["ph_value"] == 7.0
        assert repair_module._signature(repaired["ingredients"], "ingredients") == signature
        assert ingredients["Distilled water"]["concentration"] == {
            "value": "1.0",
            "unit": "L",
        }
        assert ("MnSO4 x H2O" in ingredients) is has_manganese
        if has_manganese:
            assert ingredients["MnSO4 x H2O"]["concentration"] == {
                "value": "10.0",
                "unit": "MG_PER_L",
            }


def test_repair_grounds_disclosed_unambiguous_components(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module.TARGET_M2286),
        repair_module.TARGET_M2286,
    )
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Agar, if necessary"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert ingredients["Distilled water"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:15377",
        "label": "water",
    }
    assert ingredients["MnSO4 x H2O"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:86364",
        "label": "manganese(II) sulfate monohydrate",
    }
    assert ingredients["NaCl"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:26710",
        "label": "sodium chloride",
    }
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Peptone",
    }


def test_repair_keeps_meat_extract_unmapped(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module.TARGET_M2285),
        repair_module.TARGET_M2285,
    )
    meat_extract = _by_name(repaired["ingredients"])["Meat extract"]

    assert "term" not in meat_extract
    assert "mediaingredientmech_chebi_term" not in meat_extract
    assert "retained without an ontology grounding" in meat_extract["notes"]


def test_repair_adds_ph_adjustment_without_inventing_sterilization(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module.TARGET_M2285),
        repair_module.TARGET_M2285,
    )

    assert repaired["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 7.0.",
        }
    ]
    assert "sterilization" not in repaired
    assert "ph_range" not in repaired
    assert "temperature_value" not in repaired
    assert "temperature_range" not in repaired


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(target), target)

        assert scorer_module.score_record(repaired) == (0, [])
        assert scorer_module.score_parsed([(str(target.path), repaired)]) == []
        assert repaired["data_quality_flags"] == [
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    target = repair_module.TARGET_M2286
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice["references"] == [
        {"reference": url} for url in target.reference_urls
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
    assert "sporulation MnSO4 x H2O unit artifacts" in matching_events[0]["notes"]


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGET_M2285
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.expected_id):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGET_M2285
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=target.expected_media_term):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGET_M2286
    doc = _doc(target)
    doc["ingredients"][2] = _ingredient("MnSO4 x H2O", "10", "MG_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGET_M2285
    doc = _doc(target)
    doc["solutions"] = [
        {
            "preferred_term": "NaCl solution",
            "concentration": {"value": "1.5", "unit": "PERCENT_W_V"},
            "composition": [],
        }
    ]

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_repair_contract(
    repair_module,
) -> None:
    for target in repair_module.TARGETS:
        path = repair_module.NORMALIZED / target.path
        doc = yaml.safe_load(path.read_text(encoding="utf-8"))

        assert doc["id"] == target.expected_id
        assert repair_module._source_term_id(doc) == target.expected_media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in (
            target.imported_signature,
            target.final_signature,
        )
        assert "solutions" not in doc
