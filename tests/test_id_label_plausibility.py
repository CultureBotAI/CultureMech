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
