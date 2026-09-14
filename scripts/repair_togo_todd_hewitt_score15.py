#!/usr/bin/env python3
"""Repair score-15 TOGO Todd Hewitt records."""

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
THY_PATH = Path("bacterial/todd_hewitt_broth_supplemented_with_1_wt_vol_yeast_extract.yaml")
TH_BLOOD_PATH = Path(
    "bacterial/todd_hewitt_th_broth_difco_containing_1_5_wt_vol_agar_and_6_vol_vol_sheep_blood.yaml"
)
EXPECTED_THY_ID = "CultureMech:009488"
EXPECTED_TH_BLOOD_ID = "CultureMech:009445"
EXPECTED_THY_MEDIA_TERM = "TOGO:M2963"
EXPECTED_TH_BLOOD_MEDIA_TERM = "TOGO:M2909"
YAML_LOADER = getattr(yaml, "CSafeLoader", yaml.SafeLoader)

CURATOR = "repair_togo_todd_hewitt_score15.py"
ACTION = "RESOLVED_TOGO_TODD_HEWITT_SCORE15"
TIMESTAMP = "2026-09-12T00:00:00-07:00"

TOGO_M2963 = "https://togomedium.org/medium/M2963"
TOGO_M2909 = "https://togomedium.org/medium/M2909"
OOGAI_DOI = "DOI:10.1093/dnares/dsx050"
ZHANG_DOI = "DOI:10.1016/j.micres.2013.09.007"

TODD_BD = "Todd Hewitt broth (Becton, Dickinson and Company, Franklin Lakes, NJ, USA)"
YEAST_NACALAI = "yeast extract (Nacalai Tesque, Kyoto, Japan)"
CO2 = "CO2"
SHEEP_BLOOD = "Sheep blood"
AGAR = "Agar"
TODD_DIFCO = "Todd\N{EN DASH}Hewitt (TH) broth (Difco)"
TODD_HEWITT_MEDIUM = ("CultureMech:008070", "Todd Hewitt Medium")

Component = tuple[str, str, str]

THY_LEGACY_SIGNATURE: tuple[Component, ...] = (
    (TODD_BD, "1", "G_PER_L"),
    (YEAST_NACALAI, "1", "G_PER_L"),
    (CO2, "variable", "VARIABLE"),
)
THY_REPAIRED_SIGNATURE: tuple[Component, ...] = (
    (TODD_BD, "1000", "ML_PER_L"),
    (YEAST_NACALAI, "1", "PERCENT_W_V"),
    (CO2, "5", "PERCENT_V_V"),
)

TH_BLOOD_LEGACY_SIGNATURE: tuple[Component, ...] = (
    (SHEEP_BLOOD, "6", "G_PER_L"),
    (AGAR, "1.5", "G_PER_L"),
    (TODD_DIFCO, "1", "G_PER_L"),
)
TH_BLOOD_REPAIRED_SIGNATURE: tuple[Component, ...] = (
    (SHEEP_BLOOD, "6", "PERCENT_V_V"),
    (AGAR, "1.5", "PERCENT_W_V"),
    (TODD_DIFCO, "1000", "ML_PER_L"),
)


@dataclass(frozen=True)
class TargetOrganism:
    preferred_term: str
    term_id: str
    label: str
    evidence: str


@dataclass(frozen=True)
class RecordSpec:
    target: Path
    expected_id: str
    expected_media_term: str
    legacy_signature: tuple[Component, ...]
    repaired_signature: tuple[Component, ...]
    source_url: str
    article_reference: str
    article_label: str
    notes: str
    preparation_steps: tuple[str, ...]
    target_organism: TargetOrganism
    false_kg_match: str | None = None

    @property
    def references(self) -> tuple[str, str]:
        return (self.source_url, self.article_reference)


