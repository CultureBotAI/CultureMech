#!/usr/bin/env python3
"""Apply reviewed #683 follow-ups without rewriting unrelated source bytes.

2026-11-16. Inputs: exact hash-bound additive/correction decisions, optionally
a separately pinned completed receipt for replay. Outputs: preview or durable
native-writer apply receipt with before/after evidence. No inferred chemistry.
"""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

import yaml
from curate_variant_ingredients import ApplyError, digest, recipe_path, run

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
ACTION = "VARIANT_INGREDIENT_COMPLETENESS"


def value_at(value, path):
    for key in path:
        value = value[key]
    return value


def apply_decision(record, decision):
    """Compute only explicitly approved semantic changes; never infer a quantity."""
    if set(decision) - {"path", "recipe_id", "expected_sha256", "variants", "field_replacements"}:
        raise ValueError("unknown record mutation instruction")
    desired = copy.deepcopy(record)
    operations = []
    seen_variants = set()
    for item in decision.get("variants", []):
        if set(item) - {
            "variant_index",
            "variant_name",
            "replace_modifications",
            "replace_changes",
            "append_changes",
            "append_mentions",
        }:
            raise ValueError("unknown variant mutation instruction")
        index = item["variant_index"]
        if type(index) is not int or index < 0 or index in seen_variants:
            raise ValueError("variant indices must be unique nonnegative integers")
        seen_variants.add(index)
        variant = desired["variants"][index]
        if variant["name"] != item["variant_name"]:
            raise ValueError("variant name does not match the pinned record")
        prefix = ["variants", index]
        for key, target, coordinate in (
            ("replace_modifications", "modifications", "modification_index"),
            ("replace_changes", "ingredient_changes", "change_index"),
        ):
            seen = set()
            for replacement in item.get(key, []):
                if set(replacement) != {coordinate, "expected", "replacement"}:
                    raise ValueError("unknown or incomplete replacement instruction")
                number = replacement[coordinate]
                if type(number) is not int or number < 0 or number in seen:
                    raise ValueError("replacement indices must be unique nonnegative integers")
                seen.add(number)
                if variant[target][number] != replacement["expected"]:
                    raise ValueError("replacement beforeimage does not match")
                if replacement["expected"] == replacement["replacement"]:
                    raise ValueError("no-op replacements are forbidden")
                variant[target][number] = copy.deepcopy(replacement["replacement"])
                operations.append(
                    ("replace_item", prefix + [target, number], replacement["replacement"])
                )
        for key, target in (
            ("append_changes", "ingredient_changes"),
            ("append_mentions", "ingredient_mentions"),
        ):
            additions = item.get(key, [])
            if not isinstance(additions, list):
                raise ValueError("additions must be explicit lists")
            if additions:
                if target in variant:
                    variant[target].extend(copy.deepcopy(additions))
                    operations.append(("append", prefix + [target], additions))
                else:
                    variant[target] = copy.deepcopy(additions)
                    operations.append(("insert_field", prefix, {target: additions}))
    replaced_paths = set()
    for item in decision.get("field_replacements", []):
        if set(item) != {"path", "expected", "replacement"}:
            raise ValueError("unknown or incomplete field replacement instruction")
        path = item["path"]
        if (
            not isinstance(path, list)
            or not path
            or any(type(part) not in (str, int) for part in path)
        ):
            raise ValueError("field path must be explicit string/integer coordinates")
        key = tuple(path)
        if key in replaced_paths:
            raise ValueError("duplicate field replacement")
        replaced_paths.add(key)
        allowed = (
            (
                len(path) >= 3
                and path[0] == "variants"
                and type(path[1]) is int
                and path[1] in seen_variants
                and path[2] in {"description", "purpose", "evidence"}
            )
            or path == ["target_organisms"]
            or (
                len(path) >= 4
                and path[0] == "target_organisms"
                and type(path[1]) is int
                and path[1] >= 0
                and path[2] == "evidence"
            )
        )
        if not allowed:
            raise ValueError("field replacement is outside reviewed variant/growth evidence scope")
        previous = value_at(desired, path)
        if previous != item["expected"] or previous == item["replacement"]:
            raise ValueError("field replacement is stale or a no-op")
        if path == ["target_organisms"]:
            # Only one exact descriptor removal is authorized by this operation.
            if not isinstance(previous, list):
                raise ValueError("target-organism correction requires a list")
            candidates = [
                i
                for i in range(len(previous))
                if previous[:i] + previous[i + 1 :] == item["replacement"]
            ]
            if len(candidates) != 1:
                raise ValueError(
                    "target-organism correction must remove exactly one pinned descriptor"
                )
            if item["replacement"]:
                operations.append(("delete_item", path + [candidates[0]], None))
            else:
                operations.append(("replace_field", path, []))
        elif isinstance(path[-1], int):
            operations.append(("replace_item", path, item["replacement"]))
        else:
            operations.append(("replace_field", path, item["replacement"]))
        value_at(desired, path[:-1])[path[-1]] = copy.deepcopy(item["replacement"])
    if not operations:
        raise ValueError("decision contains no changes")
    return desired, operations


