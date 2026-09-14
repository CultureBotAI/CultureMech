#!/usr/bin/env python3
"""Repair empty KOMODO 418 and 522 DSMZ Medium 318 variants."""

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

PELOBACTER = "bacterial/pelobacter_medium.yaml"
CLOSTRIDIUM_NEOPROPIONICUM = "bacterial/clostridium_neopropionicum_medium.yaml"

KOMODO_418_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=418"
)
KOMODO_522_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=522"
)
DSMZ_318_URL = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium318.pdf"
DSMZ_418_URL = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium418.pdf"
DSMZ_522_URL = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium522.pdf"
DSMZ_141_URL = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf"

SOURCE_318 = "DSMZ Medium 318"
SOURCE_418 = "DSMZ Medium 418"
SOURCE_522 = "DSMZ Medium 522"
SOURCE_141_VITAMINS = "DSMZ Medium 141 vitamin solution"

CURATOR = "repair_komodo_418_522_score30.py"
ACTION = "RESOLVED_KOMODO_418_522_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"


@dataclass(frozen=True)
class Component:
    preferred_term: str
    value: str
    unit: str
    term: tuple[str, str]
    source: str
    notes: str


@dataclass(frozen=True)
class Target:
    path: str
    expected_id: str
    expected_media_term: str
    ph_value: float
    khco3_value: str
    branch_components: tuple[Component, ...]
    preparation_steps: tuple[str, ...]
    notes: str
    references: tuple[str, ...]


def _base_note(name: str, amount: str, value: str) -> str:
    return (
        f"{SOURCE_318} lists {amount} {name} in 1000 mL water and adds 10 mL "
        "trace element solution plus 10 mL vitamin solution; after omitting "
        f"methanol this yields {value} g/L in the 1020 mL formulation."
    )


def _combined_note(name: str, base: str, stock: str, value: str) -> str:
    return (
        f"{SOURCE_318} lists {base} {name} in the main recipe and 10 mL of a "
        f"trace solution containing {stock} {name} in 1000 mL water plus 10 "
        f"mL vitamin solution, yielding {value} g/L in the 1020 mL formulation."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_318} adds 10 mL of a trace element solution containing "
        f"{stock_amount} {name} to 1000 mL water plus 10 mL vitamin solution, "
        f"yielding {value} g/L in the 1020 mL formulation."
    )


def _vitamin_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_318} adds 10 mL of the {SOURCE_141_VITAMINS} to 1000 mL "
        f"water plus 10 mL trace element solution; the vitamin stock contains "
        f"{stock_amount} {name}, yielding {value} g/L in the 1020 mL "
        "formulation."
    )


