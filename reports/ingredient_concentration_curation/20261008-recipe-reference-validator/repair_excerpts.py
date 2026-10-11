"""Guarded, evidence-only correction of two mid-word excerpt endings."""

import argparse
import copy
import json
from pathlib import Path

import review_solution_concentration_evidence as runner

from culturemech.curate.curation_event import now_iso, record_curation_event
from culturemech.validation.recipe_references import literal_match, parse_recipe, recipe_source
from culturemech.validation.write_validated import validate_recipe

HERE = Path(__file__).resolve().parent
COHORT = HERE.parent / "20261008-m142-nested-traces"
ROOT = HERE.parents[2]
ACTION = "EXPANDED_LITERAL_RECIPE_EVIDENCE_EXCERPT"
CONTEXT_SHA = "c5f79b827061f21a92b21ae48aca670d408a0efbe88b52b48e0d8ea95923c1aa"
OLD = "add per liter the following solution"
BASELINES = {
    "M933": "9aee391964d0fbedc181d7795c7fdb8582a8267e75690b2c81ee27cfc46be155",
    "M1390": "60034fb42488c92a9b87bdcdd0e6decfd339bf2c26fcd2886e50acff361acd19",
}
CHANGES = {
    "M933": ("JCM892", "add per liter the following solutions from anaerobic stocks"),
    "M1390": (
        "JCM1294",
        "Prior to inoculation, add per liter the following solutions (autoclaved and stored under N2):",
    ),
}


def check(before, after, item):
    """Invert only the permitted excerpt and append-only event, then compare all fields."""
    restored = copy.deepcopy(after)
    assert before["id"] == after["id"] == item["id"]
    source_key, expected = CHANGES[item["key"]]
    raw = (COHORT / "context.json").read_bytes()
    assert runner.sha(raw) == CONTEXT_SHA
    context = json.loads(raw)
    baseline = next(r for r in context["records"] if r["key"] == item["key"])
    assert item["path"] == baseline["path"]
    assert runner.sha(item["before_text"].encode()) == BASELINES[item["key"]]
    assert item["action"] == ACTION
    source = context["sources"][source_key]
    meta = source["metadata"]
    assert runner.sha(source["raw"].encode()) == meta["sha256"]
    assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
    content = parse_recipe(recipe_source(meta["url"]), source["raw"], meta).content
    assert literal_match(expected, content)
    assert before["evidence"][2]["reference"] == after["evidence"][2]["reference"] == meta["url"]
    assert before["evidence"][2]["snippet"] == OLD
    assert after["evidence"][2]["snippet"] == expected
    restored["evidence"][2]["snippet"] = OLD
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert event["source"] == meta["url"]
    assert json.loads(event["changes"]) == {
        "field": "evidence[2].snippet",
        "old": OLD,
        "new": expected,
    }
    assert meta["sha256"] in event["notes"]
    assert restored == before, "Unrelated data or earlier history changed"
    return {"corrected_evidence_snippets": 1, "new_curation_history": 1}


def preview():
    raw = (COHORT / "context.json").read_bytes()
    assert runner.sha(raw) == CONTEXT_SHA
    context = json.loads(raw)
    latest = json.loads((COHORT / "final-checks.json").read_text())["records"]
    plan = {"action": ACTION, "context_sha256": CONTEXT_SHA, "records": []}
    for key, (source_key, quote) in CHANGES.items():
        baseline = next(r for r in context["records"] if r["key"] == key)
        path = ROOT / baseline["path"]
        before_raw = path.read_bytes()
        assert runner.sha(before_raw) == latest[baseline["path"]]
        before = runner.load_yaml(before_raw)
        after = copy.deepcopy(before)
        assert not validate_recipe(before, target_class="MediaRecipe")
        meta = context["sources"][source_key]["metadata"]
        after["evidence"][2]["snippet"] = quote
        record_curation_event(
            after,
            curator="codex",
            action=ACTION,
            source=meta["url"],
            timestamp=now_iso(),
            notes="Expanded an excerpt that ended within the word 'solutions'. No ingredient, concentration, unit, scope, or calculation changed. Source locator: preparation paragraph; accessed="
            + meta["accessed_at"]
            + "; source SHA256="
            + meta["sha256"]
            + ".",
            changes=json.dumps({"field": "evidence[2].snippet", "old": OLD, "new": quote}),
        )
        assert not validate_recipe(after, target_class="MediaRecipe")
        after_raw = runner.render(before_raw.decode(), after)
        item = {
            "key": key,
            "id": before["id"],
            "path": baseline["path"],
            "action": ACTION,
            "before_text": before_raw.decode(),
            "before_sha256": runner.sha(before_raw),
            "after_text": after_raw.decode(),
            "after_sha256": runner.sha(after_raw),
            "source": meta,
            "field": "evidence[2].snippet",
            "old": OLD,
            "new": quote,
        }
        check(before, after, item)
        plan["records"].append(item)
    return plan


def apply(plan, verify=False):
    assert plan["action"] == ACTION and plan["context_sha256"] == CONTEXT_SHA
    assert len(plan["records"]) == 2 and {r["key"] for r in plan["records"]} == set(CHANGES)
    prepared = []
    for item in plan["records"]:
        before, after = (runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
        assert runner.sha(item["before_text"].encode()) == item["before_sha256"]
        assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
        assert not validate_recipe(after, target_class="MediaRecipe")
        check(before, after, item)
        target = ROOT / item["path"]
        assert not target.is_symlink() and target.resolve().is_relative_to(
            ROOT / "data/normalized_yaml"
        )
        current = target.read_bytes()
        if runner.sha(current) == item["after_sha256"]:
            continue
        assert not verify and runner.sha(current) == item["before_sha256"], "Record drift"
        prepared.append((target, current, item["after_text"].encode()))
    for target, before_raw, after_raw in prepared:
        assert target.read_bytes() == before_raw, "Concurrent edit"
        target.write_bytes(after_raw)
        assert target.read_bytes() == after_raw
    return {"changed": len(prepared), "verified": len(plan["records"]) - len(prepared)}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=HERE / "excerpt-plan.json")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.apply or args.verify:
        print(json.dumps(apply(json.loads(args.plan.read_text()), args.verify)))
    else:
        assert not args.plan.exists(), "Refuse to overwrite a reviewed plan"
        plan = preview()
        args.plan.write_text(json.dumps(plan, indent=2) + "\n")
        print(
            json.dumps(
                [
                    {k: r[k] for k in ("path", "field", "old", "new", "source")}
                    for r in plan["records"]
                ],
                indent=2,
            )
        )
