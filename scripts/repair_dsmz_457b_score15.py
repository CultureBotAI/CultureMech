#!/usr/bin/env python3
"""Repair DSMZ/KOMODO 457b fluoranthene and phenanthrene variants."""

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

DSMZ_457B = "bacterial/medium_with_fluoranthene.yaml"
KOMODO_457B = "bacterial/medium_with_fluoranthene_or_phenanthrene.yaml"
KOMODO_457B_1 = "bacterial/for_dsm_7526.yaml"
KOMODO_457B_2 = "bacterial/for_dsm_13022.yaml"

EXPECTED_IDS = {
    DSMZ_457B: "CultureMech:001569",
    KOMODO_457B: "CultureMech:005459",
    KOMODO_457B_1: "CultureMech:005457",
    KOMODO_457B_2: "CultureMech:005458",
}

EXPECTED_SOURCE_TERMS = {
    DSMZ_457B: "mediadive.medium:457b",
    KOMODO_457B: "komodo.medium:457b",
    KOMODO_457B_1: "komodo.medium:457b.1",
    KOMODO_457B_2: "komodo.medium:457b.2",
}

DSMZ_457B_REST = "https://mediadive.dsmz.de/rest/medium/457b"
DSMZ_457B_PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium457b.pdf"
KOMODO_BASE = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
)

CURATOR = "repair_dsmz_457b_score15.py"
ACTION = "RESOLVED_DSMZ_KOMODO_457B_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"
PH_VALUE = 6.9
DATA_QUALITY_FLAGS = ["ingredients_curated", "has_ontology_mappings"]


@dataclass(frozen=True)
class Target:
    path: str
    source_label: str
    source_url: str
    record_notes: str
    curation_notes: str
    composition_type: str = "DEFINED"
    ingredient_additions: tuple[dict[str, Any], ...] = ()
    parent_media: dict[str, str] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, str], ...] = ()


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _compound(preferred_term: str, value: str, identifier: str, label: str) -> dict[str, Any]:
    term = _term(identifier, label)
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "term": copy.deepcopy(term),
        "concentration": {"value": value, "unit": "G_PER_L"},
    }
    if identifier.startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)
    return row


def _komodo_compound(
    preferred_term: str,
    value: str,
    identifier: str,
    label: str,
    source: str,
    notes: str,
) -> dict[str, Any]:
    row = _compound(preferred_term, value, identifier, label)
    row["source"] = source
    row["notes"] = notes
    return row


def _recipe_ref(path: str, relationship: str, notes: str) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": EXPECTED_IDS[path],
        "name": Path(path).stem,
        "notes": notes,
    }


BASE_INGREDIENTS: tuple[dict[str, Any], ...] = (
    _compound("Tween 80", "0.2", "CHEBI:53426", "polysorbate 80"),
    _compound("Na2HPO4", "2.44", "CHEBI:34683", "disodium hydrogenphosphate"),
    _compound("KH2PO4", "1.52", "CHEBI:63036", "potassium dihydrogen phosphate"),
    _compound("(NH4)2SO4", "0.5", "CHEBI:62946", "ammonium sulfate"),
    _compound("MgSO4 x 7 H2O", "0.2", "CHEBI:31795", "magnesium sulfate heptahydrate"),
    _compound("CaCl2 x 2 H2O", "0.05", "CHEBI:86158", "calcium chloride dihydrate"),
    _compound("EDTA", "0.5", "CHEBI:4735", "ethylenediaminetetraacetic acid"),
    _compound("FeSO4 x 7 H2O", "0.2", "CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    _compound("ZnSO4 x 7 H2O", "0.1", "CHEBI:32312", "zinc sulfate heptahydrate"),
    _compound("MnCl2 x 4 H2O", "0.03", "CHEBI:86368", "manganese(II) chloride tetrahydrate"),
    _compound("H3BO3", "0.3", "CHEBI:33118", "boric acid"),
    _compound("CoCl2 x 6 H2O", "0.2", "CHEBI:53503", "cobalt chloride hexahydrate"),
    _compound("CuCl2 x 2 H2O", "0.01", "CHEBI:86318", "copper(II) chloride dihydrate"),
    _compound("NiCl2 x 6 H2O", "0.02", "CHEBI:34887", "nickel dichloride"),
    _compound("Na2MoO4 x 2 H2O", "0.03", "CHEBI:75213", "sodium molybdate dihydrate"),
)


DSMZ_457B_PARENT = _recipe_ref(
    DSMZ_457B,
    "STRAIN_SPECIFIC_VARIANT",
    "DSMZ Medium 457b is the official mineral medium with Tween 80 parent.",
)

KOMODO_CHILDREN = (
    _recipe_ref(
        KOMODO_457B,
        "SOURCE_DUPLICATE",
        "KOMODO Medium 457b is a source-catalogue duplicate of DSMZ Medium 457b.",
    ),
    _recipe_ref(
        KOMODO_457B_1,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 457b.1 applies DSMZ Medium 457b to DSM 7526.",
    ),
    _recipe_ref(
        KOMODO_457B_2,
        "STRAIN_SPECIFIC_VARIANT",
        "KOMODO Medium 457b.2 applies DSMZ Medium 457b to DSM 13022.",
    ),
)


PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "FILTER_STERILIZE",
        "description": (
            "DSMZ Medium 457b prepares a 2 g/L fluoranthene stock in acetone "
            "and filter-sterilizes it with a cellulose filter membrane."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "DSMZ Medium 457b adds 1 mL of the fluoranthene stock to a sterile "
            "culture flask, lets the acetone evaporate, and adds 20 mL of medium; "
            "direct addition of about 1-2 mg fluoranthene is also possible."
        ),
    },
    {
        "step_number": 3,
        "action": "ADJUST_PH",
        "description": "DSMZ Medium 457 adjusts the mineral base to pH 6.9.",
    },
    {
        "step_number": 4,
        "action": "AUTOCLAVE",
        "description": (
            "DSMZ Medium 457 autoclaves the phosphate solution separately and "
            "combines it with the rest of the medium after cooling."
        ),
    },
    {
        "step_number": 5,
        "action": "MIX",
        "description": (
            "DSMZ Medium 457b reactivates lyophilized cells in a complex medium "
            "before transferring them to mineral medium 457 with the appropriate "
            "carbon source."
        ),
    },
)


