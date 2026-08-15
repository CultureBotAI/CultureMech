#!/usr/bin/env python3
"""Nest a flattened stock cocktail under its solution, using MediaDive (#150).

A flattened cocktail is a stock trace/vitamin solution whose components were written
into a medium's `ingredients:` at STOCK strength. Read as final per-litre values
those are implausible (~1000x high). The repair moves them under a `solutions:`
entry carrying the addition volume, so the real final concentration is recoverable
as `stock_conc x addition_volume / stock_prepared_in`.

Both halves come from MediaDive (`just fetch-mediadive-volumes`), so nothing is
invented: the stock's composition, and the volume it is added at.

## The safety property: match on NAME **and** VALUE

A stock's component list overlaps the medium's own bulk ingredients. Wolfe's mineral
elixir contains MgSO4 30, NaCl 10, CaCl2 1 g/l; `aciduliprofundum_medium` separately
carries main-solution NaCl 39.97, MgSO4 33.4965, CaCl2 1.37962. Matching by NAME
alone would move the medium's bulk salts into the trace cocktail and destroy the
recipe.

So an ingredient is moved only when its name matches a stock component AND its value
equals that component's stock value (exact, after float normalisation). That is what
identifies it as the flattened stock entry rather than a legitimate bulk ingredient
that happens to share a name. Anything else is left exactly where it is.

Additional guards, each refusing rather than guessing:
  * only ingredients the audit already FLAGGED are eligible;
  * a record whose flagged rows do not all match is reported and skipped whole —
    partial nesting would leave a half-repaired recipe;
  * a record that already has a `solutions:` block is skipped (not a flattened
    cocktail by definition).

Report-only by default; `--apply` writes via record_io with a curation event.

Usage::

    just apply-cocktail-nesting                    # report what would change
    just apply-cocktail-nesting --limit 1 --apply  # canary one record
    just apply-cocktail-nesting --apply            # the eligible set
"""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import audit_concentration_plausibility as acp  # noqa: E402
from record_io import write_record  # noqa: E402

from culturemech.curate.curation_event import record_curation_event  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
VOLUMES = REPO / "data" / "import_tracking" / "reports" / "mediadive_solution_volumes.json"
KOMODO_VOLUMES = REPO / "data" / "import_tracking" / "reports" / "komodo_base_volumes.json"
# Stocks whose composition AND volume were read from a primary source, for records
# MediaDive cannot serve. Tracked curated research, not a regenerable cache.
RESEARCHED = REPO / "data" / "import_tracking" / "researched_stock_volumes.json"
# The full flattened-cocktail list, so --use-researched can reach records MediaDive
# returned nothing for (those are absent from VOLUMES entirely).
PROPOSALS = REPO / "data" / "import_tracking" / "reports" / "cocktail_nesting_proposals.tsv"


def _num(value: Any) -> float | None:
    try:
        return float(str(value).strip())
    except (TypeError, ValueError):
        return None


def _key(name: str) -> str:
    """Compare ingredient names ignoring case and whitespace only.

    Deliberately NOT fuzzy: "MgSO4 x 7 H2O" and "MgSO4" are different compounds
    (hydrate vs anhydrous) and must not collapse onto each other.
    """
    return " ".join(str(name or "").split()).lower()


def match_components(ingredients: list[dict[str, Any]],
                     stock_components: list[dict[str, Any]],
                     flagged_names: set[str]) -> tuple[list[int], list[str]]:
    """Indices of ingredients that ARE this stock's flattened components.

    Requires name match AND value match against the stock's g/l, and that the audit
    flagged the ingredient. Returns (indices, unmatched_flagged_names).
    """
    stock_by_name: dict[str, float | None] = {}
    for c in stock_components:
        v = _num(c.get("g_l"))
        if v is None:
            v = _num(c.get("amount"))
        stock_by_name[_key(c.get("compound"))] = v

    indices: list[int] = []
    matched_names: set[str] = set()
    for i, ing in enumerate(ingredients):
        name = _key(ing.get("preferred_term"))
        if name not in flagged_names:
            continue                      # only audit-flagged rows are eligible
        if name not in stock_by_name:
            continue
        want, got = stock_by_name[name], _num((ing.get("concentration") or {}).get("value"))
        if want is None or got is None or abs(want - got) > 1e-9:
            continue                      # same name, different value: a bulk ingredient
        indices.append(i)
        matched_names.add(name)
    return indices, sorted(flagged_names - matched_names)


