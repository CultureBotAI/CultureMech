"""Independent source readback, arithmetic and complete-record inversion."""

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
COHORT = HERE.parent / "20261007-komodo-media-2000-2500"
ACTION = "CORRECTED_KOMODO650_752_762_AMOUNTS_AND_PREPARATION_STAGES"


def get(doc, pointer):
    for key in pointer:
        doc = doc[key]
    return doc


def check(before, after, item):
    mid = item["medium_id"]
    capture = next(
        x
        for x in json.loads((COHORT / "inspected-candidate-context.json").read_text())
        if x["medium_id"] == mid
    )
    raw = capture["source_raw"]
    assert (
        hashlib.sha256(raw.encode()).hexdigest()
        == item["source_sha256"]
        == capture["source_metadata"]["sha256"]
    )
    assert hashlib.sha256(item["before_text"].encode()).hexdigest() == item["before_sha256"]
    source = json.loads(raw)
    data = source["data"]["solutions"][0]
    ref = "https://mediadive.dsmz.de/rest/medium/" + mid
    assert source["data"]["medium"]["id"] == int(mid)
    assert before["id"] == after["id"] == item["id"] and item["action"] == ACTION
    assert before["physical_state"] == after["physical_state"] == "LIQUID"
    for c in item["claims"]:
        assert c["old"] == (get(before, c["old_pointer"]) if c["old_pointer"] else None)
        assert c["new"] == get(after, c["pointer"])
        assert c["reference"] == ref and c["snippet"] in raw
        assert json.loads(c["snippet"]) == get(source, c["source_pointer"])
        entries = get(after, c["evidence_pointer"])["evidence"]
        assert len(entries) == (2 if not c["evidence_pointer"] else 1)
        e = entries[0]
        assert e["reference"] == ref and e["supports"] == "SUPPORT"
        assert c["field"] in e["explanation"] and c["locator"] in e["explanation"]
        assert c["snippet"] == e["snippet"] or c["snippet"] in e["explanation"]
        assert item["source_sha256"] in e["explanation"]
        for q in c["extra_excerpts"]:
            assert q["snippet"] in raw and q["snippet"] in e["explanation"]
            assert q["locator"] in e["explanation"]
    counts = collections.Counter(new_curation_history=1, new_references=2, new_evidence=2)
    restored = copy.deepcopy(after)

    def check_water(node, value):
        assert set(node) == {"preferred_term", "term", "concentration", "notes", "evidence"}
        assert node["preferred_term"] == "Distilled water"
        assert node["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
        assert node["concentration"] == {"value": value, "unit": "L"}
        assert "not" in node["notes"] and "volume" in node["notes"]
        assert len(node["evidence"]) == 1 and node["evidence"][0]["reference"] == ref
        assert data["recipe"][-1]["compound_id"] == 4 and data["recipe"][-1]["amount"] == 1000
        counts.update(new_quantity_slots=1, new_evidence=1)

    stocks = restored.pop("solutions", [])
    step = data["steps"][0]["step"]
    if mid == "650":
        assert not stocks and len(restored["ingredients"]) == 6
        water, pyr = restored["ingredients"][4:]
        assert water["concentration"] == {"value": "1", "unit": "L"}
        assert data["recipe"][4]["amount"] / 1000 == 1 and data["recipe"][4]["unit"] == "ml"
        assert pyr["concentration"] == {"value": "20", "unit": "MILLIMOLAR"}
        assert data["recipe"][5]["amount"] == 20 and data["recipe"][5]["unit"] == "mM"
        assert "Add 20 mM pyruvate after autoclaving." in data["steps"][1]["step"]
        assert "after autoclaving" in pyr["notes"] and "not a mass" in water["notes"]
        assert after["preparation_steps"] == [
            {"step_number": 1, "action": "ADJUST_PH", "description": step},
            {"step_number": 2, "action": "HEAT", "description": data["steps"][1]["step"]},
        ]
        counts["quantity_corrections"] += 2
    elif mid == "752":
        assert len(stocks) == 2 and len(restored["ingredients"]) == 7
        check_water(restored["ingredients"].pop(), "1")
        for i, s in enumerate(stocks):
            assert set(s) == {"preferred_term", "composition", "concentration", "notes", "source"}
            assert len(s["composition"]) == 1 and s["source"] == ref
            node = s["composition"][0]
            row = data["recipe"][i + 6]
            assert row["unit"] == "ml" and row["amount"] == 1
            assert s["concentration"] == {"value": "0.001", "unit": "L"}
            assert node["concentration"] == {"value": "0.36" if i == 0 else "50", "unit": "G_PER_L"}
            assert row["attribute"] == node["concentration"]["value"] + "g/l"
            assert s["preferred_term"] == node["preferred_term"] + " stock"
            assert "no final-medium volume" in s["notes"] and "stock strength" in node["notes"]
            restored["ingredients"].append(node)
        assert after["preparation_steps"] == [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Liquid medium may be prepared by adding all components together.",
            }
        ]
        assert after["preparation_steps"][0]["description"] in step
        assert "agar/carbonate alternative is not applied" in after["notes"]
        counts.update(
            new_quantity_slots=2,
            stock_stage_concentrations_rebased=2,
            stock_nodes_relocated=2,
            stock_descriptors_added=2,
        )
    else:
        assert mid == "762" and len(stocks) == 1 and len(restored["ingredients"]) == 5
        check_water(restored["ingredients"].pop(), "0.9")
        stock = stocks[0]
        assert set(stock) == {
            "preferred_term",
            "composition",
            "preparation_notes",
            "notes",
            "source",
        }
        assert stock["preferred_term"] == "Separately sterilized carbonate preparation"
        assert stock["source"] == ref and stock["preparation_notes"] == step
        assert "900 ml distilled water" in step and "100 ml water, sterilise separately" in step
        assert "not final stock volume or numeric stock addition dose" in stock["notes"]
        assert "sterilization method is not specified" in stock["notes"]
        assert len(stock["composition"]) == 3
        check_water(stock["composition"].pop(), "0.1")
        for j, node in enumerate(stock["composition"]):
            row = data["recipe"][j + 4]
            assert "concentration" not in node and row["unit"] == "g"
            assert f"{row['amount']} g {row['compound']}" in node["notes"]
            assert "withdrawn" in node["notes"] and "not final stock volume" in node["notes"]
            restored["ingredients"].append(node)
        assert after["preparation_steps"] == [
            {"step_number": 1, "action": "MIX", "description": step}
        ]
        counts.update(
            unsupported_quantity_slots_removed=2, stock_nodes_relocated=2, stock_descriptors_added=1
        )

    direct = {"650": 4, "752": 6, "762": 4}[mid]
    for i, (node, old) in enumerate(
        zip(restored["ingredients"], before["ingredients"], strict=True)
    ):
        assert node["preferred_term"] == old["preferred_term"] == data["recipe"][i]["compound"]
        if i < direct:
            assert node["concentration"] == old["concentration"]
            assert Decimal(node["concentration"]["value"]) == Decimal(str(data["recipe"][i]["g_l"]))
            assert "nominal main-recipe rate" in node["notes"] and "not a measured" in node["notes"]
        evidence = node.pop("evidence")
        assert (
            len(evidence) == 1 and evidence[0]["reference"] == ref and evidence[0]["snippet"] in raw
        )
        node.pop("notes")
        node["concentration"] = copy.deepcopy(old["concentration"])
        counts["new_evidence"] += 1
    cohort = json.loads((COHORT / "plan.json").read_text())
    mapping = next(r["mapping"] for r in cohort["records"] if r["path"] == item["path"])
    entries = restored.pop("evidence")
    assert len(entries) == 2 and entries[0]["reference"] == ref
    assert entries[1]["reference"] == cohort["mapping_source"]["reference"]
    assert (
        entries[1]["snippet"] == mapping["snippet"] and "Identity only" in entries[1]["explanation"]
    )
    refs = restored.pop("references")
    assert [r["reference"] for r in refs] == [e["reference"] for e in entries]
    assert refs[1]["title"] == "KOMODO - the Known Media Database"
    for r in refs:
        assert "source_type=" in r["notes"] and "discovery_mode=cross_reference" in r["notes"]
        assert "authors" not in r and "year" not in r
    assert restored["notes"].startswith(before["notes"] + "\n\nConcentration follow-up:")
    assert "not revalidated" in restored["notes"]
    restored["notes"] = before["notes"]
    restored.pop("preparation_steps")
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert all(c["field"] in event["changes"] for c in item["claims"])
    assert restored == before, "Unreviewed change outside the explicit inversion"
    counts["preparation_records_restored"] += 1
    return counts


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--applied", action="store_true")
    p.add_argument("--out", type=Path, required=True)
    args = p.parse_args()
    assert not args.out.exists()
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        before, after = [yaml.safe_load(item[k]) for k in ("before_text", "after_text")]
        current = (ROOT / item["path"]).read_bytes()
        assert (
            hashlib.sha256(current).hexdigest()
            == item["after_sha256" if args.applied else "before_sha256"]
        )
        assert hashlib.sha256(item["after_text"].encode()).hexdigest() == item["after_sha256"]
        counts.update(check(before, after, item))
    result = {
        "records": len(plan["records"]),
        "applied": args.applied,
        "counts": dict(counts),
        "complete_record_inversion": True,
        "all_claim_excerpts_match": True,
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
