"""Tests for the composition-based medium identification behind #262.

The point at issue: #261 refused to assert a volume whenever the fetched medium's NAME
disagreed with the record's. Composition settles what the name cannot — but only if it
is compared on VALUES. These tests pin that distinction, because comparing names alone
scores ~0.97 between unrelated anaerobic media and would wave everything through.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from fetch_komodo_base_volumes import composition_agreement  # noqa: E402
from promote_komodo_volume_candidates import promote_doc  # noqa: E402


def _medium(pairs, name="SOME MEDIUM"):
    return {"medium": {"name": name},
            "solutions": [{"recipe": [{"compound": c, "g_l": v} for c, v in pairs]}]}


def _doc(pairs):
    return {"ingredients": [{"preferred_term": c,
                             "concentration": {"value": str(v), "unit": "G_PER_L"}}
                            for c, v in pairs]}


def test_identical_composition_scores_perfect():
    pairs = [("NaCl", 10.0), ("MgSO4 x 7 H2O", 3.0), ("KCl", 0.5)]
    assert composition_agreement(_doc(pairs), _medium(pairs)) == (1.0, 3)


def test_same_compounds_different_values_do_not_confirm():
    """The failure mode this exists to catch: anaerobic media share a backbone, so the
    compound NAMES match even between unrelated media. Only the values separate them."""
    ours = [("NaCl", 10.0), ("MgSO4 x 7 H2O", 3.0), ("KCl", 0.5)]
    theirs = [("NaCl", 20.0), ("MgSO4 x 7 H2O", 1.0), ("KCl", 0.5)]
    ratio, shared = composition_agreement(_doc(ours), _medium(theirs))
    assert shared == 3 and ratio < 0.5


def test_compound_names_are_compared_ignoring_punctuation_and_case():
    ours = [("MgSO4 x 7 H2O", 3.0)]
    theirs = [("mgso4x7h2o", 3.0)]
    assert composition_agreement(_doc(ours), _medium(theirs)) == (1.0, 1)


def test_no_shared_compounds_scores_zero_not_one():
    """An empty intersection must not read as perfect agreement."""
    assert composition_agreement(_doc([("NaCl", 1.0)]), _medium([("Glucose", 1.0)])) == (0.0, 0)


# --- promotion ------------------------------------------------------------------

def _nested(with_concentration=False):
    sol = {"preferred_term": "Trace element solution SL-10",
           "composition": [],
           "preparation_notes": ("Stock prepared in 1000 ml. Composition and addition "
                                 "volume NOT asserted: proposed as 1 ml/l on basis "
                                 "CROSS_MEDIUM_INFERENCE; see concentration_candidates (#150)."),
           "concentration_candidates": [{"value": "1", "unit": "ML_PER_L",
                                         "basis": "CROSS_MEDIUM_INFERENCE"}]}
    if with_concentration:
        sol["concentration"] = {"value": "5", "unit": "ML_PER_L"}
    return {"solutions": [sol]}


def test_perfect_agreement_promotes_the_candidate():
    doc = _nested()
    promoted, sharpened = promote_doc(doc, "508", 1.0, 32, "CARBOXYDOTHERMUS MEDIUM")
    sol = doc["solutions"][0]
    assert (promoted, sharpened) == (1, 0)
    assert sol["concentration"] == {"value": "1", "unit": "ML_PER_L"}
    assert "concentration_candidates" not in sol
    assert "NOT asserted" not in sol["preparation_notes"]


def test_imperfect_agreement_leaves_it_a_candidate_but_sharpens_the_reason():
    doc = _nested()
    promoted, sharpened = promote_doc(doc, "824", 0.89, 37, "TISSIERELLA MEDIUM")
    sol = doc["solutions"][0]
    assert (promoted, sharpened) == (0, 1)
    assert "concentration" not in sol
    assert "89%" in sol["concentration_candidates"][0]["counterevidence"]


def test_too_few_shared_compounds_is_not_enough_even_at_perfect_agreement():
    doc = _nested()
    promoted, _ = promote_doc(doc, "1", 1.0, 2, "X")
    assert promoted == 0, "2 shared compounds cannot identify a medium"


def test_promotion_never_overwrites_a_stated_concentration():
    """Filling a gap is the whole licence here; overwriting a source's word is not."""
    doc = _nested(with_concentration=True)
    promoted, _ = promote_doc(doc, "508", 1.0, 32, "X")
    assert promoted == 0
    assert doc["solutions"][0]["concentration"] == {"value": "5", "unit": "ML_PER_L"}
