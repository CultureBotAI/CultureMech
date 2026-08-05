"""Guard that the deprecated `medium_type` never contradicts `composition_type` (#165).

#164 restamped 239 records `composition_type: DEFINED -> UNDEFINED` and left the
deprecated `medium_type: DEFINED` behind, so the two slots disagreed. The corpus
went from a 100% invariant to 239 violations, and an invariant nobody is watching
is one that quietly stops holding.

The expected mapping is PARSED FROM THE SCHEMA rather than hardcoded here. Each
`MediumTypeEnum` value documents its own successor ("Migrates to
composition_type=UNDEFINED"), so a schema edit moves this test with it instead of
leaving a second copy of the mapping to drift. Hardcoding it is how the two slots
disagreed in the first place.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA = REPO_ROOT / "src" / "culturemech" / "schema" / "culturemech.yaml"
sys.path.insert(0, str(REPO_ROOT / "scripts"))

# `composition_type` was later refined beyond what the deprecated slot could say:
# COMPLEX means "has undefined components", and #171 split the clearly-partial
# cases out as SEMI_DEFINED. That is a refinement of UNDEFINED, not a contradiction.
REFINEMENTS = {"UNDEFINED": {"UNDEFINED", "SEMI_DEFINED"}}


@pytest.fixture(scope="module")
def schema() -> dict:
    return yaml.safe_load(SCHEMA.read_text())


@pytest.fixture(scope="module")
def composition_mapping(schema) -> dict[str, str]:
    """medium_type value -> composition_type it declares it migrates to."""
    pv = schema["enums"]["MediumTypeEnum"]["permissible_values"]
    out = {}
    for name, body in pv.items():
        m = re.search(r"Migrates to composition_type=(\w+)", str((body or {}).get("description") or ""))
        if m:
            out[name] = m.group(1)
    return out


def test_the_schema_still_documents_a_composition_mapping(composition_mapping):
    """If this empties, every assertion below passes vacuously."""
    assert composition_mapping, "no 'Migrates to composition_type=' found in MediumTypeEnum"
    assert composition_mapping.get("DEFINED") == "DEFINED"
    assert composition_mapping.get("COMPLEX") == "UNDEFINED"


def contradictions(records, mapping) -> list[str]:
    """Records whose deprecated slot disagrees with the schema's own mapping.

    Factored out so the negative tests below can call it with constructed records.
    The corpus has 0 contradictions, so a corpus-only check passes trivially and
    proves nothing about whether the guard still works (#197).
    """
    bad = []
    for path, doc in records:
        mt = doc.get("medium_type")
        ct = doc.get("composition_type")
        if mt is None or ct is None:
            continue
        expected = mapping.get(str(mt))
        if expected is None:
            continue  # value maps to another axis; covered by its own test below
        allowed = REFINEMENTS.get(expected, {expected})
        if str(ct) not in allowed:
            bad.append(f"{getattr(path, 'name', path)}: medium_type={mt} but "
                       f"composition_type={ct} (schema says {expected})")
    return bad


def test_medium_type_never_contradicts_composition_type(media_records, composition_mapping):
    """The invariant #164 broke and #165 asks to keep settled."""
    bad = contradictions(media_records, composition_mapping)
    assert not bad, (
        f"{len(bad)} records contradict the schema's own migration mapping:\n  "
        + "\n  ".join(bad[:10]))


# --- proof the guard can fail (#197) ---------------------------------------
#
# The corpus is clean, so every corpus assertion here is trivially satisfied. These
# construct the violation instead.


def _rec(name, mt, ct):
    return (Path(name), {"medium_type": mt, "composition_type": ct})


def test_the_guard_catches_the_defect_it_was_written_for(composition_mapping):
    """#164's exact shape: composition_type restamped, deprecated slot left behind."""
    assert contradictions([_rec("a.yaml", "DEFINED", "UNDEFINED")], composition_mapping)


def test_the_guard_catches_the_reverse_disagreement(composition_mapping):
    assert contradictions([_rec("b.yaml", "COMPLEX", "DEFINED")], composition_mapping)


@pytest.mark.parametrize("mt,ct", [("COMPLEX", "UNDEFINED"), ("DEFINED", "DEFINED"),
                                   ("COMPLEX", "SEMI_DEFINED")])
def test_the_guard_accepts_agreement_and_the_documented_refinement(composition_mapping, mt, ct):
    """SEMI_DEFINED under COMPLEX is #171's refinement, not a contradiction — and a
    guard that flagged it would be switched off within a week."""
    assert not contradictions([_rec("c.yaml", mt, ct)], composition_mapping)


def test_a_widened_refinement_would_be_caught(composition_mapping):
    """REFINEMENTS is hardcoded, so widening it wrongly would silently accept the
    #164 defect. This pins that DEFINED admits only itself."""
    assert REFINEMENTS.get("DEFINED", {"DEFINED"}) == {"DEFINED"}


def test_an_empty_mapping_cannot_pass_silently(composition_mapping):
    """If the schema wording changes, `composition_mapping` empties and every
    contradiction becomes invisible. Guard the guard."""
    assert not contradictions([_rec("d.yaml", "DEFINED", "UNDEFINED")], {}), \
        "precondition: an empty mapping finds nothing"
    assert composition_mapping, "the real mapping must be non-empty"


def test_every_medium_type_value_in_use_has_a_successor_slot(media_records, schema):
    """The blocker for dropping `medium_type` entirely (#165 option 1).

    BUFFER and NEGATIVE_CONTROL document no "Migrates to" target, and
    MediumFunctionalRoleEnum has no such values — so for `specialized/pbs.yaml`
    and `specialized/water.yaml` the deprecated slot holds the ONLY classification
    the record carries. Dropping it would lose information rather than tidy it.

    This test does not demand a fix; it fails if a THIRD such record appears, so
    the unmigratable set stays known and small.
    """
    pv = schema["enums"]["MediumTypeEnum"]["permissible_values"]
    unmigratable = {
        name for name, body in pv.items()
        if not re.search(r"Migrates to", str((body or {}).get("description") or ""))
    }
    assert unmigratable == {"BUFFER", "NEGATIVE_CONTROL"}, (
        f"the set of medium_type values with no successor changed: {unmigratable}")

    stranded = [p.name for p, d in media_records if str(d.get("medium_type")) in unmigratable]
    assert sorted(stranded) == ["pbs.yaml", "water.yaml"], (
        f"records whose only classification is an unmigratable medium_type: {stranded}. "
        "Extend MediumFunctionalRoleEnum before adding more.")


def test_every_media_record_carries_a_medium_type(media_records):
    """`medium_type` is a MAINTAINED axis, not a vestige (#165).

    kgx_export emits one edge per record from this slot, so a record missing it
    contributes no type edge to the knowledge graph — silently, among ~11,092. That
    is why this asserts presence rather than merely consistency: an absent value is
    invisible in every downstream artifact until someone counts edges.

    Stamp with `just curate-medium-type --apply`.
    """
    missing = [p.name for p, d in media_records if d.get("medium_type") is None]
    assert not missing, (
        f"{len(missing)} media records have no medium_type: {missing[:10]}. "
        "Run `just curate-medium-type --apply`.")


def test_a_record_has_either_a_composition_type_or_a_directly_curated_value(media_records):
    """The two records with no composition_type are BUFFER and NEGATIVE_CONTROL,
    curated directly because the composition axis cannot express them. A third
    record in that state is an importer regression."""
    stranded = [p.name for p, d in media_records
                if d.get("composition_type") is None
                and str(d.get("medium_type")) not in {"BUFFER", "NEGATIVE_CONTROL"}]
    assert not stranded, f"records with neither axis populated: {stranded[:10]}"
