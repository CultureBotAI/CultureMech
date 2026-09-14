#!/usr/bin/env python3
"""Repair Halomarina and JCM 703 score-15 archaeal media."""

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

TOGO_M1943 = "https://togomedium.org/medium/M1943"
NBRC_1214 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1214"
JCM_703 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=703"
TOGO_M725 = "https://togomedium.org/medium/M725"
TOGO_M142 = "https://togomedium.org/medium/M142"
TOGO_M190 = "https://togomedium.org/medium/M190"

SOURCE_NBRC_1214 = "NBRC Medium 1214"
SOURCE_JCM_703 = "JCM Medium 703 / TOGO M725"
SOURCE_M142 = "TOGO M142 trace minerals"
SOURCE_M190 = "TOGO M190 trace vitamins"

CURATOR = "repair_halomarina_jcm703_score15.py"
ACTION = "RESOLVED_HALOMARINA_JCM703_SCORE15"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
    "L": "L",
    "VARIABLE": "variable",
}

RECIPE_FIELDS = (
    "medium_type",
    "composition_type",
    "physical_state",
    "ph_value",
    "ph_range",
    "temperature_value",
    "temperature_range",
    "ingredients",
    "solutions",
    "preparation_steps",
    "sterilization",
)


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    source_term: str
    recipe: dict[str, Any]
    references: tuple[str, ...]
    notes: str
    accepted_signatures: frozenset[frozenset[str]]
    flags: tuple[str, ...]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str | None = None,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _solution(
    preferred_term: str,
    value: str,
    *,
    source: str,
    notes: str,
    composition: list[dict[str, Any]],
) -> dict[str, Any]:
    return {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
        "composition": copy.deepcopy(composition),
    }


def _source_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} prints this component in its stock solution.",
        term=term,
    )


def _halomarina_recipe() -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "SOLID_AGAR",
        "ph_value": 7.5,
        "ingredients": [
            _component(
                "Casamino acids",
                "1.0",
                "G_PER_L",
                source=SOURCE_NBRC_1214,
                term=("FOODON:03315719", "mammalian milk protein (hydrolyzed)"),
            ),
            _component(
                "Bacto Yeast Extract (Difco)",
                "1.0",
                "G_PER_L",
                source=SOURCE_NBRC_1214,
                term=("FOODON:03315426", "yeast extract"),
            ),
            _component(
                "NaCl",
                "150.0",
                "G_PER_L",
                source=SOURCE_NBRC_1214,
                term=("CHEBI:26710", "sodium chloride"),
            ),
            _component(
                "Agar",
                "15.0",
                "G_PER_L",
                source=SOURCE_NBRC_1214,
                term=("CHEBI:2509", "agar"),
            ),
            _component(
                "Artificial seawater",
                "1.0",
                "L",
                source=SOURCE_NBRC_1214,
                notes=(
                    "NBRC Medium 1214 lists artificial seawater as the "
                    "solvating medium for the Halomarina medium recipe."
                ),
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Prepare the medium from 1 g Casamino acids, 1 g Bacto Yeast "
                    "Extract, 150 g NaCl, 15 g agar, and 1 L artificial seawater."
                ),
            },
            {
                "step_number": 2,
                "action": "ADJUST_PH",
                "description": "Adjust pH to 7.5.",
            },
        ],
    }


def _m142_trace_minerals() -> list[dict[str, Any]]:
    return [
        _source_component(
            "MgSO4 x 7H2O",
            "3",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:31795", "magnesium sulfate heptahydrate"),
        ),
        _source_component(
            "NaCl",
            "1",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:26710", "sodium chloride"),
        ),
        _source_component(
            "CaCl2 x 2H2O",
            "0.1",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:86158", "calcium chloride dihydrate"),
        ),
        _source_component(
            "Na2MoO4 x 2H2O",
            "0.01",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:75213", "sodium molybdate dihydrate"),
        ),
        _source_component(
            "H3BO3",
            "0.01",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:33118", "boric acid"),
        ),
        _source_component(
            "FeSO4 x 7H2O",
            "0.1",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        ),
        _source_component(
            "ZnSO4 x 7H2O",
            "0.1",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:32312", "zinc sulfate heptahydrate"),
        ),
        _source_component(
            "CuSO4 x 5H2O",
            "0.01",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:31440", "copper(II) sulfate pentahydrate"),
        ),
        _source_component(
            "CoSO4 x 7H2O",
            "0.1",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
        ),
        _source_component(
            "Nitrilotriacetic acid",
            "1.5",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:44557", "nitrilotriacetic acid"),
        ),
        _source_component(
            "MnSO4 x n H2O",
            "0.5",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:86360", "manganese(II) sulfate hydrate"),
        ),
        _source_component(
            "AlK(SO4)2",
            "0.01",
            "G_PER_L",
            source=SOURCE_M142,
            term=("CHEBI:86463", "potassium aluminium sulfate"),
        ),
        _source_component(
            "KOH solution",
            "variable",
            "VARIABLE",
            source=SOURCE_M142,
            term=("CHEBI:32035", "potassium hydroxide"),
        ),
    ]


