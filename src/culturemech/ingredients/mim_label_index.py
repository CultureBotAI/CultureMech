"""Resolve recipe ingredient labels through MIM's pinned label index.

MediaIngredientMech (MIM) publishes ``docs/data/label_index.csv`` specifically
for label-to-identity resolution.  CultureMech vendors one immutable revision
of that artifact so normal builds are offline and reproducible.  The resolver
implements MIM's row-order and ambiguity contract; it never fuzzy-matches and
never treats ``ontology_id`` as the selected identity.

Hydration state is identity-significant.  Exact matching is tried first.  The
only weaker normalization collapses whitespace, ASCII hyphen, and underscore;
digits and chemical punctuation are preserved.  A weak collision is accepted
only when every matching MIM label group independently yields the same safe
answer.
"""

from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import unicodedata
from collections import defaultdict
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, replace
from enum import Enum
from functools import lru_cache
from importlib import resources
from pathlib import Path
from typing import Any

INDEX_HEADER = (
    "label",
    "match_type",
    "identifier",
    "preferred_term",
    "ontology_id",
    "mapping_status",
    "ambiguity",
)
MATCH_TYPES = frozenset({"preferred_term", "synonym", "ontology_label"})
MAPPING_STATUSES = frozenset({"MAPPED", "UNMAPPED", "REJECTED"})
SAFE_AMBIGUITIES = frozenset({"unique", "resolved:owned", "agree:same_substance"})
AMBIGUITIES = SAFE_AMBIGUITIES | frozenset(
    {
        "conflict:different_substances",
        "unresolved:partial_chemistry",
        "unresolved:no_chemistry",
    }
)

CONTRACT_VERSION = 1
MIM_REPOSITORY = "https://github.com/CultureBotAI/MediaIngredientMech"
MIM_SOURCE_PATH = "docs/data/label_index.csv"
_RESOURCE_DIR = ("data", "mediaingredientmech")
_INDEX_NAME = "label_index.csv"
_METADATA_NAME = "label_index.metadata.json"
_FULL_SHA = re.compile(r"[0-9a-f]{40}\Z")
_WEAK_SEPARATORS = re.compile(r"[\s\-_]+")


class LabelIndexError(ValueError):
    """The pinned artifact or its consumption contract is invalid."""


class ResolutionSource(str, Enum):
    """How the final ingredient identity was selected."""

    MIM_EXACT = "mim_exact"
    MIM_NORMALIZED = "mim_normalized"
    AUTHORITATIVE_UNMAPPED = "authoritative_unmapped"
    LOCAL_FALLBACK = "local_fallback"
    AMBIGUOUS_LOCAL_FALLBACK = "ambiguous_local_fallback"
    AMBIGUOUS = "ambiguous"
    NOT_FOUND = "not_found"


@dataclass(frozen=True)
class LabelIndexRow:
    """One row in MIM's ordered label index."""

    label: str
    match_type: str
    identifier: str
    preferred_term: str
    ontology_id: str
    mapping_status: str
    ambiguity: str


@dataclass(frozen=True)
class GroundingDecision:
    """A resolver result, including enough provenance to audit the choice."""

    query_label: str
    identifier: str | None
    ontology_id: str | None
    mim_preferred_term: str | None
    matched_label: str | None
    match_type: str | None
    mapping_status: str | None
    ambiguity: str | None
    resolution_source: ResolutionSource
    local_identifier: str | None
    source_compound_id: str | None
    reason: str

    @property
    def is_resolved(self) -> bool:
        """Whether this decision selects an identity for KG publication."""

        return self.identifier is not None


def strong_label_key(value: str) -> str:
    """Case-insensitive exact key with whitespace trim and Unicode NFC only."""

    return unicodedata.normalize("NFC", value).strip().casefold()


def weak_label_key(value: str) -> str:
    """Weak key that preserves formula punctuation and all hydration digits."""

    return _WEAK_SEPARATORS.sub(" ", strong_label_key(value)).strip()


