#!/usr/bin/env python3
"""Curate evidence-backed medium212 formulations without flattening stock stages."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from dataclasses import asdict
from decimal import Decimal
from pathlib import Path

import repair_methanogen_stock_boundaries as shared
import repair_oteb_family as prior
from curation_source_fixtures import read_pdf_capture
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event
from culturemech.ingredients.mim_label_index import MIMLabelIndex
from culturemech.validation.recipe_references import html_recipe_text, parse_recipe, recipe_source
from culturemech.validation.write_validated import infer_target_class

runner, ROOT = shared.runner, shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-synthrophomonas-family"
CONTEXT_SHA = "1d9b09a2915e57c4f212f1de08bb1a5ada6b2a4b8a47b6b6c5d528d00250e84a"
DECISIONS_SHA = "46a114cb7ba3eadc3881beb1d8d21fed76f457e8c1ed3d366893184f59df74ba"
IDENTITY_SHA = "2f6d107a2c1042092e4402085f5941f969e5aa2a601f4a77b79747c93d5cc6b2"
INDEX_COMPATIBILITY_SHA = "0eb9392564e995e49b2c79a78e9db8b36ab93b7a6172abd22352cef0aa7231fa"
REVIEW_SHA = "e0f27faf288e9d48aa44560169c45b46beae1856782c9a5aca7f3af77ee36eb8"
PLAN_PATH = HERE / "plan-v2.json"
ACTION = "RESTORED_SYNTHROPHOMONAS_SOURCE_FORMULATIONS_WITH_EVIDENCE"
KEYS = {
    "K212",
    "B2805",
    "D212",
    "D212a",
    "S1038",
    "S125",
    "S1728",
    "S446",
    "S447",
    "S448",
    "S450",
    "S451",
    "S453",
    "S454",
    "S455",
    "S456",
    "S459",
    "S460",
    "S461",
    "S595",
    "S608",
    "S777",
}
PDF_ALIASES = {
    "Trypticase peptone (BD BBL)": "Trypticase peptone",
    "Sodium resazurin (0.1% w/v)": "Sodium resazurin",
    "HCl (25%)": "HCl",
    "Ethanol (95 %)": "Ethanol",
    "Starch (soluble)": "Starch",
    "DL-Dithiothreitol (DTT)": "DL-Dithiothreitol",
}
KOMODO_ALIASES = {
    "Pyridoxine-HCl": "Pyridoxine hydrochloride",
    "Cysteine-HCl x H2O": "L-Cysteine HCl x H2O",
    "Resazurin": "Sodium resazurin",
    "Trypticase": "Trypticase peptone",
}


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Context drift")
    context = json.loads(raw)
    runner.require(context["terminal"] and not context["errors"], "Incomplete captures")
    runner.require({r["key"] for r in context["records"]} == KEYS, "Cohort drift")
    raw = (HERE / "source-review.json").read_bytes()
    runner.require(runner.sha(raw) == DECISIONS_SHA, "Source decision drift")
    decisions = json.loads(raw)
    runner.require(decisions["context_sha256"] == CONTEXT_SHA, "Decision context drift")
    identity_review()
    return context, decisions


def identity_review():
    raw = (HERE / "identity-review.json").read_bytes()
    runner.require(runner.sha(raw) == IDENTITY_SHA, "Identity disposition drift")
    reviewed = json.loads(raw)
    runner.require(reviewed["context_sha256"] == CONTEXT_SHA, "Identity context drift")
    index_raw = (ROOT / "src/culturemech/data/mediaingredientmech/label_index.csv").read_bytes()
    if runner.sha(index_raw) != reviewed["mim_metadata"]["sha256"]:
        raw = (HERE / "identity-index-compatibility.json").read_bytes()
        runner.require(runner.sha(raw) == INDEX_COMPATIBILITY_SHA, "Index compatibility drift")
        successor = json.loads(raw)
        runner.require(
            successor["historical_identity_review_sha256"] == IDENTITY_SHA
            and successor["historical_index_sha256"] == reviewed["mim_metadata"]["sha256"]
            and runner.sha(index_raw) == successor["current_metadata"]["sha256"],
            "Identity index drift",
        )
        index = MIMLabelIndex.from_csv_bytes(
            index_raw, metadata=successor["current_metadata"], verify_metadata=True
        )
        runner.require(
            asdict(index.resolve_label(reviewed["mim_resolution"]["query_label"]))
            == successor["current_resolution"],
            "Identity resolution drift",
        )
    return reviewed


def sources(context):
    texts, titles, data = {}, {}, {}
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        runner.require(
            meta["http_status"] == 200
            and meta["url"] == meta["response_url"]
            and runner.sha(raw.encode()) == meta["sha256"],
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        adapter = recipe_source(meta["url"])
        if adapter:
            parsed = parse_recipe(adapter, raw, meta)
            texts[key], titles[key] = parsed.content, parsed.title
        else:
            texts[key], titles[key] = html_recipe_text(raw)
        if meta.get("pdf_path"):
            runner.require(
                runner.sha(read_pdf_capture(meta)) == meta["pdf_sha256"],
                "PDF drift",
            )
        if key.startswith("S") or key in {"D212", "D212a"}:
            data[key] = json.loads(raw)["data"]
    return data, texts, titles


class Review(shared.Review):
    append = prior.Review.append
    claim = prior.Review.claim
    proof = prior.Review.proof
    note_claim = prior.Review.note_claim
    metadata = prior.Review.metadata
    reference = prior.Review.reference

    def __init__(self, before, key):
        self.context, reviewed = frozen()
        self.specs = {r["key"]: r for r in self.context["records"]}
        runner.require(key in KEYS, "Unreviewed target")
        spec = self.specs[key]
        runner.require(
            before == runner.load_yaml(spec["before_text"]) and before["id"] == spec["id"],
            "Unreviewed baseline",
        )
        self.target_class = infer_target_class(before)
        runner.require(not runner.errors(before, self.target_class), "Baseline schema failure")
        self.data, self.texts, self.titles = sources(self.context)
        self.rows = reviewed["source_quantity_decisions"]
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.old = list(prior.walk(before))
        self.claims, self.lineage, self.used = [], [], []
        self.root_evidence = ["composition", 0] if key.startswith("S") else []
        runner.require(
            not before.get("evidence") and not before.get("variants"), "Unreviewed provenance"
        )
        if not key.startswith("S"):
            self.after["ingredients"], self.after["solutions"] = [], []

    def old_pointer(self, label):
        aliases = KOMODO_ALIASES if self.key == "K212" else PDF_ALIASES
        alias = aliases.get(label, label)
        matches = [
            list(p)
            for p, n in self.old
            if len(p) >= 2
            and n["preferred_term"].casefold() == alias.casefold()
            and "LB Medium" not in n.get("supplier_catalog", {}).get("supplier_name", "")
        ]
        runner.require(len(matches) <= 1, f"Ambiguous old ingredient: {label}")
        return matches[0] if matches else None

    def row(self, parent, decision, *, old=None, descriptor=False):
        label, source = decision["label"], decision["source"]
        old = self.old_pointer(label) if old is None else old
        reason = decision["basis"]
        if decision.get("source_amount") is not None:
            reason += f" Exact batch input: {decision['source_amount']} {decision['source_unit']}; stage={decision['stage']}."
        elif isinstance(decision.get("source_row"), dict):
            r = decision["source_row"]
            reason += f" Source input: {r['amount']} {r['unit']}; stage={decision['stage']}."
        if decision.get("additional_exact_excerpt"):
            excerpt = decision["additional_exact_excerpt"]
            runner.require(excerpt in self.texts[source], "Secondary excerpt drift")
            reason += " Additional exact source excerpt: " + excerpt
        if decision.get("calculation"):
            reason += " Calculation: " + decision["calculation"]
        start = len(self.claims)
        p = prior.Review.emit(
            self,
            parent,
            label,
            decision["proposed_quantity"],
            source,
            decision["pointer"],
            reason,
            decision["mode"],
            old=old,
            descriptor=descriptor,
            snippet=decision["snippet"],
        )
        for claim in self.claims[start:]:
            if claim["old_pointer"] and claim["old"] == claim["new"]:
                claim["status"] = "evidence_only"
            if claim["pointer"][-1] == "concentration" and claim["new"] is None:
                claim["status"] = (
                    "remove_unsupported"
                    if claim["old"] is not None
                    else (
                        "unsupported"
                        if decision["mode"] == "batch_mass_without_final_volume"
                        else "not_quantified"
                    )
                )
        node = runner.get_node(self.after, p)
        if "[Merged" in node.get("notes", ""):
            node["notes"] = "Superseded flattening history, not a current amount: " + node["notes"]
        self.lineage[-1]["source_row_id"] = decision["row_id"]
        return p

    def retained(self, pointer, decision):
        node = copy.deepcopy(runner.get_node(self.before, pointer))
        runner.require(
            node["preferred_term"] == decision["label"]
            and node["concentration"] == decision["proposed_quantity"],
            "Retained quantity drift",
        )
        runner.require(node.get("evidence"), "Missing retained evidence")
        for evidence in node["evidence"]:
            runner.require(
                evidence["reference"] == decision["reference"]
                and evidence.get("snippet") in self.texts[self.key],
                "Retained source drift",
            )
        p = self.append(["composition"], node)
        runner.require(p == pointer, "Retained path moved")
        self.claim(
            p + ["concentration"],
            pointer + ["concentration"],
            self.key,
            decision["pointer"],
            "verified",
            decision["mode"],
            decision["basis"],
            None,
            decision["snippet"],
        )
        self.lineage.append(
            {
                "pointer": p,
                "old_pointer": pointer,
                "source": self.key,
                "source_pointer": decision["pointer"],
                "source_row_id": decision["row_id"],
                "label": decision["label"],
                "kind": decision["mode"],
            }
        )

    def direct(self):
        for row in self.rows:
            if row["source"] == self.key:
                self.row(["ingredients"], row)
        if self.key == "K212":
            self.note_claim(
                "Restore this provider's 32 rows and four explicit nulls. Values such as clarified rumen fluid in g/L are provider assertions, not density conversions. Missing and null values are not zero. Preserve separate DSMZ and BacDive formulations; no new growth assertion.",
                self.key,
                "Gram & Mol amounts are per Liter of medium.",
            )
            self.note_claim(
                "KOMODO's aerobic flag is provider metadata, not verified cultivation guidance. The linked DSMZ original describes anoxic preparation; retain this source disagreement without changing unrelated growth annotations.",
                self.key,
                self.metadata(self.key, "Is Aerobic"),
            )
        else:
            self.note_claim(
                "All 32 rates are the exact BacDive strain-specific provider values, not independently recomputed final concentrations from DSMZ instructions. Distilled water is listed without a number. Existing growth assertions are preserved, not newly verified by these quantity claims. The DOI redirect was located but its versioned PDF was not inspected; evidence cites the captured strain-page PURL only.",
                self.key,
                "SYNTHROPHOMONAS MEDIUM (DSMZ Medium 212; with strain-specific modifications)",
            )

    def original(self):
        source = "DSMZ" + self.key[1:]
        rows = [r for r in self.rows if r["source"] == source]
        graph = self.data[self.key]["solutions"]
        by_id = {s["id"]: (i, s) for i, s in enumerate(graph)}
        used = set()

        def stage(stock_id, parent, ancestors=()):
            runner.require(stock_id not in ancestors, "Cyclic source stock")
            _, payload = by_id[stock_id]
            name = "main assembly" if stock_id == graph[0]["id"] else payload["name"]
            selected = [r for r in rows if r["stage"] == name]
            runner.require(len(selected) == len(payload["recipe"]), "Stage row count drift")
            for decision, entry in zip(selected, payload["recipe"], strict=True):
                label = entry.get("compound") or entry.get("solution")
                runner.require(
                    PDF_ALIASES.get(decision["label"], decision["label"]) == label
                    and Decimal(decision["source_amount"]) == Decimal(str(entry["amount"]))
                    and decision["source_unit"] == entry["unit"],
                    "PDF/API stage disagreement",
                )
                runner.require(decision["row_id"] not in used, "Repeated source stage")
                used.add(decision["row_id"])
                descriptor = entry.get("solution_id") is not None
                field = "solutions" if descriptor else "composition"
                runner.get_node(self.after, parent).setdefault(field, [])
                p = self.row(parent + [field], decision, descriptor=descriptor)
                if descriptor:
                    child = entry["solution_id"]
                    if by_id[child][1].get("recipe"):
                        stage(child, p, ancestors + (stock_id,))
                    else:
                        runner.require(child == 2618, "Unexpected empty preparation")
                        node = runner.get_node(self.after, p)
                        node.pop("composition")
                        snippet = (
                            self.context["sources"][source]["raw"]
                            .split("Clarified rumen fluid (from medium 1310)", 1)[1]
                            .split("\n\n", 1)[0]
                            .strip()
                        )
                        self.note(
                            node,
                            "Procedure-only preparation; no ingredient masses are supplied. The 30% vial fill is a storage instruction, not medium concentration. "
                            + snippet,
                        )
                        self.proof(
                            p + ["notes"],
                            None,
                            source,
                            ["clarified-fluid procedure"],
                            "evidence_only",
                            "procedure_only_stock",
                            "Preserve the original procedure without inventing ingredient quantities or a stock identity.",
                            snippet=snippet,
                        )
                    node = runner.get_node(self.after, p)
                    if node.get("composition") == []:
                        node.pop("composition")

        stage(graph[0]["id"], [])
        runner.require(used == {r["row_id"] for r in rows}, "Unrepresented PDF row")
        assembly = [r for r in rows if r["stage"] == "main assembly"]
        nominal = sum(Decimal(r["source_amount"]) for r in assembly)
        a = [r for r in rows if r["stage"] == "Solution A" and r["source_unit"] == "ml"]
        liquid_sum = sum(Decimal(r["source_amount"]) for r in a)
        self.note_claim(
            f"The listed main-stage doses sum to {nominal} ml; this is not an explicit final-volume instruction. Solution A is listed as {assembly[0]['source_amount']} ml while its liquid inputs sum to {liquid_sum} ml. Preserve the discrepancy; no additive-volume or density assumption establishes final concentrations. Only SL-10 has an explicit 1000 ml make-up statement. Other original batch masses remain in ingredient notes, not invented g/L fields.",
            source,
            "\n".join(
                self.context["sources"][source]["raw"].splitlines()[3 : 3 + len(assembly)]
            ).strip(),
        )
        self.note_claim(
            "Keep the base formulation distinct from the separately labeled strain modifications and semi-solid shipping instructions. Retained preparation steps include stock procedures; their storage fill fractions and working doses are not base-medium concentrations.",
            source,
            "For DSM 2805:" if self.key == "D212" else "For DSM 103462:",
        )

    def standalone(self):
        rows = [r for r in self.rows if r["source"] == self.key]
        self.after["composition"] = []
        ordinary = [r for r in rows if not r["source_row"].get("solution_id")]
        runner.require(len(ordinary) == len(self.before["composition"]), "Stock node drift")
        for i, decision in enumerate(ordinary):
            p = ["composition", i]
            node = self.before["composition"][i]
            runner.require(node["preferred_term"] == decision["label"], "Stock ingredient drift")
            if node.get("evidence"):
                self.retained(p, decision)
            else:
                self.row(["composition"], decision, old=p)
        if self.key == "S608":
            runner.require(self.after == self.before, "Reviewed no-op drift")
            return
        for decision in rows:
            entry = decision["source_row"]
            if not entry.get("solution_id"):
                continue
            p = self.row(["composition"], decision)
            target = decision["exact_stock_record"]
            if target:
                runner.require(
                    target
                    == {k: self.specs["S" + str(entry["solution_id"])][k] for k in ("path", "id")},
                    "Stock identity drift",
                )
                runner.get_node(self.after, p)["culturemech_term"] = {
                    "id": target["id"],
                    "label": decision["label"],
                }
                self.proof(
                    p + ["culturemech_term"],
                    None,
                    self.key,
                    decision["pointer"],
                    "add",
                    "stock_identity",
                    "Exact upstream accession maps to this existing normalized stock record. This is a preparation input, not a universal working dose.",
                    p,
                    decision["snippet"],
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
                "Every exact source row is represented in composition. Remove only the false composition placeholder and its incomplete-composition flag; this is not chemical-identity or measured-volume certification.",
            )
        if self.before.get("references"):
            runner.require(
                self.after["references"][0]["reference"]
                == self.context["sources"][self.key]["metadata"]["url"],
                "Bibliography identity drift",
            )
            self.after["references"][0]["title"] = self.titles[self.key]
            self.proof(
                ["references", 0, "title"],
                ["references", 0, "title"],
                self.key,
                ["data", "name"],
                "correct",
                "bibliographic_title",
                "Use the exact source title; preserve accession and retrieval provenance in reference notes.",
            )

    def links(self):
        if self.key not in {"K212", "D212", "D212a"}:
            return
        snippet = self.metadata("K212", "Instructions")
        reason = "KOMODO explicitly links DSMZ212, but its displayed formulation is distinct from both DSMZ212 and DSMZ212a. Remove the false K212/DSMZ212a duplicate edge. DERIVED_FROM records source provenance, not exact composition or biological equivalence. Preserve the separate DSM2805 strain-variant evidence."
        if self.key == "K212":
            self.after.pop("variant_children")
            self.proof(
                ["variant_children"],
                ["variant_children"],
                "K212",
                None,
                "remove_unsupported",
                "family_relationship",
                reason,
                snippet=snippet,
            )
            self.after["parent_media"] = self.reference("D212", "DERIVED_FROM", reason)
            self.after["variant_relationship"], self.after["variant_modifications"] = (
                "DERIVED_FROM",
                [reason],
            )
            for field in ("parent_media", "variant_relationship", "variant_modifications"):
                self.proof(
                    [field],
                    [field],
                    "K212",
                    None,
                    "add",
                    "family_relationship",
                    reason,
                    ["parent_media"],
                    snippet,
                )
        elif self.key == "D212":
            self.after["variant_children"].append(self.reference("K212", "DERIVED_FROM", reason))
            self.proof(
                ["variant_children"],
                ["variant_children"],
                "K212",
                None,
                "correct",
                "family_relationship",
                reason,
                ["variant_children", 1],
                snippet,
            )
        else:
            for field in ("parent_media", "variant_relationship", "variant_modifications"):
                self.after.pop(field)
                self.proof(
                    [field],
                    [field],
                    "K212",
                    None,
                    "remove_unsupported",
                    "family_relationship",
                    reason,
                    snippet=snippet,
                )
            self.note_claim(
                "DSMZ212a is retained as its own source formulation. No new parent relation is inferred from a similar name or accession suffix.",
                "DSMZ212a",
                self.titles["DSMZ212a"],
            )

    def archive(self):
        if self.key in {"K212", "B2805"}:
            source = self.key
            if self.key == "K212":
                snippet = (
                    self.texts[source]
                    .split("Metabolites list", 1)[1]
                    .split("Seed Metabolites list", 1)[0]
                    .strip()
                )
            else:
                snippet = (
                    "SYNTHROPHOMONAS MEDIUM (DSMZ Medium 212; with strain-specific modifications)"
                )
        elif self.key.startswith("S"):
            source = self.key
            snippet = json_excerpt(self.context["sources"][source]["raw"], ["data", "recipe"])
        else:
            source = "DSMZ" + self.key[1:]
            snippet = self.context["sources"][source]["raw"].strip()
        for field in ("ingredients", "composition", "solutions"):
            if self.before.get(field):
                self.note_claim(
                    "Archive the previous formulation nodes in append-only history. The inspected complete source defines this reconstruction, including removal of false LB expansion, placeholders and flattened stock quantities. Prior evidence content is preserved; same-reference explanations may be extended, never replaced.",
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
                    "The complete source does not support this old copied ingredient, placeholder or flattened stock amount in the current formulation. Preserve its exact prior value in history.",
                    snippet=snippet,
                )
                self.claims[-1]["ingredient"] = node["preferred_term"]
        if self.key in {"K212", "D212", "D212a"}:
            runner.require(self.after.pop("high_metal") is True, "Metal flag drift")
            self.proof(
                ["high_metal"],
                ["high_metal"],
                source,
                None,
                "remove_unsupported",
                "derived_quantity_flag",
                "Withdraw the unexplained >=1049.84 mM high-metal classification after replacing copied and flattened stock quantities. Its required final-medium molar total has not been established. This does not assert low metal or replace the flag with false.",
                snippet=snippet,
            )

    def withdraw_nickel(self):
        reviewed = identity_review()
        issues = [i for i in reviewed["issues"] if i["key"] == self.key]
        if not issues:
            return
        (issue,) = issues
        (decision,) = [r for r in self.rows if r["row_id"] == issue["source_row_id"]]
        (lineage,) = [n for n in self.lineage if n["label"] == "NiCl2 x 6 H2O"]
        p, old = lineage["pointer"], issue["old_pointer"]
        node = runner.get_node(self.after, p)
        runner.require(
            lineage["old_pointer"] == old and decision["reference"] == issue["reference"],
            "Nickel identity scope drift",
        )
        reason = (
            issue["decision"]
            + " Curator identity check: packaged MIM index SHA256="
            + reviewed["mim_metadata"]["sha256"]
            + " reports the alternate candidate as REJECTED; no replacement chemical identifier is asserted."
        )
        for field, expected in issue["old_fields"].items():
            runner.require(node.pop(field) == expected, "Nickel grounding baseline drift")
            self.proof(
                p + [field],
                old + [field],
                decision["source"],
                decision["pointer"],
                "remove_unsupported",
                "chemical_form",
                reason,
                p,
                decision["snippet"],
            )
        self.note(node, reason)
        self.proof(
            p + ["notes"],
            old + ["notes"],
            decision["source"],
            decision["pointer"],
            "evidence_only",
            "chemical_form",
            reason,
            p,
            decision["snippet"],
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
        if self.key.startswith("S"):
            self.standalone()
        elif self.key in {"D212", "D212a"}:
            self.original()
        else:
            self.direct()
        if self.key == "S608":
            return
        if self.after.get("solutions") == []:
            self.after.pop("solutions")
        self.links()
        self.withdraw_nickel()
        self.archive()

    def finish(self, timestamp):
        if self.key == "S608":
            runner.require(self.after == self.before, "No-op changed")
            return self.after, self.claims, self.lineage
        for claim in self.claims:
            claim["new"] = copy.deepcopy(
                runner.get_node(self.after, claim["pointer"][:-1]).get(claim["pointer"][-1])
            )
        refs = self.after.setdefault("references", [])
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
                else "web_page" if key in {"K212", "B2805"} else "dataset"
            )
            note = f"source_type={kind}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Individual authors and publication year not supplied; copyright/access years are not publication years. Source-scoped formulation evidence, not organism-growth evidence."
            entry["notes"] = (entry.get("notes", "") + "\n\n" + note).strip()
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restore source-specific medium212 formulations, stock-stage inputs and literal quantity evidence. Preserve old evidence content and history. Same-reference explanations are append-only; no final-volume, density, percent-basis or growth assertion is inferred.",
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
            "History overwritten",
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
            and gate["identity_review_sha256"] == IDENTITY_SHA
            and gate["records_reviewed"] == len(KEYS),
            "Unreviewed plan",
        )
        for name, digest in gate["receipt_sha256"].items():
            runner.require(
                runner.sha((HERE / (name + ".json")).read_bytes()) == digest,
                "Validation receipt drift",
            )
    context, _ = frozen()
    for spec in context["records"]:
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Cohort symlink")
        if mode == "preview":
            runner.require(
                runner.sha(path.read_bytes()) == spec["before_sha256"], "Cohort baseline drift"
            )
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
    parser.add_argument("--plan", type=Path, default=PLAN_PATH)
    args = parser.parse_args()
    _, result = process(
        ROOT, args.plan, "apply" if args.apply else "verify" if args.verify else "preview"
    )
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
