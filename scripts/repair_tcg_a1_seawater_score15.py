#!/usr/bin/env python3
"""Repair score-15 TCG and A1 seawater-family records."""

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

CURATOR = "repair_tcg_a1_seawater_score15.py"
ACTION = "RESOLVED_TCG_A1_SEAWATER_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

JCM_720 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=720"
TOGO_M743 = "https://togomedium.org/medium/M743"
DSMZ_1009 = "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1009.pdf"
KOMODO_1009 = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1009"
)
DSMZ_1054 = "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1054.pdf"
KOMODO_1054 = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1054"
)

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    source_term: str
    source_label: str
    physical_state: str
    imported_signatures: tuple[tuple[Component, ...], ...]
    ingredients: tuple[dict[str, Any], ...]
    reference_urls: tuple[str, ...]
    notes: str
    parent_media: dict[str, Any] | None = None
    variant_relationship: str | None = None
    variant_modifications: tuple[str, ...] = ()
    variant_children: tuple[dict[str, Any], ...] = field(default_factory=tuple)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str] | None = None,
    chebi_link: bool = True,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if chebi_link:
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _glucose(source: str) -> dict[str, Any]:
    return _ingredient(
        "Glucose",
        "4",
        "G_PER_L",
        source=source,
        notes=f"{source} lists 4 g glucose.",
        term=("CHEBI:17234", "glucose"),
    )


def _agar(value: str, source: str) -> dict[str, Any]:
    return _ingredient(
        "Agar",
        value,
        "G_PER_L",
        source=source,
        notes=f"{source} lists {value} g agar.",
        term=("CHEBI:2509", "agar"),
    )


def _starch(source: str) -> dict[str, Any]:
    return _ingredient(
        "Starch",
        "10",
        "G_PER_L",
        source=source,
        notes=f"{source} lists 10 g starch.",
        term=("CHEBI:28017", "starch"),
    )


def _yeast_extract(source: str) -> dict[str, Any]:
    return _ingredient(
        "Yeast extract",
        "4",
        "G_PER_L",
        source=source,
        notes=f"{source} lists 4 g generic yeast extract.",
        term=("FOODON:03315426", "yeast extract"),
        chebi_link=False,
    )


def _tcg_jcm_ingredients(source: str) -> tuple[dict[str, Any], ...]:
    return (
        _ingredient(
            "Tryptone (BD-Difco)",
            "3",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists the BD-Difco tryptone product; the product is "
                "source-disclosed but not reducible to one ChEBI molecule."
            ),
        ),
        _ingredient(
            "Casitone (BD-Difco)",
            "5",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists the BD-Difco Casitone product; the product is "
                "source-disclosed but not reducible to one ChEBI molecule."
            ),
        ),
        _glucose(source),
        _agar("15", source),
        _ingredient(
            "Artificial seawater",
            "1000",
            "ML_PER_L",
            source=source,
            notes=(
                f"{source} lists 1.0 L artificial seawater; the seawater stock "
                "is a source-disclosed mixture, not a single ChEBI molecule."
            ),
        ),
    )


def _tcg_dsmz_ingredients(source: str) -> tuple[dict[str, Any], ...]:
    return (
        _ingredient(
            "Tryptone",
            "3",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists tryptone as an undefined digest; it is not "
                "reducible to one ChEBI molecule."
            ),
        ),
        _ingredient(
            "Casitone",
            "5",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists Casitone as an undefined digest; it is not "
                "reducible to one ChEBI molecule."
            ),
        ),
        _glucose(source),
        _ingredient(
            "Seawater (see below)",
            "1000",
            "ML_PER_L",
            source=source,
            notes=(
                f"{source} lists 1.0 L seawater and defines artificial seawater "
                "as 32 g sea salt in 1000 mL distilled water."
            ),
        ),
    )


