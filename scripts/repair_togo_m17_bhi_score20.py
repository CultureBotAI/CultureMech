#!/usr/bin/env python3
"""Repair score-20 TOGO M17/BHI sugar-supplement wrappers."""

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

CURATOR = "repair_togo_m17_bhi_score20.py"
ACTION = "RESOLVED_TOGO_M17_BHI_SCORE20"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

M2230_M17_LACTOSE = "bacterial/m17_medium_supplemented_with_20_g_l_of_lactose.yaml"
M2492_M17_GLUCOSE = "bacterial/m17_broth_containing_glucose.yaml"
M2493_M17_LACTOSE = "bacterial/m17_broth_containing_lactose.yaml"
M2830_BHI_GLUCOSE = "bacterial/brain_heart_infusion_broth_with_glucose.yaml"
M2882_M17_DIFCO_GLUCOSE = "bacterial/m17_medium_difco_containing_0_5_glucose_gm17.yaml"
M2951_GM17_OXOID = "bacterial/gm17.yaml"

TOGO_M2230 = "https://togomedium.org/medium/M2230"
TOGO_M2492 = "https://togomedium.org/medium/M2492"
TOGO_M2493 = "https://togomedium.org/medium/M2493"
TOGO_M2830 = "https://togomedium.org/medium/M2830"
TOGO_M2882 = "https://togomedium.org/medium/M2882"
TOGO_M2951 = "https://togomedium.org/medium/M2951"

EXPECTED_IDS = {
    M2230_M17_LACTOSE: "CultureMech:008819",
    M2492_M17_GLUCOSE: "CultureMech:009066",
    M2493_M17_LACTOSE: "CultureMech:009067",
    M2830_BHI_GLUCOSE: "CultureMech:009375",
    M2882_M17_DIFCO_GLUCOSE: "CultureMech:009417",
    M2951_GM17_OXOID: "CultureMech:009478",
}

EXPECTED_SOURCE_TERMS = {
    M2230_M17_LACTOSE: "TOGO:M2230",
    M2492_M17_GLUCOSE: "TOGO:M2492",
    M2493_M17_LACTOSE: "TOGO:M2493",
    M2830_BHI_GLUCOSE: "TOGO:M2830",
    M2882_M17_DIFCO_GLUCOSE: "TOGO:M2882",
    M2951_GM17_OXOID: "TOGO:M2951",
}

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "temperature_value",
    "temperature_range",
    "ingredients",
    "preparation_steps",
    "sterilization",
)


@dataclass(frozen=True)
class WrapperUpdate:
    path: str
    source_label: str
    notes: str
    reference_url: str
    temperature_value: float
    ingredients: tuple[dict[str, Any], ...]
    preparation_steps: tuple[str, ...]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _sugar(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
        "term": _term(*term),
        "mediaingredientmech_chebi_term": _term(*term),
    }


def _opaque_product(preferred_term: str, source: str) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": "1000", "unit": "ML_PER_L"},
        "source": source,
        "notes": (
            f"{source} lists one liter of {preferred_term} without disclosing "
            "the internal formulation."
        ),
    }


def _mix_step(step_number: int, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": "MIX",
        "description": description,
    }


