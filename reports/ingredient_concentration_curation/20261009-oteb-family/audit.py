"""Independently project OTEB source rows and audit proposed provenance.

This module never imports or calls the repair builder.
"""

import argparse
import hashlib
import json
from functools import cache
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from culturemech.validation.recipe_references import html_recipe_text, parse_recipe, recipe_source

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SHA = "8f4e87e29247c1a0dfea3ce78ff0283c3456f1fbf7fd5b3bd3343eff06b0b52c"
ACTION = "RESTORED_OTEB_SOURCE_FORMULATIONS_AND_STOCK_SCOPES_WITH_EVIDENCE"


def get(node, path):
    for part in path:
        node = node[part]
    return node


def value(node, path):
    parent = get(node, path[:-1])
    return parent[path[-1]] if isinstance(parent, list) else parent.get(path[-1])


def walk(node, path=()):
    if isinstance(node, dict):
        yield path, node
        for k, child in node.items():
            yield from walk(child, path + (k,))
    elif isinstance(node, list):
        for i, child in enumerate(node):
            yield from walk(child, path + (i,))


@cache
def snapshot(raw):
    assert hashlib.sha256(raw).hexdigest() == SHA
    context = json.loads(raw)
    for path, digest in context["preparation_receipt_sha256"].items():
        assert hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest
    review = json.loads((HERE / "source-review.json").read_text())
    decisions = {(r["source"], tuple(r["pointer"])): r for r in review["source_decisions"]}
    pdf_rows = {tuple(r["pointer"]): r for r in review["original_pdf_decisions"]}
    assert len(decisions) == 126 and len(pdf_rows) == 30
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
            data[key] = rows[1:]
        elif key != "DSMZ1245":
            data[key] = json.loads(body)
    for decision in list(decisions.values()) + list(pdf_rows.values()):
        assert decision["snippet"] in texts[decision["source"]]
        assert decision["reference"] == context["sources"][decision["source"]]["metadata"]["url"]
    return context, decisions, pdf_rows, texts, titles, data