def _a1_ingredients(source: str) -> tuple[dict[str, Any], ...]:
    return (
        _yeast_extract(source),
        _ingredient(
            "Bacto peptone",
            "2",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists Bacto peptone; the product is source-disclosed "
                "but not reducible to one ChEBI molecule."
            ),
        ),
        _starch(source),
        _ingredient(
            "Seawater (Biomaris 089, natural or artificial)",
            "1000",
            "ML_PER_L",
            source=source,
            notes=(
                f"{source} lists 1.0 L Biomaris 089 seawater and allows natural "
                "or artificial seawater."
            ),
        ),
        _agar("20", source),
    )


def _ref(
    path: str,
    relationship: str,
    record_id: str,
    name: str,
    notes: str,
) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{path}",
        "relationship": relationship,
        "id": record_id,
        "name": name,
        "notes": notes,
    }


TCG_DSMZ_PATH = "bacterial/tcg_medium.yaml"
TCG_JCM_PATH = "bacterial/JCM_J720_TCG_MEDIUM.yaml"
TCG_KOMODO_PATH = "bacterial/KOMODO_1009_TCG_medium.yaml"
TCG_TOGO_PATH = "bacterial/TOGO_M743_TCG_Medium.yaml"
A1_DSMZ_PATH = "bacterial/a1_medium.yaml"
A1_KOMODO_PATH = "bacterial/KOMODO_1054_A1-MEDIUM.yaml"

TCG_JCM_PARENT = _ref(
    TCG_DSMZ_PATH,
    "SUPPLEMENTED_VARIANT",
    "CultureMech:000425",
    "tcg_medium",
    "JCM Medium 720 adds agar to the same tryptone, Casitone, glucose, and seawater base.",
)
TCG_TOGO_PARENT = _ref(
    TCG_JCM_PATH,
    "SOURCE_DUPLICATE",
    "CultureMech:003065",
    "tcg_medium",
    "TOGO M743 mirrors JCM Medium 720.",
)
TCG_KOMODO_PARENT = _ref(
    TCG_DSMZ_PATH,
    "SOURCE_DUPLICATE",
    "CultureMech:000425",
    "tcg_medium",
    "KOMODO Medium 1009 points to the same DSMZ Medium 1009 formulation.",
)
A1_KOMODO_PARENT = _ref(
    A1_DSMZ_PATH,
    "SOURCE_DUPLICATE",
    "CultureMech:000483",
    "a1_medium",
    "KOMODO Medium 1054 points to the same DSMZ Medium 1054 formulation.",
)

