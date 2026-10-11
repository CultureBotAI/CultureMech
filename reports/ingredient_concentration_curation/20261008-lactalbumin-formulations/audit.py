"""Independent source, amount, lineage and evidence audit; no mutator import."""

import argparse
import collections
import hashlib
import json
import re
from decimal import Decimal
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SHA = "b9afaadd95d0d21b285ebbde79b8a685f6fc18f6ecfb51b9cd2e86b2dcf8d8f2"
ACTION = "RESTORED_SOURCE_SPECIFIC_HYDROLYSATE_FORMULATIONS_WITH_EVIDENCE"


def get(node, path):
    for part in path:
        node = node[part]
    return node


def walk(node, path=()):
    if isinstance(node, dict):
        yield path, node
        for key, value in node.items():
            yield from walk(value, path + (key,))
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from walk(value, path + (i,))


def field(path):
    return "".join(f"[{p}]" if isinstance(p, int) else "." + p for p in path).lstrip(".")


def number(value):
    return format(Decimal(str(value)).normalize(), "f")


def check(before, after, item):
    raw = (HERE / "context.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    context = json.loads(raw)
    key = item["key"]
    spec = next(r for r in context["records"] if r["id"] == before["id"])
    assert before == yaml.safe_load(spec["before_text"])
    assert item["path"] == spec["path"] and item["action"] == ACTION
    data, texts, titles = {}, {}, {}
    for source, capture in context["sources"].items():
        text, meta = capture["raw"], capture["metadata"]
        assert (
            hashlib.sha256(text.encode(meta.get("encoding", "utf-8"))).hexdigest() == meta["sha256"]
        )
        assert meta["url"] == meta["response_url"] and meta["http_status"] == 200
        if source.startswith("K"):
            soup = BeautifulSoup(text, "html.parser")
            titles[source] = soup.title.get_text(strip=True)
            for tag in soup(["script", "style", "noscript", "template"]):
                tag.decompose()
            texts[source] = " ".join(soup.get_text(" ").split())
            tables = soup.find_all("table")
            rows = [
                [c.get_text(strip=True) for c in r.find_all("td")] for r in tables[2].find_all("tr")
            ][1:]
            assert len(rows) == len({r[0] for r in rows})
            data[source] = {r[0]: r for r in rows}
            assert f"ID: {source[1:]} Name:" in texts[source]
            assert "Gram & Mol amounts are per Liter of medium." in texts[source]
        elif source == "DSMZ1021":
            texts[source] = text
            titles[source] = text.splitlines()[0]
            assert titles[source] == "1021. SODALIS GLOSSINIDIUS MEDIUM"
        else:
            texts[source], data[source] = text, json.loads(text)
            titles[source] = (
                data[source]["meta"]["name"]
                if source == "M2287"
                else data[source]["data"]["medium"]["name"]
            )
    expected, descriptors = {}, {}

    def add(p, old, source, sp, kind, label, quantity):
        assert p not in expected
        expected[p] = (old, source, sp, kind, label, quantity)

    if key == "D1021":
        assert after["ingredients"] == [] and len(after["solutions"]) == 2
        assert "ph_value" not in after
        assert len(after["solutions"][0]["solutions"]) == 2
        ss = data[key]["data"]["solutions"]
        assert [s["id"] for s in ss] == [2073, 2074, 2075]
        descriptors[("solutions", 0)] = ("Combined basal preparation (Solutions A and B)", None)
        descriptors[("solutions", 1)] = ("Sterile foetal or newborn calf serum", None)
        for si, old_indices in ((1, [0, None, 4, 5, 6, 7, 8, 9, 10, None]), (2, [11, None])):
            p = ("solutions", 0, "solutions", si - 1)
            descriptors[p] = (
                ss[si]["name"],
                {
                    "value": number(Decimal(str(ss[0]["recipe"][si - 1]["amount"])) / 1000),
                    "unit": "L",
                },
            )
            assert len(get(after, p)["composition"]) == len(old_indices)
            original = (
                texts["DSMZ1021"]
                .split("Solution A:" if si == 1 else "Solution B:")[1]
                .split("Adjust pH" if si == 1 else "Sterilize solution")[0]
            )
            for ri, old in enumerate(old_indices):
                row = ss[si]["recipe"][ri]
                water = row["compound"] == "Distilled water"
                q = {
                    "value": number(Decimal(str(row["amount"])) / 1000 if water else row["g_l"]),
                    "unit": "L" if water else "G_PER_L",
                }
                add(
                    p + ("composition", ri),
                    old,
                    key,
                    ["data", "solutions", si, "recipe", ri],
                    "water" if water else "stock_rate",
                    row["compound"],
                    q,
                )
                pattern = (
                    "Lactalbumin hydrolysate or\\s+Casein hydrolysate"
                    if row["compound"] == "Lactalbumin hydrolysate"
                    else re.escape(row["compound"])
                )
                m = re.search(pattern + r"\s+([0-9.]+)\s+(g|ml)", original)
                assert m and Decimal(m[1]) == Decimal(str(row["amount"])) and m[2] == row["unit"]
            if si == 1:
                assert (
                    "pH 8.0" in get(after, p)["preparation_notes"]
                    and "titrant and amount are not specified" in get(after, p)["preparation_notes"]
                )
        assert "4 parts base to 1 part serum" in after["solutions"][0]["notes"]
        assert "Add 1 part to 4 parts" in after["solutions"][1]["notes"]
        assert len(after["variants"]) == 2
        variant = after["variants"][1]
        assert variant["relationship"] == "SUBSTITUTED_COMPONENT_VARIANT"
        assert "8.10 g casein hydrolysate, not both together" in variant["modifications"][0]
    elif key.startswith("K"):
        names = [
            "Yeast extract",
            "D-Glucose",
            "KCl",
            "MgCl2 x 6 H2O",
            "CaCl2 x 2 H2O",
            "NaCl",
            "NaHCO3",
            "Agar",
            "NaH2PO4 x 2 H2O",
            "casein hydrolysate",
            "Distilled water",
            "new borne calf serum",
        ]
        old_indices = [0, 4, 5, 6, 7, 8, 9, 10, 11, None, None, None]
        if key == "K1021_16929":
            names += ["O2", "N2", "CO2"]
            old_indices += [None] * 3
            assert "ph_value" not in after and "PH Info: null" in texts[key]
        else:
            assert after["ph_value"] == 8.0 and "PH Info: 8.0" in texts[key]
        assert set(names) == set(data[key]) and len(after["ingredients"]) == len(names)
        assert after["solutions"] == [] and len(after["variants"]) == 1
        for i, (name, old) in enumerate(zip(names, old_indices, strict=True)):
            row = data[key][name]
            unknown = name in {"Distilled water", "new borne calf serum", "O2", "N2", "CO2"}
            q = None if unknown else {"value": row[3], "unit": "G_PER_L"}
            add(
                ("ingredients", i),
                old,
                key,
                ["rows", name],
                "unquantified" if unknown else "medium_rate",
                name,
                q,
            )
            if unknown and name != "new borne calf serum":
                assert row[3:] == ["null", "null"]
                assert "unknown, not zero" in after["ingredients"][i]["notes"]
            elif name == "new borne calf serum":
                assert row[3:] == ["200.00", "0.20"]
                assert "do not establish density" in after["ingredients"][i]["notes"]
            else:
                assert (
                    "not the previously copied DSMZ stock rate" in after["ingredients"][i]["notes"]
                )
    else:
        assert key == "M2287"
        assert len(after["ingredients"]) == 1 and len(after["solutions"]) == 1
        assert "ph_value" not in after and "variants" not in after
        descriptors[("solutions", 0)] = ("Mitsuhashi-Maramorosch basal medium", None)
        assert "before supplementation" in after["solutions"][0]["notes"]
        assert len(after["solutions"][0]["composition"]) == 10
        items = data[key]["components"][0]["items"]
        assert (
            len(items) == 11
            and "supplemented with 5% heat-inactivated fetal bovine serum"
            in data[key]["comments"][0]["comment"]
        )
        for ri, row in enumerate(items):
            p = (
                ("ingredients", 0)
                if ri == 9
                else ("solutions", 0, "composition", 9 if ri == 10 else ri)
            )
            q = (
                None
                if ri == 9
                else {
                    "value": number(row["volume"]),
                    "unit": {"L": "L", "g/L": "G_PER_L", "mM": "MILLIMOLAR"}[row["unit"]],
                }
            )
            add(
                p,
                ri if ri < 10 else None,
                key,
                ["components", 0, "items", ri],
                "unknown_percent" if ri == 9 else "water" if ri == 0 else "basal_rate",
                row["component_name"],
                q,
            )
        assert "no w/v, v/v or w/w basis" in after["ingredients"][0]["notes"]
        assert "1 L water input, not 1 g/L" in after["solutions"][0]["composition"][0]["notes"]
    actual_nodes = {
        p: n
        for p, n in walk(after)
        if p[-2:-1] in {("ingredients",), ("composition",), ("solutions",)}
    }
    assert actual_nodes.keys() == expected.keys() | descriptors.keys()
    stats, mapped, lineage = collections.Counter(), set(), []
    for p, (old_index, source, sp, kind, label, quantity) in expected.items():
        node = get(after, p)
        op = ("ingredients", old_index) if old_index is not None else None
        old = get(before, op) if op else {}
        assert node.get("concentration") == quantity
        assert ("concentration" in node) == (quantity is not None)
        mutable = {"concentration", "notes", "evidence"}
        assert {k: v for k, v in node.items() if k not in mutable} == (
            {k: v for k, v in old.items() if k not in mutable} if op else {"preferred_term": label}
        )
        assert node["preferred_term"] == label and not node.get("supplier_catalog")
        if op:
            assert op not in mapped
            mapped.add(op)
            if old.get("notes"):
                assert node["notes"].startswith(old["notes"] + "\n\n")
            if p[0] == "solutions":
                stats["stock_nodes_relocated"] += 1
        if quantity:
            stats["quantity_corrections" if old.get("concentration") else "new_quantity_slots"] += (
                old.get("concentration") != quantity
            )
        elif old.get("concentration"):
            stats["unsupported_quantity_slots_removed"] += 1
        if kind == "stock_rate":
            row = get(data[source], sp)
            assert f"Source batch input: {row['amount']} {row['unit']}" in node["notes"]
            assert "API-reported stock rate, not a final-medium concentration" in node["notes"]
        lineage.append(
            {
                "pointer": list(p),
                "old_pointer": list(op) if op else None,
                "source": source,
                "source_pointer": sp,
                "kind": kind,
            }
        )
    assert sorted(lineage, key=lambda r: field(r["pointer"])) == sorted(
        item["lineage"], key=lambda r: field(r["pointer"])
    )
    for p, (label, q) in descriptors.items():
        node = get(after, p)
        assert node["preferred_term"] == label and node.get("concentration") == q
        assert ("concentration" in node) == (q is not None)
        assert set(node) <= {
            "preferred_term",
            "concentration",
            "composition",
            "solutions",
            "notes",
            "preparation_notes",
        }
        stats["stock_descriptors_added"] += 1
        stats["new_quantity_slots"] += q is not None
    removed = {("ingredients", i) for i in ((10, 11, 12) if key == "M2287" else (1, 2, 3))}
    assert mapped | removed == {("ingredients", i) for i in range(len(before["ingredients"]))}
    stats["unsupported_quantity_slots_removed"] += 3
    if key != "M2287":
        assert [s["action"] for s in after["preparation_steps"]] == [
            "ADJUST_PH",
            "AUTOCLAVE",
            "COOL",
            "MIX",
        ]
        descriptions = [s["description"] for s in after["preparation_steps"]]
        assert (
            "Solution A to pH 8.0" in descriptions[0]
            and "not a measured final-medium pH" in descriptions[0]
        )
        assert (
            "separately at 121 C for 20 min" in descriptions[1]
            and "Do not autoclave the serum" in descriptions[1]
        )
        assert (
            "50 C, then combine" in descriptions[2]
            and "4 parts" in descriptions[3]
            and "1 part" in descriptions[3]
        )
        v = after["variants"][0]
        assert v["relationship"] == "PHYSICAL_STATE_VARIANT"
        assert (
            "No membrane pore size" in v["modifications"][0]
            and "no numeric agar amount" in v["modifications"][1]
        )
        expected_links = (
            [(("variant_children", 0), "DERIVED_FROM")]
            if key == "D1021"
            else (
                [
                    (("parent_media",), "DERIVED_FROM"),
                    (("variant_children", 0), "STRAIN_SPECIFIC_VARIANT"),
                ]
                if key == "K1021"
                else [(("parent_media",), "STRAIN_SPECIFIC_VARIANT")]
            )
        )
        for p, relation in expected_links:
            a, b = get(after, p), get(before, p)
            assert a["relationship"] == relation
            assert {
                k: v for k, v in a.items() if k not in {"relationship", "notes", "evidence"}
            } == {k: v for k, v in b.items() if k not in {"relationship", "notes", "evidence"}}
            stats[
                "parent_links_corrected" if p[0] == "parent_media" else "child_links_corrected"
            ] += 1
        if key.startswith("K"):
            assert after["variant_relationship"] == after["parent_media"]["relationship"]
            assert after["variant_modifications"] == [after["parent_media"]["notes"]]
    marker = "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product:"
    assert marker in after["notes"] and after["notes"].replace(
        marker, "\n\nCommercial Product:", 1
    ).startswith(before["notes"] + "\n\n")
    allowed = {
        "ingredients",
        "solutions",
        "notes",
        "preparation_steps",
        "evidence",
        "references",
        "curation_history",
        "variants",
        "ph_value",
        "variant_children",
        "parent_media",
        "variant_relationship",
        "variant_modifications",
    }
    assert {k: v for k, v in before.items() if k not in allowed} == {
        k: v for k, v in after.items() if k not in allowed
    }
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["curator"] == "codex" and event["action"] == ACTION
    assert json.loads(event["changes"]) == [
        {k: c[k] for k in ("old_field", "field", "old", "new", "status", "reference", "snippet")}
        for c in item["claims"]
    ]
    old_slots = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    new_slots = {p + ("concentration",) for p, n in walk(after) if "concentration" in n}
    assert {
        tuple(c["old_pointer"])
        for c in item["claims"]
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    } == old_slots
    assert new_slots <= {tuple(c["pointer"]) for c in item["claims"]}
    assert {
        tuple(c["old_pointer"][:-1]) for c in item["claims"] if c["kind"] == "false_lb_removed"
    } == removed
    attached = {}
    for claim in item["claims"]:
        p, op, source = claim["pointer"], claim["old_pointer"], claim["source"]
        meta = context["sources"][source]["metadata"]
        assert claim["old"] == (get(before, op[:-1]).get(op[-1]) if op else None)
        assert claim["new"] == get(after, p[:-1]).get(p[-1])
        assert claim["field"] == field(p) and claim["old_field"] == (field(op) if op else None)
        assert (
            claim["reference"] == meta["url"]
            and claim["snippet"]
            and claim["snippet"] in texts[source]
        )
        assert field(p) in claim["explanation"] and meta["sha256"] in claim["explanation"]
        ep = claim["evidence_pointer"]
        assert ep is not None
        identity = (tuple(ep), claim["reference"])
        if identity in attached:
            attached[identity]["explanation"] += (
                "\n\nAdditional exact excerpt: " + claim["snippet"] + "\n" + claim["explanation"]
            )
        else:
            attached[identity] = {
                "reference": claim["reference"],
                "supports": "SUPPORT",
                "snippet": claim["snippet"],
                "explanation": claim["explanation"],
            }
    actual = {(p, e["reference"]): e for p, n in walk(after) for e in n.get("evidence", [])}
    assert actual == attached and len(actual) == sum(
        len(n.get("evidence", [])) for p, n in walk(after)
    )
    assert {r["reference"] for r in after["references"]} == {ref for p, ref in attached}
    assert len(after["references"]) == len({r["reference"] for r in after["references"]})
    for ref in after["references"]:
        source = next(
            k for k, c in context["sources"].items() if c["metadata"]["url"] == ref["reference"]
        )
        assert set(ref) == {"reference", "title", "notes"} and ref["title"] == titles[source]
        assert all(
            s in ref["notes"]
            for s in (
                "source_type=",
                "discovery_mode=",
                "accessed_on=",
                "capture_sha256=",
                "Authors and publication year are not supplied",
            )
        )
    assert len(item["claims"]) == {"D1021": 53, "K1021": 52, "K1021_16929": 59, "M2287": 37}[key]
    stats.update(
        new_evidence=len(actual),
        new_references=len(after["references"]),
        new_curation_history=1,
        old_quantity_slots=len(old_slots),
        claims=len(item["claims"]),
        source_rows=len(expected),
        preparation_steps_added=len(after.get("preparation_steps", [])),
        inline_variant_options_added=len(after.get("variants", [])),
    )
    return dict(stats)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--applied", action="store_true")
    args = parser.parse_args()
    plan = json.loads((HERE / "plan.json").read_text())
    results = {}
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes() if args.applied else item["after_text"].encode()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        results[item["key"]] = check(yaml.safe_load(item["before_text"]), yaml.safe_load(raw), item)
    output = HERE / ("applied-audit.json" if args.applied else "preview-audit.json")
    assert not output.exists()
    output.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results))


if __name__ == "__main__":
    main()
