#!/usr/bin/env python3
"""Repair empty KOMODO 304 METHANOSARCINA ACETIVORANS records."""

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

KOMODO_304_URL = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=304"
)
KOMODO_304_REPLACE_URL = (
    "https://komodo.modelseed.org/servlet/"
    "KomodoTomcatServerSideUtilitiesModelSeed"
    "?MediaInfo=304_replace_Trimethylamine-HCl_with_Methanol"
)
DSMZ_304_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium304.pdf"
)
DSMZ_141_URL = (
    "https://web.archive.org/web/20121030082653id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium141.pdf"
)

SOURCE_304 = "Archived DSMZ Medium 304"
SOURCE_141 = "Archived DSMZ Medium 141 trace element solution"

CURATOR = "repair_komodo_304_score30.py"
ACTION = "RESOLVED_KOMODO_304_SCORE30"
TIMESTAMP = "2026-09-10T00:00:00-07:00"
NOTES_BASE = (
    "Archived DSMZ Medium 304 defines METHANOSARCINA ACETIVORANS MEDIUM with "
    "base salts, yeast extract, 10 mL DSMZ Medium 141 trace element solution, "
    "resazurin, trimethylamine hydrochloride or methanol, cysteine "
    "hydrochloride hydrate, sodium sulfide nonahydrate, 80:20 N2/CO2, and pH "
    "7.0; the live KOMODO Medium 304 table selects the trimethylamine "
    "hydrochloride branch."
)
NOTES_REPLACE = (
    "Archived DSMZ Medium 304 defines METHANOSARCINA ACETIVORANS MEDIUM with "
    "base salts, yeast extract, 10 mL DSMZ Medium 141 trace element solution, "
    "resazurin, trimethylamine hydrochloride or methanol, cysteine "
    "hydrochloride hydrate, sodium sulfide nonahydrate, 80:20 N2/CO2, and pH "
    "7.0; the live KOMODO replacement table selects the methanol branch."
)


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
    branch_component: Component
    notes: str
    references: tuple[str, ...]


def _main_note(name: str, amount: str, value: str) -> str:
    return (
        f"{SOURCE_304} lists {amount} {name} and 10 mL of trace element "
        f"solution in 1000 mL water, yielding {value} g/L in the 1010 mL "
        "final formulation."
    )


def _combined_note(name: str, base: str, stock: str, value: str) -> str:
    return (
        f"{SOURCE_304} lists {base} {name} and adds 10 mL of the "
        f"{SOURCE_141} containing {stock} {name} to 1000 mL water, yielding "
        f"{value} g/L in the 1010 mL final formulation."
    )


def _trace_note(name: str, stock_amount: str, value: str) -> str:
    return (
        f"{SOURCE_304} adds 10 mL of the {SOURCE_141} to 1000 mL water; "
        f"the stock contains {stock_amount} {name}, yielding {value} g/L "
        "in the 1010 mL final formulation."
    )


