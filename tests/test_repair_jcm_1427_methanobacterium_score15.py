from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_1427_methanobacterium_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_jcm_1427_methanobacterium_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_1427")


def _doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "modified_methanobacterium_medium",
        "original_name": "MODIFIED METHANOBACTERIUM MEDIUM",
        "category": "archaea",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "JCM Medium J1427",
            "term": {"id": repair.EXPECTED_SOURCE_TERM, "label": "JCM 1427"},
        },
        "notes": "Source: JCM",
        "ingredients": [
            {"preferred_term": preferred_term} for preferred_term in repair.OLD_SIGNATURE
        ],
        "curation_history": [],
    }


def _solution(doc: dict, preferred_term: str) -> dict:
    for solution in doc["solutions"]:
        if solution["preferred_term"] == preferred_term:
            return solution
    raise AssertionError(f"missing {preferred_term!r}")


def test_repair_moves_stock_wrappers_to_solutions(repair_module, scorer_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "KH2PO4",
        "MgSO4 x 7H2O",
        "NaCl",
        "NH4Cl",
        "CaCl2 x 2H2O",
        "Brain heart infusion (BD Difico)",
        "Proteose peptone (BD Difico)",
        "Yeast extract (Oxoid)",
        "Sodium acetate",
        "Sodium formate",
        "Resazurin",
        "Distilled water",
    ]
    assert [row["preferred_term"] for row in repaired["solutions"]] == [
        "FeCl2 solution",
        "Trace element solution",
        "Rumen fluid, clarified",
        "Vitamin solution",
        "8% NaHCO3 solution",
        "5% Na2S x 9H2O solution",
        "5% L-Cysteine x HCl x H2O solution",
    ]
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_repair_expands_referenced_stock_compositions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    trace = _solution(repaired, "Trace element solution")
    assert len(trace["composition"]) == 8
    assert trace["composition"][5] == {
        "preferred_term": "NiCl2 x 6H2O",
        "source": "JCM Medium 187",
        "notes": "JCM Medium 187 prints this component in its stock solution.",
        "concentration": {"value": "24.0", "unit": "MG_PER_L"},
        "term": {"id": "CHEBI:53542", "label": "nickel chloride hexahydrate"},
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:53542",
            "label": "nickel chloride hexahydrate",
        },
    }

    vitamins = _solution(repaired, "Vitamin solution")
    assert len(vitamins["composition"]) == 8
    assert vitamins["composition"][0]["term"] == {
        "id": "CHEBI:176843",
        "label": "vitamin B12",
    }


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.JCM_1427},
        {"reference": repair_module.JCM_187},
        {"reference": repair_module.JCM_266},
        {"reference": repair_module.JCM_898},
    ]
    assert repaired["curation_history"][-1] == {
        "timestamp": repair_module.TIMESTAMP,
        "curator": repair_module.CURATOR,
        "action": repair_module.ACTION,
        "source": repair_module.JCM_1427,
        "notes": (
            "Moved JCM 1427 stock-solution and cross-reference wrappers into "
            "structured solutions backed by JCM 187, 266, and 898."
        ),
    }


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    path = tmp_path / repair_module.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(_doc(repair_module), sort_keys=False),
        encoding="utf-8",
    )

    first = repair_module.plan_repairs(tmp_path)
    for repaired_path, doc in first.items():
        repaired_path.write_text(repair_module.dump_record(doc), encoding="utf-8")

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
    doc["media_term"]["term"]["id"] = "jcm.grmd:187"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_SOURCE_TERM):
        repair_module.repair_record(doc)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc)
