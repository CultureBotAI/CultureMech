#!/usr/bin/env python3
"""Repair DSMZ/KOMODO 403 and 751 with evidence and separate preparation scopes."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import re
from decimal import Decimal
from pathlib import Path

import repair_jcm_stock_preparations as stocks
import repair_methanogen_stock_boundaries as shared

from culturemech.curate.curation_event import record_curation_event

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-dsmz-albumin-preparations"
CONTEXT_SHA = "5767d9b9bed74466a4f490abe98b1d9735d7b864cfaec8af0d83b29520ee7cdb"
ACTION = "RESTORED_DSMZ_ALBUMIN_PREPARATIONS_AND_CONCENTRATION_SCOPES_WITH_EVIDENCE"
LB = {"K403": [13, 14, 15], "D403": [13, 14, 15], "K751": [6, 7, 8], "D751": [6, 7, 8]}


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    return json.loads(raw)


def sources(context):
    parsed = {}
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        number = key.removeprefix("DSMZ").removeprefix("D")
        url = (
            f"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium{number}.pdf"
            if key.startswith("DSMZ")
            else f"https://mediadive.dsmz.de/rest/medium/{number}"
        )
        runner.require(
            meta["url"] == meta["response_url"] == url
            and meta["http_status"] == 200
            and runner.sha(raw.encode(meta["encoding"])) == meta["sha256"],
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        parsed[key] = raw if key.startswith("DSMZ") else json.loads(raw)
    for number, ids, sizes in (
        ("403", [818, 819, 820, 821, 822], [4, 12, 2, 2, 1]),
        ("751", [1537], [10]),
    ):
        body = parsed["D" + number]
        runner.require(
            body["status"] == 200
            and body["data"]["medium"]["id"] == int(number)
            and body["data"]["medium"]["source"] == "DSMZ"
            and body["data"]["medium"]["link"]
            == context["sources"]["DSMZ" + number]["metadata"]["url"]
            and [s["id"] for s in body["data"]["solutions"]] == ids
            and [len(s["recipe"]) for s in body["data"]["solutions"]] == sizes
            and all(not r.get("optional") for s in body["data"]["solutions"] for r in s["recipe"]),
            "Source identity/topology drift",
        )
    return parsed


class Review(shared.Review):
    append = stocks.Review.append

    def __init__(self, before, key):
        context = frozen()
        super().__init__(before, key, context=context, parsed=sources(context))
        runner.require(not before.get("solutions"), "Existing stock reconciliation needed")
        self.number, self.api, self.pdf = key[1:], "D" + key[1:], "DSMZ" + key[1:]
        self.originals = {
            n["preferred_term"]: ["ingredients", i]
            for i, n in enumerate(before["ingredients"])
            if i not in LB[key]
        }
        for i, label in zip(LB[key], ("Tryptone", "Yeast extract", "Sodium chloride"), strict=True):
            n = before["ingredients"][i]
            runner.require(
                n["preferred_term"] == label
                and "LB Medium" in n["supplier_catalog"]["supplier_name"],
                "False-LB baseline drift",
            )
        self.after["ingredients"], self.after["solutions"] = [], []

    def row(self, si, ri):
        return self.data[self.api]["data"]["solutions"][si]["recipe"][ri]

    def sp(self, si, ri):
        return ["data", "solutions", si, "recipe", ri]

    def clone(self, name, *, retain=True):
        old = self.originals.get(name) if retain else None
        return (
            copy.deepcopy(runner.get_node(self.before, old)) if old else {"preferred_term": name}
        ), old

    def lineage_node(self, pointer, old, si, ri, kind):
        self.lineage.append(
            {
                "pointer": pointer,
                "old_pointer": old,
                "source": self.api,
                "source_pointer": self.sp(si, ri),
                "kind": kind,
            }
        )

    def pdf_excerpt(self, start, end=None):
        text = self.data[self.pdf]
        runner.require(text.count(start) == 1, "Ambiguous original excerpt")
        pos = text.index(start)
        stop = text.index(end, pos) + len(end) if end else text.find("\n", pos)
        return text[pos : stop if stop >= 0 else len(text)]

    def corroborate(self, pointer, snippet, reason, ep):
        self.claim(
            pointer,
            None,
            self.pdf,
            None,
            "evidence_only",
            "original_support",
            reason + " PDF page 1; layout extraction and page image inspected.",
            ep,
            snippet,
        )

    def original_row(self, pointer, si, ri, ep):
        row = self.row(si, ri)
        if self.number == "403":
            starts = {
                (1, 0): "CMRL 1066/10 x Glutamin",
                (1, 1): "Proteose peptone No 2",
                (1, 2): "Proteose tryptone",
                (1, 3): "Proteose yeastolate (TC)",
                (1, 4): "HEPES buffer (acid)",
                (1, 5): "Na-citrate",
                (1, 6): "Glucose (",
                (1, 7): "Na-pyruvate",
                (1, 8): "N-Acetylglucosamine",
                (1, 9): "MgCl2 x 6 H2O",
                (1, 10): "L-Glutamine",
                (1, 11): "Aqua bidest.",
            }
        else:
            starts = {
                (0, i): name
                for i, name in enumerate(
                    (
                        "Corn meal agar",
                        "Peptone from soy meal",
                        "K2HPO4 ",
                        "KH2PO4 ",
                        "MgSO4 x 7 H2O",
                        "Hemin (",
                        "Distilled water",
                        "20% bovine serum albumin",
                        "10% glucose",
                        "10% cysteine",
                    )
                )
            }
        if (si, ri) in starts:
            quote = self.pdf_excerpt(starts[(si, ri)])
            match = re.search(r"([0-9]+(?:\.[0-9]+)?)\s+(g|ml)\s*$", quote)
            runner.require(
                match
                and Decimal(match[1]) == Decimal(str(row["amount"]))
                and match[2] == row["unit"],
                "Original/provider amount conflict",
            )
        elif si == 2:
            quote = self.pdf_excerpt("Dissolve 14.0 g gelatine", "water,")
        elif si == 3:
            quote = self.pdf_excerpt("Dissolve 50.05 g bovine serum albumine", "water,")
        elif si == 4:
            quote = self.pdf_excerpt("Rabbit serum, inactivated", "86.0        ml")
        else:
            raise AssertionError("Unreviewed original row")
        self.corroborate(
            pointer,
            quote,
            "Original corroborates this preparation's batch input, not a measured final volume.",
            ep,
        )

    def leaf(self, parent, si, ri, *, retain=True, stock_rate=False):
        row = self.row(si, ri)
        node, old = self.clone(row["compound"], retain=retain)
        amount, unit = row["amount"], row["unit"]
        if "water" in row["compound"].lower():
            runner.require(unit == "ml", "Water unit drift")
            node["concentration"] = {
                "value": shared.numeric(Decimal(str(amount)) / 1000),
                "unit": "L",
            }
            kind = "water"
            reason = f"Source water batch input: {amount} ml / 1000 = {node['concentration']['value']} L in this preparation only, not a measured final volume."
            if old and node.get("notes"):
                reason += " Earlier duplicate-collapse notes describe the superseded flattened record; water is now split between preparations A, B and C."
        elif stock_rate:
            runner.require(unit == "g" and "g_l" in row, "Stock strength drift")
            node["concentration"] = {"value": shared.numeric(row["g_l"]), "unit": "G_PER_L"}
            kind = "stock_rate"
            reason = f"Source batch input: {amount} g. Retain provider-declared stock g_l={row['g_l']} only within Solution {'ABC'[si - 1]}, not a receiving-medium concentration or independently measured final stock volume."
        else:
            runner.require(unit == "g", "Batch mass unit drift")
            node.pop("concentration", None)
            kind = "batch_mass"
            reason = f"Source batch input: {amount} g. Final-medium volume is not established; withdraw the unsupported final g/L assertion without replacing it with an assumed one-liter value."
        if row.get("attribute"):
            reason += " Source qualifier: " + row["attribute"] + "."
        self.note(node, reason)
        p = self.append(parent, node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"] if old else None,
            self.api,
            self.sp(si, ri),
            (
                "correct"
                if old and "concentration" in node
                else "remove_unsupported" if old else "add"
            ),
            kind,
            reason,
            p,
        )
        self.lineage_node(p, old, si, ri, kind)
        self.original_row(
            p + (["concentration"] if "concentration" in node else ["notes"]), si, ri, p
        )
        return p

    def dose(self, parent, si, ri, *, label=None, retain=False):
        row = self.row(si, ri)
        name = row.get("compound", row.get("solution"))
        node, old = self.clone(name, retain=retain)
        if label:
            node["preferred_term"] = label
        runner.require(row["unit"] == "ml", "Dose unit drift")
        node.update(
            composition=[],
            concentration={
                "value": shared.numeric(Decimal(str(row["amount"])) / 1000),
                "unit": "L",
            },
        )
        reason = f"Source batch dose: {row['amount']} ml / 1000 = {node['concentration']['value']} L per receiving batch, not g/L or a per-liter dose."
        if row.get("attribute"):
            reason += " Source product/stock qualifier: " + row["attribute"] + "."
        self.note(node, reason)
        p = self.append(parent, node)
        self.claim(
            p + ["concentration"],
            old + ["concentration"] if old else None,
            self.api,
            self.sp(si, ri),
            "correct" if old else "add",
            "batch_dose",
            reason,
            [],
        )
        self.lineage_node(p, old, si, ri, "batch_dose")
        if si > 0 or self.number == "751":
            self.original_row(p + ["concentration"], si, ri, [])
        return p

    def procedure(self, p, si, index=0):
        text = self.data[self.api]["data"]["solutions"][si]["steps"][index]["step"].strip()
        runner.get_node(self.after, p)["preparation_notes"] = text
        self.claim(
            p + ["preparation_notes"],
            None,
            self.api,
            ["data", "solutions", si, "steps", index],
            "add",
            "stock_preparation",
            "Instruction applies only to this preparation; no pore size is specified.",
            [],
            snippet=json.dumps(text, ensure_ascii=True)[1:-1],
        )

    def bsk(self):
        for ri in range(3):
            self.dose(["solutions"], 0, ri)
        self.dose(["solutions"], 4, 0, retain=True)
        a, b, c, d = (["solutions", i] for i in range(4))
        for p in (a, b, c):
            quote = self.pdf_excerpt("Combine the warm", "after filtration.")
            self.corroborate(
                p + ["notes"],
                quote,
                "Original names the combined preparations; numeric dosing is separately provider-declared.",
                [],
            )
        self.lineage_node(d, None, 0, 3, "same_serum_dose")
        self.claim(
            d + ["concentration"],
            None,
            self.api,
            self.sp(0, 3),
            "evidence_only",
            "same_serum_dose",
            "Solution D is the same 86 ml inactivated rabbit-serum input, not an additional dose. Provider serum mmol_l is not used.",
            [],
        )
        for si, p in ((1, a), (2, b), (3, c)):
            for ri, row in enumerate(self.data[self.api]["data"]["solutions"][si]["recipe"]):
                if si == 1 and ri == 0:
                    self.after["solutions"][0]["solutions"] = []
                    self.dose(a + ["solutions"], si, ri, retain=True)
                else:
                    self.leaf(
                        p + ["composition"],
                        si,
                        ri,
                        retain=not (si > 1 and "water" in row["compound"].lower()),
                        stock_rate="water" not in row["compound"].lower(),
                    )
            self.procedure(p, si)
        node, old = self.clone("NaOH")
        node["concentration"] = {"value": "5", "unit": "MOLAR"}
        reason = "Explicit 5 M NaOH titrant strength for adjusting Solution A to pH 7.6, not a receiving-medium concentration. No fixed titrant dose is specified."
        self.note(node, reason)
        titrant = {"preferred_term": "NaOH solution (5 M)", "composition": [node], "notes": reason}
        p = self.append(a + ["solutions"], titrant)
        quote = self.pdf_excerpt("Stir slowly at", "Filter sterilize.")
        self.claim(
            p + ["composition", 0, "concentration"],
            old + ["concentration"] if old else None,
            self.pdf,
            None,
            "correct" if old else "add",
            "titrant_strength",
            reason,
            p + ["composition", 0],
            quote,
        )
        self.corroborate(p + ["notes"], quote, reason, [])
        if old:
            self.lineage.append(
                {
                    "pointer": p + ["composition", 0],
                    "old_pointer": old,
                    "source": self.pdf,
                    "source_pointer": None,
                    "kind": "titrant_strength",
                }
            )
        self.corroborate(
            a + ["preparation_notes"],
            quote,
            "pH 7.6, 4-10 C and three hours belong to Solution A.",
            [],
        )
        self.corroborate(
            b + ["preparation_notes"],
            self.pdf_excerpt("Dissolve 14.0", "115\uf0b0C."),
            "Solution B is autoclaved for 15 minutes at 115 C, not a default 121 C cycle.",
            [],
        )
        self.corroborate(
            c + ["preparation_notes"],
            self.pdf_excerpt("Dissolve 50.05", "Sigma A7409."),
            "Fraction V and the Sigma A7409 replacement are source-specific alternatives, not simultaneous components.",
            [],
        )
        if "ph_value" in self.after:
            self.after.pop("ph_value")
            self.claim(
                ["ph_value"],
                ["ph_value"],
                self.pdf,
                None,
                "remove_unsupported",
                "ph_scope",
                "Move the previously global pH 7.6 assertion into Solution A preparation; the source does not specify final-medium pH.",
                [],
                quote,
            )
        mix = self.data[self.api]["data"]["solutions"][0]["steps"][0]["step"]
        self.after["preparation_steps"] = [{"step_number": 1, "action": "MIX", "description": mix}]
        self.corroborate(
            ["preparation_steps"],
            self.pdf_excerpt("Combine the warm", "after filtration."),
            "Warm combination at 37 C and filtration, with Solution B optionally added after filtration. No pore size is specified.",
            [],
        )
        alternative = self.data[self.api]["data"]["solutions"][0]["steps"][1]["step"]
        self.note(self.after, "Source alternative, not an extra preparation step: " + alternative)
        self.corroborate(
            ["notes"],
            self.pdf_excerpt("Alternatively, buy", "by filtration."),
            "Keep commercial BSK-H replacement as a distinct source alternative; do not add it to this formulation.",
            [],
        )

    def sc(self):
        for ri in (0, 1, 2, 3, 4, 6):
            self.leaf(["ingredients"], 0, ri)
        for ri in (5, 7, 8, 9):
            row = self.row(0, ri)
            p = self.dose(["solutions"], 0, ri, label=row["compound"] + " stock")
            node, old = self.clone(row["compound"])
            node.pop("concentration", None)
            reason = (
                "Stock label: "
                + row["attribute"]
                + ". Percentage basis is unspecified; no numeric stock strength or final-medium concentration is asserted."
            )
            if ri == 7:
                reason += " Bovine serum albumin is fraction V, not LB broth."
            self.note(node, reason)
            cp = self.append(p + ["composition"], node)
            self.claim(
                cp + ["concentration" if old else "notes"],
                old + ["concentration"] if old else None,
                self.api,
                self.sp(0, ri),
                "remove_unsupported" if old else "add",
                "unknown_stock_strength",
                reason,
                cp,
            )
            self.lineage_node(cp, old, 0, ri, "unknown_stock_strength")
            self.original_row(cp + ["notes"], 0, ri, cp)
            if ri == 5:
                solvent = {
                    "preferred_term": "NaOH solution (0.05 N)",
                    "composition": [
                        {
                            "preferred_term": "NaOH",
                            "notes": "Source solvent strength 0.05 N; normality is not converted to molarity.",
                        }
                    ],
                    "notes": "Hemin-stock solvent only; fixed solvent dose and percentage basis are not supplied.",
                }
                runner.get_node(self.after, p)["solutions"] = [solvent]
                quote = self.pdf_excerpt("Hemin (")
                self.corroborate(
                    p + ["solutions", 0, "notes"],
                    quote,
                    "Solvent belongs only to the hemin stock, not to the medium as a separate dose.",
                    [],
                )
                self.corroborate(
                    p + ["solutions", 0, "composition", 0, "notes"],
                    quote,
                    "Retain the explicit normality in notes without inventing a schema unit.",
                    p + ["solutions", 0, "composition", 0],
                )
            else:
                prep = "Filter-sterilize this stock separately; add after the basal medium has been autoclaved and cooled to 50 C. No filter pore size is given."
                runner.get_node(self.after, p)["preparation_notes"] = prep
                self.corroborate(
                    p + ["preparation_notes"],
                    self.pdf_excerpt("Adjust pH", "components:"),
                    "Applies to the following albumin, glucose and cysteine rows only, not hemin.",
                    [],
                )
        self.after["preparation_steps"] = [
            {
                "step_number": 1,
                "action": "ADJUST_PH",
                "description": "Adjust the basal medium to pH 6.6 before autoclaving.",
            },
            {
                "step_number": 2,
                "action": "AUTOCLAVE",
                "description": "Autoclave the basal medium, including the hemin input; the source gives no fixed cycle temperature or duration.",
            },
            {
                "step_number": 3,
                "action": "COOL",
                "description": "Cool to 50 C, then add the separately filter-sterilized albumin, glucose and cysteine stocks.",
            },
        ]
        quote = self.pdf_excerpt("Adjust pH", "components:")
        self.corroborate(
            ["preparation_steps"],
            quote,
            "Source boundary precedes recipe_order 8, the albumin row. Do not autoclave the three subsequent stocks or filter hemin by analogy.",
            [],
        )
        self.corroborate(
            ["ph_value"], quote, "Retain source pH 6.6 for the basal medium before autoclaving.", []
        )
        modifications = [
            "Omit corn meal agar.",
            "Use KH2PO4 1.5 g per batch instead of 1 g.",
            "Use K2HPO4 0.5 g per batch instead of 1 g.",
        ]
        self.after["variants"] = [
            {
                "name": "Liquid SC medium",
                "relationship": "PHYSICAL_STATE_VARIANT",
                "description": "DSMZ 751 liquid formulation with altered phosphate batch inputs; not a sequential change to the agar base recipe.",
                "modifications": modifications,
                "purpose": "Liquid medium",
            }
        ]
        self.corroborate(
            ["variants", 0, "modifications"],
            self.pdf_excerpt("For liquid medium", "K2HPO4, 0.5 g."),
            "All three modifications belong together. Grams per batch are not assumed grams per final liter.",
            ["variants", 0],
        )

    def formulate(self):
        old_notes = self.before.get("notes", "")
        provenance, separator, rejected = old_notes.partition("Commercial Product: LB Medium")
        runner.require(separator, "Missing historical LB provenance")
        self.after["notes"] = (
            provenance.rstrip()
            + "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product: LB Medium"
            + rejected
        )
        self.note(
            self.after,
            "The LB constituent expansion is withdrawn: the exact DSMZ formulation specifies bovine serum albumin instead. Source batch, stock and receiving-medium scopes are separate; chemical groundings and growth claims are not recertified.",
        )
        self.bsk() if self.number == "403" else self.sc()
        quote = (
            self.pdf_excerpt("Dissolve 50.05", "Sigma A7409.")
            if self.number == "403"
            else self.pdf_excerpt("20% bovine serum albumin")
        )
        for i in LB[self.key]:
            self.claim(
                ["notes"],
                ["ingredients", i, "concentration"],
                self.pdf,
                None,
                "remove_unsupported",
                "false_lb_removed",
                "Remove this false LB constituent and its concentration; restore the source-specific albumin preparation without importing LB groundings.",
                [],
                quote,
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
                    "title": (
                        self.data[self.pdf].splitlines()[0]
                        if key == self.pdf
                        else self.data[self.api]["data"]["medium"]["name"]
                    ),
                    "notes": f"source_type={'culture_collection_page' if key == self.pdf else 'dataset'}; discovery_mode=existing_record_reference; accessed_on={meta['accessed_at'][:10]}; capture_sha256={meta['sha256']}. Authors and publication year are not supplied. The PDF copyright year is not treated as publication year. Provider stock g_l values are attributed at stock scope only, not independent final-volume measurements.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.pdf]["metadata"]["url"],
            notes="Restore source-specific albumin, withdraw false LB inputs, separate preparation doses and stock compositions, and attach exact evidence for changed claims. Preserve IDs, unrelated groundings and earlier history. Unknown percentage bases and final-medium volume remain unknown.",
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
            "# DSMZ Preparation Follow-Up",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "The historical canonical report is unchanged. This supplement accounts for every old quantity and source row. Unknown percentage bases, final volumes, authors and publication years remain unknown. See validation receipts for actual checks; this report is not all-record completion.",
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
