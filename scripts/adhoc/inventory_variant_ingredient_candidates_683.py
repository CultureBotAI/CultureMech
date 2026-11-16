#!/usr/bin/env python3
"""Read-only curation planning inventory for variant prose (2026-11-16; issue 683).

Inputs: preserved CSV/TSV queue and authoritative normalized YAML directory.
Outputs: lossless JSON inventory and compact human-readable rows in a new directory.
This checks source coordinates and hashes; it makes no ingredient/scientific decisions.
"""

import argparse
from collections import Counter
import csv
import hashlib
import json
from pathlib import Path

import yaml


def digest(data):
    return hashlib.sha256(data).hexdigest()


def planning_groups(rows, queue_hash):
    """Scheduling groups from full manual row inspection, never scientific dispositions."""
    if queue_hash != "dd5faea741da0a11e8eb86cad2976e8bf51d42884c601e96973eba61748330ca":
        return []
    selections = [
        ("bbm_stage_context_canary", set(range(21, 25))),
        ("utex_optional_agar_carbonate", {1, 2, 3, 4, 25, 34, 35, 36, 44, 45, 56, 57, 58, 59, 60, 61, 73}),
        ("carini_ams1_source_family", set(range(146, 188)) | set(range(204, 218))),
        ("jensen_bl_source_family", set(range(237, 257))),
        ("middlebrook_alternative_recipe", set(range(321, 337))),
        ("dsmz_670_source_version_changes", set(range(290, 304))),
        ("pinchuk_m1_source_family", set(range(360, 372))),
        ("tang_tracer_source_family", {337, 338} | set(range(342, 350))),
        ("villasenor_mm_source_family", set(range(350, 360))),
        ("nordkvist_ms10_source_family", set(range(372, 380))),
        ("mattanovich_chemostat_source_family", set(range(220, 227))),
    ]
    used = set()
    for _, numbers in selections:
        if used & numbers:
            raise ValueError("planning groups overlap")
        used.update(numbers)
    for category in ("algae", "archaea", "bacterial", "specialized"):
        numbers = {i for i, row in enumerate(rows, 1)
                   if i not in used and Path(row["source_path"]).parts[0] == category}
        selections.append((category + "_remaining", numbers))
        used.update(numbers)
    if used != set(range(1, len(rows) + 1)):
        raise ValueError("planning groups do not cover every row")
    groups = []
    for name, numbers in selections:
        selected = [rows[number - 1] for number in sorted(numbers)]
        groups.append({
            "name": name,
            "rows": len(selected),
            "recipes": len({row["source_path"] for row in selected}),
            "variants": len({(row["source_path"], row["variant_index"]) for row in selected}),
            "queue_row_numbers": sorted(numbers),
            "scientific_review": False,
        })
    return groups


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", required=True, type=Path)
    parser.add_argument("--input-dir", required=True, type=Path)
    parser.add_argument("--output-dir", required=True, type=Path)
    args = parser.parse_args()
    source_root = args.input_dir.resolve(strict=True)
    output = args.output_dir.resolve()
    if output == source_root or source_root in output.parents:
        raise ValueError("output must be outside the authoritative input tree")
    csv.field_size_limit(16 * 1024 * 1024)
    with args.queue.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    records = {}
    variants = {}
    seen = set()
    lines = []
    for number, row in enumerate(rows, 1):
        relative = Path(row["source_path"])
        source = (source_root / relative).resolve(strict=True)
        if relative.is_absolute() or source_root not in source.parents:
            raise ValueError("queue source escaped the authoritative tree")
        if row["source_path"] not in records:
            content = source.read_bytes()
            document = yaml.safe_load(content)
            records[row["source_path"]] = {
                "sha256": digest(content),
                "document": document,
            }
        record = records[row["source_path"]]
        if record["sha256"] != row["source_sha256"]:
            raise ValueError("source digest differs from preserved queue: " + row["source_path"])
        document = record["document"]
        if document["id"] != row["recipe_id"]:
            raise ValueError("recipe identity differs from queue")
        vi, mi = int(row["variant_index"]), int(row["modification_index"])
        variant = document["variants"][vi]
        coordinate = (row["source_path"], vi, mi)
        if coordinate in seen:
            raise ValueError("duplicate source coordinate")
        seen.add(coordinate)
        if row["row_kind"] != "modification":
            raise ValueError("unexpected context-only row; inspect its semantics before extending")
        if variant["modifications"][mi] != row["modification_text"]:
            raise ValueError("modification text differs from source")
        if variant != json.loads(row["variant_json"]):
            raise ValueError("variant context differs from source")
        if document.get("references") != json.loads(row["record_references_json"]):
            raise ValueError("record references differ from source")
        key = (row["source_path"], vi)
        variants[key] = {
            "recipe_id": row["recipe_id"],
            "source_path": row["source_path"],
            "source_sha256": row["source_sha256"],
            "variant_index": vi,
            "variant": variant,
            "record_references": document.get("references"),
        }
        lines.append(
            f"{number:03d}\t{row['recipe_id']}\t{row['source_path']}\t"
            f"v{vi}m{mi}\t{row['variant_name']}\t"
            + json.dumps(row["modification_text"], ensure_ascii=False)
        )
    expected = {
        (path, vi, mi)
        for path, record in records.items()
        for vi, variant in enumerate(record["document"].get("variants", []))
        for mi, _ in enumerate(variant.get("modifications", []))
    }
    if seen != expected:
        raise ValueError("queue does not cover every modification in its represented recipes")
    summary = {
        "scientific_review": False,
        "queue_sha256": digest(args.queue.read_bytes()),
        "queue_rows": len(rows),
        "recipes": len(records),
        "variants": len(variants),
        "category_rows": dict(Counter(Path(row["source_path"]).parts[0] for row in rows)),
        "variant_relationships": dict(Counter(value["variant"].get("relationship", "unspecified")
                                              for value in variants.values())),
        "source_hashes_and_coordinates_verified": True,
        "limitations": "Only the preserved queue and its represented recipes are checked; no scientific claims or full-catalog absence inferred.",
    }
    groups = planning_groups(rows, summary["queue_sha256"])
    payload = {"summary": summary, "planning_groups": groups, "rows": rows, "variants": list(variants.values())}
    output.mkdir(parents=True, exist_ok=False)
    (output / "inventory.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (output / "rows.tsv").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
