#!/usr/bin/env python3
"""Run one explicit batch079 command with durable launch-error receipts.

Provenance date: 2026-11-15.
Context: CultureMech issue #752 (publish executed provenance helpers), supporting
record reviews #749, #750 and #751; successor to batch079_run_check.py.

Required inputs: run from this checkout's root with a simple positional label
and the explicit child command/arguments. The caller supplies the executable,
its input files and matching environment. The runner sets checkout-local
.venv/cache paths and the recorded batch079 Git base.
Outputs: timestamped .stdout, .stderr and .json receipts under
.temp/batch079-scientific-20261114. Receipts retain literal dotted labels,
argv, times, stream hashes, child exit and runner exit; launch errors retain
null child exit and runner exit 127 or 126. Console output is a bounded preview.

Replay limits: each invocation executes the child once, with separately
required authorization. It does not install dependencies, establish scientific
validity or make repeated source/check execution safe. Retain earlier runner
versions and failed receipts; a replay is a new event, not the historical run.
"""

from __future__ import annotations

import argparse
import errno
import hashlib
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / ".temp" / "batch079-scientific-20261114"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("label")
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    if not args.command or "/" in args.label or args.label in {".", ".."}:
        parser.error("Supply a simple label followed by one explicit command")
    if Path.cwd().resolve() != ROOT:
        parser.error("Run with the recovery checkout as explicit working directory")
    RUN.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    stem = RUN / f"{stamp}-{args.label}"
    stdout, stderr = Path(str(stem) + ".stdout"), Path(str(stem) + ".stderr")
    env = dict(os.environ)
    for name in ("PYTHONPATH", "VIRTUAL_ENV"):
        env.pop(name, None)
    env.update(
        UV_PROJECT_ENVIRONMENT=str(ROOT / ".venv"),
        UV_CACHE_DIR=str(RUN / "uv-cache"),
        UV_NO_SYNC="1",
        PATH=str(Path.home() / ".local" / "bin") + ":" + env.get("PATH", ""),
        TMPDIR=str(RUN / "tmp"),
        RECORD_REVIEW_BASE="dda27db28f1e5f4f05da6d92fbd2cc1bd6e8add3",
        GIT_OPTIONAL_LOCKS="0",
    )
    Path(env["TMPDIR"]).mkdir(exist_ok=True)
    receipt = {
        "label": args.label,
        "argv": args.command,
        "cwd": str(ROOT),
        "started_at": datetime.now(timezone.utc).isoformat(),
        "environment": {
            k: env[k]
            for k in (
                "UV_PROJECT_ENVIRONMENT",
                "UV_CACHE_DIR",
                "UV_NO_SYNC",
                "TMPDIR",
                "RECORD_REVIEW_BASE",
                "GIT_OPTIONAL_LOCKS",
            )
        },
        "stdout": str(stdout.relative_to(ROOT)),
        "stderr": str(stderr.relative_to(ROOT)),
    }
    with stdout.open("xb") as out, stderr.open("xb") as err:
        try:
            result = subprocess.run(args.command, cwd=ROOT, env=env, stdout=out, stderr=err)
        except OSError as error:
            child_exit = None
            runner_exit = 127 if error.errno == errno.ENOENT else 126
            receipt["launch_error"] = {
                "type": type(error).__name__,
                "errno": error.errno,
                "message": str(error),
            }
        else:
            child_exit = result.returncode
            runner_exit = result.returncode
    receipt.update(
        finished_at=datetime.now(timezone.utc).isoformat(),
        exit=child_exit,
        runner_exit=runner_exit,
        stdout_sha256=hashlib.sha256(stdout.read_bytes()).hexdigest(),
        stderr_sha256=hashlib.sha256(stderr.read_bytes()).hexdigest(),
    )
    path = Path(str(stem) + ".json")
    with path.open("x") as fh:
        json.dump(receipt, fh, indent=2)
        fh.write("\n")
    print(json.dumps({"receipt": str(path.relative_to(ROOT)), **receipt}), flush=True)
    print(stdout.read_text(errors="replace")[-8000:], end="", flush=True)
    print(stderr.read_text(errors="replace")[-4000:], end="", file=sys.stderr, flush=True)
    if "launch_error" in receipt:
        print("Command launch failed: " + receipt["launch_error"]["message"], file=sys.stderr)
    return runner_exit


if __name__ == "__main__":
    raise SystemExit(main())
