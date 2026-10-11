"""Exact base composition, preparation stages, snippets, and guarded writes."""

import copy
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_dsmz2_stock_boundary as repair  # noqa: E402

PLAN = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz2-stock-boundary/plan.json"


@pytest.fixture
def before():
    raw = json.loads(PLAN.read_text())["records"][0]["before_text"].encode()
    assert repair.sha(raw) == repair.BASELINE
    return raw


@pytest.fixture
def baseline(before):
    return repair.load_yaml(before)


@pytest.fixture
def sources(baseline):
    # Offline source-shaped fixture; actual source verification uses pinned captures.
    rows = [
        {
            "recipe_order": 1,
            "compound": "Peptone",
            "compound_id": 1,
            "amount": 5,
            "unit": "g",
            "g_l": 5,
            "optional": 0,
        },
        {
            "recipe_order": 2,
            "compound": "Meat extract",
            "compound_id": 2,
            "amount": 3,
            "unit": "g",
            "g_l": 3,
            "optional": 0,
        },
        {
            "recipe_order": 3,
            "compound": "Agar",
            "compound_id": 3,
            "condition": "for solid medium",
            "amount": 15,
            "unit": "g",
            "g_l": 15,
            "optional": 0,
        },
        {
            "recipe_order": 4,
            "compound": "Distilled water",
            "compound_id": 4,
            "amount": 1000,
            "unit": "ml",
            "optional": 0,
        },
    ]
    stock = {
        "id": 1,
        "name": "Main sol. 1",
        "volume": 1000,
        "recipe": rows,
        "steps": [{"step": x["description"]} for x in baseline["preparation_steps"][2:]],
    }
    main = {
        "id": 4,
        "name": "Main sol. 2",
        "volume": 1000,
        "recipe": [
            {
                "recipe_order": 1,
                "solution": "Main sol. 1",
                "solution_id": 1,
                "amount": 1000,
                "unit": "ml",
                "optional": 0,
            },
            {
                "recipe_order": 2,
                "compound": "Urea",
                "compound_id": 339,
                "amount": 20,
                "unit": "g/l",
                "g_l": 20,
                "optional": 0,
            },
        ],
        "steps": [{"step": x["description"]} for x in baseline["preparation_steps"][:2]],
    }
    medium = {
        "id": 2,
        "name": "BACILLUS PASTEURII MEDIUM",
        "source": "DSMZ",
        "link": repair.PDFS[2],
    }
    base = {"id": 1, "name": "NUTRIENT AGAR", "source": "DSMZ", "link": repair.PDFS[1]}
    return {
        repair.MEDIUM: {"data": {"medium": medium, "solutions": [main, stock]}},
        repair.BASE: {"data": {"medium": base, "solutions": [copy.deepcopy(stock)]}},
    }


def capture(sources):
    raws = {ref: json.dumps(data, indent=4) for ref, data in sources.items()}
    meta = {ref: {"accessed_at": "2026-10-07T11:00:00+00:00"} for ref in sources}
    return raws, meta


def build(baseline, sources):
    return repair.build(baseline, *capture(sources), "2026-10-07T11:01:00+00:00")


def test_stock_boundary_and_preparation_stage_are_separate(baseline, sources):
    after, claims = build(baseline, sources)
    assert [n["preferred_term"] for n in after["ingredients"]] == ["Urea"]
    stock = after["solutions"][0]
    assert stock["concentration"] == {"value": "1", "unit": "L"}
    assert stock["composition"][3]["concentration"] == {"value": "1", "unit": "L"}
    assert [n["preferred_term"] for n in stock["composition"]] == [
        "Peptone",
        "Meat extract",
        "Agar",
        "Distilled water",
    ]
    assert stock["preparation_notes"] == "\n\n".join(
        x["description"] for x in baseline["preparation_steps"][2:]
    )
    assert len(after["preparation_steps"]) == 2
    assert after["preparation_steps"][0]["action"] == "MIX"
    assert "Do not adjust pH" in after["preparation_steps"][0]["description"]
    assert after["preparation_steps"][1] == baseline["preparation_steps"][1]
    assert "variants" not in after
    assert len(claims) == 8
    assert len(after["evidence"]) == 1
    assert len(after["references"]) == 4
    raws, _ = capture(sources)
    for claim in claims:
        assert claim["snippet"] in raws[claim["reference"]]
        node = repair.get_node(after, claim["evidence_pointer"])
        entry = node["evidence"][-1]
        assert claim["field"] in entry["explanation"]
        assert claim["snippet"] == entry["snippet"] or claim["snippet"] in entry["explanation"]
        assert repair.get_node(after, claim["pointer"]) == claim["new"]


