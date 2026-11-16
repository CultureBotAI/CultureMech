#!/usr/bin/env python3
"""Retain squash-safe successor evidence authenticated by original Git objects.

Purpose: #775, 2026-11-16. Inputs: the unchanged #772 plan and fixed original
Git recipe/proposal snapshots. Outputs: a digest-pinned capsule, only with
--write; otherwise report the verified prospective files without mutation.
Existing files are never overwritten. No recipe or historical receipt changes.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from adhoc.audit_variant_coverage_683 import check_preservation  # noqa: E402
from audit_variant_ingredient_successor import (  # noqa: E402
    ACTION,
    BASE,
    CAPSULE,
    PLAN,
    PLAN_SHA256,
    PROPOSALS,
    RESULT,
    ROOT,
    sha,
)


def original(revision, path):
    return subprocess.check_output(["git", "show", f"{revision}:{path}"], cwd=ROOT)


def collect():
    plan_raw = PLAN.read_bytes()
    assert sha(plan_raw) == PLAN_SHA256, "Existing reviewed plan changed"
    plan = json.loads(plan_raw)
    assert plan["base_commit"] == BASE and plan["applied_commit"] == RESULT
    proposal_records = {}
    files = {}
    descriptions = {}
    for path in PROPOSALS:
        raw = original(RESULT, path)
        name = "proposals/" + Path(path).name
        assert name not in files
        files[name] = raw
        descriptions[path] = {"path": name, "sha256": sha(raw), "bytes": len(raw)}
        for record in json.loads(raw)["records"]:
            assert record["path"] not in proposal_records, "Duplicate reviewed proposal path"
            proposal_records[record["path"]] = (path, sha(raw), record)
    assert len(plan["records"]) == len(proposal_records) == 87
    assert {item["path"] for item in plan["records"]} == set(proposal_records)
    events = 0
    for item in plan["records"]:
        path = item["path"]
        proposal_path, proposal_sha, proposal = proposal_records[path]
        expected = {
            "path": path,
            "id": proposal["recipe_id"],
            "action": ACTION,
            "proposal_path": proposal_path,
            "proposal_sha256": proposal_sha,
        }
        for label, revision in (("before", BASE), ("after", RESULT)):
            raw = original(revision, path)
            expected[label + "_text"] = raw.decode("utf-8")
            expected[label + "_sha256"] = sha(raw)
        assert item == expected, "Plan differs from original Git evidence"
        before, after = (
            yaml.load(item[label + "_text"], Loader=yaml.CSafeLoader)
            for label in ("before", "after")
        )
        check_preservation(before, after, proposal, proposal_sha, "postapply")
        events += sum(len(variant["ingredient_changes"]) for variant in proposal["variants"])
    assert events == 377
    manifest = {
        "contract": "culturemech-variant-successor-capsule-v1",
        "issue": "https://github.com/CultureBotAI/CultureMech/issues/775",
        "base_commit": BASE,
        "applied_commit": RESULT,
        "plan": {
            "path": str(PLAN.relative_to(ROOT)),
            "sha256": sha(plan_raw),
            "bytes": len(plan_raw),
        },
        "proposals": descriptions,
        "record_paths": sorted(proposal_records),
        "records": 87,
        "events": events,
    }
    files["manifest.json"] = (json.dumps(manifest, sort_keys=True, indent=2) + "\n").encode()
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--write", action="store_true", help="Create the new evidence capsule")
    args = parser.parse_args()
    files = collect()
    if args.write:
        CAPSULE.mkdir(exist_ok=False)
        # The manifest is last; incomplete generation does not receive acceptance.
        for name in sorted(files, key=lambda value: (value == "manifest.json", value)):
            path = CAPSULE / name
            path.parent.mkdir(exist_ok=True)
            with path.open("xb") as stream:
                stream.write(files[name])
            assert path.read_bytes() == files[name]
    elif CAPSULE.exists():
        assert {
            str(path.relative_to(CAPSULE)) for path in CAPSULE.rglob("*") if path.is_file()
        } == set(files), "Capsule membership differs"
        for name, raw in files.items():
            assert (CAPSULE / name).read_bytes() == raw, "Retained capsule differs from Git"
    print(
        json.dumps(
            {
                "status": "WRITTEN" if args.write else "VERIFIED_FROM_ORIGINAL_GIT",
                "capsule": str(CAPSULE.relative_to(ROOT)),
                "manifest_sha256": sha(files["manifest.json"]),
                "plan_sha256": PLAN_SHA256,
                "records": 87,
                "events": 377,
                "files": len(files),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