class MIMLabelIndex:
    """Immutable in-memory view of MIM's ordered per-label decisions."""

    def __init__(
        self,
        rows: Sequence[LabelIndexRow],
        *,
        metadata: Mapping[str, Any] | None = None,
    ) -> None:
        if not rows:
            raise LabelIndexError("MIM label index has no data rows")
        _validate_row_sequence(rows)
        _validate_rejected_targets(rows)

        groups: dict[str, list[LabelIndexRow]] = defaultdict(list)
        group_order: list[str] = []
        for row in rows:
            key = strong_label_key(row.label)
            if key not in groups:
                group_order.append(key)
            groups[key].append(row)

        weak_groups: dict[str, list[str]] = defaultdict(list)
        for key in group_order:
            weak = weak_label_key(groups[key][0].label)
            if key not in weak_groups[weak]:
                weak_groups[weak].append(key)

        self.rows = tuple(rows)
        self.metadata = dict(metadata or {})
        self._groups = {key: tuple(group) for key, group in groups.items()}
        self._weak_groups = {key: tuple(value) for key, value in weak_groups.items()}
        self._live_identifiers = frozenset(
            row.identifier for row in rows if row.mapping_status == "MAPPED"
        )

    @classmethod
    def from_csv_bytes(
        cls,
        data: bytes,
        *,
        metadata: Mapping[str, Any] | None = None,
        verify_metadata: bool = False,
    ) -> MIMLabelIndex:
        """Parse bytes, optionally enforcing the immutable-pin metadata."""

        if verify_metadata:
            if metadata is None:
                raise LabelIndexError("metadata is required when verify_metadata=True")
            _verify_metadata(data, metadata)
        rows = _parse_csv(data)
        if metadata is not None:
            expected_rows = metadata.get("data_row_count")
            if not isinstance(expected_rows, int) or expected_rows != len(rows):
                raise LabelIndexError(
                    "metadata data_row_count does not match label index: "
                    f"{expected_rows!r} != {len(rows)}"
                )
        return cls(rows, metadata=metadata)

    @classmethod
    def from_csv_text(cls, text: str) -> MIMLabelIndex:
        """Build a resolver from an in-memory CSV fixture."""

        return cls.from_csv_bytes(text.encode("utf-8"))

    @classmethod
    def from_paths(cls, index_path: Path, metadata_path: Path) -> MIMLabelIndex:
        """Load and verify a filesystem-backed pinned artifact."""

        data = index_path.read_bytes()
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        return cls.from_csv_bytes(data, metadata=metadata, verify_metadata=True)

    @classmethod
    def from_package(cls) -> MIMLabelIndex:
        """Load and verify the label index shipped inside the wheel."""

        root = resources.files("culturemech")
        for component in _RESOURCE_DIR:
            root = root.joinpath(component)
        data = root.joinpath(_INDEX_NAME).read_bytes()
        metadata = json.loads(root.joinpath(_METADATA_NAME).read_text(encoding="utf-8"))
        return cls.from_csv_bytes(data, metadata=metadata, verify_metadata=True)

    def resolve(self, ingredient: Mapping[str, Any]) -> GroundingDecision:
        """Resolve one IngredientDescriptor, with local terms as fallback only."""

        label_value = ingredient.get("preferred_term")
        label = label_value if isinstance(label_value, str) else ""
        local_identifier, source_compound_id = _local_identifiers(ingredient)
        return self.resolve_label(
            label,
            local_identifier=local_identifier,
            source_compound_id=source_compound_id,
        )

    def resolve_label(
        self,
        label: str,
        *,
        local_identifier: str | None = None,
        source_compound_id: str | None = None,
    ) -> GroundingDecision:
        """Resolve a label, retaining explicit local/source identity diagnostics."""

        exact = self._groups.get(strong_label_key(label)) if label.strip() else None
        if exact:
            return self._decision_for_groups(
                label,
                (exact,),
                ResolutionSource.MIM_EXACT,
                local_identifier,
                source_compound_id,
            )

        weak_keys = self._weak_groups.get(weak_label_key(label), ()) if label.strip() else ()
        if weak_keys:
            groups = tuple(self._groups[key] for key in weak_keys)
            return self._decision_for_groups(
                label,
                groups,
                ResolutionSource.MIM_NORMALIZED,
                local_identifier,
                source_compound_id,
            )

        if local_identifier:
            return _local_decision(
                label,
                local_identifier,
                source_compound_id,
                source=ResolutionSource.LOCAL_FALLBACK,
                reason="label not found in pinned MIM index; retained local identity",
            )
        return GroundingDecision(
            query_label=label,
            identifier=None,
            ontology_id=None,
            mim_preferred_term=None,
            matched_label=None,
            match_type=None,
            mapping_status=None,
            ambiguity=None,
            resolution_source=ResolutionSource.NOT_FOUND,
            local_identifier=None,
            source_compound_id=source_compound_id,
            reason="label not found in pinned MIM index and no usable local identity",
        )

    def semantic_answers(self) -> dict[str, tuple[str | None, str, str]]:
        """Stable exact-label signatures used to review dependency refreshes."""

        answers: dict[str, tuple[str | None, str, str]] = {}
        for key, group in self._groups.items():
            state, row = self._group_state(group)
            identifier = row.identifier if state == "mapped" else None
            answers[key] = (identifier, state, row.ambiguity)
        return answers

    def _decision_for_groups(
        self,
        query_label: str,
        groups: Sequence[Sequence[LabelIndexRow]],
        mapped_source: ResolutionSource,
        local_identifier: str | None,
        source_compound_id: str | None,
    ) -> GroundingDecision:
        states = [self._group_state(group) for group in groups]
        representative = states[0][1]

        if all(state == "mapped" for state, _row in states):
            identifiers = {row.identifier for _state, row in states}
            if len(identifiers) == 1:
                return _mim_decision(
                    query_label,
                    representative,
                    representative.identifier,
                    mapped_source,
                    local_identifier,
                    source_compound_id,
                    "trusted MIM label-index answer",
                )

        if all(state == "unmapped" for state, _row in states):
            return _mim_decision(
                query_label,
                representative,
                None,
                ResolutionSource.AUTHORITATIVE_UNMAPPED,
                local_identifier,
                source_compound_id,
                "MIM explicitly leaves this label unmapped; local grounding suppressed",
            )

        reason = (
            "MIM label is chemically ambiguous"
            if len(groups) == 1
            else "weak normalization reaches incompatible MIM label groups"
        )
        if local_identifier:
            decision = _local_decision(
                query_label,
                local_identifier,
                source_compound_id,
                source=ResolutionSource.AMBIGUOUS_LOCAL_FALLBACK,
                reason=f"{reason}; retained explicitly labelled local fallback",
            )
            return replace(
                decision,
                ontology_id=representative.ontology_id or None,
                mim_preferred_term=representative.preferred_term,
                matched_label=representative.label,
                match_type=representative.match_type,
                mapping_status=representative.mapping_status,
                ambiguity=representative.ambiguity,
            )
        return _mim_decision(
            query_label,
            representative,
            None,
            ResolutionSource.AMBIGUOUS,
            None,
            source_compound_id,
            f"{reason}; failed closed",
        )

    def _group_state(self, group: Sequence[LabelIndexRow]) -> tuple[str, LabelIndexRow]:
        first = group[0]
        if first.ambiguity not in SAFE_AMBIGUITIES:
            return "ambiguous", first
        if first.mapping_status == "MAPPED":
            return "mapped", first
        if first.mapping_status == "UNMAPPED":
            return "unmapped", first
        if first.identifier.startswith("UNMAPPED_"):
            return "unmapped", first
        if first.identifier in self._live_identifiers:
            return "mapped", first
        return "ambiguous", first  # constructor validation makes this defensive only