COMMON_COMPONENTS: tuple[Component, ...] = (
    Component(
        "KH2PO4",
        "0.294118",
        "G_PER_L",
        ("CHEBI:63036", "potassium dihydrogen phosphate"),
        SOURCE_318,
        _base_note("KH2PO4", "0.300 g", "0.294118"),
    ),
    Component(
        "NaCl",
        "0.598039",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_318,
        _combined_note("NaCl", "0.600 g", "1.000 g/L", "0.598039"),
    ),
    Component(
        "MgCl2 x 6 H2O",
        "0.098039",
        "G_PER_L",
        ("CHEBI:86345", "magnesium dichloride hexahydrate"),
        SOURCE_318,
        _base_note("MgCl2 x 6 H2O", "0.100 g", "0.098039"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.079412",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_318,
        _combined_note("CaCl2 x 2 H2O", "0.080 g", "0.100 g/L", "0.079412"),
    ),
    Component(
        "NH4Cl",
        "0.980392",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_318,
        _base_note("NH4Cl", "1.000 g", "0.980392"),
    ),
    Component(
        "Yeast extract",
        "0.490196",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_318,
        _base_note("Yeast extract", "0.500 g", "0.490196"),
    ),
    Component(
        "Trypticase",
        "0.490196",
        "G_PER_L",
        ("MICRO:0000175", "Trypticase"),
        SOURCE_318,
        _base_note("Trypticase", "0.500 g", "0.490196"),
    ),
    Component(
        "Resazurin",
        "0.000980",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_318,
        _base_note("Resazurin", "1.000 mg", "0.000980"),
    ),
    Component(
        "Cysteine-HCl x H2O",
        "0.294118",
        "G_PER_L",
        ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
        SOURCE_318,
        _base_note("Cysteine-HCl x H2O", "0.300 g", "0.294118"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.294118",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_318,
        _base_note("Na2S x 9 H2O", "0.300 g", "0.294118"),
    ),
    Component(
        "Nitrilotriacetic acid (NTA)",
        "0.125490",
        "G_PER_L",
        ("CHEBI:44557", "nitrilotriacetic acid"),
        SOURCE_318,
        _trace_note("Nitrilotriacetic acid", "12.800 g/L", "0.125490"),
    ),
    Component(
        "FeCl3 x 6 H2O",
        "0.013235",
        "G_PER_L",
        ("CHEBI:86254", "iron trichloride hexahydrate"),
        SOURCE_318,
        _trace_note("FeCl3 x 6 H2O", "1.350 g/L", "0.013235"),
    ),
    Component(
        "MnCl2 x 4 H2O",
        "0.000980",
        "G_PER_L",
        ("CHEBI:86368", "manganese(II) chloride tetrahydrate"),
        SOURCE_318,
        _trace_note("MnCl2 x 4 H2O", "0.100 g/L", "0.000980"),
    ),
    Component(
        "CoCl2 x 6 H2O",
        "0.000235",
        "G_PER_L",
        ("CHEBI:53503", "cobalt chloride hexahydrate"),
        SOURCE_318,
        _trace_note("CoCl2 x 6 H2O", "0.024 g/L", "0.000235"),
    ),
    Component(
        "ZnCl2",
        "0.000980",
        "G_PER_L",
        ("CHEBI:49976", "zinc dichloride"),
        SOURCE_318,
        _trace_note("ZnCl2", "0.100 g/L", "0.000980"),
    ),
    Component(
        "CuCl2 x 2 H2O",
        "0.000245",
        "G_PER_L",
        ("CHEBI:86318", "copper(II) chloride dihydrate"),
        SOURCE_318,
        _trace_note("CuCl2 x 2 H2O", "0.025 g/L", "0.000245"),
    ),
    Component(
        "H3BO3",
        "0.000098",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_318,
        _trace_note("H3BO3", "0.010 g/L", "0.000098"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.000235",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_318,
        _trace_note("Na2MoO4 x 2 H2O", "0.024 g/L", "0.000235"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.001176",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_318,
        _trace_note("NiCl2 x 6 H2O", "0.120 g/L", "0.001176"),
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "0.000255",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_318,
        _trace_note("Na2SeO3 x 5 H2O", "0.026 g/L", "0.000255"),
    ),
    Component(
        "Biotin",
        "0.000019608",
        "G_PER_L",
        ("CHEBI:15956", "Biotin"),
        SOURCE_141_VITAMINS,
        _vitamin_note("Biotin", "2.00 mg/L", "0.000019608"),
    ),
    Component(
        "Folic acid",
        "0.000019608",
        "G_PER_L",
        ("CHEBI:27470", "Folic acid"),
        SOURCE_141_VITAMINS,
        _vitamin_note("Folic acid", "2.00 mg/L", "0.000019608"),
    ),
    Component(
        "Pyridoxine-HCl",
        "0.000098",
        "G_PER_L",
        ("CHEBI:30961", "Pyridoxine hydrochloride"),
        SOURCE_141_VITAMINS,
        _vitamin_note("Pyridoxine-HCl", "10.00 mg/L", "0.000098"),
    ),
    Component(
        "Thiamine-HCl x 2 H2O",
        "0.000049",
        "G_PER_L",
        ("CHEBI:132751", "Thiamine-HCl x 2 H2O"),
        SOURCE_141_VITAMINS,
        _vitamin_note("Thiamine-HCl x 2 H2O", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "Riboflavin",
        "0.000049",
        "G_PER_L",
        ("CHEBI:17015", "Riboflavin"),
        SOURCE_141_VITAMINS,
        _vitamin_note("Riboflavin", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "Nicotinic acid",
        "0.000049",
        "G_PER_L",
        ("CHEBI:15940", "Nicotinic acid"),
        SOURCE_141_VITAMINS,
        _vitamin_note("Nicotinic acid", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "Calcium pantothenate",
        "0.000049",
        "G_PER_L",
        ("CHEBI:31345", "Calcium pantothenate"),
        SOURCE_141_VITAMINS,
        _vitamin_note("D-Ca-pantothenate", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "Vitamin B12",
        "0.000000980",
        "G_PER_L",
        ("CHEBI:176843", "Vitamin B12"),
        SOURCE_141_VITAMINS,
        _vitamin_note("Vitamin B12", "0.10 mg/L", "0.000000980"),
    ),
    Component(
        "p-Aminobenzoic acid",
        "0.000049",
        "G_PER_L",
        ("CHEBI:30753", "p-Aminobenzoic acid"),
        SOURCE_141_VITAMINS,
        _vitamin_note("p-Aminobenzoic acid", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "(DL)-alpha-Lipoic acid",
        "0.000049",
        "G_PER_L",
        ("CHEBI:16494", "(DL)-alpha-Lipoic acid"),
        SOURCE_141_VITAMINS,
        _vitamin_note("Lipoic acid", "5.00 mg/L", "0.000049"),
    ),
    Component(
        "KOH",
        "variable",
        "VARIABLE",
        ("CHEBI:32035", "potassium hydroxide"),
        SOURCE_318,
        (
            f"{SOURCE_318} adjusts the trace element solution to pH 6.5 "
            "with KOH."
        ),
    ),
    Component(
        "N2",
        "80",
        "PERCENT_V_V",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_318,
        f"{SOURCE_318} uses an 80% N2 and 20% CO2 gas phase.",
    ),
    Component(
        "CO2",
        "20",
        "PERCENT_V_V",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_318,
        f"{SOURCE_318} uses an 80% N2 and 20% CO2 gas phase.",
    ),
    Component(
        "Distilled water",
        "980.392157",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_318,
        (
            f"{SOURCE_318} lists 1000 mL water before 10 mL trace and 10 mL "
            "vitamin stock additions, yielding 980.392157 mL/L in the 1020 "
            "mL formulation after omitting methanol."
        ),
    ),
)


def _khco3(value: str, source: str) -> Component:
    return Component(
        "KHCO3",
        value,
        "G_PER_L",
        ("CHEBI:81862", "potassium hydrogencarbonate"),
        source,
        f"{source} sets KHCO3 to {value} g/L.",
    )


PELOBACTER_NOTES = (
    "DSMZ Medium 418 defines PELOBACTER MEDIUM as DSMZ Medium 318 with "
    "methanol omitted, KHCO3 increased to 4.5 g/L, and 10 mM sodium gallate "
    "added from a filter-sterilized anaerobic stock; this record expands "
    "the DSMZ Medium 318 trace element stock and the DSMZ Medium 141 vitamin "
    "stock into final per-liter components."
)

CLOSTRIDIUM_NOTES = (
    "DSMZ Medium 522 defines CLOSTRIDIUM NEOPROPIONICUM MEDIUM as DSMZ "
    "Medium 318 with 4.0 g/L KHCO3 for pH 7.0 and 1.0 g/L ethanol replacing "
    "methanol; this record expands the DSMZ Medium 318 trace element stock "
    "and the DSMZ Medium 141 vitamin stock into final per-liter components."
)


TARGETS: tuple[Target, ...] = (
    Target(
        path=PELOBACTER,
        expected_id="CultureMech:005242",
        expected_media_term="komodo.medium:418",
        ph_value=7.3,
        khco3_value="4.500000",
        branch_components=(
            Component(
                "sodium gallate",
                "10",
                "MILLIMOLAR",
                ("CHEBI:115197", "sodium gallate"),
                SOURCE_418,
                (
                    f"{SOURCE_418} adds sodium gallate from a "
                    "filter-sterilized anaerobic stock solution to a final "
                    "concentration of 10 mM."
                ),
            ),
        ),
        preparation_steps=(
            "Prepare DSMZ Medium 318 without methanol and with KHCO3 at 4.5 g/L.",
            "Prepare the medium under an 80% N2 and 20% CO2 gas phase.",
            "Add vitamins, cysteine-HCl, sulfide, and sodium gallate from sterile anoxic stocks.",
            "Adjust final pH to 7.3.",
        ),
        notes=PELOBACTER_NOTES,
        references=(KOMODO_418_URL, DSMZ_418_URL, DSMZ_318_URL, DSMZ_141_URL),
    ),
    Target(
        path=CLOSTRIDIUM_NEOPROPIONICUM,
        expected_id="CultureMech:005884",
        expected_media_term="komodo.medium:522",
        ph_value=7.0,
        khco3_value="4.000000",
        branch_components=(
            Component(
                "Ethanol",
                "1.0",
                "G_PER_L",
                ("CHEBI:16236", "ethanol"),
                SOURCE_522,
                f"{SOURCE_522} replaces methanol with 1.0 g/L ethanol.",
            ),
        ),
        preparation_steps=(
            "Prepare DSMZ Medium 318 without methanol and with KHCO3 at 4.0 g/L.",
            "Add ethanol to 1.0 g/L.",
            "Prepare the medium under an 80% N2 and 20% CO2 gas phase.",
            "Sterilize vitamins, cysteine-HCl, and sulfide separately.",
            "Adjust final pH to 7.0.",
        ),
        notes=CLOSTRIDIUM_NOTES,
        references=(KOMODO_522_URL, DSMZ_522_URL, DSMZ_318_URL, DSMZ_141_URL),
    ),
)

TARGET_BY_PATH = {target.path: target for target in TARGETS}


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


def _check_source(doc: dict[str, Any], target: Target) -> None:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected immutable id {target.expected_id}, "
            f"found {doc.get('id')!r}"
        )

    source_term = _source_term_id(doc)
    if source_term != target.expected_media_term:
        raise ValueError(
            f"{target.path}: found source term {source_term!r}, "
            f"expected {target.expected_media_term!r}"
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


def _ensure_flags(doc: dict[str, Any], target: Target) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError(f"{target.path}: data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "missing_composition",
        "placeholder_composition",
        "source_information_unavailable",
    ):
        while obsolete in flags:
            flags.remove(obsolete)

    for flag in ("has_ontology_mappings", "ingredients_curated"):
        if flag not in flags:
            flags.append(flag)

    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], target: Target) -> None:
    doc["references"] = [{"reference": url} for url in target.references]


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": target.references[1],
        "notes": target.notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{target.path}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _ingredient(component: Component) -> dict[str, Any]:
    ingredient = {
        "preferred_term": component.preferred_term,
        "source": component.source,
        "notes": component.notes,
        "concentration": {"value": component.value, "unit": component.unit},
        "term": _term(*component.term),
    }
    if component.term[0].startswith("CHEBI:"):
        ingredient["mediaingredientmech_chebi_term"] = _term(*component.term)
    return ingredient


def _mix_step(step_number: int, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": "MIX",
        "description": description,
    }


def components_for(target: Target) -> tuple[Component, ...]:
    return (
        *COMMON_COMPONENTS[:8],
        _khco3(target.khco3_value, SOURCE_418 if target.path == PELOBACTER else SOURCE_522),
        *COMMON_COMPONENTS[8:],
        *target.branch_components,
    )


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    _check_source(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ph_value"] = target.ph_value
    repaired.pop("ph_range", None)
    repaired["ingredients"] = [
        _ingredient(component) for component in components_for(target)
    ]
    repaired["preparation_steps"] = [
        _mix_step(index, step)
        for index, step in enumerate(target.preparation_steps, start=1)
    ]
    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired, target)
    _ensure_references(repaired, target)
    _ensure_event(repaired, target)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for target in TARGETS:
        path = normalized / target.path
        plans[path] = repair_record(_load(path), target)
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
