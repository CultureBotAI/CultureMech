#!/usr/bin/env python3
"""Repair TOGO M1981 LB + Desferrioxamine B."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path("bacterial/lb_desferrioxamine_b.yaml")
LB_PARENT = Path("bacterial/lb_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1981_lb_desferrioxamine_score15.py"
ACTION = "RESOLVED_TOGO_M1981_LB_DESFERRIOXAMINE_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

EXPECTED_ID = "CultureMech:008564"
EXPECTED_MEDIA_TERM = "TOGO:M1981"
LB_PARENT_ID = "CultureMech:008037"
TOGO_M1981 = "https://togomedium.org/medium/M1981"
NBRC_1265 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1265"
SOURCE = "TOGO M1981 / NBRC Medium 1265"

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("NaCl", "5", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
    ("Bacto Tryptone (Difco)", "10", "G_PER_L"),
    ("Deferoxamine mesylate salt", "65", "G_PER_L"),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Bacto Tryptone (Difco)", "10", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("NaCl", "5", "G_PER_L"),
    ("Deferoxamine mesylate salt", "65", "MG_PER_L"),
    ("Distilled water", "1000", "ML_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "Deferoxamine mesylate salt": ("CHEBI:4356", "desferrioxamine B"),
    "Distilled water": ("CHEBI:15377", "water"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
}

NOTES = (
    "TOGO M1981 imports NBRC Medium 1265 LB + Desferrioxamine B. NBRC 1265 "
    "lists the LB base with 65 mg/L Deferoxamine mesylate salt, 15 g/L agar "
    "if needed, and pH 7.0."
)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{LB_PARENT}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": LB_PARENT_ID,
    "name": "lb_medium",
    "notes": (
        "NBRC Medium 1265 supplements LB Medium with 65 mg/L Deferoxamine "
        "mesylate salt."
    ),
}

VARIANT_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_ID,
    "name": "lb_desferrioxamine_b",
    "notes": PARENT_MEDIA["notes"],
}

VARIANT_MODIFICATIONS = "Adds 65 mg/L Deferoxamine mesylate salt."

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Prepare the LB base from 10 g/L Bacto Tryptone (Difco), 5 g/L "
            "yeast extract, 5 g/L NaCl, 65 mg/L Deferoxamine mesylate salt, "
            "1000 ml/L distilled water, and 15 g/L agar if needed."
        ),
    },
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str = SOURCE,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _component(
        "Bacto Tryptone (Difco)",
        "10",
        "G_PER_L",
        notes=(
            "NBRC Medium 1265 lists Bacto Tryptone (Difco) as a source-disclosed "
            "digest product not reducible to one ChEBI molecule."
        ),
    ),
    _component("Yeast extract", "5", "G_PER_L"),
    _component("NaCl", "5", "G_PER_L"),
    _component(
        "Deferoxamine mesylate salt",
        "65",
        "MG_PER_L",
        notes=(
            "NBRC Medium 1265 specifies 65 mg/L Deferoxamine mesylate salt. "
            "ChEBI has a direct descriptor for the active desferrioxamine B "
            "compound."
        ),
    ),
    _component("Distilled water", "1000", "ML_PER_L"),
    _component(
        "Agar (if needed)",
        "15",
        "G_PER_L",
        notes=f"{SOURCE} lists 15 g/L agar if needed.",
    ),
)


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(f"{TARGET}: ingredient signature drifted")
    if doc.get("solutions") not in (None, []):
        raise ValueError(f"{TARGET}: expected no solutions")


def _ensure_lb_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != LB_PARENT_ID:
        raise ValueError(f"{LB_PARENT}: expected {LB_PARENT_ID}, found {doc.get('id')}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation", "resolved_reference"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (TOGO_M1981, NBRC_1265):
        if reference not in existing:
            references.append({"reference": reference})


def _append_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": f"{TOGO_M1981}; {NBRC_1265}",
        "notes": (
            f"{NOTES} Corrected the imported distilled-water row from a g/L artifact "
            "to an ml/L volume and converted the Deferoxamine mesylate salt dose "
            "from g/L to mg/L."
        ),
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _replace_variant_child(
    doc: dict[str, Any],
    child: dict[str, Any],
) -> None:
    children = [
        row
        for row in doc.get("variant_children", [])
        if not (isinstance(row, dict) and row.get("id") == child["id"])
    ]
    children.append(copy.deepcopy(child))
    doc["variant_children"] = children


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired["ph_value"] = 7.0
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("solutions", None)
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["notes"] = NOTES
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired["parent_media"] = copy.deepcopy(PARENT_MEDIA)
    repaired["variant_relationship"] = "SUPPLEMENTED_VARIANT"
    repaired["variant_modifications"] = [VARIANT_MODIFICATIONS]
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_event(repaired)
    return repaired


def repair_lb_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_lb_parent(doc)
    repaired = copy.deepcopy(doc)
    _replace_variant_child(repaired, VARIANT_CHILD)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target_path = normalized / TARGET
    lb_parent_path = normalized / LB_PARENT
    return {
        lb_parent_path: repair_lb_parent(_load(lb_parent_path)),
        target_path: repair_target(_load(target_path)),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
        if args.apply:
            changed = write_record(path, doc)
        else:
            changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