TARGETS: tuple[Target, ...] = (
    Target(
        path=DSMZ_457B,
        source_label="DSMZ Medium 457b",
        source_url=DSMZ_457B_REST,
        record_notes=f"Source: DSMZ | Link: {DSMZ_457B_PDF}",
        curation_notes=(
            "MediaDive and DSMZ Medium 457b define MEDIUM WITH FLUORANTHENE "
            "as DSMZ Medium 457 with 200 mg/L Tween 80."
        ),
        variant_children=KOMODO_CHILDREN,
    ),
    Target(
        path=KOMODO_457B,
        source_label="KOMODO Medium 457b",
        source_url=f"{KOMODO_BASE}457b",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 457b | "
            "DSMZ Medium: 457b (mediadive.medium:457b) | Aerobic: No"
        ),
        curation_notes=(
            "KOMODO Medium 457b cites DSMZ Medium 457b but had stale "
            "dibenzofuran, DMSO, agar, and tryptic soy rows from unrelated media."
        ),
        parent_media=_recipe_ref(
            DSMZ_457B,
            "SOURCE_DUPLICATE",
            "DSMZ Medium 457b is the official MEDIUM WITH FLUORANTHENE formulation.",
        ),
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=("KOMODO source-catalogue duplicate of DSMZ Medium 457b.",),
    ),
    Target(
        path=KOMODO_457B_1,
        source_label="KOMODO Medium 457b.1",
        source_url=f"{KOMODO_BASE}457b.1",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 457b.1 | "
            "DSMZ Medium: 457b (mediadive.medium:457b) | Aerobic: No"
        ),
        curation_notes=(
            "KOMODO Medium 457b.1 records the DSM 7526 formulation with "
            "fluoranthene substrate and Tween 80."
        ),
        ingredient_additions=(
            _komodo_compound(
                "Fluoranthene",
                "0.10",
                "CHEBI:33083",
                "fluoranthene",
                "KOMODO Medium 457b.1",
                "KOMODO Medium 457b.1 lists 0.10 g/L fluoranthene for DSM 7526.",
            ),
        ),
        parent_media=DSMZ_457B_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=("Adds fluoranthene as the aromatic carbon source for DSM 7526.",),
    ),
    Target(
        path=KOMODO_457B_2,
        source_label="KOMODO Medium 457b.2",
        source_url=f"{KOMODO_BASE}457b.2",
        record_notes=(
            "Source: KOMODO ModelSEED | ID: 457b.2 | "
            "DSMZ Medium: 457b (mediadive.medium:457b) | Aerobic: No"
        ),
        curation_notes=(
            "KOMODO Medium 457b.2 records the DSM 13022 formulation with "
            "phenanthrene substrate and Casamino acids."
        ),
        composition_type="SEMI_DEFINED",
        ingredient_additions=(
            _komodo_compound(
                "Phenanthrene",
                "0.02",
                "CHEBI:28851",
                "phenanthrene",
                "KOMODO Medium 457b.2",
                "KOMODO Medium 457b.2 lists 0.02 g/L phenanthrene for DSM 13022.",
            ),
            _komodo_compound(
                "Casamino acids (DIFCO)",
                "0.30",
                "FOODON:03315719",
                "mammalian milk protein (hydrolyzed)",
                "KOMODO Medium 457b.2",
                "KOMODO Medium 457b.2 lists 0.30 g/L Casamino acids for DSM 13022.",
            ),
        ),
        parent_media=DSMZ_457B_PARENT,
        variant_relationship="STRAIN_SPECIFIC_VARIANT",
        variant_modifications=(
            "Uses phenanthrene and Casamino acids as the DSM 13022 supplements.",
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


def _require_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != EXPECTED_IDS[target.path]:
        raise ValueError(
            f"{target.path}: found id {doc.get('id')!r}, expected {EXPECTED_IDS[target.path]!r}"
        )
    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERMS[target.path]:
        raise ValueError(
            f"{target.path}: found source term {source_term!r}, expected "
            f"{EXPECTED_SOURCE_TERMS[target.path]!r}"
        )


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{target.path}: references is not a list")

    seen = {row.get("reference") for row in references if isinstance(row, dict)}
    urls = [target.source_url, DSMZ_457B_PDF]
    if target.path != DSMZ_457B:
        urls.append(DSMZ_457B_REST)

    for url in urls:
        if url not in seen:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Resolved DSMZ/KOMODO Medium 457b variant metadata and stale ingredients",
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _require_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = target.composition_type
    repaired["physical_state"] = "LIQUID"
    repaired["notes"] = target.record_notes
    repaired["ingredients"] = [
        *(copy.deepcopy(row) for row in BASE_INGREDIENTS),
        *(copy.deepcopy(row) for row in target.ingredient_additions),
    ]
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


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / target.path: repair_record(_load(normalized / target.path), target)
        for target in TARGETS
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
