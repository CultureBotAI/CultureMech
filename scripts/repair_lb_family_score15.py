#!/usr/bin/env python3
"""Repair score-15 LB and 1/3 LB records."""

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

CURATOR = "repair_lb_family_score15.py"
ACTION = "RESOLVED_LB_FAMILY_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M878 = "https://togomedium.org/medium/M878"
TOGO_M1492 = "https://togomedium.org/medium/M1492"
TOGO_M2042 = "https://togomedium.org/medium/M2042"

JCM_842 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=842"
NBRC_275 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=275"
NBRC_1340 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1340"

AGAR = ("CHEBI:2509", "agar")
NACL = ("CHEBI:26710", "sodium chloride")
PEPTONE = ("MICRO:0000178", "peptone")
WATER = ("CHEBI:15377", "water")
YEAST_EXTRACT = ("FOODON:03315426", "yeast extract")

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
    ph_value: float | None = None


def _ingredient(
    preferred_term: str,
    value: str,
    *,
    source: str,
    notes: str,
    term: Term | None = None,
) -> Ingredient:
    return Ingredient(
        preferred_term=preferred_term,
        value=value,
        unit="G_PER_L",
        source=source,
        notes=notes,
        term=term,
    )


def _water(source: str) -> Ingredient:
    return Ingredient(
        preferred_term="Distilled water",
        value="1000",
        unit="ML_PER_L",
        source=source,
        notes=f"{source} lists 1.0 L distilled water.",
        term=WATER,
    )


def _generic_lb_recipe(
    source: str,
    *,
    peptone: str,
    yeast_extract: str,
    agar_before_water: bool,
) -> tuple[Ingredient, ...]:
    agar = _ingredient(
        "Agar (if needed)",
        "15",
        source=source,
        notes=f"{source} lists 15 g agar as the optional solidifying component.",
        term=AGAR,
    )
    water = _water(source)
    tail = (agar, water) if agar_before_water else (water, agar)
    return (
        _ingredient(
            "Peptone",
            peptone,
            source=source,
            notes=f"{source} lists this generic peptone digest as a nutrient source.",
            term=PEPTONE,
        ),
        _ingredient(
            "Yeast extract",
            yeast_extract,
            source=source,
            notes=f"{source} lists this generic yeast extract as a nutrient source.",
            term=YEAST_EXTRACT,
        ),
        _ingredient(
            "NaCl",
            "5",
            source=source,
            notes=f"{source} lists 5 g sodium chloride.",
            term=NACL,
        ),
        *tail,
    )


def _difco_lb_recipe(source: str) -> tuple[Ingredient, ...]:
    return (
        _ingredient(
            "Tryptone (BD-Difco)",
            "3.3",
            source=source,
            notes=(
                f"{source} lists this as the BD-Difco tryptone product; the product "
                "is source-disclosed but not reducible to one ChEBI molecule."
            ),
        ),
        _ingredient(
            "Yeast extract (BD-Difco)",
            "1.7",
            source=source,
            notes=(
                f"{source} lists this as the BD-Difco yeast extract product; the "
                "product is source-disclosed but not reducible to one ChEBI molecule."
            ),
        ),
        _ingredient(
            "NaCl",
            "5",
            source=source,
            notes=f"{source} lists 5 g sodium chloride.",
            term=NACL,
        ),
        _ingredient(
            "Agar",
            "15",
            source=source,
            notes=f"{source} lists 15 g agar as the solidifying component.",
            term=AGAR,
        ),
        _water(source),
    )


LB_RECIPE = _generic_lb_recipe(
    "NBRC Medium 275",
    peptone="10",
    yeast_extract="5",
    agar_before_water=False,
)
NBRC_1340_RECIPE = _generic_lb_recipe(
    "NBRC Medium 1340",
    peptone="3.33",
    yeast_extract="1.67",
    agar_before_water=True,
)
JCM_842_RECIPE = _difco_lb_recipe("JCM Medium 842")

TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/lb_medium.yaml",
        record_id="CultureMech:008037",
        source_term="TOGO:M1492",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Yeast extract", "5", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Peptone", "10", "G_PER_L"),
        ),
        ingredients=LB_RECIPE,
        ph_value=7.0,
        reference_urls=(TOGO_M1492, NBRC_275),
        notes=(
            "TOGO M1492 mirrors NBRC Medium 275: 10 g peptone, 5 g yeast "
            "extract, 5 g NaCl, 1 L distilled water, 15 g optional agar, and pH 7.0."
        ),
    ),
    Target(
        path="bacterial/1_3_lb.yaml",
        record_id="CultureMech:008632",
        source_term="TOGO:M2042",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Yeast extract", "1.67", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Peptone", "3.33", "G_PER_L"),
        ),
        ingredients=NBRC_1340_RECIPE,
        reference_urls=(TOGO_M2042, NBRC_1340),
        notes=(
            "NBRC Medium 1340 lists 3.33 g peptone, 1.67 g yeast extract, "
            "5 g NaCl, 15 g optional agar, and 1 L distilled water, with pH "
            "unadjusted."
        ),
    ),
    Target(
        path="bacterial/1_3_lb_agar.yaml",
        record_id="CultureMech:003187",
        source_term="mediadive.medium:J842",
        imported_signature=(
            ("Tryptone", "3.3", "G_PER_L"),
            ("Yeast extract", "1.7", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        ingredients=JCM_842_RECIPE,
        reference_urls=(JCM_842,),
        notes=(
            "JCM Medium 842 lists 3.3 g Tryptone (BD-Difco), 1.7 g Yeast "
            "extract (BD-Difco), 5 g NaCl, 15 g agar, and 1 L distilled water."
        ),
    ),
    Target(
        path="bacterial/TOGO_M878_1_3_LB_Agar.yaml",
        record_id="CultureMech:010296",
        source_term="TOGO:M878",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
            ("Yeast extract (BD-Difco)", "1.7", "G_PER_L"),
            ("Tryptone (BD-Difco)", "3.3", "G_PER_L"),
        ),
        ingredients=JCM_842_RECIPE,
        reference_urls=(TOGO_M878, JCM_842),
        notes=(
            "TOGO M878 mirrors JCM Medium 842: 3.3 g Tryptone (BD-Difco), "
            "1.7 g Yeast extract (BD-Difco), 5 g NaCl, 15 g agar, and 1 L "
            "distilled water."
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
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != target.source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.source_term}, "
            f"found {source_term!r}"
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


def _to_row(spec: Ingredient) -> dict[str, Any]:
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


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    if key in doc:
        del doc[key]

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
    if target.ph_value is not None:
        _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    repaired["ingredients"] = [_to_row(row) for row in target.ingredients]
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
