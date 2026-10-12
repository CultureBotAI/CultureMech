"""Independent source assertions and whole-record inversion for nine stock repairs."""

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
ACTION = "CORRECTED_DSMZ546_659_670_STOCK_STAGES"


def get(doc, pointer):
    for key in pointer:
        doc = doc[key]
    return doc


def provenance(node):
    out = collections.Counter()
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"evidence", "references", "curation_history"}:
                out["new_" + key] += len(value)
            else:
                out.update(provenance(value))
    elif isinstance(node, list):
        for child in node:
            out.update(provenance(child))
    return out


def check(before, after, item, sources=None):
    sources = sources or json.loads((HERE / "plan.json").read_text())["sources"]
    mid, kind = item["key"].split("-")
    solution = kind == "solution"
    field = "composition" if solution else "ingredients"
    capture = sources[item["key"]]
    raw, meta = capture["raw"], capture["metadata"]
    assert hashlib.sha256(raw.encode()).hexdigest() == meta["sha256"] == item["source_sha256"]
    sid = {"546": 1205, "659": 1390, "670": 1413}[mid]
    ref = "https://mediadive.dsmz.de/rest/" + (f"solution/{sid}" if solution else f"medium/{mid}")
    assert meta["url"] == meta["response_url"] == ref and meta["http_status"] == 200
    source = json.loads(raw)
    data = source["data"] if solution else source["data"]["solutions"][0]
    rows, steps = data["recipe"], [r["step"] for r in data["steps"]]
    assert data["id"] == sid and data["name"] == "Main sol. " + mid and data["volume"] == 1000
    assert before["id"] == after["id"] == item["id"] and item["action"] == ACTION
    assert hashlib.sha256(item["before_text"].encode()).hexdigest() == item["before_sha256"]
    if not solution:
        term = ("komodo.medium:" if kind == "komodo" else "mediadive.medium:") + mid
        assert before["media_term"]["term"]["id"] == term
        assert before["physical_state"] == after["physical_state"] == "LIQUID"
        assert source["data"]["medium"]["id"] == int(mid)
        assert source["data"]["medium"]["link"].endswith(f"DSMZ_Medium{mid}.pdf")
    else:
        assert before["term"]["id"] == f"mediadive.solution:{sid}"
        assert after["preparation_notes"] == before["preparation_notes"] == "\n".join(steps)
        assert "evidence" not in after
    assert len({tuple(c["pointer"]) for c in item["claims"]}) == len(item["claims"])
    for c in item["claims"]:
        assert c["old"] == (get(before, c["old_pointer"]) if c["old_pointer"] else None)
        assert c["new"] == get(after, c["pointer"])
        assert c["reference"] == ref and c["snippet"] in raw
        assert json.loads(c["snippet"]) == get(source, c["source_pointer"])
        entries = [
            e for e in get(after, c["evidence_pointer"])["evidence"] if e["reference"] == ref
        ]
        assert len(entries) == 1 and entries[0]["supports"] == "SUPPORT"
        e = entries[0]
        assert all(
            v in e["explanation"]
            for v in (
                c["field"],
                c["locator"],
                c["explanation"],
                meta["sha256"],
                meta["accessed_at"],
            )
        )
        assert c["snippet"] == e["snippet"] or c["snippet"] in e["explanation"]
        for q in c["extra_excerpts"]:
            assert (
                q["snippet"] in raw
                and q["snippet"] in e["explanation"]
                and q["locator"] in e["explanation"]
            )
    counts = provenance(after)
    counts.subtract(provenance(before))
    restored = copy.deepcopy(after)
    stocks = restored.pop("solutions")
    direct = {"546": 4, "659": 7, "670": 4}[mid]
    wi = {"546": 4, "659": 7, "670": 5}[mid]
    stock_indices = {"546": (5, 6), "659": (9,), "670": (4,)}[mid]
    indices = list(range(len(rows))) if solution else [i for i in range(len(rows)) if i != wi]
    by_source = {}
    for i in range(direct):
        node = restored[field][i]
        assert node["concentration"]["unit"] == "G_PER_L"
        assert (
            Decimal(node["concentration"]["value"])
            == Decimal(str(rows[i]["g_l"]))
            == Decimal(str(rows[i]["amount"]))
        )
        assert node["notes"] == (
            f"Source batch input: {rows[i]['amount']} {rows[i]['unit']}. Retained g/L is the provider-declared nominal main-recipe rate "
            "(volume field 1000 ml), not a separately prepared base or stock concentration, or an independently measured final-volume concentration."
        )
        by_source[i] = node
    if mid == "659":
        lactose = restored[field][7]
        assert lactose["concentration"] == {"value": "8", "unit": "G_PER_L"}
        assert (
            rows[8]["compound"] == "Lactose" and rows[8]["amount"] == 8 and rows[8]["unit"] == "g/l"
        )
        assert "up to a concentration of 8.0 g/l" in steps[0]
        assert (
            "after autoclaving" in lactose["notes"]
            and "8 g/L is not the stock concentration" in lactose["notes"]
        )
        by_source[8] = lactose
    water = restored[field][direct + (mid == "659")]
    assert (
        rows[wi]["compound"] == "Distilled water"
        and rows[wi]["compound_id"] == 4
        and rows[wi]["unit"] == "ml"
    )
    assert water["concentration"] == {
        "value": {"546": "0.99", "659": "1", "670": "0.95"}[mid],
        "unit": "L",
    }
    assert Decimal(water["concentration"]["value"]) == Decimal(str(rows[wi]["amount"])) / 1000
    assert (
        water["notes"]
        == "Distilled-water input to the base per recipe batch, not final medium volume or stock carrier volume."
    )
    if solution:
        by_source[wi] = water
        counts["quantity_corrections"] += 1
    else:
        assert set(water) == {"preferred_term", "term", "concentration", "notes", "evidence"}
        assert water["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
        counts["new_quantity_slots"] += 1
        counts["water_input_nodes_added"] += 1
    assert len(restored[field]) == direct + (mid == "659") + 1 + (mid == "670")
    assert len(stocks) == len(stock_indices)
    for stock, si in zip(stocks, stock_indices, strict=True):
        assert set(stock) == {"preferred_term", "composition", "concentration", "source", "notes"}
        assert stock["source"] == ref and rows[si]["unit"] == "ml"
        assert stock["concentration"]["unit"] == "L"
        assert Decimal(stock["concentration"]["value"]) == Decimal(str(rows[si]["amount"])) / 1000
        assert stock["notes"].startswith(
            f"{rows[si]['amount']} ml stock addition per recipe batch, not per liter"
        )
        node = stock["composition"][0]
        assert stock["preferred_term"] == node["preferred_term"] + " stock"
        assert node["concentration"] == (
            {"value": "40", "unit": "PERCENT_W_V"}
            if mid == "670"
            else {"value": "1", "unit": "MOLAR"}
        )
        assert "not a final-medium concentration" in node["notes"]
        if mid == "546":
            assert rows[si]["attribute"] == "1 M" and rows[si]["amount"] == 5
            assert "as sterile solutions" in steps[1]
        elif mid == "659":
            assert rows[si]["amount"] == 1.2 and "1.2 ml 1M CaCl2 x 2 H2O" in steps[0]
        else:
            assert rows[si]["attribute"] == "40% w/v in 0.2 N H2SO4" and rows[si]["amount"] == 50
            assert "filter-sterilized under 100% N2 gas atmosphere" in steps[0]
        assert len(stock["composition"]) == 1 + (mid == "670")
        by_source[si] = node
    counts.update(
        stock_nodes_relocated=len(stocks),
        stock_stage_concentrations_rebased=len(stocks),
        stock_descriptors_added=len(stocks),
        new_quantity_slots=len(stocks),
    )
    if mid == "670":
        carrier, acid = stocks[0]["composition"][1], restored[field][-1]
        for node in (carrier, acid):
            assert (
                set(node) == {"preferred_term", "notes", "evidence"}
                and node["preferred_term"] == "H2SO4"
            )
        assert "Stock carrier is 0.2 N H2SO4; carrier amount is unspecified" in carrier["notes"]
        assert (
            "Use 4 N H2SO4 to adjust the base to pH 2.2 before autoclaving; addition amount is not quantified"
            in acid["notes"]
        )
        assert "adjust pH to 2.2 with 4 N H2SO4" in steps[0]
        counts["unquantified_carrier_nodes_added"] += 2
    # Reconstruct every original node, allowing only the reviewed amount/context/evidence changes.
    restored[field] = []
    assert set(by_source) == set(indices)
    for old, si in zip(before[field], indices, strict=True):
        node = by_source[si]
        assert node["preferred_term"] == old["preferred_term"] == rows[si]["compound"]
        evidence = node.pop("evidence")
        assert (
            len(evidence) == 1 and evidence[0]["reference"] == ref and evidence[0]["snippet"] in raw
        )
        prior = old.get("evidence", [])
        if prior:
            assert len(prior) == 1
            assert all(evidence[0][k] == v for k, v in prior[0].items() if k != "explanation")
            assert evidence[0]["explanation"].endswith(
                "Historical explanation (retained with preparation scope clarified): "
                + prior[0]["explanation"]
            )
            node["evidence"] = copy.deepcopy(prior)
            counts["evidence_scopes_corrected"] += 1
        node.pop("notes")
        counts["ingredient_context_notes_added"] += 1
        node["concentration"] = copy.deepcopy(old["concentration"])
        assert node == old, "Unrelated ingredient identity/metadata changed"
        restored[field].append(node)
    if not solution:
        actions = {"546": ("ADJUST_PH", "HEAT"), "659": ("ADJUST_PH",), "670": ("DISSOLVE",)}[mid]
        assert restored["preparation_steps"] == [
            {"step_number": i + 1, "action": a, "description": steps[i]}
            for i, a in enumerate(actions)
        ]
        if "preparation_steps" in before:
            if mid == "670":
                counts.update(preparation_actions_corrected=1, preparation_steps_relocated=1)
            restored["preparation_steps"] = copy.deepcopy(before["preparation_steps"])
        else:
            counts["preparation_steps_added"] += len(restored.pop("preparation_steps"))
    expected_notes = (
        before.get("notes", "")
        + "\n\nStock follow-up: quantities distinguish base-water inputs, stock strengths and batch doses; no measured final volume or new growth claim is inferred. Existing chemical mappings and variant links are retained, not independently validated."
    ).lstrip()
    if mid == "670":
        expected_notes += (
            " "
            + steps[1]
            + " This correction covers the base formulation only; strain-specific alternatives require separate review."
        )
    assert restored["notes"] == expected_notes
    if "notes" in before:
        restored["notes"] = before["notes"]
    else:
        restored.pop("notes")
    if solution:
        container = restored.pop("source_data")
        assert set(container) == {"origin", "evidence"} and container["origin"] == "MediaDive"
        assert len(container["evidence"]) == 1
    else:
        entries = restored.pop("evidence")
        assert len(entries) == (2 if kind == "komodo" else 1)
        if kind == "komodo":
            mapping, mm = capture["mapping"], capture["mapping_metadata"]
            assert mapping["medium_id"] == mid and mapping["original_recipe"].endswith(
                f"DSMZ_Medium{mid}.pdf"
            )
            assert (
                entries[1]["reference"] == mm["reference"]
                and entries[1]["snippet"] == mapping["snippet"]
            )
            assert (
                mm["sha256"] in entries[1]["explanation"]
                and "identity only" in entries[1]["explanation"]
            )
            refs = restored.pop("references")
            assert [r["reference"] for r in refs] == [ref, mm["reference"]]
            assert (
                refs[0]["title"] == f"MediaDive medium {mid}: " + source["data"]["medium"]["name"]
            )
            assert refs[1]["title"] == "KOMODO - the Known Media Database"
            assert all(
                "source_type=dataset" in r["notes"]
                and "discovery_mode=cross_reference" in r["notes"]
                for r in refs
            )
    event = restored["curation_history"].pop()
    assert event["curator"] == "codex" and event["action"] == ACTION and event["source"] == ref
    for c in item["claims"]:
        assert c["field"] in event["changes"]
    assert not item["claim_resolutions"]
    assert restored == before, "Unrelated record fields/history changed"
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    plan = json.loads((HERE / "plan.json").read_text())
    total = collections.Counter()
    for item in plan["records"]:
        text = (ROOT / item["path"]).read_text() if args.applied else item["after_text"]
        assert hashlib.sha256(text.encode()).hexdigest() == item["after_sha256"]
        total.update(
            check(
                yaml.load(item["before_text"], Loader=yaml.CSafeLoader),
                yaml.load(text, Loader=yaml.CSafeLoader),
                item,
                plan["sources"],
            )
        )
    result = {
        "mode": "applied" if args.applied else "preview",
        "records": len(plan["records"]),
        "counts": dict(total),
    }
    if args.out:
        assert not args.out.exists(), "Refuse audit overwrite"
        args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
