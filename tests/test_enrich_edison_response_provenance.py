"""Regression tests for task-aware Edison enrichment provenance."""

from __future__ import annotations

import importlib
import json
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
er = importlib.import_module("enrich_edison_response")

STEM = "example-edison-literature"


class _Response:
    answer = "answer"
    formatted_answer = "answer\n\nReferences\n\n1. Example\n"
    answer_reasoning = None
    created_at = None


class _Client:
    def __init__(self, *, fail_verbose: bool = False, fail_files: bool = False):
        self.fail_verbose = fail_verbose
        self.fail_files = fail_files
        self.verbose_calls = 0

    def get_task(self, *, task_id: str, verbose: bool):
        if verbose:
            self.verbose_calls += 1
            if self.fail_verbose:
                raise RuntimeError("fixture failure")
            return type(
                "Verbose",
                (),
                {"agent_state": [{"tool": "search"}], "environment_frame": None, "metadata": None},
            )()
        return _Response()

    def list_files(self, *, trajectory_id: str):
        if self.fail_files:
            raise RuntimeError("fixture failure")
        return []


def _write_fixture(tmp_path: Path, *, trace_task: str = "task-OLD") -> Path:
    meta_path = tmp_path / f"{STEM}-meta.yaml"
    meta_path.write_text(yaml.safe_dump({"status": "success", "task_id": "task-NEW"}))
    (tmp_path / f"{STEM}.md").write_text("answer")
    (tmp_path / f"{STEM}-response.json").write_text("{}")
    (tmp_path / f"{STEM}-citations.md").write_text("# Citations\n")
    (tmp_path / f"{STEM}-agent-state.json").write_text(
        json.dumps({"task_id": trace_task, "agent_state": []})
    )
    # files.json is deliberately absent so enrichment cannot early-return.
    return meta_path


def test_agent_state_presence_requires_the_current_task_id(tmp_path):
    _write_fixture(tmp_path)
    missing = er.needs_enrichment(tmp_path, STEM, force=False, task_id="task-NEW")
    assert missing["agent_state_json"] is True
    assert all(missing.values())

    (tmp_path / f"{STEM}-agent-state.json").write_text(
        json.dumps({"task_id": "task-NEW", "agent_state": []})
    )
    assert (
        er.needs_enrichment(tmp_path, STEM, force=False, task_id="task-NEW")["agent_state_json"]
        is False
    )


def test_enrichment_refetches_a_stale_trace_and_attributes_the_new_one(tmp_path):
    meta_path = _write_fixture(tmp_path)
    client = _Client()

    result = er.enrich_one(client, meta_path, force=False, dry_run=False)

    assert result["status"] == "enriched"
    assert client.verbose_calls == 1
    trace = json.loads((tmp_path / f"{STEM}-agent-state.json").read_text())
    assert trace["task_id"] == "task-NEW"
    meta = yaml.safe_load(meta_path.read_text())
    assert meta["sidecar_files"]["agent_state_json"] is True


def test_failed_refetch_does_not_reassert_the_stale_trace(tmp_path):
    meta_path = _write_fixture(tmp_path)
    client = _Client(fail_verbose=True)

    result = er.enrich_one(client, meta_path, force=False, dry_run=False)

    assert result["status"] == "enriched"
    trace = json.loads((tmp_path / f"{STEM}-agent-state.json").read_text())
    assert trace["task_id"] == "task-OLD"
    meta = yaml.safe_load(meta_path.read_text())
    assert meta["task_id"] == "task-NEW"
    assert meta["sidecar_files"]["agent_state_json"] is False


def test_task_mismatch_does_not_claim_any_sidecar_that_failed_to_refresh(tmp_path):
    meta_path = _write_fixture(tmp_path)
    (tmp_path / f"{STEM}-files.json").write_text('[{"name": "stale.yaml"}]')
    client = _Client(fail_verbose=True, fail_files=True)

    result = er.enrich_one(client, meta_path, force=False, dry_run=False)

    assert result["status"] == "enriched"
    meta = yaml.safe_load(meta_path.read_text())
    assert meta["sidecar_files"] == {
        "answer_md": True,
        "response_json": True,
        "citations_md": True,
        "agent_state_json": False,
        "files_json": False,
    }
    assert meta["artifacts_fetched"] == []
    assert meta["artifacts_skipped"] == []
