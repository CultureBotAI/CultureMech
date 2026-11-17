#!/usr/bin/env python3
"""Package a verified CultureMech v3 candidate for MIM, 2026-11-16, #683/#687.

Inputs: clean-commit full-catalog bundle, external manifest pin, coverage audit
and original queue. Outputs: a new local directory with exact source archive,
bundle, coverage and intake instructions. No network, live installation or send.
"""

import argparse
import csv
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tarfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PRODUCTS = {
    "ingredient_occurrences.tsv",
    "ingredients_list.tsv",
    "mapped_ingredients.yaml",
    "unmapped_ingredients.yaml",
    "ingredient_aggregation_errors.tsv",
    "variant_ingredient_changes.tsv",
    "variant_ingredient_holds.tsv",
}


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def regular(path):
    if path.is_symlink() or not path.is_file():
        raise ValueError("input must be a regular non-symlink file: " + str(path))
    return path


def verify_bundle(bundle, pin):
    result = subprocess.run(
        [
            sys.executable,
            "scripts/ingredient_release_bundle.py",
            "verify",
            "--bundle-dir",
            str(bundle.resolve()),
            "--expected-manifest-sha256",
            pin,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout)


def validate_coverage(coverage, queue_bytes, manifest):
    """Join the audit to exact queue membership and candidate recipe bytes (#771)."""
    if coverage["result"] != "PASS" or coverage["mode"] != "postapply":
        raise ValueError("postapply coverage audit required")
    if hashlib.sha256(queue_bytes).hexdigest() != coverage["queue_sha256"]:
        raise ValueError("queue bytes differ from audit")
    previous_limit = csv.field_size_limit()
    try:
        csv.field_size_limit(sys.maxsize)
        rows = list(csv.DictReader(io.StringIO(queue_bytes.decode("utf-8")), delimiter="\t"))
    finally:
        csv.field_size_limit(previous_limit)
    expected = {}
    for row in rows:
        path = Path(row["source_path"])
        if path.is_absolute() or ".." in path.parts or path.as_posix() != row["source_path"]:
            raise ValueError("unsafe queue source path")
        key = "data/normalized_yaml/" + path.as_posix()
        if key in expected and expected[key] != row["source_sha256"]:
            raise ValueError("inconsistent queue source hash")
        expected[key] = row["source_sha256"]
    snapshots = coverage["record_snapshots"]
    if len({item["path"] for item in snapshots}) != len(snapshots) or {
        item["path"] for item in snapshots
    } != set(expected):
        raise ValueError("coverage recipe membership differs from queue")
    if coverage["queue_rows"] != len(rows) or coverage["queue_recipes"] != len(expected):
        raise ValueError("coverage queue counts differ")
    for item in snapshots:
        relative = item["path"].removeprefix("data/normalized_yaml/")
        if (
            item["base_sha256"] != expected[item["path"]]
            or relative not in manifest["inputs"]
            or item["current_sha256"] != manifest["inputs"][relative]["sha256"]
        ):
            raise ValueError("coverage recipe hashes differ from candidate")
    counts = coverage["dispositions"]
    if any(type(value) is not int or value < 0 for value in counts.values()) or sum(
        counts.values()
    ) != len(rows):
        raise ValueError("coverage disposition counts differ from queue")
    if manifest["counts"]["variant_change_events"] != coverage["applied_assertions"]:
        raise ValueError("bundle events differ from reviewed coverage")
    if manifest["counts"]["variant_held_mentions"] != coverage["held_mentions"]:
        raise ValueError("bundle held mentions differ from reviewed coverage")


def verify_archive(path, manifest):
    """Check archived bytes and discovered source membership without extracting."""
    expected = dict(manifest["dependencies"])
    expected.update(
        {"data/normalized_yaml/" + key: value for key, value in manifest["inputs"].items()}
    )
    with tarfile.open(path, "r:gz") as archive:
        members = archive.getmembers()
        names = [member.name for member in members]
        if len(names) != len(set(names)):
            raise ValueError("duplicate archive member")
        by_name = {member.name: member for member in members}
        archived_inputs = {
            name.removeprefix("producer/data/normalized_yaml/")
            for name in names
            if name.startswith("producer/data/normalized_yaml/") and name.endswith(".yaml")
        }
        if archived_inputs != set(manifest["inputs"]):
            raise ValueError("archived corpus membership differs from candidate")
        discovered_dependencies = {
            name.removeprefix("producer/")
            for name in names
            if name.startswith("producer/src/culturemech/")
            and (
                name.endswith(".py")
                or (name.startswith("producer/src/culturemech/schema/") and name.endswith(".yaml"))
            )
        }
        if not discovered_dependencies <= set(manifest["dependencies"]):
            raise ValueError("unexpected archived source dependency")
        for relative, fingerprint in expected.items():
            member = by_name.get("producer/" + relative)
            if member is None or not member.isfile():
                raise ValueError("missing/nonregular archived source: " + relative)
            stream = archive.extractfile(member)
            digest = hashlib.sha256()
            size = 0
            with stream:
                while chunk := stream.read(1024 * 1024):
                    digest.update(chunk)
                    size += len(chunk)
            if digest.hexdigest() != fingerprint["sha256"] or size != fingerprint["bytes"]:
                raise ValueError("archived source differs from candidate: " + relative)


def package(bundle, pin, coverage_dir, queue, destination):
    """Publish a new handoff only after delivered artifacts are verified (#769–771)."""
    for directory in (bundle, coverage_dir):
        if directory.is_symlink() or not directory.is_dir():
            raise ValueError("input must be a non-symlink directory")
    if destination.is_symlink() or destination.exists():
        raise ValueError("handoff destination already exists")
    destination = destination.resolve()
    for source in (
        bundle.resolve(),
        coverage_dir.resolve(),
        queue.resolve(),
        (ROOT / "data/normalized_yaml").resolve(),
    ):
        if destination.is_relative_to(source) or source.is_relative_to(destination):
            raise ValueError("handoff destination overlaps an input")
    manifest_path = regular(bundle / "manifest.json")
    manifest_bytes = manifest_path.read_bytes()
    if hashlib.sha256(manifest_bytes).hexdigest() != pin:
        raise ValueError("unexpected manifest bytes")
    manifest = json.loads(manifest_bytes)
    if (
        manifest["git"]["dirty"]
        or manifest["scope"] != "full_catalog_direct_ingredients"
        or manifest["input_dir"] != "data/normalized_yaml"
        or manifest["contract"] != "culturemech-direct-ingredients-v3"
        or set(manifest["products"]) != PRODUCTS
    ):
        raise ValueError("handoff requires a clean full-catalog v3 producer")
    verification = verify_bundle(bundle, pin)
    coverage_path = regular(coverage_dir / "summary.json")
    coverage_bytes = coverage_path.read_bytes()
    coverage = json.loads(coverage_bytes)
    queue_bytes = regular(queue).read_bytes()
    validate_coverage(coverage, queue_bytes, manifest)
    if sha(regular(coverage_dir / "coverage.tsv")) != coverage["coverage_sha256"]:
        raise ValueError("coverage bytes differ from audit")
    # Copy only the contractual products, never incidental files or directory trees.
    sources = {Path("bundle/manifest.json"): (manifest_path, pin)}
    sources.update(
        {
            Path("bundle") / name: (regular(bundle / name), manifest["products"][name]["sha256"])
            for name in sorted(PRODUCTS)
        }
    )
    sources.update(
        {
            Path("coverage/summary.json"): (
                coverage_path,
                hashlib.sha256(coverage_bytes).hexdigest(),
            ),
            Path("coverage/coverage.tsv"): (
                coverage_dir / "coverage.tsv",
                coverage["coverage_sha256"],
            ),
            Path("original-review-queue.tsv"): (queue, coverage["queue_sha256"]),
        }
    )
    destination.mkdir(parents=True, exist_ok=False)
    for relative, (source, expected) in sources.items():
        copied = destination / relative
        copied.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, copied)
        if sha(copied) != expected:
            raise ValueError("delivered copy differs from verified input: " + str(relative))
    source_archive = destination / "producer-source.tar.gz"
    subprocess.run(
        [
            "git",
            "archive",
            "--format=tar.gz",
            "--prefix=producer/",
            "--output",
            str(source_archive),
            manifest["git"]["commit"],
        ],
        cwd=ROOT,
        check=True,
    )
    verify_archive(source_archive, manifest)
    verification = verify_bundle(destination / "bundle", pin)
    for relative, (source, expected) in sources.items():
        if sha(regular(source)) != expected or sha(regular(destination / relative)) != expected:
            raise ValueError("input or delivered copy changed during packaging")
    receipt = {
        "status": "VERIFIED_SOURCE_CANDIDATE_PENDING_ADOPTION",
        "contract": manifest["contract"],
        "producer_commit": manifest["git"]["commit"],
        "manifest_sha256": pin,
        "source_archive_sha256": sha(source_archive),
        "coverage_summary_sha256": sha(destination / "coverage/summary.json"),
        "queue_sha256": sha(destination / "original-review-queue.tsv"),
        "counts": manifest["counts"],
        "dispositions": coverage["dispositions"],
        "verification": verification,
        "adoption": "Explicitly adopt v3 in a separate reviewed MIM intake. Preserve existing frozen campaign. This is not a published SSSOM or integrated KGM release.",
    }
    (destination / "HANDOFF.md").write_text(
        "# CultureMech variant ingredient candidate for MIM\n\n"
        "Issue: https://github.com/CultureBotAI/CultureMech/issues/683\n\n"
        f"Producer commit: `{manifest['git']['commit']}`\n\n"
        f"Manifest SHA256: `{pin}`\n\n"
        "The bundle contains base occurrences and reviewed variant events. "
        "Use `ingredients_list.tsv` for identities and `ingredient_occurrences.tsv` for positive inventory membership. "
        "`variant_ingredient_changes.tsv` retains REMOVE and old REPLACE descriptors only as context. "
        "`variant_ingredient_holds.tsv` retains unresolved source labels and the precise held assertion fields; these rows never count as positive inventory occurrences. "
        "Preserve variant, stage, source evidence, dose basis and action. A zero concentration target is a change event, not positive physical presence.\n\n"
        "Extract `producer-source.tar.gz` into this new candidate directory. The archive contains the pinned implementation, schema, MIM index and source YAML. "
        "Use its locked environment to verify before intake:\n\n"
        "```bash\ncd producer\nuv sync --frozen\n"
        "uv run --frozen python scripts/ingredient_release_bundle.py verify \\\n"
        "  --bundle-dir ../bundle \\\n"
        f"  --expected-manifest-sha256 {pin}\n```\n\n"
        f"The original {coverage['queue_rows']}-row queue and coverage ledger accompany the source. "
        + "; ".join(f"{value} {key}" for key, value in sorted(coverage["dispositions"].items()))
        + ". "
        "Some structured statements retain partial holds in their reason. See #683, #759, #760 and #762. "
        "No claim of complete prose coverage or complete executable variant formulations is made.\n\n"
        "Adopt this new v3 snapshot explicitly in a separate reviewed intake. Do not overwrite the running MIM campaign's frozen inputs. "
        "Publication review, SSSOM generation/export and KGM QC remain downstream release gates.\n"
    )
    # Acceptance is last. Any earlier failure leaves incomplete evidence only.
    receipt_path = destination / "handoff.json"
    staged_receipt = destination / ".handoff.incomplete.json"
    with staged_receipt.open("x", encoding="utf-8") as stream:
        stream.write(json.dumps(receipt, indent=2) + "\n")
        stream.flush()
        os.fsync(stream.fileno())
    os.replace(staged_receipt, receipt_path)
    return receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--expected-manifest-sha256", required=True)
    parser.add_argument("--coverage", type=Path, required=True)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    receipt = package(
        args.bundle, args.expected_manifest_sha256, args.coverage, args.queue, args.output_directory
    )
    print(
        json.dumps(
            {
                "directory": str(args.output_directory.resolve()),
                "handoff_sha256": sha(args.output_directory / "handoff.json"),
                "source_archive_sha256": receipt["source_archive_sha256"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
