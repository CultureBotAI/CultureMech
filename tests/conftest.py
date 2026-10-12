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

import json
import math
import sys
from pathlib import Path
from typing import Any

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
NORMALIZED = REPO_ROOT / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

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
    "test_recipe_id_catalog.py",
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
            doc = yaml.load(path.read_text(errors="replace"), Loader=YAML_LOADER)
        except (yaml.YAMLError, OSError):
            continue
        if isinstance(doc, dict):
            out.append((path, doc))
    return out


@pytest.fixture(scope="session")
def corpus_yaml_loader(corpus):
    """Read-only lookup for scripts whose corpus-level tests inject a YAML reader."""
    by_path = dict(corpus)
    return by_path.get


@pytest.fixture
def no_reference_cache_reads(monkeypatch):
    """Independent audits must consume published inputs, not ignored raw caches."""
    original_open = Path.open

    def guarded_open(path, *args, **kwargs):
        if "references_cache" in path.parts:
            pytest.fail(f"Ignored source cache read: {path.name}")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded_open)


@pytest.fixture
def no_workstation_receipt_reads(monkeypatch):
    """Make historical absolute-path dependencies fail on their original workstation too."""
    folder = REPO_ROOT / "reports/ingredient_concentration_curation"
    forbidden = set()
    for cohort in ("20261009-halobacteria-family", "20261009-halobacteria-variants"):
        gate = json.loads((folder / cohort / "validation-preview.json").read_text())
        forbidden.update(Path(row["log"]).resolve() for row in gate["checks"])
    context = json.loads((folder / "20261009-halobacteria-variants/context.json").read_text())
    forbidden.update(
        Path(row["prior_concentration_validation"]).resolve()
        for row in context["records"]
        if "prior_concentration_validation" in row
    )
    original_open = Path.open

    def guarded_open(path, *args, **kwargs):
        if path.resolve() in forbidden:
            pytest.fail(f"Historical workstation receipt read: {path.name}")
        return original_open(path, *args, **kwargs)

    monkeypatch.setattr(Path, "open", guarded_open)


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
_expected_workers: set[str] = set()
_worker_durations: dict[str, dict[str, float]] = {}
_worker_errors: list[str] = []


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session) -> None:  # noqa: ARG001
    _call_durations.clear()
    _expected_workers.clear()
    _worker_durations.clear()
    _worker_errors.clear()


@pytest.hookimpl(optionalhook=True)
def pytest_configure_node(node) -> None:
    _expected_workers.add(node.gateway.id)


@pytest.hookimpl(optionalhook=True)
def pytest_testnodedown(node, error) -> None:
    worker = node.gateway.id
    output = getattr(node, "workeroutput", {})
    receipt = output.get("culturemech_call_durations") if isinstance(output, dict) else None
    if error is not None or worker not in _expected_workers or worker in _worker_durations:
        _worker_errors.append(f"{worker}: failed, unexpected or duplicate worker")
        return
    if not isinstance(receipt, dict) or any(
        not isinstance(nodeid, str)
        or not nodeid
        or type(seconds) is not float
        or not math.isfinite(seconds)
        or seconds < 0
        for nodeid, seconds in receipt.items()
    ):
        _worker_errors.append(f"{worker}: missing or malformed call-duration receipt")
        return
    _worker_durations[worker] = dict(receipt)


def _parallel_durations() -> dict[str, float]:
    """Reconcile final worker receipts with independently forwarded call reports."""
    errors = list(_worker_errors)
    if not _expected_workers or set(_worker_durations) != _expected_workers:
        errors.append("missing worker receipts")
    combined: dict[str, float] = {}
    for receipt in _worker_durations.values():
        if combined.keys() & receipt.keys():
            errors.append("duplicate test call across workers")
        combined.update(receipt)
    if combined != _call_durations:
        errors.append("worker receipts disagree with controller call reports")
    if errors:
        raise ValueError("; ".join(errors))
    return combined


def pytest_runtest_logreport(report) -> None:
    if report.when == "call":
        _call_durations[report.nodeid] = report.duration


def pytest_sessionfinish(session, exitstatus) -> None:  # noqa: ARG001
    # Workers publish explicit receipts. The controller must reconcile them
    # against forwarded reports before it can enforce the same serial budget.
    if hasattr(session.config, "workerinput"):
        session.config.workeroutput["culturemech_call_durations"] = dict(_call_durations)
        return
    durations = _call_durations
    if session.config.pluginmanager.hasplugin("xdist") and getattr(
        session.config.option, "numprocesses", None
    ):
        try:
            durations = _parallel_durations()
        except ValueError as exc:
            print(f"\nSLOW-TEST BUDGET INCOMPLETE: {exc}")
            session.exitstatus = 1
            return
        print(
            f"\nValidated call timings for {len(durations)} tests across "
            f"{len(_worker_durations)} workers."
        )
    over = {
        nodeid: seconds
        for nodeid, seconds in durations.items()
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
