#!/usr/bin/env python3
"""Restore source-specific albumin identities and reagent inputs in J201/J220."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from decimal import Decimal
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_m689_stocks as prior
import repair_methanogen_stock_boundaries as shared

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import html_recipe_text

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-jcm-albumin-inputs"
CONTEXT_SHA = "1d17c31b8c9f8b24725bfd290a9a096ff9db44c0ff6c3f12a142785929a761cb"
ACTION = "RESTORED_JCM_ALBUMIN_IDENTITIES_AND_REAGENT_INPUTS_WITH_EVIDENCE"
LB = {"J201": [2, 3, 4], "J220": [6, 7, 8]}
ORIGINAL_ROWS = [
    "Corn meal agar (BD-Difco) 17.0 g",
    "Phytone peptone (BD-BBL) 8.0 g",
    "K2HPO4 1.0 g",
    "KH2PO4 1.0 g",
    "MgSO4\u00b77H2O 0.2 g",
    "Hemin (0.1% in 0.05 N NaOH) 15.0 ml",
    "20% Bovine serum albumin, fraction V 10.0 ml",
    "50% Glucose 1.0 ml",
    "10% Cysteine 10.0 ml",
    "Distilled water 1.0 L",
]


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
    runner.require(
        context["source_issues"] == {"JCM201": "source_unavailable: JCM returned no recipe"}
        and "Nothing found." in data["JCM201"],
        "Original source availability changed",
    )
    for key, sid in (("J201", 3866), ("J220", 3888)):
        body = data[key]
        medium, sections = body["data"]["medium"], body["data"]["solutions"]
        runner.require(
            body["status"] == 200
            and medium["id"] == key
            and medium["source"] == "JCM"
            and medium["link"] == context["sources"]["JCM" + key[1:]]["metadata"]["url"]
            and len(sections) == 1
            and sections[0]["id"] == sid
            and len(sections[0]["recipe"]) == 10,
            "Recipe identity/topology drift",
        )
        for ri, row in enumerate(sections[0]["recipe"]):
            qualifier = {("J201", 2): " Fraction V", ("J220", 6): " fraction V"}.get((key, ri), "")
            runner.require(
                row["optional"] == 0 and row.get("condition", "") == qualifier,
                "Unreviewed qualifier",
            )
    return data


class Review(prior.Review):
    def __init__(self, before, key):
        context = frozen()
        shared.Review.__init__(self, before, key, context=context, parsed=sources(context))
        runner.require(not before.get("solutions"), "Existing solutions need reconciliation")
        for i, name in zip(LB[key], ("Tryptone", "Yeast extract", "Sodium chloride"), strict=True):
            node = before["ingredients"][i]
            runner.require(
                node["preferred_term"] == name
                and "LB Medium" in node["supplier_catalog"]["supplier_name"],
                "Product identity drift",
            )
        self.originals = {
            n["preferred_term"]: ["ingredients", i]
            for i, n in enumerate(before["ingredients"])
            if i not in LB[key]
        }
        self.after["ingredients"], self.after["solutions"] = [], []

    def original(self, p, ri, ep):
        if self.key == "J220":
            row = self.rows(self.key, 0)[ri]
            amount, unit = [
                (17, "g"),
                (8, "g"),
                (1, "g"),
                (1, "g"),
                (0.2, "g"),
                (15, "ml"),
                (10, "ml"),
                (1, "ml"),
                (10, "ml"),
                (1000, "ml"),
            ][ri]
            runner.require(
                row["amount"] == amount and row["unit"] == unit, "Original/API amount conflict"
            )
            self.corroborate(
                p,
                "JCM220",
                ORIGINAL_ROWS[ri],
                "Original JCM220 row corroborates the exact material, batch amount and preparation label; not a measured final volume or specified percentage basis.",
                ep,
            )

    def leaf(self, ri):
        p = stocks.Review.leaf(self, ["ingredients"], self.key, 0, ri)
        row = self.rows(self.key, 0)[ri]
        if row.get("condition"):
            reason = "Source material qualifier: " + row["condition"].strip() + "."
            self.note(runner.get_node(self.after, p), reason)
            self.claim(
                p + ["notes"],
                None,
                self.key,
                stocks.row_path(self.key, 0, ri),
                "evidence_only",
                "material_qualifier",
                reason,
                p,
            )
        self.original(p + ["notes"], ri, p)

    def reagent(self, ri, label, *, cmrl=False):
        row = self.rows(self.key, 0)[ri]
        runner.require(row["unit"] == "ml", "Liquid input unit drift")
        name = row["compound"]
        old = self.originals.get(name)
        value = shared.numeric(Decimal(str(row["amount"])) / 1000)
        node = (
            copy.deepcopy(runner.get_node(self.before, old)) if cmrl else {"preferred_term": label}
        )
        node.update(composition=[], concentration={"value": value, "unit": "L"})
        reason = f"Source preparation input: {row['amount']} ml = {value} L per receiving batch, not grams per liter or a dose per final liter."
        if cmrl:
            reason += " Source product qualifier: Gibco 330-1540. The source does not provide this product's composition or numeric stock strength."
        else:
            reason += f" Source reagent label: {row['attribute']}; percentage basis and stock preparation amounts are unspecified."
        if row.get("condition"):
            reason += " Source material qualifier: " + row["condition"].strip() + "."
        self.note(node, reason)
        p = self.append(["solutions"], node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"] if old else None,
            self.key,
            stocks.row_path(self.key, 0, ri),
            "correct" if old else "add",
            "batch_dose",
            reason,
            [],
        )
        self.lineage_node(p, old if cmrl else None, self.key, 0, ri, "batch_dose")
        self.original(p + ["concentration"], ri, [])
        if cmrl:
            return
        component, op = self.clone(name)
        component.pop("concentration", None)
        note = f"Source reagent label: {row['attribute']}. Percentage basis is unspecified; no numeric stock strength or stock-batch mass is asserted. The enclosing descriptor holds the receiving-batch volume."
        if row.get("condition"):
            note += " Source material qualifier: " + row["condition"].strip() + "."
        self.note(component, note)
        cp = self.append(p + ["composition"], component)
        self.claim(
            cp + ["notes"],
            None,
            self.key,
            stocks.row_path(self.key, 0, ri),
            "evidence_only" if op else "add",
            "unquantified_strength",
            note,
            cp,
        )
        self.lineage_node(cp, op, self.key, 0, ri, "unquantified_strength")
        self.original(cp + ["notes"], ri, cp)
        if ri == 5:
            self.hemin_solvent(p)
        else:
            prep = self.data[self.key]["data"]["solutions"][0]["steps"][1]["step"]
            node["preparation_notes"] = prep
            self.claim(
                p + ["preparation_notes"],
                None,
                self.key,
                ["data", "solutions", 0, "steps", 1, "step"],
                "add",
                "separate_filtration",
                "Separate stock filtration and aseptic addition; no pore size or stock recipe is inferred.",
                [],
                snippet=prep,
            )
            self.corroborate(
                p + ["preparation_notes"],
                "JCM220",
                prep,
                "Original stock filtration instruction.",
                [],
            )

    def hemin_solvent(self, p):
        node = runner.get_node(self.after, p)
        node["solutions"] = []
        reason = "Source hemin-stock solvent: 0.05 N NaOH. Its addition volume and stock preparation amounts are unspecified. Normality is not converted to molarity and is not a final-medium concentration."
        sp = self.append(
            p + ["solutions"],
            {"preferred_term": "NaOH solution (0.05 N)", "composition": [], "notes": reason},
        )
        cp = self.append(sp + ["composition"], {"preferred_term": "NaOH", "notes": reason})
        for pointer, ep in ((sp + ["notes"], []), (cp + ["notes"], cp)):
            self.claim(
                pointer,
                None,
                self.key,
                stocks.row_path(self.key, 0, 5),
                "add",
                "stock_solvent",
                reason,
                ep,
            )
            self.original(pointer, 5, ep)

    def late_j201(self):
        sp = ["data", "solutions", 0, "steps", 0, "step"]
        quote = "Add 200 ml of 7% gelatin."
        reason = "Source late preparation input: 200 ml = 0.2 L of 7% gelatin per receiving batch, added before filtration of the entire medium. Percentage basis and stock mass/solvent recipe are unspecified."
        p = self.append(
            ["solutions"],
            {
                "preferred_term": "7% gelatin solution",
                "composition": [],
                "concentration": {"value": "0.2", "unit": "L"},
                "notes": reason,
            },
        )
        self.claim(
            p + ["concentration"], None, self.key, sp, "add", "late_dose", reason, [], snippet=quote
        )
        cp = self.append(
            p + ["composition"],
            {
                "preferred_term": "Gelatin",
                "notes": "Source label: 7% gelatin. Percentage basis is unspecified; no numeric stock strength or stock-batch mass is asserted.",
            },
        )
        self.claim(
            cp + ["notes"],
            None,
            self.key,
            sp,
            "add",
            "unquantified_strength",
            runner.get_node(self.after, cp)["notes"],
            cp,
            snippet=quote,
        )
        quote = "Add sterile rabbit serum to final concentration of 6%."
        reason = "Source specifies sterile rabbit serum at final 6%, but the percentage basis and corresponding fixed addition volume are unspecified. Retain the literal label without asserting a numeric percentage, stock strength or dose. Serum is added after filtration of the medium."
        p = self.append(
            ["solutions"],
            {
                "preferred_term": "Sterile rabbit serum",
                "composition": [],
                "notes": reason,
                "preparation_notes": quote,
            },
        )
        self.claim(
            p + ["notes"],
            None,
            self.key,
            sp,
            "add",
            "unquantified_serum",
            reason,
            [],
            snippet=quote,
        )
        self.claim(
            p + ["preparation_notes"],
            None,
            self.key,
            sp,
            "add",
            "late_preparation",
            reason,
            [],
            snippet=quote,
        )

    def formulate(self):
        marker = "\n\nCommercial Product:"
        runner.require(marker in self.before["notes"], "Historical provenance drift")
        self.after["notes"] = self.before["notes"].replace(
            marker,
            "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product:",
            1,
        )
        reason = "The exact source specifies albumin fraction V, not LB broth. Remove only the reviewed LB supplier nodes and restore the source material at its preparation stage without inventing chemical grounding."
        self.note(self.after, reason)
        for i in LB[self.key]:
            self.claim(
                ["notes"],
                ["ingredients", i, "concentration"],
                self.key,
                stocks.row_path(self.key, 0, 2 if self.key == "J201" else 6),
                "correct",
                "wrong_product_removed",
                reason,
                [],
            )
        for ri, row in enumerate(self.rows(self.key, 0)):
            if row["unit"] in {"g", "mg"} or row["compound"] == "Distilled water":
                self.leaf(ri)
        if self.key == "J201":
            self.reagent(0, "CMRL 1066", cmrl=True)
            self.late_j201()
            self.after["preparation_steps"][0]["action"] = "FILTER"
            self.note(
                self.after,
                "The linked original JCM201 endpoint returned no recipe in the pinned capture. Formulation assertions here are provider-backed, not original-page corroborated.",
            )
        else:
            for ri, label in (
                (5, "Hemin solution (0.1% in 0.05 N NaOH)"),
                (6, "20% bovine serum albumin fraction V solution"),
                (7, "50% glucose solution"),
                (8, "10% cysteine solution"),
            ):
                self.reagent(ri, label)
        self.claim(
            ["preparation_steps"],
            ["preparation_steps"],
            self.key,
            ["data", "solutions", 0, "steps"],
            "correct" if self.key == "J201" else "evidence_only",
            "preparation_scope",
            "Retain the source procedure and order. FILTER represents explicit filtration without asserting the 0.22 micrometer pore size encoded by FILTER_STERILIZE.",
            [],
        )
        self.claim(
            ["ph_value"],
            ["ph_value"],
            self.key,
            ["data", "solutions", 0, "steps", 0, "step"],
            "evidence_only",
            "ph_scope",
            "Receiving-medium pH is explicitly given by the preparation.",
            [],
            snippet="Adjust pH to " + ("7.6." if self.key == "J201" else "6.6."),
        )
        if self.key == "J220":
            self.corroborate(["notes"], "JCM220", ORIGINAL_ROWS[6], reason, [])
            self.corroborate(
                ["ph_value"], "JCM220", "Adjust pH to 6.6.", "Original receiving-medium pH.", []
            )

    def finish(self, timestamp):
        for c in self.claims:
            c["new"] = copy.deepcopy(
                runner.get_node(self.after, c["pointer"][:-1]).get(c["pointer"][-1])
            )
        self.after["references"] = []
        for source in self.used:
            meta = self.context["sources"][source]["metadata"]
            notes = f"source_type={'culture_collection_page' if source.startswith('JCM') else 'dataset'}; discovery_mode=existing_record_reference; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year not supplied. Batch inputs are not independently verified final concentrations. Existing chemical groundings and organism-growth claims are not recertified."
            if self.key == "J201":
                unavailable = self.context["sources"]["JCM201"]["metadata"]
                notes += f" Original-source availability: {unavailable['url']} returned 'Nothing found.'; accessed={unavailable['accessed_at']}; capture_sha256={unavailable['sha256']}. This is an access-status observation, not original formulation evidence."
            self.after["references"].append(
                {
                    "reference": meta["url"],
                    "title": (
                        "Medium data"
                        if source.startswith("JCM")
                        else self.data[source]["data"]["medium"]["name"]
                    ),
                    "notes": notes,
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Removed false LB expansions and restored albumin fraction V, source batch inputs, reagent doses and late preparations with exact evidence. Unknown percentage bases, final volumes, stock strengths and chemical groundings remain unresolved. The JCM201 original-source access gap is disclosed, not treated as corroboration.",
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
            "# Albumin Identity And Concentration Follow-Up",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Historical canonical reports remain unchanged. Every old quantity is accounted below. Percentage bases, final volumes and chemical groundings are not inferred. J201 uses the available MediaDive recipe; the unavailable original page is not formulation evidence. Authors/year are unknown. See validation.json for actual terminal checks.",
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
