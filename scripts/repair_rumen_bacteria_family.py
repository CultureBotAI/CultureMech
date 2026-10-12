#!/usr/bin/env python3
"""Guarded source-specific medium330 repairs with independently reviewed evidence."""

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
PREP = ROOT / "reports/ingredient_concentration_curation/20261009-ruminococcus-albus-family"
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-rumen-bacteria-family"
CONTEXT_SHA = "97e6cfa229556a5251518fafb27c7506242afb62cb7be79ff7ff985dfb4e6c49"
PREPARATION_SHA = "6dd69a7db8c14d08e499d370a9bd075dc5f37d8a69ff4e6c86a4718f88c6565c"
REVIEW_SHA = "8f9525e7127628bb6c3741f21ddaef5cf0ec3221e275f24293d63ef2d71dba99"
ACTION = "RESTORED_RUMEN_BACTERIA_SOURCE_FORMULATIONS_WITH_EVIDENCE"
KEYS = {
    "DJ1029",
    "K330",
    "M1093",
    "S124",
    "S3774",
    "S5080",
    "S606",
    "S607",
    "S608",
    "K330_17630",
    "K3032",
    "D330",
    "K3131",
}


def frozen():
    raw = (PREP / "next-330-preparation.json").read_bytes()
    runner.require(runner.sha(raw) == PREPARATION_SHA, "Reviewed preparation drift")
    preparation = json.loads(raw)
    for name, digest in preparation["receipt_sha256"].items():
        runner.require(
            runner.sha((PREP / (name + ".json")).read_bytes()) == digest, "Receipt drift"
        )
    raw = (PREP / "next-330-context-approved.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Reviewed context drift")
    context = json.loads(raw)
    runner.require({r["key"] for r in context["records"]} == KEYS, "Cohort drift")
    runner.require(
        len(context["errors"]) == 1 and context["errors"][0]["key"] == "JCM1029", "Access-gap drift"
    )
    linked = json.loads((PREP / "next-330-M124.json").read_text())
    runner.require(linked["terminal"] and not linked["errors"], "Linked source unavailable")
    context["sources"]["M124"] = linked["source"]
    return context, json.loads((PREP / "next-330-row-decisions.json").read_text())


