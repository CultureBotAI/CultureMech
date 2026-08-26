"""Lossless direct ingredient-occurrence collection and aggregation (#337).

The source corpus has two root record contracts.  MediaRecipe-shaped records
own ``ingredients``; SolutionRecipe-shaped records own ``composition``.  This
module selects exactly one of those fields, records every direct descriptor
with stable coordinates, and resolves its identity through the pinned
MediaIngredientMech label index introduced by #260.

The TSV occurrence artifact is canonical.  The mapped and unmapped YAML files
are deterministic compatibility views derived from the same in-memory rows.
Input errors are collected before any successful artifact is replaced.
"""

from __future__ import annotations

import csv
import json
import os
import stat
import tempfile
from collections import defaultdict
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from pathlib import Path
from typing import Any, TextIO, cast

import yaml
from linkml.validator.report import Severity
from record_kinds import has_solution_shape
from validate_strict import _get_validator, classify, infer_target_class

from culturemech.ingredients.mim_label_index import (
    GroundingDecision,
    ResolutionSource,
    resolve_ingredient,
)

OCCURRENCE_FIELDS = (
    "recipe_id",
    "recipe_label",
    "recipe_category",
    "source_path",
    "record_class",
    "component_field",
    "component_index",
    "preferred_term",
    "label_source",
    "resolved_identifier",
    "resolution_source",
    "local_identifier",
    "source_compound_id",
    "mim_preferred_term",
    "mim_matched_label",
    "mim_match_type",
    "mim_mapping_status",
    "mim_ambiguity",
    "mim_ontology_id_diagnostic",
    "grounding_reason",
    "concentration_value",
    "concentration_unit",
    "ingredient_json",
)
ERROR_FIELDS = ("file", "layer", "category", "detail", "path", "message")


@dataclass(frozen=True)
class AggregationError:
    """One row in the shared machine-readable error report."""

    file: str
    layer: str
    category: str
    detail: str
    path: str
    message: str

    def as_dict(self) -> dict[str, str]:
        return {field: str(getattr(self, field)) for field in ERROR_FIELDS}


@dataclass(frozen=True)
class IngredientOccurrence:
    """One direct root-recipe ingredient descriptor and its grounding audit."""

    recipe_id: str
    recipe_label: str
    recipe_category: str
    source_path: str
    record_class: str
    component_field: str
    component_index: int
    preferred_term: str
    label_source: str
    resolved_identifier: str
    resolution_source: str
    local_identifier: str
    source_compound_id: str
    mim_preferred_term: str
    mim_matched_label: str
    mim_match_type: str
    mim_mapping_status: str
    mim_ambiguity: str
    mim_ontology_id_diagnostic: str
    grounding_reason: str
    concentration_value: str
    concentration_unit: str
    ingredient_json: str

    @property
    def key(self) -> tuple[str, str, int]:
        """Stable occurrence coordinate within the CultureMech corpus."""

        return self.recipe_id, self.component_field, self.component_index

    @property
    def is_resolved(self) -> bool:
        return bool(self.resolved_identifier)

    @property
    def ingredient_label(self) -> str:
        """Compatibility alias for callers that use the longer field name."""

        return self.preferred_term

    @property
    def grounding_id(self) -> str:
        """Compatibility alias; ``resolved_identifier`` is the canonical name."""

        return self.resolved_identifier

    def as_dict(self) -> dict[str, str | int]:
        return {field: getattr(self, field) for field in OCCURRENCE_FIELDS}


@dataclass(frozen=True)
class ScanResult:
    """Complete deterministic scan result, including all fatal input errors."""

    occurrences: tuple[IngredientOccurrence, ...]
    errors: tuple[AggregationError, ...]


Resolver = Callable[[Mapping[str, Any]], GroundingDecision]


def _cell(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, str):
        return value
    if isinstance(value, bool):
        return "true" if value else "false"
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return str(value)


def _error(
    source_path: str,
    category: str,
    message: str,
    *,
    path: str = "",
    detail: str = "",
    layer: str = "occurrence",
) -> AggregationError:
    return AggregationError(
        file=source_path,
        layer=layer,
        category=category,
        detail=detail,
        path=path,
        message=message[:300],
    )


