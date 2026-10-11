"""Independent source-row, preparation-stage and evidence audit for J266/J675/J1203."""

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
CONTEXT = HERE / "context.json"
SHA = "bd14d58c295cef3f05b3dc9183a375f9e4789ae3d7e8cd10583daa489bea7bee"
ACTION = "RESTORED_JCM_ACID_IDENTITIES_AND_PREPARATION_SCOPES_WITH_EVIDENCE"


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
        if not source.startswith("JCM"):
            sources[source] = json.loads(capture["raw"])

    def rows(source, section):
        return sources[source]["data"]["solutions"][section]["recipe"]

    number = key[1:]
    text = texts["JCM" + number]
    assert sources[key]["data"]["medium"]["id"] == key
    removed_indices = {"J266": [16, 17, 18], "J675": [13, 14, 15], "J1203": [10, 11, 12]}[key]
    original = {}
    for i, node in enumerate(before["ingredients"]):
        if i not in removed_indices:
            assert node["preferred_term"] not in original
            original[node["preferred_term"]] = ("ingredients", i)
    expected = {}

    def add(p, si, ri, kind, name=None, old=None, lineage=True):
        assert p not in expected
        row = rows(key, si)[ri] if si is not None else None
        label = name or row.get("compound", row.get("solution"))
        expected[p] = (si, ri, kind, label, old, lineage)

    special = {"J266": {0, 15, 16}, "J675": set(), "J1203": {13, 16}}[key]
    di = 0
    for ri, row in enumerate(rows(key, 0)):
        if ri in special or row.get("solution_id"):
            continue
        name = row["compound"]
        kind = (
            "water"
            if name == "Distilled water"
            else "liquid_input" if row["unit"] in {"ml", "L"} else "batch_mass"
        )
        add(("ingredients", di), 0, ri, kind, old=original.get(name))
        di += 1
    si_out = 0
    if key == "J266":
        add(("solutions", 0), 0, 0, "batch_dose", old=original["Rumen fluid"])
        si_out = 1
    sections = sources[key]["data"]["solutions"]

    def fill(p, si):
        for ri, row in enumerate(rows(key, si)):
            name = row["compound"]
            kind = (
                "water"
                if name == "Distilled water"
                else "liquid_input" if row["unit"] in {"ml", "L"} else "stock_rate"
            )
            add(p + ("composition", ri), si, ri, kind, old=original.get(name))
        if key == "J266" and si in {1, 2}:
            add(
                p + ("solutions", 0),
                None,
                None,
                "titrant",
                "Concentrated NaOH solution" if si == 1 else "KOH solution",
                lineage=False,
            )

    for ri, row in enumerate(rows(key, 0)):
        if row.get("solution_id"):
            si = next(i for i, sec in enumerate(sections) if sec["id"] == row["solution_id"])
            p = ("solutions", si_out)
            add(p, 0, ri, "batch_dose")
            fill(p, si)
            si_out += 1
    if key == "J266":
        for ri in (15, 16):
            p = ("solutions", si_out)
            name = rows(key, 0)[ri]["compound"]
            add(p, None, None, "separate", name + " separately prepared solution", lineage=False)
            add(p + ("composition", 0), 0, ri, "batch_mass", old=original[name])
            si_out += 1
    elif key == "J675":
        for j, name in enumerate(("Na2CO3", "L-Cysteine HCl x H2O")):
            add(("ingredients", di + j), None, None, "late_mass", name, lineage=False)
        add(("solutions", 2), None, None, "late_dose", "Fatty acid mixture", lineage=False)
        fill(("solutions", 2), 3)
    else:
        add(("solutions", 0), 0, 13, "batch_dose", "0.05% Resazurin solution")
        add(
            ("solutions", 0, "composition", 0),
            0,
            13,
            "unquantified_strength",
            old=original["Resazurin"],
        )
        add(
            ("solutions", 1),
            None,
            None,
            "separate",
            "Glucose separately prepared solution",
            lineage=False,
        )
        add(("solutions", 1, "composition", 0), 0, 16, "batch_mass", old=original["Glucose"])
    actual_nodes = {
        p
        for p, n in walk(after)
        if "preferred_term" in n
        and p[-2:-1] in {("ingredients",), ("solutions",), ("composition",)}
    }
    assert actual_nodes == set(expected)
    stats, counted, lineage = collections.Counter(), set(), []
    for p in sorted(expected, key=field):
        si, ri, kind, label, op, has_lineage = expected[p]
        row = rows(key, si)[ri] if si is not None else {}
        node, old_node = get(after, p), get(before, op) if op else {}
        excluded = {
            "notes",
            "concentration",
            "composition",
            "solutions",
            "evidence",
            "preparation_notes",
        }
        assert {k: v for k, v in node.items() if k not in excluded} == (
            {k: v for k, v in old_node.items() if k not in excluded}
            if old_node
            else {"preferred_term": label}
        )
        if old_node.get("notes"):
            assert node["notes"].startswith(old_node["notes"] + "\n\n")
        if "[Merged 2 duplicates:" in old_node.get("notes", ""):
            assert "earlier duplicate-summing note is superseded" in node["notes"]
        duplicate = op in counted
        if op and p[0] == "solutions" and not duplicate:
            stats["stock_nodes_relocated"] += 1
        if kind in {"batch_mass", "unquantified_strength", "separate", "titrant", "late_mass"}:
            assert "concentration" not in node
            if kind == "batch_mass":
                assert row["unit"] in {"g", "mg"}
                assert f"Source batch input: {row['amount']} {row['unit']}." in node["notes"]
                assert "Final preparation volume is not independently established" in node["notes"]
                if len(p) > 2:
                    assert "contribution specified for the receiving medium batch" in node["notes"]
            elif kind == "separate":
                assert "receiving-batch contribution, not a stock-batch recipe" in node["notes"]
                assert "addition volume are unspecified" in node["notes"]
                if key == "J266":
                    assert "5% label has unspecified percentage basis" in node["notes"]
                assert len(node["composition"]) == 1 and not node.get("solutions")
                stats["stock_descriptors_added"] += 1
            elif kind == "unquantified_strength":
                assert (
                    "Percentage basis is unspecified" in node["notes"] and "0.05%" in node["notes"]
                )
                stats["stock_dose_basis_corrections"] += 1
            elif kind == "titrant":
                assert (
                    node["composition"] == []
                    and "no fixed dose or numeric strength" in node["notes"]
                )
            else:
                amount = "4.0 g" if label == "Na2CO3" else "500 mg"
                assert f"Source batch input: {amount}." in node["notes"]
                assert "before distribution/autoclaving" in node["notes"]
                stats["ingredient_context_notes_added"] += 1
            if old_node.get("concentration") and not duplicate and kind != "unquantified_strength":
                stats["unsupported_quantity_slots_removed"] += 1
        elif kind == "stock_rate":
            assert node["concentration"] == {
                "value": format(Decimal(str(row["g_l"])).normalize(), "f"),
                "unit": "G_PER_L",
            }
            assert f"Source stock batch input: {row['amount']} {row['unit']}." in node["notes"]
            assert "provider-declared stock" in node["notes"]
            assert (
                "not a final-medium concentration or an independently verified final stock volume"
                in node["notes"]
            )
            if op and not duplicate:
                stats["stock_stage_concentrations_rebased"] += 1
            else:
                stats["new_quantity_slots"] += 1
        else:
            assert kind in {"water", "liquid_input", "batch_dose", "late_dose"}
            amount, unit = (1, "ml") if kind == "late_dose" else (row["amount"], row["unit"])
            assert node["concentration"] == {
                "value": format(
                    (Decimal(str(amount)) / (1000 if unit == "ml" else 1)).normalize(), "f"
                ),
                "unit": "L",
            }
            assert (
                "not a measured final volume"
                if kind == "water"
                else "not grams per liter" if kind == "liquid_input" else "per receiving batch"
            ) in node["notes"]
            if op and not duplicate:
                stats[
                    (
                        "stock_dose_basis_corrections"
                        if kind == "batch_dose"
                        else "quantity_corrections"
                    )
                ] += node["concentration"] != old_node.get("concentration")
            elif not (key == "J1203" and p == ("solutions", 0)):
                stats["new_quantity_slots"] += 1
        if op:
            counted.add(op)
        if has_lineage:
            lineage_kind = "unquantified_strength" if kind == "unquantified_strength" else kind
            lineage.append(
                {
                    "pointer": list(p),
                    "old_pointer": list(op) if op else None,
                    "source": key,
                    "source_pointer": ["data", "solutions", si, "recipe", ri],
                    "kind": lineage_kind,
                }
            )
    assert sorted(lineage, key=lambda n: field(n["pointer"])) == sorted(
        item["lineage"], key=lambda n: field(n["pointer"])
    )
    removed = {("ingredients", i) for i in removed_indices}
    assert counted | removed == {("ingredients", i) for i in range(len(before["ingredients"]))}
    assert not counted & removed
    stats["unsupported_quantity_slots_removed"] += 3
    old_counts = collections.Counter(tuple(n["old_pointer"]) for n in lineage if n["old_pointer"])
    assert {p: n for p, n in old_counts.items() if n > 1} == (
        {("ingredients", i): 2 for i in (4, 5, 6, 7)} if key == "J266" else {}
    )
    marker = "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product:"
    assert marker in after["notes"]
    assert (
        after["notes"]
        .replace(marker, "\n\nCommercial Product:", 1)
        .startswith(before["notes"] + "\n\n")
    )
    assert "Remove only the reviewed LB supplier nodes" in after["notes"]
    assert not any(n.get("supplier_catalog") for p, n in walk(after) if p in expected)
    removed_claims = [c for c in item["claims"] if c["kind"] == "wrong_product_removed"]
    assert {tuple(c["old_pointer"][:-1]) for c in removed_claims} == removed
    assert len(removed_claims) == 3
    assert after["ph_value"] == (6.5 if key == "J266" else 7.0)
    if key == "J266":
        assert after["preparation_steps"] == [before["preparation_steps"][0]]
        assert "API metadata min_pH/max_pH 7.5 conflicts" in after["notes"]
        assert after["solutions"][0]["preparation_notes"] == sections[0]["steps"][1]["step"]
        assert after["solutions"][1]["preparation_notes"] == sections[2]["steps"][0]["step"]
        assert after["solutions"][3]["preparation_notes"] == sections[1]["steps"][0]["step"]
        assert "preparation_notes" not in after["solutions"][2]
        prep = text[text.index("Separately autoclave") : text.index("Prior to inoculation")].strip()
        assert all(after["solutions"][i]["preparation_notes"] == prep for i in (4, 5))
        assert after["solutions"][0]["composition"] == []
        acid = after["solutions"][3]["composition"][2]
        assert acid["preferred_term"] == "alpha-Methylbutyric acid" and "term" not in acid
    else:
        assert after["preparation_steps"] == before["preparation_steps"]
        if key == "J1203":
            prep = text[
                text.index("Thereafter, add glucose") : text.index("Adjust pH of complete")
            ].strip()
            assert after["solutions"][1]["preparation_notes"] == prep
            assert (
                after["solutions"][0]["composition"][0]["term"] == before["ingredients"][15]["term"]
            )
            assert after["ingredients"][10]["preferred_term"] == "DL-2-Methylbutyric acid"
        else:
            assert after["ingredients"][0]["preferred_term"] == "Tryptone"
            assert "Source batch input: 5 g." in after["ingredients"][0]["notes"]
            assert (
                after["solutions"][2]["composition"][2]["preferred_term"] == "2-Methylbutyric acid"
            )
    for p, (si, ri, kind, _label, _op, _lineage) in expected.items():
        if kind in {"batch_mass", "stock_rate", "water", "liquid_input", "unquantified_strength"}:
            assert any(
                c["source"] == key
                and c["source_pointer"] == ["data", "solutions", si, "recipe", ri]
                and c["pointer"][: len(p)] == list(p)
                for c in item["claims"]
            )
    allowed = {
        "ph_value",
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
        (key, si, ri)
        for si in range(len(sources[key]["data"]["solutions"]))
        for ri in range(len(rows(key, si)))
    }
    covered_rows = {
        (c["source"], c["source_pointer"][2], c["source_pointer"][4])
        for c in item["claims"]
        if c["source_pointer"]
        and len(c["source_pointer"]) == 5
        and c["source_pointer"][:2] == ["data", "solutions"]
        and c["source_pointer"][3] == "recipe"
    }
    assert required_rows == covered_rows
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
            "Medium data" if source.startswith("JCM") else sources[source]["data"]["medium"]["name"]
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