UPDATES: tuple[WrapperUpdate, ...] = (
    WrapperUpdate(
        path=M2230_M17_LACTOSE,
        source_label="TOGO M2230",
        notes=(
            "TOGO M2230 lists M17 medium from Scharlau supplemented with "
            "20 g/L lactose and cultivated anaerobically at 42 C."
        ),
        reference_url=TOGO_M2230,
        temperature_value=42.0,
        ingredients=(
            _sugar(
                "Lactose",
                "20",
                "G_PER_L",
                source="TOGO M2230",
                notes="TOGO M2230 lists lactose added at 20 g/L.",
                term=("CHEBI:36218", "beta-lactose"),
            ),
            _opaque_product("M17 medium (Scharlau)", "TOGO M2230"),
        ),
        preparation_steps=(
            "Supplement one liter of M17 medium (Scharlau) with 20 g/L lactose.",
            "Cultivate anaerobically at 42 C.",
        ),
    ),
    WrapperUpdate(
        path=M2492_M17_GLUCOSE,
        source_label="TOGO M2492",
        notes=(
            "TOGO M2492 lists M17 broth with glucose at a final concentration "
            "of 1% and overnight anaerobic cultivation at 37 C."
        ),
        reference_url=TOGO_M2492,
        temperature_value=37.0,
        ingredients=(
            _sugar(
                "glucose",
                "1",
                "PERCENT_W_V",
                source="TOGO M2492",
                notes="TOGO M2492 lists glucose at a final concentration of 1%.",
                term=("CHEBI:17234", "glucose"),
            ),
            _opaque_product("M17 broth", "TOGO M2492"),
        ),
        preparation_steps=(
            "Supplement one liter of M17 broth with glucose to 1% final concentration.",
            "Cultivate overnight at 37 C in an anaerobic atmosphere.",
        ),
    ),
    WrapperUpdate(
        path=M2493_M17_LACTOSE,
        source_label="TOGO M2493",
        notes=(
            "TOGO M2493 lists M17 broth with lactose at a final concentration "
            "of 1% and overnight anaerobic cultivation at 37 C."
        ),
        reference_url=TOGO_M2493,
        temperature_value=37.0,
        ingredients=(
            _sugar(
                "lactose",
                "1",
                "PERCENT_W_V",
                source="TOGO M2493",
                notes="TOGO M2493 lists lactose at a final concentration of 1%.",
                term=("CHEBI:36218", "beta-lactose"),
            ),
            _opaque_product("M17 broth", "TOGO M2493"),
        ),
        preparation_steps=(
            "Supplement one liter of M17 broth with lactose to 1% final concentration.",
            "Cultivate overnight at 37 C in an anaerobic atmosphere.",
        ),
    ),
    WrapperUpdate(
        path=M2830_BHI_GLUCOSE,
        source_label="TOGO M2830",
        notes=(
            "TOGO M2830 lists brain-heart infusion broth from Difco with "
            "glucose added to 0.1% and shaken cultivation at 36 C."
        ),
        reference_url=TOGO_M2830,
        temperature_value=36.0,
        ingredients=(
            _sugar(
                "glucose",
                "0.1",
                "PERCENT_W_V",
                source="TOGO M2830",
                notes="TOGO M2830 lists glucose added to 0.1%.",
                term=("CHEBI:17234", "glucose"),
            ),
            _opaque_product("brain-heart infusion broth (Difco)", "TOGO M2830"),
        ),
        preparation_steps=(
            "Supplement one liter of brain-heart infusion broth (Difco) with glucose to 0.1%.",
            "Shake culture for 18-20 h at 36 C.",
        ),
    ),
    WrapperUpdate(
        path=M2882_M17_DIFCO_GLUCOSE,
        source_label="TOGO M2882",
        notes=(
            "TOGO M2882 lists M17 broth from Difco containing 0.5% glucose "
            "and static cultivation at 30 C for 18 h."
        ),
        reference_url=TOGO_M2882,
        temperature_value=30.0,
        ingredients=(
            _sugar(
                "Glucose",
                "0.5",
                "PERCENT_W_V",
                source="TOGO M2882",
                notes="TOGO M2882 lists 0.5% glucose.",
                term=("CHEBI:17234", "glucose"),
            ),
            _opaque_product("M17 broth (Difco)", "TOGO M2882"),
        ),
        preparation_steps=(
            "Supplement one liter of M17 broth (Difco) with glucose to 0.5%.",
            "Cultivate without agitation at 30 C for 18 h.",
        ),
    ),
    WrapperUpdate(
        path=M2951_GM17_OXOID,
        source_label="TOGO M2951",
        notes=(
            "TOGO M2951 lists M17 medium from Oxoid lot 2216165 supplemented "
            "with 0.5% w/v glucose and statically incubated at 30 C for 48 h."
        ),
        reference_url=TOGO_M2951,
        temperature_value=30.0,
        ingredients=(
            _sugar(
                "glucose",
                "0.5",
                "PERCENT_W_V",
                source="TOGO M2951",
                notes="TOGO M2951 lists glucose at 0.5% w/v.",
                term=("CHEBI:17234", "glucose"),
            ),
            _opaque_product("M17 media (Oxoid LOT2216165)", "TOGO M2951"),
        ),
        preparation_steps=(
            "Supplement one liter of M17 media (Oxoid LOT2216165) with 0.5% w/v glucose.",
            "Statically incubate 50 mL cultures at 30 C for 48 h.",
        ),
    ),
)

