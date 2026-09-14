#!/usr/bin/env python3
"""Repair TOGO M2025-M2027 NBRC aldehyde basal media."""

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

CURATOR = "repair_togo_m2025_m2027_aldehyde_basal_score15.py"
ACTION = "RESOLVED_TOGO_M2025_M2027_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]


@dataclass(frozen=True)
class TargetSpec:
    path: Path
    expected_id: str
    media_term: str
    title: str
    nbrc_no: str
    aldehyde: str
    aldehyde_value: str
    aldehyde_term: tuple[str, str]
    imported_solutions: tuple[SolutionSignature, ...]

    @property
    def source(self) -> str:
        return f"TOGO {self.media_term[5:]} / NBRC Medium {self.nbrc_no}"

    @property
    def togo_url(self) -> str:
        return f"https://togomedium.org/medium/{self.media_term[5:]}"

    @property
    def nbrc_url(self) -> str:
        return "https://www.nite.go.jp/nbrc/catalogue/" f"NBRCMediumDetailServlet?NO={self.nbrc_no}"

    @property
    def references(self) -> tuple[str, str]:
        return (self.togo_url, self.nbrc_url)


TARGETS: tuple[TargetSpec, ...] = (
    TargetSpec(
        path=Path("bacterial/basal_medium_acetaldehyde.yaml"),
        expected_id="CultureMech:008613",
        media_term="TOGO:M2025",
        title="Basal medium + Acetaldehyde",
        nbrc_no="1316",
        aldehyde="Acetaldehyde**",
        aldehyde_value="1.0",
        aldehyde_term=("CHEBI:15343", "acetaldehyde"),
        imported_solutions=(
            ("Acetaldehyde**", "1", "G_PER_L", ()),
            ("Hipolypepton*", "10", "G_PER_L", ()),
        ),
    ),
    TargetSpec(
        path=Path("bacterial/basal_medium_benzaldehyde.yaml"),
        expected_id="CultureMech:008614",
        media_term="TOGO:M2026",
        title="Basal medium + Benzaldehyde",
        nbrc_no="1317",
        aldehyde="Benzaldehyde**",
        aldehyde_value="0.5",
        aldehyde_term=("CHEBI:17169", "benzaldehyde"),
        imported_solutions=(
            ("Hipolypepton*", "10", "G_PER_L", ()),
            ("Benzaldehyde**", "0.5", "G_PER_L", ()),
        ),
    ),
    TargetSpec(
        path=Path("bacterial/basal_medium_formaldehyde.yaml"),
        expected_id="CultureMech:008615",
        media_term="TOGO:M2027",
        title="Basal medium + Formaldehyde",
        nbrc_no="1318",
        aldehyde="Formaldehyde**",
        aldehyde_value="0.5",
        aldehyde_term=("CHEBI:16842", "formaldehyde"),
        imported_solutions=(
            ("Formaldehyde**", "0.5", "G_PER_L", ()),
            ("Hipolypepton*", "10", "G_PER_L", ()),
        ),
    ),
)

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Yeast extract", "5", "G_PER_L"),
    ("NaCl", "5", "G_PER_L"),
    ("K2HPO4", "1", "G_PER_L"),
    ("Agar (if needed)", "15", "G_PER_L"),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar (if needed)": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "ML_PER_L": "ml/L",
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    spec: TargetSpec,
    preferred_term: str,
    value: str,
    unit: str,
    *,
    term: tuple[str, str] | None = None,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": spec.source,
        "notes": notes
        or f"NBRC Medium {spec.nbrc_no} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }
    grounding = term or GROUNDINGS.get(preferred_term)
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)
    return row


