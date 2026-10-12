#!/usr/bin/env python3
"""Restore source-specific Allisonella ingredients and fatty-acid stock boundaries."""

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

runner, ROOT = shared.runner, shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-allisonella-acids"
CONTEXT_SHA = "dae45cfd1b14facc31aa8691044e6718031b2cd9f8f258b4e5ae141553bfc61f"
ACTION = "RESTORED_ALLISONELLA_ACID_IDENTITIES_AND_STOCK_SCOPES_WITH_EVIDENCE"
SOURCE_URLS = {
    "D1006": "https://mediadive.dsmz.de/rest/medium/1006",
    "K1006": "https://komodo.modelseed.org/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo=1006",
    "DSMZ1006": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1006.pdf",
}
REPLACEMENTS = {
    "Cysteine-HCl x H2O": "L-Cysteine HCl x H2O",
    "Resazurin": "Sodium resazurin",
}


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    runner.require(context["terminal"] and not context["errors"], "Incomplete captures")
    runner.require({r["key"] for r in context["records"]} == {"D1006", "K1006"}, "Cohort drift")
    return context


def sources(context):
    data, texts, titles = {}, {}, {}
    runner.require(set(context["sources"]) == set(SOURCE_URLS), "Source set drift")
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        runner.require(
            meta["url"] == meta["response_url"] == SOURCE_URLS[key]
            and meta["http_status"] == 200
            and runner.sha(raw.encode("utf-8")) == meta["sha256"],
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        parsed = parse_recipe(recipe_source(meta["url"]), raw, meta)
        texts[key], titles[key] = parsed.content, parsed.title
        if key == "DSMZ1006":
            payload = read_pdf_capture(meta)
            runner.require(
                runner.sha(payload) == meta["pdf_sha256"]
                and extract_recipe_pdf(payload) == (raw, 1),
                "Original PDF drift",
            )
        elif key == "K1006":
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
                and len(rows) == 22
                and all(len(r) == 5 for r in rows),
                "KOMODO table drift",
            )
            data[key] = rows[1:]
        else:
            data[key] = json.loads(raw)
    ss = data["D1006"]["data"]["solutions"]
    runner.require(
        [s["id"] for s in ss] == [2052, 608]
        and [len(s["recipe"]) for s in ss] == [14, 7]
        and all(r["optional"] == 0 for s in ss for r in s["recipe"]),
        "DSMZ stage drift",
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

    def pdf_row(self, label):
        label = {
            "Trypticase peptone": "Trypticase peptone (BD BBL)",
            "Sodium resazurin": "Sodium resazurin (0.1% w/v)",
        }.get(label, label)
        matches = [
            line.strip()
            for line in self.texts["DSMZ1006"].splitlines()
            if line.strip().startswith(label + " ") and line.split()[-1] in {"g", "mg", "ml"}
        ]
        runner.require(len(matches) == 1, f"Ambiguous PDF row: {label}")
        return matches[0]

    def emit(
        self,
        parent,
        label,
        quantity,
        source_pointer,
        kind,
        reason,
        *,
        descriptor=False,
        snippet=None,
    ):
        old_name = REPLACEMENTS.get(label, "Trypticase peptone" if label == "Trypticase" else label)
        old = None if descriptor else self.old.get(old_name.casefold())
        replace_identity = self.key == "K1006" and label in REPLACEMENTS
        node = (
            copy.deepcopy(runner.get_node(self.before, old))
            if old and not replace_identity
            else {"preferred_term": label}
        )
        if old:
            runner.require(tuple(old) not in self.accounted, "Repeated old ingredient")
            self.accounted.add(tuple(old))
        node["preferred_term"] = label
        if quantity is None:
            node.pop("concentration", None)
        else:
            node["concentration"] = quantity
        if descriptor:
            node.update(name=label, composition=[])
        if replace_identity:
            reason += " The source label does not explicitly reproduce the copied sodium-salt or L-stereochemistry identity. Withdraw the copied annotations rather than infer that form; archive the original node in history. This is not a claim that a particular alternative chemical form is proven."
        self.note(node, reason)
        p = self.append(parent, node)
        ep = [] if descriptor else p
        self.lineage.append(
            {
                "pointer": p,
                "old_pointer": old,
                "source": self.key,
                "source_pointer": source_pointer,
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
                source_pointer,
                "correct" if old else "add",
                kind,
                reason,
                ep,
                snippet,
            )
        if replace_identity:
            for field in ("term", "mediaingredientmech_chebi_term", "mediaingredientmech_term"):
                if field in runner.get_node(self.before, old):
                    self.claim(
                        p + [field],
                        old + [field],
                        self.key,
                        source_pointer,
                        "remove_unsupported",
                        "copied_identity_withdrawn",
                        reason,
                        ep,
                        snippet,
                    )
        return p

    def context_claim(self, reason, source, snippet, *, old=None, kind="recipe_context"):
        self.note(self.after, reason)
        self.claim(["notes"], old, source, None, "evidence_only", kind, reason, [], snippet)

    def komodo(self):
        for i, row in enumerate(self.data[self.key]):
            label, _, _, gram, _ = row
            q = None if gram == "null" else {"value": gram, "unit": "G_PER_L"}
            reason = (
                "The source Gram Amount is null: no fixed amount is asserted, and missing is not zero."
                if q is None
                else f"Provider-reported medium rate: Gram Amount {gram} per liter, preserving displayed precision. The linked DSMZ preparation does not independently explain this normalization."
            )
            reason += " The Mol Amount and separate SEED aggregate table are not used to infer ingredient forms, stock doses or new molarities."
            p = self.emit(
                ["ingredients"],
                label,
                q,
                ["recipe_table", i + 1],
                "provider_medium_rate" if q else "unquantified",
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
        restored = next(row for row in self.data[self.key] if row[0] == "DL-2-Methyl butyric acid")
        self.acid_quote, self.acid_sp = " ".join(restored), None
        self.context_claim(
            "KOMODO reports Is Aerobic: true, while its linked DSMZ original uses 100% CO2 and anoxic vessels. Preserve this source conflict, not a resolved oxygen requirement or quantitative gas addition.",
            self.key,
            "Is Aerobic: true",
        )
        self.context_claim(
            "The linked original specifies anoxic preparation; it does not establish a quantitative CO2 ingredient amount or justify replacing this provider's source-specific rates.",
            "DSMZ1006",
            self.preparation_quote(),
        )

    def preparation_quote(self):
        pdf = self.texts["DSMZ1006"]
        return pdf[
            pdf.index("Dissolve ingredients") : pdf.index(
                "Volatile fatty acid mixture (from medium 330)"
            )
        ].rstrip()

    def dsmz(self):
        ss = self.data[self.key]["data"]["solutions"]
        for ri, row in enumerate(ss[0]["recipe"]):
            sp = ["data", "solutions", 0, "recipe", ri]
            label = row.get("compound", row.get("solution"))
            if label == "Sodium resazurin":
                runner.require(
                    row["attribute"] == "0.1% w/v" and row["amount"] == 0.5 and row["unit"] == "ml",
                    "Resazurin stock drift",
                )
                p = self.emit(
                    ["solutions"],
                    "Sodium resazurin (0.1% w/v)",
                    {"value": "0.0005", "unit": "L"},
                    sp,
                    "stock_dose",
                    "Source addition: 0.50 ml = 0.0005 L of 0.1% w/v sodium resazurin stock, not a mass or final-medium concentration.",
                    descriptor=True,
                )
                cp = self.emit(
                    p + ["composition"],
                    label,
                    {"value": "0.1", "unit": "PERCENT_W_V"},
                    sp,
                    "stock_strength",
                    "The explicitly stated 0.1% w/v belongs to the sodium resazurin stock. Its 0.50 ml receiving-medium dose is stored separately; no final-medium concentration is inferred.",
                )
                self.claim(
                    cp + ["concentration"],
                    None,
                    "DSMZ1006",
                    None,
                    "evidence_only",
                    "original_stock_strength",
                    "Original PDF corroborates the stock strength and separate addition volume.",
                    cp,
                    self.pdf_row(label),
                )
            elif label == "Volatile fatty acid mixture":
                runner.require(
                    row["solution_id"] == 608 and row["amount"] == 3.1 and row["unit"] == "ml",
                    "Fatty-acid dose drift",
                )
                p = self.emit(
                    ["solutions"],
                    label,
                    {"value": "0.0031", "unit": "L"},
                    sp,
                    "stock_dose",
                    "Source addition: 3.10 ml = 0.0031 L fatty-acid mixture. The nested acid volumes prepare that stock; they are not added individually in those volumes to the receiving medium.",
                    descriptor=True,
                )
                for j, acid in enumerate(ss[1]["recipe"]):
                    runner.require(acid["unit"] == "ml", "Acid input unit drift")
                    name = acid["compound"]
                    value = number(Decimal(str(acid["amount"])) / 1000)
                    cp = self.emit(
                        p + ["composition"],
                        name,
                        {"value": value, "unit": "L"},
                        ["data", "solutions", 1, "recipe", j],
                        "stock_liquid_input",
                        f"Stock preparation input: {acid['amount']} ml = {value} L. This is a liquid input volume, not grams or a finished-medium concentration. Source API g_l/mmol_l fields are not adopted because their density and conversion basis are not independently established by the original recipe.",
                    )
                    self.claim(
                        cp + ["concentration"],
                        None,
                        "DSMZ1006",
                        None,
                        "evidence_only",
                        "original_liquid_input",
                        "The original fatty-acid stock table explicitly uses ml, not g/L; no final-volume or density conversion is inferred.",
                        cp,
                        self.pdf_row(name),
                    )
            else:
                if row["unit"] == "ml":
                    runner.require(
                        label == "Distilled water" and row["amount"] == 1000,
                        "Unexpected main liquid",
                    )
                    q, kind = {"value": "1", "unit": "L"}, "water_input"
                    reason = "Source input: 1000 ml = 1 L distilled water, not a measured final-volume denominator after the other additions."
                else:
                    runner.require(row["unit"] in {"g", "mg"}, "Unexpected mass unit")
                    q, kind = None, "batch_mass"
                    reason = f"Source batch input: {row['amount']} {row['unit']}. Preserve the exact mass in notes; API g_l={row['g_l']} uses the provider's main-volume encoding and is not an independently verified final-medium concentration."
                if row.get("attribute"):
                    reason += " Source material qualifier: " + row["attribute"] + "."
                cp = self.emit(["ingredients"], label, q, sp, kind, reason)
                self.claim(
                    cp + ["notes"],
                    None,
                    "DSMZ1006",
                    None,
                    "evidence_only",
                    "original_batch_input",
                    reason,
                    cp,
                    self.pdf_row(label),
                )
            if label in {"Sodium resazurin", "Volatile fatty acid mixture"}:
                self.claim(
                    p + ["concentration"],
                    None,
                    "DSMZ1006",
                    None,
                    "evidence_only",
                    "original_stock_dose",
                    "Original source corroborates the addition dose, independently of the stock composition.",
                    [],
                    self.pdf_row(label),
                )
        self.acid_sp = ["data", "solutions", 1, "recipe", 5]
        self.acid_quote = json_excerpt(self.context["sources"][self.key]["raw"], self.acid_sp)
        step = ss[0]["steps"][0]["step"]
        runner.require(
            self.before["preparation_steps"]
            == [{"step_number": 1, "action": "AUTOCLAVE", "description": step}],
            "Preparation baseline drift",
        )
        self.claim(
            ["preparation_steps"],
            ["preparation_steps"],
            self.key,
            ["data", "solutions", 0, "steps", 0, "step"],
            "evidence_only",
            "retained_preparation",
            "Retain the source preparation order and pH adjustment; no unstated titrant or gas dose is added.",
            [],
        )
        self.context_claim(
            "The original recipe adds carbonate, fatty-acid stock and cysteine after cooling under CO2, then dispenses and autoclaves. The API main volume of 1004 ml is a provider encoding, not evidence of measured final volume or verified density conversions.",
            "DSMZ1006",
            self.preparation_quote(),
        )

    def links(self):
        quote = next(
            line for line in self.texts["K1006"].splitlines() if line.startswith("Instructions:")
        )
        reason = "KOMODO explicitly links DSMZ 1006, but its ingredient forms, nulls and reported rates are source-specific. The copied earlier concentration signature does not prove an exact duplicate; source derivation does not add a growth association."
        if self.key == "K1006":
            runner.require(
                self.before["parent_media"]["id"] == self.specs["D1006"]["id"], "Parent drift"
            )
            self.after["parent_media"]["relationship"] = "DERIVED_FROM"
            self.after["parent_media"]["notes"] = reason
            self.after["variant_relationship"] = "DERIVED_FROM"
            self.after["variant_modifications"] = [reason]
            ep = ["parent_media"]
            fields = ("parent_media", "variant_relationship", "variant_modifications")
        else:
            runner.require(
                len(self.before["variant_children"]) == 1
                and self.before["variant_children"][0]["id"] == self.specs["K1006"]["id"],
                "Child drift",
            )
            self.after["variant_children"][0]["relationship"] = "DERIVED_FROM"
            self.after["variant_children"][0]["notes"] = reason
            ep, fields = ["variant_children", 0], ("variant_children",)
        for field in fields:
            self.claim(
                [field], [field], "K1006", None, "correct", "family_relationship", reason, ep, quote
            )

    def formulate(self):
        prefix, marker, history = self.before["notes"].partition("Commercial Product: LB Medium")
        runner.require(marker, "Historical note drift")
        self.after["notes"] = (
            prefix.rstrip()
            + "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product: LB Medium"
            + history
        )
        self.komodo() if self.key == "K1006" else self.dsmz()
        if self.key == "K1006":
            self.context_claim(
                "Archive the complete prior ingredient nodes, including the copied L-cysteine and sodium-resazurin annotations, in append-only history. Their source-specific replacements do not inherit unverified chemical forms.",
                self.key,
                self.acid_quote,
                old=["ingredients"],
                kind="copied_identity_archived",
            )
        for p in self.lb:
            self.claim(
                ["notes"],
                p + ["concentration"],
                self.key,
                self.acid_sp,
                "remove_unsupported",
                "false_lb_removed",
                "Restore source-listed DL-2-methylbutyric acid instead of the false supplier-tagged LB expansion. Preserve genuine yeast extract, Trypticase and NaCl separately.",
                [],
                self.acid_quote,
            )
            self.accounted.add(tuple(p))
        runner.require(
            self.accounted == {("ingredients", i) for i in range(len(self.before["ingredients"]))},
            "Unaccounted old ingredient",
        )
        self.links()
        self.context_claim(
            "Source-specific ingredient identities and quantity scopes supersede copied flattened amounts. Unknown gas amounts, densities and final volumes remain unknown. Other existing chemical annotations and all prior history are preserved, not recertified. No taxa-media association is added.",
            self.key,
            self.acid_quote,
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
            self.after["references"].append(
                {
                    "reference": meta["url"],
                    "title": self.titles[key],
                    "notes": f"source_type={'dataset' if key == 'D1006' else 'web_page' if key == 'K1006' else 'culture_collection_page'}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year are not supplied; copyright/access years are not publication years.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=SOURCE_URLS[self.key],
            notes="Restore source-specific Allisonella ingredients and the acid/resazurin stock boundaries; retain unquantified amounts, chemical-form limits and source conflicts, and correct the reciprocal family relationship without changing permanent IDs.",
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
