#!/usr/bin/env python3
"""Repair source-backed Nutrient Broth score-15 records."""

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

CURATOR = "repair_nutrient_broths_score15.py"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M1680 = "https://togomedium.org/medium/M1680"
TOGO_M1760 = "https://togomedium.org/medium/M1760"
TOGO_M2170 = "https://togomedium.org/medium/M2170"
TOGO_M2894 = "https://togomedium.org/medium/M2894"
TOGO_M3207 = "https://togomedium.org/medium/M3207"
NBRC_885 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=885"
NBRC_972 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=972"
NBRC_1559 = "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1559"

Component = tuple[str, str, str]


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    term: tuple[str, str] | None = None,
    physicochemical_roles: tuple[str, ...] = (),
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if term is not None:
        row["term"] = _term(*term)
        if term[0].startswith("CHEBI:"):
            row["mediaingredientmech_chebi_term"] = _term(*term)
    if physicochemical_roles:
        row["physicochemical_roles"] = list(physicochemical_roles)
    return row


def _step(step_number: int, action: str, description: str) -> dict[str, Any]:
    return {
        "step_number": step_number,
        "action": action,
        "description": description,
    }


@dataclass(frozen=True)
class Repair:
    path: Path
    record_id: str
    source_term: str
    references: tuple[str, ...]
    imported_ingredients: tuple[Component, ...]
    ingredients: tuple[dict[str, Any], ...]
    notes: str
    action: str
    ph_value: float | None = None
    ph_range: dict[str, float] | None = None
    temperature_value: float | None = None
    imported_solutions: tuple[Component, ...] = ()
    preparation_steps: tuple[dict[str, Any], ...] = ()
    sterilization: dict[str, Any] | None = None
    has_unmapped_ingredients: bool = False

    @property
    def final_ingredients(self) -> tuple[Component, ...]:
        return _signature(self.ingredients, "ingredients")


M1680 = Path("bacterial/nutrient_broth_0_5_w_v_na2co3.yaml")
M1760 = Path("bacterial/nutrient_broth_5_nacl_ph_10_0.yaml")
M2170 = Path("bacterial/nutrient_broth_no_2.yaml")
M2894 = Path("bacterial/nutrient_broth_nb_ii.yaml")
M3207 = Path("bacterial/nutrient_rich_nr_medium.yaml")

WATER = ("CHEBI:15377", "water")
AGAR = ("CHEBI:2509", "agar")
NACL = ("CHEBI:26710", "sodium chloride")
NA2CO3 = ("CHEBI:29377", "sodium carbonate")
NAHCO3 = ("CHEBI:32139", "sodium hydrogencarbonate")
YEAST_EXTRACT = ("FOODON:03315426", "Yeast extract")
PEPTONE = ("MICRO:0000178", "Peptone")
CASEIN_PEPTONE = ("FOODON:03315719", "Casein peptone")
BEEF_EXTRACT = ("FOODON:03302088", "Beef extract")

AUTOCLAVED_CARBONATE = {
    "method": "AUTOCLAVE",
    "notes": (
        "Autoclave the complex nutrient-broth base and sterilize the alkaline "
        "carbonate stock separately before aseptic addition."
    ),
}

