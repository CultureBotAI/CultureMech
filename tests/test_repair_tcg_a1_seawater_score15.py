from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_tcg_a1_seawater_score15.py"
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
    return _load_script(SCRIPT, "repair_tcg_a1_seawater_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_tcg_a1")


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
            for preferred_term, value, unit in target.imported_signatures[0]
        ],
        "curation_history": [],
    }


def _by_name(doc: dict) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in doc["ingredients"]}


def test_all_targets_leave_review_ranking(repair_module, scorer_module) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(target), target)

        assert scorer_module.score_parsed([(target.path, repaired)]) == []


def test_tcg_family_removes_undocumented_agar_from_dsmz_records(repair_module) -> None:
    for path in (
        "bacterial/tcg_medium.yaml",
        "bacterial/KOMODO_1009_TCG_medium.yaml",
    ):
        target = repair_module.TARGET_BY_PATH[path]
        repaired = repair_module.repair_record(_doc(target), target)

        assert repaired["physical_state"] == "LIQUID"
        by_name = _by_name(repaired)
        assert "Agar" not in by_name
        assert by_name["Seawater (see below)"]["concentration"] == {
            "value": "1000",
            "unit": "ML_PER_L",
        }


def test_tcg_agar_records_keep_jcm_solid_formula(repair_module) -> None:
    for path in (
        "bacterial/JCM_J720_TCG_MEDIUM.yaml",
        "bacterial/TOGO_M743_TCG_Medium.yaml",
    ):
        target = repair_module.TARGET_BY_PATH[path]
        repaired = repair_module.repair_record(_doc(target), target)
        by_name = _by_name(repaired)

        assert repaired["physical_state"] == "SOLID_AGAR"
        assert by_name["Agar"]["concentration"] == {"value": "15", "unit": "G_PER_L"}
        assert by_name["Artificial seawater"]["concentration"] == {
            "value": "1000",
            "unit": "ML_PER_L",
        }
        assert "term" not in by_name["Tryptone (BD-Difco)"]
        assert "term" not in by_name["Casitone (BD-Difco)"]


def test_a1_records_ground_generic_yeast_only(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/KOMODO_1054_A1-MEDIUM.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)
    by_name = _by_name(repaired)

    assert by_name["Yeast extract"]["term"] == {
        "id": "FOODON:03315426",
        "label": "yeast extract",
    }
    assert "term" not in by_name["Bacto peptone"]
    assert "term" not in by_name["Seawater (Biomaris 089, natural or artificial)"]
    assert by_name["Seawater (Biomaris 089, natural or artificial)"]["concentration"] == {
        "value": "1000",
        "unit": "ML_PER_L",
    }


def test_variant_links_are_reciprocal(repair_module) -> None:
    tcg_jcm = repair_module.repair_record(
        _doc(repair_module.TARGET_BY_PATH["bacterial/JCM_J720_TCG_MEDIUM.yaml"]),
        repair_module.TARGET_BY_PATH["bacterial/JCM_J720_TCG_MEDIUM.yaml"],
    )
    tcg_dsmz = repair_module.repair_record(
        _doc(repair_module.TARGET_BY_PATH["bacterial/tcg_medium.yaml"]),
        repair_module.TARGET_BY_PATH["bacterial/tcg_medium.yaml"],
    )
    tcg_komodo = repair_module.repair_record(
        _doc(repair_module.TARGET_BY_PATH["bacterial/KOMODO_1009_TCG_medium.yaml"]),
        repair_module.TARGET_BY_PATH["bacterial/KOMODO_1009_TCG_medium.yaml"],
    )
    a1 = repair_module.repair_record(
        _doc(repair_module.TARGET_BY_PATH["bacterial/a1_medium.yaml"]),
        repair_module.TARGET_BY_PATH["bacterial/a1_medium.yaml"],
    )

    assert tcg_jcm["parent_media"]["id"] == "CultureMech:000425"
    assert tcg_jcm["variant_relationship"] == "SUPPLEMENTED_VARIANT"
    assert tcg_dsmz["variant_children"] == [
        {
            "path": "data/normalized_yaml/bacterial/JCM_J720_TCG_MEDIUM.yaml",
            "relationship": "SUPPLEMENTED_VARIANT",
            "id": "CultureMech:003065",
            "name": "tcg_medium",
            "notes": "JCM Medium 720 adds 15 g/L agar to DSMZ Medium 1009's liquid base.",
        },
        {
            "path": "data/normalized_yaml/bacterial/KOMODO_1009_TCG_medium.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:003514",
            "name": "tcg_medium",
            "notes": "KOMODO Medium 1009 points to the same DSMZ Medium 1009 formulation.",
        },
    ]
    assert tcg_komodo["parent_media"]["id"] == "CultureMech:000425"
    assert tcg_komodo["variant_relationship"] == "SOURCE_DUPLICATE"
    assert a1["variant_children"] == [
        {
            "path": "data/normalized_yaml/bacterial/KOMODO_1054_A1-MEDIUM.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:003630",
            "name": "a1_medium",
            "notes": "KOMODO Medium 1054 points to the same DSMZ Medium 1054 formulation.",
        }
    ]


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/tcg_medium.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [{"reference": repair_module.DSMZ_1009}]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.DSMZ_1009,
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
    target = repair_module.TARGET_BY_PATH["bacterial/tcg_medium.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/tcg_medium.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:wrong"

    with pytest.raises(ValueError, match=target.source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/tcg_medium.yaml"]
    doc = _doc(target)
    doc["ingredients"][0]["concentration"]["value"] = "4"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, target)


def test_target_records_match_reviewed_inputs(repair_module) -> None:
    for target in repair_module.TARGETS:
        doc = yaml.safe_load((repair_module.NORMALIZED / target.path).read_text(encoding="utf-8"))

        assert doc["id"] == target.record_id
        assert repair_module._signature(doc["ingredients"], "ingredients") in {
            *target.imported_signatures,
            repair_module._recipe_signature(target.ingredients),
        }
