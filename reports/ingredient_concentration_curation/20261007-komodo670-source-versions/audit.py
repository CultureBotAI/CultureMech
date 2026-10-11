"""Independent source semantics and whole-record inversion for the 670 variants."""

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
ARCHIVE = "https://bacdive.dsmz.de/pdf/4303?doi=10.13145%2Fbacdive4303.20170829.2"
DOI = "doi:10.13145/bacdive4303.20170829.2"
CURRENT = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium670.pdf"
ACTION = "CURATED_KOMODO670_STRAIN_RECIPES_WITH_SEPARATE_SOURCE_VERSIONS"


def get(doc, pointer):
    for key in pointer:
        doc = doc[key]
    return doc


def provenance(node):
    counts = collections.Counter()
    if isinstance(node, dict):
        for key, value in node.items():
            if key in {"evidence", "references", "curation_history"}:
                counts["new_" + key] += len(value)
            else:
                counts.update(provenance(value))
    elif isinstance(node, list):
        for value in node:
            counts.update(provenance(value))
    return counts


def evidence_lists(node):
    if isinstance(node, dict):
        for key, value in node.items():
            if key == "evidence":
                assert len(value) == len({e["reference"] for e in value})
                yield value
            else:
                yield from evidence_lists(value)
    elif isinstance(node, list):
        for value in node:
            yield from evidence_lists(value)