def _schema_errors(instance: dict[str, Any], source_path: str) -> list[AggregationError]:
    try:
        report = _get_validator().validate(
            instance,
            target_class=infer_target_class(instance),
        )
    except Exception as exc:  # noqa: BLE001 - preserve validate-strict's failure contract
        return [
            _error(
                source_path,
                "validator_crash",
                str(exc),
                detail=type(exc).__name__,
                layer="schema",
            )
        ]
    errors: list[AggregationError] = []
    for result in report.results:
        if result.severity != Severity.ERROR:
            continue
        category, detail = classify(result.message)
        errors.append(
            _error(
                source_path,
                category,
                result.message,
                detail=detail,
                path=result.instance_index or "",
                layer="schema",
            )
        )
    return errors


def _recipe_label(instance: Mapping[str, Any], record_class: str) -> tuple[str, str]:
    preferred = instance.get("preferred_term")
    if isinstance(preferred, str) and preferred.strip():
        return preferred, "preferred_term"
    name = instance.get("name")
    if record_class == "MediaRecipe" and isinstance(name, str) and name.strip():
        return name, "legacy_name"
    return "", "blank"


def _decision_value(value: str | None) -> str:
    return value or ""


def _occurrence_from_descriptor(
    *,
    recipe_id: str,
    recipe_label: str,
    recipe_label_source: str,
    recipe_category: str,
    source_path: str,
    record_class: str,
    component_field: str,
    component_index: int,
    descriptor: Mapping[str, Any],
    resolver: Resolver,
) -> IngredientOccurrence:
    label_value = descriptor.get("preferred_term")
    label = label_value if isinstance(label_value, str) else ""
    decision = resolver(descriptor)
    concentration = descriptor.get("concentration")
    if not isinstance(concentration, Mapping):
        concentration = {}
    return IngredientOccurrence(
        recipe_id=recipe_id,
        recipe_label=recipe_label,
        recipe_category=recipe_category,
        source_path=source_path,
        record_class=record_class,
        component_field=component_field,
        component_index=component_index,
        preferred_term=label,
        label_source=recipe_label_source,
        resolved_identifier=_decision_value(decision.identifier),
        resolution_source=decision.resolution_source.value,
        local_identifier=_decision_value(decision.local_identifier),
        source_compound_id=_decision_value(decision.source_compound_id),
        mim_preferred_term=_decision_value(decision.mim_preferred_term),
        mim_matched_label=_decision_value(decision.matched_label),
        mim_match_type=_decision_value(decision.match_type),
        mim_mapping_status=_decision_value(decision.mapping_status),
        mim_ambiguity=_decision_value(decision.ambiguity),
        mim_ontology_id_diagnostic=_decision_value(decision.ontology_id),
        grounding_reason=decision.reason,
        concentration_value=_cell(concentration.get("value")),
        concentration_unit=_cell(concentration.get("unit")),
        ingredient_json=json.dumps(
            dict(descriptor),
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ),
    )


