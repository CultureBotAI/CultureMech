#!/usr/bin/env python3
"""Report media named for a selective agent their composition omits (#181).

An antibiotic-selective medium whose composition has no antibiotic is a real
defect: the record asserts a formulation that is not the medium it names, so
growth inference, grounding and axis classification all get a confident wrong
answer with no signal.

## What "composition" means here — the correction that halved this audit twice

A stock-supplied antibiotic is recorded as a SOLUTION, not an ingredient.
`lb_rifampicin_medium` carries "Rifampicin solution (50 mg/ml)*" under
`solutions`, and its `ingredients` really are just plain LB. An earlier version of
this script checked only `ingredients` and reported 17 records; 15 were FALSE
POSITIVES on exactly that basis.

That mattered beyond the count. The Edison axis probe which prompted #181 declined
to classify `lb_rifampicin_medium` as SELECTIVE, saying "the supplied ingredient
list contains no rifampicin entry". That was accurate about the ingredient list it
was handed — which is precisely the slot the research template passes. The record
was not defective; the VIEW of it was partial, and this script reproduced the same
partial view before concluding the corpus was broken.

`composition_terms()` therefore spans `ingredients`, `solutions`, and the nested
`solutions[].composition`. Current baseline: **2** records, both DSMZ Medium 309
reached via two sources. Neither has a `solutions` entry, and the local mediadive
extraction of medium 309 lacks the neomycin too — so the gap is upstream, not in
this import, and is not locally recoverable.

## REPORT ONLY

Recovering a lost concentration needs the upstream record, and a plausible guess
that round-trips and validates is still false chemistry (#166). Where the source
kept a concentration in the NAME ("LB + 50 ug/ml Kanamycin medium"), it is
surfaced in `named_conc` for a curator — surfaced, not applied.

## Traps, each hit while building this

  * Match on WORD BOUNDARIES. A substring matcher reported 28 because `streptomyc`
    matches the GENUS *Streptomyces* and `bile` matches
    `alkalispirillum_mobile_medium`. Sixteen of the twenty-eight were artifacts.
  * "A or B" names an either/or formulation. The record holds one alternative and
    is complete, so it is suppressed — but only when at least one named agent is
    actually present.
  * A concentration belongs to the agent in ITS OWN name segment. A character
    window reached across the comma and reported `ampicillin=50 ug/ml` for a name
    reading "...Kanamycin, 100 ug/ml Ampicillin" (#188).
  * Presence in a name proves the agent belongs; ABSENCE from a finite agent list
    proves nothing. This bounds a known family; `--max-allowed 0` would be a claim
    this script cannot support.

Usage::

    just audit-selective-agent-mismatch
    just audit-selective-agent-mismatch --max-allowed 2    # current baseline
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
DEFAULT_OUT = REPO / "data" / "import_tracking" / "reports" / "selective_agent_mismatch.tsv"

# Agents whose presence makes a medium selective, and whose absence from the
# composition is therefore a defect rather than a detail. Each entry is
# (label, regex) and every regex is applied with \b...\b anchors.
#
# NOT included, deliberately: "streptomycin" is here but the genus *Streptomyces*
# is not an agent — word boundaries separate them, which is the whole reason this
# is a list of anchored patterns rather than substrings.
SELECTIVE_AGENTS: list[tuple[str, str]] = [
    # "Ampicilin" (one L) appears twice in source names — a misspelling upstream,
    # not something to normalise away, since the name is the evidence.
    ("ampicillin", r"ampicill?in"),
    ("carbenicillin", r"carbenicillin"),
    ("cefpodoxime", r"cefpodoxime"),
    ("chloramphenicol", r"chloramphenicol"),
    ("ciprofloxacin", r"ciprofloxacin"),
    ("cycloheximide", r"cycloheximide"),
    ("erythromycin", r"erythromycin"),
    ("gentamicin", r"gentamic[iy]n"),
    ("hygromycin", r"hygromycin"),
    ("kanamycin", r"kanamycin"),
    ("nalidixic acid", r"nalidixic"),
    ("neomycin", r"neomycin"),
    ("novobiocin", r"novobiocin"),
    ("nystatin", r"nystatin"),
    ("penicillin", r"penicillin"),
    ("polymyxin", r"polymyxin"),
    # "rifampin" is the US generic name (USAN) for rifampicin (INN), not a typo.
    ("rifampicin", r"(?:rifampicin|rifampin)"),
    ("spectinomycin", r"spectinomycin"),
    ("streptomycin", r"streptomycin"),
    ("tetracycline", r"tetracyclines?"),
    ("trimethoprim", r"trimethoprim"),
    ("vancomycin", r"vancomycin"),
    ("bile salts", r"bile"),
    ("crystal violet", r"crystal violet"),
    ("brilliant green", r"brilliant green"),
    ("malachite green", r"malachite green"),
    ("sodium azide", r"azide"),
    ("potassium tellurite", r"tellurite"),
    ("thallous acetate", r"thallous"),
]

# Name separators. A concentration belongs to the agent in ITS OWN segment; the
# comma in "50 ug/ml Kanamycin, 100 ug/ml Ampicillin" is what keeps the two apart.
#
# "/" is NOT a separator: units are written "ug/ml", so splitting on it turns
# every concentration into "50 ug" + "ml" and the column silently empties.
_SEGMENT = re.compile(r"\s*(?:[,;+]|\band\b)\s*", re.I)

# An either/or formulation: the record holds one alternative, not both.
_EITHER_OR = re.compile(r"\bor\b", re.I)

# "50 ug/ml Kanamycin", "Kanamycin (100 mg/l)", "0.5% bile"
_CONC = r"\d+(?:\.\d+)?\s*(?:%|ug/ml|µg/ml|mg/ml|mg/l|g/l|u/ml)"


def composition_terms(doc: dict[str, Any]) -> list[str]:
    """Every term naming something actually IN the medium.

    Must span `ingredients` AND `solutions`, and the nested `solutions[].composition`.
    Checking only `ingredients` reported 15 false positives out of 17: an
    antibiotic supplied as a stock is recorded as a SOLUTION, so
    `lb_rifampicin_medium` carries "Rifampicin solution (50 mg/ml)*" under
    `solutions` and reads as antibiotic-free if you look only at `ingredients`.

    The Edison probe that started #181 said "the supplied ingredient list contains
    no rifampicin entry" — accurate about the ingredient list it was given, which
    is exactly the slot the research template passes. The record was not defective;
    the view of it was partial.
    """
    terms: list[str] = []
    for ing in doc.get("ingredients") or []:
        if isinstance(ing, dict):
            terms.append(str(ing.get("preferred_term") or ""))
    for sol in doc.get("solutions") or []:
        if not isinstance(sol, dict):
            continue
        terms.append(str(sol.get("preferred_term") or ""))
        for sub in sol.get("composition") or []:
            if isinstance(sub, dict):
                terms.append(str(sub.get("preferred_term") or ""))
    return [t for t in terms if t]


def _compiled() -> list[tuple[str, re.Pattern[str]]]:
    return [(label, re.compile(rf"\b{rx}\b", re.I)) for label, rx in SELECTIVE_AGENTS]


def named_concentration(name: str, agent_rx: re.Pattern[str]) -> str:
    """A concentration attached to THIS agent in the NAME, if the source kept one.

    "LB + 50 ug/ml Kanamycin medium" is the useful case: the value survived in the
    name even though it never reached `ingredients`, so it is recoverable from
    tracked data rather than invented.

    Scoped to the name SEGMENT holding the agent, not a character window. A window
    reaches across separators and picks up the neighbouring agent's value —
    "LB + 50 ug/ml Kanamycin, 100 ug/ml Ampicillin" yielded `ampicillin=50 ug/ml`
    (#188). That is the #166 failure inside the very tool meant to prevent it: a
    plausible, confident, wrong concentration presented as recovered fact.

    Returns "" when the segment carries no concentration. Silence is the correct
    answer; a guess is not.
    """
    for segment in _SEGMENT.split(name):
        if agent_rx.search(segment):
            found = re.search(_CONC, segment, re.I)
            return found.group(0) if found else ""
    return ""


def audit_parsed(records: list[tuple[str, dict[str, Any]]]) -> list[dict[str, str]]:
    """Pure function over already-parsed records, so tests need no fixture files."""
    agents = _compiled()
    rows: list[dict[str, str]] = []
    for rel, doc in records:
        if not isinstance(doc, dict) or is_solution_record(doc):
            continue
        name = f"{doc.get('name') or ''} {doc.get('original_name') or ''}".strip()
        ingredients = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
        ing_text = " ".join(composition_terms(doc))
        missing, concs = [], []
        present = False
        for label, rx in agents:
            in_name, in_ings = bool(rx.search(name)), bool(rx.search(ing_text))
            if in_name and in_ings:
                present = True
            elif in_name:
                missing.append(label)
                conc = named_concentration(name, rx)
                if conc:
                    concs.append(f"{label}={conc}")

        # "M2SGC broth containing tetracycline (10 ug/ml) OR rifampin (100 ug/ml)"
        # names an either/or formulation, not a recipe holding both. The record is
        # the tetracycline variant and is complete; rifampin is the documented
        # alternative, so reporting it missing is a false positive.
        #
        # Requires at least one named agent to be PRESENT — a record naming "A or B"
        # with neither in its composition is still defective, and still reported.
        if missing and present and _EITHER_OR.search(name):
            continue

        if missing:
            rows.append({
                "file_path": rel,
                "record_id": str(doc.get("id") or ""),
                "name": str(doc.get("original_name") or doc.get("name") or ""),
                "missing_agents": "; ".join(missing),
                "named_conc": "; ".join(concs),
                "n_ingredients": str(len(ingredients)),
            })
    rows.sort(key=lambda r: r["file_path"])
    return rows


def collect(normalized: Path = NORMALIZED) -> list[dict[str, str]]:
    records = []
    for path in sorted(normalized.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        records.append((str(path.relative_to(normalized)), doc))
    return audit_parsed(records)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    ap.add_argument("--out", type=Path, default=DEFAULT_OUT)
    ap.add_argument("--max-allowed", type=int, default=None,
                    help="Exit 1 if more than N records are affected. Baseline gate: "
                         "holds the line without demanding the backlog be fixed first.")
    args = ap.parse_args(argv)

    rows = collect(args.normalized_dir)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, delimiter="\t", fieldnames=[
            "file_path", "record_id", "name", "missing_agents", "named_conc",
            "n_ingredients"])
        w.writeheader()
        w.writerows(rows)

    print(f"Media named for a selective agent absent from their ingredients: {len(rows)}")
    recoverable = [r for r in rows if r["named_conc"]]
    if recoverable:
        print(f"  of which the NAME still carries a concentration: {len(recoverable)}"
              f" (recoverable from tracked data, not invented)")
    for r in rows:
        print(f"  {r['file_path'][:52]:54s} {r['missing_agents'][:34]:36s} "
              f"{r['named_conc'][:24]}")
    print(f"\nWrote {args.out.relative_to(REPO) if args.out.is_relative_to(REPO) else args.out}")

    if args.max_allowed is not None and len(rows) > args.max_allowed:
        print(f"\nFAIL: {len(rows)} affected records exceeds --max-allowed "
              f"{args.max_allowed}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
