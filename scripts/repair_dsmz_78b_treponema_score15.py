#!/usr/bin/env python3
"""Repair DSMZ/KOMODO 78b Treponema variants."""

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

DSMZ_78B = "bacterial/chopped_meat_medium_n2_co2.yaml"
KOMODO_78 = "bacterial/KOMODO_78_CHOPPED_MEAT_medium.yaml"
KOMODO_78B = "bacterial/KOMODO_78b_medium_FOR_TREPONEMA_PARVUM.yaml"
KOMODO_78B_1 = "bacterial/for_dsm_16260.yaml"
KOMODO_78B_2 = "bacterial/for_dsm_16369.yaml"

EXPECTED_IDS = {
    DSMZ_78B: "CultureMech:001928",
    KOMODO_78: "CultureMech:006491",
    KOMODO_78B: "CultureMech:006496",
    KOMODO_78B_1: "CultureMech:006494",
    KOMODO_78B_2: "CultureMech:006495",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_78B: "mediadive.medium:78b",
    KOMODO_78: "komodo.medium:78",
    KOMODO_78B: "komodo.medium:78b",
    KOMODO_78B_1: "komodo.medium:78b.1",
    KOMODO_78B_2: "komodo.medium:78b.2",
}

DSMZ_78B_REST = "https://mediadive.dsmz.de/rest/medium/78b"
DSMZ_78B_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium78b.pdf"
KOMODO_BASE = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
)

SOURCE_DSMZ_78B = "DSMZ Medium 78b"
SOURCE_KOMODO_78B = "KOMODO Medium 78b"
SOURCE_KOMODO_78B_1 = "KOMODO Medium 78b.1"
SOURCE_KOMODO_78B_2 = "KOMODO Medium 78b.2"

CURATOR = "repair_dsmz_78b_treponema_score15.py"
ACTION = "RESOLVED_DSMZ_KOMODO_78B_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"
DATA_QUALITY_FLAGS = [
    "has_ontology_mappings",
    "has_unmapped_ingredients",
    "ingredients_curated",
]
PH_VALUE = 7.0


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    source: str
    term: tuple[str, str] | None


@dataclass(frozen=True)
class Target:
    path: str
    source_label: str
    source_url: str
    record_notes: str
    curation_notes: str
    components: tuple[Component, ...]
    parent_media: dict[str, str] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, str], ...] = ()


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    source: str,
    identifier: str | None = None,
    label: str | None = None,
) -> Component:
    if (identifier is None) != (label is None):
        raise ValueError("identifier and label must be provided together")
    return Component(
        preferred_term=preferred_term,
        value=value,
        source=source,
        term=(identifier, label) if identifier is not None and label is not None else None,
    )


def _ingredient(component: Component) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": (
            f"{component.source} lists {component.value} g/L "
            f"{component.preferred_term} in the final-component table."
        ),
        "concentration": {"value": component.value, "unit": "G_PER_L"},
    }
    if component.term is not None:
        term = _term(*component.term)
        row["term"] = term
        if component.term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)
    return row


def _recipe_ref(path: str, relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": EXPECTED_IDS[path],
        "name": Path(path).stem,
        "notes": notes,
    }


def _casamino(value: str, source: str) -> Component:
    return _component(
        "Casamino acid",
        value,
        source,
        "FOODON:03315719",
        "mammalian milk protein (hydrolyzed)",
    )


def _tryptone(value: str, source: str) -> Component:
    return _component(
        "Tryptone Peptone (Difco 0123-17)",
        value,
        source,
        "FOODON:03315719",
        "mammalian milk protein (hydrolyzed)",
    )


