#!/usr/bin/env python3
"""Propose parent/child media-variant links from the content review manifest."""

from __future__ import annotations

import argparse
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
REPORTS_DIR = REPO_ROOT / "reports"
DEFAULT_MANIFEST = REPORTS_DIR / "media_content_review_manifest.tsv"

PROPOSAL_COLUMNS = [
    "ingredient_identity_signature",
    "status",
    "confidence",
    "relationship",
    "parent_path",
    "parent_id",
    "parent_name",
    "child_path",
    "child_id",
    "child_name",
    "group_size",
    "concentration_signature_count",
    "physical_state_count",
    "parent_score",
    "child_score",
    "review_reason",
    "modifications",
]

GROUP_COLUMNS = [
    "ingredient_identity_signature",
    "status",
    "confidence",
    "parent_path",
    "parent_id",
    "parent_name",
    "group_size",
    "child_count",
    "relationship_counts",
    "concentration_signature_count",
    "physical_state_count",
    "category_count",
    "review_reason",
]

MODIFIED_PATTERNS = (
    r"\bmodified\b",
    r"\bfor_dsm\b",
    r"\bfor_strain",
    r"\bfor_strains",
    r"\badditional\b",
    r"\bwith\b",
    r"\bwithout\b",
    r"\breplace\b",
    r"\bno_",
    r"\bhalf_strength\b",
    r"\blow\b",
    r"\bhigh\b",
)

SUPPLEMENT_PATTERNS = (
    "with",
    "additional",
    "supplement",
    "blood",
    "serum",
    "antibiotic",
    "glucose",
    "starch",
    "maltose",
    "yeast_extract",
    "nacl",
    "salt",
)

ALGAE_SOURCE_DUPLICATE_REVIEW_REASON = (
    "algae source-duplicate candidate has identical parsed ingredients but "
    "semantically broad medium names; verify source/formulation before migration"
)


def int_value(row: dict[str, str], key: str) -> int:
    try:
        return int(row.get(key) or 0)
    except ValueError:
        return 0


def norm_name(value: str) -> str:
    text = str(value or "").lower()
    text = re.sub(r"[^a-z0-9]+", "_", text)
    return re.sub(r"_+", "_", text).strip("_")


def is_modified_name(row: dict[str, str]) -> bool:
    name = norm_name(row.get("name") or row.get("original_name") or row.get("yaml_path"))
    return any(re.search(pattern, name) for pattern in MODIFIED_PATTERNS)


def complete_concentration(row: dict[str, str]) -> bool:
    return (
        int_value(row, "missing_concentration_count") == 0
        and int_value(row, "malformed_concentration_count") == 0
        and int_value(row, "missing_concentration_value_count") == 0
        and int_value(row, "missing_concentration_unit_count") == 0
    )


def score_parent(row: dict[str, str]) -> int:
    total = max(int_value(row, "total_component_count"), 1)
    chebi_ratio = int_value(row, "ingredient_chebi_term_count") / total
    mim_ratio = int_value(row, "mediaingredientmech_count") / total

    score = 0
    if row.get("id"):
        score += 20
    if row.get("media_term_id"):
        score += 30
    if row.get("original_name"):
        score += 10
    if complete_concentration(row):
        score += 20
    if int_value(row, "non_schema_concentration_unit_count") == 0:
        score += 10
    score += round(30 * chebi_ratio)
    score += round(20 * mim_ratio)
    if row.get("has_merge_fingerprint") == "True":
        score += 5
    if row.get("has_chemical_fingerprint") == "True":
        score += 5
    if row.get("has_variant_fingerprint") == "True":
        score += 5
    if is_modified_name(row):
        score -= 40
    path = row.get("yaml_path", "")
    if "/KOMODO_" in path or "/TOGO_" in path or "/DSMZ_" in path or "/JCM_" in path:
        score += 10
    return score


def choose_parent(rows: list[dict[str, str]]) -> dict[str, str]:
    return sorted(
        rows,
        key=lambda row: (
            -score_parent(row),
            is_modified_name(row),
            len(row.get("name") or row.get("yaml_path") or ""),
            row.get("yaml_path") or "",
        ),
    )[0]


