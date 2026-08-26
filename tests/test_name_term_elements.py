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

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from audit_name_term_elements import formula_elements, name_elements  # noqa: E402

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
    # MIM exact-matches CAS:13408-09-8 but has only a narrow ChEBI mapping;
    # ChEBI has the phosphate anion, not the disodium pentahydrate substance.
    ("Na2glycerophosphate x 5 H2O", "CHEBI:15978"),
    # ChEBI has the anions but no sodium salts.
    ("Na2-9,10-anthraquinone-2,6-disulfonate", "CHEBI:85112"),
    ("Sodium crotonate", "CHEBI:35899"),
}

# #279 is CLOSED. These two were grounded to the wrong SUBSTANCE -- selenate read as
# sulfate, silicate as sulfite -- the same Se/Si -> S collapse that put `H2SeO3` on
# sulfurous acid. The issue recorded that ChEBI had no term for either correct compound;
# it does: `sodium selenate` (CHEBI:77775) and `sodium silicate` (CHEBI:60720), the
# anhydrous parents. Both were re-grounded there, so the wrong-pending set is gone rather
# than emptied -- which is what its own test asked for.


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
            except Exception:  # noqa: BLE001
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
        if (name, tid) in KNOWN_NO_SALT_TERM:
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
        f"(#276/#278):\n  " + "\n  ".join(f"{n!r} -> {t} lacks {m}" for n, t, m in mismatches[:15])
    )


def test_the_detector_actually_detects():
    """Anti-vacuous. Every one of these was a real corpus error, or a real false positive
    the parser had to learn to ignore."""
    # real errors it must catch
    assert name_elements("Magnesium Sulfate Heptahydrate") - formula_elements("Al.K.2O4S")
    assert name_elements("Sodium sulfide") - formula_elements("C9H10O4")
    # correct groundings it must NOT flag
    assert not name_elements("MgSO4 x 7 H2O") - formula_elements("7H2O.Mg.O4S")
    assert not name_elements("KNO3") - formula_elements("K.NO3")
    assert not name_elements("VOSO4 x 2 H2O") - formula_elements(
        "2H2O.O4S.OV"
    ), "V inside the token OV must be found"
    # designations that are not formulae
    assert name_elements("Vitamin B12") == set()
    assert name_elements("Thiamine (Vitamin B1)") == set()
    assert name_elements("PABA") == set(), "an all-letter acronym is not a formula"
    assert "I" not in name_elements("Fe(III) citrate"), "(III) is not iodine"


def test_the_allowlist_stays_small():
    assert len(KNOWN_NO_SALT_TERM) <= 6, "allowlist growing — investigate before adding"


def test_the_se_si_collapse_is_gone_from_the_corpus():
    """#279's two wrong SUBSTANCE groundings, pinned by id rather than by a set.

    `KNOWN_WRONG_PENDING_279` used to hold them, with a test asserting it stayed at
    exactly 2 and a docstring saying to delete it if it emptied. It did: the issue
    recorded that ChEBI had no term for either correct compound, and it does --
    `sodium selenate` (CHEBI:77775) and `sodium silicate` (CHEBI:60720), the
    anhydrous parents, the same tolerance `KNOWN_NO_SALT_TERM` grants elsewhere.

    Asserting the wrong ids are ABSENT, rather than deleting the coverage along
    with the set, is what stops a future import quietly reintroducing them.

    Same line scan as the fixture above, and for the same reason: parsing both
    corpora costs ~4 minutes.
    """
    import re as _re

    PREF = _re.compile(r"^\s*-?\s*preferred_term:\s*(.+?)\s*$")
    IDL = _re.compile(r"^\s*id:\s*(CHEBI:\d+)\s*$")
    wrong = {
        "CHEBI:32586": _re.compile(r"na2seo4|selenate|seo4", _re.I),  # sodium sulfate decahydrate
        "CHEBI:86477": _re.compile(r"na2sio3|silicate|sio3", _re.I),  # sodium sulfite
        "CHEBI:140435": _re.compile(r"cholesterol", _re.I),  # deuterated standard (#305)
    }
    offenders = []
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
                    pattern = wrong.get(mi.group(1))
                    if pattern and pattern.search(name):
                        offenders.append((path.name, name, mi.group(1)))
                    name = ""
    assert not offenders, f"the Se/Si -> S collapse is back: {offenders[:5]}"
