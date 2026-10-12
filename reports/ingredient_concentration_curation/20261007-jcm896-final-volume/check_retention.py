"""Exercise JCM 896's actual merge group without publishing generated records."""

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

import yaml

from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    "complete_recipe_retention",
    HERE.parent / "20261007-komodo12-extraction/check_retention.py",
)
shared = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shared)


def check():
    item = json.loads((HERE / "plan.json").read_text())["records"][0]
    target = ROOT / item["path"]
    raw = target.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
    doc = yaml.load(raw, Loader=yaml.CSafeLoader)
    groups = RecipeMatcher().group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    matches = [(fp, paths) for fp, paths in groups.items() if target in paths]
    assert len(matches) == 1
    fingerprint, paths = matches[0]
    merged = RecipeMerger().merge_group(paths, fingerprint=fingerprint)
    fields = shared.retention(merged, doc)
    return {
        "path": item["path"],
        "id": item["id"],
        "fingerprint": fingerprint,
        "group_paths": [str(p.relative_to(ROOT)) for p in paths],
        "merged_id": merged["id"],
        "field_retention": fields,
        "all_checked_fields_retained": all(fields.values()),
        "scope": "Complete ingredient/evidence, stock, preparation, physical-state and pH equality; "
        "all original root evidence and bibliography retained, allowing additional unique sources. "
        "This one group's result does not resolve the global merger defects.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists(), args.out
    result = check()
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), flush=True)
    raise SystemExit(0 if result["all_checked_fields_retained"] else 1)
