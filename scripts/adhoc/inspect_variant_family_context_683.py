#!/usr/bin/env python3
"""Inspect pinned Carini/Jensen/Pinchuk/Tang variant context (#683, 2026-11-16).

Inputs: existing planning inventory and authoritative normalized recipe files.
Output: JSON on stdout with exact selected rows, ingredients, variants and refs.
Checks current file hashes/IDs/text. Read-only; no inference or recipe changes.
"""

import argparse
import hashlib
import json
from pathlib import Path

import yaml

FAMILIES = {
    "carini_ams1_source_family",
    "jensen_bl_source_family",
    "pinchuk_m1_source_family",
    "tang_tracer_source_family",
}


def inspect(root, inventory_path, family):
    inventory = json.loads(inventory_path.read_text())
    group = next(g for g in inventory["planning_groups"] if g["name"] == family)
    records = {}
    for number in group["queue_row_numbers"]:
        row = inventory["rows"][number - 1]
        relative = "data/normalized_yaml/" + row["source_path"]
        raw = (root / relative).read_bytes()
        digest = hashlib.sha256(raw).hexdigest()
        if digest != row["source_sha256"]:
            raise ValueError(f"source hash drift: {relative}")
        record = yaml.safe_load(raw)
        vi, mi = int(row["variant_index"]), int(row["modification_index"])
        variant = record["variants"][vi]
        if record["id"] != row["recipe_id"] or variant["name"] != row["variant_name"]:
            raise ValueError(f"identity drift: {relative}")
        if variant["modifications"][mi] != row["modification_text"]:
            raise ValueError(f"source text drift: {relative}")
        item = records.setdefault(
            relative,
            {
                "path": relative,
                "recipe_id": record["id"],
                "name": record["name"],
                "sha256": digest,
                "ingredients": record.get("ingredients", []),
                "solutions": record.get("solutions", []),
                "variants": record["variants"],
                "references": record.get("references", []),
                "queue_rows": [],
            },
        )
        item["queue_rows"].append(
            {
                "queue_row_number": number,
                "variant_index": vi,
                "modification_index": mi,
                "source_text": row["modification_text"],
            }
        )
    return {"family": family, "scientific_review": False, "records": list(records.values())}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("family", choices=sorted(FAMILIES))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--view", choices=["ingredients", "modifications", "references"])
    args = parser.parse_args()
    result = inspect(args.root, args.inventory, args.family)
    if args.view:
        for record in result["records"]:
            selected = {"path": record["path"], "recipe_id": record["recipe_id"]}
            if args.view == "ingredients":
                selected["ingredients"] = [
                    {k: item[k] for k in ("preferred_term", "concentration") if k in item}
                    for item in record["ingredients"]
                ]
            elif args.view == "modifications":
                selected["queue_rows"] = record["queue_rows"]
            else:
                selected["references"] = record["references"]
            record.clear()
            record.update(selected)
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
