#!/usr/bin/env python3
"""Repair the remaining rejected peptone identities from CultureMech #484.

Preview by default; pass --apply to write and --expect-count 109 to guard the
2026-09-21 cohort. The optional JSON report records coordinates and before/after
SHA256s. Only active root ingredients/composition are touched; historical notes
remain intact. Regenerate occurrences and KGX with aggregate-all-ingredients
and kgx-export after applying.

The 29 solution entries retain their mediadive.compound source identifier:
MICRO cannot go in the CHEBI-only chebi_term slot. Removing the rejected
chebi_term lets the existing pinned MIM resolver supply the MICRO identity.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml
from record_io import dump_record
from yaml.nodes import MappingNode, ScalarNode, SequenceNode

from culturemech.ingredients.mim_label_index import get_default_mim_label_index

REPO = Path(__file__).resolve().parents[1]
NORMALIZED = REPO / "data" / "normalized_yaml"
MIM_COMMIT = "24562493919391df4468a4285b7c997960cc8868"
MIM_SOURCE = f"https://github.com/CultureBotAI/MediaIngredientMech/tree/{MIM_COMMIT}"
# Verified against MIM's reviewed ingredient YAML and OLS MICRO on 2026-09-21.
# Key on the ingredient AND rejected ID, never the ID alone.
CORRECTIONS = {
    ("Trypticase", "CHEBI:78018"): ("MICRO:0000175", "Trypticase peptone"),
    ("Bacto-tryptone", "CHEBI:78018"): ("MICRO:0000182", "tryptone"),
    ("Peptone", "FOODON:03302071"): ("MICRO:0000178", "peptone"),
}
ACTION = "CORRECTED_REJECTED_PEPTONE_GROUNDING"


def verify_mim() -> str:
    """Fail before planning edits if the packaged identity source disagrees."""
    index = get_default_mim_label_index()
    for (name, _old), (identifier, _label) in CORRECTIONS.items():
        decision = index.resolve_label(name)
        if decision.identifier != identifier or decision.mapping_status != "MAPPED":
            raise ValueError(f"MIM no longer supports {name!r} -> {identifier}")
    return str(index.metadata["source_commit"])


def _fields(node: MappingNode) -> dict:
    if not isinstance(node, MappingNode):
        raise ValueError("Expected a YAML mapping")
    return {key.value: (key, value) for key, value in node.value}


def _shared_nodes(node: object) -> set[int]:
    """Find aliased nodes and descendants whose source marks are shared."""
    seen: set[int] = set()
    shared: set[int] = set()

    def children(item: object) -> list:
        if isinstance(item, MappingNode):
            return [child for pair in item.value for child in pair]
        if isinstance(item, SequenceNode):
            return item.value
        return []

    def mark(item: object) -> None:
        if id(item) in shared:
            return
        shared.add(id(item))
        for child in children(item):
            mark(child)

    def visit(item: object) -> None:
        if id(item) in seen:
            mark(item)
            return
        seen.add(id(item))
        for child in children(item):
            visit(child)

    visit(node)
    return shared


def repair_text(text: str, timestamp: str, mim_pin: str) -> tuple[str, list[dict]]:
    """Patch parsed YAML coordinates, preserving all unrelated bytes and history."""
    doc = yaml.safe_load(text)
    expected = copy.deepcopy(doc)
    composed = yaml.compose(text)
    root = _fields(composed)
    shared = _shared_nodes(composed)

    def require_unshared(node: object) -> None:
        if id(node) in shared:
            raise ValueError("Refusing to edit an aliased YAML node")

    edits: list[tuple[int, int, str]] = []
    changes = []
    for field in ("ingredients", "composition"):
        if field not in root:
            continue
        sequence = root[field][1]
        if not isinstance(sequence, SequenceNode):
            raise ValueError(f"{field} must be a list")
        for index, node in enumerate(sequence.value):
            fields = _fields(node)
            row = expected[field][index]
            name = row.get("preferred_term")
            for slot in ("term", "chebi_term"):
                term = row.get(slot) or {}
                old = term.get("id")
                target = CORRECTIONS.get((name, old))
                if target is None:
                    continue
                identifier, label = target
                key_node, term_node = fields[slot]
                if slot == "chebi_term":
                    require_unshared(term_node)
                    source_id = (row.get("term") or {}).get("id", "")
                    if not source_id.startswith("mediadive.compound:"):
                        raise ValueError("Refusing to remove chebi_term without a source ID")
                    # Marks include the next token's indentation; remove complete
                    # lines but leave that token and its indentation untouched.
                    start = key_node.start_mark.index - key_node.start_mark.column
                    end = term_node.end_mark.index - term_node.end_mark.column
                    edits.append((start, end, ""))
                    del row[slot]
                else:
                    term_fields = _fields(term_node)
                    for key, value in (("id", identifier), ("label", label)):
                        scalar = term_fields[key][1]
                        require_unshared(scalar)
                        if not isinstance(scalar, ScalarNode):
                            raise ValueError(f"{slot}.{key} must be a scalar")
                        edits.append((scalar.start_mark.index, scalar.end_mark.index, value))
                        term[key] = value
                changes.append(
                    {
                        "recipe_id": doc["id"],
                        "json_pointer": f"/{field}/{index}/{slot}/id",
                        "preferred_term": name,
                        "rejected_id": old,
                        "resolved_id": identifier,
                        "operation": (
                            "remove_chebi_term" if slot == "chebi_term" else "replace_term"
                        ),
                    }
                )
    if not changes:
        return text, []
    details = "; ".join(
        f"{row['json_pointer']}: {row['preferred_term']} {row['rejected_id']} -> "
        f"{row['resolved_id']} ({row['operation']})"
        for row in changes
    )
    event = {
        "timestamp": timestamp,
        "curator": "repair_rejected_peptone_groundings.py",
        "action": ACTION,
        "notes": (
            f"CultureMech #484. {details}. Reviewed identities: {MIM_SOURCE}. "
            f"Publication resolver: MIM label index {mim_pin}. "
            "MediaDive source IDs and concentrations preserved."
        ),
    }
    expected.setdefault("curation_history", []).append(event)
    newline = "\r\n" if "\r\n" in text else "\n"
    event_text = dump_record({"curation_history": [event]}).replace("\n", newline)
    if "curation_history" in root:
        history = root["curation_history"][1]
        require_unshared(history)
        if not isinstance(history, SequenceNode) or history.flow_style:
            raise ValueError("Expected block-style curation_history")
        position = history.end_mark.index - history.end_mark.column
        indent = " " * history.start_mark.column
        addition = "".join(indent + line for line in event_text.splitlines(keepends=True)[1:])
        edits.append((position, position, addition))
    else:
        edits.append((len(text), len(text), ("" if text.endswith("\n") else newline) + event_text))

    result = text
    for start, end, replacement in sorted(edits, reverse=True):
        result = result[:start] + replacement + result[end:]
    if yaml.safe_load(result) != expected:
        raise ValueError("YAML patch changed data outside the planned correction")
    return result, changes


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    parser.add_argument("--expect-count", type=int)
    parser.add_argument("--report", type=Path)
    args = parser.parse_args(argv)
    pending = []
    rows = []
    try:
        mim_pin = verify_mim()
        paths = sorted(args.normalized_dir.rglob("*.yaml"))
        if not paths:
            raise ValueError(f"No YAML records under {args.normalized_dir}")
        if args.report:
            report_path = args.report.resolve()
            if report_path.is_relative_to(args.normalized_dir.resolve()) or any(
                report_path == path.resolve()
                or (args.report.exists() and args.report.samefile(path))
                for path in paths
            ):
                raise ValueError("Report path must not overlap the normalized recipe directory")
        timestamp = datetime.now(timezone.utc).isoformat()
        for path in paths:
            original_bytes = path.read_bytes()
            original = original_bytes.decode("utf-8")
            if not any(old in original for _name, old in CORRECTIONS):
                continue
            result, changes = repair_text(original, timestamp, mim_pin)
            if not changes:
                continue
            source = path.relative_to(args.normalized_dir).as_posix()
            before = hashlib.sha256(original_bytes).hexdigest()
            after = hashlib.sha256(result.encode()).hexdigest()
            rows.extend(
                dict(change, source_path=source, before_sha256=before, after_sha256=after)
                for change in changes
            )
            pending.append((path, original_bytes, result.encode("utf-8")))
        if args.expect_count is not None and len(rows) != args.expect_count:
            raise ValueError(f"Expected {args.expect_count} assignments, found {len(rows)}")
    except (OSError, ValueError, KeyError, TypeError, yaml.YAMLError) as exc:
        print(f"ERROR: {exc}; no recipe files written", file=sys.stderr)
        return 2

    written = 0
    try:
        if args.apply:
            for path, original_bytes, _result in pending:
                if path.read_bytes() != original_bytes:
                    raise OSError(f"Recipe changed after preflight: {path}")
            for path, _original_bytes, result in pending:
                path.write_bytes(result)
                written += 1
        if args.report:
            args.report.parent.mkdir(parents=True, exist_ok=True)
            args.report.write_text(
                json.dumps(
                    {
                        "applied": args.apply,
                        "mim_source": MIM_SOURCE,
                        "mim_label_index_commit": mim_pin,
                        "assignment_count": len(rows),
                        "record_count": len(pending),
                        "assignments": rows,
                    },
                    indent=2,
                )
                + "\n",
                encoding="utf-8",
            )
    except OSError as exc:
        print(f"ERROR after writing {written}/{len(pending)} recipes: {exc}", file=sys.stderr)
        return 1
    print(
        f"{'Corrected' if args.apply else 'Would correct'} {len(rows)} assignments in {len(pending)} records"
    )
    for (name, operation), count in sorted(
        Counter((r["preferred_term"], r["operation"]) for r in rows).items()
    ):
        print(f"  {count} {name}: {operation}")
    print(f"Skipped {len(paths) - len(pending)} unchanged records; failed 0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
