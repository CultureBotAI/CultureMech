"""Single source of truth for inferring PreparationActionEnum values from text.

Used by import writers (ccap/sag/utex) and the legacy-field migration script,
so the action chosen for a given description matches across newly-written and
migrated records. PreparationActionEnum is defined in
src/culturemech/schema/culturemech.yaml.
"""

from __future__ import annotations


def infer_prep_action(text: str) -> str:
    """Best-guess PreparationActionEnum value from a free-text step description.

    Returns one of the enum values; defaults to ``DISSOLVE``. Stem-based so
    inflections (``autoclaving``, ``sterilization``, ``filtered``) match.
    """
    s = (text or "").lower()
    if "autoclav" in s:                       # autoclave, autoclaved, autoclaving
        return "AUTOCLAVE"
    if "filter" in s and "steril" in s:       # filter-sterilize, filter-sterilized
        return "FILTER_STERILIZE"
    if "adjust" in s and "ph" in s:
        return "ADJUST_PH"
    if "agar" in s:
        return "ADD_AGAR"
    if "pour" in s and "plate" in s:
        return "POUR_PLATES"
    if "aliquot" in s:
        return "ALIQUOT"
    if "cool" in s:
        return "COOL"
    if "heat" in s or "boil" in s:
        return "HEAT"
    if "mix" in s or "stir" in s:
        return "MIX"
    return "DISSOLVE"
