#!/usr/bin/env python3
"""Repair flat JCM score-10 stock-solution imports."""

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
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

Component = tuple[str, str, str]

TARGETS = {
    Path("archaea/JCM_J1334_NATRONOARCHAEA_MEDIUM_II.yaml"): {
        "id": "CultureMech:015832",
        "source_id": "jcm.grmd:1334",
    },
    Path("bacterial/JCM_J1359_MINERAL_CARBONATE_MEDIUM_WITH_CASEIN_PEPTONE.yaml"): {
        "id": "CultureMech:015839",
        "source_id": "jcm.grmd:1359",
    },
    Path("bacterial/JCM_J1392_ATRIBACTEROTA_M15_MEDIUM.yaml"): {
        "id": "CultureMech:015850",
        "source_id": "jcm.grmd:1392",
    },
    Path("bacterial/JCM_J1405_THIOHALORHABDUS_METHYLOTROPHUS_MEDIUM.yaml"): {
        "id": "CultureMech:015855",
        "source_id": "jcm.grmd:1405",
    },
}

IMPORTED_SIGNATURES: dict[Path, tuple[str, ...]] = {
    Path("archaea/JCM_J1334_NATRONOARCHAEA_MEDIUM_II.yaml"): (
        "Neutral base salt medium (see below)",
        "Base soda medium (see Medium No. 1207 )",
        "1 M MgCl2 solution",
        "Trace vitamins* (see Medium No. 197 )",
        "Trace element solution (see Medium No. 1079 )",
        "Se/W solution (see Medium No. 852 )",
        "10% Yeast extract solution",
        "10% Soluble starch solution",
        "NaCl",
        "KCl",
        "K2HPO4",
        "NH4Cl",
        "(NH4)2SO4",
    ),
    Path("bacterial/JCM_J1359_MINERAL_CARBONATE_MEDIUM_WITH_CASEIN_PEPTONE.yaml"): (
        "Na2CO3",
        "NaHCO3",
        "NaCl",
        "K2HPO4",
        "Yeast extract",
        "1 M MgSO4solution",
        "1 M NH4Cl solution",
        "Trace element solution (see Medium No. 1079 )",
        "Se/W solution* (see Medium No. 852 )",
        "Trace vitamins* (see Medium No. 197 )",
        "10% Casein peptone solution",
    ),
    Path("bacterial/JCM_J1392_ATRIBACTEROTA_M15_MEDIUM.yaml"): (
        "NaCl",
        "MgCl2\u00b76H2O",
        "CaCl2\u00b72H2O",
        "NH4Cl",
        "KH2PO4",
        "Trace element solution (see Medium No. 439 )",
        "Resazurin",
        "Distilled water",
        "Selenite-tungstate solution (see Medium No. 431 )",
        "8% NaHCO3 solution",
        "Vitamin solution (see Medium No. 403 )",
        "Thiamine solution (see Medium No. 403 )",
        "Vitamin B12 solution (see Medium No. 403 )",
        "10% Yeast extract solution",
        "5% Na2S\u00b79H2O solution",
    ),
    Path("bacterial/JCM_J1405_THIOHALORHABDUS_METHYLOTROPHUS_MEDIUM.yaml"): (
        "NaCl",
        "KCl",
        "K2HPO4",
        "NH4Cl",
        "1 M MgSO4 solution",
        "Trace element solution (see Medium No. 1079 )",
        "0.002% CuCl2\u00b72H2O solution",
        "Trace vitamins* (see Medium No. 197 )",
        "3% Trimethylamine solution*",
        "2 M Sodium thiosulfate solution*",
    ),
}

