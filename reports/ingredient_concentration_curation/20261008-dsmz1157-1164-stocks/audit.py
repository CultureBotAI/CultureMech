"""Independent source arithmetic, evidence coverage and full-record inversion."""

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
ACTION = "CORRECTED_DSMZ1157_1164_STOCK_STAGES_AND_INPUTS"
CONTEXT_SHA = "746ca54df3fe06273c9d3a8e5ac2f784066460d0ae39d0fba8de499465cf9692"


def get(doc, pointer):
    for part in pointer:
        doc = doc[part]
    return doc


def provenance(doc):
    counts = collections.Counter()
    if isinstance(doc, dict):
        for k, v in doc.items():
            if k in {"evidence", "references", "curation_history"}:
                counts["new_" + k] += len(v)
            else:
                counts.update(provenance(v))
    elif isinstance(doc, list):
        for v in doc:
            counts.update(provenance(v))
    return counts


def check(before, after, item):
    raw_context = (HERE / "inspected-context.json").read_bytes()
    assert hashlib.sha256(raw_context).hexdigest() == CONTEXT_SHA
    mid, kind = item["key"].split("-")
    group = next(g for g in json.loads(raw_context)["groups"] if g["medium_id"] == mid)
    original = next(r for r in group["records"] if r["kind"] == kind)
    assert item["action"] == ACTION and item["path"] == original["path"]
    assert item["id"] == before["id"] == after["id"] == original["id"]
    assert item["before_text"] == original["before_text"]
    assert before == yaml.load(original["before_text"], Loader=yaml.CSafeLoader)
    assert hashlib.sha256(item["before_text"].encode()).hexdigest() == item["before_sha256"]
    solution = kind == "solution"
    sk = "solution" if solution else "medium"
    raw, meta = group[sk + "_raw"], group[sk + "_metadata"]
    assert hashlib.sha256(raw.encode()).hexdigest() == meta["sha256"] == item["source_sha256"]
    ref = f"https://mediadive.dsmz.de/rest/{sk}/{group['solution_id'] if solution else mid}"
    assert meta["url"] == meta["response_url"] == ref and meta["http_status"] == 200
    source = json.loads(raw)
    data = source["data"] if solution else source["data"]["solutions"][0]
    rows = data["recipe"]
    assert data["id"] == {"1157": 2323, "1164": 2333}[mid] and data["volume"] == 1000
    field = "composition" if solution else "ingredients"
    water_index = next(i for i, r in enumerate(rows) if r["compound_id"] == 4)
    stock_indices = [4, 5, 6, 7] if mid == "1157" else [6]
    basal_indices = [i for i, r in enumerate(rows) if r["unit"] == "g"]
    assert basal_indices == ([0, 1, 2] if mid == "1157" else [0, 1, 2, 3, 4, 5, 7, 8, 9])
    old_indices = (
        list(range(len(rows))) if solution else [i for i in range(len(rows)) if i != water_index]
    )
    assert len(after[field]) == len(basal_indices) + 1
    assert len(after["solutions"]) == len(stock_indices)
    restored = copy.deepcopy(after)
    restored[field] = []
    inversions = {}
    counts = collections.Counter()

    def invert_node(new, old, source_index, scope):
        node = copy.deepcopy(new)
        assert new["preferred_term"] == rows[source_index]["compound"]
        assert len(new["evidence"]) == 1
        evidence = new["evidence"][0]
        assert evidence["reference"] == ref and evidence["supports"] == "SUPPORT"
        assert evidence["snippet"] in raw and json.loads(evidence["snippet"]) == rows[source_index]
        assert scope in evidence["explanation"] and meta["sha256"] in evidence["explanation"]
        assert meta["accessed_at"] in evidence["explanation"]
        if old.get("evidence"):
            assert len(old["evidence"]) == 1
            assert {k: v for k, v in evidence.items() if k != "explanation"} == {
                k: v for k, v in old["evidence"][0].items() if k != "explanation"
            }
            assert evidence["explanation"].endswith(old["evidence"][0]["explanation"])
            assert (
                "Historical explanation (superseded where preparation scope differs): "
                in evidence["explanation"]
            )
            node["evidence"] = copy.deepcopy(old["evidence"])
            counts["evidence_scopes_corrected"] += 1
        else:
            node.pop("evidence")
        node.pop("notes")
        node["concentration"] = copy.deepcopy(old["concentration"])
        assert node == old, "Unreviewed ingredient identity/metadata change"
        return node

    for ni, ri in enumerate(basal_indices):
        old = before[field][old_indices.index(ri)]
        node = after[field][ni]
        assert node["concentration"] == old["concentration"]
        assert node["concentration"]["unit"] == "G_PER_L"
        assert Decimal(node["concentration"]["value"]) == Decimal(str(rows[ri]["g_l"]))
        assert (
            node["notes"]
            == f"Source batch input: {rows[ri]['amount']} g. Retained {rows[ri]['g_l']} g/L is the provider's nominal 1000 ml recipe rate, not a measured basal or final-medium concentration after stock additions."
        )
        inversions[ri] = invert_node(node, old, ri, f"{field}[{ni}].concentration")
        counts["ingredient_context_notes_added"] += 1

    root = after["source_data"] if solution else after
    for si, ri in enumerate(stock_indices):
        row = rows[ri]
        old = before[field][old_indices.index(ri)]
        stock = after["solutions"][si]
        assert stock["source"] == ref and stock["preferred_term"] == row["compound"] + " stock"
        assert len(stock["composition"]) == 1
        node = stock["composition"][0]
        if mid == "1157":
            assert row["unit"] == "ml"
            assert stock["concentration"] == {
                "value": str(Decimal(str(row["amount"])) / 1000),
                "unit": "L",
            }
            assert (
                stock["notes"]
                == f"Source batch dose: {row['amount']} ml stock / 1000 ml per L = {stock['concentration']['value']} L. This is an input volume, not a dose per liter of measured final medium."
            )
            prep = "Filter-sterilized" if si == 0 else "Autoclaved"
            assert (
                stock["preparation_notes"]
                == prep
                + " stock; add after autoclaving and cooling the base. No temperature, duration, pore size or solvent specified."
            )
            assert data["steps"][0]["step"].strip() == "After autoclaving and cooling add:"
            assert set(stock) == {
                "source",
                "preferred_term",
                "composition",
                "concentration",
                "notes",
                "preparation_notes",
            }
            counts["new_quantity_slots"] += 1
        else:
            assert row["amount"] == 7 and row["unit"] == "drops" and row["attribute"] == "0.5 %"
            assert set(stock) == {"source", "preferred_term", "composition", "notes"}
            assert (
                stock["notes"]
                == "Source batch dose: 7 drops of FeCl3 x 6 H2O stock labelled 0.5%. Drop volume and percentage basis are unspecified. Seven drops is not 7 g/L; no numeric volume, stock strength or final-medium concentration is inferred."
            )
        if mid == "1157" and si == 0:
            assert row["attribute"] == "0.2 mg/ml, filter-sterilized"
            assert node["concentration"] == {"value": "0.2", "unit": "MG_PER_ML"}
            assert (
                node["notes"]
                == "Source-explicit riboflavin stock strength: 0.2 mg/ml. The source's 5 ml is a stock addition volume, not 5 g/L or 5% v/v. No final-medium concentration is inferred."
            )
            counts["stock_stage_concentrations_rebased"] += 1
        else:
            assert "concentration" not in node
            percent = ["50%", "20%", "10%"][si - 1] if mid == "1157" else "0.5%"
            assert (
                node["notes"]
                == f"Source stock label: {percent}; percentage basis unspecified. The flattened recipe quantity is withdrawn at this stock stage. No mass/volume percentage basis, density, stock solvent or final-medium concentration is inferred."
            )
            counts["unsupported_quantity_slots_removed"] += 1
        scope = f"solutions[{si}].composition[0]." + (
            "concentration" if "concentration" in node else "notes"
        )
        inversions[ri] = invert_node(node, old, ri, scope)
        counts["stock_nodes_relocated"] += 1
        counts["stock_descriptors_added"] += 1
    water = after[field][-1]
    assert water["preferred_term"] == rows[water_index]["compound"] == "Distilled water"
    assert rows[water_index]["amount"] == 1000 and rows[water_index]["unit"] == "ml"
    assert water["concentration"] == {"value": "1", "unit": "L"}
    assert (
        water["notes"]
        == "Source batch input: 1000 ml distilled water = 1 L. This is not a volume percentage or a measured final-medium volume."
    )
    if solution:
        old = before[field][water_index]
        assert old["concentration"] == {"value": "1000", "unit": "PERCENT_V_V"}
        inversions[water_index] = invert_node(
            water, old, water_index, f"{field}[{len(basal_indices)}].concentration"
        )
        counts["quantity_corrections"] += 1
    else:
        assert set(water) == {"preferred_term", "term", "concentration", "notes", "evidence"}
        assert water["term"] == {"id": "mediadive.compound:4", "label": "Distilled water"}
        evidence = water["evidence"]
        assert (
            len(evidence) == 1
            and evidence[0]["reference"] == ref
            and evidence[0]["supports"] == "SUPPORT"
        )
        assert (
            json.loads(evidence[0]["snippet"]) == rows[water_index]
            and evidence[0]["snippet"] in raw
        )
        counts["water_input_nodes_added"] += 1
        counts["new_quantity_slots"] += 1
    restored[field] = [inversions[i] for i in old_indices]
    restored.pop("solutions")
    scope_note = "Stock stages and water inputs are explicit. Percentage bases, stock solvents and measured final volume are not supplied by these sources; no downstream dilution or growth claim is inferred. Existing chemical mappings and high_metal/other historical flags are retained but not validated by this concentration repair."
    assert after["notes"] == (before.get("notes", "") + "\n\n" + scope_note).lstrip()
    if "notes" in before:
        restored["notes"] = before["notes"]
    else:
        restored.pop("notes")
    counts["recipe_context_notes_corrected"] += 1
    if mid == "1164" and not solution:
        pointer = ["parent_media"] if kind == "komodo" else ["variant_children", 0]
        target_kind = "medium" if kind == "komodo" else "komodo"
        target = next(r for r in group["records"] if r["kind"] == target_kind)
        link = get(after, pointer)
        assert link["path"] == target["path"] and link["id"] == target["id"]
        get(restored, pointer)["path"] = get(before, pointer)["path"]
        counts["parent_links_corrected" if kind == "komodo" else "child_links_corrected"] += 1

    assert len(root["evidence"]) == (3 if kind == "komodo" else 2)
    api_entry, pdf_entry = root["evidence"][:2]
    assert api_entry["reference"] == ref and api_entry["snippet"] in raw
    pdf = group["pdf"]
    quote = (
        "Riboflavin (0.2 mg/ml) filter-sterilized 5.0 ml"
        if mid == "1157"
        else "FeCl3 x 6 H2O (0.5%) 7 drops"
    )
    assert (
        pdf_entry["reference"] == pdf["reference"]
        and pdf_entry["snippet"] == quote
        and quote in pdf["pages"][0]
    )
    assert (
        pdf_entry["supports"] == "SUPPORT"
        and pdf["sha256"] in pdf_entry["explanation"]
        and "page 1" in pdf_entry["explanation"]
    )
    if kind == "komodo":
        assert root["evidence"][2]["reference"] == group["mapping_metadata"]["reference"]
        assert root["evidence"][2]["snippet"] == group["mapping"]["snippet"]
    if solution:
        assert set(root) == {"origin", "evidence"} and root["origin"] == "MediaDive"
        restored.pop("source_data")
    else:
        restored.pop("evidence")
    old_refs = before.get("references", [])
    assert after["references"][: len(old_refs)] == old_refs
    new_refs = after["references"][len(old_refs) :]
    assert len(new_refs) == (3 if kind == "komodo" else 1)
    assert {r["reference"] for r in new_refs} == (
        {ref, pdf["reference"], group["mapping_metadata"]["reference"]}
        if kind == "komodo"
        else {pdf["reference"]}
    )
    for r in new_refs:
        assert "authors" not in r and "year" not in r
        assert "2008 PDF copyright notice is not treated as publication year" in r["notes"]
        if r["reference"] == pdf["reference"]:
            assert r["title"] in pdf["pages"][0]
        elif r["reference"] == group["mapping_metadata"]["reference"]:
            assert r["title"] == "KOMODO - the Known Media Database"
        else:
            assert r["title"] == json.loads(group["medium_raw"])["data"]["medium"]["name"]
    if old_refs:
        restored["references"] = copy.deepcopy(old_refs)
    else:
        restored.pop("references")
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert (
        event["action"] == ACTION
        and event["curator"] == "codex"
        and pdf["reference"] in event["source"]
    )
    restored["curation_history"].pop()
    assert restored == before, "Unreviewed whole-record change"

    seen_old = set()
    seen_new_quantities = set()
    for c in item["claims"]:
        assert get(after, c["pointer"]) == c["new"]
        if c["old_pointer"] is not None:
            assert get(before, c["old_pointer"]) == c["old"]
            if c["old_pointer"][-1] == "concentration":
                seen_old.add(tuple(c["old_pointer"]))
        if c["pointer"][-1] == "concentration":
            seen_new_quantities.add(tuple(c["pointer"]))
        if c["status"] == "unsupported":
            assert solution and c["pointer"] == ["ingredients", 0, "concentration"]
            assert c["new"] == c["old"] and c["reference"] is None
            continue
        assert c["reference"] == ref and c["snippet"] in raw
        assert json.loads(c["snippet"]) == get(source, c["source_pointer"])
        entries = get(after, c["evidence_pointer"])["evidence"]
        entry = next(e for e in entries if e["reference"] == ref)
        assert c["field"] in entry["explanation"] and c["explanation"] in entry["explanation"]
        assert c["snippet"] in entry["explanation"]
        assert c["field"] in event["changes"]
    assert seen_old == {(field, i, "concentration") for i in range(len(before[field]))} | (
        {("ingredients", 0, "concentration")} if solution else set()
    )
    expected_new = {(field, i, "concentration") for i in range(len(after[field]))}
    if solution:
        expected_new.add(("ingredients", 0, "concentration"))
    if mid == "1157":
        expected_new |= {("solutions", i, "concentration") for i in range(4)}
        expected_new.add(("solutions", 0, "composition", 0, "concentration"))
    assert seen_new_quantities == expected_new
    counts.update(provenance(after) - provenance(before))
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
        current = (ROOT / item["path"]).read_bytes()
        assert (
            hashlib.sha256(current).hexdigest()
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
