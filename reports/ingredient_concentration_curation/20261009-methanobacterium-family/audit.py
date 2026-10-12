"""Independent medium-119 source projection and complete old-slot/evidence audit."""

import hashlib
import json
import re
from decimal import Decimal
from functools import cache
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from culturemech.validation.recipe_references import html_recipe_text, parse_recipe, recipe_source

HERE = Path(__file__).resolve().parent
SHA = "db28859fc6fde46c49576874f3697f1fe44dec82751da923d2aef04f84cd4573"
ACTION = "RESTORED_MEDIUM_119_SOURCE_FORMULATIONS_AND_STOCK_SCOPES_WITH_EVIDENCE"


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


def liters(value):
    return {"value": format((Decimal(str(value)) / 1000).normalize(), "f"), "unit": "L"}


@cache
def snapshot(raw):
    assert hashlib.sha256(raw).hexdigest() == SHA
    context = json.loads(raw)
    texts, titles, data = {}, {}, {}
    for key, capture in context["sources"].items():
        body, meta = capture["raw"], capture["metadata"]
        assert hashlib.sha256(body.encode()).hexdigest() == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        parsed = parse_recipe(recipe_source(meta["url"]), body, meta)
        texts[key], titles[key] = parsed.content, parsed.title
        if key.startswith("K"):
            tables = [
                t
                for t in BeautifulSoup(body, "html.parser").find_all("table")
                if "Gram Amount" in t.get_text()
            ]
            assert len(tables) == 1
            rows = [
                [html_recipe_text(str(c))[0] for c in tr.find_all("td", recursive=False)]
                for tr in tables[0].find_all("tr")
            ]
            assert rows[0] == [
                "Name",
                "Semi unique name",
                "Unique Name",
                "Gram Amount",
                "Mol Amount",
            ]
            assert all(len(row) == 5 for row in rows)
            data[key] = rows[1:]
        elif not key.startswith("DSMZ"):
            data[key] = json.loads(body)["data"]["solutions"]
    return context, texts, titles, data


