"""Independent source-row accounting and annotation-preservation audit."""

import argparse
import collections
import copy
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
CONTEXT_SHA = "4f83dadbef9fe726b997d4291bdc2ce2e0f0558a611421ec33748f4e822f9078"


def get(node, path):
    for part in path:
        node = node[part]
    return node


def field(path):
    return "".join(f"[{p}]" if isinstance(p, int) else "." + p for p in path).lstrip(".")


def walk(node, path=()):
    if isinstance(node, dict):
        yield path, node
        for key, value in node.items():
            yield from walk(value, path + (key,))
    elif isinstance(node, list):
        for i, value in enumerate(node):
            yield from walk(value, path + (i,))


def check(before, after, item):
    raw = (HERE / "inspected-context.json").read_bytes()
    assert hashlib.sha256(raw).hexdigest() == CONTEXT_SHA
    context = json.loads(raw)
    key = item["key"]
    spec = next(r for r in context["records"] if r["key"] == key)
    assert before == yaml.safe_load(spec["before_text"])
    assert after["id"] == before["id"] == spec["id"]
    parsed = {}
    for name, source in context["sources"].items():
        m, content = source["metadata"], source["raw"]
        assert hashlib.sha256(content.encode(m["encoding"])).hexdigest() == m["sha256"]
        assert m["http_status"] == 200 and m["url"] == m["response_url"]
        parsed[name] = (
            " ".join(BeautifulSoup(content, "html.parser").get_text().split())
            if name.startswith("JCM")
            else json.loads(content)
        )
    body = parsed[key]
    expected = {}
    descriptors = {}

    def component(path, source_path, kind):
        expected[tuple(path)] = (source_path, kind)

    def stock(path, source_path, per_liter=False, definition=None):
        descriptors[tuple(path)] = (source_path, per_liter, definition)

    # This map is derived from the inspected source graph, not the mutator lineage.
    if key in {"J985", "J265"}:

        def row(si, ri):
            return ["data", "solutions", si, "recipe", ri]

        def constituents(path, si, indices):
            for i, ri in enumerate(indices):
                source_path = row(si, ri)
                kind = (
                    "water"
                    if get(body, source_path)["compound"] == "Distilled water"
                    else "stock_rate"
                )
                component(path + ["composition", i], source_path, kind)

        direct = list(range(8)) if key == "J985" else list(range(7)) + list(range(9, 16))
        for i, ri in enumerate(direct):
            component(["ingredients", i], row(0, ri), "water" if ri == direct[-1] else "batch_mass")
        links = [(8, 1), (9, 2), (10, 3), (11, 4)] if key == "J985" else [(7, 1), (8, 2)]
        for i, (ri, si) in enumerate(links):
            stock(["solutions", i], row(0, ri), definition=si)
            indices = list(range(len(body["data"]["solutions"][si]["recipe"])))
            if (key == "J985" and si == 2) or (key == "J265" and si == 1):
                indices.remove(0)
            constituents(["solutions", i], si, indices)
        if key == "J985":
            acid = ["solutions", 1, "solutions", 0]
            stock(acid, row(2, 0))
            component(acid + ["composition", 0], row(2, 0), "stock_strength")
            liquids = [(4, 12), (5, 13), (6, 14)]
        else:
            trace = ["solutions", 0, "solutions", 0]
            stock(trace, row(1, 0), definition=3)
            constituents(trace, 3, range(13))
            liquids = [(2, 16), (3, 17)]
        for i, ri in liquids:
            stock(["solutions", i], row(0, ri), key == "J265" or ri == 14)
            component(["solutions", i, "composition", 0], row(0, ri), "liquid_reagent")
    else:
        assert key == "M257"
        for i in range(17):
            component(
                ["ingredients", i],
                ["components", 0, "items", i if i < 14 else i + 2],
                "water" if i == 0 else "gas" if i >= 14 else "batch_mass",
            )
        for i, section, ri in [(0, 0, 14), (1, 0, 15), (2, 1, 0), (3, 1, 1)]:
            stock(["solutions", i], ["components", section, "items", ri], section == 1)
        for i in range(3):
            component(
                ["solutions", 0, "composition", i], ["components", 2, "items", i], "batch_mass"
            )
        stock(["solutions", 0, "solutions", 0], ["components", 2, "items", 3])

    ingredient_paths = {
        p
        for p, n in walk(after)
        if p and p[-2:-1] in {("ingredients",), ("composition",)} and "preferred_term" in n
    }
    extra_koh = ("solutions", 0, "solutions", 0, "composition", 13)
    assert ingredient_paths == set(expected) | ({extra_koh} if key == "J265" else set())
    stock_paths = {
        p for p, n in walk(after) if p and p[-2:-1] == ("solutions",) and "preferred_term" in n
    }
    assert stock_paths == set(descriptors)
    originals = {n["preferred_term"]: (i, n) for i, n in enumerate(before["ingredients"])}
    seen_old, expected_lineage, counts = collections.Counter(), [], collections.Counter()
    for path, (source_path, kind) in expected.items():
        node, source_row = get(after, path), get(body, source_path)
        name = source_row.get("compound", source_row.get("component_name"))
        assert node["preferred_term"] == name
        old_i, old = originals.get(name, (None, {}))
        if old:
            seen_old[old_i] += 1
        amount = source_row.get("amount", source_row.get("volume"))
        unit = source_row.get("unit")
        if kind == "gas":
            assert amount is None and node == old
            continue
        expected_lineage.append(
            {
                "pointer": list(path),
                "old_pointer": ["ingredients", old_i] if old else None,
                "source": key,
                "source_pointer": source_path,
                "kind": kind,
            }
        )
        annotations = {
            k: v for k, v in node.items() if k not in {"notes", "concentration", "evidence"}
        }
        assert annotations == (
            {k: v for k, v in old.items() if k not in {"notes", "concentration", "evidence"}}
            if old
            else {"preferred_term": "Distilled water"}
        )
        if old.get("notes"):
            assert node["notes"].startswith(old["notes"] + "\n\n")
        if kind in {"batch_mass", "liquid_reagent"}:
            assert "concentration" not in node
            counts["unsupported_quantity_slots_removed"] += 1
            if kind == "batch_mass":
                assert (
                    unit in {"g", "mg"} and f"Source batch input: {amount} {unit}." in node["notes"]
                )
                assert "final preparation volume is not independently established" in node["notes"]
                counts["batch_mass_notes_unverified_concentrations"] += 1
            else:
                assert unit == "ml" and source_row["attribute"] in node["notes"]
                assert "percentage basis is unspecified" in node["notes"]
        else:
            value = (
                Decimal(str(amount)) / 1000
                if kind == "water"
                else Decimal("7.7") if kind == "stock_strength" else Decimal(str(source_row["g_l"]))
            )
            expected_unit = {"water": "L", "stock_strength": "MOLAR", "stock_rate": "G_PER_L"}[kind]
            assert set(node["concentration"]) == {"value", "unit"}
            assert (
                node["concentration"]["unit"] == expected_unit
                and Decimal(node["concentration"]["value"]) == value
            )
            if kind == "water":
                assert (
                    "batch input" in node["notes"]
                    and "not a measured final volume" in node["notes"]
                )
            elif kind == "stock_rate":
                assert (
                    "provider-declared stock" in node["notes"]
                    and "not a receiving-medium concentration" in node["notes"]
                )
            else:
                assert source_row["attribute"] == "7.7 M, 25%"
                assert "25% label has unspecified basis" in node["notes"]
            if not old:
                counts["new_quantity_slots"] += 1
                counts["water_input_nodes_added"] += 1
            elif node["concentration"] != old.get("concentration"):
                counts[
                    (
                        "quantity_corrections"
                        if kind == "water"
                        else "stock_stage_concentrations_rebased"
                    )
                ] += 1
        counts["stock_nodes_relocated"] += bool(old and path[:1] == ("solutions",))
    assert set(seen_old) == set(range(len(before["ingredients"])))
    assert {i: n for i, n in seen_old.items() if n > 1} == (
        {2: 2, 4: 2, 6: 2} if key == "J265" else {}
    )
    assert sorted(item["lineage"], key=lambda x: field(x["pointer"])) == sorted(
        expected_lineage, key=lambda x: field(x["pointer"])
    )
    for path, (source_path, per_liter, si) in descriptors.items():
        node, source_row = get(after, path), get(body, source_path)
        amount, unit = source_row.get("amount", source_row.get("volume")), source_row["unit"]
        value = Decimal(str(amount)) if per_liter or unit == "L" else Decimal(str(amount)) / 1000
        assert Decimal(node["concentration"]["value"]) == value
        assert node["concentration"]["unit"] == ("ML_PER_L" if per_liter else "L")
        assert set(node["concentration"]) == {"unit", "value"}
        if per_liter:
            text = (
                body["comments"][0]["comment"]
                if key == "M257"
                else body["data"]["solutions"][0]["steps"][1 if key == "J985" else 0]["step"]
            )
            assert "add per liter" in text and "per liter" in node["notes"]
        else:
            assert "not a dose per final liter" in node["notes"]
        if key == "M257":
            i = path[1] if len(path) == 2 else 4
            old = before["solutions"][i]
            assert {
                k: v
                for k, v in node.items()
                if k not in {"notes", "composition", "concentration", "solutions"}
            } == {
                k: v
                for k, v in old.items()
                if k not in {"notes", "composition", "concentration", "solutions"}
            }
            assert node["preferred_term"] == source_row["component_name"]
            if old.get("notes"):
                assert node["notes"].startswith(old["notes"] + "\n\n")
            counts["stock_dose_basis_corrections"] += 1
        else:
            assert set(node) <= {
                "preferred_term",
                "composition",
                "solutions",
                "concentration",
                "notes",
                "term",
                "preparation_notes",
            }
            if si is not None:
                definition = body["data"]["solutions"][si]
                assert source_row["solution_id"] == definition["id"]
                assert node["term"] == {
                    "id": "mediadive.solution:" + str(definition["id"]),
                    "label": definition["name"],
                }
                assert node["preferred_term"] == definition["name"]
            else:
                assert "term" not in node
            counts["stock_descriptors_added"] += 1
            counts["new_quantity_slots"] += 1

    supported_paths, old_slots, cited = set(), set(), set()
    for claim in item["claims"]:
        path, previous = claim["pointer"], claim["old_pointer"]
        assert claim["new"] == get(after, path[:-1]).get(path[-1])
        assert claim["old"] == (get(before, previous[:-1]).get(previous[-1]) if previous else None)
        assert claim["field"] == field(path)
        if previous and previous[-1] == "concentration":
            old_slots.add(tuple(previous))
        source = context["sources"][claim["source"]]
        text = parsed[claim["source"]] if claim["source"].startswith("JCM") else source["raw"]
        assert claim["snippet"] in text and claim["reference"] == source["metadata"]["url"]
        if claim["source_pointer"] is not None:
            assert json.loads(claim["snippet"]) == get(
                parsed[claim["source"]], claim["source_pointer"]
            )
        ep = claim["evidence_pointer"]
        if ep is None:
            assert claim["kind"] == "gas" and claim["status"] == "unsupported"
            continue
        entries = get(after, ep)["evidence"]
        matching = [e for e in entries if e["reference"] == claim["reference"]]
        assert len(matching) == 1
        e = matching[0]
        assert e["supports"] == "SUPPORT" and e["snippet"] in text
        assert (
            claim["snippet"] == e["snippet"]
            or "Additional exact excerpt: " + claim["snippet"] in e["explanation"]
        )
        assert claim["explanation"] in e["explanation"]
        assert (
            claim["field"] in claim["explanation"]
            and source["metadata"]["sha256"] in claim["explanation"]
        )
        supported_paths.add(tuple(ep))
        cited.add(claim["reference"])
    assert old_slots == {p + ("concentration",) for p, n in walk(before) if "concentration" in n}
    for p, node in walk(after):
        if "evidence" in node:
            assert p in supported_paths
            assert len({e["reference"] for e in node["evidence"]}) == len(node["evidence"])
            counts["new_evidence"] += len(node["evidence"])
        if "concentration" in node and p not in {("ingredients", i) for i in range(14, 17)}:
            assert any(
                c["pointer"] == list(p) + ["concentration"] and c["evidence_pointer"] is not None
                for c in item["claims"]
            )
    assert {r["reference"] for r in after["references"]} == cited
    assert len(after["references"]) == len(cited)
    for ref in after["references"]:
        assert "authors" not in ref and "year" not in ref
        assert (
            "source_type=" in ref["notes"]
            and "discovery_mode=" in ref["notes"]
            and "accessed_on=" in ref["notes"]
        )

    restored = copy.deepcopy(after)
    restored["ingredients"] = copy.deepcopy(before["ingredients"])
    if "solutions" in before:
        restored["solutions"] = copy.deepcopy(before["solutions"])
    else:
        restored.pop("solutions")
    if key == "J985":
        steps = copy.deepcopy(before["preparation_steps"])
        steps[1]["action"] = "ALIQUOT"
        assert after["preparation_steps"] == steps
        conflict = after["solutions"][4]["composition"][0]
        assert (
            "30%" in conflict["notes"]
            and "3%" in conflict["notes"]
            and "Unresolved source disagreement" in conflict["notes"]
        )
        assert "concentration" not in conflict
        counts["preparation_actions_corrected"] += 1
    elif key == "J265":
        assert after["preparation_steps"] == before["preparation_steps"][:2]
        assert (
            after["solutions"][0]["solutions"][0]["preparation_notes"]
            == before["preparation_steps"][2]["description"]
        )
        koh = get(after, extra_koh)
        assert (
            set(koh) == {"preferred_term", "notes", "evidence"}
            and koh["preferred_term"] == "KOH solution"
        )
        assert "no fixed amount or stock strength" in koh["notes"]
        counts["preparation_steps_relocated"] += 1
        counts["unquantified_carrier_nodes_added"] += 1
    else:
        assert after["preparation_steps"] == [
            {"step_number": 1, "action": "AUTOCLAVE", "description": body["comments"][0]["comment"]}
        ]
        assert (
            after["notes"]
            == before["notes"]
            + "\n\nPost-inoculation source instruction: "
            + body["comments"][1]["comment"]
        )
        restored["notes"] = before["notes"]
        counts["preparation_steps_added"] += 1
    if "preparation_steps" in before:
        restored["preparation_steps"] = copy.deepcopy(before["preparation_steps"])
    else:
        restored.pop("preparation_steps")
    restored.pop("references")
    restored.pop("evidence")
    event = restored["curation_history"].pop()
    assert event["action"] == item["action"] and event["curator"] == "codex"
    assert event["source"] == context["sources"][key]["metadata"]["url"]
    assert "preparation" in event["changes"] and "concentration" in event["changes"]
    assert restored == before, "Unreviewed semantic change"
    counts["new_references"] = len(cited)
    counts["new_curation_history"] = 1
    return dict(counts)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    plan = json.loads((HERE / "plan.json").read_text())
    totals, rows = collections.Counter(), []
    for item in plan["records"]:
        for state in ("before", "after"):
            assert (
                hashlib.sha256(item[state + "_text"].encode()).hexdigest()
                == item[state + "_sha256"]
            )
        if args.applied:
            assert Path(item["path"]).read_bytes() == item["after_text"].encode()
        counts = check(
            yaml.safe_load(item["before_text"]), yaml.safe_load(item["after_text"]), item
        )
        totals.update(counts)
        rows.append({"path": item["path"], "counts": counts})
    result = {"terminal": True, "applied": args.applied, "records": rows, "counts": dict(totals)}
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
