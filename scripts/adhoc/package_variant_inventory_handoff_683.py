#!/usr/bin/env python3
"""Package a verified CultureMech v2 candidate for MIM, 2026-11-16, #683/#687.

Inputs: clean-commit full-catalog bundle, external manifest pin, coverage audit
and original queue. Outputs: a new local directory with exact source archive,
bundle, coverage and intake instructions. No network, live installation or send.
"""

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def sha(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--bundle", type=Path, required=True)
    parser.add_argument("--expected-manifest-sha256", required=True)
    parser.add_argument("--coverage", type=Path, required=True)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    manifest_path = args.bundle / "manifest.json"
    if sha(manifest_path) != args.expected_manifest_sha256:
        raise ValueError("unexpected manifest bytes")
    manifest = json.loads(manifest_path.read_text())
    if manifest["git"]["dirty"] or manifest["scope"] != "full_catalog_direct_ingredients":
        raise ValueError("handoff requires a full-catalog candidate from a clean producer")
    result = subprocess.run(
        [
            sys.executable,
            "scripts/ingredient_release_bundle.py",
            "verify",
            "--bundle-dir",
            str(args.bundle.resolve()),
            "--expected-manifest-sha256",
            args.expected_manifest_sha256,
        ],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=True,
    )
    verification = json.loads(result.stdout)
    coverage = json.loads((args.coverage / "summary.json").read_text())
    if coverage["result"] != "PASS" or coverage["mode"] != "postapply":
        raise ValueError("postapply coverage audit required")
    if (
        sha(args.coverage / "coverage.tsv") != coverage["coverage_sha256"]
        or sha(args.queue) != coverage["queue_sha256"]
    ):
        raise ValueError("coverage or queue bytes differ from audit")
    if manifest["counts"]["variant_change_events"] != coverage["applied_assertions"]:
        raise ValueError("bundle events differ from reviewed coverage")
    destination = args.output_directory.resolve()
    destination.mkdir(parents=True, exist_ok=False)
    shutil.copytree(args.bundle, destination / "bundle")
    shutil.copytree(args.coverage, destination / "coverage")
    shutil.copyfile(args.queue, destination / "original-review-queue.tsv")
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
    if not source_archive.stat().st_size:
        raise ValueError("empty producer archive")
    receipt = {
        "status": "VERIFIED_SOURCE_CANDIDATE_PENDING_ADOPTION",
        "contract": manifest["contract"],
        "producer_commit": manifest["git"]["commit"],
        "manifest_sha256": args.expected_manifest_sha256,
        "source_archive_sha256": sha(source_archive),
        "coverage_summary_sha256": sha(destination / "coverage/summary.json"),
        "queue_sha256": sha(destination / "original-review-queue.tsv"),
        "counts": manifest["counts"],
        "dispositions": coverage["dispositions"],
        "verification": verification,
        "adoption": "Explicitly adopt v2 in a separate reviewed MIM intake. Preserve existing frozen campaign. This is not a published SSSOM or integrated KGM release.",
    }
    (destination / "handoff.json").write_text(json.dumps(receipt, indent=2) + "\n")
    (destination / "HANDOFF.md").write_text(
        "# CultureMech variant ingredient candidate for MIM\n\n"
        f"PR: https://github.com/CultureBotAI/CultureMech/pull/764\n\n"
        f"Producer commit: `{manifest['git']['commit']}`\n\n"
        f"Manifest SHA256: `{args.expected_manifest_sha256}`\n\n"
        "The bundle adds reviewed variant events while retaining all original base occurrences. "
        "Use `ingredients_list.tsv` for identities and `ingredient_occurrences.tsv` for positive inventory membership. "
        "`variant_ingredient_changes.tsv` retains REMOVE and old REPLACE descriptors only as context. "
        "Preserve variant, stage, source evidence, dose basis and action. A zero concentration target is a change event, not positive physical presence.\n\n"
        "Extract `producer-source.tar.gz` into this new candidate directory. The archive contains the pinned implementation, schema, MIM index and source YAML. "
        "Use its locked environment to verify before intake:\n\n"
        "```bash\ncd producer\nuv sync --frozen\n"
        "uv run --frozen python scripts/ingredient_release_bundle.py verify \\\n"
        "  --bundle-dir ../bundle \\\n"
        f"  --expected-manifest-sha256 {args.expected_manifest_sha256}\n```\n\n"
        "The original396-row queue and coverage ledger accompany the source. "
        "201 statements have structured events;104 are conditions,16 already represented,44 held for evidence and31 held for the model. "
        "Some structured statements retain partial holds in their reason. See #683, #759, #760 and #762. "
        "No claim of complete prose coverage or complete executable variant formulations is made.\n\n"
        "Adopt this new v2 snapshot explicitly in a separate reviewed intake. Do not overwrite the running MIM campaign's frozen v1 inputs. "
        "Publication review, SSSOM generation/export and KGM QC remain downstream release gates.\n"
    )
    print(
        json.dumps(
            {
                "directory": str(destination),
                "handoff_sha256": sha(destination / "handoff.json"),
                "source_archive_sha256": receipt["source_archive_sha256"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
