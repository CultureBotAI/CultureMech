"""No ingredient may be grounded to a term lacking an element its NAME demands (#276, #278).

Since #275 refilled `term.label` from the ontology, a wrong id no longer looks wrong — the
label agrees with it. The ingredient's own `preferred_term` is the last independent signal,
and this is the check that uses it.

Comparing names does not work: `MgSO4 x 7 H2O` and `potassium aluminium sulfate` share the
word "sulfate", so word overlap passes the exact CHEBI:86463 error #257 fixed. The cation
is the discriminator, so this compares ELEMENTS against ChEBI's own formula.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest
import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from audit_name_term_elements import (  # noqa: E402
    formula_elements, name_elements,
)

ROOTS = [REPO / "data" / "normalized_yaml", REPO / "data" / "merge_yaml" / "merged"]

# Ingredients ChEBI has no salt term for, so the free acid/base is the best available
# grounding and the mismatch is permanent. Listed EXPLICITLY with the reason, because a
# fuzzy tolerance would hide the next real one.
KNOWN_NO_SALT_TERM = {
    # ChEBI has `Resazurin` (CHEBI:8806) but no "resazurin sodium salt".
    ("Sodium resazurin", "CHEBI:8806"),
    ("resazurin sodium salt", "CHEBI:8806"),
    # ChEBI has `2-oxoglutarate(2-)` but no disodium salt.
    ("Na2 alpha-ketoglutarate", "CHEBI:16810"),
    # ChEBI has the anions but no sodium salts.
    ("Na2-9,10-anthraquinone-2,6-disulfonate", "CHEBI:85112"),
    ("Sodium crotonate", "CHEBI:35899"),
}

# NOT the same thing, and NOT tolerated as correct. These two are grounded to the wrong
# SUBSTANCE — selenate read as sulfate, silicate as sulfite — the same Se/Si -> S collapse
# that put `H2SeO3` on sulfurous acid. ChEBI has no term for either correct compound, so
# they cannot simply be regrounded; see #279. They are listed here so the gate stays
# green on a known, recorded defect rather than being silently weakened.
KNOWN_WRONG_PENDING_279 = {
    ("Na2SeO4 x 10 H2O", "CHEBI:32586"),      # sodium SULFATE decahydrate
    ("Na2SiO3 x 5 H2O", "CHEBI:86477"),       # sodium SULFITE
}


@pytest.fixture(scope="module")
def mismatches():
    from oaklib import get_adapter
    adapter = get_adapter("sqlite:obo:chebi")
    formulas: dict[str, str] = {}

    def formula_of(tid: str) -> str:
        if tid not in formulas:
            try:
                meta = adapter.entity_metadata_map(tid) or {}
                vals = meta.get("chemrof:generalized_empirical_formula") or [""]
                formulas[tid] = vals[0] if vals else ""
            except Exception:                                     # noqa: BLE001
                formulas[tid] = ""
        return formulas[tid]

    # Line-based, not yaml.safe_load: parsing both corpora costs ~4 minutes, past this
    # suite's budget. Only preferred_term and the CHEBI id under it are needed, and
    # distinct (name, id) pairs are checked once rather than per row.
    import re as _re
    PREF = _re.compile(r"^\s*-?\s*preferred_term:\s*(.+?)\s*$")
    IDL = _re.compile(r"^\s*id:\s*(CHEBI:\d+)\s*$")
    pairs = set()
    for root in ROOTS:
        if not root.is_dir():
            continue
        for path in root.rglob("*.yaml"):
            text = path.read_text(errors="replace")
            if "CHEBI:" not in text:
                continue
            name = ""
            for line in text.splitlines():
                m = PREF.match(line)
                if m:
                    name = m.group(1).strip().strip("'\"")
                    continue
                mi = IDL.match(line)
                if mi and name:
                    pairs.add((name, mi.group(1)))
                    name = ""
    bad = []
    for name, tid in pairs:
        if (name, tid) in KNOWN_NO_SALT_TERM | KNOWN_WRONG_PENDING_279:
            continue
        want = name_elements(name)
        if not want:
            continue
        formula = formula_of(tid)
        if not formula:
            continue
        missing = want - formula_elements(formula)
        if missing:
            bad.append((name, tid, "".join(sorted(missing))))
    return sorted(set(bad))


def test_no_grounding_lacks_an_element_its_name_demands(mismatches):
    assert not mismatches, (
        f"{len(mismatches)} grounding(s) name an element the term's ChEBI formula lacks "
        f"(#276/#278):\n  " + "\n  ".join(f"{n!r} -> {t} lacks {m}" for n, t, m in mismatches[:15]))


def test_the_detector_actually_detects():
    """Anti-vacuous. Every one of these was a real corpus error, or a real false positive
    the parser had to learn to ignore."""
    # real errors it must catch
    assert name_elements("Magnesium Sulfate Heptahydrate") - formula_elements("Al.K.2O4S")
    assert name_elements("Sodium sulfide") - formula_elements("C9H10O4")
    # correct groundings it must NOT flag
    assert not name_elements("MgSO4 x 7 H2O") - formula_elements("7H2O.Mg.O4S")
    assert not name_elements("KNO3") - formula_elements("K.NO3")
    assert not name_elements("VOSO4 x 2 H2O") - formula_elements("2H2O.O4S.OV"), \
        "V inside the token OV must be found"
    # designations that are not formulae
    assert name_elements("Vitamin B12") == set()
    assert name_elements("Thiamine (Vitamin B1)") == set()
    assert name_elements("PABA") == set(), "an all-letter acronym is not a formula"
    assert "I" not in name_elements("Fe(III) citrate"), "(III) is not iodine"


def test_the_allowlist_stays_small():
    assert len(KNOWN_NO_SALT_TERM) <= 6, "allowlist growing — investigate before adding"


def test_known_wrong_groundings_are_tracked_not_forgotten():
    """These are defects, not tolerances. If the set empties, delete it; if it grows,
    something is being swept under it."""
    assert len(KNOWN_WRONG_PENDING_279) == 2, "update #279 before changing this"
