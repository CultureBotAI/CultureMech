"""Tests for recovering NBRC compositions crammed into one ingredient name (#166).

The parse must be provably faithful, because the alternative is inventing
concentrations. Two independent checks do that, and both are necessary:

  * round trip — reassembly must reproduce the source exactly, so nothing is
    invented or dropped;
  * plausibility — a wrong split can ALSO round-trip ("Tween 80" + "0.3g" and
    "Tween" + "800.3g" rebuild to the same text), so absurd values are held back.
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
def ruc():
    return _load("report_unparsed_compositions")


def test_parses_a_simple_crammed_composition(ruc):
    items, tail = ruc.parse_composition("Tryptone5gGlucose3gAgar10g")
    assert items == [("Tryptone", "5", "g"), ("Glucose", "3", "g"), ("Agar", "10", "g")]
    assert tail == ""


def test_a_truncated_formula_is_refused_not_guessed(ruc):
    """The failure that made this tool report-only.

    "KH2PO4" + "0.85g" concatenates to "KH2PO40.85g", which splits equally well
    into "KH2PO" + "40.85g". Both round-trip and 40.85 is under the plausibility
    ceiling, so the first two checks pass a parse that writes a non-existent
    compound at 47x the real concentration. An earlier version applied exactly
    that to 11 records.
    """
    verdict = ruc.assess({"ingredients": [
        {"preferred_term": "Trypticase peptone10gKH2PO40.85gGlucose5gYeast extract3g"}]})
    assert verdict["verdict"].startswith("HOLD"), verdict
    assert "truncated formula" in verdict["verdict"]


def test_the_truncated_formula_rule_only_refuses_and_never_corrects(ruc):
    """It also matches MgO, which is a real compound — so it cannot be used to
    auto-fix, only to hold back. That asymmetry is why a human is needed."""
    assert ruc.TRUNCATED_FORMULA.match("KH2PO")   # truncated
    assert ruc.TRUNCATED_FORMULA.match("MgO")     # genuine, same shape


def test_hydrate_names_still_parse(ruc):
    items, _ = ruc.parse_composition("Na2HPO4·7H2O4.9g")
    assert items == [("Na2HPO4·7H2O", "4.9", "g")]


def test_trailing_prose_is_not_treated_as_an_ingredient(ruc):
    items, tail = ruc.parse_composition("Glucose3gAdjust pH to 7.0 with NaOH.")
    assert [n for n, _, _ in items] == ["Glucose"]
    assert "Adjust pH" in tail


def test_round_trip_rejects_an_ambiguous_split(ruc):
    """The Tween 80 case: the parser reads 'Tween' + '800.3', losing the space."""
    text = "Maltose20gTween 800.3gPeptone6g"
    items, tail = ruc.parse_composition(text)
    assert not ruc.round_trips(text, items, tail)


def test_round_trip_accepts_a_faithful_parse(ruc):
    text = "Tryptone5gGlucose3g"
    items, tail = ruc.parse_composition(text)
    assert ruc.round_trips(text, items, tail)


def test_implausible_values_are_detected(ruc):
    assert ruc.implausible([("Tween", "800.3", "g")])
    assert not ruc.implausible([("Glucose", "20", "g")])


def test_water_is_exempt_from_the_plausibility_check(ruc):
    """Water at 1000 g/L is a preparation artefact, not a bad split — a different
    defect, tracked by the concentration audit rather than held back here."""
    assert not ruc.implausible([("Distilled water", "1000", "g")])


def test_a_litre_volume_basis_never_becomes_a_concentration(ruc):
    """'Distilled water1L' is the volume the recipe is made up to.

    Writing it as a per-litre figure would invent the #118 defect — water recorded
    as a solute — and in ML_PER_L, which the concentration gate does not check.
    """
    ings, basis = ruc.rebuild_ingredients([("Distilled water", "1", "L")])
    assert ings == [{"preferred_term": "Distilled water"}], ings
    assert basis == ["Distilled water 1L"]


def test_millilitre_ingredients_keep_their_concentration(ruc):
    """Seawater 750ml is a genuine proportion, not a volume basis — the unit, not
    the word 'water', is what distinguishes them."""
    ings, basis = ruc.rebuild_ingredients([("Seawater", "750", "ml")])
    assert ings[0]["concentration"] == {"value": "750", "unit": "ML_PER_L"}
    assert basis == []


def test_assess_returns_none_for_a_healthy_record(ruc):
    assert ruc.assess({"ingredients": [{"preferred_term": "Glucose"}]}) is None


def test_the_tool_cannot_write(ruc):
    """It reports; it must never gain an --apply path without the chemical
    ambiguity being resolved first."""
    import inspect
    src = inspect.getsource(ruc)
    assert "path.write_text" not in src, "the reporter has regained a write path"


def test_every_crammed_record_gets_a_verdict(ruc, media_records):
    """25 opaque records become a structured worklist, each with a reason.

    Uses the session-scoped `media_records` fixture rather than walking the corpus
    again: this test cost 102s on its own, and five such scans were enough to
    cancel the pytest job at the 40-minute CI ceiling with every test passing
    (#189). The fixture also already excludes stock solutions, which this test was
    re-implementing.
    """
    seen = 0
    for path, doc in media_records:
        verdict = ruc.assess(doc)
        if verdict:
            seen += 1
            assert verdict["verdict"].startswith(("PROPOSED", "HOLD")), verdict
            assert verdict["detail"], f"{path.name} has no reason recorded"
    assert seen == 25, f"expected 25 crammed records, found {seen}"


def test_the_docstring_does_not_advertise_commands_that_do_not_exist(ruc):
    """#180: the usage block outlived the --apply flag it documented.

    Third instance this week of a docstring describing behaviour the code lacks,
    so this checks its own module rather than trusting review to catch the next one.
    """
    import inspect
    import re
    from pathlib import Path

    doc = inspect.getdoc(ruc) or ""
    justfile = (REPO_ROOT / "project.justfile").read_text()

    for recipe in re.findall(r"just ([a-z][a-z0-9-]+)", doc):
        assert f"\n{recipe} " in justfile or f"\n{recipe}:" in justfile, (
            f"docstring references `just {recipe}`, which is not a recipe")

    src = inspect.getsource(ruc)
    for flag in set(re.findall(r"(--[a-z][a-z-]+)", doc)):
        assert f'"{flag}"' in src, f"docstring documents {flag}, which the CLI does not define"