def final_ingredients(spec: TargetSpec) -> tuple[dict[str, Any], ...]:
    return (
        _component(spec, "K2HPO4", "1.0", "G_PER_L"),
        _component(
            spec,
            "Hipolypepton*",
            "10.0",
            "G_PER_L",
            notes=(
                f"NBRC Medium {spec.nbrc_no} lists 10 g/L Hipolypepton "
                "and notes that the asterisk marks Wako Pure Chemical "
                "Industries; this peptone product is retained as an opaque "
                "complex component."
            ),
        ),
        _component(spec, "Yeast extract", "5.0", "G_PER_L"),
        _component(spec, "NaCl", "5.0", "G_PER_L"),
        _component(
            spec,
            spec.aldehyde,
            spec.aldehyde_value,
            "ML_PER_L",
            term=spec.aldehyde_term,
            notes=(
                f"NBRC Medium {spec.nbrc_no} lists {spec.aldehyde_value} "
                f"ml/L {spec.aldehyde[:-2]} and notes that the double "
                "asterisk marks separate filter sterilization."
            ),
        ),
        _component(
            spec,
            "Distilled water",
            "1.0",
            "L",
            notes=f"NBRC Medium {spec.nbrc_no} lists 1 L distilled water.",
        ),
        _component(spec, "Agar (if needed)", "15.0", "G_PER_L"),
    )


def final_ingredient_signature(spec: TargetSpec) -> tuple[Component, ...]:
    return _signature(final_ingredients(spec), "ingredients")


def preparation_steps(spec: TargetSpec) -> tuple[dict[str, Any], ...]:
    return (
        {
            "step_number": 1,
            "action": "FILTER_STERILIZE",
            "description": f"Sterilize {spec.aldehyde[:-2]} separately by filtration.",
        },
    )


def notes(spec: TargetSpec) -> str:
    return (
        f"TOGO {spec.media_term[5:]} imports NBRC Medium {spec.nbrc_no} as "
        f"{spec.title}. NBRC {spec.nbrc_no} lists 1 g K2HPO4, 10 g "
        "Hipolypepton from Wako Pure Chemical Industries, 5 g yeast extract, "
        f"5 g NaCl, {float(spec.aldehyde_value):g} ml {spec.aldehyde[:-2]}, 1 L "
        "distilled water, optional 15 g agar, and pH 7.0, and states that "
        f"{spec.aldehyde[:-2]} is sterilized separately by filtration."
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


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for solution in solutions:
        if not isinstance(solution, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = solution.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError("solution row lacks concentration")
        signatures.append(
            (
                str(solution.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _signature(solution.get("composition"), "solution composition"),
            )
        )
    return tuple(signatures)


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(doc: dict[str, Any], spec: TargetSpec) -> None:
    if doc.get("id") != spec.expected_id:
        raise ValueError(f"{spec.path}: expected id {spec.expected_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != spec.media_term:
        raise ValueError(f"{spec.path}: expected media term {spec.media_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        final_ingredient_signature(spec),
    ):
        raise ValueError(
            f"{spec.path}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (spec.imported_solutions, ()):
        raise ValueError(
            f"{spec.path}: solution signature drifted from "
            f"{spec.imported_solutions!r} to {solution_signatures!r}"
        )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any], spec: TargetSpec) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in spec.references:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any], spec: TargetSpec) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(spec.references),
        "notes": (
            f"{notes(spec)} Moved {spec.aldehyde[:-2]} and Hipolypepton out "
            "of empty solution wrappers, corrected liquid quantities, and "
            "marked the NBRC formula as curated."
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


def repair_record(doc: dict[str, Any], spec: TargetSpec) -> dict[str, Any]:
    _ensure_target(doc, spec)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "SEMI_DEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired["ingredients"] = copy.deepcopy(list(final_ingredients(spec)))
    repaired.pop("solutions", None)
    for stale_key in (
        "parent_media",
        "variant_children",
        "variant_relationship",
        "variant_modifications",
    ):
        repaired.pop(stale_key, None)
    _put_after(repaired, "notes", notes(spec), "media_term")
    repaired["preparation_steps"] = copy.deepcopy(list(preparation_steps(spec)))
    repaired.pop("sterilization", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, spec)
    _append_curation_event(repaired, spec)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / spec.path: repair_record(_load(normalized / spec.path), spec)
        for spec in TARGETS
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
