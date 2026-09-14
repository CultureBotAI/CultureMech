from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_imk_porphyra_score35.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_imk_porphyra_score35")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_imk_porphyra")


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "imk_with_porphyra",
        "original_name": "IMK with Porphyra",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "TOGO Medium M1769",
            "term": {"id": target.source_term, "label": "IMK with Porphyra"},
        },
        "notes": "Source: https://togomedium.org/medium/M1769",
        "ingredients": [],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def test_repair_models_opaque_nbrc_984_composition(
    repair_module,
    scorer_module,
) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/imk_with_porphyra.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["ingredients"] == [
        {
            "preferred_term": ("Porphyra yezoensis thalli cultivated in IMK medium with seawater"),
            "concentration": {"value": "variable", "unit": "VARIABLE"},
            "source": repair_module.SOURCE,
            "notes": (
                "NBRC Medium 984 lists the disclosed composition as Thalli of "
                "Porphyra yezoensis cultivated in IMK medium (with seawater)."
            ),
        }
    ]
    assert scorer_module.score_record(repaired) == (
        5,
        ["no pH and no temperature"],
    )
    assert scorer_module.score_parsed([("bacterial/imk_with_porphyra.yaml", repaired)]) == []


def test_repair_adds_references_flags_and_history(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/imk_with_porphyra.yaml"]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repaired["data_quality_flags"] == [
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert repaired["references"] == [
        {"reference": repair_module.TOGO_M1769},
        {"reference": repair_module.NBRC_984},
    ]
    assert repaired["curation_history"] == [
        {
            "timestamp": repair_module.TIMESTAMP,
            "curator": repair_module.CURATOR,
            "action": repair_module.ACTION,
            "source": f"{repair_module.TOGO_M1769}; {repair_module.NBRC_984}",
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
    target = repair_module.TARGET_BY_PATH["bacterial/imk_with_porphyra.yaml"]
    doc = _doc(target)
    doc["id"] = "CultureMech:wrong"

    with pytest.raises(ValueError, match=target.record_id):
        repair_module.repair_record(doc, target)


def test_repair_rejects_wrong_source(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/imk_with_porphyra.yaml"]
    doc = _doc(target)
    doc["media_term"]["term"]["id"] = "TOGO:M9999"

    with pytest.raises(ValueError, match=target.source_term):
        repair_module.repair_record(doc, target)


def test_repair_rejects_component_drift(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH["bacterial/imk_with_porphyra.yaml"]
    doc = _doc(target)
    doc["ingredients"].append({"preferred_term": "unexpected"})

    with pytest.raises(ValueError, match="component signature drifted"):
        repair_module.repair_record(doc, target)
