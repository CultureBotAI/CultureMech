"""Independent source assertions and whole-record inversion for nine water repairs."""

import argparse
import collections
import copy
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ACTION = "CORRECTED_DSMZ803_1046_1065_WATER_INPUT_UNITS"
CONTEXT_SHA = "8ec4c3dae8b5a3a0ee707c6ee2757ae7bbf4f41984e15f270697afa21eb03d5b"


def get(doc, pointer):
    for part in pointer:
        doc = doc[part]
    return doc


def check(before, after, item):
    raw_context = (HERE / "inspected-context.json").read_bytes()
    assert hashlib.sha256(raw_context).hexdigest() == CONTEXT_SHA
    mid, kind = item["key"].split("-")
    group = next(g for g in json.loads(raw_context)["groups"] if g["medium_id"] == mid)
    original = next(r for r in group["records"] if r["kind"] == kind)
    assert original["id"] == before["id"] == after["id"] == item["id"]
    assert original["path"] == item["path"] and item["action"] == ACTION
    assert item["before_text"] == original["before_text"]
    assert before == yaml.load(original["before_text"], Loader=yaml.CSafeLoader)
    assert hashlib.sha256(item["before_text"].encode()).hexdigest() == item["before_sha256"]
    solution = kind == "solution"
    source_kind = "solution" if solution else "medium"
    raw, meta = group[source_kind + "_raw"], group[source_kind + "_metadata"]
    assert hashlib.sha256(raw.encode()).hexdigest() == meta["sha256"] == item["source_sha256"]
    sid = {"803": 1634, "1046": 2114, "1065": 2155}[mid]
    ref = f"https://mediadive.dsmz.de/rest/{source_kind}/{sid if solution else mid}"
    assert meta["url"] == meta["response_url"] == ref and meta["http_status"] == 200
    source = json.loads(raw)
    data = source["data"] if solution else source["data"]["solutions"][0]
    assert data["id"] == sid and data["name"] == "Main sol. " + mid
    field = "composition" if solution else "ingredients"
    index = {"803": 8, "1046": 2, "1065": 5}[mid]
    old = before[field][index]
    water = after[field][index]
    row = data["recipe"][index]
    label = "Sea water" if mid == "1065" else "Tap water"
    assert row["compound"] == label == water["preferred_term"] == old["preferred_term"]
    assert row["compound_id"] == (286 if mid == "1065" else 322)
    assert row["amount"] == 1000 and row["unit"] == "ml" and row["optional"] == 0
    assert old["concentration"] == {
        "value": "1000",
        "unit": "PERCENT_V_V" if solution else "G_PER_L",
    }
    assert water["concentration"] == {"value": "1", "unit": "L"}
    assert Decimal(water["concentration"]["value"]) == Decimal(row["amount"]) / 1000
    expected_note = f"Source batch input: 1000 ml {label.lower()} = 1 L. This is an input volume, not a mass concentration, volume percentage or measured final-medium volume. No density or final-volume assumption is made."
    assert water["notes"] == expected_note and "notes" not in old and "evidence" not in old
    assert len(water["evidence"]) == 2
    api, pdf_entry = water["evidence"]
    assert api["reference"] == ref and api["supports"] == "SUPPORT"
    assert api["snippet"] in raw and json.loads(api["snippet"]) == row
    scope = f"{field}[{index}].concentration"
    for value in (scope, expected_note, meta["sha256"], meta["accessed_at"]):
        assert value in api["explanation"]
    pdf = group["pdf"]
    quote = {
        "803": "Tap water 1000.00 ml",
        "1046": "Tap water 1000.0 ml",
        "1065": "Sea water 1000.0 ml",
    }[mid]
    assert pdf_entry["reference"] == pdf["reference"] and pdf_entry["supports"] == "SUPPORT"
    assert pdf_entry["snippet"] == quote and quote in pdf["pages"][0]
    for value in (scope, expected_note, pdf["sha256"], pdf["accessed_at"], "page 1"):
        assert value in pdf_entry["explanation"]
    assert after["references"][:-1] == before["references"]
    reference = after["references"][-1]
    assert reference["reference"] == pdf["reference"]
    assert (
        reference["title"] == f"{mid}. " + json.loads(group["medium_raw"])["data"]["medium"]["name"]
    )
    assert reference["title"] in pdf["pages"][0]
    assert "year" not in reference and "authors" not in reference
    assert "2007 copyright notice is not treated as publication year" in reference["notes"]
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert (
        event["action"] == ACTION
        and event["curator"] == "codex"
        and event["source"] == pdf["reference"]
    )
    assert scope in event["changes"] and "-> 1 L" in event["changes"]
    changed = [c for c in item["claims"] if c["status"] == "correct"]
    assert len(changed) == 1 and changed[0]["pointer"] == [field, index]
    assert changed[0]["old"] == old["concentration"] and changed[0]["new"] == water["concentration"]
    assert changed[0]["snippet"] == api["snippet"] and changed[0]["corroboration"] == pdf_entry
    assert len(item["claims"]) == len(data["recipe"]) + int(solution)
    for i, source_row in enumerate(data["recipe"]):
        if i == index:
            continue
        node = after[field][i]
        assert node == before[field][i]
        assert node["concentration"]["unit"] == "G_PER_L"
        assert Decimal(node["concentration"]["value"]) == Decimal(str(source_row["g_l"]))
    restored = copy.deepcopy(after)
    restored[field][index]["concentration"] = copy.deepcopy(old["concentration"])
    restored[field][index].pop("notes")
    restored[field][index].pop("evidence")
    restored["references"].pop()
    restored["curation_history"].pop()
    assert restored == before, "Unreviewed change outside water/provenance"
    return collections.Counter(
        quantity_corrections=1,
        new_evidence=2,
        new_references=1,
        new_curation_history=1,
        water_input_notes_added=1,
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert (
            hashlib.sha256(raw).hexdigest()
            == item["after_sha256" if args.applied else "before_sha256"]
        )
        assert hashlib.sha256(item["after_text"].encode()).hexdigest() == item["after_sha256"]
        before, after = [
            yaml.load(item[k + "_text"], Loader=yaml.CSafeLoader) for k in ("before", "after")
        ]
        counts.update(check(before, after, item))
    result = {"records": len(plan["records"]), "applied": args.applied, **dict(counts)}
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
