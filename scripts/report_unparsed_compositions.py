#!/usr/bin/env python3
"""Recover ingredient lists from NBRC records whose composition was never parsed (#166).

25 records under `NBRC_*` carry their entire composition block crammed into the
first ingredient's `preferred_term`, separators stripped, plus a second empty
ingredient:

    Tryptone5gYeast extract3gNaCl10gUrea1gDistilled water1LAgar (if needed)15g

The composition is recoverable, so these are not lost records — they are
unparsed ones. #166 originally reported this as a single record; that was
measured with a regex whose `\\b` missed the concatenated cases, and it is 25.

## Splitting on the unit, not on digits

Ingredient names contain digits — `Na2HPO4`, `No. 3`, `·7H2O`, `Tween 80` — so
splitting on numbers is unsafe. The split anchors on a `<number><unit>` pair whose
unit is followed by an uppercase letter, a bracket, whitespace, or end-of-string,
which is where the next ingredient name begins.

## Three checks — and they are why this tool does not write

**Round trip.** Reassembling `name + value + unit` for every parsed item, plus the
unconsumed tail, must reproduce the original string EXACTLY. If it does, the parse
re-structured the text and invented nothing. This catches `Tween 800.3g` being read
as `Tween` + `800.3` — the rebuilt string loses the space and the mismatch shows.

**Plausibility.** Round trip is necessary but NOT sufficient: a wrong split can
also reassemble. `Tween 80` + `0.3g` and `Tween` + `800.3g` both rebuild to the
same text, and only the second is absurd. So any non-water solid above 100 g/L is
held back for a human rather than written.

**Truncated formula.** The decisive one, found by applying an earlier version of
this script and inspecting the result. `KH2PO4` + `0.85g` concatenates to
`KH2PO40.85g`, which splits equally well into `KH2PO` + `40.85g`. BOTH round-trip,
and 40.85 g/L sits under the plausibility ceiling — so the first two checks pass a
parse that writes a non-existent compound at 47x the real concentration. It
affected 11 of 20 records an earlier run rewrote, across KH2PO4, K2HPO4, CaCO3 and
H3BO3.

The flag is a formula-shaped name ending in an uppercase letter. It cannot be used
to auto-CORRECT, only to refuse, because it also matches `MgO`, which is a real
compound. That asymmetry is the whole argument: the ambiguity is chemical, and
resolving it needs the NBRC catalogue rather than a heuristic.

So this tool REPORTS and never writes. It turns 25 opaque records into a
structured worklist — proposed parse, trailing note, and the specific reason each
held record is ambiguous — for a curator to confirm against the source.

Named `report_` rather than `repair_` on purpose. This tool cannot write, and a
name promising repair is an invitation to add the write path back — which would
reintroduce exactly the defect documented above.

Usage::

    just report-unparsed-compositions
"""

from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_kinds import is_solution_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "unparsed_compositions.tsv"

_QTY_UNIT = r"\d+(?:\.\d+)?\s*(?:mg|ml|kg|g|l)(?=[A-Z(\[]|\s|$)"
MANGLED = re.compile(_QTY_UNIT + r".*?" + _QTY_UNIT)

TOKEN = re.compile(
    r"(?P<name>.+?)(?P<value>\d+(?:\.\d+)?)\s*(?P<unit>mg|ml|kg|mM|g|L|l)"
    r"(?=[A-Z(\[]|\s|$|\*)")

UNIT_TO_ENUM = {"g": "G_PER_L", "mg": "MG_PER_L", "ml": "ML_PER_L",
                "mM": "MILLIMOLAR"}

# "Distilled water1L" is the PREPARATION VOLUME the recipe is made up to, not a
# concentration. Writing it as a per-litre figure invents the exact defect #118
# documents — water recorded as a solute — and in ML_PER_L, which the
# concentration-plausibility gate does not even examine (it checks G_PER_L only).
# So a volume basis is kept as an ingredient without a concentration, and recorded
# in notes instead.
VOLUME_BASIS_UNITS = {"l", "L", "kg"}

# A non-water solid above this is almost certainly a bad split, not a recipe.
IMPLAUSIBLE_G_PER_L = 100.0

# A chemical formula whose trailing subscript has been eaten by the value.
# "KH2PO4" + "0.85g" concatenates to "KH2PO40.85g", which splits equally well as
# "KH2PO" + "40.85g" — and BOTH round-trip, so reassembly cannot tell them apart.
# The giveaway is a formula-shaped name ending in an uppercase letter.
#
# This is why the tool does not write. The rule below also flags MgO, which IS a
# real compound, so it cannot be used to auto-correct either — only to refuse.
TRUNCATED_FORMULA = re.compile(r"^[A-Z][A-Za-z0-9()·]*[A-Z]$")