def _m190_trace_vitamins() -> list[dict[str, Any]]:
    return [
        _source_component(
            "Biotin",
            "0.002",
            "G_PER_L",
            source=SOURCE_M190,
            term=("CHEBI:15956", "biotin"),
        ),
        _source_component(
            "p-Aminobenzoic acid",
            "0.005",
            "G_PER_L",
            source=SOURCE_M190,
            term=("CHEBI:30753", "4-aminobenzoic acid"),
        ),
        _source_component(
            "Thiamine-HCl",
            "0.005",
            "G_PER_L",
            source=SOURCE_M190,
            term=("CHEBI:49105", "thiamine hydrochloride"),
        ),
        _source_component(
            "Calcium pantothenate",
            "0.005",
            "G_PER_L",
            source=SOURCE_M190,
            term=("CHEBI:31345", "Calcium pantothenate"),
        ),
        _source_component(
            "Pyridoxine-HCl",
            "0.01",
            "G_PER_L",
            source=SOURCE_M190,
            term=("CHEBI:30961", "pyridoxine hydrochloride"),
        ),
        _source_component(
            "Folic acid",
            "0.002",
            "G_PER_L",
            source=SOURCE_M190,
            term=("CHEBI:27470", "folic acid"),
        ),
        _source_component(
            "Vitamin B12",
            "0.0001",
            "G_PER_L",
            source=SOURCE_M190,
            term=("CHEBI:176843", "vitamin B12"),
        ),
        _source_component(
            "Riboflavin",
            "0.005",
            "G_PER_L",
            source=SOURCE_M190,
            term=("CHEBI:17015", "riboflavin"),
        ),
        _source_component(
            "Nicotinic acid",
            "0.005",
            "G_PER_L",
            source=SOURCE_M190,
            term=("CHEBI:15940", "nicotinic acid"),
        ),
        _source_component(
            "Lipoic acid",
            "0.005",
            "G_PER_L",
            source=SOURCE_M190,
            term=("CHEBI:16494", "lipoic acid"),
        ),
    ]


