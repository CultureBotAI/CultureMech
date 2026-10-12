"""Adversarial guards for exact-source stock restoration, without live source access."""

import copy
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_reviewed_medium_stock_boundaries as repair  # noqa: E402


@pytest.fixture
def sample():
    doc = {
        "id": "CultureMech:001943",
        "name": "leucothrix_medium",
        "original_name": "LEUCOTHRIX MEDIUM",
        "category": "bacterial",
        "medium_type": "COMPLEX",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "DSMZ Medium 79",
            "term": {"id": "mediadive.medium:79", "label": "LEUCOTHRIX MEDIUM"},
        },
        "notes": "Source: DSMZ | Link: " + repair.PDF.format("79"),
        "ingredients": [
            {"preferred_term": "Tryptone", "concentration": {"value": "10", "unit": "G_PER_L"}},
            {
                "preferred_term": "NaCl",
                "term": {"id": "CHEBI:26710", "label": "sodium chloride"},
                "concentration": {"value": "24", "unit": "G_PER_L"},
            },
        ],
        "preparation_steps": [
            {"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 7.8."}
        ],
        "curation_history": [],
    }
    source = {
        "status": 200,
        "count": 1,
        "data": {
            "medium": {
                "id": 79,
                "name": "LEUCOTHRIX MEDIUM",
                "source": "DSMZ",
                "link": repair.PDF.format("79"),
            },
            "solutions": [
                {
                    "id": 135,
                    "name": "Main sol. 79",
                    "volume": 1000,
                    "recipe": [
                        {
                            "compound": "Tryptone",
                            "compound_id": 71,
                            "amount": 10,
                            "unit": "g",
                            "g_l": 10,
                            "optional": 0,
                        },
                        {
                            "solution": "Synthetic sea water",
                            "solution_id": 5554,
                            "amount": 1000,
                            "unit": "ml",
                            "optional": 0,
                        },
                    ],
                },
                {
                    "id": 5554,
                    "name": "Synthetic sea water",
                    "volume": 1000,
                    "recipe": [
                        {
                            "compound": "NaCl",
                            "compound_id": 43,
                            "amount": 24,
                            "unit": "g",
                            "g_l": 24,
                            "optional": 0,
                        },
                        {
                            "compound": "Distilled water",
                            "compound_id": 4,
                            "amount": 1000,
                            "unit": "ml",
                            "optional": 0,
                        },
                    ],
                    "steps": [{"step": "Adjust pH to 7.8."}],
                },
            ],
        },
    }
    return doc, source


def build(sample):
    doc, source = sample
    raw = json.dumps(source, indent=2)
    meta = {"sha256": repair.sha(raw.encode()), "accessed_at": "2026-10-07T10:00:00+00:00"}
    return repair.build(doc, raw, meta, "79", "2026-10-07T12:00:00+00:00")


def test_scopes_quantities_and_moves_preparation_without_mutating_input(sample):
    before = copy.deepcopy(sample[0])
    after, claims = build(sample)
    assert sample[0] == before
    assert after["ingredients"][0]["concentration"] == before["ingredients"][0]["concentration"]
    stock = after["solutions"][0]
    assert stock["concentration"] == {"value": "1", "unit": "L"}
    assert stock["composition"][0]["concentration"] == before["ingredients"][1]["concentration"]
    assert stock["composition"][0]["term"] == before["ingredients"][1]["term"]
    assert stock["composition"][1]["concentration"] == {"value": "1", "unit": "L"}
    assert stock["preparation_notes"] == before["preparation_steps"][0]["description"]
    assert "preparation_steps" not in after
    assert len(after["evidence"]) == 1
    assert after["curation_history"][-1]["curator"] == "codex"
    assert len(claims) == 5
    for claim in claims:
        entries = repair.get_node(after, claim["evidence_pointer"])["evidence"]
        assert len(entries) == 1
        assert claim["field"] in entries[0]["explanation"]
        assert (
            claim["snippet"] == entries[0]["snippet"]
            or claim["snippet"] in entries[0]["explanation"]
        )