def is_crammed(name: str) -> bool:
    return len(name) > 40 and bool(MANGLED.search(name))


def parse_composition(text: str) -> tuple[list[tuple[str, str, str]], str]:
    """Return (items, unconsumed_tail). Items are (name, value, unit) as written."""
    items: list[tuple[str, str, str]] = []
    pos = 0
    for m in TOKEN.finditer(text):
        items.append((m.group("name").strip(), m.group("value"), m.group("unit")))
        pos = m.end()
    return items, text[pos:]


def round_trips(text: str, items: list[tuple[str, str, str]], tail: str) -> bool:
    """The parse must reproduce the source exactly — proof it invented nothing."""
    return "".join(f"{n}{v}{u}" for n, v, u in items) + tail == text


def implausible(items: list[tuple[str, str, str]]) -> list[str]:
    bad = []
    for name, value, unit in items:
        if unit not in ("g", "kg"):
            continue
        try:
            v = float(value)
        except ValueError:
            continue
        if v > IMPLAUSIBLE_G_PER_L and "water" not in name.lower():
            bad.append(f"{name} {value}{unit}")
    return bad


def assess(doc: dict[str, Any]) -> dict[str, Any] | None:
    """Classify one record: repairable, or held back with a reason."""
    ings = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    crammed = next((i for i in ings if is_crammed(str(i.get("preferred_term") or ""))), None)
    if crammed is None:
        return None
    text = str(crammed.get("preferred_term"))
    items, tail = parse_composition(text)

    if not round_trips(text, items, tail):
        return {"verdict": "HOLD: parse does not round-trip", "items": [], "tail": tail,
                "detail": "reassembly differs from the source; the split is ambiguous "
                          "(e.g. 'Tween 800.3g' — is 80 a grade or part of the value?)"}
    bad = implausible(items)
    if bad:
        return {"verdict": "HOLD: implausible value", "items": items, "tail": tail,
                "detail": "; ".join(bad)}
    truncated = [n for n, _, _ in items if TRUNCATED_FORMULA.match(n)]
    if truncated:
        return {"verdict": "HOLD: possible truncated formula", "items": items, "tail": tail,
                "detail": f"{', '.join(truncated)} — a trailing subscript may have been "
                          f"absorbed into the value; both splits round-trip"}
    return {"verdict": "PROPOSED", "items": items, "tail": tail,
            "detail": f"{len(items)} ingredients parsed"}


def rebuild_ingredients(items: list[tuple[str, str, str]]) -> tuple[list[dict[str, Any]], list[str]]:
    """Return (ingredients, volume_basis_notes)."""
    out: list[dict[str, Any]] = []
    basis: list[str] = []
    for name, value, unit in items:
        entry: dict[str, Any] = {"preferred_term": name}
        if unit in VOLUME_BASIS_UNITS:
            basis.append(f"{name} {value}{unit}")
        else:
            enum = UNIT_TO_ENUM.get(unit)
            if enum:
                entry["concentration"] = {"value": value, "unit": enum}
        out.append(entry)
    return out, basis


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    args = ap.parse_args(argv)

    rows: list[dict[str, str]] = []
    for path in sorted(args.normalized_dir.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(doc, dict) or is_solution_record(doc):
            continue
        verdict = assess(doc)
        if verdict is None:
            continue
        rows.append({
            "file_path": str(path.relative_to(args.normalized_dir)),
            "record_id": str(doc.get("id") or ""),
            "verdict": verdict["verdict"],
            "n_recovered": str(len(verdict["items"])),
            "detail": verdict["detail"],
            "trailing_note": verdict["tail"].strip()[:120],
        })
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=[
            "file_path", "record_id", "verdict", "n_recovered", "detail", "trailing_note"])
        w.writeheader()
        w.writerows(rows)

    from collections import Counter
    tally = Counter(r["verdict"].split(":")[0] for r in rows)
    print(f"Records with an unparsed composition: {len(rows)}")
    for k, v in tally.most_common():
        print(f"  {k:8s} {v}")
    print(f"\nWrote {args.out.relative_to(REPO) if args.out.is_relative_to(REPO) else args.out}")
    print("\nREPORT ONLY — this tool deliberately does not write.")
    print("A parse can round-trip and still be wrong: 'KH2PO40.85g' splits equally")
    print("well into KH2PO4 + 0.85g and KH2PO + 40.85g. Applying the second writes")
    print("a non-existent compound at a 47x concentration. Resolving these needs the")
    print("NBRC catalogue, not a heuristic.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
