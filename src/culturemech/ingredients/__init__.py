"""Ingredient identity resolution shared by CultureMech consumers."""

from culturemech.ingredients.mim_label_index import (
    GroundingDecision,
    MIMLabelIndex,
    ResolutionSource,
    get_default_mim_label_index,
    resolve_ingredient,
)

__all__ = [
    "GroundingDecision",
    "MIMLabelIndex",
    "ResolutionSource",
    "get_default_mim_label_index",
    "resolve_ingredient",
]
