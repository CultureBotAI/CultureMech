#!/usr/bin/env python3
"""Restore the complete inspected medium-119 family without mixing source stages."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import re
from decimal import Decimal
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_lactalbumin_formulations as prior
import repair_methanogen_stock_boundaries as shared
from bs4 import BeautifulSoup
from curation_source_fixtures import read_pdf_capture

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import (
    extract_recipe_pdf,
    html_recipe_text,
    parse_recipe,
    recipe_source,
)

runner, ROOT = shared.runner, shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-methanobacterium-family"
CONTEXT_SHA = "db28859fc6fde46c49576874f3697f1fe44dec82751da923d2aef04f84cd4573"
ACTION = "RESTORED_MEDIUM_119_SOURCE_FORMULATIONS_AND_STOCK_SCOPES_WITH_EVIDENCE"
K_ACCESSIONS = (
    "119",
    "119.1",
    "119_11975",
    "119_11977",
    "119_11978",
    "119_11979",
    "119_11995",
    "119_1224",
    "119_15163",
    "119_3468",
    "119_4855",
    "119_6216",
    "119_7057",
    "119_7256",
    "119_9575",
)
SOURCE_URLS = {
    **{
        f"K{a}": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
        + a
        for a in K_ACCESSIONS
    },
    **{
        f"D{a}": "https://mediadive.dsmz.de/rest/medium/" + a
        for a in ("119", "119a", "119b", "119c")
    },
    **{
        f"DSMZ{a}": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium" + a + ".pdf"
        for a in ("119", "119a", "119b", "119c")
    },
}
STAGES = {
    "D119": [207, 208, 209, 595, 5861],
    "D119a": [210, 595, 2618, 209, 5861],
    "D119b": [211, 595, 777, 208, 209, 5861],
    "D119c": [213, 595, 208, 209, 5861],
}
RENAMED = {
    "Cysteine-HCl x H2O": "L-Cysteine HCl x H2O",
    "Resazurin": "Sodium resazurin",
    "sludge from an anaerobic digester": "Sludge",
}
IDENTITY_FIELDS = ("term", "mediaingredientmech_chebi_term", "mediaingredientmech_term")


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    runner.require(context["terminal"] and not context["errors"], "Incomplete captures")
    runner.require(
        {r["key"] for r in context["records"]} == {"K" + a for a in K_ACCESSIONS} | set(STAGES),
        "Cohort drift",
    )
    return context


def sources(context):
    data, texts, titles = {}, {}, {}
    runner.require(set(context["sources"]) == set(SOURCE_URLS), "Source set drift")
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        runner.require(
            meta["url"] == meta["response_url"] == SOURCE_URLS[key]
            and meta["http_status"] == 200
            and runner.sha(raw.encode()) == meta["sha256"],
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        parsed = parse_recipe(recipe_source(meta["url"]), raw, meta)
        texts[key], titles[key] = parsed.content, parsed.title
        if key.startswith("DSMZ"):
            payload = read_pdf_capture(meta)
            runner.require(
                runner.sha(payload) == meta["pdf_sha256"]
                and extract_recipe_pdf(payload) == (raw, 3 if key == "DSMZ119" else 2),
                "Original PDF drift",
            )
        elif key.startswith("K"):
            tables = [
                t
                for t in BeautifulSoup(raw, "html.parser").find_all("table")
                if "Gram Amount" in t.get_text()
            ]
            runner.require(len(tables) == 1, "Ambiguous recipe table")
            rows = [
                [html_recipe_text(str(c))[0] for c in tr.find_all("td", recursive=False)]
                for tr in tables[0].find_all("tr")
            ]
            runner.require(
                rows[0] == ["Name", "Semi unique name", "Unique Name", "Gram Amount", "Mol Amount"]
                and all(len(r) == 5 for r in rows)
                and len({r[0] for r in rows[1:]}) == len(rows) - 1,
                "KOMODO table drift",
            )
            data[key] = rows[1:]
        else:
            data[key] = json.loads(raw)
            ss = data[key]["data"]["solutions"]
            runner.require([s["id"] for s in ss] == STAGES[key], "DSMZ stage drift")
            runner.require(
                all(r["optional"] == 0 for s in ss for r in s.get("recipe", [])),
                "Optional input requires review",
            )
    return data, texts, titles


def number(value):
    return format(Decimal(str(value)).normalize(), "f")


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
        runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
        runner.require(
            not any(before.get(k) for k in ("evidence", "references", "solutions", "variants")),
            "Existing provenance needs reconciliation",
        )
        self.data, self.texts, self.titles = sources(self.context)
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.pdf = "DSMZ" + ("119" if key.startswith("K") else key[1:])
        self.claims, self.lineage, self.used = [], [], []
        self.old, self.lb, self.accounted = {}, [], set()
        for i, node in enumerate(before["ingredients"]):
            p = ["ingredients", i]
            if "LB Medium" in node.get("supplier_catalog", {}).get("supplier_name", ""):
                self.lb.append(p)
            else:
                label = node["preferred_term"].casefold()
                runner.require(label not in self.old, "Ambiguous old ingredient")
                self.old[label] = p
        runner.require(
            [runner.get_node(before, p)["preferred_term"] for p in self.lb]
            == ["Tryptone", "Yeast extract", "Sodium chloride"],
            "False-LB identity drift",
        )
        self.after["ingredients"], self.after["solutions"] = [], []

    def context_claim(self, reason, source, snippet, *, old=None, kind="recipe_context"):
        self.note(self.after, reason)
        self.claim(["notes"], old, source, None, "evidence_only", kind, reason, [], snippet)

    def emit(self, parent, label, quantity, sp, kind, reason, *, descriptor=False, snippet=None):
        old_name = RENAMED.get(label, label) if self.key.startswith("K") else label
        old = None if descriptor else self.old.get(old_name.casefold())
        node = (
            copy.deepcopy(runner.get_node(self.before, old)) if old else {"preferred_term": label}
        )
        if old:
            runner.require(
                tuple(old) not in self.accounted
                or (label == "Yeast extract" and self.key in {"D119", "D119b", "D119c"}),
                "Repeated old ingredient",
            )
            self.accounted.add(tuple(old))
        node["preferred_term"] = label
        withdraw = (self.key.startswith("K") and label in RENAMED) or label in {
            "NiCl2 x 6 H2O",
            "Sodium resazurin",
        }
        if withdraw:
            for field in IDENTITY_FIELDS:
                node.pop(field, None)
            reason += " Copied annotations do not establish the source's exact chemical form; withdraw them, preserve the literal source name, and archive the prior node. No replacement ontology identifier is inferred."
        if node.get("notes", "").lstrip().startswith("[Merged 2 duplicates:"):
            node["notes"] = (
                "Superseded flattening history, not a current amount: " + node["notes"].strip()
            )
        if quantity is None:
            node.pop("concentration", None)
        else:
            node["concentration"] = quantity
        if descriptor:
            node.update(name=label, composition=[])
        self.note(node, reason)
        p = self.append(parent, node)
        ep = [] if descriptor else p
        self.lineage.append(
            {
                "pointer": p,
                "old_pointer": old,
                "source": self.key,
                "source_pointer": sp,
                "label": label,
                "kind": kind,
            }
        )
        for field in ("concentration", "notes", "preferred_term") + (
            ("name",) if descriptor else ()
        ):
            self.claim(
                p + [field],
                old + [field] if old else None,
                self.key,
                sp,
                "correct" if old else "add",
                kind,
                reason,
                ep,
                snippet,
            )
        if old and withdraw:
            for field in IDENTITY_FIELDS:
                if field in runner.get_node(self.before, old):
                    self.claim(
                        p + [field],
                        old + [field],
                        self.key,
                        sp,
                        "remove_unsupported",
                        "copied_identity_withdrawn",
                        reason,
                        ep,
                        snippet,
                    )
        return p

    def pdf_row(self, si, row):
        ss = self.data[self.key]["data"]["solutions"]
        text = self.texts[self.pdf]
        if si:
            marker = ss[si]["name"] + " (from medium "
            runner.require(text.count(marker) == 1, "Ambiguous PDF stage")
            text = text.split(marker, 1)[1]
            # A table ends before the next named stock, including page breaks.
            boundaries = [
                text.find(s["name"] + " (from medium ") for s in ss[1:] if s["id"] != ss[si]["id"]
            ]
            text = text[: min([n for n in boundaries if n >= 0], default=len(text))]
        else:
            text = text[: text.index("Dissolve ingredients")]
        label = row.get("compound", row.get("solution"))
        if row.get("attribute"):
            label += " (" + row["attribute"] + ")"
        matches = [
            line.strip()
            for line in text.splitlines()
            if line.strip().startswith(label + " ") and line.split()[-1] == row["unit"]
        ]
        runner.require(len(matches) == 1, f"Ambiguous PDF row: {self.key}/{si}/{label}")
        runner.require(
            Decimal(matches[0].split()[-2]) == Decimal(str(row["amount"])),
            "PDF/API amount conflict",
        )
        return matches[0]

    def corroborate(self, p, field, si, row, reason, descriptor=False):
        self.claim(
            p + [field],
            None,
            self.pdf,
            None,
            "evidence_only",
            "original_recipe",
            reason,
            [] if descriptor else p,
            self.pdf_row(si, row),
        )

    def komodo(self):
        for i, row in enumerate(self.data[self.key]):
            label, _, _, gram, _ = row
            quantity = None if gram == "null" else {"value": gram, "unit": "G_PER_L"}
            reason = (
                "Provider Gram Amount is null; no fixed amount is asserted and missing is not zero."
                if quantity is None
                else f"Provider-reported rate: {gram} g/L, preserving the displayed precision. This table reports medium rates, not stock inputs or stock addition volumes."
            )
            reason += " No Mol Amount, SEED aggregate identity, density or linked DSMZ normalization is adopted."
            p = self.emit(
                ["ingredients"],
                label,
                quantity,
                ["recipe_table", i + 1],
                "provider_medium_rate" if quantity else "unquantified",
                reason,
                snippet=" ".join(row),
            )
            self.claim(
                p + ["notes"],
                None,
                self.key,
                None,
                "evidence_only",
                "quantity_basis",
                reason,
                p,
                "Gram & Mol amounts are per Liter of medium.",
            )
        ph = next(line for line in self.texts[self.key].splitlines() if line.startswith("PH Info:"))
        value = ph.removeprefix("PH Info: ").split(",")[0]
        if value == "null":
            self.after.pop("ph_value", None)
        else:
            self.after["ph_value"] = float(value)
        self.claim(
            ["ph_value"],
            ["ph_value"],
            self.key,
            None,
            "correct" if value == "null" else "evidence_only",
            "provider_ph",
            "Use only this exact provider accession's pH metadata; a null does not support the copied 7.6 or an inferred target pH.",
            [],
            ph,
        )
        if self.key in {"K119", "K119.1"}:
            self.context_claim(
                "Provider aerobic=true and pH=7.5 metadata disagree with the linked DSMZ anoxic preparation and complete-medium pH 6.8-7.0. Retain provider scope without asserting a resolved oxygen requirement.",
                self.key,
                "Is Aerobic: true",
            )
        self.context_claim(
            "The linked original uses anoxic preparation; its individual stock inputs and strain instructions must not silently replace this provider's reported medium rates.",
            "DSMZ119",
            "Sparge medium with 80%\nH2 and 20% CO2 gas mixture for 30 - 45 min to make it anoxic.",
        )
        variants = self.original_variants()
        relevant = {
            "K119_11977": [0],
            "K119_11978": [0],
            "K119_11995": [0],
            "K119_6216": [5],
            "K119_7057": [6],
            "K119_9575": [8],
            "K119_15163": [9],
            "K119.1": [0, 10],
        }
        for vi in relevant.get(self.key, []):
            name, snippet, modification = variants[vi]
            self.context_claim(
                f"Linked original instruction ({name}): {modification} This is a separate source/strain prescription, not an overwrite of the KOMODO table or new growth evidence. Any disagreement remains explicit.",
                "DSMZ119",
                snippet,
                kind="source_variant_comparison",
            )

    def stock(self, row, sp, si):
        name = row.get("solution", row.get("compound"))
        if "compound" in row:
            name += " (" + row["attribute"] + ")"
        runner.require(row["unit"] == "ml", "Stock dose unit drift")
        dose = number(Decimal(str(row["amount"])) / 1000)
        reason = f"Receiving-medium addition: {row['amount']} ml = {dose} L of this prepared stock. This is an addition volume, not stock strength or final-medium concentration."
        p = self.emit(
            ["solutions"],
            name,
            {"value": dose, "unit": "L"},
            sp,
            "stock_dose",
            reason,
            descriptor=True,
        )
        self.corroborate(p, "concentration", 0, row, reason, True)
        if "compound" in row:
            label = row["compound"]
            value, unit = (
                ("0.1", "PERCENT_W_V") if label == "Sodium resazurin" else ("15", "PERCENT_V_V")
            )
            runner.require(
                (label, row["attribute"])
                in {("Sodium resazurin", "0.1% w/v"), ("Methanol", "15% v/v")},
                "Unknown stock strength",
            )
            cp = self.emit(
                p + ["composition"],
                label,
                {"value": value, "unit": unit},
                sp,
                "stock_strength",
                "Explicit source stock strength; keep separate from its receiving-medium dose. No density or final-medium dilution is inferred.",
            )
            self.corroborate(
                cp,
                "concentration",
                0,
                row,
                "Original table gives stock strength and separate dose.",
            )
            return
        ss = self.data[self.key]["data"]["solutions"]
        s = ss[si]
        runner.require(s["id"] == row["solution_id"] and s["name"] == name, "Stock identity drift")
        for ri, ingredient in enumerate(s.get("recipe", [])):
            self.dsmz_component(p + ["composition"], ingredient, si, ri)
        if s.get("steps"):
            node = runner.get_node(self.after, p)
            node["preparation_notes"] = "\n\n".join(st["step"] for st in s["steps"])
            for j, _step in enumerate(s["steps"]):
                self.claim(
                    p + ["preparation_notes"],
                    None,
                    self.key,
                    ["data", "solutions", si, "steps", j, "step"],
                    "add",
                    "stock_preparation",
                    "This preparation belongs only to the named stock, not to the whole receiving medium.",
                    [],
                )
        if not s.get("recipe"):
            runner.require(s["id"] == 2618, "Unreviewed empty stock")
            runner.get_node(self.after, p).pop("composition")

    def dsmz_component(self, parent, row, si, ri):
        label = row["compound"]
        stage = self.data[self.key]["data"]["solutions"][si]["id"]
        sp = ["data", "solutions", si, "recipe", ri]
        if row["unit"] == "ml":
            value = number(Decimal(str(row["amount"])) / 1000)
            quantity, kind = {"value": value, "unit": "L"}, "liquid_input"
            reason = f"Preparation input: {row['amount']} ml = {value} L. This is input volume, not a mass, stock dose or measured final-volume denominator."
        elif stage == 5861:
            runner.require(
                label == "FeSO4 x 7 H2O" and row["amount"] == 1 and row["unit"] == "g",
                "Ferrous stock drift",
            )
            quantity, kind = {"value": "0.1", "unit": "PERCENT_W_V"}, "stock_strength"
            reason = "The named stock explicitly has 0.1% w/v ferrous sulfate heptahydrate, prepared from 1 g and 1000 ml of 0.1 N sulfuric acid. The receiving dose remains separate."
        elif stage == 595:
            runner.require(row["unit"] in {"g", "mg"}, "Trace-stock mass unit drift")
            mass = Decimal(str(row["amount"])) / (1000 if row["unit"] == "mg" else 1)
            quantity, kind = {"value": number(mass), "unit": "G_PER_L"}, "stock_makeup_rate"
            reason = f"Stock input {row['amount']} {row['unit']} = {number(mass)} g, divided by the explicitly made-up final stock volume of 1 L. Not a receiving-medium concentration."
        elif si == 0 and self.key == "D119":
            runner.require(row["unit"] == "g", "Basal mass unit drift")
            value = format(Decimal(str(row["amount"])) / Decimal("1.003"), ".6g")
            quantity, kind = {"value": value, "unit": "G_PER_L"}, "verified_final_volume_rate"
            reason = f"Direct basal input {row['amount']} g / explicit original final volume 1.003 L = {value} g/L (six significant digits). Excludes stock preparation masses and applies only to base DSMZ 119."
        else:
            runner.require(row["unit"] in {"g", "mg"}, "Batch mass unit drift")
            quantity, kind = None, "batch_mass"
            reason = f"Source batch input: {row['amount']} {row['unit']}. Keep the mass in notes; neither input water nor API volume/g_l encoding establishes a measured final volume. No g/L concentration is asserted."
        if row.get("attribute"):
            reason += " Literal source material qualifier: " + row["attribute"] + "."
        if label == "HCl":
            reason += " The 25% basis is unspecified; do not infer a mass percentage or density."
        if label == "H2SO4":
            reason += " Retain 0.1 N as source text; no unsupported normality enum, molarity or g/L is introduced."
        if label == "Yeast extract" and self.key != "D119a":
            reason += " The old combined yeast amount mixed basal and sludge preparation stages. Keep their independent inputs separate; incubation and centrifugation do not prove quantitative yeast transfer to the final medium."
        p = self.emit(parent, label, quantity, sp, kind, reason)
        self.corroborate(p, "notes", si, row, reason)
        if kind == "stock_makeup_rate":
            self.claim(
                p + ["concentration"],
                None,
                self.pdf,
                None,
                "evidence_only",
                "verified_stock_volume",
                reason,
                p,
                "Finally\nmake up to 1000.00 ml.",
            )
        elif kind == "verified_final_volume_rate":
            self.claim(
                p + ["concentration"],
                None,
                self.pdf,
                None,
                "evidence_only",
                "verified_final_volume",
                reason,
                p,
                "Final volume: 1003 ml",
            )
        elif kind == "stock_strength":
            self.claim(
                p + ["concentration"],
                None,
                self.pdf,
                None,
                "evidence_only",
                "explicit_stock_strength",
                reason,
                p,
                "FeSO4 x 7 H2O solution (0.1% w/v)",
            )

    def dsmz(self):
        ss = self.data[self.key]["data"]["solutions"]
        for ri, row in enumerate(ss[0]["recipe"]):
            sp = ["data", "solutions", 0, "recipe", ri]
            if "solution_id" in row:
                si = next(i for i, s in enumerate(ss) if s["id"] == row["solution_id"])
                self.stock(row, sp, si)
            elif row["compound"] in {"Sodium resazurin", "Methanol"}:
                self.stock(row, sp, 0)
            else:
                self.dsmz_component(["ingredients"], row, 0, ri)
        steps = ss[0]["steps"]
        runner.require(
            [s["description"] for s in self.before["preparation_steps"]]
            == [step["step"] for s in ss for step in s.get("steps", [])],
            "Flattened preparation drift",
        )
        self.after["preparation_steps"] = copy.deepcopy(
            self.before["preparation_steps"][: len(steps)]
        )
        for j in range(len(steps)):
            self.claim(
                ["preparation_steps"],
                ["preparation_steps"],
                self.key,
                ["data", "solutions", 0, "steps", j, "step"],
                "correct",
                "stage_preparation",
                "Only the main-stage instructions remain at recipe root; stock preparation instructions are preserved on their named solution descriptors.",
                [],
            )
        if self.key == "D119":
            self.after["variants"] = []
            for name, snippet, modification in self.original_variants():
                p = self.append(
                    ["variants"],
                    {
                        "name": name,
                        "relationship": "STRAIN_SPECIFIC_VARIANT",
                        "modifications": [modification],
                    },
                )
                for field in ("name", "relationship", "modifications"):
                    self.claim(
                        p + [field],
                        None,
                        self.pdf,
                        None,
                        "add",
                        "conditional_strain_recipe",
                        "Explicit original strain instruction, separate from the base formulation. This does not assert measured growth or add a taxon association.",
                        p,
                        snippet,
                    )

    def original_variants(self):
        text = self.texts["DSMZ119"]
        start = text.index("For DSM 1093")
        end = text.index("Sludge fluid (from medium 119)")
        section = text[start:end]
        starts = [m.start() for m in re.finditer(r"For DSM \d", section)] + [len(section)]
        variants = []
        for a, b in zip(starts, starts[1:], strict=False):
            snippet = section[a:b].strip()
            clean = re.sub(
                r"\u00a9 2022 DSMZ - All rights reserved\s+Page 1 of 3\s+119: METHANOBACTERIUM MEDIUM",
                "",
                snippet,
            )
            name, modification = " ".join(clean.split()).split(": ", 1)
            variants.append((name, snippet, modification))
        runner.require(len(variants) == 16, "Strain instruction count drift")
        return variants

    def ref(self, key, relation, reason):
        spec = self.specs[key]
        return {
            "id": spec["id"],
            "path": spec["path"],
            "name": runner.load_yaml(spec["before_text"])["name"],
            "relationship": relation,
            "notes": reason,
        }

    def links(self):
        derivative = "KOMODO explicitly links DSMZ 119, but its source-specific rates, nulls and metadata are not an exact copy of the original. DERIVED_FROM denotes documented source derivation, not a measured growth association."
        strain = "This provider explicitly names a strain-specific formulation linked to DSMZ 119. Retain it under the KOMODO 119 family without calling copied signatures or identical table rows an exact source duplicate."
        uncertain = "Retain this existing family candidate as UNCERTAIN, not a proven direction of derivation or a bicarbonate-only variant. DSMZ 119 uses 4 g bicarbonate and H2/CO2 preparation; DSMZ 119c uses 0.5 g and N2 preparation. Both preserve distinct stock scopes; the old LB/tryptone assertion is withdrawn."
        instructions = next(
            line for line in self.texts["K119"].splitlines() if line.startswith("Instructions:")
        )
        children = ["K" + a for a in K_ACCESSIONS if a != "119"]
        if self.key == "K119":
            self.after["parent_media"] = self.ref("D119", "DERIVED_FROM", derivative)
            self.after["variant_relationship"] = "DERIVED_FROM"
            self.after["variant_modifications"] = [derivative]
            self.after["variant_children"] = [
                self.ref(k, "STRAIN_SPECIFIC_VARIANT", strain) for k in children
            ]
            for f in ("parent_media", "variant_relationship", "variant_modifications"):
                self.claim(
                    [f],
                    [f],
                    "K119",
                    None,
                    "add",
                    "family_relationship",
                    derivative,
                    ["parent_media"],
                    instructions,
                )
            for i, k in enumerate(children):
                quote = next(
                    line for line in self.texts[k].splitlines() if line.startswith("Name:")
                )
                self.claim(
                    ["variant_children"],
                    ["variant_children"],
                    k,
                    None,
                    "correct",
                    "family_relationship",
                    strain,
                    ["variant_children", i],
                    quote,
                )
        elif self.key.startswith("K"):
            self.after["parent_media"] = self.ref("K119", "STRAIN_SPECIFIC_VARIANT", strain)
            self.after["variant_relationship"] = "STRAIN_SPECIFIC_VARIANT"
            self.after["variant_modifications"] = [strain]
            quote = next(
                line for line in self.texts[self.key].splitlines() if line.startswith("Name:")
            )
            for f in ("parent_media", "variant_relationship", "variant_modifications"):
                self.claim(
                    [f],
                    [f],
                    self.key,
                    None,
                    "correct",
                    "family_relationship",
                    strain,
                    ["parent_media"],
                    quote,
                )
        elif self.key == "D119":
            self.after["parent_media"] = self.ref("D119c", "UNCERTAIN", uncertain)
            self.after["variant_relationship"] = "UNCERTAIN"
            self.after["variant_modifications"] = [uncertain]
            self.after["variant_children"] = [self.ref("K119", "DERIVED_FROM", derivative)]
            self.claim(
                ["variant_children"],
                ["variant_children"],
                "K119",
                None,
                "add",
                "family_relationship",
                derivative,
                ["variant_children", 0],
                instructions,
            )
            for f in ("parent_media", "variant_relationship", "variant_modifications"):
                self.claim(
                    [f],
                    [f],
                    "D119c",
                    ["data", "solutions", 0, "steps", 0, "step"],
                    "correct",
                    "family_relationship",
                    uncertain,
                    ["parent_media"],
                )
        elif self.key == "D119c":
            self.after["variant_children"] = [self.ref("D119", "UNCERTAIN", uncertain)]
            self.claim(
                ["variant_children"],
                ["variant_children"],
                "D119",
                ["data", "solutions", 0, "steps", 0, "step"],
                "correct",
                "family_relationship",
                uncertain,
                ["variant_children", 0],
            )
        if self.key in {"K119", "D119b"}:
            reason = "Withdraw the unsupported K119/DSMZ119b exact-duplicate edge: K119 links original DSMZ119, whereas DSMZ119b includes methanol and selenite-tungstate and different bicarbonate, water and preparation. Their old copied ingredient signatures are not source evidence of identity."
            if self.key == "D119b":
                for f in ("parent_media", "variant_relationship", "variant_modifications"):
                    self.after.pop(f)
                    self.claim(
                        [f],
                        [f],
                        "D119b",
                        ["data", "solutions", 0, "recipe", 14],
                        "remove_unsupported",
                        "false_duplicate_withdrawn",
                        reason,
                        [],
                    )
            self.context_claim(
                reason,
                "K119",
                instructions,
                old=["variant_children"] if self.key == "K119" else None,
                kind="false_duplicate_withdrawn",
            )
            self.context_claim(
                reason, "DSMZ119b", "Methanol (15% v/v)", kind="false_duplicate_withdrawn"
            )

    def formulate(self):
        prefix, marker, history = self.before["notes"].partition("Commercial Product: LB Medium")
        runner.require(marker, "Historical note drift")
        self.after["notes"] = (
            prefix.rstrip()
            + "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product: LB Medium"
            + history
        )
        self.komodo() if self.key.startswith("K") else self.dsmz()
        if not self.after["solutions"]:
            self.after.pop("solutions")
        acid_quote = (
            " ".join(next(row for row in self.data[self.key] if row[0] == "2-Methylbutyric acid"))
            if self.key.startswith("K")
            else "DL-2-Methylbutyric acid"
        )
        acid_source = self.key if self.key.startswith("K") else self.pdf
        self.context_claim(
            "Archive all prior ingredient nodes, including false LB expansion, combined yeast amounts and copied or chemically inexact annotations, in append-only history. New nodes follow this exact source's stage and label; other unchanged chemical annotations are preserved, not recertified.",
            acid_source,
            acid_quote,
            old=["ingredients"],
            kind="old_ingredients_archived",
        )
        for i, _node in enumerate(self.before["ingredients"]):
            p = ("ingredients", i)
            if p in self.accounted:
                continue
            reason = (
                "Remove only supplier-tagged false LB constituent; restore the source methylbutyric acid and preserve genuine yeast extract and NaCl."
                if list(p) in self.lb
                else "The inspected exact-accession recipe table does not list this copied ingredient. Withdraw its current concentration/node, retain its full prior assertion in history, and do not substitute a neighboring DSMZ formulation."
            )
            self.claim(
                ["notes"],
                list(p) + ["concentration"],
                acid_source,
                None,
                "remove_unsupported",
                (
                    "false_lb_removed"
                    if list(p) in self.lb
                    else "source_mismatched_ingredient_removed"
                ),
                reason,
                [],
                acid_quote,
            )
            self.accounted.add(p)
        runner.require(
            self.accounted == {("ingredients", i) for i in range(len(self.before["ingredients"]))},
            "Unaccounted old ingredient",
        )
        self.links()
        self.context_claim(
            "Source-scoped recipe inputs supersede unsupported flattened concentrations and false LB identities. All prior history and permanent IDs remain unchanged; unquantified quantities remain unknown. No taxa-media association is added.",
            acid_source,
            acid_quote,
            old=["notes"],
        )

    def finish(self, timestamp):
        for c in self.claims:
            c["new"] = copy.deepcopy(
                runner.get_node(self.after, c["pointer"][:-1]).get(c["pointer"][-1])
            )
        self.after["references"] = []
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            source_type = (
                "culture_collection_page"
                if key.startswith("DSMZ")
                else "web_page" if key.startswith("K") else "dataset"
            )
            self.after["references"].append(
                {
                    "reference": meta["url"],
                    "title": self.titles[key],
                    "notes": f"source_type={source_type}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year are not supplied; copyright/access dates are not publication years.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=SOURCE_URLS[self.key],
            notes="Restore exact-source medium-119 ingredients, liquid inputs, stock strengths/doses and preparation scopes; preserve source-specific variants, quantity limits and disagreements, and repair reciprocal family references without inferring growth.",
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
        errors = runner.errors(self.after, "MediaRecipe")
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
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    args = parser.parse_args()
    _, result = process(
        ROOT, args.plan, "apply" if args.apply else "verify" if args.verify else "preview"
    )
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
