from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_1551_687_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_1551_687_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_1551_687")


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": Path(target.path).stem,
        "original_name": Path(target.path).stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "media_term": {
            "preferred_term": target.source_term,
            "term": {"id": target.source_term, "label": target.source_term},
        },
        "notes": "Source",
        "ingredients": [
            {
                "preferred_term": preferred_term,
                "concentration": {"value": value, "unit": unit},
            }
            for preferred_term, value, unit in target.imported_signature
        ],
        "curation_history": [],
    }


def _by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_all_targets_leave_review_ranking(repair_module, scorer_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(target), target)

        assert scorer_module.score_parsed([(target.path, repaired)]) == []


def test_dsmz_1551_restores_split_nacl_and_ph(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[
        "bacterial/948_oxoid_nutrient_broth_with_additonal_salt.yaml"
    ]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["ph_value"] == 7.2
    assert [
        (row["preferred_term"], row["concentration"])
        for row in repaired["ingredients"]
        if row["preferred_term"] == "NaCl"
    ] == [
        ("NaCl", {"value": "17.5", "unit": "G_PER_L"}),
        ("NaCl", {"value": "5", "unit": "G_PER_L"}),
    ]
    assert _by_name(repaired)["Distilled water"]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }


def test_dsmz_687_restores_water_and_blood_percentage(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)
    by_name = _by_name(repaired)

    assert by_name["Sterile defibrinated blood"]["concentration"] == {
        "value": "5",
        "unit": "PERCENT_V_V",
    }
    assert by_name["Sterile defibrinated blood"]["term"] == {
        "id": "UBERON:0000178",
        "label": "blood",
    }
    assert by_name["Deionized water"]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }
    assert "term" not in by_name["Bacto Panton (Peptone)"]
    assert "term" not in by_name["Bacto Bitone (Peptone)"]


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [{"reference": repair_module.DSMZ_687}]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.DSMZ_687,
            "notes": target.notes,
        }
    ]


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    for target in repair_module.TARGETS:
        path = tmp_path / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(target), sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(tmp_path)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(tmp_path)

    assert {
        path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(tmp_path): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:wrong"

    with pytest.raises(ValueError, match=target.source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/DSMZ_687_COLUMBIA_BLOOD_AGAR.yaml"]
    doc = _doc(target)
    doc["ingredients"][0]["concentration"]["value"] = "5"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_reviewed_inputs(repair_module) -> None:
    for target in repair_module.TARGETS:
        doc = yaml.safe_load((repair_module.NORMALIZED / target.path).read_text(encoding="utf-8"))

        assert doc["id"] == target.record_id
        assert repair_module._signature(doc["ingredients"], "ingredients") in {
            target.imported_signature,
            repair_module._recipe_signature(target),
        }
