from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_195_desulfobacter_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_195_desulfobacter_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_195")


def _ingredient(name: str) -> dict:
    return {
        "preferred_term": name,
        "term": {
            "id": "CHEBI:32588",
            "label": "potassium chloride",
        },
        "concentration": {
            "value": "999",
            "unit": "G_PER_L",
        },
    }


def _doc(repair, path: str) -> dict:
    carbon_row = "Na-acetate x 3 H2O" if path == repair.DSMZ_195 else "Na-propionate"
    ingredient_names = [
        *repair.COMMON_FINAL_CONCENTRATIONS,
        "Na2CO3",
        carbon_row,
    ]
    return {
        "id": repair.EXPECTED_IDS[path],
        "name": Path(path).stem,
        "original_name": "For DSM 4661",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "stale",
            "term": {
                "id": repair.EXPECTED_SOURCE_TERMS[path],
                "label": "stale",
            },
        },
        "notes": "Source: KOMODO ModelSEED",
        "ingredients": [_ingredient(name) for name in ingredient_names],
        "curation_history": [],
    }


def _by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_official_dilutes_stocks_to_final_medium(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.DSMZ_195),
        repair_module.TARGET_BY_PATH[repair_module.DSMZ_195],
    )
    ingredients = _by_name(repaired)

    assert ingredients["Na2CO3"]["concentration"] == {
        "value": "1.49551",
        "unit": "G_PER_L",
    }
    assert ingredients["Na-acetate x 3 H2O"]["concentration"] == {
        "value": "2.49252",
        "unit": "G_PER_L",
    }
    assert ingredients["FeCl2 x 4 H2O"]["concentration"] == {
        "value": "0.00149551",
        "unit": "G_PER_L",
    }
    assert ingredients["Biotin"]["concentration"] == {
        "value": "0.0000199402",
        "unit": "G_PER_L",
    }
    assert repaired["ph_range"] == {"min": 7.1, "max": 7.4}
    assert repaired["parent_media"] == repair_module.DESULFOBACTER_MEDIUM_PARENT
    assert repaired["variant_relationship"] == "CONCENTRATION_VARIANT"
    assert repaired["variant_children"][0]["path"].endswith("desulfobacter_sp_medium.yaml")


def test_komodo_base_restores_bicarbonate_and_acetate(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.KOMODO_195),
        repair_module.TARGET_BY_PATH[repair_module.KOMODO_195],
    )
    ingredients = _by_name(repaired)

    assert "Na2CO3" not in ingredients
    assert "Na-propionate" not in ingredients
    assert ingredients["NaHCO3"]["concentration"] == {
        "value": "5.00",
        "unit": "G_PER_L",
    }
    assert ingredients["Na-acetate x 3 H2O"]["concentration"] == {
        "value": "2.50",
        "unit": "G_PER_L",
    }
    assert repaired["parent_media"] == repair_module.KOMODO_BASE_PARENT
    assert repaired["variant_relationship"] == "SUBSTITUTED_COMPONENT_VARIANT"


def test_dsm_4661_restores_resorcinol_and_leaves_ranking(
    repair_module,
    scorer_module,
) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module, repair_module.KOMODO_195_1),
        repair_module.TARGET_BY_PATH[repair_module.KOMODO_195_1],
    )
    ingredients = _by_name(repaired)

    assert "Na2CO3" not in ingredients
    assert "Na-propionate" not in ingredients
    assert ingredients["resorcinol"]["source"] == "KOMODO Medium 195.1"
    assert ingredients["resorcinol"]["concentration"] == {
        "value": "2.50",
        "unit": "G_PER_L",
    }
    assert scorer_module.score_parsed([(repair_module.KOMODO_195_1, repaired)]) == []


def test_variant_children_are_bidirectional(repair_module) -> None:
    repaired = {
        target.path: repair_module.repair_record(_doc(repair_module, target.path), target)
        for target in repair_module.TARGETS
    }

    assert [child["path"] for child in repaired[repair_module.DSMZ_195]["variant_children"]] == [
        f"data/normalized_yaml/{repair_module.KOMODO_195}",
        f"data/normalized_yaml/{repair_module.KOMODO_195_1}",
    ]
    for path in (repair_module.KOMODO_195, repair_module.KOMODO_195_1):
        assert (
            repaired[path]["parent_media"]["path"]
            == f"data/normalized_yaml/{repair_module.DSMZ_195}"
        )


def test_refuses_unexpected_source_term(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.KOMODO_195_1]
    doc = _doc(repair_module, target.path)
    doc["media_term"]["term"]["id"] = "komodo.medium:195"

    with pytest.raises(ValueError, match="expected 'komodo.medium:195.1'"):
        repair_module.repair_record(doc, target)


def test_plan_repairs_is_idempotent(tmp_path: Path, repair_module) -> None:
    root = tmp_path / "normalized_yaml"
    for target in repair_module.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(repair_module, target.path), sort_keys=False))

    for path, doc in repair_module.plan_repairs(root).items():
        path.write_bytes(repair_module.dump_record(doc).encode("utf-8"))

    assert repair_module.plan_repairs(root) == {
        path: yaml.load(path.read_text(), Loader=repair_module.YAML_LOADER)
        for path in sorted(root.rglob("*.yaml"))
    }
