"""Independent claim readback and full-record inversion for the medium 111 repair."""

import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
ACTION = "RESTORED_DSMZ111_GLUCOSE_STOCK_AND_INPUT_BASES"
MEDIUM = "https://mediadive.dsmz.de/rest/medium/111"
SOLUTION = "https://mediadive.dsmz.de/rest/solution/190"
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium111.pdf"
STEP = "Adjust pH to 6.5. Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling."
HASHES = {
    MEDIUM: "55fa3c48de7789fb9e99215742233e9067f86705cdb7492c046fa783a5cc839b",
    SOLUTION: "37e247b4ac27dd60eddd8185e4ff45fb86dd4bf7d4c0406bb20203df7a79f3c9",
}


def get(node, pointer):
    for key in pointer:
        node = node[key]
    return node


def count_provenance(node):
    count = collections.Counter()
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"evidence", "references", "curation_history"}:
                count["new_" + key] += len(value)
            else:
                count.update(count_provenance(value))
    elif isinstance(node, list):
        for value in node:
            count.update(count_provenance(value))
    return count


def check(before, after, item, sources=None):
    if sources is None:
        sources = json.loads((HERE / "plan.json").read_text())["sources"]
    stock_record = item["key"] == "solution"
    root_field = "composition" if stock_record else "ingredients"
    reference = SOLUTION if stock_record else MEDIUM
    raw = sources[reference]["raw"]
    assert hashlib.sha256(raw.encode()).hexdigest() == HASHES[reference] == item["source_sha256"]
    source = json.loads(raw)
    base = source["data"] if stock_record else source["data"]["solutions"][0]
    assert base["id"] == 190 and base["volume"] == 950
    assert [s["step"] for s in base["steps"]] == [STEP]
    assert len(base["recipe"]) == 11 and base["recipe"][0]["amount"] == 10
    assert before["id"] == after["id"] == item["id"] and item["action"] == ACTION
    for c in item["claims"]:
        assert c["old"] == (get(before, c["old_pointer"]) if c["old_pointer"] is not None else None)
        assert c["new"] == get(after, c["pointer"])
        assert c["reference"] == reference and c["snippet"] in raw
        assert json.loads(c["snippet"]) == get(source, c["source_pointer"])
        entries = [
            e for e in get(after, c["evidence_pointer"])["evidence"] if e["reference"] == reference
        ]
        assert len(entries) == 1
        entry = entries[0]
        assert entry["supports"] == "SUPPORT" and c["field"] in entry["explanation"]
        assert c["locator"] in entry["explanation"] and HASHES[reference] in entry["explanation"]
        assert c["snippet"] == entry["snippet"] or c["snippet"] in entry["explanation"]
        for quote in c.get("extra_excerpts", []):
            assert quote["snippet"] in raw and quote["snippet"] in entry["explanation"]
            assert quote["locator"] in entry["explanation"]

    restored = copy.deepcopy(after)
    stock = restored.pop("solutions")[0]
    assert set(stock) == {"preferred_term", "composition", "preparation_notes", "notes", "source"}
    assert stock["preferred_term"] == "Separately sterilized glucose preparation"
    assert (
        stock["preparation_notes"]
        == "Sterilize glucose separately (10 g in 50 ml H2O) and mix after cooling."
    )
    assert stock["source"] == reference
    assert "not a measured stock volume" in stock["notes"]
    assert len(stock["composition"]) == 2 and "concentration" not in stock
    glucose, stock_water = stock["composition"]
    assert "concentration" not in glucose
    assert "10 g glucose in 50 ml H2O" in glucose["notes"] and "withdrawn" in glucose["notes"]
    assert "neither final volume is specified" in glucose["notes"]
    assert set(stock_water) == {"preferred_term", "concentration", "notes", "evidence"}
    assert stock_water["preferred_term"] == "Water" and stock_water["concentration"] == {
        "value": "0.05",
        "unit": "L",
    }
    assert "purity and final stock volume are not specified" in stock_water["notes"]
    assert len(restored[root_field]) == 10
    water = restored[root_field].pop()
    assert water["preferred_term"] == "Distilled water" and water["concentration"] == {
        "value": "0.95",
        "unit": "L",
    }
    assert water["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
    assert base["recipe"][10]["amount"] == 950 and base["recipe"][10]["unit"] == "ml"
    assert "not a final-volume" in water["notes"]
    for node, old, row in zip(
        [glucose] + restored[root_field], before[root_field][:10], base["recipe"][:10], strict=True
    ):
        assert node["preferred_term"] == old["preferred_term"] == row["compound"]
        if node is not glucose:
            assert (
                node["concentration"]
                == old["concentration"]
                == {"value": str(row["g_l"]), "unit": "G_PER_L"}
            )
            assert f"{row['amount']} {row['unit']}" in node["notes"]
            assert "not an independently verified concentration" in node["notes"]
        new_entries = node.pop("evidence")
        prior = old.get("evidence", [])
        assert len(new_entries) == 1 and new_entries[0]["reference"] == reference
        if prior:
            assert len(prior) == 1
            for key in ("reference", "snippet", "supports"):
                assert new_entries[0][key] == prior[0][key]
            assert prior[0]["explanation"] in new_entries[0]["explanation"]
            node["evidence"] = copy.deepcopy(prior)
        node.pop("notes")
        if node is glucose:
            node["concentration"] = copy.deepcopy(old["concentration"])
        assert node == old, "Unexpected ingredient/mapping change"
    restored[root_field].insert(0, glucose)
    if stock_record:
        water.pop("evidence")
        water.pop("notes")
        water["concentration"] = copy.deepcopy(before[root_field][-1]["concentration"])
        assert water == before[root_field][-1]
        restored[root_field].append(water)
        provenance = restored.pop("source_data")
        assert set(provenance) == {"origin", "evidence"} and provenance["origin"] == "MediaDive"
        root_entries = provenance["evidence"]
    else:
        assert set(water) == {"preferred_term", "term", "concentration", "notes", "evidence"}
        root_entries = restored.pop("evidence")
    assert root_entries[0]["reference"] == reference and root_entries[0]["supports"] == "SUPPORT"
    if item["key"] == "komodo":
        assert (
            len(root_entries) == 2 and root_entries[1]["snippet"] == sources["mapping"]["snippet"]
        )
        assert sources["mapping_metadata"]["sha256"] in root_entries[1]["explanation"]
        assert restored.pop("preparation_steps") == [
            {"step_number": 1, "action": "ADJUST_PH", "description": STEP}
        ]
    else:
        assert len(root_entries) == 1
    assert "two water inputs do not establish a measured 1 L final volume" in restored["notes"]
    if "notes" in before:
        assert restored["notes"].startswith(before["notes"] + "\n\n")
        restored["notes"] = before["notes"]
    else:
        restored.pop("notes")
    prior_refs = before.get("references", [])
    assert restored["references"][: len(prior_refs)] == prior_refs
    added_refs = restored.pop("references")[len(prior_refs) :]
    assert len(added_refs) == (3 if item["key"] == "komodo" else 1)
    assert PDF in {r["reference"] for r in added_refs}
    for r in added_refs:
        assert r["title"] and "source_type=" in r["notes"] and "discovery_mode=" in r["notes"]
        assert "authors" not in r and "year" not in r
    if prior_refs:
        restored["references"] = copy.deepcopy(prior_refs)
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert restored == before, "Unreviewed whole-record change"
    counts = count_provenance(after)
    counts.subtract(count_provenance(before))
    assert counts["new_evidence"] == (14 if item["key"] == "komodo" else 3)
    counts.update(
        stock_nodes_relocated=1,
        unsupported_quantity_slots_removed=1,
        new_quantity_slots=1 if stock_record else 2,
        quantity_corrections=1 if stock_record else 0,
        stock_descriptors_added=1,
        ingredient_context_notes_added=12,
        evidence_scopes_corrected=0 if item["key"] == "komodo" else 10,
        recipe_context_notes_corrected=1,
        preparation_steps_added=int(item["key"] == "komodo"),
    )
    return counts


def run(applied):
    plan = json.loads((HERE / "plan.json").read_text())
    total = collections.Counter()
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        expected = item["after_sha256"] if applied else item["before_sha256"]
        assert hashlib.sha256(raw).hexdigest() == expected
        before, after = [
            yaml.load(item[k], Loader=yaml.CSafeLoader) for k in ("before_text", "after_text")
        ]
        assert hashlib.sha256(item["after_text"].encode()).hexdigest() == item["after_sha256"]
        total.update(check(before, after, item, plan["sources"]))
    return {
        "stage": "applied" if applied else "preflight",
        "records": len(plan["records"]),
        **total,
        "full_record_inversion": True,
        "historical_snippets_preserved": True,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    result = run(args.applied)
    assert not args.out.exists(), "Refuse to overwrite an audit"
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))
