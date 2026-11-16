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
    # The native validated writer uses these exact corpus serialization options.
    # Refuse presentation drift before changing a record, rather than hiding it.
    baseline = yaml.safe_dump(
        record, sort_keys=False, allow_unicode=True, default_flow_style=False, width=80
    ).encode()
    if baseline != before:
        raise ValueError(f"native writer would reformat unchanged content: {decision['path']}")
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
    return {"receipt": result, "path": path, "before": before, "record": desired}


def run(
    decisions: Path, *, root: Path = ROOT, apply: bool = False, receipt: Path | None = None
) -> dict[str, Any]:
    raw = decisions.read_bytes()
    document = json.loads(raw)
    if document.get("schema_version") != 1 or not document.get("records"):
        raise ValueError("expected schema_version 1 and a nonempty records list")
    decision_digest = digest(raw)
    paths = [item["path"] for item in document["records"]]
    if len(set(paths)) != len(paths):
        raise ValueError("duplicate record decisions")
    # Validate the entire selected plan before its first write.
    plans = [plan_record(root, item, decision_digest) for item in document["records"]]
    result = {
        "schema_version": 1,
        "mode": "apply" if apply else "preview",
        "decision_sha256": decision_digest,
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
    args = parser.parse_args()
    if args.receipt and args.receipt.exists():
        parser.error("receipt destination already exists; choose a new path")
    try:
        result = run(args.decisions, apply=args.apply, receipt=args.receipt)
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
