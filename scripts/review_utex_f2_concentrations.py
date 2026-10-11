"""Preview and apply source-pinned F/2 ingredient and stock-stage corrections."""

import argparse
import collections
import copy
import json
import subprocess
from pathlib import Path

import review_solution_concentration_evidence as runner

from culturemech.curate.curation_event import now_iso, record_curation_event
from culturemech.ingredients.mim_label_index import resolve_ingredient
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261010-utex-f2"
PLAN = HERE / "plan.json"
SOURCE_SHA = "c5ab9e8f678b1a279d40262374482f3ec5d889c1afecd0f1d3991cb2923955a7"
ACTION = "CURATED_UTEX_F2_INGREDIENT_AND_STOCK_STAGE_EVIDENCE"
KEYS = {
    "f-2-medium",
    "1-percent-f-2-medium",
    "5-percent-f-2-medium",
    "8-ppt-f-2-medium",
    "f-2-nh4-medium",
}


def sources():
    raw = (HERE / "source-review.json").read_bytes()
    assert runner.sha(raw) == SOURCE_SHA, "Source ledger drift"
    source = json.loads(raw)
    records = {r["key"]: r for r in source["records"]}
    assert len(source["records"]) == 5 and set(records) == KEYS
    assert sum(len(r["claims"]) for r in records.values()) == 105
    return source, records


def check_claims(before, record, source):
    assert before == runner.load_yaml(record["before_text"])
    actual = runner.all_claims(before)
    assert [c["pointer"] for c in actual] == [c["pointer"] for c in record["claims"]]
    for claim in record["claims"]:
        node = runner.get_node(before, claim["pointer"])
        assert node["preferred_term"] == claim["ingredient"]
        assert node["concentration"] == claim["old"]
        assert claim["status"] in {"correct", "evidence_only"}
        assert (claim["status"] == "correct") == (claim["old"] != claim["new"])
        assert claim["snippet"] in source["sources"][claim["reference"]]["text"]
        assert runner.field_name(claim["pointer"] + ["concentration"]) in claim["explanation"]
        if claim["new"] is None:
            assert "not a replacement numeric amount" in claim["explanation"]
    paths = [tuple(op["pointer"]) for op in record["operations"]]
    assert len(paths) == len(set(paths)), "Overlapping operations"
    for item in record["evidence_additions"]:
        evidence = item["evidence"]
        assert evidence["snippet"] in source["sources"][evidence["reference"]]["text"]
        assert evidence["supports"] == "SUPPORT" and "Locator:" in evidence["explanation"]


def event(before, record, timestamp, source):
    doc = copy.deepcopy(before)
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="https://utex.org/products/" + record["key"],
        changes=json.dumps(record["operations"], sort_keys=True),
        notes=" ".join(source["limitations"]),
    )
    return doc["curation_history"][-1]


def evidence_by_owner(record):
    result = collections.defaultdict(list)
    for item in record["evidence_additions"]:
        result[tuple(item["pointer"])].append(item["evidence"])
    for entries in result.values():
        assert len({e["reference"] for e in entries}) == len(entries)
    return result


def transform(before, record, timestamp):
    source, _ = sources()
    check_claims(before, record, source)
    after = copy.deepcopy(before)
    for op in record["operations"]:
        parent = runner.get_node(after, op["pointer"][:-1])
        key = op["pointer"][-1]
        assert parent[key] == op["old"]
        if op["remove"]:
            parent.pop(key)
        else:
            parent[key] = copy.deepcopy(op["new"])
    for pointer, entries in evidence_by_owner(record).items():
        owner = runner.get_node(after, pointer)
        assert not (
            {e["reference"] for e in entries} & {e["reference"] for e in owner.get("evidence", [])}
        )
        owner.setdefault("evidence", []).extend(copy.deepcopy(entries))
    for bibliography in record["references"]:
        existing = [r for r in after["references"] if r["reference"] == bibliography["reference"]]
        assert len(existing) <= 1
        if existing:
            assert existing[0] == {"reference": bibliography["reference"]}
            existing[0].update(copy.deepcopy(bibliography))
        else:
            after["references"].append(copy.deepcopy(bibliography))
    after["curation_history"].append(event(before, record, timestamp, source))
    return after


