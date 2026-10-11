"""Project medium161 claims directly from captured sources, without the builder."""

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
PREP = HERE.parent / "20261009-rumen-bacteria-family"
CONTEXT_SHA = "7c14648ed630e165a4ebc834b0ff55f560e11cfc50f1507a6776b90c99b413b0"
ACTION = "RESTORED_METHANOFOLLIS_SOURCE_FORMULATIONS_WITH_EVIDENCE"


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
def snapshot(raw):
    assert hashlib.sha256(raw).hexdigest() == CONTEXT_SHA
    context = json.loads(raw)
    assert context["terminal"] and not context["errors"]
    data, texts, titles = {}, {}, {}
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        assert hashlib.sha256(raw.encode()).hexdigest() == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        parsed = parse_recipe(recipe_source(meta["url"]), raw, meta)
        texts[key], titles[key] = parsed.content, parsed.title
        if key == "K161":
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
            assert len(data[key]) == 43
        elif key == "DSMZ161":
            stage, page, rows = "main formulation", 1, []
            headings = {
                "Clarified rumen fluid (from medium 1310)": "clarified fluid procedure",
                "Modified Wolin's mineral solution (from medium 141)": "mineral stock",
                "Fatty acid mixture (from medium 119)": "fatty-acid stock",
                "Wolin's vitamin solution (10x) (from medium 120)": "vitamin stock",
            }
            for line in raw.splitlines():
                if "Page 1 of 2" in line:
                    page = 2
                if line.strip() in headings:
                    stage = headings[line.strip()]
                match = re.fullmatch(r"\s*(.+?)\s+(\d+(?:\.\d+)?)\s+(g|mg|ml)\s*", line)
                if match and not line.startswith("Final volume:"):
                    label, amount, unit = match.groups()
                    assert stage != "clarified fluid procedure"
                    rows.append((stage, page, " ".join(label.split()), amount, unit))
            assert len(rows) == 50 and "Final volume: 1001 ml" in raw
            data[key] = rows
        else:
            data[key] = json.loads(raw)
    return context, data, texts, titles


def batch(amount, unit):
    if unit == "ml":
        return {"value": str(Decimal(str(amount)) / 1000), "unit": "L"}
    assert unit in {"g", "mg"}
    return None


