#!/usr/bin/env python3
"""Repair MediaDB TAP auto and hetero/mixo records."""

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
TAP_AUTO = Path("bacterial/tap_auto.yaml")
TAP_HETERO_MIXO = Path("bacterial/tap_hetero_mixo.yaml")
EXPECTED_AUTO_ID = "CultureMech:007283"
EXPECTED_HETERO_ID = "CultureMech:007272"
EXPECTED_AUTO_MEDIA_TERM = "MEDIADB:37"
EXPECTED_HETERO_MEDIA_TERM = "MEDIADB:36"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_mediadb_tap_score15.py"
ACTION = "RESOLVED_MEDIADB_TAP_SCORE15"
PARENT_ACTION = "LINKED_MEDIADB_TAP_ACETATE_VARIANT"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

MEDIA_AUTO = "https://mediadb.systemsbiology.net/defined_media/media/37/"
MEDIA_HETERO_MIXO = "https://mediadb.systemsbiology.net/defined_media/media/36/"
SOURCE_BOYLE = "https://mediadb.systemsbiology.net/defined_media/sources/15/"
GROWTH_AUTO = "https://mediadb.systemsbiology.net/defined_media/growthdata/86/"
GROWTH_HETERO = "https://mediadb.systemsbiology.net/defined_media/growthdata/85/"
GROWTH_MIXO = "https://mediadb.systemsbiology.net/defined_media/growthdata/87/"
BOYLE_DOI = "DOI:10.1186/1752-0509-3-4"

ORTHOPHOSPHATE = "Orthophosphate"
ACETATE = "Acetate"
MANGANESE = "Manganese"
ZINC = "Zinc"
SULFATE = "Sulfate"
COPPER = "Copper"
CALCIUM = "Calcium"
MOLYBDENUM = "Molybdenum"
COBALT = "Cobalt ion"
POTASSIUM = "Potassium"
EDTA = "EDTA"
MAGNESIUM = "Magnesium"
CHLORIDE = "Cl-"
SODIUM = "Sodium"
AMMONIUM = "NH4+"
TRIS = "Tromethamine"
IRON_II = "Fe2+"
BORATE = "Borate"

Component = tuple[str, str, str]

GROUNDINGS: dict[str, tuple[str, str]] = {
    ORTHOPHOSPHATE: ("CHEBI:18367", "phosphate(3-)"),
    ACETATE: ("CHEBI:30089", "acetate"),
    MANGANESE: ("CHEBI:29035", "manganese(2+)"),
    ZINC: ("CHEBI:29105", "zinc(2+)"),
    SULFATE: ("CHEBI:16189", "sulfate"),
    COPPER: ("CHEBI:29036", "copper(2+)"),
    CALCIUM: ("CHEBI:29108", "calcium(2+)"),
    MOLYBDENUM: ("CHEBI:28685", "molybdenum atom"),
    COBALT: ("CHEBI:48828", "cobalt(2+)"),
    POTASSIUM: ("CHEBI:29103", "potassium(1+)"),
    EDTA: ("CHEBI:4735", "ethylenediaminetetraacetic acid"),
    MAGNESIUM: ("CHEBI:18420", "magnesium(2+)"),
    CHLORIDE: ("CHEBI:17996", "chloride"),
    SODIUM: ("CHEBI:29101", "sodium(1+)"),
    AMMONIUM: ("CHEBI:28938", "ammonium"),
    TRIS: ("CHEBI:9754", "tris"),
    IRON_II: ("CHEBI:29033", "iron(2+)"),
    BORATE: ("CHEBI:22908", "borate"),
}

AUTO_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (ORTHOPHOSPHATE, "1.0", "MILLIMOLAR"),
    (MANGANESE, "0.0256", "MILLIMOLAR"),
    (ZINC, "0.0765", "MILLIMOLAR"),
    (SULFATE, "0.51", "MILLIMOLAR"),
    (COPPER, "0.0063", "MILLIMOLAR"),
    (CALCIUM, "0.34", "MILLIMOLAR"),
    (MOLYBDENUM, "0.0062", "MILLIMOLAR"),
    (COBALT, "0.0068", "MILLIMOLAR"),
    (POTASSIUM, "1.94", "MILLIMOLAR"),
    (EDTA, "0.134", "MILLIMOLAR"),
    (MAGNESIUM, "0.041", "MILLIMOLAR"),
    (CHLORIDE, "8.22", "MILLIMOLAR"),
    (SODIUM, "0.27", "MILLIMOLAR"),
    (AMMONIUM, "7.48", "MILLIMOLAR"),
    (TRIS, "20.0", "MILLIMOLAR"),
    (IRON_II, "0.0179", "MILLIMOLAR"),
    (BORATE, "0.184", "MILLIMOLAR"),
)
HETERO_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    (ORTHOPHOSPHATE, "1.0", "MILLIMOLAR"),
    (ACETATE, "17.4", "MILLIMOLAR"),
    *AUTO_INGREDIENT_SIGNATURE[1:],
)

