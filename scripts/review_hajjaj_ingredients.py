"""Preview and apply the reviewed Hajjaj-family ingredient evidence operations."""

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
HERE = ROOT / "reports/ingredient_concentration_curation/20261010-hajjaj-ingredients"
PLAN = HERE / "plan.json"
SOURCE_SHA = "c17680f0b36bb27d61ee30662964506f810580e4203ecdacc517ff3f0c1a4b5b"
ACTION = "CURATED_HAJJAJ_SOURCED_INGREDIENT_AMOUNTS_AND_FORMS"
KEYS = {
    "318",
    "324",
    "325",
    "326",
    "327",
    "328",
    "329",
    "330",
    "331",
    "332",
    "333",
    "334",
    "335",
    "336",
    "337",
    "338",
    "339",
    "340",
    "341",
    "342",
}


def sources():
    if not __debug__:
        raise RuntimeError("Guarded curation requires assertions; do not use -O")
    raw = (HERE / "source-review.json").read_bytes()
    assert runner.sha(raw) == SOURCE_SHA, "Source ledger drift"
    source = json.loads(raw)
    records = {r["key"]: r for r in source["records"]}
    assert len(source["records"]) == 20 and set(records) == KEYS
    assert sum(len(r["claims"]) for r in records.values()) == 243
    for record in records.values():
        assert len({tuple(o["pointer"]) for o in record["operations"]}) == len(record["operations"])
        for op in record["operations"]:
            assert op["kind"] in {"set", "remove"}
            assert op["snippet"] in source["sources"][op["reference"]]["inspected_snippets"]
            assert op["locator"] and op["reason"] and op["counts"]
    return source, records


def check_claims(before, record):
    actual = runner.all_claims(before)
    assert [(c["pointer"], c["ingredient"], c["old"]) for c in actual] == [
        (c["pointer"], c["ingredient"], c["old"]) for c in record["claims"]
    ], "Claim inventory or ingredient identity drift"
    for claim in record["claims"]:
        assert claim["status"] in {"correct", "unsupported"}
        if claim["status"] == "correct":
            assert record["primary_article_linked"]
            assert claim["old"]["unit"] == "MILLIMOLAR" and claim["new"]["unit"] == "G_PER_L"
            assert claim["reference"].startswith("doi:")
        else:
            assert claim["old"] == claim["new"]


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
    check_claims(before, record)
    after = copy.deepcopy(before)
    for op in record["operations"]:
        parent = runner.get_node(after, op["pointer"][:-1])
        key = op["pointer"][-1]
        assert (key in parent) == op["old_present"]
        assert parent.get(key) == op["old"]
        if op["kind"] == "remove":
            assert op["old_present"] and op["new"] is None
            parent.pop(key)
        else:
            parent[key] = copy.deepcopy(op["new"])
            if key in {"evidence", "references"}:
                refs = [e["reference"] for e in parent[key]]
                assert len(refs) == len(set(refs)), "Duplicate provenance reference"
    after["curation_history"].append(event(before, record, timestamp, source))
    return after


def check(before, after, item):
    """Invert every approved field operation and require exact original recovery."""
    source, records = sources()
    record = records[item["key"]]
    assert item["action"] == ACTION and item["target_class"] == "MediaRecipe"
    assert item["id"] == before["id"] == after["id"] == record["id"]
    assert item["path"] == record["path"] and item["unresolved"] == source["limitations"]
    assert item["claims"] == record["claims"]
    assert item["primary_article_linked"] == record["primary_article_linked"]
    assert item["before_text"] == record["before_text"]
    assert (
        runner.sha(item["before_text"].encode()) == item["before_sha256"] == record["before_sha256"]
    )
    assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
    assert before == runner.load_yaml(item["before_text"])
    assert after == runner.load_yaml(item["after_text"])
    assert before["media_term"]["term"]["id"] == record["source_term"]
    check_claims(before, record)
    restored = copy.deepcopy(after)
    added = restored["curation_history"].pop()
    assert added == event(before, record, added["timestamp"], source), "Unreviewed history"
    counts = collections.Counter(new_curation_history=1)
    for op in reversed(record["operations"]):
        parent = runner.get_node(restored, op["pointer"][:-1])
        key = op["pointer"][-1]
        if op["kind"] == "remove":
            assert key not in parent, "Unverified identity restored"
        else:
            assert key in parent and parent[key] == op["new"], "Unreviewed field change"
        if op["old_present"]:
            parent[key] = copy.deepcopy(op["old"])
        else:
            parent.pop(key)
        counts.update(op["counts"])
    assert restored == before, "Unreviewed recipe, amount, growth, role or provenance change"
    return counts


def safe_targets(root, plan):
    """Validate authoritative paths without treating identity edits as amount verification."""
    _, records = sources()
    assert plan["version"] == 1
    paths = [item["path"] for item in plan["records"]]
    assert len(paths) == len(set(paths)), "Duplicate target in plan"
    tracked = set(
        subprocess.check_output(
            ["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root, text=True
        ).split("\0")
    )
    for item in plan["records"]:
        path = item["path"]
        assert (
            path in tracked and path.startswith("data/normalized_yaml/") and path.endswith(".yaml")
        ), "Non-authoritative or non-exact target"
        safe_path(root, path)
        record = records[item["key"]]
        assert path == record["path"] and record["operations"]
        assert item["before_sha256"] != item["after_sha256"], "Expected reviewed field operations"


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
            "primary_article_linked": record["primary_article_linked"],
            "before_text": raw.decode(),
            "after_text": output.decode(),
            "before_sha256": runner.sha(raw),
            "after_sha256": runner.sha(output),
            "claims": record["claims"],
            "unresolved": source["limitations"],
        }
        item["counts"] = dict(check(before, after, item))
        plan["records"].append(item)
    safe_targets(root, plan)
    return plan


def apply(plan, root=ROOT, *, verify=False):
    sources()
    root = root.resolve()
    assert plan["version"] == 1 and plan["action"] == ACTION and plan["source_sha256"] == SOURCE_SHA
    assert len(plan["records"]) == 20 and {r["key"] for r in plan["records"]} == KEYS
    safe_targets(root, plan)
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
    return {"changed": len(pending), "already_applied": 20 - len(pending)}


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
        print(json.dumps({"reviewed": 20, "records_edited": 0}))


if __name__ == "__main__":
    main()
