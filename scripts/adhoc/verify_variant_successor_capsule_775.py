#!/usr/bin/env python3
"""Verify retained successor evidence and its historical consumer without Git history.

Purpose: #775, 2026-11-16. Input: a checkout, optionally required to contain only
one commit and neither original branch commit. Output: JSON on stdout; no writes.
This tests provenance restoration, not new scientific approval or current recipes.
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
    sys.path.insert(0, str(root / "scripts"))
    import audit_variant_ingredient_successor as audit

    unavailable = []
    for revision in (audit.BASE, audit.RESULT):
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
        assert len(unavailable) == 2, "Original branch commits are unexpectedly available"
        count = subprocess.check_output(["git", "rev-list", "--count", "--all"], cwd=root)
        assert count.strip() == b"1", "Expected a single-commit repository"
    historical = root / (
        "reports/ingredient_concentration_curation/20261007-dsmz1399-stock-boundary/audit_diff.py"
    )
    spec = importlib.util.spec_from_file_location("capsule_historical_consumer", historical)
    consumer = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(consumer)
    plan = json.loads(audit.PLAN.read_bytes())
    events = 0
    for item in plan["records"]:
        before = yaml.load(item["before_text"], Loader=yaml.CSafeLoader)
        after = yaml.load(item["after_text"], Loader=yaml.CSafeLoader)
        counters = audit.check(before, after, item)
        events += counters["new_variant_ingredient_changes"]
        raw = item["after_text"].encode()
        assert audit.restore_before(raw, item["path"]) == item["before_text"].encode()
        assert consumer.invert_chain(raw, [item]) == before
    assert len(plan["records"]) == 87 and events == 377
    print(
        json.dumps(
            {
                "status": "PASS",
                "records": len(plan["records"]),
                "events": events,
                "historical_consumer": "invert_chain",
                "original_commits_unavailable": unavailable,
                "capsule_sha256": audit.CAPSULE_SHA256,
                "plan_sha256": audit.PLAN_SHA256,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
