"""Independent source checks and complete-record inversion of six repairs."""

import argparse
import collections
import copy
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ACTION = "CORRECTED_DSMZ650_752_762_MEDIUM_AND_SOLUTION_PREPARATIONS"


def get(doc, pointer):
    for key in pointer:
        doc = doc[key]
    return doc


def provenance(node):
    counts = collections.Counter()
    if isinstance(node, dict):
        for k, v in node.items():
            if k in {"evidence", "references", "curation_history"}:
                counts["new_" + k] += len(v)
            else:
                counts.update(provenance(v))
    elif isinstance(node, list):
        for child in node:
            counts.update(provenance(child))
    return counts


def check(before, after, item, sources=None):
    if sources is None:
        sources = json.loads((HERE / "plan.json").read_text())["sources"]
    mid, kind = item["key"].split("-")
    solution = kind == "solution"
    field = "composition" if solution else "ingredients"
    capture = sources[item["key"]]
    raw, meta = capture["raw"], capture["metadata"]
    assert hashlib.sha256(raw.encode()).hexdigest() == meta["sha256"] == item["source_sha256"]
    assert meta["http_status"] == 200
    sid = {"650": 1378, "752": 1538, "762": 1552}[mid]
    ref = "https://mediadive.dsmz.de/rest/" + (f"solution/{sid}" if solution else f"medium/{mid}")
    assert meta["url"] == ref
    source = json.loads(raw)
    data = source["data"] if solution else source["data"]["solutions"][0]
    rows = data["recipe"]
    steps = [r["step"] for r in data["steps"]]
    assert data["id"] == sid and data["name"] == "Main sol. " + mid and data["volume"] == 1000
    assert before["id"] == after["id"] == item["id"] and item["action"] == ACTION
    assert hashlib.sha256(item["before_text"].encode()).hexdigest() == item["before_sha256"]
    if solution:
        assert before["term"]["id"] == f"mediadive.solution:{sid}"
        assert "physical_state" not in after and "evidence" not in after
        assert after["preparation_notes"] == before["preparation_notes"] == "\n".join(steps)
    else:
        assert source["data"]["medium"]["id"] == int(mid)
        assert source["data"]["medium"]["source"] == "DSMZ"
        assert before["media_term"]["term"]["id"] == "mediadive.medium:" + mid
        assert before["physical_state"] == after["physical_state"] == "LIQUID"
    for c in item["claims"]:
        assert c["old"] == (get(before, c["old_pointer"]) if c["old_pointer"] else None)
        assert c["new"] == get(after, c["pointer"])
        assert c["reference"] == ref and c["snippet"] in raw
        assert json.loads(c["snippet"]) == get(source, c["source_pointer"])
        entries = get(after, c["evidence_pointer"])["evidence"]
        assert len(entries) == 1
        e = entries[0]
        assert e["reference"] == ref and e["supports"] == "SUPPORT"
        assert c["field"] in e["explanation"] and c["locator"] in e["explanation"]
        assert c["explanation"] in e["explanation"]
        assert c["snippet"] == e["snippet"] or c["snippet"] in e["explanation"]
        assert meta["sha256"] in e["explanation"] and meta["accessed_at"] in e["explanation"]
        for q in c["extra_excerpts"]:
            assert q["snippet"] in raw and q["snippet"] in e["explanation"]
            assert q["locator"] in e["explanation"]
    counts = provenance(after)
    counts.subtract(provenance(before))
    restored = copy.deepcopy(after)
    stocks = restored.pop("solutions", [])

    def water(node, value, existing=False):
        assert node["preferred_term"] == "Distilled water"
        assert node["concentration"] == {"value": value, "unit": "L"}
        assert "not" in node["notes"] and "volume" in node["notes"]
        assert rows[-1]["compound_id"] == 4 and rows[-1]["amount"] == 1000
        if not existing:
            assert set(node) == {"preferred_term", "term", "concentration", "notes", "evidence"}
            assert node["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
        counts["quantity_corrections" if existing else "new_quantity_slots"] += 1

    if mid == "650":
        assert not stocks and len(restored[field]) == 6
        assert restored[field][4]["concentration"] == {"value": "1", "unit": "L"}
        assert rows[4]["amount"] == 1000 and rows[4]["unit"] == "ml"
        assert restored[field][5]["concentration"] == {"value": "20", "unit": "MILLIMOLAR"}
        assert rows[5]["amount"] == 20 and rows[5]["unit"] == "mM"
        assert "Add 20 mM pyruvate after autoclaving." in steps[1]
        assert "after autoclaving" in restored[field][5]["notes"]
        counts["quantity_corrections"] += 2
        if not solution:
            assert after["preparation_steps"] == before["preparation_steps"]
    elif mid == "752":
        assert len(stocks) == 2 and len(restored[field]) == 7
        carrier = restored[field].pop()
        water(carrier, "1", solution)
        for j, stock in enumerate(stocks):
            assert set(stock) == {
                "preferred_term",
                "composition",
                "concentration",
                "source",
                "notes",
            }
            assert stock["source"] == ref and len(stock["composition"]) == 1
            node = stock["composition"][0]
            assert stock["preferred_term"] == node["preferred_term"] + " stock"
            assert stock["concentration"] == {"value": "0.001", "unit": "L"}
            assert rows[j + 6]["amount"] == 1 and rows[j + 6]["unit"] == "ml"
            assert node["concentration"] == {"value": "0.36" if j == 0 else "50", "unit": "G_PER_L"}
            assert rows[j + 6]["attribute"] == node["concentration"]["value"] + "g/l"
            assert "not per liter" in stock["notes"] and "stock strength" in node["notes"]
            restored[field].append(node)
        if solution:
            restored[field].append(carrier)
            assert "conditional liquid/agar" in after["notes"]
        else:
            assert after["preparation_steps"] == [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Liquid medium may be prepared by adding all components together.",
                }
            ]
            assert after["preparation_steps"][0]["description"] in steps[0]
            restored["preparation_steps"] = copy.deepcopy(before["preparation_steps"])
            counts["preparation_actions_corrected"] += 1
            counts["preparation_descriptions_corrected"] += 1
        counts.update(
            stock_stage_concentrations_rebased=2,
            stock_nodes_relocated=2,
            stock_descriptors_added=2,
            new_quantity_slots=2,
        )
    else:
        assert mid == "762" and len(stocks) == 1 and len(restored[field]) == 5
        carrier = restored[field].pop()
        water(carrier, "0.9", solution)
        stock = stocks[0]
        assert set(stock) == {
            "preferred_term",
            "composition",
            "source",
            "notes",
            "preparation_notes",
        }
        assert stock["source"] == ref and stock["preparation_notes"] == steps[0]
        assert stock["preferred_term"] == "Separately sterilized carbonate preparation"
        assert (
            "900 ml distilled water" in steps[0]
            and "100 ml water, sterilise separately" in steps[0]
        )
        assert "not final stock volume or a numeric stock addition dose" in stock["notes"]
        assert "sterilization method is unspecified" in stock["notes"]
        assert len(stock["composition"]) == 3
        water(stock["composition"].pop(), "0.1")
        assert len(item["claim_resolutions"]) == 2
        for j, node in enumerate(stock["composition"]):
            row = rows[j + 4]
            assert "concentration" not in node and row["unit"] == "g"
            assert f"{row['amount']} g {row['compound']}" in node["notes"]
            assert (
                "withdrawn" in node["notes"]
                and "does not establish final stock volume" in node["notes"]
            )
            r = item["claim_resolutions"][j]
            assert r["from_pointer"] == [field, j + 4]
            assert r["to_pointer"] == ["solutions", 0, "composition", j]
            assert r["old_concentration"] == before[field][j + 4]["concentration"]
            assert r["reference"] == ref and r["disposition"] == "withdrawn"
            assert r["new_field"] == f"solutions[0].composition[{j}].notes"
            assert r["reason"] in node["evidence"][0]["explanation"]
            assert r["source_snippet"] in raw and json.loads(r["source_snippet"]) == get(
                source, r["source_pointer"]
            )
            restored[field].append(node)
        if solution:
            restored[field].append(carrier)
        else:
            assert after["preparation_steps"] == [
                {"step_number": 1, "action": "MIX", "description": steps[0]}
            ]
            restored["preparation_steps"] = copy.deepcopy(before["preparation_steps"])
            counts["preparation_actions_corrected"] += 1
        counts.update(
            unsupported_quantity_slots_removed=2, stock_nodes_relocated=2, stock_descriptors_added=1
        )
    if mid != "762":
        assert item["claim_resolutions"] == []
    direct = {"650": 4, "752": 6, "762": 4}[mid]
    for i, (node, old) in enumerate(zip(restored[field], before[field], strict=True)):
        assert node["preferred_term"] == old["preferred_term"] == rows[i]["compound"]
        if i < direct:
            assert node["concentration"] == old["concentration"]
            assert node["concentration"]["unit"] == "G_PER_L"
            assert Decimal(node["concentration"]["value"]) == Decimal(str(rows[i]["g_l"]))
            factor = Decimal("0.000001") if rows[i]["unit"] == "\u00b5g" else Decimal(1)
            assert Decimal(str(rows[i]["amount"])) * factor == Decimal(
                node["concentration"]["value"]
            )
            assert (
                "nominal main-recipe rate" in node["notes"]
                and "not a concentration" in node["notes"]
            )
        evidence = node.pop("evidence")
        assert len(evidence) == 1 and evidence[0]["reference"] == ref
        assert evidence[0]["snippet"] in raw
        prior = old.get("evidence", [])
        if prior:
            assert len(prior) == 1
            for k, v in prior[0].items():
                if k == "explanation":
                    assert evidence[0][k].endswith(v)
                else:
                    assert evidence[0][k] == v
            assert (
                "Historical explanation (superseded where preparation scope differs)"
                in evidence[0]["explanation"]
            )
            node["evidence"] = copy.deepcopy(prior)
            counts["evidence_scopes_corrected"] += 1
        node.pop("notes")
        node["concentration"] = copy.deepcopy(old["concentration"])
        assert node == old, "Unreviewed ingredient identity/metadata change"
    if solution:
        provenance_root = restored.pop("source_data")
        assert (
            set(provenance_root) == {"origin", "evidence"}
            and provenance_root["origin"] == "MediaDive"
        )
        entries = provenance_root["evidence"]
    else:
        entries = restored.pop("evidence")
    assert len(entries) == 1 and entries[0]["reference"] == ref
    assert after["references"] == before["references"]
    assert "not measured final volumes" in after["notes"]
    if "notes" in before:
        assert restored["notes"].startswith(before["notes"] + "\n\nPreparation follow-up:")
        restored["notes"] = before["notes"]
    else:
        restored.pop("notes")
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex" and event["source"] == ref
    assert all(c["field"] in event["changes"] for c in item["claims"])
    assert restored == before, "Unreviewed change outside full-record inversion"
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        current = (ROOT / item["path"]).read_bytes()
        assert (
            hashlib.sha256(current).hexdigest()
            == item["after_sha256" if args.applied else "before_sha256"]
        )
        assert hashlib.sha256(item["after_text"].encode()).hexdigest() == item["after_sha256"]
        counts.update(
            check(
                yaml.safe_load(item["before_text"]),
                yaml.safe_load(item["after_text"]),
                item,
                plan["sources"],
            )
        )
    result = {
        "records": len(plan["records"]),
        "applied": args.applied,
        "counts": dict(counts),
        "complete_record_inversion": True,
        "all_claim_excerpts_match": True,
        "historical_excerpts_preserved": True,
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
