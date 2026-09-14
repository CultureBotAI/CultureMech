#!/usr/bin/env python3
"""Repair score-15 specialized JCM marine agar imports."""

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

CURATOR = "repair_jcm_specialized_marine_score15.py"
DILUTED_ACTION = "RESOLVED_JCM_DILUTED_MARINE_SCORE15"
PH_ACTION = "RESOLVED_JCM_MARINE_PH_SCORE15"
PARENT_ACTION = "LINKED_JCM_MARINE_PH_SCORE15_CHILDREN"
TIMESTAMP = "2026-09-13T00:00:00-07:00"

JCM_118 = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=118"

Component = tuple[str, str, str]

PARENT_PATH = Path("specialized/marine_agar_2216.yaml")
PARENT_ID = "CultureMech:015393"
PARENT_NAME = "marine_agar_2216"

DILUTED_IMPORTED_SIGNATURE: tuple[Component, ...] = (
    ("Marine broth 2216", "3.74", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Sea water", "750", "G_PER_L"),
)
DILUTED_FINAL_SIGNATURE: tuple[Component, ...] = (
    ("Marine broth 2216 (BD-Difco)", "3.74", "G_PER_L"),
    ("Agar", "15", "G_PER_L"),
    ("Filtered seawater", "750", "ML_PER_L"),
    ("Distilled water", "250", "ML_PER_L"),
)

MARINE_AGAR_IMPORTED_SIGNATURE: tuple[Component, ...] = (("Marine agar 2216", "55.1", "G_PER_L"),)
MARINE_AGAR_FINAL_SIGNATURE: tuple[Component, ...] = (
    ("Marine agar 2216 (BD-Difco)", "55.1", "G_PER_L"),
    ("Distilled water", "1.0", "L"),
)


@dataclass(frozen=True)
class DilutedTarget:
    path: Path
    identifier: str
    media_term_id: str
    medium_no: str
    mediadive_page: str
    mediadive_rest: str
    jcm_url: str

    @property
    def source_label(self) -> str:
        return f"JCM Medium {self.medium_no}"

    @property
    def references(self) -> tuple[str, ...]:
        return (self.mediadive_page, self.mediadive_rest, self.jcm_url)


@dataclass(frozen=True)
class PhTarget:
    path: Path
    identifier: str
    media_term_id: str
    medium_no: str
    ph_value: float
    mediadive_page: str
    mediadive_rest: str
    jcm_url: str

    @property
    def source_label(self) -> str:
        return f"JCM Medium {self.medium_no}"

    @property
    def references(self) -> tuple[str, ...]:
        return (self.mediadive_page, self.mediadive_rest, self.jcm_url, JCM_118)


DILUTED = DilutedTarget(
    path=Path("specialized/diluted_marine_agar.yaml"),
    identifier="CultureMech:015411",
    media_term_id="mediadive.medium:J644",
    medium_no="644",
    mediadive_page="https://mediadive.dsmz.de/medium/J644",
    mediadive_rest="https://mediadive.dsmz.de/rest/medium/J644",
    jcm_url="https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=644",
)

PH_TARGETS: tuple[PhTarget, ...] = (
    PhTarget(
        path=Path("specialized/marine_agar_2216_ph_8_5.yaml"),
        identifier="CultureMech:015371",
        media_term_id="mediadive.medium:J1001",
        medium_no="1001",
        ph_value=8.5,
        mediadive_page="https://mediadive.dsmz.de/medium/J1001",
        mediadive_rest="https://mediadive.dsmz.de/rest/medium/J1001",
        jcm_url="https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1001",
    ),
    PhTarget(
        path=Path("specialized/marine_agar_2216_ph_9_0.yaml"),
        identifier="CultureMech:015373",
        media_term_id="mediadive.medium:J1016",
        medium_no="1016",
        ph_value=9.0,
        mediadive_page="https://mediadive.dsmz.de/medium/J1016",
        mediadive_rest="https://mediadive.dsmz.de/rest/medium/J1016",
        jcm_url="https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1016",
    ),
)

GROUNDINGS: dict[str, tuple[str, str]] = {
    "Agar": ("CHEBI:2509", "agar"),
    "Distilled water": ("CHEBI:15377", "water"),
    "Na2CO3": ("CHEBI:29377", "sodium carbonate"),
}


def _load(path: Path) -> dict[str, Any]:
    doc = yaml.load(path.read_text(encoding="utf-8"), Loader=YAML_LOADER)
    if not isinstance(doc, dict):
        raise ValueError(f"{path}: expected a YAML mapping")
    return doc


def _term(identifier: str, label: str) -> dict[str, str]:
    return {"id": identifier, "label": label}


def _grounding(preferred_term: str) -> dict[str, dict[str, str]]:
    identifier, label = GROUNDINGS[preferred_term]
    term = _term(identifier, label)
    return {"term": term, "mediaingredientmech_chebi_term": copy.deepcopy(term)}


def _ingredient(
    preferred_term: str,
    value: str,
    unit: str,
    *,
    source: str,
    notes: str,
    grounded: bool = False,
    physicochemical_roles: list[str] | None = None,
) -> dict[str, Any]:
    row: dict[str, Any] = {
        "preferred_term": preferred_term,
        "concentration": {"value": value, "unit": unit},
        "source": source,
        "notes": notes,
    }
    if grounded:
        row.update(_grounding(preferred_term))
    if physicochemical_roles:
        row["physicochemical_roles"] = physicochemical_roles
    return row


def _signature(rows: Any) -> tuple[Component, ...]:
    if rows is None:
        rows = []
    if not isinstance(rows, list):
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


def _source_term_id(doc: dict[str, Any]) -> str:
    media_term = doc.get("media_term")
    if not isinstance(media_term, dict):
        return ""
    term = media_term.get("term")
    if not isinstance(term, dict):
        return ""
    return str(term.get("id") or "")


def _put_after(doc: dict[str, Any], key: str, value: Any, after: str) -> None:
    updated: dict[str, Any] = {}
    inserted = False
    for existing_key, existing_value in doc.items():
        if existing_key == key:
            continue
        updated[existing_key] = existing_value
        if existing_key == after:
            updated[key] = value
            inserted = True

    if not inserted:
        updated[key] = value

    doc.clear()
    doc.update(updated)


def _ensure_references(doc: dict[str, Any], references_to_add: tuple[str, ...]) -> None:
    references = doc.setdefault("references", [])
    if not isinstance(references, list):
        raise ValueError("references is not a list")

    existing = {
        row.get("reference")
        for row in references
        if isinstance(row, dict) and isinstance(row.get("reference"), str)
    }
    for reference in references_to_add:
        if reference not in existing:
            references.append({"reference": reference})


def _ensure_flags(doc: dict[str, Any]) -> None:
    flags = doc.setdefault("data_quality_flags", [])
    if not isinstance(flags, list):
        raise ValueError("data_quality_flags is not a list")

    obsolete = {
        "extracted_from_notes",
        "incomplete_composition",
        "needs_manual_curation",
        "resolved_reference",
    }
    flags = [flag for flag in flags if flag not in obsolete]
    flags.extend(("has_ontology_mappings", "has_unmapped_ingredients", "ingredients_curated"))
    doc["data_quality_flags"] = sorted(dict.fromkeys(flags))


def _append_event(
    doc: dict[str, Any],
    *,
    action: str,
    source: str,
    notes: str,
) -> None:
    event = {
        "timestamp": TIMESTAMP,
        "curator": CURATOR,
        "action": action,
        "source": source,
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


def _ensure_diluted_target(doc: dict[str, Any]) -> None:
    if doc.get("id") != DILUTED.identifier:
        raise ValueError(
            f"{DILUTED.path}: expected id {DILUTED.identifier}, found {doc.get('id')!r}"
        )
    if _source_term_id(doc) != DILUTED.media_term_id:
        raise ValueError(f"{DILUTED.path}: expected media term {DILUTED.media_term_id}")

    signature = _signature(doc.get("ingredients"))
    if signature not in {DILUTED_IMPORTED_SIGNATURE, DILUTED_FINAL_SIGNATURE}:
        raise ValueError(f"{DILUTED.path}: ingredient signature drifted to {signature!r}")


def _ensure_ph_target(target: PhTarget, doc: dict[str, Any]) -> None:
    if doc.get("id") != target.identifier:
        raise ValueError(f"{target.path}: expected id {target.identifier}, found {doc.get('id')!r}")
    if _source_term_id(doc) != target.media_term_id:
        raise ValueError(f"{target.path}: expected media term {target.media_term_id}")

    signature = _signature(doc.get("ingredients"))
    if signature not in {MARINE_AGAR_IMPORTED_SIGNATURE, MARINE_AGAR_FINAL_SIGNATURE}:
        raise ValueError(f"{target.path}: ingredient signature drifted to {signature!r}")


def _diluted_ingredients() -> list[dict[str, Any]]:
    source = DILUTED.source_label
    return [
        _ingredient(
            "Marine broth 2216 (BD-Difco)",
            "3.74",
            "G_PER_L",
            source=source,
            notes=(
                f"{source} lists 3.74 g/L Marine broth 2216 with the BD-Difco "
                "attribute; left ungrounded as an undefined commercial broth."
            ),
        ),
        _ingredient(
            "Agar",
            "15",
            "G_PER_L",
            source=source,
            notes=f"{source} lists 15.0 g/L agar.",
            grounded=True,
        ),
        _ingredient(
            "Filtered seawater",
            "750",
            "ML_PER_L",
            source=source,
            notes=f"{source} lists 750 mL/L filtered seawater.",
        ),
        _ingredient(
            "Distilled water",
            "250",
            "ML_PER_L",
            source=source,
            notes=f"{source} lists 250 mL/L distilled water.",
            grounded=True,
        ),
    ]


def _marine_agar_ingredients() -> list[dict[str, Any]]:
    return [
        _ingredient(
            "Marine agar 2216 (BD-Difco)",
            "55.1",
            "G_PER_L",
            source="JCM Medium 118",
            notes=(
                "JCM Medium 118 lists 55.1 g/L Marine agar 2216 with the "
                "BD-Difco attribute; left ungrounded as an undefined commercial agar."
            ),
        ),
        _ingredient(
            "Distilled water",
            "1.0",
            "L",
            source="JCM Medium 118",
            notes="JCM Medium 118 lists 1.0 L distilled water.",
            grounded=True,
        ),
    ]


def _sodium_carbonate_solution(target: PhTarget) -> dict[str, Any]:
    return {
        "preferred_term": "10% Na2CO3 solution",
        "concentration": {"value": "variable", "unit": "VARIABLE"},
        "notes": (
            f"{target.source_label} adjusts the autoclaved Marine Agar 2216 base "
            f"to pH {target.ph_value:.1f} with sterilized 10% Na2CO3 solution."
        ),
        "composition": [
            _ingredient(
                "Na2CO3",
                "10.0",
                "PERCENT_W_V",
                source=target.source_label,
                notes=f"{target.source_label} specifies 10% Na2CO3 solution.",
                grounded=True,
                physicochemical_roles=["BUFFER"],
            )
        ],
        "preparation_notes": "Sterilize the 10% Na2CO3 solution before addition.",
    }


def _parent_media(target: PhTarget) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{PARENT_PATH}",
        "relationship": "PH_VARIANT",
        "id": PARENT_ID,
        "name": PARENT_NAME,
        "notes": (
            f"{target.source_label} adjusts JCM Medium 118 Marine Agar 2216 "
            f"to pH {target.ph_value:.1f}."
        ),
    }


def _variant_child(target: PhTarget) -> dict[str, str]:
    return {
        "path": f"data/normalized_yaml/{target.path}",
        "relationship": "PH_VARIANT",
        "id": target.identifier,
        "name": target.path.stem,
        "notes": (
            f"{target.source_label} adjusts JCM Medium 118 Marine Agar 2216 "
            f"to pH {target.ph_value:.1f}."
        ),
    }


def repair_diluted_record(doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_diluted_target(doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    repaired["notes"] = (
        "JCM Medium 644 defines Diluted Marine Agar as 3.74 g/L Marine broth 2216 "
        "(BD-Difco), 15 g/L Agar, 750 mL/L filtered seawater, and 250 mL/L "
        "distilled water."
    )
    repaired["ingredients"] = _diluted_ingredients()
    _put_after(
        repaired,
        "preparation_steps",
        [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Prepare Diluted Marine Agar.",
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Autoclave at 121 C for 15 min.",
            },
        ],
        "ingredients",
    )
    _put_after(repaired, "sterilization", {"method": "AUTOCLAVE"}, "preparation_steps")
    repaired.pop("kg_microbe_match", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, DILUTED.references)
    _append_event(
        repaired,
        action=DILUTED_ACTION,
        source=DILUTED.mediadive_rest,
        notes=(
            "Rebuilt the JCM Medium 644 recipe from MediaDive/JCM evidence; "
            "preserved Marine broth 2216 and filtered seawater as intentionally "
            "unmapped components."
        ),
    )
    return repaired


def repair_ph_record(target: PhTarget, doc: dict[str, Any]) -> dict[str, Any]:
    _ensure_ph_target(target, doc)

    repaired = copy.deepcopy(doc)
    repaired["medium_type"] = "COMPLEX"
    repaired["composition_type"] = "UNDEFINED"
    repaired["physical_state"] = "SOLID_AGAR"
    _put_after(repaired, "ph_value", target.ph_value, "physical_state")
    repaired["notes"] = (
        f"{target.source_label} defines Marine Agar 2216 at pH {target.ph_value:.1f} "
        "as JCM Medium 118 Marine Agar 2216 adjusted after autoclaving with "
        "sterilized 10% Na2CO3 solution."
    )
    repaired["ingredients"] = _marine_agar_ingredients()
    _put_after(
        repaired,
        "solutions",
        [_sodium_carbonate_solution(target)],
        "ingredients",
    )
    _put_after(
        repaired,
        "preparation_steps",
        [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Prepare Marine agar 2216 from JCM Medium 118.",
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Autoclave the Marine Agar 2216 base at 121 C for 15 min.",
            },
            {
                "step_number": 3,
                "action": "ADJUST_PH",
                "description": (
                    f"After autoclaving, adjust pH to {target.ph_value:.1f} with "
                    "sterilized 10% Na2CO3 solution."
                ),
            },
        ],
        "solutions",
    )
    _put_after(repaired, "sterilization", {"method": "AUTOCLAVE"}, "preparation_steps")
    repaired["variant_relationship"] = "PH_VARIANT"
    repaired["variant_modifications"] = [
        f"Adjusted JCM Medium 118 Marine Agar 2216 to pH {target.ph_value:.1f} " "with 10% Na2CO3."
    ]
    repaired.pop("kg_microbe_match", None)
    repaired.pop("ph_range", None)
    repaired.pop("temperature_value", None)
    repaired.pop("temperature_range", None)
    _ensure_flags(repaired)
    _ensure_references(repaired, target.references)
    _put_after(repaired, "parent_media", _parent_media(target), "references")
    _append_event(
        repaired,
        action=PH_ACTION,
        source=target.mediadive_rest,
        notes=(
            f"Rebuilt the {target.source_label} pH wrapper from MediaDive/JCM "
            "evidence and linked it to the JCM Medium 118 Marine Agar 2216 parent."
        ),
    )
    return repaired


def repair_parent(doc: dict[str, Any]) -> dict[str, Any]:
    if doc.get("id") != PARENT_ID:
        raise ValueError(f"{PARENT_PATH}: expected id {PARENT_ID}, found {doc.get('id')!r}")

    repaired = copy.deepcopy(doc)
    variant_children = repaired.setdefault("variant_children", [])
    if not isinstance(variant_children, list):
        raise ValueError("variant_children is not a list")

    target_paths = {f"data/normalized_yaml/{target.path}" for target in PH_TARGETS}
    target_ids = {target.identifier for target in PH_TARGETS}
    retained = [
        child
        for child in variant_children
        if not (
            isinstance(child, dict)
            and (child.get("path") in target_paths or child.get("id") in target_ids)
        )
    ]
    retained.extend(_variant_child(target) for target in PH_TARGETS)
    repaired["variant_children"] = sorted(
        retained,
        key=lambda child: str(child.get("path") or "") if isinstance(child, dict) else "",
    )
    _append_event(
        repaired,
        action=PARENT_ACTION,
        source="; ".join([*(target.jcm_url for target in PH_TARGETS), JCM_118]),
        notes=(
            "Added or refreshed reciprocal PH_VARIANT links for the specialized "
            "JCM 1001 and JCM 1016 Marine Agar 2216 pH wrappers."
        ),
    )
    return repaired


def plan_repairs(normalized: Path = NORMALIZED) -> dict[Path, dict[str, Any]]:
    plans = {
        normalized / DILUTED.path: repair_diluted_record(_load(normalized / DILUTED.path)),
        normalized / PARENT_PATH: repair_parent(_load(normalized / PARENT_PATH)),
    }

    for target in PH_TARGETS:
        plans[normalized / target.path] = repair_ph_record(
            target,
            _load(normalized / target.path),
        )
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
