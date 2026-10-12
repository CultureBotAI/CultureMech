"""Stock-only DSMZ 13 source scoping and maintained-pipeline regressions."""

import collections
import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz13-stock-only"
sys.path.insert(0, str(ROOT / "scripts"))
import repair_reviewed_medium_stock_boundaries as repair  # noqa: E402

from culturemech.merge.fingerprint import RecipeFingerprinter  # noqa: E402
from culturemech.merge.matcher import RecipeMatcher  # noqa: E402
from culturemech.merge.merger import RecipeMerger  # noqa: E402


@pytest.fixture
def source_case():
    plan = json.loads((REPORT / "plan.json").read_text())
    item = plan["records"][0]
    doc = repair.load_yaml(item["before_text"])
    sources = [
        {"id": sid, "name": name, "volume": volume, "recipe": [], "steps": []}
        for sid, name, volume in [
            (16, "Main sol. 13", 1000),
            (17, "Solution A", 500),
            (18, "Solution B", 500),
        ]
    ]
    for claim in item["claims"]:
        pointer = claim["source_pointer"]
        if pointer[3] == "recipe":
            sources[pointer[2]]["recipe"].append((pointer[4], json.loads(claim["snippet"])))
        elif pointer[3] == "steps":
            sources[pointer[2]]["steps"] = json.loads(claim["snippet"])
    for source in sources:
        source["recipe"] = [row for _, row in sorted(source["recipe"])]
    sources[0]["steps"] = [{"step": doc["preparation_steps"][0]["description"]}]
    data = {
        "data": {
            "medium": {
                "id": 13,
                "name": doc["original_name"],
                "source": "DSMZ",
                "link": repair.PDF.format("13"),
            },
            "solutions": sources,
        }
    }
    return doc, data, item, plan


def proposal(source_case):
    doc, source, _, plan = source_case
    raw = json.dumps(source)
    meta = {"sha256": repair.sha(raw.encode()), "accessed_at": plan["created_at"]}
    return repair.build(
        doc,
        raw,
        meta,
        "13",
        plan["created_at"],
        chains={"13": ["13"]},
        pdf_hashes={"13": repair.DSMZ13_PDF_SHA},
    )


def test_all_ingredients_belong_to_stocks_and_preparation_is_scoped(source_case):
    before = source_case[0]
    after, claims = proposal(source_case)
    assert after["ingredients"] == []
    a, b = after["solutions"]
    assert a["term"]["id"] == "mediadive.solution:17"
    assert b["term"]["id"] == "mediadive.solution:18"
    assert a["concentration"] == b["concentration"] == {"value": "0.5", "unit": "L"}
    assert [n["concentration"] for n in a["composition"][:-1] + b["composition"][:-1]] == [
        n["concentration"] for n in before["ingredients"]
    ]
    assert (
        a["composition"][-1]["concentration"]
        == b["composition"][-1]["concentration"]
        == {"value": "0.5", "unit": "L"}
    )
    assert a["preparation_notes"] == before["preparation_steps"][1]["description"]
    assert "preparation_notes" not in b
    assert after["preparation_steps"] == before["preparation_steps"][:1]
    assert collections.Counter(c["status"] for c in claims) == {
        "relocate": 7,
        "add": 4,
        "correct_stage": 1,
    }
    assert len(after["evidence"]) == 1
    assert len(after["references"]) == 2


def test_stock_only_record_survives_actual_matcher_and_single_group_merger(source_case, tmp_path):
    doc, _ = proposal(source_case)
    path = tmp_path / "dsmz13.yaml"
    path.write_text(yaml.safe_dump(doc))
    fp = RecipeFingerprinter().fingerprint(doc)
    groups = RecipeMatcher().group_recipes([path])
    assert groups == {fp: [path]}
    merged = RecipeMerger().merge_group(groups[fp])
    assert merged["merge_fingerprint"] == fp
    for field in ("ingredients", "solutions", "evidence", "references", "preparation_steps"):
        assert merged[field] == doc[field]


@pytest.mark.parametrize(
    "change",
    [
        lambda d, s: s["data"]["solutions"][1].update(volume=1000),
        lambda d, s: s["data"]["solutions"][0]["recipe"][0].update(unit="ml/l"),
        lambda d, s: d["ingredients"][0]["concentration"].update(value="1"),
        lambda d, s: s["data"]["solutions"][2]["recipe"][1].update(condition="if required"),
        lambda d, s: d["preparation_steps"][1].update(description="Adjust the mixed medium pH."),
    ],
)
def test_source_boundary_ambiguity_is_not_accepted(source_case, change):
    change(source_case[0], source_case[1])
    with pytest.raises(ValueError):
        proposal(source_case)


