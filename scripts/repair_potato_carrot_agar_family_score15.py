#!/usr/bin/env python3
"""Repair score-15 Potato-Carrot Agar records from JCM, TOGO, and MediaDive."""

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

CURATOR = "repair_potato_carrot_agar_family_score15.py"
ACTION = "RESOLVED_POTATO_CARROT_AGAR_FAMILY"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

JCM_54 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=54"
JCM_55 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=55"
TOGO_M46 = "https://togomedium.org/medium/M46"
TOGO_M47 = "https://togomedium.org/medium/M47"
MEDIADIVE_1765 = "https://www.bacmedia.dsmz.de/medium/1765"

AGAR = ("CHEBI:2509", "agar")
WATER = ("CHEBI:15377", "water")

Component = tuple[str, str, str]
Term = tuple[str, str]


@dataclass(frozen=True)
class Ingredient:
    preferred_term: str
    value: str
    unit: str
    source: str
    notes: str
    term: Term | None = None


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    source_term: str
    imported_signature: tuple[Component, ...]
    ingredients: tuple[Ingredient, ...]
    reference_urls: tuple[str, ...]
    notes: str


def _jcm_ingredient(
    preferred_term: str,
    value: str,
    *,
    source: str,
    term: Term | None = None,
) -> Ingredient:
    return Ingredient(
        preferred_term=preferred_term,
        value=value,
        unit="G_PER_L",
        source=source,
        notes=(
            f"{source} lists {preferred_term} in the potato-carrot decoction before "
            "boiling and cheesecloth filtration."
        ),
        term=term,
    )


def _dsmz_ingredient(
    preferred_term: str,
    value: str,
    *,
    term: Term | None = None,
) -> Ingredient:
    return Ingredient(
        preferred_term=preferred_term,
        value=value,
        unit="G_PER_L",
        source="MediaDive Medium 1765",
        notes=(
            "MediaDive Medium 1765 lists this ingredient in the potato-carrot "
            "decoction before the boil, cheesecloth filtration, volume adjustment, "
            "and agar addition."
        ),
        term=term,
    )


def _water(source: str) -> Ingredient:
    return Ingredient(
        preferred_term="Distilled water",
        value="1000",
        unit="ML_PER_L",
        source=source,
        notes=f"{source} lists 1.0 L distilled water to bring the recipe to volume.",
        term=WATER,
    )


def _jcm_recipe(source: str, potato: str, carrot: str) -> tuple[Ingredient, ...]:
    return (
        _jcm_ingredient("Potato, peeled and cut", potato, source=source),
        _jcm_ingredient("Carrot, peeled and cut", carrot, source=source),
        Ingredient(
            preferred_term="Agar",
            value="15",
            unit="G_PER_L",
            source=source,
            notes=f"{source} lists agar as the solidifying component.",
            term=AGAR,
        ),
        _water(source),
    )


JCM_54_RECIPE = _jcm_recipe("JCM Medium 54", "300", "25")
JCM_55_RECIPE = _jcm_recipe("JCM Medium 55", "30", "2.5")
DSMZ_1765_RECIPE = (
    _dsmz_ingredient("Potato", "150"),
    _dsmz_ingredient("Carrot", "30"),
    Ingredient(
        preferred_term="Agar",
        value="20",
        unit="G_PER_L",
        source="MediaDive Medium 1765",
        notes="MediaDive Medium 1765 lists agar as the solidifying component.",
        term=AGAR,
    ),
    _water("MediaDive Medium 1765"),
)

TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/JCM_J54_POTATO-CARROT_AGAR.yaml",
        record_id="CultureMech:002897",
        source_term="mediadive.medium:J54",
        imported_signature=(
            ("Potato", "300", "G_PER_L"),
            ("Carrot", "25", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        ingredients=JCM_54_RECIPE,
        reference_urls=(JCM_54,),
        notes=(
            "JCM Medium 54 lists 300 g potato, 25 g carrot, 15 g agar, and "
            "1.0 L distilled water, with pH unadjusted."
        ),
    ),
    Target(
        path="bacterial/1_10_potato_carrot_agar.yaml",
        record_id="CultureMech:002908",
        source_term="mediadive.medium:J55",
        imported_signature=(
            ("Potato", "30", "G_PER_L"),
            ("Carrot", "2.5", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        ingredients=JCM_55_RECIPE,
        reference_urls=(JCM_55, JCM_54),
        notes=(
            "JCM Medium 55 lists 30 g potato, 2.5 g carrot, 15 g agar, and "
            "1.0 L distilled water, and delegates the preparation footnote to "
            "JCM Medium 54."
        ),
    ),
    Target(
        path="bacterial/potato_carrot_agar.yaml",
        record_id="CultureMech:001233",
        source_term="mediadive.medium:1765",
        imported_signature=(
            ("Potato", "150", "G_PER_L"),
            ("Carrot", "30", "G_PER_L"),
            ("Agar", "20", "G_PER_L"),
        ),
        ingredients=DSMZ_1765_RECIPE,
        reference_urls=(MEDIADIVE_1765,),
        notes=(
            "MediaDive Medium 1765 lists 150 g potato, 30 g carrot, 20 g agar, "
            "1000 mL distilled water, and final pH 7.0."
        ),
    ),
    Target(
        path="bacterial/TOGO_M46_Potato-Carrot_Agar.yaml",
        record_id="CultureMech:009858",
        source_term="TOGO:M46",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Carrot, peeled and cut", "25", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
            ("Potato, peeled and cut", "300", "G_PER_L"),
        ),
        ingredients=JCM_54_RECIPE,
        reference_urls=(TOGO_M46, JCM_54),
        notes=(
            "TOGO M46 mirrors JCM Medium 54: 300 g potato, 25 g carrot, "
            "15 g agar, and 1.0 L distilled water, with pH unadjusted."
        ),
    ),
    Target(
        path="bacterial/TOGO_M47_1_10_Potato-Carrot_Agar.yaml",
        record_id="CultureMech:009866",
        source_term="TOGO:M47",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Carrot, peeled and cut", "2.5", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
            ("Potato, peeled and cut", "30", "G_PER_L"),
        ),
        ingredients=JCM_55_RECIPE,
        reference_urls=(TOGO_M47, JCM_55, JCM_54),
        notes=(
            "TOGO M47 mirrors JCM Medium 55: 30 g potato, 2.5 g carrot, "
            "15 g agar, and 1.0 L distilled water, with the preparation footnote "
            "delegated to JCM Medium 54."
        ),
    ),
)
TARGET_BY_PATH: dict[str, Target] = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _component_signature(rows: Any) -> tuple[Component, ...]:
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


def _recipe_signature(ingredients: tuple[Ingredient, ...]) -> tuple[Component, ...]:
    return tuple((row.preferred_term, row.value, row.unit) for row in ingredients)


def _check_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != target.source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.source_term}, " f"found {source_term!r}"
        )

    signature = _component_signature(doc.get("ingredients"))
    valid_signatures = {target.imported_signature, _recipe_signature(target.ingredients)}
    if signature not in valid_signatures:
        raise ValueError(
            f"{target.path}: ingredient signature drifted from "
            f"{target.imported_signature!r} to {signature!r}"
        )

    if doc.get("solutions"):
        raise ValueError(f"{target.path}: unexpected solutions")


def _ingredient(spec: Ingredient) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": spec.preferred_term,
        "concentration": {"value": spec.value, "unit": spec.unit},
        "source": spec.source,
        "notes": spec.notes,
    }
    if spec.term is not None:
        row["term"] = _term(*spec.term)
        if spec.term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*spec.term)
    return row


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in target.reference_urls:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.reference_urls),
        "notes": target.notes,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _check_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = [_ingredient(row) for row in target.ingredients]
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_curation_event(repaired, target)
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
