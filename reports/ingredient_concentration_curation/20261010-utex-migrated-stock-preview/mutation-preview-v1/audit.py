"""Independently inspect the proposed stock claims and reject out-of-scope changes."""

import json
from collections import Counter
from copy import deepcopy
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner
from bs4 import BeautifulSoup

HERE = Path(__file__).resolve().parent
PLAN_SHA = "0cf3a08ff882d4bb2fd8d46b4cd3f376d1ad17939ccb9640ad402b1edd086b5b"
EXPECTED_ROWS = {
    "Beijerinck_Solution": [
        ("NH4Cl(CAS: 12125-02-9)", "8 g/L", "8", "G_PER_L"),
        ("CaCl2\u20222H2O(CAS: 10035-04-8)", "1 g/L", "1", "G_PER_L"),
        ("MgSO4\u20227H2O(CAS: 10034-99-8)", "2 g/L", "2", "G_PER_L"),
    ],
    "Bold_Trace_Stock": [
        ("H2SO4 conc.", "10-mL", "10", "ML_PER_L"),
        ("ZnSO4\u20227H2O", "8.82 g", "8.82", "G_PER_L"),
        ("MnCl\u20224H2O", "1.44 g", "1.44", "G_PER_L"),
        ("MoO3", "0.71 g", "0.71", "G_PER_L"),
        ("CuSO4\u20225H2O", "1.57 g", "1.57", "G_PER_L"),
        ("Co(NO3)2\u20226H2O", "0.49 g", "0.49", "G_PER_L"),
    ],
    "Boron_Stock": [("H3BO3", "11 g", "11", "G_PER_L")],
}


def pinned():
    raw = (HERE / "plan.json").read_bytes()
    assert runner.sha(raw) == PLAN_SHA
    return json.loads(raw)


def check(before, after, item):
    plan = pinned()
    original = next(record for record in plan["records"] if record["path"] == item["path"])
    assert json.dumps(item, sort_keys=True) == json.dumps(original, sort_keys=True)
    assert before == runner.load_yaml(original["before_text"])
    assert after == runner.load_yaml(original["after_text"]), "Unreviewed proposal"
    capture = next(source for source in plan["sources"] if source["reference"] == item["reference"])
    raw = Path(capture["capture"]).read_bytes()
    assert runner.sha(raw) == capture["sha256"] == item["source_capture_sha256"]
    soup = BeautifulSoup(raw, "html.parser")
    text = " ".join(soup.get_text().split())
    tables = soup.find_all("table")
    rows = (
        []
        if not tables
        else [
            [" ".join(cell.get_text().split()) for cell in row.find_all(["td", "th"])]
            for row in tables[0].find_all("tr")
        ]
    )
    stem = Path(item["path"]).stem
    expected = EXPECTED_ROWS[stem]
    assert (
        len(before["composition"])
        == len(after["composition"])
        == len(item["claims"])
        == len(expected)
    )
    restored = deepcopy(after)
    counts = Counter()
    for index, ((component, quote, value, unit), claim) in enumerate(
        zip(expected, item["claims"], strict=True)
    ):
        node = restored["composition"][index]
        if rows:
            assert rows[0][1:3] == ["Component", "Amount"]
            assert rows[index + 1][1:3] == [component, quote]
        else:
            assert "dissolve 11 g of H3BO3" in text
        assert Decimal(node["concentration"]["value"]) == Decimal(value)
        assert node["concentration"]["unit"] == unit
        evidence = node.pop("evidence")
        assert len(evidence) == 1 and evidence[0]["reference"] == item["reference"]
        assert evidence[0]["snippet"] == quote == claim["snippet"]
        assert (
            claim["basis_snippet"] in text and claim["basis_snippet"] in evidence[0]["explanation"]
        )
        assert claim["field"] in evidence[0]["explanation"]
        held = stem == "Bold_Trace_Stock" and index == 2
        assert claim["status"] == ("conflict" if held else "evidence_only")
        assert evidence[0]["supports"] == ("PARTIAL" if held else "SUPPORT")
        if held:
            assert "not independently verified" in evidence[0]["explanation"]
            assert node["term"]["id"] == "CHEBI:86368"
        assert node == before["composition"][index]
        counts["new_evidence"] += 1
    root_evidence = restored.pop("evidence")
    assert len(root_evidence) == 1 and root_evidence[0]["reference"] == item["reference"]
    assert root_evidence[0]["snippet"] in text
    assert "notes" in root_evidence[0]["explanation"]
    counts["new_evidence"] += 1
    if stem == "Beijerinck_Solution":
        assert "Final Concentration in TAP Medium" in text
        assert "approximately 800 mL" in text and "approximately 800 mL" in after["notes"]
        assert after["notes"].startswith(
            before["notes"]
            .split("Final stock concentration")[0]
            .replace("approximately 900 mL", "approximately 800 mL")
        )
    else:
        assert "Source discrepancy:" in after["notes"]
        assert after["notes"].startswith(before["notes"].split("Final stock concentration")[0])
    restored["notes"] = before["notes"]
    counts["recipe_context_notes_corrected"] += 1
    assert len(restored["references"]) == len(before["references"])
    for old, new in zip(before["references"], restored["references"], strict=True):
        if old["reference"] == item["reference"]:
            assert set(new) == {"reference", "title", "notes"}
            assert new["title"] == soup.find("h1").get_text(" ", strip=True)
            assert "source_type=culture_collection_page" in new["notes"]
            assert "discovery_mode=existing_record_reference" in new["notes"]
            assert "No named author, publication year or DOI established" in new["notes"]
            new.pop("title")
            new.pop("notes")
            counts["bibliographic_entries_enriched"] += 1
        assert old == new
    event = restored["curation_history"].pop()
    assert event["action"] == item["action"] and event["curator"] == "codex"
    assert event["source"] == item["reference"]
    assert json.loads(event["changes"])["claims"] == item["claims"]
    counts["new_curation_history"] += 1
    assert restored == before
    assert dict(counts) == item["counts"]
    return counts


