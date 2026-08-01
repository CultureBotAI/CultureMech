#!/usr/bin/env python3
"""Verify that every literature snippet attached to a CultureMech evidence
claim appears verbatim in the cached PubMed abstract for the cited
PMID/DOI.

This is the anti-hallucination gate: a curator (human or AI) must
back any literature snippet with a real reference, and the snippet
text must be a substring of the actual abstract.

Run via the `evidence-reference-validation` skill or directly:

    python3 scripts/validate_evidence_references.py
    python3 scripts/validate_evidence_references.py --strict

Verdict vocabulary (matches the Phase 1 plan):

  OK                       — snippet found in cached abstract
  MISSING_CACHE            — abstract not in references_cache (run fetcher)
  MISSING_REFERENCE        — snippet present but no PMID/DOI
  SNIPPET_NOT_IN_ABSTRACT  — snippet text not found in abstract (FAIL)
  NO_EVIDENCE              — evidence item has neither pmid/doi nor snippet
                             (allowed; informational only)

Substring matching is identical to claw's:
  NFKC normalize + lowercase + collapse whitespace + substring match.
"""
from __future__ import annotations

import argparse
import csv
import os
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = REPO_ROOT / "references_cache"
YAML_ROOT = REPO_ROOT / "data" / "normalized_yaml"

OUT_DIR = REPO_ROOT / "workspace" / "reports"
OUT_TSV = OUT_DIR / "evidence_reference_validation.tsv"
OUT_MD = OUT_DIR / "evidence_reference_validation.md"

PMID_RE = re.compile(r"^[0-9]+$")
WS_RE = re.compile(r"\s+")
PMID_REF_RE = re.compile(r"^\s*PMID\s*[:\s]\s*([0-9]+)\s*$", re.IGNORECASE)
DOI_REF_RE = re.compile(r"^\s*DOI\s*[:\s]\s*(\S+)\s*$", re.IGNORECASE)


@dataclass
class Verdict:
    yaml_path: str
    container: str
    pmid: str
    doi: str
    snippet: str
    verdict: str
    detail: str = ""


def normalize(s: str) -> str:
    """NFKC + collapse whitespace + lower for substring matching."""
    if not s:
        return ""
    s = unicodedata.normalize("NFKC", s)
    s = WS_RE.sub(" ", s).strip().lower()
    return s


def load_cache(pmid: str) -> str | None:
    p = CACHE_DIR / f"PMID_{pmid}.md"
    if not p.exists():
        return None
    return p.read_text()


def split_reference(reference: str) -> tuple[str, str]:
    """CultureMech stores citations as a single `reference:` string of
    shape `PMID:NNNNNNNN` or `DOI:10.xxxx/...`. Split into (pmid, doi)
    so the validation logic mirrors MIM's pmid/doi pair."""
    if not reference:
        return "", ""
    m = PMID_REF_RE.match(reference)
    if m:
        return m.group(1).strip(), ""
    m = DOI_REF_RE.match(reference)
    if m:
        return "", m.group(1).strip()
    return "", ""


def check_evidence(ev: dict, yaml_path: str, container: str) -> Verdict | None:
    reference = (ev.get("reference") or "").strip()
    pmid, doi = split_reference(reference)
    snippet = (ev.get("snippet") or ev.get("excerpt") or "").strip()

    if not snippet and not pmid and not doi and not reference:
        return None

    if reference and not pmid and not doi and not snippet:
        # Database/catalog references such as DSMZ:J1219 are useful
        # provenance but cannot be checked against PubMed abstract cache.
        return Verdict(yaml_path, container, "", "", "",
                       "NO_EVIDENCE",
                       f"non-literature reference without snippet: {reference!r}")

    if reference and not pmid and not doi:
        # Reference present with a snippet but couldn't be parsed as
        # PMID:/DOI:, so the snippet is not independently checkable.
        return Verdict(yaml_path, container, "", "", snippet,
                       "MISSING_REFERENCE",
                       f"unrecognized reference format: {reference!r}")

    if snippet and not (pmid or doi):
        return Verdict(yaml_path, container, pmid, doi, snippet,
                       "MISSING_REFERENCE",
                       "snippet provided but no pmid/doi")

    if (pmid or doi) and not snippet:
        return Verdict(yaml_path, container, pmid, doi, "",
                       "NO_EVIDENCE",
                       "reference cited without supporting snippet")

    if pmid and not PMID_RE.match(pmid):
        return Verdict(yaml_path, container, pmid, doi, snippet,
                       "MISSING_REFERENCE",
                       f"malformed pmid: {pmid!r}")

    if pmid:
        cache_text = load_cache(pmid)
        if cache_text is None:
            return Verdict(yaml_path, container, pmid, doi, snippet,
                           "MISSING_CACHE",
                           f"PMID:{pmid} not yet fetched")
        if normalize(snippet) in normalize(cache_text):
            return Verdict(yaml_path, container, pmid, doi, snippet,
                           "OK", "")
        return Verdict(yaml_path, container, pmid, doi, snippet,
                       "SNIPPET_NOT_IN_ABSTRACT",
                       "snippet text does not appear in abstract")

    # DOI-only: no cache layer yet (DOIs are supplementary; PMIDs are
    # primary). Treat as MISSING_CACHE.
    return Verdict(yaml_path, container, pmid, doi, snippet,
                   "MISSING_CACHE",
                   f"DOI:{doi} cache not implemented (PMID preferred)")


