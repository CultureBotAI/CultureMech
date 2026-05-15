#!/usr/bin/env python3
"""Build a corpus manifest for the media growth evidence review.

The manifest is intentionally lightweight: it records every normalized
YAML record, whether it is part of the primary growable-media target set,
and whether existing growth-evidence proposal files cover it.
"""
from __future__ import annotations

import csv
import json
from collections import Counter
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
YAML_ROOT = REPO_ROOT / "data" / "normalized_yaml"
OUT_DIR = REPO_ROOT / "reports"
TSV_OUT = OUT_DIR / "media_growth_review_manifest.tsv"
JSON_OUT = OUT_DIR / "media_growth_review_manifest.json"
MD_OUT = OUT_DIR / "media_growth_review_manifest_summary.md"
PROPOSAL_DIRS = [
    REPO_ROOT / "workspace" / "reports" / "growth_evidence_proposals",
    REPO_ROOT / "workspace" / "reports" / "growth_evidence_proposals_backfill",
]

PRIMARY_DIRS = {"algae", "archaea", "bacterial", "fungal", "specialized"}


def load_yaml(path: Path) -> dict:
    try:
        with path.open() as f:
            data = yaml.safe_load(f) or {}
    except Exception as e:
        return {"_load_error": str(e)}
    return data if isinstance(data, dict) else {"_load_error": "not a mapping"}


def proposal_index() -> dict[str, dict]:
    indexed: dict[str, dict] = {}
    for proposal_dir in PROPOSAL_DIRS:
        if not proposal_dir.is_dir():
            continue
        for path in sorted(proposal_dir.rglob("*.yaml")):
            data = load_yaml(path)
            recipe_path = data.get("recipe_path") or ""
            candidates = data.get("candidates") or []
            support_count = sum(1 for c in candidates if isinstance(c, dict) and c.get("supports") == "SUPPORT")
            review_count = sum(1 for c in candidates if isinstance(c, dict) and c.get("supports") == "REVIEW")
            entry = {
                "proposal_path": str(path.relative_to(REPO_ROOT)),
                "candidate_count": len(candidates),
                "support_count": support_count,
                "review_count": review_count,
            }
            if recipe_path:
                indexed[recipe_path] = entry
            else:
                # Also index by stem as fallback for old/manual proposals
                # that do not declare a concrete recipe_path.
                indexed.setdefault(path.stem, entry)
    return indexed


def applied_growth_counts(data: dict) -> dict[str, int]:
    target_organisms = data.get("target_organisms") or []
    growth_metric_count = 0
    supported_evidence_count = 0
    genome_id_count = 0
    if not isinstance(target_organisms, list):
        return {
            "growth_metric_count": 0,
            "supported_growth_evidence_count": 0,
            "genome_id_count": 0,
        }
    for organism in target_organisms:
        if not isinstance(organism, dict):
            continue
        genome_ids = organism.get("genome_assembly_id") or []
        if isinstance(genome_ids, list):
            genome_id_count += len(genome_ids)
        elif genome_ids:
            genome_id_count += 1
        for metric in organism.get("growth_metrics") or []:
            if not isinstance(metric, dict):
                continue
            growth_metric_count += 1
            for ev in metric.get("evidence") or []:
                if isinstance(ev, dict) and ev.get("supports") == "SUPPORT":
                    supported_evidence_count += 1
        for ev in organism.get("evidence") or []:
            if isinstance(ev, dict) and ev.get("supports") == "SUPPORT":
                supported_evidence_count += 1
    return {
        "growth_metric_count": growth_metric_count,
        "supported_growth_evidence_count": supported_evidence_count,
        "genome_id_count": genome_id_count,
    }