@pytest.mark.parametrize(
    "change",
    [
        lambda d, s: d["media_term"]["term"].update(id="mediadive.medium:78"),
        lambda d, s: d.update(original_name="DIFFERENT MEDIUM"),
        lambda d, s: d.update(notes="Other source"),
        lambda d, s: d.update(solutions=[{"preferred_term": "Already structured"}]),
        lambda d, s: d["ingredients"].reverse(),
        lambda d, s: d["ingredients"][1]["concentration"].update(value="24000"),
        lambda d, s: d["ingredients"][1]["concentration"].update(per_volume="100 ml"),
        lambda d, s: d["ingredients"][1].update(notes="Alternative salt"),
        lambda d, s: d["ingredients"][1].update(
            evidence=[
                {"reference": "https://example.org/old", "snippet": "old", "supports": "SUPPORT"}
            ]
        ),
        lambda d, s: d["preparation_steps"][0].update(description="Adjust pH to 8.0."),
        lambda d, s: d["preparation_steps"][0].update(step_number=2),
        lambda d, s: s["data"]["medium"].update(id=78),
        lambda d, s: s["data"]["medium"].update(source="Other"),
        lambda d, s: s["data"]["solutions"][0]["recipe"][1].update(solution_id=135),
        lambda d, s: s["data"]["solutions"][0]["recipe"][1].update(solution="Similar seawater"),
        lambda d, s: s["data"]["solutions"][0]["recipe"][1].update(unit="%"),
        lambda d, s: s["data"]["solutions"][0]["recipe"][1].update(optional=1),
        lambda d, s: s["data"]["solutions"][0]["recipe"][1].update(amount=0),
        lambda d, s: s["data"]["solutions"][1]["recipe"][0].update(attribute="10%"),
        lambda d, s: s["data"]["solutions"][1]["recipe"][0].update(condition="if necessary"),
        lambda d, s: s["data"]["solutions"][1]["recipe"][0].update(unit="drops"),
        lambda d, s: s["data"]["solutions"][1]["recipe"][0].update(g_l=25),
        lambda d, s: s["data"]["solutions"][1].update(volume=500),
        lambda d, s: s["data"]["solutions"][1]["recipe"][1].update(unit="g"),
        lambda d, s: s["data"]["solutions"][1]["recipe"].append({"solution_id": 135}),
        lambda d, s: s["data"]["solutions"].append(copy.deepcopy(s["data"]["solutions"][1])),
    ],
)
def test_source_or_record_ambiguity_fails_closed(sample, change):
    change(*sample)
    with pytest.raises((ValueError, KeyError)):
        build(sample)


@pytest.mark.parametrize("bad", [True, 0, -1, "NaN", "Infinity"])
def test_invalid_amounts_rejected(bad):
    with pytest.raises(ValueError):
        repair.litres(bad)


@pytest.fixture
def worktree(tmp_path, monkeypatch, sample):
    doc, source = sample
    relative = "data/normalized_yaml/bacterial/example.yaml"
    target = tmp_path / relative
    target.parent.mkdir(parents=True)
    before = repair.render("", doc)
    target.write_bytes(before)
    cache = tmp_path / "cache"
    (cache / "sources").mkdir(parents=True)
    raw = json.dumps(source)
    (cache / "sources/79.json").write_text(raw)
    metadata = {
        "url": repair.API + "79",
        "response_url": repair.API + "79",
        "http_status": 200,
        "accessed_at": "2026-10-07T10:00:00+00:00",
        "sha256": repair.sha(raw.encode()),
    }
    (cache / "sources/79.metadata.json").write_text(json.dumps(metadata))
    (cache / "DSMZ_Medium79.pdf").write_bytes(b"test PDF capture")
    original = {
        "records": [
            {
                "path": relative,
                "id": doc["id"],
                "medium_id": "79",
                "before_sha256": repair.sha(before),
                "after_sha256": repair.sha(before),
                "source_sha256": metadata["sha256"],
            }
        ]
    }
    original_path = tmp_path / repair.ORIGINAL
    original_path.parent.mkdir(parents=True)
    original_path.write_text(json.dumps(original))
    monkeypatch.setattr(repair, "ORIGINAL_SHA", repair.sha(original_path.read_bytes()))
    monkeypatch.setattr(repair, "CHAINS", {"79": ["79"]})
    monkeypatch.setattr(repair, "PDF_HASHES", {"79": repair.sha(b"test PDF capture")})
    monkeypatch.setattr(
        repair.subprocess,
        "check_output",
        lambda command, **kw: (
            (relative + "\0").encode() if "ls-files" in command else b"baseline\n"
        ),
    )
    return tmp_path, cache, tmp_path / "followup/plan.json", target, before


