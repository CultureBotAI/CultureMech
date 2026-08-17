#!/usr/bin/env python3
"""Flag ingredients grounded to a term that lacks an element the NAME demands (#276, #278).

Two groundings in this corpus named a completely different kind of molecule:

    Cysteine-HCl    -> CHEBI:52891  QSY9 succinimidyl ester(1+)   (a quencher dye)
    Sodium sulfide  -> CHEBI:85357  ...pyruvic acid, C9H10O4      (an organic acid)

Two independent instances is a pattern, not two typos, and both were found by hand. This
is the systematic check. Since #275 refilled `term.label` from the ontology, a wrong id no
longer looks wrong -- the label agrees with it -- so the only remaining independent signal
is the ingredient's own `preferred_term`.

Comparing NAMES does not work. `MgSO4 x 7 H2O` and `potassium aluminium sulfate` share the
word "sulfate", so word overlap passes the exact CHEBI:86463 error #257 fixed; and `KNO3`
shares no word with `potassium nitrate`, so word overlap flags a correct grounding. The
discriminator is the CATION, not the anion.

So this compares ELEMENTS. ChEBI publishes a formula per term
(`chemrof:generalized_empirical_formula`), and an ingredient name yields elements two ways:

  * as a formula -- `MgSO4 x 7 H2O` -> {Mg, S, O, H}
  * as words -- `Sodium sulfide` -> {Na, S}

An ingredient is flagged when its name demands an element the grounded term's formula does
not contain. Only elements the name states *unambiguously* count, and organics are skipped
entirely: C/H/O/N appear everywhere and carry no signal.

Read-only.

Usage::

    just audit-name-term-elements
    just audit-name-term-elements --yaml-dir data/merge_yaml/merged
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
NORMALIZED = REPO / "data" / "normalized_yaml"
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "name_term_element_mismatch.tsv"

# Element words that appear in ingredient names, mapped to their symbol. Deliberately
# limited to metals and distinctive non-metals: these are what distinguish one salt from
# another. Anions (sulfate, chloride, nitrate) are shared across unrelated compounds and
# are exactly what made word-overlap useless here.
ELEMENT_WORDS = {
    "sodium": "Na", "potassium": "K", "magnesium": "Mg", "calcium": "Ca",
    "iron": "Fe", "ferric": "Fe", "ferrous": "Fe", "zinc": "Zn", "copper": "Cu",
    "cupric": "Cu", "cuprous": "Cu", "manganese": "Mn", "manganous": "Mn",
    "cobalt": "Co", "cobaltous": "Co", "nickel": "Ni", "molybdenum": "Mo",
    "molybdate": "Mo", "tungsten": "W", "tungstate": "W", "selenium": "Se",
    "selenite": "Se", "selenate": "Se", "aluminium": "Al", "aluminum": "Al",
    "lithium": "Li", "barium": "Ba", "strontium": "Sr", "silver": "Ag",
    "boron": "B", "borate": "B", "boric": "B", "vanadium": "V", "vanadyl": "V",
    "titanium": "Ti", "chromium": "Cr", "cadmium": "Cd", "mercury": "Hg",
    "lead": "Pb", "tin": "Sn", "arsenic": "As", "arsenate": "As", "arsenite": "As",
    "tellurium": "Te", "tellurite": "Te", "bismuth": "Bi", "caesium": "Cs",
    "cesium": "Cs", "rubidium": "Rb", "ammonium": "N", "phosphate": "P",
    "phosphorus": "P", "sulfide": "S", "sulphide": "S", "sulfate": "S",
    "sulphate": "S", "thiosulfate": "S", "chloride": "Cl", "fluoride": "F",
    "bromide": "Br", "iodide": "I", "iodate": "I",
}

# Symbols we trust when parsed out of a formula-looking name. Two-letter first so `Na`
# is not read as N + a.
SYMBOLS = ["Na", "Mg", "Al", "Si", "Cl", "Ca", "Ti", "Cr", "Mn", "Fe", "Co", "Ni",
           "Cu", "Zn", "As", "Se", "Br", "Rb", "Sr", "Mo", "Ag", "Cd", "Sn", "Te",
           "Ba", "Cs", "Hg", "Pb", "Bi", "Li", "Be", "K", "V", "W", "B", "F", "I", "P", "S"]

# Elements that carry no signal: they are in almost every organic and in water.
UNINFORMATIVE = {"C", "H", "O", "N"}

FORMULAISH = re.compile(r"^[A-Za-z0-9()\[\]·.\s×x*+,'\-/%]+$")


# Names where a "symbol" is not an element: oxidation states, vitamin letters, and
# all-letter acronyms. Each of these produced false positives on the first run --
# `Fe(III) citrate` read (III) as iodine, `Vitamin B12` read B as boron, `PABA` read P
# as phosphorus. A detector whose output is mostly noise does not get read.
ROMAN = re.compile(r"\(\s*[IVX]+\s*\)")
VITAMIN = re.compile(r"(vitamin\s*[A-K]\s*\d*|^\s*[B-K]\d{1,2}\s*$)", re.I)  # incl. bare "B12"


def elements_from_formula(text: str) -> set[str]:
    """Element symbols in a formula-style ingredient name.

    Applied only to names containing a DIGIT. A real formula has one (`MgSO4`, `KNO3`),
    while all-letter acronyms like `PABA` and `PIPES` do not, and parsing those as
    formulae is how P became phosphorus.
    """
    raw = str(text or "")
    if not re.search(r"\d", raw):
        return set()
    s = ROMAN.sub(" ", raw)                                        # (II) is not iodine
    s = re.sub(r"\b\d+\s*H2O\b", "", s, flags=re.I)                 # drop waters
    s = re.sub(r"[·.]\s*\d*\s*H2O", "", s, flags=re.I)
    found = set()
    rest = s
    for sym in SYMBOLS:
        # A symbol counts only when the next character is not a lower-case letter, so
        # `Se` in `Selenite` is not read as the element inside a word.
        for m in re.finditer(rf"(?<![A-Za-z]){sym}(?![a-z])", rest):
            found.add(sym)
    return found


def elements_from_words(text: str) -> set[str]:
    lowered = str(text or "").lower()
    return {sym for word, sym in ELEMENT_WORDS.items()
            if re.search(rf"\b{word}\b", lowered)}


def name_elements(name: str) -> set[str]:
    """Elements the ingredient name unambiguously demands."""
    if VITAMIN.search(str(name or "")):
        return set()               # `Vitamin B12` / `K1` are designations, not formulae
    words = elements_from_words(ROMAN.sub(" ", str(name or "")))
    formula = elements_from_formula(name) if FORMULAISH.match(str(name or "")) else set()
    return (words | formula) - UNINFORMATIVE


ALL_SYMBOLS = set(SYMBOLS) | {"C", "H", "O", "N"}


def formula_elements(formula: str) -> set[str]:
    """Element symbols in a ChEBI generalized empirical formula, e.g. `7H2O.Mg.O4S`.

    Scanned left to right, two-letter symbol before one-letter, rather than searched
    with a lookbehind. The lookbehind version could not see `V` in `OV` -- it is
    preceded by a letter -- so every vanadyl sulfate row was reported as lacking
    vanadium against a formula that plainly contains it.
    """
    found: set[str] = set()
    text = str(formula or "")
    i = 0
    while i < len(text):
        ch = text[i]
        if not ch.isalpha():
            i += 1
            continue
        two = text[i:i + 2]
        if len(two) == 2 and two[1].islower() and two.capitalize() in ALL_SYMBOLS:
            found.add(two.capitalize())
            i += 2
            continue
        if ch.upper() in ALL_SYMBOLS and (ch.isupper() or i == 0):
            found.add(ch.upper())
        i += 1
    return found


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args(argv)

    seen: Counter = Counter()
    for path in args.yaml_dir.resolve().rglob("*.yaml"):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(doc, dict):
            continue
        groups = [doc.get("ingredients"), doc.get("composition")] + [
            s.get("composition") for s in (doc.get("solutions") or []) if isinstance(s, dict)]
        for items in groups:
            for ing in items or []:
                if not isinstance(ing, dict):
                    continue
                term = ing.get("term") or {}
                tid = str(term.get("id") or "")
                if tid.startswith("CHEBI:"):
                    seen[(str(ing.get("preferred_term") or ""), tid)] += 1

    from oaklib import get_adapter
    adapter = get_adapter("sqlite:obo:chebi")
    formulas: dict[str, str] = {}

    def formula_of(term_id: str) -> str:
        if term_id not in formulas:
            try:
                meta = adapter.entity_metadata_map(term_id) or {}
                vals = meta.get("chemrof:generalized_empirical_formula") or [""]
                formulas[term_id] = vals[0] if vals else ""
            except Exception:                                        # noqa: BLE001
                formulas[term_id] = ""
        return formulas[term_id]

    rows = []
    for (name, tid), count in seen.items():
        want = name_elements(name)
        if not want:
            continue
        formula = formula_of(tid)
        if not formula:
            continue
        have = formula_elements(formula)
        missing = want - have
        if missing:
            rows.append({"ingredient": name, "term_id": tid,
                         "term_label": adapter.label(tid) or "",
                         "term_formula": formula,
                         "name_demands": " ".join(sorted(want)),
                         "term_lacks": " ".join(sorted(missing)),
                         "rows": count})
    rows.sort(key=lambda r: -r["rows"])

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=list(rows[0]) if rows else
                           ["ingredient", "term_id", "term_lacks"])
        w.writeheader()
        w.writerows(rows)

    print(f"(name, CHEBI id) pairs checked: {len(seen)}")
    print(f"pairs where the term's formula LACKS an element the name demands: {len(rows)} "
          f"({sum(r['rows'] for r in rows)} ingredient rows)\n")
    for r in rows[:25]:
        print(f"  {r['rows']:5d}x  {r['ingredient'][:28]:30s} -> {r['term_id']:14s} "
              f"{r['term_label'][:26]:28s} lacks {r['term_lacks']}")
    try:
        shown = args.out.relative_to(REPO)
    except ValueError:
        shown = args.out
    print(f"\nWrote {shown} — read-only.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
