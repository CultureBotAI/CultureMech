#!/usr/bin/env python3
"""Curate KOMODO 12 only after verifying its exact original-recipe linkage."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from html.parser import HTMLParser
from pathlib import Path

from fetch_medium_concentration_sources import read_capture
from fetch_solution_concentration_sources import load_yaml
from repair_extraction_input_boundaries import COHORT
from repair_extraction_input_boundaries import build as rebuild_extraction
from repair_mediadive_stock_concentration_evidence import cell, require, sha
from review_solution_concentration_evidence import field_name, render

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
REPORTS = Path("reports/ingredient_concentration_curation")
PREVIOUS = REPORTS / "20261007-extraction-boundaries"
TARGET = "data/normalized_yaml/bacterial/KOMODO_12_SOIL_EXTRACT_medium.yaml"
BASELINE = "a50360f78301c8271e740406501c61d9b67e8947d14869b6e7a835fc824bc504"
PREVIOUS_SHA = "2d036c265c2c608a6fe382dbf55650e31412c395fea4325be0b9681d70fb5586"
HANDOFF_SHA = "29126c32da267433d703952a03f9121bae8dfddb3664ae8793546c9eb7bbc645"
ACTION = "CORRECTED_KOMODO12_EXTRACTION_FROM_VERIFIED_SOURCE_LINK"
MAPPING_URL = (
    "https://komodo.modelseed.org/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaList"
)
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium12.pdf"
SCIENCE = ("ingredients", "solutions", "preparation_steps", "evidence", "references")


class TableRows(HTMLParser):
    """Parse real table cells and links, not name-containing text matches."""

    def __init__(self):
        super().__init__()
        self.rows = []
        self.row = self.cell = None

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            require(self.row is None, "Nested source table row")
            self.row = {"cells": [], "links": []}
        elif tag in {"td", "th"} and self.row is not None:
            require(self.cell is None, "Nested source table cell")
            self.cell = []
        elif tag == "a" and self.row is not None:
            self.row["links"].append(dict(attrs))

    def handle_data(self, data):
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if tag in {"td", "th"} and self.row is not None:
            require(self.cell is not None, "Unmatched source cell")
            self.row["cells"].append("".join(self.cell).strip())
            self.cell = None
        elif tag == "tr" and self.row is not None:
            require(self.cell is None, "Unclosed source cell")
            self.rows.append(self.row)
            self.row = None


def verify_mapping(raw, handoff):
    require(
        handoff["reference"] == MAPPING_URL
        and handoff["record"] == TARGET
        and handoff["http_status"] == 200
        and sha(raw.encode()) == handoff["sha256"],
        "Source mapping identity/hash drift",
    )
    parser = TableRows()
    parser.feed(raw)
    parser.close()
    require(parser.row is None and parser.cell is None, "Unclosed source table")
    rows = [r for r in parser.rows if r["cells"] and r["cells"][0] == "12"]
    expected = handoff["source_row"]
    require(len(rows) == 1, "Missing or duplicate KOMODO source ID")
    require(
        rows[0] == {k: expected[k] for k in ("cells", "links")}
        and raw.count(expected["snippet"]) == 1,
        "Source mapping excerpt mismatch",
    )
    require(
        rows[0]["cells"]
        == [
            "12",
            "SOIL EXTRACT medium",
            "6.8 - 7.0",
            "true",
            "false",
            "false",
            PDF.replace("https:", "http:"),
        ]
        and {"href": PDF.replace("https:", "http:")} in rows[0]["links"],
        "Unreviewed source mapping/formulation",
    )


def build(doc, source_before, raw, meta, mapping, handoff, timestamp):
    verify_mapping(mapping, handoff)
    require(not list(validate_recipe(doc, target_class="MediaRecipe")), "Baseline schema failure")
    require(
        doc["id"] == "CultureMech:004048"
        and doc["original_name"] == "SOIL EXTRACT medium"
        and doc["media_term"]["term"] == {"id": "komodo.medium:12", "label": "SOIL EXTRACT medium"}
        and "DSMZ Medium: 12 (mediadive.medium:12)" in doc["notes"],
        "Local source identity drift",
    )
    require(
        doc["physical_state"] == source_before["physical_state"] == "SOLID_AGAR"
        and doc["ph_range"] == source_before["ph_range"] == {"min": 6.8, "max": 7.0}
        and doc["variant_relationship"] == "SOURCE_DUPLICATE"
        and doc["parent_media"]["id"] == source_before["id"] == "CultureMech:000762"
        and doc["parent_media"]["path"]
        == "data/normalized_yaml/bacterial/soil_extract_medium.yaml",
        "Unreviewed parent/formulation context",
    )
    require(
        not any(
            k in doc
            for k in ("solutions", "preparation_steps", "evidence", "references", "variants")
        ),
        "Existing context needs reconciliation",
    )
    expected_inputs = copy.deepcopy(source_before["ingredients"])
    for node in expected_inputs:
        node.pop("evidence", None)
    require(doc["ingredients"] == expected_inputs, "Local ingredient/context drift")
    # Rebuild from primary source captures; another curated YAML is not evidence.
    rebuilt, claims, _ = rebuild_extraction(source_before, raw, meta, "12", timestamp)
    after = copy.deepcopy(doc)
    for key in SCIENCE:
        after[key] = copy.deepcopy(rebuilt[key])
    for claim in claims:
        if claim["old_pointer"] and claim["old_pointer"][0] == "preparation_steps":
            claim.update(old=None, old_pointer=None, status="add")
        if claim["status"] == "verified":
            claim["status"] = "evidence_only"
    after["evidence"].append(
        {
            "reference": MAPPING_URL,
            "supports": "SUPPORT",
            "snippet": handoff["source_row"]["snippet"],
            "explanation": "Source-identity evidence for media_term and the ingredients, solutions, and preparation_steps curated here. The exact KOMODO ID 12 row links the original DSMZ 12 recipe. Quantities and preparation are supported separately by the exact DSMZ/MediaDive recipe excerpts, not by the KOMODO table or another local record. "
            + f"Locator={handoff['locator']}; retrieved {handoff['accessed_at']}; response SHA256={handoff['sha256']}. No new source accession, formulation variant, or growth claim is inferred.",
        }
    )
    after["references"].append(
        {
            "reference": MAPPING_URL,
            "title": "KOMODO - the Known Media Database",
            "notes": f"source_type=dataset; discovery_mode=existing_record_reference; source_organization=KOMODO; accessed_on={handoff['accessed_at'][:10]}; locator={handoff['locator']}; response_sha256={handoff['sha256']}. Exact ID and original DSMZ recipe link verified; individual authors/publication year not established. This reference supports the source mapping, not ingredient quantities.",
        }
    )
    claims.append(
        {
            "pointer": ["media_term"],
            "old_pointer": ["media_term"],
            "field": "media_term",
            "old": copy.deepcopy(doc["media_term"]),
            "new": copy.deepcopy(after["media_term"]),
            "status": "evidence_only",
            "reference": MAPPING_URL,
            "snippet": handoff["source_row"]["snippet"],
            "source_pointer": None,
            "locator": handoff["locator"],
            "evidence_pointer": [],
            "explanation": "Exact KOMODO source ID links DSMZ 12. This supports source identity only; separate original-recipe evidence supports each concentration and preparation field.",
        }
    )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        source=MAPPING_URL,
        timestamp=timestamp,
        notes="Original KOMODO source link and DSMZ recipe verified. Removed unsupported soil concentration, retained input mass in notes, corrected initial water to 1 L, and restored extraction/agar preparation. No recovered volume, extract yield, or absolute extract dose inferred.",
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'], sort_keys=True)} -> {json.dumps(c['new'], sort_keys=True)} ({c['status']})"
            for c in claims
        ),
    )
    require(not list(validate_recipe(after, target_class="MediaRecipe")), "Proposed schema failure")
    return after, claims


def process(root, source_dir, plan_path, mode):
    previous_bytes = (root / PREVIOUS / "plan.json").read_bytes()
    require(sha(previous_bytes) == PREVIOUS_SHA, "Pinned scientific review drift")
    previous = json.loads(previous_bytes)
    source = next(r for r in previous["records"] if r["medium_id"] == "12")
    require(
        sha((root / source["path"]).read_bytes()) == source["after_sha256"], "Parent result drift"
    )
    require(
        sha((source_dir / "DSMZ_Medium12.pdf").read_bytes()) == COHORT["12"]["pdf_sha"], "PDF drift"
    )
    mapping_bytes = (root / PREVIOUS / "komodo12-source-handoff.json").read_bytes()
    require(sha(mapping_bytes) == HANDOFF_SHA, "Pinned mapping handoff drift")
    handoff = json.loads(mapping_bytes)
    mapping = (source_dir / "komodo-media-list.html").read_text()
    raw, meta = read_capture(source_dir / "sources", "12")
    require(meta["sha256"] == source["source_sha256"], "Recipe source drift")
    tracked = (
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root)
        .decode()
        .split("\0")
    )
    path = root / TARGET
    require(TARGET in tracked and not path.is_symlink(), "Non-exact or symlink target")
    current = path.read_bytes()
    if mode == "preview":
        require(not plan_path.exists(), "Refuse to overwrite a reviewed plan")
        plan = {
            "version": 1,
            "action": ACTION,
            "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root)
            .decode()
            .strip(),
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
    require(sha(before) == BASELINE, "Unreviewed baseline drift")
    after, claims = build(
        load_yaml(before),
        load_yaml(source["before_text"]),
        raw,
        meta,
        mapping,
        handoff,
        plan["created_at"],
    )
    output = render(before.decode(), after)
    item = {
        "path": TARGET,
        "id": after["id"],
        "medium_id": "12",
        "action": ACTION,
        "before_text": before.decode(),
        "before_sha256": sha(before),
        "after_text": output.decode(),
        "after_sha256": sha(output),
        "source_sha256": meta["sha256"],
        "source_accessed_at": meta["accessed_at"],
        "mapping_sha256": handoff["sha256"],
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
        require(path.read_bytes() == output, "Repair not applied or persisted result differs")
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
        "# KOMODO 12 Ingredient Concentration Review",
        "",
        f"- Record: {item['path']}",
        f"- ID: {item['id']}",
        f"- Reviewed commit: `{plan['commit']}`",
        f"- Before SHA256: `{item['before_sha256']}`",
        f"- Result SHA256: `{item['after_sha256']}`",
        f"- State: {'applied locally' if applied else 'preview'}",
        "",
        "All three input ingredients and the restored extraction preparation are covered below. The extract dose/yield is unspecified, not guessed. The source mapping is verified separately from the recipe amounts. See README.md and validation.json for source metadata, validation, and remaining scope.",
        "",
        "| Field | Old field | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision | Action |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for claim in item["claims"]:
        row = dict(
            claim,
            old_field=field_name(claim["old_pointer"]) if claim["old_pointer"] else None,
            action="applied" if applied else "preview",
        )
        lines.append(
            "| "
            + " | ".join(
                cell(row.get(k))
                for k in (
                    "field",
                    "old_field",
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
    (folder / "12.md").write_text("\n".join(lines) + "\n")


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