AUTO_CHILD = {
    "path": f"data/normalized_yaml/{TAP_HETERO_MIXO}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_HETERO_ID,
    "name": "tap_hetero_mixo",
    "notes": (
        "Shares the MediaDB TAP (auto) base formulation and adds 17.4 mM "
        "acetate for heterotrophic and mixotrophic growth."
    ),
}

HETERO_PARENT = {
    "path": f"data/normalized_yaml/{TAP_AUTO}",
    "relationship": "SUPPLEMENTED_VARIANT",
    "id": EXPECTED_AUTO_ID,
    "name": "tap_auto",
    "notes": "The hetero/mixo formulation adds 17.4 mM acetate to MediaDB TAP (auto).",
}

AUTO_NOTES = (
    "MediaDB Medium 37 lists TAP (auto) as a chemically defined, minimal "
    "17-component formulation for Chlamydomonas reinhardtii. MediaDB links it "
    "to Boyle et al. 2009 and reports autotrophic growth at pH 7.0 and 25 C."
)
HETERO_NOTES = (
    "MediaDB Medium 36 lists TAP (hetero/mixo) as the MediaDB TAP base "
    "formulation supplemented with 17.4 mM acetate for Chlamydomonas "
    "reinhardtii heterotrophic and mixotrophic growth at pH 7.0 and 25 C."
)


@dataclass(frozen=True)
class GrowthMetricSpec:
    url: str
    rate: str
    context: str
    explanation: str


@dataclass(frozen=True)
class RecordSpec:
    target: Path
    expected_id: str
    expected_media_term: str
    source_url: str
    source_name: str
    notes: str
    ingredient_signature: tuple[Component, ...]
    references: tuple[str, ...]
    growth_metrics: tuple[GrowthMetricSpec, ...]


AUTO_SPEC = RecordSpec(
    target=TAP_AUTO,
    expected_id=EXPECTED_AUTO_ID,
    expected_media_term=EXPECTED_AUTO_MEDIA_TERM,
    source_url=MEDIA_AUTO,
    source_name="MediaDB Medium 37 TAP (auto)",
    notes=AUTO_NOTES,
    ingredient_signature=AUTO_INGREDIENT_SIGNATURE,
    references=(MEDIA_AUTO, SOURCE_BOYLE, GROWTH_AUTO, BOYLE_DOI),
    growth_metrics=(
        GrowthMetricSpec(
            url=GROWTH_AUTO,
            rate="0.059",
            context=(
                "MediaDB autotrophic TAP growth-data record 86 with carbon "
                "dioxide uptake and max solar flux 2100 uE/m2/s."
            ),
            explanation=(
                "MediaDB growth-data record 86 reports Chlamydomonas "
                "reinhardtii growth on TAP (auto) at pH 7.0 and 25 C."
            ),
        ),
    ),
)
HETERO_SPEC = RecordSpec(
    target=TAP_HETERO_MIXO,
    expected_id=EXPECTED_HETERO_ID,
    expected_media_term=EXPECTED_HETERO_MEDIA_TERM,
    source_url=MEDIA_HETERO_MIXO,
    source_name="MediaDB Medium 36 TAP (hetero/mixo)",
    notes=HETERO_NOTES,
    ingredient_signature=HETERO_INGREDIENT_SIGNATURE,
    references=(MEDIA_HETERO_MIXO, SOURCE_BOYLE, GROWTH_HETERO, GROWTH_MIXO, BOYLE_DOI),
    growth_metrics=(
        GrowthMetricSpec(
            url=GROWTH_HETERO,
            rate="0.035",
            context=(
                "MediaDB heterotrophic TAP growth-data record 85 with acetate "
                "uptake at 12.06 mmol/gDW/h."
            ),
            explanation=(
                "MediaDB growth-data record 85 reports heterotrophic "
                "Chlamydomonas reinhardtii growth on TAP (hetero/mixo) at "
                "pH 7.0 and 25 C."
            ),
        ),
        GrowthMetricSpec(
            url=GROWTH_MIXO,
            rate="0.066",
            context="MediaDB mixotrophic TAP growth-data record 87.",
            explanation=(
                "MediaDB growth-data record 87 reports mixotrophic "
                "Chlamydomonas reinhardtii growth on TAP (hetero/mixo) at "
                "pH 7.0 and 25 C."
            ),
        ),
    ),
)
SPECS: tuple[RecordSpec, ...] = (AUTO_SPEC, HETERO_SPEC)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(name: str, value: str, unit: str, spec: RecordSpec) -> dict[str, Any]:
    identifier, label = GROUNDINGS[name]
    term = _term(identifier, label)
    return {
        "preferred_term": name,
        "term": copy.deepcopy(term),
        "concentration": {"value": value, "unit": unit},
        "source": spec.source_name,
        "notes": f"{spec.source_name} lists {value} mM {name}.",
        "mediaingredientmech_chebi_term": copy.deepcopy(term),
    }


