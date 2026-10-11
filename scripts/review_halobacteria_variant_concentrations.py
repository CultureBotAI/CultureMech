#!/usr/bin/env python3
"""Guarded source-backed Halobacteria variant concentrations and stage boundaries."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from decimal import Decimal
from pathlib import Path

import repair_methanogen_stock_boundaries as shared
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import parse_recipe, recipe_source

runner, ROOT = shared.runner, shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-halobacteria-variants"
CONTEXT_SHA = "5c32dabb73da826f5ad4a3fc1750bb701e077f4541fcb708522970538979cb33"
REVIEW_SHA = "bdb37d465f8cc3b1b61050e73d95369c119590fa11f56041f7995bc3d8874c45"
PLAN_PATH = HERE / "plan-v2.json"
ACTION = "CURATED_HALOBACTERIA_VARIANT_CONCENTRATIONS_AND_PREPARATION_STAGES"
PARENTS = {"J168", "M159", "M160"}
PREPARED = {"J1132", "M1212"}
FAMILY = {
    "J572": "J572",
    "M576": "J572",
    "J1008": "J1008",
    "M1065": "J1008",
    "J914": "J914",
    "M959": "J914",
    "M960": "J914",
    "J377": "J377",
    "M371": "J377",
    "M372": "J377",
}
MAKEUP = "Add components to distilled water and bring volume to 1.0 L."
AGAR = "For preparation of solid medium, add 20.0 g/L agar."
BASE_PH = "Adjust pH to 7.0-7.2."
TITRANT = "After autoclaving, adjust pH to 7.5 with sterile Na2CO3 solution."
MODIFICATIONS = {
    "J572": "Use Medium No. 168 with 2.0 g/L MgSO4\u00b77H2O (final).",
    "J1008": "Use Medium No. 168 supplemented with 270.0 g/L NaCl (final) and 15.0 g/L MgSO4\u00b77H2O.",
    "J914": "Use Medium No. 168 with 150.0 g/L (final) NaCl.",
}
OVERRIDES = {
    "J572": {"MgSO4\u00b77H2O": "2"},
    "J1008": {"MgSO4\u00b77H2O": "15", "NaCl": "270"},
    "J914": {"NaCl": "150"},
}
STAGE_NOTE = (
    "These concentrations describe the prepared J168/M159 base, not an asserted "
    "post-titration final-medium concentration. The recipe uses 1 L of prepared "
    "base and then adjusts pH to 8.0. The titrant identity, dose and resulting "
    "final volume are unspecified; do not infer a carbonate reagent, zero dose, "
    "or final-medium dilution factor. Existing chemical mappings and roles are "
    "preserved, not independently recertified."
)
PROVIDER_NOTE = (
    "The captured MediaDive J1132 provider dataset identifies this preparation; "
    "the original JCM1132 page returned Nothing found. This is not a recovered "
    "JCM original or a DOI-backed publication."
)
MG_NOTE = (
    "JCM1008 explicitly states the modified 270 g/L NaCl and 15 g/L magnesium "
    "sulfate heptahydrate formulation, corroborated by TOGO M1065's g/L rows. "
    "The word supplemented leaves an operational ambiguity: adding magnesium "
    "to the unchanged 20 g/L base cannot lower its concentration to 15 g/L. "
    "No 35 g/L magnesium or 470 g/L sodium chloride sum is inferred, and this "
    "curation does not resolve that preparation ambiguity."
)
LINKS = {
    "J572": ("J168", "DERIVED_FROM"),
    "M576": ("M159", "DERIVED_FROM"),
    "J1008": ("J168", "DERIVED_FROM"),
    "M1065": ("M159", "DERIVED_FROM"),
    "J914": ("J168", "SALINITY_VARIANT"),
    "M959": ("M159", "SALINITY_VARIANT"),
    "M960": ("M160", "SALINITY_VARIANT"),
    "J377": ("J168", "SALINITY_VARIANT"),
    "J1132": ("J168", "PH_VARIANT"),
    "M1212": ("M159", "PH_VARIANT"),
}


def canonical(name):
    name = {
        "Casamino acids": "Casamino acids (BD-Difco)",
        "Yeast extract": "Yeast extract (BD-Difco)",
        "Na glutamate": "Sodium glutamate",
        "Distilled water": "distilled water",
    }.get(name, name)
    return name.replace(" x ", "\u00b7").replace("\u30fb", "\u00b7").replace(" H2O", "H2O")


def frozen():
    path = HERE / "context.json"
    runner.require(not path.is_symlink(), "Context symlink")
    raw = path.read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Context drift")
    context = json.loads(raw)
    runner.require(context["terminal"] and len(context["records"]) == 16, "Incomplete cohort")
    for key, source in context["sources"].items():
        meta, raw = source["metadata"], source["raw"]
        runner.require(
            meta["http_status"] == 200
            and meta["url"] == meta["response_url"]
            and runner.sha(raw.encode()) == meta["sha256"],
            "Capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        text = (
            raw if key == "E1132" else parse_recipe(recipe_source(meta["url"]), raw, meta).content
        )
        runner.require(text == source["parsed_text"], "Parsed source drift")
    return context


def value_at(document, pointer):
    parent = runner.get_node(document, pointer[:-1])
    return parent.get(pointer[-1]) if isinstance(parent, dict) else parent[pointer[-1]]


class Review:
    def __init__(self, before, key):
        self.context = frozen()
        self.specs = {r["key"]: r for r in self.context["records"]}
        runner.require(key in self.specs, "Unreviewed target")
        self.spec = self.specs[key]
        runner.require(before == runner.load_yaml(self.spec["before_text"]), "Baseline drift")
        runner.require(not runner.errors(before, self.spec["target_class"]), "Baseline schema")
        self.before, self.after, self.key = before, copy.deepcopy(before), key
        self.claims, self.lineage, self.used = [], [], []
        self.sources = self.context["sources"]
        self.table_key = "J377" if FAMILY.get(key) == "J377" else "J168"
        self.table = {
            canonical(n): (v, u) for n, v, u in self.sources[self.table_key]["table_rows"]
        }
        runner.require(len(self.table) == 9, "Table inventory drift")
        self.export = json.loads(self.sources["E1132"]["raw"])
        runner.require(
            [s["id"] for s in self.export["solutions"]] == [5232, 3823], "Stage graph drift"
        )

    def quote(self, source, pointer):
        return json_excerpt(self.sources[source]["raw"], pointer)

    def proof(self, pointer, source, snippet, reason, *, old=None, evidence=None, status=None):
        evidence = (
            ([] if self.key != "S3823" else ["composition", 0]) if evidence is None else evidence
        )
        meta = self.sources[source]["metadata"]
        text = (
            self.sources[source]["parsed_text"]
            if source.startswith("J")
            else self.sources[source]["raw"]
        )
        runner.require(snippet and snippet in text, "Nonliteral source snippet")
        old_value = value_at(self.before, old) if old else None
        new_value = value_at(self.after, pointer)
        field = runner.field_name(pointer)
        explanation = f"{field}: {reason} Exact captured recipe row/instruction; accessed={meta['accessed_at']}; source SHA256={meta['sha256']}."
        self.claims.append(
            {
                "pointer": pointer,
                "old_pointer": old,
                "field": field,
                "old_field": runner.field_name(old) if old else None,
                "ingredient": (
                    runner.get_node(self.after, pointer[:-1]).get(
                        "preferred_term", "Recipe context"
                    )
                    if isinstance(runner.get_node(self.after, pointer[:-1]), dict)
                    else "Recipe relationship"
                ),
                "old": copy.deepcopy(old_value),
                "new": copy.deepcopy(new_value),
                "source": source,
                "reference": meta["url"],
                "snippet": snippet,
                "explanation": explanation,
                "evidence_pointer": evidence,
                "status": status
                or (
                    "evidence_only"
                    if old_value == new_value
                    else "correct" if old_value is not None else "add"
                ),
            }
        )
        entries = runner.get_node(self.after, evidence).setdefault("evidence", [])
        found = [e for e in entries if e["reference"] == meta["url"]]
        runner.require(len(found) <= 1, "Duplicate evidence")
        if found:
            found[0]["explanation"] += (
                "\n\nAdditional exact excerpt: " + snippet + "\n" + explanation
            )
        else:
            entries.append(
                {
                    "reference": meta["url"],
                    "supports": "SUPPORT",
                    "snippet": snippet,
                    "explanation": explanation,
                }
            )
        if source not in self.used:
            self.used.append(source)

    def root(self, field, value, source, snippet, reason):
        if value is None:
            self.after.pop(field, None)
        else:
            self.after[field] = value
        self.proof([field], source, snippet, reason, old=[field] if field in self.before else None)

    def component(self, pointer, old_pointer=None):
        node = runner.get_node(self.after, pointer)
        name = canonical(node["preferred_term"])
        family = FAMILY.get(self.key)
        source, snippet, reason = self.table_key, None, ""
        proofs = []
        if name == "distilled water":
            node.pop("concentration", None)
            snippet = MAKEUP
            reason = "Water makes the preparation up to 1.0 L. Its separate input volume and mass are unspecified; neither 1 g/L nor a fixed 1 L water dose is supported."
        elif name == "agar":
            runner.require(self.key in {"M372", "M960"}, "Unselected agar option")
            node["concentration"] = {"value": "20", "unit": "G_PER_L"}
            snippet, reason = (
                AGAR,
                "Explicit 20.0 g/L agar option selected by this solid TOGO record; do not add agar to the liquid formulations.",
            )
        elif name in OVERRIDES.get(family, {}):
            node["concentration"] = {"value": OVERRIDES[family][name], "unit": "G_PER_L"}
            source, snippet = family, MODIFICATIONS[family]
            reason = "Use the recipe-specific final formulation, not the copied base amount. " + (
                MG_NOTE
                if family == "J1008"
                else "The source explicitly gives this final g/L target."
            )
            proofs.append((self.table_key, MAKEUP))
        else:
            amount, unit = self.table[name]
            old_value = node["concentration"]
            expected = Decimal(amount) / (1000 if self.key == "M1212" and unit == "mg" else 1)
            new_unit = "G_PER_L" if self.key == "M1212" or unit == "g" else "MG_PER_L"
            node["concentration"] = {"value": old_value["value"], "unit": new_unit}
            runner.require(Decimal(old_value["value"]) == expected, "Unreviewed amount")
            snippet = f"{name} {amount} {unit}"
            reason = f"{amount} {unit} in the source preparation brought to 1.0 L gives {node['concentration']['value']} {new_unit}. Separate exact volume excerpt: \"{MAKEUP}\"."
            if self.key == "M1212" and unit == "mg":
                reason += " Existing g/L value is correct: convert mg to g by dividing by 1000, then divide by the explicit 1 L prepared-base volume."
        if self.key in PREPARED or self.key == "S3823":
            reason += (
                " " + STAGE_NOTE
                if self.key in PREPARED
                else " This is the standalone prepared base, not a universal working dose or the pH-8 final medium."
            )
        if family in MODIFICATIONS:
            proofs.append((family, MODIFICATIONS[family]))
        old_conc = old_pointer + ["concentration"] if old_pointer else None
        node["notes"] = (node.get("notes", "") + "\n\n" + reason).strip()
        for field in ("concentration", "notes"):
            self.proof(
                pointer + [field],
                source,
                snippet,
                reason,
                old=old_pointer + [field] if old_pointer else None,
                evidence=pointer,
                status=(
                    "not_quantified"
                    if field == "concentration" and name == "distilled water"
                    else None
                ),
            )
        if old_pointer is None:
            self.proof(pointer + ["preferred_term"], source, snippet, reason, evidence=pointer)
        if self.key.startswith("M"):
            row_source = "M159" if self.key == "M1212" else self.key
            body = json.loads(self.sources[row_source]["raw"])
            matches = [
                (row, ["components", si, "items", ri])
                for si, sec in enumerate(body["components"])
                for ri, row in enumerate(sec["items"])
                if canonical(row["component_name"]) == name
            ]
            runner.require(len(matches) == 1, "TOGO row identity")
            row, sp = matches[0]
            if name != "distilled water":
                source_rate = Decimal(str(row["volume"])) / (
                    1000 if self.key == "M1212" and row["unit"] == "mg" else 1
                )
                runner.require(
                    source_rate == Decimal(node["concentration"]["value"]), "TOGO amount conflict"
                )
                expected_unit = (
                    "MG_PER_L" if row["unit"] == "mg" and self.key != "M1212" else "G_PER_L"
                )
                runner.require(node["concentration"]["unit"] == expected_unit, "TOGO unit conflict")
            proofs.append((row_source, self.quote(row_source, sp)))
        if self.key in {"J1132", "S3823"}:
            if name == "distilled water":
                sp = ["solutions", 1, "steps", 0]
            else:
                matches = [
                    (i, r)
                    for i, r in enumerate(self.export["solutions"][1]["recipe"])
                    if canonical(r["compound"]) == name
                ]
                runner.require(len(matches) == 1, "Provider row identity")
                i, row = matches[0]
                runner.require(
                    Decimal(str(row["amount"])) == Decimal(node["concentration"]["value"]),
                    "Provider amount conflict",
                )
                runner.require(
                    node["concentration"]["unit"]
                    == ("MG_PER_L" if row["unit"] == "mg" else "G_PER_L"),
                    "Provider unit conflict",
                )
                sp = ["solutions", 1, "recipe", i]
            proofs.append(("E1132", self.quote("E1132", sp)))
        for extra_source, extra_quote in dict.fromkeys(proofs):
            self.proof(
                pointer + ["concentration"],
                extra_source,
                extra_quote,
                reason,
                old=old_conc,
                evidence=pointer,
                status="not_quantified" if name == "distilled water" else None,
            )
        self.lineage.append(
            {"pointer": pointer, "old_pointer": old_pointer, "label": node["preferred_term"]}
        )

    def add_water(self, parent):
        index = len(runner.get_node(self.after, parent))
        runner.get_node(self.after, parent).append({"preferred_term": "distilled water"})
        self.component(parent + [index])

    def direct(self):
        for i in range(len(self.before["ingredients"])):
            self.component(["ingredients", i], ["ingredients", i])
        if self.key.startswith("J"):
            self.add_water(["ingredients"])
        family = FAMILY[self.key]
        if family in {"J572", "J1008"}:
            snippet = TITRANT if family == "J572" else "Adjust pH to 7.5."
            self.root(
                "ph_value", 7.5, family, snippet, "Recipe-specific pH 7.5 overrides the base range."
            )
        else:
            snippet = "Adjust pH to 7.0 - 7.2." if family == "J377" else BASE_PH
            if "ph_value" in self.before:
                self.root(
                    "ph_value",
                    None,
                    self.table_key,
                    snippet,
                    "Keep the source range, not a midpoint.",
                )
            self.root(
                "ph_range",
                {"min": 7.0, "max": 7.2},
                self.table_key,
                snippet,
                "Source-explicit base pH range retained by this formulation.",
            )
        if family == "J572":
            if self.key == "J572":
                self.after["solutions"] = [{"preferred_term": "Na2CO3 solution", "composition": []}]
            stock = self.after["solutions"][0]
            stock["name"] = "Na2CO3 solution"
            reason = "Sterile sodium carbonate solution adjusts the medium to pH 7.5 after autoclaving. Dose and stock strength are unspecified; retain any source-explicit variable dose without inventing a numeric concentration."
            stock["notes"] = (stock.get("notes", "") + "\n\n" + reason).strip()
            for field in ("name", "preferred_term", "composition", "concentration", "notes"):
                self.proof(
                    ["solutions", 0, field],
                    "J572",
                    TITRANT,
                    reason,
                    old=["solutions", 0, field] if self.key == "M576" else None,
                    status="not_quantified" if field == "concentration" else None,
                )
            if self.key == "M576":
                self.proof(
                    ["solutions", 0, "concentration"],
                    "M576",
                    self.quote("M576", ["components", 0, "items", 10]),
                    reason,
                    old=["solutions", 0, "concentration"],
                    status="not_quantified",
                )
            self.lineage.append(
                {
                    "pointer": ["solutions", 0],
                    "old_pointer": ["solutions", 0] if self.key == "M576" else None,
                    "label": "Na2CO3 solution",
                }
            )
        note = f'Ingredient amounts use the exact formulation and preparation stage. Separate preparation excerpt: "{MAKEUP}". Conditional solid option: "{AGAR}". Agar is included only in M372/M960 in this reviewed variant cohort; no step ordering is invented.'
        if family == "J1008":
            note += " " + MG_NOTE
        if family == "J572":
            note += " The inherited base pH range does not replace the source-explicit post-autoclave pH 7.5 target."
        self.root(
            "notes", self.before.get("notes", "") + "\n\n" + note, self.table_key, MAKEUP, note
        )
        if family in MODIFICATIONS:
            self.proof(["notes"], family, MODIFICATIONS[family], note, old=["notes"])

    def prepared(self):
        source = "E1132" if self.key == "J1132" else "M1212"
        sp = ["solutions", 0, "recipe", 0] if self.key == "J1132" else ["components", 0, "items", 0]
        dose_quote = self.quote(source, sp)
        base_name = "Main sol. J168" if self.key == "J1132" else "Halobacteria medium (M159)"
        term = (
            {"id": "mediadive.solution:3823", "label": "Main sol. J168"}
            if self.key == "J1132"
            else None
        )
        stock = {
            "preferred_term": base_name,
            "name": base_name,
            "composition": copy.deepcopy(self.before["ingredients"]),
            "concentration": {"value": "1", "unit": "L"},
            "notes": STAGE_NOTE,
            "preparation_notes": MAKEUP + "\n" + BASE_PH + "\n" + AGAR,
        }
        if term:
            stock["term"] = term
        self.after["solutions"] = [stock]
        self.after["ingredients"] = []
        for i in range(len(self.before["ingredients"])):
            self.component(["solutions", 0, "composition", i], ["ingredients", i])
        self.add_water(["solutions", 0, "composition"])
        for field in ("preferred_term", "name", "concentration", "notes"):
            self.proof(["solutions", 0, field], source, dose_quote, STAGE_NOTE)
        if term:
            self.proof(
                ["solutions", 0, "term"],
                source,
                dose_quote,
                "Retain the exact dataset solution ID; no new CultureMech ID is created.",
            )
        self.proof(
            ["solutions", 0, "preparation_notes"],
            "J168",
            MAKEUP,
            STAGE_NOTE + f' Separate preparation excerpts: "{BASE_PH}"; "{AGAR}".',
        )
        self.proof(
            ["solutions", 0, "composition"],
            source,
            dose_quote,
            "Relocate existing base constituents with their original mappings and roles into the prepared-base stage. "
            + STAGE_NOTE,
            old=["ingredients"],
        )
        self.proof(
            ["ingredients"],
            source,
            dose_quote,
            "Remove flattened direct ingredients after their evidence-backed relocation; do not double-count the base.",
            old=["ingredients"],
        )
        self.lineage.append({"pointer": ["solutions", 0], "old_pointer": None, "label": base_name})
        step_quote = self.quote(
            source, ["solutions", 0, "steps", 0] if source == "E1132" else ["comments", 0]
        )
        self.root(
            "preparation_steps",
            [{"step_number": 1, "action": "ADJUST_PH", "description": "Adjust pH to 8.0."}],
            source,
            step_quote,
            "Keep only the final adjustment at medium scope. Base make-up, its pH 7.0-7.2 and conditional agar preparation belong inside the prepared base, not after the pH-8 adjustment.",
        )
        self.root(
            "ph_value",
            8.0,
            source,
            step_quote,
            "Final source-explicit pH target; do not infer titrant identity or volume.",
        )
        note = STAGE_NOTE + (
            " " + PROVIDER_NOTE
            if self.key == "J1132"
            else " The original JCM1132 is unavailable; this record is supported by its own TOGO M1212 source and the explicitly referenced M159/J168 base."
        )
        self.root("notes", self.before.get("notes", "") + "\n\n" + note, source, dose_quote, note)

    def solution(self):
        for i in range(len(self.before["composition"])):
            self.component(["composition", i], ["composition", i])
        self.add_water(["composition"])
        reason = (
            "The exact S3823 source lists all nine base constituents, now independently matched to composition. Remove only the false placeholder and its incomplete-composition flag; optional agar remains a conditional instruction, not a liquid-base ingredient. "
            + PROVIDER_NOTE
        )
        snippet = self.quote("E1132", ["solutions", 1, "recipe"])
        self.after.pop("ingredients")
        self.proof(
            ["ingredients"],
            "E1132",
            snippet,
            reason,
            old=["ingredients", 0, "concentration"],
            status="correct",
        )
        self.proof(["ingredients"], "E1132", snippet, reason, old=["ingredients"])
        flags = [f for f in self.before["data_quality_flags"] if f != "incomplete_composition"]
        self.root("data_quality_flags", flags or None, "E1132", snippet, reason)
        self.root(
            "notes",
            (self.before.get("notes", "") + "\n\n" + reason).strip(),
            "E1132",
            snippet,
            reason,
        )

    def link_support(self, child):
        if child == "J1132":
            return (
                "E1132",
                self.quote("E1132", ["solutions", 0, "recipe", 0]),
                STAGE_NOTE + " " + PROVIDER_NOTE,
            )
        if child == "M1212":
            return "M1212", self.quote("M1212", ["components", 0, "items", 0]), STAGE_NOTE
        family = FAMILY[child]
        if family == "J377":
            return (
                "J377",
                "NaCl 100.0 g",
                "Preserve the reviewed liquid salinity-variant relationship: the exact J377 and J168 base tables agree except NaCl 100 versus 200 g per 1 L; retain pH 7.0-7.2 and correct exact tracked paths.",
            )
        reason = {
            "J572": "The modified recipe uses 2 g/L magnesium sulfate heptahydrate and post-autoclave pH 7.5 with sterile carbonate solution. It is derived from the J168 base, not a duplicate or a concentration-only change.",
            "J1008": "This JCM-derived formulation changes NaCl to 270 g/L, magnesium sulfate heptahydrate to 15 g/L and pH to 7.5. It is not a source duplicate or a salt-only change. "
            + MG_NOTE,
            "J914": "The recipe changes NaCl from the referenced base's 200 g/L to 150 g/L. Retain the reviewed liquid/solid distinction and source-explicit agar option; correct exact tracked paths.",
        }[family]
        snippet = MODIFICATIONS[family]
        if family == "J572":
            snippet += " " + TITRANT
        elif family == "J1008":
            snippet += " Adjust pH to 7.5."
        return family, snippet, reason

    def links(self):
        children = (
            [self.key] if self.key in LINKS else [c for c, (p, _) in LINKS.items() if p == self.key]
        )
        for child in children:
            parent, relation = LINKS[child]
            source, snippet, reason = self.link_support(child)
            spec = self.specs[parent if self.key == child else child]
            name = runner.load_yaml(spec["before_text"])["name"]
            link = {
                "path": spec["path"],
                "relationship": relation,
                "id": spec["id"],
                "name": name,
                "notes": reason,
            }
            if self.key == child:
                self.root("parent_media", link, source, snippet, reason)
                self.root("variant_relationship", relation, source, snippet, reason)
                self.root("variant_modifications", [reason], source, snippet, reason)
                pointer, old_pointer = ["parent_media"], (
                    ["parent_media"] if "parent_media" in self.before else None
                )
            else:
                links = self.after["variant_children"]
                indices = [i for i, row in enumerate(links) if row["id"] == spec["id"]]
                runner.require(len(indices) <= 1, "Duplicate child link")
                index = indices[0] if indices else len(links)
                old_pointer = ["variant_children", index] if indices else None
                if indices:
                    links[index] = link
                else:
                    links.append(link)
                pointer = ["variant_children", index]
                self.proof(pointer, source, snippet, reason, old=old_pointer)
            if child in PREPARED:
                sp = ["solutions", 0, "steps", 0] if child == "J1132" else ["comments", 0]
                self.proof(pointer, source, self.quote(source, sp), reason, old=old_pointer)
            else:
                self.proof(
                    pointer,
                    "J168",
                    "NaCl 200.0 g" if FAMILY[child] in {"J377", "J914"} else BASE_PH,
                    reason,
                    old=old_pointer,
                )
                if child.startswith("M"):
                    self.proof(
                        pointer,
                        child,
                        self.quote(child, ["meta"]),
                        reason + " TOGO identifies JCM as the original source, not NBRC.",
                        old=old_pointer,
                    )

    def finish(self, timestamp):
        if self.key not in PARENTS:
            old_quantities = {
                tuple(c["pointer"]) + ("concentration",) for c in runner.all_claims(self.before)
            }
            accounted = {
                tuple(c["old_pointer"])
                for c in self.claims
                if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
            }
            runner.require(old_quantities == accounted, "Unreviewed old quantity")
        else:
            runner.require(
                self.after["ingredients"] == self.before["ingredients"],
                "Parent formulation changed",
            )
        for source in self.used:
            item = self.sources[source]
            meta = item["metadata"]
            refs = self.after.setdefault("references", [])
            if any(r["reference"] == meta["url"] for r in refs):
                continue
            refs.append(
                {
                    "reference": meta["url"],
                    "title": item["parsed_title"],
                    "notes": f"source_type={'culture_collection_page' if source.startswith('J') else 'dataset'}; discovery_mode={'manual_web_search' if source == 'E1132' else 'cross_reference'}; accessed_on={meta['accessed_at'][:10]}; accession={source}; response_sha256={meta['sha256']}. Authors/year are not supplied; no publication year or DOI is invented."
                    + (" " + PROVIDER_NOTE if source == "E1132" else ""),
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            timestamp=timestamp,
            action=ACTION,
            source="; ".join(self.sources[s]["metadata"]["url"] for s in self.used),
            changes="; ".join(
                f"{c['field']}: {c['old']} -> {c['new']}"
                for c in self.claims
                if c["old"] != c["new"]
            ),
            notes="Source-specific ingredient and variant review. Every change has an exact PURL-backed excerpt. Prepared-base quantities, unquantified water/titrant, source limitations, chemical identities and prior history are preserved; no taxa-media assertions are added.",
        )
        runner.require(
            self.after["curation_history"][:-1] == self.before["curation_history"],
            "History overwritten",
        )
        errors = runner.errors(self.after, self.spec["target_class"])
        runner.require(not errors, "Proposed schema failure: " + str(errors))
        return self.after, self.claims, self.lineage


def build(before, key, timestamp):
    review = Review(before, key)
    if key in PREPARED:
        review.prepared()
    elif key == "S3823":
        review.solution()
    elif key not in PARENTS:
        review.direct()
    review.links()
    return review.finish(timestamp)


def process(root, plan_path, mode="preview"):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    runner.require(not plan_path.is_symlink(), "Plan symlink")
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse plan overwrite")
    if mode != "preview":
        receipt = HERE / "validation-preview.json"
        runner.require(not receipt.is_symlink(), "Review receipt symlink")
        raw = receipt.read_bytes()
        runner.require(runner.sha(raw) == REVIEW_SHA, "Independent review receipt drift")
        gate = json.loads(raw)
        runner.require(
            gate["terminal"]
            and not gate["errors"]
            and gate["plan_sha256"] == runner.sha(plan_path.read_bytes())
            and gate["context_sha256"] == CONTEXT_SHA
            and set(gate["independent_audit"]) == PARENTS | PREPARED | set(FAMILY) | {"S3823"}
            and gate["supported_reference_checks"] == {"total": 417, "passed": 417}
            and gate["manual_dataset_entries"] == 25
            and gate["preserved_bibliography_not_reverified"] == 2,
            "Unreviewed plan",
        )
        for check in gate["checks"]:
            log = Path(check["log"])
            runner.require(
                check["exit_code"] == 0
                and not log.is_symlink()
                and runner.sha(log.read_bytes()) == check["log_sha256"],
                "Validation log drift",
            )
    context = frozen()
    for row in context["records"]:
        path = root / row["path"]
        runner.require(not path.is_symlink(), "Cohort symlink")
        if mode == "preview":
            runner.require(
                runner.sha(path.read_bytes()) == row["before_sha256"], "Current record drift"
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
