"""Preview and apply evidence-pinned enriched-seawater stock-boundary repairs."""

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
HERE = ROOT / "reports/ingredient_concentration_curation/20261010-utex-es"
PLAN = HERE / "plan-v3.json"
SOURCE_SHA = "546319e22f1c69fb730acc2e407376f7af581b1d5d90ec6451b3f0a47eb06276"
ACTION = "CURATED_UTEX_ES_NESTED_STOCKS_AND_INGREDIENT_EVIDENCE"
KEYS = {
    "enriched-seawater-medium",
    "es-over-10-enriched-seawater-medium",
    "es-over-2-enriched-seawater-medium",
    "es-over-4-enriched-seawater-medium",
    "one-half-enriched-seawater-medium",
    "two-thirds-enriched-seawater-medium",
}


def sources():
    raw = (HERE / "source-review-v2.json").read_bytes()
    assert runner.sha(raw) == SOURCE_SHA, "Source ledger drift"
    source = json.loads(raw)
    records = {r["key"]: r for r in source["records"]}
    assert len(source["records"]) == 6 and set(records) == KEYS
    assert sum(len(r["claims"]) for r in records.values()) == 124
    return source, records


def relocated(pointer, expanded):
    if expanded and len(pointer) >= 2 and pointer[0] == "solutions" and pointer[1] > 0:
        return ["solutions", 0, "solutions", pointer[1] - 1] + pointer[2:]
    return pointer[:]


def check_claims(before, record, source):
    assert before == runner.load_yaml(record["before_text"])
    assert [c["pointer"] for c in runner.all_claims(before)] == [
        c["pointer"] for c in record["claims"]
    ]
    for claim in record["claims"]:
        node = runner.get_node(before, claim["pointer"])
        assert node["preferred_term"] == claim["ingredient"]
        assert node["concentration"] == claim["old"]
        assert claim["status"] in {"correct", "evidence_only"}
        assert claim["proposed_pointer"] == relocated(claim["pointer"], record["expanded"])
        assert claim["snippet"] in source["sources"][claim["reference"]]["text"]
        assert (
            runner.field_name(claim["proposed_pointer"] + ["concentration"]) in claim["explanation"]
        )
    pointers = [tuple(op["pointer"]) for op in record["operations"]]
    assert len(pointers) == len(set(pointers)), "Overlapping operations"
    owners = collections.defaultdict(list)
    for item in record["evidence_additions"]:
        evidence = item["evidence"]
        assert evidence["snippet"] in source["sources"][evidence["reference"]]["text"]
        assert evidence["supports"] == "SUPPORT" and "Locator:" in evidence["explanation"]
        assert item["pointer"] == relocated(item["before_pointer"], record["expanded"])
        owners[tuple(item["pointer"])].append(evidence["reference"])
    assert all(len(refs) == len(set(refs)) for refs in owners.values())


