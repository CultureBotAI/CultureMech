"""Independently check stock boundaries, literal evidence and invert only reviewed edits."""

import argparse
import copy
import hashlib
import json
from pathlib import Path

import yaml
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent


def check(before, after, item):
    context = json.loads((HERE / "inspected-context.json").read_text())
    assert before == yaml.safe_load(context["record"]["before_text"])
    assert after["id"] == before["id"] == "CultureMech:012919"
    assert len(after["solutions"]) == 1 and len(after["composition"]) == 2
    stock = after["solutions"][0]
    assert set(stock) == {"preferred_term", "composition", "concentration", "source", "notes"}
    assert stock["preferred_term"] == "HCl stock (7.7 M)"
    assert stock["concentration"] == {"value": "0.01", "unit": "L"}
    assert len(stock["composition"]) == 1
    acid = stock["composition"][0]
    assert acid["concentration"] == {"value": "7.7", "unit": "MOLAR"}
    assert acid["preferred_term"] == "HCl"
    assert "not of the prepared FeCl2 solution" in acid["notes"]
    assert "25%, without stating the percentage basis" in acid["notes"]
    assert "per FeCl2 preparation batch" in stock["notes"]
    assert "density" in acid["notes"] and "measured final volume" in acid["notes"]
    sources = context["sources"]
    api_url = sources["S3846"]["metadata"]["url"]
    original_url = sources["JCM187"]["metadata"]["url"]
    assert stock["source"] == api_url
    assert after["source_data"]["origin"] == "MediaDive"
    assert set(after["source_data"]) == {"origin", "notes", "evidence"}
    assert "import_date" not in after["source_data"]
    dose = after["source_data"]["evidence"]
    assert len(dose) == 1 and dose[0]["reference"] == api_url
    assert len(acid["evidence"]) == 2
    assert {e["reference"] for e in acid["evidence"]} == {api_url, original_url}
    by_url = {s["metadata"]["url"]: s for s in sources.values()}
    for entries, field in [
        (acid["evidence"], "solutions[0].composition[0].concentration"),
        (dose, "solutions[0].concentration"),
    ]:
        for e in entries:
            source = by_url[e["reference"]]
            raw, meta = source["raw"], source["metadata"]
            assert hashlib.sha256(raw.encode(meta["encoding"])).hexdigest() == meta["sha256"]
            text = (
                " ".join(BeautifulSoup(raw, "html.parser").get_text().split())
                if e["reference"] == original_url
                else raw
            )
            assert e["supports"] == "SUPPORT" and e["snippet"] in text
            assert field in e["explanation"]
            assert meta["accessed_at"] in e["explanation"] and meta["sha256"] in e["explanation"]
    acid_row = json.loads(dose[0]["snippet"])
    assert (
        acid_row["compound_id"],
        acid_row["attribute"],
        acid_row["amount"],
        acid_row["unit"],
    ) == (68, "7.7 M, 25%", 10, "ml")
    assert [n["concentration"] for n in after["composition"]] == [
        {"value": "1.5", "unit": "G_PER_L"},
        {"value": "0.99", "unit": "L"},
    ]
    restored = copy.deepcopy(after)
    for i, node in enumerate(restored["composition"]):
        old = before["composition"][i + 1]
        assert len(node["evidence"]) == len(old["evidence"]) == 1
        previous, current = old["evidence"][0], node["evidence"][0]
        assert current["explanation"].startswith(previous["explanation"] + " ")
        assert (
            f"Current locator after HCl stock separation: composition[{i}].concentration"
            in current["explanation"]
        )
        current["explanation"] = previous["explanation"]
        assert node == old
    moved = restored.pop("solutions")[0]["composition"][0]
    moved.pop("evidence")
    moved.pop("notes")
    moved["concentration"] = before["composition"][0]["concentration"]
    assert moved == before["composition"][0]
    restored["composition"].insert(0, moved)
    restored.pop("source_data")
    assert after["references"][:-1] == before["references"]
    ref = restored["references"].pop()
    assert ref["reference"] == original_url and ref["title"] == "Medium data"
    assert "authors" not in ref and "year" not in ref
    assert "source_type=culture_collection_page" in ref["notes"]
    assert "discovery_mode=cross_reference" in ref["notes"]
    event = restored["curation_history"].pop()
    assert event["action"] == item["action"]
    assert event["curator"] == "codex" and event["source"] == original_url
    assert restored == before, "Unreviewed semantic change"
    assert {c["field"] for c in item["claims"]} == {
        "solutions[0].composition[0].concentration",
        "solutions[0].concentration",
        "composition[0].concentration",
        "composition[1].concentration",
        "ingredients[0].concentration",
    }
    return {
        "stock_stage_concentrations_rebased": 1,
        "new_quantity_slots": 1,
        "stock_nodes_relocated": 1,
        "stock_descriptors_added": 1,
        "new_evidence": 3,
        "new_references": 1,
        "new_curation_history": 1,
        "evidence_scopes_corrected": 2,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    plan = json.loads((HERE / "plan.json").read_text())
    item = plan["records"][0]
    before, after = [yaml.safe_load(item[k + "_text"]) for k in ("before", "after")]
    for key in ("before", "after"):
        assert hashlib.sha256(item[key + "_text"].encode()).hexdigest() == item[key + "_sha256"]
    if args.applied:
        assert Path(item["path"]).read_bytes() == item["after_text"].encode()
    counts = check(before, after, item)
    args.out.write_text(
        json.dumps(
            {"terminal": True, "applied": args.applied, "records": 1, "counts": counts}, indent=2
        )
        + "\n"
    )
    print(json.dumps(counts))


if __name__ == "__main__":
    main()
