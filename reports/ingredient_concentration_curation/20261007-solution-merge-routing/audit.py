"""Check root-class routing against every exact tracked normalized record."""

import argparse
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

import yaml

from culturemech.merge.fingerprint import StandaloneSolutionError
from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger
from culturemech.validation.write_validated import infer_target_class

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def check():
    tracked = (
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=ROOT)
        .decode()
        .split("\0")
    )
    paths = sorted(ROOT / p for p in tracked if p.endswith(".yaml"))
    assert paths == find_all_recipes(ROOT / "data/normalized_yaml")
    digest = hashlib.sha256()
    classes = Counter()
    solutions = set()
    snapshots = {}
    for path in paths:
        raw = path.read_bytes()
        snapshots[path] = hashlib.sha256(raw).hexdigest()
        digest.update(str(path.relative_to(ROOT)).encode() + b"\0" + raw + b"\0")
        record = yaml.load(raw, Loader=yaml.CSafeLoader)
        kind = infer_target_class(record)
        classes[kind] += 1
        if kind == "SolutionRecipe":
            solutions.add(path)
    matcher = RecipeMatcher()
    groups = matcher.group_recipes(paths)
    admitted = {p for members in groups.values() for p in members}
    assert not (admitted & solutions)
    assert matcher._last_skip_stats["excluded_solutions"] == len(solutions)
    stats = matcher._last_skip_stats
    assert len(paths) == sum(
        stats[key]
        for key in (
            "excluded_solutions",
            "skipped_no_fingerprint",
            "skipped_error",
            "successfully_fingerprinted",
        )
    )
    plan = json.loads((HERE.parent / "20261007-dsmz111-preparation/plan.json").read_text())
    targets = []
    retention = []
    for item in plan["records"]:
        path = ROOT / item["path"]
        assert snapshots[path] == item["after_sha256"]
        record = yaml.load(path.read_bytes(), Loader=yaml.CSafeLoader)
        if path in solutions:
            try:
                RecipeMerger().merge_group([path], fingerprint="bypass-test")
            except StandaloneSolutionError:
                pass
            else:
                raise AssertionError("Direct merger accepted a standalone solution")
            targets.append(
                {
                    "path": item["path"],
                    "status": "outside_medium_scope",
                    "unchanged_from_scientific_curation": True,
                }
            )
            continue
        matches = [(fp, members) for fp, members in groups.items() if path in members]
        assert len(matches) == 1
        fp, members = matches[0]
        merged = RecipeMerger().merge_group(members, fingerprint=fp)
        targets.append(
            {
                "path": item["path"],
                "fingerprint": fp,
                "status": "medium_group",
                "unchanged_from_scientific_curation": True,
            }
        )
        fields = {
            key: merged.get(key) == record.get(key)
            for key in (
                "ingredients",
                "solutions",
                "preparation_steps",
                "preparation_notes",
                "notes",
                "ph_value",
                "source_data",
            )
        }
        for key in ("evidence", "references", "curation_history"):
            fields[key] = all(entry in merged.get(key, []) for entry in record.get(key, []))
        retention.append(
            {"path": item["path"], "fields": fields, "all_retained": all(fields.values())}
        )
    assert all(
        hashlib.sha256(path.read_bytes()).hexdigest() == sha for path, sha in snapshots.items()
    )
    return {
        "routing_passed": True,
        "tracked_normalized_records": len(paths),
        "input_content_sha256": digest.hexdigest(),
        "record_classes": dict(classes),
        "routing": stats,
        "medium_groups": len(groups),
        "all_normalized_bytes_unchanged_during_audit": True,
        "curated_targets": targets,
        "medium_111_retention": retention,
        "medium_111_all_retained": all(row["all_retained"] for row in retention),
        "scope": "Routing success is not chemical identity or evidence-retention success. Standalone solutions remain authoritative normalized records; no new concentration claim is made.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    result = check()
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
