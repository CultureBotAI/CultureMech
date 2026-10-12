"""Audit the three repaired records in actual current corpus merge groups."""

import argparse
import hashlib
import json
from pathlib import Path

import yaml

from culturemech.merge.fingerprint import StandaloneSolutionError
from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merge_recipes import find_all_recipes
from culturemech.merge.merger import RecipeMerger

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent


def check():
    plan = json.loads((HERE / "plan.json").read_text())
    matcher = RecipeMatcher()
    groups = matcher.group_formulations(find_all_recipes(ROOT / "data/normalized_yaml"))
    rows = []
    for item in plan["records"]:
        target = ROOT / item["path"]
        raw = target.read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        source = yaml.load(raw, Loader=yaml.CSafeLoader)
        matches = [(fp, paths) for fp, paths in groups.items() if target in paths]
        assert len(matches) <= 1
        if not matches:
            # An excluded input is not counted as successful evidence retention.
            try:
                fingerprint = matcher.fingerprinter.fingerprint(source)
                status = "not_represented_in_merge"
            except StandaloneSolutionError:
                fingerprint = None
                status = "outside_medium_scope"
            rows.append(
                {
                    "path": item["path"],
                    "status": status,
                    "fingerprint": fingerprint,
                    "all_checked_fields_retained": False,
                }
            )
            continue
        fp, paths = matches[0]
        merged = RecipeMerger().merge_group(paths)
        fields = {
            key: merged.get(key) == source.get(key)
            for key in (
                "ingredients",
                "composition",
                "solutions",
                "preparation_steps",
                "preparation_notes",
                "notes",
                "ph_value",
                "physical_state",
                "source_data",
            )
        }
        for field in ("evidence", "references"):
            actual = merged.get(field, [])
            fields[field] = len({e["reference"] for e in actual}) == len(actual) and all(
                e in actual for e in source.get(field, [])
            )
        fields["curation_history"] = all(
            e in merged.get("curation_history", []) for e in source["curation_history"]
        )
        rows.append(
            {
                "path": item["path"],
                "status": "checked",
                "fingerprint": fp,
                "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                "merged_id": merged["id"],
                "field_retention": fields,
                "all_checked_fields_retained": all(fields.values()),
            }
        )
    return {
        "records": rows,
        "all_retained": all(r["all_checked_fields_retained"] for r in rows),
        "retained": sum(r["all_checked_fields_retained"] for r in rows),
        "scope": "Actual current corpus groups, not a forced merge of the selected inputs. Exact ingredient/stock/preparation equality; root provenance may add but not discard entries. Excluded inputs are not a pass. No generated merge published.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    assert not args.out.exists()
    result = check()
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["all_retained"] else 1)
