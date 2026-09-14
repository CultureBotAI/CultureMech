#!/usr/bin/env python3
"""Repair JCM/NBRC ISP-2 agar with artificial seawater source duplicates."""

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
TOGO_M573_PATH = Path(
    "bacterial/TOGO_M573_Yeast_Extract-Malt_Extract_Agar_ISP-2_With_Artificial_Seawater.yaml"
)
TOGO_M1804_PATH = Path(
    "bacterial/yeast_extract_malt_extract_agar_isp_2_with_artificial_seawater.yaml"
)
JCM_J569_PATH = Path(
    "fungal/yeast_extract_malt_extract_agar_isp_2_with_artificial_seawater.yaml"
)
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m573_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M573 = "https://togomedium.org/medium/M573"
TOGO_M1804 = "https://togomedium.org/medium/M1804"
JCM_569 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=569"
MEDIADIVE_J569 = "https://mediadive.dsmz.de/medium/J569"
NBRC_1030 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1030"

PH_VALUE = 7.3
TOGO_M573_SOURCE = "TOGO M573 / JCM Medium 569"
JCM_J569_SOURCE = "MediaDive J569 / JCM Medium 569"
TOGO_M1804_SOURCE = "TOGO M1804 / NBRC Medium 1030"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    source_term: str
    action: str
    source: str
    yeast_extract: str
    malt_extract: str
    imported_signature: tuple[Component, ...]
    final_signature: tuple[Component, ...]
    references: tuple[str, ...]
    notes: str
    event_notes: str
    parent_notes: str
    variant_modification: str
    include_jcm_sterilization: bool = False