def check(before, after, item):
    context, decisions, pdf_rows, texts, titles, data = snapshot(
        (HERE / "context.json").read_bytes()
    )
    specs = {r["key"]: r for r in context["records"]}
    key, spec = item["key"], specs[item["key"]]
    assert before == yaml.load(spec["before_text"], Loader=yaml.CSafeLoader)
    assert before["id"] == after["id"] == spec["id"] and item["path"] == spec["path"]
    assert item["action"] == ACTION
    expected = {}

    def add(path, label, quantity, source, sp, *, old=None, descriptor=False, withdraw=()):
        assert path not in expected
        expected[path] = {
            "label": label,
            "quantity": quantity,
            "source": source,
            "sp": list(sp),
            "old": old,
            "descriptor": descriptor,
            "withdraw": set(withdraw),
        }

    aliases = {
        "Potassium Phosphate, dibasic": "Potassium Phosphate",
        "Calf Serum, inactivated": "Fetal bovine serum",
        "Soluble Starch": "Starch",
    }
    old_ingredients = [
        (p, n)
        for p, n in walk(before)
        if len(p) == 2
        and p[0] == "ingredients"
        and "LB Medium" not in n.get("supplier_catalog", {}).get("supplier_name", "")
    ]

    def old_for(label):
        matches = [
            p
            for p, n in old_ingredients
            if n["preferred_term"].casefold() == aliases.get(label, label).casefold()
        ]
        assert len(matches) <= 1
        return matches[0] if matches else None

    ids = {"term", "chebi_term", "mediaingredientmech_chebi_term", "mediaingredientmech_term"}
    if key.startswith("K"):
        rows = data[key]
        assert len(after["ingredients"]) == len(rows) and not after.get("solutions")
        for i, row in enumerate(rows):
            d = decisions[(key, ("Metabolites list", i))]
            assert d["row"] == row
            quantity = None if row[3] == "null" else {"value": row[3], "unit": "G_PER_L"}
            assert d["proposed_concentration"] == quantity
            add(
                ("ingredients", i),
                row[0],
                quantity,
                key,
                d["pointer"],
                old=old_for(row[0]),
                withdraw=(
                    ids
                    if row[0] in {"Potassium Phosphate, dibasic", "Thiamine Pyrophosphate"}
                    else ()
                ),
            )
        if key == "K1245":
            assert after["ph_range"] == {"min": 6.8, "max": 7.2}
        else:
            assert not {"ph_range", "ph_value"} & after.keys()
        if key == "K6000":
            assert after["record_kind"] == before["record_kind"] == "SOLUTION"
            assert "equivalence is unverified" in after["notes"]
    elif key == "D1245":
        assert [s["preferred_term"] for s in after["solutions"]] == [
            "Vitamin K1 (1% solution)",
            "Sugar Stock Solution",
        ]
        assert len(after["ingredients"]) == 16
        assert [len(s["composition"]) for s in after["solutions"]] == [1, 12]
        direct = 0
        for si, stage in enumerate(data[key]["data"]["solutions"]):
            stage_name = "main" if si == 0 else "sugar_stock"
            for ri, row in enumerate(stage["recipe"]):
                original = pdf_rows[(stage_name, ri)]
                label = row.get("compound") or row.get("solution")
                quantity = original["proposed_concentration"]
                if label == "Vitamin K1":
                    add(
                        ("solutions", 0),
                        "Vitamin K1 (1% solution)",
                        quantity,
                        "DSMZ1245",
                        [stage_name, ri],
                        descriptor=True,
                    )
                    add(
                        ("solutions", 0, "composition", 0),
                        label,
                        None,
                        "DSMZ1245",
                        [stage_name, ri],
                        old=old_for(label),
                    )
                    continue
                if row.get("solution_id") == 5688:
                    add(
                        ("solutions", 1),
                        "Sugar Stock Solution",
                        quantity,
                        "DSMZ1245",
                        [stage_name, ri],
                        descriptor=True,
                    )
                    continue
                label = {
                    "Potassium Phosphate": "Potassium Phosphate, dibasic",
                    "Fetal bovine serum": "Calf Serum, inactivated",
                    "Starch": "Soluble Starch",
                }.get(label, label)
                path = ("ingredients", direct) if si == 0 else ("solutions", 1, "composition", ri)
                add(
                    path,
                    label,
                    quantity,
                    "DSMZ1245",
                    [stage_name, ri],
                    old=old_for(label),
                    withdraw=(
                        ids
                        if label in {"Potassium Phosphate, dibasic", "Thiamine pyrophosphate"}
                        else ()
                    ),
                )
                if si == 0:
                    direct += 1
                if quantity is None:
                    inp = original["batch_input"]
                    assert (
                        f"{inp['amount']} {inp['unit']} per preparation"
                        in get(after, path)["notes"]
                    )
        assert "preparation_steps" not in after
        assert all(s["description"] in after["notes"] for s in before["preparation_steps"])
        assert "1003.1" in after["notes"] and "7.0" in after["notes"]
        assert after["ph_range"] == before["ph_range"]
    else:
        rows = data[key]["data"]["recipe"]
        assert len(after["composition"]) == len(rows)
        for ri, row in enumerate(rows):
            d = decisions[(key, ("data", "recipe", ri))]
            assert d["row"] == row
            if row.get("solution_id") == 5688:
                add(
                    ("composition", 17),
                    "Sugar Stock Solution",
                    {"value": "0.1", "unit": "L"},
                    key,
                    d["pointer"],
                )
                assert after["composition"][17]["culturemech_term"] == {
                    "id": specs["S5688"]["id"],
                    "label": "Sugar Stock Solution",
                }
                continue
            oi = ri if key == "S5688" or ri < 16 else ri - 1
            label = (
                "Vitamin K1 (1% solution)" if row["compound"] == "Vitamin K1" else row["compound"]
            )
            withdraw = (
                ids
                if row["compound"] == "Vitamin K1"
                else (
                    {"chebi_term"}
                    if key == "S5688" and row["compound"] == "Thiamine pyrophosphate"
                    else set()
                )
            )
            add(
                ("composition", oi),
                label,
                d["proposed_concentration"],
                key,
                d["pointer"],
                old=("composition", oi),
                withdraw=withdraw,
            )
            original, current = before["composition"][oi], after["composition"][oi]
            for evidence in original.get("evidence", []):
                assert evidence in current["evidence"], "Prior supported evidence was rewritten"
        assert not after.get("ingredients") and "incomplete_composition" not in after.get(
            "data_quality_flags", []
        )
        assert "source_data" not in after and "evidence" not in after and not after.get("solutions")
        if key == "S2474":
            assert after["composition"][3]["chebi_term"] == before["composition"][3]["chebi_term"]
            assert after["composition"][15]["preferred_term"] == "Fetal bovine serum"
        else:
            assert [n["preferred_term"] for n in after["composition"]].count("Maltose") == 2
    lineage = {tuple(r["pointer"]): r for r in item["lineage"]}
    actual_nodes = {
        p
        for p, n in walk(after)
        if p and p[0] in {"ingredients", "composition", "solutions"} and "preferred_term" in n
    }
    assert actual_nodes == set(expected) == set(lineage)
    for path, want in expected.items():
        node = get(after, path)
        assert (
            node["preferred_term"] == want["label"]
            and node.get("concentration") == want["quantity"]
        )
        assert (
            lineage[path]["source"] == want["source"]
            and lineage[path]["source_pointer"] == want["sp"]
        )
        assert lineage[path]["old_pointer"] == (list(want["old"]) if want["old"] else None)
        original = get(before, want["old"]) if want["old"] else {}
        ignored = {"preferred_term", "concentration", "notes", "evidence"} | want["withdraw"]
        if want["descriptor"]:
            assert node["name"] == want["label"] and set(node) <= {
                "preferred_term",
                "name",
                "composition",
                "concentration",
                "notes",
            }
            assert not ids & node.keys()
        else:
            assert not want["withdraw"] & node.keys()
            if key == "S2474" and path == ("composition", 17):
                ignored.add("culturemech_term")
            assert {k: v for k, v in node.items() if k not in ignored} == {
                k: v for k, v in original.items() if k not in ignored
            }
        if "[Collapsed" in original.get("notes", ""):
            assert node["notes"].startswith("Superseded flattening history, not a current amount:")
    check_links(key, before, after, specs)
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
    archives = {
        c["old_pointer"][0]: c["old"] for c in claims if c["kind"] == "prior_nodes_archived"
    }
    assert archives == {
        f: before[f] for f in ("ingredients", "composition", "solutions") if before.get(f)
    }
    claimed = set()
    for c in claims:
        assert c["new"] == value(after, c["pointer"])
        assert c["old"] == (value(before, c["old_pointer"]) if c["old_pointer"] else None)
        assert c["snippet"] and c["snippet"] in texts[c["source"]]
        assert c["reference"] == context["sources"][c["source"]]["metadata"]["url"]
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
    urls = {s["metadata"]["url"]: k for k, s in context["sources"].items()}
    for p, node in walk(after):
        assert len(node.get("evidence", [])) == len(
            {e["reference"] for e in node.get("evidence", [])}
        )
        for e in node.get("evidence", []):
            assert e["supports"] == "SUPPORT" and e["snippet"] in texts[urls[e["reference"]]]
            actual.add((p, e["reference"]))
    assert actual == claimed
    old_refs = {r["reference"]: r for r in before.get("references", [])}
    refs = {r["reference"]: r for r in after["references"]}
    assert len(refs) == len(after["references"]) and set(refs) == set(old_refs) | {
        c["reference"] for c in claims
    }
    for url, ref in refs.items():
        original = old_refs.get(url, {})
        assert ref["title"] == titles[urls[url]]
        assert not {"authors", "year"} & (ref.keys() - original.keys())
        assert all(
            s in ref["notes"]
            for s in (
                "source_type=",
                "discovery_mode=",
                "accessed_on=",
                context["sources"][urls[url]]["metadata"]["sha256"],
            )
        )
        assert ref["notes"].startswith(original.get("notes", ""))
    allowed = {
        "ingredients",
        "solutions",
        "composition",
        "notes",
        "evidence",
        "references",
        "curation_history",
        "parent_media",
        "variant_children",
        "variant_relationship",
        "variant_modifications",
        "preparation_steps",
    }
    if key.startswith("S"):
        allowed.add("data_quality_flags")
    assert {k: v for k, v in after.items() if k not in allowed} == {
        k: v for k, v in before.items() if k not in allowed
    }
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
        "new_evidence": len(actual) - sum(len(n.get("evidence", [])) for _, n in walk(before)),
        "new_references": len(refs) - len(old_refs),
        "new_curation_history": 1,
    }


