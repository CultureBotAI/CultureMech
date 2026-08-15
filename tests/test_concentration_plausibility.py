"""Tests for the concentration-plausibility audit (#118).

The risk with a magnitude heuristic is both directions: too loose and it misses
the stock-solution values that motivated the issue; too tight and it drowns a
curator in false positives on legitimately concentrated media. These tests pin
the three confirmed real-world cases from #118 as must-detect, and pin ordinary
final-medium concentrations as must-not-detect.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def acp():
    return _load("audit_concentration_plausibility")


@pytest.fixture(scope="module")
def corpus_findings(acp, media_records):
    """One full-corpus audit shared by the corpus-level tests.

    `audit()` parses ~11,000 YAML records; at ~90s a call, running it per test
    pushed the CI suite past its 20-minute timeout. Module scope keeps the
    coverage and pays for the walk once.
    """
    return acp.audit_parsed(media_records)


def _ing(name, value, unit="G_PER_L", ident=None):
    return {"preferred_term": name, "term": ({"id": ident} if ident else None),
            "concentration": {"value": value, "unit": unit}}


# --- must detect: the confirmed cases from #118 ---------------------------


def test_water_at_preparation_volume(acp):
    """sulfolobus_medium_for_dsm_9790 carries 'Distilled water 2000 G_PER_L'."""
    hit = acp.check_ingredient(_ing("Distilled water", "2000", ident="CHEBI:15377"))
    assert hit and hit[0] == "WATER_AS_VOLUME"


@pytest.mark.parametrize("name,value", [
    ("MnCl2 x 4 H2O", "180"),
    ("Na2B4O7 x 10 H2O", "450"),
    ("ZnSO4 x 7 H2O", "22"),
    ("CuCl2 x 2 H2O", "5"),
    ("Na2MoO4 x 2 H2O", "3"),
])
def test_trace_salts_at_stock_magnitude(acp, name, value):
    hit = acp.check_ingredient(_ing(name, value))
    assert hit and hit[0] == "TRACE_SALT_AS_STOCK", f"{name} {value} not flagged"


def test_resazurin_unit_slip(acp):
    """TOGO_M1796_Desulfovibrio_medium stores Resazurin at 1 G_PER_L (~1000x)."""
    hit = acp.check_ingredient(_ing("Resazurin", "1"))
    assert hit and hit[0] == "INDICATOR_UNIT_SLIP"


# --- must NOT detect: ordinary final-medium values ------------------------


@pytest.mark.parametrize("name,value", [
    ("NaCl", "10"),               # bulk salt, ordinary
    ("Glucose", "20"),            # carbon source
    ("Yeast extract", "5"),
    ("Agar", "15"),
    ("Distilled water", "1"),     # implausible in another way, but not a volume
    ("MgSO4 x 7 H2O", "0.5"),     # not a trace element
])
def test_ordinary_concentrations_are_not_flagged(acp, name, value):
    assert acp.check_ingredient(_ing(name, value)) is None


def test_trace_salt_below_threshold_is_not_flagged(acp):
    """Trace elements at genuine final-medium magnitude must pass."""
    assert acp.check_ingredient(_ing("MnCl2 x 4 H2O", "0.005")) is None


def test_vitamin_at_final_medium_magnitude_is_not_flagged(acp):
    assert acp.check_ingredient(_ing("Biotin", "0.00002")) is None


def test_non_gpl_units_are_out_of_scope(acp):
    """Only G_PER_L is checked; a molar-basis check needs molecular weights."""
    assert acp.check_ingredient(_ing("Resazurin", "1", unit="MG_PER_L")) is None
    assert acp.check_ingredient(_ing("MnCl2", "180", unit="MILLIMOLAR")) is None


def test_unparseable_and_nonpositive_values_are_skipped(acp):
    assert acp.check_ingredient(_ing("Resazurin", "n/a")) is None
    assert acp.check_ingredient(_ing("Resazurin", None)) is None
    assert acp.check_ingredient(_ing("Resazurin", "0")) is None


def test_hydrate_suffix_does_not_defeat_matching(acp):
    """Labels arrive with several hydrate separators."""
    for label in ("MnCl2·4H2O", "MnCl2 x 4 H2O", "MnCl2・4H2O", "MnCl2"):
        hit = acp.check_ingredient(_ing(label, "180"))
        assert hit and hit[0] == "TRACE_SALT_AS_STOCK", label


# --- cocktail roll-up -----------------------------------------------------


def test_flattened_cocktail_requires_no_solutions_block(acp, tmp_path):
    """A record that already nests its stock under `solutions:` is correct."""
    rec = tmp_path / "bacterial"
    rec.mkdir()
    import yaml
    (rec / "x.yaml").write_text(yaml.dump({
        "id": "CultureMech:1", "solutions": [{"preferred_term": "vitamins"}],
        "ingredients": [],
    }))
    rows = [{"finding": "INDICATOR_UNIT_SLIP", "file_path": "bacterial/x.yaml",
             "record_id": "CultureMech:1"} for _ in range(5)]
    [summary] = acp.summarize_records(rows, tmp_path)
    assert summary["has_solutions_block"] == "yes"
    assert summary["flattened_cocktail"] == "no"


def test_flattened_cocktail_detected_without_solutions_block(acp, tmp_path):
    rec = tmp_path / "bacterial"
    rec.mkdir()
    import yaml
    (rec / "y.yaml").write_text(yaml.dump({"id": "CultureMech:2", "ingredients": []}))
    rows = [{"finding": "INDICATOR_UNIT_SLIP", "file_path": "bacterial/y.yaml",
             "record_id": "CultureMech:2"} for _ in range(3)]
    [summary] = acp.summarize_records(rows, tmp_path)
    assert summary["flattened_cocktail"] == "yes"


def test_single_flagged_row_is_not_a_cocktail(acp, tmp_path):
    rec = tmp_path / "bacterial"
    rec.mkdir()
    import yaml
    (rec / "z.yaml").write_text(yaml.dump({"id": "CultureMech:3", "ingredients": []}))
    rows = [{"finding": "INDICATOR_UNIT_SLIP", "file_path": "bacterial/z.yaml",
             "record_id": "CultureMech:3"}]
    [summary] = acp.summarize_records(rows, tmp_path)
    assert summary["flattened_cocktail"] == "no"


# --- corpus ---------------------------------------------------------------


def test_the_three_records_named_in_issue_118_are_flagged(corpus_findings):
    """Regression: the cases that motivated the issue must stay detected."""
    flagged = {r["file_path"] for r in corpus_findings}
    for expected in (
        "archaea/sulfolobus_medium_for_dsm_9790.yaml",
        "bacterial/TOGO_M1791_Pelobacter_acetylenicus_Medium.yaml",
        "bacterial/TOGO_M1796_Desulfovibrio_medium.yaml",
    ):
        assert expected in flagged, f"{expected} no longer flagged"


def test_stock_solution_records_are_excluded(corpus_findings):
    """High magnitudes are correct in a stock-solution record by definition.

    Without this exclusion the audit would flag thousands of the ~4,784 MediaDive
    solution records that live in bacterial/ (#124).
    """
    import yaml as _yaml
    from record_kinds import is_solution_record

    normalized = REPO_ROOT / "data" / "normalized_yaml"
    # Distinct records only — the row list repeats a file once per flagged row.
    for file_path in sorted({r["file_path"] for r in corpus_findings})[:400]:
        doc = _yaml.safe_load((normalized / file_path).read_text())
        assert not is_solution_record(doc), f"solution record flagged: {file_path}"


CONCENTRATION_BACKLOG_BASELINE = 9_750
# The sharper baseline (#150): a raw row count drifts with corpus size, whereas a
# new flattened cocktail is a specific defect shape an import has reintroduced.
COCKTAIL_BASELINE = 185


def test_implausible_row_count_does_not_exceed_the_known_backlog(corpus_findings):
    """Gate NEW implausible concentrations without blocking on the backlog (#150).

    #135 shipped the audit; the repair is now partly done — #150 nested 135
    flattened cocktails from MediaDive data, taking the backlog from 11,540 rows
    across 3,914 records to 10,244 across 3,621. A guard demanding zero would fail
    immediately and be switched off — the #129 lesson about wiring a gate to a red
    suite. So this baselines at the current count, exactly as
    `check-chebi-grounding --max-allowed 101` does for grounding.

    LOWER this number as records are repaired. Raising it to make a run pass is
    the one move that defeats the purpose: it would let a fresh import land the
    same defect shape that #118 documented and #135 measured.
    """
    assert len(corpus_findings) <= CONCENTRATION_BACKLOG_BASELINE, (
        f"{len(corpus_findings)} implausible concentration rows exceeds the baseline "
        f"{CONCENTRATION_BACKLOG_BASELINE}. Something new introduced rows beyond the "
        f"known backlog — see data/import_tracking/reports/concentration_plausibility.tsv. "
        f"Do NOT raise the baseline to make this pass."
    )


def test_the_baseline_is_not_far_above_reality(corpus_findings):
    """A baseline left far above the real count silently stops gating.

    If the backlog is repaired but the number here is not lowered, this test keeps
    passing while permitting thousands of new defects. Fails once the gap exceeds
    10%, prompting the baseline to be tightened.
    """
    actual = len(corpus_findings)
    slack = CONCENTRATION_BACKLOG_BASELINE - actual
    assert slack <= CONCENTRATION_BACKLOG_BASELINE * 0.10, (
        f"baseline {CONCENTRATION_BACKLOG_BASELINE} is {slack} above the actual "
        f"{actual}; lower it to {actual} so the gate keeps biting"
    )


def test_justfile_baseline_matches_the_test_baseline():
    """Two hardcoded copies of a number that is meant to change is a drift bug (#170).

    The baseline lives in `project.justfile` (so `just
    audit-concentration-plausibility` gates outside pytest) and here (so CI gates
    without invoking just). Both must be lowered together as the backlog is
    repaired. Miss one and either the gate stops biting or local runs fail while
    CI passes — the same drift class as #144 and #157, which is why this asserts
    rather than trusts.
    """
    import re

    justfile = (REPO_ROOT / "project.justfile").read_text()
    block = justfile.split("audit-concentration-plausibility", 1)[1][:400]
    match = re.search(r"--max-allowed\s+(\d+)", block)
    assert match, "the recipe no longer passes --max-allowed; it has stopped gating"
    assert int(match.group(1)) == CONCENTRATION_BACKLOG_BASELINE, (
        f"project.justfile gates at {match.group(1)} but this file baselines at "
        f"{CONCENTRATION_BACKLOG_BASELINE}; lower both together"
    )


# --- the prevention gate (#150) ---------------------------------------------


def test_the_cocktail_baseline_matches_the_justfile(acp):
    """Same drift guard as the row baseline: two copies of a number meant to
    change must be lowered together (#170)."""
    import re
    justfile = (REPO_ROOT / "project.justfile").read_text()
    block = justfile.split("audit-concentration-plausibility", 1)[1][:400]
    match = re.search(r"--max-cocktails\s+(\d+)", block)
    assert match, "the recipe no longer passes --max-cocktails; the sharper gate is off"
    assert int(match.group(1)) == COCKTAIL_BASELINE, (
        f"justfile gates cocktails at {match.group(1)} but this file baselines at "
        f"{COCKTAIL_BASELINE}; lower both together")


def test_the_gate_baselines_match_the_current_corpus(acp, media_records):
    """#118 asked for an audit AND a repair; #135 shipped the audit, and nothing
    stopped the defect being reintroduced for another 15 issues.

    These baselines hold the line while the 3,621-record backlog is worked
    through. They must track the corpus: a baseline above the real count is a gate
    that cannot fail.
    """
    rows = acp.audit_parsed(media_records)
    rows_baseline = CONCENTRATION_BACKLOG_BASELINE
    assert len(rows) <= rows_baseline, (
        f"{len(rows)} rows exceeds the gate baseline {rows_baseline}")
    # A baseline far above the real count cannot fail, which is worse than no gate.
    assert rows_baseline - len(rows) <= 200, (
        f"gate baseline {rows_baseline} is {rows_baseline - len(rows)} above the "
        "actual count — tighten it or it will never fire")

    # The COCKTAIL baseline is the sharper gate, so it needs the same anti-vacuous
    # guard, not just `> 0` (#221): as the cocktail backlog is repaired the real
    # count drops, and a baseline left far above it silently stops being able to
    # fire. Counted in memory from `rows` + the fixture docs — calling
    # summarize_records re-reads the flagged files and blew the slow-test budget on
    # CI (193s). The cocktail rule mirrors summarize_records: no `solutions:` block
    # and >= COCKTAIL_MIN_ROWS indicator OR trace rows.
    from collections import Counter
    has_solutions = {str(p.relative_to(acp.NORMALIZED)): bool(d.get("solutions"))
                     for p, d in media_records}
    per_record: dict[str, Counter] = {}
    for r in rows:
        per_record.setdefault(r["file_path"], Counter())[r["finding"]] += 1
    cocktails = sum(
        1 for fp, c in per_record.items()
        if not has_solutions.get(fp, False)
        and (c["INDICATOR_UNIT_SLIP"] >= acp.COCKTAIL_MIN_ROWS
             or c["TRACE_SALT_AS_STOCK"] >= acp.COCKTAIL_MIN_ROWS))
    assert cocktails <= COCKTAIL_BASELINE, (
        f"{cocktails} flattened cocktails exceeds the baseline {COCKTAIL_BASELINE}")
    assert COCKTAIL_BASELINE - cocktails <= 50, (
        f"cocktail baseline {COCKTAIL_BASELINE} is {COCKTAIL_BASELINE - cocktails} "
        f"above the actual {cocktails} — tighten it or it will never fire")


def test_the_gate_is_wired_into_ci():
    """A --max-allowed flag nobody runs is not a gate. The audit carried one for
    15 issues without ever being invoked."""
    wf = REPO_ROOT / ".github" / "workflows" / "concentration-plausibility.yaml"
    assert wf.is_file(), "no workflow runs the plausibility gate"
    text = wf.read_text()
    assert "just audit-concentration-plausibility" in text
    assert "data/normalized_yaml/**" in text, "gate not triggered by corpus edits"