def iter_evidence_containers(y: dict):
    """Yield (container_label, evidence_list) tuples for every place
    CultureMech stores evidence[] entries."""
    if not isinstance(y, dict):
        return
    if isinstance(y.get("evidence"), list):
        yield "evidence", y["evidence"]
    sd = y.get("source_data")
    if isinstance(sd, dict) and isinstance(sd.get("evidence"), list):
        yield "source_data.evidence", sd["evidence"]
    for j, variant in enumerate(y.get("variants") or []):
        if not isinstance(variant, dict):
            continue
        if isinstance(variant.get("evidence"), list):
            yield f"variants[{j}].evidence", variant["evidence"]
    for j, tg in enumerate(y.get("target_organisms") or []):
        if not isinstance(tg, dict):
            continue
        if isinstance(tg.get("evidence"), list):
            yield f"target_organisms[{j}].evidence", tg["evidence"]
        for k, gm in enumerate(tg.get("growth_metrics") or []):
            if not isinstance(gm, dict):
                continue
            if isinstance(gm.get("evidence"), list):
                yield (f"target_organisms[{j}].growth_metrics[{k}].evidence",
                       gm["evidence"])


def walk_yamls() -> Iterable[Verdict]:
    if not YAML_ROOT.is_dir():
        return
    for path in sorted(YAML_ROOT.rglob("*.yaml")):
        try:
            with open(path) as f:
                y = yaml.safe_load(f) or {}
        except Exception:
            continue
        rel = str(path.relative_to(REPO_ROOT))

        for container_base, evs in iter_evidence_containers(y):
            for i, ev in enumerate(evs):
                if not isinstance(ev, dict):
                    continue
                v = check_evidence(ev, rel, f"{container_base}[{i}]")
                if v:
                    yield v


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true",
                    help=("exit 2 if any MISSING_CACHE present (default: "
                          "only SNIPPET_NOT_IN_ABSTRACT triggers exit 2)"))
    args = ap.parse_args()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    verdicts = list(walk_yamls())
    bucket: dict[str, int] = {}
    for v in verdicts:
        bucket[v.verdict] = bucket.get(v.verdict, 0) + 1

    with open(OUT_TSV, "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["yaml_path", "container", "verdict", "pmid", "doi",
                    "snippet", "detail"])
        for v in verdicts:
            w.writerow([v.yaml_path, v.container, v.verdict, v.pmid,
                        v.doi, v.snippet[:200], v.detail])

    md: list[str] = []
    md.append("# Evidence reference validation\n")
    md.append(f"Total evidence items checked: **{len(verdicts)}**\n")
    md.append("\n## Verdicts\n")
    md.append("| Verdict | Count |\n|---|---:|")
    for k in ("OK", "NO_EVIDENCE", "MISSING_CACHE", "MISSING_REFERENCE",
              "SNIPPET_NOT_IN_ABSTRACT"):
        md.append(f"| `{k}` | {bucket.get(k, 0)} |")
    if bucket.get("SNIPPET_NOT_IN_ABSTRACT", 0) > 0:
        md.append("\n## SNIPPET_NOT_IN_ABSTRACT (likely hallucinated)\n")
        md.append("| YAML | Container | PMID | Snippet (truncated) |")
        md.append("|---|---|---|---|")
        for v in verdicts:
            if v.verdict == "SNIPPET_NOT_IN_ABSTRACT":
                md.append(
                    f"| `{v.yaml_path}` | `{v.container}` | "
                    f"`{v.pmid}` | {v.snippet[:80]}... |")
    if bucket.get("MISSING_CACHE", 0) > 0:
        md.append(
            f"\n## MISSING_CACHE: {bucket['MISSING_CACHE']} entries\n")
        md.append(
            "Run `python3 scripts/fetch_pubmed_abstracts.py` to populate "
            "the cache, then rerun.\n")

    with open(OUT_MD, "w") as f:
        f.write("\n".join(md))

    print(f"Checked {len(verdicts)} evidence items")
    for k, n in sorted(bucket.items()):
        print(f"  {k:30s} {n}")
    print(f"\nWrote {OUT_TSV.relative_to(REPO_ROOT)}")
    print(f"Wrote {OUT_MD.relative_to(REPO_ROOT)}")

    if bucket.get("SNIPPET_NOT_IN_ABSTRACT", 0) > 0:
        return 2
    if args.strict and bucket.get("MISSING_CACHE", 0) > 0:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
