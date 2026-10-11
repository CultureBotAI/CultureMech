"""Independent source graph, override, annotation and evidence audit for JCM261."""

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
CONTEXT = HERE.parent / "20261008-jcm-stock-preparations/next-j261-context.json"
SHA = "da25a5f492f0fcc0bf1fdeca5f4cb0c80a261b7387c2c9acb83efdcc7b31b53c"


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
    specs = {r["key"]: r for r in context["records"]}
    key = item["key"]
    assert before == yaml.safe_load(specs[key]["before_text"])
    texts, sources = {}, {}
    for k, s in context["sources"].items():
        assert (
            hashlib.sha256(s["raw"].encode(s["metadata"]["encoding"])).hexdigest()
            == s["metadata"]["sha256"]
        )
        assert s["metadata"]["http_status"] == 200
        texts[k] = (
            " ".join(BeautifulSoup(s["raw"], "html.parser").get_text().split())
            if k.startswith("JCM")
            else s["raw"]
        )
        if not k.startswith("JCM"):
            sources[k] = json.loads(s["raw"])

    child = {"J151": "J261", "M142": "M253"}.get(key, key)
    parent = {"J261": "J151", "M253": "M142"}[child]
    other_key = parent if key == child else child
    other = yaml.safe_load(specs[other_key]["before_text"])
    link = (
        after["parent_media"]
        if key == child
        else next(v for v in after["variant_children"] if v["id"] == other["id"])
    )
    assert {k: link[k] for k in ("id", "name", "path", "relationship")} == {
        "id": other["id"],
        "name": other["name"],
        "path": specs[other_key]["path"],
        "relationship": "DERIVED_FROM",
    }
    assert len(link["evidence"]) == 2
    stats = collections.Counter()
    allowed = {"references", "curation_history", "variant_children"}
    if key == child:
        allowed |= {
            "parent_media",
            "variant_relationship",
            "variant_modifications",
            "ingredients",
            "solutions",
            "preparation_steps",
            "ph_value",
            "evidence",
        }
        assert after["variant_relationship"] == "DERIVED_FROM" and after["ph_value"] == 7.0
        assert len(after["variant_modifications"]) == 5
        assert "replacing the parent amount" in after["variant_modifications"][0]
        assert "replacing the parent amount" in after["variant_modifications"][1]
        assert "Omit elemental sulfur" in after["variant_modifications"][3]
        assert "instead of 6.5" in after["variant_modifications"][4]
        jcm = key == "J261"

        def rows(source, section):
            return (
                sources[source]["data"]["solutions"][section]["recipe"]
                if source.startswith("J")
                else sources[source]["components"][section]["items"]
            )

        expected = {}
        for i, section in enumerate((1, 2)):
            source = parent if jcm else key
            ri = i if jcm else 6 + i
            expected[("solutions", i)] = (source, 0, ri, "dose")
            for j, row in enumerate(rows(parent, section)):
                kind = (
                    "water"
                    if row.get("compound", row.get("component_name")) == "Distilled water"
                    else "rate" if jcm else "mass" if "volume" in row else "unquantified"
                )
                expected[("solutions", i, "composition", j)] = (parent, section, j, kind)
        for i, ri in enumerate((2, 7) if jcm else (0, 5, 8, 9)):
            expected[("ingredients", i)] = (
                parent if jcm else key,
                0,
                ri,
                "mass" if i < 2 else "unquantified" if i == 2 else "gas",
            )
        expected[("solutions", 2, "composition", 0)] = (
            parent if jcm else key,
            0,
            6 if jcm else 1,
            "mass",
        )
        final_start = 2 if jcm else 4
        rates = {
            ("ingredients", final_start): (
                "Yeast extract" if jcm else "Yeast extract (BD-Difco)",
                "2",
            ),
            ("ingredients", final_start + 1): (
                "Bacto peptone" if jcm else "Bacto peptone (BD-Difco)",
                "2",
            ),
            ("ingredients", final_start + 2): (
                "Na2S2O3 x 5H2O" if jcm else "Na2S2O3\u30fb5H2O",
                "1",
            ),
        }
        extras = {("solutions", 2)}
        if jcm:
            extras |= {("ingredients", 5), ("ingredients", 6), ("solutions", 1, "composition", 13)}
        nodes = {
            p
            for p, n in walk(after)
            if p
            and p[-2:-1] in {("ingredients",), ("composition",), ("solutions",)}
            and "preferred_term" in n
        }
        assert nodes == set(expected) | set(rates) | extras
        originals = {
            n["preferred_term"]: (f, i)
            for f in ("ingredients", "solutions")
            for i, n in enumerate(before.get(f, []))
        }
        seen = set()

        def annotations(path, name, source):
            node = get(after, path)
            op = originals.get(name) if source == key or jcm and source == parent else None
            old = get(before, op) if op else {}
            skip = {"concentration", "notes", "evidence", "composition", "preparation_notes"}
            if path in {("solutions", 0), ("solutions", 1)} and jcm:
                definition = sources[parent]["data"]["solutions"][path[1] + 1]
                assert node["term"] == {
                    "id": "mediadive.solution:" + str(definition["id"]),
                    "label": definition["name"],
                }
                skip.add("term")
            assert {k: v for k, v in node.items() if k not in skip} == (
                {k: v for k, v in old.items() if k not in skip} if old else {"preferred_term": name}
            )
            if op:
                seen.add(op)
                if old.get("notes"):
                    assert node["notes"].startswith(old["notes"])
            return old

        for path, (source, section, ri, kind) in expected.items():
            node = get(after, path)
            row = rows(source, section)[ri]
            name = row.get("compound", row.get("solution", row.get("component_name")))
            assert node["preferred_term"] == name
            old = annotations(path, name, source)
            amount, unit = row.get("amount", row.get("volume")), row.get("unit")
            if kind in {"dose", "water", "rate"}:
                value = (
                    Decimal(str(row["g_l"]))
                    if kind == "rate"
                    else Decimal(str(amount)) / (1000 if unit == "ml" else 1)
                )
                assert set(node["concentration"]) == {"value", "unit"}
                assert Decimal(node["concentration"]["value"]) == value
                assert node["concentration"]["unit"] == ("G_PER_L" if kind == "rate" else "L")
                if kind == "rate":
                    assert (
                        "provider-declared stock" in node["notes"]
                        and "not a final-medium concentration" in node["notes"]
                    )
                    stats["stock_stage_concentrations_rebased"] += bool(
                        old and old.get("concentration") != node["concentration"]
                    )
                if kind == "dose":
                    assert "per receiving batch" in node["notes"]
                    stats["stock_dose_basis_corrections"] += bool(old)
            elif kind == "gas":
                assert node == old and amount is None
            else:
                assert "concentration" not in node
                if kind == "mass":
                    assert f"Source batch input: {amount} {unit}." in node["notes"]
                    assert (
                        "Final preparation volume is not independently established" in node["notes"]
                    )
                else:
                    assert (
                        amount is None
                        and "no fixed dose" in node["notes"].lower()
                        or amount is None
                        and "without a fixed dose" in node["notes"]
                    )
                stats["unsupported_quantity_slots_removed"] += bool(old.get("concentration"))
            stats["stock_nodes_relocated"] += bool(
                old and path[0] == "solutions" and originals[name][0] == "ingredients"
            )
            if kind != "gas":
                claim = [
                    c
                    for c in item["claims"]
                    if c["pointer"]
                    == list(path)
                    + (["notes"] if kind == "unquantified" and not old else ["concentration"])
                    and c["source"] == source
                    and c["kind"] != "inheritance"
                ]
                assert len(claim) == 1
                source_path = (
                    ["data", "solutions", section, "recipe", ri]
                    if source.startswith("J")
                    else ["components", section, "items", ri]
                )
                assert claim[0]["source_pointer"] == source_path
        for path, (name, value) in rates.items():
            node = get(after, path)
            assert node["preferred_term"] == name and node["concentration"] == {
                "value": value,
                "unit": "G_PER_L",
            }
            old = annotations(path, name, key)
            assert "replaces the parent's amount" in node["notes"]
            assert len(node["evidence"]) == 2
            stats["quantity_corrections"] += bool(
                old and old.get("concentration") != node["concentration"]
            )
            stats["final_quantity_slots_added"] += not bool(old)
        if jcm:
            sulfur = originals["Sulfur"]
            seen.add(sulfur)
            archives = json.loads(after["curation_history"][-1]["changes"])
            assert next(c["omitted_node"] for c in archives if "omitted_node" in c) == get(
                before, sulfur
            )
            stats["explicitly_omitted_ingredient_nodes"] = 1
            for p, name in [
                (("ingredients", 5), "H2SO4"),
                (("ingredients", 6), "N2"),
                (("solutions", 1, "composition", 13), "KOH solution"),
            ]:
                node = get(after, p)
                assert node["preferred_term"] == name and set(node) == {
                    "preferred_term",
                    "notes",
                    "evidence",
                }
        assert seen == set(originals.values())
        assert len(after["ingredients"]) == 7 and len(after["solutions"]) == 3
        sulfide = after["solutions"][2]
        assert set(sulfide) == {"preferred_term", "composition", "notes", "preparation_notes"}
        assert "percentage basis" in sulfide["notes"] and "5%" in sulfide["preparation_notes"]
        assert "Steam sulfur" not in sulfide["preparation_notes"]
        assert (
            "not the mass for preparing an unspecified volume of stock"
            in sulfide["composition"][0]["notes"]
        )
        variant = (
            sources[child]["data"]["solutions"][0]["steps"][0]["step"]
            if jcm
            else sources[child]["comments"][2]["comment"]
        )
        steps = after["preparation_steps"]
        assert len(steps) == 3 and steps[0] == {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": variant,
        }
        assert steps[1]["action"] == "FILTER" and steps[2]["action"] == "MIX"
        assert all("7.0" in s["description"] and "6.5" not in s["description"] for s in steps)
        assert "No sulfur preparation or addition" in steps[2]["description"]
        trace = (
            sources[parent]["data"]["solutions"][2]["steps"][0]["step"]
            if jcm
            else sources[parent]["comments"][1]["comment"]
        )
        assert after["solutions"][1]["preparation_notes"] == trace
        old_slots = {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
        claimed = {
            tuple(c["old_pointer"])
            for c in item["claims"]
            if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
        }
        assert claimed == old_slots
        stats["old_quantity_slots"] = len(old_slots)
    assert {k: v for k, v in before.items() if k not in allowed} == {
        k: v for k, v in after.items() if k not in allowed
    }
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["curator"] == "codex"
    assert after["curation_history"][-1]["action"] == item["action"]
    prior = {(p, e["reference"]): e for p, n in walk(before) for e in n.get("evidence", [])}
    attached = dict(prior)
    for c in item["claims"]:
        p, op = c["pointer"], c["old_pointer"]
        assert c["old"] == (get(before, op[:-1]).get(op[-1]) if op else None)
        assert c["new"] == get(after, p[:-1]).get(p[-1])
        assert c["reference"] == context["sources"][c["source"]]["metadata"]["url"]
        assert c["snippet"] and c["snippet"] in texts[c["source"]]
        assert field(p) in c["explanation"] and "capture SHA256=" in c["explanation"]
        ep = c["evidence_pointer"]
        if ep is None:
            assert c["status"] == "unsupported" and c["kind"] == "gas"
            continue
        identity = (tuple(ep), c["reference"])
        if identity in attached:
            assert identity not in prior
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
    old_refs = before.get("references", [])
    assert after["references"][: len(old_refs)] == old_refs
    for ref in after["references"][len(old_refs) :]:
        assert set(ref) == {"reference", "title", "notes"}
        assert "Authors and publication year not supplied" in ref["notes"]
        assert "source_type=" in ref["notes"] and "discovery_mode=" in ref["notes"]
    assert {r["reference"] for r in after["references"]} == {r for p, r in attached}
    stats.update(
        new_evidence=len(actual) - len(prior),
        new_references=len(after["references"]) - len(old_refs),
        new_curation_history=1,
        claims=len(item["claims"]),
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
