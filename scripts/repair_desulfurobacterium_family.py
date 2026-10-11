#!/usr/bin/env python3
"""Guarded repair of the fourteen inspected medium-829 source records and stocks."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from decimal import Decimal
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_lactalbumin_formulations as prior
import repair_methanogen_stock_boundaries as shared
from bs4 import BeautifulSoup
from curation_source_fixtures import read_pdf_capture
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import (
    extract_recipe_pdf,
    html_recipe_text,
    parse_recipe,
    recipe_source,
)
from culturemech.validation.write_validated import infer_target_class

runner, ROOT = shared.runner, shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-desulfurobacterium-family"
PLAN_PATH = HERE / "plan-v2.json"
CONTEXT_SHA = "ef9c0aa87ab3f6b939c9b088337f801601151ba34e0797406b69bb038a29a0be"
ACTION = "RESTORED_MEDIUM_829_SOURCE_FORMULATIONS_AND_STOCK_SCOPES_WITH_EVIDENCE"
K_ACCESSIONS = ("829", "829a", "829.1", "829.2", "829.3", "829_16661", "2027")
STAGES = {
    "D829": [1679, 1680, 595, 777, 1038, 6262],
    "D829a": [1681, 34],
    "D829b": [1682, 595, 777, 1038, 1680, 6262],
    "D829c": [1683, 241, 5980],
    "D829d": [1684, 241, 5980],
}
SOURCE_URLS = {
    **{
        f"K{a}": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
        + a
        for a in K_ACCESSIONS
    },
    **{k: "https://mediadive.dsmz.de/rest/medium/" + k[1:] for k in STAGES},
    **{
        "DSMZ" + k[1:]: "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium" + k[1:] + ".pdf"
        for k in STAGES
    },
    "M2587": "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2587",
    "S1680": "https://mediadive.dsmz.de/rest/solution/1680",
}
IDENTITY_FIELDS = (
    "term",
    "chebi_term",
    "mediaingredientmech_chebi_term",
    "mediaingredientmech_term",
    "synonyms",
)
VOLUMES = {"D829": "1005", "D829b": "1005", "D829c": "1011", "D829d": "1020"}
K_ALIASES = {
    "MES": "MES [2-(N-morpholino) ethane sulfonic acid]",
    "D(+)-Biotin": "D-(+)-biotin",
    "Pyridoxine HCl": "Pyridoxine hydrochloride",
    "Na2-dithionite": "Na2S2O4",
    "H2O": "Distilled water",
}


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    runner.require(context["terminal"] and not context["errors"], "Incomplete sources")
    runner.require(
        {r["key"] for r in context["records"]}
        == set(STAGES) | {"K" + a for a in K_ACCESSIONS} | {"M2587", "S1680"},
        "Cohort drift",
    )
    return context


def sources(context):
    runner.require(set(context["sources"]) == set(SOURCE_URLS), "Source set drift")
    data, texts, titles = {}, {}, {}
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        runner.require(
            meta["url"] == meta["response_url"] == SOURCE_URLS[key]
            and meta["http_status"] == 200
            and runner.sha(raw.encode()) == meta["sha256"],
            "Capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        parsed = parse_recipe(recipe_source(meta["url"]), raw, meta)
        texts[key], titles[key] = parsed.content, parsed.title
        if key.startswith("DSMZ"):
            payload = read_pdf_capture(meta)
            pages = 3 if key == "DSMZ829" else 1 if key == "DSMZ829a" else 2
            runner.require(
                runner.sha(payload) == meta["pdf_sha256"]
                and extract_recipe_pdf(payload) == (raw, pages),
                "Original PDF drift",
            )
        elif key.startswith("K"):
            tables = [
                t
                for t in BeautifulSoup(raw, "html.parser").find_all("table")
                if "Gram Amount" in t.get_text()
            ]
            runner.require(len(tables) == 1, "Ambiguous table")
            rows = [
                [html_recipe_text(str(c))[0] for c in tr.find_all("td", recursive=False)]
                for tr in tables[0].find_all("tr")
            ]
            runner.require(
                rows[0] == ["Name", "Semi unique name", "Unique Name", "Gram Amount", "Mol Amount"]
                and all(len(r) == 5 for r in rows),
                "Table shape drift",
            )
            runner.require(
                len({r[0] for r in rows[1:]}) == len(rows) - 1, "Duplicate source labels"
            )
            data[key] = rows[1:]
        else:
            data[key] = json.loads(raw)
            if key in STAGES:
                ss = data[key]["data"]["solutions"]
                runner.require(
                    [s["id"] for s in ss] == STAGES[key]
                    and all(r["optional"] == 0 for s in ss for r in s["recipe"]),
                    "Source stages drift",
                )
            elif key == "S1680":
                runner.require(
                    data[key]["data"]["id"] == 1680 and len(data[key]["data"]["recipe"]) == 7,
                    "Standalone stock drift",
                )
            else:
                runner.require(
                    data[key]["meta"]["gm"] == "http://togomedium.org/medium/M2587"
                    and [s["paragraph_index"] for s in data[key]["components"]]
                    == [1, 8, 11, 14, 16, 18],
                    "TOGO stages drift",
                )
    return data, texts, titles


def number(value):
    return format(Decimal(str(value)).normalize(), "f")


def walk(node, pointer=()):
    if isinstance(node, dict):
        if "preferred_term" in node:
            yield pointer, node
        for field in ("ingredients", "composition", "solutions"):
            for i, child in enumerate(node.get(field, [])):
                yield from walk(child, pointer + (field, i))


class Review(shared.Review):
    append = stocks.Review.append
    claim = prior.Review.claim

    def __init__(self, before, key):
        self.context = frozen()
        self.specs = {r["key"]: r for r in self.context["records"]}
        spec = self.specs[key]
        runner.require(
            before == runner.load_yaml(spec["before_text"]) and before["id"] == spec["id"],
            "Unreviewed baseline",
        )
        self.target_class = infer_target_class(before)
        runner.require(not runner.errors(before, self.target_class), "Baseline schema failure")
        self.data, self.texts, self.titles = sources(self.context)
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.claims, self.lineage, self.used = [], [], []
        self.old = list(walk(before))
        # SolutionRecipe has no root evidence slot. Its reviewed water entry
        # carries explicitly scoped composition/context claims, not a fake import.
        self.root_evidence = ["composition", 6] if key == "S1680" else []
        if key != "S1680":
            runner.require(
                not before.get("evidence") and not before.get("variants"),
                "Existing evidence/variants require reconciliation",
            )
            self.after["ingredients"], self.after["solutions"] = [], []

    def proof(self, pointer, old, source, sp, status, kind, reason, ep=None, snippet=None):
        list_item = old is not None and isinstance(runner.get_node(self.before, old[:-1]), list)
        self.claim(
            pointer,
            None if list_item else old,
            source,
            sp,
            status,
            kind,
            reason,
            self.root_evidence if ep is None else ep,
            snippet,
        )
        if list_item:
            self.claims[-1].update(
                old_pointer=old,
                old_field=runner.field_name(old),
                old=copy.deepcopy(runner.get_node(self.before, old)),
            )

    def context_note(self, text, source, snippet, old=None, kind="source_context"):
        self.note(self.after, text)
        self.proof(["notes"], old, source, None, "evidence_only", kind, text, snippet=snippet)

    def emit(
        self,
        parent,
        label,
        quantity,
        source,
        sp,
        reason,
        kind,
        *,
        descriptor=False,
        snippet=None,
        old_pointer=None,
    ):
        old_label = K_ALIASES.get(label, label) if self.key.startswith("K") else label
        candidates = [
            (p, n)
            for p, n in self.old
            if len(p) >= 2
            and n["preferred_term"].casefold() == old_label.casefold()
            and "LB Medium" not in n.get("supplier_catalog", {}).get("supplier_name", "")
            and (p[-2] == "solutions") == descriptor
        ]
        runner.require(len(candidates) <= 1, "Ambiguous baseline node")
        old = (
            old_pointer
            if old_pointer is not None
            else list(candidates[0][0]) if candidates else None
        )
        node = (
            copy.deepcopy(runner.get_node(self.before, old)) if old else {"preferred_term": label}
        )
        if descriptor:
            node = {"preferred_term": label, "name": label, "composition": []}
        else:
            node["preferred_term"] = label
            for field in ("source", "notes"):
                if field in node and self.key == "K2027":
                    node.pop(field)
            if any(marker in node.get("notes", "") for marker in ("[Collapsed", "[Merged")):
                node["notes"] = (
                    "Superseded flattening history, not a current quantity: " + node["notes"]
                )
        withdrawn = []
        if not descriptor and label in {
            "NiCl2 x 6 H2O",
            "Sodium resazurin",
            "Calcium D-(+)-pantothenate",
        }:
            withdrawn = [field for field in IDENTITY_FIELDS if field in node]
            for field in withdrawn:
                node.pop(field)
            if withdrawn:
                reason += " Copied annotations do not establish this exact salt, hydrate or stereochemical form; archive them without inventing replacement identifiers."
        if quantity is None:
            node.pop("concentration", None)
        else:
            node["concentration"] = quantity
        self.note(node, reason)
        p = self.append(parent, node)
        ep = self.root_evidence if descriptor else p
        self.lineage.append(
            {
                "pointer": p,
                "old_pointer": old,
                "source": source,
                "source_pointer": sp,
                "label": label,
                "kind": kind,
            }
        )
        for field in ("preferred_term", "concentration", "notes") + (
            ("name",) if descriptor else ()
        ):
            self.proof(
                p + [field],
                old + [field] if old else None,
                source,
                sp,
                "correct" if old else "add",
                kind,
                reason,
                ep,
                snippet,
            )
        for field in withdrawn:
            self.proof(
                p + [field],
                old + [field],
                source,
                sp,
                "remove_unsupported",
                "chemical_form",
                reason,
                ep,
                snippet,
            )
        if self.key == "K2027" and old and "source" in runner.get_node(self.before, old):
            self.proof(
                p + ["source"],
                old + ["source"],
                source,
                sp,
                "remove_unsupported",
                "source_attribution",
                "KOMODO's table, not an explicit original DSMZ g/L statement, supports this provider rate or null. Original batch quantities remain separately documented.",
                ep,
                snippet,
            )
        return p

    def pdf_row(self, si, row):
        stages = self.data[self.key]["data"]["solutions"]
        text = self.texts["DSMZ" + self.key[1:]]
        if si:
            marker = stages[si]["name"] + " (from medium "
            runner.require(text.count(marker) == 1, "Ambiguous PDF stock")
            text = text.split(marker, 1)[1]
            ends = [
                text.find(s["name"] + " (from medium ")
                for s in stages[1:]
                if s["id"] != stages[si]["id"]
            ]
            text = text[: min([n for n in ends if n >= 0], default=len(text))]
        else:
            text = text.split("1. Dissolve ingredients", 1)[0]
        label = row.get("compound", row.get("solution"))
        if label == "Sulfur":
            runner.require(row["condition"] == "powdered", "Sulfur form drift")
            label += ", powdered"
        if row.get("attribute"):
            label += " (" + row["attribute"] + ")"
        matches = [
            line.strip()
            for line in text.splitlines()
            if line.strip().startswith(label + " ") and line.split()[-1] == row["unit"]
        ]
        runner.require(
            len(matches) == 1 and Decimal(matches[0].split()[-2]) == Decimal(str(row["amount"])),
            "PDF/API row disagreement: " + label,
        )
        return matches[0]

    def original_support(self, p, row, si, reason, descriptor=False):
        self.proof(
            p + ["notes"],
            None,
            "DSMZ" + self.key[1:],
            None,
            "evidence_only",
            "original_recipe",
            reason,
            self.root_evidence if descriptor else p,
            self.pdf_row(si, row),
        )

    def dsmz_component(self, parent, row, si, ri):
        stage = self.data[self.key]["data"]["solutions"][si]["id"]
        sp = ["data", "solutions", si, "recipe", ri]
        label, amount, unit = row["compound"], row["amount"], row["unit"]
        extra_quote = None
        if unit == "ml":
            quantity = {"value": number(Decimal(str(amount)) / 1000), "unit": "L"}
            kind = "liquid_input"
            reason = f"Preparation input {amount} ml / 1000 = {quantity['value']} L, not mass, volume percent or measured final volume."
        elif stage in {6262, 34}:
            expected = (
                ("Na2S2O4", 0.5, "5", "Na-dithionite solution (5% w/v)")
                if stage == 6262
                else ("Na2S x 9 H2O", 3, "3", "Neutralized sulfide solution 3% (w/v)")
            )
            runner.require(
                (label, amount, unit) == (expected[0], expected[1], "g"),
                "Explicit stock strength drift",
            )
            quantity, kind = {
                "value": expected[2],
                "unit": "PERCENT_W_V",
            }, "explicit_stock_strength"
            reason = f"Source stock heading explicitly states {expected[2]}% w/v. Preserve its {amount} g batch input, carrier/water recipe and receiving dose separately; the strength is not inferred from water volume."
            extra_quote = expected[3]
        elif stage == 595:
            runner.require(unit in {"g", "mg"}, "SL-10 mass unit drift")
            mass = Decimal(str(amount)) / (1000 if unit == "mg" else 1)
            quantity, kind = {"value": number(mass), "unit": "G_PER_L"}, "stock_makeup_rate"
            reason = f"SL-10 input {amount} {unit} = {number(mass)} g / explicit made-up stock volume 1 L. This stock rate is not a receiving-medium concentration."
            extra_quote = "Finally\nmake up to 1000.00 ml."
        elif si == 0 and self.key in VOLUMES:
            runner.require(unit == "g", "Basal mass unit drift")
            volume = Decimal(VOLUMES[self.key]) / 1000
            value = format(Decimal(str(amount)) / volume, ".6g")
            quantity, kind = {"value": value, "unit": "G_PER_L"}, "reported_final_volume_rate"
            reason = f"Direct basal input {amount} g / source-reported final volume {volume} L = {value} g/L, six significant digits. This is the printed denominator, not independently measured volume; the liquid-input discrepancy is retained at recipe root."
            extra_quote = f"Final volume: {VOLUMES[self.key]} ml"
        else:
            runner.require(unit in {"g", "mg"}, "Unreviewed batch unit")
            quantity, kind = None, "batch_mass"
            reason = f"Source batch input: {amount} {unit}. No explicit final-volume/makeup statement was found for this stage in the inspected original. Retain the mass in notes; API volume/g_l and water input are not an independently verified denominator."
        for qualifier in ("condition", "attribute"):
            if row.get(qualifier):
                reason += f" Literal source {qualifier}: {row[qualifier]}."
        if label == "HCl":
            reason += " The 25% carrier lacks an explicit percentage basis; no density or gram conversion is asserted."
        if label == "NaOH" and unit == "ml":
            reason += " The 1 N carrier strength is separate from this input volume and from the selenium-stock NaOH mass."
        p = self.emit(parent, label, quantity, self.key, sp, reason, kind)
        self.original_support(p, row, si, reason)
        if extra_quote:
            self.proof(
                p + ["concentration"],
                None,
                "DSMZ" + self.key[1:],
                None,
                "evidence_only",
                "quantity_basis",
                reason,
                p,
                extra_quote,
            )

    def unquantified(self, parent, label, source, sp, text):
        return self.emit(parent, label, None, source, sp, text, "preparation_titrant")

    def dsmz_stock(self, row, ri):
        stages = self.data[self.key]["data"]["solutions"]
        sp = ["data", "solutions", 0, "recipe", ri]
        name = row.get("solution", row.get("compound"))
        indicator = "compound" in row
        if indicator:
            runner.require(
                name == "Sodium resazurin" and row["attribute"] == "0.1% w/v",
                "Unreviewed indicator stock",
            )
            name += " (0.1% w/v)"
        runner.require(row["unit"] == "ml", "Receiving stock unit drift")
        dose = number(Decimal(str(row["amount"])) / 1000)
        reason = f"Receiving-batch addition {row['amount']} ml / 1000 = {dose} L of prepared stock, not g/L or an inferred ml/L rate. Stock strength and preparation remain separate."
        p = self.emit(
            ["solutions"],
            name,
            {"value": dose, "unit": "L"},
            self.key,
            sp,
            reason,
            "stock_dose",
            descriptor=True,
        )
        self.original_support(p, row, 0, reason, True)
        if indicator:
            cp = self.emit(
                p + ["composition"],
                "Sodium resazurin",
                {"value": "0.1", "unit": "PERCENT_W_V"},
                self.key,
                sp,
                "Explicit 0.1% w/v indicator stock, not the concentration in receiving medium. Keep its separate 0.50 ml dose.",
                "indicator_strength",
            )
            self.original_support(
                cp, row, 0, "Original row gives separate indicator strength and dose."
            )
            return
        si = next(i for i, s in enumerate(stages) if s["id"] == row["solution_id"])
        stock = stages[si]
        runner.require(stock["name"] == name, "Stock name/ID mismatch")
        for ci, component in enumerate(stock["recipe"]):
            self.dsmz_component(p + ["composition"], component, si, ci)
        steps = stock.get("steps", [])
        if steps:
            runner.get_node(self.after, p)["preparation_notes"] = "\n\n".join(
                st["step"] for st in steps
            )
            for j, _step in enumerate(steps):
                pointer = ["data", "solutions", si, "steps", j, "step"]
                self.proof(
                    p + ["preparation_notes"],
                    None,
                    self.key,
                    pointer,
                    "add",
                    "stock_preparation",
                    "Keep this complete instruction on the named stock, not at receiving-medium root.",
                )
                if stock["id"] == 1680:
                    self.unquantified(
                        p + ["composition"],
                        "NaOH",
                        self.key,
                        pointer,
                        "Unquantified growth-factor stock titration to pH 9.0. No fixed addition or strength is stated; do not reuse the selenium-stock mass or dithionite carrier volume.",
                    )
                elif stock["id"] == 241:
                    self.unquantified(
                        p + ["composition"],
                        "KOH",
                        self.key,
                        pointer,
                        "Unquantified mineral-stock titration: first NTA to pH 6.5, then completed stock to pH 7.0. These are not receiving-medium pH values or a fixed KOH dose.",
                    )
                elif stock["id"] == 34:
                    self.unquantified(
                        p + ["composition"],
                        "H2SO4",
                        self.key,
                        pointer,
                        "Add sterile 2 M sulfuric-acid carrier dropwise to stock pH about 7.0. Carrier strength is explicit but its addition volume is unquantified; no final stock sulfuric-acid concentration is asserted.",
                    )

    def dsmz(self):
        stages = self.data[self.key]["data"]["solutions"]
        for ri, row in enumerate(stages[0]["recipe"]):
            if "solution_id" in row or row.get("compound") == "Sodium resazurin":
                self.dsmz_stock(row, ri)
            else:
                self.dsmz_component(["ingredients"], row, 0, ri)
        steps = stages[0]["steps"]
        runner.require(
            [s["description"] for s in self.before["preparation_steps"]]
            == [step["step"] for stage in stages for step in stage.get("steps", [])],
            "Flattened preparation drift",
        )
        self.after["preparation_steps"] = copy.deepcopy(
            self.before["preparation_steps"][: len(steps)]
        )
        for i in range(len(steps)):
            self.proof(
                ["preparation_steps"],
                ["preparation_steps"],
                self.key,
                ["data", "solutions", 0, "steps", i, "step"],
                "correct",
                "preparation_scope",
                "Only main-recipe instructions remain at root; stock instructions are preserved on their exact stock descriptors.",
            )
        if self.key in VOLUMES:
            liquids = sum(
                Decimal(str(row["amount"])) for row in stages[0]["recipe"] if row["unit"] == "ml"
            )
            text = f"The original reports final volume {VOLUMES[self.key]} ml, while its listed main liquid inputs sum to {number(liquids)} ml. Preserve the discrepancy. Source-reported basal rates do not certify independently measured final volume; no missing makeup water is invented."
            self.context_note(text, "DSMZ" + self.key[1:], f"Final volume: {VOLUMES[self.key]} ml")
        else:
            self.context_note(
                "The inspected original 829a has no final-volume heading. Its 1020.5 ml listed liquid-input sum and the API's 1020 ml volume do not establish a measured denominator. The stock's 250 ml bottle is equipment, not final volume.",
                "DSMZ829a",
                "The sulfide solution is prepared in a 250 ml screw-capped bottle",
            )
        if self.key in {"D829", "D829c"}:
            quote = self.original_variant()
            modification = " ".join(quote.split()).split(": ", 1)[1]
            self.after["variants"] = []
            p = self.append(
                ["variants"],
                {
                    "name": (
                        "DSM 16661 and DSM 21157 source prescription"
                        if self.key == "D829"
                        else "DSM 16304 pH prescription"
                    ),
                    "relationship": "STRAIN_SPECIFIC_VARIANT",
                    "modifications": [modification],
                },
            )
            for field in ("name", "relationship", "modifications"):
                self.proof(
                    p + [field],
                    None,
                    "DSMZ" + self.key[1:],
                    None,
                    "add",
                    "conditional_variant",
                    "Original strain-specific instruction, separate from the base recipe; no measured growth association is inferred.",
                    p,
                    quote,
                )

    def original_variant(self):
        if self.key == "D829c":
            return "For DSM 16304: Adjust pH to 5.5."
        return "For DSM 16661, DSM 21157: Omit growth-stimulating factors and pressurize vials after\ninoculation to 2 bar with sterile 80% H2 and 20% CO2 gas mixture."

    def metadata(self, key, prefix):
        found = [line for line in self.texts[key].splitlines() if line.startswith(prefix + ":")]
        runner.require(len(found) == 1, "Ambiguous provider metadata")
        return found[0]

    def komodo(self):
        for ri, row in enumerate(self.data[self.key]):
            label, _, _, gram, _ = row
            quantity = None if gram == "null" else {"value": gram, "unit": "G_PER_L"}
            scope = "standalone submedium" if self.key == "K2027" else "medium"
            reason = (
                f"Exact-accession provider {scope} Gram Amount is null; no fixed amount is asserted."
                if quantity is None
                else f"Exact-accession provider {scope} Gram Amount: {gram} g/L, preserving displayed precision."
            )
            reason += " This is a source-reported rate or null, not an inferred stock dose or a normalization from the linked DSMZ recipe. Mol Amount and SEED aggregates are not adopted."
            p = self.emit(
                ["ingredients"],
                label,
                quantity,
                self.key,
                ["recipe_table", ri + 1],
                reason,
                "provider_rate" if quantity else "provider_null",
                snippet=" ".join(row),
            )
            self.proof(
                p + ["concentration"],
                None,
                self.key,
                None,
                "evidence_only",
                "provider_basis",
                reason,
                p,
                "Gram & Mol amounts are per Liter of medium.",
            )
        ph = self.metadata(self.key, "PH Info")
        value = ph.split(":", 1)[1].strip().split(",")[0]
        self.after.pop("ph_value", None)
        self.after.pop("ph_range", None)
        if value == "null":
            reason = "Exact source pH is null; withdraw the copied fixed 6.0 rather than inferring a value from the base recipe."
        elif "-" in value:
            lo, hi = [float(v.strip()) for v in value.split("-")]
            self.after["ph_range"] = {"min": lo, "max": hi}
            reason = "Use the complete provider pH range; withdraw the extra unsupported fixed pH."
        else:
            self.after["ph_value"] = float(value)
            reason = "Retain this exact accession's explicit pH; do not conflate another medium or stock pH."
        for field in ("ph_value", "ph_range"):
            if field in self.before or field in self.after:
                self.proof(
                    [field], [field], self.key, None, "correct", "provider_ph", reason, snippet=ph
                )
        if self.key == "K829a":
            for field in ("medium_type", "composition_type"):
                self.after[field] = "DEFINED"
                self.proof(
                    [field],
                    [field],
                    self.key,
                    None,
                    "correct",
                    "classification",
                    "Exact source states Is Complex: false, matching the distinct salt formulation, not the incorrectly copied medium-829 mixture.",
                    snippet="Is Complex: false",
                )
        if self.key == "K2027":
            self.after["record_kind"] = "SOLUTION"
            self.proof(
                ["record_kind"],
                ["record_kind"],
                self.key,
                None,
                "add",
                "stock_identity",
                "Explicit provider submedium assertion identifies a standalone stock, while its existing MediaRecipe schema shape and permanent identifier are preserved.",
                snippet="Is SubMedium: true",
            )
            self.context_note(
                "The six acid rates are provider-reported by KOMODO2027, not explicit g/L statements in original DSMZ829. The original growth-factor table gives batch masses and 1000 ml water without an explicit final stock volume. Keep the original preparation separate from a claim that its physical denominator was verified.",
                self.key,
                "Gram & Mol amounts are per Liter of medium.",
            )
            self.context_note(
                "Original stock preparation: six separately listed acid masses plus 1000 ml water, adjusted to pH 9.0 with unquantified NaOH and autoclaved under 100% N2. The exact KOMODO table leaves water and NaOH rates null; neither is replaced by a typical rate.",
                "DSMZ829",
                "Dissolve ingredients, adjust pH to 9.0 with NaOH, then autoclave under 100% N2 gas.",
            )
            return
        pdf = "DSMZ829a" if self.key == "K829a" else "DSMZ829"
        oxygen = self.metadata(self.key, "Is Aerobic")
        self.context_note(
            "Preserve the provider's aerobic metadata as a source assertion, not a biological growth claim. Its linked original specifies anoxic preparation; any disagreement remains unresolved rather than silently overriding either source.",
            self.key,
            oxygen,
        )
        self.context_note(
            "The original's anoxic instructions and stock preparations are separate source context; they do not override the provider's exact reported table rates and nulls.",
            pdf,
            "anoxic Hungate-type tubes",
        )
        if self.key in {"K829", "K829.1", "K829.2", "K829.3", "K829_16661"}:
            carbonate = next(row for row in self.data[self.key] if row[0] == "NaHCO3")
            self.context_note(
                "This source reports sodium bicarbonate, whereas original DSMZ829 lists sodium carbonate. Preserve exact source chemical identity; do not rename or average the two formulations.",
                self.key,
                " ".join(carbonate),
            )
            quote = next(
                line.strip()
                for line in self.texts["DSMZ829"].splitlines()
                if line.strip().startswith("Na2CO3 ")
            )
            self.context_note(
                "Original DSMZ829 lists 0.50 g sodium carbonate per basal batch; this is source comparison, not permission to replace the provider's bicarbonate rate.",
                "DSMZ829",
                quote,
            )
            dithionite = next(row for row in self.data[self.key] if row[0] == "Na2-dithionite")
            self.context_note(
                "The provider's displayed dithionite rate remains distinct from the original's 1 ml addition of 5% w/v stock; do not replace a source-specific rate with a different formulation's dilution.",
                self.key,
                " ".join(dithionite),
            )
            dose = next(
                line.strip()
                for line in self.texts["DSMZ829"].splitlines()
                if line.strip().startswith("Na-dithionite solution (5% w/v)")
                and line.split()[-1] == "ml"
            )
            self.context_note(
                "Original DSMZ829's dithionite stock strength and receiving input are separate from the KOMODO rate; the formulations are not certified identical.",
                "DSMZ829",
                dose,
            )
        if self.key in {"K829.3", "K829_16661"}:
            self.context_note(
                "Original DSMZ829 separately instructs DSM16661 and DSM21157 to omit growth factors and use 2 bar after inoculation. The provider tables retain their own quantities; notably K829_16661 still lists the acids. Source/version disagreement is explicit, not silently resolved.",
                "DSMZ829",
                self.original_variant(),
            )

    def togo(self):
        source = self.data[self.key]
        sections = source["components"]
        comments = source["comments"]
        destinations = {1: ["ingredients"]}
        stock_sections = {
            s["subcomponent_name"]: i for i, s in enumerate(sections) if s["subcomponent_name"]
        }
        for si, section in enumerate(sections):
            stage = section["paragraph_index"]
            for ri, row in enumerate(section["items"]):
                sp = ["components", si, "items", ri]
                label, amount, unit = row["component_name"], row.get("volume"), row.get("unit")
                descriptor = stage == 1 and (
                    label in stock_sections or label.startswith("Sodium resazurin")
                )
                extra = None
                if descriptor:
                    runner.require(unit == "ml", "TOGO dose unit drift")
                    quantity = {"value": number(Decimal(str(amount)) / 1000), "unit": "L"}
                    reason, kind = (
                        f"Receiving-batch dose {amount} ml = {quantity['value']} L. This is not g/L or a fixed per-liter dose. Restore the exact TOGO stock version rather than a same-named external stock.",
                        "stock_dose",
                    )
                elif unit == "ml":
                    quantity = {"value": number(Decimal(str(amount)) / 1000), "unit": "L"}
                    reason, kind = (
                        f"Source preparation input {amount} ml = {quantity['value']} L, not grams or a final-volume denominator. Keep each stage's water/carrier separate.",
                        "liquid_input",
                    )
                    if label == "HCl (25%; 7.7 M)":
                        reason += " Literal source carrier strength is 7.7 M, with unspecified-basis 25%; this does not make the whole SL-10 stock 7.7 M HCl."
                elif stage == 11:
                    runner.require(unit in {"g", "mg"}, "TOGO SL10 mass unit drift")
                    mass = Decimal(str(amount)) / (1000 if unit == "mg" else 1)
                    quantity = {"value": number(mass), "unit": "G_PER_L"}
                    reason, kind = (
                        f"SL-10 input {amount} {unit} = {number(mass)} g / explicitly made-up 1 L stock. This is not receiving-medium concentration; the old root mg-as-g interpretation is withdrawn.",
                        "stock_makeup_rate",
                    )
                    extra = "Finally make up to 1000.0 ml."
                elif stage == 18 and label == "Na2S2O4":
                    runner.require(amount == 50 and unit == "g", "TOGO dithionite mass drift")
                    quantity = {"value": "5", "unit": "PERCENT_W_V"}
                    reason, kind = (
                        "The stock heading explicitly states 5% w/v. Preserve 50 g dithionite, 50 g bicarbonate and 1000 ml water as this source's recipe, distinct from current DSMZ's NaOH carrier.",
                        "explicit_stock_strength",
                    )
                    extra = "Na-dithionite solution (5% w/v)"
                elif amount is None:
                    quantity = None
                    reason, kind = (
                        "The source gives no fixed addition amount. Preserve the stage-specific gas or titration context without a zero, typical dose or liquid concentration.",
                        "unquantified_material",
                    )
                    if row.get("conc_value") is not None:
                        reason += f" Literal gas qualifier: {row['conc_value']} {row['conc_unit']}; its percentage basis is not inferred."
                else:
                    runner.require(unit in {"g", "mg"}, "TOGO mass unit drift")
                    quantity = None
                    reason, kind = (
                        f"Exact source batch input {amount} {unit}, retained in notes. This TOGO stage has no explicit final-volume denominator; water input and the differently versioned DSMZ heading do not justify g/L.",
                        "batch_mass",
                    )
                parent = ["solutions"] if descriptor else destinations[stage]
                p = self.emit(
                    parent, label, quantity, self.key, sp, reason, kind, descriptor=descriptor
                )
                if extra:
                    self.proof(
                        p + ["concentration"],
                        None,
                        self.key,
                        None,
                        "evidence_only",
                        "quantity_basis",
                        reason,
                        p,
                        extra,
                    )
                if descriptor:
                    if label.startswith("Sodium resazurin"):
                        runner.require(
                            row["conc_value"] == 0.1 and row["conc_unit"] == "(w/v)",
                            "Indicator basis drift",
                        )
                        self.emit(
                            p + ["composition"],
                            "Sodium resazurin",
                            {"value": "0.1", "unit": "PERCENT_W_V"},
                            self.key,
                            sp,
                            "Explicit 0.1% w/v indicator strength, separate from the 0.50 ml receiving-batch dose.",
                            "indicator_strength",
                        )
                    else:
                        stock_index = stock_sections[label]
                        destinations[sections[stock_index]["paragraph_index"]] = p + ["composition"]
        self.after["preparation_steps"] = []
        for ci, item in enumerate(comments):
            if not item["comment"]:
                continue
            index = item["paragraph_index"]
            sp = ["comments", ci, "comment"]
            if index < 8:
                p = self.append(
                    ["preparation_steps"],
                    {
                        "step_number": len(self.after["preparation_steps"]) + 1,
                        "action": {
                            2: "DISSOLVE",
                            3: "ADJUST_PH",
                            4: "AUTOCLAVE",
                            5: "FILTER_STERILIZE",
                            6: "MIX",
                        }[index],
                        "description": item["comment"],
                    },
                )
                self.proof(
                    p + ["description"],
                    None,
                    self.key,
                    sp,
                    "add",
                    "medium_preparation",
                    "Retain the original main-recipe instruction and its stage; it is not new growth evidence.",
                )
            else:
                stage = max(s for s in destinations if s < index)
                p = destinations[stage][:-1]
                stock = runner.get_node(self.after, p)
                stock["preparation_notes"] = (
                    stock.get("preparation_notes", "") + "\n\n" + item["comment"]
                ).strip()
                self.proof(
                    p + ["preparation_notes"],
                    None,
                    self.key,
                    sp,
                    "add",
                    "stock_preparation",
                    "Preserve this instruction only on its source stock; do not apply stock pH or carrier preparation to the medium.",
                )
        self.after["ph_value"] = float(source["meta"]["ph"])
        self.proof(
            ["ph_value"],
            ["ph_value"],
            self.key,
            ["meta", "ph"],
            "add",
            "medium_ph",
            "Source main-medium pH, not growth-factor stock pH 9.0.",
        )
        self.after.pop("high_metal", None)
        trace = sections[2]["items"]
        co_index = next(i for i, r in enumerate(trace) if r["component_name"] == "CoCl2 x 6 H2O")
        self.proof(
            ["high_metal"],
            ["high_metal"],
            self.key,
            ["components", 2, "items", co_index],
            "remove_unsupported",
            "unsupported_flag",
            "Withdraw the unexplained high_metal assertion after correcting stock-stage mg-as-g quantities. This does not assert low metal, a biological threshold or a new false value.",
        )
        self.context_note(
            "TOGO M2587 is a distinct captured source version. It specifies a bicarbonate-based dithionite stock and no final-medium denominator; current DSMZ829's NaOH carrier and reported 1005 ml final volume must not silently replace these assertions. External same-name stock references are withdrawn unless exact composition/version identity is established.",
            self.key,
            json_excerpt(self.context["sources"][self.key]["raw"], ["components", 5, "items", 1]),
        )
        self.context_note(
            "The current DSMZ829 dithionite carrier is 0.50 ml of 1 N NaOH, unlike TOGO's bicarbonate stock. This comparison does not replace the source-specific TOGO formulation.",
            "DSMZ829",
            next(
                line.strip()
                for line in self.texts["DSMZ829"].splitlines()
                if line.strip().startswith("NaOH (1 N)")
            ),
        )
        self.context_note(
            "The TOGO dithionite section includes a hydrogen-gas item, while its preparation text specifies 80% N2 and 20% CO2. Preserve that upstream discrepancy; do not infer an amount or silently select one gas formulation.",
            self.key,
            "Dissolve NaHCO3 in water and make the solution anoxic by sparging with 80% N2 and 20% CO2 gas mixture.",
        )

    def standalone(self):
        source = self.data[self.key]["data"]
        rows = source["recipe"]
        runner.require(len(self.before["composition"]) == 7, "Standalone composition drift")
        self.after["composition"] = copy.deepcopy(self.before["composition"][:6])
        for i, row in enumerate(rows[:6]):
            p = ["composition", i]
            node = runner.get_node(self.before, p)
            runner.require(
                node["preferred_term"] == row["compound"]
                and node["term"]["id"] == f"mediadive.compound:{row['compound_id']}"
                and node["concentration"] == {"value": number(row["g_l"]), "unit": "G_PER_L"},
                "Prior stock rate drift",
            )
            evidence = [e for e in node["evidence"] if e["reference"] == SOURCE_URLS[self.key]]
            runner.require(
                len(evidence) == 1
                and evidence[0]["supports"] == "SUPPORT"
                and evidence[0]["snippet"] in self.texts[self.key],
                "Prior source evidence drift",
            )
            field = p + ["concentration"]
            self.claims.append(
                {
                    "pointer": field,
                    "old_pointer": field,
                    "field": runner.field_name(field),
                    "old_field": runner.field_name(field),
                    "ingredient": row["compound"],
                    "old": copy.deepcopy(node["concentration"]),
                    "new": copy.deepcopy(node["concentration"]),
                    "status": "verified",
                    "kind": "retained_provider_stock_rate",
                    "source": self.key,
                    "source_pointer": ["data", "recipe", i],
                    "reference": SOURCE_URLS[self.key],
                    "snippet": evidence[0]["snippet"],
                    "explanation": evidence[0]["explanation"],
                    "evidence_pointer": p,
                }
            )
            self.lineage.append(
                {
                    "pointer": p,
                    "old_pointer": p,
                    "source": self.key,
                    "source_pointer": ["data", "recipe", i],
                    "label": row["compound"],
                    "kind": "retained_provider_stock_rate",
                }
            )
        water = rows[6]
        runner.require(
            water["compound"] == "Distilled water"
            and water["amount"] == 1000
            and water["unit"] == "ml"
            and water["g_l"] is None,
            "Water source drift",
        )
        self.emit(
            ["composition"],
            "Distilled water",
            {"value": "1", "unit": "L"},
            self.key,
            ["data", "recipe", 6],
            "Correct the importer unit error: 1000 ml / 1000 = 1 L water input per stock preparation, not 1000% v/v, a measured final volume or a receiving-medium concentration.",
            "water_input",
        )
        steps = source["steps"]
        runner.require(
            len(steps) == 1 and steps[0]["step"] == self.before["preparation_notes"],
            "Standalone preparation drift",
        )
        self.unquantified(
            ["composition"],
            "NaOH",
            self.key,
            ["data", "steps", 0, "step"],
            "Source preparation adds NaOH to stock pH 9.0 without a fixed amount or carrier strength. Keep this titration separate from the provider-declared acid rates and water input.",
        )
        self.after.pop("ingredients")
        self.after["data_quality_flags"] = [
            f for f in self.before["data_quality_flags"] if f != "incomplete_composition"
        ]
        if not self.after["data_quality_flags"]:
            self.after.pop("data_quality_flags")
        for field in ("ingredients", "data_quality_flags"):
            self.proof(
                [field],
                [field],
                self.key,
                ["data", "recipe"],
                "remove_unsupported",
                "legacy_placeholder",
                "The exact source enumerates seven composition rows, which are represented in composition, with its unquantified NaOH preparation separately preserved. Remove the legacy stub and only its placeholder-related incomplete_composition flag, not a real ingredient or evidence claim.",
            )
        refs = self.after["references"]
        runner.require(
            len(refs) == 1
            and refs[0]["reference"] == SOURCE_URLS[self.key]
            and refs[0]["title"] == "MediaDive solution 1680: Growth-stimulating factors",
            "Prior bibliography drift",
        )
        refs[0]["title"] = self.titles[self.key]
        self.proof(
            ["references", 0, "title"],
            ["references", 0, "title"],
            self.key,
            ["data", "name"],
            "correct",
            "bibliographic_title",
            "Use the captured official source title. The prior MediaDive solution 1680 prefix is an accession label, not part of that title; the accession and earlier evidence remain unchanged.",
        )
        self.context_note(
            "Preserve six existing API-declared stock rates and their prior evidence unchanged. They are not independently measured final volumes or receiving-medium concentrations. Water is an explicit preparation input, and NaOH is unquantified stock titration; no universal working dose is inferred.",
            self.key,
            "Growth-stimulating factors",
        )

    def reference(self, key, relationship, notes):
        spec = self.specs[key]
        return {
            "id": spec["id"],
            "path": spec["path"],
            "name": runner.load_yaml(spec["before_text"])["name"],
            "relationship": relationship,
            "notes": notes,
        }

    def links(self):
        strain_notes = {
            "K829.1": "Source-specific DSM14290 variant: replace the base table's sulfur with 0.50 g/L yeast extract and use pH 6.5. It is not merely a pH change.",
            "K829.2": "Source-specific strain variant with a different mineral/vitamin composition and pH 6.0-6.5; the copied base signature does not establish exact duplication.",
            "K829.3": "Source-specific DSM21157 variant: its table omits all six growth-factor acids and changes other rates. It does not preserve unchanged base components merely because earlier imported signatures matched.",
            "K829_16661": "Source explicitly identifies DSM16661 modification. Displayed rows match KOMODO829 but pH is null and strain scope differs; source duplication is not proved, and original DSMZ's growth-factor omission remains a source conflict.",
        }
        derived = "The provider explicitly links this DSMZ accession. DERIVED_FROM denotes source derivation, not identical concentrations, stock scopes or biological growth evidence; retain source-specific formulation differences."
        if self.key in {"K829", "K829a"}:
            parent = "D829" if self.key == "K829" else "D829a"
            self.after["parent_media"] = self.reference(parent, "DERIVED_FROM", derived)
            self.after["variant_relationship"] = "DERIVED_FROM"
            self.after["variant_modifications"] = [derived]
            for field in ("parent_media", "variant_relationship", "variant_modifications"):
                self.proof(
                    [field],
                    [field],
                    self.key,
                    None,
                    "correct",
                    "family_relationship",
                    derived,
                    ["parent_media"],
                    self.metadata(self.key, "Instructions"),
                )
        elif self.key in {"D829", "D829a"}:
            child = "K829" if self.key == "D829" else "K829a"
            self.after["variant_children"] = [self.reference(child, "DERIVED_FROM", derived)]
            self.proof(
                ["variant_children"],
                ["variant_children"],
                child,
                None,
                "correct",
                "family_relationship",
                derived,
                ["variant_children", 0],
                self.metadata(child, "Instructions"),
            )
        if self.key == "K829":
            self.after["variant_children"] = [
                self.reference(key, "STRAIN_SPECIFIC_VARIANT", text)
                for key, text in strain_notes.items()
            ]
            for i, (key, text) in enumerate(strain_notes.items()):
                self.proof(
                    ["variant_children"],
                    ["variant_children"],
                    key,
                    None,
                    "correct",
                    "family_relationship",
                    text
                    + " Based on comparison of both complete exact-accession tables, not the title alone.",
                    ["variant_children", i],
                    self.metadata(key, "Name"),
                )
            self.context_note(
                "Remove KOMODO829a from this source-duplicate group: its exact table is a distinct salt/thiosulfate formulation explicitly linked to DSMZ829a, not a copy of the sea-salt/growth-factor base. Preserve the new reciprocal DSMZ829a source-derivation link.",
                "K829a",
                self.metadata("K829a", "Instructions"),
                ["variant_children"],
            )
        elif self.key in strain_notes:
            text = strain_notes[self.key]
            self.after["parent_media"] = self.reference("K829", "STRAIN_SPECIFIC_VARIANT", text)
            self.after["variant_relationship"] = "STRAIN_SPECIFIC_VARIANT"
            self.after["variant_modifications"] = [text]
            for field in ("parent_media", "variant_relationship", "variant_modifications"):
                self.proof(
                    [field],
                    [field],
                    self.key,
                    None,
                    "correct",
                    "family_relationship",
                    text
                    + " The complete provider tables, nulls and metadata were compared; neither ingredient-set matching nor title alone establishes equivalence.",
                    ["parent_media"],
                    self.metadata(self.key, "Name"),
                )

    def archive(self):
        if self.key.startswith("K"):
            source = self.key
            start = self.texts[source].index(
                "Name Semi unique name Unique Name Gram Amount Mol Amount"
            )
            quote = self.texts[source][start:].strip()
        elif self.key in STAGES:
            source = "DSMZ" + self.key[1:]
            quote = self.texts[source].split("1. Dissolve ingredients", 1)[0].strip()
        else:
            source = self.key
            quote = json_excerpt(
                self.context["sources"][source]["raw"],
                ["components", 0, "items"] if source == "M2587" else ["data", "recipe"],
            )
        reason = "Full exact-source recipe and stock/preparation tables were inspected. Reconstructed nodes retain explicit source scope; complete prior ingredient/stock assertions, including copied LB mappings and stage conflations, are archived in append-only history. A title alone is not the basis for removal. Unchanged annotations are preserved, not recertified; no new organism-growth association is added."
        for field in ("ingredients", "solutions"):
            if self.before.get(field):
                self.context_note(reason, source, quote, [field], "prior_nodes_archived")
        covered = {tuple(c["old_pointer"]) for c in self.claims if c["old_pointer"]}
        for p, node in self.old:
            if "concentration" in node and p + ("concentration",) not in covered:
                self.proof(
                    ["notes"],
                    list(p) + ["concentration"],
                    source,
                    None,
                    "remove_unsupported",
                    "old_quantity_accounted",
                    "The old quantity is absent or relocated in the complete source reconstruction. Preserve its exact old node in history rather than retaining an unsupported copied concentration or counting a stock component twice.",
                    snippet=quote,
                )
            for j, candidate in enumerate(node.get("concentration_candidates", [])):
                runner.require(
                    candidate["basis"] == "CROSS_MEDIUM_INFERENCE", "Unreviewed candidate basis"
                )
                self.proof(
                    ["notes"],
                    list(p) + ["concentration_candidates", j],
                    source,
                    None,
                    "remove_unsupported",
                    "old_candidate_accounted",
                    "Archive the copied cross-medium dose candidate with its unsupported descriptor. The exact provider table, not another medium, determines current quantities.",
                    snippet=quote,
                )

    def formulate(self):
        if "Commercial Product: LB Medium" in self.before.get("notes", ""):
            prefix, marker, suffix = self.before["notes"].partition("Commercial Product: LB Medium")
            self.after["notes"] = (
                prefix.rstrip()
                + "\n\nSuperseded historical provenance, not a current formulation claim:\n"
                + marker
                + suffix
            )
        if self.key.startswith("K"):
            self.komodo()
        elif self.key in STAGES:
            self.dsmz()
        elif self.key == "M2587":
            self.togo()
        else:
            self.standalone()
        if self.after.get("solutions") == []:
            self.after.pop("solutions")
        self.links()
        self.archive()

    def finish(self, timestamp):
        for claim in self.claims:
            claim["new"] = copy.deepcopy(
                runner.get_node(self.after, claim["pointer"][:-1]).get(claim["pointer"][-1])
            )
        refs = self.after.setdefault("references", [])
        runner.require(len({r["reference"] for r in refs}) == len(refs), "Duplicate references")
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            entry = next((r for r in refs if r["reference"] == meta["url"]), None)
            if entry is None:
                entry = {"reference": meta["url"]}
                refs.append(entry)
            entry.setdefault("title", self.titles[key])
            kind = (
                "culture_collection_page"
                if key.startswith("DSMZ")
                else "web_page" if key.startswith("K") else "dataset"
            )
            text = f"source_type={kind}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Individual authors and publication year not supplied; copyright/access year is not publication year. Source-scoped recipe evidence, not growth evidence."
            entry["notes"] = (entry.get("notes", "") + "\n\n" + text).strip()
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=SOURCE_URLS[self.key],
            notes="Restore exact-source medium-829 formulations and stock boundaries, preserve provider rates/nulls and source conflicts, repair quantity units and family scope, and retain prior evidence/history. Each scientific change is linked to an inspected source excerpt; no growth association inferred.",
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
        runner.require(
            self.after["curation_history"][:-1] == self.before["curation_history"],
            "Prior history changed",
        )
        runner.require(infer_target_class(self.after) == self.target_class, "Schema shape changed")
        errors = runner.errors(self.after, self.target_class)
        runner.require(not errors, f"Proposed schema failure: {errors}")
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
    parser.add_argument("--plan", type=Path, default=PLAN_PATH)
    args = parser.parse_args()
    _, result = process(
        ROOT, args.plan, "apply" if args.apply else "verify" if args.verify else "preview"
    )
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
