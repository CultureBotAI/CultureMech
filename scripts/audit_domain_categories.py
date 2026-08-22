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

The check runs in **both** directions: `bacterial/` holding archaeal media
(#114) and `archaea/` holding bacterial media (#116) are the same defect, and the
original 71-file `archaea/` import turned out to be 29 archaeal / 26 bacterial /
16 undecidable, so neither directory can be trusted as ground truth.

A record naming taxa from *both* domains (e.g. a Methanosaeta/Brevibacterium
co-culture medium) is reported as MIXED and never moved automatically. A record
naming no taxon at all ("halophile medium" — halophiles span both domains) is
reported as unresolved and likewise left alone.

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
# Where importers put recipes they could not classify; see the unresolved bucket.
DEFAULT_DOMAIN_DIR = "bacterial"

# Wording that denotes a domain without naming a taxon.
ARCHAEAL_WORDS = re.compile(
    r"\b(?:archaea|archaeal|archaeon|[a-z]*archaeote|haloarchaea[a-z]*"
    r"|methanogen|methanogens|methanogenic)\b"
)
BACTERIAL_WORDS = re.compile(r"\b(?:bacteri(?:um|a|al)|eubacteri[a-z]*|cyanobacteri[a-z]*)\b")

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


def binomial_names(con: sqlite3.Connection, root: str) -> set[str]:
    """Lowercased two-word species binomials under `root`.

    Genus names alone are sometimes homonyms across domains and get discarded —
    *Bacillus* is both a bacterial genus and a diatom genus, so it can never be
    evidence on its own. The full binomial usually is unambiguous, which recovers
    records like ``medium_for_bacillus_stearothermophilus``.
    """
    query = """
        select distinct s.value
          from entailed_edge e
          join statements r
            on r.subject = e.subject
           and r.predicate = 'obo:ncbitaxon#has_rank'
           and r.object = 'NCBITaxon:species'
          join statements s
            on s.subject = e.subject
           and (s.predicate = 'rdfs:label' or s.predicate like '%synonym%')
         where e.object = ? and e.predicate = 'rdfs:subClassOf'
    """
    out = set()
    for (value,) in con.execute(query, (root,)):
        if not value:
            continue
        parts = value.lower().split()
        if len(parts) == 2 and all(p.isalpha() for p in parts):
            out.add(" ".join(parts))
    return out


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

# MediaDive republishes DSMZ and JCM media, so a `mediadive.medium:` id alone does
# not name the registry. The corpus prefixes those by the originating registry —
# `DSMZ_1422_HALORUBRUM_MEDIUM.yaml`, `JCM_J168_HALOBACTERIA_MEDIUM.yaml` — and
# reserves the bare `mediadive_` prefix for stock-solution records.
REGISTRY_BY_SOURCE = {"dsmz": "DSMZ", "jcm": "JCM"}


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

    # only the record-level `notes:` line carries the provenance; ingredient notes
    # further down can also contain "Source:" and must not win
    match = re.search(r"^notes:.*?Source:\s*(\S+)", text, re.M)
    if match:
        # `notes: 'Source: DSMZ'` — the closing quote of the YAML scalar rides
        # along whenever Source is the last field on the line
        rec.source = match.group(1).strip("'\"")
    registry = REGISTRY_BY_SOURCE.get(rec.source.lower())
    for pattern, template in SOURCE_ID_PATTERNS:
        found = pattern.search(text)
        if found:
            if registry and template.startswith("mediadive_"):
                template = registry + "_{}"
            rec.source_id = template.format(found.group(1))
            break
    return rec


@dataclass
class Evidence:
    """Name evidence for one domain: taxon names, binomials and generic wording."""

    taxa: set[str]
    binomials: set[str]
    words: re.Pattern


def classify(rec: Recipe, archaea: Evidence, bacteria: Evidence) -> None:
    # Separators are normalised to spaces before matching: `\b` treats `_` as a
    # word character, so `\bmethanogen\b` would never fire on the slugified
    # filename `methanogen_high_salt_medium`, only on a spaced `original_name`.
    blob = NON_WORD.sub(
        " ",
        " ".join([rec.path.stem, rec.name, rec.original_name, rec.preferred_term]).lower(),
    )
    tokens = [t for t in blob.split() if t]
    pairs = {f"{a} {b}" for a, b in zip(tokens, tokens[1:], strict=False)}
    unique = set(tokens)

    def hits(ev: Evidence) -> tuple[list[str], set[str]]:
        binomials = pairs & ev.binomials
        found = sorted(unique & ev.taxa) + sorted(binomials)
        return (found or sorted(set(ev.words.findall(blob)))), binomials

    arch_hits, arch_bi = hits(archaea)
    bact_hits, bact_bi = hits(bacteria)

    def drop_epithets(found: list[str], other_binomials: set[str]) -> list[str]:
        """Discard single-word hits that are only the epithet of the other domain's
        binomial. *Methanocalculus alkaliphilus* is an archaeon; matching the
        bacterial genus *Alkaliphilus* on its species epithet is not evidence that
        the medium has anything to do with that genus."""
        words = {w for b in other_binomials for w in b.split()}
        return [f for f in found if " " in f or f not in words]

    rec.archaeal = drop_epithets(arch_hits, bact_bi)
    rec.bacterial = drop_epithets(bact_hits, arch_bi)


def slugify_for_filename(text: str) -> str:
    return re.sub(r"_+", "_", re.sub(r"[^A-Za-z0-9]+", "_", text)).strip("_")


def target_path(rec: Recipe, dest_dir: Path, reserved: set[Path]) -> Path:
    """Where `rec` should live, disambiguated by source prefix if the name is taken.

    Multiple registries (KOMODO / TOGO / JCM / DSMZ) publish distinct media that
    slugify to the same filename; the repo already disambiguates these with a
    source prefix (e.g. ``KOMODO_372_HALOBACTERIA_medium.yaml`` and
    ``TOGO_M159_Halobacteria_Medium.yaml`` both carry ``name: halobacteria_medium``).

    `reserved` accumulates the targets already handed out in this run. Every target
    is chosen before *any* file is moved, so an on-disk existence check alone would
    hand the same name to two different recipes and silently destroy one of them.
    """

    def free(candidate: Path) -> bool:
        return not candidate.exists() and candidate not in reserved

    candidate = dest_dir / rec.path.name
    if not free(candidate):
        prefix = rec.source_id or slugify_for_filename(rec.source)[:12] or "DUP"
        stem = slugify_for_filename(rec.display_name) or rec.path.stem
        candidate = dest_dir / f"{prefix}_{stem}.yaml"
        suffix = 2
        while not free(candidate):
            candidate = dest_dir / f"{prefix}_{stem}_{suffix}.yaml"
            suffix += 1

    reserved.add(candidate)
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
    try:
        arch_all = taxon_names(con, ARCHAEA)
        bact_all = taxon_names(con, BACTERIA)
        euk_all = taxon_names(con, EUKARYOTA)
        arch_bi = binomial_names(con, ARCHAEA)
        bact_bi = binomial_names(con, BACTERIA)
    finally:
        con.close()
    # only names unique to one domain are usable as evidence
    archaea = Evidence(
        taxa=arch_all - bact_all - euk_all,
        binomials=arch_bi - bact_bi,
        words=ARCHAEAL_WORDS,
    )
    bacteria = Evidence(
        taxa=bact_all - arch_all - euk_all,
        binomials=bact_bi - arch_bi,
        words=BACTERIAL_WORDS,
    )

    print(
        f"NCBITaxon: {len(archaea.taxa)} archaea-only and {len(bacteria.taxa)} "
        f"bacteria-only names at ranks {'/'.join(RANKS)}; "
        f"{len(archaea.binomials)}/{len(bacteria.binomials)} species binomials"
    )

    findings: dict[str, list[dict]] = {"misfiled": [], "mixed": [], "unresolved": []}

    # Both directions are the same defect (#114 put archaea under bacterial/, #116
    # the mirror image), so they are handled by one symmetric pass.
    moves: list[tuple[Recipe, Path, str]] = []
    reserved: set[Path] = set()
    for src_dir, dest_dir, dest_category in (
        ("bacterial", "archaea", "archaea"),
        ("archaea", "bacterial", "bacterial"),
    ):
        for path in sorted((RECIPE_ROOT / src_dir).glob("*.yaml")):
            rec = read_recipe(path)
            classify(rec, archaea, bacteria)
            own, other = (
                (rec.bacterial, rec.archaeal)
                if src_dir == "bacterial"
                else (rec.archaeal, rec.bacterial)
            )
            if not other:
                # No evidence for the other domain, so nothing to move. Absence of
                # evidence is only *reportable* outside the default directory:
                # `bacterial/` is where the importers put anything they could not
                # classify, so "chocolate agar" naming no taxon there is unremarkable.
                # In `archaea/` someone positively asserted a domain, so a name with
                # no taxonomic support is an unsubstantiated claim worth surfacing.
                if not own and src_dir != DEFAULT_DOMAIN_DIR:
                    findings["unresolved"].append(
                        {
                            "file": f"{src_dir}/{path.name}",
                            "id": rec.identifier,
                            "name": rec.display_name,
                        }
                    )
                continue
            entry = {
                "file": f"{src_dir}/{path.name}",
                "id": rec.identifier,
                "name": rec.display_name,
                "archaeal_evidence": rec.archaeal,
                "bacterial_evidence": rec.bacterial,
                "is_solution": rec.is_solution,
            }
            if own:  # names taxa from both domains -> a curator's call, never ours
                findings["mixed"].append(entry)
                continue
            dest = target_path(rec, RECIPE_ROOT / dest_dir, reserved)
            entry["moves_to"] = f"{dest_dir}/{dest.name}"
            entry["renamed"] = dest.name != path.name
            findings["misfiled"].append(entry)
            moves.append((rec, dest, dest_category))

    for direction in ("archaea", "bacterial"):
        rows = [e for e in findings["misfiled"] if e["moves_to"].startswith(direction)]
        renamed = sum(1 for e in rows if e["renamed"])
        src = "bacterial" if direction == "archaea" else "archaea"
        print(
            f"\n{src}/ -> {direction}/ : {len(rows)} misfiled "
            f"({renamed} need a source-prefixed filename to avoid a collision)"
        )
        for entry in rows:
            flag = " [RENAME]" if entry["renamed"] else ""
            flag += " [SOLUTION RECORD]" if entry["is_solution"] else ""
            ev = entry["archaeal_evidence"] or entry["bacterial_evidence"]
            print(f"  {entry['file'][:58]:<60} {','.join(ev)[:24]:<26}{flag}")

    print(f"\nMIXED domain, left in place for curation: {len(findings['mixed'])}")
    for entry in findings["mixed"]:
        print(
            f"  {entry['file'][:58]:<60} archaea={','.join(entry['archaeal_evidence'])}"
            f" bacteria={','.join(entry['bacterial_evidence'])}"
        )

    print(
        f"\nFiled outside {DEFAULT_DOMAIN_DIR}/ but naming no taxon at all "
        f"(unsubstantiated domain claim): {len(findings['unresolved'])}"
    )
    for entry in findings["unresolved"]:
        print(f"  {entry['file'][:58]:<60} {entry['name'][:34]}")

    if args.apply:
        unstamped = []
        for rec, dest, dest_category in moves:
            git_mv(rec.path, dest)
            if not restamp_category(dest, dest_category):
                unstamped.append(dest.name)
        print(f"\nApplied: moved {len(moves)} recipes and restamped their category")
        if unstamped:
            # a moved file with no category: line keeps advertising its old
            # domain to anything that reads the field
            print(
                f"WARNING: {len(unstamped)} moved file(s) had no 'category:' line to "
                f"restamp: {', '.join(unstamped[:5])}",
                file=sys.stderr,
            )
    else:
        print("\n(report only — rerun with --apply to move these files)")

    if args.json:
        args.json.write_text(json.dumps(findings, indent=2))
        print(f"findings written to {args.json}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
