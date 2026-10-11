#!/usr/bin/env python3
"""Restore JCM 1105's base and carbonate dose from its original recipe."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from decimal import Decimal
from pathlib import Path

from fetch_solution_concentration_sources import load_yaml
from repair_jcm896_final_volume import RecipeText
from repair_mediadive_stock_concentration_evidence import cell, require, sha
from review_solution_concentration_evidence import field_name, render

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
TARGET = "data/normalized_yaml/bacterial/virgibacillus_merv_medium.yaml"
BASELINE = "349e8317e227697953c3b6feafc3cba1aabc29c827f35c792803896cb2e311e7"
SEMANTIC_BASELINE = "d30edb6f50058fc4872ad0a911e185db259a49f27e4629934cf6a56d2184873f"
SOURCE_SHA = "2c7d8a4ae523578495afb0f7de58f4185a15a9cd5a489e938f46602d714356f8"
SOURCE_FILE = "JCM_GRMD1105-scope.html"
URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1105"
ACCESSED = "2026-10-07"
ACTION = "CORRECTED_JCM1105_ORIGINAL_RECIPE_STOCK_BOUNDARY"
MAKEUP = "Add components to distilled water and bring volume to 1.0 L."
OPTIONAL_AGAR = "For preparation of solid medium, add 20.0 g/L agar."
ADDITION = "After autoclaving, add the following solution (autoclaved):"
BRIDGE = f"{MAKEUP} {OPTIONAL_AGAR} {ADDITION}"
PH = "Readjust pH to 8.0, if necessary."
HEADER = (
    "Medium data Search for medium no. = [1105]. "
    "Unless otherwise stated, sterilize media by autoclaving at 121\u00b0C for 15 min. "
    "1105 VIRGIBACILLUS MERV MEDIUM"
)
FOOTER = "Copyright \u00a9 2026 Microbe Division (JCM) - All Rights Reserved"
BASE_ROWS = [
    ("Yeast extract", "10.0", "g"),
    ("Trisodium citrate\u00b73H2O", "3.0", "g"),
    ("MgSO4\u00b77H2O", "1.0", "g"),
    ("KCl", "3.0", "g"),
    ("NaCl", "100.0", "g"),
]
STOCK_ROW = ("10% Na2CO3 solution", "10.0", "ml")
LABELS = ["Yeast extract", "Trisodium citrate x 3 H2O", "MgSO4 x 7 H2O", "KCl", "NaCl", "Na2CO3"]
BASE_NOTES = f"{MAKEUP} {OPTIONAL_AGAR}"
STOCK_NOTES = "Autoclave the carbonate solution before adding it to the autoclaved base."
ROOT_STEP = (
    "Autoclave the prepared 1.0 L base. After autoclaving, add 10.0 ml of the "
    "autoclaved 10% Na2CO3 solution."
)
CARBONATE_NOTES = (
    "Original JCM 1105 specifies a 10% Na2CO3 solution without its percentage basis. "
    "The 10.0 ml addition is a stock dose, not 10 g/L carbonate. No numeric stock "
    "or final-medium carbonate concentration is asserted."
)


class RecipeSections(RecipeText):
    """Retain table boundaries and intervening preparation, not just flattened rows."""

    def __init__(self):
        super().__init__()
        self.tables = []
        self.pending = None
        self.section_end = 0

    def handle_starttag(self, tag, attrs):
        if tag == "table":
            require(self.pending is None, "Nested source table")
            self.pending = {
                "row_start": len(self.rows),
                "preceding": " ".join("".join(self.visible[self.section_end :]).split()),
            }
        super().handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        super().handle_endtag(tag)
        if tag == "table":
            require(self.pending is not None, "Unmatched source table")
            rows = self.rows[self.pending["row_start"] :]
            self.tables.append(
                {
                    "preceding": self.pending["preceding"],
                    "rows": [tuple(" ".join(c.split()) for c in r["cells"]) for r in rows],
                }
            )
            self.pending = None
            self.section_end = len(self.visible)


def inspect_source(raw):
    require(sha(raw.encode()) == SOURCE_SHA, "Original source hash drift")
    parser = RecipeSections()
    parser.feed(raw)
    parser.close()
    require(
        parser.row is None and parser.cell is None and not parser.hidden and parser.pending is None,
        "Unclosed source HTML",
    )
    require(
        parser.tables
        == [
            {"preceding": HEADER, "rows": BASE_ROWS},
            {"preceding": BRIDGE, "rows": [STOCK_ROW]},
        ],
        "Original recipe identity, tables or preparation drift",
    )
    tail = " ".join("".join(parser.visible[parser.section_end :]).split())
    require(tail == f"{PH} {FOOTER}", "Post-addition preparation drift")
    visible = " ".join("".join(parser.visible).split())
    for row in [*BASE_ROWS, STOCK_ROW]:
        require(" ".join(row) in visible, "Noncontiguous source row")
    return parser.tables, visible


def build(doc, raw, timestamp):
    inspect_source(raw)
    semantic = json.dumps(doc, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    require(sha(semantic.encode()) == SEMANTIC_BASELINE, "Unreviewed local formulation drift")
    require(not list(validate_recipe(doc, target_class="MediaRecipe")), "Baseline schema failure")
    require(
        [n["preferred_term"] for n in doc["ingredients"]] == LABELS, "Local ingredient order drift"
    )
    after = copy.deepcopy(doc)
    nodes = after["ingredients"]
    after["ingredients"] = []
    after["solutions"] = [
        {
            "preferred_term": "JCM 1105 base solution",
            "concentration": {"value": "1", "unit": "L"},
            "notes": "The complete 1.0 L prepared base is used per recipe batch; this is not a final-medium volume or per-liter working dose.",
            "composition": nodes[:5],
            "preparation_notes": BASE_NOTES,
        },
        {
            "preferred_term": STOCK_ROW[0],
            "concentration": {"value": "0.010", "unit": "L"},
            "notes": "Add 10.0 ml per recipe batch after autoclaving the 1.0 L base. The percentage basis and final-medium volume are not specified.",
            "composition": [nodes[5]],
            "preparation_notes": STOCK_NOTES,
        },
    ]
    claims = []
    context = (
        f"Original JCM 1105 recipe; accessed {ACCESSED}; capture SHA256={SOURCE_SHA}. "
        "HTML entities decoded and display whitespace normalized; chemical digits and "
        "source hydrate forms preserved. These are distinct preparation stages; no "
        "complete-medium final volume, density, percentage basis, ontology equivalence "
        "or growth claim is inferred."
    )

    def claim(
        pointer, old_pointer, old, new, status, snippet, locator, explanation, evidence_pointer
    ):
        entry = {
            "pointer": pointer,
            "old_pointer": old_pointer,
            "field": field_name(pointer),
            "old_field": field_name(old_pointer) if old_pointer else None,
            "old": copy.deepcopy(old),
            "new": copy.deepcopy(new),
            "status": status,
            "reference": URL,
            "snippet": snippet,
            "locator": locator,
            "explanation": explanation + " " + context,
            "evidence_pointer": evidence_pointer,
        }
        claims.append(entry)
        return entry

    for index, (label, amount, _) in enumerate(BASE_ROWS):
        node = nodes[index]
        old = copy.deepcopy(node["concentration"])
        node["concentration"] = {
            "value": format(Decimal(amount) / Decimal("1.0"), "f"),
            "unit": "G_PER_L",
        }
        pointer = ["solutions", 0, "composition", index, "concentration"]
        explanation = (
            f"Relocates ingredients[{index}] to solutions[0].composition[{index}] and corrects "
            f"{field_name(pointer)} ({label}) to the prepared-base amount: {amount} g / "
            f"1.0 L = {node['concentration']['value']} g/L. Additional exact makeup quote: "
            f'"{MAKEUP}"; locator=prose between the first and second tables. The imported '
            "quantity divided by the later 10 ml stock dose, not the 1 L base."
        )
        entry = claim(
            pointer,
            ["ingredients", index, "concentration"],
            old,
            node["concentration"],
            "correct",
            " ".join(BASE_ROWS[index]),
            f"first table, row {index + 1}",
            explanation,
            pointer[:-1],
        )
        node["evidence"] = [
            {
                "reference": URL,
                "supports": "SUPPORT",
                "snippet": entry["snippet"],
                "explanation": entry["explanation"],
            }
        ]

    carbonate = nodes[5]
    old = carbonate.pop("concentration")
    carbonate["notes"] = CARBONATE_NOTES
    pointer = ["solutions", 1, "composition", 0, "concentration"]
    explanation = (
        "Relocates ingredients[5] to solutions[1].composition[0], removes the unsupported "
        "10 g/L encoding from solutions[1].composition[0].concentration and records the "
        "source's unspecified percentage basis in solutions[1].composition[0].notes. "
        "The original table states a 10.0 ml stock addition, not a carbonate mass. "
        "No numeric carbonate concentration is asserted at either stage."
    )
    entry = claim(
        pointer,
        ["ingredients", 5, "concentration"],
        old,
        None,
        "remove_unsupported",
        " ".join(STOCK_ROW),
        "second table, sole row",
        explanation,
        pointer[:-1],
    )
    carbonate["evidence"] = [
        {
            "reference": URL,
            "supports": "SUPPORT",
            "snippet": entry["snippet"],
            "explanation": entry["explanation"],
        }
    ]

    root_claims = []
    for index, quote, explanation in [
        (
            0,
            MAKEUP,
            "The explicitly prepared 1.0 L base is used per recipe batch. This creates solutions[0].concentration as a batch amount, not a final-volume claim.",
        ),
        (
            1,
            " ".join(STOCK_ROW),
            "The original 10.0 ml dose / 1000 ml per L = 0.010 L per batch. This creates solutions[1].concentration, not a per-liter working dose or carbonate mass.",
        ),
    ]:
        root_claims.append(
            claim(
                ["solutions", index, "concentration"],
                None,
                None,
                after["solutions"][index]["concentration"],
                "add",
                quote,
                "inter-table preparation" if index == 0 else "second table, sole row",
                explanation,
                [],
            )
        )
    old_step = doc["preparation_steps"][0]["description"]
    root_claims.append(
        claim(
            ["solutions", 0, "preparation_notes"],
            ["preparation_steps", 0, "description"],
            old_step,
            BASE_NOTES,
            "correct_stage",
            BRIDGE,
            "inter-table preparation",
            "Moves base makeup and conditional agar instructions into solutions[0].preparation_notes. Liquid physical state remains unchanged; no agar is added.",
            [],
        )
    )
    root_claims.append(
        claim(
            ["solutions", 1, "preparation_notes"],
            None,
            None,
            STOCK_NOTES,
            "add_stage",
            ADDITION,
            "inter-table preparation",
            "Records the source's separately autoclaved carbonate-stock preparation in solutions[1].preparation_notes.",
            [],
        )
    )
    after["preparation_steps"][0]["description"] = ROOT_STEP
    root_claims.append(
        claim(
            ["preparation_steps", 0, "description"],
            ["preparation_steps", 0, "description"],
            old_step,
            ROOT_STEP,
            "correct_stage",
            BRIDGE,
            "inter-table preparation and following stock table",
            "Clarifies preparation_steps[0].description after moving base makeup to its solution: autoclave the base, then add the autoclaved 10.0 ml stock. The existing AUTOCLAVE action and later pH readjustment are preserved.",
            [],
        )
    )
    after["evidence"] = [
        {
            "reference": URL,
            "supports": "SUPPORT",
            "snippet": MAKEUP,
            "explanation": " ".join(c["explanation"] for c in root_claims)
            + f' Additional exact preparation excerpt: "{BRIDGE}"; locator=between the tables. '
            + f'Additional exact stock-row excerpt: "{" ".join(STOCK_ROW)}"; locator=second table, sole row.',
        }
    ]
    after["references"] = [
        {
            "reference": URL,
            "title": "JCM 1105: VIRGIBACILLUS MERV MEDIUM",
            "notes": f"source_type=culture_collection_page; discovery_mode=existing_record_reference; source_organization=JCM; accessed_on={ACCESSED}; capture_sha256={SOURCE_SHA}; locator=two ingredient tables and intervening/following preparation. Individual authors and recipe publication year are not supplied; copyright year is not publication evidence.",
        }
    ]
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        source=URL,
        timestamp=timestamp,
        notes="Restored six ingredient nodes to the original base and carbonate-stock stages; corrected five base concentrations using explicit 1 L makeup; removed unsupported carbonate g/L and retained unspecified 10% strength in notes. Added two explicit batch-volume doses and scoped preparation. IDs, prior history, mappings, liquid state, pH and unrelated metadata preserved.",
        changes="; ".join(
            f"{c['old_field']} -> {c['field']}: {json.dumps(c['old'], sort_keys=True)} -> {json.dumps(c['new'], sort_keys=True)}"
            for c in claims
        ),
    )
    require(not list(validate_recipe(after, target_class="MediaRecipe")), "Proposed schema failure")
    return after, claims


def process(root, source_dir, plan_path, mode):
    require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    tracked = (
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root)
        .decode()
        .split("\0")
    )
    path = root / TARGET
    require(TARGET in tracked and not path.is_symlink(), "Non-exact or symlink target")
    current = path.read_bytes()
    raw = (source_dir / SOURCE_FILE).read_bytes().decode("utf-8")
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root).decode().strip()
    if mode == "preview":
        require(not plan_path.exists(), "Refuse to overwrite a reviewed plan")
        plan = {
            "version": 1,
            "action": ACTION,
            "commit": commit,
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
        before = current
    else:
        plan = json.loads(plan_path.read_text())
        require(
            plan["version"] == 1 and plan["action"] == ACTION and len(plan["records"]) == 1,
            "Wrong plan",
        )
        before = plan["records"][0]["before_text"].encode()
    require(sha(before) == BASELINE, "Unreviewed baseline hash drift")
    after, claims = build(load_yaml(before), raw, plan["created_at"])
    output = render(before.decode(), after)
    item = {
        "path": TARGET,
        "id": after["id"],
        "medium_id": "J1105",
        "action": ACTION,
        "before_text": before.decode(),
        "before_sha256": sha(before),
        "after_text": output.decode(),
        "after_sha256": sha(output),
        "source_sha256": SOURCE_SHA,
        "source_accessed_at": ACCESSED,
        "claims": claims,
    }
    require(current in (before, output), "Concurrent edit")
    if mode == "preview":
        plan["records"] = [item]
        plan_path.parent.mkdir(parents=True, exist_ok=True)
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        require(plan["records"] == [item], "Plan/source/decision drift")
        require(path.read_bytes() == current, "Concurrent edit before write")
        if mode == "apply" and current != output:
            path.write_bytes(output)
        require(path.read_bytes() == output, "Repair not applied or result differs")
    return plan, {
        "mode": mode,
        "records": 1,
        "changed": int(mode == "apply" and current != output),
        "already_applied": int(current == output),
        "scoped_claims": len(claims),
    }


def report(folder, plan, applied):
    item = plan["records"][0]
    lines = [
        "# JCM 1105 Stock-Boundary Correction",
        "",
        f"- Follow-up target: {item['path']}",
        f"- ID: {item['id']}",
        f"- Reviewed commit: `{plan['commit']}`",
        f"- Before SHA256: `{item['before_sha256']}`",
        f"- Result SHA256: `{item['after_sha256']}`",
        f"- State: {'applied locally' if applied else 'preview'}",
        "",
        "This hash-linked successor preserves the one exact-path Record marker in the "
        "seventh cohort's original report. All scoped quantity, stock and preparation "
        "corrections are below; see README.md and validation.json for validation and scope.",
        "",
        "| Field | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision | Action |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for c in item["claims"]:
        row = dict(c, action="applied" if applied else "preview")
        lines.append(
            "| "
            + " | ".join(
                cell(row[k])
                for k in (
                    "field",
                    "old",
                    "new",
                    "status",
                    "reference",
                    "snippet",
                    "locator",
                    "explanation",
                    "action",
                )
            )
            + " |"
        )
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "J1105.md").write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--reports", type=Path)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    modes.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, args.source_dir, args.plan, mode)
    if args.reports:
        report(args.reports, plan, mode != "preview")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