def _target_organisms(spec: RecordSpec) -> list[dict[str, Any]]:
    return [
        {
            "preferred_term": "Chlamydomonas reinhardtii",
            "term": {
                "id": "NCBITaxon:3055",
                "label": "Chlamydomonas reinhardtii",
            },
            "growth_metrics": [
                {
                    "measurement_conditions": metric.context,
                    "growth_rate_per_hour": float(metric.rate),
                    "temperature_celsius": 25.0,
                    "ph_at_measurement": 7.0,
                    "evidence": [
                        {
                            "reference": metric.url,
                            "supports": "SUPPORT",
                            "explanation": metric.explanation,
                        }
                    ],
                    "is_max_attainment": False,
                }
                for metric in spec.growth_metrics
            ],
            "evidence": [
                {
                    "reference": spec.source_url,
                    "supports": "SUPPORT",
                    "explanation": (
                        f"{spec.source_name} lists Chlamydomonas reinhardtii "
                        "as an organism for this formulation and links "
                        "Boyle et al. 2009 as the source."
                    ),
                }
            ],
        }
    ]


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


def _ensure_target(doc: dict[str, Any], spec: RecordSpec) -> None:
    if doc.get("id") != spec.expected_id:
        raise ValueError(f"{spec.target}: expected id {spec.expected_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != spec.expected_media_term:
        raise ValueError(f"{spec.target}: expected media term {spec.expected_media_term}")

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature != spec.ingredient_signature:
        raise ValueError(
            f"{spec.target}: ingredient signature drifted from "
            f"{spec.ingredient_signature!r} to {signature!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag for flag in flags if flag not in {"incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], spec: RecordSpec) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in spec.references:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_event(doc: dict[str, Any], *, action: str, source: str, notes: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": source,
        "notes": notes,
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


def _ensure_parent_link(doc: dict[str, Any]) -> None:
    parent_media = doc.get("parent_media")
    if parent_media not in (None, HETERO_PARENT):
        raise ValueError(f"{TAP_HETERO_MIXO}: parent_media drifted")

    doc["parent_media"] = copy.deepcopy(HETERO_PARENT)
    _put_after(doc, "variant_relationship", "SUPPLEMENTED_VARIANT", "parent_media")
    _put_after(
        doc,
        "variant_modifications",
        ["Adds 17.4 mM acetate to MediaDB TAP (auto)."],
        "variant_relationship",
    )


def repair_record(doc: dict[str, Any], spec: RecordSpec) -> dict[str, Any]:
    _ensure_target(doc, spec)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "DEFINED"
    repaired["composition_type"] = "DEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    _put_after(repaired, "temperature_value", 25.0, "ph_value")
    repaired["ingredients"] = [
        _component(name, value, unit, spec) for name, value, unit in spec.ingredient_signature
    ]
    repaired.pop("preparation_steps", None)
    _put_after(repaired, "organism_culture_type", "isolate", "curation_history")
    _put_after(repaired, "target_organisms", _target_organisms(spec), "organism_culture_type")
    _put_after(repaired, "notes", spec.notes, "media_term")
    _ensure_references(repaired, spec)
    _ensure_flags(repaired)
    _ensure_event(
        repaired,
        action=ACTION,
        source="; ".join(spec.references),
        notes=(
            f"Grounded all {len(spec.ingredient_signature)} mM components from "
            f"{spec.source_name}, added MediaDB pH 7.0 and 25 C growth "
            "conditions, and curated Chlamydomonas reinhardtii growth metrics "
            "from the linked MediaDB growth-data records."
        ),
    )
    if spec is HETERO_SPEC:
        _ensure_parent_link(repaired)
    return repaired


def repair_auto_parent(doc: dict[str, Any]) -> dict[str, Any]:
    repaired = repair_record(doc, AUTO_SPEC)

    children = repaired.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError(f"{TAP_AUTO}: variant_children is not a list")
    for child in children:
        if not isinstance(child, dict):
            raise ValueError(f"{TAP_AUTO}: variant_children contains a non-mapping row")
        if child.get("id") == EXPECTED_HETERO_ID and child != AUTO_CHILD:
            raise ValueError(f"{TAP_AUTO}: existing {EXPECTED_HETERO_ID} child pointer drifted")

    children[:] = [
        child
        for child in children
        if not (isinstance(child, dict) and child.get("id") == EXPECTED_HETERO_ID)
    ]
    children.append(copy.deepcopy(AUTO_CHILD))
    _ensure_event(
        repaired,
        action=PARENT_ACTION,
        source=f"{MEDIA_AUTO}; {MEDIA_HETERO_MIXO}",
        notes="Linked TAP (hetero/mixo) as the 17.4 mM acetate-supplemented TAP (auto) variant.",
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / TAP_AUTO: repair_auto_parent(_load(normalized / TAP_AUTO)),
        normalized
        / TAP_HETERO_MIXO: repair_record(
            _load(normalized / TAP_HETERO_MIXO),
            HETERO_SPEC,
        ),
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
