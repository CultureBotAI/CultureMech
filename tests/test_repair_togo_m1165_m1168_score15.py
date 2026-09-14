from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1165_m1168_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1165_m1168_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1165_m1168")


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
        "id": target.record_id,
        "name": "bicarbonate_buffered_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "SEMI_DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
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
            for name, value, unit, _ in repair_module._imported_solution_signatures(target)
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_direct_formula_and_resazurin_unit(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert (
        repair_module._signature(
            repaired["ingredients"],
            "ingredients",
        )
        == repair_module.FINAL_INGREDIENT_SIGNATURE
    )
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "0.5",
        "unit": "MG_PER_L",
    }
    assert ingredients["Na2HPO4 x 2H2O"]["term"] == {
        "id": "CHEBI:91258",
        "label": "disodium hydrogenphosphate dihydrate",
    }
    assert "term" not in ingredients["Yeast extract"]
    assert "ph_value" not in repaired
    assert "ph_range" not in repaired


def test_repair_expands_shared_stocks(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    solutions = _by_name(repaired["solutions"])
    fecl2 = _by_name(solutions["FeCl2 solution"]["composition"])
    trace = _by_name(solutions["Trace element solution"]["composition"])
    selenite = _by_name(solutions["Selenite-tungstate solution"]["composition"])
    vitamins = _by_name(solutions["Trace vitamins"]["composition"])
    nahco3 = _by_name(solutions["8% NaHCO3 solution"]["composition"])

    assert solutions["FeCl2 solution"]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    assert fecl2["FeCl2 x 4H2O"]["concentration"] == {
        "value": "1.5",
        "unit": "G_PER_L",
    }
    assert trace["MnCl2 x 4H2O"]["term"] == {
        "id": "CHEBI:86368",
        "label": "manganese(II) chloride tetrahydrate",
    }
    assert selenite["Na2WO4 x 2H2O"]["term"] == {
        "id": "CHEBI:63939",
        "label": "sodium tungstate dihydrate",
    }
    assert vitamins["Vitamin B12"]["concentration"] == {
        "value": "0.1",
        "unit": "MG_PER_L",
    }
    assert nahco3["NaHCO3"]["concentration"] == {
        "value": "8.0",
        "unit": "PERCENT_W_V",
    }


def test_repair_specializes_substrate_stock_per_target(repair_module) -> None:
    expected = {
        "TOGO:M1165": ("1 M glycerin solution", "Glycerol", "CHEBI:17754"),
        "TOGO:M1166": ("1 M glycerin solution", "Glycerol", "CHEBI:17754"),
        "TOGO:M1167": (
            "1 M trisodium citrate solution",
            "Trisodium citrate",
            "CHEBI:53258",
        ),
        "TOGO:M1168": ("1 M maltose solution", "Maltose", "CHEBI:18167"),
    }

    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, target), target)
        solution_name, substrate_name, term_id = expected[target.media_term]
        solutions = _by_name(repaired["solutions"])
        substrate = _by_name(solutions[solution_name]["composition"])[substrate_name]

        assert solutions[solution_name]["concentration"] == {
            "value": "10.0",
            "unit": "ML_PER_L",
        }
        assert substrate["concentration"] == {"value": "1.0", "unit": "MOLAR"}
        assert substrate["term"]["id"] == term_id


def test_repair_record_drops_all_targets_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    parsed = []
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, target), target)
        parsed.append((str(target.path), repaired))

        assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
        assert repaired["data_quality_flags"] == [
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        ]

    assert scorer_module.score_parsed(parsed) == []


def test_repair_adds_references_and_event_once(repair_module) -> None:
    target = repair_module.TARGETS[0]
    once = repair_module.repair_record(_doc(repair_module, target), target)
    twice = repair_module.repair_record(once, target)

    assert twice["references"] == [{"reference": url} for url in repair_module._references(target)]
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

    with pytest.raises(ValueError, match="expected id CultureMech:007689"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "TOGO:M1166"

    with pytest.raises(ValueError, match="expected media term TOGO:M1165"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][0] = _ingredient("Tap water", "930", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["solutions"][0]["concentration"] = {"value": "1", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_repair_contract(repair_module) -> None:
    for target in repair_module.TARGETS:
        doc = yaml.safe_load((repair_module.NORMALIZED / target.path).read_text())

        assert doc["id"] == target.record_id
        assert repair_module._source_term_id(doc) == target.media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in (
            repair_module.IMPORTED_INGREDIENT_SIGNATURE,
            repair_module.FINAL_INGREDIENT_SIGNATURE,
        )
        assert repair_module._solution_signatures(doc) in (
            repair_module._imported_solution_signatures(target),
            repair_module._final_solution_signatures(target),
        )
