"""Check exact formulation/version retention in the actual current merge groups."""

import hashlib
import json
from pathlib import Path

import yaml

from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    out = HERE / "merge-retention.json"
    assert not out.exists()
    plan = json.loads((HERE / "plan.json").read_text())
    targets = {ROOT / r["path"]: r for r in plan["records"]}
    for path, item in targets.items():
        assert hashlib.sha256(path.read_bytes()).hexdigest() == item["after_sha256"]
    matcher = RecipeMatcher()
    groups = matcher.group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    results = []
    for fingerprint, paths in groups.items():
        relevant = [p for p in paths if p in targets]
        if not relevant:
            continue
        merged = RecipeMerger().merge_group(paths, fingerprint=fingerprint)
        for path in relevant:
            doc = yaml.load(path.read_bytes(), Loader=yaml.CSafeLoader)
            checks = {
                field: merged.get(field) == doc.get(field)
                for field in (
                    "ingredients",
                    "solutions",
                    "preparation_steps",
                    "ph_value",
                    "variants",
                    "parent_media",
                    "variant_relationship",
                    "variant_modifications",
                    "variant_children",
                    "notes",
                )
            }
            checks.update(
                evidence=all(e in merged.get("evidence", []) for e in doc["evidence"]),
                references=all(r in merged.get("references", []) for r in doc["references"]),
                event=doc["curation_history"][-1] in merged.get("curation_history", []),
            )
            results.append(
                {
                    "path": targets[path]["path"],
                    "fingerprint": fingerprint,
                    "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                    "checks": checks,
                    "passed": all(checks.values()),
                }
            )
    checked = {r["path"] for r in results}
    for item in plan["records"]:
        if item["path"] not in checked:
            results.append(
                {
                    "path": item["path"],
                    "passed": False,
                    "checks": {"present_in_merge_groups": False},
                    "note": "Not assigned to a current merge group; not proof that the formulation is retained.",
                }
            )
    result = {
        "records": len(results),
        "passed": sum(r["passed"] for r in results),
        "details": results,
        "routing_stats": matcher._last_skip_stats,
        "scope": "Actual current grouping, exact source-version/formulation/link/provenance retention. Concentration-independent fingerprints do not establish identical formulations.",
    }
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(int(result["passed"] != result["records"]))


if __name__ == "__main__":
    main()
