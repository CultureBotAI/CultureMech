"""Unit-test the pure pieces of the cocktail-nesting PROPOSAL tool (#150).

The tool never edits the corpus — it emits a worklist. What has logic worth pinning
is the addition-volume recovery: it must find a volume only in a genuine addition
context, and stay silent otherwise, because a fabricated volume corrupts a real
recipe (the whole reason the repair is a proposal, not an auto-apply).
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def pcn():
    return _load("propose_cocktail_nesting")


def _doc(*sentences):
    return {"preparation_steps": [{"description": s} for s in sentences]}


def test_recovers_a_genuine_addition_volume(pcn):
    vol, evidence = pcn.recover_volume(_doc("Autoclave and add 1.0 ml/l vitamin solution."))
    assert vol == "1.0"
    assert "vitamin solution" in evidence


def test_recovers_from_a_ml_solution_phrase(pcn):
    vol, _ = pcn.recover_volume(_doc("Combine solutions A, B, C and add 1 ml trace element solution."))
    assert vol == "1"


def test_a_volume_without_addition_context_is_not_recovered(pcn):
    """'except vitamins ... adjust to 20 ml' is not an addition of the cocktail."""
    vol, _ = pcn.recover_volume(_doc("Mix ingredients except vitamins, then adjust to 20 ml final."))
    assert vol == ""


def test_no_volume_at_all_is_silent(pcn):
    assert pcn.recover_volume(_doc("Adjust pH to 7.0 and autoclave.")) == ("", "")


def test_notes_are_also_searched(pcn):
    vol, _ = pcn.recover_volume({"notes": "Add 10 ml trace elements per litre after autoclaving."})
    assert vol == "10"


def test_cocktail_components_selects_only_flagged_trace_and_vitamin_rows(pcn):
    rows = [
        {"file_path": "a.yaml", "finding": "TRACE_SALT_AS_STOCK", "ingredient": "ZnSO4",
         "value": "22", "unit": "G_PER_L"},
        {"file_path": "a.yaml", "finding": "INDICATOR_UNIT_SLIP", "ingredient": "Biotin",
         "value": "0.02", "unit": "G_PER_L"},
        {"file_path": "a.yaml", "finding": "WATER_AS_VOLUME", "ingredient": "Water",
         "value": "1000", "unit": "G_PER_L"},
        {"file_path": "b.yaml", "finding": "TRACE_SALT_AS_STOCK", "ingredient": "MnCl2",
         "value": "5", "unit": "G_PER_L"},
    ]
    comps = pcn.cocktail_components(rows, "a.yaml")
    names = [c["ingredient"] for c in comps]
    assert names == ["ZnSO4", "Biotin"]          # trace + indicator, this file only
    assert "Water" not in names                    # WATER_AS_VOLUME is not a cocktail component
