from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1101_m1102_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1101_m1102_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_mpycy")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module, target) -> dict:
    return {
        "id": target.expected_id,
        "name": "mpycy_agar_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": target.physical_state,
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_ingredients
        ],
        "media_term": {
            "preferred_term": f"TOGO Medium {target.media_term.removeprefix('TOGO:')}",
            "term": {"id": target.media_term, "label": repair_module.TITLE},
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_sets_variant_specific_direct_components(repair_module) -> None:
    agar = repair_module.TARGETS[0]
    liquid = repair_module.TARGETS[1]
    repaired_agar = repair_module.repair_record(_doc(repair_module, agar), agar)
    repaired_liquid = repair_module.repair_record(_doc(repair_module, liquid), liquid)

    assert repaired_agar["ph_range"] == {"min": 7.6, "max": 7.8}
    assert repaired_agar["physical_state"] == "SOLID_AGAR"
    assert repair_module._signature(
        repaired_agar["ingredients"],
        "ingredients",
    ) == repair_module.AGAR_FINAL_INGREDIENT_SIGNATURE
    assert _by_name(repaired_agar["ingredients"])["Agar (if necessary)"]["term"] == {
        "id": "CHEBI:2509",
        "label": "agar",
    }

    assert repaired_liquid["ph_range"] == {"min": 7.4, "max": 7.6}
    assert repaired_liquid["physical_state"] == "LIQUID"
    assert repair_module._signature(
        repaired_liquid["ingredients"],
        "ingredients",
    ) == repair_module.LIQUID_FINAL_INGREDIENT_SIGNATURE
    assert "Agar (if necessary)" not in _by_name(repaired_liquid["ingredients"])


def test_repair_expands_m1100_solutions(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    solutions = _by_name(repaired["solutions"])
    solution_b = _by_name(solutions["Solution B"]["composition"])

    assert set(solutions) == {
        "Solution A",
        "Solution B",
        "Vitamins mix solution",
        "FeCl3 solution",
    }
    assert repair_module._signature(
        solutions["Solution A"]["composition"],
        "Solution A",
    ) == repair_module.SOLUTION_A_SIGNATURE
    assert repair_module._signature(
        solutions["Solution B"]["composition"],
        "Solution B",
    ) == repair_module.SOLUTION_B_SIGNATURE
    assert "term" not in solution_b["0.5 M Na2HPO4-NaH2PO4 buffer (pH 7.3)"]


def test_repair_expands_m290_and_fecl3_stocks(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    solutions = _by_name(repaired["solutions"])
    vitamins = _by_name(solutions["Vitamins mix solution"]["composition"])

    assert repair_module._signature(
        solutions["Vitamins mix solution"]["composition"],
        "Vitamins mix solution",
    ) == repair_module.VITAMINS_SIGNATURE
    assert repair_module._signature(
        solutions["FeCl3 solution"]["composition"],
        "FeCl3 solution",
    ) == repair_module.FECL3_SIGNATURE
    assert vitamins["Vitamin B12"]["concentration"] == {
        "value": "1.0",
        "unit": "MG_PER_L",
    }
    assert vitamins["Myo-inositol"]["term"] == {
        "id": "CHEBI:17268",
        "label": "myo-inositol",
    }


def test_repair_records_drop_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = [
        (
            str(target.path),
            repair_module.repair_record(_doc(repair_module, target), target),
        )
        for target in repair_module.TARGETS
    ]

    assert scorer_module.score_parsed(repaired) == []
    for _, doc in repaired:
        assert scorer_module.score_record(doc) == (0, [])
        assert doc["data_quality_flags"] == [
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    target = repair_module.TARGETS[0]
    once = repair_module.repair_record(_doc(repair_module, target), target)
    twice = repair_module.repair_record(once, target)

    assert twice["references"] == [
        {"reference": url} for url in (target.togo_url, *repair_module.REFERENCES)
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
    assert matching_events[0]["source"] == "; ".join(
        (target.togo_url, *repair_module.REFERENCES)
    )


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:007620"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "TOGO:M1007"

    with pytest.raises(ValueError, match="expected media term TOGO:M1101"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][0] = _ingredient("Water", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["solutions"][0]["concentration"] = {"value": "5", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)


@pytest.mark.parametrize("target", [0, 1])
def test_target_records_match_togo_mpycy_repair_contract(
    repair_module,
    target: int,
) -> None:
    target_record = repair_module.TARGETS[target]
    path = repair_module.NORMALIZED / target_record.path
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == target_record.expected_id
    assert repair_module._source_term_id(doc) == target_record.media_term
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        target_record.imported_ingredients,
        target_record.final_ingredients,
    )
    assert repair_module._solution_signatures(doc) in (
        repair_module.IMPORTED_SOLUTION_SIGNATURES,
        repair_module.FINAL_SOLUTION_SIGNATURES,
    )
