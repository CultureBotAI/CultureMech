"""Independently invert every proposed water-only correction and provenance append."""

import argparse
import copy
import hashlib
import json
import re
from collections import Counter
from decimal import Decimal
from pathlib import Path

import yaml

FOLDER = Path(__file__).resolve().parent
ROOT = FOLDER.parents[2]
ACTION = "CORRECTED_SOURCE_EXPLICIT_WATER_INPUT_AFTER_PH_ADJUSTMENT_REVIEW"


def check(before, after, item, case):
    raw = case["source_raw"]
    source = json.loads(raw)["data"]
    assert hashlib.sha256(raw.encode()).hexdigest() == item["source_sha256"]
    assert source["id"] == item["solution_id"] == case["solution_id"]
    assert source["steps"] == [{"recipe_order": None, "step": case["preparation"]}]
    assert re.fullmatch(r"Adjust pH to [0-9]+\.[0-9]+\.", case["preparation"])
    assert before["preparation_notes"] == case["preparation"]
    assert len(item["claims"]) == 1
    claim = item["claims"][0]
    assert claim["status"] == "correct"
    assert claim["pointer"][0] == "composition" and len(claim["pointer"]) == 2
    index = claim["pointer"][1]
    restored = copy.deepcopy(after)
    node = restored["composition"][index]
    old = before["composition"][index]
    assert node["term"] == old["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
    assert node["preferred_term"] == old["preferred_term"] == "Distilled water"
    assert old["concentration"] == claim["old"] == case["candidate"]["old"]
    assert set(claim["old"]) == {"value", "unit"} and claim["old"]["unit"] == "PERCENT_V_V"
    assert node["concentration"] == claim["new"]
    assert set(claim["new"]) == {"value", "unit"} and claim["new"]["unit"] == "L"
    (row,) = [r for r in source["recipe"] if r["compound_id"] == 4]
    assert json.loads(claim["snippet"]) == row and claim["snippet"] in raw
    assert row["unit"] == "ml" and row["compound"] == "Distilled water"
    assert row["optional"] == 0 and not row["attribute"] and not row["condition"]
    amount = Decimal(str(row["amount"]))
    assert source["volume"] == 1000
    assert Decimal(claim["old"]["value"]) == amount
    assert Decimal(claim["new"]["value"]) == amount / 1000
    assert node.pop("evidence") == [
        {
            "reference": claim["reference"],
            "supports": "SUPPORT",
            "snippet": claim["snippet"],
            "explanation": claim["explanation"],
        }
    ]
    assert not old.get("evidence")
    reference = f"https://mediadive.dsmz.de/rest/solution/{source['id']}"
    assert claim["reference"] == reference
    for text in (
        f"composition[{index}].concentration",
        case["preparation"],
        "$.data.steps[0]",
        f"{amount} ml / 1000 ml per L = {amount / 1000} L per preparation batch",
        "not a volume percentage",
        "No density or final-volume assumption",
        item["source_sha256"],
    ):
        assert text in claim["explanation"]
    node["concentration"] = copy.deepcopy(old["concentration"])
    old_refs = before.get("references", [])
    assert restored["references"][: len(old_refs)] == old_refs
    added_refs = len(restored["references"]) - len(old_refs)
    assert added_refs == (0 if any(r["reference"] == reference for r in old_refs) else 1)
    if added_refs:
        ref = restored["references"].pop()
        assert ref["reference"] == reference
        assert ref["title"] == f"MediaDive solution {source['id']}: {source['name']}"
        assert (
            "source_type=dataset" in ref["notes"]
            and "publication year not supplied" in ref["notes"]
        )
    if "references" not in before:
        assert restored.pop("references") == []
    event = restored["curation_history"].pop()
    assert event["action"] == item["action"] == ACTION
    assert event["curator"] == "codex" and event["source"] == reference
    assert claim["field"] in event["changes"]
    assert f"{claim['old']['value']} PERCENT_V_V -> {claim['new']['value']} L" in event["changes"]
    assert restored == before, "Unrelated record or provenance change"
    return {
        "quantity_corrections": 1,
        "new_evidence": 1,
        "new_references": added_refs,
        "new_curation_history": 1,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    plan = json.loads((FOLDER / "plan.json").read_text())
    ctx = json.loads((FOLDER / "inspected-context.json").read_text())
    cases = {r["path"]: r for r in ctx["records"]}
    counts = Counter()
    for item in plan["records"]:
        before = item["before_text"].encode()
        after = (ROOT / item["path"]).read_bytes() if args.applied else item["after_text"].encode()
        assert hashlib.sha256(before).hexdigest() == item["before_sha256"]
        assert hashlib.sha256(after).hexdigest() == item["after_sha256"]
        counts.update(
            check(
                yaml.load(before, Loader=yaml.CSafeLoader),
                yaml.load(after, Loader=yaml.CSafeLoader),
                item,
                cases[item["path"]],
            )
        )
    deferred = [c for c in ctx["records"] if c["withheld_reasons"]]
    for case in deferred:
        assert (
            hashlib.sha256((ROOT / case["path"]).read_bytes()).hexdigest() == case["before_sha256"]
        )
    result = {
        "records": len(plan["records"]),
        "applied": args.applied,
        "full_record_inversion": True,
        "deferred_unchanged": len(deferred),
        **counts,
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
