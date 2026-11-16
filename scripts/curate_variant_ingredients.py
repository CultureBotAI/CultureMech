#!/usr/bin/env python3
"""Apply explicit, source-bound variant ingredient decisions for CultureMech #683.

2026-11-16. Inputs: reviewed JSON decisions and authoritative recipe YAML.
Outputs: preview/apply receipt; apply adds only variant changes and history.
This does not extract chemical identities from prose or refresh the MIM index.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
import sys
import tempfile
import uuid
from pathlib import Path
from typing import Any

import yaml

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe, write_validated_recipe

ROOT = Path(__file__).resolve().parents[1]
ACTION = "STRUCTURED_VARIANT_INGREDIENTS"


class ApplyError(ValueError):
    """A failed apply retains observed per-record outcomes (#758)."""

    def __init__(self, message: str, receipt: dict[str, Any]):
        super().__init__(message)
        self.receipt = receipt


def persist_receipt(path: Path, receipt: dict[str, Any]) -> None:
    """Replace an existing reserved receipt without losing its previous state."""
    fd, name = tempfile.mkstemp(prefix=".variant-receipt-", dir=path.parent)
    stage = Path(name)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(receipt, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(stage, path)
    finally:
        stage.unlink(missing_ok=True)


def digest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def render_additions(before: bytes, desired: dict[str, Any], changes: list[dict]) -> bytes:
    """Insert only new fields/events at parsed block boundaries, preserving source bytes.

    Existing scalar spelling, comments and wrapping are never reserialized. The
    complete parsed result must equal the native-validated proposal; unsupported
    flow/alias layouts fail rather than invoking an approximate text rewrite.
    """
    text = before.decode("utf-8")
    tree = yaml.compose(text)
    if not isinstance(tree, yaml.MappingNode) or tree.flow_style:
        raise ValueError("source must be a block-style YAML record")

    def fields(node):
        if not isinstance(node, yaml.MappingNode) or node.flow_style:
            raise ValueError("selected variant must be a block-style YAML mapping")
        result = {}
        for key, value in node.value:
            if not isinstance(key, yaml.ScalarNode) or key.value in result:
                raise ValueError("ambiguous YAML mapping keys")
            result[key.value] = value
        return result

    root_fields = fields(tree)
    variants = root_fields["variants"]
    if not isinstance(variants, yaml.SequenceNode) or variants.flow_style:
        raise ValueError("variants must use block-style YAML")
    insertions: dict[int, list[str]] = {}

    def insert(node, fragment, indent):
        if node.flow_style:
            raise ValueError("selected YAML sequence must use block style")
        position = node.end_mark.index
        # A block can end at the next indented sequence item. Insert before
        # that line's indentation, never inside a scalar or existing token.
        line_start = text.rfind("\n", 0, position) + 1
        if position < len(text):
            if text[line_start:position].strip():
                raise ValueError("unsupported YAML insertion boundary")
            position = line_start
        rendered = yaml.safe_dump(fragment, sort_keys=False, allow_unicode=True)
        rendered = "".join(
            " " * indent + line if line.strip() else line
            for line in rendered.splitlines(keepends=True)
        )
        insertions.setdefault(position, []).append(rendered)

    for item in changes:
        node = variants.value[item["variant_index"]]
        if "ingredient_changes" in fields(node):
            raise ValueError("ingredient_changes already exists, including an empty field")
        insert(node, {"ingredient_changes": item["ingredient_changes"]}, node.start_mark.column)
    event = desired["curation_history"][-1]
    history = root_fields.get("curation_history")
    if history is None:
        insert(tree, {"curation_history": [event]}, 0)
    elif isinstance(history, yaml.SequenceNode):
        insert(history, [event], history.start_mark.column)
    else:
        raise ValueError("curation_history must be a YAML sequence")
    # At EOF the last variant and absent root history share a boundary;
    # preserve their construction order (variant field, then root field).
    for position, fragments in sorted(insertions.items(), reverse=True):
        prefix = "\n" if position and text[position - 1] != "\n" else ""
        addition = prefix + "".join(fragments)
        text = text[:position] + addition + text[position:]
    if yaml.safe_load(text) != desired:
        raise ValueError("presentation-preserving additions differ from validated proposal")
    return text.encode("utf-8")


def recipe_path(root: Path, relative: str) -> Path:
    path = root / relative
    if Path(relative).is_absolute() or ".." in Path(relative).parts:
        raise ValueError("recipe path must be relative without parent traversal")
    authority = (root / "data" / "normalized_yaml").resolve()
    if not path.resolve().is_relative_to(authority) or path.is_symlink():
        raise ValueError("recipe path must be an authoritative non-symlink YAML")
    if path.suffix != ".yaml":
        raise ValueError("recipe path must name a YAML record")
    return path


def plan_record(root: Path, decision: dict[str, Any], decision_digest: str) -> dict[str, Any]:
    path = recipe_path(root, decision["path"])
    before = path.read_bytes()
    # Aliases share object identity after safe_load/deepcopy. Selecting one
    # variant could otherwise mutate an unselected sibling through its anchor.
    if any(isinstance(token, (yaml.AliasToken, yaml.AnchorToken)) for token in yaml.scan(before)):
        raise ValueError("YAML aliases and anchors are not supported for scoped curation")
    record = yaml.safe_load(before)
    if not isinstance(record, dict) or record.get("id") != decision["recipe_id"]:
        raise ValueError(f"record identity mismatch: {decision['path']}")
    desired = copy.deepcopy(record)
    changes: list[dict[str, Any]] = []
    seen_indices: set[int] = set()
    for item in decision["variants"]:
        index = item["variant_index"]
        if type(index) is not int or index < 0 or index in seen_indices:
            raise ValueError("variant indexes must be unique nonnegative integers")
        seen_indices.add(index)
        variants = desired.get("variants", [])
        if index >= len(variants) or variants[index].get("name") != item["variant_name"]:
            raise ValueError(f"variant identity mismatch: {decision['path']} index {index}")
        variant = variants[index]
        requested = item["ingredient_changes"]
        if not isinstance(requested, list) or not requested:
            raise ValueError("each selected variant needs explicit ingredient changes")
        for change in requested:
            source_index = change["source_modification_index"]
            modifications = variant.get("modifications", [])
            if (
                type(source_index) is not int
                or source_index < 0
                or source_index >= len(modifications)
                or modifications[source_index] != change["source_text"]
            ):
                raise ValueError("source modification text/index mismatch")
        existing = variant.get("ingredient_changes", [])
        if existing == requested:
            continue
        if existing:
            raise ValueError("refusing to replace previously curated ingredient changes")
        variant["ingredient_changes"] = copy.deepcopy(requested)
        changes.append(
            {
                "variant_index": index,
                "variant_name": item["variant_name"],
                "ingredient_changes": requested,
            }
        )
    result = {
        "path": decision["path"],
        "recipe_id": decision["recipe_id"],
        "before_sha256": digest(before),
        "changes": changes,
        "status": "PLANNED" if changes else "UNCHANGED",
    }
    if not changes:
        errors = validate_recipe(record)
        if errors:
            raise ValueError("existing matching record fails validation: " + errors[0].message)
        return {"receipt": result, "path": path, "before": before, "record": record}
    if digest(before) != decision["expected_sha256"]:
        raise ValueError(f"source hash mismatch: {decision['path']}")
    record_curation_event(
        desired,
        curator="codex",
        action=ACTION,
        notes="Represent source-supported ingredient changes within their existing variants; "
        "preserve base formulation, source prose, stages and unresolved identities. "
        "LLM-assisted curation; no human review status asserted.",
        source="https://github.com/CultureBotAI/CultureMech/issues/683",
        changes=json.dumps(
            {"decision_sha256": decision_digest, "variants": changes},
            ensure_ascii=False,
            sort_keys=True,
        ),
    )
    errors = validate_recipe(desired)
    if errors:
        raise ValueError("proposed record fails validation: " + errors[0].message)
    rendered = render_additions(before, desired, changes)
    return {
        "receipt": result,
        "path": path,
        "before": before,
        "record": desired,
        "rendered": rendered,
    }


def run(
    decisions: Path,
    *,
    root: Path = ROOT,
    apply: bool = False,
    receipt: Path | None = None,
    only_record: str | None = None,
) -> dict[str, Any]:
    raw = decisions.read_bytes()
    document = json.loads(raw)
    if document.get("schema_version") != 1 or not document.get("records"):
        raise ValueError("expected schema_version 1 and a nonempty records list")
    decision_digest = digest(raw)
    paths = [item["path"] for item in document["records"]]
    if len(set(paths)) != len(paths):
        raise ValueError("duplicate record decisions")
    if only_record is not None and only_record not in paths:
        raise ValueError("selected record is absent from decisions")
    # Validate the entire selected plan before its first write.
    plans = [
        plan_record(root, item, decision_digest)
        for item in document["records"]
        if only_record is None or item["path"] == only_record
    ]
    result = {
        "schema_version": 1,
        "mode": "apply" if apply else "preview",
        "decision_sha256": decision_digest,
        "only_record": only_record,
        "records": [plan["receipt"] for plan in plans],
    }
    if apply and receipt is None:
        receipt = root / ".temp" / "variant-curation-receipts" / (str(uuid.uuid4()) + ".json")
    if receipt is not None:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        result["receipt_path"] = str(receipt)
        # Reserve and prove receipt persistence before any authoritative mutation.
        with receipt.open("x", encoding="utf-8") as stream:
            json.dump(result, stream, ensure_ascii=False, indent=2)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
    if not apply:
        return result
    try:
        for plan in plans:
            row = plan["receipt"]
            if row["status"] != "PLANNED":
                continue
            # Same filesystem, non-YAML suffix: incomplete staging is never corpus input.
            fd, name = tempfile.mkstemp(prefix=".variant-", suffix=".tmp", dir=plan["path"].parent)
            os.close(fd)
            stage = Path(name)
            try:
                write_validated_recipe(plan["record"], stage)
                actual = stage.read_bytes()
                if yaml.safe_load(actual) != plan["record"]:
                    raise ValueError("staged record differs from validated proposal")
                # The native writer validated exactly this semantic document.
                # Publish the equivalent source-preserving rendering, not its
                # canonical reserialization of unrelated existing fields.
                actual = plan["rendered"]
                stage.write_bytes(actual)
                if yaml.safe_load(stage.read_bytes()) != plan["record"]:
                    raise ValueError("source-preserving stage differs from validated proposal")
                stage.chmod(plan["path"].stat().st_mode & 0o777)
                with stage.open("rb") as stream:
                    os.fsync(stream.fileno())
                row["planned_after_sha256"] = digest(actual)
                row["status"] = "APPLYING"
                persist_receipt(receipt, result)
                if plan["path"].read_bytes() != plan["before"]:
                    raise ValueError("record changed after preview: " + row["path"])
                os.replace(stage, plan["path"])
                row["status"] = "APPLIED"
                row["after_sha256"] = digest(plan["path"].read_bytes())
                if row["after_sha256"] != row["planned_after_sha256"]:
                    raise ValueError("published record differs from staged bytes")
                persist_receipt(receipt, result)
            finally:
                stage.unlink(missing_ok=True)
        result["state"] = "COMPLETE"
        persist_receipt(receipt, result)
    except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
        result["state"] = "INCOMPLETE"
        result["error"] = str(exc)
        # Observe every target, including a replace followed by a receipt failure.
        for plan in plans:
            try:
                plan["receipt"]["observed_sha256"] = digest(plan["path"].read_bytes())
            except OSError as read_error:
                plan["receipt"]["observation_error"] = str(read_error)
        try:
            persist_receipt(receipt, result)
        except OSError as receipt_error:
            result["receipt_write_error"] = str(receipt_error)
        raise ApplyError(str(exc), result) from exc
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("decisions", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--receipt", type=Path)
    parser.add_argument(
        "--only-record", help="Select exactly one decision path for an end-to-end canary"
    )
    args = parser.parse_args()
    if args.receipt and args.receipt.exists():
        parser.error("receipt destination already exists; choose a new path")
    try:
        result = run(
            args.decisions, apply=args.apply, receipt=args.receipt, only_record=args.only_record
        )
    except ApplyError as exc:
        print(json.dumps(exc.receipt, ensure_ascii=False, indent=2), file=sys.stderr)
        return 1
    except (OSError, ValueError, KeyError, TypeError, IndexError) as exc:
        print(json.dumps({"state": "REFUSED", "error": str(exc)}), file=sys.stderr)
        return 1
    text = json.dumps(result, ensure_ascii=False, indent=2) + "\n"
    print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
