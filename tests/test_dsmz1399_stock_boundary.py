"""Guard stock membership, source dose units, provenance, and two-record writes."""

import json
import re
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_dsmz1399_stock_boundary as repair  # noqa: E402
import review_solution_concentration_evidence as reviewer  # noqa: E402

PLAN = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz1399-stock-boundary/plan.json"


@pytest.fixture
def baseline():
    plan = json.loads(PLAN.read_text())
    return {
        r["path"]: yaml.load(r["before_text"], Loader=yaml.CSafeLoader) for r in plan["records"]
    }


@pytest.fixture
def sources(baseline):
    # Offline fixture reconstructed from the reviewed literal excerpts, not a live source check.
    plan = json.loads(PLAN.read_text())
    main = {
        "id": 2837,
        "name": "Main sol. 1399",
        "volume": 1000,
        "recipe": [None] * 6,
        "steps": [{"step": baseline[repair.MEDIUM_PATH]["preparation_steps"][0]["description"]}],
    }
    stock = {"id": 2838, "name": "Total Salts", "volume": 1000, "recipe": [None] * 9}
    for c in plan["records"][0]["claims"]:
        match = re.fullmatch(r"\$\.data\.solutions\[(\d+)\]\.recipe\[(\d+)\]", c["locator"])
        assert match
        group, index = map(int, match.groups())
        (main if group == 0 else stock)["recipe"][index] = json.loads(c["snippet"])
    assert all(main["recipe"]) and all(stock["recipe"])
    payload = {"status": 200, "count": 1, "data": {"solutions": [main, stock]}}
    original_stock_rows = []
    for index, node in enumerate(baseline[repair.STOCK_PATH]["composition"]):
        if index == 7:
            original_stock_rows.append(stock["recipe"][index])
        else:
            original_stock_rows.append(json.loads(node["evidence"][0]["snippet"]))
    raw = {
        repair.MEDIUM: json.dumps(payload, indent=4),
        repair.STOCK: json.dumps({"data": {"recipe": original_stock_rows}}, indent=4),
    }
    return raw, main, stock


def build(baseline, sources, path):
    return repair.build(baseline[path], path, *sources, "2026-10-07T12:30:00+00:00")


def test_stock_boundary_and_all_changed_claims_have_exact_evidence(baseline, sources):
    doc, claims = build(baseline, sources, repair.MEDIUM_PATH)
    assert len(claims) == 15
    assert [n["preferred_term"] for n in doc["ingredients"]] == [
        "Proteose peptone no. 3",
        "Yeast extract",
        "Glucose",
        "Agar",
        "Distilled water",
    ]
    assert len(doc["solutions"]) == 1
    stock = doc["solutions"][0]
    assert stock["term"] == {"id": "mediadive.solution:2838", "label": "Total Salts"}
    assert stock["concentration"] == {"value": "0.666", "unit": "L"}
    assert stock["composition"][0]["concentration"] == {"value": "234", "unit": "G_PER_L"}
    assert doc["ingredients"][4]["concentration"] == {"value": "0.333", "unit": "L"}
    assert stock["composition"][8]["concentration"] == {"value": "1", "unit": "L"}
    assert "concentration" not in stock["composition"][7]
    assert stock["composition"][7]["notes"] == repair.DROP_NOTE
    for c in claims:
        assert c["snippet"] in sources[0][c["reference"]]
        node = reviewer.get_node(doc, c["pointer"])
        assert node.get("concentration") == c["new"]
        if c["pointer"] == ["solutions", 0]:
            node = doc
        assert node["evidence"][0]["snippet"] == c["snippet"]
        assert c["field"] in node["evidence"][0]["explanation"]


@pytest.mark.parametrize("path", list(repair.TARGETS))
def test_unrelated_fields_and_all_prior_provenance_are_preserved(baseline, sources, path):
    after, _ = build(baseline, sources, path)
    assert after["curation_history"][:-1] == baseline[path]["curation_history"]
    assert after["curation_history"][-1]["curator"] == "codex"
    after["curation_history"].pop()
    del after["references"][-2:]
    if "references" not in baseline[path]:
        after.pop("references")
    if path == repair.MEDIUM_PATH:
        after["ingredients"].pop()
        for index, node in enumerate(after["ingredients"]):
            node.pop("evidence")
            if index == 0:
                node.pop("notes")
        moved = after.pop("solutions")[0]["composition"][:-1]
        for node in moved:
            node.pop("evidence")
        moved[7].pop("notes")
        moved[7]["concentration"] = {"value": "9", "unit": "G_PER_L"}
        after["ingredients"].extend(moved)
        after.pop("evidence")
    else:
        node = after["composition"][7]
        node.pop("notes")
        node.pop("evidence")
        node["concentration"] = {"value": "9", "unit": "VARIABLE"}
    assert after == baseline[path]


def test_stock_report_covers_retained_claims_and_placeholder(baseline, sources):
    after, claims = build(baseline, sources, repair.STOCK_PATH)
    assert len(claims) == 10
    assert [c["status"] for c in claims].count("verified") == 8
    assert claims[7]["status"] == "correct" and claims[7]["new"] is None
    assert claims[9]["status"] == "unsupported"
    assert after["composition"][7]["notes"] == repair.DROP_NOTE


