"""Independent full-record inversion of the water-only follow-up."""

import argparse
import copy
import hashlib
import json
from collections import Counter
from decimal import Decimal
from pathlib import Path

import yaml

FOLDER = Path(__file__).resolve().parent
ROOT = FOLDER.parents[2]


def check(before, after, item, source_raw):
    source = json.loads(source_raw)["data"]
    assert hashlib.sha256(source_raw.encode()).hexdigest() == item["source_sha256"]
    assert source["id"] == item["solution_id"]
    assert source["steps"] == [{"recipe_order": None, "step": "Adjust pH to 7.0."}]
    assert len(item["claims"]) == 1
    claim = item["claims"][0]
    assert claim["status"] == "correct"
    assert claim["pointer"][0] == "composition" and len(claim["pointer"]) == 2
    index = claim["pointer"][1]
    restored = copy.deepcopy(after)
    node = restored["composition"][index]
    old = before["composition"][index]
    assert node["term"] == old["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
    assert node["preferred_term"] == old["preferred_term"] == "Distilled water"
    assert old["concentration"] == claim["old"] == {"value": "1000", "unit": "PERCENT_V_V"}
    assert node["concentration"] == claim["new"] == {"value": "1", "unit": "L"}
    (row,) = [r for r in source["recipe"] if r["compound_id"] == 4]
    assert json.loads(claim["snippet"]) == row and claim["snippet"] in source_raw
    assert row["unit"] == "ml" and row["compound"] == "Distilled water"
    assert row["optional"] == 0 and not row["attribute"] and not row["condition"]
    assert Decimal(str(row["amount"])) / 1000 == Decimal(node["concentration"]["value"])
    evidence = node.pop("evidence")
    assert len(evidence) == 1 and not old.get("evidence")
    entry = evidence[0]
    reference = f"https://mediadive.dsmz.de/rest/solution/{source['id']}"
    assert entry["reference"] == claim["reference"] == reference
    assert entry["supports"] == "SUPPORT" and entry["snippet"] == claim["snippet"]
    assert entry["explanation"] == claim["explanation"]
    for text in (
        f"composition[{index}].concentration",
        "1000 ml / 1000 ml per L = 1 L",
        "Adjust pH to 7.0.",
        "$.data.steps[0]",
        "not a volume percentage",
        "No density or final-volume assumption",
        item["source_sha256"],
    ):
        assert text in entry["explanation"]
    node["concentration"] = copy.deepcopy(old["concentration"])
    old_refs = before.get("references", [])
    assert restored["references"][: len(old_refs)] == old_refs
    added_refs = len(restored["references"]) - len(old_refs)
    assert added_refs == (0 if any(r["reference"] == reference for r in old_refs) else 1)
    if added_refs:
        added = restored["references"].pop()
        assert added["reference"] == reference
        assert added["title"] == f"MediaDive solution {source['id']}: {source['name']}"
        assert (
            "source_type=dataset" in added["notes"]
            and "publication year not supplied" in added["notes"]
        )
    if "references" not in before:
        assert restored.pop("references") == []
    event = restored["curation_history"].pop()
    assert (
        event["action"]
        == item["action"]
        == "CORRECTED_SOURCE_EXPLICIT_WATER_INPUT_AFTER_PH7_REVIEW"
    )
    assert event["curator"] == "codex" and event["source"] == reference
    assert f"composition[{index}].concentration" in event["changes"]
    assert "1000 PERCENT_V_V -> 1 L" in event["changes"]
    assert restored == before, "Unrelated field/provenance changed"
    return {
        "quantity_corrections": 1,
        "new_evidence": 1,
        "new_references": added_refs,
        "new_curation_history": 1,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    plan = json.loads((FOLDER / "plan.json").read_text())
    ctx = json.loads((FOLDER / "inspected-context.json").read_text())
    contexts = {r["path"]: r for r in ctx["records"]}
    counts = Counter()
    for item in plan["records"]:
        before = item["before_text"].encode()
        after = (ROOT / item["path"]).read_bytes() if args.applied else item["after_text"].encode()
        assert hashlib.sha256(before).hexdigest() == item["before_sha256"]
        assert hashlib.sha256(after).hexdigest() == item["after_sha256"]
        counts.update(
            check(
                yaml.safe_load(before),
                yaml.safe_load(after),
                item,
                contexts[item["path"]]["source_raw"],
            )
        )
    result = {
        "records": len(plan["records"]),
        "applied": args.applied,
        "full_record_inversion": True,
        **counts,
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
