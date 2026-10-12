"""Project medium330 claims directly from captured sources, without the builder."""

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
PREP = HERE.parent / "20261009-ruminococcus-albus-family"
CONTEXT_SHA = "97e6cfa229556a5251518fafb27c7506242afb62cb7be79ff7ff985dfb4e6c49"
ACTION = "RESTORED_RUMEN_BACTERIA_SOURCE_FORMULATIONS_WITH_EVIDENCE"


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
        for field, child in node.items():
            yield from walk(child, path + (field,))
    elif isinstance(node, list):
        for i, child in enumerate(node):
            yield from walk(child, path + (i,))


@cache
def snapshot(raw, linked_raw):
    assert hashlib.sha256(raw).hexdigest() == CONTEXT_SHA
    assert (
        hashlib.sha256(linked_raw).hexdigest()
        == "5c2f6f2409a8ae6231cd6d85da4ad3899977e216dd5b9084ea8b9d65a02aaeda"
    )
    context = json.loads(raw)
    context["sources"]["M124"] = json.loads(linked_raw)["source"]
    data, texts, titles = {}, {}, {}
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        assert hashlib.sha256(raw.encode()).hexdigest() == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        parsed = parse_recipe(recipe_source(meta["url"]), raw, meta)
        texts[key], titles[key] = parsed.content, parsed.title
        if key.startswith("K"):
            (table,) = [
                t
                for t in BeautifulSoup(raw, "html.parser").find_all("table")
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
        elif key == "DSMZ330":
            stage, page, rows = "main formulation", 1, []
            names = {
                "Mineral solution (from medium 330)": "mineral stock",
                "Volatile fatty acid mixture (from medium 330)": "fatty-acid stock",
                "Haemin solution (from medium 78)": "haemin stock",
            }
            for line in raw.splitlines():
                if "Page 1 of 2" in line:
                    page = 2
                if line.strip() in names:
                    stage = names[line.strip()]
                match = re.fullmatch(r"\s*(.+?)\s+(\d+(?:\.\d+)?)\s+(g|mg|ml)\s*", line)
                if match and not line.startswith("Final volume:"):
                    rows.append((stage, page, *match.groups()))
            assert len(rows) == 32 and "Final volume: 1003 ml" in raw
            assert "make up to 100 ml with distilled water and filter" in raw
            data[key] = rows
        elif key == "JCM133":
            soup = BeautifulSoup(raw, "html.parser")
            data[key] = [
                [
                    [html_recipe_text(str(c))[0] for c in tr.find_all("td", recursive=False)]
                    for tr in table.find_all("tr")
                ]
                for table in soup.find_all("table")
            ]
        else:
            data[key] = json.loads(raw)
    return context, data, texts, titles


def batch(amount, unit):
    if unit == "ml":
        return {"value": str(Decimal(str(amount)) / 1000), "unit": "L"}
    if unit == "L":
        return {"value": str(amount), "unit": "L"}
    assert unit in {"g", "mg", None}
    return None


def check(before, after, item):
    context, data, texts, titles = snapshot(
        (PREP / "next-330-context-approved.json").read_bytes(),
        (PREP / "next-330-M124.json").read_bytes(),
    )
    specs = {r["key"]: r for r in context["records"]}
    key, spec = item["key"], specs[item["key"]]
    assert before == yaml.load(spec["before_text"], Loader=yaml.CSafeLoader)
    assert before["id"] == after["id"] == spec["id"] and item["path"] == spec["path"]
    assert item["action"] == ACTION
    expected = {}

    def old_for(label):
        aliases = {
            "Cysteine-HCl x H2O": "L-Cysteine HCl x H2O",
            "Trypticase Peptone (BBL)": "Trypticase peptone",
            "Trypticase peptone (BD BBL)": "Trypticase peptone",
            "Yeast extract (OXOID)": "Yeast extract",
            "NaOH (1 N)": "NaOH",
        }
        if key in {"K330", "K330_17630", "D330"}:
            aliases.update({"Glucose": "D-Glucose", "Starch, soluble": "Starch"})
        if key.startswith("K"):
            aliases["Resazurin"] = "Sodium resazurin"
        label = aliases.get(label, label)
        matches = [
            p
            for p, n in walk(before)
            if len(p) == 2
            and p[0] in {"ingredients", "composition", "solutions"}
            and n.get("preferred_term", "").casefold() == label.casefold()
            and "LB Medium" not in n.get("supplier_catalog", {}).get("supplier_name", "")
        ]
        assert len(matches) <= 1
        return matches[0] if matches else None

    def add(path, label, quantity, source, sp, descriptor=False, old=None, stock=None):
        assert path not in expected
        expected[path] = {
            "label": label,
            "quantity": quantity,
            "source": source,
            "sp": sp,
            "descriptor": descriptor,
            "old": old_for(label) if old is None else old,
            "stock": stock,
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
        if key == "K330":
            assert after["ph_range"] == {"min": 6.7, "max": 6.8}
        else:
            assert "ph_range" not in after and "ph_value" not in after
        if key in {"K3032", "K3131"}:
            assert after["record_kind"] == "SOLUTION"
            assert "equivalence is unverified" in after["notes"]
            assert "Instructions link points to DSMZ" + key[1:] in after["notes"]
        if key == "K330_17630":
            base = {r[0]: r[3] for r in data["K330"]}
            variant = {r[0]: r[3] for r in data[key]}
            assert set(variant) - set(base) == {"rumen fluid"} and variant["rumen fluid"] == "29.13"
            assert sum(base[n] != variant[n] for n in base) == 16
    elif key == "D330":
        direct, counts, stocks = 0, {}, {}
        labels = {
            "mineral stock": "Mineral solution",
            "fatty-acid stock": "Volatile fatty acid mixture",
            "haemin stock": "Haemin solution (0.05% w/v)",
        }
        for stage, page, label, amount, unit in data["DSMZ330"]:
            ri = counts.get(stage, 0)
            counts[stage] = ri + 1
            descriptor = stage == "main formulation" and label in labels.values()
            if descriptor:
                path = ("solutions", len(stocks))
                stocks[label] = path
            elif stage == "main formulation":
                path = ("ingredients", direct)
                direct += 1
            else:
                path = stocks[labels[stage]] + ("composition", ri)
            quantity = batch(amount, unit)
            if stage == "main formulation" and unit == "g":
                quantity = {
                    "value": format(Decimal(amount) / Decimal("1.003"), ".6g"),
                    "unit": "G_PER_L",
                }
                assert (
                    "1.003 L" in get(after, path)["notes"]
                    and "Final volume: 1003 ml" in get(after, path)["notes"]
                )
            if stage == "haemin stock" and label == "Haemin":
                quantity = {"value": "0.5", "unit": "G_PER_L"}
            if stage == "haemin stock" and label == "Distilled water":
                quantity = None
            if stage == "haemin stock" and label != "NaOH (1 N)":
                assert "make up to 100 ml" in get(after, path)["notes"]
            add(path, label, quantity, "DSMZ330", [f"page {page}, {stage}", ri], descriptor)
            assert f"{amount} {unit} per preparation" in get(after, path)["notes"]
        assert "1003.6 ml" in after["notes"] and "six significant digits" in after["notes"]
    elif key == "DJ1029":
        stocks, direct = {}, 0
        for si, stage in enumerate(data[key]["data"]["solutions"]):
            for ri, row in enumerate(stage["recipe"]):
                descriptor = bool(row.get("solution_id"))
                if descriptor:
                    path = ("solutions", len(stocks))
                    stocks[row["solution_id"]] = path
                elif si == 0:
                    path = ("ingredients", direct)
                    direct += 1
                else:
                    path = stocks[stage["id"]] + ("composition", ri)
                add(
                    path,
                    row.get("compound") or row["solution"],
                    batch(row["amount"], row["unit"]),
                    key,
                    ["data", "solutions", si, "recipe", ri],
                    descriptor,
                )
                assert f"{row['amount']} {row['unit']}" in get(after, path)["notes"]
                if row.get("g_l") is not None:
                    assert f"Dataset g_l={row['g_l']}" in get(after, path)["notes"]
        assert "Original JCM1029 is unavailable" in after["notes"]
    elif key == "M1093":
        direct, stocks = 0, {}
        for si, stage in enumerate(data[key]["components"]):
            for ri, row in enumerate(stage["items"]):
                descriptor = bool(row.get("reference_media_id"))
                if descriptor:
                    path = ("solutions", len(stocks))
                    stocks[row["reference_media_id"]] = path
                elif si == 0:
                    path = ("ingredients", direct)
                    direct += 1
                else:
                    path = stocks["M1093"] + ("composition", ri)
                add(
                    path,
                    row["component_name"],
                    batch(row.get("volume"), row.get("unit")),
                    key,
                    ["components", si, "items", ri],
                    descriptor,
                )
                assert f"{row.get('volume')} {row.get('unit')}" in get(after, path)["notes"]
        assert data["M124"]["meta"]["original_media_id"] == "JCM_M133"
        assert data["M124"]["meta"]["src_url"] == context["sources"]["JCM133"]["metadata"]["url"]
        vfa = data["M124"]["components"][1]
        assert len(vfa["items"]) == 7
        for ri, row in enumerate(vfa["items"]):
            path = stocks["M124"] + ("composition", ri)
            add(
                path,
                row["component_name"],
                batch(row["volume"], row["unit"]),
                "M124",
                ["components", 1, "items", ri],
            )
            original = [
                e
                for e in get(after, path)["evidence"]
                if e["reference"] == context["sources"]["JCM133"]["metadata"]["url"]
            ]
            assert len(original) == 1 and original[0]["snippet"] in texts["JCM133"]
            assert "VFA-stock input only" in original[0]["explanation"]
            original_label = row["component_name"].replace("--", "-")
            (original_row,) = [r for r in data["JCM133"][1] if r[0] == original_label]
            assert Decimal(original_row[1]) == Decimal(str(row["volume"]))
            assert original_row[2] == row["unit"] == "ml"
            assert original[0]["snippet"] == " ".join(original_row)
        assert "Original JCM1029 is unavailable" in after["notes"]
        assert all(c["comment"] in after["notes"] for c in data[key]["comments"])
    else:
        assert key.startswith("S")
        rows = data[key]["data"]["recipe"]
        ordered = [(i, r) for i, r in enumerate(rows) if not r.get("solution_id")]
        ordinary_count = len(ordered)
        ordered += [(i, r) for i, r in enumerate(rows) if r.get("solution_id")]
        for oi, (ri, row) in enumerate(ordered):
            quantity = batch(row["amount"], row["unit"])
            if row["unit"] in {"g", "mg"} and row.get("g_l") is not None:
                quantity = {"value": str(row["g_l"]), "unit": "G_PER_L"}
            if key == "S124" and row["compound"] == "Distilled water":
                quantity = None
                assert "make up" in get(after, ("composition", oi))["notes"].lower()
            add(
                ("composition", oi),
                row.get("compound") or row["solution"],
                quantity,
                key,
                ["data", "recipe", ri],
                old=("composition", oi) if oi < ordinary_count else None,
                stock=row.get("solution_id"),
            )
            retained = oi < ordinary_count and get(before, ("composition", oi)).get("evidence")
            if row.get("attribute") and not retained:
                assert row["attribute"] in get(after, ("composition", oi))["notes"]
        assert not after.get("ingredients") and "incomplete_composition" not in after.get(
            "data_quality_flags", []
        )
        assert "evidence" not in after and "source_data" not in after
        for i, old in enumerate(before["composition"]):
            if old.get("evidence"):
                new = after["composition"][i]
                assert new["evidence"][: len(old["evidence"])] == old["evidence"]
                assert {k: v for k, v in new.items() if k != "evidence"} == {
                    k: v for k, v in old.items() if k != "evidence"
                }

    lineage = {tuple(r["pointer"]): r for r in item["lineage"]}
    actual_nodes = {
        p
        for p, n in walk(after)
        if p and p[0] in {"ingredients", "composition", "solutions"} and "preferred_term" in n
    }
    assert actual_nodes == set(expected) == set(lineage) and len(lineage) == len(item["lineage"])
    for path, want in expected.items():
        node, quantity = get(after, path), want["quantity"]
        assert node["preferred_term"] == want["label"]
        if quantity is None:
            assert "concentration" not in node
        else:
            actual = node["concentration"]
            assert actual["unit"] == quantity["unit"] and set(actual) == {"value", "unit"}
            assert (
                actual["value"] == quantity["value"]
                if key.startswith("K")
                else Decimal(actual["value"]) == Decimal(quantity["value"])
            )
        assert (
            lineage[path]["source"] == want["source"]
            and lineage[path]["source_pointer"] == want["sp"]
        )
        assert lineage[path]["old_pointer"] == (list(want["old"]) if want["old"] else None)
        old = get(before, want["old"]) if want["old"] else {}
        ignored = {"preferred_term", "concentration", "notes", "evidence"}
        if want["descriptor"]:
            assert node["name"] == want["label"] and set(node) <= {
                "preferred_term",
                "name",
                "composition",
                "concentration",
                "notes",
            }
        else:
            if key.startswith("K") and want["label"] == "Resazurin":
                ids = {
                    "term",
                    "chebi_term",
                    "mediaingredientmech_chebi_term",
                    "mediaingredientmech_term",
                }
                ignored.update(ids)
                assert not ids & node.keys()
            if want["stock"]:
                ignored.add("culturemech_term")
                assert node["culturemech_term"] == {
                    "id": specs["S" + str(want["stock"])]["id"],
                    "label": want["label"],
                }
            assert {k: v for k, v in node.items() if k not in ignored} == {
                k: v for k, v in old.items() if k not in ignored
            }

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
    for c in claims:
        assert c["old"] == (value(before, c["old_pointer"]) if c["old_pointer"] else None)
        assert c["new"] == value(after, c["pointer"])
        assert c["snippet"] and c["snippet"] in texts[c["source"]]
        assert c["reference"] == context["sources"][c["source"]]["metadata"]["url"]
        assert c["evidence_pointer"] is not None
        (entry,) = [
            e
            for e in get(after, c["evidence_pointer"])["evidence"]
            if e["reference"] == c["reference"]
        ]
        assert c["explanation"] in entry["explanation"]
        assert (
            c["snippet"] == entry["snippet"]
            or "Additional exact excerpt: " + c["snippet"] in entry["explanation"]
        )
        claimed.add((tuple(c["evidence_pointer"]), c["reference"]))
    actual, urls = set(), {s["metadata"]["url"]: k for k, s in context["sources"].items()}
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
            t in ref["notes"]
            for t in (
                "source_type=",
                "discovery_mode=",
                "accessed_on=",
                context["sources"][urls[url]]["metadata"]["sha256"],
            )
        )
        assert ref["notes"].startswith(old_refs.get(url, {}).get("notes", ""))

    relations = {
        "K330": ("D330", "DERIVED_FROM"),
        "K330_17630": ("K330", "STRAIN_SPECIFIC_VARIANT"),
    }
    if key in relations:
        target, relation = relations[key]
        ref = after["parent_media"]
        assert ref["id"] == specs[target]["id"] and ref["path"] == specs[target]["path"]
        assert (
            ref["name"] == yaml.load(specs[target]["before_text"], Loader=yaml.CSafeLoader)["name"]
        )
        assert ref["relationship"] == after["variant_relationship"] == relation
        assert after["variant_modifications"] == [ref["notes"]] and ref["evidence"]
    else:
        for field in ("parent_media", "variant_relationship", "variant_modifications"):
            assert after.get(field) == before.get(field)
    if key in {"D330", "K330"}:
        child = "K330" if key == "D330" else "K330_17630"
        (ref,) = after["variant_children"]
        assert ref["id"] == specs[child]["id"] and ref["path"] == specs[child]["path"]
        assert (
            ref["name"] == yaml.load(specs[child]["before_text"], Loader=yaml.CSafeLoader)["name"]
        )
        assert ref["relationship"] == relations[child][1] and ref["evidence"]
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
            yaml.load(item["before_text"], Loader=yaml.CSafeLoader),
            yaml.load(item["after_text"], Loader=yaml.CSafeLoader),
            item,
        )
        totals.append(result)
        print(json.dumps({"key": item["key"], **result}), flush=True)
    print(json.dumps({"total": {k: sum(r[k] for r in totals) for k in totals[0]}}), flush=True)