REPAIRS: tuple[Repair, ...] = (
    Repair(
        path=M1680,
        record_id="CultureMech:008239",
        source_term="TOGO:M1680",
        references=(TOGO_M1680, NBRC_885),
        imported_ingredients=(
            ("Distilled water", "1", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Bacto Nutrient Broth (Difco)", "8", "G_PER_L"),
        ),
        imported_solutions=(("Na2CO3*", "5", "G_PER_L"),),
        ingredients=(
            _ingredient(
                "Bacto Nutrient Broth (Difco)",
                "8.0",
                "G_PER_L",
                source="TOGO M1680 / NBRC Medium 885",
                notes=(
                    "TOGO M1680 and NBRC Medium 885 list 8.0 g/L Bacto "
                    "Nutrient Broth from Difco; the commercial product is "
                    "retained without an ontology grounding."
                ),
            ),
            _ingredient(
                "Na2CO3",
                "5.0",
                "G_PER_L",
                source="TOGO M1680 / NBRC Medium 885",
                notes=(
                    "TOGO M1680 and NBRC Medium 885 list 5.0 g/L Na2CO3 "
                    "for a 0.5% w/v alkaline supplement."
                ),
                term=NA2CO3,
            ),
            _ingredient(
                "Agar (if needed)",
                "15.0",
                "G_PER_L",
                source="TOGO M1680 / NBRC Medium 885",
                notes=(
                    "TOGO M1680 and NBRC Medium 885 list 15.0 g/L Agar if "
                    "needed for solid medium."
                ),
                term=AGAR,
                physicochemical_roles=("SOLIDIFYING_AGENT",),
            ),
            _ingredient(
                "Distilled water",
                "1000.0",
                "ML_PER_L",
                source="TOGO M1680 / NBRC Medium 885",
                notes="TOGO M1680 and NBRC Medium 885 list 1 L Distilled water.",
                term=WATER,
            ),
        ),
        ph_value=10.5,
        preparation_steps=(
            _step(
                1,
                "MIX",
                "Suspend Bacto Nutrient Broth (Difco) and optional agar in distilled water.",
            ),
            _step(2, "AUTOCLAVE", "Autoclave the nutrient-broth agar base."),
            _step(3, "AUTOCLAVE", "Sterilize the Na2CO3 stock separately."),
            _step(
                4,
                "MIX",
                "Aseptically add the sterile Na2CO3 stock to the sterile base.",
            ),
        ),
        sterilization=AUTOCLAVED_CARBONATE,
        notes=(
            "TOGO M1680 imports NBRC Medium 885: 8 g Bacto Nutrient Broth "
            "from Difco, 5 g Na2CO3, 15 g agar if needed, and 1 L distilled "
            "water; the final pH is 10.5."
        ),
        action="RESOLVED_TOGO_M1680_NBRC_885",
        has_unmapped_ingredients=True,
    ),
    Repair(
        path=M1760,
        record_id="CultureMech:008325",
        source_term="TOGO:M1760",
        references=(TOGO_M1760, NBRC_972),
        imported_ingredients=(
            ("Distilled water", "1000.0", "G_PER_L"),
            ("NaCl", "50", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Nutrient Broth (OXOID)", "13", "G_PER_L"),
            ("NaHCO3", "4.2", "G_PER_L"),
            ("Na2CO3 (anhydrous)", "5.3", "G_PER_L"),
        ),
        imported_solutions=(("Sodium-sesquicarbonate solution*", "100", "G_PER_L"),),
        ingredients=(
            _ingredient(
                "Nutrient Broth (OXOID)",
                "13.0",
                "G_PER_L",
                source="TOGO M1760 / NBRC Medium 972",
                notes=(
                    "TOGO M1760 and NBRC Medium 972 list 13.0 g/L Nutrient "
                    "Broth (OXOID); retained as an intentionally opaque "
                    "commercial product."
                ),
            ),
            _ingredient(
                "NaCl",
                "50.0",
                "G_PER_L",
                source="TOGO M1760 / NBRC Medium 972",
                notes="TOGO M1760 and NBRC Medium 972 list 50.0 g/L NaCl.",
                term=NACL,
            ),
            _ingredient(
                "NaHCO3",
                "4.2",
                "G_PER_L",
                source="TOGO M1760 / NBRC Medium 972",
                notes=(
                    "NBRC Medium 972 lists 4.2 g NaHCO3 in the separately "
                    "sterilized 100 ml sodium-sesquicarbonate stock added per liter."
                ),
                term=NAHCO3,
            ),
            _ingredient(
                "Na2CO3",
                "5.3",
                "G_PER_L",
                source="TOGO M1760 / NBRC Medium 972",
                notes=(
                    "NBRC Medium 972 lists 5.3 g anhydrous Na2CO3 in the "
                    "separately sterilized 100 ml sodium-sesquicarbonate stock "
                    "added per liter."
                ),
                term=NA2CO3,
            ),
            _ingredient(
                "Agar (if needed)",
                "15.0",
                "G_PER_L",
                source="TOGO M1760 / NBRC Medium 972",
                notes=(
                    "TOGO M1760 and NBRC Medium 972 list 15.0 g/L Agar if "
                    "needed for solid medium."
                ),
                term=AGAR,
                physicochemical_roles=("SOLIDIFYING_AGENT",),
            ),
            _ingredient(
                "Distilled water",
                "1000.0",
                "ML_PER_L",
                source="TOGO M1760 / NBRC Medium 972",
                notes=(
                    "NBRC Medium 972 uses 900 ml Distilled water in the main "
                    "base plus 100 ml water in the sodium-sesquicarbonate stock."
                ),
                term=WATER,
            ),
        ),
        ph_value=10.0,
        preparation_steps=(
            _step(
                1,
                "MIX",
                "Suspend Nutrient Broth (OXOID), NaCl, and optional agar in 900 ml distilled water.",
            ),
            _step(2, "AUTOCLAVE", "Autoclave the nutrient-broth NaCl base."),
            _step(
                3,
                "AUTOCLAVE",
                "Sterilize the 100 ml NaHCO3 and Na2CO3 sodium-sesquicarbonate stock separately.",
            ),
            _step(
                4,
                "MIX",
                "Aseptically add the sterile sodium-sesquicarbonate stock to the sterile base.",
            ),
        ),
        sterilization=AUTOCLAVED_CARBONATE,
        notes=(
            "TOGO M1760 imports NBRC Medium 972: a 900 ml main base with "
            "13 g Nutrient Broth (OXOID), 50 g NaCl, 15 g agar if needed, "
            "and a 100 ml sodium-sesquicarbonate stock containing 4.2 g "
            "NaHCO3 and 5.3 g anhydrous Na2CO3; the final pH is 10.0."
        ),
        action="RESOLVED_TOGO_M1760_NBRC_972",
        has_unmapped_ingredients=True,
    ),
    Repair(
        path=M2170,
        record_id="CultureMech:008765",
        source_term="TOGO:M2170",
        references=(TOGO_M2170, NBRC_1559),
        imported_ingredients=(
            ("Distilled water", "1", "G_PER_L"),
            ("Sodium chloride", "5", "G_PER_L"),
            ("Agar (if needed)", "15", "G_PER_L"),
            ("Lab-Lemco powder", "10", "G_PER_L"),
            ("Peptone", "10", "G_PER_L"),
        ),
        ingredients=(
            _ingredient(
                "Lab-Lemco powder",
                "10.0",
                "G_PER_L",
                source="TOGO M2170 / NBRC Medium 1559",
                notes="TOGO M2170 and NBRC Medium 1559 list 10.0 g/L Lab-Lemco powder.",
                term=BEEF_EXTRACT,
            ),
            _ingredient(
                "Peptone",
                "10.0",
                "G_PER_L",
                source="TOGO M2170 / NBRC Medium 1559",
                notes="TOGO M2170 and NBRC Medium 1559 list 10.0 g/L Peptone.",
                term=PEPTONE,
            ),
            _ingredient(
                "Sodium chloride",
                "5.0",
                "G_PER_L",
                source="TOGO M2170 / NBRC Medium 1559",
                notes="TOGO M2170 and NBRC Medium 1559 list 5.0 g/L Sodium chloride.",
                term=NACL,
            ),
            _ingredient(
                "Agar (if needed)",
                "15.0",
                "G_PER_L",
                source="TOGO M2170 / NBRC Medium 1559",
                notes=(
                    "TOGO M2170 and NBRC Medium 1559 list 15.0 g/L Agar if "
                    "needed for solid medium."
                ),
                term=AGAR,
                physicochemical_roles=("SOLIDIFYING_AGENT",),
            ),
            _ingredient(
                "Distilled water",
                "1000.0",
                "ML_PER_L",
                source="TOGO M2170 / NBRC Medium 1559",
                notes="TOGO M2170 and NBRC Medium 1559 list 1 L Distilled water.",
                term=WATER,
            ),
        ),
        ph_range={"min": 7.3, "max": 7.7},
        preparation_steps=(
            _step(1, "ADJUST_PH", "Adjust pH to 7.5 +/- 0.2."),
        ),
        notes=(
            "TOGO M2170 imports NBRC Medium 1559 Nutrient broth No. 2: "
            "10 g Lab-Lemco powder, 10 g peptone, 5 g sodium chloride, "
            "15 g agar if needed, and 1 L distilled water; pH is 7.5 +/- 0.2."
        ),
        action="RESOLVED_TOGO_M2170_NBRC_1559",
    ),
    Repair(
        path=M2894,
        record_id="CultureMech:009430",
        source_term="TOGO:M2894",
        references=(TOGO_M2894,),
        imported_ingredients=(
            ("Distilled water", "1", "G_PER_L"),
            ("Yeast extract", "1.5", "G_PER_L"),
            ("NaCl", "5", "G_PER_L"),
            ("Peptone from meat", "2.5", "G_PER_L"),
            ("Peptone from casein", "3.5", "G_PER_L"),
            ("Peptone from gelatine", "2.5", "G_PER_L"),
        ),
        ingredients=(
            _ingredient(
                "Peptone from casein",
                "3.5",
                "G_PER_L",
                source="TOGO M2894",
                notes="TOGO M2894 lists 3.5 g/L peptone from casein.",
                term=CASEIN_PEPTONE,
            ),
            _ingredient(
                "Peptone from meat",
                "2.5",
                "G_PER_L",
                source="TOGO M2894",
                notes=(
                    "TOGO M2894 lists 2.5 g/L peptone from meat; the "
                    "source-specific meat hydrolysate is retained without an "
                    "ontology grounding."
                ),
            ),
            _ingredient(
                "Peptone from gelatine",
                "2.5",
                "G_PER_L",
                source="TOGO M2894",
                notes=(
                    "TOGO M2894 lists 2.5 g/L peptone from gelatine; the "
                    "source-specific gelatin hydrolysate is retained without "
                    "an ontology grounding."
                ),
            ),
            _ingredient(
                "Yeast extract",
                "1.5",
                "G_PER_L",
                source="TOGO M2894",
                notes="TOGO M2894 lists 1.5 g/L Yeast extract.",
                term=YEAST_EXTRACT,
            ),
            _ingredient(
                "NaCl",
                "5.0",
                "G_PER_L",
                source="TOGO M2894",
                notes="TOGO M2894 lists 5.0 g/L NaCl.",
                term=NACL,
            ),
            _ingredient(
                "Distilled water",
                "1.0",
                "L",
                source="TOGO M2894",
                notes="TOGO M2894 records the NB II formulation per 1 L Distilled water.",
                term=WATER,
            ),
        ),
        temperature_value=30.0,
        notes=(
            "TOGO M2894 records Nutrient broth (NB II) with 3.5 g/L "
            "peptone from casein, 2.5 g/L peptone from meat, 2.5 g/L "
            "peptone from gelatine, 1.5 g/L yeast extract, 5 g/L NaCl, "
            "and incubation at 30 C."
        ),
        action="RESOLVED_TOGO_M2894_NBII",
        has_unmapped_ingredients=True,
    ),
    Repair(
        path=M3207,
        record_id="CultureMech:009647",
        source_term="TOGO:M3207",
        references=(TOGO_M3207,),
        imported_ingredients=(
            ("Distilled water", "1", "G_PER_L"),
            ("Yeast extract", "2", "G_PER_L"),
            ("Meat extract", "10", "G_PER_L"),
            ("Peptone", "10", "G_PER_L"),
        ),
        ingredients=(
            _ingredient(
                "Meat extract",
                "10.0",
                "G_PER_L",
                source="TOGO M3207",
                notes=(
                    "TOGO M3207 lists 10.0 g/L meat extract; the generic "
                    "complex extract is retained without an ontology grounding."
                ),
            ),
            _ingredient(
                "Peptone",
                "10.0",
                "G_PER_L",
                source="TOGO M3207",
                notes="TOGO M3207 lists 10.0 g/L Peptone.",
                term=PEPTONE,
            ),
            _ingredient(
                "Yeast extract",
                "2.0",
                "G_PER_L",
                source="TOGO M3207",
                notes="TOGO M3207 lists 2.0 g/L Yeast extract.",
                term=YEAST_EXTRACT,
            ),
            _ingredient(
                "Distilled water",
                "1.0",
                "L",
                source="TOGO M3207",
                notes=(
                    "TOGO M3207 records the nutrient-rich formulation per 1 L "
                    "Distilled water."
                ),
                term=WATER,
            ),
        ),
        temperature_value=30.0,
        notes=(
            "TOGO M3207 records nutrient rich medium with 10 g/L meat "
            "extract, 10 g/L peptone, 2 g/L yeast extract, and "
            "cultivation at 30 C."
        ),
        action="RESOLVED_TOGO_M3207_NR",
        has_unmapped_ingredients=True,
    ),
)

REPAIR_BY_PATH = {repair.path: repair for repair in REPAIRS}


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(repair: Repair, doc: dict[str, Any]) -> None:
    if doc.get("id") != repair.record_id:
        raise ValueError(
            f"{repair.path}: expected id {repair.record_id}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != repair.source_term:
        raise ValueError(f"{repair.path}: expected media term {repair.source_term}")

    ingredient_signature = _signature(doc.get("ingredients"), "ingredients")
    if ingredient_signature not in (repair.imported_ingredients, repair.final_ingredients):
        raise ValueError(f"{repair.path}: ingredient signature drifted")

    solution_signature = _signature(doc.get("solutions"), "solutions")
    if solution_signature not in (repair.imported_solutions, ()):
        raise ValueError(f"{repair.path}: solution signature drifted")


def _ensure_flags(doc: dict[str, Any], has_unmapped_ingredients: bool) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    for obsolete in ("incomplete_composition", "needs_manual_curation"):
        while obsolete in flags:
            flags.remove(obsolete)
    if not has_unmapped_ingredients:
        while "has_unmapped_ingredients" in flags:
            flags.remove("has_unmapped_ingredients")

    for flag in ("ingredients_curated", "has_ontology_mappings"):
        if flag not in flags:
            flags.append(flag)
    if has_unmapped_ingredients and "has_unmapped_ingredients" not in flags:
        flags.append("has_unmapped_ingredients")


def _ensure_references(doc: dict[str, Any], urls: tuple[str, ...]) -> None:
    rows = doc.setdefault("references", [])
    if not isinstance(rows, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in rows if isinstance(row, dict)}
    for url in urls:
        if url not in existing:
            rows.append({"reference": url})
            existing.add(url)


def _append_event(doc: dict[str, Any], repair: Repair) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": repair.action,
        "source": "; ".join(repair.references),
        "notes": repair.notes,
    }

    history = doc.setdefault("curation_history", [])
    if not isinstance(history, list):
        raise ValueError("curation_history is not a list")

    for index, existing in enumerate(history):
        if (
            isinstance(existing, dict)
            and existing.get("curator") == CURATOR
            and existing.get("action") == repair.action
        ):
            history[index] = event
            return
    history.append(event)


def repair_target(repair: Repair, doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_target(repair, doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["ingredients"] = copy.deepcopy(list(repair.ingredients))
    repaired.pop("solutions", None)

    if repair.ph_value is not None:
        _put_after(repaired, "ph_value", repair.ph_value, "physical_state")
        repaired.pop("ph_range", None)
    elif repair.ph_range is not None:
        _put_after(repaired, "ph_range", copy.deepcopy(repair.ph_range), "physical_state")
        repaired.pop("ph_value", None)
    else:
        repaired.pop("ph_value", None)
        repaired.pop("ph_range", None)

    if repair.temperature_value is not None:
        _put_after(repaired, "temperature_value", repair.temperature_value, "physical_state")
        repaired.pop("temperature_range", None)
    else:
        repaired.pop("temperature_value", None)
        repaired.pop("temperature_range", None)

    if repair.preparation_steps:
        _put_after(
            repaired,
            "preparation_steps",
            copy.deepcopy(list(repair.preparation_steps)),
            "notes",
        )
    else:
        repaired.pop("preparation_steps", None)
    if repair.sterilization is None:
        repaired.pop("sterilization", None)
    else:
        _put_after(repaired, "sterilization", copy.deepcopy(repair.sterilization), "preparation_steps")

    _put_after(repaired, "notes", repair.notes, "media_term")
    _ensure_flags(repaired, repair.has_unmapped_ingredients)
    _ensure_references(repaired, repair.references)
    _append_event(repaired, repair)
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans: dict[Path, dict[str, Any]] = {}
    for repair in REPAIRS:
        path = normalized / repair.path
        plans[path] = repair_target(repair, _load(path))
    return plans


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
