#!/usr/bin/env python3
"""Restore six OTEB source formulations with guarded, claim-linked evidence."""

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
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-oteb-family"
CONTEXT_SHA = "8f4e87e29247c1a0dfea3ce78ff0283c3456f1fbf7fd5b3bd3343eff06b0b52c"
ACTION = "RESTORED_OTEB_SOURCE_FORMULATIONS_AND_STOCK_SCOPES_WITH_EVIDENCE"
SOURCE_URLS = {
    **{
        "K"
        + key: "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo="
        + key
        for key in ("1245", "1245_18691", "6000")
    },
    "D1245": "https://mediadive.dsmz.de/rest/medium/1245",
    "S2474": "https://mediadive.dsmz.de/rest/solution/2474",
    "S5688": "https://mediadive.dsmz.de/rest/solution/5688",
    "DSMZ1245": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1245.pdf",
}
IDENTITY_FIELDS = (
    "term",
    "chebi_term",
    "mediaingredientmech_chebi_term",
    "mediaingredientmech_term",
)
ALIASES = {
    "Proteose Peptone #2": "Proteose peptone no. 2",
    "Potassium Phosphate, dibasic": "Potassium Phosphate",
    "Calf Serum, inactivated": "Fetal bovine serum",
    "Soluble Starch": "Starch",
}


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    runner.require(context["terminal"] and not context["errors"], "Incomplete captures")
    runner.require(
        {r["key"] for r in context["records"]}
        == {"K1245", "K1245_18691", "D1245", "K6000", "S2474", "S5688"},
        "Cohort drift",
    )
    for path, digest in context["preparation_receipt_sha256"].items():
        runner.require(runner.sha((ROOT / path).read_bytes()) == digest, "Reviewed decisions drift")
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
        if key.startswith("K"):
            tables = [
                t
                for t in BeautifulSoup(raw, "html.parser").find_all("table")
                if "Gram Amount" in t.get_text()
            ]
            runner.require(len(tables) == 1, "Ambiguous provider table")
            rows = [
                [html_recipe_text(str(c))[0] for c in tr.find_all("td", recursive=False)]
                for tr in tables[0].find_all("tr")
            ]
            runner.require(
                rows[0] == ["Name", "Semi unique name", "Unique Name", "Gram Amount", "Mol Amount"]
                and all(len(r) == 5 for r in rows),
                "Provider columns drift",
            )
            data[key] = rows[1:]
        elif key == "DSMZ1245":
            payload = read_pdf_capture(meta)
            runner.require(
                runner.sha(payload) == meta["pdf_sha256"]
                and extract_recipe_pdf(payload) == (raw, 2),
                "Original PDF drift",
            )
        else:
            data[key] = json.loads(raw)
    runner.require(
        [s["id"] for s in data["D1245"]["data"]["solutions"]] == [2474, 5688], "Recipe stages drift"
    )
    runner.require(
        [len(data[k]) for k in ("K1245", "K1245_18691", "K6000")] == [27, 28, 11],
        "Provider rows drift",
    )
    return data, texts, titles


def walk(node, path=()):
    if isinstance(node, dict):
        if "preferred_term" in node:
            yield path, node
        for field in ("ingredients", "composition", "solutions"):
            for i, child in enumerate(node.get(field, [])):
                yield from walk(child, path + (field, i))


