#!/usr/bin/env python3
"""Audit (and optionally fix) domain misclassification in data/normalized_yaml/.

Recipes are filed in per-domain directories (``bacterial/``, ``archaea/``, ...) and
carry a matching ``category:`` field.  Downstream tooling — notably the deep-research
prioritizer — infers the organism domain from that pair, so a medium named for an
archaeon but filed under ``bacterial/`` is silently scored and reported as Bacteria
(see issues #114 / #116).

This script cross-checks every recipe's *name* against NCBITaxon: it collects the
labels **and synonyms** of every taxon at rank genus/family/order/class/phylum under
Archaea (NCBITaxon:2157), Bacteria (NCBITaxon:2) and Eukaryota (NCBITaxon:2759),
drops any name shared between domains, and whole-word matches the remainder against
the filename, ``name`` and ``original_name``.

Matching on synonyms matters: *Methanosaeta* is only a synonym of *Methanothrix*
(NCBITaxon:2222), so a label-only audit misses every ``methanosaeta_*`` medium.
Including higher ranks matters for the same reason: *Halobacteria* (class),
*Sulfolobales* / *Thermococcales* (order) and *Methanobacteriaceae* (family) are not
genera and are invisible to a genus-only audit.

A record naming taxa from *both* domains (e.g. a Methanosaeta/Brevibacterium
co-culture medium) is reported as MIXED and never moved automatically.

Usage::

    python scripts/audit_domain_categories.py                 # report only
    python scripts/audit_domain_categories.py --json out.json # machine-readable
    python scripts/audit_domain_categories.py --apply         # move + restamp category
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import sqlite3
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
RECIPE_ROOT = REPO / "data" / "normalized_yaml"
DEFAULT_DB = Path.home() / ".data" / "oaklib" / "ncbitaxon.db"

ARCHAEA, BACTERIA, EUKARYOTA = "NCBITaxon:2157", "NCBITaxon:2", "NCBITaxon:2759"
RANKS = ("genus", "family", "order", "class", "phylum")

# Wording that denotes a domain without naming a taxon.
ARCHAEAL_WORDS = re.compile(
    r"\b(?:archaea|archaeal|archaeon|[a-z]*archaeote|haloarchaea[a-z]*"
    r"|methanogen|methanogens|methanogenic)\b"
)
BACTERIAL_WORDS = re.compile(
    r"\b(?:bacteri(?:um|a|al)|eubacteri[a-z]*|cyanobacteri[a-z]*)\b"
)

NON_WORD = re.compile(r"[^a-z0-9]+")
# Taxon names shorter than this are too collision-prone to match on.
MIN_TAXON_LEN = 5


def taxon_names(con: sqlite3.Connection, root: str) -> set[str]:
    """Lowercased labels + synonyms of all genus..phylum taxa under `root`."""
    ranks = ",".join(f"'NCBITaxon:{r}'" for r in RANKS)
    query = f"""
        select distinct s.value
          from entailed_edge e
          join statements r
            on r.subject = e.subject
           and r.predicate = 'obo:ncbitaxon#has_rank'
           and r.object in ({ranks})
          join statements s
            on s.subject = e.subject
           and (s.predicate = 'rdfs:label' or s.predicate like '%synonym%')
         where e.object = ? and e.predicate = 'rdfs:subClassOf'
    """
    return {
        row[0].lower()
        for row in con.execute(query, (root,))
        # multi-word names ("Candidatus ...") never appear in a slugified filename
        if row[0] and len(row[0]) >= MIN_TAXON_LEN and " " not in row[0]
    }


@dataclass
class Recipe:
    path: Path
    identifier: str = ""
    name: str = ""
    original_name: str = ""
    category: str = ""
    preferred_term: str = ""
    source: str = ""
    source_id: str = ""
    is_solution: bool = False
    archaeal: list[str] = field(default_factory=list)
    bacterial: list[str] = field(default_factory=list)

    @property
    def mixed(self) -> bool:
        return bool(self.archaeal and self.bacterial)

    @property
    def display_name(self) -> str:
        return self.original_name or self.preferred_term or self.name


SOURCE_ID_PATTERNS = (
    # (regex over the raw text, prefix template)
    (re.compile(r"togomedium\.org/medium/(M\d+)"), "TOGO_{}"),
    (re.compile(r"\bkomodo\.medium:(\S+)"), "KOMODO_{}"),
    (re.compile(r"\bmediadive\.medium:(\S+)"), "mediadive_{}"),
    (re.compile(r"\bID:\s*(\d+)"), "ID_{}"),
)


def read_recipe(path: Path) -> Recipe:
    rec = Recipe(path=path)
    text = path.read_text(errors="replace")
    for line in text.splitlines():
        if line.startswith("id:") and not rec.identifier:
            rec.identifier = line[3:].strip()
        elif line.startswith("name:"):
            rec.name = line[5:].strip().strip("'\"")
        elif line.startswith("original_name:"):
            rec.original_name = line[14:].strip().strip("'\"")
        elif line.startswith("category:"):
            rec.category = line[9:].strip()
        elif line.startswith("preferred_term:"):
            rec.preferred_term = line[15:].strip().strip("'\"")
        elif line.startswith("composition:"):
            rec.is_solution = True

    match = re.search(r"Source:\s*(\S+)", text)
    if match:
        rec.source = match.group(1)
    for pattern, template in SOURCE_ID_PATTERNS:
        found = pattern.search(text)
        if found:
            rec.source_id = template.format(found.group(1))
            break
    return rec


def classify(rec: Recipe, archaeal: set[str], bacterial: set[str]) -> None:
    blob = " ".join(
        [rec.path.stem, rec.name, rec.original_name, rec.preferred_term]
    ).lower()
    tokens = set(NON_WORD.split(blob))
    rec.archaeal = sorted(tokens & archaeal) or sorted(set(ARCHAEAL_WORDS.findall(blob)))
    rec.bacterial = sorted(tokens & bacterial) or sorted(set(BACTERIAL_WORDS.findall(blob)))


def slugify_for_filename(text: str) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]+", "_", text)).strip("_")


def target_path(rec: Recipe, dest_dir: Path) -> Path:
    """Where `rec` should live, disambiguated by source prefix if the name is taken.

    Multiple registries (KOMODO / TOGO / JCM / DSMZ) publish distinct media that
    slugify to the same filename; the repo already disambiguates these with a
    source prefix (e.g. ``KOMODO_372_HALOBACTERIA_medium.yaml`` and
    ``TOGO_M159_Halobacteria_Medium.yaml`` both carry ``name: halobacteria_medium``).
    """
    candidate = dest_dir / rec.path.name
    if not candidate.exists():
        return candidate

    prefix = rec.source_id or slugify_for_filename(rec.source)[:12] or "DUP"
    stem = slugify_for_filename(rec.display_name) or rec.path.stem
    candidate = dest_dir / f"{prefix}_{stem}.yaml"
    suffix = 2
    while candidate.exists():
        candidate = dest_dir / f"{prefix}_{stem}_{suffix}.yaml"
        suffix += 1
    return candidate


def restamp_category(path: Path, new_category: str) -> bool:
    text = path.read_text()
    updated, count = re.subn(
        r"^category: .*$", f"category: {new_category}", text, count=1, flags=re.M
    )
    if count:
        path.write_text(updated)
    return bool(count)


def git_mv(src: Path, dest: Path) -> None:
    try:
        subprocess.run(
            ["git", "-C", str(REPO), "mv", str(src), str(dest)],
            check=True,
            capture_output=True,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        shutil.move(str(src), str(dest))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="move unambiguous misfiles and restamp category (default: report only)",
    )
    parser.add_argument("--json", type=Path, help="write the full findings as JSON")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="NCBITaxon sqlite")
    args = parser.parse_args()

    if not args.db.exists():
        print(
            f"NCBITaxon sqlite not found at {args.db}\n"
            "Fetch it with:  runoak -i sqlite:obo:ncbitaxon info NCBITaxon:2157",
            file=sys.stderr,
        )
        return 2

    con = sqlite3.connect(args.db)
    arch_all = taxon_names(con, ARCHAEA)
    bact_all = taxon_names(con, BACTERIA)
    euk_all = taxon_names(con, EUKARYOTA)
    # only names unique to one domain are usable as evidence
    archaeal = arch_all - bact_all - euk_all
    bacterial = bact_all - arch_all - euk_all

    print(
        f"NCBITaxon: {len(archaeal)} archaea-only and {len(bacterial)} bacteria-only "
        f"names at ranks {'/'.join(RANKS)}"
    )

    findings: dict[str, list[dict]] = {"misfiled": [], "mixed": [], "reverse": []}

    # --- bacterial/ holding archaeal media -------------------------------------
    moves: list[tuple[Recipe, Path]] = []
    for path in sorted((RECIPE_ROOT / "bacterial").glob("*.yaml")):
        rec = read_recipe(path)
        classify(rec, archaeal, bacterial)
        if not rec.archaeal:
            continue
        entry = {
            "file": path.name,
            "id": rec.identifier,
            "name": rec.display_name,
            "archaeal_evidence": rec.archaeal,
            "bacterial_evidence": rec.bacterial,
            "is_solution": rec.is_solution,
        }
        if rec.mixed:
            findings["mixed"].append(entry)
            continue
        dest = target_path(rec, RECIPE_ROOT / "archaea")
        entry["moves_to"] = f"archaea/{dest.name}"
        entry["renamed"] = dest.name != path.name
        findings["misfiled"].append(entry)
        moves.append((rec, dest))

    # --- archaea/ holding bacterial media (reported, never auto-moved) ---------
    for path in sorted((RECIPE_ROOT / "archaea").glob("*.yaml")):
        rec = read_recipe(path)
        classify(rec, archaeal, bacterial)
        if rec.bacterial and not rec.archaeal:
            findings["reverse"].append(
                {
                    "file": path.name,
                    "id": rec.identifier,
                    "name": rec.display_name,
                    "bacterial_evidence": rec.bacterial,
                }
            )

    renamed = sum(1 for e in findings["misfiled"] if e["renamed"])
    print(
        f"\nbacterial/ -> archaea/ : {len(findings['misfiled'])} misfiled "
        f"({renamed} need a source-prefixed filename to avoid a collision)"
    )
    for entry in findings["misfiled"]:
        flag = " [RENAME]" if entry["renamed"] else ""
        flag += " [SOLUTION RECORD]" if entry["is_solution"] else ""
        print(
            f"  {entry['file'][:58]:<60} "
            f"{','.join(entry['archaeal_evidence'])[:24]:<26}{flag}"
        )

    print(f"\nMIXED domain, left in place for curation: {len(findings['mixed'])}")
    for entry in findings["mixed"]:
        print(
            f"  {entry['file'][:58]:<60} archaea={','.join(entry['archaeal_evidence'])}"
            f" bacteria={','.join(entry['bacterial_evidence'])}"
        )

    print(
        f"\narchaea/ naming a bacterium (pre-existing, reported only): "
        f"{len(findings['reverse'])}"
    )
    for entry in findings["reverse"]:
        print(
            f"  {entry['file'][:58]:<60} {','.join(entry['bacterial_evidence'])[:30]}"
        )

    if args.apply:
        for rec, dest in moves:
            git_mv(rec.path, dest)
            restamp_category(dest, "archaea")
        print(f"\nApplied: moved {len(moves)} recipes into archaea/ with category: archaea")
    else:
        print("\n(report only — rerun with --apply to move these files)")

    if args.json:
        args.json.write_text(json.dumps(findings, indent=2))
        print(f"findings written to {args.json}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
