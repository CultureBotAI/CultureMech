#!/usr/bin/env python3
"""Assess ingredient, concentration, and variant-modeling state for media YAMLs.

This is a corpus-audit script. It does not rewrite media records. It produces
record-level coverage and candidate variation groups that can be reviewed before
any parent/child YAML restructuring is attempted.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
YAML_ROOT = REPO_ROOT / "data" / "normalized_yaml"
REPORTS_DIR = REPO_ROOT / "reports"

RECORD_COLUMNS = [
    "yaml_path",
    "category_dir",
    "id",
    "name",
    "original_name",
    "media_term_id",
    "medium_type",
    "physical_state",
    "ingredient_count",
    "solution_count",
    "solution_component_count",
    "total_component_count",
    "ingredient_term_count",
    "ingredient_chebi_term_count",
    "ingredient_non_chebi_term_count",
    "mediaingredientmech_count",
    "culturemech_component_count",
    "parent_ingredient_count",
    "variant_type_count",
    "concentration_count",
    "missing_concentration_count",
    "malformed_concentration_count",
    "missing_concentration_value_count",
    "missing_concentration_unit_count",
    "non_schema_concentration_unit_count",
    "concentration_units",
    "unexpected_ingredient_keys",
    "embedded_variant_count",
    "has_merge_fingerprint",
    "has_chemical_fingerprint",
    "has_variant_fingerprint",
    "ingredient_identity_signature",
    "ingredient_concentration_signature",
    "load_error",
]

GROUP_COLUMNS = [
    "ingredient_identity_signature",
    "group_size",
    "concentration_signature_count",
    "physical_state_count",
    "category_count",
    "name_key_count",
    "embedded_variant_records",
    "review_reason",
    "representative_paths",
]

EXPECTED_INGREDIENT_KEYS = {
    "preferred_term",
    "term",
    "mediaingredientmech_term",
    "culturemech_term",
    "parent_ingredient",
    "variant_type",
    "concentration",
    "modifier",
    "chemical_formula",
    "molecular_weight",
    "supplier_catalog",
    "notes",
    "nutritional_roles",
    "physicochemical_roles",
    "cellular_metabolic_roles",
    "role_curie",
    "cofactors_provided",
    "evidence",
}


def schema_concentration_units(schema_path: Path) -> set[str]:
    schema = yaml.safe_load(schema_path.read_text()) or {}
    enum = (schema.get("enums") or {}).get("ConcentrationUnitEnum") or {}
    permissible = enum.get("permissible_values") or {}
    return set(permissible)


def norm_text(value: Any) -> str:
    text = str(value or "").strip().lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    text = re.sub(r"_+", "_", text).strip("_")
    return text or "missing"


def media_term_id(recipe: dict[str, Any]) -> str:
    mt = recipe.get("media_term")
    if isinstance(mt, dict):
        term = mt.get("term")
        if isinstance(term, dict) and term.get("id"):
            return str(term["id"])
        if mt.get("id"):
            return str(mt["id"])
    return ""


def component_identity(component: dict[str, Any]) -> str:
    """Return a stable identity that ignores concentration."""
    for key, nested_key in (
        ("mediaingredientmech_term", "id"),
        ("parent_ingredient", "mediaingredientmech_id"),
        ("culturemech_term", "id"),
        ("term", "id"),
    ):
        value = component.get(key)
        if isinstance(value, dict) and value.get(nested_key):
            return f"{key}:{value[nested_key]}"
    return f"name:{norm_text(component.get('preferred_term'))}"


def concentration_identity(component: dict[str, Any]) -> str:
    conc = component.get("concentration")
    if not isinstance(conc, dict):
        return "missing"
    value = str(conc.get("value") or "").strip() or "missing_value"
    unit = str(conc.get("unit") or "").strip() or "missing_unit"
    per_volume = str(conc.get("per_volume") or "").strip()
    if per_volume:
        return f"{value}|{unit}|{per_volume}"
    return f"{value}|{unit}"


def iter_components(recipe: dict[str, Any]):
    for i, ing in enumerate(recipe.get("ingredients") or []):
        if isinstance(ing, dict):
            yield f"ingredients[{i}]", ing
    for si, sol in enumerate(recipe.get("solutions") or []):
        if not isinstance(sol, dict):
            continue
        composition = sol.get("composition") or sol.get("ingredients") or []
        for ci, comp in enumerate(composition):
            if isinstance(comp, dict):
                yield f"solutions[{si}].composition[{ci}]", comp


def signature(parts: list[str]) -> str:
    text = "\n".join(sorted(parts))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def summarize_record(path: Path, units: set[str]) -> dict[str, Any]:
    rel = path.relative_to(REPO_ROOT)
    row: dict[str, Any] = dict.fromkeys(RECORD_COLUMNS, "")
    row["yaml_path"] = str(rel)
    row["category_dir"] = path.parent.name

    try:
        recipe = yaml.safe_load(path.read_text()) or {}
    except Exception as exc:  # noqa: BLE001 - audit should record bad YAMLs.
        row["load_error"] = str(exc)
        return row

    if not isinstance(recipe, dict):
        row["load_error"] = "top-level YAML is not a mapping"
        return row

    row["id"] = recipe.get("id", "")
    row["name"] = recipe.get("name", "")
    row["original_name"] = recipe.get("original_name", "")
    row["media_term_id"] = media_term_id(recipe)
    row["medium_type"] = recipe.get("medium_type", "")
    row["physical_state"] = recipe.get("physical_state", "")
    row["ingredient_count"] = len(recipe.get("ingredients") or [])
    row["solution_count"] = len(recipe.get("solutions") or [])
    row["embedded_variant_count"] = len(recipe.get("variants") or [])
    row["has_merge_fingerprint"] = bool(recipe.get("merge_fingerprint"))
    row["has_chemical_fingerprint"] = bool(recipe.get("chemical_fingerprint"))
    row["has_variant_fingerprint"] = bool(recipe.get("variant_fingerprint"))

    solution_component_count = 0
    ingredient_term_count = 0
    ingredient_chebi_term_count = 0
    ingredient_non_chebi_term_count = 0
    mediaingredientmech_count = 0
    culturemech_component_count = 0
    parent_ingredient_count = 0
    variant_type_count = 0
    concentration_count = 0
    missing_concentration_count = 0
    malformed_concentration_count = 0
    missing_concentration_value_count = 0
    missing_concentration_unit_count = 0
    non_schema_concentration_unit_count = 0
    unit_counter: Counter[str] = Counter()
    unexpected_keys: Counter[str] = Counter()
    identities: list[str] = []
    concentration_parts: list[str] = []

    for location, component in iter_components(recipe):
        if location.startswith("solutions["):
            solution_component_count += 1

        unexpected_keys.update(set(component) - EXPECTED_INGREDIENT_KEYS)

        term = component.get("term")
        if isinstance(term, dict) and term.get("id"):
            ingredient_term_count += 1
            if str(term["id"]).startswith("CHEBI:"):
                ingredient_chebi_term_count += 1
            else:
                ingredient_non_chebi_term_count += 1

        mim = component.get("mediaingredientmech_term")
        if isinstance(mim, dict) and mim.get("id"):
            mediaingredientmech_count += 1

        cmt = component.get("culturemech_term")
        if isinstance(cmt, dict) and cmt.get("id"):
            culturemech_component_count += 1

        parent = component.get("parent_ingredient")
        if isinstance(parent, dict) and parent.get("mediaingredientmech_id"):
            parent_ingredient_count += 1

        if component.get("variant_type"):
            variant_type_count += 1

        identity = component_identity(component)
        identities.append(identity)
        concentration_parts.append(f"{identity}={concentration_identity(component)}")

        conc = component.get("concentration")
        if conc is None:
            missing_concentration_count += 1
            continue
        if not isinstance(conc, dict):
            malformed_concentration_count += 1
            continue
        concentration_count += 1
        if not str(conc.get("value") or "").strip():
            missing_concentration_value_count += 1
        unit = str(conc.get("unit") or "").strip()
        if not unit:
            missing_concentration_unit_count += 1
        else:
            unit_counter[unit] += 1
            if unit not in units:
                non_schema_concentration_unit_count += 1

    row["solution_component_count"] = solution_component_count
    row["total_component_count"] = len(identities)
    row["ingredient_term_count"] = ingredient_term_count
    row["ingredient_chebi_term_count"] = ingredient_chebi_term_count
    row["ingredient_non_chebi_term_count"] = ingredient_non_chebi_term_count
    row["mediaingredientmech_count"] = mediaingredientmech_count
    row["culturemech_component_count"] = culturemech_component_count
    row["parent_ingredient_count"] = parent_ingredient_count
    row["variant_type_count"] = variant_type_count
    row["concentration_count"] = concentration_count
    row["missing_concentration_count"] = missing_concentration_count
    row["malformed_concentration_count"] = malformed_concentration_count
    row["missing_concentration_value_count"] = missing_concentration_value_count
    row["missing_concentration_unit_count"] = missing_concentration_unit_count
    row["non_schema_concentration_unit_count"] = non_schema_concentration_unit_count
    row["concentration_units"] = ";".join(sorted(unit_counter))
    row["unexpected_ingredient_keys"] = ";".join(sorted(unexpected_keys))
    row["ingredient_identity_signature"] = signature(identities)
    row["ingredient_concentration_signature"] = signature(concentration_parts)
    return row


def build_groups(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row.get("load_error"):
            continue
        if int(row.get("total_component_count") or 0) == 0:
            continue
        grouped[row["ingredient_identity_signature"]].append(row)

    groups: list[dict[str, Any]] = []
    for ident_sig, members in grouped.items():
        if len(members) < 2:
            continue
        concentration_sigs = {m["ingredient_concentration_signature"] for m in members}
        physical_states = {m["physical_state"] for m in members if m.get("physical_state")}
        categories = {m["category_dir"] for m in members if m.get("category_dir")}
        name_keys = {norm_text(m.get("name") or m.get("original_name")) for m in members}
        embedded_variant_records = sum(1 for m in members if int(m.get("embedded_variant_count") or 0) > 0)
        reasons = []
        if len(concentration_sigs) > 1:
            reasons.append("same ingredient set with different concentrations")
        if len(physical_states) > 1:
            reasons.append("same ingredient set across physical states")
        if len(name_keys) > 1:
            reasons.append("same ingredient set across multiple names")
        if embedded_variant_records:
            reasons.append("one or more records already have embedded variants")
        groups.append(
            {
                "ingredient_identity_signature": ident_sig,
                "group_size": len(members),
                "concentration_signature_count": len(concentration_sigs),
                "physical_state_count": len(physical_states),
                "category_count": len(categories),
                "name_key_count": len(name_keys),
                "embedded_variant_records": embedded_variant_records,
                "review_reason": "; ".join(reasons) or "same ingredient identity signature",
                "representative_paths": ";".join(m["yaml_path"] for m in members[:20]),
            }
        )
    groups.sort(
        key=lambda g: (
            -int(g["group_size"]),
            -int(g["concentration_signature_count"]),
            str(g["ingredient_identity_signature"]),
        )
    )
    return groups


def pct(numerator: int, denominator: int) -> str:
    if denominator == 0:
        return "0.0%"
    return f"{100 * numerator / denominator:.1f}%"


def int_sum(rows: list[dict[str, Any]], key: str) -> int:
    return sum(int(row.get(key) or 0) for row in rows)


def write_summary(rows: list[dict[str, Any]], groups: list[dict[str, Any]], out: Path) -> None:
    valid = [row for row in rows if not row.get("load_error")]
    total_records = len(rows)
    valid_records = len(valid)
    total_components = int_sum(valid, "total_component_count")
    total_direct_ingredients = int_sum(valid, "ingredient_count")
    total_solution_components = int_sum(valid, "solution_component_count")
    records_with_embedded_variants = sum(1 for row in valid if int(row.get("embedded_variant_count") or 0) > 0)
    embedded_variant_total = int_sum(valid, "embedded_variant_count")
    records_with_component_refs = sum(1 for row in valid if int(row.get("culturemech_component_count") or 0) > 0)
    records_with_all_components_concentrated = sum(
        1
        for row in valid
        if int(row.get("total_component_count") or 0) > 0
        and int(row.get("missing_concentration_count") or 0) == 0
        and int(row.get("malformed_concentration_count") or 0) == 0
        and int(row.get("missing_concentration_value_count") or 0) == 0
        and int(row.get("missing_concentration_unit_count") or 0) == 0
    )
    records_with_all_components_chebi = sum(
        1
        for row in valid
        if int(row.get("total_component_count") or 0) > 0
        and int(row.get("ingredient_chebi_term_count") or 0) == int(row.get("total_component_count") or 0)
    )

    units = Counter()
    unexpected = Counter()
    for row in valid:
        for unit in str(row.get("concentration_units") or "").split(";"):
            if unit:
                units[unit] += 1
        for key in str(row.get("unexpected_ingredient_keys") or "").split(";"):
            if key:
                unexpected[key] += 1

    by_category: dict[str, Counter[str]] = defaultdict(Counter)
    for row in valid:
        category = row.get("category_dir") or "unknown"
        by_category[category]["records"] += 1
        by_category[category]["components"] += int(row.get("total_component_count") or 0)
        by_category[category]["missing_concentration"] += int(row.get("missing_concentration_count") or 0)
        by_category[category]["embedded_variants"] += int(row.get("embedded_variant_count") or 0)

    lines: list[str] = []
    lines.append("# Media Content Review Manifest Summary\n")
    lines.append("Generated from `data/normalized_yaml/**/*.yaml`.\n")
    lines.append("## Corpus State\n")
    lines.append(f"- YAML records scanned: {total_records:,}")
    lines.append(f"- YAML records loaded: {valid_records:,}")
    lines.append(f"- YAML load errors: {total_records - valid_records:,}")
    lines.append(f"- Direct ingredient entries: {total_direct_ingredients:,}")
    lines.append(f"- Solution composition entries: {total_solution_components:,}")
    lines.append(f"- Total ingredient/component entries: {total_components:,}")
    lines.append(
        f"- Records with complete concentration value/unit coverage: "
        f"{records_with_all_components_concentrated:,} ({pct(records_with_all_components_concentrated, valid_records)})"
    )
    lines.append(
        f"- Records where every component has a CHEBI `term.id`: "
        f"{records_with_all_components_chebi:,} ({pct(records_with_all_components_chebi, valid_records)})"
    )
    lines.append(f"- Records with embedded `variants`: {records_with_embedded_variants:,}")
    lines.append(f"- Embedded variant entries: {embedded_variant_total:,}")
    lines.append(f"- Records using `culturemech_term` component links: {records_with_component_refs:,}")
    lines.append(f"- Candidate ingredient-identity variation groups: {len(groups):,}\n")

    lines.append("## Concentration Issues\n")
    lines.append(f"- Missing concentration object: {int_sum(valid, 'missing_concentration_count'):,}")
    lines.append(f"- Malformed concentration object: {int_sum(valid, 'malformed_concentration_count'):,}")
    lines.append(f"- Missing concentration value: {int_sum(valid, 'missing_concentration_value_count'):,}")
    lines.append(f"- Missing concentration unit: {int_sum(valid, 'missing_concentration_unit_count'):,}")
    lines.append(f"- Non-schema concentration units: {int_sum(valid, 'non_schema_concentration_unit_count'):,}\n")

    lines.append("## Ontology/Ingredient Issues\n")
    lines.append(f"- Components with any `term.id`: {int_sum(valid, 'ingredient_term_count'):,}")
    lines.append(f"- Components with CHEBI `term.id`: {int_sum(valid, 'ingredient_chebi_term_count'):,}")
    lines.append(f"- Components with non-CHEBI `term.id`: {int_sum(valid, 'ingredient_non_chebi_term_count'):,}")
    lines.append(f"- Components with MediaIngredientMech terms: {int_sum(valid, 'mediaingredientmech_count'):,}")
    lines.append(f"- Components with parent ingredient links: {int_sum(valid, 'parent_ingredient_count'):,}")
    lines.append(f"- Components with variant type labels: {int_sum(valid, 'variant_type_count'):,}\n")

    lines.append("## Records By Directory\n")
    lines.append("| Directory | Records | Components | Missing concentration objects | Embedded variants |")
    lines.append("|---|---:|---:|---:|---:|")
    for category, stats in sorted(by_category.items()):
        lines.append(
            f"| `{category}` | {stats['records']:,} | {stats['components']:,} | "
            f"{stats['missing_concentration']:,} | {stats['embedded_variants']:,} |"
        )
    lines.append("")

    lines.append("## Common Concentration Units\n")
    lines.append("| Unit | Records using unit |")
    lines.append("|---|---:|")
    for unit, count in units.most_common(20):
        lines.append(f"| `{unit}` | {count:,} |")
    lines.append("")

    if unexpected:
        lines.append("## Common Unexpected Ingredient Keys\n")
        lines.append("| Key | Records containing key |")
        lines.append("|---|---:|")
        for key, count in unexpected.most_common(20):
            lines.append(f"| `{key}` | {count:,} |")
        lines.append("")

    lines.append("## Top Candidate Variation Groups\n")
    lines.append("| Group size | Concentration signatures | Reason | Representative paths |")
    lines.append("|---:|---:|---|---|")
    for group in groups[:25]:
        paths = group["representative_paths"].replace(";", "<br>")
        lines.append(
            f"| {group['group_size']} | {group['concentration_signature_count']} | "
            f"{group['review_reason']} | {paths} |"
        )
    lines.append("")

    lines.append("## Outputs\n")
    lines.append("- Record manifest: `reports/media_content_review_manifest.tsv`")
    lines.append("- Record JSON: `reports/media_content_review_manifest.json`")
    lines.append("- Candidate variation groups: `reports/media_variation_candidate_groups.tsv`")
    lines.append("- Candidate variation groups JSON: `reports/media_variation_candidate_groups.json`")
    lines.append("")
    lines.append(
        "This assessment does not assert true parent/child relationships. It only "
        "identifies current representation and groups that need formulation review."
    )
    out.write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--yaml-root", type=Path, default=YAML_ROOT)
    parser.add_argument("--reports-dir", type=Path, default=REPORTS_DIR)
    args = parser.parse_args()

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    units = schema_concentration_units(REPO_ROOT / "src/culturemech/schema/culturemech.yaml")

    paths = sorted(args.yaml_root.rglob("*.yaml"))
    rows = [summarize_record(path, units) for path in paths]
    groups = build_groups(rows)

    manifest_tsv = args.reports_dir / "media_content_review_manifest.tsv"
    manifest_json = args.reports_dir / "media_content_review_manifest.json"
    groups_tsv = args.reports_dir / "media_variation_candidate_groups.tsv"
    groups_json = args.reports_dir / "media_variation_candidate_groups.json"
    summary_md = args.reports_dir / "media_content_review_manifest_summary.md"

    with manifest_tsv.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=RECORD_COLUMNS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    manifest_json.write_text(json.dumps(rows, indent=2, sort_keys=True) + "\n")

    with groups_tsv.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=GROUP_COLUMNS, delimiter="\t")
        writer.writeheader()
        writer.writerows(groups)
    groups_json.write_text(json.dumps(groups, indent=2, sort_keys=True) + "\n")

    write_summary(rows, groups, summary_md)

    print(f"Wrote {manifest_tsv.relative_to(REPO_ROOT)}")
    print(f"Wrote {manifest_json.relative_to(REPO_ROOT)}")
    print(f"Wrote {groups_tsv.relative_to(REPO_ROOT)}")
    print(f"Wrote {groups_json.relative_to(REPO_ROOT)}")
    print(f"Wrote {summary_md.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
