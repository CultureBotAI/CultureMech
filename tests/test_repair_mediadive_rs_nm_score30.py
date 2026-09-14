from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load_repair():
    path = REPO_ROOT / "scripts" / "repair_mediadive_rs_nm_score30.py"
    spec = importlib.util.spec_from_file_location(
        "repair_mediadive_rs_nm_score30",
        path,
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_mediadive_rs_nm_score30"] = mod
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "rs_medium_nutrient_medium_nm_component",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.0,
        "ingredients": [],
        "media_term": {
            "preferred_term": "public Medium P5",
            "term": {
                "id": repair.EXPECTED_SOURCE_TERM,
                "label": "RS Medium - Nutrient Medium (NM) Component",
            },
        },
        "data_quality_flags": ["incomplete_composition"],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _write_target(repair, root: Path) -> Path:
    path = root / repair.P5_RS_NM
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_minimal_doc(repair), sort_keys=False), encoding="utf-8")
    return path


def _solution_by_name(doc: dict, name: str) -> dict:
    return next(solution for solution in doc["solutions"] if solution["preferred_term"] == name)


def _component_by_name(solution: dict, name: str) -> dict:
    return next(
        component for component in solution["composition"] if component["preferred_term"] == name
    )


def test_plan_repairs_adds_rs_nm_recipe(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)

    plans = repair.plan_repairs(root)
    nm = plans[path]

    assert nm["medium_type"] == "DEFINED"
    assert nm["composition_type"] == "DEFINED"
    assert nm["ph_value"] == 7.0
    assert nm["salinity"] == "3.3%"
    assert nm["ingredients"] == []
    assert len(nm["solutions"]) == 6
    assert len(nm["preparation_steps"]) == 8

    nnm = _solution_by_name(nm, "RS Medium - Non-Nutrient Medium (NNM) Component")
    assert nnm["concentration"] == {"value": "558", "unit": "ML_PER_L"}
    assert nnm["culturemech_term"] == {
        "id": "CultureMech:010434",
        "label": "RS Medium - Non-Nutrient Medium (NNM) Component",
    }

    mix1 = _solution_by_name(nm, "Mix solution 1 (Si and Fe+EDTA)")
    assert mix1["concentration"] == {"value": "26.667", "unit": "ML_PER_L"}
    assert len(mix1["composition"]) == 4
    assert _component_by_name(mix1, "FeCl3 x 6 H2O")["concentration"] == {
        "value": "0.05448",
        "unit": "G_PER_L",
    }


def test_plan_repairs_flattens_mem_and_carbon_mix_components(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)

    nm = repair.plan_repairs(root)[path]
    mix4 = _solution_by_name(nm, "Mix solution 4 (Amino Acids)")
    mix5 = _solution_by_name(nm, "Mix solution 5 (Carbon Sources)")

    assert len(mix4["composition"]) == 21
    assert _component_by_name(mix4, "L-Alanine")["concentration"] == {
        "value": "0.040406",
        "unit": "G_PER_L",
    }

    assert len(mix5["composition"]) == 21
    assert _component_by_name(
        mix5,
        "RS Medium - Non-Nutrient Medium (NNM) Component",
    )["concentration"] == {
        "value": "136.5",
        "unit": "ML_PER_L",
    }
    assert _component_by_name(mix5, "Glycerol")["concentration"] == {
        "value": "1.134",
        "unit": "G_PER_L",
    }
    assert _component_by_name(mix5, "D-Xylose")["concentration"] == {
        "value": "7.264",
        "unit": "G_PER_L",
    }


def test_plan_repairs_adds_review_metadata_once(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)

    first = repair.plan_repairs(root)
    path.write_text(yaml.safe_dump(first[path], sort_keys=False), encoding="utf-8")

    second = repair.plan_repairs(root)
    nm = second[path]

    assert second == first
    assert nm["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert nm["references"] == [{"reference": repair.P5_PUBLIC}]

    matching_events = [
        event
        for event in nm["curation_history"]
        if (event.get("curator") == repair.CURATOR and event.get("action") == repair.ACTION)
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == repair.P5_PUBLIC


def test_plan_repairs_rejects_unexpected_target_id(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)
    doc = _minimal_doc(repair)
    doc["id"] = "CultureMech:wrong"
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    with pytest.raises(ValueError, match="expected 'CultureMech:010435'"):
        repair.plan_repairs(root)
