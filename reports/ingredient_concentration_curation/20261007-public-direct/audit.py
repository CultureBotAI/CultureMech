"""Independent evidence-only diff and actual-corpus merge-retention checks."""

import argparse
import copy
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


def audit():
    plan = json.loads((HERE / "plan.json").read_text())
    counts = {
        "edited_records": 0,
        "new_evidence": 0,
        "new_references": 0,
        "new_curation_history": 0,
    }
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        assert hashlib.sha256(item["before_text"].encode()).hexdigest() == item["before_sha256"]
        before, after = yaml.load(item["before_text"], Loader=yaml.CSafeLoader), yaml.load(
            raw, Loader=yaml.CSafeLoader
        )
        restored = copy.deepcopy(after)
        is_p6 = item["id"] == "CultureMech:010436"
        assert item["id"] in {"CultureMech:010433", "CultureMech:010436"}
        assert after["id"] == before["id"] == item["id"]
        expected = (
            [
                ("Tryptose", "10", "G_PER_L"),
                ("Beef extract", "5", "G_PER_L"),
                ("Yeast extract", "5", "G_PER_L"),
                ("NaCl", "5", "G_PER_L"),
                ("KH2PO4", "3.4", "G_PER_L"),
                ("Na2HPO4", "19.3", "G_PER_L"),
            ]
            if is_p6
            else [
                ("K2HPO4", "1.5", "G_PER_L"),
                ("MgSO4 x 7 H2O", "1.5", "G_PER_L"),
                ("Proteose peptone no. 3", "20", "G_PER_L"),
                ("Glycerol", "10", "ML_PER_L"),
                ("Agar", "15", "G_PER_L"),
            ]
        )
        assert len(restored["ingredients"]) == len(expected)
        for index, (node, (label, value, unit)) in enumerate(
            zip(restored["ingredients"], expected, strict=True)
        ):
            assert node["preferred_term"] == label
            assert node["concentration"] == {"value": value, "unit": unit}
            entries = node.pop("evidence")
            assert len(entries) == (2 if is_p6 else 1)
            for entry in entries:
                assert entry["supports"] == "SUPPORT" and entry["snippet"]
                assert f"ingredients[{index}].concentration" in entry["explanation"]
                assert label in entry["snippet"] and value in entry["snippet"]
            assert entries[0]["reference"] == "https://mediadive.dsmz.de/medium/" + (
                "P6" if is_p6 else "P3"
            )
            if is_p6:
                assert entries[1]["reference"] == "doi:10.3390/microorganisms8091359"
                assert entries[1]["snippet"] == f"{value} g/L {label}"
            counts["new_evidence"] += len(entries)
        ref_count = 2 if is_p6 else 1
        added = restored["references"][-ref_count:]
        assert all(
            all(key in r for key in ("reference", "title", "authors", "year", "notes"))
            for r in added
        )
        assert all("source_type=" in r["notes"] and "discovery_mode=" in r["notes"] for r in added)
        del restored["references"][-ref_count:]
        event = restored["curation_history"].pop()
        assert event["action"] == "ADDED_PUBLIC_DIRECT_CONCENTRATION_EVIDENCE"
        assert event["curator"] == "codex"
        assert restored == before, "Unrelated scientific or historical change"
        counts["new_references"] += ref_count
        counts["new_curation_history"] += 1
        counts["edited_records"] += 1
    assert counts == {
        "edited_records": 2,
        "new_evidence": 17,
        "new_references": 3,
        "new_curation_history": 2,
    }
    return counts


def retention():
    audit()
    spec = importlib.util.spec_from_file_location(
        "full_retention", HERE.parent / "20261007-komodo12-extraction/check_retention.py"
    )
    shared = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(shared)
    groups = RecipeMatcher().group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    results = []
    for item in json.loads((HERE / "plan.json").read_text())["records"]:
        target = ROOT / item["path"]
        matches = [(fp, paths) for fp, paths in groups.items() if target in paths]
        assert len(matches) == 1
        fp, paths = matches[0]
        merged = RecipeMerger().merge_group(paths, fingerprint=fp)
        fields = shared.retention(merged, yaml.load(target.read_bytes(), Loader=yaml.CSafeLoader))
        results.append(
            {
                "path": item["path"],
                "fingerprint": fp,
                "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                "merged_id": merged["id"],
                "field_retention": fields,
                "all_checked_fields_retained": all(fields.values()),
            }
        )
    return {
        "records": results,
        "retained": sum(r["all_checked_fields_retained"] for r in results),
        "all_retained": all(r["all_checked_fields_retained"] for r in results),
        "scope": "Actual complete corpus groups; exact ingredient/stock/preparation/state/pH retention and full source evidence/reference retention. No generated merge is published.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--retention", action="store_true")
    args = parser.parse_args()
    assert not args.out.exists(), args.out
    result = retention() if args.retention else audit()
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), flush=True)
    raise SystemExit(1 if result.get("all_retained") is False else 0)
