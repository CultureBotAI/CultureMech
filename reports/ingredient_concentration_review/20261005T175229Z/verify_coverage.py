"""Verify one audit snapshot against exact tracked paths and current record bytes."""

import argparse
import collections
import csv
import hashlib
import json
import subprocess
from pathlib import Path

from review_driver import read_inventory, validation_state


def require(condition, message):
    if not condition:
        raise ValueError(message)


def verify(out, root, tracked=None):
    inventory = read_inventory(out)
    if tracked is None:
        tracked = {
            p
            for p in subprocess.check_output(
                ["git", "ls-files", "-z", "--", "data/normalized_yaml", "data/merge_yaml/merged"],
                text=True,
                cwd=root,
            ).split("\0")
            if p.endswith(".yaml")
        }
    with (out / "manifest.tsv").open() as handle:
        manifest = list(csv.DictReader(handle, delimiter="\t"))
    require(len(manifest) == len(inventory) == len(tracked), "Record counts differ")
    require({r["path"] for r in inventory} == tracked, "Inventory paths differ from tracked corpus")
    require({r["record"] for r in manifest} == tracked, "Manifest paths differ from tracked corpus")
    reports = set((out / "records").rglob("*.md"))
    expected_reports = set()
    targets = collections.Counter()
    by_path = {r["path"]: r for r in inventory}
    for row in manifest:
        expected = Path("records") / Path(row["record"]).relative_to("data").with_suffix(".md")
        require(row["report"] == str(expected), "Noncanonical report path: " + row["report"])
        path = out / expected
        expected_reports.add(path)
        lines = [line for line in path.read_text().splitlines() if line.startswith("- Record:")]
        require(lines == ["- Record: " + row["record"]], "Invalid Record line: " + str(path))
        require(row["sha256"] == by_path[row["record"]]["sha256"], "Manifest hash mismatch")
        targets[row["record"]] += 1
    require(reports == expected_reports, "Missing or extra report files")
    require(all(count == 1 for count in targets.values()), "Duplicate report targets")
    changed = [
        r["path"]
        for r in inventory
        if hashlib.sha256((root / r["path"]).read_bytes()).hexdigest() != r["sha256"]
    ]
    require(not changed, "Corpus changed since inventory: " + str(changed))
    finalized, _ = validation_state(out, inventory)
    require(finalized, "Schema validation is not finalized")
    kind_counts = collections.defaultdict(collections.Counter)
    flag_records = collections.defaultdict(lambda: collections.defaultdict(set))
    for r in inventory:
        kind_counts[r["layer"]][r["record_kind"]] += 1
        for c in r["claims"]:
            for flag in c["flags"]:
                flag_records[r["layer"]][flag].add(r["path"])
            if any(f.startswith("PLAUSIBILITY_") for f in c["flags"]):
                flag_records[r["layer"]]["ANY_PLAUSIBILITY_FLAG"].add(r["path"])
    result = {
        "tracked_records": len(tracked),
        "manifest_rows": len(manifest),
        "per_record_markdown_files": len(reports),
        "unique_exact_record_targets": len(targets),
        "duplicate_targets": 0,
        "missing_targets": 0,
        "stale_targets": 0,
        "reports_with_exactly_one_record_line": len(reports),
        "corpus_files_changed_since_inventory": changed,
        "closed_schema_validation": "passed",
        "kind_counts": dict(kind_counts),
        "flagged_record_counts": {
            layer: {flag: len(paths) for flag, paths in flags.items()}
            for layer, flags in flag_records.items()
        },
        "does_not_certify_scientific_correctness": True,
    }
    (out / "coverage_verification.json").write_text(json.dumps(result, indent=2) + "\n")
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, nargs="?", default=Path(__file__).resolve().parent)
    args = parser.parse_args()
    print(json.dumps(verify(args.output, Path.cwd()), indent=2))
