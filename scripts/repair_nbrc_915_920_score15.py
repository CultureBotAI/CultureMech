#!/usr/bin/env python3
"""Repair the score-15 NBRC Medium 915-920 TOGO antibiotic-stock imports."""

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

PARENT = Path("bacterial/togo_medium_m1708.yaml")
PARENT_ID = "CultureMech:008270"
PARENT_MEDIA_TERM = "TOGO:M1708"

CURATOR = "repair_nbrc_915_920_score15.py"
ACTION = "RESOLVED_NBRC_915_920_SCORE15"
LINK_ACTION = "LINKED_NBRC_915_920_VARIANTS"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

BACTO_TRYPTONE = "Bacto Tryptone (Difco)"
YEAST_EXTRACT = "Yeast extract"
CALCIUM_CHLORIDE = "CaCl2\u00b72H2O"
DISTILLED_WATER = "Distilled water"
AGAR_IF_NEEDED = "Agar (if needed)"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class AntibioticStock:
    solution_name: str
    component_name: str
    grounding: tuple[str, str]

    @property
    def imported_name(self) -> str:
        return f"{self.solution_name} (500 \u03bcg/ml)*"

    @property
    def final_name(self) -> str:
        return f"{self.solution_name} (500 ug/ml)"

    @property
    def component_signature(self) -> tuple[Component, ...]:
        return ((self.component_name, "0.5", "MG_PER_ML"),)

    @property
    def imported_signature(self) -> SolutionSignature:
        return (self.imported_name, "100", "G_PER_L", ())

    @property
    def final_signature(self) -> SolutionSignature:
        return (self.final_name, "100", "ML_PER_L", self.component_signature)


@dataclass(frozen=True)
class RecordSpec:
    target: Path
    expected_id: str
    expected_media_term: str
    nbrc_no: str
    water_ml: str
    imported_solution_order: tuple[AntibioticStock, ...]
    final_solution_order: tuple[AntibioticStock, ...]
    relationship: str | None = None
    variant_notes: str | None = None

    @property
    def togo_id(self) -> str:
        return self.expected_media_term.removeprefix("TOGO:")

    @property
    def togo_url(self) -> str:
        return f"https://togomedium.org/medium/{self.togo_id}"

    @property
    def nbrc_url(self) -> str:
        return f"https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO={self.nbrc_no}"

    @property
    def source(self) -> str:
        return f"TOGO {self.togo_id} / NBRC Medium {self.nbrc_no}"

    @property
    def imported_ingredient_signature(self) -> tuple[Component, ...]:
        return (
            (DISTILLED_WATER, self.water_ml, "G_PER_L"),
            (YEAST_EXTRACT, "3", "G_PER_L"),
            (CALCIUM_CHLORIDE, "0.87", "G_PER_L"),
            (AGAR_IF_NEEDED, "15", "G_PER_L"),
            (BACTO_TRYPTONE, "5", "G_PER_L"),
        )

    @property
    def imported_solution_signature(self) -> tuple[SolutionSignature, ...]:
        return tuple(stock.imported_signature for stock in self.imported_solution_order)

    @property
    def final_ingredient_signature(self) -> tuple[Component, ...]:
        return (
            (BACTO_TRYPTONE, "5", "G_PER_L"),
            (YEAST_EXTRACT, "3", "G_PER_L"),
            (CALCIUM_CHLORIDE, "0.87", "G_PER_L"),
            (DISTILLED_WATER, self.water_ml, "ML_PER_L"),
            (AGAR_IF_NEEDED, "15", "G_PER_L"),
        )

    @property
    def final_solution_signature(self) -> tuple[SolutionSignature, ...]:
        return tuple(stock.final_signature for stock in self.final_solution_order)

    @property
    def references(self) -> tuple[str, str]:
        return (self.togo_url, self.nbrc_url)

    @property
    def solution_names(self) -> list[str]:
        return [stock.final_name for stock in self.final_solution_order]

    @property
    def solution_text(self) -> str:
        return _join([f"100 ml/L {name}" for name in self.solution_names])

    @property
    def notes(self) -> str:
        return (
            f"TOGO {self.togo_id} imports NBRC Medium {self.nbrc_no}, which "
            f"lists 5 g/L {BACTO_TRYPTONE}, 3 g/L Yeast extract, 0.87 g/L "
            f"CaCl2\u00b72H2O, {self.solution_text}, {self.water_ml} ml/L "
            "Distilled water, and 15 g/L Agar if needed at pH 7.0. The "
            "antibiotic stock solution(s) are sterilized separately by "
            "filtration."
        )

    @property
    def parent_media(self) -> dict[str, str]:
        if self.relationship is None or self.variant_notes is None:
            raise ValueError(f"{self.target}: parent record has no parent_media")
        return {
            "path": f"data/normalized_yaml/{PARENT}",
            "relationship": self.relationship,
            "id": PARENT_ID,
            "name": PARENT.stem,
            "notes": self.variant_notes,
        }

    @property
    def variant_child(self) -> dict[str, str]:
        if self.relationship is None or self.variant_notes is None:
            raise ValueError(f"{self.target}: parent record has no variant child")
        return {
            "path": f"data/normalized_yaml/{self.target}",
            "relationship": self.relationship,
            "id": self.expected_id,
            "name": self.target.stem,
            "notes": self.variant_notes,
        }