def check(before, after, item):
    source, records = sources()
    record = records[item["key"]]
    assert item["action"] == ACTION and item["target_class"] == "MediaRecipe"
    assert item["id"] == before["id"] == after["id"] == record["id"]
    assert item["path"] == record["path"] and item["unresolved"] == source["limitations"]
    assert item["before_text"] == record["before_text"]
    assert (
        runner.sha(item["before_text"].encode()) == item["before_sha256"] == record["before_sha256"]
    )
    assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
    assert before == runner.load_yaml(item["before_text"]) and after == runner.load_yaml(
        item["after_text"]
    )
    assert before["media_term"]["term"]["id"] == record["source_term"]
    assert item["claims"] == record["claims"]
    check_claims(before, record, source)
    reverted = copy.deepcopy(after)
    for pointer, entries in evidence_by_owner(record).items():
        node, old = runner.get_node(reverted, pointer), runner.get_node(before, pointer)
        assert node["evidence"] == old.get("evidence", []) + entries, "Unreviewed evidence"
        if "evidence" in old:
            node["evidence"] = copy.deepcopy(old["evidence"])
        else:
            node.pop("evidence")
    for op in record["operations"]:
        parent = runner.get_node(reverted, op["pointer"][:-1])
        key = op["pointer"][-1]
        if op["remove"]:
            assert key not in parent, "Unsupported quantity restored"
        else:
            assert parent[key] == op["new"], "Unreviewed field change"
        parent[key] = copy.deepcopy(op["old"])
    old_refs = {r["reference"]: r for r in before["references"]}
    new_refs = {r["reference"]: r for r in record["references"]}
    expected = [new_refs.get(r["reference"], r) for r in before["references"]]
    expected += [r for r in record["references"] if r["reference"] not in old_refs]
    assert reverted["references"] == expected, "Unreviewed bibliography"
    reverted["references"] = copy.deepcopy(before["references"])
    added = reverted["curation_history"].pop()
    assert added == event(before, record, added["timestamp"], source), "Unreviewed history"
    assert reverted == before, "Unreviewed root/ingredient/relationship change"
    for claim in record["claims"]:
        if claim["identity_corrected"]:
            node = runner.get_node(after, claim["pointer"])
            decision = resolve_ingredient(node)
            assert decision.identifier == decision.ontology_id == claim["identity_corrected"]
    counts = collections.Counter(
        new_evidence=len(record["evidence_additions"]), new_curation_history=1
    )
    counts["new_references"] = len(new_refs.keys() - old_refs.keys())
    counts["bibliographic_entries_enriched"] = len(new_refs.keys() & old_refs.keys())
    for op in record["operations"]:
        pointer = op["pointer"]
        if pointer[-1] == "concentration":
            counts[
                "unsupported_quantity_slots_removed" if op["remove"] else "quantity_corrections"
            ] += 1
        elif pointer[-1] == "preferred_term":
            counts["ingredient_labels_corrected"] += 1
        elif pointer[-1] == "term":
            counts["ingredient_identities_corrected"] += 1
        elif pointer[0] == "preparation_steps":
            counts[
                (
                    "preparation_actions_corrected"
                    if pointer[-1] == "action"
                    else "preparation_descriptions_corrected"
                )
            ] += 1
        elif pointer[0] == "variant_children":
            counts["child_link_notes_corrected"] += 1
        elif pointer[-1] == "notes":
            counts["ingredient_context_notes_corrected"] += 1
    return counts


def safe_path(root, path):
    target = root / path
    parts = Path(path).parts
    assert target.resolve().is_relative_to(root / "data/normalized_yaml")
    assert not any(root.joinpath(*parts[:i]).is_symlink() for i in range(1, len(parts) + 1))
    return target


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
    root = root.resolve()
    assert plan["version"] == 1 and plan["action"] == ACTION and plan["source_sha256"] == SOURCE_SHA
    assert len(plan["records"]) == 5 and {r["key"] for r in plan["records"]} == KEYS
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
    for target, before, _ in pending:
        safe_path(root, target.relative_to(root))
        assert target.read_bytes() == before, "Concurrent edit during preflight"
    for target, before, after in pending:
        safe_path(root, target.relative_to(root))
        assert target.read_bytes() == before, "Concurrent edit during write"
        target.write_bytes(after)
        assert target.read_bytes() == after
    return {"changed": len(pending), "already_applied": 5 - len(pending)}


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
        assert not args.plan.exists(), "Refuse to overwrite preview"
        plan = preview()
        with args.plan.open("x") as stream:
            json.dump(plan, stream, indent=2)
            stream.write("\n")
        print(json.dumps({"reviewed": 5, "claim_rows": 105, "records_edited": 0}))


if __name__ == "__main__":
    main()
