"""Inspect actual medium merge groups and standalone-solution routing."""

import hashlib
import json
from pathlib import Path

import yaml

from culturemech.merge.fingerprint import RecipeFingerprinter
from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger
from culturemech.validation.write_validated import infer_target_class

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
                    "status": "medium_merge_checked",
                    "fingerprint": fingerprint,
                    "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                    "checks": checks,
                    "passed": all(checks.values()),
                }
            )
    grouped = {p for paths in groups.values() for p in paths}
    for path, item in targets.items():
        if item["target_class"] != "SolutionRecipe":
            continue
        doc = yaml.safe_load(path.read_bytes())
        excluded = path not in grouped and infer_target_class(doc) == "SolutionRecipe"
        rejected = False
        try:
            RecipeFingerprinter().fingerprint(doc)
        except ValueError as exc:
            rejected = "SolutionRecipe" in str(exc)
        results.append(
            {
                "path": item["path"],
                "status": "standalone_solution_routing_checked",
                "checks": {
                    "excluded_from_medium_groups": excluded,
                    "medium_fingerprint_rejected": rejected,
                },
                "passed": excluded and rejected,
            }
        )
    assert {r["path"] for r in results} == {r["path"] for r in plan["records"]}
    result = {
        "records": len(results),
        "passed": sum(r["passed"] for r in results),
        "details": results,
        "routing_stats": matcher._last_skip_stats,
        "scope": "Exact medium formulation/provenance retention and correct standalone routing; not proof that members of concentration-independent groups are identical formulations.",
    }
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(int(result["passed"] != result["records"]))


if __name__ == "__main__":
    main()