def match_stock_signature(ingredients: list[dict[str, Any]],
                          stock_components: list[dict[str, Any]],
                          flagged_names: set[str],
                          min_components: int = 4) -> tuple[list[int], list[str]]:
    """Indices of ingredients that reproduce this stock's composition at stock values.

    Unlike `match_components`, this does NOT require every moved row to be flagged.
    A stock's sub-threshold components never trip the audit — SL-10 carries ZnCl2 at
    0.07 g/l and H3BO3 at 0.006, far below the flagging cutoff — so requiring the
    flag would move FeCl2 (1.5) alone and strand the other eight in `ingredients`.
    That is a half-repair: the stock would exist in two places at once.

    The evidence bar is raised instead of lowered. Reproducing four or more of a
    stock's components at EXACTLY its concentrations is far stronger than three
    flagged rows — 98 records match SL-10 on 8 or 9 of 9. At least one matched row
    must still be flagged, so only records the audit calls broken are touched.

    Returns (indices, unmatched_flagged_names) like `match_components`.
    """
    want: dict[str, float] = {}
    for c in stock_components:
        v = _num(c.get("g_l"))
        if v is None:
            v = _num(c.get("amount"))
        if v is not None:
            want[_key(c.get("compound"))] = v

    indices, matched = [], set()
    for i, ing in enumerate(ingredients):
        name = _key(ing.get("preferred_term"))
        got = _num((ing.get("concentration") or {}).get("value"))
        if name in want and got is not None and abs(want[name] - got) < 1e-9:
            indices.append(i)
            matched.add(name)

    if len(indices) < min_components or not (matched & flagged_names):
        return [], sorted(flagged_names)
    return indices, sorted(flagged_names - matched)


def find_summed(ingredients: list[dict[str, Any]], additions: list[dict[str, Any]],
                unmatched: list[str]) -> dict[str, list[tuple[str, float]]]:
    """Unmatched rows whose value is the exact SUM of that component across stocks.

    When a medium references two stocks that share a component, the flattening added
    them together into one ingredient: `chrysiogenes_medium` carries pyridoxine 0.4,
    which is Wolin's 0.1 + Seven vitamins 0.3. Neither stock matches 0.4, so the
    plain name+value pass correctly refuses it — but the decomposition is recoverable,
    because it is arithmetic over the specific stocks THIS medium references, checked
    to exact equality.

    Returns {ingredient_name: [(solution_name, stock_value), ...]} for the rows where
    the sum reconciles, and nothing for any row where it does not.
    """
    by_name = {_key(i.get("preferred_term")): _num((i.get("concentration") or {}).get("value"))
               for i in ingredients}
    contributions: dict[str, list[tuple[str, float]]] = {}
    for add in additions:
        for c in add.get("stock_components") or []:
            v = _num(c.get("g_l"))
            if v is None:
                continue
            contributions.setdefault(_key(c.get("compound")), []).append(
                (str(add.get("solution_name")), v))

    out = {}
    for name in unmatched:
        parts = contributions.get(name, [])
        got = by_name.get(name)
        if len(parts) >= 2 and got is not None and abs(sum(v for _, v in parts) - got) < 1e-9:
            out[name] = parts
    return out


