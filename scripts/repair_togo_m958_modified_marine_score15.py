#!/usr/bin/env python3
"""Repair the TOGO Modified Marine Agar 2216 score-15 family."""

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
M958_PATH = Path("bacterial/TOGO_M958_Modified_Marine_Agar_2216.yaml")
M1345_PATH = Path("bacterial/modified_marine_agar_2216.yaml")
M1274_PATH = Path("bacterial/modified_marine_agar_2216_with_5_nacl_ph_9.yaml")
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_m958_modified_marine_score15.py"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

TOGO_M958 = "https://togomedium.org/medium/M958"
JCM_913 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=913"
TOGO_M1345 = "https://togomedium.org/medium/M1345"
JCM_1251 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1251"
TOGO_M1274 = "https://togomedium.org/medium/M1274"
JCM_1189 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1189"
TOGO_M190 = "https://togomedium.org/medium/M190"

SOURCE_M958 = "TOGO M958 / JCM Medium 913"
SOURCE_M1345 = "TOGO M1345 / JCM Medium 1251"
SOURCE_M1274 = "TOGO M1274 / JCM Medium 1189"
SOURCE_VITAMINS = "TOGO M190 / JCM Medium 197"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

M958_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Malt extract (BD-Difco)", "1", "G_PER_L"),
    ("Casitone (BD-Difco)", "1", "G_PER_L"),
    ("Soytone (BD-Difco) or Phytone peptone (BD-BBL)", "1", "G_PER_L"),
    ("Marine agar 2216 (BD-Difco)", "55.1", "G_PER_L"),
)

M1345_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "1", "G_PER_L"),
    ("Malt extract (BD-Difco)", "1", "G_PER_L"),
    ("Casitone (BD-Difco)", "1", "G_PER_L"),
    ("Marine agar 2216 (BD-Difco)", "55.1", "G_PER_L"),
    ("Phytone peptone (BD-Difco)", "1", "G_PER_L"),
)

M1274_IMPORTED: tuple[Component, ...] = (
    ("Distilled water", "990", "G_PER_L"),
    ("NaCl", "50", "G_PER_L"),
    ("Malt extract (BD-Difco)", "1", "G_PER_L"),
    ("Casitone (BD-Difco)", "1", "G_PER_L"),
    ("Soytone (BD-Difco) or Phytone peptone (BD-BBL)", "1", "G_PER_L"),
    ("Marine agar 2216 (BD-Difco)", "55.1", "G_PER_L"),
)

M1274_IMPORTED_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("Trace vitamins (see Medium [M190])", "10", "G_PER_L", ()),
    ("Na2CO3 solution", "variable", "VARIABLE", ()),
)

