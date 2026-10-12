"""Independently reconstruct the source topology and audit every changed claim."""

import argparse
import collections
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
SHA = "5767d9b9bed74466a4f490abe98b1d9735d7b864cfaec8af0d83b29520ee7cdb"
ACTION = "RESTORED_DSMZ_ALBUMIN_PREPARATIONS_AND_CONCENTRATION_SCOPES_WITH_EVIDENCE"


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


def number(value):
    return format(Decimal(str(value)).normalize(), "f")


def check(before, after, item):
    raw = (HERE / "context.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    context = json.loads(raw)
    key, medium = item["key"], item["key"][1:]
    api, pdf = "D" + medium, "DSMZ" + medium
    spec = next(r for r in context["records"] if r["key"] == key)
    assert before == yaml.load(spec["before_text"], Loader=yaml.CSafeLoader)
    assert item["action"] == ACTION and item["path"] == spec["path"]
    texts = {k: v["raw"] for k, v in context["sources"].items()}
    for capture in context["sources"].values():
        meta = capture["metadata"]
        assert hashlib.sha256(capture["raw"].encode(meta["encoding"])).hexdigest() == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
    data = json.loads(texts[api])["data"]
    assert data["medium"]["id"] == int(medium) and data["medium"]["source"] == "DSMZ"
    sections = data["solutions"]
    assert [s["id"] for s in sections] == ([818, 819, 820, 821, 822] if medium == "403" else [1537])
    removed = {("ingredients", i) for i in ([13, 14, 15] if medium == "403" else [6, 7, 8])}
    originals = {
        n["preferred_term"]: ("ingredients", i)
        for i, n in enumerate(before["ingredients"])
        if ("ingredients", i) not in removed
    }
    expected = {}

    def add(p, si, ri, kind, label=None, old=None, lineage=True):
        row = sections[si]["recipe"][ri] if si is not None else {}
        assert p not in expected
        expected[p] = (
            si,
            ri,
            kind,
            label or row.get("compound", row.get("solution")),
            old,
            lineage,
        )

    if medium == "403":
        assert after["ingredients"] == []
        for si in range(3):
            add(("solutions", si), 0, si, "batch_dose")
        add(("solutions", 3), 4, 0, "batch_dose", old=originals["Rabbit serum"])
        for si in (1, 2, 3):
            offset = 1 if si == 1 else 0
            for ri in range(offset, len(sections[si]["recipe"])):
                row = sections[si]["recipe"][ri]
                old = (
                    originals.get(row["compound"])
                    if not (si > 1 and "water" in row["compound"].lower())
                    else None
                )
                add(
                    ("solutions", si - 1, "composition", ri - offset),
                    si,
                    ri,
                    "water" if row["unit"] == "ml" else "stock_rate",
                    old=old,
                )
        add(("solutions", 0, "solutions", 0), 1, 0, "batch_dose", old=originals["CMRL 1066"])
        add(
            ("solutions", 0, "solutions", 1),
            None,
            None,
            "titrant",
            "NaOH solution (5 M)",
            lineage=False,
        )
        add(
            ("solutions", 0, "solutions", 1, "composition", 0),
            None,
            None,
            "titrant_strength",
            "NaOH",
            originals.get("NaOH"),
            lineage=key == "K403",
        )
        assert [len(s["composition"]) for s in after["solutions"]] == [11, 2, 2, 0]
        assert after["solutions"][0]["solutions"][0]["composition"] == []
        assert "ph_value" not in after
        for i in range(3):
            assert (
                after["solutions"][i]["preparation_notes"]
                == sections[i + 1]["steps"][0]["step"].strip()
            )
        assert after["preparation_steps"] == [
            {"step_number": 1, "action": "MIX", "description": sections[0]["steps"][0]["step"]}
        ]
        assert sections[0]["steps"][1]["step"] in after["notes"]
        assert "Source alternative, not an extra preparation step:" in after["notes"]
        assert "BSA-solution Sigma A7409" in after["solutions"][2]["preparation_notes"]
        assert "50.05" in after["solutions"][2]["preparation_notes"]
        assert "mmol_l" not in str(after["solutions"][3].get("concentration"))
    else:
        for i, ri in enumerate((0, 1, 2, 3, 4, 6)):
            row = sections[0]["recipe"][ri]
            add(
                ("ingredients", i),
                0,
                ri,
                "water" if ri == 6 else "batch_mass",
                old=originals.get(row["compound"]),
            )
        for i, ri in enumerate((5, 7, 8, 9)):
            row = sections[0]["recipe"][ri]
            add(("solutions", i), 0, ri, "batch_dose", row["compound"] + " stock")
            add(
                ("solutions", i, "composition", 0),
                0,
                ri,
                "unknown_stock_strength",
                old=originals.get(row["compound"]),
            )
            assert len(after["solutions"][i]["composition"]) == 1
            if i:
                assert (
                    after["solutions"][i]["preparation_notes"]
                    == "Filter-sterilize this stock separately; add after the basal medium has been autoclaved and cooled to 50 C. No filter pore size is given."
                )
            else:
                assert "preparation_notes" not in after["solutions"][i]
        add(
            ("solutions", 0, "solutions", 0),
            None,
            None,
            "solvent",
            "NaOH solution (0.05 N)",
            lineage=False,
        )
        add(
            ("solutions", 0, "solutions", 0, "composition", 0),
            None,
            None,
            "solvent_component",
            "NaOH",
            lineage=False,
        )
        assert sections[0]["steps"][0]["recipe_order"] == 8
        assert after["ph_value"] == 6.6 and after["physical_state"] == "SOLID_AGAR"
        assert [s["action"] for s in after["preparation_steps"]] == [
            "ADJUST_PH",
            "AUTOCLAVE",
            "COOL",
        ]
        assert [s["description"] for s in after["preparation_steps"]] == [
            "Adjust the basal medium to pH 6.6 before autoclaving.",
            "Autoclave the basal medium, including the hemin input; the source gives no fixed cycle temperature or duration.",
            "Cool to 50 C, then add the separately filter-sterilized albumin, glucose and cysteine stocks.",
        ]
        assert len(after["variants"]) == 1
        variant = after["variants"][0]
        assert (
            variant["name"] == "Liquid SC medium"
            and variant["relationship"] == "PHYSICAL_STATE_VARIANT"
        )
        assert variant["modifications"] == [
            "Omit corn meal agar.",
            "Use KH2PO4 1.5 g per batch instead of 1 g.",
            "Use K2HPO4 0.5 g per batch instead of 1 g.",
        ]
        assert (
            "not a sequential change" in variant["description"]
            and variant["purpose"] == "Liquid medium"
        )
    nodes = {
        p: n
        for p, n in walk(after)
        if "preferred_term" in n
        and p[-2:-1] in {("ingredients",), ("solutions",), ("composition",)}
    }
    assert nodes.keys() == expected.keys()
    stats, mapped, lineage = collections.Counter(), set(), []
    mutable = {
        "concentration",
        "notes",
        "evidence",
        "composition",
        "solutions",
        "preparation_notes",
    }
    for p, (si, ri, kind, label, old, has_lineage) in expected.items():
        node, original = nodes[p], get(before, old) if old else {}
        row = sections[si]["recipe"][ri] if si is not None else {}
        assert {k: v for k, v in node.items() if k not in mutable} == (
            {k: v for k, v in original.items() if k not in mutable}
            if old
            else {"preferred_term": label}
        )
        assert not node.get("supplier_catalog")
        if old:
            assert old not in mapped
            mapped.add(old)
            if original.get("notes"):
                assert node["notes"].startswith(original["notes"] + "\n\n")
            if p[0] == "solutions":
                stats["stock_nodes_relocated"] += 1
        if kind in {"water", "batch_dose"}:
            assert row["unit"] == "ml"
            assert node["concentration"] == {
                "value": number(Decimal(str(row["amount"])) / 1000),
                "unit": "L",
            }
            assert (
                "not a measured final volume"
                if kind == "water"
                else "per receiving batch, not g/L or a per-liter dose"
            ) in node["notes"]
            stats[
                (
                    ("quantity_corrections" if kind == "water" else "stock_dose_basis_corrections")
                    if old
                    else "new_quantity_slots"
                )
            ] += 1
        elif kind == "stock_rate":
            assert node["concentration"] == {"value": number(row["g_l"]), "unit": "G_PER_L"}
            assert f"Source batch input: {row['amount']} g." in node["notes"]
            assert f"provider-declared stock g_l={row['g_l']}" in node["notes"]
            assert "not a receiving-medium concentration" in node["notes"]
            stats["stock_stage_concentrations_rebased" if old else "new_quantity_slots"] += 1
        elif kind == "titrant_strength":
            assert node["concentration"] == {"value": "5", "unit": "MOLAR"}
            assert (
                "Solution A to pH 7.6" in node["notes"] and "No fixed titrant dose" in node["notes"]
            )
            stats["stock_stage_concentrations_rebased" if old else "new_quantity_slots"] += 1
        else:
            assert "concentration" not in node
            if kind == "batch_mass":
                assert f"Source batch input: {row['amount']} g." in node["notes"]
                assert "Final-medium volume is not established" in node["notes"]
            elif kind == "unknown_stock_strength":
                assert (
                    row["attribute"] in node["notes"]
                    and "Percentage basis is unspecified" in node["notes"]
                )
                if row["compound"] == "Bovine serum albumin":
                    assert "fraction V" in node["notes"]
            elif kind == "titrant":
                assert "No fixed titrant dose" in node["notes"]
            elif kind == "solvent":
                assert (
                    node["notes"]
                    == "Hemin-stock solvent only; fixed solvent dose and percentage basis are not supplied."
                )
            elif kind == "solvent_component":
                assert (
                    node["notes"]
                    == "Source solvent strength 0.05 N; normality is not converted to molarity."
                )
            else:
                raise AssertionError(kind)
            if old:
                stats["unsupported_quantity_slots_removed"] += 1
            elif p[-2] == "composition":
                stats["unquantified_carrier_nodes_added"] += 1
        if p[-2] == "solutions" and not old:
            stats["stock_descriptors_added"] += 1
        if has_lineage:
            lineage.append(
                {
                    "pointer": list(p),
                    "old_pointer": list(old) if old else None,
                    "source": api if si is not None else pdf,
                    "source_pointer": (
                        ["data", "solutions", si, "recipe", ri] if si is not None else None
                    ),
                    "kind": kind,
                }
            )
    if medium == "403":
        lineage.append(
            {
                "pointer": ["solutions", 3],
                "old_pointer": None,
                "source": api,
                "source_pointer": ["data", "solutions", 0, "recipe", 3],
                "kind": "same_serum_dose",
            }
        )
    assert sorted(lineage, key=lambda x: (field(x["pointer"]), str(x["source_pointer"]))) == sorted(
        item["lineage"], key=lambda x: (field(x["pointer"]), str(x["source_pointer"]))
    )
    assert mapped | removed == {("ingredients", i) for i in range(len(before["ingredients"]))}
    stats["unsupported_quantity_slots_removed"] += 3
    assert {
        tuple(c["old_pointer"][:-1]) for c in item["claims"] if c["kind"] == "false_lb_removed"
    } == removed
    marker = "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product:"
    assert marker in after["notes"] and after["notes"].replace(
        marker, "\n\nCommercial Product:", 1
    ).startswith(before["notes"] + "\n\n")
    allowed = {
        "ingredients",
        "solutions",
        "notes",
        "preparation_steps",
        "evidence",
        "references",
        "curation_history",
        "variants",
    } | ({"ph_value"} if medium == "403" else set())
    assert {k: v for k, v in before.items() if k not in allowed} == {
        k: v for k, v in after.items() if k not in allowed
    }
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["curator"] == "codex" and event["action"] == ACTION
    assert json.loads(event["changes"]) == [
        {k: c[k] for k in ("old_field", "field", "old", "new", "status", "reference", "snippet")}
        for c in item["claims"]
    ]
    old_slots = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    new_slots = {p + ("concentration",) for p, n in walk(after) if "concentration" in n}
    assert {
        tuple(c["old_pointer"])
        for c in item["claims"]
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    } == old_slots
    assert new_slots <= {tuple(c["pointer"]) for c in item["claims"]}
    rows = {(si, ri) for si, section in enumerate(sections) for ri in range(len(section["recipe"]))}
    assert {
        (c["source_pointer"][2], c["source_pointer"][4])
        for c in item["claims"]
        if c["source"] == api
        and c["source_pointer"]
        and len(c["source_pointer"]) == 5
        and c["source_pointer"][3] == "recipe"
    } == rows
    attached = {}
    for c in item["claims"]:
        p, op, source = c["pointer"], c["old_pointer"], c["source"]
        assert source in {api, pdf}
        meta = context["sources"][source]["metadata"]
        assert c["old"] == (get(before, op[:-1]).get(op[-1]) if op else None)
        assert c["new"] == get(after, p[:-1]).get(p[-1])
        assert c["field"] == field(p) and c["old_field"] == (field(op) if op else None)
        assert c["reference"] == meta["url"] and c["snippet"] and c["snippet"] in texts[source]
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
    assert actual == attached and sum(len(n.get("evidence", [])) for p, n in walk(after)) == len(
        actual
    )
    assert len(after["references"]) == 2
    assert {r["reference"] for r in after["references"]} == {ref for p, ref in attached}
    for ref in after["references"]:
        assert set(ref) == {"reference", "title", "notes"}
        assert ref["title"] == (
            texts[pdf].splitlines()[0]
            if ref["reference"] == context["sources"][pdf]["metadata"]["url"]
            else data["medium"]["name"]
        )
        assert all(
            s in ref["notes"]
            for s in (
                "source_type=",
                "discovery_mode=",
                "accessed_on=",
                "capture_sha256=",
                "Authors and publication year are not supplied",
                "copyright year is not treated as publication year",
            )
        )
    stats["preparation_steps_relocated"] += len(before.get("preparation_steps", []))
    stats["preparation_steps_added"] += len(after["preparation_steps"])
    stats["inline_variant_options_added"] += len(after.get("variants", []))
    stats["new_evidence"] = len(actual)
    stats["new_references"] = 2
    stats["new_curation_history"] = 1
    stats["old_quantity_slots"] = len(old_slots)
    stats["claims"] = len(item["claims"])
    stats["source_rows"] = len(rows)
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
