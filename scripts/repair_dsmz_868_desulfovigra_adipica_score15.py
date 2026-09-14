#!/usr/bin/env python3
"""Repair archived DSMZ Medium 868 Desulfovigra adipica."""

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
TARGET = Path("bacterial/desulfovigra_adipica.yaml")
EXPECTED_ID = "CultureMech:006698"
EXPECTED_MEDIA_TERM = "komodo.medium:868"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_dsmz_868_desulfovigra_adipica_score15.py"
ACTION = "RESOLVED_DSMZ_868_DESULFOVIGRA_ADIPICA_SCORE15"
TIMESTAMP = "2026-09-11T00:00:00-07:00"

ARCHIVED_DSMZ_868 = (
    "https://web.archive.org/web/20121030083126id_/"
    "http://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium868.pdf"
)
SOURCE = "Archived DSMZ Medium 868"
TITLE = "DESULFOVIGRA ADIPICA"

Component = tuple[str, str, str]
SolutionSignature = tuple[str, str, str, tuple[Component, ...]]

IMPORTED_INGREDIENT_SIGNATURE: tuple[Component, ...] = (
    ("Na2CO3", "variable", "VARIABLE"),
)
FINAL_INGREDIENT_SIGNATURE: tuple[Component, ...] = ()

NA2SO4_STOCK_SIGNATURE: tuple[Component, ...] = (("Na2SO4", "100.0", "G_PER_L"),)
YEAST_EXTRACT_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Yeast extract", "100.0", "G_PER_L"),
)
NAHCO3_STOCK_SIGNATURE: tuple[Component, ...] = (("NaHCO3", "50.0", "G_PER_L"),)
PROPANOL_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Propanol", "10.0", "PERCENT_V_V"),
)
NA2S_STOCK_SIGNATURE: tuple[Component, ...] = (
    ("Na2S x 9H2O", "30.0", "G_PER_L"),
)

FINAL_SOLUTION_SIGNATURES: tuple[SolutionSignature, ...] = (
    ("10% (w/v) Na2SO4 solution", "7.0", "ML_PER_L", NA2SO4_STOCK_SIGNATURE),
    (
        "10% (w/v) Yeast extract solution",
        "10.0",
        "ML_PER_L",
        YEAST_EXTRACT_STOCK_SIGNATURE,
    ),
    (
        "Trace element solution SL-10 (DSMZ Medium 320)",
        "1.0",
        "ML_PER_L",
        (),
    ),
    ("5% (w/v) NaHCO3 solution", "50.0", "ML_PER_L", NAHCO3_STOCK_SIGNATURE),
    (
        "Selenite-tungstate solution (DSMZ Medium 385)",
        "1.0",
        "ML_PER_L",
        (),
    ),
    ("Vitamin solution (DSMZ Medium 141)", "10.0", "ML_PER_L", ()),
    ("10% (v/v) Propanol solution", "1.0", "ML_PER_L", PROPANOL_STOCK_SIGNATURE),
    ("3% (w/v) Na2S x 9H2O solution", "17.0", "ML_PER_L", NA2S_STOCK_SIGNATURE),
)

PH_RANGE = {"min": 7.0, "max": 7.2}
REFERENCES = (ARCHIVED_DSMZ_868,)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Na2SO4": ("CHEBI:32149", "sodium sulfate"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "Propanol": ("CHEBI:28831", "Propan-1-ol"),
    "Yeast extract": ("FOODON:03315426", "yeast extract"),
}

NOTES = (
    "Archived DSMZ Medium 868 lists Desulfovigra adipica as basal DSMZ "
    "Medium 503 supplemented per liter with 7.0 ml 10% Na2SO4, 10.0 ml 10% "
    "yeast extract, 1.0 ml trace element solution from DSMZ Medium 320, "
    "50.0 ml 5% NaHCO3, 1.0 ml selenite-tungstate solution from DSMZ Medium "
    "385, 10.0 ml vitamin solution from DSMZ Medium 141, 1.0 ml 10% "
    "propanol, and 17.0 ml 3% Na2S x 9H2O from sterile anaerobic stock "
    "solutions. The sheet states to adjust the completed medium to pH "
    "7.0-7.2 with sterile anaerobic 5% Na2CO3 and to feed the same amount "
    "of propanol again after growth starts."
)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str, notes: str) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": SOURCE,
        "notes": notes,
    }

    identifier, label = GROUNDINGS[preferred_term]
    row["term"] = _term(identifier, label)
    if identifier.startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = _term(identifier, label)
    return row


