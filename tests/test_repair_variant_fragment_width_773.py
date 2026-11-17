"""Exact source-bound presentation repair and durable failure evidence (#773)."""

import copy
import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

ADHOC = Path(__file__).resolve().parents[1] / "scripts/adhoc"
sys.path.insert(0, str(ADHOC))
SPEC = importlib.util.spec_from_file_location(
    "repair_variant_fragment_width_773", ADHOC / "repair_variant_fragment_width_773.py"
)
repair = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(repair)
from audit_variant_coverage_683 import NOTES, SOURCE  # noqa: E402
from record_io import dump_record  # noqa: E402


@pytest.fixture
def source(tmp_path, monkeypatch):
    relative = "data/normalized_yaml/algae/synthetic.yaml"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    base = {
        "id": "CultureMech:000001",
        "name": "Synthetic",
        "ingredients": [],
        "variants": [{"name": "Treatment", "modifications": ["Add synthetic component."]}],
    }
    base_bytes = dump_record(base).encode()
    change = {
        "action": "ADD",
        "ingredient": {"preferred_term": "synthetic component"},
        "stage": "synthetic treatment",
        "source_modification_index": 0,
        "source_text": "Add synthetic component.",
        "evidence": [
            {
                "reference": "https://example.org/synthetic",
                "supports": "SUPPORT",
                "snippet": "Add synthetic component.",
                "explanation": "Long source evidence must keep the native absolute wrapping width. "
                * 8,
            }
        ],
    }
    variants = [{"variant_index": 0, "variant_name": "Treatment", "ingredient_changes": [change]}]
    decision = {
        "path": relative,
        "recipe_id": base["id"],
        "expected_sha256": repair.curate.digest(base_bytes),
        "variants": variants,
    }
    proposal = tmp_path / "proposal.json"
    proposal.write_text(json.dumps({"schema_version": 1, "records": [decision]}))
    desired = copy.deepcopy(base)
    desired["variants"][0]["ingredient_changes"] = [change]
    desired["curation_history"] = [
        {
            "timestamp": "2026-11-16T00:00:00Z",
            "curator": "codex",
            "action": "STRUCTURED_VARIANT_INGREDIENTS",
            "notes": NOTES,
            "source": SOURCE,
            "changes": json.dumps(
                {
                    "decision_sha256": repair.curate.digest(proposal.read_bytes()),
                    "variants": variants,
                }
            ),
        }
    ]
    old_bytes = yaml.safe_dump(desired, sort_keys=False, width=84).encode()
    path.write_bytes(old_bytes)
    monkeypatch.setattr(
        repair,
        "git_bytes",
        lambda root, commit, name: (
            base_bytes if commit == repair.BASE and name == relative else old_bytes
        ),
    )
    monkeypatch.setattr(repair.curate, "validate_recipe", lambda record: [])
    monkeypatch.setattr(
        repair.curate,
        "write_validated_recipe",
        lambda record, stage: stage.write_text(dump_record(record)),
    )
    return tmp_path, path, proposal, desired, old_bytes


def test_preview_apply_and_exact_replay_preserve_values_and_timestamp(source):
    root, path, proposal, desired, old_bytes = source
    result = repair.run([proposal], root / "preview.json", root=root)
    assert result["records"][0]["status"] == "PLANNED"
    assert result["records"][0]["native_base_canonical"] is True
    assert result["records"][0]["f9_canonical"] is False
    assert result["records"][0]["repaired_canonical"] is True
    assert path.read_bytes() == old_bytes
    repair.run(
        [proposal],
        root / "applied.json",
        root=root,
        apply=True,
        only_record=str(path.relative_to(root)),
    )
    assert yaml.safe_load(path.read_bytes()) == desired
    assert dump_record(desired) == path.read_text()
    repaired = path.read_bytes()
    result = repair.run([proposal], root / "replay.json", root=root, apply=True)
    assert result["records"][0]["status"] == "UNCHANGED"
    assert path.read_bytes() == repaired
    assert len(desired["curation_history"]) == 1


def test_noncanonical_reconstruction_refuses_before_receipt_or_write(source, monkeypatch):
    root, path, proposal, _desired, old_bytes = source
    monkeypatch.setattr(
        repair.curate, "render_additions", lambda original, desired, variants: old_bytes
    )
    receipt = root / "noncanonical.json"
    with pytest.raises(ValueError, match="lose native canonicality"):
        repair.run([proposal], receipt, root=root, apply=True)
    assert path.read_bytes() == old_bytes
    assert not receipt.exists()


def test_unrecognized_preimage_refuses_before_receipt_or_recipe_write(source):
    root, path, proposal, _desired, old_bytes = source
    path.write_bytes(old_bytes + b"# concurrent change\n")
    before = path.read_bytes()
    with pytest.raises(ValueError, match="current bytes differ"):
        repair.run([proposal], root / "refused.json", root=root, apply=True)
    assert path.read_bytes() == before
    assert not (root / "refused.json").exists()


def test_partial_native_stage_never_replaces_authority(source, monkeypatch):
    root, path, proposal, _desired, old_bytes = source

    def interrupted(_record, stage):
        stage.write_text("partial")
        raise OSError("synthetic write failure")

    monkeypatch.setattr(repair.curate, "write_validated_recipe", interrupted)
    receipt = root / "failed.json"
    with pytest.raises(repair.curate.ApplyError):
        repair.run([proposal], receipt, root=root, apply=True)
    assert path.read_bytes() == old_bytes
    assert json.loads(receipt.read_text())["state"] == "INCOMPLETE"


def test_post_replace_receipt_failure_preserves_prewrite_hash_and_observation(source, monkeypatch):
    root, path, proposal, desired, _old_bytes = source
    persist = repair.curate.persist_receipt

    def fail_after_replace(destination, value):
        if value["records"][0]["status"] == "APPLIED":
            raise OSError("synthetic receipt failure")
        persist(destination, value)

    monkeypatch.setattr(repair.curate, "persist_receipt", fail_after_replace)
    receipt = root / "interrupted.json"
    with pytest.raises(repair.curate.ApplyError) as error:
        repair.run([proposal], receipt, root=root, apply=True)
    assert yaml.safe_load(path.read_bytes()) == desired
    row = json.loads(receipt.read_text())["records"][0]
    assert row["status"] == "APPLYING"
    assert row["planned_after_sha256"] == repair.curate.digest(path.read_bytes())
    assert error.value.receipt["records"][0]["observed_sha256"] == row["planned_after_sha256"]


def test_receipt_cannot_pollute_authoritative_input_tree(source):
    root, path, proposal, _desired, old_bytes = source
    receipt = path.with_name("invalid-receipt.yaml")
    with pytest.raises(ValueError, match="outside authoritative"):
        repair.run([proposal], receipt, root=root, apply=True)
    assert not receipt.exists()
    assert path.read_bytes() == old_bytes
