#!/usr/bin/env python3
"""Repair the next top score-15 records for causal graph review."""

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

CURATOR = "repair_top_causal_graph_score15.py"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

JCM_32 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=32"
CCAP_MY75S = "https://www.ccap.ac.uk/wp-content/uploads/MR_MY75S.pdf"
TOGO_M2227 = "https://togomedium.org/medium/M2227"
ATCC_1161 = "https://www.atcc.org/~/media/DE32194753474A659F151E68B8BC8D04.ashx"
TOGO_M1575 = "https://togomedium.org/medium/M1575"
NBRC_380 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=380"

AGAR = ("CHEBI:2509", "agar")
BEEF_EXTRACT = ("FOODON:03302088", "Beef extract")
GLUCOSE = ("CHEBI:17234", "glucose")
MALT_EXTRACT = ("FOODON:03301056", "malt extract")
NACL = ("CHEBI:26710", "sodium chloride")
PEPTONE = ("MICRO:0000178", "Peptone")
SEAWATER = ("ENVO:00002149", "sea water")
SUCROSE = ("CHEBI:17992", "sucrose")
WATER = ("CHEBI:15377", "water")
YEAST_EXTRACT = ("FOODON:03315426", "yeast extract")

Component = tuple[str, str, str]
Term = tuple[str, str]

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
}


@dataclass(frozen=True)
class Target:
    path: Path
    record_id: str
    media_term_id: str
    source_name: str
    imported_ingredients: tuple[Component, ...]
    final_ingredients: tuple[dict[str, Any], ...]
    notes: str
    action: str
    references: tuple[str, ...]
    physical_state: str
    composition_type: str = "UNDEFINED"
    imported_solutions: tuple[Component, ...] = field(default_factory=tuple)
    final_solutions: tuple[dict[str, Any], ...] = field(default_factory=tuple)
    ph_value: float | None = None
    ph_range: dict[str, float] | None = None
    preparation_steps: tuple[dict[str, Any], ...] = field(default_factory=tuple)
    sterilization: dict[str, Any] | None = None


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str | None = None,
    term: Term | None = None,
    nutritional_roles: tuple[str, ...] = (),
    physicochemical_roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes
        or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }

    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _solution(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    composition: tuple[dict[str, Any], ...],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
        "composition": [copy.deepcopy(row) for row in composition],
    }


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


MY20_SOURCE = "JCM Medium 32"
CCAP_SOURCE = "CCAP MR_MY75S"
M2227_SOURCE = "TOGO M2227 / ATCC Medium 1161"
M1575_SOURCE = "TOGO M1575 / NBRC Medium 380"

JCM_STERILIZATION = {
    "method": "AUTOCLAVE",
    "temperature": {"value": 121.0, "unit": "CELSIUS"},
    "duration": "15 min",
    "notes": "JCM's default instruction is to autoclave media at 121 C for 15 min.",
}