def check(before, after, item, sources=None):
    if sources is None:
        sources = json.loads((HERE / "plan.json").read_text())["sources"]
    # Pins are independent of the mutator and the editable proposal values.
    captures = HERE / "source-captures.json"
    assert (
        hashlib.sha256(captures.read_bytes()).hexdigest()
        == "c8023885299b84010701934109560f7ce3fa4b90f77c49ef890499bbb67caace"
    )
    original_sources = {s["key"]: s for s in json.loads(captures.read_text())["sources"]}
    assert all(sources[k] == v for k, v in original_sources.items())
    prior = HERE.parent / "20261007-dsmz546-659-670-stocks"
    handoff_raw = (prior / "next-variant-handoff.json").read_bytes()
    assert (
        hashlib.sha256(handoff_raw).hexdigest()
        == "ca8a5bb485e4cc985e2ef7ad52173a0a19251a1d7398c472ce9f740b2c5dcbd8"
    )
    handoff = json.loads(handoff_raw)
    pdf_raw = Path(handoff["pdf_captures"]).read_bytes()
    assert hashlib.sha256(pdf_raw).hexdigest() == handoff["pdf_captures_sha256"]
    assert sources["current"] == next(
        s for s in json.loads(pdf_raw)["sources"] if s["medium_id"] == "670"
    )
    assert sources["mapping_source"] == handoff["mapping_source"]
    for record in handoff["records"][:4]:
        assert sources[record["record"]["name"].removeprefix("for_dsm_")] == record["mapping"]
    key = item["key"]
    if key == "parent":
        raw = (prior / "plan.json").read_bytes()
        assert (
            hashlib.sha256(raw).hexdigest()
            == "3cd5480368b89753710871a2aeed202dd7014e8a00082953d7ab21542584ad2e"
        )
        prior_item = next(r for r in json.loads(raw)["records"] if r["key"] == "670-komodo")
        assert item["before_sha256"] == prior_item["after_sha256"]
        assert before == yaml.load(prior_item["after_text"], Loader=yaml.CSafeLoader)
    else:
        r = next(r for r in handoff["records"] if r["id"] == before["id"])
        assert before == r["record"] and item["before_sha256"] == r["sha256"]
    counts = provenance(after)
    counts.subtract(provenance(before))
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["curator"] == "codex" and event["action"] == ACTION and event["source"] == ARCHIVE
    assert after["references"][: len(before.get("references", []))] == before.get("references", [])
    refs = {r["reference"]: r for r in after["references"]}
    assert len(refs) == len(after["references"])
    attrs = sources["datacite4303"]["data"]["data"]["attributes"]
    for ref in (ARCHIVE, DOI):
        assert refs[ref]["year"] == attrs["publicationYear"] == 2017
        assert refs[ref]["title"] == attrs["titles"][0]["title"]
        assert refs[ref]["authors"] == "; ".join(c["name"] for c in attrs["creators"])
        assert "version=2" in refs[ref]["notes"] and "discovery_mode=" in refs[ref]["notes"]
    old_text = sources["bacdive4303"]["pages"][1]["text"]
    new_text = sources["current"]["pages"][0]["text"]
    assert "Distilled water 1000.00 ml" in old_text and "Distilled water 950.00 ml" in new_text
    for claim in item["claims"]:
        assert claim["new"] == (get(after, claim["pointer"]) if claim["pointer"] else None)
        assert claim["old"] == (get(before, claim["old_pointer"]) if claim["old_pointer"] else None)
        content = new_text if claim["reference"] == CURRENT else old_text
        if claim["reference"] not in {ARCHIVE, CURRENT}:
            content = sources[key]["snippet"]
        assert claim["snippet"] and claim["snippet"] in content
        ev = next(
            e
            for e in get(after, claim["evidence_pointer"])["evidence"]
            if e["reference"] == claim["reference"]
        )
        assert claim["snippet"] == ev["snippet"] or claim["snippet"] in ev["explanation"]
        assert claim["field"] in ev["explanation"] and claim["explanation"] in ev["explanation"]
        assert claim["field"] in event["changes"]
    old_evidence = [e for entries in evidence_lists(before) for e in entries]
    new_evidence = [e for entries in evidence_lists(after) for e in entries]
    assert all(e in new_evidence for e in old_evidence)
    for ev in new_evidence:
        if ev in old_evidence:
            continue
        content = {ARCHIVE: old_text, CURRENT: new_text}.get(ev["reference"])
        if content is None:
            content = sources[key]["snippet"]
        assert ev["supports"] == "SUPPORT" and ev["snippet"] in content
    restored = copy.deepcopy(after)
    common = {"notes", "references", "evidence", "curation_history"}
    if key == "parent":
        assert after["variant_children"][:2] == before["variant_children"][:2]
        assert len(after["variant_children"]) == 6
        for i, strain in enumerate(("9463", "9466", "9467", "9468"), 2):
            link = after["variant_children"][i]
            assert link["relationship"] == "STRAIN_SPECIFIC_VARIANT"
            assert "archived 2017" in link["notes"] and "DSM " + strain in link["notes"]
            copy_link = copy.deepcopy(link)
            for field in ("relationship", "notes"):
                copy_link[field] = before["variant_children"][i][field]
            copy_link.pop("evidence")
            assert copy_link == before["variant_children"][i]
        common.add("variant_children")
        counts["parent_links_corrected"] += 4
    else:
        assert key in {"9463", "9466", "9467", "9468"}
        nodes = after["ingredients"]
        assert len(nodes) == {"9463": 7, "9466": 8, "9467": 6, "9468": 6}[key]
        for i, mass in enumerate(("2.00", "0.25", "0.10", "0.10")):
            assert (
                "concentration" not in nodes[i]
                and "batch input: " + mass + " g" in nodes[i]["notes"]
            )
            clean = copy.deepcopy(nodes[i])
            del clean["notes"], clean["evidence"]
            clean["concentration"] = before["ingredients"][i]["concentration"]
            assert clean == before["ingredients"][i]
        assert nodes[4]["preferred_term"] == "Distilled water"
        assert set(nodes[4]) == {"preferred_term", "concentration", "notes", "evidence"}
        assert nodes[4]["concentration"] == {"value": "1", "unit": "L"}
        assert Decimal("1000") / 1000 == Decimal(nodes[4]["concentration"]["value"])
        acid = nodes[5]
        assert "concentration" not in acid
        normality = {"9463": "1", "9466": "1", "9467": "2", "9468": "4"}[key]
        assert normality + " N sulfuric acid" in acid["notes"]
        assert (
            after["ph_value"]
            == before["ph_value"]
            == {"9463": 3.5, "9466": 3.5, "9467": 3.0, "9468": 1.6}[key]
        )
        assert after["data_quality_flags"] == ["pending_curation"]
        assert (
            after["variant_relationship"]
            == after["parent_media"]["relationship"]
            == "STRAIN_SPECIFIC_VARIANT"
        )
        for f in ("path", "id", "name"):
            assert after["parent_media"][f] == before["parent_media"][f]
        para_start = old_text.index("For DSM " + key + ":")
        para_end = old_text.find("For DSM ", para_start + 1)
        if para_end == -1:
            para_end = old_text.index("\nTemperatures", para_start)
        para = old_text[para_start:para_end].strip()
        assert after["preparation_steps"] == [
            {"step_number": 1, "action": "ADJUST_PH", "description": " ".join(para.split())}
        ]
        assert after["variant_modifications"][1] == " ".join(para.split())
        assert "does not prove which recipe version" in after["notes"]
        assert "not its growth, temperature or taxonomic claims" in after["notes"]
        assert len(after["variants"]) == 1
        variant = after["variants"][0]
        assert variant["relationship"] == "DERIVED_FROM" and "DSM " + key in variant["name"]
        assert (
            "950 ml" in variant["modifications"][0]
            and "not the archive" in variant["modifications"][0]
        )
        assert all(e["reference"] == CURRENT for e in variant["evidence"])
        counts.update(
            unsupported_quantity_slots_removed=4,
            new_quantity_slots=1,
            child_links_corrected=1,
            source_version_alternatives_added=1,
        )
        if key != "9468":
            assert all("FeSO4" not in n["preferred_term"] for n in nodes)
            old_acid = copy.deepcopy(acid)
            old_acid.pop("evidence")
            old_acid["notes"] = before["ingredients"][5]["notes"]
            old_acid["concentration"] = before["ingredients"][5]["concentration"]
            assert old_acid == before["ingredients"][5]
            assert json.dumps(before["ingredients"][4]) in event["changes"]
            counts.update(unsupported_quantity_slots_removed=2, copied_ingredient_nodes_removed=1)
        if key in {"9463", "9466"}:
            assert nodes[6]["preferred_term"] == "Powdered sulfur"
            assert set(nodes[6]) == {"preferred_term", "concentration", "notes", "evidence"}
            assert nodes[6]["concentration"] == {"value": "5", "unit": "G_PER_L"}
            assert "solutions" not in after
            counts["new_quantity_slots"] += 1
        if key == "9466":
            assert nodes[7]["preferred_term"] == "Yeast extract"
            assert set(nodes[7]) == {"preferred_term", "concentration", "notes", "evidence"}
            assert nodes[7]["concentration"] == {"value": "0.2", "unit": "G_PER_L"}
            assert "stock strength" in nodes[7]["notes"] and "autoclaved" in nodes[7]["notes"]
            assert (
                "pH 3.0" in variant["modifications"][-1]
                and "pH 3.5" in variant["modifications"][-1]
            )
            counts["new_quantity_slots"] += 1
        if key == "9467":
            glucose, yeast = after["solutions"]
            for stock in (glucose, yeast):
                assert set(stock) == {"preferred_term", "source", "composition", "notes"}
                assert stock["source"] == ARCHIVE and len(stock["composition"]) == 1
            assert set(glucose["composition"][0]) == {
                "preferred_term",
                "concentration",
                "notes",
                "evidence",
            }
            assert set(yeast["composition"][0]) == {"preferred_term", "notes", "evidence"}
            assert "concentration" not in glucose and "concentration" not in yeast
            assert glucose["composition"][0]["concentration"] == {
                "value": "10",
                "unit": "PERCENT_W_V",
            }
            assert glucose["composition"][0]["preferred_term"] == "Glucose"
            assert "0.2% without a percent basis" in glucose["composition"][0]["notes"]
            assert "concentration" not in yeast["composition"][0]
            assert "1% without a stated percent basis" in yeast["composition"][0]["notes"]
            assert "0.01%" in yeast["composition"][0]["notes"]
            assert "Autoclaved" in yeast["notes"] and "Filter-sterilized" in glucose["notes"]
            assert "2.00 g/L D-glucose" in variant["modifications"][-1]
            counts.update(new_quantity_slots=1, stock_descriptors_added=2)
        if key == "9468":
            assert len(after["solutions"]) == 1
            stock = after["solutions"][0]
            assert set(stock) == {
                "preferred_term",
                "source",
                "composition",
                "concentration",
                "notes",
            }
            assert stock["source"] == ARCHIVE
            assert stock["concentration"] == {
                "value": "50",
                "unit": "ML_PER_L",
                "per_volume": "per liter of prepared MS-medium before iron-stock addition",
            }
            assert Decimal("0.25") / Decimal("5") * 1000 == Decimal(stock["concentration"]["value"])
            assert "autoclaving under N2" in stock["notes"] and "OR" in stock["notes"]
            iron, carrier = stock["composition"]
            assert iron["concentration"] == {"value": "40", "unit": "PERCENT_W_V"}
            clean = copy.deepcopy(iron)
            del clean["notes"], clean["evidence"]
            clean["concentration"] = before["ingredients"][4]["concentration"]
            assert clean == before["ingredients"][4]
            assert carrier["preferred_term"] == "H2SO4" and "concentration" not in carrier
            assert set(carrier) == {"preferred_term", "notes", "evidence"}
            assert set(acid) == {"preferred_term", "notes", "evidence"}
            assert "0.2 N H2SO4" in carrier["notes"]
            counts.update(
                new_quantity_slots=1,
                stock_descriptors_added=1,
                stock_nodes_relocated=1,
                stock_stage_concentrations_rebased=1,
                unquantified_carrier_nodes_added=2,
            )
        if key in {"9466", "9467"}:
            assert after["medium_type"] == "COMPLEX" and after["composition_type"] == "UNDEFINED"
            counts["composition_classifications_corrected"] += 1
        else:
            assert (
                after["medium_type"] == before["medium_type"]
                and after["composition_type"] == before["composition_type"]
            )
        common |= {
            "ingredients",
            "solutions",
            "parent_media",
            "variant_relationship",
            "variant_modifications",
            "variants",
            "preparation_steps",
            "data_quality_flags",
            "medium_type",
            "composition_type",
        }
    # After independently checking the changed surfaces, invert only their approved roots.
    for field in common:
        if field in before:
            restored[field] = before[field]
        else:
            restored.pop(field, None)
    assert restored == before, "Unreviewed whole-record difference"
    return counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path)
    args = parser.parse_args()
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        old_raw, new_raw = item["before_text"].encode(), item["after_text"].encode()
        assert hashlib.sha256(old_raw).hexdigest() == item["before_sha256"]
        assert hashlib.sha256(new_raw).hexdigest() == item["after_sha256"]
        if args.applied:
            assert (ROOT / item["path"]).read_bytes() == new_raw
        counts.update(
            check(
                yaml.load(old_raw, Loader=yaml.CSafeLoader),
                yaml.load(new_raw, Loader=yaml.CSafeLoader),
                item,
                plan["sources"],
            )
        )
    output = {"applied": args.applied, "records": len(plan["records"]), "counts": dict(counts)}
    if args.out:
        assert not args.out.exists()
        args.out.write_text(json.dumps(output, indent=2) + "\n")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