def liters(amount):
    return {"value": format((Decimal(str(amount)) / 1000).normalize(), "f"), "unit": "L"}


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
        reviewed = json.loads((HERE / "source-review.json").read_text())
        self.decisions = {
            (r["source"], tuple(r["pointer"])): r for r in reviewed["source_decisions"]
        }
        self.pdf_rows = {
            (r["pointer"][0], r["pointer"][1]): r for r in reviewed["original_pdf_decisions"]
        }
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.claims, self.lineage, self.used = [], [], []
        self.old = list(walk(before))
        self.root_evidence = ["composition", 3] if key.startswith("S") else []
        if not key.startswith("S"):
            runner.require(
                not any(before.get(f) for f in ("evidence", "references", "solutions", "variants")),
                "Existing provenance needs reconciliation",
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

    def note_claim(self, reason, source, snippet, old=None, kind="source_context"):
        self.note(self.after, reason)
        self.proof(["notes"], old, source, None, "evidence_only", kind, reason, snippet=snippet)

    def old_pointer(self, label):
        alias = ALIASES.get(label, label)
        candidates = [
            list(p)
            for p, n in self.old
            if len(p) >= 2
            and n["preferred_term"].casefold() == alias.casefold()
            and "LB Medium" not in n.get("supplier_catalog", {}).get("supplier_name", "")
        ]
        runner.require(len(candidates) <= 1, f"Ambiguous old ingredient: {label}")
        return candidates[0] if candidates else None

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
        old=None,
        descriptor=False,
        snippet=None,
        withdraw=False,
    ):
        node = (
            copy.deepcopy(runner.get_node(self.before, old)) if old else {"preferred_term": label}
        )
        node["preferred_term"] = label
        if descriptor:
            node = {"preferred_term": label, "name": label, "composition": []}
        if quantity is None:
            node.pop("concentration", None)
        else:
            node["concentration"] = quantity
        if "[Collapsed" in node.get("notes", ""):
            node["notes"] = "Superseded flattening history, not a current amount: " + node["notes"]
        removed = [f for f in IDENTITY_FIELDS if withdraw and f in node]
        for f in removed:
            node.pop(f)
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
        for field in removed:
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
        return p

    def metadata(self, key, prefix):
        matches = [line for line in self.texts[key].splitlines() if line.startswith(prefix + ":")]
        runner.require(len(matches) == 1, "Metadata locator drift")
        return matches[0]

    def komodo(self):
        for i, row in enumerate(self.data[self.key]):
            label, semi, unique, gram, mol = row
            decision = self.decisions[(self.key, ("Metabolites list", i))]
            reason = (
                decision["reason"]
                + " Exact per-liter heading: Gram & Mol amounts are per Liter of medium."
            )
            for f in ("identity_note", "conflict_note"):
                if f in decision:
                    reason += " " + decision[f]
            # Calf serum is not a lexical synonym for the copied fetal serum.
            old = self.old_pointer(label)
            withdraw = label in {"Potassium Phosphate, dibasic", "Thiamine Pyrophosphate"}
            self.emit(
                ["ingredients"],
                label,
                decision["proposed_concentration"],
                self.key,
                ["Metabolites list", i],
                reason,
                decision["kind"],
                old=old,
                snippet=decision["snippet"],
                withdraw=withdraw,
            )
        ph = self.metadata(self.key, "PH Info")
        if self.key == "K1245":
            runner.require(ph == "PH Info: 6.8 - 7.2", "Base pH drift")
            runner.require(self.after["ph_range"] == {"min": 6.8, "max": 7.2}, "Old pH drift")
        else:
            runner.require(
                ph == "PH Info: null"
                and not self.after.get("ph_range")
                and not self.after.get("ph_value"),
                "Unreviewed pH",
            )
        self.note_claim(
            "Preserve the exact KOMODO Gram Amounts and nulls as source-specific assertions. No provider molar aggregation or copied DSMZ formulation replaces these rows. pH metadata is retained without inferring a missing value.",
            self.key,
            ph,
        )
        if self.key == "K6000":
            self.after["notes"] = (
                "KOMODO source accession 6000 is explicitly named Sugar Stock Solution (medium 1245). The old automatically constructed DSMZ/MediaDive6000 equivalence is unverified and is archived, not asserted. Keep this standalone stock's existing MediaRecipe schema shape and record_kind SOLUTION; no receiving-medium dose is inferred."
            )
            self.proof(
                ["notes"],
                ["notes"],
                self.key,
                None,
                "correct",
                "source_identity",
                self.after["notes"],
                snippet=self.metadata(self.key, "Name"),
            )
            self.proof(
                ["record_kind"],
                ["record_kind"],
                self.key,
                None,
                "verified",
                "record_kind",
                "Retain the already established solution kind; provider SubMedium is true.",
                snippet=self.metadata(self.key, "Is SubMedium"),
            )

    def original(self):
        sugar = None
        for si, stage in enumerate(self.data["D1245"]["data"]["solutions"]):
            stage_name = "main" if si == 0 else "sugar_stock"
            runner.require(si == 0 or sugar is not None, "Missing original sugar-stock input")
            parent = ["ingredients"] if si == 0 else sugar + ["composition"]
            for ri, row in enumerate(stage["recipe"]):
                original = self.pdf_rows[(stage_name, ri)]
                snippet = original["snippet"]
                sp = ["data", "solutions", si, "recipe", ri]
                reason = original["reason"]
                reason += f" Original {stage_name} row {ri + 1}: {original['batch_input']['amount']} {original['batch_input']['unit']} per preparation."
                if row["unit"] != "ml":
                    reason += " Mass is retained in notes because the source provides no defensible final-volume denominator for this preparation; the API's g_l is not recertified as an original measured concentration."
                label = row.get("compound") or row.get("solution")
                if label == "Vitamin K1":
                    vitamin = self.emit(
                        ["solutions"],
                        "Vitamin K1 (1% solution)",
                        original["proposed_concentration"],
                        "DSMZ1245",
                        [stage_name, ri],
                        reason,
                        "unresolved_percent_stock",
                        descriptor=True,
                        snippet=snippet,
                    )
                    inner = self.emit(
                        vitamin + ["composition"],
                        "Vitamin K1",
                        None,
                        "DSMZ1245",
                        [stage_name, ri],
                        "The original specifies 1% soln but does not identify w/v, w/w, or v/v. Keep that literal strength in notes, without asserting a numeric concentration or stock solvent.",
                        "unresolved_percent_strength",
                        old=self.old_pointer("Vitamin K1"),
                        snippet=snippet,
                    )
                    self.proof(
                        inner + ["notes"],
                        None,
                        "D1245",
                        sp,
                        "conflict",
                        "provider_mass_conflict",
                        "The API g_l=0.001 is retained as countervailing provider context only; its percentage basis is not supplied.",
                        inner,
                    )
                    continue
                if row.get("solution_id") == 5688:
                    sugar = self.emit(
                        ["solutions"],
                        "Sugar Stock Solution",
                        original["proposed_concentration"],
                        "DSMZ1245",
                        [stage_name, ri],
                        reason,
                        "stock_input",
                        descriptor=True,
                        snippet=snippet,
                    )
                    self.proof(
                        sugar + ["notes"],
                        None,
                        "D1245",
                        sp,
                        "evidence_only",
                        "stock_identity",
                        "The API explicitly connects this input to solution 5688. The inline original stock keeps batch masses and both maltose rows; it is not replaced by the standalone provider's declared rates.",
                    )
                    continue
                label = (
                    "Calf Serum, inactivated"
                    if label == "Fetal bovine serum"
                    else (
                        "Potassium Phosphate, dibasic"
                        if label == "Potassium Phosphate"
                        else "Soluble Starch" if label == "Starch" else label
                    )
                )
                old = self.old_pointer(label)
                withdraw = label in {"Potassium Phosphate, dibasic", "Thiamine pyrophosphate"}
                if withdraw:
                    reason += " The copied monobasic or chloride-specific annotation does not establish the source's stated form. Withdraw it without inventing a new identifier."
                if label == "Maltose":
                    reason += " Preserve this distinct literal source row. Whether the two 8 g rows are intentional is unresolved; do not sum or collapse them."
                p = self.emit(
                    parent,
                    label,
                    original["proposed_concentration"],
                    "DSMZ1245",
                    [stage_name, ri],
                    reason,
                    original["kind"],
                    old=old,
                    snippet=snippet,
                    withdraw=withdraw,
                )
                self.proof(
                    p + ["notes"],
                    None,
                    "D1245",
                    sp,
                    "evidence_only",
                    "provider_row_context",
                    "API recipe row retained as separate provenance. The original recipe's stage, input amounts, label and unresolved denominator determine this representation.",
                    p,
                )
                if label == "Calf Serum, inactivated":
                    self.note(
                        runner.get_node(self.after, p),
                        "Identity conflict: the original says inactivated calf serum; the API says Fetal bovine serum. This record retains the original label without asserting biological interchangeability.",
                    )
                    self.proof(
                        p + ["notes"],
                        old + ["notes"],
                        "D1245",
                        sp,
                        "conflict",
                        "serum_identity_conflict",
                        "Original calf serum and API fetal bovine serum are different labels; preserve the conflict explicitly.",
                        p,
                    )
        old_steps = self.before["preparation_steps"]
        steps = self.data["D1245"]["data"]["solutions"][0]["steps"]
        runner.require(
            len(old_steps) == len(steps) == 6
            and all(s["description"] == t["step"] for s, t in zip(old_steps, steps, strict=True)),
            "Preparation baseline drift",
        )
        self.after.pop("preparation_steps")
        self.note_claim(
            "Preserve source descriptive/preparation text without falsely encoding every paragraph as an instruction: "
            + "\n".join(s["step"] for s in steps),
            "D1245",
            json_excerpt(
                self.context["sources"]["D1245"]["raw"], ["data", "solutions", 0, "steps"]
            ),
            ["preparation_steps"],
            "preparation_context",
        )
        self.proof(
            ["preparation_steps"],
            ["preparation_steps"],
            "D1245",
            ["data", "solutions", 0, "steps"],
            "remove_unsupported",
            "preparation_actions",
            "The imported actions misread descriptive text as POUR_PLATES and pH measurement at 25 C as HEAT. Preserve all original descriptions in notes instead of inventing replacement procedural actions.",
        )
        self.note_claim(
            "The original states final pH 7.0 +/- 0.2 at 25 C: the range 6.8-7.2 remains, while 25 C is a measurement condition. The printed final volume 7.0 +/- 0.7 ml is retained, but cannot establish this formula's batch denominator. The API declares 1000 ml although listed liquid inputs sum to 1003.1 ml. No final-medium g/L or density conversion is inferred.",
            "DSMZ1245",
            "Final volume 7.0 ml +/- 0.7.",
        )
        self.proof(
            ["ph_range"],
            ["ph_range"],
            "DSMZ1245",
            None,
            "verified",
            "ph_context",
            "7.0 +/- 0.2 gives 6.8-7.2; 25 C is not an incubation claim.",
            snippet="Final pH 7.0 +/- 0.2 at 25 degrees C.",
        )

    def retained(self, p, row, ri):
        node = runner.get_node(self.before, p)
        entries = [e for e in node["evidence"] if e["reference"] == SOURCE_URLS[self.key]]
        runner.require(
            len(entries) == 1
            and entries[0]["snippet"] in self.texts[self.key]
            and entries[0]["supports"] == "SUPPORT",
            "Prior supported evidence drift",
        )
        decision = self.decisions[(self.key, ("data", "recipe", ri))]
        runner.require(
            node["concentration"] == decision["proposed_concentration"],
            "Prior supported rate drift",
        )
        pointer = p + ["concentration"]
        self.claims.append(
            {
                "pointer": pointer,
                "old_pointer": pointer,
                "field": runner.field_name(pointer),
                "old_field": runner.field_name(pointer),
                "ingredient": node["preferred_term"],
                "old": copy.deepcopy(node["concentration"]),
                "new": copy.deepcopy(node["concentration"]),
                "status": "verified",
                "kind": "retained_provider_stock_rate",
                "source": self.key,
                "source_pointer": ["data", "recipe", ri],
                "reference": SOURCE_URLS[self.key],
                "snippet": entries[0]["snippet"],
                "explanation": entries[0]["explanation"],
                "evidence_pointer": p,
            }
        )
        self.lineage.append(
            {
                "pointer": p,
                "old_pointer": p,
                "source": self.key,
                "source_pointer": ["data", "recipe", ri],
                "label": row["compound"],
                "kind": "retained_provider_stock_rate",
            }
        )

    def standalone(self):
        rows = self.data[self.key]["data"]["recipe"]
        old_nodes = self.before["composition"]
        runner.require(
            len(old_nodes) == (17 if self.key == "S2474" else 12), "Standalone baseline drift"
        )
        self.after["composition"] = []
        for ri, row in enumerate(rows):
            sp = ["data", "recipe", ri]
            decision = self.decisions[(self.key, tuple(sp))]
            if row.get("solution_id") == 5688:
                continue
            oi = ri if self.key == "S5688" or ri < 16 else ri - 1
            old, p = ["composition", oi], ["composition", oi]
            runner.require(
                old_nodes[oi]["preferred_term"] == row["compound"], "Standalone row order drift"
            )
            if old_nodes[oi].get("evidence"):
                self.after["composition"].append(copy.deepcopy(old_nodes[oi]))
                self.retained(p, row, ri)
            else:
                label = (
                    "Vitamin K1 (1% solution)"
                    if row["compound"] == "Vitamin K1"
                    else row["compound"]
                )
                reason = decision["reason"]
                for field in ("identity_note", "duplicate_group"):
                    if field in decision:
                        reason += " " + decision[field]
                self.emit(
                    ["composition"],
                    label,
                    decision["proposed_concentration"],
                    self.key,
                    sp,
                    reason,
                    decision["kind"],
                    old=old,
                    withdraw=row["compound"] == "Vitamin K1",
                )
            if self.key == "S5688" and row["compound"] == "Thiamine pyrophosphate":
                node = runner.get_node(self.after, p)
                runner.require(
                    node["chebi_term"]["id"] == "CHEBI:18290", "Chloride annotation drift"
                )
                node.pop("chebi_term")
                original = self.pdf_rows[("sugar_stock", ri)]
                self.proof(
                    p + ["chebi_term"],
                    p + ["chebi_term"],
                    "DSMZ1245",
                    ["sugar_stock", ri],
                    "remove_unsupported",
                    "unverified_chemical_form",
                    "The original specifies thiamine pyrophosphate without establishing a chloride salt. Withdraw only this over-specific annotation; preserve the exact earlier provider concentration and its evidence unchanged.",
                    p,
                    original["snippet"],
                )
        if self.key == "S2474":
            row = rows[16]
            p = self.emit(
                ["composition"],
                "Sugar Stock Solution",
                liters(row["amount"]),
                self.key,
                ["data", "recipe", 16],
                "Explicit 100 ml sugar-stock input = 0.1 L per preparation. This ingredient references the standalone stock; its contents are not duplicated or flattened here. This is not a universal stock working concentration.",
                "referenced_stock_input",
            )
            node = runner.get_node(self.after, p)
            node["culturemech_term"] = {
                "id": self.specs["S5688"]["id"],
                "label": "Sugar Stock Solution",
            }
            self.proof(
                p + ["culturemech_term"],
                None,
                self.key,
                ["data", "recipe", 16],
                "add",
                "stock_identity",
                "The source row explicitly identifies solution_id 5688, matching the exact standalone CultureMech record accession.",
                p,
            )
            for ri in (13, 15):
                original = self.pdf_rows[("main", ri)]
                p = ["composition", ri]
                self.proof(
                    p + ["notes"],
                    None,
                    "DSMZ1245",
                    ["main", ri],
                    "conflict",
                    "original_source_context",
                    "The original calls the vitamin stock 1% without a percentage basis and the serum inactivated calf serum. Preserve the API solution's own serum label while recording this identity disagreement; neither source authorizes an inferred mass or percentage.",
                    p,
                    original["snippet"],
                )
        else:
            for ri in (3, 4, 8):
                original = self.pdf_rows[("sugar_stock", ri)]
                p = ["composition", ri]
                self.proof(
                    p + ["notes"],
                    p + ["notes"],
                    "DSMZ1245",
                    ["sugar_stock", ri],
                    "evidence_only",
                    "original_stock_context",
                    "Original stock rows independently retain both separate 8 g maltose entries and specify soluble starch. API g/L values are provider-declared stock rates, not inferred final-medium concentrations.",
                    p,
                    original["snippet"],
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
                "All exact source rows are represented in composition, including explicit stock inputs and distinct duplicate source rows. Remove only the old placeholder and its incomplete_composition flag, not real ingredient or evidence claims.",
            )
        refs = self.after["references"]
        runner.require(
            len(refs) == 1 and refs[0]["reference"] == SOURCE_URLS[self.key],
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
            "Use the exact official source title. The prior source/accession prefix is provenance context, not part of the title.",
        )
        self.note_claim(
            "Existing explicitly qualified API rate evidence is retained, not upgraded to measured final-volume or receiving-medium concentrations. Literal liquid amounts are preparation inputs. Unresolved source percentage, serum or duplicate-row statements remain explicit; no universal stock dose or new biological growth claim is inferred.",
            self.key,
            json_excerpt(self.context["sources"][self.key]["raw"], ["data", "name"]),
        )

    def reference(self, key, relation, text):
        spec = self.specs[key]
        return {
            "id": spec["id"],
            "path": spec["path"],
            "name": runner.load_yaml(spec["before_text"])["name"],
            "relationship": relation,
            "notes": text,
        }

    def links(self):
        derived = "The KOMODO record explicitly links DSMZ1245 but retains different provider rates, nulls and stock scopes. DERIVED_FROM denotes source derivation, not exact formulation identity or biological growth."
        variant = "The exact DSM18691 variant table retains every base row and adds a separate fetal-bovine-serum 100.00 g/L provider row while calf serum 99.70 g/L remains. pH is null. Keep a strain-specific variant, not an exact duplicate, serum substitution, or new growth association."
        if self.key in {"K1245", "K1245_18691"}:
            is_base = self.key == "K1245"
            text, parent, relation = (
                (derived, "D1245", "DERIVED_FROM")
                if is_base
                else (variant, "K1245", "STRAIN_SPECIFIC_VARIANT")
            )
            self.after["parent_media"] = self.reference(parent, relation, text)
            self.after["variant_relationship"], self.after["variant_modifications"] = relation, [
                text
            ]
            for field in ("parent_media", "variant_relationship", "variant_modifications"):
                self.proof(
                    [field],
                    [field],
                    self.key,
                    None,
                    "correct",
                    "family_relationship",
                    text,
                    ["parent_media"],
                    self.metadata(self.key, "Instructions" if is_base else "Name"),
                )
        if self.key in {"D1245", "K1245"}:
            is_original = self.key == "D1245"
            child, relation, text = (
                ("K1245", "DERIVED_FROM", derived)
                if is_original
                else ("K1245_18691", "STRAIN_SPECIFIC_VARIANT", variant)
            )
            self.after["variant_children"] = [self.reference(child, relation, text)]
            self.proof(
                ["variant_children"],
                ["variant_children"],
                child,
                None,
                "correct",
                "family_relationship",
                text,
                ["variant_children", 0],
                self.metadata(child, "Instructions" if is_original else "Name"),
            )

    def archive(self):
        source = "DSMZ1245" if self.key == "D1245" else self.key
        if self.key.startswith("K"):
            quote = (
                self.texts[source]
                .split("Metabolites list", 1)[1]
                .split("Seed Metabolites list", 1)[0]
                .strip()
            )
        elif self.key.startswith("S"):
            quote = json_excerpt(self.context["sources"][source]["raw"], ["data", "recipe"])
        else:
            quote = self.texts[source].split("Formula", 1)[1].split("Final pH", 1)[0].strip()
        reason = "Complete source tables were inspected. Reconstructed ingredient/stock nodes retain source-specific amounts and uncertainties; historical flattened amounts, false supplier-tagged LB ingredients and unsupported interpretations are archived in append-only history. Existing unrelated metadata and prior evidence remain preserved, not recertified."
        for field in ("ingredients", "composition", "solutions"):
            if self.before.get(field):
                self.note_claim(reason, source, quote, [field], "prior_nodes_archived")
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
                    "The old quantity is unsupported by this complete formulation or belongs to a relocated source input. Archive it without retaining a false LB addition, placeholder, fetal/calf equivalence or flattened stock rate.",
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
        elif self.key == "D1245":
            self.original()
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
        runner.require(len({r["reference"] for r in refs}) == len(refs), "Duplicate bibliography")
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            entry = next((r for r in refs if r["reference"] == meta["url"]), None)
            if entry is None:
                entry = {"reference": meta["url"], "title": self.titles[key]}
                refs.append(entry)
            kind = (
                "culture_collection_page"
                if key == "DSMZ1245"
                else "web_page" if key.startswith("K") else "dataset"
            )
            text = f"source_type={kind}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Individual authors and publication year not supplied; copyright/access year is not publication year. Source-scoped recipe evidence, not organism growth evidence."
            entry["notes"] = (entry.get("notes", "") + "\n\n" + text).strip()
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=SOURCE_URLS[self.key],
            notes="Restore exact-source OTEB formulation and stock scopes, preserve provider rates/nulls and original source conflicts, correct input units and family links, and retain prior evidence/history. No biological growth association added.",
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
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    args = parser.parse_args()
    _, result = process(
        ROOT, args.plan, "apply" if args.apply else "verify" if args.verify else "preview"
    )
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
