#!/usr/bin/env python3
"""Audit #683 queue coverage and exact additive recipe changes (2026-11-16).

Inputs: pinned original TSV, named proposal/disposition JSONs, Git base, recipes.
Outputs: exclusive summary.json and coverage.tsv; never writes recipe files.
Preapply accepts unchanged or exactly applied records; postapply requires every
proposed assertion. This is accounting/preservation verification, not scientific
certification of assertions or of condition-only/held source prose.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
import subprocess
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
QUEUE_SHA = "dd5faea741da0a11e8eb86cad2976e8bf51d42884c601e96973eba61748330ca"
BASE = "02e005db42246b8a04ece9df4b5657e036fa5697"
STATUSES = {
    "STRUCTURED",
    "CONDITION_ONLY",
    "ALREADY_STRUCTURED",
    "HELD_EVIDENCE",
    "HELD_MODEL",
}
SOURCE = "https://github.com/CultureBotAI/CultureMech/issues/683"
NOTES = (
    "Represent source-supported ingredient changes within their existing variants; "
    "preserve base formulation, source prose, stages and unresolved identities. "
    "LLM-assisted curation; no human review status asserted."
)


def require(condition, message):
    if not condition:
        raise ValueError(message)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def named_paths(values):
    result = {}
    for value in values:
        name, separator, path = value.partition("=")
        require(separator and name and path and name not in result, "invalid/duplicate cohort")
        result[name] = Path(path)
    return result


def integer(value, label):
    require(type(value) is int and value >= 0, "invalid nonnegative integer: " + label)
    return value


def coordinate(path, variant, modification):
    return path, variant, modification


def read_queue(raw):
    require(digest(raw) == QUEUE_SHA, "original queue digest mismatch")
    old_limit = csv.field_size_limit()
    try:
        csv.field_size_limit(16 * 1024 * 1024)
        rows = list(csv.DictReader(io.StringIO(raw.decode("utf-8")), delimiter="\t"))
    finally:
        csv.field_size_limit(old_limit)
    require(len(rows) == 396, "expected all 396 original modification rows")
    coordinates = {}
    for number, row in enumerate(rows, 1):
        require(row["row_kind"] == "modification", "unexpected queue row kind")
        relative = Path(row["source_path"])
        require(
            not relative.is_absolute() and ".." not in relative.parts,
            "unsafe queue source path",
        )
        row["record_path"] = "data/normalized_yaml/" + relative.as_posix()
        row["variant_index"] = int(row["variant_index"])
        row["modification_index"] = int(row["modification_index"])
        require(row["variant_index"] >= 0 and row["modification_index"] >= 0, "negative index")
        key = coordinate(row["record_path"], row["variant_index"], row["modification_index"])
        require(key not in coordinates, "duplicate source coordinate")
        coordinates[key] = number
    return rows, coordinates


def check_preservation(base, current, proposal, proposal_sha, mode):
    """Return application status only after exact field/event and base restoration checks."""
    restored = copy.deepcopy(current)
    applied = []
    for variant in proposal["variants"]:
        index = variant["variant_index"]
        require("ingredient_changes" not in base["variants"][index], "base already structured")
        present = restored["variants"][index].get("ingredient_changes")
        if "ingredient_changes" in restored["variants"][index]:
            require(present == variant["ingredient_changes"], "applied assertions differ")
            del restored["variants"][index]["ingredient_changes"]
            applied.append(True)
        else:
            applied.append(False)
    require(all(applied) or not any(applied), "partially applied record")
    if any(applied):
        original_history = base.get("curation_history", [])
        history = restored.get("curation_history", [])
        require(len(history) == len(original_history) + 1, "wrong appended event count")
        require(history[:-1] == original_history, "previous curation history changed")
        event = history[-1]
        require(
            set(event) == {"timestamp", "curator", "action", "notes", "source", "changes"}
            and bool(event["timestamp"])
            and event["curator"] == "codex"
            and event["action"] == "STRUCTURED_VARIANT_INGREDIENTS"
            and event["source"] == SOURCE
            and event["notes"] == NOTES,
            "unexpected curation event metadata",
        )
        require(
            json.loads(event["changes"])
            == {"decision_sha256": proposal_sha, "variants": proposal["variants"]},
            "curation event does not bind exact proposal digest/assertions",
        )
        if "curation_history" in base:
            restored["curation_history"] = history[:-1]
        else:
            del restored["curation_history"]
    require(restored == base, "unrelated parsed recipe content changed")
    require(mode != "postapply" or all(applied), "proposed record not applied")
    return "APPLIED" if all(applied) else "NOT_APPLIED"


def audit(root, queue, proposals, disposition_paths, mode):
    snapshots = {}

    def read(path):
        path = path.resolve()
        raw = path.read_bytes()
        require(path not in snapshots or snapshots[path] == raw, "input changed while reading")
        snapshots[path] = raw
        return raw

    rows, coordinates = read_queue(read(queue))
    base_records, current_records = {}, {}
    for row in rows:
        path = row["record_path"]
        if path not in base_records:
            raw = subprocess.check_output(["git", "show", BASE + ":" + path], cwd=root)
            require(digest(raw) == row["source_sha256"], "queue/Git base hash mismatch: " + path)
            base_records[path] = (yaml.safe_load(raw), digest(raw))
            current_records[path] = yaml.safe_load(read(root / path))
        base, base_sha = base_records[path]
        require(base_sha == row["source_sha256"], "inconsistent queue source hash")
        require(base["id"] == row["recipe_id"], "queue recipe identity mismatch")
        variant = base["variants"][row["variant_index"]]
        require(variant["name"] == row["variant_name"], "queue variant identity mismatch")
        require(variant == json.loads(row["variant_json"]), "queue variant snapshot mismatch")
        require(
            variant["modifications"][row["modification_index"]] == row["modification_text"],
            "queue source text mismatch",
        )
    require(set(disposition_paths) <= set(proposals), "orphan disposition input")
    dispositions, all_records, assertion_counts, cohort_summary = {}, {}, Counter(), {}
    inputs = []
    for name, path in proposals.items():
        raw = read(path)
        proposal_sha = digest(raw)
        document = json.loads(raw)
        require(document["schema_version"] == 1, "unsupported proposal schema")
        require(document.get("source_queue_sha256", QUEUE_SHA) == QUEUE_SHA, "wrong queue pin")
        inputs.append(
            {"cohort": name, "kind": "proposal", "path": str(path), "sha256": proposal_sha}
        )
        disposition_doc = document
        if name in disposition_paths:
            disposition_raw = read(disposition_paths[name])
            disposition_doc = json.loads(disposition_raw)
            require(
                disposition_doc["source_queue_sha256"] == QUEUE_SHA, "wrong disposition queue pin"
            )
            inputs.append(
                {
                    "cohort": name,
                    "kind": "dispositions",
                    "path": str(disposition_paths[name]),
                    "sha256": digest(disposition_raw),
                }
            )
        selected = set()
        for disposition in disposition_doc["dispositions"]:
            number = integer(disposition["queue_row_number"], "queue row")
            require(
                1 <= number <= len(rows) and number not in dispositions,
                "duplicate/invalid disposition row",
            )
            require(disposition["status"] in STATUSES, "unknown disposition")
            require(
                isinstance(disposition["reason"], str) and disposition["reason"].strip(),
                "missing disposition reason",
            )
            integer(disposition["assertion_count"], "assertion count")
            dispositions[number] = dict(disposition, cohort=name)
            selected.add(number)
        cohort_assertions = 0
        for record in document["records"]:
            record_path = record["path"]
            require(
                record_path in base_records and record_path not in all_records,
                "unknown/overlapping proposal recipe",
            )
            base, base_sha = base_records[record_path]
            require(
                record["expected_sha256"] == base_sha and record["recipe_id"] == base["id"],
                "proposal preimage/identity mismatch",
            )
            require(record["variants"], "empty proposed record")
            variants_seen = set()
            for variant in record["variants"]:
                index = integer(variant["variant_index"], "variant index")
                require(index not in variants_seen, "duplicate proposed variant")
                variants_seen.add(index)
                require(
                    base["variants"][index]["name"] == variant["variant_name"],
                    "proposal variant mismatch",
                )
                require(variant["ingredient_changes"], "empty proposed variant")
                changes_seen = set()
                for change in variant["ingredient_changes"]:
                    modification = integer(
                        change["source_modification_index"], "modification index"
                    )
                    number = coordinates[coordinate(record_path, index, modification)]
                    require(number in selected, "assertion belongs to another cohort")
                    require(
                        change["source_text"] == rows[number - 1]["modification_text"],
                        "assertion source text mismatch",
                    )
                    signature = json.dumps(change, sort_keys=True, ensure_ascii=False)
                    require(signature not in changes_seen, "duplicate assertion")
                    changes_seen.add(signature)
                    assertion_counts[number] += 1
                    cohort_assertions += 1
            state = check_preservation(
                base, current_records[record_path], record, proposal_sha, mode
            )
            all_records[record_path] = {
                "cohort": name,
                "state": state,
                "variants": len(record["variants"]),
            }
        cohort_summary[name] = {
            "rows": len(selected),
            "assertions": cohort_assertions,
            "records": len(document["records"]),
        }
    require(set(dispositions) == set(range(1, len(rows) + 1)), "queue coverage is incomplete")
    coverage = []
    for number, row in enumerate(rows, 1):
        disposition = dispositions[number]
        count = assertion_counts[number]
        require(
            disposition["assertion_count"] == count,
            "disposition/assertion count mismatch at row " + str(number),
        )
        require(
            (disposition["status"] == "STRUCTURED") == (count > 0),
            "structured status/count mismatch",
        )
        state = all_records.get(row["record_path"], {}).get("state", "NO_ASSERTIONS")
        coverage.append(
            {
                "queue_row_number": number,
                "cohort": disposition["cohort"],
                "recipe_id": row["recipe_id"],
                "source_path": row["source_path"],
                "source_sha256": row["source_sha256"],
                "variant_index": row["variant_index"],
                "variant_name": row["variant_name"],
                "modification_index": row["modification_index"],
                "modification_text": row["modification_text"],
                "status": disposition["status"],
                "reason": disposition["reason"],
                "assertion_count": count,
                "applied_assertion_count": count if state == "APPLIED" else 0,
            }
        )
    for path in set(base_records) - set(all_records):
        require(
            current_records[path] == base_records[path][0], "unproposed recipe changed: " + path
        )
    for path, raw in snapshots.items():
        require(path.read_bytes() == raw, "input changed during audit: " + str(path))
    summary = {
        "schema_version": 1,
        "result": "PASS",
        "mode": mode,
        "git_base": BASE,
        "queue_sha256": QUEUE_SHA,
        "queue_rows": len(rows),
        "queue_recipes": len(base_records),
        "queue_variants": len({(r["record_path"], r["variant_index"]) for r in rows}),
        "proposal_assertions": sum(assertion_counts.values()),
        "applied_assertions": sum(r["applied_assertion_count"] for r in coverage),
        "proposal_records": len(all_records),
        "record_states": dict(Counter(r["state"] for r in all_records.values())),
        "dispositions": dict(Counter(r["status"] for r in coverage)),
        "cohorts": cohort_summary,
        "input_files": inputs,
        "record_snapshots": [
            {
                "path": p,
                "base_sha256": base_records[p][1],
                "current_sha256": digest(snapshots[(root / p).resolve()]),
            }
            for p in sorted(base_records)
        ],
        "checks": [
            "exact pinned queue with unique coordinates",
            "all original 396 rows disposed exactly once",
            "recipe/variant/source-text identity",
            "per-row proposal/disposition assertion equality",
            "exact applied assertions and proposal-bound history",
            "parsed original recipe restored by removing only authorized additions",
            "all inputs stable through final read",
        ],
        "limitations": "Accounting and parsed-data preservation only. Does not certify source science, human review, whole-catalog completeness beyond this queue, or unchanged YAML presentation.",
    }
    return summary, coverage


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--proposal", action="append", required=True, metavar="COHORT=JSON")
    parser.add_argument("--dispositions", action="append", default=[], metavar="COHORT=JSON")
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--mode", choices=["preapply", "postapply"], required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    summary, coverage = audit(
        args.root.resolve(),
        args.queue,
        named_paths(args.proposal),
        named_paths(args.dispositions),
        args.mode,
    )
    args.output_dir.mkdir(parents=True, exist_ok=False)
    target = args.output_dir / "coverage.tsv"
    with target.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=list(coverage[0]), delimiter="\t")
        writer.writeheader()
        writer.writerows(coverage)
    summary["coverage_sha256"] = digest(target.read_bytes())
    with (args.output_dir / "summary.json").open("x", encoding="utf-8") as stream:
        json.dump(summary, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(
        json.dumps(
            {k: v for k, v in summary.items() if k not in {"input_files", "record_snapshots"}},
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
