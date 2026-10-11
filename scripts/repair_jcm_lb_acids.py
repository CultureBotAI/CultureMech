#!/usr/bin/env python3
"""Guarded identity and preparation-scope repairs for J266, J675 and J1203."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import re
from decimal import Decimal
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_m689_stocks as prior
import repair_methanogen_stock_boundaries as shared

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import html_recipe_text

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-jcm-lb-acids"
CONTEXT_SHA = "bd14d58c295cef3f05b3dc9183a375f9e4789ae3d7e8cd10583daa489bea7bee"
ACTION = "RESTORED_JCM_ACID_IDENTITIES_AND_PREPARATION_SCOPES_WITH_EVIDENCE"
LB = {"J266": [16, 17, 18], "J675": [13, 14, 15], "J1203": [10, 11, 12]}
GRAPHS = {
    "J266": ([3953, 3954, 3804, 3861], [18, 5, 13, 11]),
    "J675": ([4568, 4566, 4570, 4571], [8, 2, 6, 4]),
    "J1203": ([5322], [18]),
}
ACID = {
    "J266": (1, 2, "\u03b1-Methylbutyric acid 0.5 g"),
    "J675": (3, 2, "2-Methylbutyric acid 10.0 ml"),
    "J1203": (0, 10, "DL-2-Methyl butyric acid 0.2 ml"),
}


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    return json.loads(raw)


def sources(context):
    data = {}
    for key, capture in context["sources"].items():
        meta, raw = capture["metadata"], capture["raw"]
        url = (
            "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=" + key[3:]
            if key.startswith("JCM")
            else "https://mediadive.dsmz.de/rest/medium/" + key
        )
        runner.require(
            meta["url"] == meta["response_url"] == url
            and meta["http_status"] == 200
            and runner.sha(raw.encode(meta["encoding"])) == meta["sha256"],
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        data[key] = html_recipe_text(raw)[0] if key.startswith("JCM") else json.loads(raw)
    for key, (ids, sizes) in GRAPHS.items():
        body = data[key]
        medium, solutions = body["data"]["medium"], body["data"]["solutions"]
        runner.require(
            body["status"] == 200
            and medium["id"] == key
            and medium["source"] == "JCM"
            and medium["link"] == context["sources"]["JCM" + key[1:]]["metadata"]["url"]
            and [s["id"] for s in solutions] == ids
            and [len(s["recipe"]) for s in solutions] == sizes,
            "Recipe identity/topology drift",
        )
        for si, section in enumerate(solutions):
            for ri, row in enumerate(section["recipe"]):
                runner.require(
                    row["optional"] == 0
                    and row.get("condition", "")
                    == (" clarified" if (key, si, ri) == ("J266", 0, 0) else ""),
                    "Unreviewed qualifier",
                )
    return data


class Review(prior.Review):
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
            not any(before.get(k) for k in ("evidence", "references", "variants", "solutions")),
            "Existing provenance/stock needs review",
        )
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.data = sources(self.context)
        self.claims, self.lineage, self.used = [], [], []
        # Exact reviewed paths exclude false product nodes before name lookup.
        for i, name in zip(LB[key], ("Tryptone", "Yeast extract", "Sodium chloride"), strict=True):
            node = before["ingredients"][i]
            runner.require(
                node["preferred_term"] == name
                and "LB Medium" in node["supplier_catalog"]["supplier_name"],
                "Product identity drift",
            )
        self.originals = {}
        for i, node in enumerate(before["ingredients"]):
            if i in LB[key]:
                continue
            name = node["preferred_term"]
            runner.require(name not in self.originals, "Ambiguous retained ingredient")
            self.originals[name] = ["ingredients", i]
        self.after["ingredients"], self.after["solutions"] = [], []

    def leaf(self, parent, source, si, ri, *, prepared=False):
        row = self.rows(source, si)[ri]
        name = row["compound"]
        if row["unit"] in {"ml", "L"} and name != "Distilled water":
            node, old = self.clone(name)
            value = shared.numeric(
                Decimal(str(row["amount"])) / (1000 if row["unit"] == "ml" else 1)
            )
            node["concentration"] = {"value": value, "unit": "L"}
            reason = f"Source liquid batch input: {row['amount']} {row['unit']} = {value} L. This is not grams per liter, a dose per final liter, or a density-based mass conversion."
            self.note(node, reason)
            p = self.append(parent, node)
            self.claim(
                p + ["concentration"],
                old + ["concentration"] if old else None,
                source,
                stocks.row_path(source, si, ri),
                "correct" if old else "add",
                "liquid_input",
                reason,
                p,
            )
            self.lineage_node(p, old, source, si, ri, "liquid_input")
        else:
            p = stocks.Review.leaf(self, parent, source, si, ri, prepared=prepared)
        _, old = self.clone(name)
        node = runner.get_node(self.after, p)
        if old and "[Merged 2 duplicates:" in runner.get_node(self.before, old).get("notes", ""):
            reason = "The earlier duplicate-summing note is superseded: main and trace-stock inputs are separate preparation scopes. This node retains only the source row at its stated stage."
            self.note(node, reason)
            self.claim(
                p + ["notes"],
                old + ["notes"],
                source,
                stocks.row_path(source, si, ri),
                "correct",
                "duplicate_scope",
                reason,
                p,
            )
        self.original_amount(p, si, ri)
        return p

    def original_table(self, si):
        original = "JCM" + self.key[1:]
        text = self.data[original]
        if si == 0:
            end = {
                "J266": "Mix ingredients",
                "J675": "Boil and cool",
                "J1203": "Dissolve ingredients",
            }[self.key]
            return original, text[: text.index(end)]
        if self.key == "J266":
            if si == 1:
                return original, text.split("Fatty acid mixture:", 1)[1].split("Adjust pH", 1)[0]
            if si == 2:
                return (
                    "JCM151",
                    self.data["JCM151"]
                    .split("Trace minerals:", 1)[1]
                    .split("Dissolve nitrilotriacetic", 1)[0],
                )
            return (
                "JCM197",
                self.data["JCM197"]
                .split("Trace vitamins:", 1)[1]
                .split("Trace mineral solution:", 1)[0],
            )
        runner.require(self.key == "J675", "Unreviewed local stock")
        headings = [
            "Mineral solution 1:",
            "Mineral solution 2:",
            "Fatty acid mixture:",
            "Copyright",
        ]
        return original, text.split(headings[si - 1], 1)[1].split(headings[si], 1)[0]

    def original_amount(self, p, si, ri, *, dose=False):
        row = self.rows(self.key, si)[ri]
        original, table = self.original_table(si)
        name = row.get("compound", row.get("solution"))
        aliases = {
            "Rumen fluid": "Rumen fluid, clarified (see below)",
            "L-Cysteine HCl x H2O": "L-Cysteine\u00b7HCl\u00b7H2O",
            "MnSO4 x n H2O": "MnSO4\u00b7xH2O",
            "Pyridoxine hydrochloride": "Pyridoxine\u00b7HCl",
            "Thiamine HCl": "Thiamine\u00b7HCl",
            "alpha-Methylbutyric acid": "\u03b1-Methylbutyric acid",
            "DL-2-Methylbutyric acid": "DL-2-Methyl butyric acid",
            "Trace minerals": "Trace minerals (see Medium No. 151)",
            "Trace vitamins": "Trace vitamins (see Medium No. 197)",
            "Fatty acid mixture": "Fatty acid mixture (see below)",
            "S I solution 6.0 g/L": "Mineral solution 1 (see below)",
            "Mineral solution 2": "Mineral solution 2 (see below)",
        }
        name = aliases.get(name, name.replace(" x ", "\u00b7").replace(" H2O", "H2O"))
        if row.get("attribute") in {"BD-Difco", "BD-BBL"}:
            name += " (" + row["attribute"] + ")"
        if self.key == "J1203" and ri == 13:
            name = "0.05% Resazurin solution"
        matches = list(
            re.finditer(re.escape(name) + r" ([0-9]+(?:\.[0-9]+)?) (mg|g|ml|L)(?= |$)", table)
        )
        runner.require(len(matches) == 1, "Missing/ambiguous original amount")
        match = matches[0]
        scale = {
            "g": ("mass", Decimal(1)),
            "mg": ("mass", Decimal("0.001")),
            "L": ("volume", Decimal(1)),
            "ml": ("volume", Decimal("0.001")),
        }
        a, b = scale[row["unit"]], scale[match.group(2)]
        runner.require(
            a[0] == b[0] and Decimal(str(row["amount"])) * a[1] == Decimal(match.group(1)) * b[1],
            "Source amount conflict",
        )
        self.corroborate(
            p + ["concentration" if dose else "notes"],
            original,
            match.group(),
            "Original table corroborates the source batch input and exact preparation scope. Provider stock g_l, when retained, is separately attributed to the API; this quote does not establish final volume.",
            [] if dose else p,
        )

    def dose(self, parent, si, ri, *, name=None, old=None):
        row = self.rows(self.key, si)[ri]
        node = (
            copy.deepcopy(runner.get_node(self.before, old))
            if old
            else {"preferred_term": name or row["solution"]}
        )
        value = shared.numeric(Decimal(str(row["amount"])) / 1000)
        runner.require(row["unit"] == "ml", "Stock dose drift")
        node.update(composition=[], concentration={"value": value, "unit": "L"})
        reason = f"Source preparation input: {row['amount']} ml = {value} L per receiving batch, not grams per liter or a dose per final liter."
        self.note(node, reason)
        p = self.append(parent, node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"] if old else None,
            self.key,
            stocks.row_path(self.key, si, ri),
            "correct" if old else "add",
            "batch_dose",
            reason,
            [],
        )
        self.lineage_node(p, old, self.key, si, ri, "batch_dose")
        self.original_amount(p, si, ri, dose=True)
        return p

    def stock_preparation(self, p, si, ti=0, *, old_step=None):
        sp = ["data", "solutions", si, "steps", ti, "step"]
        prep = runner.get_node(self.data[self.key], sp)
        node = runner.get_node(self.after, p)
        node["preparation_notes"] = prep
        self.claim(
            p + ["preparation_notes"],
            ["preparation_steps", old_step, "description"] if old_step is not None else None,
            self.key,
            sp,
            "correct" if old_step is not None else "add",
            "stock_preparation",
            "This procedure belongs only to this preparation, not to the root medium sequence.",
            [],
            snippet=prep,
        )
        return prep

    def titrant(self, p, name, prep, source):
        node = runner.get_node(self.after, p)
        node.setdefault("solutions", [])
        reason = (
            "Source-explicit stock pH-adjustment reagent with no fixed dose or numeric strength."
        )
        cp = self.append(
            p + ["solutions"], {"preferred_term": name, "composition": [], "notes": reason}
        )
        self.corroborate(cp + ["notes"], source, prep, reason, [])
        return cp

    def fill(self, p, si):
        for ri in range(len(self.rows(self.key, si))):
            self.leaf(p + ["composition"], self.key, si, ri)
        if self.key == "J266" and si in {1, 2}:
            self.stock_preparation(p, si, old_step=2 if si == 1 else 3)
            original = "JCM266" if si == 1 else "JCM151"
            original_prep = self.data[original]
            start = (
                "Adjust pH to 7.5 with concentrated NaOH solution."
                if si == 1
                else "Dissolve nitrilotriacetic acid"
            )
            quote = original_prep[
                original_prep.index(start) : original_prep.index("Copyright")
            ].strip()
            self.corroborate(
                p + ["preparation_notes"], original, quote, "Stock-only pH procedure.", []
            )
            self.titrant(
                p, "Concentrated NaOH solution" if si == 1 else "KOH solution", quote, original
            )

    def separate(self, ri, quote):
        row = self.rows(self.key, 0)[ri]
        name = row["compound"]
        reason = "Separate preparation: composition notes retain the receiving-batch contribution, not a stock-batch recipe. Stock solvent volume, numeric strength and addition volume are unspecified."
        if self.key == "J266":
            reason += " The source 5% label has unspecified percentage basis."
        p = self.append(
            ["solutions"],
            {
                "preferred_term": name + " separately prepared solution",
                "composition": [],
                "notes": reason,
                "preparation_notes": quote,
            },
        )
        self.corroborate(p + ["preparation_notes"], "JCM" + self.key[1:], quote, reason, [])
        cp = self.leaf(p + ["composition"], self.key, 0, ri, prepared=True)
        self.corroborate(cp + ["notes"], "JCM" + self.key[1:], quote, reason, cp)

    def resazurin(self):
        old = self.originals["Resazurin"]
        row = self.rows(self.key, 0)[13]
        runner.require(row["attribute"] == "0.05%", "Resazurin strength drift")
        p = self.dose(["solutions"], 0, 13, name="0.05% Resazurin solution")
        # The old quantity was the solution dose, not a resazurin stock strength.
        self.claim(
            p + ["concentration"],
            old + ["concentration"],
            self.key,
            stocks.row_path(self.key, 0, 13),
            "correct",
            "reagent_dose_relocation",
            "Move the misencoded 1 ml solution input onto its stock descriptor. The 0.05% basis is unspecified; do not calculate resazurin mass or stock strength.",
            [],
        )
        node = copy.deepcopy(runner.get_node(self.before, old))
        node.pop("concentration")
        reason = "Source reagent label: 0.05% Resazurin solution. Percentage basis is unspecified; no numeric resazurin concentration or stock-batch mass is asserted. The enclosing descriptor holds the 1 ml receiving-batch dose."
        self.note(node, reason)
        cp = self.append(p + ["composition"], node)
        self.claim(
            cp + ["notes"],
            None,
            self.key,
            stocks.row_path(self.key, 0, 13),
            "add",
            "unquantified_strength",
            reason,
            cp,
        )
        self.lineage_node(cp, old, self.key, 0, 13, "unquantified_strength")
        self.corroborate(cp + ["notes"], "JCM1203", "0.05% Resazurin solution 1.0 ml", reason, cp)

    def late_j675(self):
        original = "JCM675"
        for name, amount, unit, quote in [
            ("Na2CO3", "4.0", "g", "add 4.0 g Na2CO3"),
            ("L-Cysteine HCl x H2O", "500", "mg", "500 mg L-cysteine\u00b7HCl\u00b7H2O."),
        ]:
            reason = f"Source batch input: {amount} {unit}. Added after boiling/cooling under CO2, before distribution/autoclaving. No final volume or numeric final concentration is inferred."
            p = self.append(["ingredients"], {"preferred_term": name, "notes": reason})
            self.corroborate(p + ["notes"], original, quote, reason, p)
        quote = "1.0 ml fatty acid mixture (see below)"
        reason = "Source late addition: 1.0 ml = 0.001 L per receiving batch, not a dose per final liter. The fatty-acid stock is added under CO2 before distribution/autoclaving."
        p = self.append(
            ["solutions"],
            {
                "preferred_term": "Fatty acid mixture",
                "composition": [],
                "concentration": {"value": "0.001", "unit": "L"},
                "notes": reason,
            },
        )
        self.corroborate(p + ["concentration"], original, quote, reason, [])
        self.fill(p, 3)

    def remove_wrong_product(self):
        marker = "\n\nCommercial Product:"
        runner.require(marker in self.before["notes"], "Historical product provenance drift")
        self.after["notes"] = self.before["notes"].replace(
            marker,
            "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product:",
            1,
        )
        reason = "The earlier LB commercial-product expansion is superseded: the exact recipe specifies a methylbutyric acid input instead. Remove only the reviewed LB supplier nodes, preserving genuine peptone, yeast extract and salt entries. Restore the acid at its source preparation stage, without inventing a chemical ID."
        self.note(self.after, reason)
        for i in LB[self.key]:
            self.claim(
                ["notes"],
                ["ingredients", i, "concentration"],
                "JCM" + self.key[1:],
                None,
                "correct",
                "wrong_product_removed",
                reason + " Removed node: " + self.before["ingredients"][i]["preferred_term"] + ".",
                [],
                snippet=ACID[self.key][2],
            )

    def formulate(self):
        self.remove_wrong_product()
        special = {"J266": {0, 15, 16}, "J675": set(), "J1203": {13, 16}}[self.key]
        main = self.rows(self.key, 0)
        for ri, row in enumerate(main):
            if ri not in special and not row.get("solution_id"):
                self.leaf(["ingredients"], self.key, 0, ri)
        if self.key == "J266":
            p = self.dose(["solutions"], 0, 0, old=self.originals["Rumen fluid"])
            self.stock_preparation(p, 0, 1, old_step=1)
        for ri, row in enumerate(main):
            if row.get("solution_id"):
                si = GRAPHS[self.key][0].index(row["solution_id"])
                p = self.dose(["solutions"], 0, ri)
                self.fill(p, si)
        if self.key == "J266":
            text = self.data["JCM266"]
            quote = text[
                text.index("Separately autoclave") : text.index("Prior to inoculation")
            ].strip()
            for ri in (15, 16):
                self.separate(ri, quote)
            self.after["preparation_steps"] = [copy.deepcopy(self.before["preparation_steps"][0])]
            self.after["ph_value"] = 6.5
            reason = "Main-medium preparation specifies pH 6.5. API metadata min_pH/max_pH 7.5 conflicts and corresponds to the fatty-acid stock procedure; it is not selected for the medium."
            self.note(self.after, reason)
            self.claim(
                ["ph_value"],
                ["ph_value"],
                "JCM266",
                None,
                "correct",
                "ph_scope",
                reason,
                [],
                snippet="adjust pH to 6.5.",
            )
            self.claim(
                ["notes"],
                None,
                self.key,
                ["data", "medium"],
                "evidence_only",
                "metadata_conflict",
                reason,
                [],
            )
        elif self.key == "J675":
            self.late_j675()
        else:
            self.resazurin()
            text = self.data["JCM1203"]
            quote = text[
                text.index("Thereafter, add glucose") : text.index("Adjust pH of complete")
            ].strip()
            self.separate(16, quote)
        self.claim(
            ["preparation_steps"],
            ["preparation_steps"],
            self.key,
            ["data", "solutions", 0, "steps"],
            "correct" if self.key == "J266" else "evidence_only",
            "preparation_scope",
            "Keep the exact receiving-medium procedure and order; stock-only procedures are scoped to their descriptors. Gas atmospheres are not numeric dissolved concentrations.",
            [],
        )
        if self.key != "J266":
            self.claim(
                ["ph_value"],
                ["ph_value"],
                "JCM" + self.key[1:],
                None,
                "evidence_only",
                "ph_scope",
                "Receiving-medium pH from the recipe-specific preparation.",
                [],
                snippet="pH to 7.0",
            )

    def finish(self, timestamp):
        for c in self.claims:
            p = c["pointer"]
            c["new"] = copy.deepcopy(runner.get_node(self.after, p[:-1]).get(p[-1]))
        self.after["references"] = []
        for source in self.used:
            meta = self.context["sources"][source]["metadata"]
            self.after["references"].append(
                {
                    "reference": meta["url"],
                    "title": (
                        "Medium data"
                        if source.startswith("JCM")
                        else self.data[source]["data"]["medium"]["name"]
                    ),
                    "notes": f"source_type={'culture_collection_page' if source.startswith('JCM') else 'dataset'}; discovery_mode={'existing_record_reference' if source in {self.key, 'JCM' + self.key[1:]} else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year not supplied. Provider-declared stock rates are not independent final-volume measurements. Existing chemical groundings and organism-growth claims are not recertified.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Superseded the erroneous LB expansion, restored source-specific fatty acids, stock definitions and doses, and retained exact preparation-stage amounts with supporting snippets. Preserved genuine same-labelled ingredients, unrelated annotations and append-only history. No final volume, percent basis, density or chemical grounding inferred.",
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


def reports(plan, applied):
    out = HERE / "records"
    out.mkdir(exist_ok=True)
    for item in plan["records"]:
        lines = [
            "# JCM Ingredient Identity And Concentration Review",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Existing canonical reports remain historical. This follow-up corrects reviewed identity and preparation errors; provider stock rates, batch inputs and final-medium rates are distinct. Unspecified percentage bases, final volumes, doses and chemical groundings remain unresolved. Authors/year are unknown. See validation.json for actual terminal checks.",
            "",
            "| Ingredient/context | Old field | Current field | Old | New | Status | DOI/PURL | Exact snippet | Decision and locator |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in item["claims"]:
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(c[k])
                    for k in (
                        "ingredient",
                        "old_field",
                        "field",
                        "old",
                        "new",
                        "status",
                        "reference",
                        "snippet",
                        "explanation",
                    )
                )
                + " |"
            )
        (out / (item["key"] + ".md")).write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    parser.add_argument("--reports", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, args.plan, mode)
    if args.reports:
        reports(plan, mode != "preview")
    print(json.dumps(result))


if __name__ == "__main__":
    main()
