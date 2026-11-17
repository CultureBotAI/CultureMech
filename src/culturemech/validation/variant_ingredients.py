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

_ACTIONS = {"ADD", "REMOVE", "REPLACE", "SET_CONCENTRATION", "SET_AMOUNT"}
_AMOUNT_UNITS = {"G", "MG", "MICROG", "ML", "L", "PERCENT"}
_SUPPORTS = {"SUPPORT", "PARTIAL", "REFUTE", "NO_EVIDENCE", "WRONG_STATEMENT"}
# Relationships describe recipes, while actions describe source-bound events
# at explicit stages. An added dose does not assert a resulting total, and a
# supplemented/omitted/substituted formulation can document mixed operations
# (#761, #768). Only SOURCE_DUPLICATE explicitly asserts no formulation change.


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
        add("action", "variant_action", "expected a supported variant ingredient action")
        action = None
    relationship = variant.get("relationship")
    if relationship == "SOURCE_DUPLICATE" and action is not None:
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
        if action in {"ADD", "REPLACE", "SET_CONCENTRATION", "SET_AMOUNT"} and modifier == "ABSENT":
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

    amount = change.get("amount")
    if action == "SET_AMOUNT" and not isinstance(amount, dict):
        add("amount", "variant_amount", "SET_AMOUNT requires an explicit literal amount")
    if "amount" in change:
        if action not in {"ADD", "REPLACE", "SET_AMOUNT"}:
            add("amount", "variant_amount", "amount is only allowed for ADD, REPLACE or SET_AMOUNT")
        if isinstance(ingredient, dict) and "concentration" in ingredient:
            add("amount", "variant_amount", "literal amount cannot also assert a concentration")
        if not isinstance(amount, dict):
            add("amount", "variant_amount", "literal amount must be a mapping")
        else:
            for field in ("value", "basis_statement"):
                if not _nonblank(amount.get(field)):
                    add(f"amount.{field}", "variant_amount", f"nonblank {field} is required")
            unit = amount.get("unit")
            if not isinstance(unit, str) or unit not in _AMOUNT_UNITS:
                add(
                    "amount.unit",
                    "variant_amount",
                    "expected a literal mass, volume or percent unit",
                )
            expected_basis = "UNSPECIFIED_PERCENT" if unit == "PERCENT" else "PER_BATCH"
            if amount.get("basis") != expected_basis:
                add("amount.basis", "variant_amount", "amount unit and source basis disagree")

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


def _mention_issues(
    mention: Any, variant: dict[str, Any], path: str
) -> list[VariantIngredientIssue]:
    """Retain explicit names without promoting withheld source assertions."""
    issues: list[VariantIngredientIssue] = []

    def add(field: str, message: str) -> None:
        location = f"{path}.{field}" if field else path
        issues.append(VariantIngredientIssue(location, "variant_mention", field, message))

    if not isinstance(mention, dict):
        add("", "withheld mention must be a mapping")
        return issues
    allowed = {
        "source_label",
        "reported_action",
        "stage",
        "source_modification_index",
        "source_text",
        "reason",
        "held_fields",
        "reported_quantity",
        "evidence",
    }
    if set(mention) - allowed:
        add(
            "",
            "withheld mention has unknown fields; grounding and presence assertions are forbidden",
        )
    for field in ("source_label", "stage", "source_text", "reason"):
        if not _nonblank(mention.get(field)):
            add(field, f"nonblank {field} is required")
    action = mention.get("reported_action")
    if not isinstance(action, str) or action not in _ACTIONS | {"UNSPECIFIED"}:
        add("reported_action", "unknown reported action")
    held = mention.get("held_fields")
    if (
        not isinstance(held, list)
        or not held
        or any(
            not isinstance(field, str)
            or field not in {"SOURCE_CLAIM", "IDENTITY_FORM", "QUANTITY", "OPERATION", "STAGE"}
            for field in held
        )
    ):
        add("held_fields", "nonempty explicit unresolved dimensions are required")
    elif len(set(held)) != len(held):
        add("held_fields", "duplicate unresolved dimension")
    source = mention.get("source_text")
    label = mention.get("source_label")
    if _nonblank(label) and isinstance(source, str) and label not in source:
        add("source_label", "held label must occur verbatim in its source modification")
    modifications = variant.get("modifications")
    index = mention.get("source_modification_index")
    if type(index) is not int or index < 0:
        add("source_modification_index", "expected a nonnegative integer")
    elif not isinstance(modifications, list) or index >= len(modifications):
        add("source_modification_index", "index is outside modifications")
    elif source != modifications[index]:
        add("source_text", "must exactly equal modifications at the source index")
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
        if not isinstance(variant, dict):
            continue
        if "ingredient_mentions" in variant:
            mentions = variant["ingredient_mentions"]
            mention_path = f"variants[{variant_index}].ingredient_mentions"
            if not isinstance(mentions, list):
                issues.append(
                    VariantIngredientIssue(mention_path, "variant_mention", "", "expected a list")
                )
            else:
                seen_mentions: set[tuple] = set()
                for mention_index, mention in enumerate(mentions):
                    found = _mention_issues(mention, variant, f"{mention_path}[{mention_index}]")
                    issues.extend(found)
                    if not found:
                        key = (
                            mention["source_modification_index"],
                            mention["source_label"],
                            mention["reported_action"],
                            mention["stage"],
                        )
                        if key in seen_mentions:
                            issues.append(
                                VariantIngredientIssue(
                                    mention_path,
                                    "duplicate_variant_mention",
                                    "",
                                    "duplicate source-bound held mention",
                                )
                            )
                        seen_mentions.add(key)
        if "ingredient_changes" not in variant:
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
                            "amount",
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
