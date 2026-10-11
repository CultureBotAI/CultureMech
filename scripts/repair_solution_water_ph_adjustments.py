#!/usr/bin/env python3
"""Apply only the hash-pinned, individually inspected pH-adjustment water inputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

import repair_solution_water_ph7 as water
from fetch_solution_concentration_sources import load_yaml, read_capture
from repair_mediadive_stock_concentration_evidence import require, sha

ROOT = Path(__file__).resolve().parents[1]
FOLDER = ROOT / "reports/ingredient_concentration_curation/20261007-solutions-water-ph-adjustments"
CONTEXT_SHA = "82e1f114755e3f8cca1d6b5de5b09f81872e479eb53c1f99873353a864bc2118"
ACTION = "CORRECTED_SOURCE_EXPLICIT_WATER_INPUT_AFTER_PH_ADJUSTMENT_REVIEW"
shared = water.shared


def context(path=FOLDER / "inspected-context.json"):
    raw = path.read_bytes()
    require(sha(raw) == CONTEXT_SHA, "Inspected context changed")
    return json.loads(raw)


def adapter(ctx):
    require(
        sha((json.dumps(ctx, indent=2) + "\n").encode()) == CONTEXT_SHA, "Context object changed"
    )
    approved = {r["solution_id"]: r for r in water.selected(ctx)}

    def review(doc, raw, meta, timestamp):
        sid = json.loads(raw)["data"]["id"]
        require(sid in approved, "Uninspected solution")
        case = approved[sid]
        require(doc == load_yaml(case["before_text"]), "Inspected record changed")
        require(
            raw == case["source_raw"] and meta == case["source_metadata"],
            "Inspected source changed",
        )
        return water.review_input(
            doc,
            raw,
            meta,
            timestamp,
            preparation=case["preparation"],
            amount_ml=case["candidate"]["source_amount"],
            old_quantity=case["candidate"]["old"],
            action=ACTION,
        )

    return shared.ReviewAdapter(
        "solution_id",
        "SolutionRecipe",
        read_capture,
        review,
        water.water_claims,
        ("ingredients", "solutions"),
    )


def make_plan(root, ctx, cache):
    return water.make_plan(
        root, ctx, cache, review_adapter=adapter(ctx), action=ACTION, context_sha=CONTEXT_SHA
    )


def validate_plan(root, plan, ctx, cache):
    water.validate_plan(
        root, plan, ctx, cache, review_adapter=adapter(ctx), action=ACTION, context_sha=CONTEXT_SHA
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
            result = shared.apply(ROOT, plan, args.cache, adapter=adapter(ctx))
            water.write_reports(args.plan.parent, plan, ctx, True)
        else:
            result = shared.verify(ROOT, plan, args.cache, adapter=adapter(ctx))
    else:
        require(not args.plan.exists(), "Refuse to overwrite plan")
        plan = make_plan(ROOT, ctx, args.cache)
        args.plan.write_text(json.dumps(plan, indent=2) + "\n")
        water.write_reports(args.plan.parent, plan, ctx, False)
        result = shared.summary(plan)
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
