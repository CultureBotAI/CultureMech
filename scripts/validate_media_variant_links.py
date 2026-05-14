#!/usr/bin/env python3
"""Validate parent/child media-variant links in normalized CultureMech YAMLs."""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
YAML_ROOT = REPO_ROOT / "data" / "normalized_yaml"
REPORTS_DIR = REPO_ROOT / "reports"
OUT_TSV = REPORTS_DIR / "media_variant_link_validation.tsv"
OUT_MD = REPORTS_DIR / "media_variant_link_validation.md"


@dataclass
class RecipeIndex:
    path_to_recipe: dict[str, dict[str, Any]]
    id_to_path: dict[str, str]


@dataclass
class Finding:
    severity: str
    yaml_path: str
    field: str
    reference: str
    message: str


def load_recipes(yaml_root: Path) -> RecipeIndex:
    path_to_recipe: dict[str, dict[str, Any]] = {}
    id_to_path: dict[str, str] = {}
    for path in sorted(yaml_root.rglob("*.yaml")):
        rel = str(path.relative_to(REPO_ROOT))
        try:
            recipe = yaml.safe_load(path.read_text()) or {}
        except Exception as exc:  # noqa: BLE001 - validator reports bad YAMLs.
            path_to_recipe[rel] = {"_load_error": str(exc)}
            continue
        if not isinstance(recipe, dict):
            path_to_recipe[rel] = {"_load_error": "top-level YAML is not a mapping"}
            continue
        path_to_recipe[rel] = recipe
        recipe_id = recipe.get("id")
        if recipe_id:
            id_to_path[str(recipe_id)] = rel
    return RecipeIndex(path_to_recipe=path_to_recipe, id_to_path=id_to_path)


def ref_key(ref: dict[str, Any]) -> str:
    return str(ref.get("id") or ref.get("path") or ref.get("name") or "").strip()


def resolve_ref(ref: dict[str, Any], index: RecipeIndex) -> str | None:
    path = ref.get("path")
    if isinstance(path, str) and path in index.path_to_recipe:
        return path
    recipe_id = ref.get("id")
    if isinstance(recipe_id, str):
        return index.id_to_path.get(recipe_id)
    return None


def child_links_parent(child_path: str, parent_path: str, index: RecipeIndex) -> bool:
    child = index.path_to_recipe.get(child_path) or {}
    parent_media = child.get("parent_media")
    if not isinstance(parent_media, dict):
        return False
    resolved_parent = resolve_ref(parent_media, index)
    return resolved_parent == parent_path


def parent_links_child(parent_path: str, child_path: str, index: RecipeIndex) -> bool:
    parent = index.path_to_recipe.get(parent_path) or {}
    for child_ref in parent.get("variant_children") or []:
        if not isinstance(child_ref, dict):
            continue
        if resolve_ref(child_ref, index) == child_path:
            return True
    return False


def validate_links(index: RecipeIndex) -> list[Finding]:
    findings: list[Finding] = []
    for path, recipe in index.path_to_recipe.items():
        if recipe.get("_load_error"):
            findings.append(
                Finding("ERROR", path, "yaml", "", f"YAML load error: {recipe['_load_error']}")
            )
            continue

        parent_media = recipe.get("parent_media")
        if parent_media is not None and not isinstance(parent_media, dict):
            findings.append(
                Finding("ERROR", path, "parent_media", "", "parent_media must be a mapping")
            )
        elif isinstance(parent_media, dict):
            resolved_parent = resolve_ref(parent_media, index)
            reference = ref_key(parent_media)
            if not resolved_parent:
                findings.append(
                    Finding("ERROR", path, "parent_media", reference, "parent_media does not resolve")
                )
            elif not parent_links_child(resolved_parent, path, index):
                findings.append(
                    Finding(
                        "ERROR",
                        path,
                        "parent_media",
                        reference,
                        "parent record does not link back to this child",
                    )
                )
            if not recipe.get("variant_relationship"):
                findings.append(
                    Finding(
                        "WARNING",
                        path,
                        "variant_relationship",
                        reference,
                        "child record has parent_media but no variant_relationship",
                    )
                )

        variant_children = recipe.get("variant_children") or []
        if variant_children and not isinstance(variant_children, list):
            findings.append(
                Finding("ERROR", path, "variant_children", "", "variant_children must be a list")
            )
            continue
        for child_ref in variant_children:
            if not isinstance(child_ref, dict):
                findings.append(
                    Finding("ERROR", path, "variant_children", "", "variant child must be a mapping")
                )
                continue
            resolved_child = resolve_ref(child_ref, index)
            reference = ref_key(child_ref)
            if not resolved_child:
                findings.append(
                    Finding(
                        "ERROR",
                        path,
                        "variant_children",
                        reference,
                        "variant child does not resolve",
                    )
                )
            elif not child_links_parent(resolved_child, path, index):
                findings.append(
                    Finding(
                        "ERROR",
                        path,
                        "variant_children",
                        reference,
                        "child record does not link back to this parent",
                    )
                )
    return findings


