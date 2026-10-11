"""Independent source/basis checks and inversion of the permitted recipe edits."""

import argparse
import collections
import copy
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def get(node, pointer):
    for part in pointer:
        node = node[part]
    return node


def evidence(node):
    if isinstance(node, list):
        return [e for child in node for e in evidence(child)]
    if not isinstance(node, dict):
        return []
    local = node.get("evidence", [])
    assert len({e["reference"] for e in local}) == len(local)
    return local + [e for k, v in node.items() if k != "evidence" for e in evidence(v)]


def check(before, after, item):
    raw = (HERE / "inspected-context.json").read_bytes()
    assert (
        hashlib.sha256(raw).hexdigest()
        == "d0e73bcc4d7c33b87dd5dcf26115e244c2d90d72fc17e3bb66252674931580c5"
    )
    context = json.loads(raw)
    key = item["key"]
    spec = next(r for r in context["records"] if r["key"] == key)
    assert before == yaml.load(spec["before_text"], Loader=yaml.CSafeLoader)
    assert item["path"] == spec["path"] and item["id"] == spec["id"]
    captures, bodies = {}, {}
    for k, source in context["sources"].items():
        meta = source["metadata"]
        assert meta["url"] == meta["response_url"] and meta["http_status"] == 200
        assert hashlib.sha256(source["raw"].encode(meta["encoding"])).hexdigest() == meta["sha256"]
        text = (
            " ".join(BeautifulSoup(source["raw"], "html.parser").get_text().split())
            if k.startswith("JCM")
            else source["raw"]
        )
        captures[meta["url"]] = (k, source, text)
        bodies[k] = text if k.startswith("JCM") else json.loads(text)
    assert not evidence(before)
    entries = evidence(after)
    assert len(entries) == {"M1038": 10, "M1039": 5, "J986": 4}[key]
    for e in entries:
        assert e["supports"] == "SUPPORT" and e["snippet"]
        assert e["snippet"] in captures[e["reference"]][2]
        assert e["explanation"]
    for c in item["claims"]:
        assert c["snippet"] and c["snippet"] in captures[c["reference"]][2]
        if c["old_pointer"]:
            assert get(before, c["old_pointer"][:-1]).get(c["old_pointer"][-1]) == c["old"]
        if c["pointer"]:
            assert get(after, c["pointer"][:-1]).get(c["pointer"][-1]) == c["new"]
        else:
            assert key == "J986" and c["status"] == "replace_with_reference" and c["new"] is None
        if c["evidence_pointer"] is not None:
            matches = [
                e
                for e in get(after, c["evidence_pointer"])["evidence"]
                if e["reference"] == c["reference"]
            ]
            assert len(matches) == 1
            assert (
                c["explanation"] in matches[0]["explanation"]
                and c["field"] in matches[0]["explanation"]
            )
            assert (
                c["snippet"] == matches[0]["snippet"] or c["snippet"] in matches[0]["explanation"]
            )
        else:
            assert (
                c["status"] == "unsupported"
                and c["old"] == c["new"]
                or key == "J986"
                and c["field"] == "solutions[0].composition"
            )
    old_quantities = {
        tuple(c["old_pointer"])
        for c in item["claims"]
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    }
    assert old_quantities == {
        (field, i, "concentration")
        for field in ("ingredients", "solutions")
        for i, n in enumerate(before.get(field, []))
        if "concentration" in n
    }
    assert len(item["claims"]) == {"M1038": 27, "M1039": 9, "J986": 43}[key]
    counts = collections.Counter(
        new_evidence=len(entries), new_references=len(after["references"]), new_curation_history=1
    )
    recovered = copy.deepcopy(after)

    if key == "M1038":
        body = bodies[key]
        rows = body["components"][0]["items"]
        assert len(after["ingredients"]) == len(rows) == 10
        for i, (node, old, row) in enumerate(
            zip(recovered["ingredients"], before["ingredients"], rows, strict=True)
        ):
            assert node["preferred_term"] == row["component_name"]
            if i >= 8:
                assert node == old and "volume" not in row
                continue
            if i == 0:
                assert (
                    row["unit"] == "ml"
                    and Decimal(node["concentration"]["value"])
                    == Decimal(str(row["volume"])) / 1000
                )
                assert node["concentration"] == {"value": "0.96", "unit": "L"}
                assert "not final-medium volume" in node["notes"]
                counts["quantity_corrections"] += 1
            else:
                assert "concentration" not in node
                assert f"Source batch amount: {row['volume']} {row['unit']}." in node["notes"]
                assert "final-medium volume is unreported" in node["notes"]
                assert (row["volume"], row["unit"]) == (1, "mg") if i == 5 else row["unit"] == "g"
                counts["unsupported_quantity_slots_removed"] += 1
            assert node["notes"].startswith(old["notes"] + "\n\n")
            node["notes"] = old["notes"]
            node["concentration"] = old["concentration"]
            node.pop("evidence")
            assert node == old
        stock_rows = body["components"][1]["items"][:6] + body["components"][2]["items"]
        assert len(recovered["solutions"]) == 7
        for i, (node, old, row) in enumerate(
            zip(recovered["solutions"], before["solutions"], stock_rows, strict=True)
        ):
            assert row["unit"] == "ml" and node["preferred_term"] == row["component_name"]
            assert node["composition"] == []
            if i == 6:
                assert "Finally, add per liter" in body["comments"][1]["comment"]
                assert node["concentration"] == {"value": str(row["volume"]), "unit": "ML_PER_L"}
                assert "not an 8 ml batch input" in node["notes"]
            else:
                assert node["concentration"]["unit"] == "L"
                assert Decimal(node["concentration"]["value"]) == Decimal(str(row["volume"])) / 1000
                assert "not a dose per final liter" in node["notes"]
            if "conc_value" in row:
                assert "percentage basis is unspecified" in node["notes"]
            if i == 1:
                assert row["conc_value"] == 3
                assert bodies["J985"]["data"]["solutions"][0]["recipe"][12]["attribute"] == "*, 30%"
                assert (
                    "3%" in node["notes"]
                    and "30%" in node["notes"]
                    and "disagreement" in node["notes"]
                )
                assert "Nothing found." in bodies["JCM985"]
            assert node["notes"].startswith(old["notes"] + "\n\n")
            node["notes"], node["concentration"] = old["notes"], old["concentration"]
            assert node == old
            counts["quantity_corrections"] += 1
        assert recovered.pop("preparation_steps") == [
            {"step_number": i + 1, "action": a, "description": body["comments"][i]["comment"]}
            for i, a in enumerate(("AUTOCLAVE", "ALIQUOT"))
        ]
    else:
        original = bodies["JCM986"]
        assert "Use Medium No. 265 supplemented with 3.0 g/L trimethylamine\u00b7HCl" in original
        assert after["ingredients"][0]["concentration"] == {"value": "3", "unit": "G_PER_L"}
        assert len(after["solutions"]) == 1 and after["solutions"][0]["composition"] == []
        dep_key, identifier = (
            ("M257", "CultureMech:009148") if key == "M1039" else ("J265", "CultureMech:000295")
        )
        dep = next(d for d in context["dependencies"] if d["key"] == dep_key)
        base = yaml.load(dep["before_text"], Loader=yaml.CSafeLoader)
        assert base["id"] == identifier and base["name"] == "methanogenium_medium"
        assert after["solutions"][0]["culturemech_term"] == {
            "id": identifier,
            "label": base["name"],
        }
        assert "265 METHANOGENIUM MEDIUM" in bodies["JCM265"]
        if key == "M1039":
            assert bodies[key]["components"][0]["items"][0]["unit"] == "g/L"
            assert bodies[key]["components"][0]["items"][1]["reference_media_id"] == "M257"
            assert bodies["M257"]["meta"]["original_media_id"] == "JCM_M265"
            assert recovered["solutions"][0]["concentration"] == {"value": "1", "unit": "L"}
            assert (
                "not 1 g/L or a measured final-medium volume" in recovered["solutions"][0]["notes"]
            )
            assert recovered.pop("preparation_steps") == [
                {
                    "step_number": 1,
                    "action": "ADJUST_PH",
                    "description": bodies[key]["comments"][1]["comment"],
                }
            ]
            recovered["ingredients"][0].pop("evidence")
            for f in ("notes", "concentration"):
                if f == "notes":
                    assert recovered["solutions"][0][f].startswith(
                        before["solutions"][0][f] + "\n\n"
                    )
                recovered["solutions"][0][f] = before["solutions"][0][f]
            recovered["solutions"][0].pop("culturemech_term")
            counts["quantity_corrections"] += 1
        else:
            assert len(before["ingredients"]) == len(base["ingredients"]) == 37
            for node, origin in zip(before["ingredients"], base["ingredients"], strict=True):
                assert "Copied from" in node["notes"] and "265" in node["notes"]
                assert {k: v for k, v in node.items() if k != "notes"} == {
                    k: v for k, v in origin.items() if k != "notes"
                }
            assert len(recovered["ingredients"]) == 1
            node = copy.deepcopy(recovered["ingredients"][0])
            node.pop("evidence")
            assert node == {
                "preferred_term": "Trimethylamine hydrochloride",
                "concentration": {"value": "3", "unit": "G_PER_L"},
            }
            stock = recovered.pop("solutions")[0]
            assert set(stock) == {"preferred_term", "composition", "culturemech_term", "notes"}
            assert stock["preferred_term"] == "METHANOGENIUM MEDIUM (JCM 265)"
            assert (
                "base constituents are not excluded" in stock["notes"]
                and "inherited concentrations remain unverified" in stock["notes"]
            )
            assert "no numeric base working dose" in stock["notes"]
            assert not bodies["J986"]["data"]["solutions"][0].get("recipe")
            recovered["ingredients"] = copy.deepcopy(before["ingredients"])
            counts.update(
                unsupported_quantity_slots_removed=37,
                copied_ingredient_nodes_replaced_by_reference=37,
                new_quantity_slots=1,
                stock_descriptors_added=1,
            )
    refs = recovered.pop("references")
    assert len(refs) == {"M1038": 2, "M1039": 3, "J986": 3}[key]
    assert len({r["reference"] for r in refs}) == len(refs)
    assert {r["reference"] for r in refs} == {e["reference"] for e in entries}
    for r in refs:
        source_key, source, _ = captures[r["reference"]]
        body, meta = bodies[source_key], source["metadata"]
        expected_title = (
            "Medium data"
            if source_key.startswith("JCM")
            else (
                body["meta"]["name"]
                if source_key.startswith("M")
                else body["data"]["medium"]["name"]
            )
        )
        assert r["title"] == expected_title and set(r) == {"reference", "title", "notes"}
        assert "source_type=" in r["notes"] and "discovery_mode=" in r["notes"]
        assert (
            "accessed_on=" + meta["accessed_at"][:10] in r["notes"] and meta["sha256"] in r["notes"]
        )
        assert "Authors and publication year not supplied" in r["notes"]
    recovered.pop("evidence")
    event = recovered["curation_history"].pop()
    assert event["curator"] == "codex" and event["action"] == item["action"]
    assert all(c["field"] in event["changes"] for c in item["claims"])
    assert recovered == before, "Unreviewed semantic edit"
    return counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    assert not args.out.exists()
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        before, after = [
            yaml.load(item[k + "_text"], Loader=yaml.CSafeLoader) for k in ("before", "after")
        ]
        if args.applied:
            assert (ROOT / item["path"]).read_text() == item["after_text"]
        counts.update(check(before, after, item))
    result = {
        "terminal": True,
        "applied": args.applied,
        "records": len(plan["records"]),
        "counts": dict(counts),
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