def infer_relationship(parent: dict[str, str], child: dict[str, str]) -> str:
    child_name = norm_name(child.get("name") or child.get("original_name") or child.get("yaml_path"))
    parent_name = norm_name(parent.get("name") or parent.get("original_name") or parent.get("yaml_path"))
    if child.get("physical_state") != parent.get("physical_state"):
        return "PHYSICAL_STATE_VARIANT"
    if "nacl" in child_name or "salt" in child_name or "salinity" in child_name:
        return "SALINITY_VARIANT"
    if re.search(r"\bph_?\d", child_name):
        return "PH_VARIANT"
    if "without" in child_name or re.search(r"\bno_", child_name):
        return "OMITTED_COMPONENT_VARIANT"
    if "replace" in child_name:
        return "SUBSTITUTED_COMPONENT_VARIANT"
    if any(pattern in child_name for pattern in SUPPLEMENT_PATTERNS):
        return "SUPPLEMENTED_VARIANT"
    if child.get("ingredient_concentration_signature") != parent.get("ingredient_concentration_signature"):
        return "CONCENTRATION_VARIANT"
    if child_name != parent_name:
        return "SOURCE_DUPLICATE"
    return "DERIVED_FROM"


def confidence_for_group(rows: list[dict[str, str]], parent: dict[str, str]) -> tuple[str, str]:
    group_size = len(rows)
    total_components = {int_value(row, "total_component_count") for row in rows}
    non_schema_units = sum(int_value(row, "non_schema_concentration_unit_count") for row in rows)
    missing_conc = sum(int_value(row, "missing_concentration_count") for row in rows)
    variable_records = sum(1 for row in rows if "VARIABLE" in (row.get("concentration_units") or ""))
    categories = {row.get("category_dir") for row in rows if row.get("category_dir")}

    reasons = []
    confidence = "HIGH"
    if group_size > 500:
        confidence = "LOW"
        reasons.append("very large group likely driven by low-information shared ingredients")
    elif group_size > 100:
        confidence = "MEDIUM"
        reasons.append("large group requires family-level review before migration")
    if len(total_components) == 1 and next(iter(total_components), 0) <= 1 and group_size > 20:
        confidence = "LOW"
        reasons.append("low component-count group")
    if variable_records > group_size * 0.5:
        confidence = "LOW"
        reasons.append("majority of records use VARIABLE concentrations")
    if non_schema_units:
        confidence = min(confidence, "MEDIUM", key=["LOW", "MEDIUM", "HIGH"].index)
        reasons.append("non-schema concentration units present")
    if missing_conc:
        confidence = "LOW"
        reasons.append("missing concentration objects present")
    if len(categories) > 1:
        confidence = min(confidence, "MEDIUM", key=["LOW", "MEDIUM", "HIGH"].index)
        reasons.append("group spans multiple category directories")
    if is_modified_name(parent):
        confidence = min(confidence, "MEDIUM", key=["LOW", "MEDIUM", "HIGH"].index)
        reasons.append("selected parent name appears modified")
    if is_algae_source_duplicate_group(rows, parent):
        confidence = "LOW"
        reasons.append(ALGAE_SOURCE_DUPLICATE_REVIEW_REASON)
    return confidence, "; ".join(reasons)


def status_for_group(confidence: str, group_size: int) -> str:
    if confidence == "LOW":
        return "REVIEW_REQUIRED"
    if group_size > 100:
        return "REVIEW_REQUIRED"
    return "PROPOSED"


def is_algae_source_duplicate_group(rows: list[dict[str, str]], parent: dict[str, str]) -> bool:
    categories = {row.get("category_dir") for row in rows if row.get("category_dir")}
    if categories != {"algae"}:
        return False
    parent_name = norm_name(parent.get("name") or parent.get("original_name") or parent.get("yaml_path"))
    parent_concentration = parent.get("ingredient_concentration_signature")
    for row in rows:
        row_name = norm_name(row.get("name") or row.get("original_name") or row.get("yaml_path"))
        if row_name != parent_name and row.get("ingredient_concentration_signature") == parent_concentration:
            return True
    return False


