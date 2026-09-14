from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_m1050_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_m1050_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_togo_m1050")


def _ingredient(name: str, value: str, unit: str) -> dict:
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
        "name": "m30",
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
            "preferred_term": "TOGO Medium M1050",
            "term": {"id": repair_module.EXPECTED_MEDIA_TERM, "label": repair_module.TITLE},
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


def test_repair_moves_flattened_m30_recipe_into_two_solutions(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    assert repaired["physical_state"] == "SOLID_AGAR"
    assert repaired["ingredients"] == []
    assert set(solutions) == {
        "Solution 1",
        "Solution 2",
        "Modified Hutner's basal salts",
        'Metals "44"',
        "Vitamin solution No. 6",
    }
    assert solutions["Solution 1"]["concentration"] == {
        "value": "1030",
        "unit": "ML_PER_L",
    }
    assert solutions["Solution 2"]["concentration"] == {
        "value": "0.2",
        "unit": "ML_PER_L",
    }
    assert (
        repair_module._signature(
            solutions["Solution 1"]["composition"],
            "solution 1",
        )
        == repair_module.SOLUTION_1_SIGNATURE
    )
    assert (
        repair_module._signature(
            solutions["Solution 2"]["composition"],
            "solution 2",
        )
        == repair_module.SOLUTION_2_SIGNATURE
    )


def test_repair_expands_modified_hutner_and_metals_44(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    hutner = solutions["Modified Hutner's basal salts"]
    hutner_components = _by_name(hutner["composition"])
    metals = solutions['Metals "44"']
    metals_components = _by_name(metals["composition"])

    hutner_reference = _by_name(solutions["Solution 1"]["composition"])[
        "Modified Hutner's basal salts"
    ]
    assert hutner_reference["concentration"] == {
        "value": "20.0",
        "unit": "ML_PER_L",
    }
    assert "composition" not in hutner_reference
    assert hutner["concentration"] == {"value": "20.0", "unit": "ML_PER_L"}
    assert (
        repair_module._signature(
            hutner["composition"],
            "Modified Hutner's basal salts",
        )
        == repair_module.MODIFIED_HUTNER_SIGNATURE
    )
    assert hutner_components["FeSO4 x 7H2O"]["concentration"] == {
        "value": "99.0",
        "unit": "MG_PER_L",
    }
    assert hutner_components["(NH4)6Mo7O24 x 4H2O"]["term"] == {
        "id": "CHEBI:86244",
        "label": "hexaammonium heptamolybdate tetrahydrate",
    }
    assert metals["concentration"] == {"value": "50.0", "unit": "ML_PER_L"}
    assert metals_components["EDTA x 2Na"]["term"] == {
        "id": "CHEBI:64734",
        "label": "EDTA disodium salt (anhydrous)",
    }
    assert metals_components["Na2B4O7 x 10H2O"]["term"] == {
        "id": "CHEBI:131366",
        "label": "disodium tetraborate decahydrate",
    }
    assert "term" not in metals_components["MnSO4 x H2O"]


def test_repair_expands_solution_2_and_vitamin_solution_no_6(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])
    solution_2_components = _by_name(solutions["Solution 2"]["composition"])
    vitamins = solutions["Vitamin solution No. 6"]
    vitamin_components = _by_name(vitamins["composition"])

    assert solution_2_components["Ampicillin (50 mg/ml)"]["term"] == {
        "id": "CHEBI:28971",
        "label": "ampicillin",
    }
    assert solution_2_components["N-Acetyl-D-glucosamine (Sigma)"]["term"] == {
        "id": "CHEBI:506227",
        "label": "N-acetyl-D-glucosamine",
    }
    assert solution_2_components["Na2HPO4 x 2H2O"]["term"] == {
        "id": "CHEBI:91258",
        "label": "disodium hydrogenphosphate dihydrate",
    }
    assert solution_2_components["Vitamin solution No. 6"]["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert vitamins["concentration"] == {"value": "variable", "unit": "VARIABLE"}
    assert (
        repair_module._signature(
            vitamins["composition"],
            "Vitamin solution No. 6",
        )
        == repair_module.VITAMIN_SOLUTION_SIGNATURE
    )
    assert vitamin_components["Pyridoxine HCl"]["concentration"] == {
        "value": "20.0",
        "unit": "MG_PER_L",
    }
    assert vitamin_components["Thiamine HCl 2H2O"]["term"] == {
        "id": "CHEBI:132751",
        "label": "thiamine hydrochloride dihydrate",
    }


def test_repair_record_drops_out_of_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_record(repaired) == (5, ["no pH and no temperature"])
    assert scorer_module.score_parsed([("bacterial/TOGO_M1050_M30.yaml", repaired)]) == []
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]


def test_repair_adds_references_and_event_once(repair_module) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert twice["references"] == [{"reference": url} for url in repair_module.REFERENCES]
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


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match="expected id CultureMech:007567"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_media_term(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "TOGO:M1007"

    with pytest.raises(ValueError, match="expected media term TOGO:M1050"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0] = _ingredient("Tris-HCl buffer", "50", "G_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)


def test_repair_record_rejects_solution_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["solutions"][0]["concentration"] = {"value": "1030", "unit": "ML_PER_L"}

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_togo_m1050_repair_contract(repair_module) -> None:
    path = repair_module.NORMALIZED / repair_module.TARGET
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))

    assert doc["id"] == repair_module.EXPECTED_ID
    assert repair_module._source_term_id(doc) == repair_module.EXPECTED_MEDIA_TERM
    assert repair_module._signature(doc["ingredients"], "ingredients") in (
        repair_module.IMPORTED_INGREDIENT_SIGNATURE,
        (),
    )
    assert repair_module._solution_signatures(doc) in (
        repair_module.IMPORTED_SOLUTION_SIGNATURES,
        repair_module.SCHEMA_INVALID_NESTED_SOLUTION_SIGNATURES,
        repair_module.FINAL_SOLUTION_SIGNATURES,
    )
