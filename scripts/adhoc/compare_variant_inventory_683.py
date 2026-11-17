#!/usr/bin/env python3
"""Compare pinned #684 base rows with a #683 v2 candidate, 2026-11-16.

Inputs: two immutable bundles and independently supplied manifest SHA256 pins.
Outputs: a new local summary and identity/label/context-only delta TSVs.
Uses streaming CSV parsing and all original columns; no recipe or input writes,
network access, scientific approval, MIM intake or SSSOM release publication.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import itertools
import json
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VARIANT_FIELDS = (
    "variant_index",
    "variant_name",
    "change_index",
    "change_action",
    "change_stage",
    "descriptor_role",
    "descriptor_path",
    "source_modification_index",
    "source_text",
    "evidence_json",
    "change_json",
)


def fingerprint(path):
    digest = hashlib.sha256()
    size = 0
    with path.open("rb") as stream:
        while chunk := stream.read(1024 * 1024):
            digest.update(chunk)
            size += len(chunk)
    return {"sha256": digest.hexdigest(), "bytes": size}


def pinned_bundle(directory, pin):
    raw = (directory / "manifest.json").read_bytes()
    if hashlib.sha256(raw).hexdigest() != pin:
        raise ValueError("manifest does not match independently supplied pin")
    manifest = json.loads(raw)
    for name, expected in manifest["products"].items():
        path = directory / name
        if Path(name).name != name or path.is_symlink() or not path.is_file():
            raise ValueError("unsafe/missing product")
        if fingerprint(path) != {key: expected[key] for key in ("sha256", "bytes")}:
            raise ValueError("product differs from pinned manifest: " + name)
    return manifest


def fields(path):
    with path.open(encoding="utf-8", newline="") as stream:
        return next(csv.reader(stream, delimiter="\t"))


def rows(path):
    with path.open(encoding="utf-8", newline="") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        while True:
            previous = csv.field_size_limit()
            try:
                csv.field_size_limit(sys.maxsize)
                row = next(reader)
            except StopIteration:
                return
            finally:
                csv.field_size_limit(previous)
            if None in row or any(value is None for value in row.values()):
                raise ValueError("malformed CSV row")
            yield row


def identity_key(row):
    """Explicitly mirror the documented grouping keys, not lossy list labels."""
    if row["resolved_identifier"]:
        return "mapped", row["resolved_identifier"]
    if not row["preferred_term"].strip():
        return "blank", row["recipe_id"], row["component_field"], row["component_index"]
    return (
        "label",
        row["preferred_term"],
        row["resolution_source"],
        row["mim_mapping_status"],
        row["mim_ambiguity"],
    )


def compare_occurrences(baseline_path, candidate_path):
    old_fields = fields(baseline_path)
    if fields(candidate_path) != old_fields + list(VARIANT_FIELDS):
        raise ValueError("v2 header does not append exactly the declared context fields")
    baseline_groups, candidate_groups = Counter(), Counter()
    baseline_labels, candidate_labels = Counter(), Counter()
    group_labels = defaultdict(set)
    variant_rows = []
    compared = 0

    def base_rows():
        for row in rows(candidate_path):
            candidate_groups[identity_key(row)] += 1
            candidate_labels[row["preferred_term"]] += 1
            group_labels[identity_key(row)].add(row["preferred_term"])
            if row["change_action"]:
                if (
                    row["change_action"] not in {"ADD", "SET_CONCENTRATION", "REPLACE"}
                    or row["descriptor_role"] != "ingredient"
                ):
                    raise ValueError("negative/context-only descriptor entered positive inventory")
                variant_rows.append(row)
                continue
            if any(row[key] for key in VARIANT_FIELDS):
                raise ValueError("base row unexpectedly carries variant context")
            yield {key: row[key] for key in old_fields}

    for before, after in itertools.zip_longest(rows(baseline_path), base_rows()):
        if before is None or after is None:
            raise ValueError("base occurrence membership/count changed")
        if before != after:
            changed = sorted(key for key in old_fields if before[key] != after[key])
            coordinate = tuple(
                before[key] for key in ("recipe_id", "component_field", "component_index")
            )
            raise ValueError(
                "base occurrence differs at " + repr(coordinate) + ": " + ", ".join(changed)
            )
        baseline_groups[identity_key(before)] += 1
        baseline_labels[before["preferred_term"]] += 1
        compared += 1
    return {
        "base_rows": compared,
        "baseline_groups": baseline_groups,
        "candidate_groups": candidate_groups,
        "baseline_labels": baseline_labels,
        "candidate_labels": candidate_labels,
        "group_labels": group_labels,
        "variant_rows": variant_rows,
    }


def context_rows(ledger_path, state):
    """Retain unresolved negative mentions separately, including existing positive labels."""
    unresolved = []
    positive = {}
    actions = defaultdict(set)
    mentions = 0
    context_count = 0
    for row in rows(ledger_path):
        coordinate = tuple(row[key] for key in ("recipe_id", "component_field", "component_index"))
        actions[row["change_action"]].add(coordinate)
        mentions += 1
        if row["counts_as_presence"] == "true":
            key = row["recipe_id"], row["descriptor_path"]
            if key in positive:
                raise ValueError("duplicate positive ledger coordinate")
            positive[key] = {
                key: value for key, value in row.items() if key != "counts_as_presence"
            }
        elif row["counts_as_presence"] == "false":
            context_count += 1
            if not row["resolved_identifier"]:
                unresolved.append(
                    {
                        **row,
                        "label_in_positive_inventory": str(
                            row["preferred_term"] in state["candidate_labels"]
                        ).lower(),
                        "label_in_baseline_inventory": str(
                            row["preferred_term"] in state["baseline_labels"]
                        ).lower(),
                    }
                )
        else:
            raise ValueError("invalid presence flag")
    expected = {(row["recipe_id"], row["descriptor_path"]): row for row in state["variant_rows"]}
    if positive != expected or len(expected) != len(state["variant_rows"]):
        raise ValueError("positive occurrence/ledger rows differ")
    return unresolved, {
        "variant_change_mentions": mentions,
        "variant_change_events": sum(len(value) for value in actions.values()),
        "variant_positive_occurrences": len(positive),
        "variant_context_only_mentions": context_count,
        "variant_changes_by_action": {key: len(value) for key, value in sorted(actions.items())},
    }


def write_tsv(path, columns, records):
    with path.open("x", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(records)


def compare(baseline, baseline_pin, candidate, candidate_pin, output):
    old = pinned_bundle(baseline, baseline_pin)
    new = pinned_bundle(candidate, candidate_pin)
    if (
        old["contract"] != "culturemech-direct-ingredients-v1"
        or new["contract"] != "culturemech-direct-ingredients-v2"
    ):
        raise ValueError("expected v1 baseline and v2 candidate")
    if any(
        item["scope"] != "full_catalog_direct_ingredients" or item["git"]["dirty"]
        for item in (old, new)
    ):
        raise ValueError("expected clean full-catalog origins")
    verification = subprocess.run(
        [
            sys.executable,
            "scripts/ingredient_release_bundle.py",
            "verify",
            "--bundle-dir",
            str(candidate.resolve()),
            "--expected-manifest-sha256",
            candidate_pin,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    state = compare_occurrences(
        baseline / "ingredient_occurrences.tsv", candidate / "ingredient_occurrences.tsv"
    )
    if (
        state["base_rows"] != old["counts"]["occurrences"]
        or state["base_rows"] != new["counts"]["base_direct_occurrences"]
    ):
        raise ValueError("base count differs from manifest")
    for manifest, directory, groups in (
        (old, baseline, state["baseline_groups"]),
        (new, candidate, state["candidate_groups"]),
    ):
        listing = list(rows(directory / "ingredients_list.tsv"))
        if (
            len(listing) != len(groups)
            or len(groups) != manifest["counts"]["ingredient_groups"]
            or sum(int(row["occurrence_count"]) for row in listing) != sum(groups.values())
        ):
            raise ValueError("independent identity grouping disagrees with list accounting")
    unresolved, ledger_counts = context_rows(candidate / "variant_ingredient_changes.tsv", state)
    if any(new["counts"][key] != value for key, value in ledger_counts.items()):
        raise ValueError("independent ledger counts differ from manifest")
    deltas = []
    for key, count in sorted(state["candidate_groups"].items()):
        previous = state["baseline_groups"][key]
        if count != previous:
            deltas.append(
                {
                    "group_key_json": json.dumps(key, ensure_ascii=False),
                    "mapping_status": (
                        "MAPPED"
                        if key[0] == "mapped"
                        else (
                            "AMBIGUOUS"
                            if key[0] == "label" and key[2] == "ambiguous"
                            else "UNMAPPED"
                        )
                    ),
                    "resolved_identifier": key[1] if key[0] == "mapped" else "",
                    "source_labels_json": json.dumps(
                        sorted(state["group_labels"][key]), ensure_ascii=False
                    ),
                    "baseline_occurrences": previous,
                    "candidate_occurrences": count,
                    "added_occurrences": count - previous,
                    "new_group": str(not previous).lower(),
                }
            )
    new_labels = []
    for label in sorted(set(state["candidate_labels"]) - set(state["baseline_labels"])):
        selected = [row for row in state["variant_rows"] if row["preferred_term"] == label]
        new_labels.append(
            {
                "source_label": label,
                "occurrences": len(selected),
                "resolved_identifiers_json": json.dumps(
                    sorted(
                        {
                            row["resolved_identifier"]
                            for row in selected
                            if row["resolved_identifier"]
                        }
                    )
                ),
                "resolution_sources_json": json.dumps(
                    sorted({row["resolution_source"] for row in selected})
                ),
                "source_coordinates_json": json.dumps(
                    [
                        {
                            key: row[key]
                            for key in (
                                "recipe_id",
                                "source_path",
                                "descriptor_path",
                                "change_action",
                                "change_stage",
                            )
                        }
                        for row in selected
                    ],
                    ensure_ascii=False,
                ),
            }
        )
    output = output.resolve()
    for source in (
        baseline.resolve(),
        candidate.resolve(),
        (ROOT / "data/normalized_yaml").resolve(),
    ):
        if output.is_relative_to(source) or source.is_relative_to(output):
            raise ValueError("comparison output overlaps input")
    output.mkdir(parents=True, exist_ok=False)
    write_tsv(
        output / "identity_deltas.tsv",
        [
            "group_key_json",
            "mapping_status",
            "resolved_identifier",
            "source_labels_json",
            "baseline_occurrences",
            "candidate_occurrences",
            "added_occurrences",
            "new_group",
        ],
        deltas,
    )
    write_tsv(
        output / "new_positive_labels.tsv",
        [
            "source_label",
            "occurrences",
            "resolved_identifiers_json",
            "resolution_sources_json",
            "source_coordinates_json",
        ],
        new_labels,
    )
    write_tsv(
        output / "unresolved_context_only_mentions.tsv",
        fields(candidate / "variant_ingredient_changes.tsv")
        + ["label_in_positive_inventory", "label_in_baseline_inventory"],
        unresolved,
    )
    # Pin checks bracket the complete comparison, including output generation.
    if (
        pinned_bundle(baseline, baseline_pin) != old
        or pinned_bundle(candidate, candidate_pin) != new
    ):
        raise ValueError("input changed during comparison")
    summary = {
        "result": "PASS",
        "baseline_manifest_sha256": baseline_pin,
        "candidate_manifest_sha256": candidate_pin,
        "baseline_commit": old["git"]["commit"],
        "candidate_commit": new["git"]["commit"],
        "native_verification": json.loads(verification.stdout),
        "base_occurrences_all_original_columns_equal": state["base_rows"],
        "baseline_identity_groups": len(state["baseline_groups"]),
        "candidate_identity_groups": len(state["candidate_groups"]),
        "new_positive_identity_groups": len(
            set(state["candidate_groups"]) - set(state["baseline_groups"])
        ),
        "new_positive_source_labels": len(new_labels),
        "unresolved_context_only_mentions": len(unresolved),
        "unresolved_context_only_labels": len({row["preferred_term"] for row in unresolved}),
        "unresolved_context_labels_absent_from_positive_inventory": sorted(
            {
                row["preferred_term"]
                for row in unresolved
                if row["label_in_positive_inventory"] == "false"
            }
        ),
        "input_files_added": sorted(set(new["inputs"]) - set(old["inputs"])),
        "input_files_removed": sorted(set(old["inputs"]) - set(new["inputs"])),
        "input_files_changed": sorted(
            path
            for path in set(old["inputs"]) & set(new["inputs"])
            if old["inputs"][path] != new["inputs"][path]
        ),
        "mim_index_metadata_unchanged": old["mim_label_index"] == new["mim_label_index"],
        **ledger_counts,
        "reports": {path.name: fingerprint(path) for path in sorted(output.glob("*.tsv"))},
        "limitations": "Exact artifact/accounting comparison, not independent scientific certification, MIM intake adoption, physical ingredient presence in every condition or published SSSOM/KGM release.",
    }
    with (output / "summary.json").open("x", encoding="utf-8") as stream:
        json.dump(summary, stream, indent=2, ensure_ascii=False)
        stream.write("\n")
    return summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--baseline", required=True, type=Path)
    parser.add_argument("--expected-baseline-manifest-sha256", required=True)
    parser.add_argument("--candidate", required=True, type=Path)
    parser.add_argument("--expected-candidate-manifest-sha256", required=True)
    parser.add_argument("--output-directory", required=True, type=Path)
    args = parser.parse_args()
    summary = compare(
        args.baseline,
        args.expected_baseline_manifest_sha256,
        args.candidate,
        args.expected_candidate_manifest_sha256,
        args.output_directory,
    )
    print(
        json.dumps(
            {
                key: value
                for key, value in summary.items()
                if key not in {"native_verification", "reports", "input_files_changed"}
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
