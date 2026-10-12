"""Check actual medium groups without confusing shared quotes with full provenance."""

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


def snippets(node, path=()):
    result = set()
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "evidence":
                result.update((path, e["reference"], e["snippet"]) for e in value)
            else:
                result.update(snippets(value, path + (key,)))
    elif isinstance(node, list):
        for i, value in enumerate(node):
            result.update(snippets(value, path + (i,)))
    return result


def check(folder=HERE):
    plan = json.loads((folder / "plan.json").read_text())
    matcher = RecipeMatcher()
    groups = matcher.group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    rows = []
    for item in plan["records"]:
        target = ROOT / item["path"]
        raw = target.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        source = yaml.load(raw, Loader=yaml.CSafeLoader)
        matches = [(fp, members) for fp, members in groups.items() if target in members]
        if item.get("target_class") == "SolutionRecipe" or item["key"] == "solution":
            assert not matches
            rows.append(
                {
                    "path": item["path"],
                    "status": "outside_medium_scope",
                    "authoritative_record_unchanged": True,
                }
            )
            continue
        assert len(matches) == 1
        fp, members = matches[0]
        merged = RecipeMerger().merge_group(members, fingerprint=fp)
        fields = {
            key: source.get(key) == merged.get(key)
            for key in (
                "ingredients",
                "solutions",
                "variants",
                "preparation_steps",
                "notes",
                "ph_value",
            )
        }
        for key in ("evidence", "references", "curation_history"):
            fields[key] = all(entry in merged.get(key, []) for entry in source.get(key, []))
        original_snippets = snippets(source)
        retained = original_snippets & snippets(merged)
        rows.append(
            {
                "path": item["path"],
                "status": "checked",
                "fingerprint": fp,
                "group_paths": [str(p.relative_to(ROOT)) for p in members],
                "fields": fields,
                "all_fields_retained": all(fields.values()),
                "source_scoped_snippets": len(original_snippets),
                "retained_scoped_snippets": len(retained),
            }
        )
    media = [r for r in rows if r["status"] == "checked"]
    return {
        "records": rows,
        "all_media_fields_retained": all(r["all_fields_retained"] for r in media),
        "all_media_snippets_retained": all(
            r["source_scoped_snippets"] == r["retained_scoped_snippets"] for r in media
        ),
        "scope": "Current full-corpus groups. Scoped literal quote retention is distinct from full ingredient, variant, explanation and history retention. Standalone solutions correctly remain outside medium merging. No generated corpus published.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--folder", type=Path, default=HERE)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    result = check(args.folder)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["all_media_fields_retained"] else 1)
