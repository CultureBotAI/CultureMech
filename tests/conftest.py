"""Shared fixtures — chiefly one parse of the corpus for the whole session.

Several corpus-level guards each walked `data/normalized_yaml/**` independently,
parsing ~15,900 YAML files per test. Four of them cost ~105s apiece locally, which
is roughly 7 minutes of a 10-minute suite spent re-reading the same files — and in
CI that was enough to hit the 40-minute job timeout and cancel the run.

Raising the timeout would have hidden it; the cost is real and grows with every
guard added. A session-scoped parse pays it once.

Use `corpus` (every record) or `media_records` (media only, stock solutions
excluded) instead of writing another `rglob`. The dicts are shared, so **treat
them as read-only** — mutating one would leak into every later test.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
NORMALIZED = REPO_ROOT / "data" / "normalized_yaml"

sys.path.insert(0, str(REPO_ROOT / "scripts"))

CORPUS_TEST_FILES = {
    "test_composition_type.py",
    "test_concentration_plausibility.py",
    "test_corpus_grounding_agreement.py",
    "test_dataclasses_current.py",
    "test_derived_artifacts.py",
    "test_grounding_hydration_agreement.py",
    "test_id_registry.py",
    "test_media_variant_links.py",
    "test_medium_type_consistency.py",
    "test_merge_yaml_freshness.py",
    "test_name_term_elements.py",
    "test_recipe_indexes.py",
    "test_record_io.py",
    "test_record_kinds.py",
    "test_ranking_duplicates.py",
    "test_researched_manifest.py",
    "test_sssom_generation.py",
}
INTEGRATION_TEST_FILES = {"test_kg_microbe_integration.py"}


def pytest_collection_modifyitems(items) -> None:
    """Assign every test to exactly one documented execution tier."""
    corpus_source_cache: dict[Path, bool] = {}
    for item in items:
        if item.path not in corpus_source_cache:
            corpus_source_cache[item.path] = any(
                token in item.path.read_text(errors="replace")
                for token in ("data/normalized_yaml", "data/merge_yaml")
            )
        module_uses_corpus = corpus_source_cache[item.path]
        if (
            item.get_closest_marker("integration")
            or item.path.name in INTEGRATION_TEST_FILES
            or "Integration" in item.nodeid
        ):
            item.add_marker(pytest.mark.integration)
        elif (
            item.get_closest_marker("corpus")
            or item.path.name in CORPUS_TEST_FILES
            or module_uses_corpus
            or {"corpus", "media_records"}.intersection(item.fixturenames)
        ):
            item.add_marker(pytest.mark.corpus)
        else:
            item.add_marker(pytest.mark.fast)


@pytest.fixture(scope="session")
def corpus() -> list[tuple[Path, dict[str, Any]]]:
    """Every parseable record under data/normalized_yaml, parsed once per session."""
    out: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(NORMALIZED.rglob("*.yaml")):
        try:
            doc = yaml.safe_load(path.read_text(errors="replace"))
        except (yaml.YAMLError, OSError):
            continue
        if isinstance(doc, dict):
            out.append((path, doc))
    return out


@pytest.fixture(scope="session")
def media_records(corpus) -> list[tuple[Path, dict[str, Any]]]:
    """Media only — stock-solution records excluded, as every guard wants (#124)."""
    from record_kinds import is_solution_record

    return [(p, d) for p, d in corpus if not is_solution_record(d)]


# --- slow-test budget (#191) -------------------------------------------------
#
# The corpus-rescan bug has now recurred four times: #189 fixed five tests that
# each re-parsed ~15,900 records, and two MORE were then added in #199 and #202,
# at 328s and 421s. The suite went 317s -> 1459s and CI from ~16 to ~34 minutes.
#
# A ban on `rglob("*.yaml")` in tests would be the wrong guard. Measured, globbing
# is cheap — the path-only globs in test_recipe_indexes and test_id_registry cost
# 0.17-0.35s. What is expensive is PARSING, and the worst offenders reached it by
# calling a script function, not by globbing. So the budget is on time, which is
# the thing that actually hurts, regardless of how a test gets there.
#
# Only `call` duration is measured. `setup` is dominated by the session-scoped
# corpus fixture, which is paid once for the whole run and is the fix rather than
# the problem.

# 120s, and the allowlist is deliberately EMPTY.
#
# The slowest call after this fix is ~66s (the prioritizer-based tests), and CI
# runs roughly 1.4x slower than local, which puts them near 90s there. So 90 would
# have needed three exemptions for tests that are not actually a problem — and a
# standing exemption is precisely what hides the next regression. One number, no
# entries, still catching the 328s and 421s cases that motivated this by a wide
# margin.
#
# If a test genuinely needs more, add it here WITH the reason. An entry should
# feel like a decision, not a mute button.
SLOW_TEST_BUDGET_S = 120.0

SLOW_TEST_ALLOWLIST: dict[str, str] = {}

_call_durations: dict[str, float] = {}


def pytest_runtest_logreport(report) -> None:
    if report.when == "call":
        _call_durations[report.nodeid] = report.duration


def pytest_sessionfinish(session, exitstatus) -> None:  # noqa: ARG001
    # Under pytest-xdist each worker holds its own `_call_durations`, and the
    # CONTROLLER's copy is empty — so this check would pass unconditionally while
    # appearing to run. xdist is not installed today, but `-n auto` is the obvious
    # response to a slow suite, and silently losing the guard is the exact failure
    # class it exists to prevent. Fail loudly instead (#213).
    if hasattr(session.config, "workerinput"):
        return  # a worker; the controller does the reporting
    if session.config.pluginmanager.hasplugin("xdist") and getattr(
        session.config.option, "numprocesses", None
    ):
        print(
            "\nSLOW-TEST BUDGET DISABLED: running under pytest-xdist, where "
            "per-worker durations never reach the controller. See #213."
        )
        session.exitstatus = 1
        return
    over = {
        nodeid: seconds
        for nodeid, seconds in _call_durations.items()
        if seconds > SLOW_TEST_BUDGET_S and nodeid not in SLOW_TEST_ALLOWLIST
    }
    if not over:
        return
    print("\n" + "=" * 72)
    print(f"SLOW TESTS: {len(over)} exceeded the {SLOW_TEST_BUDGET_S:.0f}s call budget")
    for nodeid, seconds in sorted(over.items(), key=lambda kv: -kv[1]):
        print(f"  {seconds:7.1f}s  {nodeid}")
    print("\nUse the session-scoped `corpus` / `media_records` fixtures instead of")
    print("re-parsing, or add an entry to SLOW_TEST_ALLOWLIST in tests/conftest.py")
    print("with the reason the cost is irreducible.")
    print("=" * 72)
    session.exitstatus = 1