def render(before, desired, operations):
    text = before.decode("utf-8")
    if any(isinstance(token, (yaml.AliasToken, yaml.AnchorToken)) for token in yaml.scan(text)):
        raise ValueError("aliases and anchors cannot be mutated as scoped records")
    tree = yaml.compose(text)

    def fields(node):
        if not isinstance(node, yaml.MappingNode) or node.flow_style:
            raise ValueError("expected a block mapping")
        result = {}
        for key, value in node.value:
            if not isinstance(key, yaml.ScalarNode) or key.value in result:
                raise ValueError("duplicate or unsupported mapping key")
            result[key.value] = (key, value)
        return result

    def node_at(path):
        node = tree
        for part in path:
            node = node.value[part] if type(part) is int else fields(node)[part][1]
        return node

    def line_start(index):
        return text.rfind("\n", 0, index) + 1

    def end_boundary(node):
        end = node.end_mark.index
        start = line_start(end)
        if end == len(text):
            return end
        if not text[start:end].strip():
            return start
        # Scalar end marks point just after their last character, whereas a
        # block collection usually ends at the next field's indentation.
        # Include only the scalar's own trailing newline/comment, never the
        # following field or sequence item.
        newline = text.find("\n", end)
        stop = len(text) if newline == -1 else newline
        remainder = text[end:stop].strip()
        if remainder and not remainder.startswith("#"):
            raise ValueError("unsupported non-line YAML boundary")
        return stop if newline == -1 else stop + 1

    def fragment(value, indent):
        dumped = yaml.safe_dump(value, sort_keys=False, allow_unicode=True, width=80 - indent)
        return "".join(
            " " * indent + line if line.strip() else line
            for line in dumped.splitlines(keepends=True)
        )

    edits = []
    insertions = {}
    for kind, path, value in operations:
        node = node_at(path)
        if kind in {"append", "insert_field"}:
            if node.flow_style:
                raise ValueError("cannot append into a flow collection")
            position = end_boundary(node)
            insertions.setdefault(position, []).append(fragment(value, node.start_mark.column))
        elif kind in {"replace_item", "delete_item"}:
            start = line_start(node.start_mark.index)
            prefix = text[start : node.start_mark.index]
            if prefix.strip() != "-":
                raise ValueError("expected a block sequence item boundary")
            indent = prefix.index("-")
            edits.append(
                (
                    start,
                    end_boundary(node),
                    "" if kind == "delete_item" else fragment([value], indent),
                )
            )
        else:
            parent = node_at(path[:-1])
            key = fields(parent)[path[-1]][0]
            start = line_start(key.start_mark.index)
            if text[start : key.start_mark.index].strip():
                raise ValueError("field does not begin on its own line")
            edits.append(
                (start, end_boundary(node), fragment({path[-1]: value}, key.start_mark.column))
            )
    for position, parts in insertions.items():
        prefix = "\n" if position and text[position - 1] != "\n" else ""
        edits.append((position, position, prefix + "".join(parts)))
    ordered = sorted(edits, key=lambda item: (item[0], item[1]))
    for first, second in zip(ordered, ordered[1:], strict=False):
        if second[0] < first[1]:
            raise ValueError("overlapping source edits are forbidden")
    for start, end, addition in reversed(ordered):
        text = text[:start] + addition + text[end:]
    if yaml.safe_load(text) != desired:
        raise ValueError("source-preserving rendering differs from the validated proposal")
    return text.encode("utf-8")