GROUNDINGS: dict[str, tuple[str, str]] = {
    "(NH4)2SO4": ("CHEBI:62946", "ammonium sulfate"),
    "CaCl2 x 2H2O": ("CHEBI:86158", "calcium chloride dihydrate"),
    "CuCl2 x 2H2O": ("CHEBI:86318", "copper dichloride dihydrate"),
    "Distilled water": ("CHEBI:15377", "water"),
    "K2HPO4": ("CHEBI:131527", "dipotassium hydrogen phosphate"),
    "KCl": ("CHEBI:32588", "potassium chloride"),
    "KH2PO4": ("CHEBI:63036", "potassium dihydrogen phosphate"),
    "MgCl2": ("CHEBI:6636", "magnesium dichloride"),
    "MgCl2 x 6H2O": ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    "MgSO4": ("CHEBI:32599", "magnesium sulfate"),
    "NH4Cl": ("CHEBI:31206", "ammonium chloride"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
    "Na2S x 9H2O": ("CHEBI:76209", "sodium sulfide nonahydrate"),
    "NaCl": ("CHEBI:26710", "sodium chloride"),
    "NaHCO3": ("CHEBI:32139", "sodium hydrogencarbonate"),
    "Resazurin": ("CHEBI:8806", "Resazurin"),
    "Sodium thiosulfate": ("CHEBI:132112", "sodium thiosulfate"),
    "Soluble starch": ("CHEBI:28017", "starch"),
    "Casein peptone": ("FOODON:03315719", "Casein peptone"),
    "Yeast extract": ("FOODON:03315426", "Yeast extract"),
}

UNIT_LABELS = {
    "G_PER_L": "g/L",
    "MG_PER_L": "mg/L",
    "ML_PER_L": "ml/L",
    "MOLAR": "M",
    "PERCENT_W_V": "% w/v",
}

REFERENCES = {
    Path("archaea/JCM_J1334_NATRONOARCHAEA_MEDIUM_II.yaml"): (
        1334,
        1207,
        197,
        1079,
        852,
    ),
    Path("bacterial/JCM_J1359_MINERAL_CARBONATE_MEDIUM_WITH_CASEIN_PEPTONE.yaml"): (
        1359,
        1079,
        852,
        197,
    ),
    Path("bacterial/JCM_J1392_ATRIBACTEROTA_M15_MEDIUM.yaml"): (
        1392,
        439,
        431,
        403,
    ),
    Path("bacterial/JCM_J1405_THIOHALORHABDUS_METHYLOTROPHUS_MEDIUM.yaml"): (
        1405,
        1079,
        197,
    ),
}

CURATOR = "repair_jcm_score10_stock_solutions.py"
ACTION = "RESOLVED_JCM_SCORE10_STOCK_SOLUTIONS"
TIMESTAMP = "2026-09-13T00:00:00-07:00"


def _term(preferred_term: str) -> dict[str, str]:
    identifier, label = GROUNDINGS[preferred_term]
    return {"id": identifier, "label": label}


def _component(preferred_term: str, value: str, unit: str, source: str) -> dict[str, Any]:
    term = _term(preferred_term)
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": f"{source} lists {value} {UNIT_LABELS[unit]} {preferred_term}.",
        "term": term,
    }
    if term["id"].startswith("CHEBI:"):
        row["mediaingredientmech_chebi_term"] = copy.deepcopy(term)
    return row


