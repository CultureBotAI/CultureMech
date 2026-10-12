"""Independent source, quantity, provenance and full-record inversion checks."""

import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium265.pdf"
MEDIUM = "https://mediadive.dsmz.de/rest/medium/265"
SOLUTION = "https://mediadive.dsmz.de/rest/solution/531"
ACTION = "RESTORED_DSMZ265_STOCK_STAGES_AND_ORIGINAL_SOURCE_DOSES"


def get(node, pointer):
    for part in pointer:
        node = node[part]
    return node


def count_provenance(node):
    counts = collections.Counter()
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"evidence", "references", "curation_history"}:
                counts["new_" + key] += len(value)
            else:
                counts.update(count_provenance(value))
    elif isinstance(node, list):
        for value in node:
            counts.update(count_provenance(value))
    return counts


def check(before, after, item, sources=None):
    sources = sources or json.loads((HERE / "plan.json").read_text())["sources"]
    stock_record = item["key"] == "solution"
    field = "composition" if stock_record else "ingredients"
    ref = SOLUTION if stock_record else MEDIUM
    raw = sources[ref]["raw"]
    assert hashlib.sha256(raw.encode()).hexdigest() == item["source_sha256"]
    source = json.loads(raw)["data"]
    data = source if stock_record else source["solutions"][0]
    assert data["id"] == 531 and data["volume"] == 1000
    assert before["id"] == after["id"] == item["id"] and item["action"] == ACTION
    assert (
        hashlib.sha256(sources[PDF]["raw"].encode()).hexdigest()
        == "9a228b1b3720116ac4de25b0f9bfb78ac8cc3b39600e3fe8ba62c4ee138f8790"
    )
    assert (
        sources[PDF]["metadata"]["sha256"]
        == "904a0973cffadca97f2da8c6b8cd2a89f5f842d53bdb98212d27aa86741ab173"
    )
    for c in item["claims"]:
        assert c["old"] == (get(before, c["old_pointer"]) if c["old_pointer"] is not None else None)
        assert c["new"] == get(after, c["pointer"])
        source_raw = sources[c["reference"]]["raw"]
        assert c["snippet"] and c["snippet"] in source_raw
        if c["source_pointer"] is not None:
            assert json.loads(c["snippet"]) == get(json.loads(source_raw), c["source_pointer"])
        entries = [
            e
            for e in get(after, c["evidence_pointer"])["evidence"]
            if e["reference"] == c["reference"]
        ]
        assert len(entries) == 1 and entries[0]["supports"] == "SUPPORT"
        evidence = entries[0]
        assert c["field"] in evidence["explanation"] and c["explanation"] in evidence["explanation"]
        assert c["locator"] in evidence["explanation"]
        assert c["snippet"] == evidence["snippet"] or c["snippet"] in evidence["explanation"]
        assert sources[c["reference"]]["metadata"]["sha256"] in evidence["explanation"]

    restored = copy.deepcopy(after)
    stocks = restored.pop("solutions")
    assert len(stocks) == 5
    for i, stock in enumerate(stocks):
        assert set(stock) == {
            "preferred_term",
            "composition",
            "source",
            "preparation_notes",
            "notes",
        } | ({"concentration"} if i else set())
        assert stock["source"] == PDF and stock["notes"] and stock["preparation_notes"]
    base = stocks[0]
    assert base["preferred_term"] == "Mineral salt preparation for medium 265"
    assert len(base["composition"]) == 13 and "concentration" not in base
    assert "not measured final stock or complete-medium" in base["notes"]
    assert "100% nitrogen" in base["preparation_notes"]
    assert len(restored[field]) == 1
    sulfur = restored[field][0]
    assert sulfur["preferred_term"] == "Sulfur" and "concentration" not in sulfur
    assert (
        "10 g powdered sulfur" in sulfur["notes"]
        and "3 h on each of three successive days" in sulfur["notes"]
    )
    assert "not retained as a final-medium concentration" in sulfur["notes"]
    water = base["composition"][-1]
    assert water["preferred_term"] == "Distilled water"
    assert (
        water["concentration"] == {"value": "1", "unit": "L"}
        and "not a final-volume" in water["notes"]
    )

    new_nodes = base["composition"][:-1] + [s["composition"][0] for s in stocks[1:]] + [sulfur]
    old_by_label = {n["preferred_term"]: n for n in before[field]}
    assert {n["preferred_term"] for n in new_nodes} == set(old_by_label) - (
        {"Distilled water"} if stock_record else set()
    )
    for index, node in enumerate(base["composition"][:12]):
        prior = before[field][index]
        assert (
            node["preferred_term"] == prior["preferred_term"] == data["recipe"][index]["compound"]
        )
        assert node["concentration"] == prior["concentration"]
        assert f"{data['recipe'][index]['amount']} {data['recipe'][index]['unit']}" in node["notes"]
        assert "not a verified concentration after supplement addition" in node["notes"]
    for stock, name, strength, volume in zip(
        stocks[1:4],
        ["Yeast extract", "Sucrose", "Na2S x 9 H2O"],
        ["10", "10", "3"],
        ["0.02", "0.02", "0.01"],
        strict=True,
    ):
        assert stock["preferred_term"] == f"{name} stock ({strength}% w/v)"
        assert stock["concentration"] == {"value": volume, "unit": "L"}
        assert len(stock["composition"]) == 2
        node, carrier = stock["composition"]
        assert node["preferred_term"] == name and node["concentration"] == {
            "value": strength,
            "unit": "PERCENT_W_V",
        }
        assert "batch addition" in stock["notes"] and "no" in carrier["notes"]
        assert (
            set(carrier) == {"preferred_term", "notes", "evidence"}
            and carrier["preferred_term"] == "Water"
        )
        assert len(carrier["evidence"]) == 1 and "water" in carrier["evidence"][0]["snippet"]
        if name == "Yeast extract":
            assert "20 mg/l" in node["notes"] and "2 g yeast" in node["notes"]
            assert (
                "boiled" in stock["preparation_notes"]
                and "not autoclaved" in stock["preparation_notes"]
            )
        elif name == "Sucrose":
            assert "filter-sterilized" in stock["preparation_notes"]
        else:
            assert "autoclaved under nitrogen" in stock["preparation_notes"]
    lipid = stocks[4]["composition"][0]
    assert len(stocks[4]["composition"]) == 1 and "concentration" not in lipid
    assert stocks[4]["concentration"] == {"value": "0.006-0.012", "unit": "L"}
    assert "10 ml/l" in stocks[4]["notes"] and "not silently substituted" in stocks[4]["notes"]
    assert (
        "extraction yield" in lipid["notes"] and "not inspected" in stocks[4]["preparation_notes"]
    )

    # Restore only reviewed fields; every identity, prior quote and other property must survive.
    for node in new_nodes + ([water] if stock_record else []):
        old = old_by_label[node["preferred_term"]]
        current_evidence = node.pop("evidence")
        refs = [e["reference"] for e in current_evidence]
        assert len(refs) == len(set(refs))
        for old_evidence in old.get("evidence", []):
            matches = [e for e in current_evidence if e["reference"] == old_evidence["reference"]]
            assert len(matches) == 1
            for key in ("snippet", "supports"):
                assert matches[0][key] == old_evidence[key]
            assert old_evidence["explanation"] in matches[0]["explanation"]
        for key in ("evidence", "notes", "concentration"):
            if key in old:
                node[key] = copy.deepcopy(old[key])
            else:
                node.pop(key, None)
        assert node == old, "Unreviewed ingredient/identity change"
    if not stock_record:
        assert set(water) == {"preferred_term", "term", "concentration", "notes", "evidence"}
        assert water["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
    restored[field] = [
        next(
            n
            for n in new_nodes + ([water] if stock_record else [])
            if n["preferred_term"] == old["preferred_term"]
        )
        for old in before[field]
    ]
    if stock_record:
        provenance = restored.pop("source_data")
        assert set(provenance) == {"origin", "evidence"} and provenance["origin"] == "MediaDive"
        root_entries = provenance["evidence"]
    else:
        root_entries = restored.pop("evidence")
    expected_refs = {PDF} | ({MEDIUM} if item["key"] == "dsmz" else set())
    if item["key"] == "komodo":
        mapping = sources["mapping_metadata"]["reference"]
        expected_refs.add(mapping)
        e = next(e for e in root_entries if e["reference"] == mapping)
        assert e["snippet"] == sources["mapping"]["snippet"] and "Identity only" in e["explanation"]
    assert {e["reference"] for e in root_entries} == expected_refs and len(root_entries) == len(
        expected_refs
    )
    if item["key"] == "dsmz":
        assert restored["preparation_steps"][1]["action"] == "MIX"
        assert (
            restored["preparation_steps"][3]["description"]
            == "Autoclave the mineral salt preparation at 121 \u00b0C for 15 min; prepare the supplements separately as specified."
        )
        restored["preparation_steps"][1]["action"] = before["preparation_steps"][1]["action"]
        restored["preparation_steps"][3]["description"] = before["preparation_steps"][3][
            "description"
        ]
    elif item["key"] == "komodo":
        steps = restored.pop("preparation_steps")
        assert steps[0] == {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": "Adjust final pH to 5.2.",
        }
        assert steps[1]["action"] == "MIX" and "prepared separately" in steps[1]["description"]
    assert "Historical aerobic/import annotations are not endorsed" in restored["notes"]
    if "notes" in before:
        assert restored["notes"].startswith(before["notes"] + "\n\n")
        restored["notes"] = before["notes"]
    else:
        restored.pop("notes")
    old_refs = before.get("references", [])
    assert restored["references"][: len(old_refs)] == old_refs
    added_refs = restored.pop("references")[len(old_refs) :]
    assert len(added_refs) == (3 if item["key"] == "komodo" else 1)
    assert PDF in {r["reference"] for r in added_refs}
    for r in added_refs:
        assert r["title"] and "source_type=" in r["notes"] and "discovery_mode=" in r["notes"]
        assert "authors" not in r and "year" not in r
    if old_refs:
        restored["references"] = copy.deepcopy(old_refs)
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert restored == before, "Unreviewed full-record change"
    counts = count_provenance(after)
    counts.subtract(count_provenance(before))
    counts.update(
        stock_nodes_relocated=16 + int(stock_record),
        new_quantity_slots=4 if stock_record else 5,
        unsupported_quantity_slots_removed=2,
        quantity_corrections=int(stock_record),
        stock_stage_concentrations_rebased=3,
        source_amount_conflicts_repaired=1,
        stock_descriptors_added=5,
        unquantified_carrier_nodes_added=3,
        evidence_scopes_corrected=0 if item["key"] == "komodo" else 12,
        ingredient_context_notes_added=18,
        ingredient_context_notes_corrected=3,
        water_input_nodes_added=0 if stock_record else 1,
        recipe_context_notes_corrected=1,
        preparation_actions_corrected=int(item["key"] == "dsmz"),
        preparation_descriptions_corrected=int(item["key"] == "dsmz"),
        preparation_steps_added=2 if item["key"] == "komodo" else 0,
    )
    return counts


def run(applied):
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        assert (
            hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest()
            == item["after_sha256" if applied else "before_sha256"]
        )
        before, after = [
            yaml.load(item[k], Loader=yaml.CSafeLoader) for k in ("before_text", "after_text")
        ]
        assert hashlib.sha256(item["after_text"].encode()).hexdigest() == item["after_sha256"]
        counts.update(check(before, after, item, plan["sources"]))
    return {
        "stage": "applied" if applied else "preflight",
        "records": 3,
        **counts,
        "full_record_inversion": True,
        "historical_snippets_preserved": True,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.applied)
    assert not args.out.exists(), "Refuse to overwrite audit"
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
