"""Measure stock structure and evidence retention in actual maintained merge groups."""

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
targets = {ROOT / r["path"]: r for r in plan["records"]}
groups = RecipeMatcher().group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
results, seen = [], set()
for fingerprint, paths in groups.items():
    relevant = [p for p in paths if p in targets]
    if not relevant:
        continue
    merged = RecipeMerger().merge_group(paths, fingerprint=fingerprint)
    for p in relevant:
        item = targets[p]
        assert item["kind"] != "solution", "Standalone composition entered medium merge"
        seen.add(p)
        doc = yaml.load(p.read_bytes(), Loader=yaml.CSafeLoader)
        nodes = []
        for field in ("ingredients", "solutions"):
            for node in doc[field]:
                matches = [
                    n
                    for n in merged.get(field, [])
                    if n["preferred_term"] == node["preferred_term"]
                ]
                nodes.append(
                    {
                        "field": field,
                        "name": node["preferred_term"],
                        "exact_entry_retained": node in matches,
                        "quantity_retained": len(matches) == 1
                        and matches[0].get("concentration") == node.get("concentration"),
                        "composition_retained": len(matches) == 1
                        and matches[0].get("composition") == node.get("composition"),
                    }
                )
        results.append(
            {
                "path": item["path"],
                "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                "fingerprint": fingerprint,
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
assert seen == {p for p, r in targets.items() if r["kind"] != "solution"}
failed = [
    r
    for r in results
    if not (
        all(n["exact_entry_retained"] for n in r["nodes"])
        and r["root_evidence_retained"]
        and r["references_retained"]
        and r["event_retained"]
    )
]
result = {
    "terminal": True,
    "media_records_checked": len(results),
    "standalone_solutions_excluded_as_expected": 2,
    "failed_records": len(failed),
    "details": results,
}
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "details"}))
raise SystemExit(bool(failed))
