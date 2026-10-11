"""Independent ingredient, stock-dose and evidence audit for J201/J220."""

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
SHA = "1d17c31b8c9f8b24725bfd290a9a096ff9db44c0ff6c3f12a142785929a761cb"
ACTION = "RESTORED_JCM_ALBUMIN_IDENTITIES_AND_REAGENT_INPUTS_WITH_EVIDENCE"


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
    assert "Nothing found." in texts["JCM201"]
    assert context["source_issues"] == {"JCM201": "source_unavailable: JCM returned no recipe"}
    source = sources[key]
    assert source["data"]["medium"]["id"] == key
    section = source["data"]["solutions"][0]
    assert section["id"] == {"J201": 3866, "J220": 3888}[key]
    rows = section["recipe"]
    assert len(rows) == 10
    removed = {("ingredients", i) for i in ({2, 3, 4} if key == "J201" else {6, 7, 8})}
    originals = {
        n["preferred_term"]: ("ingredients", i)
        for i, n in enumerate(before["ingredients"])
        if ("ingredients", i) not in removed
    }
    expected = {}

    def add(p, ri, kind, label=None, old=None, lineage=True):
        assert p not in expected
        name = rows[ri]["compound"] if ri is not None else None
        expected[p] = (ri, kind, label or name, old, lineage)

    solids = list(range(1, 10)) if key == "J201" else [0, 1, 2, 3, 4, 9]
    for i, ri in enumerate(solids):
        name = rows[ri]["compound"]
        add(("ingredients", i), ri, "water" if ri == 9 else "batch_mass", old=originals.get(name))
    if key == "J201":
        add(("solutions", 0), 0, "product_dose", old=originals["CMRL 1066"])
        add(("solutions", 1), None, "late_dose", "7% gelatin solution", lineage=False)
        add(("solutions", 1, "composition", 0), None, "gelatin", "Gelatin", lineage=False)
        add(("solutions", 2), None, "serum", "Sterile rabbit serum", lineage=False)
    else:
        labels = [
            "Hemin solution (0.1% in 0.05 N NaOH)",
            "20% bovine serum albumin fraction V solution",
            "50% glucose solution",
            "10% cysteine solution",
        ]
        for si, ri in enumerate(range(5, 9)):
            p = ("solutions", si)
            add(p, ri, "reagent_dose", labels[si])
            add(p + ("composition", 0), ri, "strength", old=originals.get(rows[ri]["compound"]))
        add(
            ("solutions", 0, "solutions", 0),
            None,
            "solvent",
            "NaOH solution (0.05 N)",
            lineage=False,
        )
        add(
            ("solutions", 0, "solutions", 0, "composition", 0),
            None,
            "solvent_component",
            "NaOH",
            lineage=False,
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
        if kind in {"batch_mass", "strength", "gelatin", "serum", "solvent", "solvent_component"}:
            assert "concentration" not in node
            if kind == "batch_mass":
                assert row["unit"] == "g"
                assert f"Source batch input: {row['amount']} g." in node["notes"]
                assert "Final preparation volume is not independently established" in node["notes"]
                if op:
                    stats["unsupported_quantity_slots_removed"] += 1
                else:
                    assert key == "J201" and ri == 2 and "Fraction V" in node["notes"]
                    stats["ingredient_context_notes_added"] += 1
            elif kind == "strength":
                assert row["attribute"] in node["notes"]
                assert "Percentage basis is unspecified" in node["notes"]
                assert "enclosing descriptor holds the receiving-batch volume" in node["notes"]
                if ri == 6:
                    assert "fraction V" in node["notes"] and "term" not in node
            elif kind == "gelatin":
                assert (
                    "7% gelatin" in node["notes"]
                    and "Percentage basis is unspecified" in node["notes"]
                )
                stats["unquantified_carrier_nodes_added"] += 1
            elif kind == "serum":
                assert "final 6%" in node["notes"] and "percentage basis" in node["notes"]
                assert "after filtration" in node["notes"] and node["composition"] == []
                assert (
                    node["preparation_notes"]
                    == "Add sterile rabbit serum to final concentration of 6%."
                )
                stats["stock_descriptors_added"] += 1
            else:
                assert (
                    "0.05 N NaOH" in node["notes"]
                    and "Normality is not converted to molarity" in node["notes"]
                )
                assert (
                    "addition volume and stock preparation amounts are unspecified" in node["notes"]
                )
                stats[
                    (
                        "stock_descriptors_added"
                        if kind == "solvent"
                        else "unquantified_carrier_nodes_added"
                    )
                ] += 1
        else:
            amount = 200 if kind == "late_dose" else row["amount"]
            assert kind in {"water", "product_dose", "reagent_dose", "late_dose"}
            assert kind == "late_dose" or row["unit"] == "ml"
            assert node["concentration"] == {
                "value": format((Decimal(str(amount)) / 1000).normalize(), "f"),
                "unit": "L",
            }
            if kind == "water":
                assert "not a measured final volume" in node["notes"]
                stats["new_quantity_slots"] += 1
            elif kind == "late_dose":
                assert "before filtration of the entire medium" in node["notes"]
                assert "Percentage basis" in node["notes"]
                stats.update(new_quantity_slots=1, stock_descriptors_added=1)
            else:
                assert "per receiving batch, not grams per liter" in node["notes"]
                if rows[ri]["compound"] in originals:
                    stats["stock_dose_basis_corrections"] += 1
                else:
                    stats["new_quantity_slots"] += 1
                if kind == "product_dose":
                    assert node["composition"] == [] and "Gibco 330-1540" in node["notes"]
                    assert "does not provide this product's composition" in node["notes"]
                else:
                    assert len(node["composition"]) == 1
                    if ri != 5:
                        assert node["preparation_notes"] == section["steps"][1]["step"]
                    else:
                        assert "preparation_notes" not in node
        if has_lineage:
            lineage.append(
                {
                    "pointer": list(p),
                    "old_pointer": list(op) if op else None,
                    "source": key,
                    "source_pointer": ["data", "solutions", 0, "recipe", ri],
                    "kind": {
                        "product_dose": "batch_dose",
                        "reagent_dose": "batch_dose",
                        "strength": "unquantified_strength",
                    }.get(kind, kind),
                }
            )
    assert sorted(lineage, key=lambda n: field(n["pointer"])) == sorted(
        item["lineage"], key=lambda n: field(n["pointer"])
    )
    assert mapped | removed == {("ingredients", i) for i in range(len(before["ingredients"]))}
    assert not mapped & removed
    stats["unsupported_quantity_slots_removed"] += 3
    assert not any(n.get("supplier_catalog") for p, n in walk(after) if p in expected)
    marker = "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product:"
    assert marker in after["notes"] and after["notes"].replace(
        marker, "\n\nCommercial Product:", 1
    ).startswith(before["notes"] + "\n\n")
    removed_claims = [c for c in item["claims"] if c["kind"] == "wrong_product_removed"]
    assert (
        len(removed_claims) == 3
        and {tuple(c["old_pointer"][:-1]) for c in removed_claims} == removed
    )
    prep = json.loads(json.dumps(before["preparation_steps"]))
    if key == "J201":
        prep[0]["action"] = "FILTER"
        assert "provider-backed, not original-page corroborated" in after["notes"]
        stats["preparation_actions_corrected"] += 1
    assert after["preparation_steps"] == prep
    assert after["ph_value"] == before["ph_value"] == (7.6 if key == "J201" else 6.6)
    allowed = {
        "ingredients",
        "solutions",
        "notes",
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
    ]
    old_slots = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    new_slots = {p + ("concentration",) for p, n in walk(after) if "concentration" in n}
    assert {
        tuple(c["old_pointer"])
        for c in item["claims"]
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    } == old_slots
    assert new_slots <= {tuple(c["pointer"]) for c in item["claims"]}
    covered_rows = {
        c["source_pointer"][4]
        for c in item["claims"]
        if c["source"] == key
        and c["source_pointer"]
        and len(c["source_pointer"]) == 5
        and c["source_pointer"][:4] == ["data", "solutions", 0, "recipe"]
    }
    assert covered_rows == set(range(10))
    attached = {}
    for c in item["claims"]:
        p, op = c["pointer"], c["old_pointer"]
        assert c["source"] != "JCM201"
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
    assert len(after["references"]) == (1 if key == "J201" else 2)
    for ref in after["references"]:
        assert set(ref) == {"reference", "title", "notes"}
        s = next(
            k for k, v in context["sources"].items() if v["metadata"]["url"] == ref["reference"]
        )
        assert s != "JCM201"
        assert ref["title"] == (
            "Medium data" if s.startswith("JCM") else sources[s]["data"]["medium"]["name"]
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
        if key == "J201":
            assert "access-status observation, not original formulation evidence" in ref["notes"]
            assert context["sources"]["JCM201"]["metadata"]["sha256"] in ref["notes"]
    stats.update(
        new_evidence=len(actual),
        new_references=len(after["references"]),
        new_curation_history=1,
        old_quantity_slots=len(old_slots),
        claims=len(item["claims"]),
        source_rows=10,
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
