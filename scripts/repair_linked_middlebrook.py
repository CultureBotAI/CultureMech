#!/usr/bin/env python3
"""Guarded source-specific repair of eleven linked Middlebrook formulations."""

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
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-middlebrook-linked"
CONTEXT_SHA = "de800cece2575a52bf0a6016c0e356d44d5459b653c3063e4945994dc63a98e6"
ACTION = "RESTORED_LINKED_MIDDLEBROOK_FORMULATIONS_AND_VARIANT_SCOPES_WITH_EVIDENCE"
STRAINS = ("44338", "44339", "44482", "44483", "44680")
PARENTS = {
    "K645": ("D645", "DERIVED_FROM"),
    "K645a": ("D645", "UNCERTAIN"),
    "K911": ("D911", "DERIVED_FROM"),
    "K911_44536": ("K911", "STRAIN_SPECIFIC_VARIANT"),
    **{"K645_" + strain: ("K645", "STRAIN_SPECIFIC_VARIANT") for strain in STRAINS},
}


def frozen():
    raw = (HERE / "context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    runner.require(
        {r["key"] for r in context["records"]} == set(PARENTS) | {"D645", "D911"},
        "Cohort drift",
    )
    return context


def sources(context):
    data, texts, titles = {}, {}, {}
    for key, capture in context["sources"].items():
        raw, meta = capture["raw"], capture["metadata"]
        runner.require(
            meta["url"] == meta["response_url"]
            and meta["http_status"] == 200
            and runner.sha(raw.encode(meta.get("encoding", "utf-8"))) == meta["sha256"],
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        source = recipe_source(meta["url"])
        parsed = parse_recipe(source, raw, meta)
        texts[key], titles[key] = parsed.content, parsed.title
        if key.startswith("DSMZ"):
            payload = read_pdf_capture(meta)
            runner.require(
                runner.sha(payload) == meta["pdf_sha256"] and extract_recipe_pdf(payload)[0] == raw,
                "PDF binary/extraction drift",
            )
        elif key.startswith("K"):
            soup = BeautifulSoup(raw, "html.parser")
            tables = [t for t in soup.find_all("table") if "Gram Amount" in t.get_text()]
            runner.require(len(tables) == 1, "KOMODO table drift")
            rows = [
                [html_recipe_text(str(c))[0] for c in tr.find_all("td", recursive=False)]
                for tr in tables[0].find_all("tr")
            ]
            runner.require(
                rows[0] == ["Name", "Semi unique name", "Unique Name", "Gram Amount", "Mol Amount"],
                "KOMODO columns",
            )
            data[key] = rows[1:]
        else:
            data[key] = json.loads(raw)
    for key, ids in (("D645", [1369, 1370, 1371]), ("D911", [1873, 5667, 5668])):
        runner.require(
            [s["id"] for s in data[key]["data"]["solutions"]] == ids, "DSMZ stages drift"
        )
    return data, texts, titles


def identity(name):
    return "sodium citrate" if name == "Na-citrate" else name.casefold()


def num(value):
    return format(Decimal(str(value)).normalize(), "f")


class Review(shared.Review):
    append = stocks.Review.append
    claim = prior.Review.claim

    def __init__(self, before, key):
        self.context = frozen()
        self.specs = {r["key"]: r for r in self.context["records"]}
        self.spec = self.specs[key]
        runner.require(
            before == runner.load_yaml(self.spec["before_text"])
            and before["id"] == self.spec["id"],
            "Unreviewed baseline",
        )
        runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
        runner.require(
            not any(before.get(k) for k in ("evidence", "references", "variants", "solutions")),
            "Existing provenance requires reconciliation",
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
                name = identity(node["preferred_term"])
                runner.require(name not in self.old, "Ambiguous old ingredient")
                self.old[name] = p
        runner.require(
            [runner.get_node(before, p)["preferred_term"] for p in self.lb]
            == ["Tryptone", "Yeast extract", "Sodium chloride"],
            "False-LB identity drift",
        )
        self.after["ingredients"], self.after["solutions"] = [], []

    def excerpt(self, sp):
        return json_excerpt(self.context["sources"][self.key]["raw"], sp)

    def emit(self, parent, label, sp, quantity, reason, kind, *, descriptor=False, snippet=None):
        old = self.old.get(identity(label))
        node = (
            copy.deepcopy(runner.get_node(self.before, old)) if old else {"preferred_term": label}
        )
        runner.require(
            identity(node["preferred_term"]) == identity(label), "Chemical identity drift"
        )
        if old:
            runner.require(tuple(old) not in self.accounted, "Repeated old ingredient")
            self.accounted.add(tuple(old))
        if quantity is None:
            node.pop("concentration", None)
        else:
            node["concentration"] = quantity
        if descriptor:
            node["name"] = node["preferred_term"]
            node["composition"] = []
        self.note(node, reason)
        p = self.append(parent, node)
        self.lineage.append(
            {
                "pointer": p,
                "old_pointer": old,
                "source": self.key,
                "source_pointer": sp,
                "kind": kind,
                "label": label,
            }
        )
        for field in ("concentration", "notes") + (("name",) if descriptor else ()):
            self.claim(
                p + [field],
                old + [field] if old else None,
                self.key,
                sp,
                "correct" if old else "add",
                kind,
                reason,
                [] if descriptor else p,
                snippet,
            )
        return p

    def context_claim(
        self, text, source, snippet, *, pointer=None, old=None, kind="preparation_context"
    ):
        pointer = pointer or []
        self.note(runner.get_node(self.after, pointer), text)
        self.claim(pointer + ["notes"], old, source, None, "evidence_only", kind, text, [], snippet)

    def pdf_line(self, label, *, stock=False):
        pdf = self.texts["DSMZ" + self.key[1:]]
        if stock:
            pdf = pdf[
                pdf.index(
                    "Bacto Middlebrook OADC"
                    if self.key == "D645"
                    else "Bacto Middelbrook OADC enrichment (Difco 212240):"
                ) :
            ]
        names = {
            "Sodium citrate": "Na-citrate",
            "Agar": "Bacto agar",
            "Bovine albumin": "Albumin fraction V, bovine",
            "Catalase": "Catalase (beef)",
        }
        label = names.get(label, label)
        lines = [line.strip() for line in pdf.splitlines() if line.strip().startswith(label + " ")]
        runner.require(len(lines) == 1, f"Ambiguous PDF row {label}")
        return lines[0]

    def komodo(self):
        basis = "Gram & Mol amounts are per Liter of medium."
        for i, row in enumerate(self.data[self.key]):
            label, _, _, gram, _ = row
            q = None if gram == "null" else {"value": gram, "unit": "G_PER_L"}
            reason = (
                "The source Gram Amount is null: no fixed amount is asserted; missing is not zero."
                if q is None
                else f"Provider-reported medium rate: Gram Amount {gram} per liter. Preserve displayed precision; the linked DSMZ batch/stock recipe does not independently explain this rate."
            )
            reason += " The Mol Amount column is not used to infer a new molarity or hydrate form."
            if label in {"Na2HPO4", "Pyridoxine"}:
                reason += f" Source secondary-name ambiguity: displayed name '{label}' versus '{row[1]}'; retained chemical annotations are not recertified."
            p = self.emit(
                ["ingredients"],
                label,
                ["recipe_table", i + 1],
                q,
                reason,
                "provider_medium_rate" if q else "unquantified",
                snippet=" ".join(row),
            )
            self.claim(
                p + ["notes"],
                None,
                self.key,
                None,
                "evidence_only",
                "amount_basis",
                reason,
                p,
                basis,
            )
            if label in {"hemin", "NAOH"}:
                # Keep a literal layout-text excerpt, not a whitespace-reconstructed quotation.
                pdf = self.texts["DSMZ645a"]
                quote = pdf[pdf.index("Middlebrook 7H10") : pdf.index("1N NAOH.") + len("1N NAOH.")]
                explanation = "Original DSMZ 645a says 60 micromoles hemin without a volume denominator, dissolved using 1N NAOH without an addition dose. This does not independently establish 60 uM or a mass conversion. The provider hemin rate and unquantified NaOH dose remain separately scoped."
                self.note(runner.get_node(self.after, p), explanation)
                self.claim(
                    p + ["notes"],
                    None,
                    "DSMZ645a",
                    None,
                    "evidence_only",
                    "hemin_scope",
                    explanation,
                    p,
                    quote,
                )
        albumin = next(row for row in self.data[self.key] if row[0] == "Albumin fraction V, bovine")
        self.albumin_quote, self.albumin_sp = " ".join(albumin), None
        self.context_claim(
            "This record now follows its own KOMODO table rather than the composition copied from DSMZ. Rates remain provider-qualified; a dilution mechanism is unresolved. Null PH Info is not replaced by a copied pH assertion. No source omission proves an experimentally absent ingredient.",
            self.key,
            "PH Info: null",
        )
        if self.key == "K645a":
            self.context_claim(
                "The hemin variant is not an exact duplicate of the plain 645 records. Its glycerol omission is a table observation, not evidence that the experimental preparation was glycerol-free.",
                self.key,
                self.albumin_quote,
            )

    def dsmz_row(self, parent, si, ri, *, kind):
        row = self.data[self.key]["data"]["solutions"][si]["recipe"][ri]
        label = row.get("compound", row.get("solution"))
        if row["unit"] == "ml":
            q = {"value": num(Decimal(str(row["amount"])) / 1000), "unit": "L"}
            reason = f"Source batch input: {row['amount']} ml = {q['value']} L; not a final-volume marker or a mass concentration."
        elif kind == "stock_rate":
            q = {"value": num(row["g_l"]), "unit": "G_PER_L"}
            reason = f"OADC stock input: {row['amount']} {row['unit']}; API stock g_l={row['g_l']} in its 100 ml encoding. This is a provider-reported stock rate, not a finished-medium concentration or independently measured final stock volume."
        else:
            q = None
            reason = f"Source batch amount: {row['amount']} {row['unit']}. Retain this mass in notes; no independently verified final-volume denominator supports a finished-medium g/L conversion."
            if row.get("g_l") is not None:
                reason += f" The source API g_l={row['g_l']} has its own normalization context and is not adopted as a finished-medium rate."
        if row.get("attribute"):
            reason += " Source material qualifier: " + row["attribute"] + "."
        if kind == "base_detail":
            reason += " This is detail of the commercial-base formula, not an additional simultaneous ingredient or water addition to the receiving medium."
        p = self.emit(parent, label, ["data", "solutions", si, "recipe", ri], q, reason, kind)
        if label != "Distilled water":
            self.claim(
                p + ["notes"],
                None,
                "DSMZ" + self.key[1:],
                None,
                "evidence_only",
                "original_mass_or_volume",
                reason,
                p,
                self.pdf_line(label, stock=si == 2),
            )
        return p

    def dsmz(self):
        ss = self.data[self.key]["data"]["solutions"]
        if self.key == "D645":
            p = self.dsmz_row(["ingredients"], 0, 0, kind="commercial_batch_mass")
            powder = runner.get_node(self.after, p)
            old = self.old[identity(powder["preferred_term"])]
            for field in ("term", "mediaingredientmech_chebi_term"):
                runner.require(powder[field]["id"] == "CHEBI:2509", "Unexpected powder grounding")
                powder.pop(field)
                self.claim(
                    p + [field],
                    old + [field],
                    self.key,
                    ["data", "solutions", 0, "recipe", 0],
                    "correct",
                    "mixture_grounding_removed",
                    "Commercial 7H10 mixture is not chemically identical to pure agar; withdraw the copied pure-agar grounding.",
                    p,
                )
        else:
            row = ss[0]["recipe"][0]
            self.emit(
                ["solutions"],
                row["solution"],
                ["data", "solutions", 0, "recipe", 0],
                None,
                "Commercial-base batch input: 21 g. API g_l=11.0236 is not a verified final concentration. Nested composition is source formula detail, not extra simultaneous ingredients; its water is not another receiving-medium addition.",
                "commercial_base_detail",
                descriptor=True,
            )
            for ri in range(len(ss[1]["recipe"])):
                self.dsmz_row(["solutions", 0, "composition"], 1, ri, kind="base_detail")
        for ri in (1, 2):
            self.dsmz_row(["ingredients"], 0, ri, kind="batch_volume")
        step = ss[0]["steps"][0]["step"]
        sp = ["data", "solutions", 0, "steps", 0, "step"]
        oadc = self.emit(
            ["solutions"],
            ss[2]["name"],
            sp,
            {"value": "0.1", "unit": "L"},
            "100 ml = 0.1 L OADC addition after sterilization and cooling, separate from its stock composition. Do not autoclave this later addition or infer a finished-medium denominator.",
            "stock_dose",
            descriptor=True,
        )
        for ri in range(len(ss[2]["recipe"])):
            self.dsmz_row(oadc + ["composition"], 2, ri, kind="stock_rate")
        self.albumin_sp = ["data", "solutions", 2, "recipe", 1]
        self.albumin_quote = self.excerpt(self.albumin_sp)
        self.after["preparation_steps"] = [
            {"step_number": 1, "action": "HEAT", "description": step}
        ]
        self.claim(
            ["preparation_steps"],
            ["preparation_steps"],
            self.key,
            sp,
            "correct",
            "preparation_scope",
            "Retain explicit sterilization/cooling and later OADC addition; pH and section headings are not heat/mix operations.",
            [],
        )
        if self.key == "D645":
            self.after["variants"] = [
                {
                    "name": "From-scratch alternative to commercial 7H10",
                    "relationship": "SUBSTITUTED_COMPONENT_VARIANT",
                    "description": "Use only when the commercial medium is unavailable. This is an alternative preparation, not simultaneous inputs to the commercial route; final-volume equivalence is unresolved.",
                    "modifications": [],
                }
            ]
            variant = self.after["variants"][0]
            for ri, row in enumerate(ss[1]["recipe"]):
                old = self.old.get(identity(row["compound"]))
                if old:
                    runner.require(
                        tuple(old) not in self.accounted, "Alternative repeated old ingredient"
                    )
                    self.accounted.add(tuple(old))
                value = f"Alternative preparation input: {row['compound']} {row['amount']} {row['unit']}; not an additional input to the commercial preparation. No final-medium concentration is inferred."
                variant["modifications"].append(value)
                self.lineage.append(
                    {
                        "pointer": ["variants", 0],
                        "old_pointer": old,
                        "source": self.key,
                        "source_pointer": ["data", "solutions", 1, "recipe", ri],
                        "kind": "alternative_input",
                        "label": row["compound"],
                    }
                )
                self.claim(
                    ["variants", 0, "modifications"],
                    old + ["concentration"] if old else None,
                    self.key,
                    ["data", "solutions", 1, "recipe", ri],
                    "correct",
                    "alternative_input",
                    value,
                    ["variants", 0],
                )
                self.claims[-1]["ingredient"] = row["compound"]
            variant["modifications"].append(
                "The alternative table lists 1000 ml water, not the commercial route's 900 ml. Do not sum those water inputs or assert measured final volume. Its final pH at 25 C is 6.6 +/- 0.2; no titrant or titration dose is specified."
            )
            self.claim(
                ["variants", 0, "modifications"],
                None,
                self.key,
                ["data", "solutions", 1, "steps", 0, "step"],
                "evidence_only",
                "alternative_ph",
                "Preserve pH at the alternative-table scope, not a heating instruction.",
                ["variants", 0],
            )
            pdf = self.texts["DSMZ645"]
            excerpt = pdf[
                pdf.index("If you can") : pdf.index("Bacto Middlebrook OADC enrichment:")
            ].rstrip()
            self.claim(
                ["variants", 0, "description"],
                ["ingredients"],
                "DSMZ645",
                None,
                "correct",
                "alternative_scope_and_history",
                "Archive the displaced flattened ingredient nodes, including chemical annotations, in append-only history. Only the conditional alternative carries these basal inputs; its table does not establish final-volume equivalence to the commercial route.",
                ["variants", 0],
                excerpt,
            )
        else:
            self.context_claim(
                "Final pH at 25 C is 6.6 +/- 0.2; preserve the 6.4-6.8 range without inventing a heating or titration step.",
                self.key,
                self.excerpt(["data", "solutions", 0, "steps", 1, "step"]),
            )
            self.claim(
                ["ph_range"],
                ["ph_range"],
                self.key,
                ["data", "medium"],
                "evidence_only",
                "retained_ph",
                "Retain source-reported pH range.",
                [],
            )

    def link_basis(self, child):
        if child == "K645a":
            reason = "Candidate 7H10/OADC family relationship only: hemin, historical product identifiers and unresolved preparation differences preclude an exact-duplicate or parent-plus-only-hemin assertion."
        elif "_" in child:
            reason = "The source explicitly names a medium modified for this DSM strain. Its displayed table matches the KOMODO base but does not identify the modification; no numerical difference or organism-growth association is inferred."
        else:
            reason = "The source Instructions explicitly link the DSMZ recipe. Different quantity normalization contexts remain unresolved; the prior copied signature does not prove an exact duplicate."
        if child == "K645a":
            pdf = self.texts["DSMZ645a"]
            snippet = pdf[pdf.index("Middlebrook 7H10") : pdf.index("1N NAOH.") + len("1N NAOH.")]
        else:
            lines = self.texts[child].splitlines()
            snippet = next(
                line
                for line in lines
                if line.startswith("Name:" if "_" in child else "Instructions:")
            )
        return reason, snippet

    def links(self):
        for field in (
            "parent_media",
            "variant_relationship",
            "variant_modifications",
            "variant_children",
        ):
            self.after.pop(field, None)
        if self.key in PARENTS:
            parent, relation = PARENTS[self.key]
            spec = self.specs[parent]
            reason, quote = self.link_basis(self.key)
            self.after["parent_media"] = {
                "path": spec["path"],
                "id": spec["id"],
                "name": runner.load_yaml(spec["before_text"])["name"],
                "relationship": relation,
                "notes": reason,
            }
            self.after["variant_relationship"], self.after["variant_modifications"] = relation, [
                reason
            ]
            self.claim(
                ["parent_media", "relationship"],
                None,
                "DSMZ645a" if self.key == "K645a" else self.key,
                None,
                "correct",
                "parent_link",
                reason,
                ["parent_media"],
                quote,
            )
        children = [child for child, (parent, _) in PARENTS.items() if parent == self.key]
        if children:
            self.after["variant_children"] = []
            for child in children:
                spec = self.specs[child]
                reason, quote = self.link_basis(child)
                p = self.append(
                    ["variant_children"],
                    {
                        "path": spec["path"],
                        "id": spec["id"],
                        "name": runner.load_yaml(spec["before_text"])["name"],
                        "relationship": PARENTS[child][1],
                        "notes": reason,
                    },
                )
                self.claim(
                    p + ["relationship"],
                    None,
                    "DSMZ645a" if child == "K645a" else child,
                    None,
                    "correct",
                    "child_link",
                    reason,
                    p,
                    quote,
                )
        for field in (
            "parent_media",
            "variant_relationship",
            "variant_modifications",
            "variant_children",
        ):
            if field in self.before or field in self.after:
                self.claim(
                    [field],
                    [field],
                    self.key,
                    self.albumin_sp,
                    "correct",
                    "family_topology",
                    "Replace the copied exact-duplicate topology with reciprocal source-qualified family links; retain the previous links in history and preserve permanent IDs.",
                    [],
                    self.albumin_quote,
                )

    def formulate(self):
        prefix, marker, previous = self.before["notes"].partition("Commercial Product: LB Medium")
        runner.require(marker, "Historical note drift")
        self.after["notes"] = (
            prefix.rstrip()
            + "\n\nSuperseded historical provenance (not a current formulation claim):\nCommercial Product: LB Medium"
            + previous
        )
        self.komodo() if self.key.startswith("K") else self.dsmz()
        for p in self.lb:
            self.claim(
                ["notes"],
                p + ["concentration"],
                self.key,
                self.albumin_sp,
                "remove_unsupported",
                "false_lb_removed",
                "Restore source-listed albumin instead of the false LB constituent expansion. Genuine casein digest and NaCl entries are retained separately.",
                [],
                self.albumin_quote,
            )
            self.accounted.add(tuple(p))
        for name, p in self.old.items():
            if tuple(p) not in self.accounted:
                runner.require(
                    self.key.startswith("K")
                    and (
                        name == "bacto middlebrook 7h10 agar"
                        or (self.key == "K645a" and name == "glycerol")
                    ),
                    "Unreviewed leftover node",
                )
                self.claim(
                    ["notes"],
                    p + ["concentration"],
                    self.key,
                    self.albumin_sp,
                    "remove_unsupported",
                    "copied_unlisted_input",
                    "Withdraw this copied DSMZ input that is not a separate ingredient in the complete inspected KOMODO table. Absence from that table is not proof of absence from the experimental preparation.",
                    [],
                    self.albumin_quote,
                )
                self.accounted.add(tuple(p))
        runner.require(
            self.accounted == {("ingredients", i) for i in range(len(self.before["ingredients"]))},
            "Unaccounted original ingredient",
        )
        self.links()
        self.note(
            self.after,
            "Source-specific ingredient identities, quantity bases and preparation routes supersede the copied flattened amounts. Historical events are preserved. Chemical groundings are not comprehensively recertified; no taxa-media association is added.",
        )

    def finish(self, timestamp):
        for claim in self.claims:
            claim["new"] = copy.deepcopy(
                runner.get_node(self.after, claim["pointer"][:-1]).get(claim["pointer"][-1])
            )
        self.after["references"] = []
        for key in self.used:
            meta = self.context["sources"][key]["metadata"]
            self.after["references"].append(
                {
                    "reference": meta["url"],
                    "title": self.titles[key],
                    "notes": f"source_type={'culture_collection_page' if key.startswith('DSMZ') else 'web_page' if key.startswith('K') else 'dataset'}; discovery_mode={'existing_record_reference' if key == self.key else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; accession={key}; capture_sha256={meta['sha256']}. Authors and publication year are not supplied; copyright/access years are not publication years.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=self.context["sources"][self.key]["metadata"]["url"],
            notes="Restore source-specific Middlebrook ingredients, distinguish commercial/alternative/base/OADC scopes, retain uncertainty and repair reciprocal family links without changing permanent IDs.",
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
