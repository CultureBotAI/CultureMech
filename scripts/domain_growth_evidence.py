#!/usr/bin/env python3
"""Decide a medium's domain from the organisms that actually grow on it (#138).

`audit_domain_categories.py` classifies a record by the taxon names in its own
name fields. That leaves a residue where the name carries only a *physiology* —
"HALOPHILE MEDIUM", "ACIDO-THERMOPHILE MEDIUM" — and halophiles and thermophiles
span both domains. Filing those under `archaea/` is an assertion with nothing
behind it, which is precisely what #138 objects to.

There is a second, independent evidence source: kg-microbe's MediaDive transform
records which taxa were observed to grow in each medium
(`<NCBITaxon:x> METPO:2000517 <mediadive.medium:y>`). Resolving those taxa to a
domain answers the question from observation instead of from the label. It is
decisive on names that read the opposite way to the truth — `Halobacillus` and
`Virgibacillus` are Bacillota despite the halophile naming, while `Halorubrum`
and `Haladaptatus` are Halobacteriales.

Availability: kg-microbe is a separate checkout that CI does not have. Every
entry point degrades to "no evidence" when it is absent, so the audit's behaviour
is unchanged there rather than erroring. Set `KG_MICROBE_DIR` to override the
search.
"""

from __future__ import annotations

import os
import sqlite3
from collections import defaultdict
from pathlib import Path

ARCHAEA = "NCBITaxon:2157"
BACTERIA = "NCBITaxon:2"
GROWS_IN_MEDIUM = "METPO:2000517"
_MAX_LINEAGE_HOPS = 60


def resolve_kg_microbe_dir() -> Path | None:
    """First candidate that actually holds the transformed mediadive tables.

    Same probing rationale as tests/test_kg_media_matcher.py: the repo may sit at
    <workspace>/kg-microbe or nested at <workspace>/kg-microbe/kg-microbe.
    """
    env = os.environ.get("KG_MICROBE_DIR")
    workspace = Path(__file__).resolve().parent.parent.parent.parent
    candidates = [
        *([Path(env)] if env else []),
        workspace / "kg-microbe" / "kg-microbe",
        workspace / "kg-microbe",
        Path(__file__).resolve().parent.parent.parent / "kg-microbe",
    ]
    for cand in candidates:
        mediadive = cand / "data" / "transformed" / "mediadive"
        if (mediadive / "edges.tsv").is_file():
            return cand
    return None


def load_growth_edges(kg_dir: Path) -> dict[str, set[str]]:
    """{mediadive.medium:<id>: {NCBITaxon:<id>, ...}} for observed growth."""
    edges = kg_dir / "data" / "transformed" / "mediadive" / "edges.tsv"
    out: dict[str, set[str]] = defaultdict(set)
    with edges.open() as fh:
        next(fh, None)
        for line in fh:
            # rstrip first: kg-microbe's edges.tsv has 9 columns so the object is
            # not last today, but a narrower export would leave "\n" glued to the
            # medium id and silently match nothing.
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 3:
                continue
            subject, predicate, obj = parts[0], parts[1], parts[2]
            if predicate == GROWS_IN_MEDIUM and subject.startswith("NCBITaxon:"):
                out[obj].add(subject)
    return dict(out)


class DomainResolver:
    """Walk NCBITaxon `subClassOf` up to a domain, memoised."""

    def __init__(self, con: sqlite3.Connection):
        self.con = con
        self._cache: dict[str, str | None] = {}

    def domain_of(self, taxon: str) -> str | None:
        if taxon in self._cache:
            return self._cache[taxon]
        cur, seen = taxon, set()
        for _ in range(_MAX_LINEAGE_HOPS):
            if cur == ARCHAEA:
                self._cache[taxon] = "archaea"
                return "archaea"
            if cur == BACTERIA:
                self._cache[taxon] = "bacterial"
                return "bacterial"
            row = self.con.execute(
                "SELECT object FROM edge WHERE subject=? AND predicate='rdfs:subClassOf'",
                (cur,),
            ).fetchone()
            if not row or row[0] in seen:
                break
            seen.add(row[0])
            cur = row[0]
        self._cache[taxon] = None
        return None


def domain_from_growth(
    medium_id: str,
    growth: dict[str, set[str]],
    resolver: DomainResolver,
) -> tuple[str | None, dict]:
    """Return (domain | None, detail).

    `None` when there is no growth evidence, or when the evidence names both
    domains — a medium that genuinely supports both is a curator's call, not a
    move. Taxa whose lineage cannot be resolved are counted but never decide.
    """
    taxa = growth.get(medium_id) or set()
    if not taxa:
        return None, {"n_taxa": 0, "archaea": 0, "bacterial": 0, "unresolved": 0}

    counts = {"archaea": 0, "bacterial": 0, "unresolved": 0}
    per_domain: dict[str, list[str]] = defaultdict(list)
    for taxon in sorted(taxa):
        dom = resolver.domain_of(taxon)
        counts["unresolved" if dom is None else dom] += 1
        if dom:
            per_domain[dom].append(taxon)

    detail = {"n_taxa": len(taxa), **counts, "taxa_by_domain": dict(per_domain)}
    if counts["archaea"] and counts["bacterial"]:
        return None, {**detail, "reason": "growth evidence names both domains"}
    if counts["archaea"]:
        return "archaea", detail
    if counts["bacterial"]:
        return "bacterial", detail
    return None, {**detail, "reason": "no taxon lineage resolved to a domain"}
