#!/usr/bin/env python3
"""Repair fungal JCM 2% and 4% malt agar score-15 imports."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_jcm_malt_agar_score15.py"
ACTION = "RESOLVED_JCM_MALT_AGAR_SCORE15"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

Component = tuple[str, str, str]

MALT_EXTRACT = "Malt extract (BD-Difco)"
IMPORTED_INGREDIENT_SIGNATURES: dict[Path, tuple[Component, ...]] = {
    Path("fungal/2_malt_agar.yaml"): (
        ("Malt extract", "20", "G_PER_L"),
        ("Agar", "20", "G_PER_L"),
    ),
    Path("fungal/4_malt_agar.yaml"): (
        ("Malt extract", "40", "G_PER_L"),
        ("Agar", "20", "G_PER_L"),
    ),
}

FINAL_INGREDIENT_SIGNATURES: dict[Path, tuple[Component, ...]] = {
    Path("fungal/2_malt_agar.yaml"): (
        (MALT_EXTRACT, "20", "G_PER_L"),
        ("Agar", "20", "G_PER_L"),
        ("Distilled water", "1000.0", "ML_PER_L"),
    ),
    Path("fungal/4_malt_agar.yaml"): (
        (MALT_EXTRACT, "40", "G_PER_L"),
        ("Agar", "20", "G_PER_L"),
        ("Distilled water", "1000.0", "ML_PER_L"),
    ),
}

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
}


@dataclass(frozen=True)
class Target:
    path: Path
    identifier: str
    media_term_id: str
    medium_no: str
    source_url: str
    mediadive_page: str
    mediadive_rest: str
    malt_grams: str
    ph_value: float

    @property
    def source_label(self) -> str:
        return f"MediaDive JCM Medium {self.medium_no}"

    @property
    def references(self) -> tuple[str, ...]:
        urls = [self.mediadive_page, self.mediadive_rest]
        if self.source_url:
            urls.append(self.source_url)
        return tuple(urls)


TARGETS: tuple[Target, ...] = (
    Target(
        path=Path("fungal/2_malt_agar.yaml"),
        identifier="CultureMech:010523",
        media_term_id="mediadive.medium:J38",
        medium_no="J38",
        source_url="https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=38",
        mediadive_page="https://mediadive.dsmz.de/medium/J38",
        mediadive_rest="https://mediadive.dsmz.de/rest/medium/J38",
        malt_grams="20",
        ph_value=6.5,
    ),
    Target(
        path=Path("fungal/4_malt_agar.yaml"),
        identifier="CultureMech:010514",
        media_term_id="mediadive.medium:J253",
        medium_no="J253",
        source_url="",
        mediadive_page="https://mediadive.dsmz.de/medium/J253",
        mediadive_rest="https://mediadive.dsmz.de/rest/medium/J253",
        malt_grams="40",
        ph_value=7.0,
    ),
)
TARGET_BY_PATH = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(preferred_term: str, value: str, unit: str, source_label: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source_label,
        "notes": f"{source_label} lists {value} g/L {preferred_term}.",
    }
    if preferred_term == "Distilled water":
        row["notes"] = f"{source_label} lists 1000 mL distilled water per 1 L medium."
    elif preferred_term == MALT_EXTRACT:
        row["notes"] = (
            f"{source_label} lists {value} g/L Malt extract with the BD-Difco "
            "attribute; left ungrounded as an undefined commercial extract."
        )

    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(target: Target) -> list[dict[str, Any]]:
    return [
        _ingredient(MALT_EXTRACT, target.malt_grams, "G_PER_L", target.source_label),
        _ingredient("Agar", "20", "G_PER_L", target.source_label),
        _ingredient("Distilled water", "1000.0", "ML_PER_L", target.source_label),
    ]


def _notes(target: Target) -> str:
    return (
        f"{target.source_label} lists {target.malt_grams} g/L Malt extract "
        f"(BD-Difco), 20 g/L Agar, 1000 mL/L Distilled water, and pH "
        f"{target.ph_value:.1f}."
    )


def _signature(rows: Any) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("ingredients is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("ingredients contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"ingredient {row.get('preferred_term')!r} lacks concentration")
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


def _ensure_target(target: Target, doc: dict[str, Any]) -> None:
    if doc.get("id") != target.identifier:
        raise ValueError(f"{target.path}: expected id {target.identifier}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.media_term_id:
        raise ValueError(f"{target.path}: expected media term {target.media_term_id}")

    ingredient_signature = _signature(doc.get("ingredients"))
    if ingredient_signature not in {
        IMPORTED_INGREDIENT_SIGNATURES[target.path],
        FINAL_INGREDIENT_SIGNATURES[target.path],
    }:
        raise ValueError(f"{target.path}: ingredient signature drifted to {ingredient_signature!r}")

    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    if solutions:
        raise ValueError(f"{target.path}: unexpected solutions")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag not in {"extracted_from_notes", "incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(target: Target, doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {
        row.get("reference")
        for row in references
        if isinstance(row, dict) and isinstance(row.get("reference"), str)
    }
    for url in target.references:
        if url not in existing:
            references.append({"reference": url})


def _append_event(target: Target, doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": target.mediadive_rest,
        "notes": (
            f"Added the missing 1000 mL/L distilled water row from {target.source_label}; "
            "preserved malt extract as an intentionally ungrounded BD-Difco commercial "
            "extract; and removed the stale mediadive.medium:12 fallback match."
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


def repair_record(target: Target, doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(target, doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    repaired["notes"] = _notes(target)
    repaired["ingredients"] = _ingredients(target)
    _put_after(
        repaired,
        "preparation_steps",
        [
            {
                "step_number": 1,
                "action": "ADJUST_PH",
                "description": f"Adjust pH to {target.ph_value:.1f}.",
            }
        ],
        "ingredients",
    )
    repaired.pop("kg_microbe_match", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _ensure_flags(repaired)
    _ensure_references(target, repaired)
    _append_event(target, repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(target, _load(path))
    return plans


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