TARGETS: tuple[Target, ...] = (
    Target(
        path=TCG_JCM_PATH,
        record_id="CultureMech:003065",
        source_term="mediadive.medium:J720",
        source_label="JCM Medium 720",
        physical_state="SOLID_AGAR",
        imported_signatures=(((
            ("Tryptone", "3", "G_PER_L"),
            ("Casitone", "5", "G_PER_L"),
            ("Glucose", "4", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
            ("Sea water", "1000", "G_PER_L"),
        )),),
        ingredients=_tcg_jcm_ingredients("JCM Medium 720"),
        reference_urls=(JCM_720,),
        notes=(
            "JCM Medium 720 lists 3 g Tryptone (BD-Difco), 5 g Casitone "
            "(BD-Difco), 4 g glucose, 15 g agar, and 1 L artificial seawater."
        ),
        parent_media=TCG_JCM_PARENT,
        variant_relationship="SUPPLEMENTED_VARIANT",
        variant_modifications=(
            "JCM Medium 720 adds 15 g/L agar to DSMZ Medium 1009's liquid TCG base.",
        ),
        variant_children=(
            _ref(
                TCG_TOGO_PATH,
                "SOURCE_DUPLICATE",
                "CultureMech:010148",
                "tcg_medium",
                "TOGO M743 mirrors JCM Medium 720.",
            ),
        ),
    ),
    Target(
        path=TCG_TOGO_PATH,
        record_id="CultureMech:010148",
        source_term="TOGO:M743",
        source_label="TOGO M743 / JCM Medium 720",
        physical_state="SOLID_AGAR",
        imported_signatures=(((
            ("Artificial seawater", "1", "G_PER_L"),
            ("Glucose", "4", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
            ("Tryptone (BD-Difco)", "3", "G_PER_L"),
            ("Casitone (BD-Difco)", "5", "G_PER_L"),
        )),),
        ingredients=_tcg_jcm_ingredients("TOGO M743 / JCM Medium 720"),
        reference_urls=(TOGO_M743, JCM_720),
        notes=(
            "TOGO M743 mirrors JCM Medium 720 with 3 g Tryptone (BD-Difco), "
            "5 g Casitone (BD-Difco), 4 g glucose, 15 g agar, and 1 L "
            "artificial seawater."
        ),
        parent_media=TCG_TOGO_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(
            "Source-catalogue duplicate of JCM Medium 720; TOGO M743 preserves the same formulation.",
        ),
    ),
    Target(
        path=TCG_DSMZ_PATH,
        record_id="CultureMech:000425",
        source_term="mediadive.medium:1009",
        source_label="DSMZ Medium 1009",
        physical_state="LIQUID",
        imported_signatures=(
            (
                ("Tryptone", "3", "G_PER_L"),
                ("Casitone", "5", "G_PER_L"),
                ("Glucose", "4", "G_PER_L"),
                ("Sea water", "1000", "G_PER_L"),
                ("Agar", "20", "G_PER_L"),
            ),
        ),
        ingredients=_tcg_dsmz_ingredients("DSMZ Medium 1009"),
        reference_urls=(DSMZ_1009,),
        notes=(
            "DSMZ Medium 1009 lists 3 g tryptone, 5 g Casitone, 4 g glucose, "
            "1 L seawater, and defines artificial seawater as 32 g sea salt in "
            "1000 mL distilled water; it does not include the imported 20 g/L "
            "agar row."
        ),
        variant_children=(
            _ref(
                TCG_JCM_PATH,
                "SUPPLEMENTED_VARIANT",
                "CultureMech:003065",
                "tcg_medium",
                "JCM Medium 720 adds 15 g/L agar to DSMZ Medium 1009's liquid base.",
            ),
            _ref(
                TCG_KOMODO_PATH,
                "SOURCE_DUPLICATE",
                "CultureMech:003514",
                "tcg_medium",
                "KOMODO Medium 1009 points to the same DSMZ Medium 1009 formulation.",
            ),
        ),
    ),
    Target(
        path=TCG_KOMODO_PATH,
        record_id="CultureMech:003514",
        source_term="komodo.medium:1009",
        source_label="KOMODO Medium 1009 / DSMZ Medium 1009",
        physical_state="LIQUID",
        imported_signatures=(
            (
                ("Tryptone", "3", "G_PER_L"),
                ("Casitone", "5", "G_PER_L"),
                ("Glucose", "4", "G_PER_L"),
                ("Sea water", "1000", "G_PER_L"),
                ("Agar", "20", "G_PER_L"),
            ),
        ),
        ingredients=_tcg_dsmz_ingredients("KOMODO Medium 1009 / DSMZ Medium 1009"),
        reference_urls=(KOMODO_1009, DSMZ_1009),
        notes=(
            "KOMODO Medium 1009 points to DSMZ Medium 1009. Both list tryptone, "
            "Casitone, glucose, and seawater as the recipe components; neither "
            "source lists the imported 20 g/L agar row."
        ),
        parent_media=TCG_KOMODO_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(
            "Source-catalogue duplicate of DSMZ Medium 1009; KOMODO Medium 1009 preserves the same formulation.",
        ),
    ),
    Target(
        path=A1_DSMZ_PATH,
        record_id="CultureMech:000483",
        source_term="mediadive.medium:1054",
        source_label="DSMZ Medium 1054",
        physical_state="SOLID_AGAR",
        imported_signatures=(
            (
                ("Yeast extract", "4", "G_PER_L"),
                ("Bacto peptone", "2", "G_PER_L"),
                ("Starch", "10", "G_PER_L"),
                ("Sea water", "1000", "G_PER_L"),
                ("Agar", "20", "G_PER_L"),
            ),
        ),
        ingredients=_a1_ingredients("DSMZ Medium 1054"),
        reference_urls=(DSMZ_1054,),
        notes=(
            "DSMZ Medium 1054 lists 4 g yeast extract, 2 g Bacto peptone, "
            "10 g starch, 1 L Biomaris 089 seawater, and 20 g agar."
        ),
        variant_children=(
            _ref(
                A1_KOMODO_PATH,
                "SOURCE_DUPLICATE",
                "CultureMech:003630",
                "a1_medium",
                "KOMODO Medium 1054 points to the same DSMZ Medium 1054 formulation.",
            ),
        ),
    ),
    Target(
        path=A1_KOMODO_PATH,
        record_id="CultureMech:003630",
        source_term="komodo.medium:1054",
        source_label="KOMODO Medium 1054 / DSMZ Medium 1054",
        physical_state="SOLID_AGAR",
        imported_signatures=(
            (
                ("Yeast extract", "4", "G_PER_L"),
                ("Bacto peptone", "2", "G_PER_L"),
                ("Starch", "10", "G_PER_L"),
                ("Sea water", "1000", "G_PER_L"),
                ("Agar", "20", "G_PER_L"),
            ),
        ),
        ingredients=_a1_ingredients("KOMODO Medium 1054 / DSMZ Medium 1054"),
        reference_urls=(KOMODO_1054, DSMZ_1054),
        notes=(
            "KOMODO Medium 1054 points to DSMZ Medium 1054 with 4 g yeast "
            "extract, 2 g Bacto peptone, 10 g starch, 1 L Biomaris 089 "
            "seawater, and 20 g agar."
        ),
        parent_media=A1_KOMODO_PARENT,
        variant_relationship="SOURCE_DUPLICATE",
        variant_modifications=(
            "Source-catalogue duplicate of DSMZ Medium 1054; KOMODO Medium 1054 preserves the same formulation.",
        ),
    ),
)
TARGET_BY_PATH: dict[str, Target] = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _signature(rows: Any, label: str) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
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


def _recipe_signature(rows: tuple[dict[str, Any], ...]) -> tuple[Component, ...]:
    return _signature(list(rows), "target ingredients")


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != target.source_term:
        raise ValueError(
            f"{target.path}: expected source term {target.source_term}, found {source_term!r}"
        )

    accepted = {*target.imported_signatures, _recipe_signature(target.ingredients)}
    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in accepted:
        raise ValueError(
            f"{target.path}: ingredient signature drifted from {accepted!r} to {signature!r}"
        )


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


def _ensure_variant_links(doc: dict[str, Any], target: Target) -> None:
    if target.parent_media is None:
        doc.pop("parent_media", None)
        doc.pop("variant_relationship", None)
        doc.pop("variant_modifications", None)
    else:
        _put_after(doc, "parent_media", copy.deepcopy(target.parent_media), "curation_history")
        _put_after(doc, "variant_relationship", target.variant_relationship, "parent_media")
        _put_after(
            doc,
            "variant_modifications",
            list(target.variant_modifications),
            "variant_relationship",
        )

    if target.variant_children:
        _put_after(
            doc,
            "variant_children",
            copy.deepcopy(list(target.variant_children)),
            "curation_history",
        )
    else:
        doc.pop("variant_children", None)


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["physical_state"] = target.physical_state
    repaired["ingredients"] = copy.deepcopy(list(target.ingredients))
    _ensure_variant_links(repaired, target)
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
