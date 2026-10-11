"""Independent source-row, preparation-stage and retained-annotation accounting."""

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
CONTEXT = HERE.parent / "20261008-methanogen-boundaries/next-stock-source-context.json"
SHA = "291cb565a506c5d89690780c758275f68b42dc1895fb629bd5875ec3bbb45752"


def get(node, path):
    for p in path:
        node = node[p]
    return node


def walk(node, path=()):
    if isinstance(node, dict):
        yield path, node
        for k, v in node.items():
            yield from walk(v, path + (k,))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk(v, path + (i,))


def field(path):
    return "".join(f"[{p}]" if isinstance(p, int) else "." + p for p in path).lstrip(".")


def check(before, after, item):
    raw = CONTEXT.read_bytes()
    assert hashlib.sha256(raw).hexdigest() == SHA
    context = json.loads(raw)
    key = item["key"]
    spec = next(r for r in context["records"] if r["key"] == key)
    assert before == yaml.safe_load(spec["before_text"])
    sources, texts = {}, {}
    for name, s in context["sources"].items():
        assert (
            hashlib.sha256(s["raw"].encode(s["metadata"]["encoding"])).hexdigest()
            == s["metadata"]["sha256"]
        )
        assert s["metadata"]["http_status"] == 200
        texts[name] = (
            " ".join(BeautifulSoup(s["raw"], "html.parser").get_text().split())
            if name.startswith("JCM")
            else s["raw"]
        )
        if not name.startswith("JCM"):
            sources[name] = json.loads(s["raw"])

    def rows(source, section):
        return (
            sources[source]["data"]["solutions"][section]["recipe"]
            if source.startswith("J")
            else sources[source]["components"][section]["items"]
        )

    def sp(source, section, row):
        return (
            ["data", "solutions", section, "recipe", row]
            if source.startswith("J")
            else ["components", section, "items", row]
        )

    # Expected tree from the inspected source tables, independent of compiler lineage.
    links = {
        "J151": [(0, "J151", 1), (1, "J151", 2)],
        "J187": [(7, "J187", 1), (8, "J187", 2), (9, "J187", 3)],
        "J197": [(8, "J197", 2), (9, "J197", 1)],
        "M142": [(6, "M142", 1), (7, "M142", 2)],
        "M180": [(13, "M180", 1), (14, "M180", 2), (15, "M190", 1)],
        "M190": [(13, "M190", 2), (14, "M190", 1)],
    }[key]
    separate = {
        "J151": [6],
        "J187": [6, 10, 11, 13],
        "J197": [10, 11, 12],
        "M142": [1],
        "M180": [7, 9, 11, 12],
        "M190": [6, 7, 11],
    }[key]
    expected, prepared, extras = {}, {}, set()
    for i, (ri, source, section) in enumerate(links):
        p = ("solutions", i)
        expected[p] = (key, 0, ri, "batch_dose")
        ci = 0
        for j, row in enumerate(rows(source, section)):
            name = row.get("compound", row.get("component_name"))
            if name in {"HCl", "25% HCl (7.7 M)"}:
                expected[p + ("solutions", 0)] = (source, section, j, "batch_dose")
                expected[p + ("solutions", 0, "composition", 0)] = (
                    source,
                    section,
                    j,
                    "stock_strength",
                )
            elif key == "M142" and section == 2 and j == 13:
                expected[p + ("solutions", 0)] = (source, section, j, "unquantified_titrant")
            else:
                kind = (
                    "water"
                    if name == "Distilled water"
                    else (
                        "unquantified_titrant"
                        if name == "KOH"
                        else "stock_rate" if source.startswith("J") else "batch_mass"
                    )
                )
                expected[p + ("composition", ci)] = (source, section, j, kind)
                ci += 1
        if key in {"J151", "J197"} and section == 2:
            extras.add(p + ("composition", ci))
    direct = 0
    for i, row in enumerate(rows(key, 0)):
        if i in {ri for ri, s, section in links}:
            continue
        if i in separate:
            p = ("solutions", len(links) + separate.index(i))
            prepared[p] = i
            expected[p + ("composition", 0)] = (key, 0, i, "batch_mass")
        else:
            name = row.get("compound", row.get("component_name"))
            kind = (
                "water"
                if name == "Distilled water"
                else (
                    "gas"
                    if name in {"N2", "Carbon dioxide gas", "Nitrogen gas"}
                    else "unquantified_titrant" if name == "H2SO4" else "batch_mass"
                )
            )
            expected[("ingredients", direct)] = (key, 0, i, kind)
            direct += 1
    if key in {"J151", "J187"}:
        extras.add(("ingredients", direct))
    nodes = {
        p
        for p, n in walk(after)
        if p
        and p[-2:-1] in {("ingredients",), ("composition",), ("solutions",)}
        and "preferred_term" in n
    }
    assert nodes == set(expected) | set(prepared) | extras
    originals = {
        n["preferred_term"]: (f, i)
        for f in ("ingredients", "solutions")
        for i, n in enumerate(before.get(f, []))
    }
    seen, removed, expected_lineage, stats = set(), set(), [], collections.Counter()
    for path, (source, section, ri, kind) in expected.items():
        n = get(after, path)
        row = rows(source, section)[ri]
        name = row.get("compound", row.get("solution", row.get("component_name")))
        acid_parent = kind == "batch_dose" and section > 0
        assert n["preferred_term"] == ("HCl reagent (7.7 M)" if acid_parent else name)
        op = originals.get(name) if source == key and not acid_parent else None
        old = get(before, op) if op else {}
        if op:
            seen.add(op)
        skip = {
            "concentration",
            "notes",
            "evidence",
            "composition",
            "solutions",
            "preparation_notes",
        }
        if kind == "batch_dose" and source.startswith("J") and not acid_parent:
            si = next(
                s for s in sources[source]["data"]["solutions"] if s["id"] == row["solution_id"]
            )
            assert n["term"] == {"id": "mediadive.solution:" + str(si["id"]), "label": si["name"]}
            skip.add("term")
        assert {k: v for k, v in n.items() if k not in skip} == (
            {k: v for k, v in old.items() if k not in skip}
            if old
            else {"preferred_term": n["preferred_term"]}
        )
        if old.get("notes"):
            assert n["notes"].startswith(old["notes"] + "\n\n") or kind == "gas" and n == old
        amount, unit = row.get("amount", row.get("volume")), row.get("unit")
        if kind == "gas":
            assert n == old and amount is None
            continue
        expected_lineage.append(
            {
                "pointer": list(path),
                "old_pointer": list(op) if op else None,
                "source": source,
                "source_pointer": sp(source, section, ri),
                "kind": kind,
            }
        )
        quantity_claims = [
            c
            for c in item["claims"]
            if c["pointer"] == list(path) + ["concentration"] and c["kind"] == kind
        ]
        assert len(quantity_claims) == 1
        claim = quantity_claims[0]
        assert claim["source"] == source and claim["source_pointer"] == sp(source, section, ri)
        assert claim["old_pointer"] == (list(op) + ["concentration"] if op else None)
        if kind in {"batch_mass", "unquantified_titrant"}:
            assert "concentration" not in n
            if kind == "batch_mass":
                assert unit in {"g", "mg"} and f"Source batch input: {amount} {unit}." in n["notes"]
                assert "Final preparation volume is not independently established" in n["notes"]
                if section == 0 and ri in separate:
                    assert "not the mass for preparing an unspecified volume of stock" in n["notes"]
            else:
                assert amount is None and "no fixed dose" in n["notes"]
                if row.get("conc_unit") == "N":
                    assert "1 N" in n["notes"] and "not converted to molarity" in n["notes"]
            if old.get("concentration"):
                removed.add(op)
        else:
            v = (
                Decimal(str(row["g_l"]))
                if kind == "stock_rate"
                else (
                    Decimal("7.7")
                    if kind == "stock_strength"
                    else Decimal(str(amount)) / (1000 if unit == "ml" else 1)
                )
            )
            u = {
                "water": "L",
                "batch_dose": "L",
                "stock_rate": "G_PER_L",
                "stock_strength": "MOLAR",
            }[kind]
            assert set(n["concentration"]) == {"value", "unit"}
            assert Decimal(n["concentration"]["value"]) == v and n["concentration"]["unit"] == u
            if kind == "stock_rate":
                assert (
                    section > 0
                    and "provider-declared stock" in n["notes"]
                    and "not a final-medium concentration" in n["notes"]
                )
            if kind == "water":
                assert "not a measured final volume" in n["notes"]
            if kind == "batch_dose":
                assert "per receiving batch" in n["notes"] and "not grams per liter" in n["notes"]
            stats["new_quantity_slots" if not old else "quantity_contexts_reviewed"] += 1
            if old and n["concentration"] != old.get("concentration"):
                stats[
                    {
                        "water": "quantity_corrections",
                        "batch_dose": "stock_dose_basis_corrections",
                        "stock_rate": "stock_stage_concentrations_rebased",
                        "stock_strength": "stock_stage_concentrations_rebased",
                    }[kind]
                ] += 1
        stats["stock_nodes_relocated"] += bool(
            op and op[0] == "ingredients" and path[0] == "solutions"
        )
    assert seen == {
        (f, i) for f in ("ingredients", "solutions") for i in range(len(before.get(f, [])))
    }
    assert sorted(expected_lineage, key=lambda x: field(x["pointer"])) == sorted(
        item["lineage"], key=lambda x: field(x["pointer"])
    )

    prep = (
        sources[key]["data"]["solutions"][0]["steps"][0]["step"]
        if key.startswith("J")
        else sources[key]["comments"][0]["comment"]
    )
    assert after["preparation_steps"] == [
        {
            "step_number": 1,
            "action": "FILTER" if key in {"J151", "M142"} else "AUTOCLAVE",
            "description": prep,
        }
    ]
    for p, ri in prepared.items():
        n = get(after, p)
        r = rows(key, 0)[ri]
        assert (
            n["preferred_term"]
            == r.get("compound", r.get("component_name")) + " separately prepared solution"
        )
        assert (
            n["preparation_notes"]
            == "Receiving-medium instructions (context only; not a stock-batch recipe): " + prep
            and "concentration" not in n
        )
        assert "percentage basis" in n["notes"] and len(n["composition"]) == 1
    for p in extras:
        n = get(after, p)
        assert n["preferred_term"] == ("H2SO4" if p[0] == "ingredients" else "KOH solution")
        assert set(n) == {"preferred_term", "notes", "evidence"} and "no fixed dose" in n["notes"]
    if key in {"J151", "J197", "M142", "M190"}:
        p = ("solutions", 1 if key in {"J151", "M142"} else 0)
        text = (
            sources[key]["data"]["solutions"][2]["steps"][0]["step"]
            if key.startswith("J")
            else sources[key]["comments"][1]["comment"]
        )
        assert get(after, p)["preparation_notes"] == text
    if key in {"J187", "M180"}:
        assert after["ph_range"] == {"min": 6.2, "max": 6.4} and "ph_value" not in after
    else:
        assert after["ph_value"] == (6.5 if key in {"J151", "M142"} else 6.8)
    if key in {"J197", "M190"}:
        p = next(
            p
            for p, (s, section, ri, k) in expected.items()
            if section == 0 and ri == (11 if key == "J197" else 6)
        )
        assert "Unresolved source identity discrepancy" in get(after, p)["notes"]
    allowed = {
        "ingredients",
        "solutions",
        "preparation_steps",
        "ph_value",
        "ph_range",
        "evidence",
        "references",
        "curation_history",
    }
    assert {k: v for k, v in before.items() if k not in allowed} == {
        k: v for k, v in after.items() if k not in allowed
    }
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["curator"] == "codex"
    assert after["curation_history"][-1]["action"] == item["action"]

    claimed_old = {
        tuple(c["old_pointer"])
        for c in item["claims"]
        if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
    }
    old_slots = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    assert claimed_old == old_slots
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
        if ep is not None:
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
    for ref in after["references"]:
        assert set(ref) == {"reference", "title", "notes"}
        assert ref["reference"] in {r for p, r in attached}
        assert "Authors and publication year not supplied" in ref["notes"]
        assert "source_type=" in ref["notes"] and "discovery_mode=" in ref["notes"]
    assert {r["reference"] for r in after["references"]} == {r for p, r in attached}
    stats.update(
        unsupported_quantity_slots_removed=len(removed),
        new_evidence=len(actual),
        new_references=len(after["references"]),
        new_curation_history=1,
        old_quantity_slots=len(old_slots),
        claims=len(item["claims"]),
    )
    stats["stock_descriptors_added"] = len(prepared) + sum(
        1
        for path, spec in expected.items()
        if spec[-1] == "batch_dose"
        and not any(
            lineage["pointer"] == list(path) and lineage["old_pointer"]
            for lineage in expected_lineage
        )
    )
    return dict(stats)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--applied", action="store_true")
    args = parser.parse_args()
    plan = json.loads((HERE / "plan.json").read_text())
    result = {}
    for r in plan["records"]:
        raw = (ROOT / r["path"]).read_bytes() if args.applied else r["after_text"].encode()
        assert hashlib.sha256(raw).hexdigest() == r["after_sha256"]
        result[r["key"]] = check(yaml.safe_load(r["before_text"]), yaml.safe_load(raw), r)
    (HERE / ("applied-audit.json" if args.applied else "preview-audit.json")).write_text(
        json.dumps(result, indent=2) + "\n"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
