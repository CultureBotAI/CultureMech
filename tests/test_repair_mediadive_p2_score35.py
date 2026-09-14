from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load_repair():
    path = REPO_ROOT / "scripts" / "repair_mediadive_p2_score35.py"
    spec = importlib.util.spec_from_file_location(
        "repair_mediadive_p2_score35",
        path,
    )
    mod = importlib.util.module_from_spec(spec)
    sys.modules["repair_mediadive_p2_score35"] = mod
    spec.loader.exec_module(mod)
    return mod


def _minimal_doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "taiyang_medium_no_9_prototype",
        "original_name": "Taiyang Medium No.9 (prototype)",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.0,
        "temperature_value": {"value": 37, "unit": "CELSIUS"},
        "ingredients": [],
        "media_term": {
            "preferred_term": "public Medium P2",
            "term": {
                "id": repair.EXPECTED_SOURCE_TERM,
                "label": "Taiyang Medium No.9 (prototype)",
            },
        },
        "data_quality_flags": [
            "incomplete_composition",
            "needs_manual_curation",
        ],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _write_target(repair, root: Path) -> Path:
    path = root / repair.P2_TAIYANG
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_minimal_doc(repair), sort_keys=False), encoding="utf-8")
    return path


def _solution_by_name(doc: dict, name: str) -> dict:
    return next(
        solution
        for solution in doc["solutions"]
        if solution["preferred_term"] == name
    )


def _component_by_name(solution: dict, name: str) -> dict:
    return next(
        component
        for component in solution["composition"]
        if component["preferred_term"] == name
    )


def _ingredient_by_name(doc: dict, name: str) -> dict:
    return next(
        ingredient
        for ingredient in doc["ingredients"]
        if ingredient["preferred_term"] == name
    )


def test_plan_repairs_adds_taiyang_p2_recipe(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)

    plans = repair.plan_repairs(root)
    taiyang = plans[path]

    assert taiyang["physical_state"] == "SOLID_AGAR"
    assert "ph_value" not in taiyang
    assert "temperature_value" not in taiyang
    assert len(taiyang["ingredients"]) == 14
    assert [ingredient["preferred_term"] for ingredient in taiyang["ingredients"]] == [
        "Clarified rumen fluid",
        "Sheep blood",
        "Peptone",
        "Yeast extract",
        "NaCl",
        "Cellulose",
        "Pectin",
        "Starch",
        "Inulin",
        "Trehalose",
        "Sodium pyruvate",
        "dextrin",
        "L-Cysteine HCl",
        "Agar",
    ]

    assert _ingredient_by_name(taiyang, "Sodium pyruvate")["concentration"] == {
        "value": "1",
        "unit": "G_PER_L",
    }
    assert _ingredient_by_name(taiyang, "L-Cysteine HCl")["term"] == {
        "id": "CHEBI:91247",
        "label": "L-Cysteine HCl",
    }

    assert len(taiyang["solutions"]) == 2
    assert len(taiyang["preparation_steps"]) == 7
    assert taiyang["sterilization"] == {
        "method": "AUTOCLAVE",
        "notes": (
            "The main medium is autoclaved; trehalose, sodium pyruvate, "
            "L-Cysteine HCl, sheep blood, and Haemin solution are added after "
            "autoclaving."
        ),
    }


def test_plan_repairs_adds_artifical_sea_water_stock(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)

    taiyang = repair.plan_repairs(root)[path]
    asw = _solution_by_name(taiyang, "Artifical Sea Water")

    assert asw["concentration"] == {"value": "50", "unit": "ML_PER_L"}
    assert len(asw["composition"]) == 10
    assert _component_by_name(asw, "MgCl2 x 6 H2O") == {
        "preferred_term": "MgCl2 x 6 H2O",
        "concentration": {"value": "10.64", "unit": "G_PER_L"},
        "source": repair.SRC_P2,
        "term": {
            "id": "CHEBI:86345",
            "label": "magnesium dichloride hexahydrate",
        },
        "mediaingredientmech_chebi_term": {
            "id": "CHEBI:86345",
            "label": "magnesium dichloride hexahydrate",
        },
    }
    assert _component_by_name(asw, "NaHCO3")["concentration"] == {
        "value": "0.192",
        "unit": "G_PER_L",
    }
    assert _component_by_name(asw, "SrCl2")["term"] == {
        "id": "CHEBI:36383",
        "label": "strontium dichloride",
    }


def test_plan_repairs_adds_filter_sterilized_haemin_solution(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)

    taiyang = repair.plan_repairs(root)[path]
    haemin = _solution_by_name(taiyang, "Haemin solution")

    assert haemin["concentration"] == {"value": "10", "unit": "ML_PER_L"}
    assert _component_by_name(haemin, "Haemin")["concentration"] == {
        "value": "0.5",
        "unit": "G_PER_L",
    }
    assert _component_by_name(haemin, "NaOH (1 N)")["concentration"] == {
        "value": "10",
        "unit": "ML_PER_L",
    }
    assert taiyang["preparation_steps"][2]["action"] == "FILTER_STERILIZE"


def test_plan_repairs_adds_review_metadata_once(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)

    first = repair.plan_repairs(root)
    path.write_text(yaml.safe_dump(first[path], sort_keys=False), encoding="utf-8")

    second = repair.plan_repairs(root)
    taiyang = second[path]

    assert second == first
    assert taiyang["data_quality_flags"] == [
        "ingredients_curated",
        "has_ontology_mappings",
        "has_unmapped_ingredients",
    ]
    assert taiyang["references"] == [{"reference": repair.P2_PUBLIC}]
    assert "not curated/tested" in taiyang["notes"]

    matching_events = [
        event
        for event in taiyang["curation_history"]
        if (
            event.get("curator") == repair.CURATOR
            and event.get("action") == repair.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert matching_events[0]["source"] == repair.P2_PUBLIC


def test_repaired_record_has_only_norm_level_review_need(tmp_path: Path):
    repair = _load_repair()
    import score_review_need

    root = tmp_path / "normalized"
    path = _write_target(repair, root)

    taiyang = repair.plan_repairs(root)[path]

    assert score_review_need.score_record(taiyang) == (
        5,
        ["no pH and no temperature"],
    )
    assert (
        score_review_need.score_parsed(
            [(repair.P2_TAIYANG, taiyang)],
        )
        == []
    )


def test_plan_repairs_rejects_unexpected_target_id(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)
    doc = _minimal_doc(repair)
    doc["id"] = "CultureMech:wrong"
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    with pytest.raises(ValueError, match="expected 'CultureMech:010432'"):
        repair.plan_repairs(root)


def test_plan_repairs_rejects_unexpected_source_term(tmp_path: Path):
    repair = _load_repair()
    root = tmp_path / "normalized"
    path = _write_target(repair, root)
    doc = _minimal_doc(repair)
    doc["media_term"]["term"]["id"] = "mediadive.medium:P9"
    path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    with pytest.raises(ValueError, match="expected 'mediadive.medium:P2'"):
        repair.plan_repairs(root)
