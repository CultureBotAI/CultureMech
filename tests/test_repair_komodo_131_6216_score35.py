from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_131_6216_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_komodo_131_6216")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_komodo_131_6216")


def _doc(repair) -> dict:
    return {
        "id": repair.EXPECTED_ID,
        "name": "medium_131_modified_for_dsm_6216",
        "original_name": "MEDIUM 131 MODIFIED FOR DSM 6216",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "KOMODO Medium 131_6216",
            "term": {
                "id": repair.EXPECTED_MEDIA_TERM,
                "label": "MEDIUM 131 MODIFIED FOR DSM 6216",
            },
        },
        "notes": "Source: KOMODO ModelSEED",
        "ingredients": [],
        "data_quality_flags": ["incomplete_composition"],
        "curation_history": [],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


def test_repair_record_expands_komodo_131_6216_table(
    repair_module,
    scorer_module,
) -> None:
    once = repair_module.repair_record(_doc(repair_module))
    twice = repair_module.repair_record(once)

    assert once == twice
    assert scorer_module.score_record(twice) == (0, [])
    assert len(once["ingredients"]) == 34
    assert once["ph_value"] == 7.2
    assert _ingredient(once, "Na-acetate")["concentration"] == {
        "value": "3.00",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Na2S x 9 H2O")["concentration"] == {
        "value": "1.47",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Vitamin B12")["concentration"] == {
        "value": "0.0000000980",
        "unit": "G_PER_L",
    }
    assert _ingredient(once, "Distilled water")["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }
    assert _ingredient(once, "H2")["concentration"] == {
        "value": "variable",
        "unit": "VARIABLE",
    }


def test_repair_record_adds_parent_relationship_references_and_flags(
    repair_module,
) -> None:
    repaired = repair_module.repair_record(_doc(repair_module))

    assert repaired["parent_media"] == {
        "path": repair_module.PARENT_PATH,
        "relationship": "STRAIN_SPECIFIC_VARIANT",
        "id": repair_module.PARENT_ID,
        "name": "methanobacterium_thermoautotrophicum_medium",
    }
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert repaired["references"] == [
        {"reference": repair_module.KOMODO_131_6216_URL},
        {"reference": repair_module.KOMODO_131_URL},
        {"reference": repair_module.DSMZ_131_URL},
    ]
    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]


def test_plan_repair_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    path = root / repair_module.TARGET
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(_doc(repair_module), sort_keys=False))

    first = repair_module.plan_repairs(root)
    for repaired_path, doc in first.items():
        repaired_path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(root): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_record_rejects_wrong_id(repair_module) -> None:
    doc = _doc(repair_module)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_ID):
        repair_module.repair_record(doc)


def test_repair_record_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module)
    doc["media_term"]["term"]["id"] = "komodo.medium:131"

    with pytest.raises(ValueError, match=repair_module.EXPECTED_MEDIA_TERM):
        repair_module.repair_record(doc)