def _mim_decision(
    query_label: str,
    row: LabelIndexRow,
    identifier: str | None,
    source: ResolutionSource,
    local_identifier: str | None,
    source_compound_id: str | None,
    reason: str,
) -> GroundingDecision:
    return GroundingDecision(
        query_label=query_label,
        identifier=identifier,
        ontology_id=row.ontology_id or None,
        mim_preferred_term=row.preferred_term,
        matched_label=row.label,
        match_type=row.match_type,
        mapping_status=row.mapping_status,
        ambiguity=row.ambiguity,
        resolution_source=source,
        local_identifier=local_identifier,
        source_compound_id=source_compound_id,
        reason=reason,
    )


def _local_decision(
    label: str,
    identifier: str,
    source_compound_id: str | None,
    *,
    source: ResolutionSource,
    reason: str,
) -> GroundingDecision:
    return GroundingDecision(
        query_label=label,
        identifier=identifier,
        ontology_id=None,
        mim_preferred_term=None,
        matched_label=None,
        match_type=None,
        mapping_status=None,
        ambiguity=None,
        resolution_source=source,
        local_identifier=identifier,
        source_compound_id=source_compound_id,
        reason=reason,
    )


def _nested_identifier(value: Any) -> str | None:
    if not isinstance(value, Mapping):
        return None
    identifier = value.get("id")
    if not isinstance(identifier, str) or not identifier.strip():
        return None
    return identifier.strip()


def _is_source_compound(identifier: str) -> bool:
    return identifier.casefold().startswith("mediadive.compound:")


def _local_identifiers(ingredient: Mapping[str, Any]) -> tuple[str | None, str | None]:
    term_id = _nested_identifier(ingredient.get("term"))
    chebi_term_id = _nested_identifier(ingredient.get("chebi_term"))
    source_compound_id = term_id if term_id and _is_source_compound(term_id) else None

    if chebi_term_id and not _is_source_compound(chebi_term_id):
        return chebi_term_id, source_compound_id
    if term_id and not _is_source_compound(term_id):
        return term_id, source_compound_id
    return None, source_compound_id