UPDATE_BY_PATH = {update.path: update for update in UPDATES}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True

    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ingredient_terms(doc: dict[str, Any]) -> set[str]:
    return {
        str(row.get("preferred_term") or "").lower()
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    }


def _require_source_components(doc: dict[str, Any], update: WrapperUpdate) -> None:
    if doc.get("id") != EXPECTED_IDS[update.path]:
        raise ValueError(
            f"{update.path}: found id {doc.get('id')!r}, " f"expected {EXPECTED_IDS[update.path]!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[update.path]:
        raise ValueError(
            f"{update.path}: found source term {source_term!r}, "
            f"expected {EXPECTED_SOURCE_TERMS[update.path]!r}"
        )

    expected_terms = {row["preferred_term"].lower() for row in update.ingredients}
    if _ingredient_terms(doc) != expected_terms:
        raise ValueError(
            f"{update.path}: found ingredient terms {sorted(_ingredient_terms(doc))!r}, "
            f"expected {sorted(expected_terms)!r}"
        )


def _grounded(component: dict[str, Any]) -> bool:
    for key in (
        "term",
        "mediaingredientmech_term",
        "mediaingredientmech_chebi_term",
        "culturemech_term",
    ):
        term = component.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)

    if "ingredients_curated" not in flags:
        flags.append("ingredients_curated")

    rows = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    has_grounded = any(_grounded(row) for row in rows)
    has_unmapped = any(not _grounded(row) for row in rows)

    if has_grounded and "has_ontology_mappings" not in flags:
        flags.append("has_ontology_mappings")
    elif not has_grounded and "has_ontology_mappings" in flags:
        flags.remove("has_ontology_mappings")

    if has_unmapped and "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")
    elif not has_unmapped and "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")

    if flags:
        doc["data_quality_flags"] = flags
    else:
        doc.pop("data_quality_flags", None)


def _ensure_references(doc: dict[str, Any], update: WrapperUpdate) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{update.path}: references is not a list")
    if update.reference_url not in {
        row.get("reference") for row in references if isinstance(row, dict)
    }:
        references.append({"reference": update.reference_url})


def _history(doc: dict[str, Any], path: str) -> list[Any]:
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{path}: curation_history is not a list")
    return history


def _append_curation_event(doc: dict[str, Any], update: WrapperUpdate) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved score-20 TOGO M17/BHI sugar-supplement wrapper",
        "source": update.reference_url,
        "notes": update.notes,
    }
    history = _history(doc, update.path)
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_wrapper(doc: dict[str, Any], update: WrapperUpdate) -> dict[str, Any]:
    _require_source_components(doc, update)

    repaired = copy.deepcopy(doc)
    for field in RECIPE_FIELDS:
        repaired.pop(field, None)

    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["temperature_value"] = update.temperature_value
    repaired["ingredients"] = [copy.deepcopy(row) for row in update.ingredients]
    repaired["preparation_steps"] = [
        _mix_step(index, description)
        for index, description in enumerate(update.preparation_steps, start=1)
    ]
    _put_after(repaired, "notes", update.notes, "media_term")

    _ensure_flags(repaired)
    _ensure_references(repaired, update)
    _append_curation_event(repaired, update)
    if "data_quality_flags" in repaired:
        _put_after(
            repaired,
            "data_quality_flags",
            repaired["data_quality_flags"],
            "preparation_steps",
        )
    if "references" in repaired:
        _put_after(repaired, "references", repaired["references"], "data_quality_flags")
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for update in UPDATES:
        plans[normalized / update.path] = repair_wrapper(
            _load(normalized / update.path),
            update,
        )
    return plans


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
