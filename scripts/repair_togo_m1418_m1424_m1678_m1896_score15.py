#!/usr/bin/env python3
"""Repair four score-15 TOGO/NBRC imports with sparse or migrated formulae."""

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

CURATOR = "repair_togo_m1418_m1424_m1678_m1896_score15.py"
ACTION = "RESOLVED_TOGO_M1418_M1424_M1678_M1896_SCORE15"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

TOGO_M1418 = "https://togomedium.org/medium/M1418"
TOGO_M1424 = "https://togomedium.org/medium/M1424"
TOGO_M1678 = "https://togomedium.org/medium/M1678"
TOGO_M1896 = "https://togomedium.org/medium/M1896"
NBRC_15 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=15"
NBRC_22 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=22"
NBRC_883 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=883"
NBRC_1153 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1153"

Component = tuple[str, str, str]


@dataclass(frozen=True)
class RepairTarget:
    path: Path
    record_id: str
    source_term: str
    title: str
    source: str
    references: tuple[str, str]
    imported_ingredient_signature: tuple[Component, ...]
    imported_solution_signature: tuple[Component, ...]
    final_ingredient_signature: tuple[Component, ...]
    notes: str
    event_notes: str
    ph_value: float | None = None
    preparation_steps: tuple[dict[str, Any], ...] = ()


GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "CaCO3": ("CHEBI:3311", "calcium carbonate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}
PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Agar": ("SOLIDIFYING_AGENT",),
    "Agar (if needed)": ("SOLIDIFYING_AGENT",),
    "Na2CO3": ("BUFFER",),
}
UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
}


