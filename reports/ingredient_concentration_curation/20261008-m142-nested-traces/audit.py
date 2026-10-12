"""Independent source-tree, unit, provenance and annotation audit."""

import argparse
import collections
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SHA = "c5f79b827061f21a92b21ae48aca670d408a0efbe88b52b48e0d8ea95923c1aa"


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
    assert before == yaml.load(
        next(r for r in context["records"] if r["key"] == key)["before_text"],
        Loader=yaml.CSafeLoader,
    )
    sources, texts = {}, {}
    for name, capture in context["sources"].items():
        meta = capture["metadata"]
        assert hashlib.sha256(capture["raw"].encode(meta["encoding"])).hexdigest() == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        texts[name] = (
            " ".join(BeautifulSoup(capture["raw"], "html.parser").get_text().split())
            if name.startswith("JCM")
            else capture["raw"]
        )
        if name.startswith("M"):
            sources[name] = json.loads(capture["raw"])

    # Inspected definition placement, independent of the repair's LINKS/MAIN logic.
    s0, s1 = ("solutions", 0), ("solutions", 1)
    sections = {
        "M933": {0: (), 1: (), 2: s0, 3: s0 + s0},
        "M1106": {0: (), 1: (), 2: s0, 3: s1},
        "M1124": {0: (), 1: (), 2: s1},
        "M1153": {0: (), 1: (), 2: s0, 3: s1},
        "M1378": {0: (), 1: s1},
        "M1389": {0: (), 1: (), 2: s0, 3: s0 + s0},
        "M1390": {0: (), 1: (), 2: (), 3: s0, 4: s0 + s0},
    }[key]
    base_path = {
        "M933": s0 + s0 + s0,
        "M1106": s0 + s0,
        "M1124": s1 + s0,
        "M1153": s0 + s0,
        "M1378": s1 + s0,
        "M1389": s0 + s0 + s0,
        "M1390": s0 + s0 + s0,
    }[key]
    originals = {
        n["preferred_term"]: (f, i)
        for f in ("ingredients", "solutions")
        for i, n in enumerate(before.get(f, []))
    }
    expected, source_rows = {}, []
    for source, mapping in [(key, sections), ("M142", {2: base_path})]:
        for si, parent in mapping.items():
            for ri, row in enumerate(sources[source]["components"][si]["items"]):
                name = row["component_name"]
                kind = "batch_mass"
                if row.get("volume") is None:
                    kind = "unquantified_titrant" if name == "KOH solution" else "gas"
                elif name == "Distilled water":
                    kind = "water"
                elif row.get("unit") in {"ml", "L"}:
                    kind = "batch_dose"
                if (
                    source == key
                    and (key, si) in {("M933", 1), ("M1389", 1), ("M1390", 2)}
                    and kind == "batch_dose"
                ):
                    kind = "per_liter_dose"
                if key == "M1153" and source == key and si == 3 and ri in {0, 1}:
                    kind = "makeup_reagent" if ri == 0 else "stock_rate"
                if key == "M1378" and source == key and (si, ri) == (0, 8):
                    kind, parent = "stock_strength", s0
                field_name = (
                    "solutions"
                    if kind
                    in {"batch_dose", "per_liter_dose", "makeup_reagent", "unquantified_titrant"}
                    else "composition" if parent else "ingredients"
                )
                candidates = [
                    (i, n)
                    for i, n in enumerate(get(after, parent).get(field_name, []))
                    if n["preferred_term"] == name
                ]
                assert len(candidates) == 1, (key, source, si, ri, parent, name)
                index, node = candidates[0]
                p = parent + (field_name, index)
                source_rows.append((source, si, ri, p, kind))
                if p in expected:
                    assert kind == "gas", "Only unquantified gas mentions may be deduplicated"
                else:
                    expected[p] = (source, si, ri, kind)
                parent = mapping[si]
    actual_nodes = {
        p
        for p, n in walk(after)
        if p
        and p[-2:-1] in {("ingredients",), ("solutions",), ("composition",)}
        and "preferred_term" in n
    }
    assert actual_nodes == set(expected) | ({s0} if key == "M1378" else set())
    assert get(after, base_path)["preferred_term"] == "Trace minerals (see Medium [M142])"
    assert get(after, base_path)["preparation_notes"] == sources["M142"]["comments"][1]["comment"]
    if key in {"M1106", "M1153"}:
        assert get(after, s1)["preparation_notes"] == sources[key]["comments"][1]["comment"]

    seen, removed, stats, lineage = set(), set(), collections.Counter(), []
    for p, (source, si, ri, kind) in expected.items():
        n = get(after, p)
        row = sources[source]["components"][si]["items"][ri]
        op = originals.get(row["component_name"]) if source == key else None
        old = get(before, op) if op else {}
        if op:
            seen.add(op)
        excluded = {
            "concentration",
            "notes",
            "evidence",
            "composition",
            "solutions",
            "preparation_notes",
        }
        assert {k: v for k, v in n.items() if k not in excluded} == (
            {k: v for k, v in old.items() if k not in excluded}
            if old
            else {"preferred_term": row["component_name"]}
        )
        if kind == "gas":
            assert n == old and row.get("volume") is None
        else:
            if old.get("notes"):
                assert n["notes"].startswith(old["notes"] + "\n\n")
                if "[Merged 2 duplicates:" in old["notes"]:
                    assert "duplicate-summing note is superseded" in n["notes"]
            amount, unit = row.get("volume"), row.get("unit")
            if kind in {"batch_mass", "makeup_reagent", "unquantified_titrant"}:
                assert "concentration" not in n
                if old.get("concentration"):
                    removed.add(op)
                if kind == "batch_mass":
                    assert (
                        unit in {"g", "mg"}
                        and f"Source batch input: {amount} {unit}." in n["notes"]
                    )
                    assert "Final preparation volume is not independently established" in n["notes"]
                elif kind == "makeup_reagent":
                    assert (
                        "0.1 N H2SO4" in n["notes"]
                        and "actual acid addition volume is unspecified" in n["notes"]
                    )
                else:
                    assert amount is None and "no fixed dose" in n["notes"]
            else:
                expected_value, expected_unit = {
                    "water": (Decimal(str(amount)) / (1000 if unit == "ml" else 1), "L"),
                    "batch_dose": (Decimal(str(amount)) / (1000 if unit == "ml" else 1), "L"),
                    "per_liter_dose": (
                        Decimal(str(amount)) * (1000 if unit == "L" else 1),
                        "ML_PER_L",
                    ),
                    "stock_rate": (Decimal(400), "G_PER_L"),
                    "stock_strength": (Decimal(8), "PERCENT_W_V"),
                }[kind]
                assert set(n["concentration"]) == {"value", "unit"}
                assert (
                    Decimal(n["concentration"]["value"]) == expected_value
                    and n["concentration"]["unit"] == expected_unit
                )
                if kind == "stock_rate":
                    assert "40.0 g / 0.1 L = 400 g/L" in n["notes"]
                if kind == "stock_strength":
                    assert "1.0 g / 0.08 g/ml = 12.5 ml" in n["notes"]
                if kind == "batch_dose":
                    assert "per receiving batch" in n["notes"]
                if kind == "water":
                    assert "not a measured final volume" in n["notes"]
                if row.get("conc_unit") == "%":
                    assert "Percentage basis is unspecified" in n["notes"]
                if row.get("conc_unit") == "N":
                    assert "normality is not converted to molarity" in n["notes"]
                if op and n["concentration"] != old.get("concentration"):
                    stats[
                        (
                            "stock_stage_concentrations_rebased"
                            if kind in {"stock_rate", "stock_strength"}
                            else (
                                "stock_dose_basis_corrections"
                                if kind.endswith("dose")
                                else "quantity_corrections"
                            )
                        )
                    ] += 1
                if not op:
                    stats["new_quantity_slots"] += 1
        stats["stock_nodes_relocated"] += bool(
            op and op[0] == "ingredients" and p[0] == "solutions"
        )
        lineage.append(
            {
                "pointer": list(p),
                "old_pointer": list(op) if op else None,
                "source": source,
                "source_pointer": ["components", si, "items", ri],
                "kind": kind,
            }
        )
    assert seen == set(originals.values())
    assert sorted(lineage, key=lambda x: field(x["pointer"])) == sorted(
        item["lineage"], key=lambda x: field(x["pointer"])
    )
    if key == "M1378":
        assert get(after, s0)["concentration"] == {"value": "0.0125", "unit": "L"}
        assert get(after, s0)["preferred_term"] == "NaHCO3 separately prepared solution"
        assert "1.0 g / 0.08 g/ml = 12.5 ml" in get(after, s0)["notes"]
        stats["new_quantity_slots"] += 1
        stats["stock_descriptors_added"] += 1
    if key == "M1153":
        assert (
            "apparent formula discrepancy is unresolved"
            in get(after, s0)["composition"][2]["notes"]
        )

    steps = []
    for ci, comment in enumerate(sources[key]["comments"]):
        if ci == 1 and key in {"M1106", "M1153"}:
            continue
        if (key == "M933" and ci == 1) or (key == "M1390" and ci == 2):
            assert comment["comment"] in after["notes"]
            continue
        action = (
            "HEAT"
            if key == "M1124" and ci == 0
            else (
                "ALIQUOT"
                if key == "M1390" and ci == 1
                else "ADJUST_PH" if key == "M1389" and ci == 1 else "AUTOCLAVE"
            )
        )
        steps.append(
            {"step_number": len(steps) + 1, "action": action, "description": comment["comment"]}
        )
    assert after["preparation_steps"] == steps
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
    assert after["notes"] == before["notes"] or after["notes"].startswith(before["notes"] + "\n\n")
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["curator"] == "codex" and event["action"] == item["action"]
    event_changes = json.loads(event["changes"])
    assert event_changes == [
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
    for source, si, ri, p, _kind in source_rows:
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
        assert c["reference"] == context["sources"][c["source"]]["metadata"]["url"]
        assert c["snippet"] and c["snippet"] in texts[c["source"]]
        assert field(p) in c["explanation"] and "capture SHA256=" in c["explanation"]
        ep = c["evidence_pointer"]
        if ep is None:
            assert c["kind"] == "gas" and c["status"] == "unsupported"
            continue
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
        unsupported_quantity_slots_removed=len(removed),
        new_evidence=len(actual),
        new_references=len(after["references"]),
        new_curation_history=1,
        old_quantity_slots=len(old_slots),
        claims=len(item["claims"]),
        source_rows=len(source_rows),
    )
    return dict(stats)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--applied", action="store_true")
    args = parser.parse_args()
    plan = json.loads((HERE / "plan.json").read_text())
    results = {}
    for r in plan["records"]:
        raw = (ROOT / r["path"]).read_bytes() if args.applied else r["after_text"].encode()
        assert hashlib.sha256(raw).hexdigest() == r["after_sha256"]
        results[r["key"]] = check(
            yaml.load(r["before_text"], Loader=yaml.CSafeLoader),
            yaml.load(raw, Loader=yaml.CSafeLoader),
            r,
        )
    (HERE / ("applied-audit.json" if args.applied else "preview-audit.json")).write_text(
        json.dumps(results, indent=2) + "\n"
    )
    print(json.dumps(results))


if __name__ == "__main__":
    main()
