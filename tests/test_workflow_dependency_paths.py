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
    assert len(blocks) >= 8, f"expected the known path-filtered blocks, found {len(blocks)}"
    assert len(_workflow_files()) >= 10, "workflow discovery found almost nothing"
    assert {w for w, _, _ in blocks} >= {
        "chebi-consistency.yaml",
        "concentration-plausibility.yaml",
        "curation-history.yaml",
        "label-correspondence.yaml",
        "validate-strict.yaml",
    }
