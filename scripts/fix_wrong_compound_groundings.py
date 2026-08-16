#!/usr/bin/env python3
"""Correct ingredient groundings that point at the wrong chemical species (#256).

Why this matters more than an ordinary grounding tidy-up
--------------------------------------------------------
kg-microbe resolves an ingredient with
``best_primary([chebi_id, culturemech_term_id, mim_id, ...])``. ``culturemech_term_id``
is populated from OUR ``term.id`` and outranks ``mim_id``, so a wrong id here overrides
MediaIngredientMech's correct one downstream and no MIM-side fix can reach it
(MediaIngredientMech#138). Our ``mediaingredientmech_chebi_term`` cannot catch it either
— it is a self-link to our own ``term.id`` in 119,577 of 120,131 rows.

Scope: only groundings where the record's OWN evidence contradicts the id. This script
deliberately does not touch the judgement calls in #256 (EDTA anion vs acid, thiamine
vs vitamin B1, vitamin B12 vs cyanocobalamin) — those need curation, not a sweep.

  ``Magnesium Sulfate Heptahydrate`` -> CHEBI:86463
      CHEBI:86463 is *potassium aluminium sulfate*. The rows carry
      ``label: magnesium sulfate heptahydrate``, ``CAS: 10034-99-8`` and ``MW: 246.47``,
      all of which are magnesium sulfate heptahydrate = CHEBI:31795. Every other name on
      CHEBI:86463 (``AlK(SO4)2``, ``Aluminum potassium sulfate``, ``KAl(SO4)2``) is
      correct and is left alone; the two sets share no record, so this is a bad id
      rather than a row-alignment slip.

  glucose -> CHEBI:42758
      CHEBI:42758 is *aldehydo-D-glucose*, the open-chain aldehyde tautomer (a fraction
      of a percent of glucose in solution). A medium calling for glucose means the
      ordinary sugar. Bare ``Glucose`` -> CHEBI:17234 (glucose); the explicitly-D names
      and ``Dextrose`` -> CHEBI:17634 (D-glucose).

Both replacement ids are the ones MediaIngredientMech already asserts, so the fix also
removes ~850 rows of divergence rather than trading one disagreement for another.

Usage::

    just fix-wrong-groundings                  # dry run, prints every change
    just fix-wrong-groundings --limit 1 --apply   # canary one record
    just fix-wrong-groundings --apply          # fan out
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
NORMALIZED = REPO / "data" / "normalized_yaml"

# (current wrong id, exact preferred_term) -> (correct id, correct label)
# Keyed on NAME AND ID together: the same wrong id also carries correctly-grounded
# names, and rewriting by id alone would corrupt them.
CORRECTIONS: dict[tuple[str, str], tuple[str, str]] = {
    ("CHEBI:86463", "Magnesium Sulfate Heptahydrate"): (
        "CHEBI:31795", "magnesium sulfate heptahydrate"),
    ("CHEBI:42758", "Glucose"):        ("CHEBI:17234", "glucose"),
    ("CHEBI:42758", "glucose"):        ("CHEBI:17234", "glucose"),
    ("CHEBI:42758", "D-Glucose"):      ("CHEBI:17634", "D-glucose"),
    ("CHEBI:42758", "D-glucose"):      ("CHEBI:17634", "D-glucose"),
    ("CHEBI:42758", "D(+)-Glucose"):   ("CHEBI:17634", "D-glucose"),
    ("CHEBI:42758", "Dextrose"):       ("CHEBI:17634", "D-glucose"),
    # PABA (#260, reported from MediaIngredientMech#138). CHEBI:194474 is
    # 4-ammoniobenzoate, the zwitterion. Every one of these rows carries
    # `CAS: 150-13-0` in its own notes, which is the neutral acid = CHEBI:30753, and
    # every one has an EMPTY term.label, so nothing on the record ever asserted the
    # zwitterion. MIM independently grounds the name to the acid across 1,968
    # occurrences.
    ("CHEBI:194474", "4-Aminobenzoic acid"): ("CHEBI:30753", "4-aminobenzoic acid"),
    ("CHEBI:194474", "p-Amino Benzoic Acid"): ("CHEBI:30753", "4-aminobenzoic acid"),
    ("CHEBI:194474", "p-amino benzoic acid"): ("CHEBI:30753", "4-aminobenzoic acid"),
    # Cysteine-HCl -> CHEBI:52891, which is `QSY9 succinimidyl ester(1+)` -- a
    # fluorescence quencher dye, not an amino acid at all. The same string is already
    # grounded to CHEBI:91247 (L-cysteine hydrochloride) in 40 other rows, and the name
    # carries no hydrate marker, so the anhydrous HCl salt is the target.
    ("CHEBI:52891", "Cysteine-HCl"): ("CHEBI:91247", "L-cysteine hydrochloride"),
    ("CHEBI:52891", "cysteine-HCl"): ("CHEBI:91247", "L-cysteine hydrochloride"),
    # Names that spell out HCl AND a hydrate, grounded to CHEBI:17561 (plain
    # L-cysteine) -- neither the salt nor the hydrate. The corpus already uses
    # CHEBI:91248 (L-cysteine hydrochloride hydrate) for this substance in 1,901 rows,
    # so this is the corpus disagreeing with itself, not a judgement call.
    ("CHEBI:17561", "L-Cysteine-HCl x H2O"): ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    ("CHEBI:17561", "Cysteine-HCl x H2O"): ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    ("CHEBI:17561", "Cysteine-HCl\u00b7H2O"): ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    ("CHEBI:17561", "L-cysteine-HCL x H2O"): ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    ("CHEBI:17561", "L-Cysteine-HCl\u00b7H2O"): ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    # --- #258: one ingredient name, several ids ---------------------------------
    # 63 names in the corpus are grounded more than one way (13,657 rows). The ones
    # below are those where the NAME ITSELF settles it: it spells out a hydrate the id
    # does not have, or names a salt where the id is the bare ion. Names that do NOT
    # specify a hydrate keep the anhydrous id -- `Na2MoO4` and `Sodium molybdate` stay
    # on CHEBI:75215, only the `2 H2O` spellings move -- so this is keyed on the exact
    # string, never on the id alone.
    # Deliberately excluded: `Vitamin B12` (cyanocobalamin vs the vitamer class, the
    # judgement call #256 defers), `Maltose` (generic vs alpha anomer), and the CaCl2 /
    # MgSO4 / MgCl2 rows naming hydrates that do not exist (`MgCl2 x 7 H2O`).

    # sodium molybdate DIhydrate
    ("CHEBI:75215", "Na2MoO4\u00b72H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:75215", "Na2MoO4 x 2 H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:75215", "Na2MoO4\u30fb2H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:75215", "Na2MoO4 . 2H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    # cobalt(2+) sulfate HEPTAhydrate -- here the MAJORITY was wrong: 1,161 rows named
    # `CoSO4 x 7 H2O` sat on the anhydrous id and only 5 on the heptahydrate.
    ("CHEBI:53470", "CoSO4 x 7 H2O"): ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    ("CHEBI:53470", "CoSO4\u00b77H2O"): ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    ("CHEBI:53470", "CoSO4\u30fb7H2O"): ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    ("CHEBI:53470", "CoSO4 . 7H2O"): ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    # magnesium sulfate HEPTAhydrate
    ("CHEBI:32599", "MgSO4\u00b77H2O"): ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    # disodium selenite PENTAhydrate
    ("CHEBI:48843", "Na2SeO3 x 5 H2O"): ("CHEBI:131361", "disodium selenite pentahydrate"),
    ("CHEBI:48843", "Na2SeO3\u30fb5H2O"): ("CHEBI:131361", "disodium selenite pentahydrate"),
    ("CHEBI:48843", "Na2SeO3\u00b75H2O"): ("CHEBI:131361", "disodium selenite pentahydrate"),
    ("CHEBI:48843", "Na2SeO3.5H2O"): ("CHEBI:131361", "disodium selenite pentahydrate"),
    # iron(2+) sulfate HEPTAhydrate
    ("CHEBI:75832", "FeSO4 x 7H2O"): ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    ("CHEBI:75832", "Iron (II) sulfate heptahydrate"): (
        "CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    # magnesium dichloride HEXAhydrate
    ("CHEBI:6636", "MgCl2 x 6 H2O"): ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    ("CHEBI:6636", "MgCl2x 6 H2O"): ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    ("CHEBI:6636", "MgCl2 x 6H2O"): ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    # `Starch` grounded to gellan gum -- a different polysaccharide entirely. The rows
    # actually named `Gelrite` / `Gellan Gum` stay on CHEBI:85248, correctly.
    ("CHEBI:85248", "Starch"): ("CHEBI:28017", "starch"),
    # KNO3 is the salt, CHEBI:17632 is the bare nitrate ION.
    ("CHEBI:17632", "KNO3"): ("CHEBI:63043", "potassium nitrate"),
    # zwitterion ids for names that state the neutral compound
    ("CHEBI:57305", "Glycine"): ("CHEBI:15428", "glycine"),
    ("CHEBI:35235", "L-Cysteine"): ("CHEBI:17561", "L-cysteine"),
    # the tri-anion vs the neutral salt
    ("CHEBI:4991", "Fe(III) citrate"): ("CHEBI:144421", "iron(III) citrate"),
    # Dextrose IS D-glucose, by definition. It was split three ways.
    ("CHEBI:17234", "Dextrose"): ("CHEBI:17634", "D-glucose"),
    ("CHEBI:4167", "Dextrose"): ("CHEBI:17634", "D-glucose"),
    # `Sodium citrate` with no hydrate marker, sitting on the dihydrate. The rows that
    # DO say dihydrate stay on CHEBI:32142.
    ("CHEBI:32142", "Sodium citrate"): ("CHEBI:53258", "sodium citrate"),
    ("CHEBI:32142", "Sodium Citrate"): ("CHEBI:53258", "sodium citrate"),
    ("CHEBI:32142", "sodium citrate"): ("CHEBI:53258", "sodium citrate"),
    # one stray row against the 470-row majority
    ("FOODON:03420180", "Pancreatic digest of casein"): ("MICRO:0000182", "tryptone"),
    # --- #259: hydration mismatches the LABEL DRIFT was hiding ---------------------
    # Found by comparing each ingredient's NAME against its grounded term's real CHEBI
    # label. #258-class errors in spellings that sweep missed -- and they matter here
    # because refilling term.label from the ontology would have made the label agree
    # with the wrong id, destroying the only visible signal that it was wrong.
    ("CHEBI:64734", "Na2-EDTA x 2 H2O"): ("CHEBI:64758", "EDTA disodium salt dihydrate"),
    ("CHEBI:64734", "Na-EDTA x 2 H2O"): ("CHEBI:64758", "EDTA disodium salt dihydrate"),
    ("CHEBI:64734", "Na2-EDTA\u00b72H2O"): ("CHEBI:64758", "EDTA disodium salt dihydrate"),
    ("CHEBI:87014", "VOSO4 x 2 H2O"): ("CHEBI:87009", "vanadyl sulfate dihydrate"),
    ("CHEBI:75215", "Na2MoO4 \u00b7 2H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:75215", "Na2MoO4 x 2H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:75215", "Na2MoO4. 2H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:76208", "Sodium sulfide nonahydrate"): ("CHEBI:76209", "sodium sulfide nonahydrate"),
    ("CHEBI:63675", "Sodium succinate dibasic hexahydrate"): (
        "CHEBI:63686", "sodium succinate hexahydrate"),
    # NOT fixed: `FeSO4 x 6 H2O` / `x 5 H2O` (18 rows) and `VOSO4 x 5 H2O` -- CHEBI has
    # no term for those hydrates, and they are likelier transcription errors for the
    # heptahydrate than real formulations. Left for curation.
}


PREFERRED = re.compile(r"^\s*-?\s*preferred_term:\s*(.+?)\s*$")
ID_LINE = re.compile(r"^(\s*)id:\s*(\S+)\s*$")
LABEL_LINE = re.compile(r"^(\s*)label:\s*")


def _unquote(s: str) -> str:
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "'\"":
        return s[1:-1].replace("''", "'") if s[0] == "'" else s[1:-1]
    return s


def fix_text(text: str) -> tuple[str, list[tuple[str, str, str]]]:
    """Rewrite only the id/label lines that need it, leaving the file otherwise byte-identical.

    A YAML round-trip was the obvious implementation and the wrong one: re-dumping
    reflows every long `notes:` string in the record, so a one-id change arrives as a
    67-line diff and the real edit is invisible in review. This walks lines instead.

    Correction is keyed on the enclosing ingredient's `preferred_term` AND the id, never
    the id alone — CHEBI:86463 is also carried, correctly, by `AlK(SO4)2`. Both the
    `term` block and a `mediaingredientmech_chebi_term` self-link move together; leaving
    the latter on the old id would turn a stale field into a contradictory one.
    """
    lines = text.splitlines(keepends=True)
    out = list(lines)
    changes: list[tuple[str, str, str]] = []
    name = ""
    pending: tuple[str, str] | None = None   # (indent, new_label) for the next label line
    for n, line in enumerate(lines):
        m = PREFERRED.match(line)
        if m:
            name = _unquote(m.group(1))
            pending = None
            continue
        mi = ID_LINE.match(line)
        if mi:
            repl = CORRECTIONS.get((mi.group(2), name))
            pending = None
            if repl:
                new_id, new_label = repl
                out[n] = f"{mi.group(1)}id: {new_id}\n"
                changes.append((name, mi.group(2), new_id))
                pending = (mi.group(1), new_label)
            continue
        if pending:
            ml = LABEL_LINE.match(line)
            if ml and ml.group(1) == pending[0]:
                out[n] = f"{pending[0]}label: {pending[1]}\n"
            pending = None
    return "".join(out), changes


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true",
                    help="Write the corpus. Default is a dry run.")
    ap.add_argument("--limit", type=int, default=0,
                    help="Stop after N changed records (canary).")
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED)
    args = ap.parse_args(argv)

    tally: Counter[tuple[str, str, str]] = Counter()
    touched = 0
    for path in sorted(args.yaml_dir.resolve().rglob("*.yaml")):
        try:
            text = path.read_text(errors="replace")
        except OSError:
            continue
        # Cheap prefilter — the vast majority of records carry neither wrong id.
        if not any(bad in text for bad in {k[0] for k in CORRECTIONS}):
            continue
        new_text, changes = fix_text(text)
        if not changes:
            continue
        # Re-parse defensively: a line-level edit must still leave valid YAML.
        try:
            yaml.safe_load(new_text)
        except yaml.YAMLError as exc:
            print(f"  SKIP {path.relative_to(REPO)} — edit would break YAML: {exc}",
                  file=sys.stderr)
            continue
        touched += 1
        tally.update(changes)
        try:
            rel = path.relative_to(REPO)
        except ValueError:
            rel = path            # --yaml-dir may be relative or outside the repo
        for name, old, new in changes:
            print(f"  {rel}: {name!r} {old} -> {new}")
        if args.apply:
            path.write_text(new_text)
        if args.limit and touched >= args.limit:
            break

    print(f"\n{'Corrected' if args.apply else 'Would correct'} "
          f"{sum(tally.values())} ingredient row(s) in {touched} record(s):")
    for (name, old, new), n in tally.most_common():
        print(f"  {n:5d}x  {name!r}  {old} -> {new}")
    if not args.apply:
        print("\nDry run — nothing written. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