@pytest.mark.parametrize(
    "change",
    [
        "id",
        "lineage",
        "form",
        "amount",
        "dose",
        "drop_unit",
        "drop_strength",
        "agar_condition",
        "extra_stock",
    ],
)
def test_drift_is_rejected(baseline, sources, change):
    doc = baseline[repair.MEDIUM_PATH]
    if change == "id":
        doc["id"] = "CultureMech:000001"
    elif change == "lineage":
        doc["media_term"]["term"]["id"] = "mediadive.medium:1125"
    elif change == "form":
        doc["ingredients"][5]["preferred_term"] = "MgCl2"
    elif change == "amount":
        doc["ingredients"][4]["concentration"]["value"] = "23.4"
    elif change == "dose":
        sources[1]["recipe"][3]["amount"] = 999
    elif change == "drop_unit":
        sources[2]["recipe"][7]["unit"] = "g"
    elif change == "drop_strength":
        sources[2]["recipe"][7]["attribute"] = "5 %"
    elif change == "agar_condition":
        sources[1]["recipe"][5]["condition"] = "different formulation"
    else:
        doc["solutions"] = [{"preferred_term": "Unreviewed stock"}]
    with pytest.raises(ValueError):
        build(baseline, sources, repair.MEDIUM_PATH)


def test_unverified_capture_rejected(tmp_path):
    (tmp_path / "medium-1399.json").write_text("{}")
    with pytest.raises(ValueError, match="Medium capture changed"):
        repair.captures(tmp_path)


@pytest.mark.parametrize("change", [None, "second_record_drift", "plan_drift"])
def test_preview_and_whole_batch_preflight(tmp_path, monkeypatch, baseline, sources, change):
    targets, originals = {}, {}
    for path, (identifier, cls, _) in repair.TARGETS.items():
        raw = yaml.safe_dump(baseline[path], sort_keys=False, allow_unicode=True).encode()
        local = tmp_path / path
        local.parent.mkdir(parents=True, exist_ok=True)
        local.write_bytes(raw)
        originals[path] = raw
        targets[path] = (identifier, cls, repair.sha(raw))
    monkeypatch.setattr(repair, "ROOT", tmp_path)
    monkeypatch.setattr(repair, "TARGETS", targets)
    monkeypatch.setattr(repair, "captures", lambda _: sources)
    monkeypatch.setattr(
        repair.subprocess,
        "check_output",
        lambda cmd, **kw: (
            b"test-head\n" if "rev-parse" in cmd else ("\0".join(targets) + "\0").encode()
        ),
    )
    plan_path = tmp_path / "plan.json"
    args = ["repair", "--source-dir", str(tmp_path), "--plan", str(plan_path)]
    monkeypatch.setattr(sys, "argv", args + ["--dry-run"])
    repair.main()
    assert all((tmp_path / p).read_bytes() == raw for p, raw in originals.items())
    if change == "second_record_drift":
        (tmp_path / repair.STOCK_PATH).write_bytes(originals[repair.STOCK_PATH] + b"# changed\n")
    elif change == "plan_drift":
        plan = json.loads(plan_path.read_text())
        plan["records"][1]["claims"][7]["new"] = {"value": "9", "unit": "L"}
        plan_path.write_text(json.dumps(plan))
    monkeypatch.setattr(sys, "argv", args + ["--apply"])
    if change:
        with pytest.raises(ValueError):
            repair.main()
        assert (tmp_path / repair.MEDIUM_PATH).read_bytes() == originals[repair.MEDIUM_PATH]
    else:
        repair.main()
        applied = {p: (tmp_path / p).read_bytes() for p in targets}
        assert all(applied[p] != originals[p] for p in targets)
        repair.main()
        monkeypatch.setattr(sys, "argv", args + ["--verify"])
        repair.main()
        assert all((tmp_path / p).read_bytes() == raw for p, raw in applied.items())


def test_followup_hash_chain_requires_exact_baseline_and_identity():
    before = "baseline"
    digest = repair.sha(before.encode())
    item = {"path": repair.STOCK_PATH, "id": "CultureMech:012117", "after_sha256": digest}
    successor = {**item, "before_sha256": digest, "before_text": before, "after_sha256": "b" * 64}
    assert reviewer.followup_result_hash(item) == (digest, 0)
    assert reviewer.followup_result_hash(item, [successor]) == ("b" * 64, 1)
    for key, value in (
        ("id", "CultureMech:000001"),
        ("before_text", "different"),
        ("after_sha256", "invalid"),
    ):
        broken = {**successor, key: value}
        with pytest.raises(ValueError):
            reviewer.followup_result_hash(item, [broken])
    with pytest.raises(ValueError, match="Ambiguous"):
        reviewer.followup_result_hash(item, [successor, successor])


def test_current_curation_exactly_matches_pinned_plan_after_application():
    plan = json.loads(PLAN.read_text())
    for item in plan["records"]:
        raw = (ROOT / item["path"]).read_bytes()
        assert repair.sha(raw) == item["after_sha256"]
        assert repair.sha(item["before_text"].encode()) == item["before_sha256"]
        doc = yaml.load(raw, Loader=yaml.CSafeLoader)
        assert doc["id"] == item["id"]
        assert doc["curation_history"][-1]["action"] == repair.ACTION