MY20_INGREDIENTS = (
    _component(
        "Peptone",
        "5.0",
        "G_PER_L",
        source=MY20_SOURCE,
        term=PEPTONE,
        nutritional_roles=("NITROGEN_SOURCE",),
    ),
    _component(
        "Yeast extract",
        "3.0",
        "G_PER_L",
        source=MY20_SOURCE,
        term=YEAST_EXTRACT,
        nutritional_roles=("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
    ),
    _component(
        "Malt extract",
        "3.0",
        "G_PER_L",
        source=MY20_SOURCE,
        term=MALT_EXTRACT,
        nutritional_roles=("CARBON_SOURCE", "NITROGEN_SOURCE"),
    ),
    _component(
        "Glucose",
        "200.0",
        "G_PER_L",
        source=MY20_SOURCE,
        term=GLUCOSE,
        nutritional_roles=("CARBON_SOURCE",),
    ),
    _component(
        "Agar",
        "20.0",
        "G_PER_L",
        source=MY20_SOURCE,
        term=AGAR,
        physicochemical_roles=("SOLIDIFYING_AGENT",),
    ),
    _component(
        "Distilled water",
        "1.0",
        "L",
        source=MY20_SOURCE,
        notes="JCM Medium 32 lists 1.0 L distilled water.",
        term=WATER,
    ),
)

MY75S_INGREDIENTS = (
    _component(
        "Natural filtered seawater",
        "750.0",
        "ML_PER_L",
        source=CCAP_SOURCE,
        notes="CCAP MR_MY75S lists 750.0 ml natural filtered seawater per liter.",
        term=SEAWATER,
    ),
    _component(
        "Deionised water",
        "250.0",
        "ML_PER_L",
        source=CCAP_SOURCE,
        notes="CCAP MR_MY75S lists 250.0 ml deionised water per liter.",
        term=WATER,
    ),
    _component(
        "Malt extract",
        "0.1",
        "G_PER_L",
        source=CCAP_SOURCE,
        term=MALT_EXTRACT,
        nutritional_roles=("CARBON_SOURCE", "NITROGEN_SOURCE"),
    ),
    _component(
        "Yeast extract",
        "0.1",
        "G_PER_L",
        source=CCAP_SOURCE,
        term=YEAST_EXTRACT,
        nutritional_roles=("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
    ),
    _component(
        "Bacteriological agar",
        "15.0",
        "G_PER_L",
        source=CCAP_SOURCE,
        term=AGAR,
        physicochemical_roles=("SOLIDIFYING_AGENT",),
    ),
)

M1575_INGREDIENTS = (
    _component(
        "Pepton",
        "5.0",
        "G_PER_L",
        source=M1575_SOURCE,
        term=PEPTONE,
        nutritional_roles=("NITROGEN_SOURCE",),
    ),
    _component(
        "Beef extract",
        "3.0",
        "G_PER_L",
        source=M1575_SOURCE,
        term=BEEF_EXTRACT,
        nutritional_roles=("PROTEIN_SOURCE",),
    ),
    _component(
        "Yeast extract",
        "5.0",
        "G_PER_L",
        source=M1575_SOURCE,
        term=YEAST_EXTRACT,
        nutritional_roles=("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
    ),
    _component(
        "NaCl",
        "3.0",
        "G_PER_L",
        source=M1575_SOURCE,
        term=NACL,
    ),
    _component(
        "Agar (if needed)",
        "15.0",
        "G_PER_L",
        source=M1575_SOURCE,
        term=AGAR,
        physicochemical_roles=("SOLIDIFYING_AGENT",),
    ),
    _component(
        "Distilled water",
        "1.0",
        "L",
        source=M1575_SOURCE,
        notes="NBRC Medium 380 lists 1 L distilled water.",
        term=WATER,
    ),
)

M2227_INGREDIENTS = (
    _component(
        "Distilled deionized water",
        "450.0",
        "ML_PER_L",
        source=M2227_SOURCE,
        notes=(
            "ATCC Medium 1161 combines Heart Infusion Broth with 450.0 ml/L "
            "distilled deionized water before autoclaving."
        ),
        term=WATER,
    ),
    _component(
        "Heart Infusion Broth (BD 238400)",
        "17.5",
        "G_PER_L",
        source=M2227_SOURCE,
        notes=(
            "ATCC Medium 1161 lists 17.5 g/L Heart Infusion Broth "
            "(BD 238400); this commercial broth is retained as an opaque "
            "component."
        ),
    ),
    _component(
        "Agar, Noble (BD 214230)",
        "10.0",
        "G_PER_L",
        source=M2227_SOURCE,
        notes=(
            "ATCC Medium 1161 lists 10.0 g/L Agar, Noble (BD 214230) "
            "in the component table."
        ),
        term=AGAR,
        physicochemical_roles=("SOLIDIFYING_AGENT",),
    ),
    _component(
        "Horse serum",
        "200.0",
        "ML_PER_L",
        source=M2227_SOURCE,
        notes=(
            "ATCC Medium 1161 adds 200.0 ml/L horse serum after "
            "heat-inactivation at 56 C for 30 minutes."
        ),
        term=("MICRO:0001235", "Horse serum"),
        nutritional_roles=("PROTEIN_SOURCE",),
    ),
)

M2227_SOLUTIONS = (
    _solution(
        "Yeast extract solution (15%)",
        "150.0",
        "ML_PER_L",
        source=M2227_SOURCE,
        notes="ATCC Medium 1161 adds 150.0 ml/L sterile 15% yeast extract solution.",
        composition=(
            _component(
                "Yeast extract",
                "15.0",
                "PERCENT_W_V",
                source=M2227_SOURCE,
                notes=(
                    "ATCC Medium 1161 specifies the yeast extract solution as "
                    "15.0% w/v."
                ),
                term=YEAST_EXTRACT,
                nutritional_roles=("PROTEIN_SOURCE", "VITAMIN_SOURCE"),
            ),
        ),
    ),
    _solution(
        "Sucrose solution",
        "200.0",
        "ML_PER_L",
        source=M2227_SOURCE,
        notes=(
            "ATCC Medium 1161 filter-sterilizes 40.0 g sucrose in "
            "200.0 ml distilled deionized water before addition."
        ),
        composition=(
            _component(
                "Sucrose",
                "200.0",
                "G_PER_L",
                source=M2227_SOURCE,
                notes=(
                    "ATCC Medium 1161 dissolves 40.0 g sucrose in 200.0 ml "
                    "distilled deionized water for a 200.0 g/L stock."
                ),
                term=SUCROSE,
                nutritional_roles=("CARBON_SOURCE",),
            ),
            _component(
                "Distilled deionized water",
                "1.0",
                "L",
                source=M2227_SOURCE,
                notes="ATCC Medium 1161 prepares the sucrose solution in water.",
                term=WATER,
            ),
        ),
    ),
)

TARGETS: tuple[Target, ...] = (
    Target(
        path=Path("bacterial/my20_agar.yaml"),
        record_id="CultureMech:002688",
        media_term_id="mediadive.medium:J32",
        source_name=MY20_SOURCE,
        imported_ingredients=(
            ("Peptone", "5", "G_PER_L"),
            ("Yeast extract", "3", "G_PER_L"),
            ("Malt extract", "3", "G_PER_L"),
            ("Glucose", "200", "G_PER_L"),
            ("Agar", "20", "G_PER_L"),
        ),
        final_ingredients=MY20_INGREDIENTS,
        notes=(
            "JCM Medium 32 MY20 Agar lists, per liter, 5.0 g Peptone, "
            "3.0 g Yeast extract, 3.0 g Malt extract, 200.0 g Glucose, "
            "20.0 g Agar, and 1.0 L Distilled water. MY20 is a YM Agar "
            "concentration variant that increases glucose from 10.0 g/L "
            "to 200.0 g/L."
        ),
        action="RESOLVED_JCM_32_MY20_SCORE15",
        references=(JCM_32,),
        physical_state="SOLID_AGAR",
        preparation_steps=(
            _step(
                1,
                "MIX",
                (
                    "Dissolve Peptone, Yeast extract, Malt extract, Glucose, "
                    "and Agar in 1.0 L distilled water."
                ),
            ),
            _step(2, "AUTOCLAVE", "Autoclave at 121 C for 15 min."),
        ),
        sterilization=JCM_STERILIZATION,
    ),
    Target(
        path=Path("bacterial/my75s.yaml"),
        record_id="CultureMech:000372",
        media_term_id="mediadive.medium:C60",
        source_name=CCAP_SOURCE,
        imported_ingredients=(
            ("Natural sea water", "750", "G_PER_L"),
            ("Malt extract", "0.1", "G_PER_L"),
            ("Yeast extract", "0.1", "G_PER_L"),
            ("Agar", "15", "G_PER_L"),
        ),
        final_ingredients=MY75S_INGREDIENTS,
        notes=(
            "CCAP MR_MY75S lists MY75S as Malt & Yeast Extract - 75% "
            "Seawater Agar with 750.0 ml natural filtered seawater, "
            "250.0 ml deionised water, 0.1 g Malt extract, 0.1 g Yeast "
            "extract, and 15.0 g Bacteriological agar per liter."
        ),
        action="RESOLVED_CCAP_MY75S_SCORE15",
        references=(CCAP_MY75S,),
        physical_state="SOLID_AGAR",
        preparation_steps=(
            _step(
                1,
                "HEAT",
                "Combine seawater and deionised water and heat without boiling.",
            ),
            _step(2, "DISSOLVE", "Dissolve the malt extract and yeast extract."),
            _step(
                3,
                "ADD_AGAR",
                "Cool slightly, add Bacteriological agar, and shake to disperse.",
            ),
            _step(4, "AUTOCLAVE", "Autoclave at 15 psi for 15 minutes."),
        ),
        sterilization={
            "method": "AUTOCLAVE",
            "notes": "CCAP MR_MY75S autoclaves the final agar at 15 psi for 15 minutes.",
        },
    ),
    Target(
        path=Path("bacterial/mycoplasma_medium_atcc_243_with_sucrose.yaml"),
        record_id="CultureMech:008815",
        media_term_id="TOGO:M2227",
        source_name=M2227_SOURCE,
        imported_ingredients=(
            ("Distilled deionized water", "650", "G_PER_L"),
            ("Sucrose", "40", "G_PER_L"),
            ("Horse serum", "200", "G_PER_L"),
            ("Agar, Noble (BD 214230)", "10", "G_PER_L"),
            ("Heart Infusion Broth (BD 238400)", "17.5", "G_PER_L"),
        ),
        imported_solutions=(("Yeast extract solution (15%)", "150", "G_PER_L"),),
        final_ingredients=M2227_INGREDIENTS,
        final_solutions=M2227_SOLUTIONS,
        notes=(
            "TOGO M2227 imports ATCC Medium 1161, Mycoplasma medium "
            "(ATCC 243) with sucrose. ATCC 1161 prepares the basal agar "
            "from 17.5 g Heart Infusion Broth, 10.0 g Agar Noble, and "
            "450.0 ml water; separately filter-sterilizes 40.0 g Sucrose "
            "in 200.0 ml water; and aseptically combines the cooled basal "
            "agar with the sterile sucrose, 150.0 ml 15% Yeast extract "
            "solution, and 200.0 ml heat-inactivated Horse serum."
        ),
        action="RESOLVED_TOGO_M2227_ATCC_1161_SCORE15",
        references=(TOGO_M2227, ATCC_1161),
        physical_state="SOLID_AGAR",
        ph_range={"min": 7.2, "max": 7.6},
        preparation_steps=(
            _step(
                1,
                "MIX",
                (
                    "Combine Heart Infusion Broth, Agar Noble, and "
                    "450.0 ml/L distilled deionized water."
                ),
            ),
            _step(2, "HEAT", "Boil to dissolve the Agar Noble."),
            _step(
                3,
                "AUTOCLAVE",
                "Autoclave the basal agar at 121 C for 15 minutes.",
            ),
            _step(
                4,
                "FILTER_STERILIZE",
                "Filter-sterilize Sucrose dissolved in 200.0 ml/L water.",
            ),
            _step(5, "HEAT", "Heat-inactivate Horse serum at 56 C for 30 minutes."),
            _step(
                6,
                "MIX",
                (
                    "Cool the basal agar to 50-55 C, warm the serum, "
                    "yeast extract, and sucrose solutions to 50-55 C, "
                    "and aseptically combine."
                ),
            ),
        ),
        sterilization={
            "method": "AUTOCLAVE",
            "temperature": {"value": 121.0, "unit": "CELSIUS"},
            "duration": "15 min",
            "notes": (
                "Autoclave the basal agar only; add sterile sucrose, "
                "commercial 15% yeast extract solution, and heat-inactivated "
                "horse serum aseptically after cooling."
            ),
        },
    ),
    Target(
        path=Path("bacterial/na_0_5_yeast_extract.yaml"),
        record_id="CultureMech:008124",
        media_term_id="TOGO:M1575",
        source_name=M1575_SOURCE,
        imported_ingredients=(
            ("Distilled water", "1", "G_PER_L"),
            ("Yeast extract", "5", "G_PER_L"),
            ("NaCl", "3", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Beef extract", "3", "G_PER_L"),
            ("Pepton", "5", "G_PER_L"),
        ),
        final_ingredients=M1575_INGREDIENTS,
        notes=(
            "TOGO M1575 imports NBRC Medium 380, NA + 0.5% Yeast "
            "Extract. NBRC 380 lists, per liter, 5 g Pepton, 3 g Beef "
            "extract, 5 g Yeast extract, 3 g NaCl, 15 g optional Agar, "
            "1 L Distilled water, and pH 7.0."
        ),
        action="RESOLVED_TOGO_M1575_NBRC_380_SCORE15",
        references=(TOGO_M1575, NBRC_380),
        physical_state="SOLID_AGAR",
        ph_value=7.0,
        preparation_steps=(
            _step(
                1,
                "MIX",
                (
                    "Dissolve Pepton, Beef extract, Yeast extract, NaCl, "
                    "and optional Agar in 1.0 L distilled water."
                ),
            ),
            _step(2, "ADJUST_PH", "Adjust pH to 7.0."),
        ),
    ),
)

TARGET_BY_PATH = {target.path: target for target in TARGETS}


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


def _composition_signature(rows: tuple[dict[str, Any], ...]) -> tuple[Component, ...]:
    return _signature(list(rows), "final rows")


def _grounded(row: dict[str, Any]) -> bool:
    for key in ("term", "mediaingredientmech_term", "mediaingredientmech_chebi_term"):
        term = row.get(key)
        if isinstance(term, dict) and term.get("id"):
            return True
    return False


def _all_composition_rows(doc: dict[str, Any]) -> list[dict[str, Any]]:
    rows = [row for row in doc.get("ingredients") or [] if isinstance(row, dict)]
    for solution in doc.get("solutions") or []:
        if not isinstance(solution, dict):
            continue
        rows.extend(
            row
            for row in solution.get("composition") or []
            if isinstance(row, dict)
        )
    return rows


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.media_term_id:
        raise ValueError(f"{target.path}: expected media term {target.media_term_id}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {
        target.imported_ingredients,
        _composition_signature(target.final_ingredients),
    }:
        raise ValueError(f"{target.path}: ingredient signature drifted")

    solution_signature = _signature(doc.get("solutions") or [], "solutions")
    if solution_signature not in {
        target.imported_solutions,
        _composition_signature(target.final_solutions),
    }:
        raise ValueError(f"{target.path}: solution signature drifted")


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

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)

    has_unmapped = any(not _grounded(row) for row in _all_composition_rows(doc))
    if has_unmapped and "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")
    while not has_unmapped and "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for reference in target.references:
        if reference not in existing:
            rows.append({"reference": reference})
            existing.add(reference)


def _append_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": target.action,
        "source": "; ".join(target.references),
        "notes": target.notes,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = target.composition_type
    repaired["physical_state"] = target.physical_state
    repaired.pop("ph_value", None)
    repaired.pop("ph_range", None)
    if target.ph_value is not None:
        _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    if target.ph_range is not None:
        _put_after(repaired, "ph_range", copy.deepcopy(target.ph_range), "physical_state")
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("kg_microbe_match", None)

    repaired["ingredients"] = copy.deepcopy(list(target.final_ingredients))
    if target.final_solutions:
        _put_after(
            repaired,
            "solutions",
            copy.deepcopy(list(target.final_solutions)),
            "ingredients",
        )
    else:
        repaired.pop("solutions", None)

    _put_after(repaired, "notes", target.notes, "media_term")
    if target.preparation_steps:
        _put_after(
            repaired,
            "preparation_steps",
            copy.deepcopy(list(target.preparation_steps)),
            "solutions" if target.final_solutions else "notes",
        )
    else:
        repaired.pop("preparation_steps", None)

    if target.sterilization:
        _put_after(
            repaired,
            "sterilization",
            copy.deepcopy(target.sterilization),
            "preparation_steps",
        )
    else:
        repaired.pop("sterilization", None)

    _ensure_flags(repaired)
    _ensure_references(repaired, target)
    _append_event(repaired, target)
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
