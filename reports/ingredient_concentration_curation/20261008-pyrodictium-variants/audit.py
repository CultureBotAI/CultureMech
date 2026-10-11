"""Independently audit Pyrodictium source rows, duplicate scope and explicit rates."""

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
CONTEXT = HERE.parent / "20261008-basal-makeup/next-pyrodictium-context.json"
SHA = "09b7f63c7eff389cfce01e637008468bf4558ed2ca0a294e70d5d5c5d1b1615a"
ACTION = "RESTORED_PYRODICTIUM_VARIANT_AMOUNTS_AND_STOCK_SCOPES_WITH_EVIDENCE"


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
    raw = CONTEXT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    context = json.loads(raw)
    key = item["key"]
    spec = next(r for r in context["records"] if r["key"] == key)
    assert before == yaml.safe_load(spec["before_text"])
    assert item["action"] == ACTION and item["path"] == spec["path"]
    sources, texts = {}, {}
    for source, capture in context["sources"].items():
        meta = capture["metadata"]
        assert hashlib.sha256(capture["raw"].encode(meta["encoding"])).hexdigest() == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        texts[source] = (
            html_recipe_text(capture["raw"])[0] if source.startswith("JCM") else capture["raw"]
        )
        if source.startswith("M"):
            sources[source] = json.loads(capture["raw"])

    def rows(source, section):
        return sources[source]["components"][section]["items"]

    original = {
        n["preferred_term"]: (f, i)
        for f in ("ingredients", "solutions")
        for i, n in enumerate(before[f])
    }
    expected = {}

    def add(p, source, si, ri, kind, op=None):
        assert p not in expected
        expected[p] = (source, si, ri, kind, op)

    for i, node in enumerate(before["ingredients"]):
        ri, row = next(
            (ri, row)
            for ri, row in enumerate(rows(key, 0))
            if row["component_name"] == node["preferred_term"]
        )
        rate = key != "M196" and (
            node["preferred_term"] == "Yeast extract (BD-Difco)"
            or node["preferred_term"].startswith("Na2WO4")
        )
        kind = (
            "explicit_medium_rate"
            if rate
            else "unquantified_input" if row.get("volume") is None else "batch_mass"
        )
        add(("ingredients", i), key, 0, ri, kind, ("ingredients", i))
    names = [
        "Salt base solution (see Medium [M142])",
        "Trace minerals (see Medium [M142])",
        "5% Na2S\u00b79H2O solution (pH 7.0)",
    ]
    for i, name in enumerate(names):
        ri = next(ri for ri, row in enumerate(rows(key, 0)) if row["component_name"] == name)
        p = ("solutions", i)
        add(p, key, 0, ri, "per_liter_dose" if i == 2 else "batch_dose", original[name])
        if i == 2:
            assert after["solutions"][2]["composition"] == []
            assert "solutions" not in after["solutions"][2]
            continue
        ci = 0
        for j, row in enumerate(rows("M142", i + 1)):
            if row["component_name"] == "KOH solution":
                add(p + ("solutions", 0), "M142", i + 1, j, "unquantified_titrant")
            else:
                add(
                    p + ("composition", ci),
                    "M142",
                    i + 1,
                    j,
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
    stats, lineage = collections.Counter(), []
    for p, (source, si, ri, kind, op) in expected.items():
        node, row = get(after, p), rows(source, si)[ri]
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
            else {"preferred_term": row["component_name"]}
        )
        if old.get("notes"):
            assert node["notes"].startswith(old["notes"] + "\n\n")
        amount, unit = row.get("volume"), row.get("unit")
        if kind in {"batch_mass", "unquantified_input", "unquantified_titrant"}:
            assert "concentration" not in node
            if kind == "batch_mass":
                assert (
                    unit in {"g", "mg"} and f"Source batch input: {amount} {unit}." in node["notes"]
                )
                assert "Final preparation volume is not independently established" in node["notes"]
                if not old:
                    assert "withdrawn" not in node["notes"]
            elif kind == "unquantified_input":
                assert (
                    amount is None
                    and "Removed the unsupported VARIABLE placeholder" in node["notes"]
                )
                assert (
                    "no fixed dose" if row["component_name"] == "H2SO4" else "not a fixed gas input"
                ) in node["notes"]
            else:
                assert amount is None and "no fixed dose" in node["notes"]
            stats["unsupported_quantity_slots_removed"] += bool(old.get("concentration"))
        else:
            if kind == "explicit_medium_rate":
                if row["component_name"].startswith("Na2WO4"):
                    assert key == "M198" and literal_match(
                        "0.1 mg/L Na2WO4\u00b72H2O", texts["JCM205"]
                    )
                    value, out_unit = Decimal("0.1"), "MG_PER_L"
                else:
                    value, out_unit = Decimal("0.2" if key == "M197" else "0.5"), "G_PER_L"
                    assert literal_match(
                        f"{value} g/L (final) yeast extract" + ("." if key == "M197" else ""),
                        texts["JCM204" if key == "M197" else "JCM205"],
                    )
                assert (
                    "explicit medium concentration" in node["notes"]
                    and "No final volume is inferred" in node["notes"]
                )
                stats["explicit_medium_rates_verified"] += 1
            else:
                value = Decimal(str(amount)) / (
                    1000 if unit == "ml" and kind != "per_liter_dose" else 1
                )
                out_unit = "ML_PER_L" if kind == "per_liter_dose" else "L"
            assert set(node["concentration"]) == {"value", "unit"}
            assert Decimal(node["concentration"]["value"]) == value
            assert node["concentration"]["unit"] == out_unit
            if kind == "water":
                assert "not a measured final volume" in node["notes"]
            elif kind == "batch_dose":
                assert (
                    "per receiving batch" in node["notes"]
                    and "does not establish final" in node["notes"]
                )
            elif kind == "per_liter_dose":
                assert (
                    "one later 10 ml per-liter addition" in node["notes"]
                    and "unspecified percentage basis" in node["notes"]
                )
            if old:
                stats[
                    (
                        "stock_dose_basis_corrections"
                        if kind in {"batch_dose", "per_liter_dose"}
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
    if key == "M196":
        assert {k: v for k, v in before["solutions"][3].items() if k != "notes"} == before[
            "solutions"
        ][2]
        assert "Consolidated the duplicate" in after["solutions"][2]["notes"]
        lineage.append(
            {
                "pointer": ["solutions", 2],
                "old_pointer": ["solutions", 2],
                "source": key,
                "source_pointer": ["components", 1, "items", 0],
                "kind": "duplicate_stock_member",
            }
        )
        stats["duplicate_stock_nodes_removed"] = 1
    assert sorted(
        lineage, key=lambda n: (field(n["pointer"]), field(n["old_pointer"] or []))
    ) == sorted(item["lineage"], key=lambda n: (field(n["pointer"]), field(n["old_pointer"] or [])))
    assert {tuple(n["old_pointer"]) for n in lineage if n["old_pointer"]} == {
        (f, i) for f in ("ingredients", "solutions") for i in range(len(before[f]))
    }
    assert after["solutions"][1]["preparation_notes"] == sources["M142"]["comments"][1]["comment"]
    assert (
        after["solutions"][2]["preparation_notes"]
        == "Autoclave and store this stock under N2; add once at 10 ml per liter before inoculation. The source gives no percentage basis or final receiving-medium volume."
    )

    starts = [
        "Mix components except sulfur",
        "Steam sulfur for",
        "Aseptically distribute the medium",
        "Prior to inoculation",
        "Readjust pH to",
        "Pressurize inoculated vessels",
    ]
    text = texts["JCM203"]
    bounds = [text.index(s) for s in starts]
    expected_steps = [
        {
            "step_number": i + 1,
            "action": action,
            "description": text[bounds[i] : bounds[i + 1]].strip(),
        }
        for i, action in enumerate(("AUTOCLAVE", "HEAT", "ALIQUOT", "MIX", "ADJUST_PH"))
    ]
    assert after["preparation_steps"] == expected_steps
    assert after["notes"].startswith(before["notes"] + "\n\n")
    assert (
        "TOGO's inherited preparation says H2-CO4, while original JCM203 specifies H2-CO2"
        in after["notes"]
    )
    assert text[bounds[-1] : text.index(" Copyright")].strip() in after["notes"]
    if key == "M198":
        assert (
            "omission is retained as source context, not an invented ingredient deletion"
            in after["notes"]
        )

    children = ["M197", "M198"] if key == "M196" else [key]
    for i, child in enumerate(children):
        target = child if key == "M196" else "M196"
        target_spec = next(r for r in context["records"] if r["key"] == target)
        target_data = yaml.safe_load(target_spec["before_text"])
        link = after["variant_children"][i] if key == "M196" else after["parent_media"]
        assert set(link) == {"id", "name", "path", "relationship", "notes", "evidence"}
        assert (link["id"], link["name"], link["path"], link["relationship"]) == (
            target_data["id"],
            target_data["name"],
            target_spec["path"],
            "DERIVED_FROM",
        )
        assert (
            "Explicit child rates do not establish a final volume for the parent" in link["notes"]
        )
        stats["variant_links_added"] += 1
    if key == "M196":
        assert len(after["variant_children"]) == 2
    else:
        assert after["variant_relationship"] == "DERIVED_FROM"
        expected_mods = (
            ["Use the source-explicit 0.2 g/L final yeast-extract concentration."]
            if key == "M197"
            else [
                "Use the source-explicit 0.5 g/L final yeast-extract concentration.",
                "Use the source-explicit 0.1 mg/L sodium tungstate dihydrate concentration.",
                "Omit citric acid as instructed by JCM205; none is introduced from the parent or its two referenced stock tables.",
            ]
        )
        assert after["variant_modifications"] == expected_mods
    allowed = {
        "ingredients",
        "solutions",
        "preparation_steps",
        "notes",
        "evidence",
        "references",
        "curation_history",
    } | (
        {"variant_children"}
        if key == "M196"
        else {"parent_media", "variant_relationship", "variant_modifications"}
    )
    assert {k: v for k, v in before.items() if k not in allowed} == {
        k: v for k, v in after.items() if k not in allowed
    }
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert json.loads(event["changes"]) == [
        {k: c[k] for k in ("old_field", "field", "old", "new", "status", "reference", "snippet")}
        for c in item["claims"]
    ]
    old_slots = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    assert {
        tuple(c["old_pointer"])
        for c in item["claims"]
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    } == old_slots
    new_slots = {p + ("concentration",) for p, n in walk(after) if "concentration" in n}
    assert new_slots <= {tuple(c["pointer"]) for c in item["claims"]}
    required_rows = {(key, 0, i) for i in range(len(rows(key, 0)))} | {
        ("M142", s, i) for s in (1, 2) for i in range(len(rows("M142", s)))
    }
    if key == "M196":
        required_rows |= {(key, 1, 0), (key, 1, 1)}
    covered_rows = {
        (c["source"], c["source_pointer"][1], c["source_pointer"][3])
        for c in item["claims"]
        if c["source_pointer"] and c["source_pointer"][0] == "components"
    }
    assert required_rows == covered_rows
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
        assert (
            c["reference"] == meta["url"]
            and c["snippet"]
            and literal_match(c["snippet"], texts[c["source"]])
        )
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
    assert {r["reference"] for r in after["references"]} == {r for p, r in attached}
    assert len(after["references"]) == len({r for p, r in attached})
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
        new_references=len(after["references"]),
        new_curation_history=1,
        old_quantity_slots=len(old_slots),
        claims=len(item["claims"]),
        source_rows=len(required_rows),
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
    (HERE / ("applied-audit.json" if args.applied else "preview-audit.json")).write_text(
        json.dumps(results, indent=2) + "\n"
    )
    print(json.dumps(results))


if __name__ == "__main__":
    main()
