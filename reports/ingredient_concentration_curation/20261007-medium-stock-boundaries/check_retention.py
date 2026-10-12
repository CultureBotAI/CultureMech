"""Inspect the repaired records in their actual maintained merge groups, without writes."""

import argparse
import hashlib
import json
from pathlib import Path

import yaml

from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger

ROOT = Path(__file__).resolve().parents[3]


def check(plan_path=None):
    plan_path = plan_path or Path(__file__).with_name("plan.json")
    plan = json.loads(plan_path.read_text())
    groups = RecipeMatcher().group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    results = []
    for item in plan["records"]:
        target = ROOT / item["path"]
        raw = target.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        doc = yaml.load(raw, Loader=yaml.CSafeLoader)
        matches = [(fp, paths) for fp, paths in groups.items() if target in paths]
        assert len(matches) == 1
        fp, paths = matches[0]
        merged = RecipeMerger().merge_group(paths, fingerprint=fp)
        fields = {
            k: merged.get(k) == doc.get(k)
            for k in (
                "ingredients",
                "solutions",
                "preparation_steps",
                "evidence",
                "references",
                "ph_value",
            )
        }
        results.append(
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
        "records": results,
        "retained": sum(r["all_checked_fields_retained"] for r in results),
        "all_retained": all(r["all_checked_fields_retained"] for r in results),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--plan", type=Path)
    args = parser.parse_args()
    if args.out.exists():
        raise ValueError("Do not overwrite an audit snapshot")
    result = check(args.plan)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
    raise SystemExit(0 if result["all_retained"] else 1)
