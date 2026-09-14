from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_1305_helicobacter_score15.py"
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
    return _load_script(SCRIPT, "repair_jcm_1305_helicobacter_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_1305_helicobacter")


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": Path(target.path).stem,
        "original_name": Path(target.path).stem,
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
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


def test_repair_normalizes_source_batch_and_degrounds_stocks(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module.JCM_TARGET), repair_module.JCM_TARGET)
    by_name = _by_name(repaired)

    assert by_name["Brucella broth (BD-BBL)"]["concentration"] == {
        "value": "28",
        "unit": "G_PER_L",
    }
    assert by_name["Distilled water"]["concentration"] == {
        "value": "800",
        "unit": "ML_PER_L",
    }
    assert by_name["Conc. HCl"]["concentration"] == {
        "value": "1.35",
        "unit": "ML_PER_L",
    }
    assert by_name["Fetal bovine serum (Biowest; heat inactivated)"]["concentration"] == {
        "value": "200",
        "unit": "ML_PER_L",
    }
    assert by_name["Amphotericin B (5 mg/ml DMSO)"]["concentration"] == {
        "value": "1",
        "unit": "ML_PER_L",
    }
    assert "term" not in by_name["Brucella broth (BD-BBL)"]
    assert "term" not in by_name["Fetal bovine serum (Biowest; heat inactivated)"]
    assert "term" not in by_name["Amphotericin B (5 mg/ml DMSO)"]


def test_repair_adds_incubation_conditions(repair_module) -> None:
    repaired = repair_module.repair_record(_doc(repair_module.JCM_TARGET), repair_module.JCM_TARGET)

    assert repaired["temperature_value"] == 37.0
    assert repaired["incubation_atmosphere"] == "MICROAEROPHILIC"
    assert repaired["aeration"] == "5% O2, 12% CO2, shaking at 50 rpm"
    assert repaired["culture_vessel"] == "25 cm2 polystyrene culture flask"
    assert "ph_value" not in repaired


def test_togo_record_is_linked_as_jcm_source_duplicate(repair_module) -> None:
    jcm = repair_module.repair_record(_doc(repair_module.JCM_TARGET), repair_module.JCM_TARGET)
    togo = repair_module.repair_record(_doc(repair_module.TOGO_TARGET), repair_module.TOGO_TARGET)

    assert jcm["variant_children"] == [
        {
            "path": "data/normalized_yaml/bacterial/TOGO_M1402_Helicobacter_Medium.yaml",
            "relationship": "SOURCE_DUPLICATE",
            "id": "CultureMech:007939",
            "name": "helicobacter_medium",
            "notes": "TOGO M1402 mirrors the same JCM Medium 1305 formula.",
        }
    ]
    assert togo["parent_media"] == {
        "path": "data/normalized_yaml/bacterial/JCM_J1305_HELICOBACTER_MEDIUM.yaml",
        "relationship": "SOURCE_DUPLICATE",
        "id": "CultureMech:002469",
        "name": "helicobacter_medium",
        "notes": "TOGO M1402 mirrors the same JCM Medium 1305 formula.",
    }
    assert togo["variant_relationship"] == "SOURCE_DUPLICATE"


def test_repair_adds_flags_references_and_history(repair_module) -> None:
    repaired = repair_module.repair_record(
        _doc(repair_module.TOGO_TARGET), repair_module.TOGO_TARGET
    )

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.TOGO_M1402},
        {"reference": repair_module.JCM_1305},
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": f"{repair_module.TOGO_M1402}; {repair_module.JCM_1305}",
            "notes": repair_module.TOGO_NOTES,
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
    doc = _doc(repair_module.JCM_TARGET)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=repair_module.JCM_TARGET.record_id):
        repair_module.repair_record(doc, repair_module.JCM_TARGET)


def test_repair_rejects_wrong_source(repair_module) -> None:
    doc = _doc(repair_module.JCM_TARGET)
    doc["media_term"]["term"]["id"] = "mediadive.medium:wrong"

    with pytest.raises(ValueError, match=repair_module.JCM_TARGET.source_term):
        repair_module.repair_record(doc, repair_module.JCM_TARGET)


def test_repair_rejects_component_drift(repair_module) -> None:
    doc = _doc(repair_module.JCM_TARGET)
    doc["ingredients"][0]["concentration"]["value"] = "27"

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(doc, repair_module.JCM_TARGET)


def test_target_records_match_reviewed_inputs(repair_module) -> None:
    for target in repair_module.TARGETS:
        doc = yaml.safe_load((repair_module.NORMALIZED / target.path).read_text(encoding="utf-8"))

        assert doc["id"] == target.record_id
        assert repair_module._signature(doc["ingredients"]) in {
            target.imported_signature,
            repair_module.FINAL_SIGNATURE,
        }
