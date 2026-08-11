"""Pin the stock-identification report and its refusal to guess volumes (#150).

Identifying WHICH stock a flattened cocktail came from is safe — it is an exact
name+value agreement on three or more compounds. Filling in the stock's usual
addition VOLUME is not, and these tests exist to keep the second from creeping in
after the first.
"""
from __future__ import annotations

import importlib.util
import sys
from collections import Counter
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
def ics():
    return _load("identify_cocktail_stocks")


def test_library_keeps_the_largest_observed_composition(ics):
    """A stock is reported differently by different media (optional components,
    truncated lists). Matching against the fullest one seen maximises the chance of
    clearing the 3-component bar without loosening the per-component test."""
    volumes = {
        "a.yaml": {"additions": [{"solution_name": "SL-10", "addition_volume_ml": 1,
                                  "stock_components": [{"compound": "FeCl2", "g_l": 1.5}]}]},
        "b.yaml": {"additions": [{"solution_name": "SL-10", "addition_volume_ml": 1,
                                  "stock_components": [{"compound": "FeCl2", "g_l": 1.5},
                                                       {"compound": "ZnCl2", "g_l": 0.07}]}]},
    }
    comps, vols = ics.build_library(volumes)
    assert [c["compound"] for c in comps["SL-10"]] == ["FeCl2", "ZnCl2"]
    assert vols["SL-10"] == Counter({"1": 2})


def test_library_records_volume_spread_not_just_the_mode(ics):
    """The report's whole value is showing HOW consistent a stock's volume is, so
    the distribution must survive, not collapse to a single number."""
    volumes = {
        f"{i}.yaml": {"additions": [{"solution_name": "Seven vitamins solution",
                                     "addition_volume_ml": v, "stock_components": []}]}
        for i, v in enumerate([1, 1, 1, 5])
    }
    _, vols = ics.build_library(volumes)
    assert vols["Seven vitamins solution"] == Counter({"1": 3, "5": 1})
    assert len(vols["Seven vitamins solution"]) > 1, "spread must be visible"


def test_three_components_is_the_identification_bar(ics):
    """The audit defines a cocktail as >=3 flagged rows, so three independent
    name+value agreements is the same bar — one or two could coincide."""
    assert ics.MIN_COMPONENTS == 3


def test_the_report_never_emits_an_applied_volume(ics):
    """The load-bearing guarantee. The report may carry a modal volume as EVIDENCE,
    but must not present it as the record's volume — no column may imply an
    applied or chosen value."""
    import inspect

    src = inspect.getsource(ics)
    fields = src.split('rows.append({')[1].split('})')[0]
    assert "modal_volume_ml" in fields and "volume_distribution" in fields, (
        "the evidence columns disappeared; the report is no longer showing its working")
    for banned in ("addition_volume_ml", "applied_volume", "chosen_volume"):
        assert f'"{banned}"' not in fields, (
            f"{banned} implies a decision the data does not support — see the "
            "docstring: the one stock with an invariant volume matches no blocked record")


def test_the_negative_finding_is_recorded_in_the_docstring(ics):
    """The invariant-volume shortcut is the obvious next idea and it does NOT hold.
    Losing that explanation would invite someone to re-propose it."""
    doc = ics.__doc__ or ""
    assert "SL-10" in doc and "0 blocked records" in doc
    assert "under-sampled" in doc or "under-sampled" in doc.lower()
