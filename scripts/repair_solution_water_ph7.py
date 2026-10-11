#!/usr/bin/env python3
"""Apply the individually inspected pH-7 water-input follow-up, never generalize it."""

from __future__ import annotations

import argparse
import copy
import json
import re
from collections import Counter
from pathlib import Path

import review_solution_concentration_evidence as shared
from fetch_solution_concentration_sources import API, load_yaml, read_capture
from repair_mediadive_stock_concentration_evidence import cell, exact_object, number, require, sha

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "reports/ingredient_concentration_curation/20261007-solutions-water-ph7"
CONTEXT_SHA = "056c5b9c16529457c0122699af2f5d800139da47d985b2fdf6a9b3c52b96fa18"
ACTION = "CORRECTED_SOURCE_EXPLICIT_WATER_INPUT_AFTER_PH7_REVIEW"
PREPARATION = "Adjust pH to 7.0."


def context(path=FOLDER / "inspected-context.json"):
    raw = path.read_bytes()
    require(sha(raw) == CONTEXT_SHA, "Inspected context changed")
    return json.loads(raw)


def selected(ctx):
    return [r for r in ctx["records"] if not r["withheld_reasons"]]


def water_claims(doc):
    return [
        c
        for c in shared.all_claims(doc)
        if len(c["pointer"]) == 2
        and c["pointer"][0] == "composition"
        and shared.get_node(doc, c["pointer"]).get("term", {}).get("id") == "mediadive.compound:4"
    ]


def review(doc, raw, meta, timestamp):
    return review_input(
        doc,
        raw,
        meta,
        timestamp,
        preparation=PREPARATION,
        amount_ml=1000,
        old_quantity={"value": "1000", "unit": "PERCENT_V_V"},
        action=ACTION,
    )


