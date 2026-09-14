from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_479_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "thermodesulfovibrio_medium",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [],
        "media_term": {
            "preferred_term": "JCM Medium J479",
            "term": {"id": repair.EXPECTED_MEDIA_TERM, "label": "JCM Medium J479"},
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def test_jcm_479_repair_scores_only_norm_level_ph_signal() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_479_score20")
    scorer = _load_script(SCORER, "score_review_need_for_jcm_479")

    repaired = repair.repair_record(_minimal_doc(repair))

    assert scorer.score_record(repaired) == (5, ["no pH and no temperature"])


def test_jcm_479_expands_jcm_284_solution_a_without_yeast_extract() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_479_score20_values")

    repaired = repair.repair_record(_minimal_doc(repair))

    assert [ingredient["preferred_term"] for ingredient in repaired["ingredients"]] == [
        "KH2PO4",
        "MgCl2 x 6 H2O",
        "CaCl2 x 2 H2O",
        "NH4Cl",
        "NaHCO3",
        "Resazurin",
        "Distilled water",
    ]
    assert repaired["ingredients"][0]["concentration"] == {
        "value": "0.14",
        "unit": "G_PER_L",
    }
    assert repaired["ingredients"][4]["concentration"] == {
        "value": "2.5",
        "unit": "G_PER_L",
    }
    assert [solution["preferred_term"] for solution in repaired["solutions"]] == [
        "Trace vitamins solution",
        "Trace element solution",
        "Se/W solution",
        "Solution B",
        "Solution C",
        "3% L-Cysteine x HCl x H2O solution",
        "3% Na2S x 9H2O solution",
    ]
    assert repaired["solutions"][0]["concentration"] == {
        "value": "2.0",
        "unit": "ML_PER_L",
    }
    assert repaired["solutions"][0]["composition"][0] == {
        "preferred_term": "Biotin",
        "concentration": {"value": "0.0049", "unit": "G_PER_L"},
        "source": "JCM Medium 284 Trace vitamins solution",
        "notes": "JCM Medium 284 Trace vitamins solution lists 0.0049 g/L.",
        "term": {"id": "CHEBI:15956", "label": "biotin"},
        "mediaingredientmech_chebi_term": {"id": "CHEBI:15956", "label": "biotin"},
    }
    assert repaired["solutions"][3]["concentration"] == {
        "value": "50.0",
        "unit": "ML_PER_L",
    }
    assert repaired["solutions"][3]["composition"][0]["concentration"] == {
        "value": "44.0",
        "unit": "G_PER_L",
    }
    assert repaired["solutions"][4]["composition"][0]["concentration"] == {
        "value": "56.0",
        "unit": "G_PER_L",
    }
    assert repaired["solutions"][5]["composition"][0]["concentration"] == {
        "value": "30.0",
        "unit": "G_PER_L",
    }


def test_plan_repair_is_idempotent(tmp_path: Path) -> None:
    repair = _load_script(SCRIPT, "repair_jcm_479_score20_idempotent")
    root = tmp_path / "normalized"
    path = root / repair.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_minimal_doc(repair), sort_keys=False), encoding="utf-8")

    first = repair.plan_repair(root)
    for out_path, doc in first.items():
        out_path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    assert repair.plan_repair(root) == first
