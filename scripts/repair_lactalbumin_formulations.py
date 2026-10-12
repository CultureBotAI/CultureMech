#!/usr/bin/env python3
"""Restore four source-specific hydrolysate formulations and quantity scopes."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from decimal import Decimal
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_methanogen_stock_boundaries as shared
from bs4 import BeautifulSoup
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import html_recipe_text

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-lactalbumin-formulations"
CONTEXT_SHA = "b9afaadd95d0d21b285ebbde79b8a685f6fc18f6ecfb51b9cd2e86b2dcf8d8f2"
ACTION = "RESTORED_SOURCE_SPECIFIC_HYDROLYSATE_FORMULATIONS_WITH_EVIDENCE"
KEYS = {
    "CultureMech:000443": "D1021",
    "CultureMech:003534": "K1021",
    "CultureMech:003533": "K1021_16929",
    "CultureMech:008873": "M2287",
}
URLS = {
    "D1021": "https://mediadive.dsmz.de/rest/medium/1021",
    "DSMZ1021": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1021.pdf",
    "M2287": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2287",
    "K1021": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1021",
    "K1021_16929": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1021_16929",
}
LB = {key: (10, 11, 12) if key == "M2287" else (1, 2, 3) for key in KEYS.values()}


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    for record in context["records"]:
        record["key"] = KEYS[record["id"]]
    return context


def sources(context):
    parsed, texts = {}, {}
    for key, capture in context["sources"].items():
        meta, raw = capture["metadata"], capture["raw"]
        runner.require(
            meta["url"] == meta["response_url"] == URLS[key]
            and meta["http_status"] == 200
            and runner.sha(raw.encode(meta.get("encoding", "utf-8"))) == meta["sha256"],
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        texts[key] = html_recipe_text(raw)[0] if key.startswith("K") else raw
        if key.startswith("K"):
            tables = BeautifulSoup(raw, "html.parser").find_all("table")
            rows = [
                [" ".join(c.get_text().split()) for c in tr.find_all("td")]
                for tr in tables[2].find_all("tr")
            ]
            runner.require(
                rows[0] == ["Name", "Semi unique name", "Unique Name", "Gram Amount", "Mol Amount"],
                "KOMODO table drift",
            )
            runner.require(all(len(row) == 5 for row in rows[1:]), "KOMODO row shape")
            parsed[key] = {r[0]: r for r in rows[1:]}
            runner.require(len(parsed[key]) == len(rows) - 1, "Duplicate source ingredients")
            accession = key[1:]
            runner.require(f"ID: {accession} Name:" in texts[key], "KOMODO accession drift")
            runner.require(
                "Gram & Mol amounts are per Liter of medium." in texts[key],
                "KOMODO quantity basis drift",
            )
        elif key != "DSMZ1021":
            parsed[key] = json.loads(raw)
    d = parsed["D1021"]
    ss = d["data"]["solutions"]
    runner.require(
        d["status"] == 200
        and d["data"]["medium"]["id"] == 1021
        and d["data"]["medium"]["source"] == "DSMZ",
        "DSMZ identity drift",
    )
    runner.require(
        [s["id"] for s in ss] == [2073, 2074, 2075]
        and [len(s["recipe"]) for s in ss] == [2, 10, 2],
        "DSMZ topology drift",
    )
    runner.require(all(r["optional"] == 0 for s in ss for r in s["recipe"]), "Conditional API row")
    runner.require(
        texts["DSMZ1021"].startswith("1021. SODALIS GLOSSINIDIUS MEDIUM")
        and "Lactalbumin hydrolysate or" in texts["DSMZ1021"],
        "PDF identity/alternative drift",
    )
    m = parsed["M2287"]
    runner.require(
        m["meta"]["gm"] == "http://togomedium.org/medium/M2287"
        and len(m["components"]) == 1
        and len(m["components"][0]["items"]) == 11
        and len(m["comments"]) == 2,
        "TOGO identity/topology drift",
    )
    runner.require(
        len(parsed["K1021"]) == 12 and len(parsed["K1021_16929"]) == 15, "KOMODO formulation drift"
    )
    return parsed, texts


class Review(shared.Review):
    append = stocks.Review.append

    def __init__(self, before, key):
        self.context = frozen()
        self.spec = next(r for r in self.context["records"] if r["key"] == key)
        runner.require(
            before == runner.load_yaml(self.spec["before_text"])
            and before["id"] == self.spec["id"],
            "Unreviewed baseline",
        )
        runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
        runner.require(
            not any(before.get(k) for k in ("solutions", "references", "evidence", "variants")),
            "Existing provenance needs reconciliation",
        )
        self.data, self.texts = sources(self.context)
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.claims, self.lineage, self.used = [], [], []
        for i, label in zip(LB[key], ("Tryptone", "Yeast extract", "Sodium chloride"), strict=True):
            old = before["ingredients"][i]
            runner.require(
                old["preferred_term"] == label
                and "LB Medium" in old["supplier_catalog"]["supplier_name"],
                "False-LB baseline drift",
            )
        self.after["ingredients"], self.after["solutions"] = [], []
        if key != "M2287":
            self.after["variants"] = []

    def claim(
        self,
        pointer,
        old_pointer,
        source,
        source_pointer,
        status,
        kind,
        reason,
        evidence_pointer=None,
        snippet=None,
    ):
        capture = self.context["sources"][source]
        meta = capture["metadata"]
        snippet = snippet if snippet is not None else json_excerpt(capture["raw"], source_pointer)
        runner.require(snippet and snippet in self.texts[source], "Nonliteral source excerpt")
        parent = runner.get_node(self.after, pointer[:-1])
        old = (
            runner.get_node(self.before, old_pointer[:-1]).get(old_pointer[-1])
            if old_pointer
            else None
        )
        explanation = f"{runner.field_name(pointer)}: {reason} No unstated density, final volume, percent basis or chemical identifier is inferred. Locator={runner.field_name(source_pointer) if source_pointer else 'original recipe table/text'}; accessed={meta['accessed_at']}; capture SHA256={meta['sha256']}."
        claim = {
            "pointer": pointer,
            "old_pointer": old_pointer,
            "field": runner.field_name(pointer),
            "old_field": runner.field_name(old_pointer) if old_pointer else None,
            "ingredient": parent.get("preferred_term", "Recipe preparation/context"),
            "old": copy.deepcopy(old),
            "new": copy.deepcopy(parent.get(pointer[-1])),
            "status": status,
            "kind": kind,
            "source": source,
            "source_pointer": source_pointer,
            "reference": meta["url"],
            "snippet": snippet,
            "explanation": explanation,
            "evidence_pointer": evidence_pointer,
        }
        self.claims.append(claim)
        if evidence_pointer is not None:
            if source not in self.used:
                self.used.append(source)
            entries = runner.get_node(self.after, evidence_pointer).setdefault("evidence", [])
            matches = [e for e in entries if e["reference"] == meta["url"]]
            runner.require(len(matches) <= 1, "Evidence collision")
            if matches:
                matches[0]["explanation"] += (
                    "\n\nAdditional exact excerpt: " + snippet + "\n" + explanation
                )
            else:
                entries.append(
                    {
                        "reference": meta["url"],
                        "supports": "SUPPORT",
                        "snippet": snippet,
                        "explanation": explanation,
                    }
                )

    def component(self, parent, label, old_index, source, sp, kind, quantity, reason, snippet=None):
        old = ["ingredients", old_index] if old_index is not None else None
        node = (
            copy.deepcopy(runner.get_node(self.before, old)) if old else {"preferred_term": label}
        )
        runner.require(node["preferred_term"] == label, "Ingredient identity drift")
        if quantity is None:
            node.pop("concentration", None)
        else:
            node["concentration"] = quantity
        self.note(node, reason)
        p = self.append(parent, node)
        self.lineage.append(
            {"pointer": p, "old_pointer": old, "source": source, "source_pointer": sp, "kind": kind}
        )
        self.claim(
            p + ["concentration"],
            old + ["concentration"] if old else None,
            source,
            sp,
            "correct" if old else "add" if quantity else "not_quantified",
            kind,
            reason,
            p,
            snippet,
        )
        self.claim(
            p + ["notes"],
            old + ["notes"] if old else None,
            source,
            sp,
            "evidence_only",
            kind + "_context",
            reason,
            p,
            snippet,
        )
        return p

    def pdf_snippet(self, start):
        rows = [
            s.strip() for s in self.texts["DSMZ1021"].splitlines() if s.strip().startswith(start)
        ]
        runner.require(len(rows) == 1, "Ambiguous PDF excerpt")
        return rows[0]

    def pdf_claim(self, pointer, reason, snippet, old=None, evidence=None):
        self.claim(
            pointer,
            old,
            "DSMZ1021",
            None,
            "evidence_only",
            "original_support",
            reason,
            [] if evidence is None else evidence,
            snippet,
        )

    def preparation(self):
        text = self.texts["DSMZ1021"]
        block = text[
            text.index("Sterilize solution A and B separately") : text.index("autoclaved.")
            + len("autoclaved.")
        ]
        self.after["preparation_steps"] = []
        for action, description in (
            (
                "ADJUST_PH",
                "Prepare Solution A according to the linked DSMZ 1021 protocol and adjust Solution A to pH 8.0. This is not a measured final-medium pH.",
            ),
            (
                "AUTOCLAVE",
                "For the solid preparation, sterilize Solution A and Solution B separately at 121 C for 20 min. Do not autoclave the serum-supplemented mixture.",
            ),
            ("COOL", "Cool the separately sterilized solutions to 50 C, then combine A and B."),
            (
                "MIX",
                "To 4 parts of the combined basal preparation, add 1 part sterile foetal or newborn calf serum. Preserve the reported ratio; no fixed serum batch dose or mass concentration is asserted.",
            ),
        ):
            p = self.append(
                ["preparation_steps"],
                {
                    "step_number": len(self.after["preparation_steps"]) + 1,
                    "action": action,
                    "description": description,
                },
            )
            self.pdf_claim(
                p + ["description"],
                "Linked original protocol retains separate sterilization, cooling and later serum supplementation.",
                self.pdf_snippet("Adjust pH") if action == "ADJUST_PH" else block,
            )
        p = self.append(
            ["variants"],
            {
                "name": "Liquid preparation described by DSMZ 1021",
                "relationship": "PHYSICAL_STATE_VARIANT",
                "description": "The source describes an alternative liquid preparation but does not provide a separate complete ingredient table.",
                "modifications": [
                    "Filter sterilize the liquid preparation instead of autoclaving. No membrane pore size is specified.",
                    "The source does not explicitly quantify the agar change for this alternative; no numeric agar amount is invented.",
                ],
            },
        )
        self.pdf_claim(
            p + ["modifications"],
            "Preserve the source's conditional liquid preparation, not an invented fully quantified broth recipe.",
            block,
            evidence=p,
        )
        return block

    def dsmz(self):
        ss = self.data["D1021"]["data"]["solutions"]
        base = self.append(
            ["solutions"],
            {
                "preferred_term": "Combined basal preparation (Solutions A and B)",
                "solutions": [],
                "notes": "Combine the separately prepared A and B before serum supplementation. The source then specifies 4 parts base to 1 part serum; no fixed receiving-medium dose or final total volume is asserted.",
            },
        )
        self.claim(
            base + ["notes"],
            None,
            "D1021",
            ["data", "solutions", 0, "steps", 0],
            "add",
            "base_scope",
            "Keep the pre-serum preparation separate from the receiving medium.",
            [],
        )
        indices = {1: [0, None, 4, 5, 6, 7, 8, 9, 10, None], 2: [11, None]}
        for si in (1, 2):
            descriptor = {
                "preferred_term": ss[si]["name"],
                "concentration": {
                    "value": shared.numeric(Decimal(str(ss[0]["recipe"][si - 1]["amount"])) / 1000),
                    "unit": "L",
                },
                "composition": [],
                "notes": "Provider-reported addition to the combined basal preparation before serum; not a final-medium concentration.",
            }
            sp = ["data", "solutions", 0, "recipe", si - 1]
            p = self.append(base + ["solutions"], descriptor)
            for field in ("concentration", "notes"):
                self.claim(
                    p + [field],
                    None,
                    "D1021",
                    sp,
                    "add",
                    "stock_dose",
                    "Use the source-explicit A/B batch doses at pre-serum basal scope only; ml / 1000 gives L.",
                    [],
                )
            for ri, row in enumerate(ss[si]["recipe"]):
                water = row["compound"] == "Distilled water"
                quantity = {
                    "value": shared.numeric(
                        Decimal(str(row["amount"])) / 1000 if water else row["g_l"]
                    ),
                    "unit": "L" if water else "G_PER_L",
                }
                reason = f"Source batch input: {row['amount']} {row['unit']} in {ss[si]['name']}. " + (
                    "Water is a stock batch input, not a final-volume marker."
                    if water
                    else "The attached g/L value is the API-reported stock rate, not a final-medium concentration; original water input alone does not establish a measured final stock volume."
                )
                cp = self.component(
                    p + ["composition"],
                    row["compound"],
                    indices[si][ri],
                    "D1021",
                    ["data", "solutions", si, "recipe", ri],
                    "water" if water else "stock_rate",
                    quantity,
                    reason,
                )
                if row["compound"] != "Distilled water":
                    snippet = self.pdf_snippet(
                        "Casein hydrolysate" if ri == 1 and si == 1 else row["compound"] + " "
                    )
                    if ri == 1 and si == 1:
                        start = self.texts["DSMZ1021"].index("Lactalbumin hydrolysate or")
                        end = self.texts["DSMZ1021"].index("D-Glucose", start)
                        snippet = self.texts["DSMZ1021"][start:end].rstrip()
                    self.pdf_claim(
                        cp + ["notes"],
                        "The original recipe corroborates this stock batch mass and chemical form; stock rates remain separately attributed to the API.",
                        snippet,
                        evidence=cp,
                    )
            if si == 1:
                descriptor = runner.get_node(self.after, p)
                descriptor["preparation_notes"] = (
                    "Adjust Solution A to pH 8.0 before the separately described sterilization and later additions; titrant and amount are not specified."
                )
                self.pdf_claim(
                    p + ["preparation_notes"],
                    "Move the pH instruction to its original stock context.",
                    self.pdf_snippet("Adjust pH"),
                    old=["preparation_steps", 1, "description"],
                )
        self.after.pop("ph_value")
        self.pdf_claim(
            ["ph_value"],
            "Withdraw flattened final-medium pH; the PDF places the adjustment under Solution A.",
            self.pdf_snippet("Adjust pH"),
            old=["ph_value"],
        )
        block = self.preparation()
        serum = self.append(
            ["solutions"],
            {
                "preferred_term": "Sterile foetal or newborn calf serum",
                "notes": "Add 1 part to 4 parts combined basal preparation after cooling. The source permits either serum; no mass concentration, fixed dose or numeric percent basis is inferred.",
            },
        )
        self.pdf_claim(
            serum + ["notes"],
            "Restore the explicit serum input and ratio without converting generic parts into an assumed concentration.",
            block,
        )
        p = self.append(
            ["variants"],
            {
                "name": "Casein hydrolysate alternative",
                "relationship": "SUBSTITUTED_COMPONENT_VARIANT",
                "description": "The original DSMZ recipe allows casein hydrolysate in place of lactalbumin hydrolysate.",
                "modifications": [
                    "Replace the 8.10 g lactalbumin hydrolysate batch input in Solution A with 8.10 g casein hydrolysate, not both together. Other preparation instructions are unchanged."
                ],
            },
        )
        start = self.texts["DSMZ1021"].index("Lactalbumin hydrolysate or")
        end = self.texts["DSMZ1021"].index("D-Glucose", start)
        self.pdf_claim(
            p + ["modifications"],
            "Preserve the source-explicit alternative omitted from the API, as a separate substitution rather than an additional ingredient.",
            self.texts["DSMZ1021"][start:end].rstrip(),
            evidence=p,
        )

    def komodo(self):
        rows = self.data[self.key]
        names = [
            "Yeast extract",
            "D-Glucose",
            "KCl",
            "MgCl2 x 6 H2O",
            "CaCl2 x 2 H2O",
            "NaCl",
            "NaHCO3",
            "Agar",
            "NaH2PO4 x 2 H2O",
            "casein hydrolysate",
            "Distilled water",
            "new borne calf serum",
        ]
        indices = [0, 4, 5, 6, 7, 8, 9, 10, 11, None, None, None]
        if self.key == "K1021_16929":
            names += ["O2", "N2", "CO2"]
            indices += [None] * 3
        for name, old in zip(names, indices, strict=True):
            row = rows[name]
            unquantified = name in {"Distilled water", "new borne calf serum", "O2", "N2", "CO2"}
            quantity = None if unquantified else {"value": row[3], "unit": "G_PER_L"}
            if name == "new borne calf serum":
                reason = "The table's generic Gram/Mol columns show 200.00 and 0.20 for serum; these do not establish density or a chemically meaningful molarity. No numeric concentration is adopted. The linked recipe supplies a 4:1 base/serum preparation ratio."
            elif unquantified:
                runner.require(row[3:] == ["null", "null"], "Expected unquantified source input")
                reason = "The source lists this component with null Gram and Mol amounts. Its amount is unknown, not zero; no gas fraction, flow rate or fixed water dose is inferred."
            else:
                reason = "The KOMODO table explicitly reports Gram Amount per liter of medium. Retain the exact source precision at medium scope, not the previously copied DSMZ stock rate. The separate rounded Mol Amount column is not used for conversion."
            p = self.component(
                ["ingredients"],
                name,
                old,
                self.key,
                ["rows", name],
                "unquantified" if unquantified else "medium_rate",
                quantity,
                reason,
                " ".join(row),
            )
            self.claim(
                p + ["notes"],
                None,
                self.key,
                None,
                "evidence_only",
                "table_basis",
                "The explicit table header establishes the per-liter basis for dry-ingredient mass amounts, not a valid serum mass/molar conversion.",
                p,
                "Gram & Mol amounts are per Liter of medium.",
            )
        block = self.preparation()
        serum = ["ingredients", names.index("new borne calf serum")]
        self.pdf_claim(
            serum + ["notes"],
            "The KOMODO Instructions link identifies this preparation protocol. Retain its serum ratio as text; no density is assumed.",
            block,
            evidence=serum,
        )
        if self.key == "K1021":
            snippet = "PH Info: 8.0"
            reason = "Retain the pH reported by this database page; it is not newly interpreted as a measured finished-medium pH. The original protocol locates the adjustment in Solution A."
        else:
            self.after.pop("ph_value")
            snippet = "PH Info: null"
            reason = "Withdraw the copied pH 8.0 assertion: this variant's own page has no pH value. The linked protocol's Solution A adjustment is not a final variant pH measurement."
        self.claim(
            ["ph_value"],
            ["ph_value"],
            self.key,
            None,
            "evidence_only" if self.key == "K1021" else "remove_unsupported",
            "ph_scope",
            reason,
            [],
            snippet,
        )
        self.note(self.after, reason)

    def togo(self):
        body = self.data["M2287"]
        base = self.append(
            ["solutions"],
            {
                "preferred_term": "Mitsuhashi-Maramorosch basal medium",
                "composition": [],
                "notes": "The source gives these basal concentrations before supplementation with 5% heat-inactivated fetal bovine serum. No basal-medium addition dose, final combined volume or dilution factor is supplied.",
            },
        )
        self.claim(
            base + ["notes"],
            None,
            "M2287",
            ["comments", 0],
            "add",
            "basal_scope",
            "Keep the listed basal rates separate from the later serum supplement; no post-supplement dilution is calculated.",
            [],
        )
        for ri, row in enumerate(body["components"][0]["items"]):
            serum = ri == 9
            unit = {"L": "L", "g/L": "G_PER_L", "mM": "MILLIMOLAR"}.get(row["unit"])
            quantity = None if serum else {"value": shared.numeric(row["volume"]), "unit": unit}
            reason = (
                "Source serum supplement is 5%, with no w/v, v/v or w/w basis. Withdraw the unsupported PERCENT_W_V value; preserve heat-inactivated fetal bovine serum and the unspecified percentage as text."
                if serum
                else (
                    "The source explicitly gives a 1 L water input, not 1 g/L or a measured final combined volume."
                    if ri == 0
                    else "Source-explicit basal-medium concentration before the separately described serum supplement. No final-medium dilution, molar/mass conversion or hydrate substitution is inferred."
                )
            )
            parent = ["ingredients"] if serum else base + ["composition"]
            p = self.component(
                parent,
                row["component_name"],
                ri if ri < 10 else None,
                "M2287",
                ["components", 0, "items", ri],
                "unknown_percent" if serum else "water" if ri == 0 else "basal_rate",
                quantity,
                reason,
            )
            self.claim(
                p + ["notes"],
                None,
                "M2287",
                ["comments", 0],
                "evidence_only",
                "basal_scope",
                "The source's prose confirms the basal recipe followed by serum supplementation. Its parenthetical literature citation is not a verified DOI and is not promoted to independent article evidence.",
                p,
            )

    def relationships(self):
        if self.key == "M2287":
            return
        if self.key == "D1021":
            paths = [
                (
                    ["variant_children", 0],
                    "DERIVED_FROM",
                    "K1021",
                    "casein hydrolysate casein hydrolysate",
                    "KOMODO 1021 selects the permitted casein alternative and reports post-supplement medium rates; these encodings are not treated as an exact duplicate of the lactalbumin stock-based record.",
                )
            ]
        elif self.key == "K1021":
            paths = [
                (
                    ["parent_media"],
                    "DERIVED_FROM",
                    "K1021",
                    "casein hydrolysate casein hydrolysate",
                    "KOMODO selects DSMZ's permitted casein alternative and reports medium rates rather than stock rates; exact duplicate status is withdrawn.",
                ),
                (
                    ["variant_children", 0],
                    "STRAIN_SPECIFIC_VARIANT",
                    "K1021_16929",
                    "MEDIUM 1021 MODIFIED FOR DSM 16929",
                    "The child is explicitly modified for DSM 16929 and lists additional unquantified O2, N2 and CO2; it is not an exact source duplicate.",
                ),
            ]
        else:
            paths = [
                (
                    ["parent_media"],
                    "STRAIN_SPECIFIC_VARIANT",
                    "K1021_16929",
                    "MEDIUM 1021 MODIFIED FOR DSM 16929",
                    "Explicit DSM 16929 modification with additional unquantified gas rows; no gas amount or strain growth evidence is inferred.",
                )
            ]
        for p, relationship, source, snippet, reason in paths:
            node = runner.get_node(self.after, p)
            node["relationship"], node["notes"] = relationship, reason
            for field in ("relationship", "notes"):
                self.claim(
                    p + [field],
                    p + [field],
                    source,
                    None,
                    "correct",
                    "variant_link",
                    reason,
                    p,
                    snippet,
                )
            if p == ["parent_media"]:
                self.after["variant_relationship"] = relationship
                self.after["variant_modifications"] = [reason]
                for field in ("variant_relationship", "variant_modifications"):
                    self.claim(
                        [field],
                        [field],
                        source,
                        None,
                        "correct",
                        "variant_link",
                        reason,
                        [],
                        snippet,
                    )

    def formulate(self):
        prefix, separator, previous = self.before["notes"].partition(
            "Commercial Product: LB Medium"
        )
        runner.require(separator, "Historical provenance drift")
        self.after["notes"] = (
            prefix.rstrip()
            + "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product: LB Medium"
            + previous
        )
        self.note(
            self.after,
            "The false LB constituent expansion is withdrawn. Each source's actual hydrolysate and preparation scope is retained. Existing unrelated chemical annotations and history are preserved, not recertified; no taxa-media growth association is added.",
        )
        if self.key == "D1021":
            self.dsmz()
            sp, snippet = ["data", "solutions", 1, "recipe", 1], None
        elif self.key == "M2287":
            self.togo()
            sp, snippet = ["components", 0, "items", 10], None
        else:
            self.komodo()
            sp, snippet = ["rows", "casein hydrolysate"], " ".join(
                self.data[self.key]["casein hydrolysate"]
            )
        for index in LB[self.key]:
            self.claim(
                ["notes"],
                ["ingredients", index, "concentration"],
                self.key,
                sp,
                "remove_unsupported",
                "false_lb_removed",
                "Remove the falsely substituted LB constituent and dose; the exact source specifies hydrolysate, not LB medium.",
                [],
                snippet,
            )
        self.relationships()

    def finish(self, timestamp):
        for claim in self.claims:
            claim["new"] = copy.deepcopy(
                runner.get_node(self.after, claim["pointer"][:-1]).get(claim["pointer"][-1])
            )
        self.after["references"] = []
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            title = (
                "KOMODO - the Known Media Database"
                if key.startswith("K")
                else (
                    self.texts[key].splitlines()[0]
                    if key == "DSMZ1021"
                    else (
                        self.data[key]["meta"]["name"]
                        if key == "M2287"
                        else self.data[key]["data"]["medium"]["name"]
                    )
                )
            )
            self.after["references"].append(
                {
                    "reference": meta["url"],
                    "title": title,
                    "notes": f"source_type={'culture_collection_page' if key == 'DSMZ1021' else 'dataset'}; discovery_mode={'catalog_page' if key.startswith('K') else 'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; accession={key}; capture_sha256={meta['sha256']}. Authors and publication year are not supplied. Copyright/access years are not publication years. This source supports formulation, not newly curated organism growth.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=URLS[self.key],
            notes="Restore source-specific hydrolysates, stock/basal/medium quantity boundaries, missing inputs and preparation; correct unsupported duplicate links. Preserve IDs and prior history. Unknown serum bases/doses and gas amounts remain unknown.",
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