def modification_text(parent: dict[str, str], child: dict[str, str], relationship: str) -> str:
    if relationship == "SOURCE_DUPLICATE":
        return "Same ingredient and concentration signature; review as possible duplicate source record."
    if relationship == "PHYSICAL_STATE_VARIANT":
        return f"Physical state differs from parent: {parent.get('physical_state')} -> {child.get('physical_state')}."
    if relationship == "CONCENTRATION_VARIANT":
        return "Same ingredient identity signature but concentration signature differs from parent."
    if relationship == "SALINITY_VARIANT":
        return "Name suggests salt/salinity change; verify concentration delta against source."
    if relationship == "PH_VARIANT":
        return "Name suggests pH change; verify pH/formulation delta against source."
    if relationship == "SUPPLEMENTED_VARIANT":
        return "Name suggests added supplement/component; verify ingredient delta against source."
    if relationship == "OMITTED_COMPONENT_VARIANT":
        return "Name suggests omitted component; verify ingredient delta against source."
    if relationship == "SUBSTITUTED_COMPONENT_VARIANT":
        return "Name suggests substituted component; verify ingredient delta against source."
    return "Candidate child formulation requires source/formulation review."


def read_manifest(path: Path) -> list[dict[str, str]]:
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        return [row for row in reader if not row.get("load_error")]


