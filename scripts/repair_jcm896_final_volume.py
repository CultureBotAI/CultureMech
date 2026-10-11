#!/usr/bin/env python3
"""Repair JCM 896 from its original recipe, with a frozen, replayable plan."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from decimal import Decimal
from pathlib import Path

from fetch_solution_concentration_sources import load_yaml
from repair_komodo12_extraction_evidence import TableRows
from repair_mediadive_stock_concentration_evidence import cell, require, sha
from review_solution_concentration_evidence import field_name, get_node, render

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
TARGET = "data/normalized_yaml/bacterial/modified_bsk_medium.yaml"
BASELINE = "b04cd5b9c8da3f84b37c7dbd3a8db2d91a432df510277c46ea426177a7fc6e7c"
SEMANTIC_BASELINE = "59c23286338d1efcd630d943d694f06258dcd0dee579532cf9041da730be19f1"
SOURCE_SHA = "c6e814a8bff1580ddd42179b7d401a204ae19469786fdafd140408d1522f03c8"
SOURCE_FILE = "JCM_GRMD896.html"
URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=896"
ACCESSED = "2026-10-07"
ACTION = "CORRECTED_JCM896_ORIGINAL_RECIPE_FINAL_VOLUME"
PREPARATION = (
    "Adjust pH to 7.2 with NaOH, fill up to 584 ml with distilled water "
    "and filter-sterilize with 0.22 \u00b5m PES filter."
)
VOLUME_QUOTE = "fill up to 584 ml with distilled water"
ROWS = [
    ("HEPES", "3.0", "g"),
    ("Trisodium citrate\u00b72H2O", "0.35", "g"),
    ("Glucose", "2.5", "g"),
    ("Sodium pyruvate", "0.4", "g"),
    ("N-Acetyl-D-glucosamine", "0.2", "g"),
    ("NaHCO3", "1.1", "g"),
    ("MEM alpha Modification (BioWest)", "5.2", "g"),
    ("TC Yeastolate (BD-Difco)", "1.0", "g"),
    ("Probumin Universal Grade (Millipore)", "25.0", "g"),
    ("Neopeptone (BD-Difco)", "2.5", "g"),
    (
        "Rabbit serum sterile non-hemolyzed young (Pel-Freez code No. 31125)",
        "40.0",
        "ml",
    ),
]


class RecipeText(TableRows):
    """Keep inline chemical text intact while delimiting rendered table cells."""

    def __init__(self):
        super().__init__()
        self.visible = []
        self.hidden = 0

    def handle_starttag(self, tag, attrs):
        super().handle_starttag(tag, attrs)
        if tag in {"head", "script", "style"}:
            self.hidden += 1
        if not self.hidden and tag in {"tr", "td", "th", "p", "br", "hr", "h1", "div"}:
            self.visible.append(" ")

    def handle_endtag(self, tag):
        super().handle_endtag(tag)
        if tag in {"head", "script", "style"}:
            self.hidden -= 1
            require(self.hidden >= 0, "Unmatched hidden element")
        if not self.hidden and tag in {"tr", "td", "th", "p", "br", "hr", "h1", "div"}:
            self.visible.append(" ")

    def handle_data(self, data):
        super().handle_data(data)
        if not self.hidden:
            self.visible.append(data)


def inspect_source(raw):
    require(sha(raw.encode()) == SOURCE_SHA, "Original source hash drift")
    parser = RecipeText()
    parser.feed(raw)
    parser.close()
    require(
        parser.row is None and parser.cell is None and not parser.hidden,
        "Unclosed HTML",
    )
    rows = [tuple(" ".join(c.split()) for c in r["cells"]) for r in parser.rows]
    require(rows == ROWS, "Unreviewed source table or ingredient form")
    text = " ".join("".join(parser.visible).split())
    require(
        "Search for medium no. = [896]." in text
        and ("896 MODIFIED BSK MEDIUM " + " ".join(ROWS[0])) in text
        and text.count(PREPARATION) == 1,
        "Original recipe identity or final-volume/preparation drift",
    )
    for row in rows:
        require(" ".join(row) in text, "Row quote is not contiguous rendered source text")
    return rows, text


def build(doc, raw, timestamp):
    rows, _ = inspect_source(raw)
    semantic = json.dumps(doc, sort_keys=True, ensure_ascii=True, separators=(",", ":"))
    require(
        sha(semantic.encode()) == SEMANTIC_BASELINE,
        "Unreviewed local formulation drift",
    )
    require(
        not list(validate_recipe(doc, target_class="MediaRecipe")),
        "Baseline schema failure",
    )
    after = copy.deepcopy(doc)
    claims = []
    context = (
        f'Additional exact final-volume quote: "{VOLUME_QUOTE}"; locator=preparation '
        "following the ingredient table. Final volume 584 ml = 0.584 L. The imported "
        "40 ml denominator counts serum alone and is not the final volume. "
        f"Original JCM 896 recipe; accessed {ACCESSED}; capture SHA256={SOURCE_SHA}. "
        "HTML entities decoded and display whitespace normalized; inline chemical "
        "digits preserved. Existing ontology mappings and growth claims are not validated here."
    )

    def claim(pointer, old, new, snippet, locator, explanation, evidence_pointer):
        claims.append(
            {
                "pointer": pointer,
                "old_pointer": pointer,
                "field": field_name(pointer),
                "old": old,
                "new": new,
                "status": "correct",
                "reference": URL,
                "snippet": snippet,
                "locator": locator,
                "explanation": explanation,
                "evidence_pointer": evidence_pointer,
            }
        )

    for index, row in enumerate(rows):
        label, amount, unit = row
        node = after["ingredients"][index]
        pointer = ["ingredients", index, "concentration"]
        old = copy.deepcopy(node["concentration"])
        quantity = {
            "value": format(Decimal(amount) / Decimal("0.584"), ".6g"),
            "unit": "G_PER_L" if unit == "g" else "ML_PER_L",
        }
        snippet = " ".join(row)
        locator = f"ingredient table, row {index + 1}"
        explanation = (
            f"Correction of {field_name(pointer)} ({label}): source batch amount "
            f"{amount} {unit} / (584 ml / 1000 ml per L) = {quantity['value']} {unit}/L. "
            "Normalized arithmetic is rounded to six significant digits for storage, "
            "not increased experimental precision; original stated inputs are retained "
            "in the exact quotes. No mass/volume conversion or density is assumed. "
            f"Locator={locator}. {context}"
        )
        if index == 7:
            explanation += (
                " Also corrects ingredients[7].preferred_term from generic Yeast extract "
                "to the source-specified TC Yeastolate (BD-Difco) product; no ontology "
                "equivalence is inferred."
            )
            claim(
                ["ingredients", index, "preferred_term"],
                node["preferred_term"],
                label,
                snippet,
                locator,
                explanation,
                ["ingredients", index],
            )
            node["preferred_term"] = label
        node["concentration"] = quantity
        node["evidence"] = [
            {
                "reference": URL,
                "supports": "SUPPORT",
                "snippet": snippet,
                "explanation": explanation,
            }
        ]
        claim(
            pointer,
            old,
            quantity,
            snippet,
            locator,
            explanation,
            ["ingredients", index],
        )
    pointer = ["preparation_steps", 0, "description"]
    explanation = (
        "Corrects preparation_steps[0].description: restores the original micrometer "
        "symbol in the filtration pore size; pH, final volume, and FILTER_STERILIZE "
        f"action are unchanged. {context}"
    )
    claim(
        pointer,
        get_node(doc, pointer),
        PREPARATION,
        PREPARATION,
        "preparation following the ingredient table",
        explanation,
        [],
    )
    after["preparation_steps"][0]["description"] = PREPARATION
    after["evidence"] = [
        {
            "reference": URL,
            "supports": "SUPPORT",
            "snippet": PREPARATION,
            "explanation": explanation,
        }
    ]
    after["references"] = [
        {
            "reference": URL,
            "title": "JCM 896: MODIFIED BSK MEDIUM",
            "notes": f"source_type=culture_collection_page; discovery_mode=existing_record_reference; "
            f"source_organization=JCM; accessed_on={ACCESSED}; capture_sha256={SOURCE_SHA}; "
            "locator=ingredient table and following preparation. Individual authors and recipe "
            "publication year are not supplied; website copyright year is not publication evidence.",
        }
    ]
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        source=URL,
        timestamp=timestamp,
        notes="Corrected ten mass concentrations using the original 584 ml final volume; "
        "corrected serum to ml/L without density inference, restored TC Yeastolate product "
        "name and filtration symbol. Each change has original-recipe evidence; prior history, "
        "IDs and unrelated ontology/pH/growth fields are preserved.",
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'], sort_keys=True)} -> "
            f"{json.dumps(c['new'], sort_keys=True)}"
            for c in claims
        ),
    )
    require(
        not list(validate_recipe(after, target_class="MediaRecipe")),
        "Proposed schema failure",
    )
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
        "medium_id": "J896",
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
        "# JCM 896 Concentration Correction",
        "",
        f"- Follow-up target: {item['path']}",
        f"- ID: {item['id']}",
        f"- Reviewed commit: `{plan['commit']}`",
        f"- Before SHA256: `{item['before_sha256']}`",
        f"- Result SHA256: `{item['after_sha256']}`",
        f"- State: {'applied locally' if applied else 'preview'}",
        "",
        "This hash-linked successor preserves the one exact-path Record marker in the "
        "sixth cohort's original report. Every ingredient quantity and both nonnumeric "
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
    (folder / "J896.md").write_text("\n".join(lines) + "\n")


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
