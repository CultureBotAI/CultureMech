#!/usr/bin/env python3
"""Independently compare the reviewed #683 merge projection (2026-11-16).

Inputs: three exact frozen scientific proposal pins and combined plan pin.
Output: new ignored JSON receipt of operation/disposition/preimage equality.
Reads base Git blobs; never applies recipes or imports the production composer.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

BASE = "65df76935898c6e973697389b76449686b88f8cb"
ROOT = Path(__file__).resolve().parents[2]
DIRECTORY = ROOT / "conf/variant_ingredient_curation"
INPUTS = {
    "completeness-evidence-683.json": "85f718233396d14a3bac3165694a76db4bc1bb9a1ac35923a78b1ac65b600d4b",
    "completeness-model-683.json": "548408377e4a75f000f779560647661533107b78199283df371ccda1680fde28",
    "completeness-conditions-683.json": "888fbb82de4b8148a10b46a8c07f80a8460f0ccbaa571586d52f2d1d6a7a3a24",
}
COMBINED = "db59754b282f7aa86b5fc8f54fc0b2885794c2816e7dab5d37df507b39aab554"
VARIANT_OPS = {"append_changes", "append_mentions", "replace_changes", "replace_modifications"}


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def read(name, pin):
    raw = (DIRECTORY / name).read_bytes()
    if sha(raw) != pin:
        raise ValueError("Frozen input drift: " + name)
    return json.loads(raw)


def project(document):
    operations, identities, dispositions, variant_identities = Counter(), {}, {}, {}
    mutation_paths = set()
    for record in document["records"]:
        path = record["path"]
        if path in identities:
            raise ValueError("Duplicate record")
        identities[path] = (record["recipe_id"], record["expected_sha256"])
        if set(record) - {"path", "recipe_id", "expected_sha256", "variants", "field_replacements"}:
            raise ValueError("Unknown record operation")
        for field in record.get("field_replacements", []):
            operations[(path, "record", "field_replacements", canonical(field))] += 1
            mutation_paths.add(path)
        for variant in record["variants"]:
            vi = variant["variant_index"]
            key = path, vi
            if key in variant_identities:
                raise ValueError("Duplicate variant coordinate")
            variant_identities[key] = variant["variant_name"]
            if set(variant) - VARIANT_OPS - {"variant_index", "variant_name"}:
                raise ValueError("Unknown variant operation")
            for operation in VARIANT_OPS:
                for payload in variant.get(operation, []):
                    operations[(path, str(vi), operation, canonical(payload))] += 1
                    mutation_paths.add(path)
    for row in document["dispositions"]:
        number = row["queue_row_number"]
        if number in dispositions:
            raise ValueError("Duplicate row disposition")
        dispositions[number] = canonical(row)
    return operations, identities, dispositions, variant_identities, mutation_paths


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    expected_ops, expected_ids, expected_dispositions, expected_variants = Counter(), {}, {}, {}
    expected_paths = set()
    for name, pin in INPUTS.items():
        document = read(name, pin)
        if document["base_commit"] != BASE:
            raise ValueError("Wrong source base")
        operations, identities, dispositions, variants, paths = project(document)
        expected_ops.update(operations)
        for key, value in identities.items():
            if key in expected_ids and expected_ids[key] != value:
                raise ValueError("Conflicting source record identity")
            expected_ids[key] = value
        for key, value in variants.items():
            if key in expected_variants and expected_variants[key] != value:
                raise ValueError("Conflicting source variant identity")
            expected_variants[key] = value
        if expected_dispositions.keys() & dispositions.keys():
            raise ValueError("Overlapping source dispositions")
        expected_dispositions.update(dispositions)
        expected_paths.update(paths)
    combined = read("completeness-683.json", COMBINED)
    operations, identities, dispositions, variants, paths = project(combined)
    if operations != expected_ops or dispositions != expected_dispositions:
        raise ValueError("Merged scientific operation or disposition differs")
    if set(identities) != expected_paths or paths != expected_paths:
        raise ValueError("Merged mutation membership differs")
    if any(value != expected_ids[key] for key, value in identities.items()):
        raise ValueError("Merged record identity differs")
    if any(value != expected_variants[key] for key, value in variants.items()):
        raise ValueError("Merged variant identity differs")
    pins = {Path(row["path"]).name: row["sha256"] for row in combined["reviewed_inputs"]}
    if pins != INPUTS or len(combined["reviewed_inputs"]) != len(INPUTS):
        raise ValueError("Reviewed-input pin list differs")
    for path, (_, pin) in identities.items():
        raw = subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)
        if sha(raw) != pin:
            raise ValueError("Combined preimage differs from base Git blob")
    for name, pin in {**INPUTS, "completeness-683.json": COMBINED}.items():
        read(name, pin)
    receipt = {
        "result": "PASS",
        "base_commit": BASE,
        "reviewed_proposal_pins": INPUTS,
        "combined_sha256": COMBINED,
        "mutation_records": len(identities),
        "reviewed_dispositions": len(dispositions),
        "operations_by_kind": dict(
            Counter(
                {
                    kind: sum(count for key, count in operations.items() if key[2] == kind)
                    for kind in sorted({key[2] for key in operations})
                }
            )
        ),
        "exact_operation_payloads_preserved": True,
        "exact_dispositions_preserved": True,
        "all_mutation_preimages_match_base": True,
        "limitations": "Projection equality only; scientific claims were reviewed separately. No recipe apply or full native validation performed by this helper.",
    }
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(receipt, stream, indent=2)
        stream.write("\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