def _solution(
    preferred_term: str,
    value: str,
    components: tuple[dict[str, Any], ...],
    notes: str,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "composition": copy.deepcopy(list(components)),
        "source": SOURCE,
        "notes": notes,
    }
    return row


SOLUTIONS: tuple[dict[str, Any], ...] = (
    _solution(
        "10% (w/v) Na2SO4 solution",
        "7.0",
        (
            _component(
                "Na2SO4",
                "100.0",
                "G_PER_L",
                "Solute concentration for DSMZ Medium 868 10% (w/v) Na2SO4 stock.",
            ),
        ),
        "DSMZ Medium 868 adds 7.0 ml/L sterile anaerobic 10% Na2SO4 stock.",
    ),
    _solution(
        "10% (w/v) Yeast extract solution",
        "10.0",
        (
            _component(
                "Yeast extract",
                "100.0",
                "G_PER_L",
                "Solute concentration for DSMZ Medium 868 10% (w/v) yeast extract stock.",
            ),
        ),
        "DSMZ Medium 868 adds 10.0 ml/L sterile anaerobic 10% yeast extract stock.",
    ),
    _solution(
        "Trace element solution SL-10 (DSMZ Medium 320)",
        "1.0",
        (),
        "DSMZ Medium 868 adds 1.0 ml/L sterile anaerobic trace element solution from DSMZ Medium 320.",
    ),
    _solution(
        "5% (w/v) NaHCO3 solution",
        "50.0",
        (
            _component(
                "NaHCO3",
                "50.0",
                "G_PER_L",
                "Solute concentration for DSMZ Medium 868 5% (w/v) NaHCO3 stock.",
            ),
        ),
        "DSMZ Medium 868 adds 50.0 ml/L sterile anaerobic 5% NaHCO3 stock.",
    ),
    _solution(
        "Selenite-tungstate solution (DSMZ Medium 385)",
        "1.0",
        (),
        "DSMZ Medium 868 adds 1.0 ml/L sterile anaerobic selenite-tungstate solution from DSMZ Medium 385.",
    ),
    _solution(
        "Vitamin solution (DSMZ Medium 141)",
        "10.0",
        (),
        "DSMZ Medium 868 adds 10.0 ml/L sterile anaerobic vitamin solution from DSMZ Medium 141.",
    ),
    _solution(
        "10% (v/v) Propanol solution",
        "1.0",
        (
            _component(
                "Propanol",
                "10.0",
                "PERCENT_V_V",
                "Solute proportion for DSMZ Medium 868 10% (v/v) propanol stock.",
            ),
        ),
        "DSMZ Medium 868 adds 1.0 ml/L sterile anaerobic 10% propanol stock.",
    ),
    _solution(
        "3% (w/v) Na2S x 9H2O solution",
        "17.0",
        (
            _component(
                "Na2S x 9H2O",
                "30.0",
                "G_PER_L",
                "Solute concentration for DSMZ Medium 868 3% (w/v) Na2S x 9H2O stock.",
            ),
        ),
        "DSMZ Medium 868 adds 17.0 ml/L sterile anaerobic 3% Na2S x 9H2O stock.",
    ),
)

