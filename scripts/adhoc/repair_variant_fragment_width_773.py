#!/usr/bin/env python3
"""Repair only added variant YAML presentation for #773, 2026-11-16.

Inputs: exact base02e and f9 Git bytes, reviewed proposal files and current YAML.
Outputs: preview or explicit apply receipt. Reconstructs additions with the
maintained renderer, preserving all parsed values/history timestamps and old
source lines. No new scientific claims, native writer changes or external calls.
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import curate_variant_ingredients as curate  # noqa: E402
from audit_variant_coverage_683 import check_preservation  # noqa: E402
from record_io import dump_record  # noqa: E402

BASE = "02e005db42246b8a04ece9df4b5657e036fa5697"
SOURCE = "f9dee2d216018b7495ddb1205d211e52506a8346"


def git_bytes(root, commit, relative):
    return subprocess.check_output(["git", "show", commit + ":" + relative], cwd=root)


def plan(root, decision, proposal_sha):
    relative = decision["path"]
    path = curate.recipe_path(root, relative)
    original = git_bytes(root, BASE, relative)
    source = git_bytes(root, SOURCE, relative)
    before = path.read_bytes()
    if curate.digest(original) != decision["expected_sha256"]:
        raise ValueError("proposal/base preimage mismatch: " + relative)
    desired = yaml.safe_load(source)
    if desired["id"] != decision["recipe_id"]:
        raise ValueError("record identity mismatch: " + relative)
    original_record = yaml.safe_load(original)
    check_preservation(original_record, desired, decision, proposal_sha, "postapply")
    errors = curate.validate_recipe(desired)
    if errors:
        raise ValueError("existing source fails native validation: " + errors[0].message)
    rendered = curate.render_additions(original, desired, decision["variants"])
    if yaml.safe_load(rendered) != desired:
        raise ValueError("presentation repair would change parsed content")
    native_base_canonical = dump_record(original_record).encode("utf-8") == original
    native_desired = dump_record(desired).encode("utf-8")
    f9_canonical = native_desired == source
    repaired_canonical = native_desired == rendered
    if native_base_canonical and not repaired_canonical:
        raise ValueError("presentation repair would lose native canonicality: " + relative)
    # A real retry is safe only when already exactly equal to this reconstruction.
    if before not in (source, rendered):
        raise ValueError(
            "current bytes differ from pinned f9 or exact repaired result: " + relative
        )
    status = "UNCHANGED" if before == rendered else "PLANNED"
    return {
        "path": path,
        "before": before,
        "rendered": rendered,
        "record": desired,
        "receipt": {
            "path": relative,
            "recipe_id": decision["recipe_id"],
            "status": status,
            "before_sha256": curate.digest(before),
            "f9_sha256": curate.digest(source),
            "base_sha256": curate.digest(original),
            "planned_after_sha256": curate.digest(rendered),
            "proposal_sha256": proposal_sha,
            "parsed_content_unchanged": True,
            "native_base_canonical": native_base_canonical,
            "f9_canonical": f9_canonical,
            "repaired_canonical": repaired_canonical,
        },
    }


def run(proposals, receipt, *, root=ROOT, apply=False, only_record=None):
    if receipt.resolve().is_relative_to((root / "data/normalized_yaml").resolve()):
        raise ValueError("receipt must be outside authoritative input tree")
    inputs, decisions = [], []
    for proposal in proposals:
        raw = proposal.read_bytes()
        document = json.loads(raw)
        if document["schema_version"] != 1:
            raise ValueError("unsupported proposal")
        digest = curate.digest(raw)
        inputs.append({"path": str(proposal), "sha256": digest})
        decisions.extend((item, digest) for item in document["records"])
    paths = [item["path"] for item, _digest in decisions]
    if len(paths) != len(set(paths)):
        raise ValueError("overlapping proposal recipes")
    if only_record is not None and only_record not in paths:
        raise ValueError("selected record absent from proposals")
    plans = [
        plan(root, item, digest)
        for item, digest in decisions
        if only_record is None or item["path"] == only_record
    ]
    if not plans:
        raise ValueError("no selected records")
    result = {
        "mode": "apply" if apply else "preview",
        "state": "PREPARED",
        "base_commit": BASE,
        "source_commit": SOURCE,
        "only_record": only_record,
        "proposals": inputs,
        "implementation_sha256": {
            "repair_helper": curate.digest(Path(__file__).read_bytes()),
            "maintained_renderer": curate.digest(Path(curate.__file__).read_bytes()),
        },
        "records": [item["receipt"] for item in plans],
        "scope": "Presentation of authorized additions only; no parsed values or history timestamps changed.",
    }
    receipt.parent.mkdir(parents=True, exist_ok=True)
    with receipt.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
        stream.flush()
        os.fsync(stream.fileno())
    if not apply:
        return result
    try:
        for item in plans:
            row = item["receipt"]
            if row["status"] == "UNCHANGED":
                continue
            fd, name = tempfile.mkstemp(
                prefix=".variant-width-", suffix=".tmp", dir=item["path"].parent
            )
            os.close(fd)
            stage = Path(name)
            try:
                curate.write_validated_recipe(item["record"], stage)
                if yaml.safe_load(stage.read_bytes()) != item["record"]:
                    raise ValueError("native stage differs from pinned parsed source")
                stage.write_bytes(item["rendered"])
                if (
                    stage.read_bytes() != item["rendered"]
                    or yaml.safe_load(stage.read_bytes()) != item["record"]
                ):
                    raise ValueError("presentation stage differs from reviewed reconstruction")
                stage.chmod(item["path"].stat().st_mode & 0o777)
                with stage.open("rb") as stream:
                    os.fsync(stream.fileno())
                row["status"] = "APPLYING"
                curate.persist_receipt(receipt, result)
                if item["path"].read_bytes() != item["before"]:
                    raise ValueError("record changed after preview: " + row["path"])
                os.replace(stage, item["path"])
                row["status"] = "APPLIED"
                row["after_sha256"] = curate.digest(item["path"].read_bytes())
                if row["after_sha256"] != row["planned_after_sha256"]:
                    raise ValueError("published bytes differ from reconstruction")
                curate.persist_receipt(receipt, result)
            finally:
                stage.unlink(missing_ok=True)
        result["state"] = "COMPLETE"
        curate.persist_receipt(receipt, result)
    except Exception as exc:
        result["state"] = "INCOMPLETE"
        result["error"] = str(exc)
        for item in plans:
            try:
                item["receipt"]["observed_sha256"] = curate.digest(item["path"].read_bytes())
            except OSError as error:
                item["receipt"]["observation_error"] = str(error)
        try:
            curate.persist_receipt(receipt, result)
        except OSError as error:
            result["receipt_write_error"] = str(error)
        raise curate.ApplyError(str(exc), result) from exc
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--proposal", type=Path, action="append", required=True)
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--only-record")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        result = run(args.proposal, args.receipt, apply=args.apply, only_record=args.only_record)
    except curate.ApplyError as error:
        print(json.dumps(error.receipt, indent=2), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