RIFAMPICIN = AntibioticStock(
    "Rifampicin solution",
    "Rifampicin",
    ("CHEBI:28077", "rifampicin"),
)
SPECTINOMYCIN = AntibioticStock(
    "Spectinomycin solution",
    "Spectinomycin",
    ("CHEBI:9215", "spectinomycin"),
)
KANAMYCIN = AntibioticStock(
    "Kanamycin solution",
    "Kanamycin",
    ("CHEBI:6104", "kanamycin"),
)

SPECS: tuple[RecordSpec, ...] = (
    RecordSpec(
        target=Path("bacterial/togo_medium_m1708.yaml"),
        expected_id=PARENT_ID,
        expected_media_term=PARENT_MEDIA_TERM,
        nbrc_no="915",
        water_ml="800",
        imported_solution_order=(RIFAMPICIN, SPECTINOMYCIN),
        final_solution_order=(RIFAMPICIN, SPECTINOMYCIN),
    ),
    RecordSpec(
        target=Path("bacterial/togo_medium_m1709.yaml"),
        expected_id="CultureMech:008271",
        expected_media_term="TOGO:M1709",
        nbrc_no="916",
        water_ml="900",
        imported_solution_order=(SPECTINOMYCIN,),
        final_solution_order=(SPECTINOMYCIN,),
        relationship="OMITTED_COMPONENT_VARIANT",
        variant_notes=(
            "Omits the 100 ml/L Rifampicin solution from TOGO M1708 and "
            "increases water from 800 to 900 ml/L."
        ),
    ),
    RecordSpec(
        target=Path("bacterial/togo_medium_m1710.yaml"),
        expected_id="CultureMech:008273",
        expected_media_term="TOGO:M1710",
        nbrc_no="917",
        water_ml="800",
        imported_solution_order=(RIFAMPICIN, KANAMYCIN),
        final_solution_order=(KANAMYCIN, RIFAMPICIN),
        relationship="SUBSTITUTED_COMPONENT_VARIANT",
        variant_notes=(
            "Substitutes 100 ml/L Kanamycin solution for the 100 ml/L "
            "Spectinomycin solution in TOGO M1708."
        ),
    ),
    RecordSpec(
        target=Path("bacterial/togo_medium_m1711.yaml"),
        expected_id="CultureMech:008274",
        expected_media_term="TOGO:M1711",
        nbrc_no="918",
        water_ml="700",
        imported_solution_order=(RIFAMPICIN, KANAMYCIN, SPECTINOMYCIN),
        final_solution_order=(KANAMYCIN, RIFAMPICIN, SPECTINOMYCIN),
        relationship="SUPPLEMENTED_VARIANT",
        variant_notes=(
            "Adds 100 ml/L Kanamycin solution to TOGO M1708 and decreases "
            "water from 800 to 700 ml/L."
        ),
    ),
    RecordSpec(
        target=Path("bacterial/togo_medium_m1712.yaml"),
        expected_id="CultureMech:008275",
        expected_media_term="TOGO:M1712",
        nbrc_no="919",
        water_ml="900",
        imported_solution_order=(RIFAMPICIN,),
        final_solution_order=(RIFAMPICIN,),
        relationship="OMITTED_COMPONENT_VARIANT",
        variant_notes=(
            "Omits the 100 ml/L Spectinomycin solution from TOGO M1708 and "
            "increases water from 800 to 900 ml/L."
        ),
    ),
    RecordSpec(
        target=Path("bacterial/togo_medium_m1713.yaml"),
        expected_id="CultureMech:008276",
        expected_media_term="TOGO:M1713",
        nbrc_no="920",
        water_ml="900",
        imported_solution_order=(KANAMYCIN,),
        final_solution_order=(KANAMYCIN,),
        relationship="SUBSTITUTED_COMPONENT_VARIANT",
        variant_notes=(
            "Substitutes 100 ml/L Kanamycin solution for the rifampicin and "
            "spectinomycin stock pair in TOGO M1708 and increases water from "
            "800 to 900 ml/L."
        ),
    ),
)