def check(before, after, item):
    context, data, texts, titles = snapshot((PREP / "next-161-context-approved.json").read_bytes())
    specs = {r["key"]: r for r in context["records"]}
    key, spec = item["key"], specs[item["key"]]
    assert before == yaml.safe_load(spec["before_text"])
    assert before["id"] == after["id"] == spec["id"] and item["path"] == spec["path"]
    assert item["action"] == ACTION
    expected = {}

    def old_for(label):
        aliases = {
            "D-Ca-pantothenate": "Calcium D-(+)-pantothenate",
            "Lipoic acid": "(DL)-alpha-Lipoic acid",
            "Cysteine-HCl x H2O": "L-Cysteine HCl x H2O",
            "Thiamine-HCl x 2 H2O": "Thiamine HCl",
            "Pyridoxine HCl": "Pyridoxine hydrochloride",
            "Resazurin": "Sodium resazurin",
            "KAl(SO4)2 x 12 H2O": "AlK(SO4)2 x 12 H2O",
            "Trypticase (BBL)": "Trypticase",
            "Yeast extract (Difco)": "Yeast extract",
            "Yeast extract (DIFCO)": "Yeast extract",
            "CaCl2 x 2 H2O (0.1% w/v)": "CaCl2 x 2 H2O",
            "FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4)": "FeSO4 x 7 H2O",
            "Sodium resazurin (0.1% w/v)": "Sodium resazurin",
        }
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

    if key == "K161":
        for i, row in enumerate(data[key]):
            add(
                ("ingredients", i),
                row[0],
                None if row[3] == "null" else {"value": row[3], "unit": "G_PER_L"},
                key,
                ["Metabolites list", i],
            )
        assert not after.get("solutions") and after["ph_value"] == 6.5
        assert "provider assertion" in after["notes"] and "conflicts" in after["notes"]
        assert get(after, ("ingredients", 18))["term"] == {"id": "CHEBI:8806", "label": "Resazurin"}
        assert (
            get(after, ("ingredients", 4))["term"]
            == get(before, old_for("Cysteine-HCl x H2O"))["term"]
        )
    elif key == "D161":
        direct, counts, stocks = 0, {}, {}
        stage_labels = {
            "mineral stock": "Modified Wolin's mineral solution",
            "fatty-acid stock": "Fatty acid mixture",
            "vitamin stock": "Wolin's vitamin solution (10x)",
        }
        for stage, page, label, amount, unit in data["DSMZ161"]:
            ri = counts.get(stage, 0)
            counts[stage] = ri + 1
            descriptor = stage == "main formulation" and label in set(stage_labels.values()) | {
                "Clarified rumen fluid"
            }
            if descriptor:
                path = ("solutions", len(stocks))
                stocks[label] = path
            elif stage == "main formulation":
                path = ("ingredients", direct)
                direct += 1
            else:
                path = stocks[stage_labels[stage]] + ("composition", ri)
            quantity = batch(amount, unit)
            if stage == "main formulation" and unit == "g":
                quantity = {
                    "value": format(Decimal(amount) / Decimal("1.001"), ".6g"),
                    "unit": "G_PER_L",
                }
                assert (
                    "1.001 L" in get(after, path)["notes"]
                    and "Final volume: 1001 ml" in get(after, path)["notes"]
                )
            add(path, label, quantity, "DSMZ161", [f"page {page}, {stage}", ri], descriptor)
            assert f"{amount} {unit} per preparation" in get(after, path)["notes"]
        for stage, label in (("mineral stock", "KOH"), ("fatty-acid stock", "NaOH")):
            add(
                stocks[stage_labels[stage]] + ("composition", counts[stage]),
                label,
                None,
                "DSMZ161",
                ["page2", stage, "titration"],
            )
        clarified = get(after, stocks["Clarified rumen fluid"])
        assert "composition" not in clarified and "culturemech_term" not in clarified
        assert "30% vial-fill instruction concerns storage" in clarified["notes"]
        assert "1001.5ml" in after["notes"] and "six significant digits" in after["notes"]
        assert after["preparation_steps"] == before["preparation_steps"]
    else:
        rows = data[key]["data"]["recipe"]
        order = [(ri, row) for ri, row in enumerate(rows) if not row.get("solution_id")]
        ordinary_count = len(order)
        order += [(ri, row) for ri, row in enumerate(rows) if row.get("solution_id")]
        for oi, (ri, row) in enumerate(order):
            quantity = batch(row["amount"], row["unit"])
            if row["unit"] != "ml" and row.get("g_l") is not None:
                quantity = {"value": str(row["g_l"]), "unit": "G_PER_L"}
            add(
                ("composition", oi),
                row.get("compound") or row["solution"],
                quantity,
                key,
                ["data", "recipe", ri],
                old=("composition", oi) if oi < ordinary_count else None,
                stock=row.get("solution_id") if row.get("solution_id") != 2618 else None,
            )
            retained = oi < ordinary_count and before["composition"][oi].get("evidence")
            if row.get("attribute") and not retained:
                assert row["attribute"] in after["composition"][oi]["notes"]
            if row.get("solution_id") == 2618:
                assert "culturemech_term" not in after["composition"][oi]
        if key in {"S241", "S209"}:
            label = "KOH" if key == "S241" else "NaOH"
            add(("composition", len(order)), label, None, key, ["data", "steps", 0, "step"])
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
            if key == "K161" and want["label"] == "Thiamine-HCl x 2 H2O":
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

    if key == "K161":
        assert "variant_children" not in after
        ref = after["parent_media"]
        assert ref["id"] == specs["D161"]["id"] and ref["path"] == specs["D161"]["path"]
        assert ref["name"] == yaml.safe_load(specs["D161"]["before_text"])["name"]
        assert ref["relationship"] == after["variant_relationship"] == "DERIVED_FROM"
        assert after["variant_modifications"] == [ref["notes"]] and ref["evidence"]
    elif key == "D161":
        assert not {"parent_media", "variant_relationship", "variant_modifications"} & after.keys()
        (ref,) = after["variant_children"]
        assert ref["id"] == specs["K161"]["id"] and ref["path"] == specs["K161"]["path"]
        assert ref["name"] == yaml.safe_load(specs["K161"]["before_text"])["name"]
        assert ref["relationship"] == "DERIVED_FROM" and ref["evidence"]
    else:
        for field in (
            "parent_media",
            "variant_relationship",
            "variant_modifications",
            "variant_children",
        ):
            assert after.get(field) == before.get(field)
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
            yaml.safe_load(item["before_text"]), yaml.safe_load(item["after_text"]), item
        )
        totals.append(result)
        print(json.dumps({"key": item["key"], **result}), flush=True)
    print(json.dumps({"total": {k: sum(r[k] for r in totals) for k in totals[0]}}), flush=True)
