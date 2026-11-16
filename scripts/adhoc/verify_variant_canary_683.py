#!/usr/bin/env python3
"""Verify one variant canary's persisted side effects (2026-11-16, CultureMech #683).

Inputs: reviewed decisions, applied recipe, subset bundle and source git revision.
Output: JSON receipt proving retained base/prose and exported stage-bound changes.
"""

import argparse
import csv
import hashlib
import json
import subprocess
from pathlib import Path

import yaml


def rows(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def require(condition, message):
    if not condition:
        raise ValueError(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decisions", type=Path, required=True)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--record", help="Exact recipe path when the proposal has several records")
    parser.add_argument("--baseline", default="02e005db42246b8a04ece9df4b5657e036fa5697")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    selected = [
        record
        for record in json.loads(args.decisions.read_text())["records"]
        if args.record is None or record["path"] == args.record
    ]
    require(len(selected) == 1, "select exactly one canary record")
    decision = selected[0]
    before = yaml.safe_load(
        subprocess.check_output(["git", "show", args.baseline + ":" + decision["path"]], cwd=root)
    )
    after = yaml.safe_load((root / decision["path"]).read_bytes())
    restored = json.loads(json.dumps(after))
    for item in decision["variants"]:
        actual = restored["variants"][item["variant_index"]].pop("ingredient_changes")
        require(actual == item["ingredient_changes"], "applied changes differ from decisions")
    history = restored["curation_history"].pop()
    require(history["action"] == "STRUCTURED_VARIANT_INGREDIENTS", "unexpected curation action")
    require(
        json.loads(history["changes"])["decision_sha256"]
        == hashlib.sha256(args.decisions.read_bytes()).hexdigest(),
        "history decision hash differs",
    )
    if "curation_history" not in before:
        require(not restored.pop("curation_history"), "unexpected previous history")
    require(restored == before, "base, prose or unrelated record content changed")
    occurrences = rows(args.bundle / "ingredient_occurrences.tsv")
    ledger = rows(args.bundle / "variant_ingredient_changes.tsv")
    changes = [
        (variant, index, change)
        for variant in decision["variants"]
        for index, change in enumerate(variant["ingredient_changes"])
    ]
    expected_ledger = sum(2 if change["action"] == "REPLACE" else 1 for _, _, change in changes)
    require(len(ledger) == expected_ledger, "unexpected number of change descriptors")
    positive = [row for row in occurrences if row["change_action"]]
    require(
        len(positive) == sum(change["action"] != "REMOVE" for _, _, change in changes),
        "unexpected variant occurrences",
    )
    for variant, index, change in changes:
        matching = [
            row
            for row in ledger
            if int(row["change_index"]) == index
            and int(row["variant_index"]) == variant["variant_index"]
        ]
        require(
            len(matching) == (2 if change["action"] == "REPLACE" else 1),
            "change coordinate missing or duplicated",
        )
        for row in matching:
            require(json.loads(row["change_json"]) == change, "change context lost")
            positive_role = change["action"] != "REMOVE" and row["descriptor_role"] == "ingredient"
            require(
                row["counts_as_presence"] == str(positive_role).lower(),
                "positive/negative accounting wrong",
            )
            require(row["change_stage"] == change["stage"], "stage lost")
            require(row["variant_name"] == variant["variant_name"], "variant lost")
    manifest = args.bundle / "manifest.json"
    require(len(rows(args.bundle / "ingredient_aggregation_errors.tsv")) == 0, "input errors")
    print(
        json.dumps(
            {
                "state": "VERIFIED_SUBSET_CANARY",
                "recipe_id": decision["recipe_id"],
                "base_and_original_prose_unchanged": True,
                "variant_occurrences": len(positive),
                "variant_change_mentions": len(ledger),
                "total_direct_occurrences": len(occurrences),
                "stages": [row["change_stage"] for row in ledger],
                "resolutions": [
                    {
                        "label": row["preferred_term"],
                        "resolved_identifier": row["resolved_identifier"],
                    }
                    for row in ledger
                ],
                "manifest_sha256": hashlib.sha256(manifest.read_bytes()).hexdigest(),
                "limitation": "One record only; does not verify the remaining catalog or consumer adoption.",
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
