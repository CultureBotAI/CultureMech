"""Independent inversion of the P2/P8 stock-evidence repairs."""

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
DOI = "doi:10.1007/s11104-022-05822-6"
ACTION = "CURATED_PUBLIC_STOCK_CONCENTRATIONS_FROM_SCOPED_SOURCES"


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
        assert all(e["snippet"] and e["explanation"] for e in evidence)
        count += len(evidence)
        for value in node.values():
            count += strip_evidence(value)
    elif isinstance(node, list):
        for value in node:
            count += strip_evidence(value)
    return count


def check(before, after, item):
    assert before["id"] == after["id"] == item["id"]
    assert item["medium_id"] in {"P2", "P8"}
    assert item["action"] == ACTION
    for claim in item["claims"]:
        assert get(after, claim["pointer"]) == claim["new"]
        assert get(before, claim["pointer"]) == claim["old"]
        entries = [
            e
            for e in get(after, claim["evidence_pointer"])["evidence"]
            if e["reference"] == claim["reference"]
        ]
        assert len(entries) == 1
        entry = entries[0]
        assert entry["supports"] == claim["supports"]
        assert claim["field"] in entry["explanation"]
        assert claim["snippet"] == entry["snippet"] or claim["snippet"] in entry["explanation"]
    restored = copy.deepcopy(after)
    counts = collections.Counter(
        new_evidence=strip_evidence(restored), new_references=1, new_curation_history=1
    )
    untouched = copy.deepcopy(before)
    assert strip_evidence(untouched) == 0
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    ref = restored["references"].pop()
    assert ref["reference"] == "https://mediadive.dsmz.de/medium/" + item["medium_id"]
    assert all(ref[k] for k in ("title", "authors", "year", "notes"))
    assert "source_type=user_contributed_dataset_page" in ref["notes"]
    assert "discovery_mode=" in ref["notes"]
    if item["medium_id"] == "P2":
        assert before["id"] == "CultureMech:010432"
        assert (
            counts["new_evidence"] == 28 and ref["year"] == 2023 and ref["authors"] == "Taiyang Jin"
        )
        assert len(restored["solutions"][1]["composition"]) == 3
        water = restored["solutions"][1]["composition"].pop()
        assert water == {
            "preferred_term": "Distilled water",
            "source": "MediaDive public Medium P2",
            "notes": "Make up the haemin stock to 100 ml with distilled water after dissolving 50 mg haemin in 1 ml 1 N NaOH. The added water amount is not fixed at 100 ml; no numeric water concentration or volume is asserted.",
        }
        assert {tuple(c["pointer"]) for c in item["claims"]} == {
            *[("ingredients", i, "concentration") for i in range(14)],
            ("solutions", 0, "concentration"),
            ("solutions", 1, "concentration"),
            *[("solutions", 0, "composition", i, "concentration") for i in range(10)],
            *[("solutions", 1, "composition", i, "concentration") for i in range(3)],
        }
        assert len(item["claims"]) == 29
        counts["unquantified_makeup_nodes_added"] += 1
    else:
        assert before["id"] == "CultureMech:010438" and counts["new_evidence"] == 9
        assert ref["year"] == 2024
        stock_values = ["0.002", "0.000010", "0.002", "0.002"]
        for i, value in enumerate(stock_values):
            node = restored["solutions"][i]
            assert node["concentration"] == {"value": value, "unit": "L"}
            assert "per recipe batch" in node["notes"] and "not L/L" in node["notes"]
            node["concentration"] = copy.deepcopy(before["solutions"][i]["concentration"])
            node["notes"] = before["solutions"][i]["notes"]
        sinigrin = restored["solutions"][2]["composition"][0]
        assert "sinigrin hydrate" in sinigrin.pop("notes")
        phosphate = restored["solutions"][3]["composition"][1]
        assert phosphate["concentration"] == {"value": "15", "unit": "G_PER_L"}
        assert "51.0 g/L" in phosphate.pop("notes") and phosphate["source"] == DOI
        phosphate["source"] = before["solutions"][3]["composition"][1]["source"]
        phosphate["concentration"] = copy.deepcopy(
            before["solutions"][3]["composition"][1]["concentration"]
        )
        assert restored["notes"].startswith(before["notes"])
        assert "no final-medium component dilution" in restored["notes"]
        restored["notes"] = before["notes"]
        bibliographic = restored["references"][0]
        assert bibliographic["reference"] == DOI and bibliographic["year"] == 2023
        assert all(bibliographic[k] for k in ("title", "authors", "notes"))
        assert "version=HAL v1 author manuscript" in bibliographic["notes"]
        assert not any(r["reference"] == DOI.removeprefix("doi:") for r in restored["references"])
        restored["references"][0] = copy.deepcopy(before["references"][0])
        entries = after["solutions"][3]["composition"][1]["evidence"]
        assert {e["supports"] for e in entries} == {"SUPPORT", "REFUTE"}
        assert (
            next(e for e in entries if e["supports"] == "REFUTE")["snippet"]
            == "KH2PO4 51.0 g/l 51 374.766"
        )
        counts.update(
            quantity_corrections=5,
            stock_dose_basis_corrections=4,
            ingredient_source_attributions_corrected=1,
            ingredient_context_notes_added=2,
            stock_context_notes_corrected=4,
            recipe_context_notes_corrected=1,
            bibliographic_entries_enriched=1,
        )
    assert restored == before, "Unrelated scientific or historical changes"
    return counts


def audit():
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        assert hashlib.sha256(item["before_text"].encode()).hexdigest() == item["before_sha256"]
        counts.update(check(yaml.safe_load(item["before_text"]), yaml.safe_load(raw), item))
    counts["edited_records"] = len(plan["records"])
    assert counts["edited_records"] == 2 and counts["new_evidence"] == 37
    return dict(counts)


def retention():
    from culturemech.merge.matcher import RecipeMatcher
    from culturemech.merge.merge_recipes import find_all_recipes
    from culturemech.merge.merger import RecipeMerger

    audit()
    spec = importlib.util.spec_from_file_location(
        "retention_check", HERE.parent / "20261007-komodo12-extraction/check_retention.py"
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
        "scope": "Actual complete corpus groups. No generated merge published.",
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
