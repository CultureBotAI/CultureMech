"""Check complete formulation retention plus additive source provenance for this cohort."""

import argparse
import hashlib
import json
from pathlib import Path

import yaml

from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def retention(merged, source):
    result = {
        field: merged.get(field) == source.get(field)
        for field in (
            "ingredients",
            "solutions",
            "preparation_steps",
            "physical_state",
            "ph_range",
            "ph_value",
        )
    }
    # Extra citations are allowed; every original entry must survive unmodified.
    for field in ("evidence", "references"):
        actual = merged.get(field, [])
        result[field] = len({e["reference"] for e in actual}) == len(actual) and all(
            entry in actual for entry in source.get(field, [])
        )
    return result


def check():
    items = (
        json.loads((HERE / "plan.json").read_text())["records"]
        + json.loads((HERE.parent / "20261007-extraction-boundaries/plan.json").read_text())[
            "records"
        ]
    )
    groups = RecipeMatcher().group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    records = []
    for item in items:
        target = ROOT / item["path"]
        raw = target.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        doc = yaml.load(raw, Loader=yaml.CSafeLoader)
        matches = [(fp, paths) for fp, paths in groups.items() if target in paths]
        assert len(matches) == 1
        fp, paths = matches[0]
        merged = RecipeMerger().merge_group(paths, fingerprint=fp)
        fields = retention(merged, doc)
        records.append(
            {
                "path": item["path"],
                "id": item["id"],
                "fingerprint": fp,
                "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                "merged_id": merged["id"],
                "field_retention": fields,
                "all_checked_fields_retained": all(fields.values()),
            }
        )
    return {
        "definition": "Exact equality for complete ingredients/stocks/preparation/physical-state/pH structures, including ingredient evidence. Root evidence and bibliography may add unique-reference entries but must retain every source entry completely unchanged. This is not formulation-aware merging for other groups.",
        "records": records,
        "retained": sum(r["all_checked_fields_retained"] for r in records),
        "all_retained": all(r["all_checked_fields_retained"] for r in records),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists(), args.out
    result = check()
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), flush=True)
    raise SystemExit(0 if result["all_retained"] else 1)
