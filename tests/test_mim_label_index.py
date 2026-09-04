"""Contract tests for the pinned MediaIngredientMech label resolver (#260)."""

from __future__ import annotations

import csv
import io

import pytest

from culturemech.export.kgx_export import transform
from culturemech.ingredients.mim_label_index import (
    INDEX_HEADER,
    LabelIndexError,
    MIMLabelIndex,
    ResolutionSource,
    get_default_mim_label_index,
)

pytestmark = pytest.mark.fast


def _csv(*rows: dict[str, str]) -> str:
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=INDEX_HEADER, lineterminator="\n")
    writer.writeheader()
    writer.writerows(rows)
    return output.getvalue()


def _row(
    label: str,
    identifier: str,
    *,
    preferred_term: str | None = None,
    match_type: str = "preferred_term",
    ontology_id: str | None = None,
    mapping_status: str = "MAPPED",
    ambiguity: str = "unique",
) -> dict[str, str]:
    return {
        "label": label,
        "match_type": match_type,
        "identifier": identifier,
        "preferred_term": preferred_term or label,
        "ontology_id": ontology_id if ontology_id is not None else identifier,
        "mapping_status": mapping_status,
        "ambiguity": ambiguity,
    }


def test_packaged_artifact_is_verified_and_pinned():
    index = get_default_mim_label_index()
    assert len(index.rows) == 9876
    assert index.metadata["source_commit"] == "9f09e4fb97fb0e6cbbd6f25baca40b36512adb88"
    assert index.metadata["sha256"] == (
        "a36cd4683feb89e2fc2a1721dc15008d1e10c12044e89a36c27b6621a8aaf262"
    )


def test_mim_overrides_a_conflicting_local_grounding():
    decision = get_default_mim_label_index().resolve(
        {"preferred_term": "EDTA", "term": {"id": "CHEBI:64755"}}
    )
    assert decision.identifier == "CHEBI:4735"
    assert decision.local_identifier == "CHEBI:64755"
    assert decision.resolution_source is ResolutionSource.MIM_EXACT


def test_non_chebi_mim_identity_is_retained():
    decision = get_default_mim_label_index().resolve(
        {"preferred_term": "Beef heart", "term": {"id": "UBERON:0000948"}}
    )
    assert decision.identifier == "FOODON:00004410"


def test_paba_and_registry_identifiers_follow_mim_identifier():
    index = get_default_mim_label_index()
    assert index.resolve_label("4-Aminobenzoic Acid").identifier == "CHEBI:30753"
    assert index.resolve_label("1,3-Hexanediol").identifier == "cas:21531-91-9"

    diagnostic_only = MIMLabelIndex.from_csv_text(
        _csv(_row("Registry reagent", "cas:1-23-4", ontology_id="CHEBI:999"))
    ).resolve_label("Registry reagent")
    assert diagnostic_only.identifier == "cas:1-23-4"
    assert diagnostic_only.ontology_id == "CHEBI:999"


@pytest.mark.parametrize("label", ["Calf brains", "Infusion from Potatoes"])
def test_authoritative_unmapped_suppresses_a_local_term(label: str):
    decision = get_default_mim_label_index().resolve(
        {"preferred_term": label, "term": {"id": "UBERON:0000955"}}
    )
    assert decision.identifier is None
    assert decision.resolution_source is ResolutionSource.AUTHORITATIVE_UNMAPPED
    assert decision.local_identifier == "UBERON:0000955"


def test_missing_mim_label_prefers_chebi_term_and_preserves_source_compound():
    decision = get_default_mim_label_index().resolve(
        {
            "preferred_term": "CultureMech test-only missing ingredient 260",
            "term": {"id": "mediadive.compound:999999"},
            "chebi_term": {"id": "CHEBI:12345"},
        }
    )
    assert decision.identifier == "CHEBI:12345"
    assert decision.source_compound_id == "mediadive.compound:999999"
    assert decision.resolution_source is ResolutionSource.LOCAL_FALLBACK


def test_source_compound_is_not_promoted_to_semantic_identity():
    decision = get_default_mim_label_index().resolve(
        {
            "preferred_term": "CultureMech test-only missing ingredient 260",
            "term": {"id": "mediadive.compound:999999"},
        }
    )
    assert decision.identifier is None
    assert decision.source_compound_id == "mediadive.compound:999999"


def test_merged_tombstone_resolves_only_when_a_live_record_holds_the_identifier():
    index = MIMLabelIndex.from_csv_text(
        _csv(
            _row("Legacy", "CHEBI:1", mapping_status="REJECTED"),
            _row("Live", "CHEBI:1"),
        )
    )
    assert index.resolve_label("Legacy").identifier == "CHEBI:1"

    with pytest.raises(LabelIndexError, match="not held by a live MAPPED row"):
        MIMLabelIndex.from_csv_text(_csv(_row("Legacy", "CHEBI:1", mapping_status="REJECTED")))


def test_invalid_retirement_is_authoritatively_unmapped():
    invalid = MIMLabelIndex.from_csv_text(
        _csv(
            _row(
                "Invalid label",
                "UNMAPPED_0001",
                ontology_id="",
                mapping_status="REJECTED",
            )
        )
    )
    decision = invalid.resolve_label("Invalid label", local_identifier="CHEBI:2")
    assert decision.identifier is None
    assert decision.resolution_source is ResolutionSource.AUTHORITATIVE_UNMAPPED