COMMON_COMPONENTS: tuple[Component, ...] = (
    Component(
        "NaCl",
        "23.178218",
        "G_PER_L",
        ("CHEBI:26710", "sodium chloride"),
        SOURCE_304,
        _combined_note("NaCl", "23.40 g", "1.00 g/L", "23.178218"),
    ),
    Component(
        "MgSO4 x 7 H2O",
        "9.386139",
        "G_PER_L",
        ("CHEBI:31795", "magnesium sulfate heptahydrate"),
        SOURCE_304,
        _combined_note("MgSO4 x 7 H2O", "9.45 g", "3.00 g/L", "9.386139"),
    ),
    Component(
        "Na2CO3",
        "4.950495",
        "G_PER_L",
        ("CHEBI:29377", "sodium carbonate"),
        SOURCE_304,
        _main_note("Na2CO3", "5.00 g", "4.950495"),
    ),
    Component(
        "Yeast extract",
        "0.990099",
        "G_PER_L",
        ("FOODON:03315426", "yeast extract"),
        SOURCE_304,
        _main_note("Yeast extract", "1.00 g", "0.990099"),
    ),
    Component(
        "NH4Cl",
        "0.990099",
        "G_PER_L",
        ("CHEBI:31206", "ammonium chloride"),
        SOURCE_304,
        _main_note("NH4Cl", "1.00 g", "0.990099"),
    ),
    Component(
        "KCl",
        "0.792079",
        "G_PER_L",
        ("CHEBI:32588", "potassium chloride"),
        SOURCE_304,
        _main_note("KCl", "0.80 g", "0.792079"),
    ),
    Component(
        "CaCl2 x 2 H2O",
        "0.139604",
        "G_PER_L",
        ("CHEBI:86158", "calcium chloride dihydrate"),
        SOURCE_304,
        _combined_note("CaCl2 x 2 H2O", "0.14 g", "0.10 g/L", "0.139604"),
    ),
    Component(
        "Na2HPO4",
        "0.594059",
        "G_PER_L",
        ("CHEBI:34683", "disodium hydrogenphosphate"),
        SOURCE_304,
        _main_note("Na2HPO4", "0.60 g", "0.594059"),
    ),
    Component(
        "Nitrilotriacetic acid",
        "0.014851",
        "G_PER_L",
        ("CHEBI:44557", "nitrilotriacetic acid"),
        SOURCE_141,
        _trace_note("Nitrilotriacetic acid", "1.50 g/L", "0.014851"),
    ),
    Component(
        "MnSO4 x H2O",
        "0.004950",
        "G_PER_L",
        ("CHEBI:86364", "manganese(II) sulfate monohydrate"),
        SOURCE_141,
        _trace_note("MnSO4 x H2O", "0.50 g/L", "0.004950"),
    ),
    Component(
        "FeSO4 x 7 H2O",
        "0.000990",
        "G_PER_L",
        ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("FeSO4 x 7 H2O", "0.10 g/L", "0.000990"),
    ),
    Component(
        "CoSO4 x 7 H2O",
        "0.001782",
        "G_PER_L",
        ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("CoSO4 x 7 H2O", "0.18 g/L", "0.001782"),
    ),
    Component(
        "ZnSO4 x 7 H2O",
        "0.001782",
        "G_PER_L",
        ("CHEBI:32312", "zinc sulfate heptahydrate"),
        SOURCE_141,
        _trace_note("ZnSO4 x 7 H2O", "0.18 g/L", "0.001782"),
    ),
    Component(
        "CuSO4 x 5 H2O",
        "0.0000990",
        "G_PER_L",
        ("CHEBI:31440", "copper(II) sulfate pentahydrate"),
        SOURCE_141,
        _trace_note("CuSO4 x 5 H2O", "0.01 g/L", "0.0000990"),
    ),
    Component(
        "KAl(SO4)2 x 12 H2O",
        "0.000198",
        "G_PER_L",
        ("CHEBI:86465", "potassium aluminium sulfate dodecahydrate"),
        SOURCE_141,
        _trace_note("KAl(SO4)2 x 12 H2O", "0.02 g/L", "0.000198"),
    ),
    Component(
        "H3BO3",
        "0.0000990",
        "G_PER_L",
        ("CHEBI:33118", "boric acid"),
        SOURCE_141,
        _trace_note("H3BO3", "0.01 g/L", "0.0000990"),
    ),
    Component(
        "Na2MoO4 x 2 H2O",
        "0.0000990",
        "G_PER_L",
        ("CHEBI:75213", "sodium molybdate dihydrate"),
        SOURCE_141,
        _trace_note("Na2MoO4 x 2 H2O", "0.01 g/L", "0.0000990"),
    ),
    Component(
        "NiCl2 x 6 H2O",
        "0.000297",
        "G_PER_L",
        ("CHEBI:53542", "nickel chloride hexahydrate"),
        SOURCE_141,
        _trace_note("NiCl2 x 6 H2O", "0.03 g/L", "0.000297"),
    ),
    Component(
        "Na2SeO3 x 5 H2O",
        "0.000002970",
        "G_PER_L",
        ("CHEBI:131361", "disodium selenite pentahydrate"),
        SOURCE_141,
        _trace_note("Na2SeO3 x 5 H2O", "0.30 mg/L", "0.000002970"),
    ),
    Component(
        "Resazurin",
        "0.000990",
        "G_PER_L",
        ("CHEBI:8806", "Resazurin"),
        SOURCE_304,
        _main_note("Resazurin", "1.00 mg", "0.000990"),
    ),
    Component(
        "Cysteine-HCl x H2O",
        "0.247525",
        "G_PER_L",
        ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
        SOURCE_304,
        _main_note("Cysteine-HCl x H2O", "0.25 g", "0.247525"),
    ),
    Component(
        "Na2S x 9 H2O",
        "0.247525",
        "G_PER_L",
        ("CHEBI:76209", "sodium sulfide nonahydrate"),
        SOURCE_304,
        _main_note("Na2S x 9 H2O", "0.25 g", "0.247525"),
    ),
    Component(
        "HCl",
        "variable",
        "VARIABLE",
        ("CHEBI:17883", "hydrogen chloride"),
        SOURCE_304,
        f"{SOURCE_304} adjusts the final medium to pH 7.0 with hydrochloric acid.",
    ),
    Component(
        "KOH",
        "variable",
        "VARIABLE",
        ("CHEBI:32035", "potassium hydroxide"),
        SOURCE_141,
        f"{SOURCE_141} adjusts the trace element solution with KOH.",
    ),
    Component(
        "N2",
        "variable",
        "VARIABLE",
        ("CHEBI:17997", "dinitrogen"),
        SOURCE_304,
        f"{SOURCE_304} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "CO2",
        "variable",
        "VARIABLE",
        ("CHEBI:16526", "carbon dioxide"),
        SOURCE_304,
        f"{SOURCE_304} prepares the medium under 80% N2 and 20% CO2.",
    ),
    Component(
        "Distilled water",
        "1000.000",
        "ML_PER_L",
        ("CHEBI:15377", "water"),
        SOURCE_304,
        f"{SOURCE_304} lists 1000 mL distilled water before the trace addition.",
    ),
)