def plan_record(root, decision, decision_sha256, completed=None, completed_decision_sha256=None):
    if completed and decision_sha256 != completed_decision_sha256:
        raise ValueError("current proposal differs from completed receipt proposal pin")
    path = recipe_path(root, decision["path"])
    before = path.read_bytes()
    record = yaml.safe_load(before)
    if not isinstance(record, dict) or record.get("id") != decision["recipe_id"]:
        raise ValueError("recipe identity mismatch")
    row = {
        "path": decision["path"],
        "recipe_id": decision["recipe_id"],
        "before_sha256": digest(before),
    }
    if completed and decision["path"] in completed:
        previous = completed[decision["path"]]
        if previous["before_sha256"] != decision["expected_sha256"] or previous[
            "after_sha256"
        ] != digest(before):
            raise ValueError("completed receipt does not match exact current/before bytes")
        if validate_recipe(record):
            raise ValueError("completed record fails native validation")
        row.update(
            status="UNCHANGED",
            before_sha256=previous["before_sha256"],
            after_sha256=previous["after_sha256"],
            before_text=previous["before_text"],
            after_text=previous["after_text"],
            planned_after_sha256=previous["after_sha256"],
        )
        return {"receipt": row, "path": path, "before": before, "record": record}
    if digest(before) != decision["expected_sha256"]:
        raise ValueError(
            "source hash mismatch; replay requires its independently pinned completed receipt"
        )
    desired, operations = apply_decision(record, decision)
    record_curation_event(
        desired,
        curator="codex",
        action=ACTION,
        notes="LLM-assisted reviewed variant ingredient amounts, unresolved names and exact source corrections; no human review status asserted.",
        source="https://github.com/CultureBotAI/CultureMech/issues/683",
        changes=json.dumps(
            {"decision_sha256": decision_sha256, "decision": decision},
            ensure_ascii=False,
            sort_keys=True,
        ),
    )
    if "curation_history" in record:
        operations.append(("append", ["curation_history"], [desired["curation_history"][-1]]))
    else:
        operations.append(("insert_field", [], {"curation_history": desired["curation_history"]}))
    errors = validate_recipe(desired)
    if errors:
        raise ValueError("proposed record fails native validation: " + errors[0].message)
    rendered = render(before, desired, operations)
    row.update(
        status="PLANNED",
        before_text=before.decode("utf-8"),
        after_text=rendered.decode("utf-8"),
        planned_after_sha256=digest(rendered),
    )
    return {"receipt": row, "path": path, "before": before, "record": desired, "rendered": rendered}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("decisions", type=Path)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--receipt", type=Path, required=True)
    parser.add_argument("--only-record")
    parser.add_argument("--completed-receipt", type=Path)
    parser.add_argument("--expected-completed-receipt-sha256")
    args = parser.parse_args()
    completed = {}
    completed_pin = None
    if bool(args.completed_receipt) != bool(args.expected_completed_receipt_sha256):
        parser.error(
            "completed receipt and independently recorded digest must be supplied together"
        )
    if args.completed_receipt:
        raw = args.completed_receipt.read_bytes()
        previous = json.loads(raw)
        if (
            digest(raw) != args.expected_completed_receipt_sha256
            or previous.get("state") != "COMPLETE"
            or previous.get("mode") != "apply"
            or previous.get("decision_sha256") != digest(args.decisions.read_bytes())
        ):
            raise ValueError(
                "completed receipt is not the pinned successful application of this proposal"
            )
        completed = {
            row["path"]: row
            for row in previous["records"]
            if row["status"] in {"APPLIED", "UNCHANGED"}
        }
        if len(completed) != len(previous["records"]):
            raise ValueError("completed receipt contains an unfinished record")
        for row in completed.values():
            if (
                digest(row["before_text"].encode()) != row["before_sha256"]
                or digest(row["after_text"].encode()) != row["after_sha256"]
            ):
                raise ValueError("completed receipt text does not match its digest")
        completed_pin = previous["decision_sha256"]
    try:
        result = run(
            args.decisions,
            root=ROOT,
            apply=args.apply,
            receipt=args.receipt,
            only_record=args.only_record,
            planner=lambda root, item, pin: plan_record(root, item, pin, completed, completed_pin),
        )
    except ApplyError as exc:
        print(json.dumps({"state": "INCOMPLETE", "error": str(exc), "receipt": str(args.receipt)}))
        return 1
    print(
        json.dumps(
            {
                "state": result.get("state", "PREVIEW"),
                "records": len(result["records"]),
                "receipt": str(args.receipt),
            }
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
