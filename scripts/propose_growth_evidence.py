#!/usr/bin/env python3
"""Propose growth-evidence candidates for CultureMech MediaRecipe YAMLs.

Phase A of the CultureMech literature-review pipeline (per
`/Users/marcin/.claude/plans/now-focus-on-culturemech-piped-shell.md`).
Mirrors the MIM `propose_evidence.py` flow.

Strategy (no LLM/provider — uses NCBI E-utilities directly):

  1. Walk MediaRecipe YAMLs under data/normalized_yaml/**/*.yaml,
     filtering by --medium glob, --media-term set, or --limit.
  2. Build PubMed queries from medium name + each existing
     target_organisms[].preferred_term. Fall back to medium-name
     queries (growth, OD600, doubling time, cultivation) if no
     organisms.
  3. Fetch top-N abstracts via ESearch + EFetch (idempotent cache via
     references_cache/PMID_*.md).
  4. Extract candidate (organism, genome_id, growth_metrics, evidence)
     tuples per abstract using regex.
  5. Emit one proposal YAML per medium under
     workspace/reports/growth_evidence_proposals/{medium_id}.yaml for
     curator review.

Default is dry-run (no proposal files written). `--apply` writes.

Usage:
    python3 scripts/propose_growth_evidence.py --medium "m9_minimal*" --limit 1
    python3 scripts/propose_growth_evidence.py --media-term lb_broth --apply
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "normalized_yaml"
CACHE_DIR = REPO_ROOT / "references_cache"
OUT_DIR = REPO_ROOT / "workspace" / "reports" / "growth_evidence_proposals"

EUTILS_SEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
EUTILS_FETCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
DEFAULT_RATE = 3.0
KEYED_RATE = 10.0

UA = "CultureMech-growth-evidence-proposer/1.0"

SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z])")
GENOME_ACC_RE = re.compile(r"\b((?:GCF_|GCA_|SAMN)\d+(?:\.\d+)?)\b")
BINOMIAL_RE = re.compile(r"\b([A-Z][a-z]+)\s+([a-z]+(?:[a-z\-]+)?)\b")
STRAIN_RE = re.compile(r"\b(?:strain|str\.?)\s+([A-Z0-9][A-Za-z0-9\-]{1,15})\b", re.IGNORECASE)
NUMERIC_RE = r"(\d+(?:\.\d+)?)"

OD_RE = re.compile(rf"OD\s*600\s*(?:of|=|:|~|≈)?\s*{NUMERIC_RE}", re.IGNORECASE)
OD_GENERIC_RE = re.compile(rf"optical density\s*(?:at\s*600\s*nm)?\s*(?:of|=|:|~|≈)?\s*{NUMERIC_RE}", re.IGNORECASE)
DT_RE = re.compile(rf"doubling time\s*(?:of|=|:|~|≈)?\s*{NUMERIC_RE}\s*(min(?:utes?)?|h|hours?)", re.IGNORECASE)
TD_RE = re.compile(rf"\btd\s*(?:=|:|~|≈)?\s*{NUMERIC_RE}\s*(min(?:utes?)?|h|hours?)", re.IGNORECASE)
GROWTH_RATE_RE = re.compile(rf"(?:growth rate|μ|mu)\s*(?:of|=|:|~|≈)?\s*{NUMERIC_RE}\s*(?:h\^?-?1|/h|hr-1|per hour|h\^\(-1\))", re.IGNORECASE)


# ---------------- recipe loading ----------------

def iter_recipes(medium_glob: str | None,
                 media_terms: set[str] | None,
                 limit: int | None) -> list[Path]:
    """Yield MediaRecipe YAML paths matching the filters."""
    out: list[Path] = []
    if not DATA_DIR.is_dir():
        return out
    for path in sorted(DATA_DIR.rglob("*.yaml")):
        stem = path.stem
        if medium_glob and not fnmatch.fnmatch(stem, medium_glob):
            continue
        if media_terms is not None and stem not in media_terms:
            continue
        out.append(path)
        if limit is not None and len(out) >= limit:
            break
    return out


def load_recipe(path: Path) -> dict | None:
    try:
        with open(path) as f:
            y = yaml.safe_load(f) or {}
    except Exception as e:
        print(f"  load error {path}: {e}", file=sys.stderr)
        return None
    return y if isinstance(y, dict) else None


# ---------------- PubMed I/O ----------------

def esearch(query: str, retmax: int, api_key: str | None) -> list[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": str(retmax),
        "retmode": "json",
        "sort": "relevance",
    }
    if api_key:
        params["api_key"] = api_key
    url = f"{EUTILS_SEARCH}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read().decode("utf-8")
    except Exception as e:
        print(f"  esearch error: {e}", file=sys.stderr)
        return []
    try:
        j = json.loads(data)
        return j["esearchresult"]["idlist"]
    except Exception:
        return []


def cache_path(pmid: str) -> Path:
    return CACHE_DIR / f"PMID_{pmid}.md"


def fetch_pubmed_xml(pmid: str, api_key: str | None) -> str:
    params = {"db": "pubmed", "id": pmid, "retmode": "xml", "rettype": "abstract"}
    if api_key:
        params["api_key"] = api_key
    url = f"{EUTILS_FETCH}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def parse_abstract(xml_text: str) -> dict:
    try:
        root = ET.fromstring(xml_text)
    except ET.ParseError:
        return {"title": "", "abstract": "", "year": ""}
    article = root.find(".//PubmedArticle/MedlineCitation/Article")
    if article is None:
        return {"title": "", "abstract": "", "year": ""}
    title_el = article.find("ArticleTitle")
    title = "".join(title_el.itertext()).strip() if title_el is not None else ""
    year_el = article.find("Journal/JournalIssue/PubDate/Year")
    year = year_el.text.strip() if year_el is not None and year_el.text else ""
    parts: list[str] = []
    for ab in article.findall("Abstract/AbstractText"):
        label = ab.attrib.get("Label", "")
        text = "".join(ab.itertext()).strip()
        parts.append(f"**{label}:** {text}" if label else text)
    return {"title": title, "year": year, "abstract": "\n\n".join(parts)}


def write_abstract_md(pmid: str, data: dict) -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    md = [f"# PMID:{pmid}", ""]
    if data.get("title"):
        md.append(f"**Title:** {data['title']}")
    if data.get("year"):
        md.append(f"**Year:** {data['year']}")
    md.append("")
    md.append("## Abstract")
    md.append("")
    md.append(data.get("abstract") or "*(No abstract)*")
    md.append("")
    cache_path(pmid).write_text("\n".join(md))


def load_cached_abstract(pmid: str) -> dict:
    cp = cache_path(pmid)
    if not cp.exists():
        return {"title": "", "year": "", "abstract": ""}
    md = cp.read_text()
    m_title = re.search(r"\*\*Title:\*\*\s*(.+)", md)
    m_year = re.search(r"\*\*Year:\*\*\s*(\d{4})", md)
    abstract = md.split("## Abstract\n\n", 1)[-1].strip() if "## Abstract" in md else ""
    return {
        "title": m_title.group(1).strip() if m_title else "",
        "year": m_year.group(1) if m_year else "",
        "abstract": abstract,
    }


# ---------------- query construction ----------------

def build_queries(medium_name: str, organisms: list[dict]) -> list[str]:
    queries: list[str] = []
    medium_q = medium_name.replace("_", " ")
    if organisms:
        for o in organisms:
            term = (o.get("preferred_term") or "").strip()
            if not term:
                continue
            queries.append(f'("{term}"[Title/Abstract]) AND ("{medium_q}"[All Fields] OR culture[All Fields] OR growth[All Fields])')
    else:
        for tail in ("growth", "OD600", "doubling time", "cultivation"):
            queries.append(f'"{medium_q}"[All Fields] AND {tail}[All Fields]')
    return queries


# ---------------- snippet + extraction ----------------

def split_sentences(text: str) -> list[str]:
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return []
    return [s.strip() for s in SENTENCE_SPLIT.split(text) if s.strip()]


def extract_genomes(text: str) -> list[str]:
    return sorted(set(GENOME_ACC_RE.findall(text or "")))


def extract_organisms(text: str, max_n: int = 10) -> list[str]:
    """Heuristic binomial extraction; deduped, capped."""
    seen: list[str] = []
    for m in BINOMIAL_RE.finditer(text or ""):
        bi = f"{m.group(1)} {m.group(2)}"
        if bi not in seen:
            seen.append(bi)
            if len(seen) >= max_n:
                break
    return seen


def extract_strains(text: str) -> list[str]:
    return sorted(set(m.group(1) for m in STRAIN_RE.finditer(text or "")))


def extract_growth_metrics(text: str) -> dict:
    """Return possibly-empty dict of the metrics found, with regex match
    spans suitable for later snippet selection."""
    m: dict = {}
    if (mm := OD_RE.search(text or "")) or (mm := OD_GENERIC_RE.search(text or "")):
        try:
            m["max_od600"] = float(mm.group(1))
        except (ValueError, IndexError):
            pass
    if (mm := DT_RE.search(text or "")) or (mm := TD_RE.search(text or "")):
        try:
            val = float(mm.group(1))
            unit = mm.group(2).lower()
            if unit.startswith("h"):
                val *= 60.0
            m["doubling_time_minutes"] = val
        except (ValueError, IndexError):
            pass
    if (mm := GROWTH_RATE_RE.search(text or "")):
        try:
            m["growth_rate_per_hour"] = float(mm.group(1))
        except (ValueError, IndexError):
            pass
    return m


def find_snippet_for(text: str, needle: str) -> str | None:
    if not text or not needle:
        return None
    needle_l = needle.lower()
    for s in split_sentences(text):
        if needle_l in s.lower():
            return s[:500]
    return None


# ---------------- per-recipe proposal ----------------

def propose_for_recipe(recipe: dict, recipe_path: Path,
                       retmax: int, api_key: str | None,
                       rate: float) -> dict:
    medium_name = recipe.get("name") or recipe_path.stem
    medium_id = recipe.get("id") or f"path:{recipe_path.stem}"
    organisms = recipe.get("target_organisms") or []
    queries = build_queries(medium_name, organisms)

    candidates: list[dict] = []
    seen_pmids: set[str] = set()

    for q in queries:
        pmids = esearch(q, retmax, api_key)
        time.sleep(1.0 / rate)
        for pmid in pmids:
            if pmid in seen_pmids:
                continue
            seen_pmids.add(pmid)
            cp = cache_path(pmid)
            if cp.exists():
                data = load_cached_abstract(pmid)
            else:
                try:
                    xml = fetch_pubmed_xml(pmid, api_key)
                except urllib.error.HTTPError as e:
                    print(f"  PMID {pmid}: HTTP {e.code}", file=sys.stderr)
                    continue
                except Exception as e:
                    print(f"  PMID {pmid}: {type(e).__name__}", file=sys.stderr)
                    continue
                data = parse_abstract(xml)
                write_abstract_md(pmid, data)
                time.sleep(1.0 / rate)

            abstract = data.get("abstract") or ""
            metrics = extract_growth_metrics(abstract)
            genomes = extract_genomes(abstract)
            organisms_in_abs = extract_organisms(abstract)
            strains = extract_strains(abstract)

            if not (metrics or genomes or organisms_in_abs):
                continue

            metric_snippet: str | None = None
            for needle in ("OD600", "doubling time", "growth rate", "optical density"):
                metric_snippet = find_snippet_for(abstract, needle)
                if metric_snippet:
                    break

            candidates.append({
                "pmid": pmid,
                "title": data.get("title", ""),
                "year": data.get("year", ""),
                "query": q,
                "extracted": {
                    "organisms": organisms_in_abs,
                    "strains": strains,
                    "genome_assembly_ids": genomes,
                    "growth_metrics": metrics,
                },
                "snippet": metric_snippet or "",
                "supports": "REVIEW",
            })

    return {
        "medium_id": medium_id,
        "medium_name": medium_name,
        "recipe_path": str(recipe_path.relative_to(REPO_ROOT)),
        "queries": queries,
        "candidates": candidates,
    }


# ---------------- driver ----------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--medium", type=str, default=None,
                    help="filename glob filter (matches the YAML stem, e.g. 'lb_broth*')")
    ap.add_argument("--media-term", type=str, default=None,
                    help="comma-separated set of YAML stems")
    ap.add_argument("--limit", type=int, default=None,
                    help="cap how many recipes to process")
    ap.add_argument("--retmax", type=int, default=3,
                    help="max abstracts per query (default 3)")
    ap.add_argument("--rate", type=float, default=None,
                    help="req/s (default 3, or 10 with NCBI_API_KEY)")
    ap.add_argument("--apply", action="store_true",
                    help="write proposal YAMLs (default: dry-run)")
    args = ap.parse_args()

    api_key = os.environ.get("NCBI_API_KEY")
    rate = args.rate or (KEYED_RATE if api_key else DEFAULT_RATE)
    media_terms = (set(t.strip() for t in args.media_term.split(",") if t.strip())
                   if args.media_term else None)

    recipes = iter_recipes(args.medium, media_terms, args.limit)
    if not recipes:
        print("No recipes matched the filter.")
        return 1
    print(f"Recipes to process: {len(recipes)}")
    print(f"Mode: {'APPLY (writing proposals)' if args.apply else 'DRY-RUN (no files written)'}")

    if args.apply:
        OUT_DIR.mkdir(parents=True, exist_ok=True)

    n_total_candidates = 0
    n_with_metrics = 0
    n_with_genomes = 0
    written: list[Path] = []

    for i, p in enumerate(recipes, 1):
        recipe = load_recipe(p)
        if not recipe:
            continue
        print(f"[{i}/{len(recipes)}] {p.stem}")
        proposal = propose_for_recipe(recipe, p, args.retmax, api_key, rate)
        n_cand = len(proposal["candidates"])
        n_total_candidates += n_cand
        for c in proposal["candidates"]:
            if c["extracted"]["growth_metrics"]:
                n_with_metrics += 1
            if c["extracted"]["genome_assembly_ids"]:
                n_with_genomes += 1
        print(f"  candidates: {n_cand}")

        if args.apply and n_cand > 0:
            out_path = OUT_DIR / f"{p.stem}.yaml"
            with open(out_path, "w") as f:
                yaml.safe_dump(proposal, f, sort_keys=False, allow_unicode=True)
            written.append(out_path)
            print(f"  wrote {out_path.relative_to(REPO_ROOT)}")

    print()
    print(f"Recipes processed: {len(recipes)}")
    print(f"Total candidates: {n_total_candidates}")
    print(f"  with growth_metrics: {n_with_metrics}")
    print(f"  with genome_assembly_ids: {n_with_genomes}")
    if args.apply:
        print(f"Proposal files written: {len(written)}")
    else:
        print("(dry-run — no files written; pass --apply to write)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
