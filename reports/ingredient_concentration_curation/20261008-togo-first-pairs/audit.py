"""Independently invert allowed edits and check source-scoped evidence."""

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
ROOT = HERE.parents[2]


def get(node, pointer):
    for part in pointer:
        node = node[part]
    return node


def evidence(node):
    result = []
    if isinstance(node, dict):
        entries = node.get("evidence", [])
        assert len({e["reference"] for e in entries}) == len(entries)
        result.extend(entries)
        for key, value in node.items():
            if key != "evidence":
                result.extend(evidence(value))
    elif isinstance(node, list):
        for value in node:
            result.extend(evidence(value))
    return result


def check(before, after, item):
    context_raw = (HERE / "inspected-context.json").read_bytes()
    assert (
        hashlib.sha256(context_raw).hexdigest()
        == "2add08d00b64bfa065f7a2a456e5c24111e8cfb4ffa22b66a1f27213ca170f92"
    )
    context = json.loads(context_raw)
    mid = item["key"]
    source = context["sources"][mid]
    api = source["metadata"]["url"]
    data = json.loads(source["raw"])
    original_claims = len(before["ingredients"]) + len(before.get("solutions", []))
    assert len(item["claims"]) == original_claims + (mid in {"M1001", "M1002"})
    assert len({tuple(c["pointer"]) for c in item["claims"]}) == len(item["claims"])
    for c in item["claims"]:
        row = get(data, c["source_pointer"])
        quoted = json.loads("{" + c["snippet"].rstrip().removesuffix(",") + "}")
        fields = ["component_name", "volume", "unit"]
        if c["status"] == "add":
            fields += ["conc_value", "conc_unit"]
        assert c["snippet"] in source["raw"] and quoted == {k: row[k] for k in fields}
        assert c["reference"] == api
        if c["status"] != "add":
            assert get(before, c["pointer"])["concentration"] == c["old"]
            assert row["component_name"] == c["ingredient"]
        assert get(after, c["pointer"])["concentration"] == c["new"]
    if mid in {"M1023", "M1024"}:
        assert before == after
        assert all(c["status"] == "unsupported" for c in item["claims"])
        return collections.Counter()

    jcm = context["sources"]["JCM954"]
    original = jcm["metadata"]["url"]
    soup = BeautifulSoup(jcm["raw"], "html.parser")
    # Inline chemical subscripts concatenate; table cells need explicit boundaries.
    rows = [
        " ".join(" ".join(td.get_text().split()) for td in tr.find_all("td"))
        for tr in soup.find_all("tr")
    ]
    text = " ".join(soup.get_text().split())
    entries = evidence(after)
    assert not evidence(before)
    for e in entries:
        assert e["supports"] == "SUPPORT" and e["explanation"] and e["snippet"]
        assert e["reference"] in {api, original}
        assert e["snippet"] in (source["raw"] if e["reference"] == api else text) or (
            e["reference"] == original and e["snippet"] in rows
        )
    recovered = copy.deepcopy(after)
    counts = collections.Counter(
        new_evidence=len(entries), new_references=2, new_curation_history=1
    )
    for c in item["claims"]:
        node = get(after, c["pointer"])
        row = get(data, c["source_pointer"])
        ev = get(after, c["evidence_pointer"])["evidence"]
        assert {e["reference"] for e in ev} == {api, original}
        assert all(c["field"] in e["explanation"] for e in ev)
        assert any(c["snippet"] == e["snippet"] or c["snippet"] in e["explanation"] for e in ev)
        assert any(
            c["primary_quote"] == e["snippet"] or c["primary_quote"] in e["explanation"] for e in ev
        )
        if c["status"] == "add":
            assert c["pointer"] == ["solutions", 1, "composition", 0]
            assert before["solutions"][1]["composition"] == []
            assert row["component_name"] == "1 M NH4Cl solution*"
            assert row["conc_value"] == 1 and row["conc_unit"] == "M"
            assert node["preferred_term"] == "NH4Cl"
            assert node["concentration"] == {"value": "1", "unit": "MOLAR"}
            assert set(node) == {"preferred_term", "concentration", "notes", "evidence"}
            assert "not its final-medium concentration" in node["notes"]
            recovered["solutions"][1]["composition"] = []
            counts["new_quantity_slots"] += 1
            continue
        old = get(before, c["pointer"])
        target = get(recovered, c["pointer"])
        assert node["notes"] == old["notes"] + "\n\n" + c["explanation"]
        if c["status"] == "correct":
            assert row["unit"] == "ml" and c["old"]["unit"] == "G_PER_L"
            assert node["concentration"]["unit"] == "L"
            assert Decimal(node["concentration"]["value"]) * 1000 == Decimal(str(row["volume"]))
            assert "not g/L, ml/L, or a final-medium volume" in node["notes"]
            target["concentration"] = copy.deepcopy(old["concentration"])
            counts["quantity_corrections"] += 1
        elif c["status"] == "evidence_only":
            assert mid == "M1002" and row["component_name"] == "agar" and row["unit"] == "g/L"
            assert node["concentration"] == {"value": "20", "unit": "G_PER_L"}
        else:
            assert c["status"] == "unsupported" and row["unit"] == "g"
            assert node["concentration"] == old["concentration"]
            assert "note only, not the retained final-medium concentration" in node["notes"]
            counts["batch_mass_notes_unverified_concentrations"] += 1
        target["notes"] = old["notes"]
        if c["pointer"][0] == "ingredients":
            del target["evidence"]
    assert counts["quantity_corrections"] == 4
    assert counts["new_quantity_slots"] == 1
    assert counts["batch_mass_notes_unverified_concentrations"] == 6
    assert counts["new_evidence"] == (20 if mid == "M1002" else 18)
    refs = recovered.pop("references")
    assert len(refs) == 2
    assert [(r["reference"], r["title"]) for r in refs] == [
        (api, data["meta"]["name"]),
        (original, "Medium data"),
    ]
    assert all(set(r) == {"reference", "title", "notes"} for r in refs)
    assert all(
        "accessed_on=2026-10-08" in r["notes"]
        and "discovery_mode=" in r["notes"]
        and "source_type=" in r["notes"]
        for r in refs
    )
    assert recovered["curation_history"][:-1] == before["curation_history"]
    event = recovered["curation_history"].pop()
    assert event["curator"] == "codex" and event["action"] == item["action"]
    assert all(c["field"] in event["changes"] for c in item["claims"])
    del recovered["evidence"]
    assert recovered == before, "Unreviewed semantic edit"
    return counts


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--applied", action="store_true")
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args()
    assert not args.out.exists()
    plan = json.loads((HERE / "plan.json").read_text())
    counts = collections.Counter()
    for item in plan["records"]:
        before, after = [
            yaml.load(item[k + "_text"], Loader=yaml.CSafeLoader) for k in ("before", "after")
        ]
        raw = (ROOT / item["path"]).read_bytes()
        expected = item["after_sha256"] if args.applied else item["before_sha256"]
        assert hashlib.sha256(raw).hexdigest() == expected
        counts.update(check(before, after, item))
    result = {
        "terminal": True,
        "applied": args.applied,
        "records_reviewed": 4,
        "records_changed": 2,
        "counts": dict(counts),
    }
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