def event(before, record, timestamp, source):
    doc = copy.deepcopy(before)
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="https://utex.org/products/" + record["key"],
        changes=json.dumps(
            {
                "fields": record["operations"],
                "stock_relocations": record["relocations"],
                "evidence_claims": [
                    {"pointer": e["pointer"], "reference": e["evidence"]["reference"]}
                    for e in record["evidence_additions"]
                ],
                "bibliography": [r["reference"] for r in record["references"]],
            },
            sort_keys=True,
        ),
        notes=(
            f"Added {len(record['evidence_additions'])} claim-linked evidence entries and "
            f"added or enriched {len(record['references'])} bibliography "
            f"{'entry' if len(record['references']) == 1 else 'entries'} in this record. "
            "Related formulation/stock limitations for this review batch: "
            + " ".join(source["limitations"])
        ),
    )
    return doc["curation_history"][-1]


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
    if record["expanded"]:
        stocks = after["solutions"]
        assert len(stocks) == 6 and "solutions" not in stocks[0]
        assert [s["preferred_term"] for s in stocks[1:]] == [
            r["ingredient"] for r in record["relocations"]
        ]
        stocks[0]["solutions"] = stocks[1:]
        after["solutions"] = stocks[:1]
    for addition in record["evidence_additions"]:
        node = runner.get_node(after, addition["pointer"])
        evidence = copy.deepcopy(addition["evidence"])
        assert evidence["reference"] not in {e["reference"] for e in node.get("evidence", [])}
        node.setdefault("evidence", []).append(evidence)
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
    assert before == runner.load_yaml(item["before_text"])
    assert after == runner.load_yaml(item["after_text"])
    assert before["media_term"]["term"]["id"] == record["source_term"]
    assert item["claims"] == record["claims"]
    check_claims(before, record, source)

    # Remove only the pinned additions before reversing the nested-stock move.
    reverted = copy.deepcopy(after)
    grouped = collections.defaultdict(list)
    old_pointers = {}
    for addition in record["evidence_additions"]:
        pointer = tuple(addition["pointer"])
        grouped[pointer].append(addition["evidence"])
        old_pointers[pointer] = addition["before_pointer"]
    for pointer, entries in grouped.items():
        node = runner.get_node(reverted, pointer)
        old = runner.get_node(before, old_pointers[pointer])
        assert node["evidence"] == old.get("evidence", []) + entries, "Unreviewed evidence"
        if "evidence" in old:
            node["evidence"] = copy.deepcopy(old["evidence"])
        else:
            node.pop("evidence")
    if record["expanded"]:
        assert len(reverted["solutions"]) == 1, "Unreviewed root stock membership"
        enrichment = reverted["solutions"][0]
        nested = enrichment.pop("solutions")
        assert len(nested) == 5
        assert [s["preferred_term"] for s in nested] == [
            r["ingredient"] for r in record["relocations"]
        ]
        reverted["solutions"] = [enrichment] + nested
    for op in record["operations"]:
        parent = runner.get_node(reverted, op["pointer"][:-1])
        key = op["pointer"][-1]
        if op["remove"]:
            assert key not in parent, "Unsupported assertion restored"
        else:
            if isinstance(parent, dict):
                assert key in parent, "Unreviewed field removal"
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
    assert reverted == before, "Unreviewed root, ingredient or relationship change"
    for claim in record["claims"]:
        node = runner.get_node(after, claim["proposed_pointer"])
        assert node.get("concentration") == claim["new"]
        identity = claim.get("identity_corrected")
        if identity:
            decision = resolve_ingredient(node)
            expected_id = None if identity == "unsupported-identifiers-removed" else identity
            assert decision.identifier == decision.ontology_id == expected_id
    counts = collections.Counter(
        new_evidence=len(record["evidence_additions"]),
        new_curation_history=1,
        stock_nodes_relocated=len(record["relocations"]),
        stock_dose_basis_corrections=len(record["relocations"]),
        new_references=len(new_refs.keys() - old_refs.keys()),
        bibliographic_entries_enriched=len(new_refs.keys() & old_refs.keys()),
    )
    for op in record["operations"]:
        pointer = op["pointer"]
        if pointer[-1] == "concentration":
            counts[
                "unsupported_quantity_slots_removed" if op["remove"] else "quantity_corrections"
            ] += 1
        elif pointer[-1] == "preferred_term":
            counts["ingredient_labels_corrected"] += 1
        elif pointer[-1] == "term":
            counts[
                (
                    "unsupported_primary_identities_removed"
                    if op["remove"]
                    else "ingredient_identities_corrected"
                )
            ] += 1
        elif pointer[-1] == "mediaingredientmech_chebi_term" and op["remove"]:
            counts["unsupported_secondary_identities_removed"] += 1
        elif pointer[0] in {"parent_media", "variant_children", "variant_modifications"}:
            counts["relationship_dose_descriptions_corrected"] += 1
        elif pointer[-1] == "notes":
            counts["ingredient_context_notes_corrected"] += 1
    return +counts


def safe_path(root, path):
    target = root / path
    parts = Path(path).parts
    assert target.resolve().is_relative_to(root / "data/normalized_yaml")
    assert not any(root.joinpath(*parts[:i]).is_symlink() for i in range(1, len(parts) + 1))
    return target


def preview(root=ROOT):
    root = root.resolve()
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
    assert len(plan["records"]) == 6 and {r["key"] for r in plan["records"]} == KEYS
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
    return {"changed": len(pending), "already_applied": 6 - len(pending)}


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
        print(json.dumps({"reviewed": 6, "claim_rows": 124, "records_edited": 0}))


if __name__ == "__main__":
    main()
