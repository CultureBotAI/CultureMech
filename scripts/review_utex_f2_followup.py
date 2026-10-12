"""Preview and apply the source-pinned F/2 variant and NH4 evidence successor."""

import argparse
import collections
import copy
import json
import subprocess
from pathlib import Path

import review_solution_concentration_evidence as runner
from review_utex_f2_concentrations import safe_path

from culturemech.curate.curation_event import now_iso, record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261010-utex-f2-followup"
PLAN = HERE / "plan-v2.json"
SOURCE_SHA = "2da2c7f0d0df2c65aa9e0980e757c3ff2bfdbf08290c28da22e3563bcff2e2b2"
ACTION = "CURATED_F2_VARIANT_FORMULATION_AND_NH4_RELATIONSHIP_EVIDENCE"
KEYS = {"f-2-medium", "f-2-nh4-medium"}


def sources():
    if not __debug__:
        raise RuntimeError("Guarded curation requires Python assertions; do not use -O")
    raw = (HERE / "source-review-v2.json").read_bytes()
    assert runner.sha(raw) == SOURCE_SHA, "Source ledger drift"
    source = json.loads(raw)
    records = {r["key"]: r for r in source["records"]}
    assert len(source["records"]) == 2 and set(records) == KEYS
    for record in records.values():
        for op in record["operations"]:
            assert op["snippet"] in source["sources"][op["reference"]]["inspected_snippets"]
            assert op["locator"] and op["reason"] and op["counts"]
    return source, records


def event(before, record, timestamp, source):
    doc = copy.deepcopy(before)
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="; ".join(dict.fromkeys(op["reference"] for op in record["operations"])),
        changes=json.dumps(record["operations"], sort_keys=True),
        notes=" ".join(source["limitations"]),
    )
    return doc["curation_history"][-1]


def transform(before, record, timestamp):
    source, _ = sources()
    assert before == runner.load_yaml(record["before_text"])
    after = copy.deepcopy(before)
    for op in record["operations"]:
        if op["kind"] == "append":
            node = runner.get_node(after, op["pointer"])
            assert isinstance(node, list) and len(node) == op["old_length"]
            refs = [r["reference"] for r in node + op["new"]]
            assert len(refs) == len(set(refs)), "Duplicate provenance reference"
            node.extend(copy.deepcopy(op["new"]))
        else:
            assert op["kind"] == "set"
            parent = runner.get_node(after, op["pointer"][:-1])
            key = op["pointer"][-1]
            if op["old_present"]:
                assert (not isinstance(parent, dict) or key in parent) and parent[key] == op["old"]
            else:
                assert isinstance(parent, dict) and key not in parent
            parent[key] = copy.deepcopy(op["new"])
    after["curation_history"].append(event(before, record, timestamp, source))
    return after


def check(before, after, item):
    """Invert only the pinned operations, independently of the forward transform."""
    source, records = sources()
    record = records[item["key"]]
    assert item["action"] == ACTION and item["target_class"] == "MediaRecipe"
    assert item["id"] == before["id"] == after["id"] == record["id"]
    assert item["path"] == record["path"] and item["unresolved"] == source["limitations"]
    assert item["claims"] == record["claims"] and item["before_text"] == record["before_text"]
    assert (
        runner.sha(item["before_text"].encode()) == item["before_sha256"] == record["before_sha256"]
    )
    assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
    assert before == runner.load_yaml(item["before_text"])
    assert after == runner.load_yaml(item["after_text"])
    assert before["media_term"]["term"]["id"] == record["source_term"]
    restored = copy.deepcopy(after)
    added = restored["curation_history"].pop()
    assert added == event(before, record, added["timestamp"], source), "Unreviewed history"
    counts = collections.Counter(new_curation_history=1)
    for op in reversed(record["operations"]):
        if op["kind"] == "append":
            node = runner.get_node(restored, op["pointer"])
            assert isinstance(node, list)
            assert len(node) == op["old_length"] + len(op["new"])
            assert node[op["old_length"] :] == op["new"], "Unreviewed provenance"
            del node[op["old_length"] :]
        else:
            parent = runner.get_node(restored, op["pointer"][:-1])
            key = op["pointer"][-1]
            assert (not isinstance(parent, dict) or key in parent) and parent[key] == op["new"]
            if op["old_present"]:
                parent[key] = copy.deepcopy(op["old"])
            else:
                parent.pop(key)
        counts.update(op["counts"])
    assert restored == before, "Unreviewed recipe, quantity, growth or provenance change"
    return counts


def preview(root=ROOT):
    source, records = sources()
    plan = {
        "version": 1,
        "action": ACTION,
        "source_sha256": SOURCE_SHA,
        "created_at": now_iso(),
        "commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True
        ).strip(),
        "records": [],
    }
    for key, record in records.items():
        raw = safe_path(root, record["path"]).read_bytes()
        assert runner.sha(raw) == record["before_sha256"], "Record drift"
        before = runner.load_yaml(raw)
        assert not validate_recipe(before, target_class="MediaRecipe")
        after = transform(before, record, plan["created_at"])
        assert not validate_recipe(after, target_class="MediaRecipe")
        output = runner.render(raw.decode(), after)
        item = {
            "key": key,
            "path": record["path"],
            "id": record["id"],
            "action": ACTION,
            "target_class": "MediaRecipe",
            "before_text": raw.decode(),
            "after_text": output.decode(),
            "before_sha256": runner.sha(raw),
            "after_sha256": runner.sha(output),
            "claims": record["claims"],
            "unresolved": source["limitations"],
        }
        item["counts"] = dict(check(before, after, item))
        plan["records"].append(item)
    runner.safe_targets(root, plan)
    return plan


def apply(plan, root=ROOT, *, verify=False):
    sources()
    root = root.resolve()
    assert plan["version"] == 1 and plan["action"] == ACTION and plan["source_sha256"] == SOURCE_SHA
    assert len(plan["records"]) == 2 and {r["key"] for r in plan["records"]} == KEYS
    runner.safe_targets(root, plan)
    pending = []
    for item in plan["records"]:
        before, after = (runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
        assert dict(check(before, after, item)) == item["counts"]
        assert not validate_recipe(after, target_class="MediaRecipe")
        target = safe_path(root, item["path"])
        raw = target.read_bytes()
        if runner.sha(raw) == item["after_sha256"]:
            continue
        assert not verify and runner.sha(raw) == item["before_sha256"], "Concurrent record edit"
        pending.append((target, raw, item["after_text"].encode()))
    for target, old, _ in pending:
        safe_path(root, target.relative_to(root))
        assert target.read_bytes() == old, "Concurrent edit during preflight"
    for target, old, new in pending:
        safe_path(root, target.relative_to(root))
        assert target.read_bytes() == old, "Concurrent edit during write"
        target.write_bytes(new)
        assert target.read_bytes() == new
    return {"changed": len(pending), "already_applied": 2 - len(pending)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=PLAN)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.apply or args.verify:
        print(json.dumps(apply(json.loads(args.plan.read_text()), verify=args.verify)))
    else:
        assert not args.plan.exists(), "Refuse to overwrite a preview"
        plan = preview()
        with args.plan.open("x") as stream:
            json.dump(plan, stream, indent=2)
            stream.write("\n")
        print(json.dumps({"reviewed": 2, "records_edited": 0}))


if __name__ == "__main__":
    main()