def scan_ingredient_occurrences(
    input_dir: str | Path,
    resolver: Resolver = resolve_ingredient,
) -> ScanResult:
    """Scan all YAML roots and collect their authoritative direct components.

    Every file is parsed and checked against the same closed LinkML schema used
    by ``validate_strict.py``.  Any error makes the scan unsuitable for
    publication, but all files are still visited so the error report is
    complete.
    """

    root = Path(input_dir)
    if not root.is_dir():
        return ScanResult(
            occurrences=(),
            errors=(
                _error(
                    root.as_posix(),
                    "invalid_input_dir",
                    "input directory does not exist or is not a directory",
                ),
            ),
        )

    occurrences: list[IngredientOccurrence] = []
    errors: list[AggregationError] = []
    seen_keys: dict[tuple[str, str, int], str] = {}
    seen_recipe_ids: dict[str, str] = {}

    files = sorted(root.rglob("*.yaml"), key=lambda item: item.as_posix())
    if not files:
        return ScanResult(
            occurrences=(),
            errors=(
                _error(
                    root.as_posix(),
                    "no_input_files",
                    "input directory contains no YAML files",
                ),
            ),
        )

    for path in files:
        source_path = path.relative_to(root).as_posix()
        try:
            instance = yaml.safe_load(path.read_text(encoding="utf-8"))
        except UnicodeDecodeError as exc:
            errors.append(
                _error(
                    source_path,
                    "input_decode_error",
                    str(exc),
                    detail="expected UTF-8",
                    layer="schema",
                )
            )
            continue
        except yaml.YAMLError as exc:
            errors.append(
                _error(
                    source_path,
                    "yaml_parse_error",
                    str(exc).splitlines()[0],
                    layer="schema",
                )
            )
            continue
        except OSError as exc:
            errors.append(
                _error(
                    source_path,
                    "input_read_error",
                    str(exc),
                    detail=type(exc).__name__,
                )
            )
            continue

        if instance is None:
            errors.append(
                _error(
                    source_path,
                    "empty_file",
                    "file parsed as None",
                    layer="schema",
                )
            )
            continue
        if not isinstance(instance, dict):
            errors.append(
                _error(
                    source_path,
                    "invalid_record_root",
                    "root YAML value must be a mapping",
                )
            )
            continue

        validation_errors = _schema_errors(instance, source_path)
        if validation_errors:
            errors.extend(validation_errors)
            continue

        record_class = "SolutionRecipe" if has_solution_shape(instance) else "MediaRecipe"
        component_field = "composition" if record_class == "SolutionRecipe" else "ingredients"
        recipe_id_value = instance.get("id")
        if not isinstance(recipe_id_value, str) or not recipe_id_value.strip():
            errors.append(
                _error(
                    source_path,
                    "missing_recipe_id",
                    "root record has no usable CultureMech id",
                    path="/id",
                )
            )
            continue
        recipe_id = recipe_id_value.strip()
        previous_recipe_path = seen_recipe_ids.get(recipe_id)
        if previous_recipe_path is not None:
            errors.append(
                _error(
                    source_path,
                    "duplicate_recipe_id",
                    f"root recipe id also appears in {previous_recipe_path}",
                    path="/id",
                    detail=recipe_id,
                )
            )
            continue
        seen_recipe_ids[recipe_id] = source_path
        recipe_label, recipe_label_source = _recipe_label(instance, record_class)
        if not recipe_label:
            errors.append(
                _error(
                    source_path,
                    "missing_recipe_label",
                    "root record has no canonical display label",
                    path="/preferred_term" if record_class == "SolutionRecipe" else "/name",
                )
            )
            continue

        components = instance.get(component_field)
        if not isinstance(components, list):
            errors.append(
                _error(
                    source_path,
                    "invalid_component_collection",
                    f"{component_field} must be a list",
                    path=f"/{component_field}",
                )
            )
            continue

        recipe_category = _cell(instance.get("category") or "UNKNOWN").upper()
        for index, descriptor in enumerate(components):
            descriptor_path = f"/{component_field}/{index}"
            if not isinstance(descriptor, Mapping):
                errors.append(
                    _error(
                        source_path,
                        "invalid_component",
                        "ingredient descriptor must be a mapping",
                        path=descriptor_path,
                    )
                )
                continue
            try:
                occurrence = _occurrence_from_descriptor(
                    recipe_id=recipe_id,
                    recipe_label=recipe_label,
                    recipe_label_source=recipe_label_source,
                    recipe_category=recipe_category,
                    source_path=source_path,
                    record_class=record_class,
                    component_field=component_field,
                    component_index=index,
                    descriptor=descriptor,
                    resolver=resolver,
                )
            except Exception as exc:  # noqa: BLE001 - report instead of silently skipping
                errors.append(
                    _error(
                        source_path,
                        "resolver_error",
                        str(exc),
                        path=descriptor_path,
                        detail=type(exc).__name__,
                    )
                )
                continue
            previous_path = seen_keys.get(occurrence.key)
            if previous_path is not None:
                errors.append(
                    _error(
                        source_path,
                        "duplicate_occurrence_key",
                        "stable occurrence coordinate also appears in " + previous_path,
                        path=descriptor_path,
                        detail="|".join(map(str, occurrence.key)),
                    )
                )
                continue
            seen_keys[occurrence.key] = source_path
            occurrences.append(occurrence)

    occurrences.sort(
        key=lambda row: (
            row.recipe_id,
            row.component_field,
            row.component_index,
            row.source_path,
        )
    )
    errors.sort(
        key=lambda row: (
            row.file,
            row.layer,
            row.path,
            row.category,
            row.message,
        )
    )
    return ScanResult(tuple(occurrences), tuple(errors))


