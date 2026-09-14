from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_78b_treponema_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_78b_treponema_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_78b")


def _doc(repair, path: str) -> dict:
    return {
        "id": repair.EXPECTED_IDS[path],
        "name": Path(path).stem,
        "original_name": "For DSM 16260",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": "stale",
            "term": {
                "id": repair.EXPECTED_SOURCE_TERMS[path],
                "label": "stale",
            },
        },
        "notes": "stale",
        "ingredients": [
            {"preferred_term": "Agar", "concentration": {"value": "14.6341", "unit": "G_PER_L"}},
            {"preferred_term": "Vitamin K1", "concentration": {"value": "0.1", "unit": "G_PER_L"}},
            {"preferred_term": "Ethanol", "concentration": {"value": "959.5", "unit": "G_PER_L"}},
        ],
        "curation_history": [],
        "parent_media": {
            "path": "data/normalized_yaml/bacterial/KOMODO_78_CHOPPED_MEAT_medium.yaml",
            "relationship": "SOURCE_DUPLICATE",
        },
        "variant_relationship": "SOURCE_DUPLICATE",
    }


def _by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_komodo_78b_uses_current_treponema_table(repair_module, scorer_module) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.KOMODO_78B]

    repaired = repair_module.repair_target(_doc(repair_module, target.path), target)
    ingredients = _by_name(repaired)

    assert repaired["physical_state"] == "LIQUID"
    assert repaired["parent_media"]["id"] == repair_module.EXPECTED_IDS[repair_module.DSMZ_78B]
    assert len(repaired["variant_children"]) == 2
    assert len(repaired["ingredients"]) == 18
    assert ingredients["Casamino acid"]["concentration"] == {"value": "0.16", "unit": "G_PER_L"}
    assert ingredients["Na-pyruvate"]["term"] == {
        "id": "CHEBI:50144",
        "label": "sodium pyruvate",
    }
    assert "Agar" not in ingredients
    assert "Vitamin K1" not in ingredients
    assert "Ethanol" not in ingredients
    assert scorer_module.score_record(repaired) == (0, [])


def test_dsm_16260_adds_ribose_and_glucuronic_acid(repair_module, scorer_module) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.KOMODO_78B_1]

    repaired = repair_module.repair_target(_doc(repair_module, target.path), target)
    ingredients = _by_name(repaired)

    assert len(repaired["ingredients"]) == 20
    assert ingredients["Ribose"]["concentration"] == {"value": "1.91", "unit": "G_PER_L"}
    assert ingredients["Glucuronic acid"]["term"] == {
        "id": "CHEBI:4178",
        "label": "D-glucuronic acid",
    }
    assert repaired["parent_media"]["id"] == repair_module.EXPECTED_IDS[repair_module.KOMODO_78B]
    assert scorer_module.score_record(repaired) == (0, [])


def test_dsm_16369_uses_maltose_and_omits_pyruvate_branch(repair_module, scorer_module) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.KOMODO_78B_2]

    repaired = repair_module.repair_target(_doc(repair_module, target.path), target)
    ingredients = _by_name(repaired)

    assert len(repaired["ingredients"]) == 15
    assert ingredients["maltose"]["concentration"] == {"value": "1.93", "unit": "G_PER_L"}
    assert "KCl" not in ingredients
    assert "Na-pyruvate" not in ingredients
    assert "N-acetylglucosamine" not in ingredients
    assert "glutathione" not in ingredients
    assert scorer_module.score_record(repaired) == (0, [])


def test_official_78b_keeps_only_main_liquid_recipe_components(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.DSMZ_78B]

    repaired = repair_module.repair_target(_doc(repair_module, target.path), target)
    ingredients = _by_name(repaired)

    assert repaired["ph_value"] == 7.0
    assert len(repaired["ingredients"]) == 6
    assert ingredients["Ground beef"]["concentration"] == {"value": "487.805", "unit": "G_PER_L"}
    assert "Haemin" not in ingredients
    assert "Vitamin K3" not in ingredients


def test_removes_78b_children_from_old_komodo_78_parent(repair_module) -> None:
    doc = _doc(repair_module, repair_module.KOMODO_78)
    doc["variant_children"] = [
        {"path": "data/normalized_yaml/bacterial/KOMODO_78b_medium_FOR_TREPONEMA_PARVUM.yaml"},
        {"path": "data/normalized_yaml/bacterial/for_dsm_16260.yaml"},
        {"path": "data/normalized_yaml/bacterial/for_dsm_16369.yaml"},
        {"path": "data/normalized_yaml/bacterial/medium_78_modified_for_dsm_1396.yaml"},
    ]

    repaired = repair_module.repair_komodo_78_parent(doc)

    assert repaired["variant_children"] == [
        {"path": "data/normalized_yaml/bacterial/medium_78_modified_for_dsm_1396.yaml"},
    ]


def test_refuses_unexpected_source_term(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.KOMODO_78B]
    doc = _doc(repair_module, target.path)
    doc["media_term"]["term"]["id"] = "komodo.medium:78"

    with pytest.raises(ValueError, match="expected 'komodo.medium:78b'"):
        repair_module.repair_target(doc, target)


def test_script_is_idempotent_on_minimal_tree(tmp_path: Path, repair_module) -> None:
    root = tmp_path / "normalized_yaml"
    for target in repair_module.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(repair_module, target.path), sort_keys=False))

    parent_path = root / repair_module.KOMODO_78
    parent_path.parent.mkdir(parents=True, exist_ok=True)
    parent = _doc(repair_module, repair_module.KOMODO_78)
    parent["variant_children"] = [
        {"path": "data/normalized_yaml/bacterial/KOMODO_78b_medium_FOR_TREPONEMA_PARVUM.yaml"},
    ]
    parent_path.write_text(yaml.safe_dump(parent, sort_keys=False))

    for path, doc in repair_module.plan_repairs(root).items():
        path.write_bytes(repair_module.dump_record(doc).encode("utf-8"))

    assert repair_module.plan_repairs(root) == {
        path: yaml.load(path.read_text(), Loader=repair_module.YAML_LOADER)
        for path in sorted(root.rglob("*.yaml"))
    }
