#!/usr/bin/env python3
"""Prepare manual evidence-completion decisions for #683 (2026-11-16).

Inputs: original pinned queue, prior coverage, clean-base recipe bytes, inspected
primary captures. Output: new exact-preimage proposal; never edits recipes.
Scientific decisions below are manual, not inferred from name matching or regex.
"""

from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import json
import subprocess
from collections import Counter
from pathlib import Path

import yaml

BASE = "65df76935898c6e973697389b76449686b88f8cb"
QUEUE_SHA = "dd5faea741da0a11e8eb86cad2976e8bf51d42884c601e96973eba61748330ca"
ROOT = Path(__file__).resolve().parents[2]
NEW = ".temp/variant-completeness-683/sources/"
OLD = ".temp/variant-683/"
SOURCES = {
    "matsui": (
        "DOI:10.1104/pp.18.00453",
        "matsui-2018-html/source.html",
        "beecd6db87651dbf5f4119169a755249ba977070ee4a7046d26dff3bab3b5d43",
        "Methods: culture conditions and transformation",
    ),
    "kato": (
        "doi:10.1264/jsme2.ME19128",
        "methylotroph-2020/source.xml",
        "2ade9577ad927b568273334fa9b14d2da22d155f877535d317ad13a0977a224d",
        "Methods: cultivation of methanotrophs",
    ),
    "jcm": (
        "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219",
        "jcm-1219/source.html",
        "2806065d7ad8b108c3b23277e18e4209fbf7680f6e1f911e74797633cffb788b",
        "Medium 1219 preparation, before and after autoclaving",
    ),
    "shang": (
        "doi:10.1007/s00203-013-0895-5",
        "shang-2013/source.xml",
        "d26c9bfe4a445ba08b9cfe9268c088dd792f95d136361d25a8837165a4bc5bae",
        "Methods: modified DSMZ640, substrate-specific experiments",
    ),
    "kosch": (
        "doi:10.5283/epub.34741",
        "koschnitzki-2017/source.pdf",
        "21117464e1481e058031575f2bd668afd37677cd842636230adf54982111e8f9",
        "Printed pages27–28, sections2.2.2.1–2.2.2.2",
    ),
    "blood": (
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium693.pdf",
        "dsmz-693/source.pdf",
        "bc08397f9aaad4e1f5615cb0957e3359859c24e96048098a7391312f40db787d",
        "Page1, Columbia Blood Medium",
    ),
    "bacdive": (
        "https://bacdive.dsmz.de/strain/14567",
        "bacdive-14567/source.html",
        "cd8a83938bf166884c464027fc77342841252638faf882c269de1be908737ade",
        "Strain aliases and culture-medium693 composition",
    ),
    "sakai": (
        "https://soka.repo.nii.ac.jp/record/39772/files/kogakukenkyuka_SAKAI-HIROYUKI%28%E5%85%A8%E6%96%87%29.pdf",
        "sakai-thesis/source.pdf",
        "12cf628555cb29552e907e4f73215f62655047cbbaa2b2900bc6d5f197f03c4f",
        "2019 dissertation ch3, sections3.2.1,3.2.3.3,3.3.2.3; printed pages35,38,42",
    ),
    "ohanlon": (
        "doi:10.1186/1471-2334-11-200",
        "ohanlon-2011/source.xml",
        "37875cb2ef97cf504d653942057a525e07fa9ca1519a53576c2238364df841d9",
        "Methods: growth of bacterial species, explicit basal/supplemented contrast",
    ),
    "ms10": (
        "doi:10.1111/j.1365-2672.1995.tb03131.x",
        "ms10-1995-html/source.html",
        "bc9d34a0206c79d44a445e40c9004878057131a25f722c89a647dba8fff54797",
        "Publisher abstract only; full article requires subscription",
    ),
}
PRIOR_SOURCES = {
    "tsuji": (
        "DOI:10.1007/s10126-021-10037-4",
        "sources/tsuji-2021-table-s1/source.pdf",
        "1cc2581bf2363ea89d31f170ae398b94d1125c647cc1c655a54417e6c73aac98",
        "TableS1: basal components(mM), trace elements(µM)",
    ),
    "willard": (
        "doi:10.1128/mbio.01033-24",
        "sources/willard-2024/source.xml",
        "7808bc365628f8d1a71ab0a20135f2f0619a19fc6db1d587961007e8c0ecaba3",
        "Materials and Methods: low-sulfate Brock salts and species-specific pH",
    ),
    "carini": (
        "doi:10.1038/ncomms5346",
        "family-sources/carini-2014/source.pdf",
        "f20160ac5dc3840b1fb757178b876f0bd41f34fe6cb2be1aec2928d28dbf667e",
        "Page5 visually inspected: alternative-phosphorus treatments; PDF text corrupts µ",
    ),
}


def digest(data):
    return hashlib.sha256(data).hexdigest()


def evidence(key, snippet, explanation, support="SUPPORT"):
    reference = (SOURCES | PRIOR_SOURCES)[key][0]
    return {
        "reference": reference,
        "supports": support,
        "snippet": snippet,
        "explanation": explanation,
    }


