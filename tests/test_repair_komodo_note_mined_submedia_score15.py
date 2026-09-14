from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_note_mined_submedia_score15.py"
SCORER = REPO / "scripts" / "score_review_need.py"
RECORD_KINDS = REPO / "scripts" / "record_kinds.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_komodo_note_mined_submedia_score15")


@pytest.fixture(scope="module")
def scorer_module():
    return _load_script(SCORER, "score_review_need_for_note_mined_submedia")


@pytest.fixture(scope="module")
def record_kinds_module():
    return _load_script(RECORD_KINDS, "record_kinds_for_note_mined_submedia")


def _ingredient(name: str, value: str, unit: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": unit}}


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": target.path.stem,
        "original_name": target.path.stem,
        "category": "bacterial",
        "medium_type": "DEFINED",
        "composition_type": "DEFINED",
        "physical_state": "LIQUID",
        "notes": ("pH buffer: KOH | Source: KOMODO ModelSEED | ID: 3029 | " "SubMedium: Yes"),
        "media_term": {
            "preferred_term": "KOMODO Medium",
            "term": {"id": target.media_term, "label": target.path.stem},
        },
        "ingredients": [_ingredient(name, value, unit) for name, value, unit in target.signature],
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def test_repair_retypes_every_note_mined_submedium(
    repair_module,
    record_kinds_module,
    scorer_module,
) -> None:
    for target in repair_module.TARGETS:
        repaired = repair_module.repair_record(_doc(target), target)

        assert repaired["record_kind"] == "SOLUTION"
        assert record_kinds_module.is_solution_record(repaired)
        assert scorer_module.score_parsed([(str(target.path), repaired)]) == []


def test_repair_preserves_note_mined_buffer_row(
    repair_module,
) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(target), target)

    assert repair_module._signature(repaired["ingredients"], "ingredients") == (
        ("NaOH", "variable", "VARIABLE"),
    )


def test_repair_adds_event_once(
    repair_module,
) -> None:
    target = repair_module.TARGETS[1]
    once = repair_module.repair_record(_doc(target), target)
    twice = repair_module.repair_record(once, target)

    assert twice == once
    matching_events = [
        event
        for event in once["curation_history"]
        if (
            event.get("curator") == repair_module.CURATOR
            and event.get("action") == repair_module.ACTION
        )
    ]
    assert len(matching_events) == 1
    assert "SubMedium: Yes" in matching_events[0]["notes"]


def test_repair_rejects_non_submedium_record(
    repair_module,
) -> None:
    target = repair_module.TARGETS[2]
    doc = _doc(target)
    doc["notes"] = "Source: KOMODO ModelSEED"

    with pytest.raises(ValueError, match="expected SubMedium provenance"):
        repair_module.repair_record(doc, target)