THY_SPEC = RecordSpec(
    target=THY_PATH,
    expected_id=EXPECTED_THY_ID,
    expected_media_term=EXPECTED_THY_MEDIA_TERM,
    legacy_signature=THY_LEGACY_SIGNATURE,
    repaired_signature=THY_REPAIRED_SIGNATURE,
    source_url=TOGO_M2963,
    article_reference=OOGAI_DOI,
    article_label="Oogai et al. 2018",
    notes=(
        "TOGO M2963 lists Todd Hewitt broth supplemented with 1% w/v yeast extract "
        "and 5% CO2. Oogai et al. cultured Aggregatibacter actinomycetemcomitans "
        "strains in this THY broth at 37 C under 5% CO2 without shaking."
    ),
    preparation_steps=(
        "Supplement Todd Hewitt broth with 1% w/v yeast extract.",
        "Cultivate at 37 C under 5% CO2 without shaking.",
    ),
    target_organism=TargetOrganism(
        preferred_term="Aggregatibacter actinomycetemcomitans",
        term_id="NCBITaxon:714",
        label="Aggregatibacter actinomycetemcomitans",
        evidence=(
            "Oogai et al. report that five Aggregatibacter actinomycetemcomitans "
            "strains were grown in THY broth at 37 C under 5% CO2 without shaking."
        ),
    ),
)

TH_BLOOD_SPEC = RecordSpec(
    target=TH_BLOOD_PATH,
    expected_id=EXPECTED_TH_BLOOD_ID,
    expected_media_term=EXPECTED_TH_BLOOD_MEDIA_TERM,
    legacy_signature=TH_BLOOD_LEGACY_SIGNATURE,
    repaired_signature=TH_BLOOD_REPAIRED_SIGNATURE,
    source_url=TOGO_M2909,
    article_reference=ZHANG_DOI,
    article_label="Zhang et al. 2014",
    notes=(
        "TOGO M2909 lists Todd-Hewitt broth with 1.5% w/v agar and 6% v/v sheep "
        "blood. Zhang et al. cultured Streptococcus suis strains at 37 C on this "
        "Todd-Hewitt sheep-blood agar formulation."
    ),
    preparation_steps=(
        "Supplement Todd-Hewitt broth with 1.5% w/v agar and 6% v/v sheep blood.",
        "Cultivate Streptococcus suis strains at 37 C.",
    ),
    target_organism=TargetOrganism(
        preferred_term="Streptococcus suis",
        term_id="NCBITaxon:1307",
        label="Streptococcus suis",
        evidence=(
            "Zhang et al. report that Streptococcus suis strains were cultured at "
            "37 C in Todd-Hewitt broth or on Todd-Hewitt broth containing 1.5% "
            "w/v agar and 6% v/v sheep blood."
        ),
    ),
    false_kg_match="mediadive.medium:12",
)

SPECS: tuple[RecordSpec, ...] = (THY_SPEC, TH_BLOOD_SPEC)


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


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
    culturemech_term: tuple[str, str] | None = None,
    nutritional_roles: tuple[str, ...] = (),
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
    if culturemech_term is not None:
        row["culturemech_term"] = _term(*culturemech_term)
    if nutritional_roles:
        row["nutritional_roles"] = list(nutritional_roles)
    return row


def _component(name: str, value: str, unit: str, spec: RecordSpec) -> dict[str, Any]:
    source = spec.expected_media_term.replace(":", " ")
    if name == YEAST_NACALAI:
        return _ingredient(
            name,
            value,
            unit,
            source=source,
            notes=f"{source} lists 1% w/v yeast extract from Nacalai Tesque.",
            term=("FOODON:03315426", "yeast extract"),
            nutritional_roles=("NITROGEN_SOURCE",),
        )
    if name == CO2:
        return _ingredient(
            name,
            value,
            unit,
            source=source,
            notes=f"{source} lists 5% CO2 as the incubation atmosphere.",
            term=("CHEBI:16526", "carbon dioxide"),
        )
    if name == SHEEP_BLOOD:
        return _ingredient(
            name,
            value,
            unit,
            source=source,
            notes=f"{source} lists 6% v/v sheep blood.",
            term=("UBERON:0000178", "blood"),
        )
    if name == AGAR:
        return _ingredient(
            name,
            value,
            unit,
            source=source,
            notes=f"{source} lists 1.5% w/v agar.",
            term=("CHEBI:2509", "agar"),
        )
    return _ingredient(
        name,
        value,
        unit,
        source=source,
        notes=f"{source} lists the opaque Todd Hewitt broth base for this formulation.",
        culturemech_term=TODD_HEWITT_MEDIUM,
    )