TARGETS: tuple[RepairTarget, ...] = (
    RepairTarget(
        path=Path("bacterial/vegetable_juice_seawater_agar_v_8_swa.yaml"),
        record_id="CultureMech:007955",
        source_term="TOGO:M1418",
        title="Vegetable Juice Seawater Agar (V-8 SWA)",
        source="TOGO M1418 / NBRC Medium 15",
        references=(TOGO_M1418, NBRC_15),
        imported_ingredient_signature=(
            ("Seawater (2% salinity)", "800", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        imported_solution_signature=(
            ("CaCO3*", "3", "G_PER_L"),
            ("Vegetable juice*", "200", "G_PER_L"),
        ),
        final_ingredient_signature=(
            ("Vegetable juice", "200", "ML_PER_L"),
            ("CaCO3", "3", "G_PER_L"),
            ("Seawater (2% salinity)", "800", "ML_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        ph_value=7.0,
        preparation_steps=(
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Add 3 g CaCO3 to approximately 300 ml V-8 vegetable juice "
                    "and stir for 2 h."
                ),
                "duration": "2 h",
            },
            {
                "step_number": 2,
                "action": "FILTER",
                "description": (
                    "Centrifuge and retain 200 ml of the clarified vegetable "
                    "juice supernatant."
                ),
            },
            {
                "step_number": 3,
                "action": "MIX",
                "description": (
                    "Add 800 ml seawater at 2% salinity and 15 g agar to "
                    "the 200 ml vegetable juice supernatant."
                ),
            },
            {
                "step_number": 4,
                "action": "ADJUST_PH",
                "description": "Adjust pH to 7.0.",
            },
        ),
        notes=(
            "TOGO M1418 imports NBRC Medium 15 as Vegetable Juice Seawater Agar "
            "(V-8 SWA). NBRC 15 lists 200 ml Vegetable juice, 3 g CaCO3, "
            "800 ml Seawater at 2% salinity, and 15 g Agar at pH 7.0."
        ),
        event_notes=(
            "Flattened the migrated Vegetable juice and CaCO3 solution wrappers, "
            "corrected Vegetable juice and Seawater from mass-like imports to "
            "ml/L volume additions, grounded CaCO3 and agar, added pH 7.0 and "
            "NBRC's V-8 juice clarification procedure, and retained Vegetable "
            "juice and Seawater as sourced opaque components."
        ),
    ),
    RepairTarget(
        path=Path("bacterial/trypticase_yeast_extract_agar_tys.yaml"),
        record_id="CultureMech:007962",
        source_term="TOGO:M1424",
        title="Trypticase Yeast Extract Agar (TYS)",
        source="TOGO M1424 / NBRC Medium 22",
        references=(TOGO_M1424, NBRC_22),
        imported_ingredient_signature=(
            ("Yeast extract", "1", "G_PER_L"),
            ("Seawater (2% salinity)", "1", "G_PER_L"),
            ("Agar", "12", "G_PER_L"),
        ),
        imported_solution_signature=(
            ("Trypticase Peptone (BBL) or Hipolypepton*", "0.1", "G_PER_L"),
        ),
        final_ingredient_signature=(
            ("Trypticase Peptone (BBL) or Hipolypepton", "0.1", "G_PER_L"),
            ("Yeast extract", "1", "G_PER_L"),
            ("Agar", "12", "G_PER_L"),
            ("Seawater (2% salinity)", "1.0", "L"),
        ),
        notes=(
            "TOGO M1424 imports NBRC Medium 22 as Trypticase Yeast Extract Agar "
            "(TYS). NBRC 22 lists 0.1 g Trypticase Peptone (BBL) or "
            "Hipolypepton, 1 g Yeast extract, 12 g Agar, and 1 L Seawater at "
            "2% salinity."
        ),
        event_notes=(
            "Flattened the migrated Trypticase Peptone solution wrapper, "
            "corrected Seawater from a mass-like 1 g/L import to 1 L, grounded "
            "Yeast extract and agar, and retained the alternative Trypticase "
            "Peptone or Hipolypepton input and Seawater as sourced opaque "
            "components."
        ),
    ),
    RepairTarget(
        path=Path("bacterial/tsb_0_2_w_v_na2co3.yaml"),
        record_id="CultureMech:008236",
        source_term="TOGO:M1678",
        title="TSB + 0.2%(w/v) Na2CO3",
        source="TOGO M1678 / NBRC Medium 883",
        references=(TOGO_M1678, NBRC_883),
        imported_ingredient_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
        ),
        imported_solution_signature=(
            ("Na2CO3**", "2", "G_PER_L"),
            ("Bacto Tryptic Soy Broth*", "30", "G_PER_L"),
        ),
        final_ingredient_signature=(
            ("Bacto Tryptic Soy Broth", "30", "G_PER_L"),
            ("Na2CO3", "2", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Distilled water", "1.0", "L"),
        ),
        ph_value=8.5,
        preparation_steps=(
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Suspend 30 g Bacto Tryptic Soy Broth and 15 g agar, if "
                    "needed, in 1 L distilled water."
                ),
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Sterilize 2 g Na2CO3 separately by autoclaving.",
            },
            {
                "step_number": 3,
                "action": "MIX",
                "description": (
                    "Add the separately autoclaved Na2CO3 to the other "
                    "ingredients; the final pH is around 8.5."
                ),
            },
        ),
        notes=(
            "TOGO M1678 imports NBRC Medium 883 as TSB + 0.2%(w/v) Na2CO3. "
            "NBRC 883 lists 30 g Bacto Tryptic Soy Broth, 2 g Na2CO3 "
            "sterilized separately by autoclaving, 15 g Agar if needed, "
            "and 1 L Distilled water; the final pH is around 8.5."
        ),
        event_notes=(
            "Flattened the migrated Bacto Tryptic Soy Broth and Na2CO3 "
            "solution wrappers, corrected Distilled water from a mass-like "
            "1 g/L import to 1 L, grounded Na2CO3, water, and agar, added "
            "the final pH and separate Na2CO3 sterilization, and retained "
            "Bacto Tryptic Soy Broth as a sourced opaque component."
        ),
    ),
    RepairTarget(
        path=Path("bacterial/tryptone_yeast_extract_broth_isp_medium_no_1.yaml"),
        record_id="CultureMech:008471",
        source_term="TOGO:M1896",
        title="Tryptone Yeast Extract Broth (ISP Medium No.1)",
        source="TOGO M1896 / NBRC Medium 1153",
        references=(TOGO_M1896, NBRC_1153),
        imported_ingredient_signature=(
            ("Distilled water", "1", "G_PER_L"),
            ("Agar (if needed)", "20", "G_PER_L"),
            ("ISP Medium 1 (Difco)", "8", "G_PER_L"),
        ),
        imported_solution_signature=(),
        final_ingredient_signature=(
            ("ISP Medium 1 (Difco)", "8", "G_PER_L"),
            ("Agar (if needed)", "20", "G_PER_L"),
            ("Distilled water", "1.0", "L"),
        ),
        notes=(
            "TOGO M1896 imports NBRC Medium 1153 as Tryptone Yeast Extract "
            "Broth (ISP Medium No.1). NBRC 1153 lists 8 g ISP Medium 1 "
            "(Difco), 20 g Agar if needed, and 1 L Distilled water."
        ),
        event_notes=(
            "Corrected Distilled water from a mass-like 1 g/L import to 1 L, "
            "grounded water and agar, and retained ISP Medium 1 (Difco) as a "
            "sourced opaque commercial component."
        ),
    ),
)


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


