from __future__ import annotations

import copy
import importlib.util
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parent.parent
SCRIPT = REPO / "scripts" / "repair_komodo_418_522_score30.py"


def load_script():
    spec = importlib.util.spec_from_file_location("repair_komodo_418_522_score30", SCRIPT)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def repair_module():
    return load_script()


def _doc(repair_module, target):
    return {
        "id": target.expected_id,
        "media_term": {
            "preferred_term": target.expected_media_term,
            "term": {"id": target.expected_media_term, "label": "source medium"},
        },
        "ingredients": [],
        "curation_history": [],
        "data_quality_flags": ["incomplete_composition"],
    }


def _by_name(repaired: dict, name: str) -> dict:
    rows = [
        row
        for row in repaired["ingredients"]
        if row["preferred_term"] == name
    ]
    assert len(rows) == 1
    return rows[0]


def _repair(repair_module, path: str) -> dict:
    target = repair_module.TARGET_BY_PATH[path]
    return repair_module.repair_record(_doc(repair_module, target), target)


def test_target_inventory(repair_module) -> None:
    assert [target.path for target in repair_module.TARGETS] == [
        repair_module.PELOBACTER,
        repair_module.CLOSTRIDIUM_NEOPROPIONICUM,
    ]
    assert {
        target.path: target.expected_media_term
        for target in repair_module.TARGETS
    } == {
        repair_module.PELOBACTER: "komodo.medium:418",
        repair_module.CLOSTRIDIUM_NEOPROPIONICUM: "komodo.medium:522",
    }


def test_dsmz_318_base_and_trace_components_are_scaled(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.PELOBACTER)

    assert _by_name(repaired, "KH2PO4")["concentration"] == {
        "value": "0.294118",
        "unit": "G_PER_L",
    }
    assert _by_name(repaired, "NaCl")["concentration"] == {
        "value": "0.598039",
        "unit": "G_PER_L",
    }
    assert _by_name(repaired, "CaCl2 x 2 H2O")["concentration"] == {
        "value": "0.079412",
        "unit": "G_PER_L",
    }
    assert _by_name(repaired, "Nitrilotriacetic acid (NTA)")["concentration"] == {
        "value": "0.125490",
        "unit": "G_PER_L",
    }
    assert _by_name(repaired, "Distilled water")["concentration"] == {
        "value": "980.392157",
        "unit": "ML_PER_L",
    }


def test_medium_141_vitamin_stock_is_scaled(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.CLOSTRIDIUM_NEOPROPIONICUM)

    assert _by_name(repaired, "Vitamin B12")["concentration"] == {
        "value": "0.000000980",
        "unit": "G_PER_L",
    }
    assert _by_name(repaired, "Pyridoxine-HCl")["concentration"] == {
        "value": "0.000098",
        "unit": "G_PER_L",
    }
    assert _by_name(repaired, "Thiamine-HCl x 2 H2O")["term"] == {
        "id": "CHEBI:132751",
        "label": "Thiamine-HCl x 2 H2O",
    }


def test_pelobacter_has_sodium_gallate_branch(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.PELOBACTER)
    names = {row["preferred_term"] for row in repaired["ingredients"]}

    assert repaired["ph_value"] == 7.3
    assert _by_name(repaired, "KHCO3")["concentration"] == {
        "value": "4.500000",
        "unit": "G_PER_L",
    }
    assert _by_name(repaired, "sodium gallate")["concentration"] == {
        "value": "10",
        "unit": "MILLIMOLAR",
    }
    assert "Methanol" not in names
    assert "Ethanol" not in names


def test_clostridium_neopropionicum_has_ethanol_branch(repair_module) -> None:
    repaired = _repair(repair_module, repair_module.CLOSTRIDIUM_NEOPROPIONICUM)
    names = {row["preferred_term"] for row in repaired["ingredients"]}

    assert repaired["ph_value"] == 7.0
    assert _by_name(repaired, "KHCO3")["concentration"] == {
        "value": "4.000000",
        "unit": "G_PER_L",
    }
    assert _by_name(repaired, "Ethanol")["concentration"] == {
        "value": "1.0",
        "unit": "G_PER_L",
    }
    assert "Methanol" not in names
    assert "sodium gallate" not in names


def test_repair_is_idempotent_and_clears_incomplete_flag(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.PELOBACTER]
    first = repair_module.repair_record(_doc(repair_module, target), target)
    second = repair_module.repair_record(copy.deepcopy(first), target)

    assert second == first
    assert "incomplete_composition" not in first["data_quality_flags"]
    assert "ingredients_curated" in first["data_quality_flags"]
    assert len(first["ingredients"]) == len(repair_module.COMMON_COMPONENTS) + 2


def test_source_guards_reject_wrong_source_term(repair_module) -> None:
    target = repair_module.TARGET_BY_PATH[repair_module.CLOSTRIDIUM_NEOPROPIONICUM]
    doc = _doc(repair_module, target)
    doc["media_term"]["term"]["id"] = "komodo.medium:418"

    with pytest.raises(ValueError, match="expected 'komodo.medium:522'"):
        repair_module.repair_record(doc, target)
