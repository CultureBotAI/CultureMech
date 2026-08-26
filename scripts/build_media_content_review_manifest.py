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
from record_kinds import has_solution_shape, is_solution_record
from triage_missing_compositions import has_no_usable_composition

REPO_ROOT = Path(__file__).resolve().parent.parent
YAML_ROOT = REPO_ROOT / "data" / "normalized_yaml"
REPORTS_DIR = REPO_ROOT / "reports"

RECORD_COLUMNS = [
    "yaml_path",
    "category_dir",
    "record_kind",
    "record_shape",
    "id",
    "name",
    "preferred_term",
    "original_name",
    "missing_name",
    "missing_composition",
    "media_term_id",
    "medium_type",
    "physical_state",
    "ingredient_count",
    "solution_count",
    "top_level_solution_component_count",
    "solution_component_count",
    "total_component_count",
    "malformed_component_count",
    "missing_component_name_count",
    "ingredient_term_count",
    "ingredient_chebi_term_count",
    "ingredient_non_chebi_term_count",
    "mediaingredientmech_count",
    "culturemech_component_count",
    "parent_ingredient_count",
    "variant_type_count",
    "concentration_count",
    "solution_concentration_count",
    "solution_concentration_candidate_count",
    "missing_concentration_count",
    "missing_solution_concentration_count",
    "missing_solution_concentration_with_candidates_count",
    "missing_solution_concentration_without_candidates_count",
    "malformed_concentration_count",
    "missing_concentration_value_count",
    "missing_concentration_unit_count",
    "non_schema_concentration_unit_count",
    "variable_concentration_count",
    "variable_solution_concentration_count",
    "unresolved_concentration_count",
    "unresolved_solution_concentration_count",
    "concentration_units",
    "unexpected_ingredient_keys",
    "embedded_variant_count",
    "has_merge_fingerprint",
    "has_chemical_fingerprint",
    "has_variant_fingerprint",
    "ingredient_identity_signature",
    "ingredient_concentration_signature",
    "review_status",
    "issue_count",
    "issue_codes",
    "issue_locations",
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

VARIABLE_VALUES = {"variable", "varies", "unspecified", "unknown", "n/a", "na"}

BLOCKING_ISSUES = {
    "LOAD_ERROR",
    "TOP_LEVEL_NOT_MAPPING",
    "MISSING_MEDIA_NAME",
    "MISSING_SOLUTION_NAME",
    "MISSING_MEDIA_COMPOSITION",
    "MISSING_SOLUTION_COMPOSITION",
    "MISSING_PHYSICAL_STATE",
    "MALFORMED_INGREDIENTS",
    "MALFORMED_SOLUTIONS",
    "MALFORMED_SOLUTION_COMPOSITION",
    "MALFORMED_COMPONENT",
    "MISSING_COMPONENT_NAME",
    "MALFORMED_CONCENTRATION",
    "MALFORMED_CONCENTRATION_CANDIDATES",
    "MISSING_CONCENTRATION_VALUE",
    "MISSING_CONCENTRATION_UNIT",
    "NON_SCHEMA_CONCENTRATION_UNIT",
    "UNEXPECTED_INGREDIENT_KEYS",
}


def schema_review_config(schema_path: Path) -> tuple[set[str], set[str], set[str]]:
    schema = yaml.safe_load(schema_path.read_text()) or {}
    enum = (schema.get("enums") or {}).get("ConcentrationUnitEnum") or {}
    permissible = enum.get("permissible_values") or {}
    classes = schema.get("classes") or {}
    ingredient = classes.get("IngredientDescriptor") or {}
    solution = classes.get("SolutionDescriptor") or {}
    ingredient_keys = set(ingredient.get("attributes") or {})
    solution_keys = set(solution.get("attributes") or {})
    return set(permissible), ingredient_keys, solution_keys


def schema_concentration_units(schema_path: Path) -> set[str]:
    """Compatibility helper for callers that only need the concentration enum."""
    return schema_review_config(schema_path)[0]


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
        ("mediaingredientmech_chebi_term", "id"),
        ("chebi_term", "id"),
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


def nested_solution_components(solution: dict[str, Any]) -> tuple[str, Any]:
    """Return the authoritative nested component slot and value for a solution."""
    composition = solution.get("composition")
    legacy_ingredients = solution.get("ingredients")
    if composition:
        return "composition", composition
    if legacy_ingredients is not None:
        return "ingredients", legacy_ingredients
    return "composition", composition


def iter_components(recipe: dict[str, Any]):
    """Yield location, value, and schema class for every media component.

    Native SolutionRecipe records use top-level ``composition``. Their
    ``ingredients`` slot is explicitly a legacy placeholder and must not be
    counted a second time. For MediaRecipe-shaped records, each stock-solution
    descriptor is itself a media component with a working concentration; its
    inline composition is then audited as IngredientDescriptor content.
    """
    if has_solution_shape(recipe):
        composition = recipe.get("composition")
        if isinstance(composition, list):
            for i, component in enumerate(composition):
                yield f"composition[{i}]", component, "INGREDIENT"
        return

    ingredients = recipe.get("ingredients")
    if isinstance(ingredients, list):
        for i, ingredient in enumerate(ingredients):
            yield f"ingredients[{i}]", ingredient, "INGREDIENT"

    solutions = recipe.get("solutions")
    if not isinstance(solutions, list):
        return
    for si, sol in enumerate(solutions):
        yield f"solutions[{si}]", sol, "SOLUTION"
        if not isinstance(sol, dict):
            continue
        nested_key, nested = nested_solution_components(sol)
        if isinstance(nested, list):
            for ci, component in enumerate(nested):
                yield f"solutions[{si}].{nested_key}[{ci}]", component, "INGREDIENT"


def signature(parts: list[str]) -> str:
    text = "\n".join(sorted(parts))
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def summarize_record(
    path: Path,
    units: set[str],
    expected_ingredient_keys: set[str] | None = None,
    repo_root: Path = REPO_ROOT,
    *,
    expected_solution_keys: set[str] | None = None,
) -> dict[str, Any]:
    rel = path.relative_to(repo_root)
    row: dict[str, Any] = dict.fromkeys(RECORD_COLUMNS, "")
    row["yaml_path"] = str(rel)
    row["category_dir"] = path.parent.name

    try:
        recipe = yaml.safe_load(path.read_text())
    except Exception as exc:  # noqa: BLE001 - audit should record bad YAMLs.
        row["load_error"] = str(exc)
        row["review_status"] = "BLOCKING"
        row["issue_count"] = 1
        row["issue_codes"] = "LOAD_ERROR"
        return row

    if not isinstance(recipe, dict):
        row["load_error"] = "top-level YAML is not a mapping"
        row["review_status"] = "BLOCKING"
        row["issue_count"] = 1
        row["issue_codes"] = "TOP_LEVEL_NOT_MAPPING"
        return row

    expected_ingredient_keys = expected_ingredient_keys or set()
    expected_solution_keys = expected_solution_keys or set()
    solution_record = is_solution_record(recipe)
    solution_shape = has_solution_shape(recipe)
    issues: set[str] = set()
    issue_locations: set[str] = set()

    def flag(code: str, location: str) -> None:
        issues.add(code)
        issue_locations.add(f"{code}@{location}")

    row["record_kind"] = "SOLUTION" if solution_record else "MEDIA"
    row["record_shape"] = "SOLUTION_RECIPE" if solution_shape else "MEDIA_RECIPE"
    row["id"] = recipe.get("id", "")
    row["name"] = recipe.get("name", "")
    row["preferred_term"] = recipe.get("preferred_term", "")
    row["original_name"] = recipe.get("original_name", "")

    record_name = recipe.get("preferred_term") if solution_shape else recipe.get("name")
    row["missing_name"] = int(not str(record_name or "").strip())
    if row["missing_name"]:
        flag(
            "MISSING_SOLUTION_NAME" if solution_record else "MISSING_MEDIA_NAME",
            "preferred_term" if solution_shape else "name",
        )
    if not str(recipe.get("id") or "").strip():
        flag("MISSING_ID", "id")

    missing_composition = False
    if not solution_record:
        missing_composition = has_no_usable_composition(recipe) is not None
        if missing_composition:
            flag("MISSING_MEDIA_COMPOSITION", "ingredients|solutions")
    elif solution_shape and (
        not isinstance(recipe.get("composition"), list) or not recipe.get("composition")
    ):
        missing_composition = True
        flag("MISSING_SOLUTION_COMPOSITION", "composition")
    elif solution_record and not solution_shape and has_no_usable_composition(recipe) is not None:
        # Curated stock-solution records left in MediaRecipe shape. They are not
        # media missing recipes, but they remain explicit content-review work.
        flag("SOLUTION_STUB", "ingredients|solutions")
    row["missing_composition"] = int(missing_composition)

    row["media_term_id"] = media_term_id(recipe)
    row["medium_type"] = recipe.get("medium_type", "")
    row["physical_state"] = recipe.get("physical_state", "")
    if not solution_record:
        if not str(recipe.get("physical_state") or "").strip():
            flag("MISSING_PHYSICAL_STATE", "physical_state")
        if not str(recipe.get("medium_type") or "").strip():
            flag("MISSING_MEDIUM_TYPE", "medium_type")
        if not str(recipe.get("category") or "").strip():
            flag("MISSING_CATEGORY", "category")

    ingredients = recipe.get("ingredients")
    solutions = recipe.get("solutions")
    composition = recipe.get("composition")
    row["ingredient_count"] = len(ingredients) if isinstance(ingredients, list) else 0
    row["solution_count"] = len(solutions) if isinstance(solutions, list) else 0
    row["top_level_solution_component_count"] = (
        len(composition) if solution_shape and isinstance(composition, list) else 0
    )
    if not solution_shape and ingredients is not None and not isinstance(ingredients, list):
        flag("MALFORMED_INGREDIENTS", "ingredients")
    if not solution_shape and solutions is not None and not isinstance(solutions, list):
        flag("MALFORMED_SOLUTIONS", "solutions")
    if solution_shape and composition is not None and not isinstance(composition, list):
        flag("MALFORMED_SOLUTION_COMPOSITION", "composition")
    if isinstance(solutions, list):
        for si, solution in enumerate(solutions):
            if not isinstance(solution, dict):
                flag("MALFORMED_SOLUTIONS", f"solutions[{si}]")
                continue
            nested_key, nested = nested_solution_components(solution)
            if nested is not None and not isinstance(nested, list):
                flag(
                    "MALFORMED_SOLUTION_COMPOSITION",
                    f"solutions[{si}].{nested_key}",
                )

    variants = recipe.get("variants")
    row["embedded_variant_count"] = len(variants) if isinstance(variants, list) else 0
    row["has_merge_fingerprint"] = bool(recipe.get("merge_fingerprint"))
    row["has_chemical_fingerprint"] = bool(recipe.get("chemical_fingerprint"))
    row["has_variant_fingerprint"] = bool(recipe.get("variant_fingerprint"))

    solution_component_count = 0
    malformed_component_count = 0
    missing_component_name_count = 0
    ingredient_term_count = 0
    ingredient_chebi_term_count = 0
    ingredient_non_chebi_term_count = 0
    mediaingredientmech_count = 0
    culturemech_component_count = 0
    parent_ingredient_count = 0
    variant_type_count = 0
    concentration_count = 0
    solution_concentration_count = 0
    solution_concentration_candidate_count = 0
    missing_concentration_count = 0
    missing_solution_concentration_count = 0
    missing_solution_concentration_with_candidates_count = 0
    missing_solution_concentration_without_candidates_count = 0
    malformed_concentration_count = 0
    missing_concentration_value_count = 0
    missing_concentration_unit_count = 0
    non_schema_concentration_unit_count = 0
    variable_concentration_count = 0
    variable_solution_concentration_count = 0
    unresolved_concentration_count = 0
    unresolved_solution_concentration_count = 0
    unit_counter: Counter[str] = Counter()
    unexpected_keys: Counter[str] = Counter()
    identities: list[str] = []
    concentration_parts: list[str] = []
    component_entry_count = 0

    for location, component, component_kind in iter_components(recipe):
        component_entry_count += 1
        if component_kind == "INGREDIENT" and location.startswith("solutions["):
            solution_component_count += 1

        if not isinstance(component, dict):
            malformed_component_count += 1
            flag("MALFORMED_COMPONENT", location)
            continue

        expected_keys = (
            expected_solution_keys if component_kind == "SOLUTION" else expected_ingredient_keys
        )
        component_unexpected_keys = set(component) - expected_keys
        unexpected_keys.update(component_unexpected_keys)
        for key in component_unexpected_keys:
            flag("UNEXPECTED_INGREDIENT_KEYS", f"{location}.{key}")
        if not str(component.get("preferred_term") or "").strip():
            missing_component_name_count += 1
            flag("MISSING_COMPONENT_NAME", f"{location}.preferred_term")

        if component_kind == "INGREDIENT":
            term_ids = []
            for term_key in ("term", "chebi_term", "mediaingredientmech_chebi_term"):
                term = component.get(term_key)
                if isinstance(term, dict) and term.get("id"):
                    term_ids.append(str(term["id"]))
            if term_ids:
                ingredient_term_count += 1
            if any(term_id.startswith("CHEBI:") for term_id in term_ids):
                ingredient_chebi_term_count += 1
            primary_term = component.get("term")
            if (
                isinstance(primary_term, dict)
                and primary_term.get("id")
                and not str(primary_term["id"]).startswith("CHEBI:")
            ):
                ingredient_non_chebi_term_count += 1

        mim_terms = (
            component.get("mediaingredientmech_term"),
            component.get("mediaingredientmech_chebi_term"),
        )
        if any(isinstance(term, dict) and term.get("id") for term in mim_terms):
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

        solution_candidate_count = 0
        if component_kind == "SOLUTION":
            candidates = component.get("concentration_candidates")
            if isinstance(candidates, list):
                solution_candidate_count = len(candidates)
                solution_concentration_candidate_count += solution_candidate_count
            elif candidates is not None:
                flag(
                    "MALFORMED_CONCENTRATION_CANDIDATES",
                    f"{location}.concentration_candidates",
                )

        conc = component.get("concentration")
        if conc is None:
            missing_concentration_count += 1
            unresolved_concentration_count += 1
            if component_kind == "SOLUTION":
                missing_solution_concentration_count += 1
                unresolved_solution_concentration_count += 1
                if solution_candidate_count:
                    missing_solution_concentration_with_candidates_count += 1
                else:
                    missing_solution_concentration_without_candidates_count += 1
                flag("MISSING_SOLUTION_CONCENTRATION", f"{location}.concentration")
            else:
                flag("MISSING_CONCENTRATION", f"{location}.concentration")
            continue
        if not isinstance(conc, dict):
            malformed_concentration_count += 1
            unresolved_concentration_count += 1
            if component_kind == "SOLUTION":
                unresolved_solution_concentration_count += 1
            flag("MALFORMED_CONCENTRATION", f"{location}.concentration")
            continue
        concentration_count += 1
        if component_kind == "SOLUTION":
            solution_concentration_count += 1
        unresolved = False
        value = str(conc.get("value") or "").strip()
        if not value:
            missing_concentration_value_count += 1
            unresolved = True
            flag("MISSING_CONCENTRATION_VALUE", f"{location}.concentration.value")
        unit = str(conc.get("unit") or "").strip()
        if not unit:
            missing_concentration_unit_count += 1
            unresolved = True
            flag("MISSING_CONCENTRATION_UNIT", f"{location}.concentration.unit")
        else:
            unit_counter[unit] += 1
            if unit not in units:
                non_schema_concentration_unit_count += 1
                unresolved = True
                flag("NON_SCHEMA_CONCENTRATION_UNIT", f"{location}.concentration.unit")
        if unit == "VARIABLE" or value.lower() in VARIABLE_VALUES:
            variable_concentration_count += 1
            if component_kind == "SOLUTION":
                variable_solution_concentration_count += 1
            unresolved = True
            flag("VARIABLE_CONCENTRATION", f"{location}.concentration")
        if unresolved:
            unresolved_concentration_count += 1
            if component_kind == "SOLUTION":
                unresolved_solution_concentration_count += 1

    row["solution_component_count"] = solution_component_count
    row["total_component_count"] = component_entry_count
    row["malformed_component_count"] = malformed_component_count
    row["missing_component_name_count"] = missing_component_name_count
    row["ingredient_term_count"] = ingredient_term_count
    row["ingredient_chebi_term_count"] = ingredient_chebi_term_count
    row["ingredient_non_chebi_term_count"] = ingredient_non_chebi_term_count
    row["mediaingredientmech_count"] = mediaingredientmech_count
    row["culturemech_component_count"] = culturemech_component_count
    row["parent_ingredient_count"] = parent_ingredient_count
    row["variant_type_count"] = variant_type_count
    row["concentration_count"] = concentration_count
    row["solution_concentration_count"] = solution_concentration_count
    row["solution_concentration_candidate_count"] = solution_concentration_candidate_count
    row["missing_concentration_count"] = missing_concentration_count
    row["missing_solution_concentration_count"] = missing_solution_concentration_count
    row["missing_solution_concentration_with_candidates_count"] = (
        missing_solution_concentration_with_candidates_count
    )
    row["missing_solution_concentration_without_candidates_count"] = (
        missing_solution_concentration_without_candidates_count
    )
    row["malformed_concentration_count"] = malformed_concentration_count
    row["missing_concentration_value_count"] = missing_concentration_value_count
    row["missing_concentration_unit_count"] = missing_concentration_unit_count
    row["non_schema_concentration_unit_count"] = non_schema_concentration_unit_count
    row["variable_concentration_count"] = variable_concentration_count
    row["variable_solution_concentration_count"] = variable_solution_concentration_count
    row["unresolved_concentration_count"] = unresolved_concentration_count
    row["unresolved_solution_concentration_count"] = unresolved_solution_concentration_count
    row["concentration_units"] = ";".join(sorted(unit_counter))
    row["unexpected_ingredient_keys"] = ";".join(sorted(unexpected_keys))
    row["ingredient_identity_signature"] = signature(identities)
    row["ingredient_concentration_signature"] = signature(concentration_parts)
    row["review_status"] = (
        "BLOCKING" if issues & BLOCKING_ISSUES else "NEEDS_REVIEW" if issues else "PASS"
    )
    row["issue_count"] = len(issues)
    row["issue_codes"] = ";".join(sorted(issues))
    row["issue_locations"] = ";".join(sorted(issue_locations))
    return row


def build_groups(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if row.get("load_error"):
            continue
        if row.get("record_kind") == "SOLUTION":
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
    media = [row for row in valid if row.get("record_kind") == "MEDIA"]
    solutions = [row for row in valid if row.get("record_kind") == "SOLUTION"]
    total_records = len(rows)
    valid_records = len(valid)
    total_components = int_sum(valid, "total_component_count")
    total_direct_ingredients = int_sum(media, "ingredient_count")
    total_solution_descriptors = int_sum(media, "solution_count")
    total_nested_solution_components = int_sum(media, "solution_component_count")
    total_top_level_solution_components = int_sum(solutions, "top_level_solution_component_count")
    records_with_embedded_variants = sum(
        1 for row in media if int(row.get("embedded_variant_count") or 0) > 0
    )
    embedded_variant_total = int_sum(media, "embedded_variant_count")
    records_with_component_refs = sum(
        1 for row in valid if int(row.get("culturemech_component_count") or 0) > 0
    )
    records_with_all_components_concentrated = sum(
        1
        for row in media
        if int(row.get("total_component_count") or 0) > 0
        and int(row.get("unresolved_concentration_count") or 0) == 0
    )
    records_with_all_components_chebi = sum(
        1
        for row in media
        if int(row.get("total_component_count") or 0) - int(row.get("solution_count") or 0) > 0
        and int(row.get("ingredient_chebi_term_count") or 0)
        == int(row.get("total_component_count") or 0) - int(row.get("solution_count") or 0)
    )

    units = Counter()
    unexpected = Counter()
    issue_counts = Counter()
    status_counts = Counter(str(row.get("review_status") or "UNKNOWN") for row in rows)
    media_status_counts = Counter(str(row.get("review_status") or "UNKNOWN") for row in media)
    for row in valid:
        for unit in str(row.get("concentration_units") or "").split(";"):
            if unit:
                units[unit] += 1
        for key in str(row.get("unexpected_ingredient_keys") or "").split(";"):
            if key:
                unexpected[key] += 1
    for row in rows:
        for code in str(row.get("issue_codes") or "").split(";"):
            if code:
                issue_counts[code] += 1

    by_category: dict[str, Counter[str]] = defaultdict(Counter)
    for row in valid:
        category = row.get("category_dir") or "unknown"
        by_category[category]["records"] += 1
        by_category[category][str(row.get("record_kind") or "UNKNOWN").lower()] += 1
        by_category[category]["components"] += int(row.get("total_component_count") or 0)
        by_category[category]["unresolved_concentration"] += int(
            row.get("unresolved_concentration_count") or 0
        )
        by_category[category]["embedded_variants"] += int(row.get("embedded_variant_count") or 0)

    lines: list[str] = []
    lines.append("# Media Content Review Manifest Summary\n")
    lines.append("Generated from `data/normalized_yaml/**/*.yaml`.\n")
    lines.append("## Corpus State\n")
    lines.append(f"- YAML records scanned: {total_records:,}")
    lines.append(f"- YAML records loaded: {valid_records:,}")
    lines.append(f"- YAML load errors: {total_records - valid_records:,}")
    lines.append(f"- Media records: {len(media):,}")
    lines.append(f"- Standalone solution records: {len(solutions):,}")
    lines.append(f"- Direct media ingredient entries: {total_direct_ingredients:,}")
    lines.append(f"- Media stock-solution descriptor entries: {total_solution_descriptors:,}")
    lines.append(f"- Inline media solution-composition entries: {total_nested_solution_components:,}")
    lines.append(f"- Standalone solution composition entries: {total_top_level_solution_components:,}")
    lines.append(f"- Total authoritative ingredient/component entries: {total_components:,}")
    lines.append(
        f"- Media with fully resolved concentration coverage: "
        f"{records_with_all_components_concentrated:,} "
        f"({pct(records_with_all_components_concentrated, len(media))})"
    )
    lines.append(
        f"- Media where every chemical ingredient descriptor has a CHEBI grounding: "
        f"{records_with_all_components_chebi:,} ({pct(records_with_all_components_chebi, len(media))})"
    )
    lines.append(f"- Records with embedded `variants`: {records_with_embedded_variants:,}")
    lines.append(f"- Embedded variant entries: {embedded_variant_total:,}")
    lines.append(f"- Records using `culturemech_term` component links: {records_with_component_refs:,}")
    lines.append(f"- Candidate ingredient-identity variation groups: {len(groups):,}\n")

    lines.append("## Required Content Checks\n")
    lines.append(f"- Media missing `name`: {int_sum(media, 'missing_name'):,}")
    lines.append(f"- Media with no usable ingredients or solutions: {int_sum(media, 'missing_composition'):,}")
    lines.append(f"- Media components missing `preferred_term`: {int_sum(media, 'missing_component_name_count'):,}")
    missing_concentrations = int_sum(media, "missing_concentration_count")
    missing_solution_concentrations = int_sum(media, "missing_solution_concentration_count")
    missing_solution_with_candidates = int_sum(
        media, "missing_solution_concentration_with_candidates_count"
    )
    missing_solution_without_candidates = int_sum(
        media, "missing_solution_concentration_without_candidates_count"
    )
    variable_concentrations = int_sum(media, "variable_concentration_count")
    variable_solution_concentrations = int_sum(media, "variable_solution_concentration_count")
    lines.append(f"- Media component entries missing concentration object: {missing_concentrations:,}")
    lines.append(
        f"  - Chemical ingredient descriptors: "
        f"{missing_concentrations - missing_solution_concentrations:,}"
    )
    lines.append(f"  - Stock-solution descriptors: {missing_solution_concentrations:,}")
    lines.append(
        f"    - With one or more non-asserted concentration candidates: "
        f"{missing_solution_with_candidates:,}"
    )
    lines.append(
        f"    - Without a concentration candidate: {missing_solution_without_candidates:,}"
    )
    lines.append(f"- Media components with malformed concentration object: {int_sum(media, 'malformed_concentration_count'):,}")
    lines.append(f"- Media components missing concentration value: {int_sum(media, 'missing_concentration_value_count'):,}")
    lines.append(f"- Media components missing concentration unit: {int_sum(media, 'missing_concentration_unit_count'):,}")
    lines.append(f"- Media component entries with `VARIABLE`/unspecified concentration: {variable_concentrations:,}")
    lines.append(
        f"  - Chemical ingredient descriptors: "
        f"{variable_concentrations - variable_solution_concentrations:,}"
    )
    lines.append(f"  - Stock-solution descriptors: {variable_solution_concentrations:,}")
    lines.append(f"- Media components with non-schema concentration units: {int_sum(media, 'non_schema_concentration_unit_count'):,}\n")

    lines.append("## Review Outcome\n")
    lines.append("| Status | All records | Media only |")
    lines.append("|---|---:|---:|")
    for status in ("BLOCKING", "NEEDS_REVIEW", "PASS", "UNKNOWN"):
        if status_counts[status] or media_status_counts[status]:
            lines.append(
                f"| `{status}` | {status_counts[status]:,} | {media_status_counts[status]:,} |"
            )
    lines.append("")

    lines.append("## Issue Codes\n")
    lines.append("| Issue | Records |")
    lines.append("|---|---:|")
    for issue, count in issue_counts.most_common():
        lines.append(f"| `{issue}` | {count:,} |")
    lines.append("")

    lines.append("## Ontology/Ingredient Issues\n")
    lines.append(f"- Components with any `term.id`: {int_sum(valid, 'ingredient_term_count'):,}")
    lines.append(f"- Components with CHEBI `term.id`: {int_sum(valid, 'ingredient_chebi_term_count'):,}")
    lines.append(f"- Components with non-CHEBI `term.id`: {int_sum(valid, 'ingredient_non_chebi_term_count'):,}")
    lines.append(f"- Components with MediaIngredientMech terms: {int_sum(valid, 'mediaingredientmech_count'):,}")
    lines.append(f"- Components with parent ingredient links: {int_sum(valid, 'parent_ingredient_count'):,}")
    lines.append(f"- Components with variant type labels: {int_sum(valid, 'variant_type_count'):,}\n")

    lines.append("## Records By Directory\n")
    lines.append("| Directory | Records | Media | Solutions | Components | Unresolved concentrations | Embedded variants |")
    lines.append("|---|---:|---:|---:|---:|---:|---:|")
    for category, stats in sorted(by_category.items()):
        lines.append(
            f"| `{category}` | {stats['records']:,} | {stats['media']:,} | "
            f"{stats['solution']:,} | {stats['components']:,} | "
            f"{stats['unresolved_concentration']:,} | {stats['embedded_variants']:,} |"
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
    parser.add_argument("--out", type=Path, default=None,
                        help="Write ONLY the manifest .tsv to this path and nothing "
                             "else. Used by the derived-artifacts freshness check "
                             "(#168): the .tsv is the one consumed output, so a check "
                             "need not also regenerate the untracked json/groups/summary.")
    args = parser.parse_args()

    units, ingredient_keys, solution_keys = schema_review_config(
        REPO_ROOT / "src/culturemech/schema/culturemech.yaml"
    )
    paths = sorted(args.yaml_root.rglob("*.yaml"))
    rows = [
        summarize_record(
            path,
            units,
            ingredient_keys,
            expected_solution_keys=solution_keys,
        )
        for path in paths
    ]

    if args.out is not None:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=RECORD_COLUMNS, delimiter="\t")
            writer.writeheader()
            writer.writerows(rows)
        return 0

    args.reports_dir.mkdir(parents=True, exist_ok=True)
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
