"""A merged duplicate must never invent a quantity (#394).

`cleanup_media_quality.py` collapsed duplicate ingredient rows by ADDING their
concentrations. It wrote `Agar 50.0 g/L` from `15.0, 15.0, 20.0` in 186 records
— agar sets at 15-20 g/L, so those media cannot pour — and `Methanol 1584.0
g/L` from `792.0, 792.0`, which is above the density of methanol. 4,503 rows
corpus-wide carried a summed value and no gate looked at any of them.

The repair is only defensible where every merged part is the same value. These
tests pin both halves: that the unambiguous case is collapsed, and that the
ambiguous one is refused rather than guessed.

Every literal is copied from a real record.
"""

from __future__ import annotations

from decimal import Decimal

import pytest
from audit_merged_duplicates import classify, merged_parts
from repair_merged_duplicates import repair_ingredient, repair_record


def summed(name: str, value: str, parts: str, note_prefix: str = "") -> dict:
    return {
        "preferred_term": name,
        "concentration": {"value": value, "unit": "G_PER_L"},
        "notes": f"{note_prefix} [Merged {len(parts.split(','))} duplicates: {parts}]",
    }


# --- reading the note ----------------------------------------------------


def test_the_parts_are_recovered_from_the_note():
    assert merged_parts(" (for solid medium) [Merged 3 duplicates: 15.0, 15.0, 20.0]") == [
        Decimal("15.0"),
        Decimal("15.0"),
        Decimal("20.0"),
    ]


def test_a_row_with_no_merge_note_is_not_a_merge():
    assert merged_parts("Solidifying agent (for TSA only)") is None
    assert merged_parts(None) is None
    assert merged_parts("") is None


def test_the_collapsed_note_is_also_recognised():
    """So a repaired row is still identifiable as having been merged."""
    assert merged_parts("[Collapsed 2 identical duplicates: 100.0, 100.0]") == [
        Decimal("100.0"),
        Decimal("100.0"),
    ]


# --- classification ------------------------------------------------------


def test_a_sum_of_identical_parts_is_mechanically_repairable():
    finding, parts = classify(summed("Methanol", "1584.0", "792.0, 792.0"))
    assert finding == "IDENTICAL_PARTS"
    assert parts == [Decimal("792.0"), Decimal("792.0")]


def test_a_sum_of_differing_parts_needs_curation():
    finding, _ = classify(summed("Agar", "50.0", "15.0, 15.0, 20.0", " (for solid medium)"))
    assert finding == "DIFFERING_PARTS"


def test_a_value_that_is_not_the_sum_is_not_reported():
    """A repaired row holds one part, not the total, so it stops being a finding."""
    assert classify(summed("Methanol", "792.0", "792.0, 792.0")) is None


def test_a_single_part_is_not_a_merge():
    assert classify(summed("NaCl", "5.0", "5.0")) is None


def test_a_non_numeric_concentration_does_not_raise():
    row = summed("NaCl", "variable", "1.0, 1.0")
    assert classify(row) is None


# --- the repair ----------------------------------------------------------


def test_the_unambiguous_case_collapses_to_the_one_distinct_value():
    row = summed("Sodium phosphate buffer", "200.0", "100.0, 100.0")
    assert repair_ingredient(row) == ("200.0", "100.0")
    assert row["concentration"] == {"value": "100.0", "unit": "G_PER_L"}


def test_the_ambiguous_case_is_refused_not_guessed():
    """15 or 20 is a question about the source recipe. Arithmetic cannot answer it."""
    row = summed("Agar", "50.0", "15.0, 15.0, 20.0", " (for solid medium)")
    before = dict(row["concentration"])

    assert repair_ingredient(row) is None
    assert row["concentration"] == before, "the ambiguous row was modified"
    assert "Merged" in row["notes"], "the evidence was rewritten without a repair"


def test_the_note_records_the_collapse_and_keeps_the_parts():
    row = summed("Methanol", "1584.0", "792.0, 792.0")
    repair_ingredient(row)
    assert row["notes"] == "[Collapsed 2 identical duplicates: 792.0, 792.0]"
    assert classify(row) is None, "a repaired row must stop being a finding"


def test_a_prefix_note_survives_the_rewrite():
    row = summed("Agar", "30.0", "15.0, 15.0", " (for solid medium)")
    repair_ingredient(row)
    assert row["notes"].startswith("(for solid medium)")
    assert "Collapsed 2 identical duplicates" in row["notes"]


def test_repairing_is_idempotent():
    row = summed("Methanol", "1584.0", "792.0, 792.0")
    assert repair_ingredient(row) is not None
    assert repair_ingredient(row) is None


def test_nested_solution_composition_is_repaired_too():
    record = {
        "solutions": [
            {
                "preferred_term": "Trace elements",
                "composition": [summed("NaCl", "10.0", "5.0, 5.0")],
            }
        ]
    }
    changed = repair_record(record)
    assert changed == [("NaCl", "10.0", "5.0")]
    assert record["solutions"][0]["composition"][0]["concentration"]["value"] == "5.0"