def count_links(index: RecipeIndex) -> tuple[int, int]:
    parent_links = 0
    child_links = 0
    for recipe in index.path_to_recipe.values():
        if isinstance(recipe.get("parent_media"), dict):
            child_links += 1
        variant_children = recipe.get("variant_children") or []
        if isinstance(variant_children, list):
            parent_links += sum(1 for item in variant_children if isinstance(item, dict))
    return parent_links, child_links


def write_reports(findings: list[Finding], index: RecipeIndex, reports_dir: Path) -> None:
    reports_dir.mkdir(parents=True, exist_ok=True)
    parent_links, child_links = count_links(index)
    errors = sum(1 for finding in findings if finding.severity == "ERROR")
    warnings = sum(1 for finding in findings if finding.severity == "WARNING")

    with OUT_TSV.open("w", newline="") as handle:
        writer = csv.writer(handle, delimiter="\t", lineterminator="\n")
        writer.writerow(["severity", "yaml_path", "field", "reference", "message"])
        for finding in findings:
            writer.writerow(
                [
                    finding.severity,
                    finding.yaml_path,
                    finding.field,
                    finding.reference,
                    finding.message,
                ]
            )

    lines = [
        "# Media Variant Link Validation",
        "",
        f"- YAML records scanned: {len(index.path_to_recipe):,}",
        f"- Parent-to-child links: {parent_links:,}",
        f"- Child-to-parent links: {child_links:,}",
        f"- Errors: {errors:,}",
        f"- Warnings: {warnings:,}",
        "",
    ]
    if findings:
        lines.extend(["## Findings", "", "| Severity | YAML | Field | Reference | Message |"])
        lines.append("|---|---|---|---|---|")
        for finding in findings[:100]:
            lines.append(
                f"| {finding.severity} | `{finding.yaml_path}` | `{finding.field}` | "
                f"`{finding.reference}` | {finding.message} |"
            )
        if len(findings) > 100:
            lines.append(f"\nOnly first 100 of {len(findings):,} findings are shown.")
    else:
        lines.append("No parent/child media-variant link problems found.")
    OUT_MD.write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--yaml-root", type=Path, default=YAML_ROOT)
    parser.add_argument("--reports-dir", type=Path, default=REPORTS_DIR)
    args = parser.parse_args()

    index = load_recipes(args.yaml_root)
    findings = validate_links(index)
    write_reports(findings, index, args.reports_dir)
    errors = sum(1 for finding in findings if finding.severity == "ERROR")
    warnings = sum(1 for finding in findings if finding.severity == "WARNING")
    parent_links, child_links = count_links(index)
    print(f"Scanned {len(index.path_to_recipe)} YAML records")
    print(f"Parent-to-child links: {parent_links}")
    print(f"Child-to-parent links: {child_links}")
    print(f"Errors: {errors}")
    print(f"Warnings: {warnings}")
    print(f"Wrote {OUT_TSV.relative_to(REPO_ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(REPO_ROOT)}")
    return 2 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
