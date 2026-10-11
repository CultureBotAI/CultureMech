#!/usr/bin/env python3
"""Guarded repair of 13 inspected Middlebrook ingredient/stock encodings."""

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

runner = shared.runner
ROOT = shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-middlebrook-stages"
CONTEXT_SHA = "4836291dddb141d452fc5c01b0730d3badce0759dd54a8e7ba0446e7aff478d7"
ACTION = "RESTORED_MIDDLEBROOK_INGREDIENT_AND_STOCK_SCOPES_WITH_EVIDENCE"
KEYS = {
    "D857",
    "M2403",
    "M2328",
    "M2879",
    "M2399",
    "M1946",
    "M2407",
    "M2401",
    "M2402",
    "M2397",
    "M2880",
    "M2400",
    "M2404",
}


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    runner.require({r["key"] for r in context["records"]} == KEYS, "Inventory drift")
    return context


def sources(context):
    data, texts = {}, {}
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        runner.require(
            runner.sha(raw.encode(meta.get("encoding", "utf-8"))) == meta["sha256"]
            and meta["url"] == meta["response_url"]
            and meta["http_status"] == 200,
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        if key == "NBRC1219":
            soup = BeautifulSoup(raw, "html.parser")
            for tag in soup(["script", "style", "noscript", "template"]):
                tag.decompose()
            texts[key] = " ".join(soup.get_text(" ").split())
            runner.require(
                "Distilled water 900 mL" in texts[key] and "1219" in texts[key],
                "NBRC identity/quantity drift",
            )
        else:
            texts[key] = raw
            if key != "DSMZ857":
                data[key] = json.loads(raw)
        if key.startswith("M"):
            runner.require(
                data[key]["meta"]["gm"] == f"http://togomedium.org/medium/{key}",
                "TOGO identity drift",
            )
        elif key == "D857":
            runner.require(
                data[key]["data"]["medium"]["id"] == 857
                and data[key]["data"]["medium"]["source"] == "DSMZ",
                "DSMZ identity drift",
            )
            runner.require(
                [s["id"] for s in data[key]["data"]["solutions"]] == [1749, 1750],
                "DSMZ stock drift",
            )
        elif key == "DSMZ857":
            runner.require(raw.startswith("857. BACTO MIDDLEBROOK 7H9 BROTH"), "PDF identity drift")
            runner.require(
                runner.sha(read_pdf_capture(meta)) == meta["pdf_sha256"],
                "PDF binary drift",
            )
    return data, texts


def number(value):
    return format(Decimal(str(value)).normalize(), "f")


def label_key(value):
    return value.strip().strip("*").strip().casefold()


class Review(shared.Review):
    append = stocks.Review.append
    claim = prior.Review.claim

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
            not any(before.get(k) for k in ("evidence", "references", "variants")),
            "Existing evidence needs reconciliation",
        )
        self.data, self.texts = sources(self.context)
        self.key, self.before, self.after = key, before, copy.deepcopy(before)
        self.claims, self.lineage, self.used = [], [], []
        self.originals, self.lb = {}, []
        for field in ("ingredients", "solutions"):
            for i, node in enumerate(before.get(field, [])):
                p = [field, i]
                if "LB Medium" in node.get("supplier_catalog", {}).get("supplier_name", ""):
                    self.lb.append(p)
                else:
                    name = label_key(node["preferred_term"])
                    runner.require(name not in self.originals, "Ambiguous old identity")
                    self.originals[name] = p
        runner.require(
            [runner.get_node(before, p)["preferred_term"] for p in self.lb]
            == ["Tryptone", "Yeast extract", "Sodium chloride"],
            "False-LB baseline drift",
        )
        self.after["ingredients"], self.after["solutions"] = [], []

    def excerpt(self, sp):
        excerpt = json_excerpt(self.context["sources"][self.key]["raw"], sp)
        if sp[:1] == ["components"]:
            positions = [
                excerpt.find('"' + k + '"') for k in ("gmo_id", "roles", "reference_media_id")
            ]
            stops = [i for i in positions if i > 0]
            if stops:
                excerpt = excerpt[: min(stops)].rstrip().rstrip(",")
        return excerpt

    def emit(
        self,
        parent,
        name,
        sp,
        quantity,
        reason,
        kind,
        *,
        descriptor=False,
        old=None,
        source=None,
        snippet=None,
    ):
        source = source or self.key
        old = self.originals.get(label_key(name)) if old is None else old
        node = (
            copy.deepcopy(runner.get_node(self.before, old))
            if old
            else {"preferred_term": name.strip()}
        )
        runner.require(
            label_key(node["preferred_term"]) == label_key(name), "Ingredient identity drift"
        )
        if quantity is None:
            node.pop("concentration", None)
        else:
            node["concentration"] = quantity
        if descriptor:
            runner.require(not node.get("composition"), "Existing stock requires reconciliation")
            node["composition"] = []
            node["name"] = node["preferred_term"]
        if "Merged" in node.get("notes", ""):
            reason += " Earlier merged-quantity text is retained only as historical provenance; the separated source stages supersede it."
        self.note(node, reason)
        p = self.append(parent, node)
        self.lineage.append(
            {"pointer": p, "old_pointer": old, "source": source, "source_pointer": sp, "kind": kind}
        )
        excerpt = snippet if snippet is not None else self.excerpt(sp)
        evidence = [] if descriptor else p
        for field in ("concentration", "notes") + (("name",) if descriptor else ()):
            self.claim(
                p + [field],
                old + [field] if old else None,
                source,
                sp,
                "correct" if old else "add",
                kind,
                reason,
                evidence,
                excerpt,
            )
        return p

    def amount(self, row, context):
        amount, unit = row["volume"], row["unit"]
        reason = f"Source amount: {amount} {unit}; scope: {context}."
        if unit in {"ml", "L"}:
            quantity = {
                "value": number(Decimal(str(amount)) / (1000 if unit == "ml" else 1)),
                "unit": "L",
            }
            reason += f" Volume-only input/dose, not a final-volume marker; {amount} {unit} = {quantity['value']} L."
            kind = "batch_volume"
        elif unit == "% (v/v)":
            quantity = {"value": number(amount), "unit": "PERCENT_V_V"}
            reason += " The percentage basis is explicitly volume/volume."
            kind = "explicit_percent"
        elif unit == "%":
            quantity = None
            reason += " Percentage basis is unspecified; the earlier w/v or g/L assertion is withdrawn, not replaced with an assumed basis."
            kind = "unknown_percent_basis"
        else:
            runner.require(unit in {"g", "mg"}, "Unreviewed source unit")
            quantity = None
            reason += " This table does not give an explicit final-volume denominator. Preserve the exact mass here; no g/L conversion is asserted. The schema has no mass-only concentration unit."
            kind = "batch_mass"
        return quantity, reason, kind

    def togo(self):
        groups = self.data[self.key]["components"]
        roots = [0, 1] if self.key in {"M2400", "M2401"} else [0]
        named = {
            label_key(g["subcomponent_name"]): i for i, g in enumerate(groups) if i not in roots
        }
        runner.require(len(named) == len(groups) - len(roots), "Duplicate stock group")
        visited = set(roots)
        self.stock_paths = {}
        for ci in roots:
            for ri, row in enumerate(groups[ci]["items"]):
                sp = ["components", ci, "items", ri]
                name = row["component_name"]
                q, reason, kind = self.amount(row, "main preparation input")
                if row.get("reference_media_id"):
                    runner.require(
                        row["reference_media_id"] == self.key, "External stock requires review"
                    )
                    si = named[label_key(name)]
                    runner.require(si not in visited, "Repeated or cyclic stock use")
                    visited.add(si)
                    powder = row["unit"] in {"g", "mg"}
                    reason += (
                        " Inline commercial-base formula detail, not extra simultaneous ingredients. Its table masses have no verified volume/dilution basis."
                        if powder
                        else " Inline enrichment composition is separate from its dose and from finished-medium concentrations."
                    )
                    p = self.emit(
                        ["solutions"],
                        name,
                        sp,
                        q,
                        reason,
                        "base_detail" if powder else "stock_dose",
                        descriptor=True,
                    )
                    self.stock_paths[si] = p
                    for sj, component in enumerate(groups[si]["items"]):
                        runner.require(
                            not component.get("reference_media_id"), "Nested stock needs review"
                        )
                        cq, cr, ck = self.amount(
                            component,
                            f"{groups[si]['subcomponent_name']} {'formula-detail table' if powder else 'stock preparation'}",
                        )
                        self.emit(
                            p + ["composition"],
                            component["component_name"],
                            ["components", si, "items", sj],
                            cq,
                            cr,
                            ck,
                        )
                else:
                    self.emit(["ingredients"], name, sp, q, reason, kind)
        runner.require(visited == set(range(len(groups))), "Unaccounted source group")
        albumin = [
            (ci, ri)
            for ci, g in enumerate(groups)
            for ri, r in enumerate(g["items"])
            if "albumin" in r["component_name"].casefold() and not r.get("reference_media_id")
        ]
        runner.require(len(albumin) == 1, "Albumin identity needs review")
        self.albumin_sp = ["components", albumin[0][0], "items", albumin[0][1]]
        self.togo_context()

    def context_claim(self, text, source, sp=None, snippet=None, pointer=None):
        p = pointer or []
        self.note(runner.get_node(self.after, p), text)
        self.claim(
            p + ["notes"],
            p + ["notes"] if not p else None,
            source,
            sp,
            "evidence_only",
            "preparation_context",
            text,
            [],
            snippet,
        )

    def togo_context(self):
        comments = self.data[self.key]["comments"]
        # Retain protocol text with its stage; do not promote literature excerpts to growth claims.
        schedules = {
            "M2328": [(0, None)],
            "M2399": [(0, None), (2, 1)],
            "M1946": [],
            "M2407": [],
            "M2879": [],
            "M2880": [],
            "M2403": [(0, None), (3, 2), (4, 2)],
            "M2401": [(0, None), (1, None), (3, 2)],
            "M2400": [(0, None), (1, None), (3, 2)],
            "M2397": [(0, None), (1, None), (2, None), (4, 1)],
            "M2402": [(1, None), (4, 2), (5, 2)],
            "M2404": [(0, None), (3, 2), (5, None)],
        }
        for i, si in schedules[self.key]:
            text = comments[i]["comment"]
            runner.require(text, "Preparation locator drift")
            scope = (
                "main preparation"
                if si is None
                else self.data[self.key]["components"][si]["subcomponent_name"]
            )
            reason = f"Source preparation context ({scope}): {text}"
            if self.key == "M2402" and i == 1:
                reason += " Source conflict: this broth table has no agar row, although the prose mentions dissolving agar. No agar is added by inference."
            if self.key == "M2404" and i == 5:
                reason += " This describes reagent reconstitution; ethanol retention in the finished medium and the final volume are not specified."
            self.context_claim(
                reason,
                self.key,
                ["comments", i, "comment"],
                pointer=self.stock_paths.get(si) if si is not None else None,
            )
        if self.key == "M2399":
            self.after["physical_state"] = "SOLID_AGAR"
            self.claim(
                ["physical_state"],
                ["physical_state"],
                self.key,
                ["comments", 0, "comment"],
                "correct",
                "physical_state",
                "The 7H10 preparation explicitly dissolves agar; the former liquid classification is withdrawn.",
                [],
            )
        if self.key == "M1946":
            reason = "Source-version conflict: TOGO M1946 lists 895 ml main water; the inspected current NBRC 1219 page lists 900 mL. This TOGO record preserves 895 ml as its provider's input, not a verified final volume; no silent source-version substitution is made."
            self.context_claim(
                reason,
                self.key,
                ["components", 0, "items", 0],
                self.excerpt(["components", 0, "items", 0]),
            )
            self.context_claim(reason, "NBRC1219", snippet="Distilled water 900 mL")
        if self.key in {"M2879", "M2880"}:
            reason = (
                "Unresolved source conflict: M2879's table describes ADC/Tween-supplemented plates, while the quoted cultivation sentence assigns OADC to plates using 'respectively'. Preserve the table as a provider-reported formulation, not as a verified formulation for the study."
                if self.key == "M2879"
                else "The quoted cultivation sentence assigns ADC/Tween to liquid medium, but the original publication is unidentified and uninspected."
            )
            reason += " No organism-growth association is curated from this secondary quotation."
            self.context_claim(reason, self.key, ["comments", 0, "comment"])

    def dsmz(self):
        ss = self.data[self.key]["data"]["solutions"]
        for ri, row in enumerate(ss[0]["recipe"][:12]):
            self.emit(
                ["ingredients"],
                row["compound"],
                ["data", "solutions", 0, "recipe", ri],
                {"value": number(row["g_l"]), "unit": "G_PER_L"},
                "Basal constituent rate for the source's explicitly one-liter final medium; commercial 4.7 g powder represents this same base, not an additional ingredient.",
                "final_rate",
            )
        protocol = ss[0]["steps"][1]["step"]
        for name, amount in (("Distilled water", "0.9"), ("Glycerol", "0.002")):
            self.emit(
                ["ingredients"],
                name,
                ["data", "solutions", 0, "steps", 1, "step"],
                {"value": amount, "unit": "L"},
                f"Source preparation input, {amount} L; water is 900 ml and glycerol is 2 ml. The API table's 1000 ml water row conflicts with its preparation prose and the original PDF; this input follows the explicit preparation, not a sum of component volumes.",
                "batch_volume",
                snippet=json_excerpt(
                    self.context["sources"][self.key]["raw"],
                    ["data", "solutions", 0, "steps", 1, "step"],
                ),
            )
        p = self.emit(
            ["solutions"],
            "ADC Enrichment",
            ["data", "solutions", 0, "recipe", 13],
            {"value": "0.1", "unit": "L"},
            "100 ml = 0.1 L enrichment addition after cooling; its stock composition below is not finished-medium concentration.",
            "stock_dose",
            descriptor=True,
        )
        for ri, row in enumerate(ss[1]["recipe"]):
            water = row["compound"] == "Distilled water"
            q = (
                {"value": "0.1", "unit": "L"}
                if water
                else {"value": number(row["g_l"]), "unit": "G_PER_L"}
            )
            reason = "ADC stock preparation: " + (
                "100 ml water = 0.1 L input, not an asserted final-volume marker."
                if water
                else f"MediaDive explicitly reports {row['g_l']} g/L for this stock from {row['amount']} {row['unit']} in its 100 ml stock encoding; not a finished-medium rate."
            )
            if row.get("attribute"):
                reason += f" Source material qualifier: {row['attribute']}."
            self.emit(
                p + ["composition"],
                row["compound"],
                ["data", "solutions", 1, "recipe", ri],
                q,
                reason,
                "batch_volume" if water else "provider_stock_rate",
                old=[] if water else None,
            )
        self.albumin_sp = ["data", "solutions", 1, "recipe", 0]
        self.context_claim(
            "Original DSMZ 857 protocol explicitly prepares one liter final medium with 900 ml water and 2 ml glycerol, then adds 100 ml ADC after cooling. Do not autoclave the added enrichment or replace its 0.3 mg catalase with another recipe's OADC amount.",
            "DSMZ857",
            snippet=self.texts["DSMZ857"][
                self.texts["DSMZ857"]
                .index("To prepare one liter") : self.texts["DSMZ857"]
                .index("mix throughly.")
                + len("mix throughly.")
            ],
        )
        for i in range(3):
            self.claim(
                ["preparation_steps", i, "description"],
                ["preparation_steps", i, "description"],
                self.key,
                ["data", "solutions", 0, "steps", i, "step"],
                "evidence_only",
                "retained_preparation",
                "Retain the source-specific powder preparation, sterilization, cooling and later ADC addition.",
                [],
            )
        self.claim(
            ["ph_range"],
            ["ph_range"],
            self.key,
            ["data", "solutions", 0, "steps", 0, "step"],
            "evidence_only",
            "retained_ph",
            "6.6 +/- 0.2 at 25 C gives 6.4 to 6.8; preserve the reported pH range.",
            [],
        )
        runner.require("900 ml" in protocol and "2 ml glycerol" in protocol, "Protocol drift")

    def formulate(self):
        prefix, separator, previous = self.before["notes"].partition(
            "Commercial Product: LB Medium"
        )
        runner.require(separator, "Historical provenance drift")
        self.after["notes"] = (
            prefix.rstrip()
            + "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product: LB Medium"
            + previous
        )
        self.note(
            self.after,
            "False LB constituent expansion is withdrawn. Source-specific amounts and preparation boundaries supersede flattened concentrations. Existing chemical annotations and earlier history are preserved, not recertified; no organism-growth association is added.",
        )
        if self.key == "D857":
            self.dsmz()
        else:
            self.togo()
        for old in self.lb:
            self.claim(
                ["notes"],
                old + ["concentration"],
                self.key,
                self.albumin_sp,
                "remove_unsupported",
                "false_lb_removed",
                "Restore the source's albumin entry and remove this falsely substituted LB constituent and concentration; the complete source formulation contains no LB preparation.",
                [],
                self.excerpt(self.albumin_sp),
            )
        accounted = {tuple(link["old_pointer"]) for link in self.lineage if link["old_pointer"]} | {
            tuple(p) for p in self.lb
        }
        expected = {
            (field, i)
            for field in ("ingredients", "solutions")
            for i in range(len(self.before.get(field, [])))
        }
        runner.require(accounted == expected, "Unaccounted original node")

    def finish(self, timestamp):
        for claim in self.claims:
            claim["new"] = copy.deepcopy(
                runner.get_node(self.after, claim["pointer"][:-1]).get(claim["pointer"][-1])
            )
        self.after["references"] = []
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            title = (
                "Catalogue Detail Medium | NITE - NBRC Culture Catalogue"
                if key == "NBRC1219"
                else (
                    self.texts[key].splitlines()[0]
                    if key == "DSMZ857"
                    else (
                        self.data[key]["data"]["medium"]["name"]
                        if key == "D857"
                        else self.data[key]["meta"]["name"]
                    )
                )
            )
            self.after["references"].append(
                {
                    "reference": meta["url"],
                    "title": title,
                    "notes": f"source_type={'culture_collection_page' if key in {'DSMZ857', 'NBRC1219'} else 'dataset'}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; accession={key}; capture_sha256={meta['sha256']}. Authors and publication year are not supplied; access/copyright years are not publication years. Formulation evidence, not newly curated growth evidence.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restore albumin and separate basal inputs, commercial-base detail and ADC/OADC stock amounts/doses. Correct volume/mass confusion; retain unsupported mass/percent bases and source-version conflicts explicitly. Preserve IDs and all prior history.",
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