def _target_organisms(spec: RecordSpec) -> list[dict[str, Any]]:
    organism = spec.target_organism
    return [
        {
            "preferred_term": organism.preferred_term,
            "term": {"id": organism.term_id, "label": organism.label},
            "evidence": [
                {
                    "reference": spec.article_reference,
                    "supports": "SUPPORT",
                    "explanation": organism.evidence,
                }
            ],
        }
    ]


def _preparation_steps(spec: RecordSpec) -> list[dict[str, Any]]:
    return [
        {"step_number": index, "action": "MIX", "description": description}
        for index, description in enumerate(spec.preparation_steps, start=1)
    ]


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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _ensure_target(doc: dict[str, Any], spec: RecordSpec) -> None:
    if doc.get("id") != spec.expected_id:
        raise ValueError(f"{spec.target}: expected id {spec.expected_id}, found {doc.get('id')!r}")
    if _source_term_id(doc) != spec.expected_media_term:
        raise ValueError(f"{spec.target}: expected media term {spec.expected_media_term}")

    signature = _signature(doc.get("ingredients"), "ingredients")
    if signature not in {spec.legacy_signature, spec.repaired_signature}:
        raise ValueError(
            f"{spec.target}: ingredient signature drifted from known signatures to {signature!r}"
        )


def _put_after(doc: dict[str, Any], key: str, value: Any, after_key: str) -> None:
    if key in doc:
        doc[key] = value
        return

    rebuilt: dict[str, Any] = {}
    placed = False
    for existing_key, existing_value in doc.items():
        rebuilt[existing_key] = existing_value
        if existing_key == after_key:
            rebuilt[key] = value
            placed = True
    if not placed:
        rebuilt[key] = value

    doc.clear()
    doc.update(rebuilt)


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    flags = [
        flag
        for flag in flags
        if flag
        not in {
            "has_unmapped_ingredients",
            "incomplete_composition",
            "needs_manual_curation",
        }
    ]
    flags.extend(("has_ontology_mappings", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _ensure_references(doc: dict[str, Any], spec: RecordSpec) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {row.get("reference") for row in references if isinstance(row, dict)}
    for reference in spec.references:
        if reference not in existing:
            references.append({"reference": reference})
            existing.add(reference)


def _ensure_event(doc: dict[str, Any], spec: RecordSpec) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": ACTION,
        "source": "; ".join(spec.references),
        "notes": (
            f"Curated {spec.expected_media_term} from TOGO and {spec.article_label}; "
            "corrected imported percentage units, added 37 C cultivation evidence, "
            "and linked opaque Todd Hewitt broth to a curated CultureMech recipe."
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


def repair_record(doc: dict[str, Any], spec: RecordSpec) -> dict[str, Any]:
    _ensure_target(doc, spec)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR" if spec is TH_BLOOD_SPEC else "LIQUID"
    _put_after(repaired, "temperature_value", 37.0, "physical_state")
    repaired["ingredients"] = [
        _component(name, value, unit, spec) for name, value, unit in spec.repaired_signature
    ]
    _put_after(repaired, "organism_culture_type", "isolate", "curation_history")
    _put_after(repaired, "target_organisms", _target_organisms(spec), "organism_culture_type")
    _put_after(repaired, "notes", spec.notes, "media_term")
    repaired["preparation_steps"] = _preparation_steps(spec)
    _ensure_references(repaired, spec)
    _ensure_flags(repaired)
    _ensure_event(repaired, spec)

    if spec.false_kg_match is not None:
        kg_match = repaired.get("kg_microbe_match")
        if kg_match not in (None, spec.false_kg_match):
            raise ValueError(f"{spec.target}: unexpected kg_microbe_match {kg_match!r}")
        repaired.pop("kg_microbe_match", None)

    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    return {
        normalized / spec.target: repair_record(_load(normalized / spec.target), spec)
        for spec in SPECS
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
