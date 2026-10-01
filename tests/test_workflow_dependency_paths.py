"""Every path-filtered workflow must watch `pyproject.toml` and `uv.lock` (#369).

A `paths:` filter decides whether a gate runs at all. Before this, none of the
five corpus gates listed the dependency files, so a PR that changed only
`pyproject.toml` and `uv.lock` started `tests.yaml` — which has no filter — and
nothing else. `label-correspondence` was the sharpest case: it runs the OAK
id-label check and caches `~/.data/oaklib`, so it is precisely the gate that
would notice an oaklib regression, and precisely the one a lockfile edit could
not start.

#365 hid this. It bumped oaklib and showed 7 green checks, but the gates ran only
because the forced linkml upgrade regenerated files under
`src/culturemech/schema/**`, which *is* filtered on. Had the change stayed the
pin-only edit it was scoped as, the gates would have been skipped and the PR
would have looked just as green. A coincidence was standing in for a gate.

MediaIngredientMech#495 and TraitMech#566 are the same finding in the sibling
repos; MIM fixed it first and MediaIngredientMech#499 confirmed the fix works —
that PR touched only `pyproject.toml`, `uv.lock` and a file under `tests/`, which
is not in MIM's filter, and `id-label-gate` still ran.
"""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

WORKFLOWS = Path(__file__).resolve().parent.parent / ".github" / "workflows"
DEPENDENCY_FILES = ("pyproject.toml", "uv.lock")


def _paths_blocks(document: dict) -> list[tuple[str, list[str]]]:
    """Every trigger in one workflow that carries a `paths:` filter.

    `on` is quoted deliberately: YAML 1.1 reads a bare `on:` key as the boolean
    True, so `document["on"]` misses it and a test written that way passes by
    finding nothing at all.
    """
    triggers = document.get(True, document.get("on"))
    if not isinstance(triggers, dict):
        return []
    return [
        (name, config["paths"])
        for name, config in triggers.items()
        if isinstance(config, dict) and isinstance(config.get("paths"), list)
    ]


def _workflow_files() -> list[Path]:
    """Both suffixes. GitHub accepts `.yml` and `.yaml` interchangeably, and
    `.yml` is what most templates emit. Globbing one of them would let a new
    gate arrive unguarded while this file kept reporting all-clear — the same
    failure shape it exists to catch, one level up (#376)."""
    return sorted({*WORKFLOWS.glob("*.yaml"), *WORKFLOWS.glob("*.yml")})


def _blocks() -> list[tuple[str, str, list[str]]]:
    found = []
    for path in _workflow_files():
        for trigger, paths in _paths_blocks(yaml.safe_load(path.read_text())):
            found.append((path.name, trigger, paths))
    return found


@pytest.mark.parametrize(
    "workflow,trigger,paths",
    _blocks(),
    ids=lambda v: v if isinstance(v, str) else "",
)
def test_a_path_filtered_workflow_watches_the_dependency_files(workflow, trigger, paths):
    missing = [f for f in DEPENDENCY_FILES if f not in paths]
    assert not missing, (
        f"{workflow} [{trigger}] does not watch {', '.join(missing)}, so a "
        "dependency-only change cannot trigger it — the shape that let #365 show "
        "green without running the gates"
    )


def test_the_guard_is_not_vacuous():
    """Parametrising over a discovered set can silently collect nothing.

    If `_paths_blocks` stops finding filters — the `on:`-is-True trap above is
    the likely way — every case above vanishes and the suite still passes.
    """
    blocks = _blocks()
    assert len(_workflow_files()) >= 10, "workflow discovery found almost nothing"
    # PR checks are now unconditional for merge queues. These push scopes remain
    # filtered, so discovering none is still a parser/discovery failure.
    assert {(workflow, trigger) for workflow, trigger, _ in blocks} >= {
        ("curation-history.yaml", "push"),
        ("label-correspondence.yaml", "push"),
        ("generate-pages.yaml", "push"),
    }


@pytest.mark.parametrize("on_key", ["on", True])
def test_path_discovery_handles_yaml_boolean_keys_and_unfiltered_events(on_key):
    paths = ["data/**", "pyproject.toml", "uv.lock"]
    document = {on_key: {"pull_request": None, "push": {"paths": paths}}}
    assert _paths_blocks(document) == [("push", paths)]


@pytest.mark.parametrize(
    "publication_input",
    [
        "src/culturemech/ingredients/chebi_structures.py",
        "src/culturemech/data/chebi/structure_index.csv",
        "src/culturemech/export/browser_export.py",
        "src/culturemech/templates/media.html.j2",
        "pages/media_growth_review.html",
        "scripts/update_readme_stats.py",
    ],
)
def test_pages_rebuilds_when_publication_inputs_change(publication_input):
    from fnmatch import fnmatchcase

    document = yaml.safe_load((WORKFLOWS / "generate-pages.yaml").read_text())
    triggers = document.get(True, document.get("on"))
    paths = triggers["push"]["paths"]
    assert any(
        fnmatchcase(publication_input, pattern) for pattern in paths
    ), f"Pages stages or reads {publication_input}, but a change cannot trigger its build"


def test_pages_refreshes_shared_claw_inputs_and_checks_published_counts():
    document = yaml.safe_load((WORKFLOWS / "generate-pages.yaml").read_text())
    triggers = document.get(True, document.get("on"))
    assert triggers.get("schedule"), "claw changes need a scheduled Pages refresh"
    steps = document["jobs"]["build"]["steps"]
    stats_check = next(
        i
        for i, step in enumerate(steps)
        if "scripts/update_readme_stats.py --check" in step.get("run", "")
    )
    upload = next(
        i
        for i, step in enumerate(steps)
        if step.get("uses", "").startswith("actions/upload-pages-artifact@")
    )
    assert stats_check < upload
