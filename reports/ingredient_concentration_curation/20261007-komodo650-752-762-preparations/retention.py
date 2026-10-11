"""Check complete curated formulation retention in actual maintained merge groups."""

import json
from pathlib import Path

import yaml

from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    output = HERE / "merge-retention.json"
    assert not output.exists()
    plan = json.loads((HERE / "plan.json").read_text())
    targets = {ROOT / r["path"]: r for r in plan["records"]}
    groups = RecipeMatcher().group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    results = []
    for fingerprint, paths in groups.items():
        relevant = [p for p in paths if p in targets]
        if not relevant:
            continue
        merged = RecipeMerger().merge_group(paths, fingerprint=fingerprint)
        for path in relevant:
            doc = yaml.safe_load(path.read_bytes())
            checks = {
                field: merged.get(field) == doc.get(field)
                for field in ("ingredients", "solutions", "preparation_steps", "notes")
            }
            checks.update(
                evidence=all(e in merged.get("evidence", []) for e in doc["evidence"]),
                references=all(r in merged.get("references", []) for r in doc["references"]),
                event=doc["curation_history"][-1] in merged.get("curation_history", []),
            )
            results.append(
                {
                    "path": targets[path]["path"],
                    "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                    "fingerprint": fingerprint,
                    "checks": checks,
                    "passed": all(checks.values()),
                }
            )
    assert {r["path"] for r in results} == {r["path"] for r in plan["records"]}
    result = {
        "records": len(results),
        "passed": sum(r["passed"] for r in results),
        "details": results,
        "scope": "Exact formulation and provenance retention, not a claim that other members of concentration-independent groups are scientifically equivalent.",
    }
    output.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(int(result["passed"] != result["records"]))


if __name__ == "__main__":
    main()
