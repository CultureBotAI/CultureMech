"""Independent semantic inversion and actual-group retention for P7/P10."""

import argparse
import collections
import copy
import hashlib
import importlib.util
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ACTION = "CORRECTED_PUBLIC_RECIPE_INPUT_BASES_WITH_SCOPED_EVIDENCE"


def get(node, pointer):
    for key in pointer:
        if node is None:
            return None
        if isinstance(node, list):
            node = node[key] if key < len(node) else None
        else:
            node = node.get(key)
    return node


def strip_evidence(node):
    count = 0
    if isinstance(node, dict):
        evidence = node.pop("evidence", [])
        assert len({e["reference"] for e in evidence}) == len(evidence)
        assert all(
            e["snippet"] and e["explanation"] and e["supports"] == "SUPPORT" for e in evidence
        )
        count += len(evidence)
        for value in node.values():
            count += strip_evidence(value)
    elif isinstance(node, list):
        for value in node:
            count += strip_evidence(value)
    return count


def check(before, after, item):
    assert before["id"] == after["id"] == item["id"]
    assert item["action"] == ACTION and item["medium_id"] in {"P7", "P10"}
    for c in item["claims"]:
        assert get(before, c["pointer"]) == c["old"]
        assert get(after, c["pointer"]) == c["new"]
        evidence = get(after, c["evidence_pointer"])["evidence"]
        entries = [e for e in evidence if e["reference"] == c["reference"]]
        assert len(entries) == 1 and entries[0]["supports"] == "SUPPORT"
        assert c["field"] in entries[0]["explanation"]
        assert c["snippet"] == entries[0]["snippet"] or c["snippet"] in entries[0]["explanation"]
    restored, original = copy.deepcopy(after), copy.deepcopy(before)
    count = collections.Counter(
        new_evidence=strip_evidence(restored), new_references=1, new_curation_history=1
    )
    assert strip_evidence(original) == 0
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    ref = restored["references"].pop()
    assert ref["reference"] == "https://mediadive.dsmz.de/medium/" + item["medium_id"]
    assert all(ref[k] for k in ("title", "authors", "year", "notes"))
    assert (
        "source_type=user_contributed_dataset_page" in ref["notes"]
        and "discovery_mode=existing_record_reference" in ref["notes"]
    )

    def water(container, amount, label="Distilled water"):
        node = container.pop()
        assert set(node) == {"preferred_term", "source", "notes"} | (
            {"concentration"} if amount else set()
        )
        assert node["preferred_term"] == label
        assert node["source"] == "MediaDive public Medium " + item["medium_id"]
        assert node["notes"]
        if amount:
            assert node["concentration"] == {"value": amount, "unit": "L"}
            count["new_quantity_slots"] += 1
        else:
            count["unquantified_solvent_nodes_added"] += 1
        count["water_input_nodes_added"] += 1

    assert "final" in restored["notes"] and restored["notes"] != before["notes"]
    restored["notes"] = before["notes"]
    water(restored["ingredients"], "1")
    if item["medium_id"] == "P7":
        assert before["id"] == "CultureMech:010437" and count["new_evidence"] == 23
        assert len(item["claims"]) == 32
        assert ref["year"] == 2023 and ref["authors"] == "Lorenz"
        water(restored["solutions"][0]["composition"], None, "Water")
        water(restored["solutions"][1]["composition"], "0.1", "Water")
        water(restored["solutions"][2]["composition"], "1")
        for i, value in enumerate(("0.005", "0.0004", "0.001")):
            node = restored["solutions"][i]
            assert node["concentration"] == {"value": value, "unit": "L"}
            assert "batch" in node["notes"] and "not L/L" in node["notes"]
            node["concentration"] = copy.deepcopy(before["solutions"][i]["concentration"])
            node["notes"] = before["solutions"][i]["notes"]
        ethanol = restored["ingredients"][8]
        assert ethanol["concentration"] == {"value": "0.0005", "unit": "L"}
        assert "not L/L" in ethanol.pop("notes")
        ethanol["concentration"] = copy.deepcopy(before["ingredients"][8]["concentration"])
        for i, literal in [(0, "0.1%"), (1, "10 mg Vitamin B12 in 100 ml H2O")]:
            node = restored["solutions"][i]["composition"][0]
            assert "concentration" not in node and literal in node.pop("notes")
            node["concentration"] = copy.deepcopy(
                before["solutions"][i]["composition"][0]["concentration"]
            )
        count.update(
            quantity_corrections=4,
            stock_dose_basis_corrections=3,
            unsupported_quantity_slots_removed=2,
            ingredient_context_notes_added=3,
            stock_context_notes_corrected=3,
        )
    else:
        assert before["id"] == "CultureMech:010430" and count["new_evidence"] == 16
        assert len(item["claims"]) == 19 and ref["year"] == 2024
        stock = restored["solutions"][0]
        assert "concentration" not in stock and "'trace'" in stock["notes"]
        stock["concentration"] = copy.deepcopy(before["solutions"][0]["concentration"])
        stock["notes"] = before["solutions"][0]["notes"]
        assert "salts or proportions" in restored["ingredients"][3].pop("notes")
        copper = after["solutions"][0]["composition"][3]
        assert copper["evidence"][0]["snippet"] == "**CuSO4 x 5 H2O**: Pesar 0.05 g."
        assert "Final volume of this solution" in copper["evidence"][0]["explanation"]
        count.update(
            unsupported_quantity_slots_removed=1,
            ingredient_context_notes_added=1,
            stock_context_notes_corrected=1,
        )
    count["recipe_context_notes_corrected"] += 1
    assert restored == before, "Unrelated scientific or historical edit"
    return count