def _write_tsv(
    stream: TextIO,
    fieldnames: Sequence[str],
    rows: Sequence[Mapping[str, Any]],
) -> None:
    writer = csv.DictWriter(
        stream,
        fieldnames=fieldnames,
        delimiter="\t",
        quoting=csv.QUOTE_MINIMAL,
        lineterminator="\n",
    )
    writer.writeheader()
    writer.writerows(rows)


def _write_occurrences_stream(
    stream: TextIO,
    occurrences: Sequence[IngredientOccurrence],
) -> None:
    writer = csv.DictWriter(
        stream,
        fieldnames=OCCURRENCE_FIELDS,
        delimiter="\t",
        quoting=csv.QUOTE_MINIMAL,
        lineterminator="\n",
    )
    writer.writeheader()
    for row in occurrences:
        writer.writerow(row.as_dict())


def _write_errors_stream(stream: TextIO, errors: Sequence[AggregationError]) -> None:
    _write_tsv(stream, ERROR_FIELDS, [row.as_dict() for row in errors])


def _safe_dump(value: Any, stream: TextIO) -> None:
    yaml.safe_dump(
        value,
        stream,
        allow_unicode=True,
        sort_keys=False,
        default_flow_style=False,
    )


def _write_yaml_collection_stream(stream: TextIO, value: Mapping[str, Any]) -> None:
    """Write one top-level collection without representing its full row list.

    PyYAML constructs an in-memory representation graph for a whole value before
    emitting it.  Dumping each top-level list entry separately preserves the
    same YAML data model and ordering while keeping the 200k-row mapped view
    within a practical memory bound.
    """

    scalar_values = {key: item for key, item in value.items() if not isinstance(item, list)}
    if scalar_values:
        _safe_dump(scalar_values, stream)
    for key, items in value.items():
        if not isinstance(items, list):
            continue
        if not items:
            stream.write(f"{key}: []\n")
            continue
        stream.write(f"{key}:\n")
        for item in items:
            _safe_dump([item], stream)


ArtifactWriter = Callable[[TextIO], None]


def _stage_writer(path: Path, writer: ArtifactWriter) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="\n",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    )
    staged = Path(handle.name)
    try:
        with handle:
            writer(cast(TextIO, handle))
            handle.flush()
            os.fsync(handle.fileno())
        mode = stat.S_IMODE(path.stat().st_mode) if path.exists() else 0o644
        staged.chmod(mode)
    except Exception:
        staged.unlink(missing_ok=True)
        raise
    return staged


def _backup_destination(path: Path) -> Path | None:
    if not path.exists():
        return None
    descriptor, backup_name = tempfile.mkstemp(
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".bak",
    )
    os.close(descriptor)
    backup = Path(backup_name)
    backup.unlink()
    os.link(path, backup)
    return backup


def _atomic_write_many(artifacts: Sequence[tuple[Path, ArtifactWriter]]) -> None:
    resolved_destinations = [destination.resolve() for destination, _writer in artifacts]
    if len(resolved_destinations) != len(set(resolved_destinations)):
        raise ValueError("artifact destinations must be distinct")
    staged: list[tuple[Path, Path]] = []
    backups: dict[Path, Path | None] = {}
    replaced: list[Path] = []
    try:
        for destination, writer in artifacts:
            staged.append((_stage_writer(destination, writer), destination))
        for _temporary, destination in staged:
            backups[destination] = _backup_destination(destination)
        for temporary, destination in staged:
            os.replace(temporary, destination)
            replaced.append(destination)
    except Exception:
        for destination in reversed(replaced):
            backup = backups.get(destination)
            if backup is None:
                destination.unlink(missing_ok=True)
            else:
                os.replace(backup, destination)
        raise
    finally:
        for temporary, _destination in staged:
            temporary.unlink(missing_ok=True)
        for backup in backups.values():
            if backup is not None:
                backup.unlink(missing_ok=True)


