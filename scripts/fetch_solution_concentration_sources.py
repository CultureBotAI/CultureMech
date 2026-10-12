#!/usr/bin/env python3
"""Snapshot exact tracked solution targets and cache official raw JSON evidence.

Never writes recipe data. Fetch is serial and resumable, with provenance and
content hashes. The public /solutions index omits main solutions, so inventory
comes from exact tracked root mediadive.solution identifiers, not that index.
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import subprocess
import time
import urllib.error
import urllib.request
from pathlib import Path

import yaml
from repair_mediadive_stock_concentration_evidence import require, sha

ROOT = Path(__file__).resolve().parents[1]
API = "https://mediadive.dsmz.de/rest/solution/"
PRIOR_ACTIONS = {"CURATED_MEDIADIVE_STOCK_CONCENTRATION_EVIDENCE"}


def load_yaml(raw):
    return yaml.load(raw, Loader=yaml.CSafeLoader)


def inventory(root):
    paths = (
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root)
        .decode()
        .split("\0")
    )
    records, previous = [], []
    total = 0
    for path in paths:
        if not path.endswith(".yaml"):
            continue
        raw = (root / path).read_bytes()
        doc = load_yaml(raw)
        total += 1
        sid = str((doc.get("term") or {}).get("id", ""))
        match = re.fullmatch(r"mediadive\.solution:(\d+)", sid)
        if not match:
            continue
        item = {
            "path": path,
            "id": doc["id"],
            "solution_id": int(match[1]),
            "name": doc["preferred_term"],
            "before_sha256": sha(raw),
        }
        reviewed = any(e.get("action") in PRIOR_ACTIONS for e in doc.get("curation_history", []))
        (previous if reviewed else records).append(item)
    records.sort(key=lambda r: (r["solution_id"], r["path"]))
    return {
        "version": 1,
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root).decode().strip(),
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "normalized_count": total,
        "previously_curated": previous,
        "records": records,
    }


def read_capture(cache, sid):
    raw = (cache / f"{sid}.json").read_bytes()
    meta = json.loads((cache / f"{sid}.metadata.json").read_text())
    require(meta["url"] == API + str(sid) == meta["response_url"], "Source URL mismatch")
    require(
        meta["http_status"] == 200 and meta["sha256"] == sha(raw), "Source hash/status mismatch"
    )
    payload = json.loads(raw)
    require(payload["status"] == 200 and payload["count"] == 1, "Invalid source envelope")
    require(payload["data"]["id"] == sid, "Wrong source solution")
    datetime.datetime.fromisoformat(meta["accessed_at"])
    return raw.decode(), meta


def fetch_one(cache, sid, timeout=30):
    url = API + str(sid)
    request = urllib.request.Request(
        url, headers={"Accept": "application/json", "User-Agent": "CultureMech-evidence-review/1.0"}
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        require(response.status == 200 and response.url == url, "Unexpected source redirect/status")
        raw = response.read()
    payload = json.loads(raw)
    require(payload["status"] == 200 and payload["count"] == 1, "Source unavailable")
    require(payload["data"]["id"] == sid, "Source ID mismatch")
    meta = {
        "url": url,
        "response_url": url,
        "http_status": 200,
        "sha256": sha(raw),
        "accessed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }
    (cache / f"{sid}.json").write_bytes(raw)
    (cache / f"{sid}.metadata.json").write_text(json.dumps(meta, indent=2) + "\n")
    return meta


def fetch(records, cache, delay=0.25):
    cache.mkdir(parents=True, exist_ok=True)
    stats = {"selected": len(records), "fetched": 0, "cached": 0, "failed": 0}
    failures = []
    consecutive = 0
    for index, record in enumerate(records, 1):
        sid = record["solution_id"]
        try:
            if (cache / f"{sid}.json").exists():
                read_capture(cache, sid)
                stats["cached"] += 1
            else:
                fetch_one(cache, sid)
                stats["fetched"] += 1
                time.sleep(delay)
            consecutive = 0
        except (OSError, ValueError, KeyError) as exc:
            stats["failed"] += 1
            failures.append({"solution_id": sid, "path": record["path"], "error": str(exc)})
            consecutive += 1
            # A broken/rate-limited endpoint is not a reason to hammer the corpus.
            if isinstance(exc, urllib.error.HTTPError) and exc.code in {429, 503}:
                break
            if consecutive >= 3:
                break
            time.sleep(max(delay, 1))
        if index % 25 == 0:
            print(json.dumps({"processed": index, **stats}), flush=True)
    stats["processed"] = stats["fetched"] + stats["cached"] + stats["failed"]
    stats["complete"] = stats["processed"] == stats["selected"] and not failures
    (cache / "last_fetch.json").write_text(
        json.dumps({**stats, "failures": failures}, indent=2) + "\n"
    )
    return stats


def select(manifest, offset, limit):
    require(offset >= 0 and limit >= 0, "Offsets and limits must be nonnegative")
    return manifest["records"][offset : offset + limit if limit else None]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--create-inventory", action="store_true")
    parser.add_argument("--cache", type=Path)
    parser.add_argument("--offset", type=int, default=0)
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--delay", type=float, default=0.25)
    args = parser.parse_args()
    if args.create_inventory:
        require(not args.inventory.exists(), "Refuse to overwrite a pinned inventory")
        args.inventory.parent.mkdir(parents=True, exist_ok=True)
        snapshot = inventory(ROOT)
        args.inventory.write_text(json.dumps(snapshot, indent=2) + "\n")
        print(
            json.dumps(
                {
                    "pending_solutions": len(snapshot["records"]),
                    "previously_curated": len(snapshot["previously_curated"]),
                    "normalized_records": snapshot["normalized_count"],
                }
            ),
            flush=True,
        )
    if args.cache:
        require(args.delay >= 0.25, "Retain serial source rate limiting")
        snapshot = json.loads(args.inventory.read_text())
        stats = fetch(select(snapshot, args.offset, args.limit), args.cache, args.delay)
        print(json.dumps(stats), flush=True)
        return 0 if stats["complete"] else 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
