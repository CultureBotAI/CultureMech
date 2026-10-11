"""Independently audit the four albumin repairs against pinned source rows."""

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
SHA = "a4853a8d073e506bf37fb1952d47551a3b84a94f5429b687c33b13f1340cd7f8"
ACTION = "RESTORED_ALBUMIN_COUNTERPART_IDENTITIES_AND_STOCK_CONCENTRATIONS_WITH_EVIDENCE"


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
    assert before == yaml.safe_load(spec["before_text"])
    assert item["action"] == ACTION and item["path"] == spec["path"]
    data, texts = {}, {}
    for source, capture in context["sources"].items():
        meta = capture["metadata"]
        assert hashlib.sha256(capture["raw"].encode(meta["encoding"])).hexdigest() == meta["sha256"]
        assert meta["http_status"] == 200 and meta["url"] == meta["response_url"]
        texts[source] = (
            html_recipe_text(capture["raw"])[0] if source.startswith("JCM") else capture["raw"]
        )
        if not source.startswith("JCM"):
            data[source] = json.loads(capture["raw"])
    assert "Nothing found." in texts["JCM201"]
    assert context["source_issues"] == {"JCM201": "source_unavailable: JCM returned no recipe"}
    rows = (
        data[key]["data"]["solutions"][0]["recipe"]
        if key == "J252"
        else data[key]["components"][0]["items"]
    )
    number = {"M194": "201", "M213": "220", "M244": "252", "J252": "252"}[key]
    if key == "J252":
        assert data[key]["data"]["medium"]["id"] == key
        assert data[key]["data"]["solutions"][0]["id"] == 3938
    else:
        assert data[key]["meta"]["original_media_id"] == "JCM_M" + number
    assert len(rows) == {"M194": 12, "M213": 10, "M244": 16, "J252": 15}[key]
    removed = {
        ("ingredients", i)
        for i in {"M194": [7, 8, 9], "M213": [2, 3, 4], "M244": [10, 11, 12], "J252": [1, 2, 3]}[
            key
        ]
    }
    originals = {
        n["preferred_term"]: ("ingredients", i)
        for i, n in enumerate(before["ingredients"])
        if ("ingredients", i) not in removed
    }
    expected = {}

    def add(p, ri, kind, *, label=None, op=None, lineage=True):
        name = rows[ri].get("compound", rows[ri].get("component_name")) if ri is not None else None
        assert p not in expected
        expected[p] = (ri, kind, label or name, op, lineage)

    direct = {
        "M194": [1, 2, 3, 4, 5, 6, 7, 8, 10],
        "M213": [3, 4, 5, 6, 8, 9],
        "M244": [0, 1, 2, 3, 5, 6, 7, 8, 9, 11, 12, 14, 15],
        "J252": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14],
    }[key]
    for i, ri in enumerate(direct):
        name = rows[ri].get("compound", rows[ri].get("component_name"))
        add(
            ("ingredients", i),
            ri,
            (
                "water"
                if name == "Distilled water"
                else "unquantified_gas" if name == "N2" else "batch_mass"
            ),
            op=originals.get(name),
        )
    if key == "M194":
        add(("solutions", 0), 0, "batch_dose", label="7% gelatin solution")
        add(("solutions", 0, "composition", 0), 0, "unquantified_strength", op=originals["gelatin"])
        add(("solutions", 1), 9, "batch_dose", op=originals["CMRL 1066 (Gibco 330--1540)"])
        add(("solutions", 2), 11, "unquantified_serum", op=originals["sterile rabbit serum"])
    elif key == "M213":
        for si, (ri, label) in enumerate(
            ((0, "Glucose"), (1, "Cysteine"), (2, "Bovine serum albumin, fraction V"), (7, "Hemin"))
        ):
            add(("solutions", si), ri, "batch_dose", op=originals.get(rows[ri]["component_name"]))
            add(("solutions", si, "composition", 0), ri, "unquantified_strength", label=label)
        add(
            ("solutions", 3, "solutions", 0),
            None,
            "solvent",
            label="NaOH solution (0.05 N)",
            lineage=False,
        )
        add(
            ("solutions", 3, "solutions", 0, "composition", 0),
            None,
            "solvent_component",
            label="NaOH",
            lineage=False,
        )
    else:
        row_ids = [13, 10, 4] if key == "M244" else [0, 1, 12]
        labels = [
            "10% yeast extract solution",
            "10% (w/v) bovine serum albumin solution",
            "5% neutralized sodium sulfide nonahydrate solution",
        ]
        for si, ri in enumerate(row_ids):
            p = ("solutions", si)
            add(p, ri, "albumin_dose" if si == 1 else "prepared", label=labels[si], lineage=False)
            name = rows[ri].get("compound", rows[ri].get("component_name"))
            add(
                p + ("composition", 0),
                ri,
                "albumin_strength" if si == 1 else "batch_mass",
                op=originals.get(name),
            )
    actual_nodes = {
        p
        for p, n in walk(after)
        if "preferred_term" in n
        and p[-2:-1] in {("ingredients",), ("solutions",), ("composition",)}
    }
    assert actual_nodes == set(expected)
    stats, lineage, mapped = collections.Counter(), [], set()
    for p, (ri, kind, label, op, has_lineage) in expected.items():
        node, old = get(after, p), get(before, op) if op else {}
        row = rows[ri] if ri is not None else {}
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
            else {"preferred_term": label}
        )
        if op:
            mapped.add(op)
            if old.get("notes"):
                assert node["notes"].startswith(old["notes"] + "\n\n")
            if p[0] == "solutions":
                stats["stock_nodes_relocated"] += 1
        amount, unit = row.get("amount", row.get("volume")), row.get("unit")
        if kind in {"water", "batch_dose"}:
            assert unit in {"L", "ml"}
            value = format((Decimal(str(amount)) / (1000 if unit == "ml" else 1)).normalize(), "f")
            assert node["concentration"] == {"value": value, "unit": "L"}
            assert (
                "not a measured final volume" in node["notes"]
                if kind == "water"
                else "per receiving batch, not g/L" in node["notes"]
            )
            if kind == "water":
                stats["quantity_corrections" if op else "new_quantity_slots"] += 1
            else:
                dose_old = originals.get(row.get("compound", row.get("component_name")))
                stats["stock_dose_basis_corrections" if dose_old else "new_quantity_slots"] += 1
        elif kind == "albumin_strength":
            assert node["concentration"] == {"value": "10", "unit": "PERCENT_W_V"}
            assert amount == 1 and unit == "g"
            assert (
                "Source batch input: 1 g." in node["notes"]
                and "10 g per 100 ml = 100 g/L" in node["notes"]
            )
            assert "not the receiving-medium concentration" in node["notes"]
            stats["new_quantity_slots"] += 1
        elif kind == "albumin_dose":
            assert node["concentration"] == {"value": "0.01", "unit": "L"}
            assert (
                "1 g / explicit stock strength (10 g / 0.1 L = 100 g/L) = 0.01 L (10 ml)"
                in node["notes"]
            )
            assert "calculated, not directly printed" in node["notes"]
            stats["new_quantity_slots"] += 1
        else:
            assert "concentration" not in node
            if kind == "batch_mass":
                assert unit in {"g", "mg"}
                assert f"Source batch input: {amount} {unit}." in node["notes"]
                assert "Final preparation volume is not independently established" in node["notes"]
                if p[0] == "solutions":
                    assert "contribution specified for the receiving medium batch" in node["notes"]
                stats[
                    "unsupported_quantity_slots_removed" if op else "ingredient_context_notes_added"
                ] += 1
            elif kind == "unquantified_gas":
                assert amount is None and "preparation-atmosphere context" in node["notes"]
                stats["unsupported_quantity_slots_removed"] += 1
            elif kind == "unquantified_serum":
                assert "final 6%" in node["notes"] and "after medium filtration" in node["notes"]
                assert node["composition"] == []
                assert (
                    node["preparation_notes"]
                    == "Add sterile rabbit serum to final concentration of 6%."
                )
                stats["unsupported_quantity_slots_removed"] += 1
            elif kind == "unquantified_strength":
                assert "percentage basis" in node["notes"].lower()
                if key == "M194":
                    assert "7% gelatin" in node["notes"] and "single 200 ml" in node["notes"]
                else:
                    assert row["component_name"] in node["notes"]
                if not op:
                    stats["unquantified_carrier_nodes_added"] += 1
            elif kind in {"solvent", "solvent_component"}:
                assert (
                    "0.05 N NaOH" in node["notes"]
                    and "normality is not converted to molarity" in node["notes"]
                )
                assert "No solvent dose or stock preparation volume" in node["notes"]
                if kind == "solvent_component":
                    stats["unquantified_carrier_nodes_added"] += 1
            elif kind == "prepared":
                assert "stock percentage basis and fixed dose are unspecified" in node["notes"]
            else:
                raise AssertionError(kind)
        if p[-2] == "solutions":
            if not op:
                stats["stock_descriptors_added"] += 1
            if key == "M194" and p == ("solutions", 1):
                assert (
                    node["composition"] == []
                    and "composition and stock strength are not supplied" in node["notes"]
                )
            if key == "M213" and len(p) == 2:
                assert len(node["composition"]) == 1
                if p[1] < 3:
                    assert node["preparation_notes"] == data[key]["comments"][1]["comment"]
                else:
                    assert "preparation_notes" not in node
            if kind in {"prepared", "albumin_dose"}:
                assert len(node["composition"]) == 1
                first, last = (
                    ("Filter-sterilize bovine", "Before inoculation")
                    if kind == "albumin_dose"
                    else ("Separately autoclave", "Filter-sterilize bovine")
                )
                original = texts["JCM252"]
                sterilize = original[original.index(first) : original.index(last)].strip()
                late = original[
                    original.index("Before inoculation") : original.index("Copyright")
                ].strip()
                assert node["preparation_notes"] == sterilize + " " + late
        if has_lineage:
            lineage.append(
                {
                    "pointer": list(p),
                    "old_pointer": list(op) if op else None,
                    "source": key,
                    "source_pointer": (
                        ["data", "solutions", 0, "recipe", ri]
                        if key == "J252"
                        else ["components", 0, "items", ri]
                    ),
                    "kind": "batch_mass" if kind == "albumin_strength" else kind,
                }
            )
    assert sorted(lineage, key=lambda n: field(n["pointer"])) == sorted(
        item["lineage"], key=lambda n: field(n["pointer"])
    )
    assert mapped | removed == {("ingredients", i) for i in range(len(before["ingredients"]))}
    assert not mapped & removed
    stats["unsupported_quantity_slots_removed"] += 3
    assert all(not get(after, p).get("supplier_catalog") for p in expected)
    removed_claims = [c for c in item["claims"] if c["kind"] == "wrong_product_removed"]
    assert (
        len(removed_claims) == 3
        and {tuple(c["old_pointer"][:-1]) for c in removed_claims} == removed
    )
    marker = "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product:"
    assert marker in after["notes"] and after["notes"].replace(
        marker, "\n\nCommercial Product:", 1
    ).startswith(before["notes"] + "\n\n")
    if key == "M194":
        assert "TOGO-provider-backed, not original-page corroborated" in after["notes"]
        prep_text = data[key]["comments"][0]["comment"]
        actions = ["MIX", "ADJUST_PH", "MIX", "FILTER", "MIX"]
    elif key == "M213":
        prep_text = " ".join(c["comment"] for c in data[key]["comments"])
        actions = ["ADJUST_PH", "FILTER"]
    else:
        original = texts["JCM252"]
        prep_text = original[original.index("Mix components") : original.index("Copyright")].strip()
        actions = ["MIX", "HEAT", "ADJUST_PH", "AUTOCLAVE", "AUTOCLAVE", "FILTER", "MIX"]
        assert "Adjust pH to 7.6 at 80-90C." in after["preparation_steps"][2]["description"]
    steps = after["preparation_steps"]
    assert " ".join(s["description"] for s in steps) == prep_text
    assert [s["action"] for s in steps] == actions
    assert [s["step_number"] for s in steps] == list(range(1, len(steps) + 1))
    assert all(set(s) == {"step_number", "action", "description"} for s in steps)
    assert after["ph_value"] == (6.6 if key == "M213" else 7.6)
    stats["preparation_steps_added"] += len(steps) - len(before.get("preparation_steps", []))
    if key == "M244":
        assert before["high_metal"] is True and "high_metal" not in after
        assert (
            "Withdraw the unsupported high_metal classification, not replace it with false"
            in after["notes"]
        )
        stats["unsupported_flags_removed"] += 1
    allowed = {
        "ingredients",
        "solutions",
        "notes",
        "preparation_steps",
        "ph_value",
        "evidence",
        "references",
        "curation_history",
    } | ({"high_metal"} if key == "M244" else set())
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
    new_slots = {p + ("concentration",) for p, n in walk(after) if "concentration" in n}
    assert {
        tuple(c["old_pointer"])
        for c in item["claims"]
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    } == old_slots
    assert new_slots <= {tuple(c["pointer"]) for c in item["claims"]}
    prefix = ["data", "solutions", 0, "recipe"] if key == "J252" else ["components", 0, "items"]
    assert {
        c["source_pointer"][-1]
        for c in item["claims"]
        if c["source"] == key and c["source_pointer"] and c["source_pointer"][:-1] == prefix
    } == set(range(len(rows)))
    attached = {}
    for c in item["claims"]:
        p, op = c["pointer"], c["old_pointer"]
        assert c["source"] in ({key} if key == "M194" else {key, "JCM" + number})
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
    assert actual == attached and sum(len(n.get("evidence", [])) for p, n in walk(after)) == len(
        actual
    )
    assert {r["reference"] for r in after["references"]} == {ref for p, ref in attached}
    assert len(after["references"]) == (1 if key == "M194" else 2)
    for ref in after["references"]:
        assert set(ref) == {"reference", "title", "notes"}
        source = next(
            k for k, v in context["sources"].items() if v["metadata"]["url"] == ref["reference"]
        )
        assert source != "JCM201"
        assert ref["title"] == (
            "Medium data"
            if source.startswith("JCM")
            else (
                data[source]["meta"]["name"]
                if source.startswith("M")
                else data[source]["data"]["medium"]["name"]
            )
        )
        assert all(
            t in ref["notes"]
            for t in (
                "source_type=",
                "discovery_mode=",
                "accessed_on=",
                "capture_sha256=",
                "Authors and publication year not supplied",
            )
        )
        if key == "M194":
            assert "access-status observation, not formulation evidence" in ref["notes"]
    stats.update(
        new_evidence=len(actual),
        new_references=len(after["references"]),
        new_curation_history=1,
        old_quantity_slots=len(old_slots),
        claims=len(item["claims"]),
        source_rows=len(rows),
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
