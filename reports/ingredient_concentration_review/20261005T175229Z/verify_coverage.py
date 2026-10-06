import collections
import csv
import gzip
import hashlib
import json
import subprocess
from pathlib import Path

root = Path.cwd()
out = root / "reports/ingredient_concentration_review/20261005T175229Z"
source = (out / "inventory.jsonl").open() if (out / "inventory.jsonl").exists() else gzip.open(out / "inventory.jsonl.gz", "rt")
with source:
    inventory = [json.loads(line) for line in source]
tracked = {p for p in subprocess.check_output(["git", "ls-files", "-z", "--", "data/normalized_yaml", "data/merge_yaml/merged"], text=True).split("\0") if p.endswith(".yaml")}
manifest = list(csv.DictReader((out / "manifest.tsv").open(), delimiter="\t"))
assert len(manifest) == len(inventory) == len(tracked)
assert {r["record"] for r in manifest} == tracked
reports = list((out / "records").rglob("*.md"))
assert len(reports) == len(tracked)
targets = collections.Counter()
for row in manifest:
    path = out / row["report"]
    lines = [line for line in path.read_text().splitlines() if line.startswith("- Record:")]
    assert lines == ["- Record: " + row["record"]], (row["record"], lines)
    targets[row["record"]] += 1
assert all(count == 1 for count in targets.values())
changed = [r["path"] for r in inventory if hashlib.sha256((root / r["path"]).read_bytes()).hexdigest() != r["sha256"]]
assert not changed, changed
schema = json.loads((out / "validation_complete.json").read_text())
assert schema["files_scanned"] == len(tracked) and schema["exit_code"] == 0
assert list(csv.DictReader((out / "strict_validation.tsv").open(), delimiter="\t")) == []
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
    "tracked_records": len(tracked), "manifest_rows": len(manifest),
    "per_record_markdown_files": len(reports), "unique_exact_record_targets": len(targets),
    "duplicate_targets": 0, "missing_targets": 0, "stale_targets": 0,
    "reports_with_exactly_one_record_line": len(reports),
    "corpus_files_changed_since_inventory": changed,
    "closed_schema_validation": schema["status"],
    "kind_counts": dict(kind_counts),
    "flagged_record_counts": {layer: {flag: len(paths) for flag, paths in flags.items()} for layer, flags in flag_records.items()},
    "does_not_certify_scientific_correctness": True,
}
(out / "coverage_verification.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