PREPARATION_STEPS: tuple[dict[str, Any], ...] = (
    {
        "step_number": 1,
        "action": "MIX",
        "description": (
            "Use basal DSMZ Medium 503 and add the Na2SO4, yeast extract, "
            "trace element, NaHCO3, selenite-tungstate, vitamin, propanol, "
            "and Na2S x 9H2O supplements from sterile anaerobic stock "
            "solutions at the listed amounts per liter."
        ),
    },
    {
        "step_number": 2,
        "action": "ADJUST_PH",
        "description": (
            "After completing the medium, adjust to pH 7.0-7.2 with sterile "
            "anaerobic 5% Na2CO3."
        ),
    },
    {
        "step_number": 3,
        "action": "MIX",
        "description": "When growth has started, feed the same amount of propanol again.",
    },
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


def _ingredient_signature(rows: Any) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, (list, tuple)):
        raise ValueError("ingredients is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("ingredients contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"ingredient {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _component_signature(rows: Any) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
        raise ValueError("solution composition is not a list")

    signature: list[Component] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("solution composition contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"component {row.get('preferred_term')!r} lacks concentration")
        signature.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
            )
        )
    return tuple(signature)


def _solution_signatures(rows: Any) -> tuple[SolutionSignature, ...]:
    if not isinstance(rows, list):
        raise ValueError("solutions is not a list")

    signatures: list[SolutionSignature] = []
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("solutions contains a non-mapping row")
        concentration = row.get("concentration")
        if not isinstance(concentration, dict):
            raise ValueError(f"solution {row.get('preferred_term')!r} lacks concentration")
        signatures.append(
            (
                str(row.get("preferred_term") or ""),
                str(concentration.get("value") or ""),
                str(concentration.get("unit") or ""),
                _component_signature(row.get("composition")),
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


def _ensure_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != EXPECTED_ID:
        raise ValueError(f"{TARGET}: expected id {EXPECTED_ID}, found {doc.get('id')!r}")
    if _source_term_id(doc) != EXPECTED_MEDIA_TERM:
        raise ValueError(f"{TARGET}: expected media term {EXPECTED_MEDIA_TERM}")

    ingredient_signature = _ingredient_signature(doc.get("ingredients"))
    if ingredient_signature not in (
        IMPORTED_INGREDIENT_SIGNATURE,
        FINAL_INGREDIENT_SIGNATURE,
    ):
        raise ValueError(
            f"{TARGET}: ingredient signature drifted from "
            f"{IMPORTED_INGREDIENT_SIGNATURE!r} to {ingredient_signature!r}"
        )

    if ingredient_signature == FINAL_INGREDIENT_SIGNATURE:
        solution_signatures = _solution_signatures(doc.get("solutions"))
        if solution_signatures != FINAL_SOLUTION_SIGNATURES:
            raise ValueError(
                f"{TARGET}: solution signature drifted from "
                f"{FINAL_SOLUTION_SIGNATURES!r} to {solution_signatures!r}"
            )


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in (
        "incomplete_composition",
        "legacy_source_url_unavailable",
        "needs_manual_curation",
        "source_information_unavailable",
    ):
        if obsolete in flags:
            flags.remove(obsolete)
    for flag in (
        "has_ontology_mappings",
        "has_unmapped_ingredients",
        "ingredients_curated",
    ):
        if flag not in flags:
            flags.append(flag)


def _ensure_references(doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for url in REFERENCES:
        if url not in existing:
            references.append({"reference": url})


def _append_curation_event(doc: dict[str, Any]) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(REFERENCES),
        "notes": (
            f"{NOTES} Replaced the KOMODO pH-buffer placeholder with the "
            "archived DSMZ supplement list and removed a stale kg_microbe_match "
            "to MediaDive 634c."
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
    _ensure_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "LIQUID"
    _put_after(repaired, "ph_range", copy.deepcopy(PH_RANGE), "physical_state")
    _put_after(repaired, "notes", NOTES, "media_term")
    repaired["ingredients"] = []
    _put_after(repaired, "solutions", copy.deepcopy(list(SOLUTIONS)), "ingredients")
    repaired["preparation_steps"] = copy.deepcopy(list(PREPARATION_STEPS))
    repaired.pop("ph_value", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    repaired.pop("kg_microbe_match", None)
    _ensure_flags(repaired)
    _ensure_references(repaired)
    _append_curation_event(repaired)
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