def main():
    plan = pinned()
    counts = Counter()
    rejected = []
    for item in plan["records"]:
        before, after = (runner.load_yaml(item[key]) for key in ("before_text", "after_text"))
        counts.update(check(before, after, item))
        for fault in (
            "amount",
            "unit",
            "snippet",
            "support",
            "identity",
            "notes",
            "history",
            "reference",
            "year",
        ):
            changed = deepcopy(after)
            node = changed["composition"][0]
            if fault == "amount":
                node["concentration"]["value"] = "999"
            elif fault == "unit":
                node["concentration"]["unit"] = "MOLAR"
            elif fault == "snippet":
                node["evidence"][0]["snippet"] = "invented"
            elif fault == "support":
                node["evidence"][0]["supports"] = "PARTIAL"
            elif fault == "identity":
                node["term"]["id"] = "CHEBI:1"
            elif fault == "notes":
                changed["notes"] += "Universal final dose is 10 mL/L."
            elif fault == "history":
                changed["curation_history"][0]["notes"] = "rewritten"
            elif fault == "reference":
                node["evidence"][0]["reference"] = "https://example.invalid"
            else:
                changed["references"][0]["year"] = 2026
            try:
                check(before, changed, item)
            except AssertionError:
                rejected.append({"path": item["path"], "fault": fault})
            else:
                raise AssertionError("Accepted forged " + fault)
    assert len(rejected) == 27
    assert dict(counts) == plan["counts"]
    result = {
        "terminal": True,
        "passed": True,
        "plan_sha256": PLAN_SHA,
        "source_captures_reparsed": 3,
        "concentration_claims_checked": 10,
        "counts_proposed_only": dict(counts),
        "rejected_faults": rejected,
        "records_edited": 0,
        "all_record_goal_complete": False,
    }
    with (HERE / "semantic-audit.json").open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({key: value for key, value in result.items() if key != "rejected_faults"}))


if __name__ == "__main__":
    main()