TOGO_M573_IMPORTED: tuple[Component, ...] = (
    ("Malt extract (BD-Difco)", "10", "G_PER_L"),
    ("Artificial seawater", "1", "G_PER_L"),
    ("Glucose", "4", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Yeast extract (BD-Difco)", "4", "G_PER_L"),
)

JCM_J569_IMPORTED: tuple[Component, ...] = (
    ("Yeast extract", "4", "G_PER_L"),
    ("Malt extract", "10", "G_PER_L"),
    ("Glucose", "4", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Sea water", "1000", "G_PER_L"),
)

TOGO_M1804_IMPORTED: tuple[Component, ...] = (
    ("Bacto Malt Extract (Difco)", "10", "G_PER_L"),
    ("Artificial seawater", "1", "G_PER_L"),
    ("Glucose", "4", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Bacto Yeast Extract (Difco)", "4", "G_PER_L"),
)

JCM_FINAL: tuple[Component, ...] = (
    ("Yeast extract (BD-Difco)", "4.0", "G_PER_L"),
    ("Malt extract (BD-Difco)", "10.0", "G_PER_L"),
    ("Glucose", "4.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Artificial seawater", "1000.0", "ML_PER_L"),
)

NBRC_FINAL: tuple[Component, ...] = (
    ("Bacto Yeast Extract (Difco)", "4.0", "G_PER_L"),
    ("Bacto Malt Extract (Difco)", "10.0", "G_PER_L"),
    ("Glucose", "4.0", "G_PER_L"),
    ("Agar", "15.0", "G_PER_L"),
    ("Artificial seawater", "1000.0", "ML_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Yeast extract (BD-Difco)": ("FOODON:03315426", "yeast extract"),
    "Bacto Yeast Extract (Difco)": ("FOODON:03315426", "yeast extract"),
    "Malt extract (BD-Difco)": ("FOODON:03301056", "malt extract"),
    "Bacto Malt Extract (Difco)": ("FOODON:03301056", "malt extract"),
    "Glucose": ("CHEBI:17234", "glucose"),
    "Agar": ("CHEBI:2509", "agar"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}

JCM_STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
}

JCM_NOTES = (
    "JCM Medium 569 defines Yeast Extract-Malt Extract Agar (ISP-2) With "
    "Artificial Seawater with 4 g yeast extract, 10 g malt extract, 4 g "
    "glucose, 15 g agar, and 1 L artificial seawater, adjusted to pH 7.3."
)

NBRC_NOTES = (
    "NBRC Medium 1030 defines Yeast extract-malt extract agar (ISP-2) with "
    "artificial seawater with 4 g Bacto Yeast Extract (Difco), 10 g Bacto "
    "Malt Extract (Difco), 4 g glucose, 15 g agar, and 1 L artificial "
    "seawater, adjusted to pH 7.3."
)

PARENT_MEDIA = {
    "path": f"data/normalized_yaml/{JCM_J569_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:010536",
    "name": "yeast_extract_malt_extract_agar_isp_2_with_artificial_seawater",
    "notes": (
        "This record represents the same pH 7.3 ISP-2 with artificial seawater "
        "formulation as JCM Medium 569 / MediaDive J569."
    ),
}

TOGO_M573_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M573_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:009969",
    "name": "yeast_extract_malt_extract_agar_isp_2_with_artificial_seawater",
    "notes": (
        "TOGO M573 imports the same JCM Medium 569 ISP-2 artificial-seawater "
        "formulation represented by MediaDive J569."
    ),
}

TOGO_M1804_CHILD = {
    "path": f"data/normalized_yaml/{TOGO_M1804_PATH}",
    "relationship": "SOURCE_DUPLICATE",
    "id": "CultureMech:008374",
    "name": "yeast_extract_malt_extract_agar_isp_2_with_artificial_seawater",
    "notes": (
        "TOGO M1804 imports the same pH 7.3 ISP-2 artificial-seawater "
        "formulation from NBRC Medium 1030."
    ),
}

TARGETS: tuple[Target, ...] = (
    Target(
        path=TOGO_M573_PATH,
        record_id="CultureMech:009969",
        source_term="TOGO:M573",
        action="RESOLVED_TOGO_M573_SCORE15",
        source=TOGO_M573_SOURCE,
        yeast_extract="Yeast extract (BD-Difco)",
        malt_extract="Malt extract (BD-Difco)",
        imported_signature=TOGO_M573_IMPORTED,
        final_signature=JCM_FINAL,
        references=(TOGO_M573, JCM_569, MEDIADIVE_J569),
        notes=JCM_NOTES,
        event_notes=(
            "Corrected the imported artificial-seawater volume, added pH 7.3 "
            "from JCM Medium 569, grounded the yeast extract, malt extract, "
            "glucose, and agar rows, retained Artificial seawater as an "
            "intentionally unmapped 1000 ml/L input, removed the stale "
            "MediaDive 7 match, and linked MediaDive J569 as a source duplicate."
        ),
        parent_notes=TOGO_M573_CHILD["notes"],
        variant_modification=(
            "Same JCM Medium 569 ISP-2 with artificial seawater formulation "
            "represented by MediaDive J569."
        ),
        include_jcm_sterilization=True,
    ),
    Target(
        path=TOGO_M1804_PATH,
        record_id="CultureMech:008374",
        source_term="TOGO:M1804",
        action="RESOLVED_TOGO_M1804_SCORE15",
        source=TOGO_M1804_SOURCE,
        yeast_extract="Bacto Yeast Extract (Difco)",
        malt_extract="Bacto Malt Extract (Difco)",
        imported_signature=TOGO_M1804_IMPORTED,
        final_signature=NBRC_FINAL,
        references=(TOGO_M1804, NBRC_1030),
        notes=NBRC_NOTES,
        event_notes=(
            "Corrected the imported artificial-seawater volume, added pH 7.3 "
            "from NBRC Medium 1030, grounded the Bacto yeast extract, Bacto "
            "malt extract, glucose, and agar rows, retained Artificial "
            "seawater as an intentionally unmapped 1000 ml/L input, removed "
            "the stale MediaDive 7 match, and linked MediaDive J569 as the "
            "same formulation."
        ),
        parent_notes=TOGO_M1804_CHILD["notes"],
        variant_modification=(
            "Same final pH 7.3 ISP-2 artificial-seawater formulation as "
            "JCM Medium 569, with NBRC source-specific Bacto-branded yeast "
            "and malt extracts."
        ),
    ),
    Target(
        path=JCM_J569_PATH,
        record_id="CultureMech:010536",
        source_term="mediadive.medium:J569",
        action="RESOLVED_JCM_569_ISP2_ARTIFICIAL_SEAWATER",
        source=JCM_J569_SOURCE,
        yeast_extract="Yeast extract (BD-Difco)",
        malt_extract="Malt extract (BD-Difco)",
        imported_signature=JCM_J569_IMPORTED,
        final_signature=JCM_FINAL,
        references=(JCM_569, MEDIADIVE_J569),
        notes=JCM_NOTES,
        event_notes=(
            "Corrected the imported artificial-seawater row from a 1000 g/L "
            "Sea water placeholder to a 1000 ml/L Artificial seawater input, "
            "grounded the yeast extract and malt extract rows, retained "
            "Artificial seawater as intentionally unmapped, and linked the "
            "TOGO M573 and TOGO M1804 source duplicates."
        ),
        parent_notes="",
        variant_modification="",
        include_jcm_sterilization=True,
    ),
)

TARGET_BY_PATH = {target.path: target for target in TARGETS}
JCM_PARENT = TARGET_BY_PATH[JCM_J569_PATH]
CHILD_LINKS = (TOGO_M573_CHILD, TOGO_M1804_CHILD)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str | None = None,
    nutritional_roles: tuple[str, ...] = (),
    physicochemical_roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _ingredients(target: Target) -> list[dict[str, Any]]:
    return [
        _component(
            target.yeast_extract,
            "4.0",
            "G_PER_L",
            source=target.source,
            notes=f"{target.source} lists 4 g/L {target.yeast_extract}.",
            nutritional_roles=("NITROGEN_SOURCE",),
        ),
        _component(
            target.malt_extract,
            "10.0",
            "G_PER_L",
            source=target.source,
            notes=f"{target.source} lists 10 g/L {target.malt_extract}.",
            nutritional_roles=("CARBON_SOURCE", "NITROGEN_SOURCE"),
        ),
        _component(
            "Glucose",
            "4.0",
            "G_PER_L",
            source=target.source,
            nutritional_roles=("CARBON_SOURCE",),
        ),
        _component(
            "Agar",
            "15.0",
            "G_PER_L",
            source=target.source,
            physicochemical_roles=("SOLIDIFYING_AGENT",),
        ),
        _component(
            "Artificial seawater",
            "1000.0",
            "ML_PER_L",
            source=target.source,
            notes=(
                f"{target.source} lists 1 L artificial seawater per liter; "
                "the artificial seawater mixture is retained without a "
                "single-compound ontology grounding."
            ),
        ),
    ]


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
            raise ValueError(
                f"{label} row {row.get('preferred_term')!r} lacks concentration"
            )
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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: found id {doc.get('id')!r}, expected "
            f"{target.record_id!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != target.source_term:
        raise ValueError(
            f"{target.path}: found source term {source_term!r}, "
            f"expected {target.source_term!r}"
        )

    if _signature(doc.get("ingredients"), "ingredients") not in (
        target.imported_signature,
        target.final_signature,
    ):
        raise ValueError(f"{target.path}: ingredient signature drifted")


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

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for reference in references:
        if reference not in existing:
            rows.append({"reference": reference})
            existing.add(reference)


def _append_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": target.action,
        "source": "; ".join(target.references),
        "notes": target.event_notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == target.action
        ):
            history[index] = event
            return
    history.append(event)


def _ensure_child_links(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    expected_by_id = {child["id"]: child for child in CHILD_LINKS}
    filtered: list[Any] = []
    seen: set[str] = set()
    for child in children:
        if not isinstance(child, dict):
            raise ValueError("variant_children contains a non-mapping row")
        child_id = str(child.get("id") or "")
        child_path = str(child.get("path") or "")
        replacement = next(
            (
                link
                for link in CHILD_LINKS
                if link["id"] == child_id or link["path"] == child_path
            ),
            None,
        )
        if replacement is not None:
            if replacement["id"] not in seen:
                filtered.append(copy.deepcopy(replacement))
                seen.add(replacement["id"])
            continue
        filtered.append(child)

    for child_id, child in expected_by_id.items():
        if child_id not in seen:
            filtered.append(copy.deepcopy(child))

    doc["variant_children"] = filtered


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", PH_VALUE, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("kg_microbe_match", None)
    repaired.pop("solutions", None)
    repaired["ingredients"] = _ingredients(target)
    _put_after(repaired, "notes", target.notes, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        [
            {
                "step_number": 1,
                "action": "ADJUST_PH",
                "description": "Adjust pH to 7.3.",
            },
        ],
        "notes",
    )
    if target.include_jcm_sterilization:
        _put_after(
            repaired,
            "sterilization",
            copy.deepcopy(JCM_STERILIZATION),
            "preparation_steps",
        )
    else:
        repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, target.references)
    _append_event(repaired, target)

    if target.path == JCM_J569_PATH:
        _ensure_child_links(repaired)
    else:
        parent = copy.deepcopy(PARENT_MEDIA)
        parent["notes"] = target.parent_notes
        _put_after(repaired, "parent_media", parent, "references")
        _put_after(repaired, "variant_relationship", "SOURCE_DUPLICATE", "parent_media")
        _put_after(
            repaired,
            "variant_modifications",
            [target.variant_modification],
            "variant_relationship",
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
