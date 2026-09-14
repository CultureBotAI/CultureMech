from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m2023_am3_antibiotics_score15.py"
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
    return _load_script(SCRIPT, "repair_togo_m2023_am3_antibiotics_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m2023")


def _component(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
    }


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "am3_nalidixic_acid_kanamycin_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ingredients": [
            _component(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M2023",
            "term": {
                "id": repair_module.EXPECTED_MEDIA_TERM,
                "label": repair_module.TITLE,
            },
        },
        "notes": "Source: TOGO M2023",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
        "parent_media": {
            "path": "data/normalized_yaml/bacterial/am3_medium.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:008609",
            "name": "am3_medium",
        },
        "variant_relationship": "SOURCE_DUPLICATE",
        "variant_modifications": [
            "Same ingredient and concentration signature; review as possible "
            "duplicate source record.",
        ],
    }


def _parent_doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_PARENT_ID,
        "name": "am3_medium",
        "original_name": "AM3 medium",
        "category": "bacterial",
        "media_term": {
            "preferred_term": "TOGO Medium M2021",
            "term": {
                "id": repair_module.EXPECTED_PARENT_MEDIA_TERM,
                "label": "AM3 medium",
            },
        },
        "curation_history": [],
        "variant_children": [
            {
                "path": (
                    "data/normalized_yaml/bacterial/"
                    "am3_nalidixic_acid_kanamycin_medium.yaml"
                ),
                "relationship": "SOURCE_DUPLICATE",
                "id": repair_module.EXPECTED_ID,
                "name": "am3_nalidixic_acid_kanamycin_medium",
                "notes": (
                    "Same ingredient and concentration signature; review as "
                    "possible duplicate source record."
                ),
            },
            {
                "path": "data/normalized_yaml/bacterial/am3_nalidixic_acid_medium.yaml",
                "relationship": "SOURCE_DUPLICATE",
                "id": "CultureMech:008610",
                "name": "am3_nalidixic_acid_medium",
                "notes": (
                    "Same ingredient and concentration signature; review as "
                    "possible duplicate source record."
                ),
            },
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_am3_formula_and_marks_selective(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["functional_role"] == ["SELECTIVE"]
    assert "ph_value" not in repaired
    assert repair_module._signature(
        repaired["ingredients"],
        "ingredients",
    ) == repair_module.FINAL_INGREDIENT_SIGNATURE
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "1000.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Beef extract"]["term"] == {
        "id": "FOODON:03302088",
        "label": "Beef extract",
    }
    assert ingredients["Peptone"]["term"] == {
        "id": "MICRO:0000178",
        "label": "Peptone",
    }
    assert ingredients["Agar (if needed)"]["term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []


def test_repair_expands_filter_sterilized_antibiotic_stocks(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    nalidixic = _by_name(
        solutions["Nalidixic acid solution (100 mg/ml)"]["composition"]
    )["Nalidixic acid"]
    kanamycin = _by_name(solutions["Kanamycin solution (25 mg/ml)"]["composition"])[
        "Kanamycin"
    ]

    assert repair_module._solution_signatures(repaired) == (
        repair_module.FINAL_SOLUTION_SIGNATURES
    )
    assert solutions["Nalidixic acid solution (100 mg/ml)"]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    assert solutions["Kanamycin solution (25 mg/ml)"]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    assert nalidixic["concentration"] == {"value": "100.0", "unit": "MG_PER_ML"}
    assert nalidixic["term"] == {
        "id": "CHEBI:100147",
        "label": "nalidixic acid",
    }
    assert kanamycin["concentration"] == {"value": "25.0", "unit": "MG_PER_ML"}
    assert kanamycin["term"] == {"id": "CHEBI:6104", "label": "kanamycin"}


def test_repair_adds_preparation_variant_references_and_event_once(
    repair_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert [step["action"] for step in twice["preparation_steps"]] == [
        "MIX",
        "AUTOCLAVE",
        "FILTER_STERILIZE",
        "MIX",
    ]
    assert twice["parent_media"] == repair_module.PARENT_MEDIA
    assert twice["variant_relationship"] == "SUPPLEMENTED_VARIANT"
    assert twice["variant_modifications"] == repair_module.VARIANT_MODIFICATIONS
    assert twice["sterilization"] == repair_module.STERILIZATION
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
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
    assert matching_events[0]["source"] == "; ".join(repair_module.REFERENCES)


def test_repair_updates_parent_variant_child_once(repair_module) -> None:
    once = repair_module.repair_parent(_parent_doc(repair_module))
    twice = repair_module.repair_parent(once)

    assert twice["variant_children"] == [
        repair_module.TOGO_CHILD,
        {
            "path": "data/normalized_yaml/bacterial/am3_nalidixic_acid_medium.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:008610",
            "name": "am3_nalidixic_acid_medium",
            "notes": (
                "Same ingredient and concentration signature; review as possible "
                "duplicate source record."
            ),
        },
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


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M2022"

    with pytest.raises(ValueError, match="expected media term TOGO:M2023"):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _component("Distilled water", "1000", "ML_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["preferred_term"] = "Kanamycin solution (25 mg/ml)"

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m2023_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        repair_module.FINAL_INGREDIENT_SIGNATURE,
    )
    assert repair_module._solution_signatures(doc) in (
        repair_module.IMPORTED_SOLUTION_SIGNATURES,
        repair_module.FINAL_SOLUTION_SIGNATURES,
    )
