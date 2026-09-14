from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_1199_ph_variants_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_komodo_1199_ph_variants")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_1199")


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": Path(target.path).stem,
        "original_name": "For DSM 19966" if target.ph_value else "K7 medium",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": f"KOMODO Medium {target.media_term_id.removeprefix('komodo.medium:')}",
            "term": {"id": target.media_term_id, "label": "K7 medium"},
        },
        "notes": "Source: KOMODO ModelSEED",
        "ingredients": [
            {
                "preferred_term": "Glucose",
                "term": {"id": "CHEBI:17234", "label": "glucose"},
            },
            {"preferred_term": "Yeast extract"},
            {"preferred_term": "Peptone"},
        ],
        "curation_history": [],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing {preferred_term!r}")


def test_repair_expands_parent_table_and_links_children(
    repair_module,
    scorer_module,
) -> None:
    parent = repair_module.TARGET_BY_PATH["bacterial/KOMODO_1199_K7_medium.yaml"]

    repaired = repair_module.repair_record(_doc(parent), parent)
    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "Yeast extract",
        "Distilled water",
        "Glucose",
        "Peptone",
    ]
    assert _ingredient(repaired, "Distilled water")["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert [child["relationship"] for child in repaired["variant_children"]] == [
        "PH_VARIANT",
        "PH_VARIANT",
    ]
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )


def test_repair_retypes_strain_children_as_ph_variants(
    repair_module,
    scorer_module,
) -> None:
    child = repair_module.TARGET_BY_PATH["bacterial/for_dsm_19966.yaml"]

    repaired = repair_module.repair_record(_doc(child), child)
    assert repaired["ph_value"] == 5.5
    assert repaired["parent_media"] == {
        "path": repair_module.PARENT_PATH,
        "relationship": "PH_VARIANT",
        "id": repair_module.PARENT_ID,
        "name": repair_module.PARENT_NAME,
    }
    assert repaired["variant_relationship"] == "PH_VARIANT"
    assert scorer_module.score_record(repaired) == (0, [])


def test_plan_repair_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    for target in repair_module.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(target), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(root)
    for repaired_path, doc in first.items():
        repaired_path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in second.items()
    } == {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in first.items()
    }


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/for_dsm_19966.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/for_dsm_19966.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "komodo.medium:1199"

    with pytest.raises(ValueError, match=target.media_term_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/for_dsm_19966.yaml"]
    doc = _doc(target)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)
