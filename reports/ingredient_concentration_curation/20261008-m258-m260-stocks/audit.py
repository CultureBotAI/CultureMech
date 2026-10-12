"""Independent source-row, preparation-stage and evidence audit for M258/M260."""

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
SHA = "b8e92ccde02abf688c54a0dc916142a971f6336216f3be270c84d88c9886b926"
ACTION = "REPAIRED_M258_IDENTITY_AND_M260_NESTED_STOCK_WITH_EVIDENCE"


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

    def rows(source, section):
        return sources[source]["components"][section]["items"]

    number = {"M258": "266", "M260": "268"}[key]
    text = texts["JCM" + number]
    assert sources[key]["meta"]["original_media_id"] == "JCM_M" + number
    original = {
        n["preferred_term"]: (f, i)
        for f in ("ingredients", "solutions")
        for i, n in enumerate(before[f])
    }
    assert len(original) == sum(len(before[f]) for f in ("ingredients", "solutions"))
    expected = {}

    def add(p, source, si, ri, kind, op=None):
        assert p not in expected
        expected[p] = (source, si, ri, kind, op)

    def definition(p, source, section):
        ci, ni = 0, 0
        for ri, row in enumerate(rows(source, section)):
            name = row["component_name"]
            op = original.get(name) if source == key else None
            if row.get("reference_media_id"):
                assert (key, source, section, ri) == ("M260", "M260", 1, 10)
                np = p + ("solutions", ni)
                add(np, source, section, ri, "batch_dose", op)
                definition(np, "M142", 2)
                ni += 1
            elif name in {"KOH solution", "NaOH"}:
                add(p + ("solutions", ni), source, section, ri, "unquantified_titrant", op)
                ni += 1
            else:
                kind = (
                    "water"
                    if name == "Distilled water"
                    else "unquantified_product" if row.get("volume") is None else "batch_mass"
                )
                add(p + ("composition", ci), source, section, ri, kind, op)
                ci += 1

    di, stock_rows, reducer_rows = 0, [], []
    for ri, row in enumerate(rows(key, 0)):
        name = row["component_name"]
        if row.get("reference_media_id"):
            stock_rows.append(ri)
        elif name in {"Na2S\u30fb9H2O", "L--Cysteine\u30fbHCl\u30fbH2O"}:
            reducer_rows.append(ri)
        else:
            kind = (
                "unquantified_input"
                if row.get("volume") is None
                else "water" if name == "Distilled water" else "batch_mass"
            )
            add(("ingredients", di), key, 0, ri, kind, original[name])
            di += 1
    for i, ri in enumerate(stock_rows):
        row = rows(key, 0)[ri]
        p = ("solutions", i)
        add(p, key, 0, ri, "batch_dose", original[row["component_name"]])
        source = row["reference_media_id"]
        section = (
            {14: 1, 17: 2}[ri]
            if key == source == "M258"
            else 1 if source == "M260" else 2 if source == "M142" else 1
        )
        definition(p, source, section)
    reducers = []
    for i, ri in enumerate(reducer_rows, len(stock_rows)):
        p = ("solutions", i)
        reducers.append(p)
        add(p, key, 0, ri, "separate_preparation")
        add(
            p + ("composition", 0),
            key,
            0,
            ri,
            "batch_mass",
            original[rows(key, 0)[ri]["component_name"]],
        )
    actual = {
        p
        for p, n in walk(after)
        if "preferred_term" in n
        and p[-2:-1] in {("ingredients",), ("solutions",), ("composition",)}
    }
    assert actual == set(expected)
    stats, lineage, counted = collections.Counter(), [], set()
    for p, (source, si, ri, kind, op) in expected.items():
        node, row = get(after, p), rows(source, si)[ri]
        old_node = get(before, op) if op else {}
        excluded = {
            "notes",
            "concentration",
            "composition",
            "solutions",
            "evidence",
            "preparation_notes",
        }
        label = row["component_name"] + (
            " separately prepared solution" if kind == "separate_preparation" else ""
        )
        assert {k: v for k, v in node.items() if k not in excluded} == (
            {k: v for k, v in old_node.items() if k not in excluded}
            if old_node
            else {"preferred_term": label}
        )
        if old_node.get("notes"):
            assert node["notes"].startswith(old_node["notes"] + "\n\n")
        if old_node and "[Merged 2 duplicates:" in old_node.get("notes", ""):
            assert "earlier duplicate-summing note is superseded" in node["notes"]
        duplicate = op in counted
        if op and op[0] == "ingredients" and p[0] == "solutions" and not duplicate:
            stats["stock_nodes_relocated"] += 1
        amount, unit = row.get("volume"), row.get("unit")
        if kind in {"water", "batch_dose"}:
            assert unit in {"ml", "L"}
            value = Decimal(str(amount)) / (1000 if unit == "ml" else 1)
            assert set(node["concentration"]) == {"value", "unit"}
            assert (
                Decimal(node["concentration"]["value"]) == value
                and node["concentration"]["unit"] == "L"
            )
            assert (
                "not a measured final volume"
                if kind == "water"
                else "not grams per liter or a dose per final liter"
            ) in node["notes"]
            if old_node and not duplicate:
                stats[
                    (
                        "stock_dose_basis_corrections"
                        if kind == "batch_dose"
                        else "quantity_corrections"
                    )
                ] += node["concentration"] != old_node.get("concentration")
            else:
                stats["new_quantity_slots"] += 1
        else:
            assert "concentration" not in node
            if kind == "batch_mass":
                assert (
                    unit in {"g", "mg"} and f"Source batch input: {amount} {unit}." in node["notes"]
                )
                assert "Final preparation volume is not independently established" in node["notes"]
                if not old_node:
                    assert "withdrawn" not in node["notes"]
                if p[:-2] in reducers:
                    assert amount == 0.5 and unit == "g"
                    assert "contribution specified for the receiving medium batch" in node["notes"]
            elif kind == "unquantified_input":
                assert (
                    amount is None
                    and "Removed the unsupported VARIABLE placeholder" in node["notes"]
                )
                assert "not a fixed gas input" in node["notes"]
            elif kind == "unquantified_product":
                assert amount is None and "not an additional independent dose" in node["notes"]
                assert "300 ml receiving-batch input" in node["notes"]
            elif kind == "unquantified_titrant":
                assert amount is None and "no fixed dose" in node["notes"]
                assert node["composition"] == [] and not node.get("solutions")
            else:
                assert kind == "separate_preparation"
                assert (
                    "0.5 g receiving-batch contribution, not a stock-batch recipe" in node["notes"]
                )
                assert "source 5% label has unspecified percentage basis" in node["notes"]
                assert len(node["composition"]) == 1 and not node.get("solutions")
                stats["stock_descriptors_added"] += 1
            stats["unsupported_quantity_slots_removed"] += (
                bool(old_node.get("concentration")) and not duplicate
            )
        if op:
            counted.add(op)
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
    removed = {("ingredients", i) for i in (23, 24, 25)} if key == "M258" else set()
    assert counted | removed == {
        (f, i) for f in ("ingredients", "solutions") for i in range(len(before[f]))
    }
    assert not counted & removed
    stats["unsupported_quantity_slots_removed"] += len(removed)
    counts = collections.Counter(tuple(n["old_pointer"]) for n in lineage if n["old_pointer"])
    assert {p: n for p, n in counts.items() if n > 1} == {("ingredients", 0): 2}
    trace = next(
        n for p, n in walk(after) if n.get("preferred_term") == "Trace minerals (see Medium [M142])"
    )
    assert trace["preparation_notes"] == sources["M142"]["comments"][1]["comment"]
    assert literal_match(trace["preparation_notes"], texts["JCM151"])
    if key == "M258":
        assert len(after["ingredients"]) == 15 and len(after["solutions"]) == 6
        names = {n["preferred_term"] for p, n in walk(after) if p in expected}
        assert not names & {"Tryptone", "Yeast extract", "Sodium chloride"}
        alpha = after["solutions"][3]["composition"][4]
        assert alpha["preferred_term"] == "\u03b1-Methylbutyric acid"
        assert set(alpha) == {"preferred_term", "notes", "evidence"}
        rumen = text[
            text.index("To prepare the clarified rumen fluid,") : text.index("Fatty acid mixture:")
        ].strip()
        fatty = text[
            text.index("Adjust pH to 7.5 with concentrated NaOH solution.") : text.index(
                "Copyright"
            )
        ].strip()
        assert after["solutions"][0]["preparation_notes"] == rumen
        assert after["solutions"][3]["preparation_notes"] == fatty
        assert "preparation_notes" not in after["solutions"][2]
        starts = [
            "Mix ingredients",
            "Bring to a boil",
            "Dispense the medium",
            "After autoclaving",
            "Separately autoclave",
            "Prior to inoculation",
            "Pressurize",
        ]
        actions = ["MIX", "HEAT", "ALIQUOT", "STORE", "AUTOCLAVE", "MIX"]
        bounds = [text.index(s) for s in starts]
        steps = [
            {
                "step_number": i + 1,
                "action": a,
                "description": text[bounds[i] : bounds[i + 1]].strip(),
            }
            for i, a in enumerate(actions)
        ]
        pressure = text[bounds[-1] : text.index("To prepare the clarified rumen fluid,")].strip()
        for p in reducers:
            assert get(after, p)["preparation_notes"] == steps[4]["description"]
        marker = "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product:"
        restored = after["notes"].replace(marker, "\n\nCommercial Product:", 1)
        assert restored.startswith(before["notes"] + "\n\n")
        assert after["notes"].endswith("Original post-inoculation instruction: " + pressure)
        assert "three unrelated LB constituents are removed" in after["notes"]
        removal_claims = [c for c in item["claims"] if c["kind"] == "wrong_product_removed"]
        assert {tuple(c["old_pointer"][:-1]) for c in removal_claims} == removed
        assert all(
            c["snippet"] == "\u03b1-Methylbutyric acid 0.5 g" and c["pointer"] == ["notes"]
            for c in removal_claims
        )
    else:
        assert len(after["ingredients"]) == 7 and len(after["solutions"]) == 1
        seawater = after["solutions"][0]
        assert len(seawater["composition"]) == 10 and seawater["solutions"] == [trace]
        assert "preparation_notes" not in seawater
        assert "enclosing stock preparation, not directly to the final medium" in trace["notes"]
        steps = [{"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 7.5."}]
        assert after["notes"] == before["notes"]
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
        for si in range(len(sources[key]["components"]))
        for ri in range(len(rows(key, si)))
    } | {("M142", 2, i) for i in range(14)}
    if key == "M258":
        required_rows |= {("M190", 1, i) for i in range(11)}
    covered_rows = {
        (c["source"], c["source_pointer"][1], c["source_pointer"][3])
        for c in item["claims"]
        if c["source_pointer"] and c["source_pointer"][0] == "components"
    }
    assert required_rows == covered_rows
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
