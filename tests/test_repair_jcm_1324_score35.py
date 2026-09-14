from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_jcm_1324_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_jcm_1324_score35")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_jcm_1324")


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "jcm_medium_no_1324",
        "original_name": "JCM MEDIUM No. 1324",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "JCM Medium J1324",
            "term": {"id": target.source_term, "label": "JCM MEDIUM No. 1324"},
        },
        "notes": "Source: JCM",
        "ingredients": [],
        "curation_history": [],
        "data_quality_flags": [
            "incomplete_composition",
            "source_information_unavailable",
        ],
    }


def _ingredient(doc: dict, preferred_term: str) -> dict:
    for ingredient in doc["ingredients"]:
        if ingredient["preferred_term"] == preferred_term:
            return ingredient
    raise AssertionError(f"missing ingredient {preferred_term!r}")


def test_repair_expands_main_solution_1324(repair_module, scorer_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/jcm_medium_no_1324.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["medium_type"] == "DEFINED"
    assert repaired["composition_type"] == "DEFINED"
    assert repaired["ph_value"] == 6.8
    assert [row["preferred_term"] for row in repaired["ingredients"]] == [
        "Distilled water",
        "NH4Cl",
        "K2HPO4",
        "KH2PO4",
        "MgSO4 x 6 H2O",
        "CaCl2 x 2 H2O",
        "FeSO4 x 7 H2O",
        "Methanol",
    ]
    assert scorer_module.score_record(repaired) == (0, [])


def test_repair_corrects_imported_units(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/jcm_medium_no_1324.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert _ingredient(repaired, "Distilled water")["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert _ingredient(repaired, "Methanol")["concentration"] == {
        "value": "5",
        "unit": "ML_PER_L",
    }


def test_repair_grounds_defined_components(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/jcm_medium_no_1324.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert _ingredient(repaired, "MgSO4 x 6 H2O")["term"] == {
        "id": "CHEBI:32599",
        "label": "magnesium sulfate",
    }
    assert _ingredient(repaired, "FeSO4 x 7 H2O")["term"] == {
        "id": "CHEBI:75836",
        "label": "iron(2+) sulfate heptahydrate",
    }
    assert _ingredient(repaired, "Methanol")["term"] == {
        "id": "CHEBI:17790",
        "label": "methanol",
    }


def test_repair_preserves_preparation_notes(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/jcm_medium_no_1324.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["preparation_steps"][-1] == {
        "step_number": 4,
        "action": "MIX",
        "description": (
            "Add sterile methanol to a final concentration of 0.5% in the " "sterile medium."
        ),
    }


def test_repair_adds_references_and_history(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/jcm_medium_no_1324.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["data_quality_flags"] == [
        "has_ontology_mappings",
        "ingredients_curated",
    ]
    assert repaired["references"] == [{"reference": repair_module.JCM_1324}]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": repair_module.JCM_1324,
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
    target = repair_module.TARGET_BY_PATH["bacterial/jcm_medium_no_1324.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/jcm_medium_no_1324.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "mediadive.medium:J9999"

    with pytest.raises(ValueError, match=target.source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/jcm_medium_no_1324.yaml"]
    doc = _doc(target)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="component signature drifted"):
        repair_module.repair_record(doc, target)