def test_preview_apply_verify_noop_and_plan_tampering(worktree):
    root, cache, plan_path, target, before = worktree
    plan, result = repair.process(root, cache, plan_path, "preview")
    assert target.read_bytes() == before and result["changed"] == 0
    with pytest.raises(ValueError, match="not applied"):
        repair.process(root, cache, plan_path, "verify")
    assert repair.process(root, cache, plan_path, "apply")[1]["changed"] == 1
    after = target.read_bytes()
    assert repair.process(root, cache, plan_path, "verify")[1]["already_applied"] == 1
    assert repair.process(root, cache, plan_path, "apply")[1]["changed"] == 0
    assert target.read_bytes() == after
    plan["records"][0]["claims"][0]["snippet"] = "fabricated"
    plan_path.write_text(json.dumps(plan))
    with pytest.raises(ValueError, match="decision"):
        repair.process(root, cache, plan_path, "apply")
    assert target.read_bytes() == after


@pytest.mark.parametrize("damage", ["record", "source", "metadata", "pdf", "path"])
def test_apply_revalidates_inputs_before_writing(worktree, damage):
    root, cache, plan_path, target, before = worktree
    repair.process(root, cache, plan_path, "preview")
    if damage == "record":
        target.write_bytes(before + b"\n# concurrent edit\n")
    elif damage == "source":
        p = cache / "sources/79.json"
        p.write_text(p.read_text() + " ")
    elif damage == "metadata":
        p = cache / "sources/79.metadata.json"
        data = json.loads(p.read_text())
        data["accessed_at"] = "2026-10-08T10:00:00+00:00"
        p.write_text(json.dumps(data))
    elif damage == "pdf":
        (cache / "DSMZ_Medium79.pdf").write_bytes(b"changed")
    else:
        p = json.loads(plan_path.read_text())
        p["records"][0]["path"] = "../../escape.yaml"
        plan_path.write_text(json.dumps(p))
    unchanged = target.read_bytes()
    with pytest.raises(ValueError):
        repair.process(root, cache, plan_path, "apply")
    assert target.read_bytes() == unchanged


def audit_module():
    path = (
        ROOT
        / "reports/ingredient_concentration_curation/20261007-dsmz1399-stock-boundary/audit_diff.py"
    )
    spec = importlib.util.spec_from_file_location("independent_stock_audit", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_applied_batch_has_exact_hashes_and_independent_semantic_inversion():
    folder = ROOT / "reports/ingredient_concentration_curation/20261007-medium-stock-boundaries"
    plan = json.loads((folder / "plan.json").read_text())
    audit = audit_module()
    assert [r["medium_id"] for r in plan["records"]] == list(repair.CHAINS)
    for item in plan["records"]:
        before = repair.load_yaml(item["before_text"])
        raw = (ROOT / item["path"]).read_bytes()
        assert repair.sha(raw) == item["after_sha256"]
        assert repair.sha(item["before_text"].encode()) == item["before_sha256"]
        after = repair.load_yaml(raw)
        assert after["id"] == before["id"] == item["id"]
        audit.invert_stock_batch(before, after, item)
        text = (folder / f"{item['medium_id']}.md").read_text()
        assert f"- Follow-up target: {item['path']}" in text
        assert "- Record:" not in text
        assert sum(line.startswith("| ") for line in text.splitlines()) == len(item["claims"]) + 2
    assert dict(audit.counts) == {
        "stock_nodes_relocated": 44,
        "new_quantity_slots": 23,
        "preparation_steps_relocated": 3,
        "new_evidence": 100,
        "new_references": 20,
        "new_curation_history": 7,
    }


@pytest.mark.parametrize("damage", ["quantity", "chemical", "root", "snippet", "extra_stock_node"])
def test_independent_inversion_rejects_unreviewed_changes(damage):
    folder = ROOT / "reports/ingredient_concentration_curation/20261007-medium-stock-boundaries"
    item = json.loads((folder / "plan.json").read_text())["records"][0]
    before = repair.load_yaml(item["before_text"])
    after = repair.load_yaml((ROOT / item["path"]).read_bytes())
    if damage == "quantity":
        after["solutions"][0]["composition"][0]["concentration"]["value"] = "999"
    elif damage == "chemical":
        after["solutions"][0]["composition"][0]["term"]["id"] = "CHEBI:999"
    elif damage == "root":
        after["ph_value"] = 9
    elif damage == "snippet":
        after["solutions"][0]["composition"][0]["evidence"][0]["snippet"] = "fabricated"
    else:
        after["solutions"][0]["composition"].append(
            copy.deepcopy(after["solutions"][0]["composition"][0])
        )
    with pytest.raises(AssertionError):
        audit_module().invert_stock_batch(before, after, item)