def iter_records(proposals: dict[str, dict]) -> list[dict]:
    rows: list[dict] = []
    for path in sorted(YAML_ROOT.rglob("*.yaml")):
        rel = str(path.relative_to(REPO_ROOT))
        parts = path.relative_to(YAML_ROOT).parts
        category_dir = parts[0] if parts else ""
        data = load_yaml(path)

        primary_target = category_dir in PRIMARY_DIRS
        excluded_reason = "" if primary_target else "supporting_solution_record"

        proposal = proposals.get(rel) or proposals.get(path.stem) or {}
        growth_counts = applied_growth_counts(data)
        support_count = proposal.get("support_count", 0)
        review_count = proposal.get("review_count", 0)
        candidate_count = proposal.get("candidate_count", 0)
        if growth_counts["growth_metric_count"] and growth_counts["supported_growth_evidence_count"]:
            review_status = "applied_growth_evidence"
        elif support_count:
            review_status = "has_supported_growth_candidate"
        elif candidate_count:
            review_status = "has_review_candidates"
        elif proposal.get("proposal_path"):
            review_status = "reviewed_no_candidates"
        else:
            review_status = "not_reviewed"

        rows.append({
            "yaml_path": rel,
            "category_dir": category_dir,
            "primary_target": primary_target,
            "excluded_reason": excluded_reason,
            "id": data.get("id", ""),
            "name": data.get("name", ""),
            "original_name": data.get("original_name", ""),
            "medium_type": data.get("medium_type", ""),
            "physical_state": data.get("physical_state", ""),
            "target_organism_count": len(data.get("target_organisms") or []),
            "growth_metric_count": growth_counts["growth_metric_count"],
            "supported_growth_evidence_count": growth_counts["supported_growth_evidence_count"],
            "genome_id_count": growth_counts["genome_id_count"],
            "variant_count": len(data.get("variants") or []),
            "proposal_path": proposal.get("proposal_path", ""),
            "proposal_candidate_count": candidate_count,
            "proposal_support_count": support_count,
            "proposal_review_count": review_count,
            "review_status": review_status,
            "load_error": data.get("_load_error", ""),
        })
    return rows


def write_outputs(rows: list[dict]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    fields = [
        "yaml_path",
        "category_dir",
        "primary_target",
        "excluded_reason",
        "id",
        "name",
        "original_name",
        "medium_type",
        "physical_state",
        "target_organism_count",
        "growth_metric_count",
        "supported_growth_evidence_count",
        "genome_id_count",
        "variant_count",
        "proposal_path",
        "proposal_candidate_count",
        "proposal_support_count",
        "proposal_review_count",
        "review_status",
        "load_error",
    ]
    with TSV_OUT.open("w", newline="") as f:
        writer = csv.DictWriter(f, fields, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    with JSON_OUT.open("w") as f:
        json.dump(rows, f, indent=2)

    total = len(rows)
    primary = [r for r in rows if r["primary_target"]]
    supporting = total - len(primary)
    by_status = Counter(r["review_status"] for r in rows)
    by_primary_status = Counter(r["review_status"] for r in primary)
    by_dir = Counter(r["category_dir"] for r in rows)
    errors = [r for r in rows if r["load_error"]]
    with_applied_growth = [r for r in rows if r["growth_metric_count"]]
    with_supported_applied = [r for r in rows if r["supported_growth_evidence_count"]]
    with_genome_ids = [r for r in rows if r["genome_id_count"]]
    with_variants = [r for r in rows if r["variant_count"]]

    lines = [
        "# Media Growth Review Manifest Summary",
        "",
        "Generated from `data/normalized_yaml/**/*.yaml` and existing proposal YAMLs.",
        "",
        "## Counts",
        "",
        f"- Total normalized YAML records: {total}",
        f"- Primary target records: {len(primary)}",
        f"- Supporting solution records: {supporting}",
        f"- YAML load errors: {len(errors)}",
        f"- Records with applied growth metrics: {len(with_applied_growth)}",
        f"- Records with supported applied growth evidence: {len(with_supported_applied)}",
        f"- Records with genome assembly IDs on target organisms: {len(with_genome_ids)}",
        f"- Records with modeled variants: {len(with_variants)}",
        "",
        "## Records By Directory",
        "",
        "| Directory | Count |",
        "|---|---:|",
    ]
    for key, count in sorted(by_dir.items()):
        lines.append(f"| `{key}` | {count} |")

    lines.extend([
        "",
        "## Review Status",
        "",
        "| Status | All records | Primary targets |",
        "|---|---:|---:|",
    ])
    for status in ("applied_growth_evidence", "has_supported_growth_candidate", "has_review_candidates", "reviewed_no_candidates", "not_reviewed"):
        lines.append(f"| `{status}` | {by_status.get(status, 0)} | {by_primary_status.get(status, 0)} |")

    lines.extend([
        "",
        "## Outputs",
        "",
        f"- TSV: `{TSV_OUT.relative_to(REPO_ROOT)}`",
        f"- JSON: `{JSON_OUT.relative_to(REPO_ROOT)}`",
        "",
        "This manifest is a coverage artifact only. It does not validate that all records have been researched.",
        "",
    ])
    MD_OUT.write_text("\n".join(lines))


def main() -> int:
    rows = iter_records(proposal_index())
    write_outputs(rows)
    print(f"Wrote {TSV_OUT.relative_to(REPO_ROOT)}")
    print(f"Wrote {JSON_OUT.relative_to(REPO_ROOT)}")
    print(f"Wrote {MD_OUT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