M958_FINAL: tuple[Component, ...] = (
    ("Marine agar 2216 (BD-Difco)", "55.1", "G_PER_L"),
    ("Casitone (BD-Difco)", "1.0", "G_PER_L"),
    ("Soytone (BD-Difco) or Phytone peptone (BD-BBL)", "1.0", "G_PER_L"),
    ("Malt extract (BD-Difco)", "1.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

M1345_FINAL: tuple[Component, ...] = (
    ("Marine agar 2216 (BD-Difco)", "55.1", "G_PER_L"),
    ("Casitone (BD-Difco)", "1.0", "G_PER_L"),
    ("Phytone peptone (BD-Difco)", "1.0", "G_PER_L"),
    ("Malt extract (BD-Difco)", "1.0", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)

M1274_FINAL: tuple[Component, ...] = (
    ("Marine agar 2216 (BD-Difco)", "55.1", "G_PER_L"),
    ("Casitone (BD-Difco)", "1.0", "G_PER_L"),
    ("Soytone (BD-Difco) or Phytone peptone (BD-BBL)", "1.0", "G_PER_L"),
    ("Malt extract (BD-Difco)", "1.0", "G_PER_L"),
    ("NaCl", "50.0", "G_PER_L"),
    ("Distilled water", "990.0", "ML_PER_L"),
)

TRACE_VITAMIN_COMPOSITION: tuple[Component, ...] = (
    ("Biotin", "2.0", "MG_PER_L"),
    ("p-Aminobenzoic acid", "5.0", "MG_PER_L"),
    ("Thiamine HCl", "5.0", "MG_PER_L"),
    ("Calcium pantothenate", "5.0", "MG_PER_L"),
    ("Pyridoxine HCl", "10.0", "MG_PER_L"),
    ("Folic acid", "2.0", "MG_PER_L"),
    ("Vitamin B12", "0.1", "MG_PER_L"),
    ("Riboflavin", "5.0", "MG_PER_L"),
    ("Nicotinic acid", "5.0", "MG_PER_L"),
    ("Lipoic acid", "5.0", "MG_PER_L"),
    ("Distilled water", "1000.0", "ML_PER_L"),
)

M1274_FINAL_SOLUTIONS: tuple[SolutionSignature, ...] = (
    ("Trace vitamins", "10.0", "ML_PER_L", TRACE_VITAMIN_COMPOSITION),
    ("10% Na2CO3 solution", "variable", "VARIABLE", (("Na2CO3", "10.0", "PERCENT_W_V"),)),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Biotin": ("CHEBI:15956", "biotin"),
    "Calcium pantothenate": ("CHEBI:31345", "Calcium pantothenate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Folic acid": ("CHEBI:27470", "folic acid"),
    "Lipoic acid": ("CHEBI:16494", "lipoic acid"),
    "Malt extract (BD-Difco)": ("FOODON:03301056", "malt extract"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "Nicotinic acid": ("CHEBI:15940", "nicotinic acid"),
    "Phytone peptone (BD-Difco)": ("FOODON:03315720", "Soy peptone"),
    "p-Aminobenzoic acid": ("CHEBI:30753", "4-aminobenzoic acid"),
    "Pyridoxine HCl": ("CHEBI:30961", "pyridoxine hydrochloride"),
    "Riboflavin": ("CHEBI:17015", "riboflavin"),
    "Thiamine HCl": ("CHEBI:49105", "thiamine hydrochloride"),
    "Vitamin B12": ("CHEBI:176843", "vitamin B12"),
}

NUTRITIONAL_ROLES: dict[str, tuple[str, ...]] = {
    "Biotin": ("VITAMIN_SOURCE",),
    "Calcium pantothenate": ("VITAMIN_SOURCE",),
    "Casitone (BD-Difco)": ("PROTEIN_SOURCE",),
    "Folic acid": ("VITAMIN_SOURCE",),
    "Lipoic acid": ("VITAMIN_SOURCE",),
    "Malt extract (BD-Difco)": ("CARBON_SOURCE", "NITROGEN_SOURCE"),
    "Nicotinic acid": ("VITAMIN_SOURCE",),
    "Phytone peptone (BD-Difco)": ("PROTEIN_SOURCE",),
    "p-Aminobenzoic acid": ("VITAMIN_SOURCE",),
    "Pyridoxine HCl": ("VITAMIN_SOURCE",),
    "Riboflavin": ("VITAMIN_SOURCE",),
    "Soytone (BD-Difco) or Phytone peptone (BD-BBL)": ("PROTEIN_SOURCE",),
    "Thiamine HCl": ("VITAMIN_SOURCE",),
    "Vitamin B12": ("VITAMIN_SOURCE",),
}

PHYSICOCHEMICAL_ROLES: dict[str, tuple[str, ...]] = {
    "Marine agar 2216 (BD-Difco)": ("SOLIDIFYING_AGENT",),
    "Na2CO3": ("BUFFER",),
    "NaCl": ("OSMOTIC_AGENT",),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "L": "L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "PERCENT_W_V": "% w/v",
    "VARIABLE": "variable",
}


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
    term: bool = True,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
    }

    grounding = GROUNDINGS.get(preferred_term) if term else None
    if grounding:
        row["term"] = _term(*grounding)
        if grounding[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*grounding)

    nutritional_roles = NUTRITIONAL_ROLES.get(preferred_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)

    physicochemical_roles = PHYSICOCHEMICAL_ROLES.get(preferred_term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)

    return row


def _composition(signature: tuple[Component, ...], source: str) -> list[dict[str, Any]]:
    return [
        _component(name, value, unit, source=source, term=name != "Marine agar 2216 (BD-Difco)")
        for name, value, unit in signature
    ]


def _trace_vitamins() -> dict[str, Any]:
    return {
        "preferred_term": "Trace vitamins",
        "concentration": {"value": "10.0", "unit": "ML_PER_L"},
        "source": SOURCE_M1274,
        "notes": f"{SOURCE_M1274} adds 10 ml/L Trace vitamins from TOGO M190/JCM Medium 197.",
        "composition": [
            _component(name, value, unit, source=SOURCE_VITAMINS)
            for name, value, unit in TRACE_VITAMIN_COMPOSITION
        ],
    }


def _na2co3_solution() -> dict[str, Any]:
    return {
        "preferred_term": "10% Na2CO3 solution",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "source": SOURCE_M1274,
        "notes": f"{SOURCE_M1274} adjusts the medium to pH 9.0 with sterilized 10% Na2CO3 solution.",
        "term": _term(*GROUNDINGS["Na2CO3"]),
        "mediaingredientmech_chebi_term": _term(*GROUNDINGS["Na2CO3"]),
        "composition": [
            _component(
                "Na2CO3",
                "10.0",
                "PERCENT_W_V",
                source=SOURCE_M1274,
                notes=f"{SOURCE_M1274} specifies the pH-adjustment Na2CO3 solution as 10% w/v.",
            )
        ],
        "preparation_notes": "Sterilize before use.",
    }


def _m1274_solutions() -> list[dict[str, Any]]:
    return [_trace_vitamins(), _na2co3_solution()]


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


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


def _ensure_references(doc: dict[str, Any], references: tuple[str, ...]) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for reference in references:
        if reference not in existing:
            rows.append({"reference": reference})
            existing.add(reference)


def _append_event(
    doc: dict[str, Any],
    *,
    action: str,
    references: tuple[str, ...],
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": "; ".join(references),
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


def _ensure_record(
    doc: dict[str, Any],
    *,
    expected_id: str,
    media_term: str,
    imported: tuple[Component, ...],
    final: tuple[Component, ...],
    imported_solutions: tuple[SolutionSignature, ...] = (),
    final_solutions: tuple[SolutionSignature, ...] = (),
) -> None:
    if doc.get("id") != expected_id:
        raise ValueError(f"expected {expected_id}, found {doc.get('id')}")
    if _source_term_id(doc) != media_term:
        raise ValueError(f"expected media term {media_term}, found {_source_term_id(doc)!r}")
    if _signature(doc.get("ingredients"), "ingredients") not in (imported, final):
        raise ValueError("ingredient signature drifted")
    if _solution_signatures(doc.get("solutions"), "solutions") not in (
        imported_solutions,
        final_solutions,
    ):
        raise ValueError("solution signature drifted")


def _repair_base(
    doc: dict[str, Any],
    *,
    final: tuple[Component, ...],
    source: str,
    ph: float,
    references: tuple[str, ...],
    action: str,
    notes: str,
) -> dict[str, Any]:
    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", ph, "physical_state")
    repaired["ingredients"] = _composition(final, source)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _put_after(repaired, "notes", notes, "media_term")
    _put_after(
        repaired,
        "preparation_steps",
        [
            {
                "step_number": 1,
                "action": "MIX",
                "description": f"Combine the Modified Marine Agar 2216 components listed by {source}.",
            },
            {
                "step_number": 2,
                "action": "ADJUST_PH",
                "description": f"Adjust pH to {ph:.1f}.",
            },
        ],
        "ingredients",
    )
    _ensure_flags(repaired)
    _ensure_references(repaired, references)
    _append_event(
        repaired,
        action=action,
        references=references,
        notes=(
            "Corrected JCM Modified Marine Agar 2216 water units, added the "
            "source pH, grounded the disclosed complex nutrient products where "
            "possible, and marked remaining BD products as intentionally "
            "unmapped source components."
        ),
    )
    return repaired


def repair_m958(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_record(
        doc,
        expected_id="CultureMech:010382",
        media_term="TOGO:M958",
        imported=M958_IMPORTED,
        final=M958_FINAL,
    )
    return _repair_base(
        doc,
        final=M958_FINAL,
        source=SOURCE_M958,
        ph=7.5,
        references=(TOGO_M958, JCM_913),
        action="RESOLVED_TOGO_M958_MODIFIED_MARINE",
        notes=(
            "JCM Medium 913 Modified Marine Agar 2216 lists 55.1 g/L Marine "
            "agar 2216, 1.0 g/L Casitone, 1.0 g/L Soytone or Phytone peptone, "
            "1.0 g/L Malt extract, and 1.0 L Distilled water; adjust pH to 7.5."
        ),
    )


def repair_m1345(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_record(
        doc,
        expected_id="CultureMech:007881",
        media_term="TOGO:M1345",
        imported=M1345_IMPORTED,
        final=M1345_FINAL,
    )
    return _repair_base(
        doc,
        final=M1345_FINAL,
        source=SOURCE_M1345,
        ph=7.5,
        references=(TOGO_M1345, JCM_1251),
        action="RESOLVED_TOGO_M1345_MODIFIED_MARINE",
        notes=(
            "JCM Medium 1251 Modified Marine Agar 2216 lists 55.1 g/L Marine "
            "agar 2216, 1.0 g/L Casitone, 1.0 g/L Phytone peptone, 1.0 g/L "
            "Malt extract, and 1.0 L Distilled water; adjust pH to 7.5."
        ),
    )


def repair_m1274(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_record(
        doc,
        expected_id="CultureMech:007807",
        media_term="TOGO:M1274",
        imported=M1274_IMPORTED,
        final=M1274_FINAL,
        imported_solutions=M1274_IMPORTED_SOLUTIONS,
        final_solutions=M1274_FINAL_SOLUTIONS,
    )
    repaired = _repair_base(
        doc,
        final=M1274_FINAL,
        source=SOURCE_M1274,
        ph=9.0,
        references=(TOGO_M1274, JCM_1189, TOGO_M190),
        action="RESOLVED_TOGO_M1274_MODIFIED_MARINE_NACL_PH9",
        notes=(
            "JCM Medium 1189 Modified Marine Agar 2216 with 5% NaCl (pH 9) "
            "lists the JCM 913 marine-agar base plus 50.0 g/L NaCl, "
            "10.0 ml/L Trace vitamins, 990.0 ml/L Distilled water, and pH "
            "adjustment to 9.0 with sterilized 10% Na2CO3 solution."
        ),
    )
    _put_after(repaired, "solutions", _m1274_solutions(), "ingredients")
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / M958_PATH: repair_m958(_load(normalized / M958_PATH)),
        normalized / M1345_PATH: repair_m1345(_load(normalized / M1345_PATH)),
        normalized / M1274_PATH: repair_m1274(_load(normalized / M1274_PATH)),
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
    print(f"\n{verb} {changed_count} file(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
