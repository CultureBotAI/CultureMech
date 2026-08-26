#!/usr/bin/env python3
"""Build the public CultureMech recipe-ID lifecycle catalog.

The live corpus is authoritative for current records.  Retired IDs are kept in
``data/culturemech_id_tombstones.tsv`` so deleting a YAML file cannot make an
issued identifier reusable.  The resulting catalog is a deterministic view of
both sources and is safe for downstream consumers to pin by Git commit or
release tag.

Usage::

    just refresh-id-catalog
    just check-id-catalog
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
DEFAULT_CORPUS = REPO / "data" / "normalized_yaml"
DEFAULT_TOMBSTONES = REPO / "data" / "culturemech_id_tombstones.tsv"
DEFAULT_OUT = REPO / "data" / "culturemech_recipe_catalog.tsv"

CATALOG_SCHEMA_VERSION = "1"
CATALOG_HEADER = (
    "culturemech_id",
    "lineage_signature",
    "file_path",
    "display_name",
    "lifecycle_status",
    "successor_ids",
    "lifecycle_note",
    "catalog_schema_version",
)
TOMBSTONE_HEADER = (
    "culturemech_id",
    "lineage_signature",
    "display_name",
    "lifecycle_status",
    "successor_ids",
    "reason",
)
ID_RE = re.compile(r"^CultureMech:(\d{6})$")
TOP_LEVEL_ID_RE = re.compile(r"^id:[ \t]*(.*?)[ \t]*$", re.MULTILINE)
TOP_LEVEL_LINEAGE_RE = re.compile(r"^id_lineage_token:[ \t]*(.*?)[ \t]*$", re.MULTILINE)
TOP_LEVEL_DISPLAY_RE = re.compile(r"^(?:name|preferred_term):[ \t]*(.*?)[ \t]*$", re.MULTILINE)
ASSIGNMENT_EVENT_RE = re.compile(
    r"^- timestamp:[ \t]*(?P<timestamp>.*?)[ \t]*\r?\n"
    r"  curator:[ \t]*culturemech-id-assigner-v1\.0[ \t]*\r?\n"
    r"  action:[ \t]*Assigned CultureMech ID[ \t]*\r?\n"
    r"  notes:[ \t]*(?P<notes>.*?)[ \t]*$",
    re.MULTILINE,
)
LINEAGE_TOKEN_RE = re.compile(r"^legacy:[0-9a-f]{64}$")
LINEAGE_SIGNATURE_RE = re.compile(r"^sha256:[0-9a-f]{64}$")
TOMBSTONE_STATUSES = frozenset({"DELETED", "MERGED", "SPLIT"})
LEGACY_UNKNOWN_LINEAGE_IDS = frozenset(
    {
        "CultureMech:000190",
        "CultureMech:000306",
        "CultureMech:003009",
        "CultureMech:015406",
    }
)


@dataclass(frozen=True)
class CatalogRow:
    """One current recipe or retired identifier."""

    culturemech_id: str
    lineage_signature: str
    file_path: str
    display_name: str
    lifecycle_status: str
    successor_ids: tuple[str, ...] = ()
    lifecycle_note: str = ""


def id_number(culturemech_id: str) -> int | None:
    """Return the numeric part of a canonical ID, or ``None`` if malformed."""
    match = ID_RE.fullmatch(culturemech_id)
    if not match:
        return None
    number = int(match.group(1))
    return number if 1 <= number <= 999_999 else None


def _scalar(raw: str) -> str:
    """Decode one YAML scalar without parsing an entire recipe."""
    try:
        value = yaml.safe_load(f"value: {raw}\n").get("value")
    except (AttributeError, yaml.YAMLError):
        return ""
    return "" if value is None else str(value).strip()


def _relative_path(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except ValueError:
        return path.resolve().as_posix()


def _lineage_signature(text: str, culturemech_id: str) -> tuple[str, str | None]:
    """Return the immutable lineage witness for one live record.

    Normal records use the ID-assignment curation event written by the allocator.
    A small legacy cohort predating that event carries an explicit opaque token.
    Neither witness is an external identifier; it exists so CI can detect moving
    an issued ID to another record while allowing names and paths to change.
    """
    assignment_matches = list(ASSIGNMENT_EVENT_RE.finditer(text))
    token_matches = TOP_LEVEL_LINEAGE_RE.findall(text)
    if len(assignment_matches) + len(token_matches) != 1:
        return "", (
            "expected exactly one ID-lineage witness (assignment event or "
            f"id_lineage_token), found {len(assignment_matches) + len(token_matches)}"
        )

    if assignment_matches:
        match = assignment_matches[0]
        timestamp = _scalar(match.group("timestamp"))
        notes = _scalar(match.group("notes"))
        expected_notes = f"Assigned stable identifier: {culturemech_id}"
        if not timestamp:
            return "", "ID-assignment event has no timestamp"
        if notes != expected_notes:
            return "", (
                f"ID-assignment event says {notes!r}, expected {expected_notes!r}; "
                "the ID may have been reassigned"
            )
        anchor = f"assignment\0{timestamp}\0{culturemech_id}"
    else:
        token = _scalar(token_matches[0])
        if not LINEAGE_TOKEN_RE.fullmatch(token):
            return "", "id_lineage_token must be legacy: followed by 64 lowercase hex digits"
        anchor = f"legacy\0{token}"

    return "sha256:" + hashlib.sha256(anchor.encode("utf-8")).hexdigest(), None


def scan_corpus(corpus: Path, repo_root: Path = REPO) -> tuple[dict[str, CatalogRow], list[str]]:
    """Read current IDs, paths, and display names without fully parsing the corpus."""
    rows: dict[str, CatalogRow] = {}
    errors: list[str] = []
    first_path: dict[str, Path] = {}
    lineage_paths: dict[str, Path] = {}

    for path in sorted(corpus.rglob("*.yaml")):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError as exc:
            errors.append(f"{path}: cannot read: {exc}")
            continue

        id_matches = TOP_LEVEL_ID_RE.findall(text)
        if not id_matches:
            errors.append(f"{path}: missing top-level id")
            continue
        if len(id_matches) != 1:
            errors.append(f"{path}: expected one top-level id, found {len(id_matches)}")
            continue
        culturemech_id = _scalar(id_matches[0])
        if id_number(culturemech_id) is None:
            errors.append(f"{path}: malformed id {culturemech_id!r}; expected CultureMech:NNNNNN")
            continue

        display_match = TOP_LEVEL_DISPLAY_RE.search(text)
        display_name = _scalar(display_match.group(1)) if display_match else ""
        if not display_name:
            errors.append(f"{path}: missing top-level name/preferred_term")
            continue

        lineage_signature, lineage_error = _lineage_signature(text, culturemech_id)
        if lineage_error:
            errors.append(f"{path}: {lineage_error}")
            continue
        if lineage_signature in lineage_paths:
            errors.append(
                f"{culturemech_id}: lineage witness duplicates "
                f"{_relative_path(lineage_paths[lineage_signature], repo_root)}"
            )
            continue
        lineage_paths[lineage_signature] = path

        if culturemech_id in rows:
            errors.append(
                f"{culturemech_id}: duplicate live id in "
                f"{_relative_path(first_path[culturemech_id], repo_root)} and "
                f"{_relative_path(path, repo_root)}"
            )
            continue
        first_path[culturemech_id] = path
        rows[culturemech_id] = CatalogRow(
            culturemech_id=culturemech_id,
            lineage_signature=lineage_signature,
            file_path=_relative_path(path, repo_root),
            display_name=display_name,
            lifecycle_status="ACTIVE",
        )

    return rows, errors


def read_tombstones(path: Path) -> tuple[dict[str, CatalogRow], list[str]]:
    """Read the append-only retired-ID ledger."""
    rows: dict[str, CatalogRow] = {}
    errors: list[str] = []
    try:
        stream = path.open(encoding="utf-8", newline="")
    except OSError as exc:
        return {}, [f"{path}: cannot read tombstones: {exc}"]

    with stream:
        reader = csv.DictReader(stream, delimiter="\t")
        if tuple(reader.fieldnames or ()) != TOMBSTONE_HEADER:
            return {}, [
                f"{path}: expected header {' | '.join(TOMBSTONE_HEADER)}, got "
                f"{' | '.join(reader.fieldnames or [])}"
            ]
        for line_number, raw in enumerate(reader, start=2):
            culturemech_id = (raw["culturemech_id"] or "").strip()
            lineage_signature = (raw["lineage_signature"] or "").strip()
            display_name = (raw["display_name"] or "").strip()
            status = (raw["lifecycle_status"] or "").strip()
            successors = tuple(
                value.strip() for value in (raw["successor_ids"] or "").split(";") if value.strip()
            )
            reason = (raw["reason"] or "").strip()
            prefix = f"{path}:{line_number}"
            if id_number(culturemech_id) is None:
                errors.append(f"{prefix}: malformed id {culturemech_id!r}")
                continue
            if culturemech_id in rows:
                errors.append(f"{prefix}: duplicate tombstone {culturemech_id}")
                continue
            if lineage_signature == "UNKNOWN":
                if culturemech_id not in LEGACY_UNKNOWN_LINEAGE_IDS:
                    errors.append(f"{prefix}: UNKNOWN lineage is allowed only for baseline gaps")
            elif not LINEAGE_SIGNATURE_RE.fullmatch(lineage_signature):
                errors.append(f"{prefix}: malformed lineage_signature")
            if not display_name:
                errors.append(f"{prefix}: display_name is required")
            if status not in TOMBSTONE_STATUSES:
                errors.append(
                    f"{prefix}: lifecycle_status must be one of "
                    f"{', '.join(sorted(TOMBSTONE_STATUSES))}"
                )
            if any(id_number(successor) is None for successor in successors):
                errors.append(f"{prefix}: malformed successor_ids")
            if not reason:
                errors.append(f"{prefix}: reason is required")
            if status == "DELETED" and successors:
                errors.append(f"{prefix}: DELETED ids cannot have successors")
            if status == "MERGED" and len(successors) != 1:
                errors.append(f"{prefix}: MERGED ids require exactly one successor")
            if status == "SPLIT" and len(successors) < 2:
                errors.append(f"{prefix}: SPLIT ids require at least two successors")
            if len(successors) != len(set(successors)):
                errors.append(f"{prefix}: successor_ids must be unique")
            rows[culturemech_id] = CatalogRow(
                culturemech_id=culturemech_id,
                lineage_signature=lineage_signature,
                file_path="",
                display_name=display_name,
                lifecycle_status=status,
                successor_ids=successors,
                lifecycle_note=reason,
            )

    return rows, errors


def _successor_cycles(rows: dict[str, CatalogRow]) -> list[str]:
    graph = {
        culturemech_id: row.successor_ids
        for culturemech_id, row in rows.items()
        if row.successor_ids
    }
    errors: list[str] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(culturemech_id: str, trail: tuple[str, ...]) -> None:
        if culturemech_id in visiting:
            start = trail.index(culturemech_id)
            errors.append("successor cycle: " + " -> ".join((*trail[start:], culturemech_id)))
            return
        if culturemech_id in visited:
            return
        visiting.add(culturemech_id)
        for successor in graph.get(culturemech_id, ()):
            visit(successor, (*trail, culturemech_id))
        visiting.remove(culturemech_id)
        visited.add(culturemech_id)

    for culturemech_id in sorted(graph):
        visit(culturemech_id, ())
    return errors


def build_catalog(
    corpus: Path = DEFAULT_CORPUS,
    tombstones_path: Path = DEFAULT_TOMBSTONES,
    repo_root: Path = REPO,
) -> tuple[dict[str, CatalogRow], list[str]]:
    """Combine live records and tombstones and validate the lifecycle graph."""
    live, errors = scan_corpus(corpus, repo_root=repo_root)
    tombstones, tombstone_errors = read_tombstones(tombstones_path)
    errors.extend(tombstone_errors)

    reused = sorted(set(live) & set(tombstones))
    errors.extend(
        f"{culturemech_id}: retired id reused by a live record" for culturemech_id in reused
    )

    rows = {**tombstones, **live}
    for row in tombstones.values():
        for successor in row.successor_ids:
            if successor == row.culturemech_id:
                errors.append(f"{row.culturemech_id}: cannot succeed itself")
            elif successor not in rows:
                errors.append(f"{row.culturemech_id}: unknown successor {successor}")

    numbers = sorted(number for value in rows if (number := id_number(value)) is not None)
    if numbers:
        missing = sorted(set(range(1, numbers[-1] + 1)) - set(numbers))
        if missing:
            sample = ", ".join(f"CultureMech:{number:06d}" for number in missing[:10])
            errors.append(
                f"{len(missing)} id(s) are absent from both corpus and tombstone ledger: {sample}"
            )

    errors.extend(_successor_cycles(rows))
    return rows, errors


def _tsv_field(value: str) -> str:
    if "\t" in value or "\n" in value or "\r" in value:
        raise ValueError(f"catalog fields cannot contain tabs or newlines: {value!r}")
    return value


def render_catalog(rows: dict[str, CatalogRow]) -> str:
    """Render a deterministic, LF-terminated TSV."""
    lines = ["\t".join(CATALOG_HEADER)]
    for row in sorted(rows.values(), key=lambda value: id_number(value.culturemech_id) or 0):
        fields = (
            row.culturemech_id,
            row.lineage_signature,
            row.file_path,
            row.display_name,
            row.lifecycle_status,
            ";".join(row.successor_ids),
            row.lifecycle_note,
            CATALOG_SCHEMA_VERSION,
        )
        lines.append("\t".join(_tsv_field(value) for value in fields))
    return "\n".join(lines) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    parser.add_argument("--tombstones", type=Path, default=DEFAULT_TOMBSTONES)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--check", action="store_true", help="fail if the tracked catalog is stale")
    args = parser.parse_args(argv)

    rows, errors = build_catalog(args.corpus, args.tombstones)
    if errors:
        print(f"ERROR: recipe ID catalog has {len(errors)} violation(s):", file=sys.stderr)
        for error in errors[:30]:
            print(f"  - {error}", file=sys.stderr)
        return 2

    wanted = render_catalog(rows)
    active = sum(row.lifecycle_status == "ACTIVE" for row in rows.values())
    retired = len(rows) - active
    if args.check:
        try:
            current = args.out.read_text(encoding="utf-8")
        except OSError:
            current = ""
        if current != wanted:
            print(
                f"ERROR: {args.out} is stale; run `just refresh-id-catalog`.",
                file=sys.stderr,
            )
            return 1
        print(f"Recipe ID catalog is current: {active} active, {retired} retired.")
        return 0

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(wanted, encoding="utf-8")
    print(f"Wrote {len(rows)} rows ({active} active, {retired} retired) -> {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