def plan_record(path: Path, doc: dict[str, Any], additions: list[dict[str, Any]],
                flagged_names: set[str], split_summed: bool = False) -> dict[str, Any] | None:
    """What nesting this record would do, or None when it is not safely nestable.

    Handles EVERY stock the medium references, not just the first. A medium commonly
    carries a trace-element stock and a vitamin stock, and their components are
    flattened together into one ingredient list; nesting only the first would leave
    the vitamins stranded and the record half-repaired.
    """
    if doc.get("solutions"):
        return None                        # already structured; not a flattened cocktail
    ingredients = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]

    groups: list[dict[str, Any]] = []
    claimed: set[int] = set()
    for addition in additions:
        matcher = (match_stock_signature if addition.get("match_full_signature")
                   else match_components)
        indices, _ = matcher(
            ingredients, addition.get("stock_components") or [], flagged_names)
        indices = [i for i in indices if i not in claimed]   # never move one twice
        if not indices:
            continue
        claimed.update(indices)
        groups.append({
            "indices": indices,
            "solution_name": addition.get("solution_name"),
            "addition_volume_ml": addition.get("addition_volume_ml"),
            "stock_prepared_in_ml": addition.get("stock_prepared_in_ml"),
            "moved": [ingredients[i].get("preferred_term") for i in indices],
            # Researched stocks carry a citation; MediaDive-sourced ones do not. The
            # provenance note must say which, or the record claims MediaDive supplied
            # a figure it never did.
            "citation": addition.get("citation"),
            "volume_basis": addition.get("volume_basis"),
            "volume_support": addition.get("volume_support"),
            "volume_counterevidence": addition.get("volume_counterevidence"),
            "researched_on": addition.get("researched_on"),
        })
    # NOTE: the "nothing to do" check happens AFTER the split pass below, not here.
    # A record can have no direct name+value match at all and still be repairable —
    # when every flagged row was summed across two stocks, which is exactly the case
    # the split exists for. Returning early here refused those records outright.
    matched_names = {_key(ingredients[i].get("preferred_term")) for i in claimed}
    unmatched = sorted(flagged_names - matched_names)

    # Rows the flattening SUMMED across two stocks are recoverable by arithmetic.
    splits: dict[str, list[tuple[str, float]]] = {}
    if split_summed and unmatched:
        splits = find_summed(ingredients, additions, unmatched)
        if splits:
            idx_by_name = {_key(i.get("preferred_term")): n for n, i in enumerate(ingredients)}
            for name in splits:
                claimed.add(idx_by_name[name])
            unmatched = [u for u in unmatched if u not in splits]

            # A stock may contribute ONLY summed rows — every one of its components
            # was merged into another stock's entry, so the name+value pass created
            # no group for it. Without a group its share of the split is dropped and
            # the record silently loses that stock entirely, which is worse than not
            # splitting at all. Give each contributing stock a group.
            have = {g["solution_name"] for g in groups}
            by_solution = {a.get("solution_name"): a for a in additions}
            for parts in splits.values():
                for solution_name, _value in parts:
                    if solution_name in have:
                        continue
                    add = by_solution.get(solution_name) or {}
                    groups.append({
                        "indices": [],
                        "solution_name": solution_name,
                        "addition_volume_ml": add.get("addition_volume_ml"),
                        "stock_prepared_in_ml": add.get("stock_prepared_in_ml"),
                        "moved": [],
                        "citation": add.get("citation"),
                        "volume_basis": add.get("volume_basis"),
                        "volume_support": add.get("volume_support"),
                        "volume_counterevidence": add.get("volume_counterevidence"),
                        "researched_on": add.get("researched_on"),
                    })
                    have.add(solution_name)

    if not groups:
        return None                        # nothing matched, and nothing reconciled

    return {
        "path": path,
        "groups": groups,
        "splits": splits,
        "unmatched": unmatched,
        "moved_total": sum(len(g["moved"]) for g in groups) + len(splits),
    }


