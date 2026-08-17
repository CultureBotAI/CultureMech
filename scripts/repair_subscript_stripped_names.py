#!/usr/bin/env python3
"""Restore digits lost from formula ingredient names (#276 item 3).

Some `preferred_term` values are unreadable as chemistry because their subscripts are
gone: `H BO` for H3BO3, `Na WO .2H O` for Na2WO4·2H2O. The gap where each digit was is
still there, which is what makes the reconstruction determinate rather than a guess.

It is not a uniform strip. `MgSO .7H2O` keeps the `2` in `H2O` but loses the `4`, so
ASCII digits survived while subscript characters (₂₃₄) did not -- an encoding step, not a
parser. Whatever did it is upstream and still unfixed; this repairs the damage it left.

Each repair is listed EXPLICITLY rather than inferred by rule. A rule that guessed
subscripts would be wrong exactly where it mattered: `Na VO` is either Na3VO4
(orthovanadate) or NaVO3 (metavanadate), the corpus gives no way to tell, and it is
deliberately NOT repaired here.

Where a name is grounded, the grounded term corroborates the reconstruction -- `As O` sits
on `diarsenic trioxide`, which is As2O3 -- so these are not read off the formula alone.

The corrupted original is preserved in `notes`. The source string is otherwise
unrecoverable, and a reader should be able to see that the name was repaired rather than
transcribed.

Read-only by default; `--apply` writes via record_io with a curation event.

Usage::

    just repair-subscript-names                    # report
    just repair-subscript-names --limit 1 --apply  # canary
    just repair-subscript-names --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

from record_io import write_record  # noqa: E402

from culturemech.curate.curation_event import record_curation_event  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"

# corrupted name -> (repaired name, what corroborates it)
REPAIRS: dict[str, tuple[str, str]] = {
    "H BO":                 ("H3BO3", "grounded to boric acid (CHEBI:33118)"),
    "As O":                 ("As2O3", "grounded to diarsenic trioxide (CHEBI:30621)"),
    "LiCl.H O":             ("LiCl.H2O", "grounded to lithium chloride (CHEBI:48607)"),
    "Co(NO ) .6H O":        ("Co(NO3)2.6H2O", "grounded to cobalt dinitrate hexahydrate"),
    "Na WO .2H O":          ("Na2WO4.2H2O", "grounded to sodium tungstate dihydrate"),
    "MnSO .H O":            ("MnSO4.H2O", "manganese(II) sulfate monohydrate"),
    "Ca(NO ) .4H O":        ("Ca(NO3)2.4H2O", "calcium nitrate tetrahydrate"),
    "Fe(NH ) (SO ) .6H O":  ("Fe(NH4)2(SO4)2.6H2O", "ferrous ammonium sulfate hexahydrate"),
    "Na SO .10H O":         ("Na2SO4.10H2O", "sodium sulfate decahydrate"),
    "K SO":                 ("K2SO4", "potassium sulfate"),
    "K CO":                 ("K2CO3", "potassium carbonate"),
    # NOT repaired: `Na VO` -- Na3VO4 (ortho) and NaVO3 (meta) are both plausible and
    # the corpus does not disambiguate. Guessing here would be the same class of error
    # this file exists to undo.
}

NOTE = ("Name repaired (#276): the source string `{old}` had lost its subscript digits; "
        "restored to `{new}` — {why}.")


def repair_doc(doc: dict[str, Any]) -> list[tuple[str, str]]:
    """Rewrite corrupted names in place. Returns (old, new) per change."""
    changed: list[tuple[str, str]] = []
    groups = [doc.get("ingredients"), doc.get("composition")] + [
        s.get("composition") for s in (doc.get("solutions") or []) if isinstance(s, dict)]
    for items in groups:
        if not isinstance(items, list):
            continue
        for ing in items:
            if not isinstance(ing, dict):
                continue
            old = str(ing.get("preferred_term") or "")
            repl = REPAIRS.get(old)
            if not repl:
                continue
            new, why = repl
            ing["preferred_term"] = new
            note = NOTE.format(old=old, new=new, why=why)
            existing = str(ing.get("notes") or "").strip()
            ing["notes"] = f"{existing} {note}".strip() if existing else note
            changed.append((old, new))
    return changed


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED)
    args = ap.parse_args(argv)

    from collections import Counter
    tally: Counter = Counter()
    touched = 0
    for path in sorted(args.yaml_dir.resolve().rglob("*.yaml")):
        try:
            text = path.read_text(errors="replace")
        except OSError:
            continue
        if not any(bad in text for bad in REPAIRS):
            continue
        try:
            doc = yaml.safe_load(text)
        except yaml.YAMLError:
            continue
        if not isinstance(doc, dict):
            continue
        changed = repair_doc(doc)
        if not changed:
            continue
        touched += 1
        tally.update(changed)
        print(f"  {path.name[:44]:46s} " + ", ".join(f"{o!r}->{n!r}" for o, n in changed)[:60])
        if args.apply:
            record_curation_event(
                doc, curator="repair_subscript_stripped_names.py",
                action="REPAIRED_SUBSCRIPT_STRIPPED_NAME",
                notes=("Restored digits lost from formula ingredient name(s) by an "
                       "upstream encoding step (#276): "
                       + "; ".join(f"{o} -> {n}" for o, n in changed)
                       + ". The corrupted original is preserved in each ingredient's notes."),
                changes=f"{len(changed)} preferred_term(s) repaired")
            write_record(path, doc)
        if args.limit and touched >= args.limit:
            break

    print(f"\n{'Repaired' if args.apply else 'Would repair'} {sum(tally.values())} name(s) "
          f"in {touched} record(s):")
    for (old, new), n in tally.most_common():
        print(f"  {n:4d}x  {old!r} -> {new!r}")
    if not args.apply:
        print("\nReport only. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