class Proposal:
    def __init__(self, queue, coverage):
        self.rows = queue
        self.coverage = coverage
        self.records = {}
        self.documents = {}
        self.dispositions = {}

    def target(self, number):
        row = self.rows[number - 1]
        path = "data/normalized_yaml/" + row["source_path"]
        if path not in self.records:
            content = (ROOT / path).read_bytes()
            base_content = subprocess.check_output(["git", "show", f"{BASE}:{path}"], cwd=ROOT)
            if content != base_content:
                raise ValueError("Recipe changed since reviewed base: " + path)
            document = yaml.safe_load(content)
            if document["id"] != row["recipe_id"]:
                raise ValueError("Recipe ID drift")
            self.documents[path] = document
            self.records[path] = {
                "path": path,
                "recipe_id": document["id"],
                "expected_sha256": digest(content),
                "variants": [],
            }
        vi, mi = int(row["variant_index"]), int(row["modification_index"])
        variant = self.documents[path]["variants"][vi]
        if (
            variant["name"] != row["variant_name"]
            or variant["modifications"][mi] != row["modification_text"]
        ):
            raise ValueError("Original queue coordinate/text drift")
        targets = self.records[path]["variants"]
        target = next((v for v in targets if v["variant_index"] == vi), None)
        if target is None:
            target = {"variant_index": vi, "variant_name": variant["name"]}
            targets.append(target)
        return row, self.records[path], target, variant

    def resulting_text(self, number):
        row, _, target, _ = self.target(number)
        mi = int(row["modification_index"])
        replacements = target.get("replace_modifications", [])
        return next(
            (v["replacement"] for v in replacements if v["modification_index"] == mi),
            row["modification_text"],
        )

    def correction(self, number, replacement):
        row, _, target, _ = self.target(number)
        target.setdefault("replace_modifications", []).append(
            {
                "modification_index": int(row["modification_index"]),
                "expected": row["modification_text"],
                "replacement": replacement,
            }
        )

    def field(self, number, path, replacement):
        _, record, _, _ = self.target(number)
        current = self.documents[record["path"]]
        for key in path:
            current = current[key]
        record.setdefault("field_replacements", []).append(
            {"path": path, "expected": copy.deepcopy(current), "replacement": replacement}
        )

    def change(
        self,
        number,
        action,
        label,
        stage,
        items,
        concentration=None,
        amount=None,
        old=None,
        notes="",
    ):
        row, _, target, _ = self.target(number)
        value = {
            "action": action,
            "ingredient": {"preferred_term": label},
            "stage": stage,
            "source_modification_index": int(row["modification_index"]),
            "source_text": self.resulting_text(number),
            "evidence": items,
        }
        if concentration:
            value["ingredient"]["concentration"] = concentration
        if amount:
            value["amount"] = amount
        if old:
            value["replaced_ingredient"] = {"preferred_term": old}
        if notes:
            value["notes"] = notes
        target.setdefault("append_changes", []).append(value)

    def mention(
        self,
        number,
        label,
        reason,
        fields,
        action="UNSPECIFIED",
        stage="unspecified in source",
        quantity=None,
        items=None,
    ):
        row, _, target, _ = self.target(number)
        text = self.resulting_text(number)
        if label not in text:
            raise ValueError(f"Mention label is not literal in row{number}: {label}")
        value = {
            "source_label": label,
            "reported_action": action,
            "stage": stage,
            "source_modification_index": int(row["modification_index"]),
            "source_text": text,
            "reason": reason,
            "held_fields": fields,
        }
        if quantity:
            value["reported_quantity"] = quantity
        if items:
            value["evidence"] = items
        target.setdefault("append_mentions", []).append(value)

    def dispose(self, number, status, reason):
        row, _, target, _ = self.target(number)
        mi = int(row["modification_index"])
        self.dispositions[number] = {
            "queue_row_number": number,
            "prior_status": self.coverage[number]["status"],
            "status": status,
            "reason": reason,
            "append_assertion_count": sum(
                v["source_modification_index"] == mi for v in target.get("append_changes", [])
            ),
            "append_mention_count": sum(
                v["source_modification_index"] == mi for v in target.get("append_mentions", [])
            ),
        }


def conc(value, unit, basis=None):
    result = {"value": value, "unit": unit}
    if basis:
        result["per_volume"] = basis
    return result


def amount(value, unit, statement):
    return {"value": value, "unit": unit, "basis": "PER_BATCH", "basis_statement": statement}


