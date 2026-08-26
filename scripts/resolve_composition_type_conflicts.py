#!/usr/bin/env python3
"""Resolve the 46 reviewed DEFINED/undefined-component contradictions.

Every target currently asserts both ``medium_type: DEFINED`` and
``composition_type: DEFINED`` while carrying yeast extract, peptone, soytone, or
casamino acids. Presence of one of those mixtures proves DEFINED false.

The target composition is conservative. ``SEMI_DEFINED`` is used only for the
six records satisfying the repository's positive-evidence rule: exactly one
undefined component below 0.5 g/L and every other ingredient CHEBI-grounded.
All remaining records become ``UNDEFINED``; that value is true without making
the stronger claim that the undefined input is merely a small supplement.
``medium_type`` changes to its maintained compatibility counterpart ``COMPLEX``
in the same operation.

The migration is dry-run by default. It changes only the two scalar lines and
requires exact path, record id, undefined-component names, and mass signatures.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
from audit_composition_type import undefined_components, undefined_mass  # noqa: E402

NORMALIZED = REPO / "data" / "normalized_yaml"


@dataclass(frozen=True)
class Target:
    path: str
    record_id: str
    undefined_names: str
    undefined_g_per_l: str
    composition_type: str


TARGETS = tuple(
    Target(*row)
    for row in (
        (
            "archaea/KOMODO_141_METHANOGENIUM_medium.yaml",
            "CultureMech:004144",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "archaea/KOMODO_390_PYROBACULUM_MEDIUM.yaml",
            "CultureMech:005172",
            "Trypticase peptone; Yeast extract",
            "0.69307",
            "UNDEFINED",
        ),
        (
            "archaea/KOMODO_927_HALORHABDUS_UTAHENSIS_medium.yaml",
            "CultureMech:006845",
            "Yeast extract",
            "1",
            "UNDEFINED",
        ),
        (
            "archaea/halorhabdus_utahensis_medium.yaml",
            "CultureMech:002099",
            "Yeast extract",
            "1",
            "UNDEFINED",
        ),
        (
            "archaea/methanococcus_sp_medium.yaml",
            "CultureMech:004145",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "archaea/methanogenium_medium_h2_co2.yaml",
            "CultureMech:000254",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "archaea/pyrobaculum_medium.yaml",
            "CultureMech:001497",
            "Trypticase peptone; Yeast extract",
            "0.69307",
            "UNDEFINED",
        ),
        (
            "bacterial/NBRC_14.yaml",
            "CultureMech:007476",
            "Soytone",
            "1",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_13380.yaml",
            "CultureMech:005170",
            "Trypticase peptone; Yeast extract",
            "0.69307",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_13514.yaml",
            "CultureMech:005171",
            "Trypticase peptone; Yeast extract",
            "0.69307",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_14042.yaml",
            "CultureMech:004140",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_1497_dsm_1537_dsm_2067_dsm_2279_dsm_2373_dsm_17251_and_dsm17508.yaml",
            "CultureMech:004129",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_15219_dsm_16458_and_dsm_18860.yaml",
            "CultureMech:004128",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_15558_and_dsm_16458.yaml",
            "CultureMech:004141",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_2095.yaml",
            "CultureMech:004132",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_21626.yaml",
            "CultureMech:004124",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_2373.yaml",
            "CultureMech:004135",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_2831.yaml",
            "CultureMech:004136",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_4184.yaml",
            "CultureMech:005168",
            "Trypticase peptone; Yeast extract",
            "0.69307",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_4185.yaml",
            "CultureMech:005169",
            "Trypticase peptone; Yeast extract",
            "0.69307",
            "UNDEFINED",
        ),
        (
            "bacterial/for_dsm_4254.yaml",
            "CultureMech:004139",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/for_strain_dsm_1498_dsm_15558_and_dsm_22353.yaml",
            "CultureMech:004134",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/ignavibacteria_medium.yaml",
            "CultureMech:000835",
            "Yeast extract",
            "2",
            "UNDEFINED",
        ),
        (
            "bacterial/lentimonas_medium.yaml",
            "CultureMech:001187",
            "Yeast extract",
            "0.01",
            "UNDEFINED",
        ),
        (
            "bacterial/medium_141_modified_for_dsm_11571.yaml",
            "CultureMech:004122",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/medium_141_modified_for_dsm_11916.yaml",
            "CultureMech:004123",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/medium_141_modified_for_dsm_1224.yaml",
            "CultureMech:004125",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/medium_141_modified_for_dsm_13459.yaml",
            "CultureMech:004126",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/medium_141_modified_for_dsm_14266.yaml",
            "CultureMech:004127",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/medium_141_modified_for_dsm_3599.yaml",
            "CultureMech:004130",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/medium_141_modified_for_dsm_3821.yaml",
            "CultureMech:004131",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/medium_141_modified_for_dsm_4138.yaml",
            "CultureMech:004133",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/medium_141_modified_for_dsm_7268.yaml",
            "CultureMech:004137",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/medium_141_modified_for_dsm_7466.yaml",
            "CultureMech:004138",
            "Yeast extract; Trypticase peptone",
            "3.94866",
            "UNDEFINED",
        ),
        (
            "bacterial/petrotoga_medium.yaml",
            "CultureMech:001856",
            "Yeast extract",
            "0.197433",
            "SEMI_DEFINED",
        ),
        (
            "bacterial/thermochromatium_allochromatium_medium.yaml",
            "CultureMech:000935",
            "Yeast extract",
            "0.1",
            "UNDEFINED",
        ),
        (
            "specialized/definedmedia_adamslab_glucose_yeastextract.yaml",
            "CultureMech:015510",
            "Yeast Extract",
            "1",
            "UNDEFINED",
        ),
        (
            "specialized/mccas_h2_complete.yaml",
            "CultureMech:015576",
            "CASamino acids",
            "2",
            "UNDEFINED",
        ),
        (
            "specialized/mccas_h2_fe_free.yaml",
            "CultureMech:015577",
            "CASamino acids",
            "2",
            "UNDEFINED",
        ),
        (
            "specialized/mmx_casamino.yaml",
            "CultureMech:015601",
            "casamino acids",
            "1.5",
            "UNDEFINED",
        ),
        (
            "specialized/rch2_defined_glucose_ye.yaml",
            "CultureMech:015709",
            "Yeast Extract",
            "0.1",
            "SEMI_DEFINED",
        ),
        (
            "specialized/rch2_defined_glucose_ye_10mmnitrate.yaml",
            "CultureMech:015710",
            "Yeast Extract",
            "0.1",
            "SEMI_DEFINED",
        ),
        (
            "specialized/rch2_defined_nocarbon_ye.yaml",
            "CultureMech:015721",
            "Yeast Extract",
            "0.01",
            "SEMI_DEFINED",
        ),
        (
            "specialized/rch2_defined_ye.yaml",
            "CultureMech:015726",
            "Yeast Extract",
            "0.1",
            "SEMI_DEFINED",
        ),
        (
            "specialized/rch2_defined_ye_10mm_nitrate.yaml",
            "CultureMech:015727",
            "Yeast Extract",
            "0.1",
            "SEMI_DEFINED",
        ),
        (
            "specialized/xantho_mme_glucose_casamino.yaml",
            "CultureMech:015787",
            "casamino acids",
            "1.5",
            "UNDEFINED",
        ),
    )
)


def _component_signature(doc: dict[str, Any]) -> tuple[str, str]:
    hits = undefined_components(doc)
    names = "; ".join(str(row.get("preferred_term") or "") for row in hits)
    mass = undefined_mass(hits)
    return names, "" if mass is None else f"{mass:g}"


def plan_repair(doc: dict[str, Any], target: Target, text: str) -> tuple[str, bool]:
    if str(doc.get("id") or "") != target.record_id:
        raise ValueError(
            f"{target.path}: expected {target.record_id}, found {doc.get('id')!r}"
        )
    if _component_signature(doc) != (
        target.undefined_names,
        target.undefined_g_per_l,
    ):
        raise ValueError(f"{target.path}: undefined-component signature drifted")

    current = (str(doc.get("medium_type") or ""), str(doc.get("composition_type") or ""))
    desired = ("COMPLEX", target.composition_type)
    if current == desired:
        return text, False
    if current != ("DEFINED", "DEFINED"):
        raise ValueError(f"{target.path}: unexpected type axes {current!r}")

    updated = text.replace("medium_type: DEFINED\n", "medium_type: COMPLEX\n", 1)
    updated = updated.replace(
        "composition_type: DEFINED\n",
        f"composition_type: {target.composition_type}\n",
        1,
    )
    if updated == text:
        raise ValueError(f"{target.path}: could not replace both type lines")
    return updated, True


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--normalized-dir", type=Path, default=NORMALIZED)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)

    plans: list[tuple[Path, str]] = []
    for target in TARGETS:
        path = args.normalized_dir / target.path
        text = path.read_text(encoding="utf-8")
        doc = yaml.safe_load(text)
        if not isinstance(doc, dict):
            raise SystemExit(f"{path}: expected a YAML mapping")
        try:
            updated, changed = plan_repair(doc, target, text)
        except ValueError as exc:
            raise SystemExit(str(exc)) from exc
        print(
            f"{'fix' if changed else 'skip':4s}  {target.path}: "
            f"DEFINED -> {target.composition_type}"
        )
        if changed:
            plans.append((path, updated))

    if args.apply:
        for path, updated in plans:
            path.write_text(updated, encoding="utf-8")
    print(f"\n{'updated' if args.apply else 'would update'} {len(plans)} record(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
