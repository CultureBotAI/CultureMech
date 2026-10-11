"""Guard the exact receiving-medium link and unchanged nested stock amounts."""

import copy
import json
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_jcm_m1308_stock_evidence as repair  # noqa: E402


@pytest.fixture
def reviewed_record():
    doc = yaml.load((ROOT / repair.TARGET).read_bytes(), Loader=yaml.CSafeLoader)
    refs = {repair.MEDIUM} | {
        f"https://mediadive.dsmz.de/rest/solution/{sid}" for _, sid, _, _ in repair.STOCKS
    }
    for stock_index, _, _, _ in repair.STOCKS:
        for node in doc["solutions"][stock_index]["composition"]:
            node.pop("evidence", None)
    doc["references"] = [r for r in doc["references"] if r["reference"] not in refs]
    doc["curation_history"] = [e for e in doc["curation_history"] if e["action"] != repair.ACTION]
    return doc


@pytest.fixture
def sources(reviewed_record):
    medium = {
        "medium": {"id": "J1219", "source": "JCM", "link": repair.JCM},
        "solutions": [{"id": 5347, "name": "Main sol. J1219", "recipe": []}],
    }
    result = {}
    for stock_index, sid, name, ids in repair.STOCKS:
        rows = []
        for cid, node in zip(
            ids, reviewed_record["solutions"][stock_index]["composition"], strict=True
        ):
            amount = float(node["concentration"]["value"])
            rows.append(
                {
                    "compound_id": cid,
                    "compound": node["preferred_term"],
                    "amount": amount,
                    "unit": "mg",
                    "g_l": amount / 1000,
                    "optional": 0,
                    "condition": None,
                    "attribute": None,
                    "solution_id": None,
                }
            )
        rows.append({"compound_id": 4})
        source = {"id": sid, "name": name, "volume": 1000, "recipe": rows, "steps": []}
        result[f"solution-{sid}"] = (json.dumps(source), source)
        medium["solutions"].append(copy.deepcopy(source))
        medium["solutions"][0]["recipe"].append(
            {"solution_id": sid, "solution": name, "amount": 10, "unit": "ml", "optional": 0}
        )
    result["J1219"] = (json.dumps(medium), medium)
    return result


def test_only_scoped_evidence_references_and_history_are_added(reviewed_record, sources):
    after, claims = repair.build(reviewed_record, sources, "2026-10-07T12:00:00+00:00")
    assert len(claims) == 12
    assert all(c["old"] == c["new"] and c["status"] == "evidence_only" for c in claims)
    for stock_index, sid, _, _ in repair.STOCKS:
        for index, node in enumerate(after["solutions"][stock_index]["composition"]):
            evidence = node.pop("evidence")
            assert len(evidence) == 1
            assert evidence[0]["snippet"] in sources[f"solution-{sid}"][0]
            assert (
                f"solutions[{stock_index}].composition[{index}].concentration"
                in evidence[0]["explanation"]
            )
            assert repair.MEDIUM in evidence[0]["explanation"]
            assert "not an independently measured final volume" in evidence[0]["explanation"]
    assert after["curation_history"][:-1] == reviewed_record["curation_history"]
    event = after["curation_history"].pop()
    assert event["curator"] == "codex" and event["action"] == repair.ACTION
    assert all(str(sid) in event["source"] for _, sid, _, _ in repair.STOCKS)
    assert after["references"][:-3] == reviewed_record["references"]
    del after["references"][-3:]
    assert after == reviewed_record


@pytest.mark.parametrize("change", ["lineage", "link", "volume", "form", "amount", "local_dose"])
def test_source_or_record_drift_is_rejected(reviewed_record, sources, change):
    if change == "lineage":
        reviewed_record["notes"] = "Unrelated recipe"
    elif change == "link":
        sources["J1219"][1]["solutions"][0]["recipe"][0]["amount"] = 1
    elif change == "volume":
        sources["solution-3981"][1]["volume"] = 500
    elif change == "form":
        reviewed_record["solutions"][1]["composition"][0]["preferred_term"] = "Na2SeO3"
    elif change == "amount":
        sources["solution-3981"][1]["recipe"][0]["g_l"] = 0.04
    else:
        reviewed_record["solutions"][1]["concentration"]["unit"] = "G_PER_L"
    with pytest.raises(ValueError):
        repair.build(reviewed_record, sources, "2026-10-07T12:00:00+00:00")


def test_unverified_capture_bytes_are_rejected(tmp_path):
    (tmp_path / "ingredient-mediadive-J1219-20261007.json").write_text("{}")
    with pytest.raises(ValueError, match="Source changed"):
        repair.captures(tmp_path)


def test_preview_apply_verify_and_rerun(tmp_path, monkeypatch, reviewed_record, sources):
    path = tmp_path / repair.TARGET
    path.parent.mkdir(parents=True)
    before = yaml.safe_dump(reviewed_record, allow_unicode=True, sort_keys=False).encode()
    path.write_bytes(before)
    monkeypatch.setattr(repair, "ROOT", tmp_path)
    monkeypatch.setattr(repair, "BEFORE", repair.sha(before))
    monkeypatch.setattr(repair, "captures", lambda _: sources)
    monkeypatch.setattr(
        repair.subprocess, "check_output", lambda *a, **k: (repair.TARGET + "\0").encode()
    )
    args = ["repair", "--source-dir", str(tmp_path), "--plan", str(tmp_path / "plan.json")]
    monkeypatch.setattr(sys, "argv", args + ["--dry-run"])
    repair.main()
    assert path.read_bytes() == before
    monkeypatch.setattr(sys, "argv", args + ["--apply"])
    repair.main()
    after = path.read_bytes()
    assert after != before
    repair.main()
    assert path.read_bytes() == after
    monkeypatch.setattr(sys, "argv", args + ["--verify"])
    repair.main()
    assert path.read_bytes() == after
