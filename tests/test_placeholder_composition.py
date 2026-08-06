"""Guard against the "See source for composition" placeholder ingredient (#175).

100 media carried a single fake ingredient whose preferred_term was literally
"See source for composition" — a uniform import artifact that made empty records
match every ingredient scan. It was removed; the incomplete_composition flag
carries the state instead. These tests pin the repair and the classifier.
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
def cpc():
    return _load("curate_placeholder_composition")


def test_is_placeholder_matches_the_exact_phrase(cpc):
    assert cpc.is_placeholder({"preferred_term": "See source for composition"})
    assert cpc.is_placeholder({"preferred_term": "see source for composition "})
    assert not cpc.is_placeholder({"preferred_term": "Beef extract"})
    assert not cpc.is_placeholder("Beef extract")


def test_repair_empties_and_flags_a_placeholder_only_record(cpc):
    doc = {"ingredients": [{"preferred_term": "See source for composition",
                            "concentration": {"value": "variable", "unit": "G_PER_L"}}]}
    assert cpc.repair(doc) is True
    assert doc["ingredients"] == []
    assert "incomplete_composition" in doc["data_quality_flags"]
    assert doc["curation_history"][-1]["action"] == "REMOVED_PLACEHOLDER_INGREDIENT"


def test_repair_preserves_real_ingredients_and_does_not_flag(cpc):
    """A placeholder sitting among real ingredients is de-polluted, but the record
    is NOT declared empty — it has a composition."""
    doc = {"ingredients": [
        {"preferred_term": "Beef extract"},
        {"preferred_term": "See source for composition"}]}
    assert cpc.repair(doc) is True
    assert [i["preferred_term"] for i in doc["ingredients"]] == ["Beef extract"]
    assert "incomplete_composition" not in (doc.get("data_quality_flags") or [])


def test_repair_is_a_noop_without_the_placeholder(cpc):
    doc = {"ingredients": [{"preferred_term": "Beef extract"}]}
    assert cpc.repair(doc) is False


def test_no_media_record_carries_the_placeholder(cpc, media_records):
    """Recurrence guard: a fresh import reintroducing the placeholder fails here."""
    offenders = [str(p) for p, d in media_records
                 if any(cpc.is_placeholder(i) for i in d.get("ingredients") or [])]
    assert offenders == [], (
        f"{len(offenders)} media carry the placeholder ingredient again; run "
        "`just curate-placeholder-composition --apply`.")
