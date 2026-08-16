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


def test_paba_zwitterion_is_corrected_and_the_empty_label_filled():
    """#260: CHEBI:194474 is 4-ammoniobenzoate; every row carried CAS 150-13-0 (the
    neutral acid) and an EMPTY label, so nothing on the record asserted the zwitterion."""
    for name in ("4-Aminobenzoic acid", "p-Amino Benzoic Acid", "p-amino benzoic acid"):
        text = (
            "ingredients:\n"
            f"- preferred_term: {name}\n"
            "  notes: 'CAS: 150-13-0; MW: 137.14'\n"
            "  term:\n"
            "    id: CHEBI:194474\n"
            "    label: ''\n"
        )
        new, changes = fix_text(text)
        assert changes == [(name, "CHEBI:194474", "CHEBI:30753")]
        assert "id: CHEBI:30753" in new
        assert "label: 4-aminobenzoic acid" in new, "empty label must be filled"
        assert yaml.safe_load(new)["ingredients"][0]["notes"].startswith("CAS: 150-13-0")


def test_cysteine_hcl_is_moved_off_a_fluorescent_dye():
    """CHEBI:52891 is `QSY9 succinimidyl ester(1+)` — a quencher dye, not an amino
    acid. The same string is already grounded to CHEBI:91247 in 40 other rows."""
    for name in ("Cysteine-HCl", "cysteine-HCl"):
        text = ("ingredients:\n"
                f"- preferred_term: {name}\n"
                "  term:\n"
                "    id: CHEBI:52891\n"
                "    label: ''\n")
        new, changes = fix_text(text)
        assert changes == [(name, "CHEBI:52891", "CHEBI:91247")]
        assert "label: L-cysteine hydrochloride" in new


def test_hydrated_hcl_names_move_off_plain_l_cysteine():
    """A name spelling out both HCl and a hydrate must not sit on CHEBI:17561, which
    is neither. The corpus already uses CHEBI:91248 for this substance 1,901 times."""
    for name in ("L-Cysteine-HCl x H2O", "Cysteine-HCl x H2O", "L-cysteine-HCL x H2O"):
        text = ("ingredients:\n"
                f"- preferred_term: {name}\n"
                "  term:\n"
                "    id: CHEBI:17561\n"
                "    label: L-cysteine\n")
        new, changes = fix_text(text)
        assert changes == [(name, "CHEBI:17561", "CHEBI:91248")], name
        assert "label: L-cysteine hydrochloride hydrate" in new


def test_plain_cysteine_names_keep_chebi_17561():
    """Only HCl-and-hydrate names move. The free amino acid is correctly 17561, and
    keying on the id alone would have wrecked 169 legitimate rows."""
    for name in ("L-Cysteine", "Cysteine", "L-cysteine"):
        text = ("ingredients:\n"
                f"- preferred_term: {name}\n"
                "  term:\n"
                "    id: CHEBI:17561\n"
                "    label: L-cysteine\n")
        new, changes = fix_text(text)
        assert changes == [], name
        assert new == text


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

def test_hydrate_names_move_but_anhydrous_names_do_not():
    """#258's core rule. The SAME wrong id is correct for the unmarked name, so this
    can only be keyed on name+id — `Na2MoO4` must stay anhydrous while
    `Na2MoO4 x 2 H2O` moves to the dihydrate."""
    moves = ("Na2MoO4 x 2 H2O", "CHEBI:75215", "CHEBI:75213")
    stays = ("Na2MoO4", "CHEBI:75215")
    text = ("ingredients:\n"
            f"- preferred_term: {moves[0]}\n  term:\n    id: {moves[1]}\n    label: x\n"
            f"- preferred_term: {stays[0]}\n  term:\n    id: {stays[1]}\n    label: y\n")
    new, changes = fix_text(text)
    assert changes == [(moves[0], moves[1], moves[2])]
    assert f"id: {stays[1]}" in new, "the anhydrous row must survive"

def test_the_majority_reading_is_not_assumed_correct():
    """1,161 rows had `CoSO4 x 7 H2O` on the anhydrous id and 5 on the heptahydrate.
    The 5 were right; a majority-wins rule would have entrenched the error."""
    text = ("ingredients:\n- preferred_term: CoSO4 x 7 H2O\n  term:\n"
            "    id: CHEBI:53470\n    label: cobalt(2+) sulfate\n")
    new, changes = fix_text(text)
    assert changes == [("CoSO4 x 7 H2O", "CHEBI:53470", "CHEBI:91244")]
    assert "label: cobalt(2+) sulfate heptahydrate" in new

def test_starch_moves_off_gellan_gum_but_gellan_gum_does_not():
    for name, expect in (("Starch", "CHEBI:28017"), ("Gelrite", None)):
        text = ("ingredients:\n"
                f"- preferred_term: {name}\n  term:\n    id: CHEBI:85248\n    label: g\n")
        new, changes = fix_text(text)
        if expect:
            assert changes and f"id: {expect}" in new, name
        else:
            assert changes == [] and new == text, name

def test_bare_ion_ids_move_to_the_named_salt():
    text = ("ingredients:\n- preferred_term: KNO3\n  term:\n"
            "    id: CHEBI:17632\n    label: nitrate\n")
    new, changes = fix_text(text)
    assert changes == [("KNO3", "CHEBI:17632", "CHEBI:63043")]
    assert "label: potassium nitrate" in new

def test_dextrose_collapses_onto_d_glucose_from_both_wrong_ids():
    for wrong in ("CHEBI:17234", "CHEBI:4167"):
        text = ("ingredients:\n"
                f"- preferred_term: Dextrose\n  term:\n    id: {wrong}\n    label: g\n")
        new, changes = fix_text(text)
        assert changes == [("Dextrose", wrong, "CHEBI:17634")], wrong
