#!/usr/bin/env python3
"""Verify exact completeness and prior successor layers from retained evidence.

Purpose: #683, 2026-11-16. Input: a checkout, optionally with only one commit and
no original feature commits. Output: JSON evidence on stdout; no writes.
Checks current recipe bytes and both historical inversion paths without Git
object reads for scientific/proposal evidence or any external lookup.
"""

from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import yaml


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--checkout", type=Path, default=Path(__file__).resolve().parents[2])
    parser.add_argument("--require-single-commit", action="store_true")
    args = parser.parse_args()
    root = args.checkout.resolve()
    sys.path[:0] = [str(root / "scripts"), str(root / "src")]
    import audit_variant_completeness_successor as audit
    import audit_variant_ingredient_successor as earlier
    import curate_variant_completeness as updater

    import culturemech.validation.write_validated as validation

    for module in (audit, earlier, updater, validation):
        assert (
            Path(module.__file__).resolve().is_relative_to(root)
        ), "Imported outside proof checkout"
    unavailable = []
    for revision in (earlier.BASE, earlier.RESULT, audit.BASE):
        result = subprocess.run(
            ["git", "cat-file", "-e", revision + "^{commit}"],
            cwd=root,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=False,
        )
        if result.returncode:
            unavailable.append(revision)
    if args.require_single_commit:
        assert len(unavailable) == 3, "Original branch history is unexpectedly available"
        assert (
            subprocess.check_output(["git", "rev-list", "--count", "--all"], cwd=root).strip()
            == b"1"
        )
    historical = root / (
        "reports/ingredient_concentration_curation/20261007-dsmz1399-stock-boundary/audit_diff.py"
    )
    spec = importlib.util.spec_from_file_location("completeness_historical_consumer", historical)
    consumer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(consumer)
    layered = 0
    plan = json.loads(audit.PLAN.read_bytes())
    for item in plan["records"]:
        raw = (root / item["path"]).read_bytes()
        assert (
            audit.sha(raw) == item["after_sha256"]
        ), "Current recipe differs from retained afterimage"
        before = yaml.load(item["before_text"], Loader=yaml.CSafeLoader)
        after = yaml.load(raw, Loader=yaml.CSafeLoader)
        assert audit.check(before, after, item)["new_curation_history"] == 1
        assert audit.restore_before(raw, item["path"]) == item["before_text"].encode()
        chain = [item]
        if item["path"] in earlier.proposal_records():
            old = earlier.expected_item(item["path"])
            assert (
                item["before_sha256"] == old["after_sha256"]
            ), "Historical layers are disconnected"
            expected = old["before_text"].encode()
            chain.append(old)
            layered += 1
        else:
            expected = item["before_text"].encode()
        assert earlier.restore_before(raw, item["path"]) == expected
        assert consumer.invert_chain(raw, chain) == yaml.load(expected, Loader=yaml.CSafeLoader)
    print(
        json.dumps(
            {
                "status": "PASS",
                "records": len(plan["records"]),
                "two_layer_records": layered,
                "historical_consumer": "invert_chain",
                "original_commits_unavailable": unavailable,
                "plan_sha256": audit.PLAN_SHA256,
                "capsule_sha256": audit.CAPSULE_SHA256,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
