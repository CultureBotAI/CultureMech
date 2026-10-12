#!/usr/bin/env python3
"""Guarded exact-source medium-436 repairs with independently reviewed evidence."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from pathlib import Path

import repair_methanogen_stock_boundaries as shared
import repair_oteb_family as prior
from bs4 import BeautifulSoup
from curation_source_fixtures import read_pdf_capture
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import html_recipe_text, parse_recipe, recipe_source
from culturemech.validation.write_validated import infer_target_class

runner, ROOT = shared.runner, shared.ROOT
PREP = ROOT / "reports/ingredient_concentration_curation/20261009-oteb-family"
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-ruminococcus-albus-family"
CONTEXT_SHA = "45d48a0e66d0504c0bea2655ea38f2a88c4c3034f8f4bd520f6e6848e22d0b55"
DECISIONS_SHA = "8995f1de0310ac60be1331140d889d69884a47989d25ebc2807d8fee616ddc05"
REVIEW_SHA = "a9f49f317be4f051f9f874d162c815d9923efb4e770f16d6fb67b03a8c021654"
ACTION = "RESTORED_RUMINOCOCCUS_ALBUS_SOURCE_FORMULATIONS_WITH_EVIDENCE"
UNCHANGED = {"DJ675", "S4674", "K3037"}
KEYS = {"K436", "K436_18848", "K3017", "D436", "M694", "M2636", "S882", "S883", "S884", "S885"}


def frozen():
    raw = (PREP / "next-436-context-approved.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Reviewed context drift")
    context = json.loads(raw)
    decisions = (PREP / "next-436-row-decisions.json").read_bytes()
    runner.require(runner.sha(decisions) == DECISIONS_SHA, "Reviewed row decisions drift")
    runner.require({r["key"] for r in context["records"]} == KEYS | UNCHANGED, "Cohort drift")
    runner.require(
        len(context["errors"]) == 1
        and context["errors"][0]["key"] == "K3037"
        and context["errors"][0]["http_status"] == 403,
        "Unreviewed access failures",
    )
    return context, json.loads(decisions)


def sources(context):
    data, texts, titles = {}, {}, {}
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        runner.require(
            meta["http_status"] == 200
            and meta["url"] == meta["response_url"]
            and runner.sha(raw.encode()) == meta["sha256"],
            "Capture drift",
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
            runner.require(len(tables) == 1, "Ambiguous KOMODO table")
            rows = [
                [html_recipe_text(str(c))[0] for c in tr.find_all("td", recursive=False)]
                for tr in tables[0].find_all("tr")
            ]
            runner.require(
                rows[0] == ["Name", "Semi unique name", "Unique Name", "Gram Amount", "Mol Amount"],
                "Provider column drift",
            )
            data[key] = rows[1:]
        elif key == "DSMZ436":
            runner.require(
                runner.sha(read_pdf_capture(meta)) == meta["pdf_sha256"],
                "Original PDF drift",
            )
        elif key != "JCM675":
            data[key] = json.loads(raw)
    return data, texts, titles


class Review(shared.Review):
    append = prior.Review.append
    claim = prior.Review.claim
    proof = prior.Review.proof
    note_claim = prior.Review.note_claim
    emit = prior.Review.emit
    metadata = prior.Review.metadata
    reference = prior.Review.reference

    def __init__(self, before, key):
        self.context, review = frozen()
        self.specs = {r["key"]: r for r in self.context["records"]}
        runner.require(key in KEYS, "Comparison or inaccessible record is not an edit target")
        spec = self.specs[key]
        runner.require(
            before == runner.load_yaml(spec["before_text"]) and before["id"] == spec["id"],
            "Unreviewed baseline",
        )
        self.target_class = infer_target_class(before)
        runner.require(not runner.errors(before, self.target_class), "Baseline schema failure")
        self.data, self.texts, self.titles = sources(self.context)
        self.decisions = {(r["source"], tuple(r["pointer"])): r for r in review["rows"]}
        self.pdf = review["original_pdf_rows"]
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.claims, self.lineage, self.used = [], [], []
        self.old = list(prior.walk(before))
        self.root_evidence = (
            ["composition", 5 if key == "S882" else 0] if key.startswith("S") else []
        )
        runner.require(
            not before.get("evidence") and not before.get("variants"), "Unreviewed provenance"
        )
        if not key.startswith("S"):
            runner.require(not before.get("references"), "Unreviewed bibliography")
            self.after["ingredients"], self.after["solutions"] = [], []

    def old_pointer(self, label):
        alias = (
            "L-Cysteine HCl x H2O"
            if label == "Cysteine-HCl x H2O" and self.key != "M2636"
            else label
        )
        candidates = [
            list(p)
            for p, n in self.old
            if len(p) >= 2
            and n["preferred_term"].casefold() == alias.casefold()
            and "LB Medium" not in n.get("supplier_catalog", {}).get("supplier_name", "")
        ]
        runner.require(len(candidates) <= 1, f"Ambiguous old ingredient: {label}")
        return candidates[0] if candidates else None

    def from_row(self, parent, source, sp, label, *, descriptor=False, old=None):
        decision = self.decisions[(source, tuple(sp))]
        row = decision["source_row"]
        reason = decision["basis"]
        if isinstance(row, dict):
            reason += f" Source input: {row.get('amount', row.get('volume'))} {row.get('unit')} at {runner.field_name(sp)}."
        else:
            reason += " Exact heading: Gram & Mol amounts are per Liter of medium."
        if decision["mode"] == "explicit_variant_supplement_rate":
            reason += (
                " Additional exact excerpt at meta.name: " + decision["additional_exact_excerpt"]
            )
        old = self.old_pointer(label) if old is None else old
        p = self.emit(
            parent,
            label,
            decision["proposed_quantity"],
            source,
            sp,
            reason,
            decision["mode"],
            old=old,
            descriptor=descriptor,
            snippet=decision["snippet"],
        )
        node = runner.get_node(self.after, p)
        if "[Merged 4 duplicates:" in node.get("notes", ""):
            node["notes"] = "Superseded flattening history, not a current amount: " + node["notes"]
        if descriptor and old:
            for field in ("term", "culturemech_term"):
                if field in runner.get_node(self.before, old):
                    self.proof(
                        p + [field],
                        old + [field],
                        source,
                        sp,
                        "remove_unsupported",
                        "stock_scope",
                        "Keep this source's inline stock. The old same-name stock link does not establish identical composition or units.",
                        snippet=decision["snippet"],
                    )
        if label == "CaCl2 x 7 H2O":
            note = "Retain the literal seven-water source label. Other sources use dihydrate or hexahydrate labels; no chemical-form equivalence or molecular weight is inferred. Existing generic calcium-chloride annotation is not hydrate-specific evidence."
            self.note(node, note)
            self.proof(
                p + ["notes"],
                None,
                source,
                sp,
                "conflict",
                "hydrate_identity",
                note,
                p,
                decision["snippet"],
            )
        if self.key == "M2636" and label == "MgSO4 x 7 H2O":
            runner.require(
                node["mediaingredientmech_chebi_term"]["id"] == "CHEBI:32599", "MIM baseline drift"
            )
            node.pop("mediaingredientmech_chebi_term")
            self.proof(
                p + ["mediaingredientmech_chebi_term"],
                old + ["mediaingredientmech_chebi_term"],
                source,
                sp,
                "remove_unsupported",
                "chemical_form",
                "The copied generic magnesium sulfate mapping does not establish this explicit heptahydrate. Preserve the existing hydrate-specific primary term; do not invent a replacement MIM linkage.",
                p,
                decision["snippet"],
            )
        return p

    def komodo(self):
        for i, row in enumerate(self.data[self.key]):
            self.from_row(["ingredients"], self.key, ["Metabolites list", i], row[0])
        ph = self.metadata(self.key, "PH Info")
        if self.key == "K436_18848":
            runner.require(
                ph == "PH Info: null" and self.before["ph_value"] == 7, "Variant pH drift"
            )
            self.after.pop("ph_value")
            self.proof(
                ["ph_value"],
                ["ph_value"],
                self.key,
                None,
                "remove_unsupported",
                "variant_ph",
                "The variant's pH is null; withdraw the copied base pH without substituting a value.",
                snippet=ph,
            )
        elif self.key == "K436":
            runner.require(ph == "PH Info: 7.0" and self.after["ph_value"] == 7, "Base pH drift")
        if self.key == "K3017":
            self.after["notes"] = (
                "KOMODO accession 3017 names Fatty acid mixture (medium 436), but its Instructions link points to DSMZ3017. That conflicting DSMZ/MediaDive3017 equivalence is unverified and is withdrawn from the formulation assertion. All four displayed Gram Amounts are null; identities are restored without copying numerical doses from another provider. Keep its legacy MediaRecipe shape and record_kind SOLUTION."
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
                ["notes"],
                ["notes"],
                self.key,
                None,
                "conflict",
                "source_accession_conflict",
                "The provider Instructions URL itself conflicts with the medium436 stock name. No independent DSMZ3017 equivalence has been established.",
                snippet=self.metadata(self.key, "Instructions"),
            )
        self.note_claim(
            "KOMODO displayed Gram Amounts and nulls are source-specific assertions. Rounded molar columns and aggregated SEED entries are not ingredient evidence. No organism-growth association is inferred.",
            self.key,
            "Gram & Mol amounts are per Liter of medium.",
        )

    def original(self):
        stocks = {}
        api = self.data["D436"]["data"]["solutions"]
        runner.require([s["id"] for s in api] == [882, 883, 884, 885], "Original stage drift")
        offsets = [0, 11, 12, 17]
        for si, stage in enumerate(api):
            parent = ["ingredients"] if si == 0 else stocks[stage["name"]] + ["composition"]
            for ri, row in enumerate(stage["recipe"]):
                source_row = self.pdf[offsets[si] + ri]
                label = source_row["ingredient"]
                expected = row.get("compound", row.get("solution"))
                runner.require(
                    label == expected
                    or (label, expected) == ("Cysteine-HCl x H2O", "L-Cysteine HCl x H2O"),
                    "Original label drift",
                )
                runner.require(
                    float(source_row["source_amount"]) == row["amount"]
                    and source_row["source_unit"] == row["unit"],
                    "Original input drift",
                )
                descriptor = "solution_id" in row
                reason = f"Original {source_row['stage']} input: {source_row['source_amount']} {source_row['source_unit']} per preparation. {source_row['basis']}"
                p = self.emit(
                    ["solutions"] if descriptor else parent,
                    label,
                    source_row["proposed_quantity"],
                    "DSMZ436",
                    ["page 1", source_row["stage"], ri],
                    reason,
                    source_row["mode"],
                    old=self.old_pointer(label),
                    descriptor=descriptor,
                    snippet=source_row["exact_extracted_line"].strip(),
                )
                self.proof(
                    p + ["notes"],
                    None,
                    "D436",
                    ["data", "solutions", si, "recipe", ri],
                    "evidence_only",
                    "provider_context",
                    "The API row corroborates identity and input. Its g_l and mmol_l values do not resolve the original's final-volume or percent basis.",
                    [] if descriptor else p,
                )
                if descriptor:
                    stocks[label] = p
        steps = self.before["preparation_steps"]
        runner.require(
            len(steps) == 3 and steps[-1]["action"] == "HEAT", "Preparation baseline drift"
        )
        self.after.pop("preparation_steps")
        self.note_claim(
            "Preserve original preparation descriptions, but withdraw the incorrect HEAT encoding of incubation: "
            + "\n".join(s["description"] for s in steps),
            "D436",
            json_excerpt(self.context["sources"]["D436"]["raw"], ["data", "solutions"]),
            ["preparation_steps"],
            "preparation_scope",
        )
        self.proof(
            ["preparation_steps"],
            ["preparation_steps"],
            "D436",
            ["data", "solutions"],
            "remove_unsupported",
            "preparation_actions",
            "Retain all descriptions in notes. Incubation at 37 C belongs to inoculated medium, not heating the fatty-acid stock.",
        )
        self.note_claim(
            "The original supplies 920 ml water, two 40 ml mineral inputs and a separate 1 ml acid input. Their sum is not an explicit final volume. Literal mineral percentages have no declared basis; no g/L or molarity is inferred.",
            "DSMZ436",
            self.context["sources"]["DSMZ436"]["raw"].split("Inoculate", 1)[0].strip(),
        )

    def togo(self):
        payload = self.data[self.key]
        stocks = {}
        names = {"Mineral solution 1", "Mineral solution 2", "Fatty acid mixture"}
        for si, stage in enumerate(payload["components"]):
            stock_name = stage["subcomponent_name"]
            parent = (
                stocks[stock_name] + ["composition"] if stock_name in names else ["ingredients"]
            )
            for ri, row in enumerate(stage["items"]):
                label = row["component_name"]
                descriptor = row.get("reference_media_id") == self.key
                p = self.from_row(
                    ["solutions"] if descriptor else parent,
                    self.key,
                    ["components", si, "items", ri],
                    label,
                    descriptor=descriptor,
                )
                if descriptor:
                    name = label.replace(" (see below)", "")
                    stocks[name[0].upper() + name[1:]] = p
        runner.require(set(stocks) == names, "Missing source stock boundary")
        self.note_claim(
            "Preparation order is preserved as source text; provider paragraph grouping does not make all inputs simultaneous: "
            + "\n".join(c["comment"] for c in payload["comments"] if c["comment"]),
            self.key,
            json_excerpt(self.context["sources"][self.key]["raw"], ["comments"]),
        )
        if self.key == "M2636":
            p = stocks["Mineral solution 2"]
            self.note(
                runner.get_node(self.after, p),
                "The old solution4674 reference described a different formula (dibasic phosphate, different salts and hydrate). This source's inline percent-labelled stock supersedes that link; no same-name substitution is permitted.",
            )
            self.proof(
                p + ["notes"],
                None,
                "S4674",
                ["data", "recipe"],
                "conflict",
                "different_stock",
                "Comparison stock4674 has K2HPO4 and different amounts, not this source's KH2PO4 stock. Its existing supported quantities must not be changed to fit this medium.",
            )
        original = "JCM675" if self.key == "M694" else "DSMZ436"
        self.note_claim(
            "Original-source cross-check retains source-specific preparation stages and calcium hydrate labels. Similar names do not establish exact equivalence, percentage basis or a final-volume denominator.",
            original,
            self.texts[original].strip(),
        )

    def standalone(self):
        rows = self.data[self.key]["data"]["recipe"]
        old_nodes = self.before["composition"]
        self.after["composition"] = []
        # Append missing stock inputs after existing nodes to preserve prior evidence paths.
        ordinary = [(i, r) for i, r in enumerate(rows) if not r.get("solution_id")]
        runner.require(len(ordinary) == len(old_nodes), "Standalone node count drift")
        for oi, (ri, row) in enumerate(ordinary):
            p = ["composition", oi]
            runner.require(
                old_nodes[oi]["preferred_term"] == row["compound"], "Standalone identity drift"
            )
            if old_nodes[oi].get("evidence"):
                node = copy.deepcopy(old_nodes[oi])
                decision = self.decisions[(self.key, ("data", "recipe", ri))]
                runner.require(
                    node["concentration"] == decision["proposed_quantity"], "Prior quantity drift"
                )
                self.after["composition"].append(node)
                entry = node["evidence"][0]
                runner.require(
                    entry["snippet"] in self.texts[self.key] and len(node["evidence"]) == 1,
                    "Prior evidence drift",
                )
                self.claims.append(
                    {
                        "pointer": p + ["concentration"],
                        "old_pointer": p + ["concentration"],
                        "field": runner.field_name(p + ["concentration"]),
                        "old_field": runner.field_name(p + ["concentration"]),
                        "ingredient": node["preferred_term"],
                        "old": copy.deepcopy(node["concentration"]),
                        "new": copy.deepcopy(node["concentration"]),
                        "status": "verified",
                        "kind": "retained_provider_rate",
                        "source": self.key,
                        "source_pointer": ["data", "recipe", ri],
                        "reference": entry["reference"],
                        "snippet": entry["snippet"],
                        "explanation": entry["explanation"],
                        "evidence_pointer": p,
                    }
                )
                self.lineage.append(
                    {
                        "pointer": p,
                        "old_pointer": p,
                        "source": self.key,
                        "source_pointer": ["data", "recipe", ri],
                        "label": node["preferred_term"],
                        "kind": "retained_provider_rate",
                    }
                )
            else:
                self.from_row(
                    ["composition"], self.key, ["data", "recipe", ri], row["compound"], old=p
                )
        for ri, row in enumerate(rows):
            if not row.get("solution_id"):
                continue
            p = self.from_row(["composition"], self.key, ["data", "recipe", ri], row["solution"])
            spec = self.specs["S" + str(row["solution_id"])]
            runner.get_node(self.after, p)["culturemech_term"] = {
                "id": spec["id"],
                "label": row["solution"],
            }
            self.proof(
                p + ["culturemech_term"],
                None,
                self.key,
                ["data", "recipe", ri],
                "add",
                "stock_identity",
                "The source explicitly names this solution_id. This is a batch input, not a universal stock working concentration.",
                p,
            )
        self.after.pop("ingredients")
        flags = [f for f in self.before["data_quality_flags"] if f != "incomplete_composition"]
        if flags:
            self.after["data_quality_flags"] = flags
        else:
            self.after.pop("data_quality_flags")
        for field in ("ingredients", "data_quality_flags"):
            self.proof(
                [field],
                [field],
                self.key,
                ["data", "recipe"],
                "remove_unsupported",
                "legacy_placeholder",
                "Every exact recipe row is represented in composition. Remove the false placeholder and only its incomplete-composition flag; unresolved scientific bases remain explicit.",
            )
        if self.before.get("references"):
            self.after["references"][0]["title"] = self.titles[self.key]
            self.proof(
                ["references", 0, "title"],
                ["references", 0, "title"],
                self.key,
                ["data", "name"],
                "correct",
                "bibliographic_title",
                "Use the actual source title, with accession and discovery metadata in notes.",
            )
        if self.key == "S885":
            old = self.before["preparation_notes"]
            self.after["preparation_notes"] = (
                "Provider-declared stock volume: 100 ml, not proof of final volume. Imported receiving-medium context, not a stock preparation instruction: "
                + old
            )
            self.proof(
                ["preparation_notes"],
                ["preparation_notes"],
                self.key,
                ["data", "steps"],
                "correct",
                "preparation_scope",
                "Inoculation and 37 C incubation describe the receiving medium, not preparing this stock.",
            )
            self.proof(
                ["preparation_notes"],
                ["preparation_notes"],
                "DSMZ436",
                None,
                "evidence_only",
                "original_preparation_scope",
                "The original locates this sentence after the complete medium and stocks; preserve it as receiving-medium context.",
                snippet=next(
                    line.strip()
                    for line in self.texts["DSMZ436"].splitlines()
                    if line.startswith("Inoculate")
                ),
            )

    def links(self):
        derived = "KOMODO explicitly derives from DSMZ436 but has different displayed rates, nulls and stock scopes. DERIVED_FROM does not assert exact composition or biological equivalence."
        variant = "The exact DSM18848 variant retains the base provider rows and adds maltose and starch, each 1.00 g/L. Variant pH is null. Keep a strain-specific formulation, not an exact duplicate or a new growth association."
        if self.key in {"K436", "K436_18848"}:
            base = self.key == "K436"
            parent, relation, reason = (
                ("D436", "DERIVED_FROM", derived)
                if base
                else ("K436", "STRAIN_SPECIFIC_VARIANT", variant)
            )
            self.after["parent_media"] = self.reference(parent, relation, reason)
            self.after["variant_relationship"], self.after["variant_modifications"] = relation, [
                reason
            ]
            for field in ("parent_media", "variant_relationship", "variant_modifications"):
                self.proof(
                    [field],
                    [field],
                    self.key,
                    None,
                    "correct",
                    "family_relationship",
                    reason,
                    ["parent_media"],
                    self.metadata(self.key, "Instructions" if base else "Name"),
                )
        if self.key in {"D436", "K436"}:
            original = self.key == "D436"
            child, relation, reason = (
                ("K436", "DERIVED_FROM", derived)
                if original
                else ("K436_18848", "STRAIN_SPECIFIC_VARIANT", variant)
            )
            self.after["variant_children"] = [self.reference(child, relation, reason)]
            self.proof(
                ["variant_children"],
                ["variant_children"],
                child,
                None,
                "correct",
                "family_relationship",
                reason,
                ["variant_children", 0],
                self.metadata(child, "Instructions" if original else "Name"),
            )

    def archive(self):
        if self.key.startswith("K"):
            source = self.key
            snippet = (
                self.texts[source]
                .split("Metabolites list", 1)[1]
                .split("Seed Metabolites list", 1)[0]
                .strip()
            )
        elif self.key == "D436":
            source, snippet = "DSMZ436", self.context["sources"]["DSMZ436"]["raw"].strip()
        else:
            source = self.key
            snippet = json_excerpt(
                self.context["sources"][source]["raw"],
                ["data", "recipe"] if source.startswith("S") else ["components"],
            )
        for field in ("ingredients", "composition", "solutions"):
            if self.before.get(field):
                self.note_claim(
                    "Complete source rows determine the reconstructed formulation. Archive the prior flattened nodes, unsupported LB additions and stock links in append-only history. Unrelated annotations are preserved, not recertified.",
                    source,
                    snippet,
                    [field],
                    "prior_nodes_archived",
                )
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
                    "This old amount belongs to an unsupported LB addition, placeholder, or relocated source stage. Archive it without retaining a false concentration.",
                    snippet=snippet,
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
        elif self.key.startswith("M"):
            self.togo()
        elif self.key.startswith("S"):
            self.standalone()
        else:
            self.original()
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
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            entry = next((r for r in refs if r["reference"] == meta["url"]), None)
            if entry is None:
                entry = {"reference": meta["url"], "title": self.titles[key]}
                refs.append(entry)
            kind = (
                "culture_collection_page"
                if key in {"DSMZ436", "JCM675"}
                else "web_page" if key.startswith("K") else "dataset"
            )
            note = f"source_type={kind}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Individual authors and publication year not supplied. Copyright/access years are not publication years. Source-scoped ingredient evidence, not organism-growth evidence."
            entry["notes"] = (entry.get("notes", "") + "\n\n" + note).strip()
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restore exact-source medium436 formulation, preparation stages and input units. Preserve qualified prior rates, source-specific nulls and unresolved original bases. No growth association added.",
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
        runner.require(infer_target_class(self.after) == self.target_class, "Target shape changed")
        errors = runner.errors(self.after, self.target_class)
        runner.require(not errors, f"Proposed schema failure: {errors}")
        return self.after, self.claims, self.lineage


def build(before, key, timestamp):
    review = Review(before, key)
    review.formulate()
    return review.finish(timestamp)


def process(root, plan_path, mode="preview"):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    runner.require(not plan_path.is_symlink(), "Plan symlink")
    if mode != "preview":
        reviewed = (HERE / "validation-preview.json").read_bytes()
        runner.require(runner.sha(reviewed) == REVIEW_SHA, "Independent review receipt drift")
        gate = json.loads(reviewed)
        runner.require(
            gate["terminal"]
            and gate["plan_sha256"] == runner.sha(plan_path.read_bytes())
            and gate["context_sha256"] == CONTEXT_SHA
            and gate["records_proposed"] == len(KEYS),
            "Unreviewed plan",
        )
    context, _ = frozen()
    for spec in context["records"]:
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Cohort symlink")
        if mode == "preview" or spec["key"] in UNCHANGED:
            runner.require(
                runner.sha(path.read_bytes()) == spec["before_sha256"], "Cohort baseline drift"
            )
    context["records"] = [r for r in context["records"] if r["key"] in KEYS]
    return shared.process(
        root,
        plan_path,
        mode,
        context=context,
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
    HERE.mkdir(exist_ok=True)
    _, result = process(
        ROOT, args.plan, "apply" if args.apply else "verify" if args.verify else "preview"
    )
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