def write_occurrences_tsv(
    path: str | Path,
    occurrences: Sequence[IngredientOccurrence],
) -> None:
    """Atomically write the canonical, uncapped occurrence table."""

    _atomic_write_many(
        [(Path(path), lambda stream: _write_occurrences_stream(stream, occurrences))]
    )


def write_error_report(path: str | Path, errors: Sequence[AggregationError]) -> None:
    """Atomically write the shared error header even when there are no rows."""

    _atomic_write_many([(Path(path), lambda stream: _write_errors_stream(stream, errors))])


def write_yaml_output(path: str | Path, value: Mapping[str, Any]) -> None:
    """Atomically write one deterministic compatibility-view YAML file."""

    _atomic_write_many([(Path(path), lambda stream: _write_yaml_collection_stream(stream, value))])


def write_occurrences_and_yaml(
    occurrences_path: str | Path,
    occurrences: Sequence[IngredientOccurrence],
    yaml_path: str | Path,
    value: Mapping[str, Any],
) -> None:
    """Publish a compatibility wrapper's two outputs as one staged set."""

    _atomic_write_many(
        [
            (
                Path(occurrences_path),
                lambda stream: _write_occurrences_stream(stream, occurrences),
            ),
            (
                Path(yaml_path),
                lambda stream: _write_yaml_collection_stream(stream, value),
            ),
        ]
    )


def ensure_distinct_output_paths(*paths: str | Path) -> None:
    """Reject CLI output aliases before any error or success artifact is touched."""

    resolved = [Path(path).resolve() for path in paths]
    if len(resolved) != len(set(resolved)):
        raise ValueError("ingredient aggregation output paths must be distinct")


def _occurrence_dict(row: IngredientOccurrence) -> dict[str, Any]:
    occurrence = {
        "recipe_id": row.recipe_id,
        "recipe_label": row.recipe_label,
        "recipe_category": row.recipe_category,
        "source_path": row.source_path,
        "component_field": row.component_field,
        "component_index": row.component_index,
        "preferred_term": row.preferred_term,
        "resolution_source": row.resolution_source,
        "grounding_reason": row.grounding_reason,
    }
    optional = {
        "resolved_identifier": row.resolved_identifier,
        "source_compound_id": row.source_compound_id,
        "local_identifier": row.local_identifier,
        "mim_preferred_term": row.mim_preferred_term,
        "mim_matched_label": row.mim_matched_label,
        "mim_match_type": row.mim_match_type,
        "mim_mapping_status": row.mim_mapping_status,
        "mim_ambiguity": row.mim_ambiguity,
        "mim_ontology_id_diagnostic": row.mim_ontology_id_diagnostic,
    }
    occurrence.update({key: value for key, value in optional.items() if value})
    return occurrence


def _ingredient(row: IngredientOccurrence) -> dict[str, Any]:
    value = json.loads(row.ingredient_json)
    if not isinstance(value, dict):  # pragma: no cover - constructor guarantees it
        raise TypeError("ingredient_json must encode a mapping")
    return value


def _concentration_rows(rows: Sequence[IngredientOccurrence]) -> list[dict[str, str]]:
    unique: dict[tuple[str, str, str], dict[str, str]] = {}
    for row in rows:
        ingredient = _ingredient(row)
        notes = _cell(ingredient.get("notes"))
        if not row.concentration_value and not row.concentration_unit and not notes:
            continue
        key = row.concentration_value, row.concentration_unit, notes
        unique[key] = {
            "value": row.concentration_value,
            "unit": row.concentration_unit,
            "notes": notes,
        }
    return [unique[key] for key in sorted(unique)]


def _ontology_source(identifier: str) -> str:
    prefix = identifier.partition(":")[0].upper()
    if prefix in {"CHEBI", "FOODON", "NCIT", "MESH", "UBERON", "ENVO"}:
        return prefix
    return "OTHER"


def _canonical_term(rows: Sequence[IngredientOccurrence]) -> str:
    mim_terms = sorted({row.mim_preferred_term for row in rows if row.mim_preferred_term})
    if mim_terms:
        return mim_terms[0]
    source_terms = sorted({row.preferred_term for row in rows if row.preferred_term})
    return source_terms[0] if source_terms else rows[0].resolved_identifier


