"""Tests that ``sidecar_files`` describes THIS Edison run, not the directory.

Edison output stems are deterministic — ``{slug}-edison-{job}`` — so re-running
the same medium and job writes into a directory that already holds the previous
run's sidecars. ``capture_full_response`` used to report ``sidecar_files`` from a
plain ``.exists()`` sweep of that directory, which meant a fresh run that failed
to fetch the agent-state trace still reported ``agent_state_json: true`` next to
its own new ``task_id``. An auditor following the meta would open the previous
task's trajectory believing it belonged to the new one (#288).

The fix records which keys the invocation actually wrote. These tests pin that
behaviour, and pin the deliberate escape hatch: ``_existing_sidecars`` without a
written-set still returns a disk snapshot, because ``enrich_edison_response``
backfills sidecars for the *same* ``task_id`` already in the meta.

No Edison client is constructed and no credits are spent — the response is a
stub object and ``client=None`` exercises the "verbose fetch skipped" path.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent


def _load_module():
    path = REPO_ROOT / "scripts" / "_edison_capture.py"
    spec = importlib.util.spec_from_file_location("_edison_capture", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["_edison_capture"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def ec():
    return _load_module()


class _StubResponse:
    """Minimal stand-in for the SDK response object.

    Only the attributes ``capture_full_response`` reads are defined; anything
    else falls through ``getattr(..., default)`` as it would for a job type that
    does not carry the field.
    """

    def __init__(self, task_id: str, answer: str = "new answer"):
        self.task_id = task_id
        self.answer = answer
        self.formatted_answer = f"{answer}\n\nReferences\n\n1. doe2020paper pages 1-2\n"
        self.status = "success"
        self.has_successful_answer = True


STEM = "archaeoglobus_medium_dsm_399-edison-literature"

# The sidecars a *previous*, fully successful run of the same stem left behind.
PRIOR_RUN_FILES = {
    f"{STEM}.md": "old answer",
    f"{STEM}-response.json": '{"task_id": "task-OLD"}',
    f"{STEM}-citations.md": "# Citations\n",
    f"{STEM}-agent-state.json": '{"task_id": "task-OLD", "agent_state": []}',
    f"{STEM}-files.json": "[]",
}


@pytest.fixture
def prior_run_dir(tmp_path: Path) -> Path:
    for name, body in PRIOR_RUN_FILES.items():
        (tmp_path / name).write_text(body)
    return tmp_path


def test_stale_sidecars_are_not_attributed_to_the_new_task(ec, prior_run_dir):
    """The regression: a rerun that fetches neither trace reports neither.

    ``client=None`` is how a run behaves when the verbose fetch and
    ``list_files`` are skipped, so nothing rewrites the agent-state or files
    sidecars — yet both are sitting on disk from ``task-OLD``.
    """
    meta = ec.capture_full_response(
        response=_StubResponse("task-NEW"),
        client=None,
        out_dir=prior_run_dir,
        stem=STEM,
        query="q",
        base_meta={"slug": "archaeoglobus_medium_dsm_399"},
    )

    assert meta["task_id"] == "task-NEW"
    assert meta["sidecar_files"] == {
        # written by this invocation, unconditionally
        "answer_md": True,
        "response_json": True,
        "citations_md": True,
        # left over from task-OLD — must not be claimed by task-NEW
        "agent_state_json": False,
        "files_json": False,
    }

    # The stale files themselves are left alone; only the claim about them
    # changes. Deleting them would destroy the earlier run's evidence.
    assert (prior_run_dir / f"{STEM}-agent-state.json").exists()
    assert json.loads(
        (prior_run_dir / f"{STEM}-agent-state.json").read_text()
    )["task_id"] == "task-OLD"


def test_sidecars_this_run_did_write_are_reported_true(ec, prior_run_dir):
    """The fix must not simply report False for everything it did not fetch.

    A client that answers both secondary fetches makes this run the author of
    all five sidecars, and the meta should say so even though five files of the
    same names were already present.
    """

    class _Client:
        def get_task(self, task_id, verbose=False):  # noqa: ARG002
            return type("V", (), {"agent_state": [{"tool": "search"}],
                                  "environment_frame": None,
                                  "metadata": None})()

        def list_files(self, trajectory_id):  # noqa: ARG002
            return []

    meta = ec.capture_full_response(
        response=_StubResponse("task-NEW"),
        client=_Client(),
        out_dir=prior_run_dir,
        stem=STEM,
        query="q",
        base_meta={},
    )

    assert meta["sidecar_files"] == dict.fromkeys(
        ["answer_md", "response_json", "citations_md",
         "agent_state_json", "files_json"],
        True,
    )
    # ...and the rewritten trace really is the new task's.
    assert json.loads(
        (prior_run_dir / f"{STEM}-agent-state.json").read_text()
    )["task_id"] == "task-NEW"


def test_empty_output_dir_reports_only_what_was_written(ec, tmp_path):
    """First run of a stem: no prior files, so the two unfetched keys are False
    for the ordinary reason rather than the stale-file reason."""
    meta = ec.capture_full_response(
        response=_StubResponse("task-FIRST"),
        client=None,
        out_dir=tmp_path / "nested",
        stem=STEM,
        query="q",
        base_meta={},
    )
    assert meta["sidecar_files"]["answer_md"] is True
    assert meta["sidecar_files"]["agent_state_json"] is False


def test_written_set_cannot_claim_a_file_that_is_absent(ec, tmp_path):
    """Belt-and-braces: the report is an AND of "we wrote it" and "it is there".

    A key in the written set whose file never materialised (a failed write, a
    later unlink) must still report False, so the meta never points at a path
    that does not exist.
    """
    assert ec._existing_sidecars(tmp_path, STEM, {"answer_md", "files_json"}) == {
        "answer_md": False,
        "response_json": False,
        "citations_md": False,
        "agent_state_json": False,
        "files_json": False,
    }


def test_omitting_the_written_set_still_snapshots_the_disk(ec, prior_run_dir):
    """The ``enrich_edison_response`` contract.

    Backfill runs against the ``task_id`` already stored in the meta, so "what
    is on disk for this stem" is the truthful answer there and must not regress
    to the written-set semantics.
    """
    assert ec._existing_sidecars(prior_run_dir, STEM) == dict.fromkeys(
        ["answer_md", "response_json", "citations_md",
         "agent_state_json", "files_json"],
        True,
    )


def test_dry_run_reports_no_sidecars_at_all(ec, prior_run_dir):
    """A dry run spends nothing and authors nothing, so it must not inherit the
    previous run's sidecar claims — ``capture_dry_run`` omits the key entirely
    rather than reporting a directory snapshot."""
    meta = ec.capture_dry_run(
        out_dir=prior_run_dir,
        stem=STEM,
        query="rendered prompt",
        base_meta={"slug": "archaeoglobus_medium_dsm_399"},
    )
    assert meta["status"] == "dry-run"
    assert "sidecar_files" not in meta
    assert "task_id" not in meta
    # and it must not have overwritten the earlier run's answer
    assert (prior_run_dir / f"{STEM}.md").read_text() == "old answer"
