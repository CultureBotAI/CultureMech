#!/usr/bin/env python3
"""Repair TOGO M1004/M1005 Modified Growth Medium records."""

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

CURATOR = "repair_togo_m1004_m1005_score15.py"
ACTION = "RESOLVED_TOGO_M1004_M1005_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M1004 = "https://togomedium.org/medium/M1004"
TOGO_M1005 = "https://togomedium.org/medium/M1005"
TOGO_M578 = "https://togomedium.org/medium/M578"
JCM_574 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=574"
JCM_956 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=956"

SOURCE_M578 = "JCM Medium 574"
MDS_SOURCE = "TOGO M578 / JCM Medium 574"
TITLE = "Modified Growth Medium With 23% Total Salt Concentration"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

MDS_IMPORTED_SOLUTION = (
    "MDS salt water (see Medium [M578])",
    "767",
    "G_PER_L",
    (),
)
MDS_SIGNATURE: tuple[Component, ...] = (
    ("NaCl", "240.0", "G_PER_L"),
    ("MgCl2 x 6H2O", "30.0", "G_PER_L"),
    ("MgSO4 x 7H2O", "35.0", "G_PER_L"),
    ("KCl", "7.0", "G_PER_L"),
    ("1 M CaCl2 solution", "5.0", "ML_PER_L"),
    ("Distilled water", "1.0", "L"),
)
MDS_FINAL_SOLUTION = ("MDS salt water", "767", "ML_PER_L", MDS_SIGNATURE)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MgSO4 x 7H2O": ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Peptone (Oxoid)": ("MICRO:0000178", "peptone"),
    "1 M CaCl2 solution": ("CHEBI:3312", "calcium dichloride"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}
UNIT_LABELS = {
    "G_PER_L": "g/L",
    "ML_PER_L": "ml/L",
}


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    source_term: str
    source_label: str
    togo_url: str
    original_source: str
    ingredient_signature: tuple[Component, ...]
    ingredients: tuple[dict[str, Any], ...]

    @property
    def notes(self) -> str:
        agar_note = ""
        if any(row["preferred_term"] == "Agar" for row in self.ingredients):
            agar_note = ", 20 g/L agar"

        return (
            f"{self.source_label} records {self.original_source} {TITLE} with "
            f"233 ml/L distilled water, 2 g/L yeast extract, 10 g/L Peptone "
            f"(Oxoid), 767 ml/L MDS salt water from TOGO M578{agar_note}, and "
            "final adjustment to pH 7.0. JCM Medium 574 defines MDS salt water "
            "as NaCl, MgCl2 x 6H2O, MgSO4 x 7H2O, KCl, and 1 M CaCl2 solution "
            "brought to 1 L and adjusted to pH 7.5 with 1 M Tris base."
        )

    @property
    def references(self) -> tuple[str, ...]:
        return (self.togo_url, TOGO_M578, JCM_956, JCM_574)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    term = GROUNDINGS[preferred_term]
    row["term"] = _term(*term)
    if term[0].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def _top_level_component(
    preferred_term: str,
    value: str,
    unit: str,
    source: str,
) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    )


def _mds_component(preferred_term: str, value: str, unit: str) -> dict[str, Any]:
    return _component(
        preferred_term,
        value,
        unit,
        source=SOURCE_M578,
        notes=f"{SOURCE_M578} prints this component in its MDS salt-water stock.",
    )


def _mds_salt_water(source: str) -> dict[str, Any]:
    return {
        "preferred_term": "MDS salt water",
        "concentration": {"value": "767", "unit": "ML_PER_L"},
        "source": source,
        "notes": f"{source} adds 767 ml/L MDS salt water from TOGO M578/JCM 574.",
        "composition": [
            _mds_component("NaCl", "240.0", "G_PER_L"),
            _mds_component("MgCl2 x 6H2O", "30.0", "G_PER_L"),
            _mds_component("MgSO4 x 7H2O", "35.0", "G_PER_L"),
            _mds_component("KCl", "7.0", "G_PER_L"),
            _component(
                "1 M CaCl2 solution",
                "5.0",
                "ML_PER_L",
                source=SOURCE_M578,
                notes=(
                    "JCM Medium 574 adds 5 ml/L 1 M CaCl2 solution to "
                    "MDS salt water."
                ),
            ),
            _mds_component("Distilled water", "1.0", "L"),
        ],
        "preparation_notes": (
            "JCM Medium 574 brings the MDS salt water stock to 1.0 L with "
            "distilled water and adjusts it to pH 7.5 with 1 M Tris base."
        ),
    }


