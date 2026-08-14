"""Tests for scripts/fix_wrong_compound_groundings.py (#256).

The two properties worth defending are the ones that were nearly got wrong while
writing it: keying on name AND id (CHEBI:86463 is legitimately carried by the
aluminium salts), and leaving the rest of the file byte-identical (a YAML round-trip
reflows every long `notes:` string and buries the real edit).
"""

from __future__ import annotations

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

from fix_wrong_compound_groundings import fix_text  # noqa: E402


def test_wrong_magnesium_id_is_corrected():
    text = (
        "ingredients:\n"
        "- preferred_term: Magnesium Sulfate Heptahydrate\n"
        "  term:\n"
        "    id: CHEBI:86463\n"
        "    label: magnesium sulfate heptahydrate\n"
    )
    new, changes = fix_text(text)
    assert changes == [("Magnesium Sulfate Heptahydrate", "CHEBI:86463", "CHEBI:31795")]
    assert "id: CHEBI:31795" in new


def test_aluminium_salts_keep_chebi_86463():
    """The same id, correctly used. Keying on the id alone would corrupt these."""
    for name in ("AlK(SO4)2", "Aluminum potassium sulfate", "KAl(SO4)2"):
        text = (
            "ingredients:\n"
            f"- preferred_term: {name}\n"
            "  term:\n"
            "    id: CHEBI:86463\n"
            "    label: potassium aluminium sulfate\n"
        )
        new, changes = fix_text(text)
        assert changes == [], f"{name} must not be rewritten"
        assert new == text


def test_glucose_forms_map_to_their_own_targets():
    cases = {
        "Glucose": "CHEBI:17234",
        "glucose": "CHEBI:17234",
        "D-Glucose": "CHEBI:17634",
        "Dextrose": "CHEBI:17634",
    }
    for name, want in cases.items():
        text = (
            "ingredients:\n"
            f"- preferred_term: {name}\n"
            "  term:\n"
            "    id: CHEBI:42758\n"
            "    label: aldehydo-D-glucose\n"
        )
        new, _ = fix_text(text)
        assert f"id: {want}" in new, name
        assert "aldehydo" not in new, f"{name} kept the stale label"


def test_mim_self_link_moves_with_the_term():
    """Leaving the self-link behind would make the record self-contradictory."""
    text = (
        "ingredients:\n"
        "- preferred_term: Glucose\n"
        "  term:\n"
        "    id: CHEBI:42758\n"
        "    label: aldehydo-D-glucose\n"
        "  mediaingredientmech_chebi_term:\n"
        "    id: CHEBI:42758\n"
        "    label: aldehydo-D-glucose\n"
    )
    new, changes = fix_text(text)
    assert len(changes) == 2
    assert new.count("CHEBI:17234") == 2
    assert "CHEBI:42758" not in new


def test_unrelated_lines_are_untouched():
    """Byte-for-byte outside the corrected id/label pair."""
    text = (
        "ingredients:\n"
        "- preferred_term: Magnesium Sulfate Heptahydrate\n"
        "  concentration:\n"
        "    value: '0.075'\n"
        "    unit: G_PER_L\n"
        "  term:\n"
        "    id: CHEBI:86463\n"
        "    label: magnesium sulfate heptahydrate\n"
        "  notes: 'Mapping: micromediaparam_legacy (confidence: 0.90); CAS: 10034-99-8;"
        " MW: 246.47'\n"
    )
    new, _ = fix_text(text)
    before, after = text.splitlines(), new.splitlines()
    assert len(before) == len(after)
    differing = [i for i, (a, b) in enumerate(zip(before, after)) if a != b]
    assert differing == [6], "only the id line should differ"
    assert yaml.safe_load(new)["ingredients"][0]["notes"] == \
        yaml.safe_load(text)["ingredients"][0]["notes"]


def test_quoted_preferred_term_is_matched():
    text = (
        "ingredients:\n"
        "- preferred_term: 'D(+)-Glucose'\n"
        "  term:\n"
        "    id: CHEBI:42758\n"
        "    label: aldehydo-D-glucose\n"
    )
    new, changes = fix_text(text)
    assert changes and "id: CHEBI:17634" in new


def test_name_scope_does_not_leak_to_the_next_ingredient():
    """A correction must not carry over to a following, differently-named ingredient."""
    text = (
        "ingredients:\n"
        "- preferred_term: Glucose\n"
        "  term:\n"
        "    id: CHEBI:42758\n"
        "    label: aldehydo-D-glucose\n"
        "- preferred_term: AlK(SO4)2\n"
        "  term:\n"
        "    id: CHEBI:86463\n"
        "    label: potassium aluminium sulfate\n"
    )
    new, changes = fix_text(text)
    assert len(changes) == 1
    assert "id: CHEBI:86463" in new
    assert "label: potassium aluminium sulfate" in new