def review_input(doc, raw, meta, timestamp, *, preparation, amount_ml, old_quantity, action):
    """Build one reviewed water edit; callers must pin the complete inspected context."""
    require(re.fullmatch(r"Adjust pH to [0-9]+\.[0-9]+\.", preparation), "Unreviewed preparation")
    source = json.loads(raw)["data"]
    sid = source["id"]
    reference = API + str(sid)
    require(meta["url"] == meta["response_url"] == reference, "Wrong source URL")
    require(meta["sha256"] == sha(raw.encode()), "Source hash mismatch")
    require(
        doc.get("term") == {"id": f"mediadive.solution:{sid}", "label": source["name"]}
        and doc.get("preferred_term") == source["name"],
        "Exact solution identity mismatch",
    )
    require(
        source.get("steps") == [{"recipe_order": None, "step": preparation}], "Preparation drift"
    )
    require(doc.get("preparation_notes") == preparation, "Local preparation drift")
    require(not doc.get("solutions") and not doc.get("notes"), "Unreviewed local context")
    rows = source["recipe"]
    require(
        all(
            r.get("compound_id") is not None
            and r.get("solution_id") is None
            and r.get("solution") is None
            for r in rows
        ),
        "Stock rows need separate review",
    )
    identities = [(f"mediadive.compound:{r['compound_id']}", r["compound"]) for r in rows]
    local = [(n.get("term", {}).get("id"), n.get("preferred_term")) for n in doc["composition"]]
    require(Counter(identities) == Counter(local), "Direct inventory drift")
    require(
        all(n.get("term", {}).get("label") == n["preferred_term"] for n in doc["composition"]),
        "Ingredient label drift",
    )
    claims = water_claims(doc)
    require(len(claims) == 1, "Ambiguous local water")
    matches = [(i, r) for i, r in enumerate(rows) if r["compound_id"] == 4]
    require(len(matches) == 1, "Ambiguous source water")
    index, row = matches[0]
    require(
        row["compound"] == "Distilled water" and row["unit"] == "ml", "Water identity or unit drift"
    )
    require(
        row.get("optional") == 0 and not row.get("condition") and not row.get("attribute"),
        "Conditional water",
    )
    require(row.get("g_l") is None and row.get("mmol_l") is None, "Unexpected water concentration")
    claim = claims[0]
    node = shared.get_node(doc, claim["pointer"])
    require(
        not node.get("notes") and not node.get("evidence"),
        "Existing water context needs reconciliation",
    )
    require(node["preferred_term"] == "Distilled water", "Local water label drift")
    amount = number(amount_ml)
    require(amount > 0 and number(row["amount"]) == amount, "Unreviewed water input")
    require(number(source["volume"]) == 1000, "Unreviewed source volume")
    require(
        set(old_quantity) == {"value", "unit"}
        and old_quantity["unit"] == "PERCENT_V_V"
        and number(old_quantity["value"]) == amount,
        "Old water value does not match diagnosed importer error",
    )
    require(claim["old"] == old_quantity, "Old water amount drift")
    liters = format(amount / 1000, "f")
    proposed = {"value": liters, "unit": "L"}
    snippet = exact_object(raw, row)
    preparation_excerpt = exact_object(raw, source["steps"][0])
    locator = f"$.data.recipe[{index}] (compound_id=4)"
    explanation = (
        f"Concentration evidence for {claim['field']} (Distilled water) in MediaDive solution {sid}; "
        f"locator={locator}. Source-explicit water input: {amount} ml / 1000 ml per L = {liters} L per preparation batch. "
        f"This replaces the importer unit error ({old_quantity['value']} PERCENT_V_V), not the recipe formulation. "
        f"Separately located exact preparation excerpt at $.data.steps[0]: {preparation_excerpt}. "
        "The inspected preparation only adjusts pH; it does not instruct make-up to a final volume. "
        "This is the listed water input, not a volume percentage, measured final volume, stock strength, "
        "or receiving-medium concentration. No density or final-volume assumption is made. "
        "Unchanged non-water amounts and chemical mappings are not newly verified by this follow-up. "
        f"Retrieved {meta['accessed_at']}; response SHA256={meta['sha256']}."
    )
    claim.update(
        new=proposed,
        status="correct",
        reference=reference,
        snippet=snippet,
        locator=locator,
        explanation=explanation,
    )
    after = copy.deepcopy(doc)
    target = shared.get_node(after, claim["pointer"])
    target["concentration"] = proposed
    target.setdefault("evidence", []).append(
        {
            "reference": reference,
            "supports": "SUPPORT",
            "snippet": snippet,
            "explanation": explanation,
        }
    )
    refs = after.setdefault("references", [])
    require(sum(r["reference"] == reference for r in refs) <= 1, "Duplicate root source reference")
    if not any(r["reference"] == reference for r in refs):
        refs.append(
            {
                "reference": reference,
                "title": f"MediaDive solution {sid}: {source['name']}",
                "notes": f"source_type=dataset; discovery_mode=existing_record_reference; accessed_on={meta['accessed_at'][:10]}; source_organization=DSMZ; response_sha256={meta['sha256']}; individual authors and publication year not supplied. Water input only; no stock strength or final-volume assertion.",
            }
        )
    record_curation_event(
        after,
        curator="codex",
        action=action,
        source=reference,
        timestamp=timestamp,
        changes=f"{claim['field']}: {old_quantity['value']} PERCENT_V_V -> {liters} L water input per preparation batch ({amount} ml / 1000).",
        notes="Individually inspected source water row and pH-adjustment instruction; literal snippet and locator attached. Existing non-water claims, provenance, preparation, and identifiers preserved. No final-volume inference.",
    )
    return after, claims


def adapter():
    return shared.ReviewAdapter(
        "solution_id",
        "SolutionRecipe",
        read_capture,
        review,
        water_claims,
        ("ingredients", "solutions"),
    )


def make_plan(root, ctx, cache, *, review_adapter=None, action=ACTION, context_sha=CONTEXT_SHA):
    review_adapter = review_adapter or adapter()
    records = [
        {k: r[k] for k in ("path", "id", "solution_id", "before_sha256", "before_text")}
        for r in selected(ctx)
    ]
    plan = shared.preview(root, records, cache, ctx["commit"], adapter=review_adapter)
    plan.update(
        action=action,
        context_sha256=context_sha,
        scope="Water input only; unchanged claims are not newly verified.",
    )
    for item in plan["records"]:
        require(
            not item["failure"] and not item["baseline_errors"] and not item["post_errors"],
            "Failed preview",
        )
        raw, meta = read_capture(cache, item["solution_id"])
        after, _ = review_adapter.reviewer(
            load_yaml(item["before_text"]), raw, meta, plan["created_at"]
        )
        item.update(action=action, after_text=shared.render(item["before_text"], after).decode())
    validate_plan(
        root,
        plan,
        ctx,
        cache,
        review_adapter=review_adapter,
        action=action,
        context_sha=context_sha,
    )
    return plan