def _preparation_steps(source: str, solid: bool) -> list[dict[str, Any]]:
    mix = (
        "Mix distilled water, yeast extract, Peptone (Oxoid), and MDS salt "
        "water thoroughly."
    )
    if solid:
        mix = (
            "Mix distilled water, yeast extract, agar, Peptone (Oxoid), and "
            "MDS salt water thoroughly."
        )

    return [
        {
            "step_number": 1,
            "action": "MIX",
            "description": mix,
        },
        {
            "step_number": 2,
            "action": "ADJUST_PH",
            "description": f"Adjust {source} to pH 7.0.",
        },
    ]


def _liquid_recipe(source: str) -> tuple[dict[str, Any], ...]:
    return (
        _top_level_component("Distilled water", "233", "ML_PER_L", source),
        _top_level_component("Yeast extract", "2", "G_PER_L", source),
        _top_level_component("Peptone (Oxoid)", "10", "G_PER_L", source),
    )


def _solid_recipe(source: str) -> tuple[dict[str, Any], ...]:
    return (
        _top_level_component("Distilled water", "233", "ML_PER_L", source),
        _top_level_component("Yeast extract", "2", "G_PER_L", source),
        _top_level_component("Agar", "20", "G_PER_L", source),
        _top_level_component("Peptone (Oxoid)", "10", "G_PER_L", source),
    )


M1004_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "233", "G_PER_L"),
    ("Yeast extract", "2", "G_PER_L"),
    ("Peptone (Oxoid)", "10", "G_PER_L"),
)
M1005_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Distilled water", "233", "G_PER_L"),
    ("Yeast extract", "2", "G_PER_L"),
    ("agar", "20", "G_PER_L"),
    ("Peptone (Oxoid)", "10", "G_PER_L"),
)

TARGETS: tuple[Target, ...] = (
    Target(
        path="bacterial/TOGO_M1004_Modified_Growth_Medium_With_23_Total_Salt_Concentration.yaml",
        record_id="CultureMech:007517",
        source_term="TOGO:M1004",
        source_label="TOGO M1004",
        togo_url=TOGO_M1004,
        original_source="JCM_M956",
        ingredient_signature=M1004_INGREDIENT_SIGNATURE,
        ingredients=_liquid_recipe("TOGO M1004"),
    ),
    Target(
        path="bacterial/TOGO_M1005_Modified_Growth_Medium_With_23_Total_Salt_Concentration.yaml",
        record_id="CultureMech:007518",
        source_term="TOGO:M1005",
        source_label="TOGO M1005",
        togo_url=TOGO_M1005,
        original_source="JCM_M956-2",
        ingredient_signature=M1005_INGREDIENT_SIGNATURE,
        ingredients=_solid_recipe("TOGO M1005"),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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


def _solution_signatures(doc: dict[str, Any]) -> tuple[SolutionSignature, ...]:
    signatures: list[SolutionSignature] = []
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")

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


def _ensure_target(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.record_id:
        raise ValueError(
            f"{target.path}: expected id {target.record_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != target.source_term:
        raise ValueError(f"{target.path}: expected media term {target.source_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    final_ingredient_signature = _signature(target.ingredients, "target ingredients")
    if ingredient_signature not in (
        target.ingredient_signature,
        final_ingredient_signature,
    ):
        raise ValueError(
            f"{target.path}: ingredient signature drifted from "
            f"{target.ingredient_signature!r} to {ingredient_signature!r}"
        )

    solution_signatures = _solution_signatures(doc)
    if solution_signatures not in (
        (MDS_IMPORTED_SOLUTION,),
        (MDS_FINAL_SOLUTION,),
    ):
        raise ValueError(f"{target.path}: MDS solution signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)
    if "has_unmapped_ingredients" in flags:
        flags.remove("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
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
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired.pop("ph_range", None)
    repaired["ingredients"] = copy.deepcopy(list(target.ingredients))
    repaired["solutions"] = [_mds_salt_water(target.source_label)]
    _put_after(
        repaired,
        "preparation_steps",
        _preparation_steps(
            target.source_label,
            any(row["preferred_term"] == "Agar" for row in target.ingredients),
        ),
        "solutions",
    )
    _put_after(repaired, "notes", target.notes, "media_term")
    repaired.pop("sterilization", None)
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