def sources(context):
    data, texts, titles = {}, {}, {}
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        runner.require(
            meta["http_status"] == 200
            and meta["url"] == meta["response_url"]
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
                rows[0] == ["Name", "Semi unique name", "Unique Name", "Gram Amount", "Mol Amount"],
                "Provider columns drift",
            )
            data[key] = rows[1:]
        elif key == "DSMZ330":
            runner.require(
                runner.sha(read_pdf_capture(meta)) == meta["pdf_sha256"],
                "Original PDF drift",
            )
        elif key != "JCM133":
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
        self.context, decisions = frozen()
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
        self.decisions = {(r["source"], tuple(r["pointer"])): r for r in decisions["rows"]}
        self.pdf = decisions["original_pdf_rows"]
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.claims, self.lineage, self.used = [], [], []
        self.old = list(prior.walk(before))
        self.root_evidence = (
            ["composition", 1 if key in {"S124", "S5080"} else 0] if key.startswith("S") else []
        )
        runner.require(
            not before.get("evidence") and not before.get("variants"), "Unreviewed provenance"
        )
        if not key.startswith("S"):
            runner.require(not before.get("references"), "Unreviewed bibliography")
            self.after["ingredients"], self.after["solutions"] = [], []

    def old_pointer(self, label):
        aliases = {
            "Cysteine-HCl x H2O": "L-Cysteine HCl x H2O",
            "Trypticase Peptone (BBL)": "Trypticase peptone",
            "Trypticase peptone (BD BBL)": "Trypticase peptone",
            "Yeast extract (OXOID)": "Yeast extract",
            "NaOH (1 N)": "NaOH",
        }
        if self.key in {"K330", "K330_17630", "D330"}:
            aliases.update({"Glucose": "D-Glucose", "Starch, soluble": "Starch"})
        # A source's generic resazurin label does not validate the copied sodium-salt identity.
        if self.key.startswith("K"):
            aliases["Resazurin"] = "Sodium resazurin"
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

    def from_row(self, parent, source, sp, label, *, descriptor=False, old=None):
        decision = self.decisions[(source, tuple(sp))]
        row, reason = decision["source_row"], decision["basis"]
        if isinstance(row, dict):
            reason += f" Source input: {row.get('amount', row.get('volume'))} {row.get('unit')}; stage={decision.get('stage_name') or source}."
            if row.get("attribute"):
                reason += f" Source attribute: {row['attribute']}."
            if self.key == "DJ1029" and row.get("g_l") is not None:
                reason += f" Dataset g_l={row['g_l']} is retained here as provider context, not original-methods concentration evidence."
        else:
            reason += " Exact heading: Gram & Mol amounts are per Liter of medium."
        old = self.old_pointer(label) if old is None else old
        withdraw = self.key.startswith("K") and label == "Resazurin"
        if withdraw:
            reason += " The source says Resazurin, not sodium resazurin. Withdraw copied salt-specific grounding; no replacement chemical identifier is inferred."
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
            withdraw=withdraw,
        )
        return p

    def komodo(self):
        for i, row in enumerate(self.data[self.key]):
            self.from_row(["ingredients"], self.key, ["Metabolites list", i], row[0])
        self.note_claim(
            "Preserve exact displayed Gram Amounts and nulls as source-specific assertions. Rounded molar columns and aggregated SEED rows are not ingredient evidence. No growth association is inferred.",
            self.key,
            "Gram & Mol amounts are per Liter of medium.",
        )
        ph = self.metadata(self.key, "PH Info")
        if self.key == "K330":
            runner.require(
                ph == "PH Info: 6.7 - 6.8" and self.after["ph_range"] == {"min": 6.7, "max": 6.8},
                "Base pH drift",
            )
        else:
            runner.require(
                ph == "PH Info: null"
                and not self.after.get("ph_value")
                and not self.after.get("ph_range"),
                "Unknown pH drift",
            )
        self.note_claim(
            "Retain source-specific pH; a null variant or stock pH does not inherit the base pH.",
            self.key,
            ph,
        )
        if self.key in {"K3032", "K3131"}:
            accession = self.key[1:]
            self.after["notes"] = (
                f"KOMODO accession {accession} names a stock from medium330, but its Instructions link points to DSMZ{accession}. That conflicting DSMZ/MediaDive{accession} equivalence is unverified and is withdrawn. Restore only this provider's displayed rows; retain its legacy MediaRecipe shape and record_kind SOLUTION."
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
                "The conflicting Instructions link is present in the provider itself, not proven to be solely an importer error.",
                snippet=self.metadata(self.key, "Instructions"),
            )

    def original(self):
        stocks = {}
        stock_labels = {
            "Mineral solution",
            "Volatile fatty acid mixture",
            "Haemin solution (0.05% w/v)",
        }
        stage_to_label = {
            "mineral stock": "Mineral solution",
            "fatty-acid stock": "Volatile fatty acid mixture",
            "haemin stock": "Haemin solution (0.05% w/v)",
        }
        stage_counts = {}
        for row in self.pdf:
            stage, label = row["stage"], row["ingredient"]
            ri = stage_counts.get(stage, 0)
            stage_counts[stage] = ri + 1
            descriptor = label in stock_labels and stage == "main formulation"
            parent = (
                ["solutions"]
                if descriptor
                else (
                    ["ingredients"]
                    if stage == "main formulation"
                    else stocks[stage_to_label[stage]] + ["composition"]
                )
            )
            reason = f"Original {stage} input: {row['source_amount']} {row['source_unit']} per preparation. {row['basis']}"
            if row.get("calculation"):
                reason += " Calculation: " + row["calculation"] + "."
            if row.get("additional_exact_excerpt"):
                reason += (
                    " Additional exact excerpt ("
                    + row.get("additional_locator", "page 2 haemin procedure")
                    + "): "
                    + row["additional_exact_excerpt"]
                )
            p = self.emit(
                parent,
                label,
                row["proposed_quantity"],
                "DSMZ330",
                [row["locator"], ri],
                reason,
                row["mode"],
                old=self.old_pointer(label),
                descriptor=descriptor,
                snippet=row["exact_extracted_line"].strip(),
            )
            if descriptor:
                stocks[label] = p
        self.note_claim(
            "The source explicitly states nominal final volume 1003 ml. Listed liquid inputs total 1003.6 ml; do not substitute that sum, assume volume additivity, or claim measured precision. Main mass rates use the stated 1.003 L denominator, rounded to six significant digits. Stock batch masses without a final-volume instruction remain in notes.",
            "DSMZ330",
            "Final volume: 1003 ml",
        )
        self.note_claim(
            "Preparation stages and the strain-specific 30 ml/l rumen-fluid supplement remain source context, not a base ingredient or new growth association. Preserve CO2 treatment and post-autoclave sterile anoxic additions.",
            "DSMZ330",
            self.texts["DSMZ330"]
            .split("Dissolve ingredients", 1)[1]
            .split("Mineral solution (from", 1)[0]
            .strip(),
        )

    def dataset_medium(self):
        stocks = {}
        for si, stage in enumerate(self.data[self.key]["data"]["solutions"]):
            parent = ["ingredients"] if si == 0 else stocks[stage["id"]] + ["composition"]
            for ri, row in enumerate(stage["recipe"]):
                descriptor = bool(row.get("solution_id"))
                p = self.from_row(
                    ["solutions"] if descriptor else parent,
                    self.key,
                    ["data", "solutions", si, "recipe", ri],
                    row.get("compound") or row["solution"],
                    descriptor=descriptor,
                )
                if descriptor:
                    stocks[row["solution_id"]] = p
        self.note_claim(
            "Original JCM1029 is unavailable: its current endpoint returned no recipe. This formulation is supported by the inspected MediaDive dataset only. Its declared volume and g_l fields do not establish the original final-volume basis. Main and mineral masses are retained as exact batch inputs in notes; acid inputs retain liquid volumes. Existing preparation descriptions are dataset assertions, not newly verified original methods.",
            self.key,
            json_excerpt(self.context["sources"][self.key]["raw"], ["data", "medium"]),
        )

    def togo(self):
        stocks = {}
        for si, stage in enumerate(self.data[self.key]["components"]):
            parent = ["ingredients"] if si == 0 else stocks["M1093"] + ["composition"]
            for ri, row in enumerate(stage["items"]):
                descriptor = bool(row.get("reference_media_id"))
                p = self.from_row(
                    ["solutions"] if descriptor else parent,
                    self.key,
                    ["components", si, "items", ri],
                    row["component_name"],
                    descriptor=descriptor,
                )
                if descriptor:
                    stocks[row["reference_media_id"]] = p
        linked = json.loads((PREP / "next-330-linked-stock-review.json").read_text())
        for row in linked["rows"]:
            togo, original = row["togo_source"], row["original_source"]
            p = self.emit(
                stocks["M124"] + ["composition"],
                row["ingredient"],
                row["proposed_batch_volume"],
                "M124",
                togo["pointer"],
                row["basis"]
                + " M1093 explicitly links M124; M124 identifies original JCM133. Import only the VFA subsection.",
                "linked_vfa_batch_input",
                snippet=togo["snippet"],
            )
            self.proof(
                p + ["concentration"],
                None,
                "JCM133",
                original["pointer"],
                "evidence_only",
                "linked_original_subsection",
                row["basis"]
                + " The other 24 table rows of Medium10 are outside this stock and are not imported.",
                p,
                original["snippet"],
            )
        self.proof(
            stocks["M124"] + ["notes"],
            None,
            "M124",
            ["meta"],
            "evidence_only",
            "cross_reference_chain",
            "M1093's explicit M124 link and M124's JCM_M133 metadata support only the VFA subsection, not wholesale import of Medium10.",
        )
        self.note_claim(
            "Original JCM1029 is unavailable. Do not transfer DSMZ330's nominal denominator to this source. Split the 960 ml main water from the 1 L mineral-stock water; retain exact mg inputs and unquantified CO2. Provider preparation text: "
            + "\n".join(c["comment"] for c in self.data[self.key]["comments"]),
            self.key,
            json_excerpt(self.context["sources"][self.key]["raw"], ["comments"]),
        )

    def retained(self, p, ri, row):
        node = copy.deepcopy(runner.get_node(self.before, p))
        decision = self.decisions[(self.key, ("data", "recipe", ri))]
        runner.require(
            node["concentration"] == decision["proposed_quantity"] and len(node["evidence"]) == 1,
            "Prior quantity/evidence drift",
        )
        entry = node["evidence"][0]
        runner.require(entry["snippet"] in self.texts[self.key], "Prior snippet drift")
        self.after["composition"].append(node)
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
                "label": row["compound"],
                "kind": "retained_provider_rate",
            }
        )

    def standalone(self):
        rows = self.data[self.key]["data"]["recipe"]
        self.after["composition"] = []
        ordinary = [(i, r) for i, r in enumerate(rows) if not r.get("solution_id")]
        runner.require(
            len(ordinary) == len(self.before["composition"]), "Standalone node count drift"
        )
        for oi, (ri, row) in enumerate(ordinary):
            p = ["composition", oi]
            runner.require(
                self.before["composition"][oi]["preferred_term"] == row["compound"],
                "Standalone identity drift",
            )
            if self.before["composition"][oi].get("evidence"):
                self.retained(p, ri, row)
            else:
                self.from_row(
                    ["composition"], self.key, ["data", "recipe", ri], row["compound"], old=p
                )
        for ri, row in enumerate(rows):
            if row.get("solution_id"):
                p = self.from_row(
                    ["composition"], self.key, ["data", "recipe", ri], row["solution"]
                )
                runner.get_node(self.after, p)["culturemech_term"] = {
                    "id": self.specs["S" + str(row["solution_id"])]["id"],
                    "label": row["solution"],
                }
                self.proof(
                    p + ["culturemech_term"],
                    None,
                    self.key,
                    ["data", "recipe", ri],
                    "add",
                    "stock_identity",
                    "The exact source solution_id identifies this batch stock input; no universal working concentration is inferred.",
                    p,
                )
        # S607 already has evidence on every ingredient. Its actual parent dataset
        # independently identifies the same stock, allowing old entries to stay exact.
        source, sp = (
            ("D330", ["data", "solutions", 1]) if self.key == "S607" else (self.key, ["data"])
        )
        if self.key == "S607":
            stock = runner.get_node(self.data[source], sp)
            runner.require(
                stock["id"] == 607
                and stock["name"] == self.titles[self.key]
                and [{k: v for k, v in r.items() if v is not None} for r in stock["recipe"]]
                == [{k: v for k, v in r.items() if v is not None} for r in rows],
                "Parent stock identity drift",
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
                source,
                sp + ["recipe"],
                "remove_unsupported",
                "legacy_placeholder",
                "All exact source rows are represented in composition. Remove the false placeholder and only its incomplete-composition flag, not supported quantities or remaining scientific uncertainties.",
            )
        if self.before.get("references"):
            self.after["references"][0]["title"] = self.titles[self.key]
            self.proof(
                ["references", 0, "title"],
                ["references", 0, "title"],
                source,
                sp + ["name"],
                "correct",
                "bibliographic_title",
                "Use the actual source title. Source/accession provenance belongs in notes. For stock607 the parent dataset explicitly identifies the same solution id and title.",
            )
        if self.key in {"S124", "S606", "S5080"}:
            self.note_claim(
                "Stock input volumes are not final-medium concentrations. Explicit reagent strengths remain source attributes; make-up water is not a fixed added volume. Provider g_l values on retained mass rows remain qualified dataset rates, not newly verified original-methods arithmetic.",
                self.key,
                json_excerpt(self.context["sources"][self.key]["raw"], ["data", "recipe"]),
            )
        if self.key == "S5080":
            self.note_claim(
                "Original JCM1029 is unavailable. Retained provider rates and preparation text must not be promoted to current original-methods verification.",
                self.key,
                json_excerpt(self.context["sources"][self.key]["raw"], ["data", "name"]),
            )

    def links(self):
        derived = "KOMODO explicitly derives from DSMZ330 but has different displayed rates, nulls and stock scopes. DERIVED_FROM does not assert exact formulation identity or biological equivalence."
        variant = "The exact DSM17630 variant changes sixteen displayed provider rates and adds rumen fluid 29.13 g/L; eleven common rows remain unchanged. Its pH is null. Preserve the strain-specific provider formulation, not an exact duplicate or a density-based conversion of DSMZ's 30 ml/l supplement. No growth association is added."
        if self.key in {"K330", "K330_17630"}:
            base = self.key == "K330"
            parent, relation, reason = (
                ("D330", "DERIVED_FROM", derived)
                if base
                else ("K330", "STRAIN_SPECIFIC_VARIANT", variant)
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
        if self.key in {"D330", "K330"}:
            original = self.key == "D330"
            child, relation, reason = (
                ("K330", "DERIVED_FROM", derived)
                if original
                else ("K330_17630", "STRAIN_SPECIFIC_VARIANT", variant)
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
            source, sp = self.key, None
            snippet = (
                self.texts[source]
                .split("Metabolites list", 1)[1]
                .split("Seed Metabolites list", 1)[0]
                .strip()
            )
        elif self.key == "D330":
            source, sp, snippet = "DSMZ330", None, self.context["sources"]["DSMZ330"]["raw"].strip()
        else:
            source = "D330" if self.key == "S607" else self.key
            sp = (
                ["data", "solutions", 1, "recipe"]
                if self.key == "S607"
                else (
                    ["data", "recipe"]
                    if self.key.startswith("S")
                    else ["components"] if self.key.startswith("M") else ["data", "solutions"]
                )
            )
            snippet = json_excerpt(self.context["sources"][source]["raw"], sp)
        for field in ("ingredients", "composition", "solutions"):
            if self.before.get(field):
                self.note_claim(
                    "Complete inspected source rows define this reconstruction. Archive old flattened quantities, false LB expansions, placeholders and copied stock-solvent claims in append-only history. Unrelated annotations remain preserved, not recertified.",
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
                    sp,
                    "remove_unsupported",
                    "old_quantity_accounted",
                    "The old quantity is a false LB/placeholder/copied stock-solvent claim or a relocated stage. Preserve its old value in history, not as an unsupported concentration.",
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
        elif self.key.startswith("S"):
            self.standalone()
        elif self.key == "D330":
            self.original()
        elif self.key == "DJ1029":
            self.dataset_medium()
        else:
            self.togo()
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
                if key in {"DSMZ330", "JCM133"}
                else "web_page" if key.startswith("K") else "dataset"
            )
            note = f"source_type={kind}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Individual authors and publication year not supplied; copyright/access years are not publication years. Source-scoped formulation evidence, not organism-growth evidence."
            entry["notes"] = (entry.get("notes", "") + "\n\n" + note).strip()
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restore source-specific medium330 ingredients, stock scopes and input units with literal evidence. Preserve prior supported entries, provider nulls, unknown original bases and the JCM1029 access gap. No growth association added.",
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
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    args = parser.parse_args()
    HERE.mkdir(exist_ok=True)
    _, result = process(
        ROOT, args.plan, "apply" if args.apply else "verify" if args.verify else "preview"
    )
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
