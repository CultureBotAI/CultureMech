#!/usr/bin/env python3
"""Repair the next sparse score-15 TOGO and JCM records."""

from __future__ import annotations

import argparse
import copy
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_sparse_top_score15.py"
ACTION = "RESOLVED_SPARSE_TOP_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

JCM_86 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=86"
JCM_359 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=359"
NBRC_893 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=893"
TOGO_M1688 = "https://togomedium.org/medium/M1688"
TOGO_M2318 = "https://togomedium.org/medium/M2318"

AGAR = ("CHEBI:2509", "agar")
GLUCOSE = ("CHEBI:17234", "glucose")
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
    solution_signature: tuple[Component, ...] = field(default_factory=tuple)


def _component(
    preferred_term: str,
    value: str,
    *,
    source: str,
    notes: str,
    term: Term | None = None,
    unit: str = "G_PER_L",
) -> Ingredient:
    return Ingredient(
        preferred_term=preferred_term,
        value=value,
        unit=unit,
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


TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/1_10_strength_ytss_agar.yaml",
        record_id="CultureMech:008905",
        source_term="TOGO:M2318",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("yeast extract", "0.4", "PERCENT_W_V"),
            ("sea salts", "20", "G_PER_L"),
            ("tryptone", "0.25", "PERCENT_W_V"),
        ),
        ingredients=(
            _water("TOGO M2318"),
            _component(
                "yeast extract",
                "0.4",
                unit="PERCENT_W_V",
                source="TOGO M2318",
                notes="TOGO M2318 lists 0.4% yeast extract in 1/10-strength YTSS.",
                term=YEAST_EXTRACT,
            ),
            _component(
                "sea salts",
                "20",
                source="TOGO M2318",
                notes="TOGO M2318 lists sea salts as a mineral source.",
            ),
            _component(
                "tryptone",
                "0.25",
                unit="PERCENT_W_V",
                source="TOGO M2318",
                notes="TOGO M2318 lists this as tryptone.",
            ),
        ),
        reference_urls=(TOGO_M2318,),
        notes=(
            "TOGO M2318 lists 1 L distilled water, 0.4% yeast extract, "
            "20 g/L sea salts, and 0.25% tryptone."
        ),
    ),
    Target(
        path="bacterial/1_5_lbm_medium.yaml",
        record_id="CultureMech:008247",
        source_term="TOGO:M1688",
        imported_signature=(
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Bacto Yeast  Extract (Difco)", "1", "G_PER_L"),
            ("Bacto Tryptone (Difco)", "2", "G_PER_L"),
        ),
        solution_signature=(("Seawater*", "1", "G_PER_L"),),
        ingredients=(
            _component(
                "Agar (if needed)",
                "15",
                source="NBRC Medium 893",
                notes="NBRC Medium 893 lists 15 g agar as the optional solidifying component.",
                term=AGAR,
            ),
            _component(
                "Bacto Yeast  Extract (Difco)",
                "1",
                source="NBRC Medium 893",
                notes=(
                    "NBRC Medium 893 lists the Bacto Yeast Extract Difco product; "
                    "the product is source-disclosed but not reducible to one "
                    "ChEBI molecule."
                ),
            ),
            _component(
                "Bacto Tryptone (Difco)",
                "2",
                source="NBRC Medium 893",
                notes=(
                    "NBRC Medium 893 lists the Bacto Tryptone Difco product; the "
                    "product is source-disclosed but not reducible to one ChEBI "
                    "molecule."
                ),
            ),
        ),
        ph_value=7.0,
        reference_urls=(TOGO_M1688, NBRC_893),
        notes=(
            "TOGO M1688 mirrors NBRC Medium 893: 1 L seawater, 15 g optional "
            "agar, 1 g Bacto Yeast Extract, 2 g Bacto Tryptone, and pH 7.0."
        ),
    ),
    Target(
        path="bacterial/1_tryptone_agar.yaml",
        record_id="CultureMech:002718",
        source_term="mediadive.medium:J359",
        imported_signature=(
            ("Tryptone", "10", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        ingredients=(
            _component(
                "Tryptone (BD-Difco)",
                "10",
                source="JCM Medium 359",
                notes=(
                    "JCM Medium 359 lists the BD-Difco tryptone product; the "
                    "product is source-disclosed but not reducible to one ChEBI "
                    "molecule."
                ),
            ),
            _component(
                "Bacto agar (BD-Difco)",
                "15",
                source="JCM Medium 359",
                notes="JCM Medium 359 lists 15 g Bacto agar.",
                term=AGAR,
            ),
            _water("JCM Medium 359"),
        ),
        ph_value=7.0,
        reference_urls=(JCM_359,),
        notes=(
            "JCM Medium 359 lists 10 g Tryptone (BD-Difco), 15 g Bacto agar "
            "(BD-Difco), 1 L distilled water, and pH 7.0."
        ),
    ),
    Target(
        path="bacterial/25_glucose_medium.yaml",
        record_id="CultureMech:003216",
        source_term="mediadive.medium:J86",
        imported_signature=(
            ("Glucose", "250", "G_PER_L"),
            ("Polypeptone", "5", "G_PER_L"),
            ("Malt extract", "3", "G_PER_L"),
            ("Yeast extract", "3", "G_PER_L"),
            ("Agar", "25", "G_PER_L"),
        ),
        ingredients=(
            _component(
                "Glucose",
                "250",
                source="JCM Medium 86",
                notes="JCM Medium 86 lists 250 g glucose.",
                term=GLUCOSE,
            ),
            _component(
                "Polypepton (Nihon Pharm. Co.)",
                "5",
                source="JCM Medium 86",
                notes="JCM Medium 86 lists the Nihon Pharmaceutical Polypepton product.",
            ),
            _component(
                "Malt extract",
                "3",
                source="JCM Medium 86",
                notes="JCM Medium 86 lists this generic malt extract.",
            ),
            _component(
                "Yeast extract",
                "3",
                source="JCM Medium 86",
                notes="JCM Medium 86 lists this generic yeast extract.",
                term=YEAST_EXTRACT,
            ),
            _component(
                "Agar",
                "25",
                source="JCM Medium 86",
                notes="JCM Medium 86 lists 25 g agar.",
                term=AGAR,
            ),
            _water("JCM Medium 86"),
        ),
        reference_urls=(JCM_86,),
        notes=(
            "JCM Medium 86 lists 250 g glucose, 5 g Polypepton, 3 g malt "
            "extract, 3 g yeast extract, 25 g agar, and 1 L distilled water."
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


def _signature(rows: Any, key: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError(f"{key} is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{key} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{key} row {row.get('preferred_term')!r} lacks concentration")
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

    signature = _signature(doc.get("ingredients"), "ingredients")
    valid_signatures = {target.imported_signature, _recipe_signature(target.ingredients)}
    if signature not in valid_signatures:
        raise ValueError(
            f"{target.path}: ingredient signature drifted from "
            f"{target.imported_signature!r} to {signature!r}"
        )

    solution_signature = _signature(doc.get("solutions") or [], "solutions")
    if solution_signature != target.solution_signature:
        raise ValueError(
            f"{target.path}: solution signature drifted from "
            f"{target.solution_signature!r} to {solution_signature!r}"
        )


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
