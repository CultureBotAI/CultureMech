"""Guard that composition_type does not contradict the ingredient list (#158).

`MediumCompositionTypeEnum.DEFINED` means "every component and its exact quantity
is known". 285 records asserted it while listing yeast extract, peptone or
tryptone — chemically undefined by definition.

Only one direction is testable, and the asymmetry is the whole design:

  * containing "yeast extract" **proves** a record is not DEFINED.
  * containing none of the recognised names proves **nothing** — the list is
    finite, and an unrecognised extract simply is not matched.

So the corpus assertion below is one-directional. The 1,894 UNDEFINED records with
no recognised undefined component are not evidence of anything and are not
asserted on.
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
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def act():
    return _load("audit_composition_type")


def _ing(name, value=None, unit="G_PER_L"):
    d = {"preferred_term": name}
    if value is not None:
        d["concentration"] = {"value": value, "unit": unit}
    return d


# --- component detection --------------------------------------------------


@pytest.mark.parametrize("name", [
    "Yeast extract", "yeast extract", "Peptone", "Tryptone", "Casamino acids",
    "Beef extract", "Meat extract", "Malt extract", "Proteose peptone",
    "Brain-heart infusion", "Casein hydrolysate", "Soytone", "Trypticase peptone",
])
def test_undefined_components_are_detected(act, name):
    assert act.undefined_components({"ingredients": [_ing(name, "5")]}), name


@pytest.mark.parametrize("name", [
    "Glucose", "NaCl", "Agar", "MgSO4 x 7 H2O", "Distilled water",
    "Ammonium sulfate", "Sodium molybdate",
])
def test_defined_chemicals_are_not_flagged(act, name):
    """False positives here would restamp correctly-DEFINED media."""
    assert not act.undefined_components({"ingredients": [_ing(name, "5")]})


def test_malformed_ingredients_do_not_crash(act):
    doc = {"ingredients": [_ing("Yeast extract", "5"), "not-a-dict", None]}
    assert len(act.undefined_components(doc)) == 1


# --- mass, which decides UNDEFINED vs SEMI_DEFINED ------------------------


def test_mass_sums_the_undefined_components(act):
    ings = [_ing("Peptone", "5"), _ing("Yeast extract", "3")]
    assert act.undefined_mass(ings) == 8.0


def test_unquantified_component_yields_none_not_a_partial_sum(act):
    """Guessing low here would silently restamp a record on incomplete data."""
    ings = [_ing("Peptone", "5"), _ing("Yeast extract")]
    assert act.undefined_mass(ings) is None


def test_non_gpl_unit_yields_none(act):
    assert act.undefined_mass([_ing("Yeast extract", "500", "MG_PER_L")]) is None


def test_unparseable_value_yields_none(act):
    assert act.undefined_mass([_ing("Yeast extract", "trace")]) is None


# --- restamp is surgical --------------------------------------------------


def test_restamp_changes_only_the_composition_type_line(act, tmp_path):
    p = tmp_path / "r.yaml"
    p.write_text("id: CultureMech:1\ncomposition_type: DEFINED\nname: x\n"
                 "notes: 'mentions composition_type: DEFINED in prose'\n")
    assert act.restamp(p, "UNDEFINED")
    lines = p.read_text().splitlines()
    assert lines[1] == "composition_type: UNDEFINED"
    assert lines[3].endswith("in prose'"), "prose mentioning the slot must be untouched"


def test_restamp_reports_false_when_slot_absent(act, tmp_path):
    p = tmp_path / "r.yaml"
    p.write_text("id: CultureMech:1\nname: x\n")
    assert act.restamp(p, "UNDEFINED") is False


# --- the corpus -----------------------------------------------------------


def test_no_defined_record_carries_a_bulk_undefined_component(act):
    """One-directional by design — see the module docstring.

    The threshold matches the repair: at >= 5 g/L, no reading of SEMI_DEFINED's
    "a small amount" applies, so DEFINED is unambiguously wrong.
    """
    offenders = [
        (r["file_path"], r["undefined_g_per_l"])
        for r in act.audit()
        if r["_mass"] is not None and r["_mass"] >= act.DEFAULT_THRESHOLD
    ]
    assert not offenders, (
        f"{len(offenders)} record(s) assert composition_type: DEFINED while carrying "
        f">= {act.DEFAULT_THRESHOLD:g} g/L of chemically undefined components "
        f"(e.g. {offenders[:3]}) — run `just audit-composition-type --apply`"
    )


def test_medium_type_and_composition_type_do_not_contradict():
    """The deprecated slot must not disagree with the live one (#165).

    `medium_type` is deprecated and #154 removed its last reader, but it is still
    present on 11,092 records and still schema-valid, so a reader could pick it
    up. Restamping only `composition_type` in #164 broke this invariant on 239
    records — 0 disagreements before, 239 after — which is how this test came to
    exist.

    Mapping is the schema's own: `composition_type: UNDEFINED` "replaces the
    deprecated MediumTypeEnum value COMPLEX".

    Dropping `medium_type` from the corpus entirely is the better long-term fix
    and is tracked in #165; this only holds the line until then.
    """
    import yaml as _yaml
    from record_kinds import is_solution_record

    # The deprecated vocabulary is COARSER than the live one: it has no
    # SEMI_DEFINED. A record that is SEMI_DEFINED today was legitimately COMPLEX
    # under the old single-axis enum, because COMPLEX meant "contains an undefined
    # component" and a SEMI_DEFINED medium does. So COMPLEX maps to a SET.
    #
    # This widened after #152 promoted 612 records to SEMI_DEFINED and this test
    # failed — the mapping was too strict once a third value became populated, not
    # the data. DEFINED stays one-to-one: it still means "no undefined component",
    # so it cannot legitimately pair with either of the others.
    expect = {"COMPLEX": {"UNDEFINED", "SEMI_DEFINED"}, "DEFINED": {"DEFINED"}}
    bad = []
    for path in (REPO_ROOT / "data" / "normalized_yaml").rglob("*.yaml"):
        doc = _yaml.safe_load(path.read_text(errors="replace"))
        if not isinstance(doc, dict) or is_solution_record(doc):
            continue
        mt, ct = doc.get("medium_type"), doc.get("composition_type")
        if mt is None or ct is None:
            continue
        if str(ct) not in expect.get(str(mt), {str(mt)}):
            bad.append(f"{path.name}: medium_type={mt} composition_type={ct}")
    assert not bad, (
        f"{len(bad)} record(s) have a deprecated medium_type contradicting "
        f"composition_type (e.g. {bad[:3]}) — see #165"
    )


# --- SEMI_DEFINED promotion (#152) ----------------------------------------


def _grounded(name, value):
    return {"preferred_term": name, "term": {"id": "CHEBI:12345"},
            "concentration": {"value": value, "unit": "G_PER_L"}}


def test_semi_defined_accepts_a_defined_base_with_a_trace_of_yeast_extract(act):
    """The enum's own example, and the real shape: mineral salts + trace extract."""
    doc = {"ingredients": [_grounded("NaCl", "5"), _grounded("MgSO4", "1"),
                           _ing("Yeast extract", "0.1")]}
    ok, why = act.semi_defined_candidate(doc)
    assert ok, why


def test_semi_defined_rejects_an_ungrounded_other_ingredient(act):
    """'Predominantly defined' must be EVIDENCED, not inferred from absence.

    The word list is finite, so an unmatched ingredient may be an unrecognised
    extract. Requiring CHEBI grounding on the others is positive evidence; treating
    'nothing else matched' as proof would run the #158 asymmetry backwards.
    """
    doc = {"ingredients": [_grounded("NaCl", "5"),
                           {"preferred_term": "Mystery infusion", "concentration":
                            {"value": "10", "unit": "G_PER_L"}},
                           _ing("Yeast extract", "0.1")]}
    ok, why = act.semi_defined_candidate(doc)
    assert not ok and "not CHEBI-grounded" in why


def test_semi_defined_rejects_a_bulk_undefined_component(act):
    doc = {"ingredients": [_grounded("NaCl", "5"), _ing("Yeast extract", "5")]}
    ok, why = act.semi_defined_candidate(doc)
    assert not ok and "small amount" in why


def test_semi_defined_rejects_two_undefined_components(act):
    doc = {"ingredients": [_grounded("NaCl", "5"),
                           _ing("Yeast extract", "0.1"), _ing("Peptone", "0.1")]}
    ok, why = act.semi_defined_candidate(doc)
    assert not ok and "exactly one" in why


def test_semi_defined_rejects_an_unquantified_component(act):
    doc = {"ingredients": [_grounded("NaCl", "5"), _ing("Yeast extract")]}
    ok, why = act.semi_defined_candidate(doc)
    assert not ok and "unquantified" in why


def test_semi_defined_rejects_a_record_with_no_other_ingredients(act):
    """Nothing to be 'predominantly defined' about."""
    ok, why = act.semi_defined_candidate({"ingredients": [_ing("Yeast extract", "0.1")]})
    assert not ok and "no other ingredients" in why


def test_all_three_composition_axes_are_populated_in_the_corpus():
    """#152: the schema advertised three values and only two were ever emitted.

    Asserts SEMI_DEFINED is non-empty so it cannot silently regress to zero — a
    coverage check on `composition_type` alone read as complete while one of its
    permissible values had no records at all.
    """
    import yaml as _yaml
    from record_kinds import is_solution_record
    from collections import Counter

    seen = Counter()
    for path in (REPO_ROOT / "data" / "normalized_yaml").rglob("*.yaml"):
        doc = _yaml.safe_load(path.read_text(errors="replace"))
        if not isinstance(doc, dict) or is_solution_record(doc):
            continue
        if doc.get("composition_type"):
            seen[str(doc["composition_type"])] += 1
    for value in ("DEFINED", "UNDEFINED", "SEMI_DEFINED"):
        assert seen[value] > 0, f"no record carries composition_type: {value} — {dict(seen)}"


def test_semi_defined_report_is_idempotent_and_covers_both_verdicts():
    """The report must not change shape between the promoting run and the next (#172).

    Scanning only UNDEFINED records meant a re-run dropped every PROMOTED row,
    because those records are SEMI_DEFINED by then — so the committed artifact
    looked like 197 near-misses with no record of the 612 promotions. Including
    already-promoted records fixes that; `restamp()` is a no-op when the value
    already matches, so the promoted COUNT stays honest.
    """
    import csv

    report = (REPO_ROOT / "data" / "import_tracking" / "reports"
              / "composition_type_semi_defined.tsv")
    assert report.is_file(), "run `just audit-composition-type --promote-semi-defined`"
    rows = list(csv.DictReader(report.open(), delimiter="\t"))
    verdicts = {r["verdict"].split(":")[0] for r in rows}
    assert "PROMOTED" in verdicts, "no promoted rows — the report is not idempotent"
    assert "CURATOR" in verdicts, "no near-miss rows — the actionable subset is missing"

    near = [r for r in rows if r["verdict"].startswith("CURATOR")]
    assert all(r["ungrounded_siblings"] for r in near), (
        "a near-miss row names no ungrounded sibling, which is the thing a curator acts on"
    )
