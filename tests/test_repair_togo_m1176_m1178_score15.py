from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1176_m1178_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1176_m1178_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1176_m1178")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module, target) -> dict:
    doc = {
        "id": target.record_id,
        "name": "anaerobic_natural_seawater_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module._imported_ingredient_signature(target)
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {target.media_term.removeprefix('TOGO:')}",
            "term": {"id": target.media_term, "label": repair_module.TITLE},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }
    solutions = [
        _solution(name, value, unit)
        for name, value, unit, _ in repair_module._imported_solution_signatures(target)
    ]
    if solutions:
        doc["solutions"] = solutions
    return doc


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_shared_base_and_resazurin_unit(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert repaired["ph_value"] == 7.0
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert ingredients["Distilled water"]["concentration"] == {
        "value": "250.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Natural seawater (filtrated)"]["concentration"] == {
        "value": "750.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.5",
        "unit": "MG_PER_L",
    }
    assert ingredients["N2"]["term"] == {"id": "CHEBI:17997", "label": "dinitrogen"}
    assert "term" not in ingredients["Tryptone"]


def test_repair_expands_reducer_stocks(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    solutions = _by_name(repaired["solutions"])

    assert solutions["5% L-Cysteine HCl H2O solution"]["concentration"] == {
        "value": "6.0",
        "unit": "ML_PER_L",
    }
    assert solutions["5% Na2S x 9H2O solution"]["concentration"] == {
        "value": "6.0",
        "unit": "ML_PER_L",
    }
    assert solutions["5% L-Cysteine HCl H2O solution"]["composition"][0]["term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }
    assert solutions["5% Na2S x 9H2O solution"]["composition"][0]["term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }


def test_repair_specializes_strain_variants(repair_module) -> None:
    by_term = {target.media_term: target for target in repair_module.TARGETS}

    pyruvate = repair_module.repair_record(
        _doc(repair_module, by_term["TOGO:M1176"]),
        by_term["TOGO:M1176"],
    )
    omitted = repair_module.repair_record(
        _doc(repair_module, by_term["TOGO:M1177"]),
        by_term["TOGO:M1177"],
    )
    vitamin = repair_module.repair_record(
        _doc(repair_module, by_term["TOGO:M1178"]),
        by_term["TOGO:M1178"],
    )

    pyruvate_ingredients = _by_name(pyruvate["ingredients"])
    omitted_ingredients = _by_name(omitted["ingredients"])
    vitamin_solutions = _by_name(vitamin["solutions"])
    vitamin_components = _by_name(vitamin_solutions["Trace vitamins"]["composition"])

    assert pyruvate_ingredients["sodium pyruvate"]["concentration"] == {
        "value": "10.0",
        "unit": "MILLIMOLAR",
    }
    assert pyruvate_ingredients["sodium pyruvate"]["term"] == {
        "id": "CHEBI:50144",
        "label": "sodium pyruvate",
    }
    assert "Resazurin" not in omitted_ingredients
    assert "solutions" not in omitted
    assert vitamin_solutions["Trace vitamins"]["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }
    assert vitamin_components["Vitamin B12"]["concentration"] == {
        "value": "0.1",
        "unit": "MG_PER_L",
    }


def test_repair_record_drops_all_targets_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    parsed = []
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, target), target)
        parsed.append((str(target.path), repaired))

        assert scorer_module.score_record(repaired) == (0, [])
        assert repaired["data_quality_flags"] == [
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        ]

    assert scorer_module.score_parsed(parsed) == []


def test_repair_adds_references_and_event_once(repair_module) -> None:
    target = repair_module.TARGETS[-1]
    once = repair_module.repair_record(_doc(repair_module, target), target)
    twice = repair_module.repair_record(once, target)

    assert twice["references"] == [
        {"reference": url} for url in repair_module._references(target)
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
    assert matching_events[0]["source"] == "; ".join(repair_module._references(target))


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:007701"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "TOGO:M1177"

    with pytest.raises(ValueError, match="expected media term TOGO:M1176"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][0] = _ingredient("Tap water", "250", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["solutions"][0] = _solution("5% Na2S x 9H2O solution", "7", "G_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)
