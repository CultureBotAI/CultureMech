from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2852_wilkins_chalgren_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2852_wilkins_chalgren_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2852")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": (
            "wilkins_chalgren_agar_plates_supplemented_with_10_human_blood_"
            "and_antibiotics"
        ),
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2852",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_restores_wilkins_chalgren_human_blood_and_antibiotics(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["functional_role"] == ["SELECTIVE"]
    assert repaired["temperature_value"] == 37.0
    assert repaired["incubation_atmosphere"] == "MICROAEROPHILIC"
    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert ingredients["Vancomycin"]["term"] == {
        "id": "CHEBI:28001",
        "label": "vancomycin",
    }
    assert ingredients["Cefsulodin"]["term"] == {
        "id": "CHEBI:3507",
        "label": "cefsulodin",
    }
    assert ingredients["Human blood"]["term"] == {
        "id": "UBERON:0000178",
        "label": "blood",
    }
    assert ingredients["Trimethoprim"]["cellular_metabolic_roles"] == ["INHIBITOR"]
    assert "term" not in ingredients["Fungizone (Bristol-Myers Squibb Co.)"]
    assert "term" not in ingredients["Wilkins-Chalgren agar plates (Oxoid)"]
    assert scorer_module.score_record(repaired) == (0, [])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_captures_microaerobic_gas_percentages(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Oxygen gas"]["concentration"] == {
        "value": "5",
        "unit": "PERCENT_V_V",
    }
    assert ingredients["Oxygen gas"]["term"] == {
        "id": "CHEBI:15379",
        "label": "dioxygen",
    }
    assert ingredients["Carbon dioxide gas"]["concentration"] == {
        "value": "10",
        "unit": "PERCENT_V_V",
    }
    assert ingredients["Nitrogen gas"]["concentration"] == {
        "value": "85",
        "unit": "PERCENT_V_V",
    }


def test_repair_adds_h_pylori_strain_evidence_and_references_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice == once
    assert once["organism_culture_type"] == "isolate"
    assert [row["strain"] for row in once["target_organisms"]] == [
        "B38",
        "J99 (ATCC 700824)",
    ]
    assert once["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
    ]
    assert once["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]

    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == "; ".join(repair_module.REFERENCES)


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:009395"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2854"

    with pytest.raises(ValueError, match="expected media term TOGO:M2852"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_component_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("vancomycin", "10", "MG_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)
