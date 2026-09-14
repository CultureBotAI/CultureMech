#!/usr/bin/env python3
"""Repair TOGO M1970/M1971/M1972 LB streptomycin/rifampicin media."""

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
LB_PARENT = Path("bacterial/lb_medium.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m1970_m1971_m1972_lb_streptomycin_rifampicin_score15.py"
ACTION = "RESOLVED_TOGO_M1970_M1971_M1972_LB_STREPTOMYCIN_RIFAMPICIN_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

LB_PARENT_ID = "CultureMech:008037"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class AntibioticStock:
    solution_name: str
    addition_ml: str
    component_name: str
    component_mg: str

    @property
    def imported_name(self) -> str:
        return f"{self.solution_name}*"

    @property
    def source_ml(self) -> str:
        return self.addition_ml.removesuffix(".0")

    @property
    def component_signature(self) -> tuple[Component, ...]:
        return ((self.component_name, self.component_mg, "MG_PER_ML"),)

    @property
    def final_signature(self) -> SolutionSignature:
        return (
            self.solution_name,
            self.addition_ml,
            "ML_PER_L",
            self.component_signature,
        )

    @property
    def imported_signature(self) -> SolutionSignature:
        return (self.imported_name, self.source_ml, "G_PER_L", ())


@dataclass(frozen=True)
class RecordSpec:
    target: Path
    expected_id: str
    expected_media_term: str
    original_name: str
    nbrc_no: str
    water_ml: str
    imported_solution_order: tuple[AntibioticStock, ...]
    final_solution_order: tuple[AntibioticStock, ...]

    @property
    def togo_id(self) -> str:
        return self.expected_media_term.removeprefix("TOGO:")

    @property
    def togo_url(self) -> str:
        return f"https://togomedium.org/medium/{self.togo_id}"

    @property
    def nbrc_url(self) -> str:
        return "https://www.nite.go.jp/nbrc/catalogue/" f"NBRCMediumDetailServlet?NO={self.nbrc_no}"

    @property
    def source(self) -> str:
        return f"TOGO {self.togo_id} / NBRC Medium {self.nbrc_no}"

    @property
    def imported_ingredient_signature(self) -> tuple[Component, ...]:
        return (
            ("Distilled water", self.water_ml, "G_PER_L"),
            ("Yeast extract", "5", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Bacto Tryptone (Difco)", "10", "G_PER_L"),
        )

    @property
    def imported_solution_signature(self) -> tuple[SolutionSignature, ...]:
        return tuple(stock.imported_signature for stock in self.imported_solution_order)

    @property
    def final_ingredient_signature(self) -> tuple[Component, ...]:
        return (
            ("Bacto Tryptone (Difco)", "10", "G_PER_L"),
            ("Yeast extract", "5", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Distilled water", self.water_ml, "ML_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
        )

    @property
    def final_solution_signature(self) -> tuple[SolutionSignature, ...]:
        return tuple(stock.final_signature for stock in self.final_solution_order)

    @property
    def added_solution_text(self) -> str:
        return _join_stock_phrases(
            [
                f"{stock.addition_ml} ml/L {stock.solution_name}"
                for stock in self.final_solution_order
            ]
        )

    @property
    def notes(self) -> str:
        return (
            f"TOGO {self.togo_id} imports NBRC Medium {self.nbrc_no} "
            f"{self.original_name}. NBRC {self.nbrc_no} lists the LB base "
            f"with {self.added_solution_text}, 15 g/L agar if needed, and "
            "pH 7.0."
        )

    @property
    def parent_media(self) -> dict[str, str]:
        return {
            "path": f"data/normalized_yaml/{LB_PARENT}",
            "relationship": "SUPPLEMENTED_VARIANT",
            "id": LB_PARENT_ID,
            "name": "lb_medium",
            "notes": (
                f"NBRC Medium {self.nbrc_no} supplements LB Medium with "
                f"separately filter-sterilized {self.added_solution_text}."
            ),
        }

    @property
    def variant_child(self) -> dict[str, str]:
        return {
            "path": f"data/normalized_yaml/{self.target}",
            "relationship": "SUPPLEMENTED_VARIANT",
            "id": self.expected_id,
            "name": self.target.stem,
            "notes": self.parent_media["notes"],
        }

    @property
    def variant_modifications(self) -> str:
        return f"Adds {self.added_solution_text} after separate filter " "sterilization."


STREPTOMYCIN = AntibioticStock(
    solution_name="Streptomycin solution (50 mg/ml)",
    addition_ml="10.0",
    component_name="Streptomycin",
    component_mg="50.0",
)
RIFAMPICIN = AntibioticStock(
    solution_name="Rifampicin solution (50 mg/ml)",
    addition_ml="5.0",
    component_name="Rifampicin",
    component_mg="50.0",
)

SPECS: tuple[RecordSpec, ...] = (
    RecordSpec(
        target=Path("bacterial/lb_streptomycin_medium.yaml"),
        expected_id="CultureMech:008552",
        expected_media_term="TOGO:M1970",
        original_name="LB + Streptomycin medium",
        nbrc_no="1248",
        water_ml="990",
        imported_solution_order=(STREPTOMYCIN,),
        final_solution_order=(STREPTOMYCIN,),
    ),
    RecordSpec(
        target=Path("bacterial/lb_rifampicin_medium.yaml"),
        expected_id="CultureMech:008553",
        expected_media_term="TOGO:M1971",
        original_name="LB + Rifampicin medium",
        nbrc_no="1249",
        water_ml="995",
        imported_solution_order=(RIFAMPICIN,),
        final_solution_order=(RIFAMPICIN,),
    ),
    RecordSpec(
        target=Path("bacterial/lb_streptomycin_rifampicin_medium.yaml"),
        expected_id="CultureMech:008554",
        expected_media_term="TOGO:M1972",
        original_name="LB + Streptomycin, Rifampicin medium",
        nbrc_no="1250",
        water_ml="985",
        imported_solution_order=(RIFAMPICIN, STREPTOMYCIN),
        final_solution_order=(STREPTOMYCIN, RIFAMPICIN),
    ),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Rifampicin": ("CHEBI:28077", "rifampicin"),
    "Streptomycin": ("CHEBI:17076", "streptomycin"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_ML": "mg/ml",
    "ML_PER_L": "ml/L",
}


def _join_stock_phrases(phrases: list[str]) -> str:
    if len(phrases) == 1:
        return phrases[0]
    return f"{', '.join(phrases[:-1])}, and {phrases[-1]}"


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
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def _ingredients(spec: RecordSpec) -> tuple[dict[str, Any], ...]:
    return (
        _component(
            "Bacto Tryptone (Difco)",
            "10",
            "G_PER_L",
            source=spec.source,
            notes=(
                f"NBRC Medium {spec.nbrc_no} lists Bacto Tryptone (Difco) "
                "as a source-disclosed digest product not reducible to one "
                "ChEBI molecule."
            ),
        ),
        _component("Yeast extract", "5", "G_PER_L", source=spec.source),
        _component("NaCl", "5", "G_PER_L", source=spec.source),
        _component("Distilled water", spec.water_ml, "ML_PER_L", source=spec.source),
        _component(
            "Agar (if needed)",
            "15",
            "G_PER_L",
            source=spec.source,
            notes=f"{spec.source} lists 15 g/L agar if needed.",
        ),
    )


def _solution(stock: AntibioticStock, spec: RecordSpec) -> dict[str, Any]:
    return {
        "preferred_term": stock.solution_name,
        "concentration": {"value": stock.addition_ml, "unit": "ML_PER_L"},
        "source": spec.source,
        "notes": (f"{spec.source} lists {stock.source_ml} ml/L {stock.solution_name}."),
        "term": _term(*GROUNDINGS[stock.component_name]),
        "mediaingredientmech_chebi_term": _term(*GROUNDINGS[stock.component_name]),
        "composition": [
            _component(
                stock.component_name,
                stock.component_mg,
                "MG_PER_ML",
                source=spec.source,
                notes=(
                    f"NBRC Medium {spec.nbrc_no} specifies this stock as "
                    f"{stock.component_mg.removesuffix('.0')} mg/ml "
                    f"{stock.component_name}."
                ),
            )
        ],
        "name": stock.solution_name,
        "preparation_notes": "Sterilize separately by filtration.",
    }


def _solutions(spec: RecordSpec) -> tuple[dict[str, Any], ...]:
    return tuple(_solution(stock, spec) for stock in spec.final_solution_order)


def _preparation_steps(spec: RecordSpec) -> tuple[dict[str, Any], ...]:
    stocks = _join_stock_phrases(
        [
            (f"{stock.component_mg.removesuffix('.0')} mg/ml " f"{stock.component_name.lower()}")
            for stock in spec.final_solution_order
        ]
    )
    additions = _join_stock_phrases(
        [
            f"{stock.addition_ml} ml/L filter-sterilized {stock.solution_name}"
            for stock in spec.final_solution_order
        ]
    )
    return (
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Prepare the LB base from 10 g/L Bacto Tryptone (Difco), "
                "5 g/L yeast extract, 5 g/L NaCl, "
                f"{spec.water_ml} ml/L distilled water, and 15 g/L agar if "
                "needed."
            ),
        },
        {
            "step_number": 2,
            "action": "FILTER_STERILIZE",
            "description": f"Sterilize the {stocks} stocks separately by filtration.",
        },
        {
            "step_number": 3,
            "action": "MIX",
            "description": f"Add {additions} to the LB base.",
        },
    )


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
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_signature(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signature: list[SolutionSignature] = []
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
                _signature(row.get("composition"), f"{label} composition"),
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


def _ensure_target(doc: dict[str, Any], spec: RecordSpec) -> None:
    if doc.get("id") != spec.expected_id:
        raise ValueError(f"{spec.target}: expected {spec.expected_id}, found {doc.get('id')}")
    if _source_term_id(doc) != spec.expected_media_term:
        raise ValueError(f"{spec.target}: expected media term {spec.expected_media_term}")
    if _signature(doc.get("ingredients"), "ingredients") not in (
        spec.imported_ingredient_signature,
        spec.final_ingredient_signature,
    ):
        raise ValueError(f"{spec.target}: ingredient signature drifted")
    if _solution_signature(doc.get("solutions"), "solutions") not in (
        spec.imported_solution_signature,
        spec.final_solution_signature,
    ):
        raise ValueError(f"{spec.target}: solution signature drifted")


def _ensure_lb_parent(doc: dict[str, Any]) -> None:
    if doc.get("id") != LB_PARENT_ID:
        raise ValueError(f"{LB_PARENT}: expected {LB_PARENT_ID}, found {doc.get('id')}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation", "resolved_reference"):
        while obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], spec: RecordSpec) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (spec.togo_url, spec.nbrc_url):
        if reference not in existing:
            references.append({"reference": reference})


def _append_event(doc: dict[str, Any], spec: RecordSpec) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": f"{spec.togo_url}; {spec.nbrc_url}",
        "notes": (
            f"{spec.notes} Corrected the imported distilled-water row from a "
            "g/L artifact to NBRC's ml/L volume and nested the separately "
            "filter-sterilized 50 mg/ml antibiotic stocks."
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


def _replace_variant_child(
    doc: dict[str, Any],
    child: dict[str, Any],
) -> None:
    children = [
        row
        for row in doc.get("variant_children", [])
        if not (isinstance(row, dict) and row.get("id") == child["id"])
    ]
    children.append(copy.deepcopy(child))
    doc["variant_children"] = children


def repair_target(doc: dict[str, Any], spec: RecordSpec) -> dict[str, Any]:
    _ensure_target(doc, spec)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired["ph_value"] = 7.0
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(_ingredients(spec)))
    repaired["solutions"] = copy.deepcopy(list(_solutions(spec)))
    repaired["notes"] = spec.notes
    repaired["preparation_steps"] = copy.deepcopy(list(_preparation_steps(spec)))
    repaired["parent_media"] = copy.deepcopy(spec.parent_media)
    repaired["variant_relationship"] = "SUPPLEMENTED_VARIANT"
    repaired["variant_modifications"] = [spec.variant_modifications]
    _ensure_flags(repaired)
    _ensure_references(repaired, spec)
    _append_event(repaired, spec)
    return repaired


def repair_lb_parent(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_lb_parent(doc)
    repaired = copy.deepcopy(doc)
    for spec in SPECS:
        _replace_variant_child(repaired, spec.variant_child)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans = {
        normalized / spec.target: repair_target(_load(normalized / spec.target), spec)
        for spec in SPECS
    }
    lb_parent_path = normalized / LB_PARENT
    plans[lb_parent_path] = repair_lb_parent(_load(lb_parent_path))
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
