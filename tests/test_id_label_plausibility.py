"""Plausibility gate for label-waived (id, label) slots.

The waiver exists so curators can keep human-facing recipe names ("Distilled
water" on CHEBI:15377, "KH2PO4" on CHEBI:63036) instead of OBO canonical labels.
Before this gate the waiver checked only that the id EXISTED, so a valid id for
an entirely different molecule passed silently — CHEBI:86457 was asserted for
"MnCl .4H O" and is in fact 2-hydroxybenzoyl-AMP.

These tests pin both directions: the curator-intended labels must keep passing,
and the unrelated-compound case must fail.
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

import pytest

_REPO = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location(
    "validate_id_label_correspondence",
    _REPO / "scripts" / "validate_id_label_correspondence.py",
)
mod = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(mod)

chem = mod.chem_formula


class FakeAdapter:
    """Minimal OAK stand-in: label, alias map and a molecular-formula metadata map."""

    def __init__(self, terms: dict[str, dict]):
        self._terms = terms

    def label(self, curie: str):
        entry = self._terms.get(curie)
        return entry["label"] if entry else None

    def entity_alias_map(self, curie: str):
        entry = self._terms.get(curie) or {}
        return {"oio:hasExactSynonym": list(entry.get("synonyms", []))}

    def entity_metadata_map(self, curie: str):
        entry = self._terms.get(curie) or {}
        formula = entry.get("formula")
        return {"chebi:formula": [formula]} if formula else {}


ADAPTER = FakeAdapter({
    # correct groundings that MUST keep passing
    "CHEBI:15377": {"label": "water", "synonyms": ["H2O"]},
    "CHEBI:63036": {"label": "potassium dihydrogen phosphate", "formula": "KH2O4P"},
    "CHEBI:86368": {"label": "manganese(II) chloride tetrahydrate",
                    "formula": "Cl2Mn.4H2O"},
    "CHEBI:34887": {"label": "nickel dichloride", "formula": "Cl2Ni"},
    # wrong groundings that MUST fail
    "CHEBI:86457": {"label": "2-hydroxybenzoyl-AMP", "formula": "C17H18N5O9P"},
    "CHEBI:74559": {"label": "Lys-Ile", "formula": "C12H25N3O3"},
    "CHEBI:33141": {"label": "dichromate(2-)", "formula": "Cr2O7"},
    # correct grounding whose LABEL lost its subscripts upstream
    "CHEBI:29377": {"label": "sodium carbonate", "formula": "CO3.2Na"},
    # an ALL-CAPS abbreviation that IS the canonical label but parses as a
    # formula (C,C,C,P) conflicting with the real formula C9H5ClN4.
    "CHEBI:3259": {"label": "CCCP", "formula": "C9H5ClN4"},
})


def _classify(label: str, curie: str, **kw):
    return mod.classify(
        curie=curie, label=label, adapter=ADAPTER,
        policy="canonical_or_synonym", scope="exact_related",
        label_waived=True, waiver_mode="plausible", **kw,
    )["verdict"]


@pytest.mark.parametrize("label,curie", [
    ("Distilled water", "CHEBI:15377"),   # shares the word "water"
    ("KH2PO4", "CHEBI:63036"),            # formula matches exactly
    ("MnCl2 x 4 H2O", "CHEBI:86368"),     # formula matches exactly
    ("NiCl2 x 6 H2O", "CHEBI:34887"),     # hydrate → anhydrous parent, tolerated
    ("H2O", "CHEBI:15377"),               # matches a synonym
])
def test_curator_labels_still_pass(label, curie):
    assert _classify(label, curie) == "OK_ID_ONLY"


@pytest.mark.parametrize("label,curie", [
    ("MnCl .4H O", "CHEBI:86457"),  # no shared word with 2-hydroxybenzoyl-AMP
    ("KI", "CHEBI:74559"),          # K,I vs C,H,N,O — element conflict
    ("H BO", "CHEBI:33141"),        # B vs Cr — element conflict
])
def test_unrelated_compound_is_flagged(label, curie):
    assert _classify(label, curie) == "IMPLAUSIBLE_LABEL"


def test_abbreviation_matching_canonical_label_is_not_a_formula_conflict():
    """An exact match to the term's own label must win before the formula check.

    "CCCP" is CHEBI:3259's canonical label; read as a formula it is C3P, which
    conflicts with the real C9H5ClN4. Without the exact-match short-circuit the
    ontology's own label was reported IMPLAUSIBLE_LABEL.
    """
    assert _classify("CCCP", "CHEBI:3259") == "OK_ID_ONLY"


def test_lost_subscripts_reported_separately():
    """Correct grounding, damaged label — a name repair, not a mapping error."""
    assert _classify("NaCO3", "CHEBI:29377") == "LABEL_SUBSCRIPTS_LOST"
    assert "LABEL_SUBSCRIPTS_LOST" not in mod._ERROR_VERDICTS


def test_out_of_range_accession_distinguished_from_missing():
    """A PubChem CID wearing a CHEBI prefix gets its own verdict."""
    assert _classify("Nicotinate", "CHEBI:10716816", max_accession=300000) == \
        "ID_OUT_OF_RANGE"
    # Below the ceiling and simply absent → the ordinary missing-id verdict.
    assert _classify("Whatever", "CHEBI:99999", max_accession=300000) == \
        "ID_NOT_FOUND"


def test_default_waiver_mode_is_unchanged():
    """Without opt-in, the historical blanket waiver still applies."""
    verdict = mod.classify(
        curie="CHEBI:86457", label="MnCl .4H O", adapter=ADAPTER,
        policy="canonical_or_synonym", scope="exact_related",
        label_waived=True,  # waiver_mode defaults to "id_only"
    )["verdict"]
    assert verdict == "OK_ID_ONLY"


@pytest.mark.parametrize("label,formula,expected", [
    ("KH2PO4", "KH2O4P", "MATCH"),
    ("MnCl2 x 4 H2O", "Cl2Mn.4H2O", "MATCH"),
    ("Fe(NH4)2(SO4)2 x 6 H2O", "Fe.2H4N.2O4S.6H2O", "MATCH"),
    ("NiCl2 x 6 H2O", "Cl2Ni", "HYDRATE_RELAXED"),
    ("NaCO3", "CO3.2Na", "SUBSCRIPTS_LOST"),
    ("KI", "C12H25N3O3", "CONFLICT"),
    ("Distilled water", "H2O", None),   # prose label — not comparable
])
def test_formula_comparison(label, formula, expected):
    assert chem.compare_formulas(label, formula) == expected


def test_roman_oxidation_state_parses():
    """'Fe(III)PO4' must not read III as three iodine atoms."""
    assert chem.parse_formula("Fe(III)PO4") == {"Fe": 1, "P": 1, "O": 4}


def test_unparseable_formula_refuses_to_judge():
    """Returning None means 'cannot judge' — never a mismatch."""
    assert chem.parse_formula("Not a formula at all") is None
    assert chem.parse_ontology_formula("C12H20O2R") is None  # generic R group


# --- hydrate separators -----------------------------------------------------
# Regression cases from a live scan of 23,129 real CultureMech ingredient
# labels. The separator before a hydrate tail appears as whitespace, a dot, a
# middot, or an "x", sometimes combined; getting any of them wrong silently
# fabricates an element multiset, which is worse than declining to judge.


@pytest.mark.parametrize(
    "label, expected",
    [
        # Whitespace alone is a separator. Requiring x/·/* absorbed the
        # multiplier into the preceding element: "CaCl2 2H2O" parsed to Cl:22
        # and produced a false SUBSCRIPTS_LOST on a correct label.
        ("CaCl2 2H2O", {"Ca": 1, "Cl": 2, "H": 4, "O": 2}),
        ("MgSO4 7H2O", {"Mg": 1, "S": 1, "O": 11, "H": 14}),
        # A dot separator with surrounding spaces. Both forms occur in
        # CultureMech (CuSO4 . 5H2O x14, Na2MoO4. 2H2O x2); accepting
        # whitespace as a separator must not strand the dot in the core.
        ("CuSO4 . 5H2O", {"Cu": 1, "S": 1, "O": 9, "H": 10}),
        ("Na2MoO4. 2H2O", {"Na": 2, "Mo": 1, "O": 6, "H": 4}),
        # Long-standing forms that must keep working.
        ("CaCl2 x 2 H2O", {"Ca": 1, "Cl": 2, "H": 4, "O": 2}),
        ("CuSO4·5H2O", {"Cu": 1, "S": 1, "O": 9, "H": 10}),
        # "x" as separator with no count is a monohydrate, not a variable.
        ("MnSO4 x H2O", {"Mn": 1, "S": 1, "O": 5, "H": 2}),
    ],
)
def test_hydrate_separator_forms(label, expected):
    assert chem.parse_formula(label) == expected


@pytest.mark.parametrize("label", ["VOSO4·xH2O", "MnSO4 x n H2O", "Fe2(SO4)3 x n H2O"])
def test_variable_hydrate_refuses_to_judge(label):
    """An unknown multiplier must return None, not a guess of 1.

    The spaced form already did; the contiguous "·xH2O" form guessed, so the
    same meaning got two answers.
    """
    assert chem.parse_formula(label) is None


# --- R-prefixed element symbols ---------------------------------------------


@pytest.mark.parametrize(
    "formula, expected",
    [
        ("ClRb", {"Cl": 1, "Rb": 1}),   # rubidium chloride — "RbCl" is a real label
        ("Cl3Ru", {"Cl": 3, "Ru": 1}),
        ("Cl3Rh", {"Cl": 3, "Rh": 1}),
        ("O2Re", {"O": 2, "Re": 1}),
    ],
)
def test_r_prefixed_elements_are_not_generic_r_groups(formula, expected):
    """A substring test for "R" also matched Rb/Ru/Rh/Re/Ra/Rn, dropping the
    formula check and leaving correct labels reported IMPLAUSIBLE_LABEL."""
    assert chem.parse_ontology_formula(formula) == expected


@pytest.mark.parametrize("formula", ["RCOOH", "C10H18RO"])
def test_generic_r_group_still_refused(formula):
    assert chem.parse_ontology_formula(formula) is None
