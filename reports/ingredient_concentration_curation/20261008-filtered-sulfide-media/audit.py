"""Independently verify filtered-medium stock scope, amounts and literal evidence."""

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
SHA = "9ef2e61a0c079c15a0cc2577004711a46a8d425872737561c8e333a2655490d4"
ACTION = "RESTORED_FILTERED_MEDIA_STOCK_SCOPES_AND_BATCH_AMOUNTS_WITH_EVIDENCE"


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
    key = item["key"]
    spec = next(r for r in context["records"] if r["key"] == key)
    assert before == yaml.load(spec["before_text"], Loader=yaml.CSafeLoader)
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

    number = {"M199": "206", "M206": "213", "M207": "214"}[key]
    text = texts["JCM" + number]
    assert sources[key]["meta"]["original_media_id"] == "JCM_M" + number
    original = {
        n["preferred_term"]: (f, i)
        for f in ("ingredients", "solutions")
        for i, n in enumerate(before[f])
    }
    assert len(original) == sum(len(before[f]) for f in ("ingredients", "solutions"))
    expected = {}

    def add(p, source, si, ri, kind, op=None):
        assert p not in expected
        expected[p] = (source, si, ri, kind, op)

    di, stock_rows = 0, []
    for ri, row in enumerate(rows(key, 0)):
        name = row["component_name"]
        if row.get("reference_media_id"):
            stock_rows.append(ri)
        elif name != "Na2S\u30fb9H2O":
            kind = (
                "unquantified_input"
                if row.get("volume") is None
                else "water" if name == "Distilled water" else "batch_mass"
            )
            add(("ingredients", di), key, 0, ri, kind, original[name])
            di += 1
    for i, ri in enumerate(stock_rows):
        row = rows(key, 0)[ri]
        p = ("solutions", i)
        add(p, key, 0, ri, "batch_dose", original[row["component_name"]])
        salt = row["component_name"].startswith("Salt base")
        source, si = (key, 1) if salt else ("M142", 2)
        ci = 0
        for j, child in enumerate(rows(source, si)):
            name = child["component_name"]
            op = original[name] if salt else None
            if name == "KOH solution":
                add(p + ("solutions", 0), source, si, j, "unquantified_titrant")
                continue
            kind = (
                "explicit_stock_rate"
                if salt and name in {"NaCl", "KI"}
                else "water" if name == "Distilled water" else "batch_mass"
            )
            add(p + ("composition", ci), source, si, j, kind, op)
            if salt and kind != "explicit_stock_rate":
                assert all(
                    child.get(k) == rows("M142", 1)[j].get(k)
                    for k in ("component_name", "volume", "unit")
                )
            ci += 1
    sulfide_ri = next(
        i for i, row in enumerate(rows(key, 0)) if row["component_name"] == "Na2S\u30fb9H2O"
    )
    sulfide = ("solutions", len(stock_rows))
    add(sulfide, key, 0, sulfide_ri, "separate_preparation")
    add(sulfide + ("composition", 0), key, 0, sulfide_ri, "batch_mass", original["Na2S\u30fb9H2O"])
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
        label = row["component_name"] + (
            " separately prepared solution" if kind == "separate_preparation" else ""
        )
        assert {k: v for k, v in node.items() if k not in excluded} == (
            {k: v for k, v in old.items() if k not in excluded}
            if old
            else {"preferred_term": label}
        )
        if old.get("notes"):
            assert node["notes"].startswith(old["notes"] + "\n\n")
        if op and op[0] == "ingredients" and p[0] == "solutions":
            stats["stock_nodes_relocated"] += 1
        amount, unit = row.get("volume"), row.get("unit")
        if kind in {
            "batch_mass",
            "unquantified_input",
            "unquantified_titrant",
            "separate_preparation",
        }:
            assert "concentration" not in node
            if kind == "batch_mass":
                assert (
                    unit in {"g", "mg"} and f"Source batch input: {amount} {unit}." in node["notes"]
                )
                assert "Final preparation volume is not independently established" in node["notes"]
                if not old:
                    assert "withdrawn" not in node["notes"]
                if p == sulfide + ("composition", 0):
                    assert amount == 0.5 and unit == "g"
                    assert "contribution specified for the receiving medium batch" in node["notes"]
            elif kind == "unquantified_input":
                assert (
                    amount is None
                    and "Removed the unsupported VARIABLE placeholder" in node["notes"]
                )
                assert (
                    "no fixed dose" if row["component_name"] == "H2SO4" else "not a fixed gas input"
                ) in node["notes"]
                if row["component_name"] == "H2SO4":
                    assert ("1 N H2SO4" in node["notes"]) == (key == "M206")
            elif kind == "unquantified_titrant":
                assert amount is None and "no fixed dose" in node["notes"]
                assert node["composition"] == [] and not node.get("solutions")
            else:
                assert (
                    "0.5 g receiving-batch contribution, not a stock-batch recipe" in node["notes"]
                )
                assert "Stock solvent volume and addition volume are unspecified" in node["notes"]
                assert len(node["composition"]) == 1 and not node.get("solutions")
                assert ("source 5% label has unspecified percentage basis" in node["notes"]) == (
                    key != "M207"
                )
                if key == "M207":
                    assert "JCM214 gives no stock strength" in node["notes"]
                stats["stock_descriptors_added"] += 1
            stats["unsupported_quantity_slots_removed"] += bool(old.get("concentration"))
        else:
            if kind == "explicit_stock_rate":
                assert key == "M199" and source == key and si == 1
                assert literal_match(
                    "17.0 g/L (final) NaCl and 2.5 mg/L (final) KI.", texts["JCM206"]
                )
                value, out_unit = (
                    (Decimal("17"), "G_PER_L")
                    if row["component_name"] == "NaCl"
                    else (Decimal("2.5"), "MG_PER_L")
                )
                assert (
                    "final salt-base stock concentration" in node["notes"]
                    and "not a receiving-medium concentration" in node["notes"]
                )
                stats["stock_stage_concentrations_rebased"] += 1
            else:
                assert unit in {"ml", "L"}
                value = Decimal(str(amount)) / (1000 if unit == "ml" else 1)
                out_unit = "L"
            assert set(node["concentration"]) == {"value", "unit"}
            assert (
                Decimal(node["concentration"]["value"]) == value
                and node["concentration"]["unit"] == out_unit
            )
            if kind == "water":
                assert "not a measured final volume" in node["notes"]
            elif kind == "batch_dose":
                assert (
                    "per receiving batch" in node["notes"]
                    and "not grams per liter or a dose per final liter" in node["notes"]
                )
            if old:
                stats[
                    (
                        "stock_dose_basis_corrections"
                        if kind == "batch_dose"
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
    assert {tuple(n["old_pointer"]) for n in lineage if n["old_pointer"]} == {
        (f, i) for f in ("ingredients", "solutions") for i in range(len(before[f]))
    }
    trace = after["solutions"][1 if key == "M199" else 0]
    assert trace["preparation_notes"] == sources["M142"]["comments"][1]["comment"]
    assert literal_match(trace["preparation_notes"], texts["JCM151"])

    starts = ["Mix ingredients", "Sterilize by filtration"]
    actions = ["MIX", "FILTER"]
    if key == "M199":
        starts += ["Steam sulfur", "Neutralize", "Aseptically", "Prior to inoculation"]
        actions += ["HEAT", "AUTOCLAVE", "MIX", "MIX"]
    else:
        starts += ["Neutralize", "Aseptically"]
        actions += ["AUTOCLAVE", "MIX"]
    starts += ["Pressurize"]
    bounds = [text.index(s) for s in starts]
    steps = [
        {
            "step_number": i + 1,
            "action": action,
            "description": text[bounds[i] : bounds[i + 1]].strip(),
        }
        for i, action in enumerate(actions)
    ]
    assert after["preparation_steps"] == steps
    assert (
        get(after, sulfide)["preparation_notes"] == steps[3 if key == "M199" else 2]["description"]
    )
    end = text.index(" Salt base solution:") if key == "M199" else text.index(" Copyright")
    pressure = text[bounds[-1] : end].strip()
    assert (
        after["notes"] == before["notes"] + "\n\nOriginal post-inoculation instruction: " + pressure
    )
    allowed = {
        "ingredients",
        "solutions",
        "preparation_steps",
        "notes",
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
    ]
    old_slots = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    assert {
        tuple(c["old_pointer"])
        for c in item["claims"]
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    } == old_slots
    new_slots = {p + ("concentration",) for p, n in walk(after) if "concentration" in n}
    assert new_slots <= {tuple(c["pointer"]) for c in item["claims"]}
    required_rows = {
        (key, s, i)
        for s in range(len(sources[key]["components"]))
        for i in range(len(rows(key, s)))
    } | {("M142", 2, i) for i in range(len(rows("M142", 2)))}
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
