"""Guard that no-composition media are flagged incomplete, not silent (#175).

A media record with no ingredients and no solutions has no usable composition, yet
validate-strict passes it. 126 such records carried no data_quality_flag at all;
they were flagged incomplete_composition so the gap is visible. This pins that
invariant and the classifier.
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
def cfe():
    return _load("curate_flag_empty_composition")


def test_no_composition_detection(cfe):
    assert cfe.has_no_composition({})
    assert cfe.has_no_composition({"ingredients": []})
    assert not cfe.has_no_composition({"ingredients": [{"preferred_term": "Agar"}]})
    assert not cfe.has_no_composition({"solutions": [{"preferred_term": "Trace elements"}]})


def test_needs_flag_only_when_unflagged_and_empty(cfe):
    assert cfe.needs_flag({"ingredients": []})
    assert not cfe.needs_flag({"ingredients": [],
                               "data_quality_flags": ["incomplete_composition"]})
    assert not cfe.needs_flag({"ingredients": [{"preferred_term": "Agar"}]})


def test_flag_adds_flag_and_event(cfe):
    doc = {"ingredients": []}
    assert cfe.flag(doc) is True
    assert "incomplete_composition" in doc["data_quality_flags"]
    assert doc["curation_history"][-1]["action"] == "FLAGGED_INCOMPLETE_COMPOSITION"
    # idempotent: a second pass does nothing
    assert cfe.flag(doc) is False


def test_every_empty_medium_is_flagged(cfe, media_records):
    """Recurrence guard: a media record with no ingredients and no solutions must
    carry the incomplete_composition flag, or a fresh import left a silent gap."""
    silent = [str(p) for p, d in media_records if cfe.needs_flag(d)]
    assert silent == [], (
        f"{len(silent)} media have no composition and no incomplete_composition "
        "flag; run `just curate-flag-empty-composition --apply`.")