CHILD_SPECS = SPECS[1:]

GROUNDINGS: dict[str, tuple[str, str]] = {
    AGAR_IF_NEEDED: ("CHEBI:2509", "agar"),
    CALCIUM_CHLORIDE: ("CHEBI:86158", "calcium chloride dihydrate"),
    DISTILLED_WATER: ("CHEBI:15377", "water"),
    KANAMYCIN.component_name: KANAMYCIN.grounding,
    RIFAMPICIN.component_name: RIFAMPICIN.grounding,
    SPECTINOMYCIN.component_name: SPECTINOMYCIN.grounding,
    YEAST_EXTRACT: ("FOODON:03315426", "yeast extract"),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    AGAR_IF_NEEDED: ("SOLIDIFYING_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_ML": "mg/ml",
    "ML_PER_L": "ml/L",
}


def _join(items: list[str]) -> str:
    if len(items) == 1:
        return items[0]
    return f"{', '.join(items[:-1])}, and {items[-1]}"


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
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_signatures(rows: Any, label: str) -> tuple[SolutionSignature, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError(f"{label} is not a list")

    signatures: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError(f"{label} contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"{label} row {row.get('preferred_term')!r} lacks concentration")
        signatures.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(row.get("composition"), f"{label} composition"),
            )
        )
    return tuple(signatures)


def _notes(spec: RecordSpec, preferred_term: str, value: str, unit: str) -> str:
    if preferred_term == BACTO_TRYPTONE:
        return (
            f"{spec.source} lists 5 g/L Bacto Tryptone (Difco); this "
            "commercial peptone is retained as a source-disclosed complex "
            "digest."
        )
    if preferred_term == AGAR_IF_NEEDED:
        return f"{spec.source} lists {value} {UNIT_LABELS[unit]} agar if needed."
    return f"{spec.source} lists {value} {UNIT_LABELS[unit]} {preferred_term}."


def _component(
    spec: RecordSpec,
    preferred_term: str,
    value: str,
    unit: str,
    *,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": spec.source,
        "notes": notes or _notes(spec, preferred_term, value, unit),
    }
    grounding = GROUNDINGS.get(preferred_term)
    if grounding is not None:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles is not None:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _ingredients(spec: RecordSpec) -> list[dict[str, Any]]:
    return [
        _component(spec, name, value, unit) for name, value, unit in spec.final_ingredient_signature
    ]


def _stock(spec: RecordSpec, stock: AntibioticStock) -> dict[str, Any]:
    return {
        "preferred_term": stock.final_name,
        "concentration": {"value": "100", "unit": "ML_PER_L"},
        "source": spec.source,
        "notes": f"{spec.source} lists 100 ml/L {stock.final_name}.",
        "term": _term(*stock.grounding),
        "mediaingredientmech_chebi_term": _term(*stock.grounding),
        "composition": [
            _component(
                spec,
                stock.component_name,
                "0.5",
                "MG_PER_ML",
                notes=(
                    f"NBRC Medium {spec.nbrc_no} specifies this stock as "
                    f"500 ug/ml {stock.component_name}."
                ),
            )
        ],
        "name": stock.final_name,
        "preparation_notes": "Sterilize separately by filtration.",
    }


def _solutions(spec: RecordSpec) -> list[dict[str, Any]]:
    return [_stock(spec, stock) for stock in spec.final_solution_order]


def _preparation_steps(spec: RecordSpec) -> list[dict[str, Any]]:
    return [
        {
            "step_number": 1,
            "action": "MIX",
            "description": (
                "Combine 5 g/L Bacto Tryptone (Difco), 3 g/L Yeast extract, "
                f"0.87 g/L CaCl2\u00b72H2O, and {spec.water_ml} ml/L "
                "Distilled water."
            ),
        },
        {
            "step_number": 2,
            "action": "MIX",
            "description": f"Add 15 g/L agar when solid NBRC Medium {spec.nbrc_no} is needed.",
        },
        {
            "step_number": 3,
            "action": "FILTER_STERILIZE",
            "description": (f"Sterilize {_join(spec.solution_names)} separately by filtration."),
        },
        {
            "step_number": 4,
            "action": "MIX",
            "description": (
                "Add "
                f"{_join([f'100 ml/L filter-sterilized {name}' for name in spec.solution_names])}."
            ),
        },
        {
            "step_number": 5,
            "action": "ADJUST_PH",
            "description": "Adjust pH to 7.0.",
        },
    ]


def _ensure_record(doc: dict[str, Any], spec: RecordSpec) -> None:
    if doc.get("id") != spec.expected_id:
        raise ValueError(f"{spec.target}: expected id {spec.expected_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != spec.expected_media_term:
        raise ValueError(f"{spec.target}: expected media term {spec.expected_media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in {
        spec.imported_ingredient_signature,
        spec.final_ingredient_signature,
    }:
        raise ValueError(f"{spec.target}: ingredient signature drifted to {ingredient_signature!r}")

    solution_signatures = _solution_signatures(doc.get("solutions"), "solutions")
    if solution_signatures not in {
        spec.imported_solution_signature,
        spec.final_solution_signature,
    }:
        raise ValueError(f"{spec.target}: solution signature drifted to {solution_signatures!r}")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag for flag in flags if flag not in {"incomplete_composition", "needs_manual_curation"}
    ]
    flags.extend(("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], spec: RecordSpec) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in spec.references:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _append_curation_event(
    doc: dict[str, Any],
    *,
    action: str,
    source: str,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": source,
        "notes": notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == action
        ):
            history[index] = event
            return
    history.append(event)


def _ensure_variant_children(doc: dict[str, Any]) -> None:
    children = doc.setdefault("variant_children", [])
    if not isinstance(children, list):
        raise ValueError("variant_children is not a list")

    child_ids = {spec.expected_id for spec in CHILD_SPECS}
    child_paths = {f"data/normalized_yaml/{spec.target}" for spec in CHILD_SPECS}
    retained = [
        child
        for child in children
        if (
            isinstance(child, dict)
            and child.get("id") not in child_ids
            and child.get("path") not in child_paths
        )
    ]
    if len(retained) != len(children) - sum(
        1
        for child in children
        if (
            isinstance(child, dict)
            and (child.get("id") in child_ids or child.get("path") in child_paths)
        )
    ):
        raise ValueError("variant_children contains a non-mapping row")

    retained.extend(copy.deepcopy(spec.variant_child) for spec in CHILD_SPECS)
    doc["variant_children"] = retained


def repair_record(doc: dict[str, Any], spec: RecordSpec) -> dict[str, Any]:
    _ensure_record(doc, spec)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = _ingredients(spec)
    _put_after(repaired, "solutions", _solutions(spec), "ingredients")
    _put_after(repaired, "preparation_steps", _preparation_steps(spec), "solutions")
    _put_after(repaired, "notes", spec.notes, "media_term")
    _ensure_flags(repaired)
    _ensure_references(repaired, spec)
    _append_curation_event(
        repaired,
        action=ACTION,
        source="; ".join(spec.references),
        notes=(
            f"Curated TOGO:{spec.togo_id} from TOGO and NBRC Medium "
            f"{spec.nbrc_no}; corrected Distilled water from a mass-like "
            f"{spec.water_ml} g/L import to {spec.water_ml} ml/L, nested "
            "500 ug/ml antibiotic stocks with their active components, "
            "added pH 7.0, grounded yeast extract, calcium chloride "
            "dihydrate, antibiotic components, water, and agar, and "
            "retained Bacto Tryptone as a sourced opaque component."
        ),
    )

    if spec.relationship is None:
        repaired.pop("parent_media", None)
        repaired.pop("variant_relationship", None)
        repaired.pop("variant_modifications", None)
    else:
        repaired["parent_media"] = copy.deepcopy(spec.parent_media)
        repaired["variant_relationship"] = spec.relationship
        repaired["variant_modifications"] = [spec.variant_notes]
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != PARENT_ID:
        raise ValueError(f"{PARENT}: expected id {PARENT_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != PARENT_MEDIA_TERM:
        raise ValueError(f"{PARENT}: expected media term {PARENT_MEDIA_TERM}")

    repaired = copy.deepcopy(doc)
    _ensure_variant_children(repaired)
    _append_curation_event(
        repaired,
        action=LINK_ACTION,
        source="; ".join(spec.nbrc_url for spec in SPECS),
        notes=("Linked NBRC Media 916-920 as antibiotic-stock variants of NBRC Medium 915."),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for spec in SPECS:
        path = normalized / spec.target
        plans[path] = repair_record(_load(path), spec)

    parent_path = normalized / PARENT
    plans[parent_path] = repair_parent(plans[parent_path])
    return plans


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
