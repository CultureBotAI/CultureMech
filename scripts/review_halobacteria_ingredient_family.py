#!/usr/bin/env python3
"""Preview or explicitly apply five independently reviewed Halobacteria repairs."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
from decimal import Decimal
from pathlib import Path

import repair_methanogen_stock_boundaries as shared
from curation_receipt_fixtures import read_receipt_capture
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.recipe_references import parse_recipe, recipe_source

runner, ROOT = shared.runner, shared.ROOT
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-halobacteria-family"
CONTEXT_SHA = "51b2cbe0e68dafaa7d155bd838c04e863169fc1de75e6ec64a856e77d7617bc3"
INSPECTION_SHA = "ac02f2b62e0309aa079e09d5016f23da70c98f18ea877cf9eb134ff038e65b6d"
REVIEW_SHA = "9025c39dfb7ea93a3281fced9bf335d6558a59a3f886ea9a75f082b585acbae2"
PLAN_PATH = HERE / "plan-v2.json"
ACTION = "CURATED_HALOBACTERIA_SOURCE_CONCENTRATIONS"
KEYS = {"J168", "J1007", "M159", "M160", "M1064"}
MAKEUP = "Add components to distilled water and bring volume to 1.0 L."
BASE_PH = "Adjust pH to 7.0-7.2."
AGAR = "For preparation of solid medium, add 20.0 g/L agar."
MODIFIED = (
    "Use Medium No. 168 supplemented with 1.0 g/L sodium pyruvate and "
    "1.0 g/L MgSO4\u00b77H2O (final)."
)
TITRATION = "After autoclaving, adjust pH to 8.0 with sterile Na2CO3 solution."
STERILIZE = "Unless otherwise stated, sterilize media by autoclaving at 121\u00b0C for 15 min."
MG_NOTE = (
    "The modified recipe explicitly states 1.0 g/L MgSO4 heptahydrate (final), "
    "also reported as 1 g/L by TOGO M1064. Record this source-stated target, not "
    "20 g/L copied from the base or an inferred 21 g/L sum. The word supplemented "
    "and the base recipe's 20 g per 1 L leave a preparation ambiguity: literal "
    "addition to the unchanged base cannot produce the stated lower target. "
    "This curation does not claim that operational ambiguity is resolved."
)
WATER_NOTE = (
    "Distilled water is used to bring the recipe to 1.0 L final volume. Its "
    "individual input volume and mass are unspecified; the imported 1 g/L is "
    "not supported, and the table's 1 L is not a fixed water dose."
)
ALIASES = {
    "Casamino acids": "Casamino acids (BD-Difco)",
    "Yeast extract": "Yeast extract (BD-Difco)",
    "Na glutamate": "Sodium glutamate",
    "MgSO4 x 7 H2O": "MgSO4\u00b77H2O",
    "MgSO4\u30fb7H2O": "MgSO4\u00b77H2O",
    "FeCl2 x 4 H2O": "FeCl2\u00b74H2O",
    "FeCl2\u30fb4H2O": "FeCl2\u00b74H2O",
    "MnCl2 x 4 H2O": "MnCl2\u00b74H2O",
    "MnCl2\u30fb4H2O": "MnCl2\u00b74H2O",
}


def frozen():
    raw = (HERE / "captures-approved.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Capture drift")
    context = json.loads(raw)
    raw = (HERE / "source-inspection.json").read_bytes()
    runner.require(runner.sha(raw) == INSPECTION_SHA, "Inspection drift")
    inspected = json.loads(raw)
    runner.require(
        context["terminal"]
        and not context["errors"]
        and inspected["terminal"]
        and inspected["capture_sha256"] == CONTEXT_SHA
        and {r["key"] for r in context["records"]} == KEYS,
        "Incomplete source review",
    )
    index = ROOT / "src/culturemech/data/mediaingredientmech/label_index.csv"
    runner.require(
        runner.sha(index.read_bytes()) == inspected["mim_metadata"]["sha256"],
        "MIM drift",
    )
    for key, item in context["sources"].items():
        raw, meta = item["raw"], item["metadata"]
        runner.require(
            meta["http_status"] == 200
            and meta["url"] == meta["response_url"]
            and runner.sha(raw.encode()) == meta["sha256"],
            "Raw source drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        parsed = parse_recipe(recipe_source(meta["url"]), raw, meta)
        runner.require(parsed.content == inspected["sources"][key]["text"], "Parsed source drift")
    return context, inspected


class Review:
    def __init__(self, before, key):
        self.context, self.inspected = frozen()
        self.specs = {r["key"]: r for r in self.context["records"]}
        runner.require(key in KEYS, "Unreviewed target")
        self.spec = self.specs[key]
        runner.require(before == runner.load_yaml(self.spec["before_text"]), "Baseline drift")
        runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
        runner.require(
            not before.get("evidence")
            and not before.get("references")
            and not before.get("variants")
            and all(not n.get("evidence") for n in before["ingredients"]),
            "Existing provenance requires separate reconciliation",
        )
        self.before, self.after, self.key = before, copy.deepcopy(before), key
        self.claims, self.lineage, self.used = [], [], []
        self.modified = key in {"J1007", "M1064"}
        self.base_rows = {
            name: (amount, unit)
            for name, amount, unit in self.inspected["sources"]["JCM168"]["table_rows"]
        }
        runner.require(len(self.base_rows) == 9, "Base table drift")
        self.togo_rows = {}
        if key.startswith("M"):
            data = json.loads(self.context["sources"][key]["raw"])
            jcm = "1007" if self.modified else "168"
            runner.require(
                data["meta"]["original_media_id"] == "JCM_M" + jcm + ("-2" if key == "M160" else "")
                and before["media_term"]["term"]["id"] == "TOGO:" + key,
                "TOGO source identity drift",
            )
            self.togo_rows = {
                row["component_name"]: (row, ["components", si, "items", ri])
                for si, section in enumerate(data["components"])
                for ri, row in enumerate(section["items"])
            }
            runner.require(
                len(self.togo_rows)
                == len(before["ingredients"]) + len(before.get("solutions", [])),
                "TOGO row inventory drift",
            )

    def claim(
        self,
        pointer,
        source,
        snippet,
        reason,
        evidence_pointer,
        old_pointer=None,
        status=None,
    ):
        meta = self.context["sources"][source]["metadata"]
        raw = self.context["sources"][source]["raw"]
        text = self.inspected["sources"][source]["text"] if source.startswith("JCM") else raw
        runner.require(snippet and snippet in text, "Nonliteral snippet")
        parent = runner.get_node(self.after, pointer[:-1])
        old = (
            runner.get_node(self.before, old_pointer[:-1]).get(old_pointer[-1])
            if old_pointer
            else None
        )
        new = parent.get(pointer[-1])
        field = runner.field_name(pointer)
        explanation = (
            f"{field}: {reason} Source locator: exact recipe row or preparation instruction; "
            f"accessed={meta['accessed_at']}; source SHA256={meta['sha256']}."
        )
        self.claims.append(
            {
                "pointer": pointer,
                "old_pointer": old_pointer,
                "field": field,
                "old_field": runner.field_name(old_pointer) if old_pointer else None,
                "ingredient": parent.get("preferred_term", "Recipe context"),
                "old": copy.deepcopy(old),
                "new": copy.deepcopy(new),
                "status": status
                or ("evidence_only" if old == new else "correct" if old is not None else "add"),
                "source": source,
                "reference": meta["url"],
                "snippet": snippet,
                "explanation": explanation,
                "evidence_pointer": evidence_pointer,
            }
        )
        entries = runner.get_node(self.after, evidence_pointer).setdefault("evidence", [])
        prior = [e for e in entries if e["reference"] == meta["url"]]
        runner.require(len(prior) <= 1, "Duplicate evidence reference")
        if prior:
            prior[0]["explanation"] += (
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

    def ingredient(self, index, *, added=False):
        pointer = ["ingredients", index]
        node = self.after["ingredients"][index]
        label = node["preferred_term"]
        canonical = ALIASES.get(label, label)
        old_pointer = None if added else pointer + ["concentration"]
        if label == "distilled water":
            node.pop("concentration", None)
            source, snippet, reason = "JCM168", MAKEUP, WATER_NOTE
        elif self.modified and canonical in {"MgSO4\u00b77H2O", "sodium pyruvate"}:
            node["concentration"] = {"value": "1", "unit": "G_PER_L"}
            source, snippet = "JCM1007", MODIFIED
            reason = (
                MG_NOTE
                if canonical.startswith("MgSO4")
                else "Explicit 1.0 g/L sodium pyruvate supplement in JCM1007; not present in unmodified JCM168."
            )
        elif label == "agar":
            runner.require(
                self.key == "M160",
                "Agar belongs only to the reviewed solid formulation",
            )
            node["concentration"] = {"value": "20", "unit": "G_PER_L"}
            source, snippet, reason = (
                "JCM168",
                AGAR,
                "Explicit 20.0 g/L agar option, selected by TOGO M160. Do not add agar to the liquid formulations.",
            )
        else:
            amount, unit = self.base_rows[canonical]
            old = node["concentration"]
            runner.require(Decimal(old["value"]) == Decimal(amount), "Unreviewed amount")
            node["concentration"] = {
                "value": old["value"],
                "unit": "MG_PER_L" if unit == "mg" else "G_PER_L",
            }
            source, snippet = "JCM168", f"{canonical} {amount} {unit}"
            reason = (
                f"JCM168 specifies {amount} {unit} in the recipe brought to 1.0 L; "
                f"{amount} {unit} / 1.0 L gives the stated per-liter rate. "
                f'Separate exact volume excerpt: "{MAKEUP}". '
                "Hydrate form is retained; no molar or density conversion is used."
            )
            if self.modified:
                reason += f' JCM1007 inherits this base component; separate exact cross-reference: "{MODIFIED}".'
        node["notes"] = (node.get("notes", "") + "\n\n" + reason).strip()
        self.claim(
            pointer + ["concentration"],
            source,
            snippet,
            reason,
            pointer,
            old_pointer,
            "not_quantified" if label == "distilled water" else None,
        )
        self.claim(
            pointer + ["notes"],
            source,
            snippet,
            reason,
            pointer,
            None if added else pointer + ["notes"],
        )
        if added:
            self.claim(pointer + ["preferred_term"], source, snippet, reason, pointer)
        if self.key.startswith("M"):
            row, sp = self.togo_rows[label]
            quote = json_excerpt(self.context["sources"][self.key]["raw"], sp)
            if label != "distilled water":
                unit = row["unit"]
                expected = "MG_PER_L" if unit == "mg" else "G_PER_L"
                runner.require(
                    Decimal(str(row["volume"])) == Decimal(node["concentration"]["value"])
                    and expected == node["concentration"]["unit"],
                    "TOGO amount/unit conflict",
                )
            self.claim(
                pointer + ["concentration"],
                self.key,
                quote,
                reason + f" TOGO row locator: {runner.field_name(sp)}.",
                pointer,
                old_pointer,
                "not_quantified" if label == "distilled water" else None,
            )
        self.lineage.append(
            {
                "pointer": pointer,
                "old_pointer": None if added else pointer,
                "source": source,
                "label": label,
            }
        )

    def set_root(self, field, value, source, snippet, reason):
        if value is None:
            self.after.pop(field, None)
        else:
            self.after[field] = value
        self.claim(
            [field],
            source,
            snippet,
            reason,
            [],
            [field] if field in self.before else None,
        )

    def formulate(self):
        for index in range(len(self.before["ingredients"])):
            self.ingredient(index)
        if not self.key.startswith("M"):
            self.after["ingredients"].append({"preferred_term": "distilled water"})
            self.ingredient(len(self.after["ingredients"]) - 1, added=True)
        if self.key == "J1007":
            self.after["ingredients"].append({"preferred_term": "sodium pyruvate"})
            self.ingredient(len(self.after["ingredients"]) - 1, added=True)
        if self.modified:
            self.set_root(
                "ph_value",
                8.0,
                "JCM1007",
                TITRATION,
                "Explicit post-autoclave pH target; carbonate dose and stock strength are unspecified.",
            )
            if self.key == "J1007":
                self.after["solutions"] = [
                    {
                        "preferred_term": "Na2CO3 solution",
                        "name": "Na2CO3 solution",
                        "composition": [],
                    }
                ]
            stock = self.after["solutions"][0]
            stock["name"] = "Na2CO3 solution"
            stock["notes"] = (
                stock.get("notes", "")
                + "\n\nSterile Na2CO3 solution is added after autoclaving to adjust pH to 8.0. Neither a fixed dose nor a stock strength is supplied; no inline strength is invented."
            ).strip()
            for field in (
                "preferred_term",
                "name",
                "composition",
                "concentration",
                "notes",
            ):
                old = ["solutions", 0, field] if self.key == "M1064" else None
                self.claim(
                    ["solutions", 0, field],
                    "JCM1007",
                    TITRATION,
                    stock["notes"],
                    [],
                    old,
                    "not_quantified" if field == "concentration" else None,
                )
            if self.key == "M1064":
                _, sp = self.togo_rows["Na2CO3 solution"]
                self.claim(
                    ["solutions", 0, "concentration"],
                    self.key,
                    json_excerpt(self.context["sources"][self.key]["raw"], sp),
                    stock["notes"] + f" TOGO row locator: {runner.field_name(sp)}.",
                    [],
                    ["solutions", 0, "concentration"],
                    "not_quantified",
                )
            self.lineage.append(
                {
                    "pointer": ["solutions", 0],
                    "old_pointer": ["solutions", 0] if self.key == "M1064" else None,
                    "source": "JCM1007",
                    "label": "Na2CO3 solution",
                }
            )
        else:
            if "ph_value" in self.before:
                self.set_root(
                    "ph_value",
                    None,
                    "JCM168",
                    BASE_PH,
                    "Retain the source range, not its midpoint as a single target.",
                )
            self.set_root(
                "ph_range",
                {"min": 7.0, "max": 7.2},
                "JCM168",
                BASE_PH,
                "Source-explicit pH range.",
            )
        if self.key in {"J1007", "J168"}:
            parent, child = self.specs["J168"], self.specs["J1007"]
            reason = "JCM1007 modifies JCM168 with sodium pyruvate, a distinct magnesium target and pH 8.0. It is not a SOURCE_DUPLICATE. Correct the reviewed reciprocal link's stale category path only; other family relationships need separate source review."
            if self.key == "J1007":
                link = {
                    "path": parent["path"],
                    "relationship": "DERIVED_FROM",
                    "id": parent["id"],
                    "name": "halobacteria_medium",
                }
                self.set_root("parent_media", link, "JCM1007", MODIFIED, reason)
                self.set_root("variant_relationship", "DERIVED_FROM", "JCM1007", MODIFIED, reason)
                self.set_root(
                    "variant_modifications",
                    [
                        MG_NOTE,
                        "Add sodium pyruvate at 1 g/L and adjust pH to 8.0 after autoclaving.",
                    ],
                    "JCM1007",
                    MODIFIED,
                    reason + " " + TITRATION,
                )
            else:
                children = copy.deepcopy(self.before["variant_children"])
                matches = [i for i, link in enumerate(children) if link["id"] == child["id"]]
                runner.require(len(matches) == 1, "Child link drift")
                i = matches[0]
                children[i].update(path=child["path"], relationship="DERIVED_FROM", notes=reason)
                self.after["variant_children"] = children
                self.claim(
                    ["variant_children", i, "path"],
                    "JCM1007",
                    MODIFIED,
                    reason,
                    [],
                    ["variant_children", i, "path"],
                )
                self.claim(
                    ["variant_children", i, "relationship"],
                    "JCM1007",
                    MODIFIED,
                    reason,
                    [],
                    ["variant_children", i, "relationship"],
                )
                self.claim(
                    ["variant_children", i, "notes"],
                    "JCM1007",
                    MODIFIED,
                    reason,
                    [],
                    ["variant_children", i, "notes"],
                )
        context_note = (
            f'Source preparation excerpts: "{MAKEUP}"; "{STERILIZE}". '
            "These instructions are not converted into an inferred step ordering. "
        )
        if self.modified:
            context_note += f'Separate JCM1007 excerpt: "{TITRATION}". {MG_NOTE}'
        else:
            context_note += f'Separate JCM168 excerpts: "{BASE_PH}"; "{AGAR}". '
            context_note += (
                "The agar option is selected only for M160; liquid formulations remain unchanged."
            )
        self.after["notes"] += "\n\n" + context_note
        self.claim(["notes"], "JCM168", MAKEUP, context_note, [], ["notes"])
        if self.modified:
            self.claim(["notes"], "JCM1007", MODIFIED, context_note, [], ["notes"])

    def finish(self, timestamp):
        old_claims = {tuple(c["pointer"]) for c in runner.all_claims(self.before)}
        reviewed = {
            tuple(c["old_pointer"][:-1])
            for c in self.claims
            if c["old_pointer"] and c["old_pointer"][-1] == "concentration"
        }
        runner.require(old_claims == reviewed, "Unreviewed old quantity")
        runner.require(
            self.after.get("high_metal") == self.before.get("high_metal"),
            "Unreviewed high-metal flag",
        )
        for source in self.used:
            item = self.context["sources"][source]
            meta = item["metadata"]
            self.after.setdefault("references", []).append(
                {
                    "reference": meta["url"],
                    "title": item["parsed_title"],
                    "notes": f"source_type={'culture_collection_page' if source.startswith('JCM') else 'dataset'}; discovery_mode={'cross_reference' if source == 'JCM168' and self.modified else 'existing_record_reference'}; accessed_on={meta['accessed_at'][:10]}; accession={source}; response_sha256={meta['sha256']}. Authors and publication year are not supplied; copyright year is not treated as publication year.",
                }
            )
        record_curation_event(
            self.after,
            curator="codex",
            timestamp=timestamp,
            action=ACTION,
            source=self.context["sources"]["JCM1007" if self.modified else "JCM168"]["metadata"][
                "url"
            ],
            changes="; ".join(
                f"{c['field']}: {c['old']} -> {c['new']}"
                for c in self.claims
                if c["old"] != c["new"]
            ),
            notes="Source-specific ingredient review with exact PURL-backed excerpts. Trace metals use mg/L, water is final-volume make-up, and modified-medium magnesium retains the explicit source target and preparation ambiguity. Existing chemical mappings and high-metal flags are preserved; no taxa-media claims are added.",
        )
        runner.require(
            self.after["curation_history"][:-1] == self.before["curation_history"],
            "History overwritten",
        )
        runner.require(not runner.errors(self.after, "MediaRecipe"), "Proposed schema failure")
        return self.after, self.claims, self.lineage


def build(before, key, timestamp):
    review = Review(before, key)
    review.formulate()
    return review.finish(timestamp)


def process(root, plan_path, mode="preview"):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    runner.require(not plan_path.is_symlink(), "Plan symlink")
    if mode != "preview":
        receipt = HERE / "validation-preview.json"
        runner.require(not receipt.is_symlink(), "Review receipt symlink")
        reviewed = receipt.read_bytes()
        runner.require(runner.sha(reviewed) == REVIEW_SHA, "Independent review receipt drift")
        gate = json.loads(reviewed)
        runner.require(
            gate["terminal"]
            and not gate["errors"]
            and gate["plan_sha256"] == runner.sha(plan_path.read_bytes())
            and gate["context_sha256"] == CONTEXT_SHA
            and gate["inspection_sha256"] == INSPECTION_SHA
            and set(gate["independent_audit"]) == KEYS
            and gate["reference_checks"] == {"total": 105, "passed": 105},
            "Unreviewed plan",
        )
        for check in gate["checks"]:
            runner.require(check["exit_code"] == 0, "Validation log drift")
            try:
                read_receipt_capture(check["log"], check["log_sha256"])
            except ValueError as error:
                raise ValueError("Validation log drift") from error
    context, _ = frozen()
    for item in context["records"]:
        path = root / item["path"]
        runner.require(not path.is_symlink(), "Cohort symlink")
        if mode == "preview":
            runner.require(
                runner.sha(path.read_bytes()) == item["before_sha256"], "Current record drift"
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
