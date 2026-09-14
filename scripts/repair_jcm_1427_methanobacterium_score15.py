#!/usr/bin/env python3
"""Repair JCM 1427 Modified Methanobacterium Medium stock wrappers."""

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
TARGET = "archaea/JCM_J1427_MODIFIED_METHANOBACTERIUM_MEDIUM.yaml"
EXPECTED_ID = "CultureMech:015863"
EXPECTED_SOURCE_TERM = "jcm.grmd:1427"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

JCM_1427 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1427"
JCM_187 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=187"
JCM_266 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=266"
JCM_898 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=898"

CURATOR = "repair_jcm_1427_methanobacterium_score15.py"
ACTION = "RESOLVED_JCM_1427_METHANOBACTERIUM_SCORE15"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
SOURCE_1427 = "JCM Medium 1427"
SOURCE_187 = "JCM Medium 187"
SOURCE_266 = "JCM Medium 266"
SOURCE_898 = "JCM Medium 898"

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "L": "L",
}

OLD_SIGNATURE = (
    "KH2PO4",
    "MgSO4·7H2O",
    "NaCl",
    "NH4Cl",
    "CaCl2·2H2O",
    "FeCl2 solution (see Medium No. 187 )",
    "Trace element solution (see Medium No. 187 )",
    "Brain heart infusion (BD Difico)",
    "Proteose peptone (BD Difico)",
    "Yeast extract (Oxoid)",
    "Sodium acetate",
    "Sodium formate",
    "Rumen fluid, clarified (see Medium No. 266 )",
    "Resazurin",
    "Distilled water",
    "Vitamin solution (see Medium No. 898 )",
    "8% NaHCO3 solution",
    "5% Na2S·9H2O solution",
    "5% L-Cysteine·HCl·H2O solution",
)


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    term: tuple[str, str] | None = None,
    source: str = SOURCE_1427,
    notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "source": source,
        "notes": notes or f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "concentration": {"value": value, "unit": unit},
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
    notes: str,
    composition: list[dict[str, Any]] | None = None,
    preparation_notes: str | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "notes": notes,
    }
    if composition is not None:
        row["composition"] = copy.deepcopy(composition)
    if preparation_notes is not None:
        row["preparation_notes"] = preparation_notes
    return row


def _stock_component(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    term: tuple[str, str] | None = None,
) -> dict[str, Any]:
    return _ingredient(
        preferred_term,
        value,
        unit,
        source=source,
        notes=f"{source} prints this component in its stock solution.",
        term=term,
    )


INGREDIENTS: tuple[dict[str, Any], ...] = (
    _ingredient(
        "KH2PO4",
        "0.5",
        "G_PER_L",
        term=("CHEBI:63036", "potassium dihydrogen phosphate"),
    ),
    _ingredient(
        "MgSO4 x 7H2O",
        "0.4",
        "G_PER_L",
        term=("CHEBI:31795", "magnesium sulfate heptahydrate"),
    ),
    _ingredient("NaCl", "0.4", "G_PER_L", term=("CHEBI:26710", "sodium chloride")),
    _ingredient("NH4Cl", "0.4", "G_PER_L", term=("CHEBI:31206", "ammonium chloride")),
    _ingredient(
        "CaCl2 x 2H2O",
        "0.05",
        "G_PER_L",
        term=("CHEBI:86158", "calcium chloride dihydrate"),
    ),
    _ingredient(
        "Brain heart infusion (BD Difico)",
        "6.0",
        "G_PER_L",
        notes=(
            "JCM Medium 1427 lists Brain heart infusion (BD Difico) as a "
            "commercial complex product."
        ),
    ),
    _ingredient(
        "Proteose peptone (BD Difico)",
        "6.0",
        "G_PER_L",
        notes=("JCM Medium 1427 lists Proteose peptone (BD Difico) as a complex " "peptone input."),
    ),
    _ingredient(
        "Yeast extract (Oxoid)",
        "2.0",
        "G_PER_L",
        notes="JCM Medium 1427 lists Yeast extract (Oxoid).",
    ),
    _ingredient(
        "Sodium acetate",
        "1.0",
        "G_PER_L",
        term=("CHEBI:32954", "sodium acetate"),
    ),
    _ingredient(
        "Sodium formate",
        "2.0",
        "G_PER_L",
        term=("CHEBI:62965", "sodium formate"),
    ),
    _ingredient(
        "Resazurin",
        "0.5",
        "MG_PER_L",
        term=("CHEBI:8806", "Resazurin"),
    ),
    _ingredient(
        "Distilled water",
        "940.0",
        "ML_PER_L",
        term=("CHEBI:15377", "water"),
    ),
)

SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution(
        "FeCl2 solution",
        "1.0",
        notes="JCM Medium 1427 adds 1.0 ml/L FeCl2 solution from JCM Medium 187.",
        composition=[
            _stock_component(
                "25% HCl (7.7 M)",
                "10.0",
                "ML_PER_L",
                source=SOURCE_187,
                term=("CHEBI:17883", "hydrogen chloride"),
            ),
            _stock_component(
                "FeCl2 x 4H2O",
                "1.5",
                "G_PER_L",
                source=SOURCE_187,
                term=("CHEBI:86249", "iron dichloride tetrahydrate"),
            ),
            _stock_component(
                "Distilled water",
                "990.0",
                "ML_PER_L",
                source=SOURCE_187,
                term=("CHEBI:15377", "water"),
            ),
        ],
    ),
    _solution(
        "Trace element solution",
        "1.0",
        notes=("JCM Medium 1427 adds 1.0 ml/L Trace element solution from " "JCM Medium 187."),
        composition=[
            _stock_component(
                "ZnCl2",
                "70.0",
                "MG_PER_L",
                source=SOURCE_187,
                term=("CHEBI:49976", "zinc dichloride"),
            ),
            _stock_component(
                "MnCl2 x 4H2O",
                "100.0",
                "MG_PER_L",
                source=SOURCE_187,
                term=("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
            ),
            _stock_component(
                "H3BO3",
                "6.0",
                "MG_PER_L",
                source=SOURCE_187,
                term=("CHEBI:33118", "boric acid"),
            ),
            _stock_component(
                "CoCl2 x 6H2O",
                "190.0",
                "MG_PER_L",
                source=SOURCE_187,
                term=("CHEBI:53503", "cobalt chloride hexahydrate"),
            ),
            _stock_component(
                "CuCl2 x 2H2O",
                "2.0",
                "MG_PER_L",
                source=SOURCE_187,
                term=("CHEBI:86318", "copper(II) chloride dihydrate"),
            ),
            _stock_component(
                "NiCl2 x 6H2O",
                "24.0",
                "MG_PER_L",
                source=SOURCE_187,
                term=("CHEBI:53542", "nickel chloride hexahydrate"),
            ),
            _stock_component(
                "Na2MoO4 x 2H2O",
                "36.0",
                "MG_PER_L",
                source=SOURCE_187,
                term=("CHEBI:75213", "sodium molybdate dihydrate"),
            ),
            _stock_component(
                "Distilled water",
                "1.0",
                "L",
                source=SOURCE_187,
                term=("CHEBI:15377", "water"),
            ),
        ],
    ),
    _solution(
        "Rumen fluid, clarified",
        "10.0",
        notes=(
            "JCM Medium 1427 adds 10.0 ml/L clarified rumen fluid prepared "
            "according to JCM Medium 266."
        ),
    ),
    _solution(
        "Vitamin solution",
        "1.0",
        notes=("JCM Medium 1427 adds 1.0 ml/L Vitamin solution from " "JCM Medium 898."),
        composition=[
            _stock_component(
                "Vitamin B12",
                "100.0",
                "MG_PER_L",
                source=SOURCE_898,
                term=("CHEBI:176843", "vitamin B12"),
            ),
            _stock_component(
                "p-Aminobenzoic acid",
                "80.0",
                "MG_PER_L",
                source=SOURCE_898,
                term=("CHEBI:30753", "4-aminobenzoic acid"),
            ),
            _stock_component(
                "Biotin",
                "20.0",
                "MG_PER_L",
                source=SOURCE_898,
                term=("CHEBI:15956", "biotin"),
            ),
            _stock_component(
                "Nicotinic acid",
                "200.0",
                "MG_PER_L",
                source=SOURCE_898,
                term=("CHEBI:15940", "nicotinic acid"),
            ),
            _stock_component(
                "DL-Calcium pantothenate",
                "100.0",
                "MG_PER_L",
                source=SOURCE_898,
                term=("CHEBI:31345", "Calcium pantothenate"),
            ),
            _stock_component(
                "Pyridoxine HCl",
                "300.0",
                "MG_PER_L",
                source=SOURCE_898,
                term=("CHEBI:30961", "pyridoxine hydrochloride"),
            ),
            _stock_component(
                "Thiamine HCl",
                "200.0",
                "MG_PER_L",
                source=SOURCE_898,
                term=("CHEBI:49105", "thiamine hydrochloride"),
            ),
            _stock_component(
                "Distilled water",
                "1.0",
                "L",
                source=SOURCE_898,
                term=("CHEBI:15377", "water"),
            ),
        ],
    ),
    _solution(
        "8% NaHCO3 solution",
        "50.0",
        notes="JCM Medium 1427 adds 50.0 ml/L filter-sterilized 8% NaHCO3 solution.",
        composition=[
            _stock_component(
                "NaHCO3",
                "80.0",
                "G_PER_L",
                source=SOURCE_1427,
                term=("CHEBI:32139", "sodium hydrogencarbonate"),
            )
        ],
        preparation_notes="Filter-sterilize before anaerobic addition.",
    ),
    _solution(
        "5% Na2S x 9H2O solution",
        "10.0",
        notes=("JCM Medium 1427 adds 10.0 ml/L 5% Na2S x 9H2O solution " "before inoculation."),
        composition=[
            _stock_component(
                "Na2S x 9H2O",
                "50.0",
                "G_PER_L",
                source=SOURCE_1427,
                term=("CHEBI:76209", "sodium sulfide nonahydrate"),
            )
        ],
        preparation_notes="Autoclave under N2 and store under a N2 atmosphere.",
    ),
    _solution(
        "5% L-Cysteine x HCl x H2O solution",
        "10.0",
        notes=(
            "JCM Medium 1427 adds 10.0 ml/L 5% L-Cysteine x HCl x H2O "
            "solution before inoculation."
        ),
        composition=[
            _stock_component(
                "L-Cysteine x HCl x H2O",
                "50.0",
                "G_PER_L",
                source=SOURCE_1427,
                term=("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
            )
        ],
        preparation_notes="Autoclave under N2 and store under a N2 atmosphere.",
    ),
)

NEW_SIGNATURE = tuple(row["preferred_term"] for row in INGREDIENTS)


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


def _component_names(doc: dict[str, Any]) -> tuple[str, ...]:
    return tuple(
        str(row.get("preferred_term") or "")
        for row in doc.get("ingredients") or []
        if isinstance(row, dict)
    )


def _require_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    source_term = _source_term_id(doc)
    if source_term != EXPECTED_SOURCE_TERM:
        raise ValueError(
            f"{TARGET}: expected source term {EXPECTED_SOURCE_TERM}, found {source_term!r}"
        )
    if _component_names(doc) not in (OLD_SIGNATURE, NEW_SIGNATURE):
        raise ValueError(f"{TARGET}: JCM 1427 ingredient signature drifted")


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")
    flags.extend(
        (
            "has_ontology_mappings",
            "has_unmapped_ingredients",
            "ingredients_curated",
        )
    )
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")
    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in (JCM_1427, JCM_187, JCM_266, JCM_898):
        if reference not in existing:
            references.append({"reference": reference})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": JCM_1427,
        "notes": (
            "Moved JCM 1427 stock-solution and cross-reference wrappers into "
            "structured solutions backed by JCM 187, 266, and 898."
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
    repaired["notes"] = (
        "Source: JCM Medium 1427. FeCl2, trace-element, clarified-rumen-fluid, "
        "and vitamin stocks are expanded or cross-referenced from JCM Mediums "
        "187, 266, and 898."
    )
    repaired["ingredients"] = copy.deepcopy(list(INGREDIENTS))
    repaired["solutions"] = copy.deepcopy(list(SOLUTIONS))
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _ensure_event(repaired)
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
        print(f"{status:5s} {path.relative_to(args.normalized_dir)}")

    verb = "wrote" if args.apply else "would write"
    print(f"\n{verb} {changed_count} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
