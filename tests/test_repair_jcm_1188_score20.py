from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_1188_score20.py"
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
        "name": "marine_chloroflexi_medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [],
        "media_term": {
            "preferred_term": "TOGO Medium M1273",
            "term": {"id": repair.EXPECTED_MEDIA_TERM, "label": "Marine Chloroflexi"},
        },
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def test_jcm_1188_repair_scores_zero() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_1188_score20")
    scorer = _load_script(SCORER, "score_review_need_for_jcm_1188")

    repaired = repair.repair_record(_minimal_doc(repair))

    assert scorer.score_record(repaired) == (0, [])


def test_jcm_1188_rebuilds_current_official_formula() -> None:
    repair = _load_script(SCRIPT, "repair_jcm_1188_score20_values")

    repaired = repair.repair_record(_minimal_doc(repair))

    assert [ingredient["preferred_term"] for ingredient in repaired["ingredients"]] == [
        "KH2PO4",
        "MgCl2 x 6 H2O",
        "CaCl2 x 2 H2O",
        "NH4Cl",
        "NaCl",
        "Yeast extract",
        "Peptone",
        "Distilled water",
    ]
    assert repaired["ingredients"][1]["concentration"] == {
        "value": "4.0",
        "unit": "G_PER_L",
    }
    assert repaired["ph_value"] == 7.0
    assert [solution["preferred_term"] for solution in repaired["solutions"]] == [
        "Trace vitamins solution",
        "Trace mineral solution",
        "Se/W solution",
        "1 M Sodium pyruvate",
        "8% NaHCO3 solution",
        "5% L-Cysteine x HCl x H2O solution",
        "5% Na2S x 9H2O solution",
    ]
    assert repaired["solutions"][3]["composition"] == [
        {
            "preferred_term": "Sodium pyruvate",
            "concentration": {"value": "1.0", "unit": "MOLAR"},
            "term": {"id": "CHEBI:50144", "label": "sodium pyruvate"},
            "mediaingredientmech_chebi_term": {
                "id": "CHEBI:50144",
                "label": "sodium pyruvate",
            },
        }
    ]
    assert repaired["solutions"][4]["composition"][0]["concentration"] == {
        "value": "80.0",
        "unit": "G_PER_L",
    }


def test_plan_repair_is_idempotent(tmp_path: Path) -> None:
    repair = _load_script(SCRIPT, "repair_jcm_1188_score20_idempotent")
    root = tmp_path / "normalized"
    path = root / repair.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_minimal_doc(repair), sort_keys=False), encoding="utf-8")

    first = repair.plan_repair(root)
    for out_path, doc in first.items():
        out_path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    assert repair.plan_repair(root) == first
