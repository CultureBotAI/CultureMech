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

    expect = {"COMPLEX": "UNDEFINED", "DEFINED": "DEFINED"}
    bad = []
    for path in (REPO_ROOT / "data" / "normalized_yaml").rglob("*.yaml"):
        doc = _yaml.safe_load(path.read_text(errors="replace"))
        if not isinstance(doc, dict) or is_solution_record(doc):
            continue
        mt, ct = doc.get("medium_type"), doc.get("composition_type")
        if mt is None or ct is None:
            continue
        if expect.get(str(mt), str(mt)) != str(ct):
            bad.append(f"{path.name}: medium_type={mt} composition_type={ct}")
    assert not bad, (
        f"{len(bad)} record(s) have a deprecated medium_type contradicting "
        f"composition_type (e.g. {bad[:3]}) — see #165"
    )