def _komodo_components(
    source: str,
    values: dict[str, str],
    extras: tuple[Component, ...] = (),
    omit: frozenset[str] = frozenset(),
) -> tuple[Component, ...]:
    base = (
        _casamino(values["Casamino acid"], source),
        _component("KCl", values["KCl"], source, "CHEBI:32588", "potassium chloride"),
        _component("L-Glutamine", values["L-Glutamine"], source, "CHEBI:18050", "L-glutamine"),
        _component("Na-pyruvate", values["Na-pyruvate"], source, "CHEBI:50144", "sodium pyruvate"),
        _component("Casitone", values["Casitone"], source),
        _component(
            "K2HPO4", values["K2HPO4"], source, "CHEBI:131527", "dipotassium hydrogen phosphate"
        ),
        _component(
            "Yeast extract", values["Yeast extract"], source, "FOODON:03315426", "yeast extract"
        ),
        _component(
            "N-acetylglucosamine",
            values["N-acetylglucosamine"],
            source,
            "CHEBI:59640",
            "N-acetylglucosamine",
        ),
        _component("glutathione", values["glutathione"], source, "CHEBI:16856", "glutathione"),
        _tryptone(values["Tryptone Peptone (Difco 0123-17)"], source),
        _component("Fetal or newborn calf serum", values["Fetal or newborn calf serum"], source),
        _component(
            "Ascorbic acid", values["Ascorbic acid"], source, "CHEBI:22652", "ascorbic acid"
        ),
        _component("hemin", values["hemin"], source, "CHEBI:50385", "hemin"),
        _component("Cysteine", values["Cysteine"], source, "CHEBI:17561", "L-cysteine"),
        _component("Resazurin", values["Resazurin"], source, "CHEBI:8806", "Resazurin"),
        _component("L-Serine", values["L-Serine"], source, "CHEBI:17115", "L-serine"),
        _component("L-Histidine", values["L-Histidine"], source, "CHEBI:15971", "L-histidine"),
        _component("Ground beef (fat free)", values["Ground beef (fat free)"], source),
    )
    return (*extras, *(row for row in base if row.preferred_term not in omit))


DSMZ_78B_COMPONENTS = (
    _component("Ground beef", "487.805", SOURCE_DSMZ_78B),
    _component("Casitone", "29.2683", SOURCE_DSMZ_78B),
    _component("Yeast extract", "4.87805", SOURCE_DSMZ_78B, "FOODON:03315426", "yeast extract"),
    _component(
        "K2HPO4", "4.87805", SOURCE_DSMZ_78B, "CHEBI:131527", "dipotassium hydrogen phosphate"
    ),
    _component("Sodium resazurin", "0.000487805", SOURCE_DSMZ_78B, "CHEBI:8806", "Resazurin"),
    _component(
        "L-Cysteine HCl x H2O",
        "0.487805",
        SOURCE_DSMZ_78B,
        "CHEBI:91248",
        "L-cysteine hydrochloride hydrate",
    ),
)

KOMODO_78B_COMPONENTS = _komodo_components(
    SOURCE_KOMODO_78B,
    {
        "Casamino acid": "0.16",
        "KCl": "0.49",
        "L-Glutamine": "0.68",
        "Na-pyruvate": "0.49",
        "Casitone": "28.55",
        "K2HPO4": "4.76",
        "Yeast extract": "4.92",
        "N-acetylglucosamine": "0.49",
        "glutathione": "1.37",
        "Tryptone Peptone (Difco 0123-17)": "0.16",
        "Fetal or newborn calf serum": "9.76",
        "Ascorbic acid": "0.10",
        "hemin": "4.88E-4",
        "Cysteine": "0.48",
        "Resazurin": "9.52E-4",
        "L-Serine": "0.49",
        "L-Histidine": "0.59",
        "Ground beef (fat free)": "475.91",
    },
)

KOMODO_78B_1_COMPONENTS = _komodo_components(
    SOURCE_KOMODO_78B_1,
    {
        "Casamino acid": "0.15",
        "KCl": "0.48",
        "L-Glutamine": "0.67",
        "Na-pyruvate": "0.48",
        "Casitone": "28.01",
        "K2HPO4": "4.67",
        "Yeast extract": "4.82",
        "N-acetylglucosamine": "0.48",
        "glutathione": "1.34",
        "Tryptone Peptone (Difco 0123-17)": "0.15",
        "Fetal or newborn calf serum": "9.57",
        "Ascorbic acid": "0.10",
        "hemin": "4.78E-4",
        "Cysteine": "0.47",
        "Resazurin": "9.34E-4",
        "L-Serine": "0.48",
        "L-Histidine": "0.57",
        "Ground beef (fat free)": "466.80",
    },
    extras=(
        _component("Ribose", "1.91", SOURCE_KOMODO_78B_1, "CHEBI:16988", "D-ribose"),
        _component(
            "Glucuronic acid", "1.91", SOURCE_KOMODO_78B_1, "CHEBI:4178", "D-glucuronic acid"
        ),
    ),
)

