"""Validate source-bound variant ingredient changes (#683, 2026-11-16).

Input: a parsed recipe. Output: structured issues or LinkML ValidationResults;
no mutation or external lookup. This checks source coordinates, explicit stage,
operation consistency and evidence structure, not scientific truth or identity.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any

from linkml.validator.report import Severity, ValidationResult

_ACTIONS = {"ADD", "REMOVE", "REPLACE", "SET_CONCENTRATION"}
_SUPPORTS = {"SUPPORT", "PARTIAL", "REFUTE", "NO_EVIDENCE", "WRONG_STATEMENT"}
_NARROW_RELATIONSHIPS = {
    "SOURCE_DUPLICATE": set(),
    "SUPPLEMENTED_VARIANT": {"ADD"},
    "OMITTED_COMPONENT_VARIANT": {"REMOVE"},
    "CONCENTRATION_VARIANT": {"SET_CONCENTRATION"},
}
# SUBSTITUTED_COMPONENT_VARIANT describes a recipe-level relationship. An
# alternative formulation can contain additions, omissions and dose changes;
# only an individual REPLACE event claims a one-to-one replacement (#761).


@dataclass(frozen=True)
class VariantIngredientIssue:
    """A validation failure at a precise recipe-relative path."""

    path: str
    category: str
    detail: str
    message: str


def _nonblank(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _change_issues(change: Any, variant: dict[str, Any], path: str) -> list[VariantIngredientIssue]:
    issues: list[VariantIngredientIssue] = []

    def add(field: str, category: str, message: str) -> None:
        location = f"{path}.{field}" if field else path
        issues.append(VariantIngredientIssue(location, category, field, f"{location}: {message}"))

    if not isinstance(change, dict):
        add("", "variant_change_type", "ingredient change must be a mapping")
        return issues

    action = change.get("action")
    if not isinstance(action, str) or action not in _ACTIONS:
        add("action", "variant_action", "expected ADD, REMOVE, REPLACE or SET_CONCENTRATION")
        action = None
    relationship = variant.get("relationship")
    if (
        isinstance(relationship, str)
        and relationship in _NARROW_RELATIONSHIPS
        and action is not None
        and action not in _NARROW_RELATIONSHIPS[relationship]
    ):
        add("action", "variant_relationship", f"{action} contradicts {relationship}")
    if not _nonblank(change.get("stage")):
        add("stage", "variant_stage", "nonblank preparation or experimental stage is required")

    modifications = variant.get("modifications")
    index = change.get("source_modification_index")
    if type(index) is not int or index < 0:  # bool is not a source coordinate
        add("source_modification_index", "variant_source_index", "expected a nonnegative integer")
    elif not isinstance(modifications, list) or index >= len(modifications):
        add("source_modification_index", "variant_source_index", "index is outside modifications")
    elif change.get("source_text") != modifications[index]:
        add(
            "source_text",
            "variant_source_text",
            "must exactly equal modifications at the source index",
        )
    if not _nonblank(change.get("source_text")):
        add(
            "source_text",
            "variant_source_text",
            "nonblank exact source modification text is required",
        )

    ingredient = change.get("ingredient")
    if not isinstance(ingredient, dict) or not _nonblank(ingredient.get("preferred_term")):
        add(
            "ingredient",
            "variant_ingredient",
            "a descriptor with a nonblank preferred_term is required",
        )
    else:
        modifier = ingredient.get("modifier")
        if action in {"ADD", "REPLACE", "SET_CONCENTRATION"} and modifier == "ABSENT":
            add(
                "ingredient.modifier",
                "variant_presence",
                "ABSENT contradicts a positive change event",
            )
        if action == "REMOVE" and modifier not in (None, "ABSENT"):
            add(
                "ingredient.modifier",
                "variant_presence",
                "REMOVE cannot increase or decrease an ingredient",
            )
        if action == "SET_CONCENTRATION":
            concentration = ingredient.get("concentration")
            if not isinstance(concentration, dict) or not all(
                _nonblank(concentration.get(field)) for field in ("value", "unit")
            ):
                add(
                    "ingredient.concentration",
                    "variant_concentration",
                    "SET_CONCENTRATION requires value and unit",
                )

    if action == "REPLACE":
        old = change.get("replaced_ingredient")
        if not isinstance(old, dict) or not _nonblank(old.get("preferred_term")):
            add(
                "replaced_ingredient",
                "variant_replacement",
                "REPLACE requires the old ingredient descriptor",
            )
    elif "replaced_ingredient" in change:
        add(
            "replaced_ingredient",
            "variant_replacement",
            "only REPLACE may carry the old ingredient",
        )

    evidence = change.get("evidence")
    if not isinstance(evidence, list) or not evidence:
        add("evidence", "variant_evidence", "nonempty claim-scoped evidence is required")
    else:
        supported = False
        references: set[str] = set()
        for number, item in enumerate(evidence):
            field = f"evidence[{number}]"
            if not isinstance(item, dict):
                add(field, "variant_evidence", "evidence must be a mapping")
                continue
            for key in ("reference", "snippet", "explanation"):
                if not _nonblank(item.get(key)):
                    add(f"{field}.{key}", "variant_evidence", f"nonblank {key} is required")
            support = item.get("supports")
            if not isinstance(support, str) or support not in _SUPPORTS:
                add(f"{field}.supports", "variant_evidence", "invalid evidence support level")
            supported |= support == "SUPPORT"
            reference = item.get("reference")
            if _nonblank(reference):
                if reference in references:
                    add(f"{field}.reference", "variant_evidence", "duplicate evidence reference")
                references.add(reference)
        if not supported:
            add(
                "evidence",
                "variant_evidence",
                "at least one evidence item must SUPPORT this change",
            )
    return issues


def validate_recipe_variant_ingredients(instance: dict[str, Any]) -> list[VariantIngredientIssue]:
    """Validate only curated ingredient_changes; legacy prose remains valid.

    Broad or unspecified variant relationships are permitted: a source-specific
    stage does not establish exact parent formulation equivalence. Duplicate
    scientific change payloads are refused; separate doses remain distinct.
    """
    issues: list[VariantIngredientIssue] = []
    if not isinstance(instance, dict) or not isinstance(instance.get("variants"), list):
        return issues
    for variant_index, variant in enumerate(instance["variants"]):
        if not isinstance(variant, dict) or "ingredient_changes" not in variant:
            continue
        path = f"variants[{variant_index}].ingredient_changes"
        changes = variant["ingredient_changes"]
        if not isinstance(changes, list):
            issues.append(
                VariantIngredientIssue(path, "variant_changes_type", "", f"{path}: expected a list")
            )
            continue
        seen: set[str] = set()
        for change_index, change in enumerate(changes):
            entry_path = f"{path}[{change_index}]"
            found = _change_issues(change, variant, entry_path)
            issues.extend(found)
            if found:
                continue
            try:
                key = json.dumps(
                    {
                        field: change.get(field)
                        for field in (
                            "action",
                            "ingredient",
                            "replaced_ingredient",
                            "stage",
                            "source_modification_index",
                            "source_text",
                        )
                    },
                    sort_keys=True,
                    allow_nan=False,
                )
            except (TypeError, ValueError):
                issues.append(
                    VariantIngredientIssue(
                        entry_path,
                        "variant_change_type",
                        "",
                        f"{entry_path}: change must contain JSON-compatible values",
                    )
                )
                continue
            if key in seen:
                issues.append(
                    VariantIngredientIssue(
                        entry_path,
                        "duplicate_variant_change",
                        "",
                        f"{entry_path}: duplicate action, ingredient, stage and source coordinate",
                    )
                )
            seen.add(key)
    return issues


def variant_ingredient_validation_results(instance: dict[str, Any]) -> list[ValidationResult]:
    """Expose semantic errors through the standard LinkML validation interface."""
    return [
        ValidationResult(
            type="variant_ingredients",
            severity=Severity.ERROR,
            message=issue.message,
            context=[issue.path],
        )
        for issue in validate_recipe_variant_ingredients(instance)
    ]
