"""Independent claim readback, preparation checks and whole-record inversion."""

import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ACTION = "CORRECTED_DSMZ489_STOCK_BOUNDARIES_AND_WATER_INPUT"


def get(node, pointer):
    for key in pointer:
        node = node[key]
    return node


def provenance(node):
    counts = collections.Counter()
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"evidence", "references", "curation_history"}:
                counts["new_" + key] += len(value)
            else:
                counts.update(provenance(value))
    elif isinstance(node, list):
        for value in node:
            counts.update(provenance(value))
    return counts


def check(before, after, item, sources=None):
    if sources is None:
        sources = json.loads((HERE / "plan.json").read_text())["sources"]
    key = item["key"]
    solution = key == "solution"
    field = "composition" if solution else "ingredients"
    ref = "https://mediadive.dsmz.de/rest/" + ("solution/995" if solution else "medium/489")
    raw = sources[ref]["raw"]
    source = json.loads(raw)
    data = source["data"] if solution else source["data"]["solutions"][0]
    assert (
        hashlib.sha256(raw.encode()).hexdigest()
        == item["source_sha256"]
        == sources[ref]["metadata"]["sha256"]
    )
    assert data["id"] == 995 and data["volume"] == 1000 and len(data["recipe"]) == 12
    assert before["id"] == after["id"] == item["id"] and item["action"] == ACTION
    for c in item["claims"]:
        assert c["old"] == (get(before, c["old_pointer"]) if c["old_pointer"] is not None else None)
        assert c["new"] == get(after, c["pointer"])
        assert c["reference"] == ref and c["snippet"] in raw
        assert json.loads(c["snippet"]) == get(source, c["source_pointer"])
        entries = [
            e for e in get(after, c["evidence_pointer"])["evidence"] if e["reference"] == ref
        ]
        assert len(entries) == 1 and entries[0]["supports"] == "SUPPORT"
        e = entries[0]
        assert c["field"] in e["explanation"] and c["locator"] in e["explanation"]
        assert c["snippet"] == e["snippet"] or c["snippet"] in e["explanation"]
        assert item["source_sha256"] in e["explanation"]
    restored = copy.deepcopy(after)
    assert len(restored[field]) == 9 and len(restored["solutions"]) == 3
    water = restored[field].pop()
    assert water["preferred_term"] == data["recipe"][11]["compound"] == "Distilled water"
    assert data["recipe"][11]["amount"] == 1000 and data["recipe"][11]["unit"] == "ml"
    assert water["concentration"] == {"value": "1", "unit": "L"}
    assert (
        "input" in water["notes"] and "not a volume percentage or measured final" in water["notes"]
    )
    assert len(water["evidence"]) == 1 and water["evidence"][0]["reference"] == ref
    stocks = restored.pop("solutions")
    for si, stock in enumerate(stocks):
        assert len(stock["composition"]) == 1 and stock["source"] == ref
        allowed = {
            "preferred_term",
            "source",
            "notes",
            "composition",
            "concentration" if si == 0 else "preparation_notes",
        }
        assert set(stock) == allowed
        node = stock["composition"][0]
        row = data["recipe"][8 + si]
        assert node["preferred_term"] == row["compound"]
        if si == 0:
            assert row["attribute"] == "0.1% w/v" and row["amount"] == 0.5 and row["unit"] == "ml"
            assert stock["concentration"] == {"value": "0.0005", "unit": "L"}
            assert node["concentration"] == {"value": "0.1", "unit": "PERCENT_W_V"}
            assert (
                "not per liter" in stock["notes"] and "not independently validated" in node["notes"]
            )
        else:
            assert row["amount"] == 0.15 and row["unit"] == "g"
            assert "concentration" not in node and "concentration" not in stock
            assert stock["preparation_notes"] in data["steps"][0]["step"]
            assert (
                "After sterilization" in stock["preparation_notes"]
                and "100% N2" in stock["preparation_notes"]
            )
            assert (
                "0.15 g" in node["notes"]
                and "solvent identity and numeric stock dose are unspecified" in node["notes"]
            )
        restored[field].append(node)
    for i, (node, old) in enumerate(zip(restored[field], before[field][:11], strict=True)):
        row = data["recipe"][i]
        assert node["preferred_term"] == old["preferred_term"] == row["compound"]
        if i < 8:
            assert (
                node["concentration"]
                == old["concentration"]
                == {"value": str(row["g_l"]), "unit": "G_PER_L"}
            )
            assert "nominal 1000 ml recipe rate" in node["notes"]
        else:
            node["concentration"] = copy.deepcopy(old["concentration"])
        entries = node.pop("evidence")
        assert len(entries) == 1 and entries[0]["reference"] == ref
        if old.get("evidence"):
            assert len(old["evidence"]) == 1
            for slot in ("reference", "supports", "snippet"):
                assert entries[0][slot] == old["evidence"][0][slot]
            assert entries[0]["explanation"].endswith(old["evidence"][0]["explanation"])
            node["evidence"] = copy.deepcopy(old["evidence"])
        node.pop("notes")
        assert node == old, "Unreviewed ingredient/mapping change"
    water.pop("notes")
    water.pop("evidence")
    if solution:
        water["concentration"] = copy.deepcopy(before[field][11]["concentration"])
        assert water == before[field][11]
        restored[field].append(water)
        container = restored.pop("source_data")
        assert set(container) == {"origin", "evidence"} and container["origin"] == "MediaDive"
        root = container["evidence"]
    else:
        assert set(water) == {"preferred_term", "term", "concentration"}
        assert water["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
        root = restored.pop("evidence")
    assert len(root) == (3 if key == "komodo" else 2) and root[0]["reference"] == ref
    pdf = sources["pdf"]
    assert root[1]["reference"] == pdf["reference"] and root[1]["supports"] == "SUPPORT"
    assert root[1]["snippet"] == "Sodium resazurin (0.1% w/v) 0.50 ml"
    assert (
        root[1]["snippet"] in pdf["extracted_text"] and pdf["pdf_sha256"] in root[1]["explanation"]
    )
    assert (
        "Distilled water 1000.00 ml" in pdf["extracted_text"]
        and "Distilled water 1000.00 ml" in root[1]["explanation"]
    )
    assert "not verified incubation or growth evidence" in restored["notes"]
    if "notes" in before:
        assert restored["notes"].startswith(before["notes"] + "\n\n")
        restored["notes"] = before["notes"]
    else:
        restored.pop("notes")
    if key == "komodo":
        assert root[2]["reference"] == sources["mapping_metadata"]["reference"]
        assert (
            root[2]["snippet"] == sources["mapping"]["snippet"] and root[2]["supports"] == "SUPPORT"
        )
        assert restored.pop("preparation_steps") == [
            {"step_number": 1, "action": "DISSOLVE", "description": data["steps"][0]["step"]}
        ]
    refs = restored.pop("references")
    prior = before.get("references", [])
    assert refs[: len(prior)] == prior and len(refs[len(prior) :]) == (3 if key == "komodo" else 1)
    for r in refs[len(prior) :]:
        assert r["title"] and all(
            k in r["notes"] for k in ("source_type=", "discovery_mode=", "accessed_on=")
        )
        assert "authors" not in r and "year" not in r
    if prior:
        restored["references"] = copy.deepcopy(prior)
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert ref in event["source"] and pdf["reference"] in event["source"]
    assert all(c["field"] in event["changes"] for c in item["claims"])
    assert restored == before, "Unreviewed whole-record change"
    counts = provenance(after)
    counts.subtract(provenance(before))
    counts.update(
        stock_nodes_relocated=3,
        stock_descriptors_added=3,
        stock_stage_concentrations_rebased=1,
        unsupported_quantity_slots_removed=2,
        quantity_corrections=int(solution),
        new_quantity_slots=1 if solution else 2,
        ingredient_context_notes_added=12,
        recipe_context_notes_corrected=1,
        evidence_scopes_corrected=0 if key == "komodo" else 10,
        preparation_steps_added=int(key == "komodo"),
    )
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes() if args.applied else item["after_text"].encode()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        counts.update(
            check(
                yaml.load(item["before_text"], Loader=yaml.CSafeLoader),
                yaml.load(raw, Loader=yaml.CSafeLoader),
                item,
                plan["sources"],
            )
        )
    result = {
        "full_record_inversion": True,
        "records": len(plan["records"]),
        "applied": args.applied,
        **counts,
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
