#!/usr/bin/env python3
"""Rebuild data/culturemech_id_registry.tsv from the corpus (#144).

The registry maps every CultureMech id to the file holding it. A category move
changes the path but not the id, so every bulk recategorization silently rots it:
#115 moved 629 records, #120 another 73, #137 more, #143 three — none updated the
registry, leaving 5,511 rows pointing at files that no longer exist.

Deliberately separate from `assign_culturemech_ids.py`. That script *mints* ids,
so pointing it at a stale registry to fix paths risks renumbering records as a
side effect. This one never invents, retires or reassigns an id: it reads the id
each record already declares and records where that record now lives.

Safety rails, all fatal rather than silently papered over:

  * a record with no `id:` — the registry cannot represent it, and minting one is
    `assign-ids`' job, not this script's.
  * the same id in two files — the map would be ambiguous, and picking a winner
    would hide a real collision that `assign-ids-check` exists to surface.

Usage::

    just refresh-id-registry --dry-run   # report drift, write nothing
    just refresh-id-registry             # rewrite the registry
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DEFAULT_CORPUS = REPO / "data" / "normalized_yaml"
DEFAULT_REGISTRY = REPO / "data" / "culturemech_id_registry.tsv"
HEADER = "culturemech_id\tfile_path"

# The record id is a top-level key, so it is anchored at column 0. Ingredient and
# curation blocks further down also contain `id:` at an indent and must not win.
ID_RE = re.compile(r"^id:\s*(CultureMech:\d+)\s*$", re.M)


def scan_corpus(corpus: Path) -> tuple[dict[str, Path], list[Path], dict[str, list[Path]]]:
    """Return (id -> path, records_without_id, duplicated_ids)."""
    found: dict[str, list[Path]] = defaultdict(list)
    missing: list[Path] = []
    for path in sorted(corpus.rglob("*.yaml")):
        try:
            text = path.read_text(errors="replace")
        except OSError:
            missing.append(path)
            continue
        match = ID_RE.search(text)
        if match:
            found[match.group(1)].append(path)
        else:
            missing.append(path)
    duplicates = {cid: paths for cid, paths in found.items() if len(paths) > 1}
    resolved = {cid: paths[0] for cid, paths in found.items() if len(paths) == 1}
    return resolved, missing, duplicates


def read_registry(path: Path) -> dict[str, str]:
    if not path.is_file():
        return {}
    out: dict[str, str] = {}
    for i, line in enumerate(path.read_text().splitlines()):
        if i == 0 or not line.strip():
            continue
        cid, _, file_path = line.partition("\t")
        out[cid] = file_path
    return out


def render(mapping: dict[str, Path]) -> str:
    rows = sorted(mapping.items(), key=lambda kv: kv[0])
    body = "\n".join(f"{cid}\t{path.relative_to(REPO).as_posix()}" for cid, path in rows)
    return f"{HEADER}\n{body}\n"


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    ap.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY)
    ap.add_argument("--dry-run", action="store_true",
                    help="report drift without writing")
    args = ap.parse_args(argv)

    resolved, missing, duplicates = scan_corpus(args.corpus)

    if duplicates:
        print(f"ERROR: {len(duplicates)} id(s) appear in more than one file; the "
              f"registry would be ambiguous. Run `just assign-ids-check`.",
              file=sys.stderr)
        for cid, paths in sorted(duplicates.items())[:10]:
            print(f"  {cid}: {', '.join(str(p.relative_to(REPO)) for p in paths)}",
                  file=sys.stderr)
        return 2

    if missing:
        print(f"ERROR: {len(missing)} record(s) carry no top-level `id:`. Mint them "
              f"with `just assign-ids` first — this script never invents ids.",
              file=sys.stderr)
        for p in missing[:10]:
            print(f"  {p.relative_to(REPO)}", file=sys.stderr)
        return 2

    current = read_registry(args.registry)
    wanted = {cid: path.relative_to(REPO).as_posix() for cid, path in resolved.items()}

    repathed = {c for c in set(current) & set(wanted) if current[c] != wanted[c]}
    added = set(wanted) - set(current)
    dropped = set(current) - set(wanted)
    stale_now = {c for c, p in current.items() if not (REPO / p).is_file()}

    print(f"corpus records      : {len(wanted)}")
    print(f"registry rows       : {len(current)}")
    print(f"  paths corrected   : {len(repathed)}")
    print(f"  ids added         : {len(added)}")
    print(f"  ids dropped       : {len(dropped)}")
    print(f"  rows that pointed at a missing file: {len(stale_now)}")

    if dropped:
        print("\nNOTE: ids in the registry with no record in the corpus. This script "
              "drops them; if that is wrong, they were deleted records and the "
              "deletion is the thing to review:", file=sys.stderr)
        for cid in sorted(dropped)[:10]:
            print(f"  {cid} -> {current[cid]}", file=sys.stderr)

    if args.dry_run:
        print("\nDRY RUN — nothing written.")
        return 0

    args.registry.write_text(render(resolved))
    print(f"\nWrote {len(resolved)} rows -> {args.registry.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