def apply_plan(doc: dict[str, Any], plan: dict[str, Any]) -> None:
    """Move each stock's matched ingredients under its own solutions[] entry."""
    ingredients = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    all_moved = {i for g in plan["groups"] for i in g["indices"]}

    splits = plan.get("splits") or {}
    by_name_idx = {_key(i.get("preferred_term")): n for n, i in enumerate(ingredients)}
    all_moved |= {by_name_idx[n] for n in splits}
    kept = [ing for i, ing in enumerate(ingredients) if i not in all_moved]

    def split_parts(solution_name: str) -> list[dict[str, Any]]:
        """Copies of summed ingredients belonging to this solution, each restored to
        its own stock value rather than the summed one."""
        out = []
        for name, parts in splits.items():
            for sol, value in parts:
                if sol != solution_name:
                    continue
                # deepcopy, not dict(): a shallow copy shares the nested `term` and
                # `mediaingredientmech_chebi_term` dicts with the ingredient this row
                # was split from, and both end up in DIFFERENT solutions. yaml.dump
                # then emits them as anchors/aliases (&id001 / *id001), so the two
                # solutions alias one object — mutating one silently changes the other.
                src = copy.deepcopy(ingredients[by_name_idx[name]])
                src["concentration"] = {"value": str(value), "unit": "G_PER_L"}
                out.append(src)
        return out

    solutions = []
    for g in plan["groups"]:
        solution: dict[str, Any] = {
            "preferred_term": g["solution_name"],
            "composition": [ingredients[i] for i in g["indices"]] + split_parts(g["solution_name"]),
        }
        vol = {"value": str(g["addition_volume_ml"]), "unit": "ML_PER_L"}
        basis = g.get("volume_basis") or "READ_FROM_THIS_MEDIUM"

        if basis == "READ_FROM_THIS_MEDIUM":
            # Printed in this medium's own recipe — an assertion, so it may be stated.
            solution["concentration"] = vol
            provenance = ("volume from this medium's own MediaDive recipe (#150)."
                          if not g.get("citation")
                          else f"volume read from {g['citation']} (#150).")
        else:
            # Everything weaker is a PROPOSAL. It goes in concentration_candidates and
            # leaves `concentration` unset, so nothing a tool concluded can be mistaken
            # for something a source said — and a later reading of the real recipe has
            # nothing to overwrite.
            candidate = {**vol, "basis": basis}
            for key, field in (("volume_support", "support"),
                               ("volume_counterevidence", "counterevidence"),
                               ("citation", "source")):
                if g.get(key):
                    candidate[field] = g[key]
            candidate["proposed_by"] = "apply_cocktail_nesting.py"
            if g.get("researched_on"):
                candidate["proposed_on"] = g["researched_on"]
            solution["concentration_candidates"] = [candidate]
            provenance = (f"addition volume NOT asserted: proposed as "
                          f"{g['addition_volume_ml']} ml/l on basis {basis}; see "
                          f"concentration_candidates (#150).")

        solution["preparation_notes"] = (
            f"Stock prepared in {g['stock_prepared_in_ml']} ml. Composition and "
            + provenance)
        solutions.append(solution)

    doc["ingredients"] = kept
    doc["solutions"] = solutions
    detail = "; ".join(f"{len(g['moved'])} -> {g['solution_name']!r} @ "
                       f"{g['addition_volume_ml']} ml/l" for g in plan["groups"])
    record_curation_event(
        doc, curator="apply_cocktail_nesting.py", action="NESTED_FLATTENED_COCKTAIL",
        notes=(f"Moved {plan['moved_total']} stock-strength component(s) out of "
               f"ingredients into {len(solutions)} solution(s): {detail}."
               + (f" {len(splits)} component(s) were SUMMED across stocks by the "
                  f"flattening and are restored to each stock's own value, verified by "
                  f"exact sum: {', '.join(sorted(splits))}." if splits else "")
               + " Each moved "
               "component matched the MediaDive stock by name AND value; bulk "
               "ingredients sharing a name were left in place (#150)."),
        changes=(f"Nested {plan['moved_total']} ingredient(s) under {len(solutions)} "
                 f"solution(s); ingredients {len(ingredients)} -> {len(kept)}"))


