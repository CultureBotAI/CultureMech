"""Check these three media in actual merge groups; exclude the standalone solution."""

import json
from pathlib import Path

import yaml

from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
plan = json.loads((HERE / "plan.json").read_text())
out = HERE / "merge-retention.json"
assert not out.exists()
targets = {ROOT / r["path"]: r for r in plan["records"] if r["target_class"] == "MediaRecipe"}
excluded = {ROOT / r["path"] for r in plan["records"] if r["target_class"] == "SolutionRecipe"}
groups = RecipeMatcher().group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
results, seen = [], set()
for fingerprint, paths in groups.items():
    assert not excluded.intersection(paths)
    relevant = [p for p in paths if p in targets]
    if not relevant:
        continue
    merged = RecipeMerger().merge_group(paths, fingerprint=fingerprint)
    for path in relevant:
        seen.add(path)
        doc = yaml.load(path.read_bytes(), Loader=yaml.CSafeLoader)
        nodes = []
        for node in doc["solutions"]:
            matches = [
                n
                for n in merged.get("solutions", [])
                if n["preferred_term"] == node["preferred_term"]
            ]
            nodes.append(
                {
                    "name": node["preferred_term"],
                    "exact_entry_retained": node in matches,
                    "composition_retained": len(matches) == 1
                    and matches[0].get("composition") == node["composition"],
                    "no_invented_working_dose": len(matches) == 1
                    and "concentration" not in matches[0],
                }
            )
        results.append(
            {
                "path": targets[path]["path"],
                "fingerprint": fingerprint,
                "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                "nodes": nodes,
                "root_evidence_retained": all(
                    e in merged.get("evidence", []) for e in doc["evidence"]
                ),
                "references_retained": all(
                    r in merged.get("references", []) for r in doc["references"]
                ),
                "event_retained": doc["curation_history"][-1] in merged.get("curation_history", []),
            }
        )
assert seen == set(targets)
failed = [
    r
    for r in results
    if not (
        all(n["exact_entry_retained"] and n["no_invented_working_dose"] for n in r["nodes"])
        and r["root_evidence_retained"]
        and r["references_retained"]
        and r["event_retained"]
    )
]
result = {
    "terminal": True,
    "media_records_checked": len(results),
    "solutions_excluded": len(excluded),
    "failed_records": len(failed),
    "details": results,
}
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "details"}))
raise SystemExit(bool(failed))
