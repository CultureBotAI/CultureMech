from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_780_score20.py"
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
        "name": "patel_laboratory_medium_with_glycerin",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "ingredients": [],
        "media_term": {
            "preferred_term": "JCM Medium J780",
            "term": {"id": repair.EXPECTED_MEDIA_TERM, "label": "JCM Medium J780"},
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def test_jcm_780_repair_scores_zero() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_780_score20")
    scorer = _load_script(SCORER, "score_review_need_for_jcm_780")

    repaired = repair.repair_record(_minimal_doc(repair))

    assert scorer.score_record(repaired) == (0, [])


def test_jcm_780_rebuilds_full_final_liter_and_glycerin_stock() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_780_score20_values")

    repaired = repair.repair_record(_minimal_doc(repair))

    assert [ingredient["preferred_term"] for ingredient in repaired["ingredients"]] == [
        "NH4Cl",
        "K2HPO4",
        "KH2PO4",
        "MgCl2 x 6 H2O",
        "CaCl2 x 2 H2O",
        "NaCl",
        "HEPES",
        "Yeast extract",
        "Na2SO4",
        "Distilled water",
    ]
    assert repaired["ingredients"][1]["concentration"] == {
        "value": "0.6",
        "unit": "G_PER_L",
    }
    assert repaired["ingredients"][8]["concentration"] == {
        "value": "2.84",
        "unit": "G_PER_L",
    }
    assert repaired["ph_value"] == 7.0
    assert [solution["preferred_term"] for solution in repaired["solutions"]] == [
        "Trace vitamins",
        "Trace mineral solution",
        "20% (w/v) Glycerin solution",
    ]
    assert repaired["solutions"][2]["concentration"] == {
        "value": "10.0",
        "unit": "ML_PER_L",
    }
    assert repaired["solutions"][2]["composition"] == [
        {
            "preferred_term": "Glycerol",
            "concentration": {"value": "200.0", "unit": "G_PER_L"},
            "term": {"id": "CHEBI:17754", "label": "glycerol"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:17754",
                "label": "glycerol",
            },
        }
    ]


def test_plan_repair_is_idempotent(tmp_path: Path) -> None:
    repair = _load_script(SCRIPT, "repair_jcm_780_score20_idempotent")
    root = tmp_path / "normalized"
    path = root / repair.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_minimal_doc(repair), sort_keys=False), encoding="utf-8")

    first = repair.plan_repair(root)
    for out_path, doc in first.items():
        out_path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    assert repair.plan_repair(root) == first