def source_medium(doc: dict[str, Any]) -> str | None:
    """The DSMZ medium number this record came from, or None when it cannot be trusted.

    `applies_to_media` gates a researched volume to media whose own DSMZ sheet was
    read, so this number must actually address that sheet. For a KOMODO-sourced
    record it does NOT: the notes stamp "DSMZ Medium: 294" on
    KOMODO_294_PELOBACTER_ACIDIGALLICI_MEDIUM, but DSMZ 294 is SYNTROPHUS HQGo1 —
    a different medium. That is the #244 collision, and trusting the stamp here would
    cite one medium's sheet as verification for another's volume.

    So only a `mediadive.medium:` id is accepted. KOMODO-sourced records are reported
    as unverifiable and left to stocks that carry no `applies_to_media` gate.
    """
    mid = str(((doc.get("media_term") or {}).get("term") or {}).get("id") or "")
    m = re.fullmatch(r"mediadive\.medium:(\w+)", mid)
    return m.group(1) if m else None


def stocks_for_record(researched: list[dict[str, Any]],
                      doc: dict[str, Any]) -> list[dict[str, Any]]:
    """Researched stocks usable for THIS record.

    A stock carrying `applies_to_media` is restricted to those media: the addition
    volume is a property of the citing medium, not of the stock — MediaDive observes
    "Seven vitamins solution" at four different volumes — so a record whose medium
    was not read is left alone rather than given a volume by association.
    """
    med = source_medium(doc)
    usable = []
    for stock in researched:
        allowed = stock.get("applies_to_media")
        if allowed and med not in set(allowed):
            continue
        usable.append(stock)
    return usable


def load_researched_stocks() -> list[dict[str, Any]]:
    """Researched stocks, shaped like a MediaDive `addition` so the same code path
    and the same name+value safety test apply to both."""
    if not RESEARCHED.is_file():
        return []
    try:
        data = json.loads(RESEARCHED.read_text())
    except (json.JSONDecodeError, OSError):
        return []
    return [s for s in data.get("stocks", []) if s.get("addition_volume_ml") is not None]


def load_komodo_volumes() -> dict[str, list[dict[str, Any]]]:
    """Addition volumes recovered for KOMODO-sourced records via their base medium.

    Written by `fetch_komodo_base_volumes.py`, which resolves a `komodo.medium:` key to
    a DSMZ medium number only when the structural derivation and the tracked
    KOMODO->DSMZ export agree, and marks each entry READ_FROM_THIS_MEDIUM or
    CROSS_MEDIUM_INFERENCE. `apply_plan` already routes those two differently, so a
    number inferred from a base medium lands in `concentration_candidates` and never in
    `concentration`.
    """
    if not KOMODO_VOLUMES.is_file():
        print(f"Run `just fetch-komodo-volumes` first — {KOMODO_VOLUMES.name} is missing.",
              file=sys.stderr)
        return {}
    try:
        data = json.loads(KOMODO_VOLUMES.read_text())
    except (json.JSONDecodeError, OSError):
        return {}
    return {rel: info.get("additions") or []
            for rel, info in data.items() if info.get("additions")}


