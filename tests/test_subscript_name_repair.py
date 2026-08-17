"""Tests for scripts/repair_subscript_stripped_names.py (#276 item 3)."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from repair_subscript_stripped_names import REPAIRS, repair_doc  # noqa: E402


def test_a_stripped_name_is_restored_and_the_original_kept():
    doc = {"ingredients": [{"preferred_term": "H BO", "notes": "from the source PDF"}]}
    changed = repair_doc(doc)
    ing = doc["ingredients"][0]
    assert changed == [("H BO", "H3BO3")]
    assert ing["preferred_term"] == "H3BO3"
    assert "H BO" in ing["notes"], "the corrupted original must survive in notes"
    assert "from the source PDF" in ing["notes"], "existing notes must not be clobbered"


def test_ambiguous_names_are_not_guessed():
    """`Na VO` is Na3VO4 or NaVO3 and the corpus cannot say which. Guessing would be the
    same class of error this script exists to undo."""
    assert "Na VO" not in REPAIRS
    doc = {"ingredients": [{"preferred_term": "Na VO"}]}
    assert repair_doc(doc) == []
    assert doc["ingredients"][0]["preferred_term"] == "Na VO"


def test_names_are_repaired_wherever_they_sit():
    """Solution records carry a top-level `composition:`, which an ingredients-only walk
    misses — that is how a bad grounding hid until #275."""
    doc = {"composition": [{"preferred_term": "As O"}],
           "solutions": [{"composition": [{"preferred_term": "K SO"}]}]}
    changed = dict(repair_doc(doc))
    assert changed == {"As O": "As2O3", "K SO": "K2SO4"}


def test_an_uncorrupted_name_is_untouched():
    doc = {"ingredients": [{"preferred_term": "MgSO4 x 7 H2O"}]}
    before = dict(doc["ingredients"][0])
    assert repair_doc(doc) == []
    assert doc["ingredients"][0] == before


def test_every_repair_actually_adds_digits():
    """A repair that changes nothing, or removes information, is a bug."""
    for old, (new, why) in REPAIRS.items():
        assert new != old
        assert sum(c.isdigit() for c in new) > sum(c.isdigit() for c in old), old
        assert why, f"{old} has no corroboration recorded"
