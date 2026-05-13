#!/usr/bin/env python3
"""Apply or dry-run proposed parent/child media-variant links."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml as pyyaml

try:
    from ruamel.yaml import YAML as RuamelYAML
except ImportError:  # pragma: no cover - exercised only outside the uv env
    RuamelYAML = None

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_PROPOSALS = REPO_ROOT / "reports" / "media_variant_link_proposals.tsv"
REPORTS_DIR = REPO_ROOT / "reports"
DRY_RUN_JSON = REPORTS_DIR / "media_variant_link_apply_plan.json"
DRY_RUN_TSV = REPORTS_DIR / "media_variant_link_apply_plan.tsv"
ROUND_TRIP_YAML = RuamelYAML() if RuamelYAML else None
if ROUND_TRIP_YAML:
    ROUND_TRIP_YAML.default_flow_style = False
    ROUND_TRIP_YAML.preserve_quotes = True

PLAN_COLUMNS = [
    "action",
    "relationship",
    "confidence",
    "parent_path",
    "child_path",
    "status",
    "message",
]


def load_yaml(path: Path) -> dict[str, Any]:
    if ROUND_TRIP_YAML:
        data = ROUND_TRIP_YAML.load(path) or {}
    else:
        data = pyyaml.safe_load(path.read_text()) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{path} is not a YAML mapping")
    return data


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    if ROUND_TRIP_YAML:
        with path.open("w") as handle:
            ROUND_TRIP_YAML.dump(data, handle)
        path.write_text("\n".join(line.rstrip() for line in path.read_text().splitlines()) + "\n")
    else:
        path.write_text(pyyaml.safe_dump(data, sort_keys=False, allow_unicode=True))


def read_proposals(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def include_proposal(row: dict[str, str], args: argparse.Namespace) -> bool:
    if args.status and row.get("status") not in args.status:
        return False
    if args.confidence and row.get("confidence") not in args.confidence:
        return False
    if args.relationship and row.get("relationship") not in args.relationship:
        return False
    if args.signature and row.get("ingredient_identity_signature") not in args.signature:
        return False
    return True


def recipe_ref(path: str, recipe: dict[str, Any], relationship: str, notes: str = "") -> dict[str, Any]:
    ref = {
        "path": path,
        "relationship": relationship,
    }
    if recipe.get("id"):
        ref["id"] = recipe["id"]
    if recipe.get("name"):
        ref["name"] = recipe["name"]
    if notes:
        ref["notes"] = notes
    return ref


def ref_matches(ref: dict[str, Any], path: str, recipe_id: str | None) -> bool:
    return ref.get("path") == path or (recipe_id and ref.get("id") == recipe_id)


def plan_links(rows: list[dict[str, str]], args: argparse.Namespace) -> list[dict[str, str]]:
    selected = [row for row in rows if include_proposal(row, args)]
    if args.limit is not None:
        selected = selected[: args.limit]

    plans: list[dict[str, str]] = []
    recipes: dict[str, dict[str, Any]] = {}
    dirty: set[str] = set()

    def recipe_for(rel_path: str) -> dict[str, Any]:
        if rel_path not in recipes:
            recipes[rel_path] = load_yaml(REPO_ROOT / rel_path)
        return recipes[rel_path]

    grouped_by_parent: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in selected:
        grouped_by_parent[row["parent_path"]].append(row)

    for parent_path, links in grouped_by_parent.items():
        parent = recipe_for(parent_path)
        parent_children = parent.setdefault("variant_children", [])
        if not isinstance(parent_children, list):
            plans.append(
                {
                    "action": "skip_parent",
                    "relationship": "",
                    "confidence": "",
                    "parent_path": parent_path,
                    "child_path": "",
                    "status": "ERROR",
                    "message": "parent variant_children exists but is not a list",
                }
            )
            continue

        for row in links:
            child_path = row["child_path"]
            relationship = row["relationship"]
            child = recipe_for(child_path)
            child_id = str(child.get("id") or "")
            parent_id = str(parent.get("id") or "")
            child_notes = row.get("modifications") or ""

            child_ref_exists = any(ref_matches(ref, child_path, child_id) for ref in parent_children if isinstance(ref, dict))
            if not child_ref_exists:
                parent_children.append(recipe_ref(child_path, child, relationship, child_notes))
                dirty.add(parent_path)
                plans.append(
                    {
                        "action": "add_variant_child",
                        "relationship": relationship,
                        "confidence": row.get("confidence", ""),
                        "parent_path": parent_path,
                        "child_path": child_path,
                        "status": "PLANNED",
                        "message": "add child reference to parent",
                    }
                )

            parent_media = child.get("parent_media")
            if parent_media and isinstance(parent_media, dict) and not ref_matches(parent_media, parent_path, parent_id):
                plans.append(
                    {
                        "action": "skip_child_parent_conflict",
                        "relationship": relationship,
                        "confidence": row.get("confidence", ""),
                        "parent_path": parent_path,
                        "child_path": child_path,
                        "status": "ERROR",
                        "message": "child already links to a different parent",
                    }
                )
                continue

            if not isinstance(parent_media, dict):
                child["parent_media"] = recipe_ref(parent_path, parent, relationship, row.get("review_reason", ""))
                dirty.add(child_path)
                plans.append(
                    {
                        "action": "add_parent_media",
                        "relationship": relationship,
                        "confidence": row.get("confidence", ""),
                        "parent_path": parent_path,
                        "child_path": child_path,
                        "status": "PLANNED",
                        "message": "add parent reference to child",
                    }
                )

            if child.get("variant_relationship") != relationship:
                child["variant_relationship"] = relationship
                dirty.add(child_path)
                plans.append(
                    {
                        "action": "set_variant_relationship",
                        "relationship": relationship,
                        "confidence": row.get("confidence", ""),
                        "parent_path": parent_path,
                        "child_path": child_path,
                        "status": "PLANNED",
                        "message": "set child variant relationship",
                    }
                )

            modification = row.get("modifications") or ""
            if modification:
                modifications = child.setdefault("variant_modifications", [])
                if not isinstance(modifications, list):
                    plans.append(
                        {
                            "action": "skip_variant_modifications",
                            "relationship": relationship,
                            "confidence": row.get("confidence", ""),
                            "parent_path": parent_path,
                            "child_path": child_path,
                            "status": "ERROR",
                            "message": "child variant_modifications exists but is not a list",
                        }
                    )
                elif modification not in modifications:
                    modifications.append(modification)
                    dirty.add(child_path)
                    plans.append(
                        {
                            "action": "add_variant_modification",
                            "relationship": relationship,
                            "confidence": row.get("confidence", ""),
                            "parent_path": parent_path,
                            "child_path": child_path,
                            "status": "PLANNED",
                            "message": "add child modification summary",
                        }
                    )

    if args.apply:
        for rel_path in sorted(dirty):
            write_yaml(REPO_ROOT / rel_path, recipes[rel_path])

    return plans


def write_plan(plans: list[dict[str, str]], reports_dir: Path) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    with DRY_RUN_TSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=PLAN_COLUMNS, delimiter="\t")
        writer.writeheader()
        writer.writerows(plans)
    DRY_RUN_JSON.write_text(json.dumps(plans, indent=2, sort_keys=True) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--proposals", type=Path, default=DEFAULT_PROPOSALS)
    parser.add_argument("--status", action="append", default=["PROPOSED"])
    parser.add_argument("--confidence", action="append", default=["HIGH"])
    parser.add_argument("--relationship", action="append")
    parser.add_argument("--signature", action="append")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--reports-dir", type=Path, default=REPORTS_DIR)
    parser.add_argument("--apply", action="store_true", help="Write YAML edits. Default is dry-run.")
    args = parser.parse_args()

    rows = read_proposals(args.proposals)
    plans = plan_links(rows, args)
    write_plan(plans, args.reports_dir)

    status_counts = Counter(plan["status"] for plan in plans)
    action_counts = Counter(plan["action"] for plan in plans)
    print(f"Mode: {'APPLY' if args.apply else 'DRY-RUN'}")
    print(f"Plan actions: {len(plans)}")
    for action, count in sorted(action_counts.items()):
        print(f"  {action}: {count}")
    for status, count in sorted(status_counts.items()):
        print(f"  status {status}: {count}")
    print(f"Wrote {DRY_RUN_TSV.relative_to(REPO_ROOT)}")
    print(f"Wrote {DRY_RUN_JSON.relative_to(REPO_ROOT)}")
    return 2 if status_counts.get("ERROR") else 0


if __name__ == "__main__":
    raise SystemExit(main())
