"""Check DSMZ 2's real merge group; never write generated recipe files."""

import argparse
import hashlib
import json
from pathlib import Path

import yaml

from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger

ROOT = Path(__file__).resolve().parents[3]


def check():
    item = json.loads(Path(__file__).with_name("plan.json").read_text())["records"][0]
    target = ROOT / item["path"]
    raw = target.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
    doc = yaml.load(raw, Loader=yaml.CSafeLoader)
    matcher = RecipeMatcher()
    groups = matcher.group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    matches = [(fp, paths) for fp, paths in groups.items() if target in paths]
    assert len(matches) == 1
    fp, paths = matches[0]
    merged = RecipeMerger().merge_group(paths, fingerprint=fp)
    checks = {
        k: merged.get(k) == doc.get(k)
        for k in ("ingredients", "solutions", "preparation_steps", "evidence", "references")
    }
    return {
        "path": item["path"],
        "id": item["id"],
        "fingerprint": fp,
        "group_paths": [str(p.relative_to(ROOT)) for p in paths],
        "merged_id": merged["id"],
        "field_retention": checks,
        "all_checked_fields_retained": all(checks.values()),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    if args.out.exists():
        raise ValueError("Do not overwrite an audit snapshot")
    result = check()
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))
    raise SystemExit(0 if result["all_checked_fields_retained"] else 1)
