"""Independent source readback and full-record inversion of six input repairs."""

import argparse
import collections
import copy
import hashlib
import json
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ACTION = "CORRECTED_DSMZ467_WATER_AND_DSMZ469_FILTERED_PREPARATIONS"


def get(node, pointer):
    for key in pointer:
        node = node[key]
    return node


def count_provenance(node):
    result = collections.Counter()
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"evidence", "references", "curation_history"}:
                result["new_" + key] += len(value)
            else:
                result.update(count_provenance(value))
    elif isinstance(node, list):
        for child in node:
            result.update(count_provenance(child))
    return result


def check(before, after, item, sources=None):
    if sources is None:
        sources = json.loads((HERE / "plan.json").read_text())["sources"]
    mid, kind = item["key"].split("-")
    solution = kind == "solution"
    field = "composition" if solution else "ingredients"
    ref = "https://mediadive.dsmz.de/rest/" + (
        "solution/" + str(int(mid) + 492) if solution else "medium/" + mid
    )
    raw = sources[ref]["raw"]
    assert (
        hashlib.sha256(raw.encode()).hexdigest()
        == item["source_sha256"]
        == sources[ref]["metadata"]["sha256"]
    )
    source = json.loads(raw)
    data = source["data"] if solution else source["data"]["solutions"][0]
    assert data["id"] == int(mid) + 492 and data["volume"] == 1000 and len(data["recipe"]) == 7
    assert before["id"] == after["id"] == item["id"] and item["action"] == ACTION
    for c in item["claims"]:
        assert c["old"] == (get(before, c["old_pointer"]) if c["old_pointer"] is not None else None)
        assert c["new"] == get(after, c["pointer"])
        assert c["reference"] == ref and c["snippet"] in raw
        assert json.loads(c["snippet"]) == get(source, c["source_pointer"])
        entries = [
            e for e in get(after, c["evidence_pointer"])["evidence"] if e["reference"] == ref
        ]
        assert len(entries) == 1
        e = entries[0]
        assert e["supports"] == "SUPPORT" and c["field"] in e["explanation"]
        assert c["locator"] in e["explanation"] and item["source_sha256"] in e["explanation"]
        assert c["snippet"] == e["snippet"] or c["snippet"] in e["explanation"]
        for quote in c.get("extra_excerpts", []):
            assert quote["snippet"] in raw and quote["snippet"] in e["explanation"]

    restored = copy.deepcopy(after)
    water = restored[field][-1]
    assert water["preferred_term"] == ("Tap water" if mid == "467" else "Distilled water")
    assert water["concentration"] == {"value": "1" if mid == "467" else "0.98", "unit": "L"}
    assert data["recipe"][-1]["amount"] == (1000 if mid == "467" else 980)
    assert data["recipe"][-1]["unit"] == "ml" and "not a" in water["notes"]
    pdf = sources["pdfs"][mid]
    pdf_entries = (
        water["evidence"]
        if mid == "467"
        else (after["source_data"]["evidence"] if solution else after["evidence"])
    )
    p = [e for e in pdf_entries if e["reference"] == pdf["reference"]]
    assert (
        len(p) == 1 and p[0]["supports"] == "SUPPORT" and p[0]["snippet"] in pdf["extracted_text"]
    )
    assert pdf["pdf_sha256"] in p[0]["explanation"]
    if mid == "467":
        assert p[0]["snippet"] == "Tap water 1000.0 ml"
        assert restored[field][:6] == before[field][:6]
    else:
        assert p[0]["snippet"] == "Catalase and MgSO4 are sterilized separately by filtration."
        assert (
            "Distilled water 1000.0 ml" in p[0]["explanation"]
            and "does not partition" in p[0]["explanation"]
        )
        stocks = restored.pop("solutions")
        assert len(stocks) == 2 and len(restored[field]) == 5
        step = data["steps"][0]["step"]
        assert (
            "to 10 ml of distilled water each" in step
            and "sterilize separately by filtration" in step
        )
        for i in range(2):
            stock = stocks[i]
            assert set(stock) == {
                "preferred_term",
                "composition",
                "preparation_notes",
                "notes",
                "source",
            }
            assert (
                stock["preferred_term"]
                == "Separately filtered "
                + ("magnesium sulfate" if i == 0 else "catalase")
                + " preparation"
            )
            assert stock["source"] == ref and stock["preparation_notes"] == step.removeprefix(
                "Adjust pH to 7.0. "
            )
            assert (
                "not final stock volume" in stock["notes"]
                and "No filter pore size is specified" in stock["notes"]
            )
            assert len(stock["composition"]) == 2
            solute, carrier = stock["composition"]
            assert "concentration" not in solute and "withdrawn" in solute["notes"]
            assert ("0.2 g MgSO4 x 7 H2O" if i == 0 else "60 mg catalase") in solute["notes"]
            assert "final stock and medium volumes are unspecified" in solute["notes"]
            assert set(carrier) == {"preferred_term", "term", "concentration", "notes", "evidence"}
            assert carrier["preferred_term"] == "Distilled water"
            assert carrier["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
            assert carrier["concentration"] == {"value": "0.01", "unit": "L"}
            assert "not a measured final stock volume" in carrier["notes"]
        restored[field].pop()
        nodes = restored[field]
        nodes.insert(3, stocks[0]["composition"][0])
        nodes.append(stocks[1]["composition"][0])
        for i, (node, old, row) in enumerate(
            zip(nodes, before[field][:6], data["recipe"][:6], strict=True)
        ):
            assert node["preferred_term"] == old["preferred_term"] == row["compound"]
            entries = node.pop("evidence")
            assert len(entries) == 1 and entries[0]["reference"] == ref
            prior = old.get("evidence", [])
            if prior:
                for key in ("reference", "snippet", "supports"):
                    assert entries[0][key] == prior[0][key]
                assert prior[0]["explanation"] in entries[0]["explanation"]
                node["evidence"] = copy.deepcopy(prior)
            if i in (3, 5):
                node["concentration"] = copy.deepcopy(old["concentration"])
            else:
                assert (
                    node["concentration"]
                    == old["concentration"]
                    == {"value": str(row["g_l"]), "unit": "G_PER_L"}
                )
                assert (
                    "nominal main-recipe rate" in node["notes"]
                    and "not a concentration in the 980 ml" in node["notes"]
                )
            node.pop("notes")
            assert node == old, "Unreviewed ingredient/mapping change"
        if solution:
            provenance = restored.pop("source_data")
            assert set(provenance) == {"origin", "evidence"} and provenance["origin"] == "MediaDive"
            entries = provenance["evidence"]
        else:
            entries = restored.pop("evidence")
        assert len(entries) == (3 if kind == "komodo" else 2)
        assert entries[0]["reference"] == ref and entries[1] == p[0]
        if kind == "komodo":
            assert entries[2]["reference"] == sources["mapping_metadata"]["reference"]
            assert entries[2]["supports"] == "SUPPORT"
            assert entries[2]["snippet"] == sources["mapping"][mid]["snippet"]
            assert sources["mapping_metadata"]["sha256"] in entries[2]["explanation"]
        assert (
            "API allocation of 980 ml" in restored["notes"]
            and "does not independently specify 980/10/10" in restored["notes"]
        )
        assert "not measured final volumes" in restored["notes"]
        if "notes" in before:
            assert restored["notes"].startswith(before["notes"] + "\n\n")
            restored["notes"] = before["notes"]
        else:
            restored.pop("notes")
        if not solution:
            assert restored["preparation_steps"] == [
                {"step_number": 1, "action": "ADJUST_PH", "description": step}
            ]
            if kind == "komodo":
                restored.pop("preparation_steps")
            else:
                restored["preparation_steps"] = copy.deepcopy(before["preparation_steps"])
    if mid == "467" or solution:
        water.pop("notes")
        water.pop("evidence")
        water["concentration"] = copy.deepcopy(before[field][-1]["concentration"])
        assert water == before[field][-1]
        if mid == "469":
            restored[field].append(water)
    else:
        assert set(water) == {"preferred_term", "term", "concentration", "notes", "evidence"}
        assert water["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
    prior_refs = before.get("references", [])
    refs = restored.pop("references")
    assert refs[: len(prior_refs)] == prior_refs
    assert len(refs[len(prior_refs) :]) == (3 if item["key"] == "469-komodo" else 1)
    assert pdf["reference"] in {r["reference"] for r in refs[len(prior_refs) :]}
    for r in refs[len(prior_refs) :]:
        assert r["title"] and "source_type=" in r["notes"] and "discovery_mode=" in r["notes"]
        assert "authors" not in r and "year" not in r
    if prior_refs:
        restored["references"] = copy.deepcopy(prior_refs)
    event = restored["curation_history"].pop()
    assert event["action"] == ACTION and event["curator"] == "codex"
    assert ref in event["source"] and pdf["reference"] in event["source"]
    for c in item["claims"]:
        assert c["field"] in event["changes"]
    assert restored == before, "Unreviewed whole-record change"
    counts = count_provenance(after)
    counts.subtract(count_provenance(before))
    assert counts["new_evidence"] == (2 if mid == "467" else 12 if kind == "komodo" else 6)
    counts["quantity_corrections"] += int(mid == "467" or solution)
    if mid == "469":
        counts.update(
            stock_nodes_relocated=2,
            unsupported_quantity_slots_removed=2,
            new_quantity_slots=2 if solution else 3,
            stock_descriptors_added=2,
            ingredient_context_notes_added=9,
            recipe_context_notes_corrected=1,
            evidence_scopes_corrected=5 if kind != "komodo" else 0,
            preparation_actions_corrected=int(kind == "dsmz"),
            preparation_steps_added=int(kind == "komodo"),
        )
    else:
        counts["ingredient_context_notes_added"] += 1
    return counts


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    plan = json.loads((HERE / "plan.json").read_text())
    totals = collections.Counter()
    for item in plan["records"]:
        before = yaml.load(item["before_text"], Loader=yaml.CSafeLoader)
        raw = (ROOT / item["path"]).read_bytes() if args.applied else item["after_text"].encode()
        assert hashlib.sha256(raw).hexdigest() == item["after_sha256"]
        totals.update(check(before, yaml.load(raw, Loader=yaml.CSafeLoader), item, plan["sources"]))
    result = {
        "full_record_inversion": True,
        "records": len(plan["records"]),
        "applied": args.applied,
        **totals,
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
