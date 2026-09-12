"""Required checks must report on every PR and its actual merge queue candidate."""

from copy import deepcopy
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
# Job/check names are an external ruleset contract. Renames require coordinated
# settings changes; deriving this list from the workflows would hide a deletion.
REQUIRED_JOBS = {
    "chebi-consistency.yaml": {"consistency": "consistency"},
    "concentration-plausibility.yaml": {"plausibility": "plausibility"},
    "curation-history.yaml": {"history": "history"},
    "label-correspondence.yaml": {"label-drift-report": "label-drift-report"},
    "tests.yaml": {
        "changed-python-quality": "Changed Python quality + wheel smoke",
        "fast": "Fast tests",
        "corpus-and-integration": "Full corpus and integration suite",
    },
    "validate-strict.yaml": {"validate": "validate"},
    "vendored-sync.yaml": {"vendored-sync": "vendored-sync"},
}


def _load(name):
    return yaml.safe_load((ROOT / ".github" / "workflows" / name).read_text())


def _assert_required_workflow(document, expected_jobs):
    events = document.get("on", document.get(True, {}))
    assert "pull_request" in events, "missing PR trigger"
    assert events["pull_request"] in (None, {}), "required PR checks cannot be filtered"
    assert events.get("merge_group") == {"types": ["checks_requested"]}, "missing queue trigger"
    for job_id, check_name in expected_jobs.items():
        job = document["jobs"][job_id]
        assert job.get("name", job_id) == check_name, "required check renamed"
        assert "if" not in job, "required job cannot skip the candidate"
        assert not job.get("continue-on-error"), "required job must fail on errors"
        for step in job.get("steps", []):
            if step.get("uses", "").startswith("actions/checkout@"):
                assert "ref" not in step.get("with", {}), "must check out the event's candidate"
    concurrency = document.get("concurrency")
    if concurrency:
        assert "github.run_id" in concurrency["group"], "queue runs need distinct groups"
        assert concurrency["cancel-in-progress"] == "${{ github.event_name == 'pull_request' }}"


@pytest.mark.parametrize("workflow", REQUIRED_JOBS)
def test_required_workflow_runs_for_pr_and_merge_group(workflow):
    _assert_required_workflow(_load(workflow), REQUIRED_JOBS[workflow])


@pytest.mark.parametrize("defect", ["queue", "paths", "skip", "cancel", "checkout"])
def test_the_guard_rejects_a_broken_workflow(defect):
    name = "vendored-sync.yaml"
    document = _load(name)
    _assert_required_workflow(document, REQUIRED_JOBS[name])  # unmutated control
    broken = deepcopy(document)
    events = broken.get("on", broken.get(True))
    job = broken["jobs"]["vendored-sync"]
    if defect == "queue":
        del events["merge_group"]
    elif defect == "paths":
        events["pull_request"] = {"paths": ["src/**"]}
    elif defect == "skip":
        job["if"] = "github.event_name == 'pull_request'"
    elif defect == "cancel":
        broken["concurrency"]["cancel-in-progress"] = True
    else:
        job["steps"][0]["with"] = {"ref": "main"}
    with pytest.raises(AssertionError):
        _assert_required_workflow(broken, REQUIRED_JOBS[name])


def test_required_job_names_are_unambiguous():
    names = [
        _load(workflow)["jobs"][job_id].get("name", job_id)
        for workflow, jobs in REQUIRED_JOBS.items()
        for job_id in jobs
    ]
    assert len(names) == len(set(names)), "different required workflows report the same check"


def test_changed_python_uses_the_complete_merge_group_base():
    steps = _load("tests.yaml")["jobs"]["changed-python-quality"]["steps"]
    quality = next(step for step in steps if step.get("name") == "Ruff and Black on changed Python")
    assert quality["env"]["GITHUB_EVENT_BEFORE"] == (
        "${{ github.event.merge_group.base_sha || github.event.before }}"
    )