def test_cohort_cannot_be_selected_implicitly(source_case, tmp_path):
    doc, source, _, plan = source_case
    with pytest.raises(ValueError, match="Unreviewed source"):
        repair.build(doc, json.dumps(source), {}, "13", plan["created_at"])
    with pytest.raises(ValueError, match="Unreviewed cohort"):
        repair.process(tmp_path, tmp_path, tmp_path / "plan.json", "apply", cohort="arbitrary")


def test_applied_hash_and_independent_inversion(source_case):
    before, _, item, _ = source_case
    raw = (ROOT / item["path"]).read_bytes()
    assert repair.sha(raw) == item["after_sha256"]
    assert repair.sha(item["before_text"].encode()) == item["before_sha256"]
    after = repair.load_yaml(raw)
    path = REPORT.parent / "20261007-dsmz1399-stock-boundary/audit_diff.py"
    spec = importlib.util.spec_from_file_location("independent_dsmz13_audit", path)
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    audit.invert_stock_batch(before, after, item)
    assert dict(audit.counts) == {
        "stock_nodes_relocated": 7,
        "new_quantity_slots": 4,
        "preparation_steps_relocated": 1,
        "new_evidence": 10,
        "new_references": 2,
        "new_curation_history": 1,
    }


def test_corpus_fingerprint_impact_is_exactly_stock_only_or_nested():
    impact = json.loads((REPORT / "fingerprint-impact-before-curation.json").read_text())
    assert impact["records"] == 15910
    assert len(impact["changed"]) == 38
    assert sum(c["old_fingerprint"] is None for c in impact["changed"]) == 32
    successor_folder = REPORT.parent / "20261007-public-stocks"
    successors = {
        item["path"]: item
        for item in json.loads((successor_folder / "plan.json").read_text())["records"]
    }
    spec = importlib.util.spec_from_file_location(
        "independent_public_stock_audit", successor_folder / "audit.py"
    )
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    fingerprinter = RecipeFingerprinter()
    rs_folder = REPORT.parent / "20261007-rs-stock-boundaries"
    rs_successors = {
        item["path"]: item for item in json.loads((rs_folder / "plan.json").read_text())["records"]
    }
    spec = importlib.util.spec_from_file_location(
        "independent_rs_stock_audit", rs_folder / "audit.py"
    )
    rs_audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(rs_audit)
    for row in impact["changed"]:
        raw = (ROOT / row["path"]).read_bytes()
        # Preserve the historical impact snapshot; accept only an independently
        # inverted, hash-linked successor, not arbitrary later source edits.
        if row["path"] in successors:
            item = successors[row["path"]]
            assert item["id"] == row["id"]
            assert repair.sha(raw) == item["after_sha256"]
            assert item["before_sha256"] == row["sha256"]
            before = repair.load_yaml(item["before_text"])
            after = repair.load_yaml(raw)
            audit.check(before, after, item)
            assert fingerprinter.fingerprint(after) == row["new_fingerprint"]
            raw = item["before_text"].encode()
        elif row["path"] in rs_successors:
            item = rs_successors[row["path"]]
            assert item["id"] == row["id"]
            assert repair.sha(raw) == item["after_sha256"]
            assert item["before_sha256"] == row["sha256"]
            before, after = repair.load_yaml(item["before_text"]), repair.load_yaml(raw)
            rs_audit.check(before, after, item)
            delta = rs_audit.fingerprint_delta(before, after)
            assert delta["before"] == row["new_fingerprint"]
            assert delta["added_identifiers"] == ["purified water"]
            assert not delta["removed_identifiers"]
            raw = item["before_text"].encode()
        assert repair.sha(raw) == row["sha256"]
        doc = repair.load_yaml(raw)
        assert doc["id"] == row["id"]
        assert fingerprinter.fingerprint(doc) == row["new_fingerprint"]
        if row["old_fingerprint"] is None:
            assert doc["ingredients"] == [] and doc["solutions"]
        else:
            assert any(s.get("solutions") for s in doc["solutions"])
