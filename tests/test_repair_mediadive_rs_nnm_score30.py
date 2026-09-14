from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load_repair():
    path = REPO_ROOT / "scripts" / "repair_mediadive_rs_nnm_score30.py"
    spec = importlib.util.spec_from_file_location(
        "repair_mediadive_rs_nnm_score30",
        path,
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_mediadive_rs_nnm_score30"] = mod
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "rs_medium_non_nutrient_medium_nnm_component",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.0,
        "ingredients": [],
        "media_term": {
            "preferred_term": "public Medium P4",
            "term": {
                "id": repair.EXPECTED_SOURCE_TERM,
                "label": "RS Medium - Non-Nutrient Medium (NNM) Component",
            },
        },
        "data_quality_flags": ["incomplete_composition"],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _write_target(repair, root: Path) -> Path:
    path = root / repair.P4_RS_NNM
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_minimal_doc(repair), sort_keys=False), encoding="utf-8")
    return path


def _ingredient_by_name(doc: dict, name: str) -> dict:
    return next(
        ingredient
        for ingredient in doc["ingredients"]
        if ingredient["preferred_term"] == name
    )


def test_plan_repairs_adds_rs_nnm_recipe(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)

    plans = repair.plan_repairs(root)
    nnm = plans[path]

    assert nnm["medium_type"] == "DEFINED"
    assert nnm["composition_type"] == "DEFINED"
    assert nnm["ph_value"] == 7.0
    assert nnm["salinity"] == "3.3%"
    assert len(nnm["ingredients"]) == 32
    assert len(nnm["preparation_steps"]) == 5
    assert _ingredient_by_name(nnm, "NaCl")["concentration"] == {
        "value": "26.9",
        "unit": "G_PER_L",
    }
    assert _ingredient_by_name(nnm, "NaBr")["concentration"] == {
        "value": "1.05",
        "unit": "MG_PER_L",
    }
    assert _ingredient_by_name(nnm, "AgNO3")["concentration"] == {
        "value": "0.002",
        "unit": "MICROG_PER_L",
    }
    assert _ingredient_by_name(nnm, "TiCl3")["concentration"] == {
        "value": "0.0013",
        "unit": "ML_PER_L",
    }


def test_plan_repairs_adds_review_metadata_once(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)

    first = repair.plan_repairs(root)
    path.write_text(yaml.safe_dump(first[path], sort_keys=False), encoding="utf-8")

    second = repair.plan_repairs(root)
    nnm = second[path]

    assert second == first
    assert nnm["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert nnm["references"] == [{"reference": repair.P4_PUBLIC}]

    matching_events = [
        event
        for event in nnm["curation_history"]
        if (
            event.get("curator") == repair.CURATOR
            and event.get("action") == repair.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == repair.P4_PUBLIC


def test_plan_repairs_rejects_unexpected_target_id(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)
    doc = _minimal_doc(repair)
    doc["id"] = "CultureMech:wrong"
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    with pytest.raises(ValueError, match="expected 'CultureMech:010434'"):
        repair.plan_repairs(root)
