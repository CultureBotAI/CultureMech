"""Independent M689 source-row, quantity, scope, and preservation audit."""

import argparse
import collections
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml

from culturemech.validation.recipe_references import html_recipe_text, literal_match

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SHA = "6b81dbac10cc4ea690b661f517aa88968b1945cb6a4a794c1b642a00f87fbc44"
ACTION = "RESTORED_M689_STOCK_DOSES_AND_COMPOSITIONS_WITH_EVIDENCE"


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


def check(before, after, item):
    raw = (HERE / "context.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    context = json.loads(raw)
    assert before == yaml.load(context["records"][0]["before_text"], Loader=yaml.CSafeLoader)
    assert item["key"] == "M689" and item["action"] == ACTION
    sources, texts = {}, {}
    for key, capture in context["sources"].items():
        meta = capture["metadata"]
        assert hashlib.sha256(capture["raw"].encode(meta["encoding"])).hexdigest() == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        texts[key] = (
            html_recipe_text(capture["raw"])[0] if key.startswith("JCM") else capture["raw"]
        )
        if key.startswith("M"):
            sources[key] = json.loads(capture["raw"])

    expected = {}

    def add(p, source, si, ri, kind, op=None):
        assert p not in expected
        expected[p] = (source, si, ri, kind, op)

    for ri in range(6):
        add(
            ("ingredients", ri),
            "M689",
            0,
            ri,
            "water" if ri == 0 else "unquantified_gas" if ri == 5 else "batch_mass",
            ("ingredients", ri),
        )
    add(("ingredients", 6), "M689", 1, 4, "unquantified_titrant", ("ingredients", 6))
    for i, source, section in [(0, "M180", 1), (1, "M180", 2), (2, "M142", 2), (3, "M190", 1)]:
        p = ("solutions", i)
        add(p, "M689", 1, i, "per_liter_dose", p)
        ci = 0
        for ri, row in enumerate(sources[source]["components"][section]["items"]):
            if (source, section, ri) == ("M180", 1, 0):
                q = p + ("solutions", 0)
                add(q, source, section, ri, "batch_dose")
                add(q + ("composition", 0), source, section, ri, "stock_strength")
            elif row["component_name"] == "KOH solution":
                add(p + ("solutions", 0), source, section, ri, "unquantified_titrant")
            else:
                add(
                    p + ("composition", ci),
                    source,
                    section,
                    ri,
                    "water" if row["component_name"] == "Distilled water" else "batch_mass",
                )
                ci += 1
    actual = {
        p
        for p, n in walk(after)
        if "preferred_term" in n
        and p[-2:-1] in {("ingredients",), ("solutions",), ("composition",)}
    }
    assert actual == set(expected)
    lineage, stats = [], collections.Counter()
    for p, (source, si, ri, kind, op) in expected.items():
        node = get(after, p)
        row = sources[source]["components"][si]["items"][ri]
        old = get(before, op) if op else {}
        excluded = {
            "notes",
            "concentration",
            "composition",
            "solutions",
            "evidence",
            "preparation_notes",
        }
        assert {k: v for k, v in node.items() if k not in excluded} == (
            {k: v for k, v in old.items() if k not in excluded}
            if old
            else {
                "preferred_term": (
                    "HCl reagent (7.7 M)" if kind == "batch_dose" else row["component_name"]
                )
            }
        )
        if kind == "unquantified_gas":
            assert row.get("volume") is None and "concentration" not in node
            assert node["notes"].startswith(old["notes"] + "\n\n")
            assert (
                "N2 atmosphere, not a fixed gas input or dissolved concentration" in node["notes"]
            )
            stats["unsupported_quantity_slots_removed"] += 1
        else:
            if old.get("notes"):
                assert node["notes"].startswith(old["notes"] + "\n\n")
            amount, unit = row.get("volume"), row.get("unit")
            if kind in {"batch_mass", "unquantified_titrant"}:
                assert "concentration" not in node
                if kind == "batch_mass":
                    assert unit in {"g", "mg"}
                    assert f"Source batch input: {amount} {unit}." in node["notes"]
                    assert (
                        "Final preparation volume is not independently established" in node["notes"]
                    )
                    if not old:
                        assert "withdrawn" not in node["notes"]
                else:
                    assert amount is None and "no fixed dose" in node["notes"]
                stats["unsupported_quantity_slots_removed"] += bool(old.get("concentration"))
            else:
                value, out_unit = {
                    "water": (Decimal(str(amount)) / (1000 if unit == "ml" else 1), "L"),
                    "per_liter_dose": (Decimal(str(amount)), "ML_PER_L"),
                    "batch_dose": (Decimal("0.01"), "L"),
                    "stock_strength": (Decimal("7.7"), "MOLAR"),
                }[kind]
                assert set(node["concentration"]) == {"value", "unit"}
                assert Decimal(node["concentration"]["value"]) == value
                assert node["concentration"]["unit"] == out_unit
                if kind == "water":
                    assert "not a measured final volume" in node["notes"]
                if kind in {"batch_dose", "stock_strength"}:
                    assert "25% basis is unspecified" in node["notes"]
                if old:
                    stats[
                        (
                            "stock_dose_basis_corrections"
                            if kind == "per_liter_dose"
                            else "quantity_corrections"
                        )
                    ] += node["concentration"] != old.get("concentration")
                else:
                    stats["new_quantity_slots"] += 1
        lineage.append(
            {
                "pointer": list(p),
                "old_pointer": list(op) if op else None,
                "source": source,
                "source_pointer": ["components", si, "items", ri],
                "kind": kind,
            }
        )
    assert sorted(lineage, key=lambda n: field(n["pointer"])) == sorted(
        item["lineage"], key=lambda n: field(n["pointer"])
    )
    assert after["solutions"][2]["preparation_notes"] == sources["M142"]["comments"][1]["comment"]
    assert (
        after["solutions"][3]["preparation_notes"]
        == "Filter-sterilize this vitamin stock under N2 before its 10 ml/L addition; JCM670 marks this row with an asterisk."
    )
    assert after["preparation_steps"] == [
        {
            "step_number": ci + 1,
            "action": action,
            "description": sources["M689"]["comments"][ci]["comment"],
        }
        for ci, action in enumerate(("AUTOCLAVE", "ADJUST_PH"))
    ]
    assert literal_match("add to the medium (per liter):", texts["JCM670"])
    assert literal_match("Resazurin 0.5 mg", texts["JCM670"])
    assert literal_match("Trace vitamins (see Medium No. 197)* 10.0 ml", texts["JCM670"])
    allowed = {
        "ingredients",
        "solutions",
        "preparation_steps",
        "evidence",
        "references",
        "curation_history",
    }
    assert {k: v for k, v in before.items() if k not in allowed} == {
        k: v for k, v in after.items() if k not in allowed
    }
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert json.loads(event["changes"]) == [
        {k: c[k] for k in ("old_field", "field", "old", "new", "status", "reference", "snippet")}
        for c in item["claims"]
        if c["status"] not in {"unsupported", "evidence_only"}
    ]
    old_slots = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    assert {
        tuple(c["old_pointer"])
        for c in item["claims"]
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    } == old_slots
    new_slots = {p + ("concentration",) for p, n in walk(after) if "concentration" in n}
    assert new_slots <= {tuple(c["pointer"]) for c in item["claims"]}
    for p, (source, si, ri, _kind, _op) in expected.items():
        assert any(
            c["source"] == source
            and c["source_pointer"] == ["components", si, "items", ri]
            and c["pointer"][: len(p)] == list(p)
            for c in item["claims"]
        )
    attached = {}
    for c in item["claims"]:
        p, op = c["pointer"], c["old_pointer"]
        assert c["old"] == (get(before, op[:-1]).get(op[-1]) if op else None)
        assert c["new"] == get(after, p[:-1]).get(p[-1])
        assert c["field"] == field(p) and c["old_field"] == (field(op) if op else None)
        meta = context["sources"][c["source"]]["metadata"]
        assert c["reference"] == meta["url"]
        assert c["snippet"] and literal_match(c["snippet"], texts[c["source"]])
        assert field(p) in c["explanation"] and meta["sha256"] in c["explanation"]
        ep = c["evidence_pointer"]
        assert ep is not None
        identity = (tuple(ep), c["reference"])
        if identity in attached:
            attached[identity]["explanation"] += (
                "\n\nAdditional exact excerpt: " + c["snippet"] + "\n" + c["explanation"]
            )
        else:
            attached[identity] = {
                "reference": c["reference"],
                "supports": "SUPPORT",
                "snippet": c["snippet"],
                "explanation": c["explanation"],
            }
    actual = {(p, e["reference"]): e for p, n in walk(after) for e in n.get("evidence", [])}
    assert actual == attached
    assert sum(len(n.get("evidence", [])) for p, n in walk(after)) == len(actual)
    assert len(after["references"]) == len({r for p, r in attached}) == 8
    for ref in after["references"]:
        assert set(ref) == {"reference", "title", "notes"}
        source = next(
            k for k, s in context["sources"].items() if s["metadata"]["url"] == ref["reference"]
        )
        assert ref["title"] == (
            "Medium data" if source.startswith("JCM") else sources[source]["meta"]["name"]
        )
        assert "Authors and publication year not supplied" in ref["notes"]
        assert all(
            t in ref["notes"]
            for t in ("source_type=", "discovery_mode=", "accessed_on=", "capture_sha256=")
        )
    stats.update(
        new_evidence=len(actual),
        new_references=8,
        new_curation_history=1,
        old_quantity_slots=len(old_slots),
        claims=len(item["claims"]),
        source_rows=47,
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
        results[item["key"]] = check(
            yaml.load(item["before_text"], Loader=yaml.CSafeLoader),
            yaml.load(raw, Loader=yaml.CSafeLoader),
            item,
        )
    (HERE / ("applied-audit.json" if args.applied else "preview-audit.json")).write_text(
        json.dumps(results, indent=2) + "\n"
    )
    print(json.dumps(results))


if __name__ == "__main__":
    main()
