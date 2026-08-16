"""Tests for scripts/dedupe_identical_ingredients.py (#263)."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from dedupe_identical_ingredients import dedupe  # noqa: E402


def _ing(name, value, **extra):
    return {"preferred_term": name,
            "concentration": {"value": value, "unit": "G_PER_L"}, **extra}


def test_a_fully_identical_row_is_removed():
    doc = {"ingredients": [_ing("Tryptone", "10.0"), _ing("Tryptone", "10.0")]}
    removed, differing = dedupe(doc)
    assert removed == ["Tryptone"] and differing == []
    assert len(doc["ingredients"]) == 1


def test_rows_differing_in_provenance_are_kept():
    """Same name and concentration, different notes. Collapsing means choosing which
    provenance survives — a curation call, not a mechanical one."""
    doc = {"ingredients": [_ing("Sodium chloride", "5.0", notes="from source A"),
                           _ing("Sodium chloride", "5.0", notes="from source B")]}
    removed, differing = dedupe(doc)
    assert removed == []
    assert differing == ["Sodium chloride"]
    assert len(doc["ingredients"]) == 2


def test_same_name_different_concentration_is_never_touched():
    doc = {"ingredients": [_ing("Glucose", "10.0"), _ing("Glucose", "20.0")]}
    removed, differing = dedupe(doc)
    assert removed == [] and differing == []
    assert len(doc["ingredients"]) == 2


def test_three_copies_collapse_to_one():
    doc = {"ingredients": [_ing("NaCl", "1")] * 3}
    removed, _ = dedupe(doc)
    assert len(removed) == 2 and len(doc["ingredients"]) == 1


def test_a_record_with_no_duplicates_is_left_untouched():
    doc = {"ingredients": [_ing("A", "1"), _ing("B", "2")]}
    before = [dict(i) for i in doc["ingredients"]]
    removed, differing = dedupe(doc)
    assert removed == [] and differing == []
    assert doc["ingredients"] == before
