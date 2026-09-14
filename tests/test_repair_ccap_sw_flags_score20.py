from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_ccap_sw_flags_score20.py"
SCORER = REPO / "scripts" / "score_review_need.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_ccap_sw_flags")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_ccap_sw_flags")


def _doc(repair, *, record_id: str = "CultureMech:000136") -> dict:
    return {
        "id": record_id,
        "name": "s_w_amp",
        "original_name": "S/W + AMP",
        "category": "algae",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "BIPHASIC",
        "ph_range": {"min": 7.0, "max": 8.0},
        "notes": "Full recipe available at https://www.ccap.ac.uk/wp-content/uploads/MR_SW_AMP.pdf",
        "ingredients": [
            {"preferred_term": name} for name in repair.EXPECTED["algae/s_w_amp.yaml"][1]
        ],
        "curation_history": [{"action": repair.SOURCE_ACTION}],
    }


def test_repair_adds_sparse_flags_once(repair_module, scorer_module) -> None:
    once = repair_module.repair_record(
        "algae/s_w_amp.yaml",
        _doc(repair_module),
        *repair_module.EXPECTED["algae/s_w_amp.yaml"],
    )
    twice = repair_module.repair_record(
        "algae/s_w_amp.yaml",
        once,
        *repair_module.EXPECTED["algae/s_w_amp.yaml"],
    )

    assert once == twice
    assert once["data_quality_flags"] == [
        "has_unmapped_ingredients",
        "ingredients_curated",
    ]
    assert scorer_module.score_record(once) == (
        10,
        ["no media_term (untraceable to a source catalogue)"],
    )
    events = [
        event
        for event in twice["curation_history"]
        if event.get("curator") == repair_module.CURATOR
    ]
    assert len(events) == 1


def test_plan_repair_is_idempotent(repair_module, tmp_path: Path) -> None:
    root = tmp_path / "normalized"
    for relative_path, (expected_id, expected_ingredients) in repair_module.EXPECTED.items():
        path = root / relative_path
        path.parent.mkdir(parents=True, exist_ok=True)
        doc = _doc(repair_module, record_id=expected_id)
        doc["ingredients"] = [{"preferred_term": name} for name in expected_ingredients]
        path.write_text(yaml.safe_dump(doc, sort_keys=False), encoding="utf-8")

    first = repair_module.plan_repairs(root)
    for repaired_path, doc in first.items():
        repaired_path.write_text(repair_module.dump_record(doc), encoding="utf-8")

    second = repair_module.plan_repairs(root)

    assert {
        path.relative_to(root): repair_module.dump_record(doc) for path, doc in second.items()
    } == {path.relative_to(root): repair_module.dump_record(doc) for path, doc in first.items()}


def test_repair_rejects_wrong_id(repair_module) -> None:
    with pytest.raises(ValueError, match=repair_module.EXPECTED["algae/s_w_amp.yaml"][0]):
        repair_module.repair_record(
            "algae/s_w_amp.yaml",
            _doc(repair_module, record_id="CultureMech:wrong"),
            *repair_module.EXPECTED["algae/s_w_amp.yaml"],
        )


def test_repair_rejects_missing_source_repair_event(repair_module) -> None:
    doc = _doc(repair_module)
    doc["curation_history"] = []

    with pytest.raises(ValueError, match="missing reviewed CCAP PDF repair event"):
        repair_module.repair_record(
            "algae/s_w_amp.yaml",
            doc,
            *repair_module.EXPECTED["algae/s_w_amp.yaml"],
        )


def test_repair_rejects_ingredient_drift(repair_module) -> None:
    doc = _doc(repair_module)
    doc["ingredients"].pop()

    with pytest.raises(ValueError, match="ingredient signature drifted"):
        repair_module.repair_record(
            "algae/s_w_amp.yaml",
            doc,
            *repair_module.EXPECTED["algae/s_w_amp.yaml"],
        )
