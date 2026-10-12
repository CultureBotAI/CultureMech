"""Reconcile all proposed concentration nodes against captured UTEX source rows."""

import json
from collections import Counter
from copy import deepcopy
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner
import review_utex_seven_stocks as guard
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
PLAN_SHA = "9a74e5496124432d48df9f83e4d62b2a6646bae12a6082ebfa534740bcea2f94"


def documents():
    raw = (HERE / "plan.json").read_bytes()
    assert runner.sha(raw) == PLAN_SHA
    plan = json.loads(raw)
    sources = {}
    captures = []
    for source in plan["sources"]:
        if "capture" in source:
            raw = Path(source["capture"]).read_bytes()
            assert runner.sha(raw) == source["sha256"]
            soup = BeautifulSoup(raw, "html.parser")
            text = " ".join(soup.get_text().split())
            tables = [
                [
                    [" ".join(c.get_text().split()) for c in row.find_all(["th", "td"])]
                    for row in table.find_all("tr")
                ]
                for table in soup.find_all("table")
            ]
            sources[source["reference"]] = {"text": text, "tables": tables, "source": source}
            captures.append(source["reference"])
        else:
            assert source["access_method"] == "primary source inspected with web tool"
            sources[source["reference"]] = {
                "text": source["snippet"],
                "source": source,
                "manual_ledger_only": True,
            }
    return plan, sources, captures


def concentration_nodes(doc):
    result = {}

    def walk(node, path):
        if isinstance(node, dict):
            if "concentration" in node:
                result[path + ".concentration"] = node
            for key in ("composition", "solutions"):
                for index, child in enumerate(node.get(key, [])):
                    walk(child, f"{path + '.' if path else ''}{key}[{index}]")

    walk(doc, "")
    return result


def check(doc, item, sources):
    baseline = runner.load_yaml(item["before_text"])
    expected = runner.load_yaml(item["after_text"])
    stem = Path(item["path"]).stem
    source = sources[item["reference"]]
    text, tables = source["text"], source["tables"]
    nodes = concentration_nodes(doc)
    assert set(nodes) == {c.get("proposed_field", c["field"]) for c in item["claims"]}
    assert len(nodes) == len(item["claims"])
    if stem == "DAS_Macro_Solution":
        assert doc["composition"] == [] and len(doc["solutions"]) == 2
        assert "For 40 mL total" in text
        assert tables[0][0][1:5] == [
            "Component",
            "Amount",
            "Stock Solution Concentration",
            "Final Concentration in DAS",
        ]
        for i, stock in enumerate(doc["solutions"]):
            row = tables[0][i + 1]
            dose = Decimal(row[2].split()[0]) / Decimal("40") * 100
            assert Decimal(stock["concentration"]["value"]) == dose
            assert stock["concentration"]["unit"] == "PERCENT_V_V"
            component = stock["composition"][0]
            assert component["concentration"] == {"value": row[3].split()[0], "unit": "MOLAR"}
            assert f"solutions[{i}].concentration" in doc["evidence"][0]["explanation"]
            assert row[2] in doc["evidence"][0]["explanation"]
            assert "term" not in stock
        assert doc["solutions"][0]["composition"][0]["term"]["id"] == "CHEBI:63005"
        phosphate = doc["solutions"][1]["composition"][0]
        assert phosphate["chemical_formula"] == "Na2HPO4.7H2O" and "term" not in phosphate
        assert "unresolved" in phosphate["notes"]
    else:
        assert len(doc["composition"]) == len(baseline["composition"])
        for i, node in enumerate(doc["composition"]):
            if stem == "EDTA_Stock":
                amount = ("50", "31")[i]
                assert ("50 grams of EDTA, acid form" if i == 0 else "31 grams of KOH") in text
                assert "Bring the total volume to 1 Liter" in text
            else:
                assert tables[0][0][1:3] == ["Component", "Amount"]
                amount = tables[0][i + 1][2].split()[0]
            denominator = Decimal("0.1") if stem == "DAS_Vitamin_Cocktail" else Decimal("1")
            assert Decimal(node["concentration"]["value"]) == Decimal(amount) / denominator
            assert node["concentration"]["unit"] == "G_PER_L"
            assert node["concentration"] == baseline["composition"][i]["concentration"]
            assert node["evidence"][0]["snippet"] == item["claims"][i]["snippet"]
            if tables:
                assert node["evidence"][0]["snippet"] == tables[0][i + 1][2]
            if i in guard.IDENTITIES.get(stem, {}):
                assert node["term"]["id"] == guard.IDENTITIES[stem][i]
                assert node["mediaingredientmech_chebi_term"] == node["term"]
            else:
                assert node["term"] == baseline["composition"][i]["term"]
    checked = Counter()
    for field, node in nodes.items():
        location = (
            doc["evidence"]
            if field.count(".") == 1 and field.startswith("solutions[")
            else node["evidence"]
        )
        matched = [e for e in location if e["reference"] == item["reference"]]
        assert len(matched) == 1 and field in matched[0]["explanation"]
        assert matched[0]["supports"] == "SUPPORT"
        checked["concentration_claims"] += 1
    for node in [doc, *nodes.values()]:
        entries = node.get("evidence", [])
        assert len({e["reference"] for e in entries}) == len(entries)
        for entry in entries:
            origin = sources[entry["reference"]]
            assert entry["snippet"] in origin["text"]
            assert entry["supports"] == "SUPPORT"
            checked[
                (
                    "manual_identity_ledger_entries"
                    if origin.get("manual_ledger_only")
                    else "captured_snippet_entries"
                )
            ] += 1
    assert doc["notes"] == expected["notes"]
    assert doc["curation_history"][:-1] == baseline["curation_history"]
    assert doc["references"] == expected["references"]
    assert doc["source_data"] == baseline["source_data"]
    assert doc["id"] == baseline["id"] and doc["category"] == baseline["category"]
    return checked


