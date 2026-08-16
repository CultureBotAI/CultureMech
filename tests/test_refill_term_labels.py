"""Tests for scripts/refill_term_labels.py (#259)."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from refill_term_labels import refill_text  # noqa: E402


class FakeLabels:
    def __init__(self, mapping): self.m = mapping
    def get(self, term_id): return self.m.get(term_id)


def test_ingredient_string_is_replaced_by_the_ontology_label():
    text = ("ingredients:\n- preferred_term: MgSO4 x 7 H2O\n  term:\n"
            "    id: CHEBI:31795\n    label: MgSO4 x 7 H2O\n")
    new, stats = refill_text(text, FakeLabels({"CHEBI:31795": "magnesium sulfate heptahydrate"}))
    d = yaml.safe_load(new)
    assert d["ingredients"][0]["term"]["label"] == "magnesium sulfate heptahydrate"
    assert d["ingredients"][0]["preferred_term"] == "MgSO4 x 7 H2O", \
        "the ingredient's own string must stay in preferred_term"
    assert stats["corrected"] == 1


def test_empty_labels_are_filled():
    text = "ingredients:\n- preferred_term: X\n  term:\n    id: CHEBI:1\n    label: ''\n"
    new, stats = refill_text(text, FakeLabels({"CHEBI:1": "widget"}))
    assert yaml.safe_load(new)["ingredients"][0]["term"]["label"] == "widget"
    assert stats["empty -> filled"] == 1


def test_an_unresolvable_id_is_left_completely_alone():
    """Blanking it would hide the finding that the id does not resolve."""
    text = ("ingredients:\n- preferred_term: X\n  term:\n"
            "    id: MediaIngredientMech:000389\n    label: Cysteine-HCl\n")
    new, stats = refill_text(text, FakeLabels({}))
    assert new == text
    assert stats["unresolvable id (left alone)"] == 1


def test_labels_needing_quotes_stay_valid_yaml():
    """yaml.dump('water') emits a trailing '...' document-end marker, which corrupted
    every file on the first run. Labels with colons and quotes must round-trip."""
    for label in ["water", "iron: special", "5'-nucleotide", 'has "quotes"', "a, b"]:
        text = "ingredients:\n- preferred_term: X\n  term:\n    id: CHEBI:1\n    label: old\n"
        new, _ = refill_text(text, FakeLabels({"CHEBI:1": label}))
        assert yaml.safe_load(new)["ingredients"][0]["term"]["label"] == label, label


def test_a_correct_label_is_not_rewritten():
    text = "ingredients:\n- preferred_term: X\n  term:\n    id: CHEBI:1\n    label: widget\n"
    new, stats = refill_text(text, FakeLabels({"CHEBI:1": "widget"}))
    assert new == text and stats["already correct"] == 1


def test_a_label_not_under_an_id_is_untouched():
    text = "solutions:\n- preferred_term: S\n  label: some solution label\n"
    new, _ = refill_text(text, FakeLabels({"CHEBI:1": "widget"}))
    assert new == text
