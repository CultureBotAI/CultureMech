#!/usr/bin/env python3
"""Repair TOGO M455 Alkali-Reinforced Clostridial Agar and its JCM J455 duplicate."""

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
TARGET = Path("bacterial/TOGO_M455_Alkali-Reinforced_Clostridial_Agar.yaml")
PARENT = Path("bacterial/alkali_reinforced_clostridial_agar.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_ID = "CultureMech:009842"
EXPECTED_PARENT_ID = "CultureMech:002805"
EXPECTED_MEDIA_TERM = "TOGO:M455"
EXPECTED_PARENT_MEDIA_TERM = "mediadive.medium:J455"

CURATOR = "repair_togo_m455_score15.py"
ACTION = "RESOLVED_TOGO_M455_SCORE15"
PARENT_ACTION = "RESOLVED_JCM_455_ALKALI_REINFORCED_CLOSTRIDIAL_AGAR"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M455 = "https://togomedium.org/medium/M455"
MEDIADIVE_J455 = "https://mediadive.dsmz.de/medium/J455"
JCM_455 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=455"

TOGO_SOURCE = "TOGO M455 / JCM Medium 455"
PARENT_SOURCE = "MediaDive J455 / JCM Medium 455"
TITLE = "Alkali-Reinforced Clostridial Agar"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "900", "G_PER_L"),
    ("Reinforced clostridial agar (Sigma)", "51", "G_PER_L"),
)

IMPORTED_PARENT_INGREDIENT_SIGNATURE: tuple[Component, ...] = (("Agar", "56.6667", "G_PER_L"),)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Reinforced clostridial agar (Sigma)", "51.0", "G_PER_L"),
    ("Distilled water", "900.0", "ML_PER_L"),
)

SODIUM_CARBONATE_SIGNATURE: tuple[Component, ...] = (("Na2CO3", "10.0", "PERCENT_W_V"),)

IMPORTED_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("Na2CO3 solution", "100", "G_PER_L", ()),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("10% Na2CO3 solution", "100.0", "ML_PER_L", SODIUM_CARBONATE_SIGNATURE),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Distilled water": ("CHEBI:15377", "water"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}

REFERENCES = (TOGO_M455, JCM_455, MEDIADIVE_J455)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{PARENT}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_PARENT_ID,
    "name": "alkali_reinforced_clostridial_agar",
    "notes": (
        "TOGO M455 imports the same JCM Medium 455 Alkali-Reinforced "
        "Clostridial Agar formulation represented by MediaDive J455."
    ),
}

TOGO_CHILD = {
    "path": f"data/normalized_yaml/{TARGET}",
    "relationship": "SOURCE_DUPLICATE",
    "id": EXPECTED_ID,
    "name": "alkali_reinforced_clostridial_agar",
    "notes": (
        "TOGO M455 imports the same JCM Medium 455 Alkali-Reinforced "
        "Clostridial Agar formulation represented by MediaDive J455."
    ),
}

VARIANT_MODIFICATIONS = (
    "Same JCM Medium 455 Alkali-Reinforced Clostridial Agar formulation as "
    "the MediaDive J455 source record."
)

RECIPE_NOTES = (
    "JCM Medium 455 Alkali-Reinforced Clostridial Agar lists 51 g "
    "Reinforced clostridial agar (Sigma) in 900 ml distilled water per liter. "
    "After autoclaving at 121 C for 15 min, 100 ml of sterile 10% Na2CO3 "
    "solution is added aseptically and the final pH is checked to be about "
    "10.0."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": ("Autoclave the reinforced clostridial agar base at 121 C for 15 min."),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Aseptically add 100 ml/L sterile 10% Na2CO3 solution after " "autoclaving."
        ),
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "Check final pH to be about 10.0.",
    },
)

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "Sterilize the 10% Na2CO3 solution separately before aseptic addition.",
}


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
    source: str,
    notes: str | None = None,
    term: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(source: str) -> list[dict[str, Any]]:
    return [
        _component(
            "Reinforced clostridial agar (Sigma)",
            "51.0",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists 51.0 g/L Reinforced clostridial agar "
                "(Sigma); this dehydrated commercial mixture is retained as "
                "an opaque complex component."
            ),
            term=False,
        ),
        _component("Distilled water", "900.0", "ML_PER_L", source=source),
    ]


