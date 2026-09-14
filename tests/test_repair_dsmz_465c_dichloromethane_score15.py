from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_465c_dichloromethane_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_465c_dichloromethane_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_465c")


def _doc(repair, path: str) -> dict:
    return {
        "id": repair.EXPECTED_IDS[path],
        "name": Path(path).stem,
        "original_name": "For DSM 6813",
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
        "notes": "Commercial Product: Tryptic Soy Broth (TSB) / Tryptic Soy Agar (TSA)",
        "ingredients": [
            {
                "preferred_term": "Peptone",
                "concentration": {
                    "value": "5",
                    "unit": "G_PER_L",
                },
            },
            {
                "preferred_term": "Agar",
                "concentration": {
                    "value": "65.0",
                    "unit": "G_PER_L",
                },
                "notes": "[Merged 4 duplicates: 15.0, 15.0, 20.0, 15.0]",
            },
            {
                "preferred_term": "Biphenyl contaminant",
                "concentration": {
                    "value": "0.5",
                    "unit": "G_PER_L",
                },
            },
        ],
        "curation_history": [],
    }


def _komodo_465_doc(repair) -> dict:
    doc = _doc(repair, repair.KOMODO_465)
    doc["original_name"] = "MINERAL MEDIUM PH 7.25"
    doc["variant_children"] = [
        {
            "path": f"data/normalized_yaml/{repair.KOMODO_465C_1}",
            "relationship": "SOURCE_DUPLICATE",
            "id": repair.EXPECTED_IDS[repair.KOMODO_465C_1],
            "name": Path(repair.KOMODO_465C_1).stem,
        },
        {
            "path": "data/normalized_yaml/bacterial/for_dsm_9675_and_dsm_9685.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:005572",
            "name": "for_dsm_9675_and_dsm_9685",
        },
    ]
    return doc


def _by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_official_dilutes_sl4_to_one_ml_per_liter(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.DSMZ_465C),
        repair_module.TARGET_BY_PATH[repair_module.DSMZ_465C],
    )
    ingredients = _by_name(repaired)

    assert len(ingredients) == 14
    assert "Bromothymol blue" not in ingredients
    assert ingredients["Na2-EDTA"]["concentration"] == {
        "value": "0.0005",
        "unit": "G_PER_L",
    }
    assert ingredients["FeSO4 x 7 H2O"]["concentration"] == {
        "value": "0.0002",
        "unit": "G_PER_L",
    }
    assert repaired["medium_type"] == "DEFINED"
    assert repaired["composition_type"] == "DEFINED"
    assert repaired["physical_state"] == "LIQUID"
    assert repaired["ph_value"] == 7.25
    assert repaired["variant_children"][0]["path"].endswith(
        "KOMODO_465c_MINERAL_MEDIUM_WITH_DICHLOROMETHANE.yaml"
    )


def test_komodo_465c_replaces_contaminated_rows(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.KOMODO_465C),
        repair_module.TARGET_BY_PATH[repair_module.KOMODO_465C],
    )
    ingredients = _by_name(repaired)

    assert len(ingredients) == 15
    assert not {"Peptone", "Agar", "Biphenyl contaminant"} & set(ingredients)
    assert ingredients["Bromothymol blue"]["term"] == {
        "id": "CHEBI:86155",
        "label": "bromothymol blue",
    }
    assert ingredients["Bromothymol blue"]["concentration"] == {
        "value": "0.05",
        "unit": "G_PER_L",
    }
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert "Tryptic Soy" not in repaired["notes"]
    assert repaired["parent_media"] == repair_module.KOMODO_465C_PARENT
    assert repaired["variant_relationship"] == "SUPPLEMENTED_VARIANT"


def test_dsm_6813_uses_ten_ml_sl4_and_leaves_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.KOMODO_465C_1),
        repair_module.TARGET_BY_PATH[repair_module.KOMODO_465C_1],
    )
    ingredients = _by_name(repaired)

    assert ingredients["Na2-EDTA"]["concentration"] == {
        "value": "0.005",
        "unit": "G_PER_L",
    }
    assert ingredients["FeSO4 x 7 H2O"]["concentration"] == {
        "value": "0.002",
        "unit": "G_PER_L",
    }
    assert repaired["parent_media"] == repair_module.KOMODO_465C_1_PARENT
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert any("10 ml/L" in note for note in repaired["variant_modifications"])
    assert scorer_module.score_parsed([(repair_module.KOMODO_465C_1, repaired)]) == []


def test_repair_removes_only_stale_child_from_komodo_465(repair_module) -> None:
    repaired = repair_module.repair_komodo_465_parent(_komodo_465_doc(repair_module))

    assert [child["id"] for child in repaired["variant_children"]] == [
        "CultureMech:005572"
    ]
    assert repaired["curation_history"][0]["curator"] == repair_module.CURATOR


def test_refuses_unexpected_source_term(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.KOMODO_465C_1]
    doc = _doc(repair_module, target.path)
    doc["media_term"]["term"]["id"] = "komodo.medium:465c"

    with pytest.raises(ValueError, match="expected 'komodo.medium:465c.1'"):
        repair_module.repair_record(doc, target)


def test_plan_repairs_is_idempotent(tmp_path: Path, repair_module) -> None:
    root = tmp_path / "normalized_yaml"
    for target in repair_module.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(repair_module, target.path), sort_keys=False))

    komodo_465 = root / repair_module.KOMODO_465
    komodo_465.parent.mkdir(parents=True, exist_ok=True)
    komodo_465.write_text(
        yaml.safe_dump(_komodo_465_doc(repair_module), sort_keys=False)
    )

    for path, doc in repair_module.plan_repairs(root).items():
        path.write_bytes(repair_module.dump_record(doc).encode("utf-8"))

    assert repair_module.plan_repairs(root) == {
        path: yaml.load(path.read_text(), Loader=repair_module.YAML_LOADER)
        for path in sorted(root.rglob("*.yaml"))
    }
