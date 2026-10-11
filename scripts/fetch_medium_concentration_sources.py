#!/usr/bin/env python3
"""Freeze unreviewed exact medium targets and cache official, hash-pinned sources."""

import argparse
import datetime
import json
import re
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

from fetch_solution_concentration_sources import load_yaml, select
from repair_mediadive_stock_concentration_evidence import require, sha

ROOT = Path(__file__).resolve().parents[1]
API = "https://mediadive.dsmz.de/rest/medium/"


def identifier(value):
    value = str(value)
    require(re.fullmatch(r"[A-Za-z]*\d+[A-Za-z]*", value), "Unsafe medium source identifier")
    return value


def inventory(root, coverage):
    previous = json.loads(coverage.read_text())
    tracked = set(
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root)
        .decode()
        .split("\0")
    )
    records = []
    for item in previous["pending_records"]:
        source = item["source_term"] or ""
        if not source.startswith("mediadive.medium:"):
            continue
        relative = item["path"]
        require(relative in tracked and not (root / relative).is_symlink(), "Non-exact target")
        raw = (root / relative).read_bytes()
        require(sha(raw) == item["sha256"], f"Coverage baseline drift: {relative}")
        doc = load_yaml(raw)
        require(
            doc["id"] == item["id"] and doc["media_term"]["term"]["id"] == source, "Identity drift"
        )
        records.append(
            {
                "path": relative,
                "id": doc["id"],
                "medium_id": identifier(source.split(":", 1)[1]),
                "name": doc["original_name"],
                "before_sha256": sha(raw),
            }
        )

    def order(item):
        prefix, number, suffix = re.fullmatch(
            r"([A-Za-z]*)(\d+)([A-Za-z]*)", item["medium_id"]
        ).groups()
        return prefix, int(number), suffix, item["path"]

    records.sort(key=order)
    require(len({r["path"] for r in records}) == len(records), "Duplicate target")
    return {
        "version": 1,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root).decode().strip(),
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "coverage_snapshot": str(coverage),
        "records": records,
    }


def check_payload(raw, mid):
    payload = json.loads(raw)
    require(payload["status"] == 200 and payload["count"] == 1, "Invalid source envelope")
    require(str(payload["data"]["medium"]["id"]) == identifier(mid), "Wrong source medium")
    require(isinstance(payload["data"]["solutions"], list), "Missing source solution inventory")


def read_capture(cache, mid):
    mid = identifier(mid)
    raw = (cache / f"{mid}.json").read_bytes()
    meta = json.loads((cache / f"{mid}.metadata.json").read_text())
    require(meta["url"] == API + mid == meta["response_url"], "Source URL mismatch")
    require(
        meta["http_status"] == 200 and sha(raw) == meta["sha256"], "Source hash/status mismatch"
    )
    datetime.datetime.fromisoformat(meta["accessed_at"])
    check_payload(raw, mid)
    return raw.decode(), meta


def fetch_one(cache, mid):
    mid = identifier(mid)
    url = API + mid
    request = urllib.request.Request(
        url, headers={"Accept": "application/json", "User-Agent": "CultureMech-evidence-review/1.0"}
    )
    with urllib.request.urlopen(request, timeout=45) as response:
        require(response.status == 200 and response.url == url, "Unexpected redirect/status")
        raw = response.read()
    check_payload(raw, mid)
    meta = {
        "url": url,
        "response_url": url,
        "http_status": 200,
        "sha256": sha(raw),
        "accessed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    (cache / f"{mid}.json").write_bytes(raw)
    (cache / f"{mid}.metadata.json").write_text(json.dumps(meta, indent=2) + "\n")


def fetch(records, cache, delay=0.25):
    require(delay >= 0.25, "Retain serial rate limiting")
    cache.mkdir(parents=True, exist_ok=True)
    stats = {"selected": len(records), "fetched": 0, "cached": 0, "failed": 0}
    failures, consecutive = [], 0
    for index, item in enumerate(records, 1):
        mid = item["medium_id"]
        try:
            if (cache / f"{identifier(mid)}.json").exists():
                read_capture(cache, mid)
                stats["cached"] += 1
            else:
                fetch_one(cache, mid)
                stats["fetched"] += 1
                time.sleep(delay)
            consecutive = 0
        except (OSError, ValueError, KeyError, TypeError) as exc:
            failures.append({"path": item["path"], "medium_id": mid, "error": str(exc)})
            stats["failed"] += 1
            consecutive += 1
            if (
                isinstance(exc, urllib.error.HTTPError) and exc.code in {429, 503}
            ) or consecutive >= 3:
                break
            time.sleep(1)
        if index % 25 == 0:
            print(json.dumps({"processed": index, **stats}), flush=True)
    stats["processed"] = stats["fetched"] + stats["cached"] + stats["failed"]
    stats["complete"] = stats["processed"] == stats["selected"] and not failures
    (cache / "last_fetch.json").write_text(
        json.dumps({**stats, "failures": failures}, indent=2) + "\n"
    )
    return stats


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--create-from-coverage", type=Path)
    parser.add_argument("--cache", type=Path)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=0)
    args = parser.parse_args()
    if args.create_from_coverage:
        require(not args.inventory.exists(), "Refuse to overwrite frozen inventory")
        result = inventory(ROOT, args.create_from_coverage)
        args.inventory.parent.mkdir(parents=True, exist_ok=True)
        args.inventory.write_text(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"pending_media": len(result["records"])}), flush=True)
    if args.cache:
        result = fetch(
            select(json.loads(args.inventory.read_text()), args.offset, args.limit), args.cache
        )
        print(json.dumps(result), flush=True)
        return 0 if result["complete"] else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
