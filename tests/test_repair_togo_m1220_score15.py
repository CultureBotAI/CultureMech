from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1220_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1220_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1220")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _solution(name: str, value: str, unit: str) -> dict:
    return {
        "preferred_term": name,
        "composition": [],
        "concentration": {"value": value, "unit": unit},
    }


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.RECORD_ID,
        "name": "natronospira_proteinivora_medium",
        "original_name": "Natronospira Proteinivora Medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "media_term": {
            "preferred_term": "TOGO Medium M1220",
            "term": {
                "id": repair_module.MEDIA_TERM,
                "label": "Natronospira Proteinivora Medium",
            },
        },
        "notes": "Source: TOGO",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
        "high_metal": True,
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in repair_module.IMPORTED_SOLUTION_SIGNATURES
        ],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_expands_basic_and_basal_media(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["medium_type"] == "COMPLEX"
    assert repaired["composition_type"] == "SEMI_DEFINED"
    assert repaired["ingredients"] == []

    solutions = _by_name(repaired["solutions"])
    basic = _by_name(solutions["Basic mineral salt medium 1"]["composition"])
    basal = _by_name(solutions["Basal medium 2"]["composition"])

    assert solutions["Basic mineral salt medium 1"]["concentration"] == {
        "value": "500.0",
        "unit": "ML_PER_L",
    }
    assert basic["NaCl"]["concentration"] == {"value": "240.0", "unit": "G_PER_L"}
    assert basic["1 M K2HPO4 solution"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert basic["1 M K2HPO4 solution"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:131527",
        "label": "dipotassium hydrogen phosphate",
    }

    assert solutions["Basal medium 2"]["concentration"] == {
        "value": "500.0",
        "unit": "ML_PER_L",
    }
    assert basal["Na2CO3"]["concentration"] == {"value": "190.0", "unit": "G_PER_L"}
    assert basal["2 M NH4Cl solution"]["concentration"] == {
        "value": "4.0",
        "unit": "ML_PER_L",
    }


def test_repair_preserves_unexpanded_trace_stock_additions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    basic = _by_name(solutions["Basic mineral salt medium 1"]["composition"])
    basal = _by_name(solutions["Basal medium 2"]["composition"])

    assert basic["Trace element solution"]["concentration"] == {
        "value": "1.0",
        "unit": "ML_PER_L",
    }
    assert "term" not in basic["Trace element solution"]
    assert basal["Trace element solution"]["concentration"] == {
        "value": "2.0",
        "unit": "ML_PER_L",
    }
    assert "term" not in basal["Trace element solution"]


def test_repair_expands_complex_organic_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    tryptone = _by_name(solutions["10% Tryptone solution"]["composition"])
    yeast = _by_name(solutions["1.0% Yeast extract solution"]["composition"])

    assert tryptone["Tryptone"]["concentration"] == {
        "value": "100.0",
        "unit": "G_PER_L",
    }
    assert tryptone["Tryptone"]["term"] == {
        "id": "MICRO:0000182",
        "label": "Tryptone",
    }
    assert yeast["Yeast extract"]["concentration"] == {
        "value": "10.0",
        "unit": "G_PER_L",
    }
    assert yeast["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }


def test_repair_omits_unadded_casein_solution(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    components = repair_module._composition_components(repaired)

    assert "Casein" not in {row["preferred_term"] for row in components}
    assert "Casein solution" not in {row["preferred_term"] for row in repaired["solutions"]}
    assert "gives no Casein solution addition" in repaired["notes"]


def test_repair_drops_m1220_out_of_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([(str(repair_module.TARGET), repaired)]) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [{"reference": url} for url in repair_module._references()]
    matching_events = [
        event
        for event in twice["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == "; ".join(repair_module._references())


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:007748"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1221"

    with pytest.raises(ValueError, match="expected media term TOGO:M1220"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Tap water", "1", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0] = _solution("Other stock", "15", "G_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)