def _solutions(source: str) -> list[dict[str, Any]]:
    notes = f"{source} adds 100.0 ml/L sterile 10% Na2CO3 solution."
    return [
        {
            "preferred_term": "10% Na2CO3 solution",
            "concentration": {"value": "100.0", "unit": "ML_PER_L"},
            "source": source,
            "notes": notes,
            "composition": [
                _component(
                    "Na2CO3",
                    "10.0",
                    "PERCENT_W_V",
                    source=source,
                    notes="JCM Medium 455 specifies a 10% Na2CO3 solution.",
                )
            ],
            "preparation_notes": ("Sterilize the 10% Na2CO3 solution before aseptic addition."),
        }
    ]


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
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_signatures(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signatures: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signatures.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), f"{label} composition"),
            )
        )
    return tuple(signatures)


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
        raise ValueError(f"expected {EXPECTED_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"expected media term {EXPECTED_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("target ingredient signature drifted")
    if _solution_signatures(doc.get("solutions"), "solutions") not in (
        IMPORTED_SOLUTION_SIGNATURES,
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError("target solution signature drifted")


def _ensure_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_PARENT_ID:
        raise ValueError(f"expected {EXPECTED_PARENT_ID}, found {doc.get('id')}")
    if _source_term_id(doc) != EXPECTED_PARENT_MEDIA_TERM:
        raise ValueError(f"expected media term {EXPECTED_PARENT_MEDIA_TERM}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        IMPORTED_PARENT_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError("parent ingredient signature drifted")
    if _solution_signatures(doc.get("solutions"), "solutions") not in (
        (),
        FINAL_SOLUTION_SIGNATURES,
    ):
        raise ValueError("parent solution signature drifted")
    kg_match = doc.get("kg_microbe_match")
    if kg_match not in (None, "mediadive.medium:12"):
        raise ValueError(f"parent unexpected kg_microbe_match {kg_match!r}")


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    if key in doc:
        doc[key] = value
        return

    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True
    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
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
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], *, action: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(REFERENCES),
        "notes": RECIPE_NOTES,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def _ensure_child_link(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    filtered: list[Any] = []
    inserted = False
    for child in children:
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_ID or child.get("path") == TOGO_CHILD["path"]:
            if not inserted:
                filtered.append(copy.deepcopy(TOGO_CHILD))
                inserted = True
            continue
        filtered.append(child)

    if not inserted:
        filtered.append(copy.deepcopy(TOGO_CHILD))
    doc["variant_children"] = filtered


def _repair_common(
    doc: dict[str, Any],
    *,
    source: str,
    action: str,
) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 10.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired["ingredients"] = _ingredients(source)
    _put_after(repaired, "solutions", _solutions(source), "ingredients")
    _put_after(repaired, "preparation_steps", list(PREPARATION_STEPS), "solutions")
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _put_after(repaired, "notes", RECIPE_NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired, action=action)
    return repaired


def repair_target(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(doc)

    repaired = _repair_common(doc, source=TOGO_SOURCE, action=ACTION)
    _put_after(repaired, "parent_media", copy.deepcopy(PARENT_MEDIA), "references")
    _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
    _put_after(
        repaired,
        "variant_modifications",
        [VARIANT_MODIFICATIONS],
        "variant_relationship",
    )
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_parent(doc)

    repaired = _repair_common(doc, source=PARENT_SOURCE, action=PARENT_ACTION)
    repaired.pop("kg_microbe_match", None)
    _ensure_child_link(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    target = normalized / TARGET
    parent = normalized / PARENT
    return {
        target: repair_target(_load(target)),
        parent: repair_parent(_load(parent)),
    }


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in plans.items():
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
