#!/usr/bin/env python3
"""Repair the empty KOMODO 532 Methanogenium sp. medium record."""

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
TARGET = "archaea/methanogenium_sp_medium.yaml"
EXPECTED_ID = "CultureMech:005910"
EXPECTED_MEDIA_TERM = "komodo.medium:532"
SOURCE_URL = (
    "https://komodo.modelseed.org/servlet/" "KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=532"
)
SOURCE_NAME = "KOMODO MediaInfo 532"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_komodo_532_score35.py"
ACTION = "RESOLVED_KOMODO_532_SCORE35"
TIMESTAMP = "2026-09-10T00:00:00-07:00"

NOTES = (
    "KOMODO MediaInfo 532 lists 27 quantified g/L components for "
    "METHANOGENIUM SP. medium and also lists CO2, H2O, H2, distilled water, "
    "and NaOH without gram or mol amounts."
)

KOMODO_532_COMPONENTS: tuple[tuple[str, str | None, tuple[str, str] | None], ...] = (
    ("KH2PO4", "0.49", ("CHEBI:63036", "potassium dihydrogen phosphate")),
    ("CoCl2 x 6 H2O", "1.87E-4", ("CHEBI:53503", "cobalt chloride hexahydrate")),
    ("HCl", "6.65E-4", ("CHEBI:17883", "hydrogen chloride")),
    ("CaCl2 x 2 H2O", "0.05", ("CHEBI:86158", "calcium chloride dihydrate")),
    ("Na2S x 9 H2O", "0.49", ("CHEBI:76209", "sodium sulfide nonahydrate")),
    ("ZnCl2", "6.91E-5", ("CHEBI:49976", "zinc dichloride")),
    ("2-Methylbutyric acid", "0.49", ("CHEBI:37070", "2-methylbutyric acid")),
    ("NH4Cl", "0.40", ("CHEBI:31206", "ammonium chloride")),
    ("CO2", None, ("CHEBI:16526", "carbon dioxide")),
    ("CuCl2 x 2 H2O", "1.97E-6", ("CHEBI:86318", "copper(II) chloride dihydrate")),
    ("Na2MoO4 x 2 H2O", "3.55E-5", ("CHEBI:75213", "sodium molybdate dihydrate")),
    ("H3BO3", "5.92E-6", ("CHEBI:33118", "boric acid")),
    ("NiCl2 x 6 H2O", "2.52E-3", ("CHEBI:53542", "nickel chloride hexahydrate")),
    ("Isovaleric acid", "0.49", ("CHEBI:28484", "isovaleric acid")),
    ("Isobutyric acid", "0.49", ("CHEBI:16135", "isobutyric acid")),
    ("MgSO4 x 7 H2O", "0.40", ("CHEBI:31795", "magnesium sulfate heptahydrate")),
    ("H2O", None, ("CHEBI:15377", "water")),
    ("Cysteine-HCl x H2O", "0.49", ("CHEBI:91248", "L-cysteine hydrochloride hydrate")),
    ("Resazurin", "9.89E-4", ("CHEBI:8806", "Resazurin")),
    ("Na-formate", "1.98", ("CHEBI:62965", "sodium formate")),
    ("NaHCO3", "3.96", ("CHEBI:32139", "sodium hydrogencarbonate")),
    ("Yeast extract", "1.19", ("FOODON:03315426", "yeast extract")),
    ("MnCl2 x 4 H2O", "9.87E-5", ("CHEBI:86368", "manganese(II) chloride tetrahydrate")),
    ("Valeric acid", "0.49", ("CHEBI:17418", "valeric acid")),
    ("Na-acetate", "0.99", ("CHEBI:32954", "sodium acetate")),
    ("FeSO4 x 7 H2O", "1.98E-3", ("CHEBI:75836", "iron(2+) sulfate heptahydrate")),
    ("H2", None, ("CHEBI:18276", "dihydrogen")),
    ("Distilled water", None, ("CHEBI:15377", "water")),
    ("NaCl", "5.40", ("CHEBI:26710", "sodium chloride")),
    ("FeCl2 x 4 H2O", "1.48E-3", ("CHEBI:86249", "iron dichloride tetrahydrate")),
    ("NaOH", None, ("CHEBI:32145", "sodium hydroxide")),
    ("sludge from an anaerobic digester", "49.46", None),
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _check_source(doc: dict[str, Any]) -> None:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        raise ValueError(f"{TARGET}: missing media_term")
    term = media_term.get("term")
    if not isinstance(term, dict) or term.get("id") != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: missing expected media term {EXPECTED_MEDIA_TERM}")


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
        raise ValueError(f"{TARGET}: data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in ("has_ontology_mappings", "ingredients_curated", "has_unmapped_ingredients"):
        if flag not in flags:
            flags.append(flag)


def _ensure_reference(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError(f"{TARGET}: references is not a list")

    found = {row.get("reference") for row in references if isinstance(row, dict)}
    if SOURCE_URL not in found:
        references.append({"reference": SOURCE_URL})


def _ensure_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Replaced empty KOMODO 532 composition with live KOMODO MediaInfo data",
        "source": SOURCE_URL,
        "notes": NOTES,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError(f"{TARGET}: curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == ACTION
        ):
            history[index] = event
            return
    history.append(event)


def _source_note(preferred_term: str, value: str | None) -> str:
    if value is None:
        return f"{SOURCE_NAME} lists {preferred_term} without a gram or mol amount."
    return f"{SOURCE_NAME} lists {value} g/L {preferred_term}."


def _ingredient(
    preferred_term: str,
    value: str | None,
    term: tuple[str, str] | None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "source": SOURCE_NAME,
        "notes": _source_note(preferred_term, value),
    }
    if value is not None:
        row["concentration"] = {"value": value, "unit": "G_PER_L"}
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    return row


def repair_record(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected immutable id {EXPECTED_ID}, found {doc.get('id')!r}")
    _check_source(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    repaired["ingredients"] = [_ingredient(*component) for component in KOMODO_532_COMPONENTS]
    _put_after(repaired, "notes", NOTES, "media_term")
    _ensure_flags(repaired)
    _ensure_reference(repaired)
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