def _jcm703_recipe() -> dict[str, Any]:
    return {
        "medium_type": "COMPLEX",
        "composition_type": "UNDEFINED",
        "physical_state": "LIQUID",
        "ph_value": 7.0,
        "ingredients": [
            _component(
                "Distilled water",
                "1",
                "L",
                source=SOURCE_JCM_703,
                term=("CHEBI:15377", "water"),
            ),
            _component(
                "Yeast extract",
                "0.5",
                "G_PER_L",
                source=SOURCE_JCM_703,
                term=("FOODON:03315426", "yeast extract"),
            ),
            _component(
                "NaCl",
                "0.6",
                "G_PER_L",
                source=SOURCE_JCM_703,
                term=("CHEBI:26710", "sodium chloride"),
            ),
            _component(
                "CaCl2 x 2H2O",
                "0.1",
                "G_PER_L",
                source=SOURCE_JCM_703,
                term=("CHEBI:86158", "calcium chloride dihydrate"),
            ),
            _component(
                "KH2PO4",
                "0.3",
                "G_PER_L",
                source=SOURCE_JCM_703,
                term=("CHEBI:63036", "potassium dihydrogen phosphate"),
            ),
            _component(
                "NH4Cl",
                "1",
                "G_PER_L",
                source=SOURCE_JCM_703,
                term=("CHEBI:31206", "ammonium chloride"),
            ),
            _component(
                "K2HPO4",
                "0.3",
                "G_PER_L",
                source=SOURCE_JCM_703,
                term=("CHEBI:131527", "dipotassium hydrogen phosphate"),
            ),
            _component(
                "Resazurin",
                "0.5",
                "MG_PER_L",
                source=SOURCE_JCM_703,
                term=("CHEBI:8806", "Resazurin"),
            ),
            _component(
                "MgCl2 x 6H2O",
                "0.2",
                "G_PER_L",
                source=SOURCE_JCM_703,
                term=("CHEBI:86345", "magnesium dichloride hexahydrate"),
            ),
            _component(
                "KCl",
                "0.1",
                "G_PER_L",
                source=SOURCE_JCM_703,
                term=("CHEBI:32588", "potassium chloride"),
            ),
            _component(
                "Sodium acetate",
                "0.5",
                "G_PER_L",
                source=SOURCE_JCM_703,
                term=("CHEBI:32954", "sodium acetate"),
            ),
            _component(
                "L-Cysteine x HCl x H2O",
                "0.5",
                "G_PER_L",
                source=SOURCE_JCM_703,
                term=("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
            ),
            _component(
                "Sodium formate",
                "0.3",
                "PERCENT_W_V",
                source=SOURCE_JCM_703,
                notes=(
                    "JCM Medium 703 supplements JCM Medium 702 with 0.3% "
                    "final sodium formate."
                ),
                term=("CHEBI:62965", "sodium formate"),
            ),
            _component(
                "CO2",
                "variable",
                "VARIABLE",
                source=SOURCE_JCM_703,
                notes="JCM Medium 703 uses an N2-CO2 gas phase at 80:20 by volume.",
                term=("CHEBI:16526", "carbon dioxide"),
            ),
            _component(
                "N2",
                "variable",
                "VARIABLE",
                source=SOURCE_JCM_703,
                notes="JCM Medium 703 uses an N2-CO2 gas phase at 80:20 by volume.",
                term=("CHEBI:17997", "dinitrogen"),
            ),
        ],
        "solutions": [
            _solution(
                "Trace minerals (TOGO Medium M142)",
                "10",
                source=SOURCE_JCM_703,
                notes=(
                    "JCM Medium 703 / TOGO M725 adds 10 ml/L Trace minerals "
                    "from TOGO M142."
                ),
                composition=_m142_trace_minerals(),
            ),
            _solution(
                "Trace vitamins (TOGO Medium M190)",
                "10",
                source=SOURCE_JCM_703,
                notes=(
                    "JCM Medium 703 / TOGO M725 adds 10 ml/L Trace vitamins "
                    "from TOGO M190."
                ),
                composition=_m190_trace_vitamins(),
            ),
            _solution(
                "8% NaHCO3 solution",
                "25",
                source=SOURCE_JCM_703,
                notes="JCM Medium 703 / TOGO M725 adds 25 ml/L 8% NaHCO3 solution.",
                composition=[
                    _source_component(
                        "NaHCO3",
                        "80",
                        "G_PER_L",
                        source=SOURCE_JCM_703,
                        term=("CHEBI:32139", "sodium hydrogencarbonate"),
                    )
                ],
            ),
            _solution(
                "3% Na2S x 9H2O solution",
                "10",
                source=SOURCE_JCM_703,
                notes=(
                    "JCM Medium 703 / TOGO M725 adds 10 ml/L 3% Na2S x "
                    "9H2O solution."
                ),
                composition=[
                    _source_component(
                        "Na2S x 9H2O",
                        "30",
                        "G_PER_L",
                        source=SOURCE_JCM_703,
                        term=("CHEBI:76209", "sodium sulfide nonahydrate"),
                    )
                ],
            ),
        ],
        "preparation_steps": [
            {
                "step_number": 1,
                "action": "MIX",
                "description": (
                    "Mix the base components except NaHCO3, Na2S x 9H2O, "
                    "and trace vitamins."
                ),
            },
            {
                "step_number": 2,
                "action": "HEAT",
                "description": (
                    "Bring the medium to a boil for several seconds and cool "
                    "under N2-CO2 (80:20, v/v)."
                ),
            },
            {
                "step_number": 3,
                "action": "AUTOCLAVE",
                "description": (
                    "Distribute under N2-CO2, seal with butyl rubber stoppers, "
                    "and autoclave."
                ),
            },
            {
                "step_number": 4,
                "action": "MIX",
                "description": (
                    "Add the sterile NaHCO3, Na2S x 9H2O, and trace vitamin "
                    "solutions per liter."
                ),
            },
            {
                "step_number": 5,
                "action": "ADJUST_PH",
                "description": "Check pH of the medium to be about 7.0.",
            },
            {
                "step_number": 6,
                "action": "MIX",
                "description": (
                    "Pressurize inoculated bottles to 200 kPa with N2-CO2 "
                    "(80:20, v/v)."
                ),
            },
        ],
    }


def _signature(recipe: dict[str, Any]) -> frozenset[str]:
    return frozenset(
        str(row.get("preferred_term") or "")
        for key in ("ingredients", "solutions")
        for row in recipe.get(key, [])
        if isinstance(row, dict)
    )


HALOMARINA_RECIPE = _halomarina_recipe()
JCM703_RECIPE = _jcm703_recipe()

TARGET_BY_PATH: dict[str, Target] = {
    "archaea/halomarina_medium.yaml": Target(
        path="archaea/halomarina_medium.yaml",
        record_id="CultureMech:008522",
        source_term="TOGO:M1943",
        recipe=HALOMARINA_RECIPE,
        references=(TOGO_M1943, NBRC_1214),
        notes=(
            "NBRC Medium 1214 records Halomarina medium as 1 g "
            "Casamino acids, 1 g Bacto Yeast Extract (Difco), 150 g NaCl, "
            "15 g agar, and 1 L artificial seawater adjusted to pH 7.5."
        ),
        accepted_signatures=frozenset(
            {
                frozenset(
                    {
                        "NaCl",
                        "Artificial seawater",
                        "Agar",
                        "Bacto Yeast Extract (Difco)",
                        "Casamino acids",
                    }
                )
            }
        ),
        flags=(
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        ),
    ),
    "archaea/methanobacterium_medium_ii_with_formae.yaml": Target(
        path="archaea/methanobacterium_medium_ii_with_formae.yaml",
        record_id="CultureMech:003049",
        source_term="mediadive.medium:J703",
        recipe=JCM703_RECIPE,
        references=(JCM_703, TOGO_M725, TOGO_M142, TOGO_M190),
        notes=(
            "JCM Medium 703 was recovered from source-equivalent TOGO M725; "
            "the recipe uses JCM Medium 702 supplemented with 0.3% final sodium "
            "formate and 10 ml/L Trace minerals from M142, 10 ml/L Trace "
            "vitamins from M190, 25 ml/L 8% NaHCO3, and 10 ml/L 3% "
            "Na2S x 9H2O."
        ),
        accepted_signatures=frozenset(
            {
                frozenset(
                    {
                        "Distilled water",
                        "Yeast extract",
                        "NaCl",
                        "CaCl2\u30fb2H2O",
                        "KH2PO4",
                        "NH4Cl",
                        "K2HPO4",
                        "Resazurin",
                        "MgCl2\u30fb6H2O",
                        "KCl",
                        "Sodium acetate",
                        "L-Cysteine\u30fbHCl\u30fbH2O",
                        "sodium formate",
                        "Carbon dioxide gas",
                        "Nitrogen gas",
                        "Trace minerals (see Medium [M142])",
                        "Trace vitamins (see Medium [M190])",
                        "8% NaHCO3 solution*",
                        "3% Na2S\u30fb9H2O solution",
                    }
                ),
                _signature(JCM703_RECIPE),
            }
        ),
        flags=("has_ontology_mappings", "ingredients_curated"),
    ),
}
TARGETS = tuple(TARGET_BY_PATH.values())


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


def _top_level_signature(doc: dict[str, Any]) -> frozenset[str]:
    return frozenset(
        str(row.get("preferred_term") or "")
        for key in ("ingredients", "solutions")
        for row in doc.get(key) or []
        if isinstance(row, dict)
    )


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
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

    signature = _top_level_signature(doc)
    if signature not in target.accepted_signatures:
        raise ValueError(f"{target.path}: component signature drifted")


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {
        row.get("reference") for row in references if isinstance(row, dict)
    }
    for url in target.references:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
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
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _ensure_target(doc, target)

    repaired = copy.deepcopy(doc)
    for recipe_field in RECIPE_FIELDS:
        if recipe_field in target.recipe:
            repaired[recipe_field] = copy.deepcopy(target.recipe[recipe_field])
        else:
            repaired.pop(recipe_field, None)
    repaired["notes"] = target.notes
    repaired["data_quality_flags"] = list(target.flags)
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
