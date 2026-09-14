from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_halomarina_jcm703_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_halomarina_jcm703_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_halomarina_jcm703")


def _doc(target) -> dict:
    media_term = "TOGO:M1943"
    if "methanobacterium" in target.path:
        media_term = "mediadive.medium:J703"

    return {
        "id": target.record_id,
        "name": Path(target.path).stem,
        "original_name": Path(target.path).stem,
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": target.source_term,
            "term": {"id": media_term, "label": target.source_term},
        },
        "notes": "Source: imported",
        "ingredients": [
            {"preferred_term": name}
            for name in next(iter(target.accepted_signatures))
            if "solution" not in name and not name.startswith("Trace ")
        ],
        "solutions": [
            {"preferred_term": name, "composition": []}
            for name in next(iter(target.accepted_signatures))
            if "solution" in name or name.startswith("Trace ")
        ],
        "curation_history": [],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc.get("ingredients") or doc.get("composition") or []:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


def _solution(doc: dict, preferred_term: str) -> dict:
    for solution in doc["solutions"]:
        if solution["preferred_term"] == preferred_term:
            return solution
    raise AssertionError(f"missing solution {preferred_term!r}")


def test_halomarina_uses_nbrc_1214_composition(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/halomarina_medium.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["ph_value"] == 7.5
    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "Casamino acids",
        "Bacto Yeast Extract (Difco)",
        "NaCl",
        "Agar",
        "Artificial seawater",
    ]
    assert _ingredient(repaired, "Artificial seawater")["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert _ingredient(repaired, "Bacto Yeast Extract (Difco)")["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert scorer_module.score_record(repaired) == (0, [])


def test_jcm703_expands_recovered_jcm_stocks(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/methanobacterium_medium_ii_with_formae.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["ph_value"] == 7.0
    assert [row["preferred_term"] for row in repaired["solutions"]] == [
        "Trace minerals (TOGO Medium M142)",
        "Trace vitamins (TOGO Medium M190)",
        "8% NaHCO3 solution",
        "3% Na2S x 9H2O solution",
    ]
    assert _ingredient(repaired, "CaCl2 x 2H2O")["term"] == {
        "id": "CHEBI:86158",
        "label": "calcium chloride dihydrate",
    }
    assert _ingredient(repaired, "Sodium formate")["concentration"] == {
        "value": "0.3",
        "unit": "PERCENT_W_V",
    }
    assert scorer_module.score_record(repaired) == (0, [])


def test_jcm703_inlines_m142_and_m190_solution_components(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/methanobacterium_medium_ii_with_formae.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    trace_minerals = _solution(repaired, "Trace minerals (TOGO Medium M142)")
    assert len(trace_minerals["composition"]) == 13
    assert _ingredient(trace_minerals, "MgSO4 x 7H2O")["concentration"] == {
        "value": "3",
        "unit": "G_PER_L",
    }

    trace_vitamins = _solution(repaired, "Trace vitamins (TOGO Medium M190)")
    assert len(trace_vitamins["composition"]) == 10
    assert _ingredient(trace_vitamins, "Vitamin B12")["term"] == {
        "id": "CHEBI:176843",
        "label": "vitamin B12",
    }


def test_jcm703_inlines_direct_stock_solution_components(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/methanobacterium_medium_ii_with_formae.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    bicarbonate = _solution(repaired, "8% NaHCO3 solution")
    assert bicarbonate["concentration"] == {"value": "25", "unit": "ML_PER_L"}
    assert bicarbonate["composition"] == [
        {
            "preferred_term": "NaHCO3",
            "concentration": {"value": "80", "unit": "G_PER_L"},
            "source": repair_module.SOURCE_JCM_703,
            "notes": ("JCM Medium 703 / TOGO M725 prints this component in its " "stock solution."),
            "term": {
                "id": "CHEBI:32139",
                "label": "sodium hydrogencarbonate",
            },
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:32139",
                "label": "sodium hydrogencarbonate",
            },
        }
    ]

    sulfide = _solution(repaired, "3% Na2S x 9H2O solution")
    assert _ingredient(sulfide, "Na2S x 9H2O")["concentration"] == {
        "value": "30",
        "unit": "G_PER_L",
    }


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/halomarina_medium.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.TOGO_M1943},
        {"reference": repair_module.NBRC_1214},
    ]
    assert repaired["curation_history"][-1] == {
        "timestamp": repair_module.TIMESTAMP,
        "curator": repair_module.CURATOR,
        "action": repair_module.ACTION,
        "source": f"{repair_module.TOGO_M1943}; {repair_module.NBRC_1214}",
        "notes": target.notes,
    }


def test_solution_compositions_are_flat_ingredients(repair_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(target), target)

        for solution in repaired.get("solutions", []):
            for component in solution.get("composition", []):
                assert "composition" not in component
                assert "preparation_notes" not in component


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    for target in repair_module.TARGETS:
        path = tmp_path / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(target), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(tmp_path)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert {
        path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/halomarina_medium.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/halomarina_medium.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=target.source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["archaea/halomarina_medium.yaml"]
    doc = _doc(target)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="component signature drifted"):
        repair_module.repair_record(doc, target)
