"""Verify retained recovery receipts and write a bounded batch079 checkpoint.

Provenance date: 2026-11-15.
Context: CultureMech #752 (complete provenance publication), scientific follow-up
#749/#750/#751, and technical recovery #753/#754. This checkpoint does not repair
scientific records or establish export/admission readiness.

Required inputs: explicit checkout-root working directory, Python/PyYAML and
--history-manifest-sha256 plus --final-fast-receipt-sha256. The first must match
scripts/batch079_provenance/manifest.json and every archived version; the second
must match the retained 20261115T084010973746Z-provenance-test-fast-corrected.json
under .temp/batch079-scientific-20261114, including its argv, times and streams.
Header-time reviewed digests are, respectively:
4fa39b1ef05468752fea17bd4fdaafb2d0c20d4acd4376b0217394beda88489e
ac88fd7469f1e8b48572dd2813c62f3cb55566a1237c5306544922a0cfe22fd8
Further required local inputs are the named original native/check/test/recovery
receipts and streams, three immutable review pairs, helper-pre-format manifest,
current helpers, provenance archives and historical Git objects. Optional --pr
records a PR value; --runtime-only suppresses the public checkpoint write.
Repeatable --followup-receipt binds successful issue756 checks and their exact streams.
Outputs: timestamped runtime checkpoint JSON and CURRENT.md under the ignored
run directory; by default reviews/batch079-recovery-20261115.json, preserving
any previous public checkpoint in an exclusive ignored archive. Git commands
read archived bytes, HEAD and branch; no tests, validators or publication run.

Replay limits: guards require actual retained evidence, not a copied success
claim. Repeated authorized runs create new runtime snapshots and may replace
the public checkpoint; they do not rerun tests or rewrite immutable reviews.
The final fast outcome is parsed from its bound receipt, while failed earlier
attempts remain separate. Header-only changes after that run are not represented
as a second full-suite execution. No push, PR creation or merge is performed.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RUN = Path(".temp/batch079-scientific-20261114")
BASE = "dda27db28f1e5f4f05da6d92fbd2cc1bd6e8add3"
ARCHIVE_COMMIT = "71d94151e0090b8f99cb828cb94e36ee53ed0156"
REVIEW_IDS = [
    "20261115T080257Z-batch079-record07-desulfothermus",
    "20261115T081711Z-batch079-record08-desulfotignum",
    "20261115T082226Z-batch079-record10-desulfotomaculum",
]


def pin(path: Path) -> dict:
    data = (ROOT / path).read_bytes()
    return {"path": str(path), "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--runtime-only", action="store_true")
    parser.add_argument("--pr", default="pending")
    parser.add_argument("--history-manifest-sha256", required=True)
    parser.add_argument("--final-fast-receipt-sha256", required=True)
    parser.add_argument("--followup-receipt", type=Path, action="append", default=[])
    args = parser.parse_args()
    assert Path.cwd().resolve() == ROOT
    now = datetime.now(timezone.utc)
    history_manifest = Path("scripts/batch079_provenance/manifest.json")
    assert pin(history_manifest)["sha256"] == args.history_manifest_sha256
    history_record = json.loads((ROOT / history_manifest).read_text())
    assert history_record["versions"], "Historical source archive must be nonempty"
    for version in history_record["versions"]:
        assert pin(Path(version["archive_path"]))["sha256"] == version["sha256"]
    native_names = {
        "07": [
            "20261115T075705104393Z-record07-schema.json",
            "20261115T075705924125Z-record07-strict.json",
            "20261115T075713230348Z-record07-terms.json",
            "20261115T075714381035Z-record07-references.json",
        ],
        "08": [
            "20261115T081420069829Z-record08-schema.json",
            "20261115T081420547292Z-record08-strict.json",
            "20261115T081418248294Z-record08-terms.json",
            "20261115T081419407643Z-record08-references.json",
        ],
        "10": [
            "20261115T081824139492Z-record10-schema.json",
            "20261115T081824635873Z-record10-strict.json",
            "20261115T081825506772Z-record10-terms.json",
            "20261115T081825245374Z-record10-references.json",
        ],
    }
    targets = {
        "07": "DESULFOTHERMUS_NAPHTHAE_MEDIUM",
        "08": "DESULFOTIGNUM_MEDIUM",
        "10": "DESULFOTOMACULUM_PBE_MEDIUM",
    }
    native_pins = []
    for number, names in native_names.items():
        for check, name in zip(["schema", "strict", "terms", "references"], names, strict=True):
            path = RUN / name
            receipt = json.loads((ROOT / path).read_text())
            assert receipt["exit"] == 0
            target = "data/merge_yaml/merged/" + targets[number] + ".yaml"
            expected_argv = ["just", "validate-" + check, target]
            if check == "strict":
                expected_argv += [
                    "--out",
                    str(RUN / ("record" + number) / "strict.tsv"),
                    "--workers",
                    "1",
                    "--quiet",
                ]
            assert receipt["argv"] == expected_argv
            for stream in ("stdout", "stderr"):
                assert pin(Path(receipt[stream]))["sha256"] == receipt[stream + "_sha256"]
            if check == "references":
                assert "Reference checks: 0; issues: 0" in (ROOT / receipt["stdout"]).read_text()
            native_pins.append({**pin(path), "record": number, "check": check, "exit": 0})
    persisted_path = RUN / "20261115T082358847745Z-record10-persisted-check.json"
    contract_path = RUN / "20261115T082457743515Z-final-review-contract.json"
    for path, argv, expected in [
        (persisted_path, ["just", "check-record-reviews"], "45"),
        (contract_path, ["just", "test-record-reviews"], "4 passed"),
    ]:
        receipt = json.loads((ROOT / path).read_text())
        assert receipt["exit"] == 0 and receipt["argv"] == argv
        for stream in ("stdout", "stderr"):
            assert pin(Path(receipt[stream]))["sha256"] == receipt[stream + "_sha256"]
        result_text = (ROOT / receipt["stdout"]).read_text()
        if path == persisted_path:
            assert json.loads(result_text)["valid_reviews"] == 45
        else:
            assert expected in result_text
    broader_test_receipts = []
    for name, expected_exit, expected_summary in [
        (
            "20261115T082713515827Z-provenance-test-fast.json",
            2,
            "1 failed, 4130 passed, 7 skipped, 3599 deselected",
        ),
        ("20261115T082935806192Z-provenance-isolated-fixture-test.json", 0, "1 passed in 0.06s"),
    ]:
        path = RUN / name
        receipt = json.loads((ROOT / path).read_text())
        assert receipt["exit"] == expected_exit
        for stream in ("stdout", "stderr"):
            assert pin(Path(receipt[stream]))["sha256"] == receipt[stream + "_sha256"]
        assert expected_summary in (ROOT / receipt["stdout"]).read_text()
        broader_test_receipts.append(
            {
                **pin(path),
                "exit": receipt["exit"],
                "streams": [pin(Path(receipt["stdout"])), pin(Path(receipt["stderr"]))],
            }
        )
    completed_fast_path = RUN / "20261115T083248743353Z-provenance-test-fast-outside-git.json"
    completed_fast = json.loads((ROOT / completed_fast_path).read_text())
    expected_fast_argv = [
        "/usr/bin/env",
        "PYTEST_ADDOPTS=--basetemp=" + str(ROOT.parent / "batch079-fast-fixtures-20261115T084000Z"),
        "just",
        "test-fast",
    ]
    assert completed_fast["argv"] == expected_fast_argv
    assert completed_fast["exit"] == 1 and completed_fast["runner_exit"] == 1
    for stream in ("stdout", "stderr"):
        assert pin(Path(completed_fast[stream]))["sha256"] == completed_fast[stream + "_sha256"]
    completed_fast_summary = (
        "1 failed, 15960 passed, 23 skipped, 3599 deselected, 2 warnings, " "150 errors in 303.37s"
    )
    assert completed_fast_summary in (ROOT / completed_fast["stdout"]).read_text()
    completed_fast_result = {
        **pin(completed_fast_path),
        "exit": completed_fast["exit"],
        "runner_exit": completed_fast["runner_exit"],
        "status": "completed with one failure and 150 setup errors; not a pass",
        "summary": completed_fast_summary,
        "counts": {
            "passed": 15960,
            "failed": 1,
            "errors": 150,
            "skipped": 23,
            "deselected": 3599,
            "warnings": 2,
        },
        "streams": [pin(Path(completed_fast["stdout"])), pin(Path(completed_fast["stderr"]))],
        "recipe": pin(Path("project.justfile")),
    }
    recovery_results = []
    for name, expected_sha, expected_argv, expected_summary in [
        (
            "20261115T083857560744Z-test-fixture-history-fetch.json",
            "2f71b5c9ce231ad582a5a035be96130c00463394c7908eae4307fa031bfb437d",
            [
                "git",
                "fetch",
                "--no-tags",
                "--no-write-fetch-head",
                "origin",
                "f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f",
            ],
            None,
        ),
        (
            "20261115T083942839556Z-provenance-focused-after-portability-history-fix.json",
            "62113e509b30b258a2ea64fef6c4f8753c3108132939fd8853026286c5c1e222",
            [
                str(Path.home() / ".local/bin/uv"),
                "run",
                "--extra",
                "dev",
                "pytest",
                "tests/test_public_direct_concentrations.py",
                "tests/test_public_recipe_input_basis.py",
                "tests/test_public_stock_concentrations.py",
                "tests/test_rs_stock_boundaries.py",
                "tests/test_scripts_are_machine_independent.py",
                "-m",
                "fast",
                "--no-cov",
                "-q",
                "--basetemp=" + str(ROOT.parent / "batch079-focused-fixtures-20261115T084000Z"),
            ],
            "1182 passed in 17.89s",
        ),
    ]:
        path = RUN / name
        assert pin(path)["sha256"] == expected_sha
        receipt = json.loads((ROOT / path).read_text())
        assert receipt["argv"] == expected_argv
        assert receipt["exit"] == 0 and receipt["runner_exit"] == 0
        for stream in ("stdout", "stderr"):
            assert pin(Path(receipt[stream]))["sha256"] == receipt[stream + "_sha256"]
        if expected_summary is not None:
            assert expected_summary in (ROOT / receipt["stdout"]).read_text()
        recovery_results.append(
            {
                **pin(path),
                "exit": 0,
                "summary": expected_summary,
                "streams": [pin(Path(receipt["stdout"])), pin(Path(receipt["stderr"]))],
            }
        )
    final_fast_path = RUN / "20261115T084010973746Z-provenance-test-fast-corrected.json"
    assert pin(final_fast_path)["sha256"] == args.final_fast_receipt_sha256
    final_fast = json.loads((ROOT / final_fast_path).read_text())
    assert final_fast["argv"] == [
        "/usr/bin/env",
        "PYTEST_ADDOPTS=--basetemp="
        + str(ROOT.parent / "batch079-corrected-fast-fixtures-20261115T084100Z"),
        "just",
        "test-fast",
    ]
    assert type(final_fast["exit"]) is int
    assert final_fast["runner_exit"] == final_fast["exit"]
    assert datetime.fromisoformat(final_fast["finished_at"]) >= datetime.fromisoformat(
        final_fast["started_at"]
    )
    for stream in ("stdout", "stderr"):
        assert pin(Path(final_fast[stream]))["sha256"] == final_fast[stream + "_sha256"]
    final_fast_stdout = (ROOT / final_fast["stdout"]).read_text()
    count_pattern = r"(\d+) (failed|passed|skipped|deselected|warnings?|errors?|xfailed|xpassed)"
    summary_pattern = (
        r"(?:" + count_pattern + r")(?:, " + count_pattern + r")*"
        r" in \d+(?:\.\d+)?s(?: \([^)]*\))?"
    )
    final_summaries = [
        line.strip("= \t")
        for line in final_fast_stdout.splitlines()
        if re.fullmatch(summary_pattern, line.strip("= \t"))
    ]
    assert len(final_summaries) == 1, "Expected one actual final pytest summary"
    final_summary = final_summaries[0]
    final_counts = {
        {"warning": "warnings", "error": "errors"}.get(label, label): int(value)
        for value, label in re.findall(count_pattern, final_summary)
    }
    final_interrupted = "KeyboardInterrupt" in final_fast_stdout
    if final_fast["exit"] == 0:
        assert not final_interrupted
        assert final_counts.get("failed", 0) == 0 and final_counts.get("errors", 0) == 0
    final_fast_result = {
        **pin(final_fast_path),
        "exit": final_fast["exit"],
        "runner_exit": final_fast["runner_exit"],
        "status": (
            "passed"
            if final_fast["exit"] == 0
            else (
                "interrupted; not a pass"
                if final_interrupted
                else "completed with a nonzero exit; not a pass"
            )
        ),
        "summary": final_summary,
        "counts": final_counts,
        "streams": [pin(Path(final_fast["stdout"])), pin(Path(final_fast["stderr"]))],
        "recipe": pin(Path("project.justfile")),
    }
    reviews = []
    for review_id in REVIEW_IDS:
        folder = Path("reviews/structured") / review_id
        record = yaml.safe_load((ROOT / folder / "review.yaml").read_text())
        assert record["completion"] == "completed" and record["verdict"] == "needs_curation"
        reviews.append(
            {
                "record": review_id.split("-record")[1].split("-")[0],
                "review_id": review_id,
                "target": record["targets"][0]["target_id"],
                "verdict": record["verdict"],
                "completion": record["completion"],
                "findings": dict(Counter(x["severity"] for x in record["findings"])),
                "bundle": [pin(folder / "review.yaml"), pin(folder / "review.md")],
            }
        )
    receipts = []
    for path in sorted((ROOT / RUN).glob("*.json")):
        obj = json.loads(path.read_text())
        if not isinstance(obj, dict) or not {"argv", "exit", "stdout", "stderr"} <= obj.keys():
            continue
        for stream in ("stdout", "stderr"):
            assert pin(Path(obj[stream]))["sha256"] == obj[stream + "_sha256"], path
        receipts.append(
            {
                **pin(path.relative_to(ROOT)),
                **{k: obj[k] for k in ("label", "argv", "exit", "started_at", "finished_at")},
                "streams": [pin(Path(obj["stdout"])), pin(Path(obj["stderr"]))],
            }
        )
    helpers = []
    followup_pins = []
    for path in args.followup_receipt:
        receipt = json.loads((ROOT / path).read_text())
        assert receipt["label"].startswith("issue756-")
        assert receipt["exit"] == receipt["runner_exit"] == 0
        for stream in ("stdout", "stderr"):
            assert pin(Path(receipt[stream]))["sha256"] == receipt[stream + "_sha256"]
        followup_pins.append(
            {
                **pin(path),
                "label": receipt["label"],
                "exit": receipt["exit"],
                "started_at": receipt["started_at"],
                "finished_at": receipt["finished_at"],
                "streams": [pin(Path(receipt["stdout"])), pin(Path(receipt["stderr"]))],
            }
        )

    original = json.loads((ROOT / RUN / "helper-pre-format-manifest.json").read_text())
    before = {item["path"]: item for item in original}
    assert len(before) == 8
    for name, item in before.items():
        archived_bytes = subprocess.check_output(
            ["git", "show", ARCHIVE_COMMIT + ":" + name], cwd=ROOT
        )
        assert hashlib.sha256(archived_bytes).hexdigest() == item["sha256"]
    for path in sorted((ROOT / "scripts").glob("batch079*.py")):
        relative = path.relative_to(ROOT)
        row = pin(relative)
        if str(relative) in before:
            row["retained_pre_format_sha256"] = before[str(relative)]["sha256"]
            row["retained_pre_format_git_commit"] = ARCHIVE_COMMIT
            row["byte_relation"] = (
                "Historical retained bytes are in the archive commit; current formatting/lint edits, the record10 required-input CLI repair and issue756 review-draft width successors do not restamp immutable review inputs."
            )
        helpers.append(row)
    history = [
        pin(p.relative_to(ROOT))
        for p in sorted((ROOT / "scripts/batch079_provenance").rglob("*.txt"))
    ]
    snapshot = {
        "updated_at": now.isoformat().replace("+00:00", "Z"),
        "scope": "Bounded scientific assessment of recovered batch079 records07,08,10; no full-batch completion or source repair is claimed.",
        "baseline": BASE,
        "original_retained_helper_commit": ARCHIVE_COMMIT,
        "reviews": reviews,
        "helpers": helpers,
        "historical_source_archives": history,
        "history_manifest": pin(history_manifest),
        "verified_native_checks": native_pins,
        "persisted_review_check": pin(persisted_path),
        "review_contract_test": pin(contract_path),
        "publication_plan_reconciliation": "The owner explicitly superseded the earlier bundle-only plan. All available executed provenance helper versions, retained superseded drafts, exact historical source archives, and this checkpoint accompany the three immutable pairs. Earlier saved review notes and script strings describe their draft-time plan and remain historical attestations; they are not current publication policy. See issue752 and scripts/batch079_provenance/README.md.",
        "environment": {
            "python": "3.13.2",
            "environment": ".venv",
            "lock_sha256": pin(Path("uv.lock"))["sha256"],
            "sync_receipt": str(RUN / "environment-sync.json"),
            "origins_receipt": str(RUN / "20261115T075601984823Z-environment-origins.json"),
        },
        "technical_scope": "All three selected generated records passed schema, one-file schema-layer strict, configured terms and reference validators. Each reference check inspected ZERO evidence assertions. These exits do not establish scientific truth.",
        "broader_test_scope": {
            "status": "final required full fast run: " + final_fast_result["status"],
            "summary": "All attempts remain separate. The first broad run was interrupted inside a Git-backed fixture directory; one isolated outside-Git fixture check then passed. The first completed outside-Git full run exited 1 with 15960 passed, one failure and 150 setup errors. Those setup errors could not read baseline commit f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f, which was absent in that tested shallow checkout. Its one assertion failure identified the record10 builder's machine-specific path. The exact missing commit was subsequently fetched without updating FETCH_HEAD or tags, and the builder now requires --original-native-dir. The five affected test modules then passed all 1182 cases. The owner subsequently required a complete corrected just test-fast run; its actual exit, final summary and counts are bound separately below. The documented -m fast --no-cov recipe was retained. Earlier failures are not relabeled as passes, and technical test outcomes do not resolve the scientific findings. See issues753/754.",
            "initial_attempts": broader_test_receipts,
            "first_completed_run": completed_fast_result,
            "recovery_operations": recovery_results,
            "final_required_full_run": final_fast_result,
        },
        "remaining_scientific_source_export_blockers": [
            "Record07: stock nesting/doses, stale generated content, nickel hydrate and sodium-resazurin identity, preparation/source equivalence and narrow evidence; exact KOMODO source unavailable.",
            "Record08: DSM383/383a output collapse, intermediate/stock placement, nickel and sodium-resazurin grounding, SL-10 scope, qualified variant rationale and unestablished high_metal total.",
            "Record10: generated volume units/preparation, unsupported owner percentage basis, nominal-batch denominator and source-specific evidence limits; direct TOGO timed out, peptone specificity unconfirmed.",
            "Authoritative repairs and regenerated exports remain follow-up in749/750/751. No catalog, KG-Microbe admission or export release readiness is asserted.",
        ],
        "issues": [
            "https://github.com/CultureBotAI/CultureMech/issues/" + str(n)
            for n in (749, 750, 751, 752, 753, 754, 756)
        ],
        "pr692": "Separate draft at last independently verified02e005db42246b8a04ece9df4b5657e036fa5697, includes684 and had9greenchecks. Its scientific/source/export gates remain separate; this task did not mutate it.",
        "preservation": "Existing reviews and historical01–06/09 artifacts remain unchanged;26historical pins were independently rehashed. Original failures, shallow-clone diagnostics, unsupported list flag and record10 source timeout remain retained. No merge, force push, cleanup, paid research or historical batch publication.",
        "reproducibility": "A fresh checkout can inspect published code, exact historical source text, scientific reviews and input hashes. Reproducing authoring needs the retained ignored raw captures, peer artifacts, original receipt streams and matching environment. No helper rerun constitutes a fresh scientific review.",
        "documents_access": "The historical macOS Documents EPERM was separate from completed SSH technical checks. The explicit agent-work recovery checkout is usable; Documents was not retried or permissions changed.",
    }
    if followup_pins:
        snapshot["post_ci_review_width_repair"] = {
            "issue": "https://github.com/CultureBotAI/CultureMech/issues/756",
            "failed_candidate": "61d501fd9eff12a387a2e013a7f983801d9a9809",
            "failed_ci_job": "https://github.com/CultureBotAI/CultureMech/actions/runs/43696509390/job/132758127461",
            "change": "Removed only explicit YAML width keywords from three draft review builders; no corpus guard or scientific source changed.",
            "checks": followup_pins,
            "scope": "Focused width-equivalence, record-IO, review-contract, portability, native saved-review and static checks; see exact receipt streams.",
            "full_suite_after_repair": "Not repeated locally; new-head CI remains required.",
        }

    if not args.runtime_only:
        public_path = ROOT / "reviews/batch079-recovery-20261115.json"
        if public_path.exists():
            archive = (
                ROOT
                / RUN
                / ("public-checkpoint-before-" + now.strftime("%Y%m%dT%H%M%S%fZ") + ".json")
            )
            with archive.open("xb") as handle:
                handle.write(public_path.read_bytes())
        public_path.write_text(json.dumps(snapshot, indent=2) + "\n")
    runtime = {
        **snapshot,
        "workdir": str(ROOT),
        "pr": args.pr,
        "head": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "branch": subprocess.check_output(
            ["git", "branch", "--show-current"], cwd=ROOT, text=True
        ).strip(),
        "commands_and_streams": receipts,
    }
    destination = ROOT / RUN / ("checkpoint-" + now.strftime("%Y%m%dT%H%M%S%fZ") + ".json")
    with destination.open("x") as handle:
        handle.write(json.dumps(runtime, indent=2) + "\n")
    (ROOT / RUN / "CURRENT.md").write_text(
        f"Current bounded recovery checkpoint: {destination.relative_to(ROOT)}\nPR: {args.pr}\nAll3 assessments completed needs_curation; source repairs/export gates remain follow-up.\n"
    )
    print(
        json.dumps(
            {
                "checkpoint": str(destination.relative_to(ROOT)),
                "sha256": pin(destination.relative_to(ROOT))["sha256"],
                "receipts": len(receipts),
            }
        )
    )


if __name__ == "__main__":
    main()
