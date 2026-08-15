"""Tests for scripts/audit_grounding_consistency.py (#258)."""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from audit_grounding_consistency import classify, groundings  # noqa: E402


def test_hydration_difference_is_classified_as_hydrate():
    assert classify("CoSO4 x 7 H2O",
                    {"CHEBI:53470": "cobalt(2+) sulfate",
                     "CHEBI:91244": "cobalt(2+) sulfate heptahydrate"}) == "HYDRATE"


def test_different_substances_are_not_called_a_hydrate_split():
    """`Starch` vs `gellan gum` is a wrong compound, not a waters-of-crystallisation
    difference, and must not be swept up by a mechanical hydrate fix."""
    assert classify("Starch",
                    {"CHEBI:28017": "starch", "CHEBI:85248": "gellan gum"}) == "OTHER"


def test_ion_ids_are_flagged():
    assert classify("Glycine",
                    {"CHEBI:15428": "glycine",
                     "CHEBI:57305": "glycine zwitterion"}) == "ION"


def test_groundings_counts_each_row(tmp_path):
    (tmp_path / "a.yaml").write_text(
        "ingredients:\n"
        "- preferred_term: Dextrose\n  term:\n    id: CHEBI:17634\n"
        "- preferred_term: Dextrose\n  term:\n    id: CHEBI:4167\n"
        "solutions:\n- preferred_term: S\n  composition:\n"
        "  - preferred_term: Dextrose\n    term:\n      id: CHEBI:17634\n")
    g = groundings(tmp_path)
    assert dict(g["Dextrose"]) == {"CHEBI:17634": 2, "CHEBI:4167": 1}