def _branch_component(name: str, value: str, term: tuple[str, str]) -> Component:
    return Component(
        name,
        value,
        "G_PER_L",
        term,
        SOURCE_304,
        (
            f"{SOURCE_304} lists {name} as an alternative substrate for the "
            f"medium and live KOMODO selects this branch, yielding {value} "
            "g/L in the 1010 mL final formulation."
        ),
    )


TARGETS: tuple[Target, ...] = (
    Target(
        "archaea/KOMODO_304_METHANOSARCINA_ACETIVORANS_medium.yaml",
        "CultureMech:004832",
        "komodo.medium:304",
        _branch_component(
            "Trimethylamine-HCl",
            "2.970297",
            ("CHEBI:64700", "trimethylamine hydrochloride"),
        ),
        NOTES_BASE,
        (KOMODO_304_URL, DSMZ_304_URL, DSMZ_141_URL),
    ),
    Target(
        "archaea/methanosarcina_acetivorans_medium_replace_trimethylamine_hcl_with_methanol.yaml",
        "CultureMech:004821",
        "komodo.medium:304_replace_Trimethylamine-HCl_with_Methanol",
        _branch_component("Methanol", "4.950495", ("CHEBI:17790", "methanol")),
        NOTES_REPLACE,
        (KOMODO_304_REPLACE_URL, DSMZ_304_URL, DSMZ_141_URL),
    ),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _check_source(doc: dict[str, Any], target: Target) -> None:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{target.path}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != target.expected_media_term:
        raise ValueError(
            f"{target.path}: missing expected media term " f"{target.expected_media_term}"
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
    doc["references"] = [{"reference": reference} for reference in target.references]


def _ensure_event(doc: dict[str, Any], target: Target) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": DSMZ_304_URL,
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


def repair_record(doc: dict[str, Any], target: Target) -> dict[str, Any]:
    if doc.get("id") != target.expected_id:
        raise ValueError(
            f"{target.path}: expected immutable id {target.expected_id}, "
            f"found {doc.get('id')!r}"
        )
    _check_source(doc, target)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_value", 7.0, "physical_state")
    repaired["ingredients"] = [
        _ingredient(component)
        for component in (*COMMON_COMPONENTS[:-5], target.branch_component, *COMMON_COMPONENTS[-5:])
    ]
    _put_after(repaired, "notes", target.notes, "media_term")
    _ensure_flags(repaired, target)
    _ensure_references(repaired, target)
    _ensure_event(repaired, target)
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
