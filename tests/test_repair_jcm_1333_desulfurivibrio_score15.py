from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_1333_desulfurivibrio_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_1333_desulfurivibrio_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_1333_desulfurivibrio")


def _doc(repair_module) -> dict:
    return {
        "id": repair_module.EXPECTED_ID,
        "name": "desulfurivibrio_ames2_medium",
        "original_name": "DESULFURIVIBRIO AMeS2 MEDIUM",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "JCM Medium J1333",
            "term": {
                "id": repair_module.EXPECTED_SOURCE_TERM,
                "label": "DESULFURIVIBRIO AMeS2 MEDIUM",
            },
        },
        "notes": "Source",
        "ingredients": [
            {
                "preferred_term": preferred_term,
                "concentration": {"value": value, "unit": unit},
            }
            for preferred_term, value, unit in repair_module.IMPORTED_INGREDIENT_SIGNATURE
        ],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_repair_leaves_review_ranking(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert scorer_module.score_parsed([(repair_module.TARGET, repaired)]) == []


def test_repair_splits_simple_stocks_into_solutions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    ingredients = _by_name(repaired["ingredients"])
    solutions = _by_name(repaired["solutions"])

    assert set(ingredients) == {"Na2CO3", "NaHCO3", "NaCl", "K2HPO4", "Sulfur"}
    assert "1 M MgCl2 solution" in solutions
    assert "1 M NH4Cl solution" in solutions
    assert solutions["1 M MgCl2 solution"]["composition"] == [
        {
            "preferred_term": "MgCl2",
            "concentration": {"value": "1", "unit": "MOLAR"},
            "source": repair_module.SOURCE,
            "notes": "Solute of the 1 M MgCl2 stock added by JCM Medium 1333.",
            "term": {"id": "CHEBI:6636", "label": "magnesium dichloride"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:6636",
                "label": "magnesium dichloride",
            },
        }
    ]
    assert solutions["1 M NH4Cl solution"]["composition"][0]["term"] == {
        "id": "CHEBI:31206",
        "label": "ammonium chloride",
    }


def test_repair_keeps_trace_stocks_opaque(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    for preferred_term in (
        "Trace element solution (JCM Medium 1079)",
        "Se/W solution (JCM Medium 852)",
        "Trace vitamins (JCM Medium 197)",
    ):
        assert preferred_term in solutions
        assert "composition" not in solutions[preferred_term]
        assert "term" not in solutions[preferred_term]


def test_repair_documents_conditional_sulfide_solution(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))
    solutions = _by_name(repaired["solutions"])

    sulfide = solutions["5% Na2S x 9H2O solution"]
    assert "conditionally" in sulfide["notes"]
    assert sulfide["composition"][0]["term"] == {
        "id": "CHEBI:76209",
        "label": "sodium sulfide nonahydrate",
    }
    assert (
        "If the inoculum does not contain sulfide"
        in repaired["preparation_steps"][-1]["description"]
    )


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.JCM_1333},
        {"reference": repair_module.JCM_1079},
        {"reference": repair_module.JCM_852},
        {"reference": repair_module.JCM_197},
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.JCM_1333,
            "notes": repair_module.NOTES,
        }
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    path = tmp_path / repair_module.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_doc(repair_module), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(tmp_path)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert {
        path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "jcm.grmd:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_SOURCE_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_component_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"][0]["concentration"]["value"] = "21.0"

    with pytest.raises(ValueError, match="ingredient/solution signature drifted"):
        repair_module.repair_record(doc)


def test_target_record_matches_reviewed_input(repair_module) -> None:
    doc = yaml.safe_load(
        (repair_module.NORMALIZED / repair_module.TARGET).read_text(encoding="utf-8")
    )

    assert doc["id"] == repair_module.EXPECTED_ID
    assert (
        repair_module._signature(doc["ingredients"], "ingredients"),
        repair_module._signature(doc.get("solutions"), "solutions"),
    ) in {
        (
            repair_module.IMPORTED_INGREDIENT_SIGNATURE,
            repair_module.IMPORTED_SOLUTION_SIGNATURE,
        ),
        (repair_module.FINAL_INGREDIENT_SIGNATURE, repair_module.FINAL_SOLUTION_SIGNATURE),
    }
