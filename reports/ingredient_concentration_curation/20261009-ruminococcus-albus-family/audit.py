"""Independently project medium436 sources; never import the repair builder."""

import argparse
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
PREP = HERE.parent / "20261009-oteb-family"
CONTEXT_SHA = "45d48a0e66d0504c0bea2655ea38f2a88c4c3034f8f4bd520f6e6848e22d0b55"
ACTION = "RESTORED_RUMINOCOCCUS_ALBUS_SOURCE_FORMULATIONS_WITH_EVIDENCE"


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
        for key, child in node.items():
            yield from walk(child, path + (key,))
    elif isinstance(node, list):
        for i, child in enumerate(node):
            yield from walk(child, path + (i,))


@cache
def snapshot(raw):
    assert hashlib.sha256(raw).hexdigest() == CONTEXT_SHA
    context = json.loads(raw)
    data, texts, titles = {}, {}, {}
    for key, source in context["sources"].items():
        body, meta = source["raw"], source["metadata"]
        assert hashlib.sha256(body.encode()).hexdigest() == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        parsed = parse_recipe(recipe_source(meta["url"]), body, meta)
        texts[key], titles[key] = parsed.content, parsed.title
        if key.startswith("K"):
            (table,) = [
                t
                for t in BeautifulSoup(body, "html.parser").find_all("table")
                if "Gram Amount" in t.get_text()
            ]
            rows = [
                [html_recipe_text(str(c))[0] for c in tr.find_all("td", recursive=False)]
                for tr in table.find_all("tr")
            ]
            assert rows[0] == [
                "Name",
                "Semi unique name",
                "Unique Name",
                "Gram Amount",
                "Mol Amount",
            ]
            data[key] = rows[1:]
        elif key == "DSMZ436":
            rows, stage = [], "main formulation"
            for line in body.splitlines():
                if line.strip() in {
                    "Mineral solution 1:",
                    "Mineral solution 2:",
                    "Fatty acid mixture:",
                }:
                    stage = line.strip().rstrip(":")
                match = re.fullmatch(r"\s*(.+?)\s+(\d+(?:\.\d+)?)\s+(g|mg|ml|%)\s*", line)
                if match:
                    label, amount, unit = match.groups()
                    rows.append((stage, label, amount, unit))
            assert len(rows) == 21
            data[key] = rows
        elif key != "JCM675":
            data[key] = json.loads(body)
    return context, data, texts, titles


def batch(amount, unit):
    if unit == "ml":
        return {"value": str(Decimal(str(amount)) / 1000), "unit": "L"}
    assert unit in {"g", "mg", "%", None}
    return None


