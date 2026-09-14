#!/usr/bin/env python3
"""Repair score-15 JCM 188 / NBRC 103 duplicate and pH-variant records."""

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
JCM_PATH = Path("bacterial/jcm_medium_no_188.yaml")
JCM_SOLUTION_PATH = Path("bacterial/mediadive_3848_Main_sol_J188.yaml")
TOGO_JCM_PATH = Path("bacterial/togo_medium_m181.yaml")
TOGO_NBRC_PATH = Path("bacterial/togo_medium_m1428.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

EXPECTED_JCM_ID = "CultureMech:002549"
EXPECTED_SOLUTION_ID = "CultureMech:012921"
EXPECTED_TOGO_JCM_ID = "CultureMech:008391"
EXPECTED_TOGO_NBRC_ID = "CultureMech:007966"
EXPECTED_JCM_MEDIA_TERM = "mediadive.medium:J188"
EXPECTED_JCM_SOLUTION_TERM = "mediadive.solution:3848"
EXPECTED_TOGO_JCM_MEDIA_TERM = "TOGO:M181"
EXPECTED_TOGO_NBRC_MEDIA_TERM = "TOGO:M1428"

JCM_URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=188"
MEDIADIVE_J188 = "https://mediadive.dsmz.de/medium/J188"
MEDIADIVE_SOLUTION_3848 = "https://mediadive.dsmz.de/solutions/3848"
TOGO_M181 = "https://togomedium.org/medium/M181"
TOGO_M1428 = "https://togomedium.org/medium/M1428"
NBRC_103 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=103"

CURATOR = "repair_jcm188_m1428_score15.py"
ACTION = "RESOLVED_JCM188_M1428_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

PEPTONE = "Peptone"
YEAST_EXTRACT = "Yeast extract"
MALT_EXTRACT = "Malt extract"
GLUCOSE = "Glucose"
OLIVE_OIL = "Olive oil"
AGAR = "Agar"
DISTILLED_WATER = "Distilled water"

Component = tuple[str, str, str]

JCM_LEGACY_SIGNATURE: tuple[Component, ...] = (
    (PEPTONE, "5", "G_PER_L"),
    (YEAST_EXTRACT, "3", "G_PER_L"),
    (MALT_EXTRACT, "3", "G_PER_L"),
    (GLUCOSE, "10", "G_PER_L"),
    (OLIVE_OIL, "10", "G_PER_L"),
    (AGAR, "15", "G_PER_L"),
)

TOGO_LEGACY_SIGNATURE: tuple[Component, ...] = (
    (DISTILLED_WATER, "1", "G_PER_L"),
    (YEAST_EXTRACT, "3", "G_PER_L"),
    (OLIVE_OIL, "10", "G_PER_L"),
    (GLUCOSE, "10", "G_PER_L"),
    (AGAR, "15", "G_PER_L"),
    (MALT_EXTRACT, "3", "G_PER_L"),
    (PEPTONE, "5", "G_PER_L"),
)

FINAL_SIGNATURE: tuple[Component, ...] = (
    (PEPTONE, "5", "G_PER_L"),
    (YEAST_EXTRACT, "3", "G_PER_L"),
    (MALT_EXTRACT, "3", "G_PER_L"),
    (GLUCOSE, "10", "G_PER_L"),
    (OLIVE_OIL, "10", "G_PER_L"),
    (AGAR, "15", "G_PER_L"),
    (DISTILLED_WATER, "1000", "ML_PER_L"),
)

SOLUTION_LEGACY_SIGNATURE: tuple[Component, ...] = (
    (PEPTONE, "5", "G_PER_L"),
    (YEAST_EXTRACT, "3", "G_PER_L"),
    (MALT_EXTRACT, "3", "G_PER_L"),
    (GLUCOSE, "10", "G_PER_L"),
    (OLIVE_OIL, "10", "G_PER_L"),
    (AGAR, "15", "G_PER_L"),
    (DISTILLED_WATER, "1000", "PERCENT_V_V"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    PEPTONE: ("MICRO:0000178", "peptone"),
    YEAST_EXTRACT: ("FOODON:03315426", "yeast extract"),
    MALT_EXTRACT: ("FOODON:03301056", "malt extract"),
    GLUCOSE: ("CHEBI:17234", "glucose"),
    OLIVE_OIL: ("CHEBI:752944", "olive oil"),
    AGAR: ("CHEBI:2509", "agar"),
    DISTILLED_WATER: ("CHEBI:15377", "water"),
}

MEDIADIVE_COMPOUNDS: dict[str, tuple[str, str]] = {
    PEPTONE: ("mediadive.compound:1", "Peptone"),
    YEAST_EXTRACT: ("mediadive.compound:16", "Yeast extract"),
    MALT_EXTRACT: ("mediadive.compound:116", "Malt extract"),
    GLUCOSE: ("mediadive.compound:5", "Glucose"),
    OLIVE_OIL: ("mediadive.compound:1674", "Olive oil"),
    AGAR: ("mediadive.compound:3", "Agar"),
    DISTILLED_WATER: ("mediadive.compound:4", "Distilled water"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    PEPTONE: ("NITROGEN_SOURCE",),
    YEAST_EXTRACT: ("NITROGEN_SOURCE",),
    MALT_EXTRACT: ("CARBON_SOURCE", "NITROGEN_SOURCE"),
    GLUCOSE: ("CARBON_SOURCE",),
    OLIVE_OIL: ("CARBON_SOURCE",),
}
MEDIAINGREDIENTMECH_CHEBI = frozenset({GLUCOSE, AGAR, DISTILLED_WATER})

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}


@dataclass(frozen=True)
class RecipeSpec:
    path: Path
    expected_id: str
    expected_media_term: str
    legacy_signature: tuple[Component, ...]
    ph_value: float
    source_label: str
    source_url: str
    extra_reference: str
    parent_relationship: str | None
    parent_notes: str | None
    variant_modifications: tuple[str, ...]
    notes: str

    @property
    def references(self) -> tuple[str, str]:
        return (self.source_url, self.extra_reference)


JCM_SPEC = RecipeSpec(
    path=JCM_PATH,
    expected_id=EXPECTED_JCM_ID,
    expected_media_term=EXPECTED_JCM_MEDIA_TERM,
    legacy_signature=JCM_LEGACY_SIGNATURE,
    ph_value=6.0,
    source_label="JCM Medium 188",
    source_url=JCM_URL,
    extra_reference=MEDIADIVE_J188,
    parent_relationship=None,
    parent_notes=None,
    variant_modifications=(),
    notes=(
        "JCM Medium 188 contains 5 g/L peptone, 3 g/L yeast extract, 3 g/L "
        "malt extract, 10 g/L glucose, 10 g/L olive oil, 15 g/L agar, and "
        "distilled water, adjusted to pH 6.0."
    ),
)

TOGO_JCM_SPEC = RecipeSpec(
    path=TOGO_JCM_PATH,
    expected_id=EXPECTED_TOGO_JCM_ID,
    expected_media_term=EXPECTED_TOGO_JCM_MEDIA_TERM,
    legacy_signature=TOGO_LEGACY_SIGNATURE,
    ph_value=6.0,
    source_label="TOGO M181 / JCM Medium 188",
    source_url=TOGO_M181,
    extra_reference=JCM_URL,
    parent_relationship="SOURCE_DUPLICATE",
    parent_notes=(
        "TOGO M181 imports the same JCM Medium 188 formula represented by MediaDive J188."
    ),
    variant_modifications=("Same ingredient, concentration, and pH signature as JCM Medium 188.",),
    notes=(
        "TOGO M181 imports JCM Medium 188: peptone, yeast extract, malt "
        "extract, glucose, olive oil, agar, and distilled water adjusted to "
        "pH 6.0."
    ),
)

TOGO_NBRC_SPEC = RecipeSpec(
    path=TOGO_NBRC_PATH,
    expected_id=EXPECTED_TOGO_NBRC_ID,
    expected_media_term=EXPECTED_TOGO_NBRC_MEDIA_TERM,
    legacy_signature=TOGO_LEGACY_SIGNATURE,
    ph_value=5.6,
    source_label="TOGO M1428 / NBRC Medium 103",
    source_url=TOGO_M1428,
    extra_reference=NBRC_103,
    parent_relationship="PH_VARIANT",
    parent_notes=(
        "NBRC Medium 103 uses the same ingredient and concentration signature "
        "as JCM Medium 188, but specifies pH 5.6."
    ),
    variant_modifications=("Adjusted to pH 5.6 instead of pH 6.0.",),
    notes=(
        "NBRC Medium 103 contains 10 g/L glucose, 5 g/L peptone, 3 g/L "
        "yeast extract, 3 g/L malt extract, 10 g/L olive oil, 15 g/L agar, "
        "and 1 L distilled water, adjusted to pH 5.6."
    ),
)

SPECS: tuple[RecipeSpec, ...] = (JCM_SPEC, TOGO_JCM_SPEC, TOGO_NBRC_SPEC)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _record_term_id(doc: dict[str, Any]) -> str:
    term = doc.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _put_after(doc: dict[str, Any], key: str, value: Any, after_key: str) -> None:
    if key in doc:
        doc[key] = value
        return

    rebuilt: dict[str, Any] = {}
    placed = False
    for existing_key, existing_value in doc.items():
        rebuilt[existing_key] = existing_value
        if existing_key == after_key:
            rebuilt[key] = value
            placed = True
    if not placed:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


def _ingredient(preferred_term: str, value: str, unit: str, source: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": _term(*GROUNDINGS[preferred_term]),
    }
    if preferred_term in MEDIAINGREDIENTMECH_CHEBI:
        row["mediaingredientmech_chebi_term"] = _term(*GROUNDINGS[preferred_term])
    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles is not None:
        row["nutritional_roles"] = list(nutritional_roles)
    return row


def _solution_component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": "MediaDive solution 3848",
        "notes": f"MediaDive solution 3848 lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": _term(*MEDIADIVE_COMPOUNDS[preferred_term]),
    }
    grounding = GROUNDINGS[preferred_term]
    if grounding[0].startswith("CHEBI:"):
        row["chebi_term"] = _term(*grounding)
    return row


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag
        not in {
            "has_unmapped_ingredients",
            "incomplete_composition",
            "needs_manual_curation",
        }
    ]
    flags.extend(("has_ontology_mappings", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for reference in references:
        if reference not in existing:
            rows.append({"reference": reference})
            existing.add(reference)


def _event(source: str, notes: str) -> dict[str, str]:
    return {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": source,
        "notes": notes,
    }


def _ensure_event(doc: dict[str, Any], event: dict[str, str]) -> None:
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


def _recipe_ref(spec: RecipeSpec) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{spec.path}",
        "relationship": spec.parent_relationship or "",
        "id": spec.expected_id,
        "name": spec.path.stem,
        "notes": spec.parent_notes or "",
    }


def _parent_media(spec: RecipeSpec) -> dict[str, str]:
    if spec.parent_relationship is None or spec.parent_notes is None:
        raise ValueError(f"{spec.path}: parent metadata unavailable")
    return {
        "path": f"data/normalized_yaml/{JCM_PATH}",
        "relationship": spec.parent_relationship,
        "id": EXPECTED_JCM_ID,
        "name": JCM_PATH.stem,
        "notes": spec.parent_notes,
    }


def _ensure_recipe(doc: dict[str, Any], spec: RecipeSpec) -> None:
    if doc.get("id") != spec.expected_id:
        raise ValueError(f"{spec.path}: expected id {spec.expected_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != spec.expected_media_term:
        raise ValueError(f"{spec.path}: expected media term {spec.expected_media_term}")

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in {spec.legacy_signature, FINAL_SIGNATURE}:
        raise ValueError(f"{spec.path}: ingredient signature drifted to {signature!r}")


def _ensure_solution(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_SOLUTION_ID:
        raise ValueError(
            f"{JCM_SOLUTION_PATH}: expected id {EXPECTED_SOLUTION_ID}, found {doc.get('id')!r}"
        )
    if _record_term_id(doc) != EXPECTED_JCM_SOLUTION_TERM:
        raise ValueError(f"{JCM_SOLUTION_PATH}: expected term {EXPECTED_JCM_SOLUTION_TERM}")

    signature = _signature(doc.get("composition"), "composition")
    if signature not in {SOLUTION_LEGACY_SIGNATURE, FINAL_SIGNATURE}:
        raise ValueError(f"{JCM_SOLUTION_PATH}: composition signature drifted to {signature!r}")


def _recipe_ingredients(spec: RecipeSpec) -> list[dict[str, Any]]:
    return [
        _ingredient(name, value, unit, spec.source_label) for name, value, unit in FINAL_SIGNATURE
    ]


def _solution_composition() -> list[dict[str, Any]]:
    return [_solution_component(name, value, unit) for name, value, unit in FINAL_SIGNATURE]


def repair_recipe(doc: dict[str, Any], spec: RecipeSpec) -> dict[str, Any]:
    _ensure_recipe(doc, spec)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", spec.ph_value, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _recipe_ingredients(spec)
    _put_after(repaired, "notes", spec.notes, "media_term")
    repaired["preparation_steps"] = [
        {
            "step_number": 1,
            "action": "ADJUST_PH",
            "description": f"Adjust pH to {spec.ph_value:.1f}.",
        }
    ]
    if spec is JCM_SPEC:
        repaired["variant_children"] = [
            _recipe_ref(TOGO_JCM_SPEC),
            _recipe_ref(TOGO_NBRC_SPEC),
        ]
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)
    else:
        repaired.pop("variant_children", None)
        _put_after(repaired, "parent_media", _parent_media(spec), "curation_history")
        _put_after(
            repaired,
            "variant_relationship",
            spec.parent_relationship,
            "parent_media",
        )
        _put_after(
            repaired,
            "variant_modifications",
            list(spec.variant_modifications),
            "variant_relationship",
        )
    _ensure_flags(repaired)
    _ensure_references(repaired, spec.references)
    _ensure_event(
        repaired,
        _event(
            "; ".join(spec.references),
            (
                f"Curated {spec.expected_media_term} from {spec.source_label}; "
                "corrected the imported distilled-water unit, added pH, "
                "grounded all disclosed components, and repaired the JCM "
                "Medium 188 source-duplicate / pH-variant relationships."
            ),
        ),
    )
    return repaired


def repair_solution(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_solution(doc)

    repaired = copy.deepcopy(doc)
    repaired["composition"] = _solution_composition()
    repaired.pop("ingredients", None)
    _put_after(
        repaired,
        "preparation_notes",
        "MediaDive solution 3848 records the parsed Main sol. J188 composition.",
        "composition",
    )
    _put_after(repaired, "notes", JCM_SPEC.notes, "preparation_notes")
    _ensure_flags(repaired)
    _ensure_references(repaired, (MEDIADIVE_J188, MEDIADIVE_SOLUTION_3848))
    _ensure_event(
        repaired,
        _event(
            f"{MEDIADIVE_J188}; {MEDIADIVE_SOLUTION_3848}",
            (
                "Restored Main sol. J188 as the parsed MediaDive solution, "
                "corrected the distilled-water unit to ml/L, and removed the "
                "placeholder ingredient row."
            ),
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans = {
        normalized / spec.path: repair_recipe(_load(normalized / spec.path), spec) for spec in SPECS
    }
    plans[normalized / JCM_SOLUTION_PATH] = repair_solution(_load(normalized / JCM_SOLUTION_PATH))
    return plans


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
