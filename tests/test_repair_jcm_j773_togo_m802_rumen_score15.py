from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_j773_togo_m802_rumen_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_j773_togo_m802_rumen_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_j773_togo_m802")


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
        "name": "rumen_fluid_medium",
        "original_name": repair_module.TITLE,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit)
            for name, value, unit in target.imported_ingredient_signature
        ],
        "solutions": [
            _solution(name, value, unit)
            for name, value, unit, _ in target.imported_solution_signature
        ],
        "media_term": {
            "preferred_term": "JCM Medium J773",
            "term": {"id": target.media_term, "label": repair_module.TITLE},
        },
        "notes": "Source: JCM",
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_corrects_shared_formula_and_leaves_review_ranking(
    repair_module,
    scorer_module,
) -> None:
    parsed = []
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(repair_module, target), target)
        parsed.append((str(target.path), repaired))

        assert repaired["medium_type"] == "COMPLEX"
        assert repaired["composition_type"] == "UNDEFINED"
        assert repaired["physical_state"] == "LIQUID"
        assert repaired["ph_value"] == 6.5
        assert (
            repair_module._signature(repaired["ingredients"], "ingredients")
            == repair_module.FINAL_INGREDIENT_SIGNATURE
        )
        assert (
            repair_module._solution_signature(repaired["solutions"], "solutions")
            == repair_module.FINAL_SOLUTION_SIGNATURE
        )
        assert scorer_module.score_record(repaired) == (0, [])

    assert scorer_module.score_parsed(parsed) == []


def test_repair_fixes_togo_m802_unit_slips(repair_module) -> None:
    target = repair_module.TARGETS[1]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert ingredients["Distilled water"]["concentration"] == {
        "value": "660.0",
        "unit": "ML_PER_L",
    }
    assert ingredients["CaCl2 x 2H2O"]["concentration"] == {
        "value": "8.0",
        "unit": "MG_PER_L",
    }
    assert ingredients["Resazurin"]["concentration"] == {
        "value": "1.0",
        "unit": "MG_PER_L",
    }
    assert ingredients["FeSO4 x 7H2O"]["concentration"] == {
        "value": "2.0",
        "unit": "MG_PER_L",
    }
    assert solutions["Rumen fluid, clarified (JCM Medium 266)"]["concentration"] == {
        "value": "300.0",
        "unit": "ML_PER_L",
    }


def test_repair_grounds_defined_components_and_gases(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["MgSO4 x 7H2O"]["term"] == {
        "id": "CHEBI:31795",
        "label": "magnesium sulfate heptahydrate",
    }
    assert ingredients["L-Cysteine HCl H2O"]["term"] == {
        "id": "CHEBI:91248",
        "label": "L-cysteine hydrochloride hydrate",
    }
    assert ingredients["Na2S x 9H2O"]["physicochemical_roles"] == ["REDUCING_AGENT"]
    assert ingredients["N2"]["mediaingredientmech_chebi_term"] == {
        "id": "CHEBI:17997",
        "label": "dinitrogen",
    }
    assert ingredients["Yeast extract (BD-Difco)"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert "term" not in ingredients["Trypticase peptone (BD-BBL)"]


def test_repair_preserves_external_solution_boundaries(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(repair_module, target), target)
    solutions = _by_name(repaired["solutions"])

    assert solutions["Rumen fluid, clarified (JCM Medium 266)"] == {
        "preferred_term": "Rumen fluid, clarified (JCM Medium 266)",
        "concentration": {"value": "300.0", "unit": "ML_PER_L"},
        "source": "JCM Medium 773 / JCM Medium 266",
        "notes": ("JCM Medium 773 adds 300.0 ml/L clarified rumen fluid from JCM Medium 266."),
        "composition": [],
    }
    assert all(solution["composition"] == [] for solution in repaired["solutions"])


def test_repair_adds_flags_references_and_event_once(repair_module) -> None:
    target = repair_module.TARGETS[-1]
    once = repair_module.repair_record(_doc(repair_module, target), target)
    twice = repair_module.repair_record(once, target)

    assert twice["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert twice["references"] == [
        {"reference": reference} for reference in repair_module.REFERENCES
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
    assert "TOGO g/L import artifacts" in matching_events[0]["notes"]


def test_plan_repairs_both_target_records(repair_module) -> None:
    assert repair_module.plan_repairs() == {
        repair_module.NORMALIZED
        / target.path: repair_module.repair_record(
            yaml.safe_load((repair_module.NORMALIZED / target.path).read_text(encoding="utf-8")),
            target,
        )
        for target in repair_module.TARGETS
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_media_term(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=target.media_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["ingredients"][0] = _ingredient("Tap water", "660", "ML_PER_L")

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_repair_rejects_solution_drift(repair_module) -> None:
    target = repair_module.TARGETS[0]
    doc = _doc(repair_module, target)
    doc["solutions"][0] = _solution("Trace minerals", "300", "ML_PER_L")

    with pytest.raises(ValueError, match="solution signature drifted"):
        repair_module.repair_record(doc, target)


def test_corpus_records_match_repair_contract(repair_module) -> None:
    for target in repair_module.TARGETS:
        doc = yaml.safe_load((repair_module.NORMALIZED / target.path).read_text(encoding="utf-8"))

        assert doc["id"] == target.record_id
        assert repair_module._source_term_id(doc) == target.media_term
        assert repair_module._signature(doc["ingredients"], "ingredients") in (
            target.imported_ingredient_signature,
            repair_module.FINAL_INGREDIENT_SIGNATURE,
        )
        assert repair_module._solution_signature(doc["solutions"], "solutions") in (
            target.imported_solution_signature,
            repair_module.FINAL_SOLUTION_SIGNATURE,
        )
