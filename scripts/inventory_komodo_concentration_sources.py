#!/usr/bin/env python3
"""Freeze exact KOMODO targets and their original-recipe links, not amount evidence."""

from __future__ import annotations

import argparse
import collections
import datetime
import json
import re
import subprocess
from pathlib import Path

from fetch_solution_concentration_sources import load_yaml
from repair_komodo12_extraction_evidence import MAPPING_URL, TableRows
from repair_mediadive_stock_concentration_evidence import require, sha

ROOT = Path(__file__).resolve().parents[1]


class MappingTable(TableRows):
    """Retain exact HTML spans while parsing the table's cells and links."""

    def __init__(self, raw):
        super().__init__()
        self.raw = raw
        self.offsets = [0]
        for line in raw.splitlines(keepends=True):
            self.offsets.append(self.offsets[-1] + len(line))
        self.start = None
        self.feed(raw)
        self.close()
        require(self.row is None and self.cell is None, "Unclosed mapping table")

    def absolute_offset(self):
        line, column = self.getpos()
        return self.offsets[line - 1] + column

    def handle_starttag(self, tag, attrs):
        if tag == "tr":
            self.start = self.absolute_offset()
        super().handle_starttag(tag, attrs)

    def handle_endtag(self, tag):
        super().handle_endtag(tag)
        if tag == "tr":
            end = self.raw.index(">", self.absolute_offset()) + 1
            self.rows[-1]["snippet"] = self.raw[self.start : end]


def read_mapping(path, metadata):
    raw = path.read_bytes()
    require(
        metadata["reference"] == MAPPING_URL and metadata["http_status"] == 200,
        "Wrong mapping source",
    )
    require(sha(raw) == metadata["sha256"], "Mapping hash drift")
    datetime.datetime.fromisoformat(metadata["accessed_at"])
    rows = {}
    header_seen = False
    for row in MappingTable(raw.decode()).rows:
        if len(row["cells"]) != 7:
            require(
                not any("MediaInfo=" in link.get("href", "") for link in row["links"]),
                "Mapping table columns changed",
            )
            continue
        if row["cells"] == [
            "ID",
            "Name",
            "PH Info",
            "Is Complex",
            "Is Aerobic",
            "Is SubMedium",
            "Instructions",
        ]:
            require(not header_seen, "Duplicate source header")
            header_seen = True
            continue
        sid = row["cells"][0]
        require(
            header_seen and re.fullmatch(r"[0-9][0-9A-Za-z._ (),-]*", sid),
            "Unreviewed KOMODO accession syntax",
        )
        require(sid not in rows, "Duplicate source mapping accession")
        require(len(row["cells"]) == 7, "Mapping table columns changed")
        url = row["cells"][6]
        match = re.fullmatch(
            r"https?://www\.dsmz\.de/microorganisms/medium/pdf/DSMZ_Medium(\d+[A-Za-z]*)\.pdf", url
        )
        require(
            match is not None and {"href": url} in row["links"], "Unreviewed original-recipe URL"
        )
        require(
            {"href": f"/komodo/servlet/KomodoTomcatServerSideUtilitiesModelSeed?MediaInfo={sid}"}
            in row["links"],
            "Mapping row identity link drift",
        )
        rows[sid] = {
            **row,
            "medium_id": match[1],
            "original_recipe": url.replace("http:", "https:", 1),
        }
    require(header_seen and rows, "Missing mapping table")
    return rows


def inventory(root, coverage_path, mapping_path, metadata):
    coverage = json.loads(coverage_path.read_text())
    rows = read_mapping(mapping_path, metadata)
    tracked = set(
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root)
        .decode()
        .split("\0")
    )
    records = []
    counts = collections.Counter()
    for item in coverage["pending_records"]:
        term = item["source_term"] or ""
        if not term.startswith("komodo.medium:"):
            continue
        path = root / item["path"]
        require(item["path"] in tracked and not path.is_symlink(), "Non-exact authoritative target")
        raw = path.read_bytes()
        require(sha(raw) == item["sha256"], "Coverage target drift")
        doc = load_yaml(raw)
        sid = term.split(":", 1)[1]
        require(
            doc["id"] == item["id"] and doc["media_term"]["term"]["id"] == term,
            "Record identity drift",
        )
        require(sid in rows, "Unmapped KOMODO target")
        row = rows[sid]
        exact_name = doc["original_name"] == row["cells"][1] == doc["media_term"]["term"]["label"]
        base_id = sid == row["medium_id"]
        relationship = doc.get("variant_relationship")
        counts["exact_names" if exact_name else "name_differences"] += 1
        counts["base_accessions" if base_id else "variant_accessions"] += 1
        records.append(
            {
                "path": item["path"],
                "id": doc["id"],
                "name": doc["original_name"],
                "before_sha256": sha(raw),
                "komodo_id": sid,
                "medium_id": row["medium_id"],
                "mapping": row,
                "exact_mapping_name": exact_name,
                "exact_base_accession": base_id,
                "variant_relationship": relationship,
            }
        )

    def key(item):
        return [
            int(part) if part.isdigit() else part for part in re.split(r"(\d+)", item["komodo_id"])
        ]

    records.sort(key=key)
    require(len({r["path"] for r in records}) == len(records), "Duplicate target")
    return {
        "version": 1,
        "commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True
        ).strip(),
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "coverage_snapshot": str(coverage_path),
        "coverage_sha256": sha(coverage_path.read_bytes()),
        "mapping_source": {
            k: metadata[k] for k in ("reference", "http_status", "accessed_at", "sha256")
        },
        "scope": "Original-recipe mapping only. No ingredient amount is supported by this inventory. Variant links do not authorize base-recipe concentrations.",
        "summary": {"records": len(records), "source_rows": len(rows), **counts},
        "records": records,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--coverage", required=True, type=Path)
    parser.add_argument("--mapping", required=True, type=Path)
    parser.add_argument("--mapping-metadata", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    require(not args.out.exists(), "Refuse to overwrite frozen inventory")
    result = inventory(
        ROOT, args.coverage, args.mapping, json.loads(args.mapping_metadata.read_text())
    )
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps(result["summary"], indent=2))


if __name__ == "__main__":
    main()