def test_a_record_with_nothing_to_repair_is_untouched():
    record = {"ingredients": [{"preferred_term": "NaCl", "concentration": {"value": "5.0"}}]}
    assert repair_record(record) == []


@pytest.mark.parametrize("bad", [None, "x", 42, []])
def test_merged_parts_tolerates_junk(bad):
    assert merged_parts(bad) is None


# --- the mutator that caused it -----------------------------------------


def _fixer():
    from cleanup_media_quality import MediaQualityFixer

    return MediaQualityFixer()


def _row(name: str, value: str) -> dict:
    return {"preferred_term": name, "concentration": {"value": value, "unit": "G_PER_L"}}


def test_the_mutator_no_longer_sums_disagreeing_duplicates():
    """The defect itself. `15.0 + 15.0 + 20.0 = 50.0` reached 186 records."""
    base, warning = _fixer()._merge_ingredient_group(
        [_row("Agar", "15.0"), _row("Agar", "15.0"), _row("Agar", "20.0")]
    )

    assert base["concentration"]["value"] != "50.0", "the merge summed again"
    assert base["concentration"]["value"] == "15.0", "it should keep the first, not compute"
    assert warning is not None, "a disagreement must be reported, not resolved silently"
    assert "needs curation" in base["notes"]


def test_the_mutator_still_collapses_identical_duplicates():
    """Collapsing is the correct operation when every duplicate agrees."""
    base, warning = _fixer()._merge_ingredient_group(
        [_row("Sodium phosphate buffer", "100.0"), _row("Sodium phosphate buffer", "100.0")]
    )

    assert base["concentration"]["value"] == "100.0"
    assert warning is None
    assert "Collapsed 2 identical duplicates" in base["notes"]


def test_a_collapse_the_mutator_writes_is_not_a_finding():
    """The mutator and the audit have to agree, or the gate reports its own output."""
    base, _ = _fixer()._merge_ingredient_group([_row("NaCl", "5.0"), _row("NaCl", "5.0")])
    assert classify(base) is None


# --- repeated rows with no merge note (#283) ----------------------------


def _scan_one(record: dict) -> dict:
    """Findings for a single in-memory record, keyed by finding name."""
    from collections import Counter, defaultdict

    from audit_merged_duplicates import _collect

    rows: list[dict] = []
    stats: Counter = Counter()
    by_name: dict = defaultdict(list)
    merged: set = set()
    for section in ("ingredients", "solutions"):
        _collect(record.get(section), by_name, merged, rows, stats, "x.yaml", "CultureMech:1")
    # mirror scan()'s per-record pass
    from audit_merged_duplicates import _decimal

    out = Counter(stats)
    for key in sorted(by_name):
        if key in merged or len(by_name[key]) < 2:
            continue
        numeric = [
            v
            for v in (_decimal((i.get("concentration") or {}).get("value")) for i in by_name[key])
            if v is not None and v > 0
        ]
        if len(numeric) >= 2:
            out["REPEATED_INGREDIENT"] += 1
    return out


def test_the_ucm_shape_is_caught_without_a_merge_note():
    """#283: `ucm.yaml` lists trace elements twice, 1000x apart, and never merged."""
    record = {
        "ingredients": [
            {"preferred_term": "As2O3", "concentration": {"value": "0.000093", "unit": "G_PER_L"}},
            {"preferred_term": "As2O3", "concentration": {"value": "0.093", "unit": "G_PER_L"}},
        ]
    }
    assert _scan_one(record)["REPEATED_INGREDIENT"] == 1


def test_an_exact_duplicate_is_caught_too():
    """`NaOH 4.0` twice has no ratio to notice, and is still redundancy."""
    record = {
        "ingredients": [
            {"preferred_term": "NaOH", "concentration": {"value": "4.0", "unit": "G_PER_L"}},
            {"preferred_term": "NaOH", "concentration": {"value": "4.0", "unit": "G_PER_L"}},
        ]
    }
    assert _scan_one(record)["REPEATED_INGREDIENT"] == 1


def test_the_same_name_in_different_units_is_not_a_repeat():
    """Two units are two different claims, not a duplicated one."""
    record = {
        "ingredients": [
            {"preferred_term": "NaCl", "concentration": {"value": "5.0", "unit": "G_PER_L"}},
            {"preferred_term": "NaCl", "concentration": {"value": "5.0", "unit": "MILLIMOLAR"}},
        ]
    }
    assert _scan_one(record)["REPEATED_INGREDIENT"] == 0


def test_a_single_row_is_not_a_repeat():
    record = {
        "ingredients": [
            {"preferred_term": "NaCl", "concentration": {"value": "5.0", "unit": "G_PER_L"}}
        ]
    }
    assert _scan_one(record)["REPEATED_INGREDIENT"] == 0


def test_a_merged_row_is_not_double_reported():
    """A row with a merge note belongs to COEXISTING_ROW, not REPEATED_INGREDIENT."""
    record = {
        "ingredients": [
            summed("Agar", "50.0", "15.0, 15.0, 20.0"),
            {"preferred_term": "Agar", "concentration": {"value": "15.0", "unit": "G_PER_L"}},
        ]
    }
    assert _scan_one(record)["REPEATED_INGREDIENT"] == 0