def audit():
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        assert hashlib.sha256(item["before_text"].encode()).hexdigest() == item["before_sha256"]
        counts.update(check(yaml.safe_load(item["before_text"]), yaml.safe_load(raw), item))
    counts["edited_records"] = len(plan["records"])
    assert counts["edited_records"] == 2 and counts["new_evidence"] == 39
    return dict(counts)


def retention():
    from culturemech.merge.matcher import RecipeMatcher
    from culturemech.merge.merge_recipes import find_all_recipes
    from culturemech.merge.merger import RecipeMerger

    audit()
    spec = importlib.util.spec_from_file_location(
        "retention_fields", HERE.parent / "20261007-komodo12-extraction/check_retention.py"
    )
    shared = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(shared)
    groups = RecipeMatcher().group_recipes(find_all_recipes(ROOT / "data/normalized_yaml"))
    rows = []
    for item in json.loads((HERE / "plan.json").read_text())["records"]:
        target = ROOT / item["path"]
        matches = [(f, paths) for f, paths in groups.items() if target in paths]
        assert len(matches) == 1
        fingerprint, paths = matches[0]
        merged = RecipeMerger().merge_group(paths, fingerprint=fingerprint)
        source = yaml.safe_load(target.read_bytes())
        fields = shared.retention(merged, source)
        fields.update(
            {key: merged.get(key) == source.get(key) for key in ("notes", "curation_history")}
        )
        rows.append(
            {
                "path": item["path"],
                "fingerprint": fingerprint,
                "group_paths": [str(p.relative_to(ROOT)) for p in paths],
                "merged_id": merged["id"],
                "field_retention": fields,
                "all_checked_fields_retained": all(fields.values()),
            }
        )
    return {
        "records": rows,
        "retained": sum(r["all_checked_fields_retained"] for r in rows),
        "all_retained": all(r["all_checked_fields_retained"] for r in rows),
        "scope": "Actual complete corpus groups, including water membership changes. No generated merge published.",
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--retention", action="store_true")
    args = parser.parse_args()
    assert not args.out.exists(), args.out
    result = retention() if args.retention else audit()
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result), flush=True)
    raise SystemExit(1 if result.get("all_retained") is False else 0)
