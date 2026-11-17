#!/usr/bin/env python3
"""Retain reviewed completeness edges without branch-history runtime dependencies.

Purpose: #683, 2026-11-16. Inputs: final combined apply receipt and decisions,
their independently supplied SHA256s, fixed Git baseline and current recipes.
Outputs: exact plan and capsule only with --write; otherwise verified preview.
No recipe changes, overwrite, network access or private receipt paths in output.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from audit_variant_completeness_successor import (  # noqa: E402
    ACTION,
    BASE,
    CAPSULE,
    PLAN,
    ROOT,
    check_semantics,
    sha,
)
from curate_variant_ingredients import recipe_path  # noqa: E402

from culturemech.validation.write_validated import validate_recipe  # noqa: E402


def pinned(path, expected):
    assert re.fullmatch(r"[0-9a-f]{64}", expected), "Expected a full lowercase SHA256"
    assert path.is_file() and not path.is_symlink(), "Evidence must be a regular file"
    raw = path.read_bytes()
    assert sha(raw) == expected, "Evidence differs from externally supplied pin"
    return raw


def collect(decision_path, decision_pin, receipt_path, receipt_pin):
    decision_raw, receipt_raw = pinned(decision_path, decision_pin), pinned(
        receipt_path, receipt_pin
    )
    document, receipt = json.loads(decision_raw), json.loads(receipt_raw)
    assert document["schema_version"] == 1 and document["records"]
    assert receipt["schema_version"] == 1 and receipt["mode"] == "apply"
    assert receipt["state"] == "COMPLETE" and receipt["decision_sha256"] == decision_pin
    decisions = {item["path"]: item for item in document["records"]}
    rows = {item["path"]: item for item in receipt["records"]}
    assert len(decisions) == len(document["records"]) == len(rows) == len(receipt["records"])
    assert set(decisions) == set(rows), "Final receipt must cover every mutation decision"
    items = []
    for path in sorted(decisions):
        decision, row = decisions[path], rows[path]
        current = recipe_path(ROOT, path)
        assert row["recipe_id"] == decision["recipe_id"]
        assert row["status"] in {"APPLIED", "UNCHANGED"}
        original = subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)
        before_raw, after_raw = (
            row[label + "_text"].encode("utf-8") for label in ("before", "after")
        )
        assert original == before_raw, "Beforeimage differs from fixed Git baseline"
        assert current.read_bytes() == after_raw, "Current recipe differs from completed receipt"
        assert sha(before_raw) == row["before_sha256"] == decision["expected_sha256"]
        assert sha(after_raw) == row["after_sha256"] == row["planned_after_sha256"]
        assert before_raw != after_raw, "No-op records must stay out of the mutation capsule"
        before, after = (yaml.load(raw, Loader=yaml.CSafeLoader) for raw in (before_raw, after_raw))
        assert not validate_recipe(after), "Applied record fails native validation"
        check_semantics(before, after, decision, decision_pin)
        items.append(
            {
                "path": path,
                "id": decision["recipe_id"],
                "action": ACTION,
                "decision_sha256": decision_pin,
                "source_receipt_sha256": receipt_pin,
                "before_text": before_raw.decode("utf-8"),
                "before_sha256": sha(before_raw),
                "after_text": after_raw.decode("utf-8"),
                "after_sha256": sha(after_raw),
            }
        )
    plan = {
        "base_commit": BASE,
        "decision_sha256": decision_pin,
        "source_receipt_sha256": receipt_pin,
        "scope": "Exact reviewed completeness changes; every earlier audit remains required",
        "records": items,
    }
    plan_raw = (json.dumps(plan, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    manifest = {
        "contract": "culturemech-variant-completeness-successors-v1",
        "base_commit": BASE,
        "source_receipt_sha256": receipt_pin,
        "plan": {
            "path": PLAN.relative_to(ROOT).as_posix(),
            "sha256": sha(plan_raw),
            "bytes": len(plan_raw),
        },
        "decisions": {"path": "decisions.json", "sha256": decision_pin, "bytes": len(decision_raw)},
        "records": len(items),
        "record_paths": sorted(decisions),
    }
    manifest_raw = (json.dumps(manifest, sort_keys=True, indent=2) + "\n").encode("utf-8")
    return {
        PLAN: plan_raw,
        CAPSULE / "decisions.json": decision_raw,
        CAPSULE / "manifest.json": manifest_raw,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decisions", type=Path, required=True)
    parser.add_argument("--expected-decision-sha256", required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--expected-receipt-sha256", required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()
    files = collect(
        args.decisions, args.expected_decision_sha256, args.receipt, args.expected_receipt_sha256
    )
    if args.write:
        assert not any(
            path.exists() or path.is_symlink() for path in files
        ), "Evidence already exists"
        PLAN.parent.mkdir(parents=True, exist_ok=True)
        CAPSULE.mkdir(exist_ok=False)
        for path, raw in files.items():
            with path.open("xb") as stream:
                stream.write(raw)
            assert path.read_bytes() == raw
    elif any(path.exists() for path in files):
        assert all(
            path.is_file() and path.read_bytes() == raw for path, raw in files.items()
        ), "Retained evidence differs"
    print(
        json.dumps(
            {
                "status": "WRITTEN" if args.write else "VERIFIED_PREVIEW",
                "records": len(json.loads(files[PLAN])["records"]),
                "plan_sha256": sha(files[PLAN]),
                "capsule_sha256": sha(files[CAPSULE / "manifest.json"]),
                "decision_sha256": args.expected_decision_sha256,
                "source_receipt_sha256": args.expected_receipt_sha256,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