def _stock(
    preferred_term: str,
    value: str,
    *,
    source: str,
    notes: str,
    composition: tuple[Component, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": "ML_PER_L"},
        "source": source,
        "notes": notes,
    }
    if composition:
        row["composition"] = [
            _component(component, amount, unit, source) for component, amount, unit in composition
        ]
    return row


def _jcm_url(number: int) -> str:
    return f"https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD={number}"


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ingredient_signature(doc: dict[str, Any]) -> tuple[str, ...]:
    ingredients = doc.get("ingredients") or []
    if not isinstance(ingredients, list):
        raise ValueError("ingredients is not a list")
    return tuple(
        str(row.get("preferred_term") or "") for row in ingredients if isinstance(row, dict)
    )


def _solution_signature(doc: dict[str, Any]) -> tuple[str, ...]:
    solutions = doc.get("solutions") or []
    if not isinstance(solutions, list):
        raise ValueError("solutions is not a list")
    return tuple(str(row.get("preferred_term") or "") for row in solutions if isinstance(row, dict))


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


def _ensure_references(path: Path, doc: dict[str, Any]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for number in REFERENCES[path]:
        reference = _jcm_url(number)
        if reference not in existing:
            references.append({"reference": reference})


def _ensure_event(path: Path, doc: dict[str, Any], notes: str) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "changes": "Moved flat JCM stock additions into solutions",
        "source": _jcm_url(REFERENCES[path][0]),
        "notes": notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")
    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == event["curator"]
            and existing.get("action") == event["action"]
        ):
            history[index] = event
            return
    history.append(event)


def _j1334() -> tuple[list[dict[str, Any]], list[dict[str, Any]], str]:
    source = "JCM Medium 1334"
    return (
        [],
        [
            _stock(
                "Neutral base salt medium",
                "750.0",
                source=source,
                notes=(
                    "JCM Medium 1334 adds 750.0 ml/L Neutral base salt medium "
                    "prepared from the salts listed below the main recipe."
                ),
                composition=(
                    ("NaCl", "240.0", "G_PER_L"),
                    ("KCl", "5.0", "G_PER_L"),
                    ("K2HPO4", "2.5", "G_PER_L"),
                    ("NH4Cl", "0.4", "G_PER_L"),
                    ("(NH4)2SO4", "0.1", "G_PER_L"),
                ),
            ),
            _stock(
                "Base soda medium (JCM Medium 1207)",
                "250.0",
                source=f"{source} / JCM Medium 1207",
                notes="JCM Medium 1334 mixes 250.0 ml/L Base soda medium.",
            ),
            _stock(
                "1 M MgCl2 solution",
                "1.0",
                source=source,
                notes="JCM Medium 1334 adds 1.0 ml/L 1 M MgCl2 solution.",
                composition=(("MgCl2", "1.0", "MOLAR"),),
            ),
            _stock(
                "Trace vitamins (JCM Medium 197)",
                "5.0",
                source=f"{source} / JCM Medium 197",
                notes="JCM Medium 1334 adds 5.0 ml/L filter-sterilized Trace vitamins.",
            ),
            _stock(
                "Trace element solution (JCM Medium 1079)",
                "1.0",
                source=f"{source} / JCM Medium 1079",
                notes="JCM Medium 1334 adds 1.0 ml/L Trace element solution.",
            ),
            _stock(
                "Se/W solution (JCM Medium 852)",
                "0.5",
                source=f"{source} / JCM Medium 852",
                notes="JCM Medium 1334 adds 0.5 ml/L Se/W solution.",
            ),
            _stock(
                "10% Yeast extract solution",
                "0.2",
                source=source,
                notes=("JCM Medium 1334 adds 0.2 ml/L autoclaved 10% Yeast " "extract solution."),
                composition=(("Yeast extract", "100.0", "G_PER_L"),),
            ),
            _stock(
                "10% Soluble starch solution",
                "10.0",
                source=source,
                notes=("JCM Medium 1334 adds 10.0 ml/L autoclaved 10% " "Soluble starch solution."),
                composition=(("Soluble starch", "100.0", "G_PER_L"),),
            ),
        ],
        (
            "Resolved JCM Medium 1334's inline Neutral base salt medium and "
            "simple MgCl2, yeast extract, and soluble starch stocks; kept "
            "JCM 1207, JCM 197, JCM 1079, and JCM 852 stocks as sourced "
            "opaque cross-references."
        ),
    )


def _j1359() -> tuple[list[dict[str, Any]], list[dict[str, Any]], str]:
    source = "JCM Medium 1359"
    ingredients = [
        _component("Na2CO3", "62.0", "G_PER_L", source),
        _component("NaHCO3", "46.0", "G_PER_L", source),
        _component("NaCl", "18.0", "G_PER_L", source),
        _component("K2HPO4", "1.0", "G_PER_L", source),
        _component("Yeast extract", "0.2", "G_PER_L", source),
    ]
    solutions = [
        _stock(
            "1 M MgSO4 solution",
            "1.0",
            source=source,
            notes="JCM Medium 1359 adds 1.0 ml/L 1 M MgSO4 solution.",
            composition=(("MgSO4", "1.0", "MOLAR"),),
        ),
        _stock(
            "1 M NH4Cl solution",
            "4.0",
            source=source,
            notes="JCM Medium 1359 adds 4.0 ml/L 1 M NH4Cl solution.",
            composition=(("NH4Cl", "1.0", "MOLAR"),),
        ),
        _stock(
            "Trace element solution (JCM Medium 1079)",
            "1.0",
            source=f"{source} / JCM Medium 1079",
            notes="JCM Medium 1359 adds 1.0 ml/L Trace element solution.",
        ),
        _stock(
            "Se/W solution (JCM Medium 852)",
            "1.0",
            source=f"{source} / JCM Medium 852",
            notes="JCM Medium 1359 adds 1.0 ml/L Se/W solution.",
        ),
        _stock(
            "Trace vitamins (JCM Medium 197)",
            "1.0",
            source=f"{source} / JCM Medium 197",
            notes="JCM Medium 1359 adds 1.0 ml/L filter-sterilized Trace vitamins.",
        ),
        _stock(
            "10% Casein peptone solution",
            "10.0",
            source=source,
            notes=(
                "JCM Medium 1359 adds 10.0 ml/L filter-sterilized 10% " "Casein peptone solution."
            ),
            composition=(("Casein peptone", "100.0", "G_PER_L"),),
        ),
    ]
    return (
        ingredients,
        solutions,
        (
            "Moved JCM Medium 1359 MgSO4, NH4Cl, and casein peptone stocks "
            "into solutions and grounded the direct yeast extract row."
        ),
    )


def _j1392() -> tuple[list[dict[str, Any]], list[dict[str, Any]], str]:
    source = "JCM Medium 1392"
    ingredients = [
        _component("NaCl", "20.0", "G_PER_L", source),
        _component("MgCl2 x 6H2O", "3.0", "G_PER_L", source),
        _component("CaCl2 x 2H2O", "0.15", "G_PER_L", source),
        _component("NH4Cl", "0.25", "G_PER_L", source),
        _component("KH2PO4", "0.2", "G_PER_L", source),
        _component("Resazurin", "1.0", "MG_PER_L", source),
        _component("Distilled water", "950.0", "ML_PER_L", source),
    ]
    solutions = [
        _stock(
            "Trace element solution (JCM Medium 439)",
            "1.0",
            source=f"{source} / JCM Medium 439",
            notes="JCM Medium 1392 adds 1.0 ml/L Trace element solution.",
        ),
        _stock(
            "Selenite-tungstate solution (JCM Medium 431)",
            "1.0",
            source=f"{source} / JCM Medium 431",
            notes="JCM Medium 1392 adds 1.0 ml/L Selenite-tungstate solution.",
        ),
        _stock(
            "8% NaHCO3 solution",
            "50.0",
            source=source,
            notes="JCM Medium 1392 adds 50.0 ml/L 8% NaHCO3 solution.",
            composition=(("NaHCO3", "80.0", "G_PER_L"),),
        ),
        _stock(
            "Vitamin solution (JCM Medium 403)",
            "1.0",
            source=f"{source} / JCM Medium 403",
            notes="JCM Medium 1392 adds 1.0 ml/L Vitamin solution.",
        ),
        _stock(
            "Thiamine solution (JCM Medium 403)",
            "1.0",
            source=f"{source} / JCM Medium 403",
            notes="JCM Medium 1392 adds 1.0 ml/L Thiamine solution.",
        ),
        _stock(
            "Vitamin B12 solution (JCM Medium 403)",
            "1.0",
            source=f"{source} / JCM Medium 403",
            notes="JCM Medium 1392 adds 1.0 ml/L Vitamin B12 solution.",
        ),
        _stock(
            "10% Yeast extract solution",
            "20.0",
            source=source,
            notes="JCM Medium 1392 adds 20.0 ml/L 10% Yeast extract solution.",
            composition=(("Yeast extract", "100.0", "G_PER_L"),),
        ),
        _stock(
            "5% Na2S x 9H2O solution",
            "10.0",
            source=source,
            notes="JCM Medium 1392 adds 10.0 ml/L 5% Na2S x 9H2O solution.",
            composition=(("Na2S x 9H2O", "50.0", "G_PER_L"),),
        ),
    ]
    return (
        ingredients,
        solutions,
        (
            "Moved JCM Medium 1392 NaHCO3, yeast extract, and sulfide stocks "
            "into solutions; kept the JCM 439, JCM 431, and JCM 403 "
            "cross-referenced stocks opaque."
        ),
    )


def _j1405() -> tuple[list[dict[str, Any]], list[dict[str, Any]], str]:
    source = "JCM Medium 1405"
    ingredients = [
        _component("NaCl", "180.0", "G_PER_L", source),
        _component("KCl", "5.0", "G_PER_L", source),
        _component("K2HPO4", "2.5", "G_PER_L", source),
        _component("NH4Cl", "0.2", "G_PER_L", source),
    ]
    solutions = [
        _stock(
            "1 M MgSO4 solution",
            "1.0",
            source=source,
            notes="JCM Medium 1405 adds 1.0 ml/L 1 M MgSO4 solution.",
            composition=(("MgSO4", "1.0", "MOLAR"),),
        ),
        _stock(
            "Trace element solution (JCM Medium 1079)",
            "1.0",
            source=f"{source} / JCM Medium 1079",
            notes="JCM Medium 1405 adds 1.0 ml/L Trace element solution.",
        ),
        _stock(
            "0.002% CuCl2 x 2H2O solution",
            "1.0",
            source=source,
            notes="JCM Medium 1405 adds 1.0 ml/L 0.002% CuCl2 x 2H2O solution.",
            composition=(("CuCl2 x 2H2O", "0.002", "PERCENT_W_V"),),
        ),
        _stock(
            "Trace vitamins (JCM Medium 197)",
            "5.0",
            source=f"{source} / JCM Medium 197",
            notes="JCM Medium 1405 adds 5.0 ml/L filter-sterilized Trace vitamins.",
        ),
        _stock(
            "3% Trimethylamine solution",
            "20.0",
            source=source,
            notes=(
                "JCM Medium 1405 adds 20.0 ml/L filter-sterilized 3% " "Trimethylamine solution."
            ),
        ),
        _stock(
            "2 M Sodium thiosulfate solution",
            "1.0",
            source=source,
            notes=(
                "JCM Medium 1405 adds 1.0 ml/L filter-sterilized 2 M "
                "Sodium thiosulfate solution."
            ),
            composition=(("Sodium thiosulfate", "2.0", "MOLAR"),),
        ),
    ]
    return (
        ingredients,
        solutions,
        (
            "Moved JCM Medium 1405 MgSO4, CuCl2, trace vitamin, "
            "trimethylamine, and sodium thiosulfate stocks into solutions."
        ),
    )


REPAIRS = {
    Path("archaea/JCM_J1334_NATRONOARCHAEA_MEDIUM_II.yaml"): _j1334,
    Path("bacterial/JCM_J1359_MINERAL_CARBONATE_MEDIUM_WITH_CASEIN_PEPTONE.yaml"): (_j1359),
    Path("bacterial/JCM_J1392_ATRIBACTEROTA_M15_MEDIUM.yaml"): _j1392,
    Path("bacterial/JCM_J1405_THIOHALORHABDUS_METHYLOTROPHUS_MEDIUM.yaml"): _j1405,
}

FINAL_SIGNATURES = {
    path: tuple(row["preferred_term"] for row in builder()[0]) for path, builder in REPAIRS.items()
}
FINAL_SOLUTION_SIGNATURES = {
    path: tuple(row["preferred_term"] for row in builder()[1]) for path, builder in REPAIRS.items()
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _ensure_target(path: Path, doc: dict[str, Any]) -> None:
    target = TARGETS[path]
    if doc.get("id") != target["id"]:
        raise ValueError(f"{path}: expected {target['id']}, found {doc.get('id')!r}")
    source_id = _source_term_id(doc)
    if source_id != target["source_id"]:
        raise ValueError(f"{path}: expected {target['source_id']}, found {source_id!r}")

    current = (_ingredient_signature(doc), _solution_signature(doc))
    accepted = {
        (IMPORTED_SIGNATURES[path], ()),
        (FINAL_SIGNATURES[path], FINAL_SOLUTION_SIGNATURES[path]),
    }
    if current not in accepted:
        raise ValueError(f"{path}: ingredient/solution signature drifted: {current!r}")


def repair_record(path: Path, doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(path, doc)

    ingredients, solutions, notes = REPAIRS[path]()
    repaired = copy.deepcopy(doc)
    repaired["ingredients"] = ingredients
    _put_after(repaired, "solutions", solutions, "ingredients")
    _ensure_references(path, repaired)
    _ensure_event(path, repaired, notes)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / relative: repair_record(relative, _load(normalized / relative))
        for relative in TARGETS
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
