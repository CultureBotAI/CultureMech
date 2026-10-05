"""Resolve retained map source stems through the current stable-ID registry.

Coordinates and embedded point metadata are historical and remain unchanged.
Exact source stems that still exist in the normalized corpus receive links.
Category matches take precedence; category moves require a globally unique
stable identity. Missing or ambiguous identities remain unresolved.
"""

from __future__ import annotations

import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def build_links(root: Path = ROOT) -> dict:
    registry = root / "data/culturemech_id_registry.tsv"
    candidates: dict[str, set[str]] = {}
    with registry.open() as stream:
        for row in csv.DictReader(stream, delimiter="\t"):
            path = Path(row["file_path"])
            ident = row["culturemech_id"]
            if (
                path.parts[:2] == ("data", "normalized_yaml")
                and len(path.parts) == 4
                and (root / path).is_file()
                and re.fullmatch(r"CultureMech:\d{6}", ident)
            ):
                key = path.parts[2] + "/" + path.stem
                candidates.setdefault(key, set()).add(ident)
                candidates.setdefault("*/" + path.stem, set()).add(ident)
    return {
        "registry_sha256": hashlib.sha256(registry.read_bytes()).hexdigest(),
        "identity_basis": "Exact source stem in current registry; prefer category, allow category moves only when the source stem has one unique stable ID",
        "links": {
            key: "../pages/normalized/" + next(iter(ids)).split(":")[1] + ".html"
            for key, ids in sorted(candidates.items())
            if len(ids) == 1
        },
    }


if __name__ == "__main__":
    output = ROOT / "app/map-record-links.json"
    output.write_text(json.dumps(build_links(), indent=2) + "\n")
    print(f"Wrote {output}")