def _mapping_quality(rows: Sequence[IngredientOccurrence]) -> str:
    match_types = {row.mim_match_type for row in rows if row.mim_match_type}
    resolution_sources = {row.resolution_source for row in rows}
    if match_types & {"synonym", "ontology_label"} or ResolutionSource.MIM_NORMALIZED.value in (
        resolution_sources
    ):
        return "SYNONYM_MATCH"
    if resolution_sources <= {
        ResolutionSource.MIM_EXACT.value,
        ResolutionSource.MIM_NORMALIZED.value,
    }:
        return "DIRECT_MATCH"
    return "INFERRED"


def _category_summary(
    rows: Sequence[IngredientOccurrence],
    *,
    mapped: bool,
) -> list[dict[str, Any]]:
    by_category: dict[str, list[IngredientOccurrence]] = defaultdict(list)
    for row in rows:
        by_category[row.recipe_category or "UNKNOWN"].append(row)
    summary: list[dict[str, Any]] = []
    for category in sorted(by_category):
        category_rows = by_category[category]
        unique_keys = {
            row.resolved_identifier if mapped else _unmapped_group_key(row) for row in category_rows
        }
        summary.append(
            {
                "category": category,
                "recipes_with_mapped" if mapped else "recipes_with_unmapped": len(
                    {row.recipe_id for row in category_rows}
                ),
                "total_mapped_instances" if mapped else "total_unmapped_instances": len(
                    category_rows
                ),
                "unique_mapped_count" if mapped else "unique_unmapped_count": len(unique_keys),
            }
        )
    return summary


def build_mapped_output(
    occurrences: Sequence[IngredientOccurrence],
    min_occurrences: int = 1,
) -> dict[str, Any]:
    """Build the identity-first mapped compatibility view."""

    groups: dict[str, list[IngredientOccurrence]] = defaultdict(list)
    for row in occurrences:
        if row.is_resolved:
            groups[row.resolved_identifier].append(row)

    entries: list[dict[str, Any]] = []
    included_rows: list[IngredientOccurrence] = []
    for identifier, group in groups.items():
        rows = sorted(group, key=lambda row: row.key + (row.source_path,))
        if len(rows) < min_occurrences:
            continue
        included_rows.extend(rows)
        canonical_term = _canonical_term(rows)
        source_labels = sorted({row.preferred_term for row in rows if row.preferred_term})
        entries.append(
            {
                "preferred_term": canonical_term,
                "resolved_identifier": identifier,
                "ontology_label": canonical_term,
                "ontology_source": _ontology_source(identifier),
                "occurrence_count": len(rows),
                "distinct_recipe_count": len({row.recipe_id for row in rows}),
                "recipe_occurrences": [_occurrence_dict(row) for row in rows],
                "concentration_info": _concentration_rows(rows),
                "synonyms": [label for label in source_labels if label != canonical_term],
                "mapping_quality": _mapping_quality(rows),
            }
        )

    entries.sort(key=lambda entry: (-entry["occurrence_count"], entry["resolved_identifier"]))
    ontology_rows: dict[str, list[IngredientOccurrence]] = defaultdict(list)
    for row in included_rows:
        ontology_rows[_ontology_source(row.resolved_identifier)].append(row)
    total = len(included_rows)
    ontology_summary = []
    for source in sorted(ontology_rows):
        rows = ontology_rows[source]
        ontology_summary.append(
            {
                "ontology_source": source,
                "unique_terms_count": len({row.resolved_identifier for row in rows}),
                "total_instances": len(rows),
                "coverage_percentage": round((len(rows) * 100.0 / total), 6) if total else 0.0,
            }
        )
    return {
        "total_mapped_count": len(entries),
        "total_instances": total,
        "recipe_count": len({row.recipe_id for row in included_rows}),
        "mapped_ingredients": entries,
        "summary_by_category": _category_summary(included_rows, mapped=True),
        "summary_by_ontology": ontology_summary,
    }


def _unmapped_group_key(row: IngredientOccurrence) -> tuple[str, ...]:
    if not row.preferred_term.strip():
        return (
            "blank",
            row.recipe_id,
            row.component_field,
            str(row.component_index),
        )
    return (
        "label",
        row.preferred_term,
        row.resolution_source,
        row.mim_mapping_status,
        row.mim_ambiguity,
    )


