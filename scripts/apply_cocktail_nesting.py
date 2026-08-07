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
import json
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


def plan_record(path: Path, doc: dict[str, Any], additions: list[dict[str, Any]],
                flagged_names: set[str]) -> dict[str, Any] | None:
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
        indices, _ = match_components(
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
        })
    if not groups:
        return None

    matched_names = {_key(ingredients[i].get("preferred_term")) for i in claimed}
    return {
        "path": path,
        "groups": groups,
        "unmatched": sorted(flagged_names - matched_names),
        "moved_total": sum(len(g["moved"]) for g in groups),
    }


def apply_plan(doc: dict[str, Any], plan: dict[str, Any]) -> None:
    """Move each stock's matched ingredients under its own solutions[] entry."""
    ingredients = [i for i in doc.get("ingredients") or [] if isinstance(i, dict)]
    all_moved = {i for g in plan["groups"] for i in g["indices"]}
    kept = [ing for i, ing in enumerate(ingredients) if i not in all_moved]

    solutions = []
    for g in plan["groups"]:
        solutions.append({
            "preferred_term": g["solution_name"],
            "composition": [ingredients[i] for i in g["indices"]],
            "concentration": {"value": str(g["addition_volume_ml"]), "unit": "ML_PER_L"},
            "preparation_notes": (
                f"Stock prepared in {g['stock_prepared_in_ml']} ml; added at "
                f"{g['addition_volume_ml']} ml per litre of medium. Composition and "
                f"volume from MediaDive (#150)."),
        })

    doc["ingredients"] = kept
    doc["solutions"] = solutions
    detail = "; ".join(f"{len(g['moved'])} -> {g['solution_name']!r} @ "
                       f"{g['addition_volume_ml']} ml/l" for g in plan["groups"])
    record_curation_event(
        doc, curator="apply_cocktail_nesting.py", action="NESTED_FLATTENED_COCKTAIL",
        notes=(f"Moved {plan['moved_total']} stock-strength component(s) out of "
               f"ingredients into {len(solutions)} solution(s): {detail}. Each moved "
               f"component matched the MediaDive stock by name AND value; bulk "
               f"ingredients sharing a name were left in place (#150)."),
        changes=(f"Nested {plan['moved_total']} ingredient(s) under {len(solutions)} "
                 f"solution(s); ingredients {len(ingredients)} -> {len(kept)}"))


def build_plans() -> tuple[list[dict[str, Any]], list[tuple[str, list[str]]]]:
    if not VOLUMES.is_file():
        print(f"Run `just fetch-mediadive-volumes` first — {VOLUMES.name} is missing.",
              file=sys.stderr)
        return [], []
    volumes = json.loads(VOLUMES.read_text())
    rows = acp.audit(NORMALIZED)
    flagged_by_file: dict[str, set[str]] = {}
    for r in rows:
        if r["finding"] in ("TRACE_SALT_AS_STOCK", "INDICATOR_UNIT_SLIP"):
            flagged_by_file.setdefault(r["file_path"], set()).add(_key(r["ingredient"]))

    plans, skipped = [], []
    for rel, info in sorted(volumes.items()):
        additions = info.get("additions") or []
        if not additions:
            continue
        path = NORMALIZED / rel
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if not isinstance(doc, dict):
            continue
        flagged = flagged_by_file.get(rel, set())
        if not flagged:
            continue
        plan = plan_record(path, doc, additions, flagged)
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
    args = ap.parse_args(argv)

    plans, skipped = build_plans()
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