def main():
    plan, sources, captures = documents()
    checked = Counter()
    mutations = []
    for item in plan["records"]:
        doc = runner.load_yaml(item["after_text"])
        checked.update(check(doc, item, sources))
        for field in concentration_nodes(doc):
            changed = deepcopy(doc)
            concentration_nodes(changed)[field]["concentration"]["value"] = "999"
            try:
                check(changed, item, sources)
            except AssertionError:
                mutations.append({"path": item["path"], "field": field, "fault": "amount"})
            else:
                raise AssertionError("Accepted incorrect quantity")
        for fault in (
            "unit",
            "snippet",
            "support",
            "identity",
            "notes",
            "history",
            "reference",
            "year",
        ):
            changed = deepcopy(doc)
            ingredient = (
                changed["composition"][0]
                if changed["composition"]
                else changed["solutions"][0]["composition"][0]
            )
            if fault == "unit":
                ingredient["concentration"]["unit"] = "ML_PER_L"
            elif fault == "snippet":
                ingredient["evidence"][0]["snippet"] = "invented"
            elif fault == "support":
                ingredient["evidence"][0]["supports"] = "PARTIAL"
            elif fault == "identity":
                ingredient["term"] = {"id": "CHEBI:1", "label": "wrong"}
            elif fault == "notes":
                changed["notes"] += "Autoclave at an invented temperature."
            elif fault == "history":
                changed["curation_history"][0]["notes"] = "rewritten"
            elif fault == "reference":
                ingredient["evidence"][0]["reference"] = "https://example.invalid"
            else:
                changed["references"][0]["year"] = 2026
            try:
                check(changed, item, sources)
            except (AssertionError, KeyError):
                mutations.append({"path": item["path"], "fault": fault})
            else:
                raise AssertionError("Accepted incorrect " + fault)
    assert checked["concentration_claims"] == 36 and len(mutations) == 92
    result = {
        "terminal": True,
        "passed": True,
        "plan_sha256": PLAN_SHA,
        "counts": dict(checked),
        "source_captures_reparsed": len(captures),
        "rejected_mutations": mutations,
        "records_edited": 0,
        "manual_ledger_scope_note": "Supplier and uncaptured ChEBI identities retain manual-source provenance; this audit is not a fresh live-source validation.",
        "all_record_goal_complete": False,
    }
    with (HERE / "semantic-audit.json").open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({k: v for k, v in result.items() if k != "rejected_mutations"}, indent=2))


if __name__ == "__main__":
    main()