def build_proposals(rows: list[dict[str, str]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if int_value(row, "total_component_count") == 0:
            continue
        grouped[row["ingredient_identity_signature"]].append(row)

    proposals: list[dict[str, Any]] = []
    group_rows: list[dict[str, Any]] = []
    for ident_sig, members in sorted(grouped.items()):
        if len(members) < 2:
            continue
        parent = choose_parent(members)
        confidence, review_reason = confidence_for_group(members, parent)
        status = status_for_group(confidence, len(members))
        concentration_sigs = {m["ingredient_concentration_signature"] for m in members}
        physical_states = {m["physical_state"] for m in members if m.get("physical_state")}
        categories = {m["category_dir"] for m in members if m.get("category_dir")}
        relationship_counter: Counter[str] = Counter()

        for child in members:
            if child["yaml_path"] == parent["yaml_path"]:
                continue
            relationship = infer_relationship(parent, child)
            relationship_counter[relationship] += 1
            proposals.append(
                {
                    "ingredient_identity_signature": ident_sig,
                    "status": status,
                    "confidence": confidence,
                    "relationship": relationship,
                    "parent_path": parent["yaml_path"],
                    "parent_id": parent.get("id", ""),
                    "parent_name": parent.get("name", ""),
                    "child_path": child["yaml_path"],
                    "child_id": child.get("id", ""),
                    "child_name": child.get("name", ""),
                    "group_size": len(members),
                    "concentration_signature_count": len(concentration_sigs),
                    "physical_state_count": len(physical_states),
                    "parent_score": score_parent(parent),
                    "child_score": score_parent(child),
                    "review_reason": review_reason,
                    "modifications": modification_text(parent, child, relationship),
                }
            )

        group_rows.append(
            {
                "ingredient_identity_signature": ident_sig,
                "status": status,
                "confidence": confidence,
                "parent_path": parent["yaml_path"],
                "parent_id": parent.get("id", ""),
                "parent_name": parent.get("name", ""),
                "group_size": len(members),
                "child_count": len(members) - 1,
                "relationship_counts": ";".join(
                    f"{rel}:{count}" for rel, count in sorted(relationship_counter.items())
                ),
                "concentration_signature_count": len(concentration_sigs),
                "physical_state_count": len(physical_states),
                "category_count": len(categories),
                "review_reason": review_reason,
            }
        )
    proposals.sort(
        key=lambda row: (
            row["status"],
            row["confidence"],
            -int(row["group_size"]),
            row["parent_path"],
            row["child_path"],
        )
    )
    group_rows.sort(
        key=lambda row: (
            row["status"],
            row["confidence"],
            -int(row["group_size"]),
            row["parent_path"],
        )
    )
    return proposals, group_rows


def write_tsv(path: Path, rows: list[dict[str, Any]], columns: list[str]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=columns, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)


def write_summary(proposals: list[dict[str, Any]], groups: list[dict[str, Any]], out: Path) -> None:
    status_counts = Counter(row["status"] for row in proposals)
    confidence_counts = Counter(row["confidence"] for row in proposals)
    relationship_counts = Counter(row["relationship"] for row in proposals)
    group_status_counts = Counter(row["status"] for row in groups)

    lines = [
        "# Media Variant Link Proposal Summary",
        "",
        "Generated from `reports/media_content_review_manifest.tsv`.",
        "",
        "## Scope",
        "",
        f"- Candidate parent groups: {len(groups):,}",
        f"- Candidate parent-child links: {len(proposals):,}",
        f"- Proposed links ready for curated migration: {status_counts.get('PROPOSED', 0):,}",
        f"- Links requiring review before migration: {status_counts.get('REVIEW_REQUIRED', 0):,}",
        "",
        "## Group Status",
        "",
        "| Status | Groups |",
        "|---|---:|",
    ]
    for status, count in sorted(group_status_counts.items()):
        lines.append(f"| `{status}` | {count:,} |")
    lines.extend(["", "## Link Confidence", "", "| Confidence | Links |", "|---|---:|"])
    for confidence, count in sorted(confidence_counts.items()):
        lines.append(f"| `{confidence}` | {count:,} |")
    lines.extend(["", "## Relationship Counts", "", "| Relationship | Links |", "|---|---:|"])
    for relationship, count in relationship_counts.most_common():
        lines.append(f"| `{relationship}` | {count:,} |")
    lines.extend(
        [
            "",
            "## Outputs",
            "",
            "- Link proposals: `reports/media_variant_link_proposals.tsv`",
            "- Link proposals JSON: `reports/media_variant_link_proposals.json`",
            "- Group proposals: `reports/media_variant_parent_group_proposals.tsv`",
            "- Group proposals JSON: `reports/media_variant_parent_group_proposals.json`",
            "",
            "These are proposed relationships, not applied YAML edits. `PROPOSED` rows "
            "still require source/formulation review before writing parent/child links.",
        ]
    )
    out.write_text("\n".join(lines) + "\n")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, default=DEFAULT_MANIFEST)
    parser.add_argument("--reports-dir", type=Path, default=REPORTS_DIR)
    args = parser.parse_args()

    args.reports_dir.mkdir(parents=True, exist_ok=True)
    rows = read_manifest(args.manifest)
    proposals, group_rows = build_proposals(rows)

    proposal_tsv = args.reports_dir / "media_variant_link_proposals.tsv"
    proposal_json = args.reports_dir / "media_variant_link_proposals.json"
    group_tsv = args.reports_dir / "media_variant_parent_group_proposals.tsv"
    group_json = args.reports_dir / "media_variant_parent_group_proposals.json"
    summary_md = args.reports_dir / "media_variant_link_proposal_summary.md"

    write_tsv(proposal_tsv, proposals, PROPOSAL_COLUMNS)
    proposal_json.write_text(json.dumps(proposals, indent=2, sort_keys=True) + "\n")
    write_tsv(group_tsv, group_rows, GROUP_COLUMNS)
    group_json.write_text(json.dumps(group_rows, indent=2, sort_keys=True) + "\n")
    write_summary(proposals, group_rows, summary_md)

    print(f"Wrote {proposal_tsv.relative_to(REPO_ROOT)}")
    print(f"Wrote {proposal_json.relative_to(REPO_ROOT)}")
    print(f"Wrote {group_tsv.relative_to(REPO_ROOT)}")
    print(f"Wrote {group_json.relative_to(REPO_ROOT)}")
    print(f"Wrote {summary_md.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
