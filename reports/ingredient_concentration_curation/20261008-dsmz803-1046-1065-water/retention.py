"""Check these water inputs in actual merge groups, excluding standalone solutions."""

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
results = []
seen = set()
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
        claim = next(c for c in item["claims"] if c["status"] == "correct")
        node = doc["ingredients"][claim["pointer"][1]]
        matches = [
            n
            for n in merged.get("ingredients", [])
            if n["preferred_term"] == node["preferred_term"]
            and n.get("concentration") == node["concentration"]
        ]
        retained = len(matches) == 1 and all(
            e in matches[0].get("evidence", []) for e in node["evidence"]
        )
        results.append(
            {
                "path": item["path"],
                "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                "fingerprint": fingerprint,
                "amount_and_both_exact_evidence_entries_retained": retained,
                "input_note_retained": len(matches) == 1
                and node["notes"] in matches[0].get("notes", ""),
                "pdf_reference_retained": doc["references"][-1] in merged.get("references", []),
                "event_retained": doc["curation_history"][-1] in merged.get("curation_history", []),
            }
        )
assert seen == {p for p, r in targets.items() if r["kind"] != "solution"}
failed = [
    r
    for r in results
    if not all(
        r[k]
        for k in [
            "amount_and_both_exact_evidence_entries_retained",
            "input_note_retained",
            "pdf_reference_retained",
            "event_retained",
        ]
    )
]
result = {
    "terminal": True,
    "media_records_checked": len(results),
    "standalone_solutions_excluded_as_expected": 3,
    "failed_records": len(failed),
    "details": results,
}
out.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps({k: v for k, v in result.items() if k != "details"}))
raise SystemExit(bool(failed))