def _unmapped_status(rows: Sequence[IngredientOccurrence]) -> str:
    if any(row.resolution_source == ResolutionSource.AMBIGUOUS.value for row in rows):
        return "AMBIGUOUS"
    return "UNMAPPED"


def build_unmapped_output(
    occurrences: Sequence[IngredientOccurrence],
    min_occurrences: int = 1,
) -> dict[str, Any]:
    """Build the unresolved compatibility view without dropping blank labels."""

    groups: dict[tuple[str, ...], list[IngredientOccurrence]] = defaultdict(list)
    for row in occurrences:
        if not row.is_resolved:
            groups[_unmapped_group_key(row)].append(row)

    entries: list[dict[str, Any]] = []
    included_rows: list[IngredientOccurrence] = []
    for key, group in groups.items():
        rows = sorted(group, key=lambda row: row.key + (row.source_path,))
        if len(rows) < min_occurrences:
            continue
        included_rows.extend(rows)
        first = rows[0]
        notes = sorted(
            {
                _cell(_ingredient(row).get("notes"))
                for row in rows
                if _cell(_ingredient(row).get("notes"))
            }
        )
        placeholder_id = (
            first.preferred_term
            if first.preferred_term
            else f"blank:{first.recipe_id}:{first.component_field}:{first.component_index}"
        )
        entries.append(
            {
                "preferred_term": first.preferred_term,
                "placeholder_id": placeholder_id,
                "raw_ingredient_text": notes,
                "parsed_chemical_name": first.preferred_term or (notes[0] if notes else ""),
                "occurrence_count": len(rows),
                "distinct_recipe_count": len({row.recipe_id for row in rows}),
                "recipe_occurrences": [_occurrence_dict(row) for row in rows],
                "concentration_info": _concentration_rows(rows),
                "mapping_status": _unmapped_status(rows),
                "_sort_key": key,
            }
        )

    entries.sort(
        key=lambda entry: (
            -entry["occurrence_count"],
            entry["preferred_term"],
            entry["placeholder_id"],
            entry["_sort_key"],
        )
    )
    for entry in entries:
        entry.pop("_sort_key")
    return {
        "total_unmapped_count": len(entries),
        "total_instances": len(included_rows),
        "recipe_count": len({row.recipe_id for row in included_rows}),
        "unmapped_ingredients": entries,
        "summary_by_category": _category_summary(included_rows, mapped=False),
    }


def run_aggregation(
    input_dir: str | Path,
    occurrences_output: str | Path,
    mapped_output: str | Path,
    unmapped_output: str | Path,
    errors_output: str | Path,
    min_occurrences: int = 1,
    verbose: bool = False,
    resolver: Resolver = resolve_ingredient,
) -> int:
    """Scan once and publish all deterministic views, or only the error report."""

    if min_occurrences < 1:
        raise ValueError("min_occurrences must be at least 1")
    ensure_distinct_output_paths(
        occurrences_output,
        mapped_output,
        unmapped_output,
        errors_output,
    )
    result = scan_ingredient_occurrences(input_dir, resolver=resolver)
    write_error_report(errors_output, result.errors)
    if result.errors:
        if verbose:
            print(
                f"Ingredient aggregation failed with {len(result.errors)} input error(s); "
                f"see {errors_output}"
            )
        return 1

    mapped = build_mapped_output(result.occurrences, min_occurrences=min_occurrences)
    unmapped = build_unmapped_output(result.occurrences, min_occurrences=min_occurrences)
    _atomic_write_many(
        [
            (
                Path(occurrences_output),
                lambda stream: _write_occurrences_stream(stream, result.occurrences),
            ),
            (
                Path(mapped_output),
                lambda stream: _write_yaml_collection_stream(stream, mapped),
            ),
            (
                Path(unmapped_output),
                lambda stream: _write_yaml_collection_stream(stream, unmapped),
            ),
        ]
    )
    if verbose:
        print(
            "Ingredient aggregation complete: "
            f"{len(result.occurrences)} occurrences, "
            f"{mapped['total_instances']} mapped, {unmapped['total_instances']} unmapped"
        )
    return 0
