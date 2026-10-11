"""Independent source arithmetic, provenance coverage and semantic inversion."""

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


def get(node, pointer):
    for part in pointer:
        node = node[part]
    return node


def evidence(node):
    entries = []
    if isinstance(node, dict):
        local = node.get("evidence", [])
        assert len({e["reference"] for e in local}) == len(local)
        entries.extend(local)
        for key, value in node.items():
            if key != "evidence":
                entries.extend(evidence(value))
    elif isinstance(node, list):
        for value in node:
            entries.extend(evidence(value))
    return entries


def check(before, after, item):
    raw = (HERE / "inspected-context.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "86dff028638962f3766ee4b97586df8bcab635b831e9a1fb2423b7b43ca2c536"
    )
    context = json.loads(raw)
    captured = {s["metadata"]["url"]: s for s in context["sources"].values()}
    for source in captured.values():
        meta = source["metadata"]
        assert meta["url"] == meta["response_url"] and meta["http_status"] == 200
        assert hashlib.sha256(source["raw"].encode(meta["encoding"])).hexdigest() == meta["sha256"]
    assert "Nothing found." in context["sources"]["original"]["raw"]
    key, togo = item["key"], item["key"].startswith("M")
    standalone = key == "solution"
    field = "composition" if standalone else "ingredients"
    source = context["sources"][key]
    data = json.loads(source["raw"])
    if togo:
        rows = data["components"][0]["items"]
        step = data["comments"][0]["comment"]
        names = [r["component_name"] for r in rows]
        amounts = [r["volume"] for r in rows]
    else:
        body = data["data"] if standalone else data["data"]["solutions"][0]
        rows, step = body["recipe"], body["steps"][0]["step"]
        names = [r["compound"] for r in rows]
        amounts = [r["amount"] for r in rows]
        assert body.get("volume") is None
        assert all(r.get("g_l") is None and r["unit"] == "g" for r in rows)
    assert "bring volume to 500.0 ml." in step
    assert "remaining components in 500 ml distilled water" in step
    assert "Autoclave the two solutions separately and combine them after autoclaving." in step
    assert [n["preferred_term"] for n in before[field]] == names
    assert after[field] == [] and len(after["solutions"]) == 2
    magnesium, base = after["solutions"]
    assert len(magnesium["composition"]) == 2
    assert magnesium["preparation_notes"] == step.split(" Separately")[0]
    assert (
        base["preparation_notes"]
        == "Separately" + step.split(" Separately")[1].split(" Autoclave")[0]
    )
    for stock in after["solutions"]:
        assert set(stock) == {"preferred_term", "composition", "notes", "preparation_notes"}
        assert "no numeric" in stock["notes"]
    assert "actual volume added after autoclaving is unreported" in magnesium["notes"]
    assert "not a 500 ml final solution volume" in base["notes"]
    assert magnesium["preferred_term"] == "JCM973 magnesium chloride preparation"
    assert base["preferred_term"] == "JCM973 remaining-components preparation"
    assert not evidence(before)
    entries = evidence(after)
    assert len(entries) == (12 if key == "M1024" else 11)
    for e in entries:
        assert e["reference"] in captured and e["supports"] == "SUPPORT"
        assert e["snippet"] and e["snippet"] in captured[e["reference"]]["raw"]
        assert e["explanation"] and "Nothing found." in e["explanation"]
    assert len({tuple(c["pointer"]) for c in item["claims"]}) == len(item["claims"])
    expected_claims = len(before[field]) + 4 + standalone
    assert len(item["claims"]) == expected_claims
    for c in item["claims"]:
        actual = get(after, c["pointer"][:-1]).get(c["pointer"][-1])
        assert actual == c["new"]
        if c["old_pointer"]:
            assert get(before, c["old_pointer"]) == c["old"]
        if c["status"] == "unsupported":
            assert standalone and c["pointer"] == ["ingredients", 0, "concentration"]
            assert c["old"] == c["new"]
            continue
        assert c["reference"] == source["metadata"]["url"]
        assert c["snippet"] in source["raw"] and c["snippet"]
        matching = [
            e
            for e in get(after, c["evidence_pointer"])["evidence"]
            if e["reference"] == c["reference"]
        ]
        assert len(matching) == 1
        e = matching[0]
        assert c["explanation"] in e["explanation"] and c["field"] in e["explanation"]
        assert c["snippet"] == e["snippet"] or c["snippet"] in e["explanation"]
    counts = collections.Counter(
        new_evidence=len(entries),
        new_references=2,
        new_curation_history=1,
        stock_descriptors_added=2,
    )
    restored = []
    for i, old in enumerate(before[field]):
        matches = [c for c in item["claims"] if c["old_pointer"] == [field, i, "concentration"]]
        assert len(matches) == 1
        claim = matches[0]
        node = copy.deepcopy(get(after, claim["pointer"][:-1]))
        assert node["preferred_term"] == names[i]
        amount = Decimal(str(amounts[i]))
        if togo and i == 0:
            assert claim["pointer"] == ["solutions", 1, "composition", 0, "concentration"]
            assert node["concentration"] == {"value": "0.5", "unit": "L"}
            assert "Source input for the remaining-components" in node["notes"]
            counts["quantity_corrections"] += 1
        else:
            quoted = (
                json.loads("{" + claim["snippet"].rstrip().removesuffix(",") + "}")
                if togo
                else json.loads(claim["snippet"])
            )
            assert quoted == (
                {k: rows[i][k] for k in ["component_name", "volume", "unit"]} if togo else rows[i]
            )
            assert step in claim["explanation"]
            if i == (3 if togo else 1):
                assert claim["pointer"] == ["solutions", 0, "composition", 0, "concentration"]
                assert "6H2O" in names[i] or "6 H2O" in names[i]
                assert node["concentration"]["unit"] == "G_PER_L"
                assert Decimal(node["concentration"]["value"]) == amount / (Decimal("500.0") / 1000)
                assert (
                    "before autoclaving" in node["notes"]
                    and "No final-medium concentration" in node["notes"]
                )
                counts["stock_stage_concentrations_rebased"] += 1
            else:
                assert claim["pointer"][:2] == ["solutions", 1]
                assert "concentration" not in node
                assert (
                    f"Source amount: {amounts[i]} g per remaining-components recipe batch, not per liter."
                    in node["notes"]
                )
                assert "final mixed-medium volume is unreported" in node["notes"]
                counts["unsupported_quantity_slots_removed"] += 1
        if "notes" in old:
            assert node["notes"].startswith(old["notes"] + "\n\n")
            node["notes"] = old["notes"]
        else:
            node.pop("notes")
        node["concentration"] = copy.deepcopy(old["concentration"])
        node.pop("evidence")
        assert node == old, "Ingredient identity or unrelated field changed"
        restored.append(node)
        counts["stock_nodes_relocated"] += 1
    water = magnesium["composition"][1]
    assert set(water) == {"preferred_term", "notes", "evidence"}
    assert water["preferred_term"] == "Distilled water"
    assert "not 500 ml of water input" in water["notes"]
    assert "water amount remains unquantified" in water["notes"]
    assert len(base["composition"]) == len(before[field]) - (1 if togo else 0)
    if not togo:
        water = base["composition"][0]
        assert set(water) == {"preferred_term", "concentration", "notes", "evidence"}
        assert water["preferred_term"] == "Distilled water"
        assert water["concentration"] == {"value": "0.5", "unit": "L"}
        counts["new_quantity_slots"] += 1
    recovered = copy.deepcopy(after)
    recovered[field] = restored
    del recovered["solutions"]
    if standalone:
        assert set(recovered["source_data"]) == {"origin", "evidence"}
        assert recovered["source_data"]["origin"] == "MediaDive"
        del recovered["source_data"]
    else:
        del recovered["evidence"]
    if togo:
        assert recovered.pop("preparation_steps") == [
            {"step_number": 1, "action": "AUTOCLAVE", "description": step}
        ]
    refs = recovered.pop("references")
    other = "medium" if togo else "M1023"
    assert [r["reference"] for r in refs] == [
        context["sources"][k]["metadata"]["url"] for k in (key, other)
    ]
    for r in refs:
        assert set(r) == {"reference", "title", "notes"}
        assert (
            "source_type=dataset" in r["notes"]
            and "discovery_mode=existing_record_reference" in r["notes"]
        )
        assert (
            "accessed_on=2026-10-08" in r["notes"]
            and "Authors and publication year not supplied" in r["notes"]
        )
        body = json.loads(captured[r["reference"]]["raw"])
        title = (
            body["meta"]["name"]
            if "meta" in body
            else body["data"].get("medium", body["data"])["name"]
        )
        assert r["title"] == title
    event = recovered["curation_history"].pop()
    assert event["curator"] == "codex" and event["action"] == item["action"]
    assert all(c["field"] in event["changes"] for c in item["claims"])
    assert recovered == before, "Unreviewed semantic edit"
    return counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        before, after = [
            yaml.load(item[k + "_text"], Loader=yaml.CSafeLoader) for k in ("before", "after")
        ]
        expected = item["after_sha256"] if args.applied else item["before_sha256"]
        assert hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest() == expected
        counts.update(check(before, after, item))
    result = {
        "terminal": True,
        "applied": args.applied,
        "records_changed": 4,
        "counts": dict(counts),
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
