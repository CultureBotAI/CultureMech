from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_togo_nbrc_water_ph_review_batch.py"


def _load_script(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return _load_script(SCRIPT, "repair_togo_nbrc_water_ph_review_batch")


def _ingredient(name: str, value: str, unit: str) -> dict:
    row = {"preferred_term": name, "concentration": {"value": value, "unit": unit}}
    if name in {"Carbon dioxide gas", "Nitrogen gas"}:
        row["notes"] = "Properties: gas"
    return row


def _doc(target) -> dict:
    return {
        "id": target.record_id,
        "name": "review_target",
        "original_name": "Review target",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ingredients": [
            _ingredient(name, value, unit) for name, value, unit in target.imported_signature
        ],
        "media_term": {"term": {"id": target.source_term, "label": "Review target"}},
        "applications": ["Microbial cultivation"],
        "curation_history": [],
    }


def _by_name(rows: list[dict]) -> dict[str, dict]:
    return {row["preferred_term"]: row for row in rows}


def test_m1797_restores_volumetric_water_and_ph_value(repair_module) -> None:
    target = repair_module.TARGETS[0]
    repaired = repair_module.repair_record(_doc(target), target)

    assert _by_name(repaired["ingredients"])["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert repaired["ph_value"] == 4.0
    assert "ph_range" not in repaired
    assert "variant_children" not in repaired


def test_m3041_restores_water_ph_and_child_link(repair_module) -> None:
    target = repair_module.TARGETS[1]
    doc = _doc(target)
    doc["physical_state"] = "SOLID_AGAR"

    repaired = repair_module.repair_record(doc, target)

    assert _by_name(repaired["ingredients"])["Distilled water"]["concentration"] == {
        "value": "1.0",
        "unit": "L",
    }
    assert repaired["ph_range"] == {"min": 6.0, "max": 7.0}
    assert repaired["variant_children"] == [repair_module.M3041_CHILD]


def test_m3042_restores_anaerobic_liquid_instructions(repair_module) -> None:
    target = repair_module.TARGETS[2]
    repaired = repair_module.repair_record(_doc(target), target)
    ingredients = _by_name(repaired["ingredients"])

    assert ingredients["Distilled water"]["concentration"] == {"value": "1.0", "unit": "L"}
    assert "N2/CO2 atmosphere" in ingredients["Carbon dioxide gas"]["notes"]
    assert "N2/CO2 atmosphere" in ingredients["Nitrogen gas"]["notes"]
    assert repaired["ph_range"] == {"min": 6.0, "max": 7.0}
    assert repaired["preparation_steps"] == repair_module.M3042_PREPARATION_STEPS
    assert repaired["sterilization"] == repair_module.M3042_STERILIZATION
    assert repaired["parent_media"] == repair_module.M3042_PARENT
    assert repaired["variant_relationship"] == "PHYSICAL_STATE_VARIANT"
    assert repaired["variant_modifications"] == [repair_module.M3042_VARIANT_MODIFICATION]


def test_repair_appends_events_and_references_once(repair_module) -> None:
    for target in repair_module.TARGETS:
        once = repair_module.repair_record(_doc(target), target)
        twice = repair_module.repair_record(once, target)

        assert [row["reference"] for row in twice["references"]] == list(target.references)
        assert [
            event
            for event in twice["curation_history"]
            if event["curator"] == repair_module.CURATOR and event["action"] == target.action
        ] == [
            {
                "timestamp": repair_module.TIMESTAMP,
                "curator": repair_module.CURATOR,
                "action": target.action,
                "source": "; ".join(target.references),
                "notes": target.notes,
            }
        ]