def _notes(target: RepairTarget, preferred_term: str, value: str, unit: str) -> str:
    amount = f"{value} {UNIT_LABELS[unit]}"
    if preferred_term == "Bacto Tryptic Soy Broth":
        return (
            f"{target.source} lists {amount} Bacto Tryptic Soy Broth; this "
            "commercial powder is retained as a source-disclosed complex component."
        )
    if preferred_term == "ISP Medium 1 (Difco)":
        return (
            f"{target.source} lists {amount} ISP Medium 1 (Difco); this "
            "commercial powder is retained as a source-disclosed complex component."
        )
    if preferred_term == "Seawater (2% salinity)":
        return (
            f"{target.source} lists {amount} Seawater at 2% salinity without "
            "disclosing the seawater composition."
        )
    if preferred_term == "Trypticase Peptone (BBL) or Hipolypepton":
        return (
            f"{target.source} lists {amount} Trypticase Peptone (BBL) or "
            "Hipolypepton without disclosing a digest composition."
        )
    if preferred_term == "Vegetable juice":
        return (
            f"{target.source} lists {amount} Vegetable juice supernatant; this "
            "food extract is retained as a source-disclosed complex component."
        )
    if preferred_term == "Agar (if needed)":
        return f"{target.source} lists {amount} Agar if needed."
    return f"{target.source} lists {amount} {preferred_term}."


def _component(target: RepairTarget, name: str, value: str, unit: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": name,
        "concentration": {"value": value, "unit": unit},
        "source": target.source,
        "notes": _notes(target, name, value, unit),
    }

    grounding = GROUNDINGS.get(name)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(name)
    if physicochemical_roles is not None:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _ingredients(target: RepairTarget) -> list[dict[str, Any]]:
    return [
        _component(target, name, value, unit)
        for name, value, unit in target.final_ingredient_signature
    ]


def _ensure_target(doc: dict[str, Any], target: RepairTarget) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.source_term:
        raise ValueError(f"{target.path}: expected media term {target.source_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    solution_signature = _signature(doc.get("solutions"), "solutions")

    valid_signatures = (
        (target.imported_ingredient_signature, target.imported_solution_signature),
        (target.final_ingredient_signature, ()),
    )
    if (ingredient_signature, solution_signature) not in valid_signatures:
        raise ValueError(
            f"{target.path}: component signature drifted to "
            f"ingredients={ingredient_signature!r}, solutions={solution_signature!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag not in {"incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(
        (
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        )
    )
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], target: RepairTarget) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in target.references:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_event(doc: dict[str, Any], target: RepairTarget) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
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
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any], target: RepairTarget) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    if target.ph_value is None:
        repaired.pop("ph_value", None)
    else:
        _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(target)
    repaired.pop("solutions", None)
    if target.preparation_steps:
        _put_after(
            repaired,
            "preparation_steps",
            copy.deepcopy(list(target.preparation_steps)),
            "media_term",
        )
    else:
        repaired.pop("preparation_steps", None)
    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _ensure_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    repairs: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        repairs[path] = repair_record(_load(path), target)
    return repairs


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans = plan_repairs(args.normalized_dir)
    changed_count = 0
    for path, doc in sorted(plans.items()):
        changed = path.read_bytes() != dump_record(doc).encode("utf-8")
        changed_count += int(changed)
        if args.apply and changed:
            write_record(path, doc)
        status = "wrote" if args.apply and changed else "would" if changed else "skip"
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
