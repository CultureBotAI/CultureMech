"""CLAW-governed contract: declared review skills persist validated observations."""

import importlib.util
import os
import subprocess
from copy import deepcopy
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture(scope="module")
def reviews():
    spec = importlib.util.spec_from_file_location("shared_record_reviews", ROOT / "scripts/record_review.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_review_skill_routes_and_rubrics_exist(reviews):
    profile = reviews.load_document((ROOT / "conf/record_review.yaml").read_bytes())
    assert set(profile) == {"version", "repository", "skills", "rubrics"}
    assert profile["version"] == 1
    assert profile["repository"].lower() == reviews.repository_identity(ROOT).lower()
    assert profile["skills"] and profile["rubrics"]
    for key in ("skills", "rubrics"):
        assert isinstance(profile[key], list)
        assert len(profile[key]) == len(set(profile[key]))
        for relative in profile[key]:
            reviews.relative_path(relative)
            body = reviews.read_bytes(ROOT, relative).decode("utf-8")
            if key == "skills":
                assert "docs/record-reviews.md" in body, f"{relative} bypasses the shared output contract"
    assert reviews.read_bytes(ROOT, "docs/record-review-profile.md")
    assert reviews.read_bytes(ROOT, "docs/record-reviews.md")


def test_every_saved_structured_bundle_is_valid(reviews):
    identity = reviews.repository_identity(ROOT)
    reviews.assert_append_only(ROOT, os.environ.get("RECORD_REVIEW_BASE", "HEAD"))
    for path in reviews.review_paths(ROOT):
        review = reviews.read_review(ROOT, path)
        assert review["repository"].lower() == identity.lower()


@pytest.fixture
def sample(tmp_path, reviews):
    root = (tmp_path / "synthetic-repository").resolve()
    root.mkdir()
    for args in (("init",), ("config", "user.name", "Contract fixture"),
                 ("config", "user.email", "fixture@example.invalid"),
                 ("remote", "add", "origin", "https://github.com/Example/FixtureMech.git")):
        subprocess.run(["git", "-C", str(root), *args], check=True, capture_output=True)
    (root / "record.yaml").write_text("id: EX:fixture\n")
    subprocess.run(["git", "-C", str(root), "add", "record.yaml"], check=True, capture_output=True)
    subprocess.run(["git", "-C", str(root), "commit", "-m", "Synthetic fixture"],
                   check=True, capture_output=True)
    owner = {"repository": "Example/FixtureMech", "path": "record.yaml", "role": "test fixture"}
    targets = [{"target_id": "EX:fixture", "path": "record.yaml", "label": "Synthetic fixture",
                "kind": "maintained", "owner_paths": [owner]}]
    inspection = reviews.inspect_source(root, targets)
    record = {
        "schema_version": "1.0.0", "review_id": "20260101T000000Z-synthetic-contract",
        "kind": "record", "repository": "Example/FixtureMech", "title": "Synthetic contract test",
        "started_at": "2026-01-01T00:00:00Z", "finished_at": "2026-01-01T00:00:00Z",
        "reviewer": {"identity": "contract fixture", "kind": "deterministic",
                     "independence": "not_applicable", "independence_basis": "No scientific review."},
        "skill": "contract-test", "completion": "completed", "verdict": "pass",
        "scientific_review": False, "summary": "Only the synthetic fixture is assessed.",
        "source": inspection["source"], "targets": targets,
        "scope": {"description": "Synthetic identity check.", "selection": "Explicit fixture.",
                  "coverage": "full", "population_size": 1, "reviewed_target_ids": ["EX:fixture"]},
        "checks": [{"check_id": "id", "name": "Fixture ID", "required": True, "status": "passed",
                    "summary": "Explicit fixture ID inspected.", "target_ids": ["EX:fixture"],
                    "evidence_ids": ["fixture"]}],
        "evidence": [{"evidence_id": "fixture", "kind": "record_content", "reference": "record.yaml",
                      "accessed_at": "2026-01-01T00:00:00Z", "support": "supports",
                      "summary": "The synthetic fixture declares EX:fixture."}],
        "assessments": [{"assessment_id": "identity", "area": "identity", "topic": "Fixture identity",
                         "outcome": "supported", "summary": "Fixture ID matches.",
                         "target_ids": ["EX:fixture"], "evidence_ids": ["fixture"]}],
        "findings": [], "actions": [], "limitations": [],
    }
    return root, record


def test_shared_saver_round_trip_and_immutability(reviews, sample):
    root, record = sample
    path = reviews.save_review(root, record)
    assert reviews.read_review(root, str(path.relative_to(root))) == record
    assert path.with_name("review.md").read_text() == reviews.render_markdown(record)
    with pytest.raises(reviews.ReviewError, match="immutable"):
        reviews.save_review(root, record)
    path.with_name("review.md").write_text("An independent, misleading verdict")
    with pytest.raises(reviews.ReviewError, match="Markdown does not match"):
        reviews.read_review(root, str(path.relative_to(root)))


def test_shared_saver_refuses_changed_inputs_and_false_passes(reviews, sample):
    root, record = sample
    invalid = deepcopy(record)
    invalid["checks"][0]["status"] = "failed"
    with pytest.raises(reviews.ReviewError, match="passing verdict"):
        reviews.validate_review(invalid)
    invalid = deepcopy(record)
    invalid["scientific_review"] = True
    with pytest.raises(reviews.ReviewError, match="not scientific"):
        reviews.validate_review(invalid)
    (root / "record.yaml").write_text("id: EX:changed\n")
    with pytest.raises(reviews.ReviewError, match="input changed"):
        reviews.save_review(root, record)
    assert not (root / reviews.REPORT_ROOT).exists()
