"""Independent source-membership, stage, evidence, and preservation audit."""

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
SHA = "e2970bd6a1ebf9d9ba9c900aa1666cf7e8c15aac8c2bb2739c40bc4506492198"
ACTION = "RESTORED_BASAL_MAKEUP_AND_SUPPLEMENT_STAGES_WITH_EVIDENCE"


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

    original = {
        n["preferred_term"]: (f, i)
        for f in ("ingredients", "solutions")
        for i, n in enumerate(before[f])
    }
    assert len(original) == sum(len(before[f]) for f in ("ingredients", "solutions"))
    expected = {}

    def rows(source, section):
        return sources[source]["components"][section]["items"]

    def add(p, source, si, ri, kind, op=None):
        assert p not in expected
        expected[p] = (source, si, ri, kind, op)

    def stock(p, si, ri):
        row = rows(key, si)[ri]
        add(
            p,
            key,
            si,
            ri,
            "per_liter_dose" if si == 1 and key != "M809" else "batch_dose",
            original[row["component_name"]],
        )
        ref = row.get("reference_media_id")
        if ref:
            section = 1 if ref == "M190" else 2
            ci = 0
            for j, ingredient in enumerate(rows(ref, section)):
                name = ingredient["component_name"]
                if name == "KOH solution":
                    add(p + ("solutions", 0), ref, section, j, "unquantified_titrant")
                else:
                    op = original.get(name) if ref == key and name != "Distilled water" else None
                    add(
                        p + ("composition", ci),
                        ref,
                        section,
                        j,
                        "water" if name == "Distilled water" else "batch_mass",
                        op,
                    )
                    ci += 1
        elif row.get("conc_unit") == "M":
            assert row["component_name"] == "1 M Glucose solution" and row["conc_value"] == 1
            add(p + ("composition", 0), key, si, ri, "stock_strength")
        else:
            assert row["conc_unit"] == "%"
            assert get(after, p)["composition"] == []

    ci, sj = 0, 0
    for ri, row in enumerate(rows(key, 0)):
        if row.get("reference_media_id"):
            stock(("solutions", 0, "solutions", sj), 0, ri)
            sj += 1
        elif key == "M975" and row["component_name"] == "KOH":
            p = ("solutions", 0, "solutions", sj)
            add(p, key, 0, ri, "titrant_stock")
            add(p + ("composition", 0), key, 0, ri, "stock_strength", original["KOH"])
            sj += 1
        else:
            kind = (
                "makeup_water"
                if row["component_name"] == "Distilled water"
                else "unquantified_input" if row.get("volume") is None else "basal_rate"
            )
            add(
                ("solutions", 0, "composition", ci),
                key,
                0,
                ri,
                kind,
                original[row["component_name"]],
            )
            ci += 1
    for i in range(len(rows(key, 1))):
        stock(("solutions", i + 1), 1, i)

    base = after["solutions"][0]
    assert after["ingredients"] == []
    assert set(base) == {"preferred_term", "composition", "solutions", "notes"}
    assert base["preferred_term"] == "Basal preparation at the 1 L makeup stage"
    assert "before later supplements" in base["notes"] and "No fixed dose" in base["notes"]
    actual = {
        p
        for p, n in walk(after)
        if "preferred_term" in n
        and p[-2:-1] in {("ingredients",), ("solutions",), ("composition",)}
    }
    assert actual == set(expected) | {("solutions", 0)}
    lineage, stats = [], collections.Counter(base_preparations_added=1)
    for p, (source, si, ri, kind, op) in expected.items():
        node = get(after, p)
        row = rows(source, si)[ri]
        old = get(before, op) if op else {}
        excluded = {
            "notes",
            "concentration",
            "composition",
            "solutions",
            "evidence",
            "preparation_notes",
        }
        label = (
            "KOH reagent (10 M)"
            if kind == "titrant_stock"
            else "Glucose" if kind == "stock_strength" and not op else row["component_name"]
        )
        assert {k: v for k, v in node.items() if k not in excluded} == (
            {k: v for k, v in old.items() if k not in excluded}
            if old
            else {"preferred_term": label}
        )
        if old.get("notes"):
            assert node["notes"].startswith(old["notes"] + "\n\n")
        amount, unit = row.get("volume"), row.get("unit")
        if kind in {
            "makeup_water",
            "unquantified_input",
            "batch_mass",
            "unquantified_titrant",
            "titrant_stock",
        }:
            assert "concentration" not in node
            if kind == "makeup_water":
                assert "actual addition amount is unspecified" in node["notes"]
                if key == "M975":
                    assert "Both statements are preserved" in node["notes"]
                if key == "M809":
                    assert "duplicate-summing" in node["notes"]
            elif kind == "batch_mass":
                assert (
                    unit in {"g", "mg"} and f"Source batch input: {amount} {unit}." in node["notes"]
                )
                assert "Final preparation volume is not independently established" in node["notes"]
                if not old:
                    assert "withdrawn" not in node["notes"]
            elif kind == "unquantified_input":
                assert amount is None and "unsupported VARIABLE placeholder" in node["notes"]
            elif kind == "unquantified_titrant":
                assert amount is None and "no fixed dose" in node["notes"]
            else:
                assert "addition volume is unspecified" in node["notes"]
            stats["unsupported_quantity_slots_removed"] += bool(old.get("concentration"))
        else:
            if kind == "basal_rate":
                assert unit in {"g", "mg", "g/L"}
                value, out_unit = Decimal(str(amount)), "MG_PER_L" if unit == "mg" else "G_PER_L"
                assert "not a final supplemented-medium rate" in node["notes"]
                stats["stock_nodes_relocated"] += 1
            elif kind == "stock_strength":
                value, out_unit = Decimal(str(row["conc_value"])), "MOLAR"
                assert "not" in node["notes"] and "medium" in node["notes"]
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
            if row.get("conc_unit") == "%":
                assert "percentage basis is unspecified" in node["notes"]
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
    assert sorted(lineage, key=lambda n: field(n["pointer"])) == sorted(
        item["lineage"], key=lambda n: field(n["pointer"])
    )
    assert {tuple(n["old_pointer"]) for n in lineage if n["old_pointer"]} == set(original.values())

    for p, (source, si, ri, _kind, _op) in expected.items():
        ref = rows(source, si)[ri].get("reference_media_id")
        if ref == "M142":
            assert get(after, p)["preparation_notes"] == sources[ref]["comments"][1]["comment"]
        elif ref == "M809":
            assert get(after, p)["preparation_notes"] == sources[ref]["comments"][3]["comment"]
    description = sources[key]["comments"][0]["comment"]
    if key == "M853":
        description = description.replace("Adjust pH to 7.0 with KOH", "Adjust pH to 7.5 with KOH")
    steps = [{"step_number": 1, "action": "AUTOCLAVE", "description": description}]
    if key == "M809":
        steps.append(
            {
                "step_number": 2,
                "action": "ADJUST_PH",
                "description": sources[key]["comments"][1]["comment"],
            }
        )
    assert after["preparation_steps"] == steps
    if key in {"M823", "M853"}:
        target = next(
            r for r in context["records"] if r["key"] == ("M823" if key == "M853" else "M853")
        )
        target_data = yaml.load(target["before_text"], Loader=yaml.CSafeLoader)
        link = after["parent_media"] if key == "M853" else after["variant_children"][0]
        assert set(link) == {"id", "name", "path", "relationship", "notes", "evidence"}
        assert (link["id"], link["name"], link["path"], link["relationship"]) == (
            target_data["id"],
            target_data["name"],
            target["path"],
            "DERIVED_FROM",
        )
        assert "salt-substitution and pH variant" in link["notes"]
        if key == "M853":
            assert after["ph_value"] == 7.5 and after["variant_relationship"] == "DERIVED_FROM"
            assert after["variant_modifications"] == [
                "Replace basal calcium chloride dihydrate with the specified 5.0 g/L magnesium sulfate heptahydrate.",
                "Adjust pH to 7.5 instead of the parent's 7.0.",
            ]
        else:
            assert len(after["variant_children"]) == 1
        stats["variant_links_added"] += 1
    allowed = {
        "ingredients",
        "solutions",
        "preparation_steps",
        "evidence",
        "references",
        "curation_history",
    }
    allowed |= (
        {"parent_media", "variant_relationship", "variant_modifications", "ph_value"}
        if key == "M853"
        else {"variant_children"} if key == "M823" else set()
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
        source_rows=len({(s, si, ri) for s, si, ri, k, op in expected.values()}),
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
