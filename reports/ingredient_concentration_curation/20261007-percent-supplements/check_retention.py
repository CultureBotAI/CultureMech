"""Check the actual groups, including exclusive variant and source evidence retention."""

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
    "full_retention", HERE.parent / "20261007-komodo12-extraction/check_retention.py"
)
shared = importlib.util.module_from_spec(spec)
spec.loader.exec_module(shared)


def check():
    plan = json.loads((HERE / "plan.json").read_text())
    groups = RecipeMatcher().group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    results, merged_groups = [], {}
    for item in plan["records"]:
        target = ROOT / item["path"]
        raw = target.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        doc = yaml.load(raw, Loader=yaml.CSafeLoader)
        matches = [(fp, paths) for fp, paths in groups.items() if target in paths]
        assert len(matches) == 1
        fingerprint, paths = matches[0]
        if fingerprint not in merged_groups:
            merged_groups[fingerprint] = RecipeMerger().merge_group(paths, fingerprint=fingerprint)
        merged = merged_groups[fingerprint]
        fields = shared.retention(merged, doc)
        fields["variants"] = all(v in merged.get("variants", []) for v in doc.get("variants", []))
        fields["variant_children"] = all(
            v in merged.get("variant_children", []) for v in doc.get("variant_children", [])
        )
        # A source wrapper's parent link need not be copied to the canonical merge;
        # the selected methylamine branch must not lose its formulation distinction.
        if item["key"] == "m956":
            fields["methylamine_only"] = [
                n.get("preferred_term") for n in merged.get("ingredients", [])
            ] == ["Methylamine"] and not merged.get("variants")
        results.append(
            {
                "path": item["path"],
                "id": item["id"],
                "fingerprint": fingerprint,
                "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                "merged_id": merged["id"],
                "field_retention": fields,
                "all_checked_fields_retained": all(fields.values()),
            }
        )
    return {
        "records": results,
        "groups": len(merged_groups),
        "retained": sum(r["all_checked_fields_retained"] for r in results),
        "all_retained": all(r["all_checked_fields_retained"] for r in results),
        "scope": "Complete ingredient, stock, preparation, state, pH, root evidence and bibliography retention; source variant options and child links must survive in full. Checks the actual corpus groups, not a forced curated-only subset. No generated records are published.",
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
