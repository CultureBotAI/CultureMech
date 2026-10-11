"""Independent Middlebrook scope, amount, provenance and edit-coverage audit."""

import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SHA = "4836291dddb141d452fc5c01b0730d3badce0759dd54a8e7ba0446e7aff478d7"
ACTION = "RESTORED_MIDDLEBROOK_INGREDIENT_AND_STOCK_SCOPES_WITH_EVIDENCE"


def get(node, path):
    for part in path:
        node = node[part]
    return node


def walk(node, path=()):
    if isinstance(node, dict):
        yield path, node
        for k, v in node.items():
            yield from walk(v, path + (k,))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, path + (i,))


def norm(name):
    return name.strip().strip("*").strip().lower()


def num(v):
    return format(Decimal(str(v)).normalize(), "f")


def check(before, after, item):
    raw = (HERE / "context.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    context = json.loads(raw)
    key = item["key"]
    spec = next(r for r in context["records"] if r["key"] == key)
    assert before == yaml.safe_load(spec["before_text"])
    assert item["path"] == spec["path"] and item["action"] == ACTION
    assert before["id"] == after["id"] == spec["id"]
    texts, data = {}, {}
    for source, capture in context["sources"].items():
        text, meta = capture["raw"], capture["metadata"]
        assert (
            hashlib.sha256(text.encode(meta.get("encoding", "utf-8"))).hexdigest() == meta["sha256"]
        )
        assert meta["url"] == meta["response_url"] and meta["http_status"] == 200
        if source == "NBRC1219":
            soup = BeautifulSoup(text, "html.parser")
            for tag in soup(["script", "style", "noscript", "template"]):
                tag.decompose()
            texts[source] = " ".join(soup.get_text(" ").split())
        else:
            texts[source] = text
            if source != "DSMZ857":
                data[source] = json.loads(text)
    expected = {}

    def add(p, name, q, sp, kind):
        assert p not in expected
        expected[p] = (name, q, tuple(sp), kind)

    if key.startswith("M"):
        source = data[key]
        assert source["meta"]["gm"] == "http://togomedium.org/medium/" + key
        groups = source["components"]
        roots = {0, 1} if key in {"M2400", "M2401"} else {0}
        named = {norm(g["subcomponent_name"]): i for i, g in enumerate(groups) if i not in roots}
        main, stock, visited = 0, 0, set(roots)

        def amount(r):
            value, unit = r["volume"], r["unit"]
            if unit in {"ml", "L"}:
                return {
                    "value": num(Decimal(str(value)) / (1000 if unit == "ml" else 1)),
                    "unit": "L",
                }, "batch_volume"
            if unit == "% (v/v)":
                return {"value": num(value), "unit": "PERCENT_V_V"}, "explicit_percent"
            assert unit in {"%", "g", "mg"}
            return None, "unknown_percent_basis" if unit == "%" else "batch_mass"

        for ci in sorted(roots):
            for ri, row in enumerate(groups[ci]["items"]):
                q, kind = amount(row)
                if row.get("reference_media_id"):
                    assert row["reference_media_id"] == key
                    si = named[norm(row["component_name"])]
                    assert si not in visited
                    visited.add(si)
                    p = ("solutions", stock)
                    stock += 1
                    add(
                        p,
                        row["component_name"],
                        q,
                        ["components", ci, "items", ri],
                        "base_detail" if row["unit"] in {"g", "mg"} else "stock_dose",
                    )
                    assert len(get(after, p)["composition"]) == len(groups[si]["items"])
                    for j, component in enumerate(groups[si]["items"]):
                        cq, ck = amount(component)
                        add(
                            p + ("composition", j),
                            component["component_name"],
                            cq,
                            ["components", si, "items", j],
                            ck,
                        )
                else:
                    add(
                        ("ingredients", main),
                        row["component_name"],
                        q,
                        ["components", ci, "items", ri],
                        kind,
                    )
                    main += 1
        assert visited == set(range(len(groups)))
        assert len(after["ingredients"]) == main and len(after["solutions"]) == stock
        assert len(expected) == sum(len(g["items"]) for g in groups)
    else:
        assert key == "D857" and data[key]["data"]["medium"]["id"] == 857
        ss = data[key]["data"]["solutions"]
        assert len(after["ingredients"]) == 14 and len(after["solutions"]) == 1
        for i, row in enumerate(ss[0]["recipe"][:12]):
            add(
                ("ingredients", i),
                row["compound"],
                {"value": num(row["g_l"]), "unit": "G_PER_L"},
                ["data", "solutions", 0, "recipe", i],
                "final_rate",
            )
        for i, name, value in ((12, "Distilled water", "0.9"), (13, "Glycerol", "0.002")):
            add(
                ("ingredients", i),
                name,
                {"value": value, "unit": "L"},
                ["data", "solutions", 0, "steps", 1, "step"],
                "batch_volume",
            )
        add(
            ("solutions", 0),
            "ADC Enrichment",
            {"value": "0.1", "unit": "L"},
            ["data", "solutions", 0, "recipe", 13],
            "stock_dose",
        )
        assert len(after["solutions"][0]["composition"]) == 4
        for i, row in enumerate(ss[1]["recipe"]):
            water = i == 3
            q = (
                {"value": "0.1", "unit": "L"}
                if water
                else {"value": num(row["g_l"]), "unit": "G_PER_L"}
            )
            add(
                ("solutions", 0, "composition", i),
                row["compound"],
                q,
                ["data", "solutions", 1, "recipe", i],
                "batch_volume" if water else "provider_stock_rate",
            )
        assert (
            "0.0003" in texts["DSMZ857"]
            and "To prepare one liter of final medium" in texts["DSMZ857"]
        )
        assert after["preparation_steps"] == before["preparation_steps"]
        assert after["ph_range"] == {"min": 6.4, "max": 6.8}

    old_nodes, lb = {}, []
    for field in ("ingredients", "solutions"):
        for i, node in enumerate(before.get(field, [])):
            if "LB Medium" in node.get("supplier_catalog", {}).get("supplier_name", ""):
                lb.append((field, i))
            else:
                assert norm(node["preferred_term"]) not in old_nodes
                old_nodes[norm(node["preferred_term"])] = (field, i)
    assert len(lb) == 3
    lineage = {tuple(link["pointer"]): link for link in item["lineage"]}
    assert len(lineage) == len(item["lineage"]) and set(lineage) == set(expected)
    actual_nodes = {
        p
        for p, n in walk(after)
        if "preferred_term" in n and p and p[0] in {"ingredients", "solutions"}
    }
    assert actual_nodes == set(expected)
    concentration_claims = set()
    for p, (name, quantity, sp, kind) in expected.items():
        node = get(after, p)
        assert norm(node["preferred_term"]) == norm(name) and node.get("concentration") == quantity
        assert "LB Medium" not in node.get("supplier_catalog", {}).get("supplier_name", "")
        old = old_nodes.get(norm(name))
        assert lineage[p]["old_pointer"] == (
            list(old)
            if old
            else ([] if key == "D857" and p == ("solutions", 0, "composition", 3) else None)
        )
        assert (
            tuple(lineage[p]["source_pointer"]) == sp
            and lineage[p]["source"] == key
            and lineage[p]["kind"] == kind
        )
        if old:
            original = get(before, old)
            ignored = {"concentration", "notes", "name", "composition", "evidence"}
            assert {k: v for k, v in node.items() if k not in ignored} == {
                k: v for k, v in original.items() if k not in ignored
            }
            assert node.get("notes", "").startswith(original.get("notes", ""))
        else:
            assert not any(
                k in node for k in ("term", "supplier_catalog", "mediaingredientmech_chebi_term")
            )
        if key.startswith("M"):
            row = get(data[key], sp)
            assert f"Source amount: {row['volume']} {row['unit']}" in node["notes"]
            if quantity is None:
                assert (
                    "schema has no mass-only"
                    if row["unit"] in {"g", "mg"}
                    else "basis is unspecified"
                ) in node["notes"]
        if p[0] == "solutions" and len(p) == 2:
            assert node["name"] == node["preferred_term"] and "evidence" not in node
        concentration_claims.add(p + ("concentration",))

    claims = item["claims"]
    assert concentration_claims == {
        tuple(c["pointer"]) for c in claims if c["pointer"][-1] == "concentration"
    }
    old_quantities = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    assert old_quantities == {
        tuple(c["old_pointer"])
        for c in claims
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    }
    assert {tuple(c["old_pointer"][:-1]) for c in claims if c["kind"] == "false_lb_removed"} == set(
        lb
    )
    for p in expected:
        assert any(tuple(c["pointer"]) == p + ("notes",) for c in claims)
    for c in claims:
        p, old, source = c["pointer"], c["old_pointer"], c["source"]
        assert c["new"] == get(after, p[:-1]).get(p[-1])
        assert c["old"] == (get(before, old[:-1]).get(old[-1]) if old else None)
        assert c["snippet"] and c["snippet"] in texts[source]
        assert c["reference"] == context["sources"][source]["metadata"]["url"]
        assert c["evidence_pointer"] is not None
        entries = get(after, c["evidence_pointer"])["evidence"]
        matches = [e for e in entries if e["reference"] == c["reference"]]
        assert len(matches) == 1
        e = matches[0]
        assert (
            c["snippet"] == e["snippet"]
            or "Additional exact excerpt: " + c["snippet"] in e["explanation"]
        )
        assert c["explanation"] in e["explanation"]
    claimed = {(tuple(c["evidence_pointer"]), c["reference"]) for c in claims}
    actual_evidence = set()
    for p, n in walk(after):
        if "evidence" in n:
            assert len(n["evidence"]) == len({e["reference"] for e in n["evidence"]})
            for e in n["evidence"]:
                assert e["supports"] == "SUPPORT" and e["snippet"] and e["explanation"]
                source = next(
                    k
                    for k, v in context["sources"].items()
                    if v["metadata"]["url"] == e["reference"]
                )
                assert e["snippet"] in texts[source]
                actual_evidence.add((p, e["reference"]))
    assert actual_evidence == claimed
    assert {r["reference"] for r in after["references"]} == {c["reference"] for c in claims}
    for ref in after["references"]:
        assert "authors" not in ref and "year" not in ref
        source = next(
            k for k, v in context["sources"].items() if v["metadata"]["url"] == ref["reference"]
        )
        title = (
            "Catalogue Detail Medium | NITE - NBRC Culture Catalogue"
            if source == "NBRC1219"
            else (
                texts[source].splitlines()[0]
                if source == "DSMZ857"
                else (
                    data[source]["data"]["medium"]["name"]
                    if source == "D857"
                    else data[source]["meta"]["name"]
                )
            )
        )
        assert (
            ref["title"] == title
            and context["sources"][source]["metadata"]["sha256"] in ref["notes"]
        )
    assert "Superseded historical provenance (not a current formulation claim)" in after["notes"]
    if key == "M1946":
        assert "895 ml" in after["notes"] and "900 mL" in after["notes"]
    if key == "M2879":
        assert "Unresolved source conflict" in after["notes"] and "respectively" in after["notes"]
    if key == "M2402":
        assert "no agar row" in after["notes"]
    if key == "M2404":
        assert "ethanol retention" in after["notes"]
    allowed = {"ingredients", "solutions", "notes", "evidence", "references", "curation_history"}
    if key == "M2399":
        allowed.add("physical_state")
        assert after["physical_state"] == "SOLID_AGAR"
        assert any(c["pointer"] == ["physical_state"] for c in claims)
    assert {k: v for k, v in after.items() if k not in allowed} == {
        k: v for k, v in before.items() if k not in allowed
    }
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert json.loads(event["changes"]) == [
        {k: c[k] for k in ("old_field", "field", "old", "new", "status", "reference", "snippet")}
        for c in claims
    ]
    return {
        "source_nodes": len(expected),
        "old_quantity_slots": len(old_quantities),
        "claims": len(claims),
        "new_evidence": len(actual_evidence),
        "new_references": len(after["references"]),
        "new_curation_history": 1,
    }


if __name__ == "__main__":
    plan = json.loads((HERE / "plan.json").read_text())
    result = {}
    for item in plan["records"]:
        result[item["key"]] = check(
            yaml.safe_load(item["before_text"]), yaml.safe_load(item["after_text"]), item
        )
    print(json.dumps(result, indent=2))
