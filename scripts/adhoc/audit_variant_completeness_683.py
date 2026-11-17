#!/usr/bin/env python3
"""Merge reviewed #683 cohorts or audit complete source coverage (2026-11-16).

Inputs: independently pinned proposals, original immutable queue, authenticated
successor capsules and current recipes. Outputs: new proposal/coverage artifacts.
Never edits recipes or infers scientific approval from a label or assertion count.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
from adhoc.audit_variant_coverage_683 import read_queue  # noqa: E402
from curate_variant_completeness import apply_decision, recipe_path  # noqa: E402

from culturemech.validation.write_validated import validate_recipe  # noqa: E402

PRIOR = (
    "bbm-dispositions-683",
    "utex-optional-683",
    "remaining-families-683",
    "carini-jensen-pinchuk-tang-683",
    "bacterial-specialized-dispositions-683",
    "algae-archaea-683",
)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def require(value, reason):
    if not value:
        raise ValueError(reason)


def pinned(path, pin):
    require(path.is_file() and not path.is_symlink(), "Expected regular proposal")
    raw = path.read_bytes()
    require(digest(raw) == pin, "Proposal digest mismatch")
    return json.loads(raw)


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("x", encoding="utf-8") as stream:
        json.dump(value, stream, indent=2, ensure_ascii=False)
        stream.write("\n")


def merge(inputs, output):
    records, dispositions, pins = {}, {}, []
    for source, pin in inputs:
        path = Path(source)
        document = pinned(path, pin)
        require(document["schema_version"] == 1, "Unknown proposal format")
        pins.append({"path": path.as_posix(), "sha256": pin})
        source_paths = set()
        for item in document["dispositions"]:
            number = item["queue_row_number"]
            require(number not in dispositions, "Overlapping reviewed row disposition")
            dispositions[number] = item
        for item in document["records"]:
            require(item["path"] not in source_paths, "Duplicate record within source cohort")
            source_paths.add(item["path"])
            raw = recipe_path(ROOT, item["path"]).read_bytes()
            require(digest(raw) == item["expected_sha256"], "Source proposal preimage changed")
            before = yaml.safe_load(raw)
            require(before["id"] == item["recipe_id"], "Source proposal identity changed")
            try:
                apply_decision(before, item)
            except ValueError as exc:
                if str(exc) != "decision contains no changes":
                    raise
            if item["path"] not in records:
                records[item["path"]] = copy.deepcopy(item)
                continue
            combined = records[item["path"]]
            require(
                all(combined[key] == item[key] for key in ("recipe_id", "expected_sha256")),
                "Inconsistent proposal preimage",
            )
            combined.setdefault("field_replacements", []).extend(
                copy.deepcopy(item.get("field_replacements", []))
            )
            variants = {v["variant_index"]: v for v in combined["variants"]}
            for variant in item["variants"]:
                index = variant["variant_index"]
                if index not in variants:
                    combined["variants"].append(copy.deepcopy(variant))
                    variants[index] = combined["variants"][-1]
                    continue
                require(
                    variants[index]["variant_name"] == variant["variant_name"],
                    "Variant identity conflict",
                )
                for key, value in variant.items():
                    if key not in {"variant_index", "variant_name"}:
                        require(isinstance(value, list), "Mutation payload is not a list")
                        variants[index].setdefault(key, []).extend(copy.deepcopy(value))
    mutations = []
    for record in records.values():
        # Disposition-only source rows remain in the ledger, not empty histories.
        raw = recipe_path(ROOT, record["path"]).read_bytes()
        require(digest(raw) == record["expected_sha256"], "Recipe changed since source review")
        before = yaml.safe_load(raw)
        require(before["id"] == record["recipe_id"], "Recipe identity differs from proposal")
        try:
            desired, _ = apply_decision(before, record)
        except ValueError as exc:
            if str(exc) == "decision contains no changes":
                continue
            raise
        errors = validate_recipe(desired)
        require(not errors, f"Merged proposal fails native validation: {record['path']}: {errors}")
        mutations.append(record)
    value = {
        "schema_version": 1,
        "reviewed_inputs": pins,
        "records": sorted(mutations, key=lambda item: item["path"]),
        "dispositions": [dispositions[n] for n in sorted(dispositions)],
    }
    write_json(output, value)
    return {
        "sha256": digest(output.read_bytes()),
        "records": len(mutations),
        "dispositions": len(dispositions),
    }


def audit(queue, proposal_path, pin, output):
    # Imported lazily so preview/merge can precede final capsule generation.
    from audit_variant_completeness_successor import retained_evidence
    from audit_variant_ingredient_successor import restore_before

    proposal = pinned(proposal_path, pin)
    require(
        retained_evidence()[2]["decisions"]["sha256"] == pin,
        "Coverage proposal differs from authenticated applied decisions",
    )
    queue_bytes = queue.read_bytes()
    rows, _ = read_queue(queue_bytes)
    dispositions, inputs = {}, []
    for name in PRIOR:
        path = ROOT / "conf/variant_ingredient_curation" / (name + ".json")
        raw = path.read_bytes()
        inputs.append({"path": path.relative_to(ROOT).as_posix(), "sha256": digest(raw)})
        for row in json.loads(raw)["dispositions"]:
            number = row["queue_row_number"]
            require(number not in dispositions, "Duplicate original coverage row")
            dispositions[number] = row
    require(set(dispositions) == set(range(1, len(rows) + 1)), "Original coverage incomplete")
    revised = set()
    for item in proposal["dispositions"]:
        number = item["queue_row_number"]
        require(
            number in dispositions and number not in revised,
            "Invalid/duplicate revised disposition",
        )
        require(item["reason"].strip(), "Missing reviewed disposition reason")
        revised.add(number)
        dispositions[number] = item
    snapshots, records, coverage, actions = {}, {}, [], Counter()
    held_total = 0
    for number, row in enumerate(rows, 1):
        path = row["record_path"]
        if path not in records:
            raw = (ROOT / path).read_bytes()
            original = restore_before(raw, path)
            require(
                digest(original) == row["source_sha256"],
                "Successor does not restore original queue bytes",
            )
            records[path] = yaml.safe_load(raw)
            require(not validate_recipe(records[path]), "Current recipe fails native validation")
            snapshots[path] = {
                "path": path,
                "base_sha256": digest(original),
                "current_sha256": digest(raw),
            }
        record = records[path]
        require(record["id"] == row["recipe_id"], "Recipe identity changed")
        variant = record["variants"][row["variant_index"]]
        require(variant["name"] == row["variant_name"], "Variant identity changed")
        index = row["modification_index"]
        changes = [
            c
            for c in variant.get("ingredient_changes", [])
            if c["source_modification_index"] == index
        ]
        mentions = [
            m
            for m in variant.get("ingredient_mentions", [])
            if m["source_modification_index"] == index
        ]
        disposition = dispositions[number]
        status = disposition["status"]
        require(
            status
            in {
                "STRUCTURED",
                "PARTIALLY_STRUCTURED",
                "HELD_EVIDENCE",
                "HELD_MODEL",
                "CONDITION_ONLY",
                "CONTEXT_ONLY",
                "ALREADY_STRUCTURED",
            },
            f"Unknown reviewed disposition at row {number}",
        )
        if status in {"HELD_EVIDENCE", "HELD_MODEL", "PARTIALLY_STRUCTURED"}:
            require(mentions, f"Reviewed hold lacks a retained named claim at row {number}")
        if status == "STRUCTURED":
            require(changes, f"Reviewed structured row lacks an applied change at row {number}")
        if mentions:
            status = "PARTIALLY_STRUCTURED" if changes else "WITHHELD_NAMED_CLAIMS"
        elif changes:
            status = "STRUCTURED"
        else:
            require(
                status in {"CONDITION_ONLY", "CONTEXT_ONLY", "ALREADY_STRUCTURED"},
                f"Unrepresented held claims at row {number}",
            )
        actions.update(c["action"] for c in changes)
        held_total += len(mentions)
        coverage.append(
            {
                "queue_row_number": number,
                "recipe_id": row["recipe_id"],
                "source_path": row["source_path"],
                "source_sha256": row["source_sha256"],
                "variant_index": row["variant_index"],
                "variant_name": row["variant_name"],
                "modification_index": index,
                "modification_text": row["modification_text"],
                "current_modification_text": variant["modifications"][index],
                "status": status,
                "reviewed_status": disposition["status"],
                "reason": disposition["reason"],
                "applied_assertion_count": len(changes),
                "held_mention_count": len(mentions),
            }
        )
    actual_events = sum(
        len(v.get("ingredient_changes", []))
        for r in records.values()
        for v in r.get("variants", [])
    )
    actual_holds = sum(
        len(v.get("ingredient_mentions", []))
        for r in records.values()
        for v in r.get("variants", [])
    )
    require(
        actual_events == sum(actions.values()) and actual_holds == held_total,
        "Unaccounted structured source coordinates",
    )
    for path, snapshot in snapshots.items():
        require(
            digest((ROOT / path).read_bytes()) == snapshot["current_sha256"],
            "Recipe changed during coverage audit",
        )
    require(
        queue.read_bytes() == queue_bytes and digest(proposal_path.read_bytes()) == pin,
        "Audit input changed during coverage audit",
    )
    for item in inputs:
        require(
            digest((ROOT / item["path"]).read_bytes()) == item["sha256"],
            "Prior disposition changed during coverage audit",
        )
    output.mkdir(parents=True, exist_ok=False)
    with (output / "coverage.tsv").open("x", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, list(coverage[0]), delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(coverage)
    summary = {
        "schema_version": 2,
        "result": "PASS",
        "mode": "postapply",
        "queue_sha256": digest(queue_bytes),
        "queue_rows": len(rows),
        "queue_recipes": len(records),
        "queue_variants": len({(r["record_path"], r["variant_index"]) for r in rows}),
        "applied_assertions": actual_events,
        "changes_by_action": dict(actions),
        "held_mentions": held_total,
        "dispositions": dict(Counter(row["status"] for row in coverage)),
        "record_snapshots": [snapshots[p] for p in sorted(snapshots)],
        "reviewed_proposal_sha256": pin,
        "prior_disposition_inputs": inputs,
        "coverage_sha256": digest((output / "coverage.tsv").read_bytes()),
        "scope": "All original396 variant-modification rows; explicit unresolved names retained separately. Other free-text fields and referenced-table expansions are not claimed exhaustive.",
    }
    write_json(output / "summary.json", summary)
    return {
        key: value
        for key, value in summary.items()
        if key not in {"record_snapshots", "prior_disposition_inputs"}
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    combine = sub.add_parser("merge")
    combine.add_argument(
        "--proposal", action="append", nargs=2, required=True, metavar=("PATH", "SHA256")
    )
    combine.add_argument("--output", type=Path, required=True)
    check = sub.add_parser("audit")
    check.add_argument("--queue", type=Path, required=True)
    check.add_argument("--proposal", type=Path, required=True)
    check.add_argument("--expected-proposal-sha256", required=True)
    check.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    value = (
        merge(args.proposal, args.output)
        if args.command == "merge"
        else audit(args.queue, args.proposal, args.expected_proposal_sha256, args.output)
    )
    print(json.dumps(value, indent=2))


if __name__ == "__main__":
    main()
