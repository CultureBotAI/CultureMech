#!/usr/bin/env python3
"""Repair TOGO M2852 Wilkins-Chalgren agar plates for H. pylori."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from record_io import dump_record, write_record  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"
TARGET = Path(
    "bacterial/"
    "wilkins_chalgren_agar_plates_supplemented_with_10_human_blood_and_antibiotics.yaml"
)
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m2852_wilkins_chalgren_score15.py"
ACTION = "RESOLVED_TOGO_M2852_WILKINS_CHALGREN_SCORE15"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

EXPECTED_ID = "CultureMech:009395"
EXPECTED_MEDIA_TERM = "TOGO:M2852"

TOGO_M2852 = "https://togomedium.org/medium/M2852"
TOGO_M2852_API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2852"
BERNARDE_2010_DOI = "https://doi.org/10.1074/mcp.M110.001065"
BERNARDE_2010_PMID = "PMID:20610778"
REFERENCES = (TOGO_M2852, TOGO_M2852_API, BERNARDE_2010_DOI, BERNARDE_2010_PMID)

SOURCE = "TOGO M2852 / Bernarde et al. 2010"
TITLE = (
    "Wilkins-Chalgren agar plates (supplemented with 10% human blood "
    "and antibiotics)"
)

Component = tuple[str, str, str]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("vancomycin (Lilly France S.A., Fergesheim, France)", "1", "G_PER_L"),
    ("human blood", "10", "PERCENT_W_V"),
    ("cefsulodin (Takeda France S.A., Puteaux, France)", "5", "G_PER_L"),
    ("Fungizone (Bristol-Myers Squibb Co.)", "5", "G_PER_L"),
    ("trimethoprim (GlaxoSmithKline)", "1", "G_PER_L"),
    ("Carbon dioxide gas", "variable", "VARIABLE"),
    ("Nitrogen gas", "variable", "VARIABLE"),
    ("Oxygen gas", "variable", "VARIABLE"),
    (
        "Wilkins-Chalgren agar plates (Oxoid Ltd., Hampshire, UK)",
        "variable",
        "VARIABLE",
    ),
)

FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Wilkins-Chalgren agar plates (Oxoid)", "variable", "VARIABLE"),
    ("Human blood", "10", "PERCENT_V_V"),
    ("Vancomycin", "1.0", "MG_PER_ML"),
    ("Cefsulodin", "5.0", "MG_PER_ML"),
    ("Fungizone (Bristol-Myers Squibb Co.)", "5.0", "MG_PER_ML"),
    ("Trimethoprim", "1.0", "MG_PER_ML"),
    ("Oxygen gas", "5", "PERCENT_V_V"),
    ("Carbon dioxide gas", "10", "PERCENT_V_V"),
    ("Nitrogen gas", "85", "PERCENT_V_V"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Carbon dioxide gas": ("CHEBI:16526", "carbon dioxide"),
    "Cefsulodin": ("CHEBI:3507", "cefsulodin"),
    "Human blood": ("UBERON:0000178", "blood"),
    "Nitrogen gas": ("CHEBI:17997", "dinitrogen"),
    "Oxygen gas": ("CHEBI:15379", "dioxygen"),
    "Trimethoprim": ("CHEBI:45924", "trimethoprim"),
    "Vancomycin": ("CHEBI:28001", "vancomycin"),
}

NOTES = (
    "TOGO M2852 captures the Helicobacter pylori B38/J99 growth condition from "
    "Bernarde et al. 2010: commercial Oxoid Wilkins-Chalgren agar plates "
    "supplemented with 10% human blood, 1 mg/ml vancomycin, 5 mg/ml cefsulodin, "
    "5 mg/ml Fungizone, and 1 mg/ml trimethoprim, then incubated 48 h at 37 C "
    "under 5% O2, 10% CO2, and 85% N2."
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Use Oxoid Wilkins-Chalgren agar plates supplemented with 10% human blood."
        ),
    },
    {
        "step_number": 2,
        "action": "MIX",
        "description": (
            "Supplement the plates with 1 mg/ml vancomycin, 5 mg/ml cefsulodin, "
            "5 mg/ml Fungizone, and 1 mg/ml trimethoprim."
        ),
    },
)

TARGET_ORGANISMS: tuple[dict[str, Any], ...] = (
    {
        "preferred_term": "Helicobacter pylori",
        "term": {"id": "NCBITaxon:210", "label": "Helicobacter pylori"},
        "strain": "B38",
        "evidence": [
            {
                "reference": BERNARDE_2010_PMID,
                "supports": "SUPPORT",
                "snippet": "H. pylori B38 and J99 cells were cultured",
                "explanation": (
                    "Bernarde et al. 2010 directly reports growth of H. pylori "
                    "B38 for 48 h on this supplemented Wilkins-Chalgren agar "
                    "plate condition."
                ),
            }
        ],
    },
    {
        "preferred_term": "Helicobacter pylori",
        "term": {"id": "NCBITaxon:210", "label": "Helicobacter pylori"},
        "strain": "J99 (ATCC 700824)",
        "evidence": [
            {
                "reference": BERNARDE_2010_PMID,
                "supports": "SUPPORT",
                "snippet": "H. pylori B38 and J99 cells were cultured",
                "explanation": (
                    "Bernarde et al. 2010 directly reports growth of H. pylori "
                    "J99 for 48 h on this supplemented Wilkins-Chalgren agar "
                    "plate condition."
                ),
            }
        ],
    },
)

UNIT_LABELS = {
    "MG_PER_ML": "mg/ml",
    "PERCENT_V_V": "%",
    "VARIABLE": "variable",
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str | None = None,
    term: bool = True,
    cellular_metabolic_roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": (
            notes
            or f"{SOURCE} lists {value} {UNIT_LABELS[unit]} {preferred_term}."
        ),
    }
    if term:
        grounding = GROUNDINGS[preferred_term]
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    if cellular_metabolic_roles:
        row["cellular_metabolic_roles"] = list(cellular_metabolic_roles)
    return row


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "Wilkins-Chalgren agar plates (Oxoid)",
        "variable",
        "VARIABLE",
        notes=(
            "Bernarde et al. 2010 uses pre-poured Oxoid Wilkins-Chalgren agar "
            "plates; the commercial plate substrate is retained as an opaque "
            "unmapped product because the source does not disclose a per-liter "
            "mass or internal formulation."
        ),
        term=False,
    ),
    _ingredient(
        "Human blood",
        "10",
        "PERCENT_V_V",
        notes=(
            "Bernarde et al. 2010 supplements the Wilkins-Chalgren agar "
            "plates with 10% human blood."
        ),
    ),
    _ingredient(
        "Vancomycin",
        "1.0",
        "MG_PER_ML",
        notes=(
            "Bernarde et al. 2010 lists 1 mg/ml vancomycin from "
            "Lilly France S.A."
        ),
        cellular_metabolic_roles=("INHIBITOR",),
    ),
    _ingredient(
        "Cefsulodin",
        "5.0",
        "MG_PER_ML",
        notes=(
            "Bernarde et al. 2010 lists 5 mg/ml cefsulodin from "
            "Takeda France S.A."
        ),
        cellular_metabolic_roles=("INHIBITOR",),
    ),
    _ingredient(
        "Fungizone (Bristol-Myers Squibb Co.)",
        "5.0",
        "MG_PER_ML",
        notes=(
            "Bernarde et al. 2010 lists 5 mg/ml Fungizone from "
            "Bristol-Myers Squibb Co.; the branded product is retained "
            "unmapped because the source does not identify its active ingredient."
        ),
        term=False,
        cellular_metabolic_roles=("INHIBITOR",),
    ),
    _ingredient(
        "Trimethoprim",
        "1.0",
        "MG_PER_ML",
        notes=(
            "Bernarde et al. 2010 lists 1 mg/ml trimethoprim from "
            "GlaxoSmithKline."
        ),
        cellular_metabolic_roles=("INHIBITOR",),
    ),
    _ingredient(
        "Oxygen gas",
        "5",
        "PERCENT_V_V",
        notes=(
            "Bernarde et al. 2010 incubates the plates under microaerobic "
            "5% O2, 10% CO2, and 85% N2."
        ),
    ),
    _ingredient(
        "Carbon dioxide gas",
        "10",
        "PERCENT_V_V",
        notes=(
            "Bernarde et al. 2010 incubates the plates under microaerobic "
            "5% O2, 10% CO2, and 85% N2."
        ),
    ),
    _ingredient(
        "Nitrogen gas",
        "85",
        "PERCENT_V_V",
        notes=(
            "Bernarde et al. 2010 incubates the plates under microaerobic "
            "5% O2, 10% CO2, and 85% N2."
        ),
    ),
)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _signature(rows: list[dict[str, Any]], field: str) -> tuple[Component, ...]:
    signature: list[Component] = []
    for index, row in enumerate(rows):
        if not isinstance(row, dict):
            raise ValueError(f"{field}[{index}]: expected a mapping")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{field}[{index}]: missing concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"expected id {EXPECTED_ID}, found {doc.get('id')!r}")

    source_term = _source_term_id(doc)
    if source_term != EXPECTED_MEDIA_TERM:
        raise ValueError(
            f"expected media term {EXPECTED_MEDIA_TERM}, found {source_term!r}"
        )

    ingredient_signature = _signature(doc.get("ingredients") or [], "ingredients")
    if ingredient_signature not in {
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    }:
        raise ValueError(
            "ingredient signature drifted from the reviewed TOGO M2852 recipe"
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


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            "Curated TOGO M2852 from the official TOGO API payload and "
            "Bernarde et al. 2010; corrected imported atmosphere values to "
            "the 5:10:85 O2/CO2/N2 percentages and retained Wilkins-Chalgren "
            "agar plates and Fungizone as opaque source-level products."
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


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    _require_target(doc)

    repaired = copy.deepcopy(doc)

    for field in (
        "medium_type",
        "composition_type",
        "physical_state",
        "functional_role",
        "temperature_value",
        "incubation_atmosphere",
        "ingredients",
        "preparation_steps",
        "organism_culture_type",
        "target_organisms",
        "data_quality_flags",
        "references",
    ):
        repaired.pop(field, None)

    _put_after(repaired, "medium_type", "COMPLEX", "category")
    _put_after(repaired, "composition_type", "UNDEFINED", "medium_type")
    _put_after(repaired, "functional_role", ["SELECTIVE"], "composition_type")
    _put_after(repaired, "physical_state", "SOLID_AGAR", "functional_role")
    _put_after(repaired, "temperature_value", 37.0, "physical_state")
    _put_after(
        repaired,
        "incubation_atmosphere",
        "MICROAEROPHILIC",
        "temperature_value",
    )
    _put_after(
        repaired,
        "ingredients",
        copy.deepcopy(list(INGREDIENTS)),
        "incubation_atmosphere",
    )
    _put_after(repaired, "notes", NOTES, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        copy.deepcopy(list(PREPARATION_STEPS)),
        "applications",
    )
    _put_after(repaired, "organism_culture_type", "isolate", "curation_history")
    _put_after(
        repaired,
        "target_organisms",
        copy.deepcopy(list(TARGET_ORGANISMS)),
        "organism_culture_type",
    )
    _put_after(
        repaired,
        "data_quality_flags",
        ["ingredients_curated", "has_ontology_mappings", "has_unmapped_ingredients"],
        "target_organisms",
    )
    _put_after(
        repaired,
        "references",
        [{"reference": reference} for reference in REFERENCES],
        "data_quality_flags",
    )
    _append_curation_event(repaired)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    path = normalized / TARGET
    return {path: repair_record(_load(path))}


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
        print(f"{status} {path.relative_to(args.normalized_dir)}")

    action = "wrote" if args.apply else "would write"
    print(f"{action} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
