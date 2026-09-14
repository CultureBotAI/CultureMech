#!/usr/bin/env python3
"""Repair JCM 481/482 reinforced clostridial sea-salt variants."""

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

CURATOR = "repair_jcm_j481_j482_sea_salt_score15.py"
ACTION = "RESOLVED_JCM_481_482_SEA_SALT_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

JCM_481 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=481"
JCM_482 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=482"
TOGO_M482 = "https://togomedium.org/medium/M482"
TOGO_M483 = "https://togomedium.org/medium/M483"

Component = tuple[str, str, str]

STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
}

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "AUTOCLAVE",
        "description": "Autoclave at 121 C for 15 min.",
    },
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
}


@dataclass(frozen=True)
class Target:
    path: Path
    expected_id: str
    expected_media_term: str
    title: str
    sea_salts_value: str
    imported_signature: tuple[Component, ...]
    references: tuple[str, ...]
    source: str

    @property
    def final_signature(self) -> tuple[Component, ...]:
        return (
            ("Reinforced clostridial medium (BD-Difco)", "38.0", "G_PER_L"),
            ("Sea salts (Sigma)", self.sea_salts_value, "G_PER_L"),
            ("Agar", "15.0", "G_PER_L"),
            ("Distilled water", "1.0", "L"),
        )

    @property
    def jcm_url(self) -> str:
        return self.references[-1]

    @property
    def notes(self) -> str:
        return (
            f"{self.source} records {self.title} with 38 g/L Reinforced "
            f"clostridial medium (BD-Difco), {self.sea_salts_value} g/L Sea "
            "salts (Sigma), 15 g/L Agar, 1 L distilled water, and the JCM "
            "default autoclaving at 121 C for 15 min. The commercial BD-Difco "
            "base and Sigma sea-salt mixture are retained as opaque unmapped "
            "components because JCM does not disclose their subcomposition."
        )


TARGETS: tuple[Target, ...] = (
    Target(
        path=Path("bacterial/reinforced_clostridial_medium_with_3_sea_salt.yaml"),
        expected_id="CultureMech:002831",
        expected_media_term="mediadive.medium:J481",
        title="JCM Medium 481 reinforced clostridial medium with 3% sea salt",
        sea_salts_value="30.0",
        imported_signature=(
            ("Reinforced clostridial medium", "38", "G_PER_L"),
            ("Sea Salt", "30", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        references=(JCM_481,),
        source="JCM Medium 481",
    ),
    Target(
        path=Path("bacterial/reinforced_clostridial_medium_with_4_sea_salt.yaml"),
        expected_id="CultureMech:002832",
        expected_media_term="mediadive.medium:J482",
        title="JCM Medium 482 reinforced clostridial medium with 4% sea salt",
        sea_salts_value="40.0",
        imported_signature=(
            ("Reinforced clostridial medium", "38", "G_PER_L"),
            ("Sea Salt", "40", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        references=(JCM_482,),
        source="JCM Medium 482",
    ),
    Target(
        path=Path("bacterial/TOGO_M482_Reinforced_Clostridial_Medium_With_3_Sea_Salt.yaml"),
        expected_id="CultureMech:009869",
        expected_media_term="TOGO:M482",
        title="TOGO M482 / JCM Medium 481 reinforced clostridial medium with 3% sea salt",
        sea_salts_value="30.0",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Sea salts (Sigma)", "30", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
            ("Reinforced clostridial medium (BD-Difco)", "38", "G_PER_L"),
        ),
        references=(TOGO_M482, JCM_481),
        source="TOGO M482 / JCM Medium 481",
    ),
    Target(
        path=Path("bacterial/TOGO_M483_Reinforced_Clostridial_Medium_With_4_Sea_Salt.yaml"),
        expected_id="CultureMech:009870",
        expected_media_term="TOGO:M483",
        title="TOGO M483 / JCM Medium 482 reinforced clostridial medium with 4% sea salt",
        sea_salts_value="40.0",
        imported_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Sea salts (Sigma)", "40", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
            ("Reinforced clostridial medium (BD-Difco)", "38", "G_PER_L"),
        ),
        references=(TOGO_M483, JCM_482),
        source="TOGO M483 / JCM Medium 482",
    ),
)

BY_PATH = {target.path: target for target in TARGETS}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(target: Target, preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": target.source,
    }
    if preferred_term == "Reinforced clostridial medium (BD-Difco)":
        row["notes"] = (
            f"{target.source} lists 38 g/L commercial BD-Difco Reinforced "
            "Clostridial Medium but does not disclose its component recipe."
        )
    elif preferred_term == "Sea salts (Sigma)":
        row["notes"] = (
            f"{target.source} lists {target.sea_salts_value} g/L commercial "
            "Sigma sea salts; this heterogeneous salt mixture is retained as "
            "an opaque source-qualified component."
        )
    else:
        row["notes"] = (
            f"{target.source} lists {value} {'L' if unit == 'L' else 'g/L'} " f"{preferred_term}."
        )
        row["term"] = _term(*GROUNDINGS[preferred_term])
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(row["term"])
        if preferred_term == "Agar":
            row["physicochemical_roles"] = ["SOLIDIFYING_AGENT"]
    return row


def _ingredients(target: Target) -> list[dict[str, Any]]:
    return [_component(target, *component) for component in target.final_signature]


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected id {target.expected_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.expected_media_term:
        raise ValueError(f"{target.path}: expected media term {target.expected_media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (target.imported_signature, target.final_signature):
        raise ValueError(f"{target.path}: ingredient signature drifted")

    if doc.get("solutions"):
        raise ValueError(f"{target.path}: unexpected solutions block")


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


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in target.references:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(target.references),
        "notes": (
            "Corrected the JCM 481/482 reinforced-clostridial sea-salt "
            "formula, grounded water and agar, added JCM default autoclaving, "
            "and marked the BD-Difco base and Sigma sea salts as intentionally "
            "opaque commercial ingredients."
        ),
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
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired["ingredients"] = _ingredients(target)
    repaired.pop("solutions", None)
    repaired.pop("kg_microbe_match", None)
    _put_after(repaired, "preparation_steps", copy.deepcopy(list(PREPARATION_STEPS)), "media_term")
    _put_after(repaired, "sterilization", copy.deepcopy(STERILIZATION), "preparation_steps")
    _put_after(repaired, "notes", target.notes, "sterilization")
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(_load(path), target)
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