def _parse_csv(data: bytes) -> list[LabelIndexRow]:
    try:
        text = data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise LabelIndexError("MIM label index is not UTF-8") from exc
    reader = csv.DictReader(io.StringIO(text, newline=""))
    if tuple(reader.fieldnames or ()) != INDEX_HEADER:
        raise LabelIndexError(
            f"unexpected MIM label-index header: {reader.fieldnames!r}; expected {INDEX_HEADER!r}"
        )

    rows: list[LabelIndexRow] = []
    for line_number, raw in enumerate(reader, start=2):
        if None in raw:
            raise LabelIndexError(f"row {line_number} has columns beyond the contract header")
        row = LabelIndexRow(**{field: raw[field] for field in INDEX_HEADER})
        _validate_row(row, line_number)
        rows.append(row)
    return rows


def _validate_row(row: LabelIndexRow, line_number: int) -> None:
    for field in ("label", "identifier", "preferred_term"):
        if not getattr(row, field).strip():
            raise LabelIndexError(f"row {line_number} has an empty {field}")
    if row.match_type not in MATCH_TYPES:
        raise LabelIndexError(f"row {line_number} has unknown match_type {row.match_type!r}")
    if row.mapping_status not in MAPPING_STATUSES:
        raise LabelIndexError(
            f"row {line_number} has unknown mapping_status {row.mapping_status!r}"
        )
    if row.ambiguity not in AMBIGUITIES:
        raise LabelIndexError(f"row {line_number} has unknown ambiguity {row.ambiguity!r}")


def _validate_row_sequence(rows: Sequence[LabelIndexRow]) -> None:
    closed: set[str] = set()
    current: str | None = None
    group_ambiguity: str | None = None
    for position, row in enumerate(rows, start=2):
        key = strong_label_key(row.label)
        if not key:
            raise LabelIndexError(f"row {position} has an empty normalized label")
        if key != current:
            if current is not None:
                closed.add(current)
            if key in closed:
                raise LabelIndexError(
                    f"label group {row.label!r} is not contiguous at row {position}"
                )
            current = key
            group_ambiguity = row.ambiguity
        elif row.ambiguity != group_ambiguity:
            raise LabelIndexError(
                f"label group {row.label!r} has inconsistent ambiguity at row {position}"
            )


def _validate_rejected_targets(rows: Sequence[LabelIndexRow]) -> None:
    """Require every merge tombstone to point at a live published identity."""

    live_identifiers = {row.identifier for row in rows if row.mapping_status == "MAPPED"}
    dangling = sorted(
        {
            row.identifier
            for row in rows
            if row.mapping_status == "REJECTED"
            and not row.identifier.startswith("UNMAPPED_")
            and row.identifier not in live_identifiers
        }
    )
    if dangling:
        preview = ", ".join(dangling[:10])
        suffix = f" (+{len(dangling) - 10} more)" if len(dangling) > 10 else ""
        raise LabelIndexError(
            "REJECTED merge tombstone identifier is not held by a live MAPPED row: "
            f"{preview}{suffix}"
        )


def _verify_metadata(data: bytes, metadata: Mapping[str, Any]) -> None:
    if metadata.get("consumer_contract_version") != CONTRACT_VERSION:
        raise LabelIndexError(
            "unsupported MIM label-index consumer contract version: "
            f"{metadata.get('consumer_contract_version')!r}"
        )
    if metadata.get("repository") != MIM_REPOSITORY:
        raise LabelIndexError(f"unexpected MIM repository: {metadata.get('repository')!r}")
    if metadata.get("source_path") != MIM_SOURCE_PATH:
        raise LabelIndexError(f"unexpected MIM source path: {metadata.get('source_path')!r}")
    source_commit = metadata.get("source_commit")
    if not isinstance(source_commit, str) or not _FULL_SHA.fullmatch(source_commit):
        raise LabelIndexError("source_commit must be a full lowercase 40-character Git SHA")
    if metadata.get("header") != list(INDEX_HEADER):
        raise LabelIndexError("metadata header does not match the consumer contract")
    if metadata.get("byte_count") != len(data):
        raise LabelIndexError(
            f"metadata byte_count does not match artifact: {metadata.get('byte_count')!r} != {len(data)}"
        )
    actual_digest = hashlib.sha256(data).hexdigest()
    if metadata.get("sha256") != actual_digest:
        raise LabelIndexError(
            f"metadata sha256 does not match artifact: {metadata.get('sha256')!r} != {actual_digest}"
        )


@lru_cache(maxsize=1)
def get_default_mim_label_index() -> MIMLabelIndex:
    """Return the verified packaged resolver, loading it only once per process."""

    return MIMLabelIndex.from_package()


def resolve_ingredient(ingredient: Mapping[str, Any]) -> GroundingDecision:
    """Resolve with the pinned default index."""

    return get_default_mim_label_index().resolve(ingredient)