def check(before, after, item):
    context, texts, titles, data = snapshot((HERE / "context.json").read_bytes())
    specs = {r["key"]: r for r in context["records"]}
    key, spec = item["key"], specs[item["key"]]
    assert before == yaml.load(spec["before_text"], Loader=yaml.CSafeLoader)
    assert before["id"] == after["id"] == spec["id"]
    assert item["path"] == spec["path"] and item["action"] == ACTION
    old, lb = {}, set()
    for i, node in enumerate(before["ingredients"]):
        if "LB Medium" in node.get("supplier_catalog", {}).get("supplier_name", ""):
            lb.add(("ingredients", i))
        else:
            label = node["preferred_term"].casefold()
            assert label not in old
            old[label] = ("ingredients", i)
    assert len(lb) == 3
    expected = {}
    renamed = {
        "Cysteine-HCl x H2O": "L-Cysteine HCl x H2O",
        "Resazurin": "Sodium resazurin",
        "sludge from an anaerobic digester": "Sludge",
    }

    def add(path, label, quantity, sp, kind, descriptor=False):
        assert path not in expected
        old_name = renamed.get(label, label) if key.startswith("K") else label
        expected[path] = {
            "label": label,
            "quantity": quantity,
            "source_pointer": sp,
            "kind": kind,
            "old_pointer": None if descriptor else old.get(old_name.casefold()),
            "descriptor": descriptor,
        }

    def component(path, row, si, ri):
        label, stage = row["compound"], data[key][si]["id"]
        sp = ["data", "solutions", si, "recipe", ri]
        if row["unit"] == "ml":
            q, kind = liters(row["amount"]), "liquid_input"
        elif stage == 5861:
            assert label == "FeSO4 x 7 H2O" and row["amount"] == 1
            q, kind = {"value": "0.1", "unit": "PERCENT_W_V"}, "stock_strength"
        elif stage == 595:
            grams = Decimal(str(row["amount"])) / (1000 if row["unit"] == "mg" else 1)
            q, kind = {
                "value": format(grams.normalize(), "f"),
                "unit": "G_PER_L",
            }, "stock_makeup_rate"
        elif si == 0 and key == "D119":
            q, kind = {
                "value": format(Decimal(str(row["amount"])) * 1000 / 1003, ".6g"),
                "unit": "G_PER_L",
            }, "verified_final_volume_rate"
        else:
            q, kind = None, "batch_mass"
        add(path, label, q, sp, kind)
        if q is None:
            assert f"{row['amount']} {row['unit']}" in get(after, path)["notes"]
        if row.get("attribute"):
            assert row["attribute"] in get(after, path)["notes"]

    if key.startswith("K"):
        assert "solutions" not in after and len(after["ingredients"]) == len(data[key])
        for i, row in enumerate(data[key]):
            q = None if row[3] == "null" else {"value": row[3], "unit": "G_PER_L"}
            add(
                ("ingredients", i),
                row[0],
                q,
                ["recipe_table", i + 1],
                "unquantified" if q is None else "provider_medium_rate",
            )
        ph = next(line for line in texts[key].splitlines() if line.startswith("PH Info:"))[
            9:
        ].split(",")[0]
        assert after.get("ph_value") == (None if ph == "null" else float(ph))
        assert "variants" not in after and "preparation_steps" not in after
        required_comparisons = {
            "K119.1": 2,
            "K119_11977": 1,
            "K119_11978": 1,
            "K119_11995": 1,
            "K119_6216": 1,
            "K119_7057": 1,
            "K119_9575": 1,
            "K119_15163": 1,
        }
        assert len(
            [c for c in item["claims"] if c["kind"] == "source_variant_comparison"]
        ) == required_comparisons.get(key, 0)
    else:
        ss = data[key]
        ni, ns = 0, 0
        for ri, row in enumerate(ss[0]["recipe"]):
            sp = ["data", "solutions", 0, "recipe", ri]
            if "solution_id" in row or row.get("compound") in {"Sodium resazurin", "Methanol"}:
                path = ("solutions", ns)
                ns += 1
                label = row.get("solution", row.get("compound"))
                if "compound" in row:
                    label += " (" + row["attribute"] + ")"
                add(path, label, liters(row["amount"]), sp, "stock_dose", True)
                stock = get(after, path)
                if "compound" in row:
                    assert len(stock["composition"]) == 1
                    q = (
                        {"value": "15", "unit": "PERCENT_V_V"}
                        if row["compound"] == "Methanol"
                        else {"value": "0.1", "unit": "PERCENT_W_V"}
                    )
                    add(path + ("composition", 0), row["compound"], q, sp, "stock_strength")
                else:
                    si = next(i for i, s in enumerate(ss) if s["id"] == row["solution_id"])
                    assert len(stock.get("composition", [])) == len(ss[si].get("recipe", []))
                    for j, r in enumerate(ss[si].get("recipe", [])):
                        component(path + ("composition", j), r, si, j)
                    preparation = "\n\n".join(s["step"] for s in ss[si].get("steps", []))
                    assert stock.get("preparation_notes", "") == preparation
            else:
                component(("ingredients", ni), row, 0, ri)
                ni += 1
        assert len(after["ingredients"]) == ni and len(after["solutions"]) == ns
        assert after["preparation_steps"] == before["preparation_steps"][: len(ss[0]["steps"])]
        assert [s["description"] for s in after["preparation_steps"]] == [
            s["step"] for s in ss[0]["steps"]
        ]
        for f in ("ph_value", "ph_range"):
            assert after.get(f) == before.get(f)
        if key == "D119":
            assert len(after["variants"]) == 16
            for variant in after["variants"]:
                assert variant["relationship"] == "STRAIN_SPECIFIC_VARIANT"
                assert (
                    variant["evidence"][0]["reference"]
                    == context["sources"]["DSMZ119"]["metadata"]["url"]
                )
                snippet = variant["evidence"][0]["snippet"]
                assert snippet in texts["DSMZ119"] and snippet.startswith(variant["name"] + ":")
                clean = re.sub(
                    r"\u00a9 2022 DSMZ - All rights reserved\s+Page 1 of 3\s+119: METHANOBACTERIUM MEDIUM",
                    "",
                    snippet,
                )
                assert variant["modifications"] == [" ".join(clean.split()).split(": ", 1)[1]]
            assert "0.3 g DL-Dithiothreitol" in after["variants"][9]["modifications"][0]
            assert "3.00 g/l" in after["variants"][5]["modifications"][0]
        else:
            assert "variants" not in after

    actual_nodes = {
        p
        for p, n in walk(after)
        if p and p[0] in {"ingredients", "solutions"} and "preferred_term" in n
    }
    assert actual_nodes == set(expected)
    lineage = []
    for path, wanted in expected.items():
        node, op = get(after, path), wanted["old_pointer"]
        assert (
            node["preferred_term"] == wanted["label"]
            and node.get("concentration") == wanted["quantity"]
        )
        assert "LB Medium" not in node.get("supplier_catalog", {}).get("supplier_name", "")
        ignore = {"notes", "concentration", "preferred_term", "evidence"}
        withdraw = (key.startswith("K") and wanted["label"] in renamed) or wanted["label"] in {
            "NiCl2 x 6 H2O",
            "Sodium resazurin",
        }
        if withdraw:
            ids = {"term", "mediaingredientmech_chebi_term", "mediaingredientmech_term"}
            assert not (ids & node.keys())
            ignore |= ids
        if wanted["descriptor"]:
            assert node["name"] == node["preferred_term"] and "evidence" not in node
            ignore |= {"name", "composition", "preparation_notes"}
        original = get(before, op) if op else {}
        assert {k: v for k, v in node.items() if k not in ignore} == {
            k: v for k, v in original.items() if k not in ignore
        }
        if original.get("notes", "").lstrip().startswith("[Merged 2 duplicates:"):
            assert node["notes"].startswith(
                "Superseded flattening history, not a current amount: " + original["notes"].strip()
            )
        else:
            assert node["notes"].startswith(original.get("notes", ""))
        if key.startswith("K"):
            assert (
                "Gram & Mol amounts are per Liter of medium." in node["evidence"][0]["explanation"]
            )
        lineage.append(
            {
                "pointer": list(path),
                "old_pointer": list(op) if op else None,
                "source": key,
                "source_pointer": wanted["source_pointer"],
                "label": wanted["label"],
                "kind": wanted["kind"],
            }
        )
    assert sorted(lineage, key=str) == sorted(item["lineage"], key=str)

    parent = {"K119": ("D119", "DERIVED_FROM"), "D119": ("D119c", "UNCERTAIN")}.get(key)
    if key.startswith("K") and key != "K119":
        parent = ("K119", "STRAIN_SPECIFIC_VARIANT")
    children = []
    if key == "K119":
        children = [
            (r["key"], "STRAIN_SPECIFIC_VARIANT")
            for r in context["records"]
            if r["key"].startswith("K") and r["key"] != "K119"
        ]
    elif key == "D119":
        children = [("K119", "DERIVED_FROM")]
    elif key == "D119c":
        children = [("D119", "UNCERTAIN")]

    def link(ref, other, relation):
        target = specs[other]
        assert {k: ref[k] for k in ("path", "id", "name", "relationship")} == {
            "path": target["path"],
            "id": target["id"],
            "name": yaml.load(target["before_text"], Loader=yaml.CSafeLoader)["name"],
            "relationship": relation,
        }
        assert ref["evidence"] and ref["notes"]

    if parent:
        link(after["parent_media"], *parent)
        assert after["variant_relationship"] == parent[1]
        assert after["variant_modifications"] == [after["parent_media"]["notes"]]
    else:
        assert not {"parent_media", "variant_relationship", "variant_modifications"} & after.keys()
    assert len(after.get("variant_children", [])) == len(children)
    for ref in after.get("variant_children", []):
        matches = [(k, rel) for k, rel in children if specs[k]["id"] == ref["id"]]
        assert len(matches) == 1
        link(ref, *matches[0])
    assert len({r["id"] for r in after.get("variant_children", [])}) == len(children)

    claims = item["claims"]
    old_quantities = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    assert old_quantities == {
        tuple(c["old_pointer"])
        for c in claims
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    }
    assert {p + ("concentration",) for p in expected} == {
        tuple(c["pointer"]) for c in claims if c["pointer"][-1] == "concentration"
    }
    assert {tuple(c["old_pointer"][:-1]) for c in claims if c["kind"] == "false_lb_removed"} == lb
    archived = [c for c in claims if c["kind"] == "old_ingredients_archived"]
    assert len(archived) == 1 and archived[0]["old"] == before["ingredients"]
    claimed = set()
    for c in claims:
        p, op, source = c["pointer"], c["old_pointer"], c["source"]
        assert c["new"] == get(after, p[:-1]).get(p[-1])
        assert c["old"] == (get(before, op[:-1]).get(op[-1]) if op else None)
        assert c["snippet"] and c["snippet"] in texts[source]
        assert c["reference"] == context["sources"][source]["metadata"]["url"]
        assert c["evidence_pointer"] is not None
        entries = [
            e
            for e in get(after, c["evidence_pointer"])["evidence"]
            if e["reference"] == c["reference"]
        ]
        assert len(entries) == 1 and c["explanation"] in entries[0]["explanation"]
        assert (
            c["snippet"] == entries[0]["snippet"]
            or "Additional exact excerpt: " + c["snippet"] in entries[0]["explanation"]
        )
        claimed.add((tuple(c["evidence_pointer"]), c["reference"]))
    actual = set()
    for p, node in walk(after):
        if "evidence" not in node:
            continue
        assert len(node["evidence"]) == len({e["reference"] for e in node["evidence"]})
        for e in node["evidence"]:
            source = next(
                k for k, s in context["sources"].items() if s["metadata"]["url"] == e["reference"]
            )
            assert (
                e["supports"] == "SUPPORT"
                and e["snippet"]
                and e["snippet"] in texts[source]
                and e["explanation"]
            )
            actual.add((p, e["reference"]))
    assert actual == claimed
    refs = after["references"]
    assert len(refs) == len({r["reference"] for r in refs})
    assert {r["reference"] for r in refs} == {c["reference"] for c in claims}
    for ref in refs:
        source = next(
            k for k, s in context["sources"].items() if s["metadata"]["url"] == ref["reference"]
        )
        assert ref["title"] == titles[source] and not {"authors", "year"} & ref.keys()
        assert all(
            s in ref["notes"]
            for s in (
                "source_type=",
                "discovery_mode=",
                "accessed_on=",
                context["sources"][source]["metadata"]["sha256"],
            )
        )
    allowed = {
        "ingredients",
        "solutions",
        "notes",
        "evidence",
        "references",
        "curation_history",
        "parent_media",
        "variant_children",
        "variant_relationship",
        "variant_modifications",
        "preparation_steps",
        "ph_value",
        "variants",
    }
    assert {k: v for k, v in after.items() if k not in allowed} == {
        k: v for k, v in before.items() if k not in allowed
    }
    assert "Superseded historical provenance (not a current formulation claim)" in after["notes"]
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["curator"] == "codex" and event["action"] == ACTION
    assert json.loads(event["changes"]) == [
        {k: c[k] for k in ("old_field", "field", "old", "new", "status", "reference", "snippet")}
        for c in claims
    ]
    return {
        "source_nodes": len(expected),
        "old_quantity_slots": len(old_quantities),
        "claims": len(claims),
        "new_evidence": len(actual),
        "new_references": len(refs),
        "new_curation_history": 1,
    }


if __name__ == "__main__":
    plan = json.loads((HERE / "plan.json").read_text())
    result = {
        r["key"]: check(
            yaml.load(r["before_text"], Loader=yaml.CSafeLoader),
            yaml.load(r["after_text"], Loader=yaml.CSafeLoader),
            r,
        )
        for r in plan["records"]
    }
    print(json.dumps(result, indent=2))