def validate_plan(
    root, plan, ctx, cache, *, review_adapter=None, action=ACTION, context_sha=CONTEXT_SHA
):
    review_adapter = review_adapter or adapter()
    shared.safe_targets(root, plan)
    require(
        plan.get("action") == action
        and plan.get("context_sha256") == context_sha
        and plan["commit"] == ctx["commit"],
        "Plan scope drift",
    )
    approved = selected(ctx)
    require(
        [r["path"] for r in plan["records"]] == [r["path"] for r in approved],
        "Plan membership drift",
    )
    for item, frozen in zip(plan["records"], approved, strict=True):
        path = root / item["path"]
        require(path.resolve() == path.absolute(), "Symlink ancestor refused")
        for key in ("path", "id", "solution_id", "before_text", "before_sha256"):
            require(item[key] == frozen[key], f"Frozen {key} drift")
        require(sha(item["before_text"].encode()) == item["before_sha256"], "Baseline hash drift")
        raw, meta = read_capture(cache, item["solution_id"])
        require(
            raw == frozen["source_raw"] and meta == frozen["source_metadata"],
            "Inspected source drift",
        )
        require(
            meta["sha256"] == item["source_sha256"]
            and meta["accessed_at"] == item["source_accessed_at"],
            "Plan source drift",
        )
        before = load_yaml(item["before_text"])
        after, claims = review_adapter.reviewer(before, raw, meta, plan["created_at"])
        require(item.get("action") == action and claims == item["claims"], "Plan claims drift")
        require(
            item["failure"] is None and item["baseline_errors"] == item["post_errors"] == [],
            "Failed plan",
        )
        require(not shared.errors(before) and not shared.errors(after), "Schema failure")
        shared.check_merge_inputs(before, after, review_adapter)
        output = shared.render(item["before_text"], after)
        require(
            output.decode() == item["after_text"] and sha(output) == item["after_sha256"],
            "Plan result drift",
        )


def write_reports(folder, plan, ctx, applied):
    state = "applied locally" if applied else "preview only"
    for item in plan["records"]:
        claim = item["claims"][0]
        lines = [
            f"# Water Input Follow-up: {item['id']}",
            "",
            f"- Follow-up target: {item['path']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- Source SHA256: {item['source_sha256']}",
            f"- Source accessed: {item['source_accessed_at']}",
            f"- State: {state}",
            "- Scope: water input only; supplement to the existing canonical per-record review, not new review coverage.",
            "- Validation: before/after closed schema passed; see baseline-validation.json and post-validation.json for terminal checks.",
            "",
            "| Field | Ingredient | Old | New | Status | Source | Exact snippet | Locator | Calculation / context |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
            "| "
            + " | ".join(
                cell(claim[k])
                for k in (
                    "field",
                    "ingredient",
                    "old",
                    "new",
                    "status",
                    "reference",
                    "snippet",
                    "locator",
                    "explanation",
                )
            )
            + " |",
            "",
        ]
        (folder / f"{item['solution_id']}-followup.md").write_text("\n".join(lines))
    deferred = [
        {k: r[k] for k in ("path", "id", "solution_id", "before_sha256", "withheld_reasons")}
        for r in ctx["records"]
        if r["withheld_reasons"]
    ]
    (folder / "deferred.json").write_text(
        json.dumps(
            {
                "scope": "Triage only; no proposed or applied edit, not complete source reviews.",
                "records": deferred,
            },
            indent=2,
        )
        + "\n"
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--plan", type=Path, default=FOLDER / "plan.json")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    ctx = context()
    if args.apply or args.verify:
        plan = json.loads(args.plan.read_text())
        validate_plan(ROOT, plan, ctx, args.cache)
        if args.apply:
            result = shared.apply(ROOT, plan, args.cache, adapter=adapter())
            write_reports(args.plan.parent, plan, ctx, True)
        else:
            result = shared.verify(ROOT, plan, args.cache, adapter=adapter())
    else:
        require(not args.plan.exists(), "Refuse to overwrite plan")
        plan = make_plan(ROOT, ctx, args.cache)
        args.plan.write_text(json.dumps(plan, indent=2) + "\n")
        write_reports(args.plan.parent, plan, ctx, False)
        result = shared.summary(plan)
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
