#!/usr/bin/env python3
"""Restore medium161 source formulations without conflating stock and final amounts."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from pathlib import Path

import repair_methanogen_stock_boundaries as shared
import repair_oteb_family as prior
import repair_rumen_bacteria_family as rumen
from bs4 import BeautifulSoup
from curation_source_fixtures import read_pdf_capture
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import html_recipe_text, parse_recipe, recipe_source
from culturemech.validation.write_validated import infer_target_class

runner, ROOT = shared.runner, shared.ROOT
PREP = ROOT / "reports/ingredient_concentration_curation/20261009-rumen-bacteria-family"
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-methanofollis-family"
CONTEXT_SHA = "7c14648ed630e165a4ebc834b0ff55f560e11cfc50f1507a6776b90c99b413b0"
DECISIONS_SHA = "75a1d525844b88f6b37282e5e0e920897c8aec027c8ffa8747b0a17f454b254f"
REVIEW_SHA = "e9c0f0d3dc5f49528e395fc3a88ea2f1eef2aacd3a0853584baa246e378058ab"
ACTION = "RESTORED_METHANOFOLLIS_SOURCE_FORMULATIONS_WITH_EVIDENCE"
KEYS = {"K161", "D161", "S209", "S241", "S277", "S5980"}
ALIASES = {
    "D-Ca-pantothenate": "Calcium D-(+)-pantothenate",
    "Lipoic acid": "(DL)-alpha-Lipoic acid",
    "Cysteine-HCl x H2O": "L-Cysteine HCl x H2O",
    "Thiamine-HCl x 2 H2O": "Thiamine HCl",
    "Pyridoxine HCl": "Pyridoxine hydrochloride",
    "Resazurin": "Sodium resazurin",
    "KAl(SO4)2 x 12 H2O": "AlK(SO4)2 x 12 H2O",
    "Trypticase (BBL)": "Trypticase",
    "Yeast extract (Difco)": "Yeast extract",
    "Yeast extract (DIFCO)": "Yeast extract",
    "CaCl2 x 2 H2O (0.1% w/v)": "CaCl2 x 2 H2O",
    "FeSO4 x 7 H2O (0.1% w/v in 0.1 N H2SO4)": "FeSO4 x 7 H2O",
    "Sodium resazurin (0.1% w/v)": "Sodium resazurin",
}


def frozen():
    raw = (PREP / "next-161-context-approved.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Reviewed context drift")
    context = json.loads(raw)
    runner.require(context["terminal"] and not context["errors"], "Incomplete captures")
    runner.require({r["key"] for r in context["records"]} == KEYS, "Cohort drift")
    raw = (PREP / "next-161-row-decisions-reviewed.json").read_bytes()
    runner.require(runner.sha(raw) == DECISIONS_SHA, "Reviewed source decisions drift")
    decisions = json.loads(raw)
    runner.require(decisions["context_sha256"] == CONTEXT_SHA, "Decision context drift")
    return context, decisions


def sources(context):
    data, texts, titles = {}, {}, {}
    runner.require(set(context["sources"]) == KEYS | {"DSMZ161"}, "Source set drift")
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
        if key == "K161":
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
        elif key == "DSMZ161":
            runner.require(
                runner.sha(read_pdf_capture(meta)) == meta["pdf_sha256"],
                "Original PDF drift",
            )
        else:
            data[key] = json.loads(raw)
    return data, texts, titles


class Review(shared.Review):
    append = prior.Review.append
    claim = prior.Review.claim
    proof = prior.Review.proof
    note_claim = prior.Review.note_claim
    metadata = prior.Review.metadata
    reference = prior.Review.reference
    retained = rumen.Review.retained

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
        self.pdf, self.titrants = decisions["original_pdf_rows"], decisions["titrant_decisions"]
        self.withdrawals = decisions["identity_withdrawals"].get(key, {})
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.claims, self.lineage, self.used = [], [], []
        self.old = list(prior.walk(before))
        self.root_evidence = {
            "S209": ["composition", 0],
            "S241": ["composition", 15],
            "S277": ["composition", 13],
            "S5980": ["composition", 0],
        }.get(key, [])
        runner.require(
            not before.get("evidence") and not before.get("variants"), "Unreviewed provenance"
        )
        if not key.startswith("S"):
            runner.require(
                not before.get("references") and not before.get("solutions"),
                "Unreviewed bibliography or stocks",
            )
            self.after["ingredients"], self.after["solutions"] = [], []

    def old_pointer(self, label):
        alias = ALIASES.get(label, label)
        matches = [
            list(p)
            for p, n in self.old
            if len(p) >= 2
            and n["preferred_term"].casefold() == alias.casefold()
            and "LB Medium" not in n.get("supplier_catalog", {}).get("supplier_name", "")
        ]
        runner.require(len(matches) <= 1, f"Ambiguous old ingredient: {label}")
        return matches[0] if matches else None

    def emit(self, *args, **kwargs):
        p = prior.Review.emit(self, *args, **kwargs)
        node = runner.get_node(self.after, p)
        if "[Merged" in node.get("notes", ""):
            node["notes"] = "Superseded flattening history, not a current amount: " + node["notes"]
        return p

    def from_row(self, parent, source, sp, label, *, old=None):
        decision = self.decisions[(source, tuple(sp))]
        row, reason = decision["source_row"], decision["basis"]
        if isinstance(row, dict):
            reason += f" Source input: {row['amount']} {row['unit']}; stage={decision.get('stage_name') or source}."
            if row.get("attribute"):
                reason += f" Source attribute: {row['attribute']}."
        else:
            reason += " Exact heading: Gram & Mol amounts are per Liter of medium."
        withdraw = label in self.withdrawals
        if withdraw:
            reason += (
                " "
                + self.withdrawals[label]
                + "; withdraw copied identity annotations without inventing a replacement ID."
            )
        return self.emit(
            parent,
            label,
            decision["proposed_quantity"],
            source,
            sp,
            reason,
            decision["mode"],
            old=self.old_pointer(label) if old is None else old,
            snippet=decision["snippet"],
            withdraw=withdraw,
        )

    def komodo(self):
        for i, row in enumerate(self.data[self.key]):
            self.from_row(["ingredients"], self.key, ["Metabolites list", i], row[0])
        self.note_claim(
            "Preserve this provider's exact displayed Gram Amounts and nulls. The 300.00 g/L clarified-rumen-fluid row is a provider assertion, not a conversion from original ml. No density, stereochemistry, missing amount or growth association is inferred.",
            self.key,
            "Gram & Mol amounts are per Liter of medium.",
        )
        runner.require(
            self.metadata(self.key, "PH Info") == "PH Info: 6.5" and self.after["ph_value"] == 6.5,
            "pH drift",
        )
        self.note_claim(
            "Retain this provider's pH6.5. Its aerobic flag is source metadata, not a verified cultivation condition; the linked original describes anoxic preparation.",
            self.key,
            self.metadata(self.key, "Is Aerobic"),
        )
        self.note_claim(
            "The linked original uses anoxic preparation and H2/CO2 incubation. This conflicts with KOMODO's aerobic flag; preserve the source distinction rather than certify either as biological growth evidence.",
            "DSMZ161",
            self.original_procedure(),
        )

    def original_procedure(self):
        text = self.texts["DSMZ161"]
        start = text.index("Dissolve ingredients")
        return text[start : text.index("Clarified rumen fluid (from", start)].strip()

    def original(self):
        stocks, counts = {}, {}
        stage_labels = {
            "mineral stock": "Modified Wolin's mineral solution",
            "fatty-acid stock": "Fatty acid mixture",
            "vitamin stock": "Wolin's vitamin solution (10x)",
        }
        stock_labels = set(stage_labels.values()) | {"Clarified rumen fluid"}
        for row in self.pdf:
            stage, label = row["stage"], " ".join(row["ingredient"].split())
            ri = counts.get(stage, 0)
            counts[stage] = ri + 1
            descriptor = stage == "main formulation" and label in stock_labels
            parent = (
                ["solutions"]
                if descriptor
                else (
                    ["ingredients"]
                    if stage == "main formulation"
                    else stocks[stage_labels[stage]] + ["composition"]
                )
            )
            reason = f"Original {stage} input: {row['source_amount']} {row['source_unit']} per preparation. {row['basis']}"
            if row.get("calculation"):
                reason += (
                    " Calculation: "
                    + row["calculation"]
                    + ". Additional exact excerpt (page1 header): "
                    + row["additional_exact_excerpt"]
                )
            p = self.emit(
                parent,
                label,
                row["proposed_quantity"],
                "DSMZ161",
                [row["locator"], ri],
                reason,
                row["mode"],
                old=self.old_pointer(label),
                descriptor=descriptor,
                snippet=row["exact_extracted_line"].strip(),
            )
            if descriptor:
                stocks[label] = p
        clarified = stocks["Clarified rumen fluid"]
        runner.get_node(self.after, clarified).pop("composition")
        snippet = (
            self.texts["DSMZ161"]
            .split("Clarified rumen fluid (from medium 1310)", 1)[1]
            .split("Modified Wolin's mineral solution (from", 1)[0]
            .strip()
        )
        reason = (
            "Procedure-only clarified fluid; no ingredient amounts are stated for its preparation. The 30% vial-fill instruction concerns storage, not concentration. No standalone CultureMech identity is inferred. "
            + snippet
        )
        self.note(runner.get_node(self.after, clarified), reason)
        self.proof(
            clarified + ["notes"],
            None,
            "DSMZ161",
            ["page1 clarified-fluid procedure"],
            "evidence_only",
            "procedure_only_stock",
            reason,
            snippet=snippet,
        )
        for row in self.titrants:
            stage = "mineral stock" if row["ingredient"] == "KOH" else "fatty-acid stock"
            self.emit(
                stocks[stage_labels[stage]] + ["composition"],
                row["ingredient"],
                None,
                "DSMZ161",
                ["page2", stage, "titration"],
                row["basis"],
                "unquantified_titrant",
                snippet=self.pdf_titration(row["ingredient"]),
            )
        self.note_claim(
            "Original nominal final volume is1001ml, while listed liquid inputs total1001.5ml. Use1.001 L for the ten main mass rates, rounded to six significant digits, not measured precision or assumed additive volume. Preserve exact stock batch inputs without inventing final stock denominators.",
            "DSMZ161",
            "Final volume: 1001 ml",
        )
        self.note_claim(
            "Preserve preparation stages: anoxic main preparation, separate clarified-fluid procedure, mineral-stock titration and fatty-acid-stock titration. Existing preparation steps remain source-scoped; storage filling fractions are not medium concentrations.",
            "DSMZ161",
            self.original_procedure(),
        )

    def pdf_titration(self, label):
        text = self.texts["DSMZ161"]
        if label == "NaOH":
            return "Adjust pH to 7.5 with concentrated NaOH."
        start = text.index("First dissolve nitrilotriacetic acid")
        return text[start : text.index("Fatty acid mixture (from", start)].strip()

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
                key = "S" + str(row["solution_id"])
                if key in self.specs:
                    runner.get_node(self.after, p)["culturemech_term"] = {
                        "id": self.specs[key]["id"],
                        "label": row["solution"],
                    }
                    self.proof(
                        p + ["culturemech_term"],
                        None,
                        self.key,
                        ["data", "recipe", ri],
                        "add",
                        "stock_identity",
                        "Exact upstream stock accession maps to this existing normalized record; no universal working dose is inferred.",
                        p,
                    )
                else:
                    runner.require(row["solution_id"] == 2618, "Unknown stock")
        for row in self.titrants:
            if row["source"] == self.key:
                self.emit(
                    ["composition"],
                    row["ingredient"],
                    None,
                    self.key,
                    row["pointer"],
                    row["basis"],
                    row["mode"],
                    snippet=row["snippet"],
                )
        source, sp = self.key, ["data"]
        if self.key == "S5980":
            source, sp = "D161", ["data", "solutions", 4]
            parent = runner.get_node(self.data[source], sp)

            def clean(rs):
                return [{k: v for k, v in r.items() if v is not None} for r in rs]

            runner.require(
                parent["id"] == 5980
                and parent["name"] == self.titles[self.key]
                and clean(parent["recipe"]) == clean(rows),
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
                "Represent every exact source row in composition; remove the false placeholder and only its incomplete-composition flag. This does not recertify chemical mappings or measured final volumes.",
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
                "Use the exact source title; retain accession, source and retrieval qualifiers in bibliography notes. Parent source names and identifies the same stock where used.",
            )
        if self.key == "S277":
            self.note_claim(
                "Preserve qualified provider rates and all existing evidence paths. Reagent strengths and batch liquid doses are distinct from final-medium concentrations. Source water input is660ml, not a volume percentage. Append the four explicitly listed stock inputs without reordering earlier supported rows; clarified fluid has no standalone normalized ID.",
                self.key,
                json_excerpt(self.context["sources"][self.key]["raw"], ["data", "recipe"]),
            )

    def links(self):
        if self.key not in {"K161", "D161"}:
            return
        reason = "KOMODO explicitly derives from DSMZ161 but preserves a distinct source title, displayed rates, nulls, chemical forms and stock scopes. DERIVED_FROM is source provenance, not exact formulation identity, biological equivalence or a new growth claim. Correct stale bacterial paths to the current exact archaea paths."
        snippet = self.metadata("K161", "Instructions")
        if self.key == "K161":
            self.after.pop("variant_children")
            self.after["parent_media"] = self.reference("D161", "DERIVED_FROM", reason)
            self.after["variant_relationship"], self.after["variant_modifications"] = (
                "DERIVED_FROM",
                [reason],
            )
            self.proof(
                ["variant_children"],
                ["variant_children"],
                "K161",
                None,
                "remove_unsupported",
                "family_relationship",
                reason,
                snippet=snippet,
            )
            for field in ("parent_media", "variant_relationship", "variant_modifications"):
                self.proof(
                    [field],
                    [field],
                    "K161",
                    None,
                    "correct",
                    "family_relationship",
                    reason,
                    ["parent_media"],
                    snippet,
                )
        else:
            for field in ("parent_media", "variant_relationship", "variant_modifications"):
                self.after.pop(field)
                self.proof(
                    [field],
                    [field],
                    "K161",
                    None,
                    "remove_unsupported",
                    "family_relationship",
                    reason,
                    snippet=snippet,
                )
            self.after["variant_children"] = [self.reference("K161", "DERIVED_FROM", reason)]
            self.proof(
                ["variant_children"],
                ["variant_children"],
                "K161",
                None,
                "correct",
                "family_relationship",
                reason,
                ["variant_children", 0],
                snippet,
            )

    def archive(self):
        if self.key == "K161":
            source, sp = self.key, None
            snippet = (
                self.texts[source]
                .split("Metabolites list", 1)[1]
                .split("Seed Metabolites list", 1)[0]
                .strip()
            )
        elif self.key == "D161":
            source, sp, snippet = "DSMZ161", None, self.context["sources"]["DSMZ161"]["raw"].strip()
        else:
            source, sp = (
                ("D161", ["data", "solutions", 4, "recipe"])
                if self.key == "S5980"
                else (self.key, ["data", "recipe"])
            )
            snippet = json_excerpt(self.context["sources"][source]["raw"], sp)
        for field in ("ingredients", "composition", "solutions"):
            if self.before.get(field):
                self.note_claim(
                    "Complete inspected source rows define this reconstruction. Archive false LB expansions, flattened quantities and placeholders in append-only history. Preserve earlier supported evidence exactly; unrelated chemical annotations are not recertified.",
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
                    "Withdraw an old false LB, placeholder, unsupported copied ingredient or flattened stock quantity from the current formulation; preserve its exact value in history.",
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
        if self.key == "K161":
            self.komodo()
        elif self.key == "D161":
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
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            entry = next((r for r in refs if r["reference"] == meta["url"]), None)
            if entry is None:
                entry = {"reference": meta["url"], "title": self.titles[key]}
                refs.append(entry)
            kind = (
                "culture_collection_page"
                if key == "DSMZ161"
                else "web_page" if key == "K161" else "dataset"
            )
            note = f"source_type={kind}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Individual authors and publication year not supplied; copyright/access years are not publication years. Source-scoped formulation evidence, not organism-growth evidence."
            entry["notes"] = (entry.get("notes", "") + "\n\n" + note).strip()
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restore distinct medium161 source formulations, stock scopes, input units and unquantified titrants with exact evidence. Preserve prior supported entries and unknown quantities; correct false duplicate direction and stale paths. No growth association added.",
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