def test_round_trip_inversion_preserves_every_unrelated_field(baseline, sources):
    after, _ = build(baseline, sources)
    assert after["curation_history"][:-1] == baseline["curation_history"]
    assert after["curation_history"][-1]["curator"] == "codex"
    after["curation_history"].pop()
    del after["references"][-4:]
    if "references" not in baseline:
        after.pop("references")
    stock = after.pop("solutions")[0]
    stock["composition"].pop()
    after["ingredients"].extend(stock["composition"])
    for node in after["ingredients"]:
        node["evidence"].pop()
        if not node["evidence"]:
            node.pop("evidence")
    after.pop("evidence")
    after["preparation_steps"][0]["action"] = "ADJUST_PH"
    after["preparation_steps"].extend(copy.deepcopy(baseline["preparation_steps"][2:]))
    assert after == baseline


@pytest.mark.parametrize(
    "change",
    [
        "id",
        "medium",
        "form",
        "amount",
        "dose",
        "volume",
        "base_disagrees",
        "condition",
        "pH",
        "instructions",
        "action",
        "stock",
        "variant",
    ],
)
def test_identity_amount_and_stage_drift_refused(baseline, sources, change):
    data = sources[repair.MEDIUM]["data"]
    if change == "id":
        baseline["id"] = "CultureMech:001400"
    elif change == "medium":
        data["medium"]["id"] = 3
    elif change == "form":
        baseline["ingredients"][1]["preferred_term"] = "Peptone variant"
    elif change == "amount":
        baseline["ingredients"][0]["concentration"]["value"] = "2"
    elif change == "dose":
        data["solutions"][0]["recipe"][0]["amount"] = 100
    elif change == "volume":
        data["solutions"][0]["volume"] = 500
    elif change == "base_disagrees":
        sources[repair.BASE]["data"]["solutions"][0]["recipe"][0]["amount"] = 50
    elif change == "condition":
        data["solutions"][1]["recipe"][2]["condition"] = "for different strain"
    elif change == "pH":
        data["solutions"][1]["steps"][0]["step"] = "Adjust final medium to pH 7."
    elif change == "instructions":
        baseline["preparation_steps"][0]["description"] = "Add urea after autoclaving."
    elif change == "action":
        baseline["preparation_steps"][0]["action"] = "AUTOCLAVE"
    elif change == "stock":
        baseline["solutions"] = [{"preferred_term": "Other base"}]
    else:
        baseline["variants"] = [{"name": "Other", "modifications": ["Change quantity"]}]
    with pytest.raises(ValueError):
        build(baseline, sources)


@pytest.mark.parametrize("damage", [None, "record", "plan", "metadata", "source"])
def test_preview_apply_verify_and_drift(tmp_path, monkeypatch, before, sources, damage):
    target = tmp_path / repair.TARGET
    target.parent.mkdir(parents=True)
    target.write_bytes(before)
    raw, meta = capture(sources)
    monkeypatch.setattr(repair, "captures", lambda _: (raw, meta))
    monkeypatch.setattr(
        repair.subprocess,
        "check_output",
        lambda cmd, **kw: b"test-head\n" if "rev-parse" in cmd else (repair.TARGET + "\0").encode(),
    )
    plan_path = tmp_path / "plan.json"
    repair.process(tmp_path, tmp_path, plan_path, "preview")
    assert target.read_bytes() == before
    if damage == "record":
        target.write_bytes(before + b"# Concurrent edit\n")
    elif damage == "plan":
        plan = json.loads(plan_path.read_text())
        plan["records"][0]["claims"][0]["new"]["value"] = "200"
        plan_path.write_text(json.dumps(plan))
    elif damage == "metadata":
        meta[repair.MEDIUM]["accessed_at"] = "2026-10-07T12:00:00+00:00"
    elif damage == "source":
        data = json.loads(raw[repair.MEDIUM])
        data["data"]["solutions"][0]["recipe"][1]["unit"] = "mg"
        raw[repair.MEDIUM] = json.dumps(data, indent=4)
    original = target.read_bytes()
    if damage:
        with pytest.raises(ValueError):
            repair.process(tmp_path, tmp_path, plan_path, "apply")
        assert target.read_bytes() == original
    else:
        _, applied = repair.process(tmp_path, tmp_path, plan_path, "apply")
        assert applied["changed"] == 1 and applied["new_evidence_entries"] == 6
        output = target.read_bytes()
        assert repair.process(tmp_path, tmp_path, plan_path, "apply")[1]["changed"] == 0
        assert repair.process(tmp_path, tmp_path, plan_path, "verify")[1]["already_applied"] == 1
        assert target.read_bytes() == output


def test_unverified_capture_cannot_be_used(tmp_path):
    folder = tmp_path / "sources"
    folder.mkdir()
    (folder / "1.json").write_text("{}")
    with pytest.raises((ValueError, OSError, KeyError)):
        repair.captures(tmp_path)
