"""Guard exact snippets, stock boundaries, source pins, and this applied cohort."""

import copy
import importlib.util
import json
import re
import sys
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from review_solution_concentration_evidence import (  # noqa: E402
    followup_chain,
    followup_result_hash,
)

from tests.test_medium_concentration_batch import AUDIT, FOLLOWUPS  # noqa: E402

SPEC = importlib.util.spec_from_file_location(
    "stock_repair", ROOT / "scripts/repair_mediadive_stock_concentration_evidence.py"
)
repair = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(repair)


@pytest.fixture
def inputs():
    row = {
        "recipe_order": 1,
        "compound": "Na2SeO3 x 5 H2O",
        "compound_id": 107,
        "solution": None,
        "solution_id": None,
        "attribute": None,
        "condition": None,
        "amount": 4,
        "unit": "mg",
        "g_l": 0.004,
        "optional": 0,
    }
    source = {
        "id": 3981,
        "name": "Se/W solution",
        "volume": 1000,
        "recipe": [row],
        "steps": [],
    }
    before = {
        "id": "CultureMech:013038",
        "preferred_term": source["name"],
        "term": {"id": "mediadive.solution:3981", "label": source["name"]},
        "composition": [
            {
                "preferred_term": row["compound"],
                "term": {"id": "mediadive.compound:107", "label": row["compound"]},
                "concentration": {"value": "0.004", "unit": "G_PER_L"},
                "evidence": [
                    {
                        "reference": "https://example.org/earlier-role",
                        "supports": "SUPPORT",
                        "snippet": "earlier role",
                        "explanation": "Existing role claim, not a concentration.",
                    }
                ],
            }
        ],
        "ingredients": [
            {
                "preferred_term": "See source for composition",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
        ],
        "curation_history": [
            {"timestamp": "2026-01-01T00:00:00Z", "curator": "original", "action": "import"}
        ],
    }
    return before, source


def proposal(before, source):
    raw = json.dumps({"status": 200, "count": 1, "data": source}, indent=4)
    return (
        repair.curate(
            before,
            raw,
            3981,
            "CultureMech:013038",
            repair.sha(raw.encode()),
            timestamp="2026-10-07T08:00:00Z",
        ),
        raw,
    )


def test_proposal_preserves_existing_claims_and_quotes_literal_json(inputs):
    before, source = inputs
    original = copy.deepcopy(before)
    (after, claims), raw = proposal(before, source)
    assert before == original
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["curator"] == "codex"
    evidence = after["composition"][0]["evidence"]
    assert evidence[0] == before["composition"][0]["evidence"][0]
    assert evidence[-1]["snippet"] in raw
    assert json.loads(evidence[-1]["snippet"]) == source["recipe"][0]
    assert "composition[0].concentration" in evidence[-1]["explanation"]
    assert "provider-declared stock" in evidence[-1]["explanation"]
    assert [c["status"] for c in claims] == ["evidence_only", "unsupported"]
    assert not repair.validate_recipe(after, target_class="SolutionRecipe")


@pytest.mark.parametrize(
    "mutation",
    [
        "identity",
        "label",
        "salt",
        "duplicate",
        "volume",
        "mass",
        "optional",
        "condition",
        "attribute",
        "nested",
        "working_dose",
    ],
)
def test_unreviewed_states_are_refused(inputs, mutation):
    before, source = inputs
    row = source["recipe"][0]
    if mutation == "identity":
        before["term"]["id"] = "mediadive.solution:3980"
    elif mutation == "label":
        before["preferred_term"] = "Other stock"
    elif mutation == "salt":
        before["composition"][0]["term"]["label"] = "Na2SeO3"
    elif mutation == "duplicate":
        source["recipe"].append(copy.deepcopy(row))
        before["composition"].append(copy.deepcopy(before["composition"][0]))
    elif mutation == "volume":
        source["volume"] = 0
    elif mutation == "mass":
        row["g_l"] = 4
    elif mutation == "optional":
        row["optional"] = 1
    elif mutation == "condition":
        row["condition"] = "Only for strain X"
    elif mutation == "attribute":
        row["attribute"] = "10 mM"
    elif mutation == "nested":
        before["solutions"] = [{"preferred_term": "extra stock"}]
    else:
        before["concentration"] = {"value": "0.01", "unit": "L"}
    with pytest.raises(ValueError):
        proposal(before, source)


def test_source_hash_mismatch_is_refused(inputs):
    before, source = inputs
    raw = json.dumps({"status": 200, "count": 1, "data": source})
    with pytest.raises(ValueError, match="Source hash"):
        repair.curate(before, raw, 3981, before["id"], "0" * 64)


@pytest.mark.parametrize("value", [None, True, "NaN", "Infinity", -1])
def test_missing_or_nonfinite_quantities_are_not_defaulted(value):
    with pytest.raises(ValueError):
        repair.number(value)


def test_zero_is_not_missing():
    assert repair.number(0) == 0


def test_ambiguous_exact_excerpts_are_refused():
    with pytest.raises(ValueError, match="Ambiguous"):
        repair.exact_object('[{"amount": 1}, {"amount": 1}]', {"amount": 1})


def test_preflight_refuses_all_writes_on_a_concurrent_edit(tmp_path):
    first, second = tmp_path / "first.yaml", tmp_path / "second.yaml"
    first.write_bytes(b"old")
    second.write_bytes(b"user edit")
    plans = [{"path": p, "before": b"old", "after": b"new"} for p in (first, second)]
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.apply(plans)
    assert first.read_bytes() == b"old"
    assert second.read_bytes() == b"user edit"


def test_byte_identical_rerun_does_not_write(tmp_path):
    path = tmp_path / "record.yaml"
    path.write_bytes(b"unchanged")
    mtime = path.stat().st_mtime_ns
    assert repair.apply([{"path": path, "before": b"unchanged", "after": b"unchanged"}]) == 0
    assert path.stat().st_mtime_ns == mtime


def setup_preflight(tmp_path, monkeypatch, inputs):
    before, source = inputs
    relative = "data/normalized_yaml/bacterial/test_stock.yaml"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    baseline = yaml.safe_dump(before, sort_keys=False).encode()
    path.write_bytes(baseline)
    raw = json.dumps({"status": 200, "count": 1, "data": source}, indent=4).encode()
    (tmp_path / "ingredient-mediadive-solution-3981-20261007.json").write_bytes(raw)
    monkeypatch.setattr(
        repair,
        "COHORT",
        [(3981, before["id"], path.name, repair.sha(baseline), repair.sha(raw))],
    )

    def git_output(args, **kwargs):
        if args[1] == "ls-files":
            return (relative + "\0").encode()
        assert args == ["git", "show", f"{repair.BASE}:{relative}"]
        return baseline

    monkeypatch.setattr(repair.subprocess, "check_output", git_output)
    return path, baseline


def test_complete_prepare_apply_cycle_is_idempotent(tmp_path, monkeypatch, inputs):
    path, baseline = setup_preflight(tmp_path, monkeypatch, inputs)
    preview = repair.prepare(tmp_path, tmp_path)
    assert path.read_bytes() == baseline
    assert repair.apply(preview) == 1
    applied = path.read_bytes()
    mtime = path.stat().st_mtime_ns
    assert repair.apply(repair.prepare(tmp_path, tmp_path)) == 0
    assert path.read_bytes() == applied
    assert path.stat().st_mtime_ns == mtime
    assert len(yaml.safe_load(applied)["curation_history"]) == 2


def test_prepare_does_not_discard_presentation_edits(tmp_path, monkeypatch, inputs):
    path, baseline = setup_preflight(tmp_path, monkeypatch, inputs)
    changed = b"# User note\n" + baseline
    path.write_bytes(changed)
    with pytest.raises(ValueError, match="presentation"):
        repair.prepare(tmp_path, tmp_path)
    assert path.read_bytes() == changed


def test_default_cli_only_previews(tmp_path, monkeypatch, inputs, capsys):
    path, baseline = setup_preflight(tmp_path, monkeypatch, inputs)
    monkeypatch.setattr(repair, "ROOT", tmp_path)
    monkeypatch.setattr(sys, "argv", ["repair", "--source-dir", str(tmp_path)])
    repair.main()
    assert path.read_bytes() == baseline
    summary = json.loads(capsys.readouterr().out.strip().splitlines()[-1])
    assert summary["mode"] == "preview"
    assert summary["changed"] == 0


@pytest.mark.parametrize("sid,stable_id,filename,baseline_hash,source_hash", repair.COHORT)
def test_applied_stock_data_and_complete_per_record_report(
    sid, stable_id, filename, baseline_hash, source_hash
):
    path = ROOT / "data/normalized_yaml/bacterial" / filename
    report_path = (
        ROOT
        / "reports/ingredient_concentration_curation/20261007-mediadive-stocks"
        / (path.stem + ".md")
    )
    text = report_path.read_text()
    result_hashes = re.findall(r"^- Result SHA256: `([a-f0-9]{64})`$", text, re.MULTILINE)
    assert len(result_hashes) == 1
    item = {
        "path": path.relative_to(ROOT).as_posix(),
        "id": stable_id,
        "after_sha256": result_hashes[0],
    }
    successors = [
        r
        for plan_path in FOLLOWUPS
        for r in json.loads(plan_path.read_text())["records"]
        if r["before_sha256"] != r["after_sha256"]
    ]
    raw = path.read_bytes()
    expected, _ = followup_result_hash(item, successors)
    assert repair.sha(raw) == expected
    chain = followup_chain(item, successors)
    doc = AUDIT.invert_chain(raw, chain) if chain else yaml.safe_load(raw)
    historical_raw = chain[0]["before_text"].encode() if chain else raw
    assert repair.sha(historical_raw) == result_hashes[0]
    assert doc["id"] == stable_id
    reference = f"https://mediadive.dsmz.de/rest/solution/{sid}"
    assert [r["reference"] for r in doc["references"]].count(reference) == 1
    for index, node in enumerate(doc["composition"]):
        compound_id = int(node["term"]["id"].split(":")[1])
        if sid == 595 and compound_id == 68:
            assert node["concentration"] == {"value": "2.5", "unit": "G_PER_L"}
            assert not node.get("evidence")
            continue
        entries = [e for e in node["evidence"] if e["reference"] == reference]
        assert len(entries) == 1
        evidence = entries[0]
        row = json.loads(evidence["snippet"])
        assert row["compound_id"] == compound_id
        assert row["compound"] == node["preferred_term"]
        assert evidence["supports"] == "SUPPORT"
        assert f"composition[{index}].concentration" in evidence["explanation"]
        assert source_hash in evidence["explanation"]
        if compound_id == 4:
            expected = (
                {"value": "to 1 L final volume", "unit": "VARIABLE"}
                if sid in repair.MAKE_UP
                else {"value": "1", "unit": "L"}
            )
            assert node["concentration"] == expected
            if sid in repair.MAKE_UP:
                assert repair.MAKE_UP[sid] in evidence["explanation"]
        else:
            assert node["concentration"]["unit"] == "G_PER_L"
            assert repair.number(node["concentration"]["value"]) == repair.number(row["g_l"])
            assert "not a concentration in any receiving medium" in evidence["explanation"]
    assert doc["ingredients"] == [
        {
            "preferred_term": "See source for composition",
            "concentration": {"value": "variable", "unit": "VARIABLE"},
        }
    ]
    assert sum(e["action"] == repair.ACTION for e in doc["curation_history"]) == 1
    assert not repair.validate_recipe(doc, target_class="SolutionRecipe")
    lines = text.splitlines()
    assert [line for line in lines if line.startswith("- Record:")] == [
        f"- Record: data/normalized_yaml/bacterial/{filename}"
    ]
    assert sum(line.startswith("| `") for line in lines) == len(doc["composition"]) + 1
    assert baseline_hash in text
    assert repair.sha(historical_raw) in text
