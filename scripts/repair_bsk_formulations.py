#!/usr/bin/env python3
"""Restore three distinct BSK formulations with guarded, claim-level evidence."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import re
from decimal import Decimal
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_methanogen_stock_boundaries as shared
from bs4 import BeautifulSoup

from culturemech.curate.curation_event import record_curation_event

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-bsk-formulations"
CONTEXT_SHA = "afef4e855d33495a1e7f54c7e6b809fe345c26533ad19f00a626328bc60136c3"
ACTION = "RESTORED_SOURCE_SPECIFIC_BSK_FORMULATIONS_WITH_INGREDIENT_EVIDENCE"
KEYS = {"CultureMech:008994": "M2410", "CultureMech:001256": "D1829", "CultureMech:002533": "J173"}
LB = {"M2410": (4, 5, 6), "D1829": (8, 9, 10), "J173": (1, 2, 3)}


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    for item in context["records"]:
        item["key"] = KEYS[item["id"]]
    return context


def sources(context):
    parsed = {}
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        url = {
            "M2410": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2410",
            "D1829": "https://mediadive.dsmz.de/rest/medium/1829",
            "J173": "https://mediadive.dsmz.de/rest/medium/J173",
            "JCM173": "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=173",
            "DSMZ1829": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1829.pdf",
        }[key]
        runner.require(
            meta["url"] == meta["response_url"] == url
            and meta["http_status"] == 200
            and runner.sha(raw.encode(meta.get("encoding", "utf-8"))) == meta["sha256"],
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        parsed[key] = (
            " ".join(BeautifulSoup(raw, "html.parser").get_text().split())
            if key == "JCM173"
            else raw if key == "DSMZ1829" else json.loads(raw)
        )
    for key, accession, provider, ids, sizes in (
        ("D1829", 1829, "DSMZ", [6374], [12]),
        ("J173", "J173", "JCM", [3829, 3830, 3831], [0, 10, 3]),
    ):
        body = parsed[key]
        ss = body["data"]["solutions"]
        runner.require(
            body["status"] == 200
            and body["data"]["medium"]["id"] == accession
            and body["data"]["medium"]["source"] == provider
            and [s["id"] for s in ss] == ids
            and [len(s.get("recipe", [])) for s in ss] == sizes
            and all(not r.get("optional") for s in ss for r in s.get("recipe", [])),
            "Source topology drift",
        )
    m = parsed["M2410"]
    runner.require(
        m["meta"]["gm"] == "http://togomedium.org/medium/M2410"
        and m["meta"]["name"] == "BSK II Medium"
        and m["meta"]["src_url"] == ""
        and len(m["components"]) == 1
        and len(m["components"][0]["items"]) == 12
        and len(m["comments"]) == 11
        and not m["comments"][-1]["comment"],
        "TOGO source drift",
    )
    runner.require(
        "173 BARBOUR-SFOENNER-KELLY (BSK) II MEDIUM" in parsed["JCM173"]
        and parsed["J173"]["data"]["medium"]["link"]
        == context["sources"]["JCM173"]["metadata"]["url"]
        and parsed["DSMZ1829"].startswith("1829: BSKII medium (Borrelia)")
        and "Final volume: 100 ml" in parsed["DSMZ1829"],
        "Original recipe identity drift",
    )
    return parsed


class Review(shared.Review):
    append = stocks.Review.append

    def __init__(self, before, key):
        # This cohort has duplicate labels: only guarded original indices identify nodes.
        self.context = frozen()
        self.spec = next(r for r in self.context["records"] if r["key"] == key)
        runner.require(
            before == runner.load_yaml(self.spec["before_text"])
            and before["id"] == self.spec["id"],
            "Unreviewed baseline",
        )
        runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
        runner.require(
            not any(before.get(k) for k in ("solutions", "evidence", "references", "variants")),
            "Existing provenance needs reconciliation",
        )
        self.data = sources(self.context)
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.claims, self.lineage, self.used = [], [], []
        for i, label in zip(LB[key], ("Tryptone", "Yeast extract", "Sodium chloride"), strict=True):
            node = before["ingredients"][i]
            runner.require(
                node["preferred_term"] == label
                and "LB Medium" in node["supplier_catalog"]["supplier_name"],
                "False-LB baseline drift",
            )
        self.after["ingredients"], self.after["solutions"] = [], []

    def row(self, si, ri):
        return self.data[self.key]["data"]["solutions"][si]["recipe"][ri]

    def sp(self, si, ri):
        return ["data", "solutions", si, "recipe", ri]

    def clone(self, label, old_index):
        old = ["ingredients", old_index] if old_index is not None else None
        node = (
            copy.deepcopy(runner.get_node(self.before, old)) if old else {"preferred_term": label}
        )
        runner.require(node["preferred_term"] == label, "Ingredient identity drift")
        return node, old

    def pdf_line(self, start):
        lines = [
            s.strip() for s in self.data["DSMZ1829"].splitlines() if s.strip().startswith(start)
        ]
        runner.require(len(lines) == 1, "Ambiguous PDF row")
        return lines[0]

    def original_row(self, pointer, si, ri, evidence_pointer):
        row = self.row(si, ri)
        if self.key == "D1829":
            starts = (
                "HEPES ",
                "Trisodium citrate x 2 H2O",
                "Glucose ",
                "Pyruvate ",
                "N-Acetylglucosamine ",
                "Sodium bicarbonate ",
                "Yeast extract ",
                "Bacto peptone (",
                "Bovine serum albumin (",
                "Rabbit serum ",
                "MEM alpha Modification (",
                "Deionized water ",
            )
            snippet, source = self.pdf_line(starts[ri]), "DSMZ1829"
        else:
            soup = BeautifulSoup(self.context["sources"]["JCM173"]["raw"], "html.parser")
            tr = soup.find_all("table")[si - 1].find_all("tr")[ri]
            snippet, source = " ".join(tr.get_text().split()), "JCM173"
        if "amount" in row:
            match = re.search(r"([0-9]+(?:\.[0-9]+)?)\s+(g|mg|ml)$", snippet)
            runner.require(
                match
                and Decimal(match[1]) == Decimal(str(row["amount"]))
                and match[2] == row["unit"],
                "Original/provider amount conflict",
            )
        self.claim(
            pointer,
            None,
            source,
            None,
            "evidence_only",
            "original_support",
            "Original recipe row corroborates the source-specific ingredient, batch amount and unit; preparation scope is retained.",
            evidence_pointer,
            snippet,
        )

    def remember(self, pointer, old, source_pointer, kind):
        self.lineage.append(
            {
                "pointer": pointer,
                "old_pointer": old,
                "source": self.key,
                "source_pointer": source_pointer,
                "kind": kind,
            }
        )

    def dsmz(self):
        for ri in range(12):
            row = self.row(0, ri)
            old_i = ri if ri < 8 else {8: None, 9: 11, 10: 12, 11: None}[ri]
            node, old = self.clone(row["compound"], old_i)
            if ri == 11:
                kind = "makeup"
                node.pop("concentration", None)
                self.note(
                    node,
                    "Deionized water: make up the complete medium to a final volume of 100 ml; this is not a fixed 100 ml water addition.",
                )
                reason = "The original specifies water fill up to 100 ml, not a fixed carrier input. No numeric water dose is asserted."
            else:
                kind = "final_volume_rate"
                value = shared.numeric(Decimal(str(row["amount"])) / Decimal("0.1"))
                unit = "ML_PER_L" if row["unit"] == "ml" else "G_PER_L"
                node["concentration"] = {"value": value, "unit": unit}
                reason = f"Original final volume is 100 ml = 0.1 L: {row['amount']} {row['unit']} / 0.1 L = {value} {unit}. This is the receiving-medium rate, not a mass interpretation of a liquid input."
                if row.get("attribute"):
                    self.note(
                        node, "Original source component specification: " + row["attribute"] + "."
                    )
            p = self.append(["ingredients"], node)
            self.remember(p, old, self.sp(0, ri), kind)
            field = "notes" if kind == "makeup" else "concentration"
            self.claim(
                p + [field],
                old + ["concentration"] if old else None,
                self.key,
                self.sp(0, ri),
                "correct" if old else "add",
                kind,
                reason,
                p,
            )
            self.original_row(p + [field], 0, ri, p)
            if kind != "makeup":
                self.claim(
                    p + ["concentration"],
                    None,
                    "DSMZ1829",
                    None,
                    "evidence_only",
                    "volume_basis",
                    reason,
                    p,
                    "Final volume: 100 ml",
                )
            if row.get("attribute"):
                self.claim(
                    p + ["notes"],
                    old + ["notes"] if old else None,
                    self.key,
                    self.sp(0, ri),
                    "add",
                    "source_context",
                    "Preserve the exact product/fraction qualifier.",
                    p,
                )
        procedure = self.row_procedure()
        stock = {
            "preferred_term": "NaOH solution (1 M)",
            "composition": [
                {"preferred_term": "NaOH", "concentration": {"value": "1", "unit": "MOLAR"}}
            ],
            "notes": "Titrate to final pH 7.3. The 1 M value is titrant stock strength; no fixed dose or final-medium NaOH concentration is specified.",
        }
        p = self.append(["solutions"], stock)
        for suffix, ep in (
            (["notes"], []),
            (["composition", 0, "concentration"], p + ["composition", 0]),
        ):
            self.claim(
                p + suffix, None, "DSMZ1829", None, "add", "titrant", stock["notes"], ep, procedure
            )
        self.after["preparation_steps"] = [
            {
                "step_number": 1,
                "action": "MIX",
                "description": "Combine the recipe ingredients. The source specifies a final medium volume of 100 ml, using deionized water as makeup; no separate makeup-versus-titration order is asserted.",
            },
            {
                "step_number": 2,
                "action": "ADJUST_PH",
                "description": "Adjust to pH 7.3 with 1 M NaOH.",
            },
            {
                "step_number": 3,
                "action": "FILTER",
                "description": "Filter-sterilize; the source specifies no filter pore size.",
            },
        ]
        self.claim(
            ["ph_value"],
            ["ph_value"],
            "DSMZ1829",
            None,
            "evidence_only",
            "final_ph",
            "Retain the explicitly stated final pH.",
            [],
            "Final pH: 7.3",
        )
        self.claim(
            ["preparation_steps"],
            ["preparation_steps"],
            "DSMZ1829",
            None,
            "correct",
            "preparation",
            "Separate mixing, pH adjustment and filtration. FILTER_STERILIZE would imply an unsupported 0.22 micrometer pore size.",
            [],
            procedure,
        )
        self.claim(
            ["preparation_steps"],
            None,
            "DSMZ1829",
            None,
            "evidence_only",
            "makeup",
            "Water is makeup, not a fixed addition.",
            [],
            self.pdf_line("Deionized water "),
        )

    def row_procedure(self):
        return self.pdf_line("Combine all ingredients")

    def jcm(self):
        old_indices = {1: [0, None, 4, 5, 6, 7, 8, 9, 10, None], 2: [11, 12, None]}
        original = self.data["JCM173"]
        start = original.index("Adjust pH to 7.6")
        procedure = original[start : original.index("Copyright", start)].strip()
        self.after.pop("ph_value")
        for si in (1, 2):
            stock = {
                "preferred_term": f"Solution {'A' if si == 1 else 'B'}",
                "composition": [],
                "notes": "Separate source preparation. Water input does not independently establish measured final stock volume or a fixed parent addition dose. MediaDive g_l values below are provider-reported stock rates, not final-medium concentrations.",
            }
            p = self.append(["solutions"], stock)
            self.claim(
                p + ["notes"],
                None,
                self.key,
                ["data", "solutions", si],
                "add",
                "preparation_boundary",
                stock["notes"],
                [],
            )
            for ri, old_i in enumerate(old_indices[si]):
                row = self.row(si, ri)
                node, old = self.clone(row["compound"], old_i)
                if row["unit"] == "ml":
                    kind = "water"
                    node["concentration"] = {
                        "value": shared.numeric(Decimal(str(row["amount"])) / 1000),
                        "unit": "L",
                    }
                    reason = f"Source water input {row['amount']} ml / 1000, in this preparation only. Not a measured final volume or a parent dose."
                else:
                    kind = "stock_rate"
                    node["concentration"] = {"value": shared.numeric(row["g_l"]), "unit": "G_PER_L"}
                    reason = f"MediaDive explicitly reports g_l={row['g_l']} inside this stock preparation; source batch input is {row['amount']} {row['unit']}. Retain only at stock scope, not as an independently measured final volume or receiving-medium rate."
                extra = "; ".join(row[k].strip() for k in ("condition", "attribute") if row.get(k))
                self.note(node, reason + (" Source specification: " + extra + "." if extra else ""))
                leaf = self.append(p + ["composition"], node)
                self.remember(leaf, old, self.sp(si, ri), kind)
                for field in ("concentration", "notes"):
                    self.claim(
                        leaf + [field],
                        old + [field] if old else None,
                        self.key,
                        self.sp(si, ri),
                        "correct" if old else "add",
                        kind,
                        reason,
                        leaf,
                    )
                self.original_row(leaf + ["concentration"], si, ri, leaf)
        titrant = {
            "preferred_term": "NaOH solution (1 N)",
            "composition": [
                {
                    "preferred_term": "NaOH",
                    "notes": "Source titrant strength: 1 N. Normality is not silently converted to molarity; fixed addition dose and final-medium concentration are unspecified.",
                }
            ],
        }
        p = self.append(["solutions"], titrant)
        self.claim(
            p + ["composition", 0, "notes"],
            None,
            "JCM173",
            None,
            "add",
            "normality",
            "Preserve titrant normality without inventing a MOLAR value or dose.",
            p + ["composition", 0],
            procedure,
        )
        serum = {
            "preferred_term": "Heat-inactivated sterile rabbit serum",
            "concentration": {"value": "0.04", "unit": "L"},
            "notes": "Pel-Freez Biologicals; heat-inactivated at 56 C for 45 min. Add 40 ml after combining Solutions A and B. This is a batch dose, not 40 ml/L.",
        }
        p = self.append(["solutions"], serum)
        for field in ("concentration", "notes"):
            self.claim(
                p + [field],
                None,
                "JCM173",
                None,
                "add",
                "serum_dose",
                "40 ml / 1000 = 0.04 L per prepared batch; retain heat treatment and timing.",
                [],
                procedure,
            )
        self.after["preparation_steps"] = [
            {
                "step_number": 1,
                "action": "ADJUST_PH",
                "description": "Adjust pH to 7.6 with 1 N NaOH at the source's pre-combination stage; a final combined-medium pH measurement is not stated.",
            },
            {
                "step_number": 2,
                "action": "FILTER_STERILIZE",
                "description": "Sterilize by filtration through a 0.22 micrometer filter (Millipore), before the source's subsequent combination instruction.",
            },
            {
                "step_number": 3,
                "action": "AUTOCLAVE",
                "description": "Autoclave Solution B separately. The JCM page's general default is 121 C for 15 min unless otherwise stated.",
            },
            {
                "step_number": 4,
                "action": "MIX",
                "description": "Mix Solutions A and B, then add 40 ml heat-inactivated (56 C, 45 min) sterile rabbit serum (Pel-Freez Biologicals).",
            },
        ]
        self.claim(
            ["ph_value"],
            ["ph_value"],
            "JCM173",
            None,
            "remove_unsupported",
            "ph_scope",
            "Keep the pH adjustment in source order, before combination/serum. Do not assert a measured final combined-medium pH.",
            [],
            procedure,
        )
        self.claim(
            ["preparation_steps"],
            ["preparation_steps"],
            "JCM173",
            None,
            "correct",
            "preparation",
            "Restore separate actions and original 0.22 micrometer typography. The API's placement of all instructions under B does not make the complete medium autoclaved.",
            [],
            procedure,
        )
        self.claim(
            ["preparation_steps"],
            None,
            "JCM173",
            None,
            "evidence_only",
            "autoclave_default",
            "Apply the explicitly qualified page-level default only to the separate Solution B autoclave step.",
            [],
            "Unless otherwise stated, sterilize media by autoclaving at 121\u00b0C for 15 min.",
        )

    def togo(self):
        rows = self.data[self.key]["components"][0]["items"]
        old_indices = [0, 1, 2, 3, None, 7, 8, 9, 10, 11, 12, 13]
        for ri in (0, 1, 2, 3, 4, 5, 6, 7, 8, 10):
            row, sp = rows[ri], ["components", 0, "items", ri]
            node, old = self.clone(row["component_name"], old_indices[ri])
            if row["unit"] == "ml":
                kind = "water"
                node["concentration"] = {"value": "0.9", "unit": "L"}
                reason = (
                    "Source input is 900 ml water = 0.9 L, not 900 g/L or a measured final volume."
                )
            else:
                kind = "batch_mass"
                node.pop("concentration", None)
                reason = f"Source batch input: {row['volume']} g. No final-medium volume is specified after gelatin and serum; do not reinterpret batch mass as g/L."
            self.note(node, reason)
            p = self.append(["ingredients"], node)
            self.remember(p, old, sp, kind)
            for field in ("concentration", "notes"):
                self.claim(
                    p + [field],
                    old + [field] if old else None,
                    self.key,
                    sp,
                    "correct" if old else "add",
                    kind,
                    reason,
                    p,
                )
        row = rows[9]
        cmrl, old = self.clone(row["component_name"], 11)
        cmrl["concentration"] = {"value": "0.1", "unit": "L"}
        self.note(
            cmrl,
            "Source dose: 100 ml = 0.1 L of the specified 10X CMRL 1066 without glutamine. No product composition or final-medium g/L is inferred.",
        )
        p = self.append(["solutions"], cmrl)
        self.remember(p, old, ["components", 0, "items", 9], "batch_dose")
        for field in ("concentration", "notes"):
            self.claim(
                p + [field],
                old + [field],
                self.key,
                ["components", 0, "items", 9],
                "correct",
                "batch_dose",
                cmrl["notes"],
                [],
            )
        node, old = self.clone("NaOH", 13)
        node.pop("concentration")
        self.note(
            node,
            "Source stock strength is 1 N, not an asserted molarity or final-medium concentration. Titrate to pH 7.6 at 20-25 C before gelatin/serum additions; no fixed dose is given.",
        )
        p = self.append(
            ["solutions"], {"preferred_term": "NaOH solution (1 N)", "composition": [node]}
        )
        leaf = p + ["composition", 0]
        self.remember(leaf, old, ["components", 0, "items", 11], "normality")
        for field in ("concentration", "notes"):
            self.claim(
                leaf + [field],
                old + [field],
                self.key,
                ["components", 0, "items", 11],
                "correct",
                "normality",
                node["notes"],
                leaf,
            )
            self.claim(
                leaf + [field],
                None,
                self.key,
                ["comments", 3],
                "evidence_only",
                "titrant_timing",
                "Preserve the temperature-specific adjustment before subsequent additions.",
                leaf,
            )
        gelatin = {
            "preferred_term": "Gelatin solution (7 percent; basis unspecified)",
            "concentration": {"value": "0.2", "unit": "L"},
            "composition": [
                {
                    "preferred_term": "Gelatin",
                    "notes": "Difco gelatin stock: 7 percent, with no stated w/v, w/w or v/v basis. No numeric stock mass concentration is asserted.",
                }
            ],
            "preparation_notes": "Dissolve gelatin in boiling water as the source describes, then add 200 ml of this stock after pH adjustment. No gelatin mass or final-medium percentage is calculated.",
        }
        p = self.append(["solutions"], gelatin)
        for field in ("concentration", "preparation_notes"):
            self.claim(
                p + [field],
                None,
                self.key,
                ["comments", 4],
                "add",
                "gelatin",
                "200 ml / 1000 = 0.2 L is a stock batch dose; the 7 percent strength has an unstated basis.",
                [],
            )
        self.claim(
            p + ["composition", 0, "notes"],
            None,
            self.key,
            ["comments", 4],
            "add",
            "unknown_percent_basis",
            "Preserve the reported percentage as qualified text only.",
            p + ["composition", 0],
        )
        p = self.append(
            ["solutions"],
            {
                "preferred_term": "Unheated rabbit serum",
                "notes": "Before use, add unheated rabbit serum (trace hemolyzed; Pel-Freez Biologicals) to a final 6 percent. Percentage basis and fixed batch dose are not stated; neither is guessed.",
            },
        )
        self.claim(
            p + ["notes"],
            None,
            self.key,
            ["comments", 6],
            "add",
            "serum",
            "Preserve unheated serum and the stated final percentage without selecting a basis or inventing a dose.",
            [],
        )
        comments = self.data[self.key]["comments"]
        self.after["preparation_steps"] = []
        actions = {
            0: "AUTOCLAVE",
            1: "MIX",
            2: "DISSOLVE",
            3: "ADJUST_PH",
            4: "MIX",
            5: "FILTER",
            6: "MIX",
            7: "ALIQUOT",
        }
        for ci, action in actions.items():
            description = comments[ci]["comment"]
            if ci == 2:
                description = "Add the source-listed ingredients to the diluted CMRL 1066. The provider requests an addition order, but its item array is not accepted as that order; exact addition order remains unresolved here."
            p = self.append(
                ["preparation_steps"],
                {"step_number": ci + 1, "action": action, "description": description},
            )
            self.claim(
                p + ["description"],
                None,
                self.key,
                ["comments", ci],
                "add",
                "preparation",
                "Retain source sequence, temperature and treatment. Use FILTER rather than the 0.22 micrometer-specific enum for the stated 0.2 micrometer membrane. Do not infer dry-ingredient addition order from API array order.",
                [],
            )
        for ci in (8, 9):
            self.note(self.after, comments[ci]["comment"])
            self.claim(
                ["notes"],
                ["notes"],
                self.key,
                ["comments", ci],
                "add",
                "context",
                "Preserve source incubation and altitude-dependent container-fill context as text, not a guessed preparation action.",
                [],
            )

    def formulate(self):
        provenance, separator, rejected = self.before["notes"].partition(
            "Commercial Product: LB Medium"
        )
        runner.require(separator, "Missing historical LB provenance")
        self.after["notes"] = (
            provenance.rstrip()
            + "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product: LB Medium"
            + rejected
        )
        self.note(
            self.after,
            "The false LB constituent expansion is withdrawn in favor of this source's bovine serum albumin input. Existing unrelated chemical annotations are preserved, not recertified. This repair does not assert equivalence with other BSK formulations or add organism-growth evidence.",
        )
        {"D1829": self.dsmz, "J173": self.jcm, "M2410": self.togo}[self.key]()
        sp = {
            "D1829": self.sp(0, 8),
            "J173": self.sp(1, 1),
            "M2410": ["components", 0, "items", 4],
        }[self.key]
        for i in LB[self.key]:
            self.claim(
                ["notes"],
                ["ingredients", i, "concentration"],
                self.key,
                sp,
                "remove_unsupported",
                "false_lb_removed",
                "Remove the unsupported LB ingredient and its dose; the exact source specifies bovine serum albumin instead.",
                [],
            )

    def finish(self, timestamp):
        for claim in self.claims:
            claim["new"] = copy.deepcopy(
                runner.get_node(self.after, claim["pointer"][:-1]).get(claim["pointer"][-1])
            )
        self.after["references"] = []
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            title = (
                "Medium data"
                if key == "JCM173"
                else (
                    self.data[key].splitlines()[0]
                    if key == "DSMZ1829"
                    else (
                        self.data[key]["meta"]["name"]
                        if key == "M2410"
                        else self.data[key]["data"]["medium"]["name"]
                    )
                )
            )
            self.after["references"].append(
                {
                    "reference": meta["url"],
                    "title": title,
                    "notes": f"source_type={'culture_collection_page' if key in {'DSMZ1829', 'JCM173'} else 'dataset'}; discovery_mode={'cross_reference' if key == 'DSMZ1829' else 'existing_record_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year are not supplied; copyright year is not publication year. Source-specific formulation evidence, not growth evidence.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restore source-specific albumin, quantity scopes, missing inputs and preparation boundaries. Preserve ID, prior history and unrelated groundings. Unknown doses, percentage bases and final volumes stay unknown; distinct formulations are not blended.",
            changes=json.dumps(
                [
                    {
                        k: c[k]
                        for k in (
                            "old_field",
                            "field",
                            "old",
                            "new",
                            "status",
                            "reference",
                            "snippet",
                        )
                    }
                    for c in self.claims
                ],
                ensure_ascii=True,
            ),
        )
        runner.require(not runner.errors(self.after, "MediaRecipe"), "Proposed schema failure")
        return self.after, self.claims, self.lineage


def build(before, key, timestamp):
    review = Review(before, key)
    review.formulate()
    return review.finish(timestamp)


def process(root, plan_path, mode):
    return shared.process(
        root,
        plan_path,
        mode,
        context=frozen(),
        context_sha=CONTEXT_SHA,
        builder=build,
        action=ACTION,
    )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    args = parser.parse_args()
    _, result = process(
        ROOT, args.plan, "apply" if args.apply else "verify" if args.verify else "preview"
    )
    print(json.dumps(result))


if __name__ == "__main__":
    main()
