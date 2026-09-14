from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_dsmz_504_swm_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_dsmz_504_swm_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_dsmz_504")


def _target(repair, path: str):
    return repair.TARGET_BY_PATH[path]


def _doc(repair, target) -> dict:
    return {
        "id": repair.EXPECTED_IDS[target.path],
        "name": Path(target.path).stem,
        "original_name": target.source_label.replace("KOMODO Medium 504.4", "For DSM 12881"),
        "category": target.path.split("/", 1)[0],
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": target.source_label,
            "term": {
                "id": repair.EXPECTED_SOURCE_TERMS[target.path],
                "label": target.source_label,
            },
        },
        "notes": "Source: KOMODO ModelSEED | DSMZ Medium: 504",
        "ingredients": [
            {
                "preferred_term": "D-Glucose",
                "concentration": {"value": "2", "unit": "G_PER_L"},
                "term": {"id": "CHEBI:17634", "label": "D-glucose"},
            }
        ],
        "solutions": [
            {
                "preferred_term": "Trace element solution SL-10",
                "concentration": {"value": "1", "unit": "ML_PER_L"},
            }
        ],
        "curation_history": [],
    }


def _doc_with_solution_candidates(repair, target) -> dict:
    doc = _doc(repair, target)
    for solution in doc["solutions"]:
        solution.pop("concentration", None)
        solution["concentration_candidates"] = [
            {
                "value": "1",
                "unit": "ML_PER_L",
                "basis": "CROSS_MEDIUM_INFERENCE",
            }
        ]
        solution["preparation_notes"] = "not asserted"
    doc["solutions"].append(
        {
            "preferred_term": "Seven vitamins solution",
            "concentration_candidates": [
                {
                    "value": "1",
                    "unit": "ML_PER_L",
                    "basis": "CROSS_MEDIUM_INFERENCE",
                }
            ],
            "preparation_notes": "not asserted",
        }
    )
    return doc


def _write_minimal_tree(repair, root: Path) -> None:
    for target in repair.TARGETS:
        path = root / target.path
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(yaml.safe_dump(_doc(repair, target), sort_keys=False), encoding="utf-8")


def test_dsmz_504_parent_gains_komodo_children(repair_module) -> None:
    target = _target(repair_module, repair_module.DSMZ_504)

    repaired = repair_module.repair_record(_doc(repair_module, target), target)

    assert repaired["ph_range"] == {"min": 7.2, "max": 7.4}
    assert [step["action"] for step in repaired["preparation_steps"]] == [
        "AUTOCLAVE",
        "FILTER_STERILIZE",
        "ADJUST_PH",
    ]
    assert [child["path"] for child in repaired["variant_children"]] == [
        f"data/normalized_yaml/{path}"
        for path in (
            repair_module.KOMODO_504,
            repair_module.KOMODO_504_1,
            repair_module.KOMODO_504_2,
            repair_module.KOMODO_504_3,
            repair_module.KOMODO_504_4,
            repair_module.KOMODO_504_5,
            repair_module.KOMODO_504_6,
        )
    ]


def test_dsm_12881_becomes_curated_strain_variant(repair_module, scorer_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_504_4)
    original = _doc(repair_module, target)

    repaired = repair_module.repair_record(original, target)

    assert repaired["ingredients"] == original["ingredients"]
    assert repaired["solutions"][0]["concentration"] == {"value": "1", "unit": "ML_PER_L"}
    assert repaired["data_quality_flags"] == ["ingredients_curated", "has_ontology_mappings"]
    assert repaired["parent_media"]["path"] == (
        f"data/normalized_yaml/{repair_module.DSMZ_504}"
    )
    assert repaired["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert repaired["variant_modifications"] == [
        "Uses 2 g/L glucose and 0.5 g/L yeast extract for DSM 12881.",
    ]
    assert scorer_module.score_parsed([("bacterial/for_dsm_12881.yaml", repaired)]) == []


def test_variant_links_are_directional(repair_module) -> None:
    repaired = {
        target.path: repair_module.repair_record(_doc(repair_module, target), target)
        for target in repair_module.TARGETS
    }

    for path in (
        repair_module.KOMODO_504,
        repair_module.KOMODO_504_1,
        repair_module.KOMODO_504_2,
        repair_module.KOMODO_504_3,
        repair_module.KOMODO_504_4,
        repair_module.KOMODO_504_5,
        repair_module.KOMODO_504_6,
    ):
        assert repaired[path]["parent_media"]["path"] == f"data/normalized_yaml/{repair_module.DSMZ_504}"

    for path, doc in repaired.items():
        parent_media = doc.get("parent_media")
        if parent_media is not None:
            assert parent_media["path"] != f"data/normalized_yaml/{path}"


def test_dsm_6233_solution_candidates_are_resolved(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_504_2)

    repaired = repair_module.repair_record(
        _doc_with_solution_candidates(repair_module, target),
        target,
    )

    concentrations = {
        solution["preferred_term"]: solution["concentration"]
        for solution in repaired["solutions"]
    }
    assert concentrations == {
        "Trace element solution SL-10": {"value": "2", "unit": "ML_PER_L"},
        "Seven vitamins solution": {"value": "1", "unit": "ML_PER_L"},
    }
    assert all("concentration_candidates" not in solution for solution in repaired["solutions"])


def test_plan_repairs_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    _write_minimal_tree(repair_module, root)

    first = repair_module.plan_repairs(root)
    for path, doc in first.items():
        path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in second.items()
    } == {
        path.relative_to(root): repair_module.dump_record(doc)
        for path, doc in first.items()
    }


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = _target(repair_module, repair_module.KOMODO_504_4)
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "komodo.medium:504.5"

    with pytest.raises(ValueError, match="expected 'komodo.medium:504.4'"):
        repair_module.repair_record(doc, target)