def build_plans(split_summed: bool = False, use_researched: bool = False,
                use_komodo: bool = False) -> tuple[list[dict[str, Any]], list[tuple[str, list[str]]]]:
    if not VOLUMES.is_file():
        print(f"Run `just fetch-mediadive-volumes` first — {VOLUMES.name} is missing.",
              file=sys.stderr)
        return [], []
    volumes = json.loads(VOLUMES.read_text())
    researched = load_researched_stocks() if use_researched else []
    komodo = load_komodo_volumes() if use_komodo else {}
    rows = acp.audit(NORMALIZED)
    flagged_by_file: dict[str, set[str]] = {}
    for r in rows:
        if r["finding"] in ("TRACE_SALT_AS_STOCK", "INDICATOR_UNIT_SLIP"):
            flagged_by_file.setdefault(r["file_path"], set()).add(_key(r["ingredient"]))

    plans, skipped = [], []
    # Records MediaDive served, plus (when enabled) every other flattened cocktail,
    # which the researched stocks may cover.
    candidates: dict[str, list[dict[str, Any]]] = {
        rel: (info.get("additions") or []) for rel, info in volumes.items()}
    # KOMODO-sourced records MediaDive could not be asked about directly, resolved
    # through their base medium number. Never overrides a direct MediaDive answer.
    for rel, adds in komodo.items():
        if not candidates.get(rel):
            candidates[rel] = adds
    if researched:
        import csv as _csv
        with PROPOSALS.open() as fh:
            for row in _csv.DictReader(fh, delimiter="\t"):
                candidates.setdefault(row["file_path"], [])

    for rel, mediadive_additions in sorted(candidates.items()):
        # A researched stock is only consulted when MediaDive gave nothing for this
        # record — never to override the medium's own recipe — and only if it is
        # cleared for that record's source medium.
        additions = mediadive_additions
        path = NORMALIZED / rel
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(doc, dict):
            continue
        if not additions and researched:
            additions = stocks_for_record(researched, doc)
        if not additions:
            continue
        flagged = flagged_by_file.get(rel, set())
        if not flagged:
            continue
        plan = plan_record(path, doc, additions, flagged, split_summed)
        if plan is None:
            continue
        if plan["unmatched"]:
            skipped.append((rel, plan["unmatched"]))
            continue                       # refuse a partial repair
        plans.append(plan)
    return plans, skipped


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--apply", action="store_true", help="Write. Default is report-only.")
    ap.add_argument("--limit", type=int, default=0, help="Only the first N records.")
    ap.add_argument("--use-researched", action="store_true",
                    help="Also nest records whose stock is covered by "
                         "data/import_tracking/researched_stock_volumes.json — stocks "
                         "whose volume was read from a primary source for media "
                         "MediaDive does not serve. The name+value match still gates "
                         "every move.")
    ap.add_argument("--use-komodo", action="store_true",
                    help="Also nest KOMODO-sourced records whose medium number was "
                         "resolved to a MediaDive base medium by "
                         "`just fetch-komodo-volumes`. Volumes read from a medium "
                         "whose name agrees are asserted; everything else is written "
                         "as a concentration_candidate, never as a concentration.")
    ap.add_argument("--split-summed", action="store_true",
                    help="Also repair rows the flattening SUMMED across two stocks, "
                         "restoring each stock's own value. Opt-in: it reconstructs a "
                         "decomposition rather than moving a value verbatim, and is "
                         "accepted only on an exact sum match.")
    args = ap.parse_args(argv)

    plans, skipped = build_plans(args.split_summed, args.use_researched, args.use_komodo)
    if args.limit:
        plans = plans[:args.limit]

    print(f"{len(plans)} record(s) fully nestable from MediaDive data:")
    for p in plans[:25]:
        detail = "; ".join(f"{len(g['moved'])}->{g['solution_name'][:26]!r}@{g['addition_volume_ml']}ml"
                           for g in p["groups"])
        print(f"  {str(p['path'].relative_to(NORMALIZED))[:44]:46s} {detail}")
    if len(plans) > 25:
        print(f"  ... and {len(plans) - 25} more")
    if skipped:
        print(f"\n{len(skipped)} record(s) SKIPPED — some flagged rows did not match the "
              f"MediaDive stock by name+value, so a partial nesting was refused:")
        for rel, unmatched in skipped[:10]:
            print(f"  {rel[:46]:48s} unmatched={unmatched[:3]}")

    if not args.apply:
        print("\nReport only. Re-run with --apply to nest.")
        return 0

    written = 0
    for p in plans:
        doc = yaml.safe_load(p["path"].read_text(errors="replace"))
        apply_plan(doc, p)
        if write_record(p["path"], doc):
            written += 1
    print(f"\nNested {written} record(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