KOMODO_78B_2_COMPONENTS = _komodo_components(
    SOURCE_KOMODO_78B_2,
    {
        "Casamino acid": "0.15",
        "KCl": "0",
        "L-Glutamine": "0.68",
        "Na-pyruvate": "0",
        "Casitone": "28.28",
        "K2HPO4": "4.71",
        "Yeast extract": "4.87",
        "N-acetylglucosamine": "0",
        "glutathione": "0",
        "Tryptone Peptone (Difco 0123-17)": "0.15",
        "Fetal or newborn calf serum": "9.66",
        "Ascorbic acid": "0.10",
        "hemin": "4.83E-4",
        "Cysteine": "0.47",
        "Resazurin": "9.43E-4",
        "L-Serine": "0.48",
        "L-Histidine": "0.58",
        "Ground beef (fat free)": "471.31",
    },
    extras=(_component("maltose", "1.93", SOURCE_KOMODO_78B_2, "CHEBI:17306", "maltose"),),
    omit=frozenset({"KCl", "Na-pyruvate", "N-acetylglucosamine", "glutathione"}),
)

DSMZ_78B_PARENT = _recipe_ref(
    DSMZ_78B,
    "STRAIN_SPECIFIC_VARIANT",
    "DSMZ Medium 78b is the official CHOPPED MEAT MEDIUM (N2/CO2) recipe.",
)

KOMODO_78B_PARENT = _recipe_ref(
    KOMODO_78B,
    "STRAIN_SPECIFIC_VARIANT",
    "KOMODO Medium 78b is the Treponema parvum formulation of DSMZ Medium 78b.",
)

PREPARATION_STEPS = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": (
            "DSMZ Medium 78b boils lean chopped beef or horse meat with water and "
            "NaOH for 15 min, filters while retaining meat particles and filtrate, "
            "adds Casitone, yeast extract, K2HPO4, resazurin, and water to 700 ml, "
            "sparges with 80% N2/20% CO2 for 30-45 min, adds L-cysteine HCl x H2O, "
            "adjusts pH to 7.0, dispenses under the same gas into Hungate tubes "
            "with meat particles, and autoclaves at 121 C for 20 min."
        ),
    },
    {
        "step_number": 2,
        "action": "FILTER_STERILIZE",
        "description": (
            "When the DSMZ catalogue specifies Haemin, Vitamin K1, or Vitamin K3, "
            "prepare those stocks separately, filter-sterilize them, and add them "
            "to the autoclaved chopped-meat medium."
        ),
    },
)


KOMODO_CHILDREN = (
    _recipe_ref(
        KOMODO_78B_1,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 78b.1 adapts KOMODO Medium 78b for DSM 16260.",
    ),
    _recipe_ref(
        KOMODO_78B_2,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 78b.2 adapts KOMODO Medium 78b for DSM 16369.",
    ),
)

TARGETS = (
    Target(
        path=DSMZ_78B,
        source_label=SOURCE_DSMZ_78B,
        source_url=DSMZ_78B_REST,
        record_notes=f"Source: DSMZ | Link: {DSMZ_78B_PDF}",
        curation_notes=(
            "MediaDive defines DSMZ Medium 78b as liquid CHOPPED MEAT MEDIUM "
            "(N2/CO2); optional Haemin/Vitamin K stock-solution internals were "
            "removed from the final-ingredient list."
        ),
        components=DSMZ_78B_COMPONENTS,
        variant_children=(
            _recipe_ref(
                KOMODO_78B,
                "STRAIN_SPECIFIC_VARIANT",
                "KOMODO Medium 78b is the Treponema parvum formulation of DSMZ Medium 78b.",
            ),
        ),
    ),
    Target(
        path=KOMODO_78B,
        source_label=SOURCE_KOMODO_78B,
        source_url=f"{KOMODO_BASE}78b",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 78b | "
            "DSMZ Medium: 78b (mediadive.medium:78b) | Aerobic: Yes"
        ),
        curation_notes=(
            "KOMODO Medium 78b records the Treponema parvum formulation of DSMZ "
            "Medium 78b; stale DSMZ Medium 78 agar and vitamin-stock rows were removed."
        ),
        components=KOMODO_78B_COMPONENTS,
        parent_media=DSMZ_78B_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Records the KOMODO/DSMZ 78b final-component table for Treponema parvum.",
        ),
        variant_children=KOMODO_CHILDREN,
    ),
    Target(
        path=KOMODO_78B_1,
        source_label=SOURCE_KOMODO_78B_1,
        source_url=f"{KOMODO_BASE}78b.1",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 78b.1 | "
            "DSMZ Medium: 78b (mediadive.medium:78b) | Aerobic: Yes"
        ),
        curation_notes=(
            "KOMODO Medium 78b.1 records the DSM 16260 strain variant of the "
            "Treponema parvum formulation."
        ),
        components=KOMODO_78B_1_COMPONENTS,
        parent_media=KOMODO_78B_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Adds ribose and D-glucuronic acid to the Treponema parvum formulation for DSM 16260.",
        ),
    ),
    Target(
        path=KOMODO_78B_2,
        source_label=SOURCE_KOMODO_78B_2,
        source_url=f"{KOMODO_BASE}78b.2",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 78b.2 | "
            "DSMZ Medium: 78b (mediadive.medium:78b) | Aerobic: Yes"
        ),
        curation_notes=(
            "KOMODO Medium 78b.2 records the DSM 16369 strain variant of the "
            "Treponema parvum formulation."
        ),
        components=KOMODO_78B_2_COMPONENTS,
        parent_media=KOMODO_78B_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Adds maltose and omits KCl, Na-pyruvate, N-acetylglucosamine, and glutathione.",
        ),
    ),
)

