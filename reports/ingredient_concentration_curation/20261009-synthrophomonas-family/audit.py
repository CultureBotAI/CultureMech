"""Independent medium212 source projection and append-only provenance checks."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter
from decimal import Decimal
from functools import cache
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

from culturemech.validation.recipe_references import html_recipe_text, parse_recipe, recipe_source

HERE = Path(__file__).resolve().parent
CONTEXT_SHA = "1d9b09a2915e57c4f212f1de08bb1a5ada6b2a4b8a47b6b6c5d528d00250e84a"
ACTION = "RESTORED_SYNTHROPHOMONAS_SOURCE_FORMULATIONS_WITH_EVIDENCE"
IDENTITY_SHA = "2f6d107a2c1042092e4402085f5941f969e5aa2a601f4a77b79747c93d5cc6b2"


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


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


def amounts_equal(actual, expected):
    if expected is None or expected["unit"] == "VARIABLE":
        return actual == expected
    return (
        actual is not None
        and set(actual) == {"value", "unit"}
        and actual["unit"] == expected["unit"]
        and Decimal(actual["value"]) == Decimal(expected["value"])
    )


@cache
def snapshot(raw):
    assert sha(raw) == CONTEXT_SHA
    context = json.loads(raw)
    data, texts, titles = {}, {}, {}
    for key, source in context["sources"].items():
        raw, meta = source["raw"], source["metadata"]
        assert sha(raw.encode()) == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        adapter = recipe_source(meta["url"])
        if adapter:
            parsed = parse_recipe(adapter, raw, meta)
            texts[key], titles[key] = parsed.content, parsed.title
        else:
            texts[key], titles[key] = html_recipe_text(raw)
        if key == "K212":
            (table,) = [
                t
                for t in BeautifulSoup(raw, "html.parser").find_all("table")
                if "Gram Amount" in t.get_text()
            ]
            rows = [
                [html_recipe_text(str(c))[0] for c in tr.find_all("td", recursive=False)]
                for tr in table.find_all("tr")
            ]
            assert rows.pop(0) == [
                "Name",
                "Semi unique name",
                "Unique Name",
                "Gram Amount",
                "Mol Amount",
            ]
            assert len(rows) == 32 and all(len(r) == 5 for r in rows)
            data[key] = [
                (r[0], None if r[3] == "null" else {"value": r[3], "unit": "G_PER_L"}) for r in rows
            ]
        elif key == "B2805":
            (table,) = [
                t
                for t in BeautifulSoup(raw, "html.parser").find_all("table")
                if "Na-propionate" in t.get_text()
            ]
            lines = table.get_text(" ", strip=True).split("Composition:\n")[1].splitlines()
            assert len(lines) == 33
            data[key] = []
            for line in lines:
                if line == "Distilled water":
                    label, quantity = line, None
                else:
                    match = re.fullmatch(
                        r"(.+?) ([0-9]+(?:\.[0-9]+)?(?:[eE][+-]?[0-9]+)?) g/l", line
                    )
                    assert match
                    label, number = match.groups()
                    quantity = {"value": number, "unit": "G_PER_L"}
                data[key].append((label, quantity))
        elif key in {"DSMZ212", "DSMZ212a"}:
            stage, rows = "main assembly", []
            headings = {"Solution " + letter for letter in "ABCDEFGHI"}
            headings.update(
                {
                    "Trace element solution SL-10",
                    "Selenite-tungstate solution",
                    "Clarified rumen fluid",
                    "Seven vitamins solution",
                    "Vitamin K1 solution",
                    "Volatile fatty acid mixture",
                    "Sugar mix",
                }
            )
            for line_no, line in enumerate(raw.splitlines(), 1):
                heading = line.strip().split(" (from medium", 1)[0]
                if heading in headings:
                    stage = heading
                match = re.fullmatch(r"\s*(.+?)\s+(\d+(?:\.\d+)?)\s+(g|mg|ml)\s*", line)
                if match:
                    label, amount, unit = match.groups()
                    rows.append(
                        {
                            "stage": stage,
                            "label": label,
                            "amount": amount,
                            "unit": unit,
                            "line": line_no,
                        }
                    )
            assert len(rows) == (49 if key == "DSMZ212" else 74)
            data[key] = rows
        elif key.startswith("S") or key in {"D212", "D212a"}:
            data[key] = json.loads(raw)["data"]
    return context, data, texts, titles


def projection(key, data):
    expected = {}
    if key in {"K212", "B2805"}:
        for i, (label, quantity) in enumerate(data[key]):
            expected[("ingredients", i)] = {
                "label": label,
                "quantity": quantity,
                "source": key,
                "descriptor": False,
            }
    elif key.startswith("S"):
        rows = data[key]["recipe"]
        order = [r for r in rows if not r.get("solution_id")] + [
            r for r in rows if r.get("solution_id")
        ]
        for i, row in enumerate(order):
            label = row.get("compound") or row["solution"]
            if key == "S595" and label == "Distilled water":
                quantity = {"value": "to 1 L final volume", "unit": "VARIABLE"}
            elif row["unit"] == "ml":
                quantity = {"value": str(Decimal(str(row["amount"])) / 1000), "unit": "L"}
            else:
                assert row.get("g_l") is not None
                quantity = {"value": str(row["g_l"]), "unit": "G_PER_L"}
            expected[("composition", i)] = {
                "label": label,
                "quantity": quantity,
                "source": key,
                "descriptor": False,
                "row": row,
            }
    else:
        source = "DSMZ" + key[1:]
        rows = data[source]
        stages = {r["stage"] for r in rows} | {"Clarified rumen fluid"}

        def descend(stage, path, seen=()):
            assert stage not in seen
            count = Counter()
            for row in (r for r in rows if r["stage"] == stage):
                label = row["label"]
                descriptor = label in stages
                field = "solutions" if descriptor else "composition"
                pointer = path + (field, count[field])
                count[field] += 1
                if stage == "Trace element solution SL-10" and label == "Distilled water":
                    quantity = {"value": "to 1 L final volume", "unit": "VARIABLE"}
                elif row["unit"] == "ml":
                    quantity = {"value": str(Decimal(row["amount"]) / 1000), "unit": "L"}
                elif stage == "Trace element solution SL-10":
                    quantity = {
                        "value": str(
                            Decimal(row["amount"])
                            * (Decimal("0.001") if row["unit"] == "mg" else 1)
                        ),
                        "unit": "G_PER_L",
                    }
                else:
                    quantity = None
                expected[pointer] = {
                    "label": label,
                    "quantity": quantity,
                    "source": source,
                    "descriptor": descriptor,
                    "row": row,
                }
                if descriptor:
                    descend(label, pointer, seen + (stage,))

        descend("main assembly", ())
        assert len(expected) == len(rows)
    return expected


def check(before, after, item):
    context, data, texts, titles = snapshot((HERE / "context.json").read_bytes())
    specs = {r["key"]: r for r in context["records"]}
    key, spec = item["key"], specs[item["key"]]
    raw_identity = (HERE / "identity-review.json").read_bytes()
    assert sha(raw_identity) == IDENTITY_SHA
    identity = {i["key"]: i for i in json.loads(raw_identity)["issues"]}
    assert before == yaml.safe_load(spec["before_text"])
    assert after == yaml.safe_load(item["after_text"])
    assert sha(item["after_text"].encode()) == item["after_sha256"]
    assert before["id"] == after["id"] == spec["id"] and item["path"] == spec["path"]
    assert item["action"] == ACTION
    expected = projection(key, data)
    actual = {
        p: n
        for p, n in walk(after)
        if p and p[0] in {"ingredients", "composition", "solutions"} and "preferred_term" in n
    }
    lineage = {tuple(r["pointer"]): r for r in item["lineage"]}
    assert len(lineage) == len(item["lineage"]) and set(actual) == set(expected) == set(lineage)
    aliases = {
        "Trypticase peptone (BD BBL)": "Trypticase peptone",
        "Sodium resazurin (0.1% w/v)": "Sodium resazurin",
        "HCl (25%)": "HCl",
        "Ethanol (95 %)": "Ethanol",
        "Starch (soluble)": "Starch",
        "DL-Dithiothreitol (DTT)": "DL-Dithiothreitol",
    }
    if key == "K212":
        aliases = {
            "Pyridoxine-HCl": "Pyridoxine hydrochloride",
            "Cysteine-HCl x H2O": "L-Cysteine HCl x H2O",
            "Resazurin": "Sodium resazurin",
            "Trypticase": "Trypticase peptone",
        }
    old_nodes = {
        p: n
        for p, n in walk(before)
        if p and p[0] in {"ingredients", "composition", "solutions"} and "preferred_term" in n
    }
    for path, row in expected.items():
        node, line = actual[path], lineage[path]
        assert node["preferred_term"] == row["label"]
        assert amounts_equal(node.get("concentration"), row["quantity"]), (
            key,
            path,
            node.get("concentration"),
            row,
        )
        assert line["source"] == row["source"] and line["label"] == row["label"]
        candidates = [
            p
            for p, n in old_nodes.items()
            if n["preferred_term"].casefold() == aliases.get(row["label"], row["label"]).casefold()
            and "LB Medium" not in n.get("supplier_catalog", {}).get("supplier_name", "")
        ]
        assert len(candidates) <= 1
        old_path = candidates[0] if candidates else None
        assert line["old_pointer"] == (list(old_path) if old_path else None)
        if row["descriptor"]:
            assert node["name"] == row["label"]
            assert set(node) <= {
                "name",
                "preferred_term",
                "concentration",
                "composition",
                "solutions",
                "notes",
            }
        else:
            old = old_nodes.get(old_path, {})
            fields = set(node) | set(old)
            for f in fields - {
                "preferred_term",
                "concentration",
                "notes",
                "evidence",
                "culturemech_term",
            }:
                withdrawn = (
                    row["label"] == "NiCl2 x 6 H2O"
                    and key in identity
                    and f in identity[key]["old_fields"]
                )
                if withdrawn:
                    assert old[f] == identity[key]["old_fields"][f] and f not in node
                else:
                    assert node.get(f) == old.get(f), (key, path, f)
            if row.get("row", {}).get("solution_id"):
                sid = "S" + str(row["row"]["solution_id"])
                assert node.get("culturemech_term") == (
                    {"id": specs[sid]["id"], "label": row["label"]} if sid in specs else None
                )
            else:
                assert node.get("culturemech_term") == old.get("culturemech_term")
        if row["source"].startswith("DSMZ"):
            assert f"{row['row']['amount']} {row['row']['unit']}" in node["notes"]
            assert line["source_pointer"] == ["PDF extracted line", row["row"]["line"]]

    covered_old, covered_new = set(), set()
    for claim in item["claims"]:
        p = claim["pointer"]
        old_p = claim["old_pointer"]
        assert claim["new"] == value(after, p)
        assert claim["old"] == (value(before, old_p) if old_p else None)
        if p[-1] == "concentration" and claim["new"] is not None and claim["old"] == claim["new"]:
            assert claim["status"] in {"verified", "evidence_only"}
        meta = context["sources"][claim["source"]]["metadata"]
        assert claim["reference"] == meta["url"]
        assert claim["snippet"] and claim["snippet"] in texts[claim["source"]]
        if old_p:
            covered_old.add(tuple(old_p))
        covered_new.add(tuple(p))
        if claim["evidence_pointer"] is not None:
            container = get(after, claim["evidence_pointer"])
            entries = [
                e for e in container.get("evidence", []) if e["reference"] == claim["reference"]
            ]
            assert len(entries) == 1 and entries[0]["supports"] == "SUPPORT"
            assert (
                claim["snippet"] == entries[0]["snippet"]
                or claim["snippet"] in entries[0]["explanation"]
            )
            assert claim["explanation"] in entries[0]["explanation"]
        else:
            assert claim["status"] == "verified" and p[-1] == "concentration"
            entries = get(after, p[:-1])["evidence"]
            assert any(
                e["reference"] == claim["reference"] and e.get("snippet") in texts[claim["source"]]
                for e in entries
            )
    old_quantities = {p + ("concentration",) for p, n in old_nodes.items() if "concentration" in n}
    assert old_quantities <= covered_old
    assert {p + ("concentration",) for p in expected} <= covered_new
    assert len(item["claims"]) == len(
        {
            (
                tuple(c["pointer"]),
                tuple(c["old_pointer"] or []),
                c["kind"],
                c["source"],
                c["snippet"],
            )
            for c in item["claims"]
        }
    )

    preserved, extended = 0, 0
    for p, old in walk(before):
        if len(p) >= 2 and p[-2] == "evidence":
            new = get(after, p)
            assert {k: v for k, v in new.items() if k != "explanation"} == {
                k: v for k, v in old.items() if k != "explanation"
            }
            assert new["explanation"].startswith(old["explanation"])
            preserved += 1
            extended += new != old
    references = {r["reference"]: r for r in after.get("references", [])}
    assert len(references) == len(after.get("references", []))
    for p, node in walk(after):
        if (not p or p[0] != "curation_history") and "evidence" in node:
            assert len({e["reference"] for e in node["evidence"]}) == len(node["evidence"])
            for e in node["evidence"]:
                if e.get("snippet"):
                    assert e["reference"] in references
                    (source,) = [
                        s
                        for s in context["sources"].values()
                        if s["metadata"]["url"] == e["reference"]
                    ]
                    (skey,) = [k for k, s in context["sources"].items() if s is source]
                    assert e["snippet"] in texts[skey]
    for r in after.get("references", []):
        matching = [
            k for k, s in context["sources"].items() if s["metadata"]["url"] == r["reference"]
        ]
        if r.get("title"):
            assert matching and r["title"] == titles[matching[0]]
        assert "authors" not in r and "year" not in r
    allowed = {
        "ingredients",
        "composition",
        "solutions",
        "notes",
        "evidence",
        "references",
        "curation_history",
    }
    if key.startswith("S"):
        allowed.add("data_quality_flags")
        assert "evidence" not in after and "source_data" not in after
        assert "ingredients" not in after and "incomplete_composition" not in after.get(
            "data_quality_flags", []
        )
    if key in {"K212", "D212", "D212a"}:
        allowed.update(
            {
                "high_metal",
                "parent_media",
                "variant_children",
                "variant_relationship",
                "variant_modifications",
            }
        )
        assert "high_metal" not in after
    for field in (set(before) | set(after)) - allowed:
        assert before.get(field) == after.get(field), (key, field)
    if key == "S608":
        assert after == before and item["after_text"] == item["before_text"]
    else:
        assert after["curation_history"][:-1] == before["curation_history"]
        event = after["curation_history"][-1]
        assert event["action"] == ACTION and event["curator"] == "codex"
        assert json.loads(event["changes"]) == [
            {
                k: c[k]
                for k in ("old_field", "field", "old", "new", "status", "reference", "snippet")
            }
            for c in item["claims"]
        ]
    if key in {"D212", "D212a"}:
        assert after["ingredients"] == [] and len(after["solutions"]) == (6 if key == "D212" else 9)
        assert ("1003.00 ml" if key == "D212" else "1008.00 ml") in after["notes"]
        assert ("942.50 ml" if key == "D212" else "916.60 ml") in after["notes"]
    if key == "K212":
        assert (
            after["parent_media"]["id"] == specs["D212"]["id"]
            and after["parent_media"]["relationship"] == "DERIVED_FROM"
        )
        assert "variant_children" not in after and not after.get("solutions")
    if key == "D212":
        assert after["variant_children"][0] == before["variant_children"][0]
        assert (
            len(after["variant_children"]) == 2
            and after["variant_children"][1]["id"] == specs["K212"]["id"]
        )
        assert after["variant_children"][1]["relationship"] == "DERIVED_FROM"
    if key == "D212a":
        assert not set(after) & {"parent_media", "variant_relationship", "variant_modifications"}
    return {
        "key": key,
        "source_nodes": len(expected),
        "old_quantity_slots": len(old_quantities),
        "claims": len(item["claims"]),
        "prior_evidence_content_preserved": preserved,
        "prior_evidence_explanations_extended": extended,
        "changed": after != before,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=HERE / "plan-v2.json")
    parser.add_argument("--out", type=Path, default=HERE / "independent-successor-audit.json")
    args = parser.parse_args()
    plan = json.loads(args.plan.read_text())
    context, _, _, _ = snapshot((HERE / "context.json").read_bytes())
    assert {r["key"] for r in plan["records"]} == {r["key"] for r in context["records"]}
    results = [
        check(yaml.safe_load(r["before_text"]), yaml.safe_load(r["after_text"]), r)
        for r in plan["records"]
    ]
    for r in context["records"]:
        assert sha(Path(r["path"]).read_bytes()) == r["before_sha256"]
    out = {
        "terminal": True,
        "auditor_sha256": sha(Path(__file__).read_bytes()),
        "identity_review_sha256": IDENTITY_SHA,
        "plan_sha256": sha(args.plan.read_bytes()),
        "context_sha256": CONTEXT_SHA,
        "records_edited": 0,
        "results": results,
        "totals": {k: sum(r[k] for r in results) for k in results[0] if k != "key"},
        "all_record_goal_complete": False,
        "independent_source_projection_passed": True,
        "limits": [
            "Local preview only; no source YAML edited.",
            "BacDive page evidence is checked against the captured HTML, not a verified DOI-version PDF.",
            "Chemical annotations are preserved, not certified by quantity evidence.",
            "Per-record external validators, runtime merging, and independent adjudication remain required before application.",
        ],
    }
    with args.out.open("x") as handle:
        json.dump(out, handle, indent=2)
        handle.write("\n")
    print(json.dumps(out["totals"]))


if __name__ == "__main__":
    main()