def check(before, after, item):
    context, data, texts, titles = snapshot((PREP / "next-436-context-approved.json").read_bytes())
    specs = {r["key"]: r for r in context["records"]}
    key, spec = item["key"], specs[item["key"]]
    assert key not in {"DJ675", "S4674", "K3037"}
    assert before == yaml.safe_load(spec["before_text"])
    assert before["id"] == after["id"] == spec["id"] and item["path"] == spec["path"]
    assert item["action"] == ACTION
    expected = {}

    def old_for(label):
        if label == "Cysteine-HCl x H2O" and key != "M2636":
            label = "L-Cysteine HCl x H2O"
        matches = [
            p
            for p, n in walk(before)
            if len(p) == 2
            and p[0] in {"ingredients", "solutions", "composition"}
            and n.get("preferred_term", "").casefold() == label.casefold()
            and "LB Medium" not in n.get("supplier_catalog", {}).get("supplier_name", "")
        ]
        assert len(matches) <= 1
        return matches[0] if matches else None

    def add(path, label, amount, source, sp, descriptor=False, old=None):
        assert path not in expected
        expected[path] = {
            "label": label,
            "quantity": amount,
            "source": source,
            "sp": sp,
            "descriptor": descriptor,
            "old": old_for(label) if old is None else old,
        }

    if key.startswith("K"):
        for i, row in enumerate(data[key]):
            add(
                ("ingredients", i),
                row[0],
                None if row[3] == "null" else {"value": row[3], "unit": "G_PER_L"},
                key,
                ["Metabolites list", i],
            )
        assert not after.get("solutions")
        if key == "K436":
            assert after["ph_value"] == 7
        else:
            assert "ph_value" not in after
        if key == "K3017":
            assert after["record_kind"] == "SOLUTION"
            assert "Instructions link points to DSMZ3017" in after["notes"]
            assert "equivalence is unverified" in after["notes"]
    elif key == "D436":
        assert not after.get("preparation_steps")
        assert all(s["description"] in after["notes"] for s in before["preparation_steps"])
        direct, ri, stage_prev = 0, 0, None
        stock_paths = {}
        for stage, label, amount, unit in data["DSMZ436"]:
            ri = ri + 1 if stage == stage_prev else 0
            stage_prev = stage
            descriptor = label in {"Mineral solution 1", "Mineral solution 2", "Fatty acid mixture"}
            if descriptor:
                path = ("solutions", len(stock_paths))
                stock_paths[label] = path
            elif stage == "main formulation":
                path = ("ingredients", direct)
                direct += 1
            else:
                path = stock_paths[stage] + ("composition", ri)
            add(path, label, batch(amount, unit), "DSMZ436", ["page 1", stage, ri], descriptor)
            assert f"{amount} {unit} per preparation" in get(after, path)["notes"]
        assert len(after["ingredients"]) == 8 and len(after["solutions"]) == 3
        assert after["ph_value"] == before["ph_value"] == 7
    elif key.startswith("M"):
        direct, stock_paths = 0, {}
        for si, stage in enumerate(data[key]["components"]):
            is_stock = stage["subcomponent_name"] in {
                "Mineral solution 1",
                "Mineral solution 2",
                "Fatty acid mixture",
            }
            for ri, row in enumerate(stage["items"]):
                label = row["component_name"]
                descriptor = row.get("reference_media_id") == key
                if descriptor:
                    path = ("solutions", len(stock_paths))
                    stock_paths[label.replace(" (see below)", "").casefold()] = path
                elif is_stock:
                    path = stock_paths[stage["subcomponent_name"].casefold()] + ("composition", ri)
                else:
                    path = ("ingredients", direct)
                    direct += 1
                amount = batch(row.get("volume"), row.get("unit"))
                if key == "M2636" and label in {"Maltose", "Starch"}:
                    assert "maltose (1g/L), starch (1g/L)" in data[key]["meta"]["name"]
                    assert row["volume"] == 1 and row["unit"] == "g"
                    amount = {"value": "1", "unit": "G_PER_L"}
                add(path, label, amount, key, ["components", si, "items", ri], descriptor)
                assert f"{row.get('volume')} {row.get('unit')}" in get(after, path)["notes"]
        assert len(after["solutions"]) == 3
        assert all(c["comment"] in after["notes"] for c in data[key]["comments"])
    else:
        assert key in {"S882", "S883", "S884", "S885"}
        rows = data[key]["data"]["recipe"]
        ordered = [(i, r) for i, r in enumerate(rows) if not r.get("solution_id")]
        ordered += [(i, r) for i, r in enumerate(rows) if r.get("solution_id")]
        for oi, (ri, row) in enumerate(ordered):
            amount = (
                {"value": str(row["g_l"]), "unit": "G_PER_L"}
                if row.get("g_l") is not None
                else batch(row["amount"], row["unit"])
            )
            label = row.get("compound") or row["solution"]
            add(("composition", oi), label, amount, key, ["data", "recipe", ri])
            if row.get("solution_id"):
                assert after["composition"][oi]["culturemech_term"] == {
                    "id": specs["S" + str(row["solution_id"])]["id"],
                    "label": label,
                }
        assert "ingredients" not in after and "incomplete_composition" not in after.get(
            "data_quality_flags", []
        )
        assert "evidence" not in after and "source_data" not in after
        if key == "S885":
            assert "not a stock preparation instruction" in after["preparation_notes"]
            assert before["preparation_notes"] in after["preparation_notes"]
        for i, n in enumerate(before["composition"]):
            if n.get("evidence"):
                assert after["composition"][i] == n

    lineage = {tuple(r["pointer"]): r for r in item["lineage"]}
    actual_nodes = {
        p
        for p, n in walk(after)
        if p and p[0] in {"ingredients", "solutions", "composition"} and "preferred_term" in n
    }
    assert actual_nodes == set(expected) == set(lineage)
    assert len(lineage) == len(item["lineage"])
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
        old = get(before, want["old"]) if want["old"] else {}
        ignored = {"preferred_term", "concentration", "notes", "evidence"}
        if want["descriptor"]:
            assert node["name"] == want["label"]
            assert set(node) <= {"preferred_term", "name", "composition", "concentration", "notes"}
        else:
            if key == "M2636" and want["label"] == "MgSO4 x 7 H2O":
                ignored.add("mediaingredientmech_chebi_term")
                assert "mediaingredientmech_chebi_term" not in node
            if key == "S882" and path[1] >= 8:
                ignored.add("culturemech_term")
            assert {k: v for k, v in node.items() if k not in ignored} == {
                k: v for k, v in old.items() if k not in ignored
            }
        if "[Merged 4 duplicates:" in old.get("notes", ""):
            assert node["notes"].startswith("Superseded flattening history, not a current amount:")

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
    assert {
        c["old_pointer"][0]: c["old"] for c in claims if c["kind"] == "prior_nodes_archived"
    } == {f: before[f] for f in ("ingredients", "composition", "solutions") if before.get(f)}
    claimed = set()
    for claim in claims:
        assert claim["old"] == (
            value(before, claim["old_pointer"]) if claim["old_pointer"] else None
        )
        assert claim["new"] == value(after, claim["pointer"])
        assert claim["snippet"] and claim["snippet"] in texts[claim["source"]]
        assert claim["reference"] == context["sources"][claim["source"]]["metadata"]["url"]
        assert claim["evidence_pointer"] is not None
        (entry,) = [
            e
            for e in get(after, claim["evidence_pointer"])["evidence"]
            if e["reference"] == claim["reference"]
        ]
        assert claim["explanation"] in entry["explanation"]
        assert (
            claim["snippet"] == entry["snippet"]
            or "Additional exact excerpt: " + claim["snippet"] in entry["explanation"]
        )
        claimed.add((tuple(claim["evidence_pointer"]), claim["reference"]))
    actual = set()
    urls = {s["metadata"]["url"]: k for k, s in context["sources"].items()}
    for p, node in walk(after):
        entries = node.get("evidence", [])
        assert len(entries) == len({e["reference"] for e in entries})
        for e in entries:
            assert e["supports"] == "SUPPORT" and e["snippet"] in texts[urls[e["reference"]]]
            actual.add((p, e["reference"]))
    assert actual == claimed
    old_refs = {r["reference"]: r for r in before.get("references", [])}
    refs = {r["reference"]: r for r in after["references"]}
    assert len(refs) == len(after["references"]) and set(refs) == set(old_refs) | {
        c["reference"] for c in claims
    }
    for url, ref in refs.items():
        assert ref["title"] == titles[urls[url]] and not {"authors", "year"} & ref.keys()
        assert all(
            text in ref["notes"]
            for text in (
                "source_type=",
                "discovery_mode=",
                "accessed_on=",
                context["sources"][urls[url]]["metadata"]["sha256"],
            )
        )
        assert ref["notes"].startswith(old_refs.get(url, {}).get("notes", ""))

    relations = {
        "K436": ("D436", "DERIVED_FROM"),
        "K436_18848": ("K436", "STRAIN_SPECIFIC_VARIANT"),
    }
    if key in relations:
        target, relation = relations[key]
        ref = after["parent_media"]
        assert ref["id"] == specs[target]["id"] and ref["path"] == specs[target]["path"]
        assert ref["relationship"] == after["variant_relationship"] == relation
        assert after["variant_modifications"] == [ref["notes"]] and ref["evidence"]
        assert ref["name"] == yaml.safe_load(specs[target]["before_text"])["name"]
    else:
        for field in ("parent_media", "variant_relationship", "variant_modifications"):
            assert after.get(field) == before.get(field)
    if key in {"D436", "K436"}:
        child = "K436" if key == "D436" else "K436_18848"
        (ref,) = after["variant_children"]
        assert ref["id"] == specs[child]["id"] and ref["path"] == specs[child]["path"]
        assert ref["relationship"] == relations[child][1] and ref["evidence"]
        assert ref["name"] == yaml.safe_load(specs[child]["before_text"])["name"]
    else:
        assert after.get("variant_children") == before.get("variant_children")
    allowed = {
        "ingredients",
        "composition",
        "solutions",
        "notes",
        "evidence",
        "references",
        "curation_history",
        "parent_media",
        "variant_relationship",
        "variant_modifications",
        "variant_children",
    }
    if key.startswith("S"):
        allowed.add("data_quality_flags")
    if key == "S885":
        allowed.add("preparation_notes")
    if key == "D436":
        allowed.add("preparation_steps")
    if key == "K436_18848":
        allowed.add("ph_value")
    assert {k: v for k, v in before.items() if k not in allowed} == {
        k: v for k, v in after.items() if k not in allowed
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
        "new_evidence": len(actual) - sum(len(n.get("evidence", [])) for _, n in walk(before)),
        "new_references": len(refs) - len(old_refs),
        "new_curation_history": 1,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    args = parser.parse_args()
    totals = []
    for item in json.loads(args.plan.read_text())["records"]:
        result = check(
            yaml.safe_load(item["before_text"]), yaml.safe_load(item["after_text"]), item
        )
        totals.append(result)
        print(json.dumps({"key": item["key"], **result}), flush=True)
    print(json.dumps({"total": {k: sum(r[k] for r in totals) for k in totals[0]}}), flush=True)