def check_links(key, before, after, specs):
    links = {
        "K1245": ("D1245", "DERIVED_FROM"),
        "K1245_18691": ("K1245", "STRAIN_SPECIFIC_VARIANT"),
    }

    def check_ref(ref, target, relation):
        spec = specs[target]
        assert {f: ref[f] for f in ("id", "path", "name", "relationship")} == {
            "id": spec["id"],
            "path": spec["path"],
            "name": yaml.load(spec["before_text"], Loader=yaml.CSafeLoader)["name"],
            "relationship": relation,
        }
        assert ref["evidence"] and ref["notes"]

    if key in links:
        parent, relation = links[key]
        check_ref(after["parent_media"], parent, relation)
        assert after["variant_relationship"] == relation
        assert after["variant_modifications"] == [after["parent_media"]["notes"]]
    else:
        for f in ("parent_media", "variant_relationship", "variant_modifications"):
            assert after.get(f) == before.get(f)
    if key in {"D1245", "K1245"}:
        child = "K1245" if key == "D1245" else "K1245_18691"
        assert len(after["variant_children"]) == 1
        check_ref(after["variant_children"][0], child, links[child][1])
    else:
        assert after.get("variant_children") == before.get("variant_children")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text())
    results = {}
    for item in plan["records"]:
        results[item["key"]] = check(
            yaml.load(item["before_text"], Loader=yaml.CSafeLoader),
            yaml.load(item["after_text"], Loader=yaml.CSafeLoader),
            item,
        )
        print(json.dumps({"key": item["key"], **results[item["key"]]}), flush=True)
    print(
        json.dumps(
            {
                "total": {
                    k: sum(r[k] for r in results.values()) for k in next(iter(results.values()))
                }
            }
        ),
        flush=True,
    )
