"""Independent source/topology, dimensional and claim-coverage audit for BSK repairs."""

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
SHA = "afef4e855d33495a1e7f54c7e6b809fe345c26533ad19f00a626328bc60136c3"
ACTION = "RESTORED_SOURCE_SPECIFIC_BSK_FORMULATIONS_WITH_INGREDIENT_EVIDENCE"


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
    key = item["key"]
    spec = next(r for r in context["records"] if r["id"] == before["id"])
    assert before == yaml.load(spec["before_text"], Loader=yaml.CSafeLoader)
    assert item["path"] == spec["path"] and item["action"] == ACTION
    texts, data = {}, {}
    for source, capture in context["sources"].items():
        meta, text = capture["metadata"], capture["raw"]
        assert (
            hashlib.sha256(text.encode(meta.get("encoding", "utf-8"))).hexdigest() == meta["sha256"]
        )
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        texts[source] = (
            " ".join(BeautifulSoup(text, "html.parser").get_text().split())
            if source == "JCM173"
            else text
        )
        if source in {"M2410", "D1829", "J173"}:
            data[source] = json.loads(text)
    removed = {
        ("ingredients", i)
        for i in {"D1829": (8, 9, 10), "J173": (1, 2, 3), "M2410": (4, 5, 6)}[key]
    }
    expected = {}

    def add(p, sp, kind, old=None, label=None):
        row = get(data[key], sp) if sp is not None else {}
        label = label or row.get("compound", row.get("component_name"))
        assert p not in expected and label
        expected[p] = (sp, kind, ("ingredients", old) if old is not None else None, label)

    if key == "D1829":
        assert data[key]["data"]["medium"]["id"] == 1829
        assert "Final volume: 100 ml" in texts["DSMZ1829"]
        assert len(after["ingredients"]) == 12 and len(after["solutions"]) == 1
        for ri in range(12):
            add(
                ("ingredients", ri),
                ["data", "solutions", 0, "recipe", ri],
                "makeup" if ri == 11 else "final_volume_rate",
                ri if ri < 8 else {8: None, 9: 11, 10: 12, 11: None}[ri],
            )
        add(("solutions", 0), None, "descriptor", label="NaOH solution (1 M)")
        add(("solutions", 0, "composition", 0), None, "molar_titrant", label="NaOH")
        assert after["ph_value"] == 7.3
        assert [s["action"] for s in after["preparation_steps"]] == ["MIX", "ADJUST_PH", "FILTER"]
        assert "0.22" not in str(after["preparation_steps"])
        assert (
            "no separate makeup-versus-titration order is asserted"
            in after["preparation_steps"][0]["description"]
        )
        assert "no filter pore size" in after["preparation_steps"][2]["description"]
        assert after["ingredients"][8]["notes"].endswith("Fraction V.")
        assert after["ingredients"][10]["notes"].endswith("BioWest Cat No. P0440.")
        assert after["ingredients"][7]["notes"].endswith("Becton Dickinson.")
    elif key == "J173":
        assert data[key]["data"]["medium"]["id"] == "J173"
        assert after["ingredients"] == [] and len(after["solutions"]) == 4
        for si, old_indices in ((1, [0, None, 4, 5, 6, 7, 8, 9, 10, None]), (2, [11, 12, None])):
            add(
                ("solutions", si - 1),
                None,
                "descriptor",
                label="Solution A" if si == 1 else "Solution B",
            )
            assert len(after["solutions"][si - 1]["composition"]) == len(old_indices)
            for ri, old in enumerate(old_indices):
                add(
                    ("solutions", si - 1, "composition", ri),
                    ["data", "solutions", si, "recipe", ri],
                    "water" if ri == len(old_indices) - 1 else "stock_rate",
                    old,
                )
        add(("solutions", 2), None, "descriptor", label="NaOH solution (1 N)")
        add(("solutions", 2, "composition", 0), None, "normality", label="NaOH")
        add(("solutions", 3), None, "heated_serum", label="Heat-inactivated sterile rabbit serum")
        assert "ph_value" not in after
        assert [s["action"] for s in after["preparation_steps"]] == [
            "ADJUST_PH",
            "FILTER_STERILIZE",
            "AUTOCLAVE",
            "MIX",
        ]
        assert "0.22 micrometer" in after["preparation_steps"][1]["description"]
        assert "Solution B separately" in after["preparation_steps"][2]["description"]
        assert (
            "general default is 121 C for 15 min unless otherwise stated"
            in after["preparation_steps"][2]["description"]
        )
        assert (
            "Unless otherwise stated, sterilize media by autoclaving at 121\u00b0C for 15 min."
            in texts["JCM173"]
        )
        assert "with glutamate" in after["solutions"][0]["composition"][0]["notes"]
        assert "Fraction V; Wako" in after["solutions"][0]["composition"][1]["notes"]
        assert "2.5 mg" in after["solutions"][1]["composition"][0]["notes"]
        assert "Neopeptone (BD-Difco) 2.5 mg" in texts["JCM173"]
        assert (
            after["solutions"][0]["composition"][6]["mediaingredientmech_term"]
            == before["ingredients"][8]["mediaingredientmech_term"]
        )
    else:
        assert key == "M2410" and data[key]["meta"]["gm"].endswith("/M2410")
        assert len(after["ingredients"]) == 10 and len(after["solutions"]) == 4
        old_indices = [0, 1, 2, 3, None, 7, 8, 9, 10, 11, 12, 13]
        for i, ri in enumerate((0, 1, 2, 3, 4, 5, 6, 7, 8, 10)):
            add(
                ("ingredients", i),
                ["components", 0, "items", ri],
                "water" if ri == 0 else "batch_mass",
                old_indices[ri],
            )
        add(("solutions", 0), ["components", 0, "items", 9], "batch_dose", 11)
        add(("solutions", 1), None, "descriptor", label="NaOH solution (1 N)")
        add(("solutions", 1, "composition", 0), ["components", 0, "items", 11], "normality", 13)
        add(
            ("solutions", 2),
            None,
            "gelatin_dose",
            label="Gelatin solution (7 percent; basis unspecified)",
        )
        add(("solutions", 2, "composition", 0), None, "gelatin_unknown", label="Gelatin")
        add(("solutions", 3), None, "unheated_serum", label="Unheated rabbit serum")
        assert "ph_value" not in after
        assert [s["action"] for s in after["preparation_steps"]] == [
            "AUTOCLAVE",
            "MIX",
            "DISSOLVE",
            "ADJUST_PH",
            "MIX",
            "FILTER",
            "MIX",
            "ALIQUOT",
        ]
        for ci in (0, 1, 3, 4, 5, 6, 7):
            assert (
                after["preparation_steps"][ci]["description"]
                == data[key]["comments"][ci]["comment"]
            )
        assert (
            "exact addition order remains unresolved"
            in after["preparation_steps"][2]["description"]
        )
        assert "without glutamine" in after["solutions"][0]["preferred_term"]
        assert "No product composition" in after["solutions"][0]["notes"]
        for ci in (8, 9):
            assert data[key]["comments"][ci]["comment"] in after["notes"]
    nodes = {
        p: n
        for p, n in walk(after)
        if "preferred_term" in n
        and p[-2:-1] in {("ingredients",), ("solutions",), ("composition",)}
    }
    assert nodes.keys() == expected.keys()
    stats, mapped, expected_lineage = collections.Counter(), set(), []
    mutable = {
        "concentration",
        "notes",
        "evidence",
        "composition",
        "solutions",
        "preparation_notes",
    }
    for p, (sp, kind, old, label) in expected.items():
        node, previous = nodes[p], get(before, old) if old else {}
        row = get(data[key], sp) if sp is not None else {}
        assert {k: v for k, v in node.items() if k not in mutable} == (
            {k: v for k, v in previous.items() if k not in mutable}
            if old
            else {"preferred_term": label}
        )
        assert not node.get("supplier_catalog")
        if old:
            assert old not in mapped
            mapped.add(old)
            if previous.get("notes"):
                assert node["notes"].startswith(previous["notes"] + "\n\n")
            if p[0] == "solutions":
                stats["stock_nodes_relocated"] += 1
        if kind in {"water", "batch_dose"}:
            amount = row["volume"] if key == "M2410" else row["amount"]
            assert row["unit"] == "ml"
            assert node["concentration"] == {
                "value": number(Decimal(str(amount)) / 1000),
                "unit": "L",
            }
        elif kind == "final_volume_rate":
            assert node["concentration"] == {
                "value": number(Decimal(str(row["amount"])) / Decimal("0.1")),
                "unit": "ML_PER_L" if row["unit"] == "ml" else "G_PER_L",
            }
        elif kind == "stock_rate":
            assert node["concentration"] == {"value": number(row["g_l"]), "unit": "G_PER_L"}
            assert f"source batch input is {row['amount']} {row['unit']}" in node["notes"]
            assert (
                "not as an independently measured final volume or receiving-medium rate"
                in node["notes"]
            )
            stats["stock_stage_concentrations_rebased"] += bool(old)
        elif kind == "molar_titrant":
            assert node["concentration"] == {"value": "1", "unit": "MOLAR"}
        elif kind == "heated_serum":
            assert node["concentration"] == {"value": "0.04", "unit": "L"}
            assert "56 C for 45 min" in node["notes"] and "Pel-Freez" in node["notes"]
        elif kind == "gelatin_dose":
            assert node["concentration"] == {"value": "0.2", "unit": "L"}
            assert (
                "boiling water" in node["preparation_notes"]
                and "No gelatin mass" in node["preparation_notes"]
            )
        else:
            assert "concentration" not in node
            if kind == "batch_mass":
                assert (
                    row["unit"] == "g"
                    and f"Source batch input: {row['volume']} g." in node["notes"]
                )
                assert "No final-medium volume is specified" in node["notes"]
            elif kind == "makeup":
                assert "not a fixed 100 ml water addition" in node["notes"]
            elif kind == "normality":
                assert "1 N" in node["notes"] and "molarity" in node["notes"]
            elif kind == "gelatin_unknown":
                assert (
                    "7 percent" in node["notes"]
                    and "no stated w/v, w/w or v/v basis" in node["notes"]
                )
            elif kind == "unheated_serum":
                assert (
                    "unheated" in node["notes"]
                    and "final 6 percent" in node["notes"]
                    and "neither is guessed" in node["notes"]
                )
            else:
                assert kind == "descriptor"
        if "concentration" in node:
            if "concentration" not in previous:
                stats["new_quantity_slots"] += 1
            elif node["concentration"] != previous["concentration"]:
                stats["quantity_corrections"] += 1
        elif "concentration" in previous:
            stats["unsupported_quantity_slots_removed"] += 1
        if p[-2] == "solutions" and not old:
            stats["stock_descriptors_added"] += 1
        if sp is not None:
            expected_lineage.append(
                {
                    "pointer": list(p),
                    "old_pointer": list(old) if old else None,
                    "source": key,
                    "source_pointer": sp,
                    "kind": kind,
                }
            )
    assert sorted(expected_lineage, key=lambda v: field(v["pointer"])) == sorted(
        item["lineage"], key=lambda v: field(v["pointer"])
    )
    assert mapped | removed == {("ingredients", i) for i in range(len(before["ingredients"]))}
    stats["unsupported_quantity_slots_removed"] += len(removed)
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
    } | ({"ph_value"} if key == "J173" else set())
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
    attached = {}
    for claim in item["claims"]:
        p, op, source = claim["pointer"], claim["old_pointer"], claim["source"]
        assert (
            source in {"M2410"}
            if key == "M2410"
            else source in {key, "DSMZ1829" if key == "D1829" else "JCM173"}
        )
        meta = context["sources"][source]["metadata"]
        assert claim["old"] == (get(before, op[:-1]).get(op[-1]) if op else None)
        assert claim["new"] == get(after, p[:-1]).get(p[-1])
        assert claim["field"] == field(p) and claim["old_field"] == (field(op) if op else None)
        assert (
            claim["reference"] == meta["url"]
            and claim["snippet"]
            and claim["snippet"] in texts[source]
        )
        assert field(p) in claim["explanation"] and meta["sha256"] in claim["explanation"]
        ep = claim["evidence_pointer"]
        assert ep is not None
        identity = (tuple(ep), claim["reference"])
        if identity in attached:
            attached[identity]["explanation"] += (
                "\n\nAdditional exact excerpt: " + claim["snippet"] + "\n" + claim["explanation"]
            )
        else:
            attached[identity] = {
                "reference": claim["reference"],
                "supports": "SUPPORT",
                "snippet": claim["snippet"],
                "explanation": claim["explanation"],
            }
    actual = {(p, e["reference"]): e for p, n in walk(after) for e in n.get("evidence", [])}
    assert actual == attached and sum(len(n.get("evidence", [])) for p, n in walk(after)) == len(
        actual
    )
    assert len(after["references"]) == (1 if key == "M2410" else 2)
    assert {r["reference"] for r in after["references"]} == {ref for p, ref in attached}
    for ref in after["references"]:
        assert set(ref) == {"reference", "title", "notes"}
        source = next(
            k for k, v in context["sources"].items() if v["metadata"]["url"] == ref["reference"]
        )
        expected_title = (
            "Medium data"
            if source == "JCM173"
            else (
                texts[source].splitlines()[0]
                if source == "DSMZ1829"
                else (
                    data[source]["meta"]["name"]
                    if source == "M2410"
                    else data[source]["data"]["medium"]["name"]
                )
            )
        )
        assert ref["title"] == expected_title
        assert all(
            s in ref["notes"]
            for s in (
                "source_type=",
                "discovery_mode=",
                "accessed_on=",
                "capture_sha256=",
                "Authors and publication year are not supplied",
                "copyright year is not publication year",
            )
        )
    stats["preparation_steps_added"] = len(after["preparation_steps"])
    stats["preparation_steps_relocated"] = len(before.get("preparation_steps", []))
    stats["new_evidence"] = len(actual)
    stats["new_references"] = len(after["references"])
    stats["new_curation_history"] = 1
    stats["old_quantity_slots"] = len(old_slots)
    stats["claims"] = len(item["claims"])
    stats["source_rows"] = len(expected_lineage)
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
    output = HERE / ("applied-audit.json" if args.applied else "preview-audit.json")
    assert not output.exists()
    output.write_text(json.dumps(results, indent=2) + "\n")
    print(json.dumps(results))


if __name__ == "__main__":
    main()
