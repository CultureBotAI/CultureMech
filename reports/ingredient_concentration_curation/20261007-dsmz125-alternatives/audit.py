"""Independently invert the water/alternative repair and verify literal evidence."""

import argparse
import collections
import copy
import hashlib
import json
from decimal import Decimal
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
STEP = "Add 5 ml methanol or incubate under methane-air (4:1). Adjust pH to 6.8."
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium125.pdf"
ACTION = "RESTORED_DSMZ125_ALTERNATIVE_CARBON_PREPARATIONS_AND_WATER_INPUT"


def restore(node, before, key):
    if key in before:
        node[key] = copy.deepcopy(before[key])
    else:
        node.pop(key)


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
    solution = item["key"] == "solution"
    field = "composition" if solution else "ingredients"
    reference = "https://mediadive.dsmz.de/rest/" + ("solution/223" if solution else "medium/125")
    raw = sources[reference]["raw"]
    assert hashlib.sha256(raw.encode()).hexdigest() == item["source_sha256"]
    source = json.loads(raw)["data"]
    source = source if solution else source["solutions"][0]
    assert source["id"] == 223 and source["volume"] == 1000
    assert [step["step"] for step in source["steps"]] == [STEP]
    restored = copy.deepcopy(after)
    counts = collections.Counter()

    def evidence(entry, quote=None, row=None):
        assert set(entry) == {"reference", "supports", "snippet", "explanation"}
        assert entry["reference"] == reference and entry["supports"] == "SUPPORT"
        assert entry["snippet"] and entry["snippet"] in raw and entry["explanation"]
        if quote is not None:
            assert entry["snippet"] == quote
        if row is not None:
            assert json.loads(entry["snippet"]) == row

    assert len(restored[field]) == 13 and len(before[field]) == (13 if solution else 12)
    for i, (old, new) in enumerate(zip(before[field][:12], restored[field][:12], strict=True)):
        row = source["recipe"][i]
        assert new["preferred_term"] == row["compound"]
        assert new["concentration"]["unit"] == "G_PER_L"
        assert Decimal(str(new["concentration"]["value"])) == Decimal(str(row["g_l"]))
        if item["key"] == "komodo":
            assert not old.get("evidence") and len(new["evidence"]) == 1
            evidence(new.pop("evidence")[0], row=row)
        assert new == old, (item["path"], i, "Existing ingredient/mapping/evidence drift")
    water = restored[field][12]
    assert water["preferred_term"] == "Distilled water"
    assert water["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
    assert water["concentration"] == {"value": "1", "unit": "L"}
    assert source["recipe"][12]["amount"] == 1000 and source["recipe"][12]["unit"] == "ml"
    assert (
        water["notes"]
        == "Batch distilled-water input: 1000 ml = 1 L; not a percentage or a measured final medium volume."
    )
    assert len(water["evidence"]) == 1
    evidence(water.pop("evidence")[0], row=source["recipe"][12])
    water.pop("notes")
    if solution:
        assert before[field][12]["concentration"] == {"value": "1000", "unit": "PERCENT_V_V"}
        water["concentration"] = copy.deepcopy(before[field][12]["concentration"])
        assert water == before[field][12]
        assert set(restored["source_data"]) == {"origin", "evidence"}
        assert restored["source_data"]["origin"] == "MediaDive"
        assert len(restored["source_data"]["evidence"]) == 1
        evidence(restored.pop("source_data")["evidence"][0], quote=STEP)
        counts["quantity_corrections"] += 1
    else:
        assert set(water) == {"preferred_term", "term", "concentration"}
        restored[field].pop()
        counts["new_quantity_slots"] += 1
        counts["water_input_nodes_added"] += 1
        variants = restored.pop("variants")
        assert len(variants) == 2
        expected = [
            (
                "Methanol preparation option",
                "SUPPLEMENTED_VARIANT",
                [
                    "Add 5 ml methanol to the source's common basal batch; do not combine this option with the methane-air alternative.",
                    "This is a batch addition, not 5 ml/L or 0.5% final-medium methanol; final volume and methanol purity are not specified.",
                ],
            ),
            (
                "Methane-air incubation option",
                "DERIVED_FROM",
                [
                    "Incubate under methane-air (4:1) as the alternative to adding methanol.",
                    "The gas ratio is not a liquid ingredient dose or a dissolved methane concentration; no gas pressure or total volume is specified.",
                ],
            ),
        ]
        for i, (variant, (name, relationship, modifications)) in enumerate(
            zip(variants, expected, strict=True)
        ):
            assert set(variant) == {
                "name",
                "relationship",
                "description",
                "modifications",
                "purpose",
                "evidence",
            }
            assert variant["name"] == name and variant["relationship"] == relationship
            assert variant["modifications"] == modifications
            assert variant["description"] and variant["purpose"]
            assert len(variant["evidence"]) == 1
            evidence(variant["evidence"][0], quote=STEP)
            assert f"variants[{i}]" in variant["evidence"][0]["explanation"]
        entries = restored.pop("evidence")
        assert len(entries) == (2 if item["key"] == "komodo" else 1)
        evidence(entries[0], quote=STEP)
        if item["key"] == "komodo":
            assert entries[1]["snippet"] == sources["mapping"]["snippet"]
            assert entries[1]["reference"] == sources["mapping_metadata"]["reference"]
            assert sources["mapping"]["cells"][:3] == ["125", "METHYLOBACTERIUM MEDIUM", "6.8"]
            assert sources["mapping"]["original_recipe"] == PDF
            assert "Identity only" in entries[1]["explanation"]
        assert restored["preparation_steps"] == [
            {"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 6.8."}
        ]
        restore(restored, before, "preparation_steps")
        counts["inline_variant_options_added"] += 2
        counts[
            (
                "preparation_steps_added"
                if item["key"] == "komodo"
                else "preparation_descriptions_corrected"
            )
        ] += 1

    notes_claim = next(c for c in item["claims"] if c["field"] == "notes and preparation evidence")
    assert restored["notes"] == notes_claim["new"] and before.get("notes") == notes_claim["old"]
    assert "Neither alternative is selected or combined here" in restored["notes"]
    assert "not a measured final volume" in restored["notes"]
    assert "not independently verified final concentrations" in restored["notes"]
    restore(restored, before, "notes")
    original_refs = before.get("references", [])
    assert restored["references"][: len(original_refs)] == original_refs
    added = restored["references"][len(original_refs) :]
    assert [r["reference"] for r in added] == (
        [reference, sources["mapping_metadata"]["reference"], PDF]
        if item["key"] == "komodo"
        else [PDF]
    )
    for ref in added:
        assert set(ref) == {"reference", "title", "notes"} and ref["title"]
        assert all(
            key in ref["notes"] for key in ("source_type=", "discovery_mode=", "accessed_on=")
        )
    restore(restored, before, "references")
    assert restored["curation_history"][:-1] == before["curation_history"]
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert reference in event["source"] and event["changes"]
    assert restored == before, (item["path"], "Unreviewed record changes")
    delta = count_provenance(after)
    delta.subtract(count_provenance(before))
    counts.update(delta)
    counts["recipe_context_notes_corrected"] += 1
    counts["ingredient_context_notes_added"] += 1
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        expected = item["after_sha256"] if args.applied else item["before_sha256"]
        assert hashlib.sha256(raw).hexdigest() == expected
        before = yaml.safe_load(item["before_text"])
        after = yaml.safe_load(raw if args.applied else item["after_text"])
        counts.update(check(before, after, item, plan["sources"]))
    result = {
        "stage": "applied" if args.applied else "preview",
        "records": len(plan["records"]),
        **counts,
        "full_record_inversion": True,
        "historical_snippets_preserved": True,
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