def test_unsafe_ambiguity_fails_closed_but_labels_a_local_fallback():
    index = MIMLabelIndex.from_csv_text(
        _csv(
            _row(
                "Shared",
                "CHEBI:1",
                match_type="synonym",
                preferred_term="One",
                ambiguity="conflict:different_substances",
            ),
            _row(
                "shared",
                "CHEBI:2",
                match_type="synonym",
                preferred_term="Two",
                ambiguity="conflict:different_substances",
            ),
        )
    )
    unresolved = index.resolve_label("SHARED")
    assert unresolved.identifier is None
    assert unresolved.resolution_source is ResolutionSource.AMBIGUOUS

    fallback = index.resolve_label("SHARED", local_identifier="CHEBI:3")
    assert fallback.identifier == "CHEBI:3"
    assert fallback.ambiguity == "conflict:different_substances"
    assert fallback.resolution_source is ResolutionSource.AMBIGUOUS_LOCAL_FALLBACK


@pytest.mark.parametrize("ambiguity", ["unique", "resolved:owned", "agree:same_substance"])
def test_every_safe_ambiguity_class_is_accepted(ambiguity: str):
    index = MIMLabelIndex.from_csv_text(_csv(_row("Safe", "CHEBI:1", ambiguity=ambiguity)))
    assert index.resolve_label("Safe").identifier == "CHEBI:1"


@pytest.mark.parametrize(
    "ambiguity",
    [
        "conflict:different_substances",
        "unresolved:partial_chemistry",
        "unresolved:no_chemistry",
    ],
)
def test_every_unsafe_ambiguity_class_is_refused(ambiguity: str):
    index = MIMLabelIndex.from_csv_text(_csv(_row("Unsafe", "CHEBI:1", ambiguity=ambiguity)))
    assert index.resolve_label("Unsafe").resolution_source is ResolutionSource.AMBIGUOUS


def test_weak_normalization_is_safe_only_for_one_semantic_answer():
    safe = MIMLabelIndex.from_csv_text(_csv(_row("Sodium-chloride", "CHEBI:26710")))
    decision = safe.resolve_label("sodium chloride")
    assert decision.identifier == "CHEBI:26710"
    assert decision.resolution_source is ResolutionSource.MIM_NORMALIZED

    collision = MIMLabelIndex.from_csv_text(_csv(_row("A-B", "CHEBI:1"), _row("A B", "CHEBI:2")))
    assert collision.resolve_label("A-B").identifier == "CHEBI:1"  # exact wins
    ambiguous = collision.resolve_label("A_B")
    assert ambiguous.identifier is None
    assert ambiguous.resolution_source is ResolutionSource.AMBIGUOUS

    agreement = MIMLabelIndex.from_csv_text(_csv(_row("C-D", "CHEBI:3"), _row("C D", "CHEBI:3")))
    assert agreement.resolve_label("C_D").identifier == "CHEBI:3"


def test_hydration_digits_and_formula_punctuation_never_collapse():
    index = MIMLabelIndex.from_csv_text(
        _csv(
            _row("CaCl2 x 2 H2O", "CHEBI:86124"),
            _row("CaCl2 x 6 H2O", "CHEBI:91243"),
        )
    )
    decision = index.resolve_label("CaCl2 x 7 H2O")
    assert decision.identifier is None
    assert decision.resolution_source is ResolutionSource.NOT_FOUND


def test_invalid_header_and_noncontiguous_groups_are_rejected():
    with pytest.raises(LabelIndexError, match="header"):
        MIMLabelIndex.from_csv_text("label,identifier\nA,CHEBI:1\n")

    with pytest.raises(LabelIndexError, match="not contiguous"):
        MIMLabelIndex.from_csv_text(
            _csv(
                _row("A", "CHEBI:1"),
                _row("B", "CHEBI:2"),
                _row("a", "CHEBI:1", match_type="synonym"),
            )
        )

    with pytest.raises(LabelIndexError, match="unknown mapping_status"):
        MIMLabelIndex.from_csv_text(_csv(_row("A", "CHEBI:1", mapping_status="PENDING_REVIEW")))

    with pytest.raises(LabelIndexError, match="inconsistent ambiguity"):
        MIMLabelIndex.from_csv_text(
            _csv(
                _row("A", "CHEBI:1"),
                _row("a", "CHEBI:1", match_type="synonym", ambiguity="resolved:owned"),
            )
        )


def test_kgx_uses_mim_for_override_non_chebi_and_authoritative_unmapped():
    record = {
        "name": "Resolver Canary",
        "ingredients": [
            {"preferred_term": "EDTA", "term": {"id": "CHEBI:64755"}},
            {"preferred_term": "Beef heart", "term": {"id": "UBERON:0000948"}},
            {"preferred_term": "Calf brains", "term": {"id": "UBERON:0000955"}},
        ],
    }
    ingredient_objects = {
        edge["object"] for edge in transform(record) if edge["predicate"] == "biolink:has_part"
    }
    assert ingredient_objects == {"CHEBI:4735", "FOODON:00004410"}


def test_kgx_labels_ambiguous_and_source_anchored_local_fallbacks():
    record = {
        "name": "Fallback Canary",
        "ingredients": [
            {
                "preferred_term": "(2S)-2-aminobutanedioic acid",
                "term": {"id": "CHEBI:17053"},
            },
            {
                "preferred_term": "CultureMech test-only missing ingredient 260",
                "term": {"id": "mediadive.compound:999999"},
                "chebi_term": {"id": "CHEBI:12345"},
            },
        ],
    }
    ingredient_objects = {
        edge["object"] for edge in transform(record) if edge["predicate"] == "biolink:has_part"
    }
    assert ingredient_objects == {"CHEBI:17053", "CHEBI:12345"}