def prepare(p):
    # Newly accessible Matsui Methods support a named stock and agar context,
    # not an inferred expansion of the stock or addition to every liquid culture.
    for n in (5, 28):
        p.change(
            n,
            "ADD",
            "Guillard f solution",
            "Matsui2018 F/2ASW diatom culture formulation",
            [
                evidence(
                    "matsui",
                    "artificial seawater supplemented with one-half-strength Guillard’s f solution",
                    "Methods, culture conditions. Named nutrient mixture at half strength; no unreported component concentrations or parent-medium equivalence inferred.",
                )
            ],
            notes="Named stock only; half-strength is a relative formulation statement, not a measured absolute ingredient concentration.",
        )
        p.dispose(
            n,
            "STRUCTURED",
            "Primary full Methods now inspected; named Guillard mixture preserved without decomposition.",
        )
    p.change(
        6,
        "ADD",
        "agar",
        "Matsui2018 transformation and selection plates; separate from liquid culture",
        [
            evidence(
                "matsui",
                "F/2ASW agar plate",
                "Transformation Methods directly name agar plates. Agar quantity is not printed in this passage; no dose is inferred.",
            )
        ],
    )
    p.dispose(
        6,
        "STRUCTURED",
        "Agar is supported only in the stated plate stages; liquid formulations remain separate.",
    )

    p.correction(
        8,
        "Modified F/2ASW uses 1 nM sodium selenite (Na2SeO3) and 0.1 mM sodium metasilicate nonahydrate (Na2SiO3.9H2O).",
    )
    p.change(
        8,
        "ADD",
        "Na2SeO3",
        "Tsuji2021 modified F/2ASW sodium-response formulation",
        [
            evidence(
                "tsuji",
                "Na2SeO3 b 0.001",
                "TableS1 header 'Trace elements (μM)' supplies the unit. Whitespace-normalized row quote gives0.001µM, equivalent to1nM; prior10nM prose was incorrect (#759).",
            )
        ],
        conc("1", "NANOMOLAR"),
        notes="0.001µM×1000nM/µM=1nM; no mass conversion or universal parent supplementation.",
    )
    p.change(
        8,
        "ADD",
        "Na2SiO3.9H2O",
        "Tsuji2021 modified F/2ASW sodium-response formulation",
        [
            evidence(
                "tsuji",
                "Na2SiO3·9H2O b 0.1",
                "TableS1 header 'Basal seawater components (mM)' supplies the unit. Whitespace-normalized row gives0.1mM; nonahydrate is explicit.",
            )
        ],
        conc("0.1", "MILLIMOLAR"),
    )
    p.dispose(
        8, "STRUCTURED", "Corrected source conflict759; exact source form and1nM selenite retained."
    )

    hartzell = "Exact Hartzell1999 chapter remained unavailable anonymously (publisher403). Existing prose is retained as an unapproved source claim; Reed2001 does not verify this distinct preparation."
    for label in ("NaCl", "MgSO4", "MgCl2.6H2O", "KCl", "NH4Cl", "CaCl2.2H2O", "K2HPO4"):
        p.mention(
            74, label, hartzell, ["SOURCE_CLAIM", "QUANTITY"], stage="Hartzell1999 STL salt stocks"
        )
    p.dispose(
        74,
        "HELD_EVIDENCE",
        "All seven literal salt names retained as withheld mentions; source stock formulation remains unverified.",
    )
    for n, labels, quantity in (
        (75, ("PIPES",), "20 ml of1M perL"),
        (76, ("sodium lactate",), "7 ml of30%(w/v) perL"),
        (77, ("Wolfe's vitamin mixture",), "10 ml/L"),
        (79, ("Na2S", "Na2S2O3"), "100mM/200mM stock added at0.5%v/v"),
        (80, ("N2",), None),
    ):
        for label in labels:
            p.mention(
                n,
                label,
                hartzell + " The separately verified Reed-stage events remain supported.",
                ["SOURCE_CLAIM"],
                stage="Hartzell1999 STL preparation, separate from Reed2001",
                quantity=quantity,
            )
        p.dispose(
            n,
            "PARTIALLY_STRUCTURED",
            "Existing Reed events preserved; distinct Hartzell claim(s) now machine-readable and withheld.",
        )
    for label in (
        "1000x trace element stock",
        "Na2EDTA.2H2O",
        "Mn",
        "Co",
        "Zn",
        "Ni",
        "Cu",
        "B",
        "Al",
        "Mo",
        "W",
        "Se",
        "V",
        "(NH4)2Fe(SO4)2",
    ):
        p.mention(
            78,
            label,
            hartzell
            + " Element symbols name unspecified salts and do not establish counterions/hydration.",
            ["SOURCE_CLAIM", "IDENTITY_FORM"],
            stage="Hartzell1999 STL trace stock",
        )
    p.dispose(
        78,
        "HELD_EVIDENCE",
        "Literal stock/chemical labels retained without inventing salt species from elemental symbols.",
    )

    p.mention(
        81,
        "SME",
        "Primary thesis verifies the half-strength named base. Expansion or equivalence to this imported parent is not established; preserve this as a named formulation mention rather than duplicate its constituents.",
        ["OPERATION"],
        stage="Koschnitzki2017 half-strength SME base preparation",
        quantity="500mL SME stock in the stated1000mL preparation",
        items=[
            evidence(
                "kosch",
                "SME",
                "Section2.2.2.2 table lists500mL SME and final water adjustment to1000mL; section2.2.2.1 separately defines the stock.",
                "PARTIAL",
            )
        ],
    )
    p.dispose(
        81,
        "CONTEXT_ONLY",
        "Half-strength base formulation verified; named base retained as operation-held mention, no automatic parent expansion.",
    )
    p.change(
        82,
        "ADD",
        "elemental sulfur",
        "Koschnitzki2017 serum-bottle preparation after20mL medium dispensing",
        [
            evidence(
                "kosch",
                "one spatula of elemental sulfur added",
                "Printed page28. This is an uncalibrated spatula amount, not a mass concentration.",
            )
        ],
        notes="One spatula per prepared bottle; do not manufacture a gram or g/L dose.",
    )
    p.dispose(
        82,
        "STRUCTURED",
        "Elemental sulfur identity supported with the unquantified spatula basis preserved.",
    )
    p.change(
        83,
        "ADD",
        "Na2S.7-9H2O",
        "Koschnitzki2017 reduction of the prepared half-SME batch",
        [
            evidence(
                "kosch",
                "Na2S x 7-9 H2O (0.5 g dissolved in 2 ml ddH2O)",
                "Printed page28. Preserve the source's hydration range; do not silently select nonahydrate from the separate reagent list.",
            )
        ],
        amount=amount(
            "0.5",
            "G",
            "Added in2mL water after the half-SME preparation had been adjusted to1000mL; no exact final-volume concentration inferred.",
        ),
        notes="Literal source hydration range retained without ontology identity or molar-mass conversion.",
    )
    p.mention(
        83,
        "Na2S",
        "Sulfide addition and0.5g batch amount are supported; exact hydration remains the source range7–9 rather than a uniquely resolved chemical form.",
        ["IDENTITY_FORM"],
        "ADD",
        "Koschnitzki2017 reducing-agent preparation",
    )
    p.dispose(
        83,
        "PARTIALLY_STRUCTURED",
        "Supported sulfide addition; literal hydration range remains explicitly unresolved.",
    )
    p.change(
        84,
        "ADD",
        "NaHCO3",
        "Koschnitzki2017 half-SME base before reducing-agent addition",
        [
            evidence(
                "kosch",
                "NaHCO3 0.16 g 1.9 mM",
                "Section2.2.2.2 table, whitespace-normalized row:0.16g with water adjusted to1000mL before the separate reducing-agent addition.",
            )
        ],
        amount=amount(
            "0.16",
            "G",
            "Half-SME preparation adjusted to1000mL before adding the reducing-agent solution.",
        ),
    )
    for label, value in (("SrCl2.6H2O", "0.015"), ("KI", "0.5")):
        p.change(
            84,
            "ADD",
            label,
            "Koschnitzki2017 SME stock preparation;500mL stock used for half-SME",
            [
                evidence(
                    "kosch",
                    ("SrCl2 x 6 H2O 0.015 g" if label.startswith("Sr") else "KI 0.5 g"),
                    "Section2.2.2.1 stock table, whitespace-normalized row, adjusted to1000mL. This stock amount is not the final half-SME amount.",
                )
            ],
            amount=amount(
                value,
                "G",
                "SME stock batch adjusted to1000mL; only500mL of this stock is used in the separate half-SME preparation.",
            ),
        )
    p.dispose(
        84,
        "STRUCTURED",
        "Named bicarbonate and stock-specific strontium/iodide retained with distinct preparation stages and absolute amounts.",
    )

    p.correction(
        110,
        "65-75C; species-specific pH2-3, adjusted with concentrated HCl in the Willard2024 formulation.",
    )
    p.change(
        110,
        "ADD",
        "HCl",
        "Willard2024 species-specific medium pH adjustment",
        [
            evidence(
                "willard",
                "media pH-adjusted with concentrated HCl",
                "Culture Methods name concentrated HCl only; H2SO4 was an unsupported alternative in this variant (#762). No titrant dose is reported.",
            )
        ],
    )
    p.dispose(
        110,
        "STRUCTURED",
        "Source-specific HCl correction762; unquantified titrant addition, no parent acid change.",
    )
    sakai_stage = (
        "Sakai2019 dissertation HS-1T negative anaerobic growth test; no growth after four weeks"
    )
    p.correction(
        112,
        "Anaerobic test medium reduced with Na2S.9H2O (0.5 g/L) and resazurin (1 mg/L), as specified in Sakai2019 dissertation section3.2.3.3.",
    )
    p.correction(
        113,
        "Anaerobic test headspace H2/CO2 (80:20) at110kPa; separate tests with and without10g/L elemental sulfur (Sakai2019 dissertation).",
    )
    p.correction(
        114,
        "Anaerobic test at65C and pH3.0; HS-1T did not grow even after four weeks (Sakai2019 dissertation sections3.2.3.3 and3.3.2.3).",
    )
    p.change(
        111,
        "ADD",
        "yeast extract",
        sakai_stage,
        [
            evidence(
                "sakai",
                "yeast extract (1 g/L)",
                "Results3.3.2.3 identifies the negative-test medium and absence of growth; Methods3.2.1 defines MBSY. Ingredient use is not growth support.",
            )
        ],
        conc("1", "G_PER_L"),
    )
    p.change(
        112,
        "ADD",
        "Na2S.9H2O",
        sakai_stage,
        [
            evidence(
                "sakai",
                "Na2S.9H2O (0.5 g/L)",
                "Methods3.2.3.3 explicitly specifies nonahydrate. No anhydrous mass equivalence inferred.",
            )
        ],
        conc("0.5", "G_PER_L"),
    )
    p.change(
        112,
        "ADD",
        "resazurin",
        sakai_stage,
        [
            evidence(
                "sakai",
                "Resazurin (1 mg/L)",
                "Methods3.2.3.3 identifies the oxygen indicator in the negative-growth test.",
            )
        ],
        conc("1", "MG_PER_L"),
    )
    p.change(
        113,
        "ADD",
        "elemental sulfur",
        sakai_stage + "; sulfur-containing test arm only",
        [
            evidence(
                "sakai",
                "with and without elemental sulfur (10 g/L)",
                "Separate sulfur-containing and sulfur-free tests; do not assert sulfur in the no-sulfur arm.",
            )
        ],
        conc("10", "G_PER_L"),
    )
    for label in ("H2", "CO2"):
        p.mention(
            113,
            label,
            "Gas mixture is verified in the test headspace, not an aqueous ingredient. Ratio80:20 and110kPa are gas conditions, not liquid concentrations.",
            ["OPERATION"],
            "ADD",
            sakai_stage + "; headspace",
            "H2/CO2 80:20;110kPa",
            [
                evidence(
                    "sakai",
                    "H2/CO2 (80:20, 110 kPa)",
                    "Methods3.2.3.3; phase-specific gas input retained outside the liquid ingredient occurrence set.",
                    "PARTIAL",
                )
            ],
        )
    p.dispose(
        111,
        "STRUCTURED",
        "Yeast-extract quantity verified for the negative test, not anaerobic growth.",
    )
    p.dispose(112, "STRUCTURED", "Nonahydrate and resazurin doses verified for the negative test.")
    p.dispose(
        113,
        "PARTIALLY_STRUCTURED",
        "Sulfur-containing test arm represented; gas conditions retained as phase-scoped mentions.",
    )
    p.dispose(
        114,
        "CONDITION_ONLY",
        "Exact negative-test conditions/result corrected from author's primary dissertation; no new ingredient in this row.",
    )
    _, record, target, variant = p.target(111)
    vi = target["variant_index"]
    p.field(
        111,
        ["variants", vi, "description"],
        "Anaerobic MBSY test formulation for Sulfodiicoccus acidiphilus HS-1T. The author's2019 dissertation reports no growth in this formulation after four weeks; it is not successful anaerobic cultivation.",
    )
    p.field(
        111,
        ["variants", vi, "purpose"],
        "Preserve the negative anaerobic growth-test formulation and its ingredients without asserting a growth-supporting medium.",
    )
    p.field(
        111,
        ["variants", vi, "evidence"],
        [
            evidence(
                "sakai",
                "Strain HS-1T did not grow under anaerobic conditions",
                "Dissertation3.3.2.3 reports no growth after four weeks; Methods3.2.3.3 documents the test ingredients. REFUTE applies to anaerobic growth, not to the recorded test formulation. Full2017 journal Methods were not retrieved; the explicit updated conditions are attributed to2019 dissertation.",
                "REFUTE",
            )
        ],
    )
    organisms = p.documents[record["path"]]["target_organisms"]
    removed = [
        v
        for v in organisms
        if v.get("preferred_term") == "Sulfodiicoccus acidiphilus"
        and v.get("scoped_to_variant") == variant["name"]
    ]
    if len(removed) != 1:
        raise ValueError("Expected exactly one incorrect anaerobic-growth target")
    p.field(111, ["target_organisms"], [copy.deepcopy(v) for v in organisms if v is not removed[0]])

    p.mention(
        116,
        "tryptone",
        "The inspected Auernik2008 primary Methods support yeast extract but do not verify this tryptone alternative. Preserve supported yeast-extract event separately.",
        ["SOURCE_CLAIM"],
        "ADD",
        "reported heterotrophic alternative",
        "0.1%",
    )
    p.dispose(
        116,
        "PARTIALLY_STRUCTURED",
        "Supported yeast extract unchanged; tryptone alternative explicitly withheld.",
    )

    for n in (119, 121):
        p.dispose(
            n,
            "CONTEXT_ONLY",
            "Explicitly unreported basal composition/brand/stock context; no additional named chemical requiring an invented descriptor. Existing separate supported ingredient event remains unchanged.",
        )
    for n in (123, 312, 389):
        p.mention(
            n,
            "agar",
            "Source/prose explicitly leaves an agar-change amount and operation unestablished. Liquid filtration alone does not establish zero agar or an approved REMOVE.",
            ["OPERATION", "QUANTITY"],
        )
        p.dispose(
            n,
            "CONTEXT_ONLY",
            "Unreported agar-change context retained as a withheld mention; no inferred omission.",
        )
    for n, label in ((124, "Friis medium"), (395, "M9 medium")):
        p.mention(
            n,
            label,
            "Named modified whole-medium reference, without an enumerated ingredient or formulation. Retain the literal medium identity as context; do not decompose or assert parent equivalence.",
            ["IDENTITY_FORM", "OPERATION"],
        )
        p.dispose(
            n,
            "CONTEXT_ONLY",
            "Whole-medium mention retained; source row supplies no individual ingredient to certify.",
        )

    p.correction(
        134,
        "BacDive strain14567 lists DSMZ693 with50g/L defibrinated sheep blood; DSMZ693 recipe PDF instead states5% defibrinated sheep blood without a percentage basis. This source disagreement is unresolved. The local parent contains horse blood at40g/L.",
    )
    p.change(
        134,
        "REPLACE",
        "defibrinated sheep blood",
        "BacDive14567 DSMZ693 source-specific Columbia blood agar formulation",
        [
            evidence(
                "blood",
                "5% defibrinated sheep blood",
                "DSMZ693 confirms sheep-blood identity. Percent basis is unstated; no common quantity is inferred from the differing BacDive mass concentration.",
            ),
            evidence(
                "bacdive",
                "Defibrinated sheep blood 50.0 g/l",
                "BacDive14567 medium693 confirms this type-strain source and sheep-blood identity. Its quantity differs in basis from the DSMZ PDF; only identity replacement is asserted.",
            ),
        ],
        old="horse blood",
        notes="Both source-specific quantity statements remain unresolved; no concentration or amount is approved for this replacement.",
    )
    p.mention(
        134,
        "defibrinated sheep blood",
        "Identity is supported and represented by a separate REPLACE event. Quantity-only conflict777: BacDive50g/L versus DSMZ5% with unspecified basis; no conversion chosen.",
        ["QUANTITY"],
        "REPLACE",
        "DSMZ693/BacDive14567 formulation",
        "BacDive50g/L; DSMZ5% with unspecified basis",
    )
    p.dispose(
        134,
        "PARTIALLY_STRUCTURED",
        "Sheep-for-horse identity supported; conflicting quantities retained without reconciliation by assumption.",
    )

    p.change(
        151,
        "SET_CONCENTRATION",
        "phosphite",
        "Carini2014 alternate-phosphorus utilization assay",
        [
            evidence(
                "carini",
                "1.0 µM phosphite",
                "Page5 cultivation-details paragraph, visually inspected. Nominal phosphite label/dose supported; printed NaPHO3·5H2O stoichiometry remains unresolved, with no corrected formula or mass conversion.",
            )
        ],
        conc("1.0", "MICROMOLAR"),
    )
    p.mention(
        151,
        "NaPHO3.5H2O",
        "The nominal phosphite label and1µM assay dose are independently supported. The printed salt stoichiometry/hydration remains unresolved and must not be corrected or mapped to a precise salt by assumption.",
        ["IDENTITY_FORM"],
        "SET_CONCENTRATION",
        "Carini2014 alternate-phosphorus assay",
        "nominal1µM phosphite",
    )
    p.dispose(
        151,
        "PARTIALLY_STRUCTURED",
        "Nominal phosphite occurrence/dose admitted; exact printed salt identity withheld.",
    )

    p.correction(
        192,
        "Add15.0g agar per JCM1219 preparation batch before autoclaving; the source does not specify a final1L volume.",
    )
    p.change(
        192,
        "ADD",
        "agar",
        "JCM1219 solid-medium preparation before autoclaving",
        [
            evidence(
                "jcm",
                "For preparation of solid medium, add 15.0 g agar.",
                "Source lists970mL water and separate stock/post-cooling additions;15g is an absolute batch mass, not established15g/L (#776).",
            )
        ],
        amount=amount(
            "15.0",
            "G",
            "JCM1219 listed preparation batch;970mL water plus stocks and later additions, no stated final volume.",
        ),
    )
    p.dispose(
        192, "STRUCTURED", "Corrected unsupported denominator776; source batch mass retained."
    )
    p.change(
        193,
        "REMOVE",
        "CaCl2",
        "Kato2020 Ca-free basal trace-element solution before separate metal supplementation",
        [
            evidence(
                "kato",
                "trace element solution (CaCl2 was omitted)",
                "Cultivation Methods explicitly omit CaCl2 from the trace solution. Separate after-autoclaving metal arms can add CaCl2; this is not a universal final-culture calcium absence.",
            )
        ],
    )
    p.dispose(
        193,
        "STRUCTURED",
        "Explicit trace-stock omission verified; later metal-supplement arms remain separate.",
    )
    for label in ("peptone", "yeast extract"):
        p.change(
            219,
            "REMOVE",
            label,
            "Marteinsson2010 single-carbon-source assay plates; separate from routine MB1/2",
            [
                {
                    "reference": "doi:10.1099/ijs.0.012724-0",
                    "supports": "SUPPORT",
                    "snippet": "plates containing MB1/2 without peptone and yeast extract",
                    "explanation": "Primary-paper author copy inspected at https://www.academia.edu/165327461/, printed page2730. Routine half-strength medium and specific omission-assay plates are distinct. Anonymous local capture returned403; no local source hash is claimed.",
                }
            ],
        )
    p.dispose(
        219,
        "STRUCTURED",
        "Primary paper explicitly supports the two assay-specific omissions; no routine-medium omission inferred.",
    )
    for n, labels in ((227, ("CaCO3",)), (229, ("glucose", "KH2PO4", "MgSO4.7H2O", "CaCO3"))):
        for label in labels:
            p.mention(
                n,
                label,
                "Exact1979 Brierley/Thornton primary full Methods remain subscription-only. Abstract does not verify the local ingredient/omission quantities; preserve literal labels without approving the claim.",
                ["SOURCE_CLAIM"],
                "REMOVE" if label == "CaCO3" else "UNSPECIFIED",
                "reported Becking pH5 variant",
            )
        p.dispose(
            n,
            "HELD_EVIDENCE",
            "Bounded primary retrieval reached subscription preview; explicit source labels retained in held ledger.",
        )

    for n in (239, 243, 247, 251, 255):
        p.change(
            n,
            "SET_CONCENTRATION",
            "MgCl2",
            "Jensen1993 nominal BL formulation, same variant-specific treatment",
            [
                {
                    "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
                    "supports": "SUPPORT",
                    "snippet": "MgCl2 0.52a 0.52",
                    "explanation": "Table1 row quote normalizes whitespace and superscript footnote a; header 'Concn (mM) or presence in medium' and BL column establish0.52mM. Nominal MgCl2 does not promote the parent's hexahydrate. Publisher PDF page4363 inspected via browser; no locally captured hash is claimed.",
                }
            ],
            conc("0.52", "MILLIMOLAR"),
        )
        for label in ("MgCl2", "molybdate"):
            p.mention(
                n,
                label,
                "Nominal MgCl2 presence/dose is separately supported; its hydrate is unspecified. The source's printed molybdate formula/hydration is not safely reconciled to the parent's tetrahydrate. No mass/hydrate conversion or exact-salt identity is approved.",
                ["IDENTITY_FORM"],
                stage="Jensen1993 Table1 nominal formulation",
            )
        p.dispose(
            n,
            "PARTIALLY_STRUCTURED",
            "Nominal MgCl2 retained independently of unknown hydrate; molybdate form remains quarantined.",
        )

    # Literal masses and volumes are per source preparation containing one litre
    # of distilled water. They are not normalized to a fabricated final volume.
    batch_basis = "Shang2013 preparation stated as 'per liter distilled water'; final volume after all additions is not specified."
    shang_stage = "Shang2013 modified DSMZ640 preparation per litre of water input"
    p.correction(
        260,
        "Shang2013 lists FeCl3.6H2O2.5mg per preparation batch containing1L distilled-water input; this does not establish a final2.5mg/L concentration or the exact displaced ferrous iron form.",
    )
    p.correction(
        261,
        "Shang2013 adds trace element solution SL-10(1mL, DSMZ320) and vitamin solution(5mL, DSMZ141, filter-sterilized) per batch containing1L distilled-water input; final volume is unspecified.",
    )
    p.correction(
        262,
        "Shang2013 adds resazurin0.5mg per batch containing1L distilled-water input; final volume is unspecified.",
    )
    p.correction(
        263,
        "Shang2013 lists10.0g substrate per preparation batch containing1L distilled-water input, with separate oat spelt xylan, xylose and glucose experiments; no simultaneous mixture or universal fixed-glucose removal is inferred.",
    )
    p.correction(
        264,
        "Shang2013 recipe per1L distilled-water input:0.9g NH4Cl,0.9g NaCl,0.4g MgCl2.6H2O,0.75g KH2PO4,1.5g K2HPO4,0.75g cysteine-HCl.H2O,2g tryptone,1g yeast extract; pH7.0, prepared under100%N2,5mL portions in15mL Hungate tubes, autoclaved. This water-input basis is not a stated final medium volume.",
    )
    components = {
        260: [("FeCl3.6H2O", "2.5", "MG", "2.5 mg FeCl3 × 6 H2O")],
        261: [
            ("trace element solution SL-10", "1", "ML", "1 ml trace element solution SL-10"),
            ("vitamin solution", "5", "ML", "5 ml vitamin solution"),
        ],
        262: [("resazurin", "0.5", "MG", "0.5 mg resazurin")],
        264: [
            ("NH4Cl", "0.9", "G", "0.9 g NH4Cl"),
            ("NaCl", "0.9", "G", "0.9 g NaCl"),
            ("MgCl2.6H2O", "0.4", "G", "0.4 g MgCl2 × 6 H2O"),
            ("KH2PO4", "0.75", "G", "0.75 g KH2PO4"),
            ("K2HPO4", "1.5", "G", "1.5 g K2HPO4"),
            ("cysteine-HCl.H2O", "0.75", "G", "0.75 g cysteine-HCl × H2O"),
            ("tryptone", "2", "G", "2 g tryptone"),
            ("yeast extract", "1", "G", "1 g yeast extract"),
        ],
    }
    for n, components_for_row in components.items():
        for label, value, unit, snippet in components_for_row:
            p.change(
                n,
                "ADD",
                label,
                shang_stage,
                [
                    evidence(
                        "shang",
                        snippet,
                        "Methods full formulation uses the heading 'per liter distilled water'. Absolute source-batch input is retained; ADD is source-stage input, not an asserted difference from every imported parent ingredient.",
                    )
                ],
                amount=amount(value, unit, batch_basis),
                notes="No complete parent-equivalence or ferrous-to-ferric substitution is inferred from source presence alone.",
            )
        if n == 260:
            p.mention(
                n,
                "ferrous iron",
                "Ferric hexahydrate source input is verified; this source passage does not identify a specific displaced ferrous salt or demonstrate chemical-form equivalence to the parent.",
                ["OPERATION", "IDENTITY_FORM"],
                "REPLACE",
                shang_stage,
            )
        p.dispose(
            n,
            "PARTIALLY_STRUCTURED" if n == 260 else "STRUCTURED",
            "Named source-batch inputs supported; original per-litre prose is interpreted only as per litre of input water, not a final concentration.",
        )
    for label, snippet, stage in (
        (
            "oat spelt xylan",
            "10 g/l of oat spelt xylan as substrate",
            "Shang2013 xylanase production culture",
        ),
        ("xylose", "10.0 g substrate", "Shang2013 xylose substrate alternative"),
        ("glucose", "10.0 g substrate", "Shang2013 glucose substrate alternative"),
    ):
        p.change(
            263,
            "ADD",
            label,
            stage,
            [
                evidence(
                    "shang",
                    snippet,
                    "Methods define10g substrate per litre water preparation and separate substrate experiments; xylose isolation and glucose protein-analysis arms are distinct. No simultaneous three-substrate medium is asserted.",
                )
            ],
            amount=amount("10.0", "G", batch_basis),
        )
    p.mention(
        263,
        "glucose",
        "Separate glucose, xylose and xylan source arms are supported; an operation removing a fixed parent glucose across every assay is not established by the source.",
        ["OPERATION"],
        "REPLACE",
        "Shang2013 separate substrate arms",
    )
    p.dispose(
        263,
        "PARTIALLY_STRUCTURED",
        "Named substrate arms retained separately; parent-removal inference withheld.",
    )
    for label in ("Formate", "fumarate"):
        p.change(
            273,
            "REMOVE",
            label.lower(),
            "O'Hanlon2011 plain ATCC1490 strains; separate from B.ureolyticus supplemented medium",
            [
                evidence(
                    "ohanlon",
                    "ATCC medium 1490 with formate and fumarate",
                    "Methods explicitly contrast the listed plain-ATCC1490 strains with B.ureolyticus in ATCC1490 with formate/fumarate. This formulation distinction supports omission relative to the supplemented parent, not unreported salts or zero-dose conversion.",
                )
            ],
        )
    p.dispose(
        273,
        "STRUCTURED",
        "Explicit within-source basal/supplemented contrast verified; omission is scoped to named plain-medium group.",
    )
    for label in ("Carbonate", "CO2"):
        p.mention(
            275,
            label,
            "Johnston2001 full Methods remain inaccessible anonymously. Existing text gives no exact carbonate species/dose or gas composition; do not infer bicarbonate or aqueous CO2 concentration.",
            ["SOURCE_CLAIM", "IDENTITY_FORM", "QUANTITY"],
            "ADD",
            "reported ATCC1490 carbonate/CO2-buffered formulation",
        )
    p.dispose(
        275,
        "HELD_EVIDENCE",
        "Both literal buffer labels retained; exact species/phase/quantity not invented.",
    )
    p.mention(
        287,
        "vitamin solution",
        "Named mixture replacement is already supported by Hiibel2015. Its constituent list and dose are not supplied by the inspected passage; do not invent additional vitamins or inherit unrelated stock composition.",
        ["IDENTITY_FORM", "QUANTITY"],
        "REPLACE",
        "Hiibel2015 Nannochloropsis maintenance medium",
    )
    p.dispose(
        287,
        "PARTIALLY_STRUCTURED",
        "Existing named mixture replacement preserved; unresolved composition/dose now machine-readable.",
    )
    for n in (373, 376, 378):
        p.mention(
            n,
            "phosphate",
            "Nordkvist2003 distinguishes reactor medium from threefold-phosphate preculture. Full1995MS10 base remained subscription-only after exact publisher inspection; specific reactor phosphate salt/dose cannot be inferred from the ratio or imported parent.",
            ["IDENTITY_FORM", "QUANTITY"],
            "SET_CONCENTRATION",
            "Nordkvist2003 reactor versus preculture",
            "preculture threefold relative to reactor",
        )
        p.dispose(
            n,
            "HELD_EVIDENCE",
            "Literal phosphate-family mention preserved; exact base-source species and quantities remain unresolved.",
        )
    p.mention(
        383,
        "L-phenylalanine",
        "Presence and sole-nitrogen-source role are already supported. Dose and any specific displaced nitrogen ingredient are not reported in the inspected primary abstract; label presence is not withdrawn.",
        ["QUANTITY"],
        "ADD",
        "reported phototrophic OU5 sole-nitrogen-source experiment",
    )
    p.dispose(
        383,
        "PARTIALLY_STRUCTURED",
        "Supported L-phenylalanine identity retained; unreported amount explicit, no named displaced salt invented.",
    )
    for n in (148, 155, 162, 169, 176, 183, 209, 216):
        for label in ("B1", "B3", "B5", "B6", "B9", "B12"):
            p.mention(
                n,
                label,
                "The source-literal vitamin designation and dose are already supported in ingredient_changes. A more specific vitamer or salt form is not supplied by the cited formulation; this form-only hold does not demote supported label presence or dosage.",
                ["IDENTITY_FORM"],
                stage="Carini source-specific AMS1 vitamin formulation",
            )
        p.dispose(
            n,
            "PARTIALLY_STRUCTURED",
            "Existing vitamin-label/dose events remain supported; unresolved chemical forms explicit in separate held mentions.",
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", required=True, type=Path)
    parser.add_argument("--coverage", required=True, type=Path)
    parser.add_argument("--prior-worktree", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    if args.output.exists():
        raise ValueError("Proposal output must be new")
    raw_queue = args.queue.read_bytes()
    if digest(raw_queue) != QUEUE_SHA:
        raise ValueError("Original queue pin mismatch")
    csv.field_size_limit(16 * 1024 * 1024)
    with args.queue.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    with args.coverage.open(newline="", encoding="utf-8") as stream:
        coverage = {
            int(row["queue_row_number"]): row for row in csv.DictReader(stream, delimiter="\t")
        }
    if len(rows) != 396 or len(coverage) != 396:
        raise ValueError("Expected complete original396-row accounting")
    proposal = Proposal(rows, coverage)
    prepare(proposal)
    expected = {n for n, row in coverage.items() if row["status"] == "HELD_EVIDENCE"}
    expected |= {75, 76, 77, 79, 80, 116, 287, 383, 148, 155, 162, 169, 176, 183, 209, 216}
    if set(proposal.dispositions) != expected:
        raise ValueError("Evidence/partial scope is not exact")
    inspections = []
    for prior, sources in ((False, SOURCES), (True, PRIOR_SOURCES)):
        for key, (reference, path, expected_hash, locator) in sources.items():
            source_path = (args.prior_worktree / OLD / path) if prior else (ROOT / NEW / path)
            actual_hash = digest(source_path.read_bytes())
            if actual_hash != expected_hash:
                raise ValueError("Inspected source drift: " + key)
            inspections.append(
                {
                    "key": key,
                    "reference": reference,
                    "path": (
                        str(source_path.relative_to(ROOT))
                        if source_path.is_relative_to(ROOT)
                        else str(Path("..") / args.prior_worktree.name / OLD / path)
                    ),
                    "sha256": actual_hash,
                    "locator": locator,
                }
            )
    payload = {
        "schema_version": 1,
        "base_commit": BASE,
        "source_queue_sha256": QUEUE_SHA,
        "scope": "Manual evidence completion:44 prior evidence holds plus16 partial rows; supported source-stage labels and quantities separated from exact forms, operations and negative-test context. No recipe applied by this helper.",
        "source_inspections": inspections,
        "browser_inspections": [
            {
                "reference": "doi:10.1128/aem.59.12.4363-4366.1993",
                "url": "https://journals.asm.org/doi/epdf/10.1128/aem.59.12.4363-4366.1993",
                "locator": "Table1, printed4363",
                "sha256": None,
            },
            {
                "reference": "doi:10.1099/ijs.0.012724-0",
                "url": "https://www.academia.edu/165327461/",
                "locator": "Primary paper page2730, assay plate omissions",
                "sha256": None,
            },
        ],
        "records": sorted(proposal.records.values(), key=lambda r: r["path"]),
        "dispositions": [proposal.dispositions[n] for n in sorted(proposal.dispositions)],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(
        json.dumps(
            {
                "path": str(args.output),
                "sha256": digest(args.output.read_bytes()),
                "records": len(payload["records"]),
                "rows": len(payload["dispositions"]),
                "statuses": dict(Counter(d["status"] for d in payload["dispositions"])),
                "append_changes": sum(d["append_assertion_count"] for d in payload["dispositions"]),
                "append_mentions": sum(d["append_mention_count"] for d in payload["dispositions"]),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