TARGET_BY_PATH = {target.path: target for target in TARGETS}


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
    media_term = doc.get("media_term") or {}
    term = media_term.get("term") if isinstance(media_term, dict) else {}
    return str(term.get("id") or "") if isinstance(term, dict) else ""


def _require_path(doc: dict[str, Any], path: str) -> None:
    if doc.get("id") != EXPECTED_IDS[path]:
        raise ValueError(f"{path}: found id {doc.get('id')!r}, expected {EXPECTED_IDS[path]!r}")
    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[path]:
        raise ValueError(
            f"{path}: found source term {source_term!r}, expected "
            f"{EXPECTED_SOURCE_TERMS[path]!r}"
        )


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    urls = [target.source_url, DSMZ_78B_PDF, DSMZ_78B_REST]
    seen = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in urls:
        if url not in seen:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ/KOMODO Medium 78b Treponema variant metadata and stale ingredients",
        "source": target.source_url,
        "notes": target.curation_notes,
    }
    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.path}: curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_target(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_path(doc, target.path)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["notes"] = target.record_notes
    repaired["ingredients"] = [_ingredient(component) for component in target.components]
    repaired.pop("ph_range", None)

    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "ingredients")
    _put_after(repaired, "data_quality_flags", list(DATA_QUALITY_FLAGS), "preparation_steps")

    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
    _put_after(repaired, "references", repaired["references"], "data_quality_flags")

    for field in (
        "parent_media",
        "variant_relationship",
        "variant_modifications",
        "variant_children",
    ):
        repaired.pop(field, None)

    after = "references"
    if target.parent_media is not None:
        _put_after(repaired, "parent_media", copy.deepcopy(target.parent_media), after)
        after = "parent_media"
    if target.variant_relationship is not None:
        _put_after(repaired, "variant_relationship", target.variant_relationship, after)
        after = "variant_relationship"
    if target.variant_modifications:
        _put_after(repaired, "variant_modifications", list(target.variant_modifications), after)
        after = "variant_modifications"
    if target.variant_children:
        _put_after(
            repaired,
            "variant_children",
            [copy.deepcopy(row) for row in target.variant_children],
            after,
        )

    return repaired


def repair_komodo_78_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _require_path(doc, KOMODO_78)
    repaired = copy.deepcopy(doc)
    removed = {KOMODO_78B, KOMODO_78B_1, KOMODO_78B_2}
    removed_paths = {f"data/normalized_yaml/{path}" for path in removed}
    children = [
        child
        for child in repaired.get("variant_children", [])
        if not isinstance(child, dict) or child.get("path") not in removed_paths
    ]
    repaired["variant_children"] = children
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans = {
        normalized / target.path: repair_target(_load(normalized / target.path), target)
        for target in TARGETS
    }
    plans[normalized / KOMODO_78] = repair_komodo_78_parent(_load(normalized / KOMODO_78))
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
