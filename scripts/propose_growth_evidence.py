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


# ---------------- perturbation / conditional-growth patterns ----------------
#
# These regexes drive the v2-schema extraction (PerturbationContext,
# StrainModification, NutrientOverride, growth_mode, is_max_attainment)
# added by commit 0a81ef48c. The extractor does NOT auto-resolve
# ontology CURIEs — the curator supplies those at review time. We only
# surface descriptors, types, and quantitative levels when extractable.

# StrainModification — knockouts, deletions, insertions, mutants, adapted strains.
_STRAIN_MOD_PATTERNS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\b(?P<target>[A-Za-z][\w-]{1,30})\s*[:]{2}\s*Tn\d+\b"),
     "INSERTION"),
    (re.compile(r"\b(?P<target>[A-Za-z][\w-]{1,30})\s*[:]{2}knockout\b", re.IGNORECASE),
     "KNOCKOUT"),
    (re.compile(r"\bknockout(?:\s+(?:strain|mutant))?\s+(?:of\s+)?(?P<target>[A-Za-z][\w-]{1,30})\b", re.IGNORECASE),
     "KNOCKOUT"),
    (re.compile(r"\b(?P<target>[A-Za-z][\w-]{1,30})\s+knockout\b", re.IGNORECASE),
     "KNOCKOUT"),
    (re.compile(r"\b(?:Δ|delta)\s*(?P<target>[A-Za-z][\w-]{1,30})\b", re.IGNORECASE),
     "DELETION"),
    (re.compile(r"\bdeletion\s+(?:strain|mutant)?\s*(?:of\s+)?(?P<target>[A-Za-z][\w-]{1,30})\b", re.IGNORECASE),
     "DELETION"),
    (re.compile(r"\b(?P<target>[A-Za-z][\w-]{1,30})\s+deletion\b", re.IGNORECASE),
     "DELETION"),
    (re.compile(r"\b(?P<target>[A-Za-z][\w-]{1,30})-deficient\b", re.IGNORECASE),
     "KNOCKOUT"),
    (re.compile(r"\bserially\s+adapted\s+for\s+(?:growth\s+on\s+)?(?P<target>[A-Za-z][\w\-\s]{2,40})\b", re.IGNORECASE),
     "ADAPTATION"),
    (re.compile(r"\b(?:experimentally\s+)?adapted\s+(?:for|to)\s+(?:growth\s+on\s+)?(?P<target>[A-Za-z][\w\-\s]{2,40})\b", re.IGNORECASE),
     "ADAPTATION"),
    (re.compile(r"\bselected\s+for\s+(?P<target>[A-Za-z][\w\-\s]{2,40})\b", re.IGNORECASE),
     "SELECTION"),
    (re.compile(r"\bmutant\s+strain(?:\s+(?:of|in)\s+)?(?P<target>[A-Za-z][\w-]{1,30})?\b", re.IGNORECASE),
     "POINT_MUTATION"),
]

# Chemical-stress detection — heavy metals, oxidative agents, antibiotics.
# Heavy-metal pattern: matches "<agent> ... <level> <unit>" within ~40
# chars. Levels often appear before the agent ("addition of 10 mg L-1
# Cr(VI)") so we anchor on either order. Units accept the common
# formatter variants used in PubMed abstracts: "mg/L", "mg L-1",
# "mg·L-1", "mM", "µM", etc.
_LEVEL_UNIT = r"(?P<level>\d+(?:\.\d+)?)\s*(?P<unit>mg\s*[·\s/]?\s*L\s*-?\s*1|mg\s*/\s*L|mg/L|mM|µM|uM|μM|µg/mL|ug/mL|nM|%)"
_METAL_AGENT = r"(?P<agent>Cr\(VI\)|Cr6\+|Cr\(III\)|Cd\d*\+?|Pb\d*\+?|Hg\d*\+?|As\d*\+?|Ni\d*\+?|Cu\d*\+?|Zn\d*\+?)"
_HEAVY_METAL_RE = re.compile(
    rf"{_METAL_AGENT}(?:\s+at\s+|\s+of\s+|\s+\(|\s+){_LEVEL_UNIT}",
    re.IGNORECASE,
)
# Reverse-order ("10 mg L-1 Cr(VI)") — common in chemistry abstracts.
_HEAVY_METAL_REV_RE = re.compile(
    rf"{_LEVEL_UNIT}\s+(?:of\s+)?{_METAL_AGENT}",
    re.IGNORECASE,
)
# Even without a numeric level — flag heavy-metal mention.
_HEAVY_METAL_LITE_RE = re.compile(
    r"\b(?P<agent>Cr\(VI\)|Cr6\+|Cr\(III\)|Cd2\+|Pb2\+|Hg2\+|As\d+\+|chromate|chromium|cadmium|mercury|arsenic|nickel)\b",
    re.IGNORECASE,
)
_OXIDATIVE_RE = re.compile(
    r"\b(?P<agent>H2O2|hydrogen\s+peroxide|peroxide|paraquat|menadione|oxidative\s+stress)\b",
    re.IGNORECASE,
)
_ANTIBIOTIC_RE = re.compile(
    r"\b(?P<agent>ampicillin|kanamycin|tetracycline|chloramphenicol|streptomycin|rifampicin|gentamicin|spectinomycin)"
    r"(?:\s+at\s+(?P<level>\d+(?:\.\d+)?)\s*(?P<unit>mg/mL|µg/mL|ug/mL|µg·mL-1|mM|µM|uM))?",
    re.IGNORECASE,
)

# Temperature-stress — explicit cold-shock / heat-stress / "at N°C" phrasing.
_TEMP_STRESS_AFFIRMATIVES = (
    "cold shock", "cold-shock", "cold stress", "cold growth",
    "heat shock", "heat-shock", "heat stress",
    "low temperature", "elevated temperature", "temperature shock",
)
_TEMP_RE = re.compile(
    rf"\bat\s+{NUMERIC_RE}\s*(?:°\s*C|degrees?\s*C|°?C)\b",
    re.IGNORECASE,
)
_TEMP_AND_GROWTH_RE = re.compile(
    rf"\b(?:grow|grew|growth|cultivation|cultivated|incubated)\s+(?:at\s+)?{NUMERIC_RE}\s*(?:°\s*C|degrees?\s*C|°?C)\b",
    re.IGNORECASE,
)

# Nutrient overrides — "sole carbon source", "as the only nitrogen source", etc.
_SOLE_SOURCE_RE = re.compile(
    r"(?:^|\b)(?P<source>[A-Za-z][\w\-\(\),]{1,40}(?:\s+[\w\-\(\),]{1,40}){0,3})"
    r"\s+(?:when\s+used\s+)?as\s+(?:the\s+)?(?:sole|only)\s+source\s+of\s+(?P<role>nitrogen|carbon|sulfur|phosphate|phosphorus|electron)\b",
    re.IGNORECASE,
)
_SOLE_SOURCE_ALT_RE = re.compile(
    r"\b(?:sole|only)\s+(?P<role>nitrogen|carbon|sulfur|phosphate|phosphorus|electron)\s+(?:source|donor|acceptor)\s*[:\-]?\s*(?P<source>[A-Za-z][\w\-\(\),]{1,40}(?:\s+[\w\-\(\),]{1,40}){0,3})",
    re.IGNORECASE,
)
_WITH_SOURCE_RE = re.compile(
    r"\bwith\s+(?P<source>[A-Za-z][\w\-\(\),]{1,40}(?:\s+[\w\-\(\),]{1,40}){0,2})"
    r"\s+as\s+(?:the\s+)?(?:sole\s+)?(?P<role>carbon|nitrogen|sulfur|phosphate|phosphorus|electron)\s+source\b",
    re.IGNORECASE,
)

# Growth mode — chemostat / fed-batch / biofilm / continuous flow.
_GROWTH_MODE_PATTERNS: list[tuple[re.Pattern, str]] = [
    (re.compile(r"\bchemostat\b", re.IGNORECASE), "CHEMOSTAT"),
    (re.compile(r"\bturbidostat\b", re.IGNORECASE), "TURBIDOSTAT"),
    (re.compile(r"\bfed[\s-]batch\b", re.IGNORECASE), "FED_BATCH"),
    (re.compile(r"\bcontinuous(?:[\s-]flow)?\s+(?:culture|cultivation)\b", re.IGNORECASE), "CONTINUOUS_FLOW"),
    (re.compile(r"\bbiofilm\b", re.IGNORECASE), "BIOFILM"),
    (re.compile(r"\bbatch\s+(?:culture|growth|cultivation)\b", re.IGNORECASE), "BATCH"),
]

# Max-attainment affirmatives extending the OD-context ones to apply
# across all metric types. Used for is_max_attainment detection.
_MAX_ATTAINMENT_AFFIRMATIVES = (
    "up to", "maximum", "minimum doubling time", "fastest", "shortest",
    "exponential phase", "exponential growth",
    "optimum growth", "optimal growth", "highest", "max ",
)
_CONDITIONAL_MARKERS = (
    "during slow growth", "slow-growth",
    "lag phase", "stress", "deficient", "knockout", "mutant",
    "adapted", "limited", "limitation",
    "cold shock", "heat shock", "cold growth",
    "as sole source", "as the sole source", "as the only source",
    "as the sole carbon", "as the sole nitrogen",
    "chemostat", "fed-batch", "biofilm",
)


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


# Phrases that indicate the OD value is a setpoint (inoculum density,
# harvest density, induction OD, suspension prep) rather than a
# max-attained density. When any of these appear within ~80 chars
# before the OD match, skip the extraction — the curator would only
# reject these anyway, and surfacing them as candidates wastes the
# triage step's time.
_OD_SETPOINT_PRECEDENTS = (
    "diluted to", "diluted at", "adjusted to", "adjusted at",
    "resuspended to", "resuspended at", "suspended to", "suspended at",
    "harvested at", "harvested when", "collected at",
    "induced at", "induced with", "induction at",
    "inoculated at", "inoculated to",
    "prepared at", "prepared to",
    "spotted at",
    "starting at",
    "until reaching", "to reach an",
    "containing 10", "containing approximately",  # CFU/ml conversions
    "= 0.0", "= 0.1", "= 0.2", "= 0.3", "= 0.5",  # canonical inoculum levels
    "of 0.0", "of 0.1", "of 0.2", "of 0.3", "of 0.5",
)

_MAX_OD_AFFIRMATIVES = (
    "up to", "reached", "reaches", "grew to", "growth to",
    "stationary phase", "final od", "maximum od", "max od",
    "attained", "exponential phase",
)


def _is_max_od_context(text: str, span_start: int) -> bool:
    """True if the OD600 match looks like a max-attained-density
    claim, not a setpoint/inoculum density. Heuristic — checks ~80
    chars before the match for affirmative max-attained markers, and
    rejects when the immediate antecedent is a known inoculum/setpoint
    phrase."""
    window = (text or "")[max(0, span_start - 80): span_start].lower()
    if any(phrase in window for phrase in _OD_SETPOINT_PRECEDENTS):
        return False
    # If an affirmative max marker is present nearby, accept.
    if any(phrase in window for phrase in _MAX_OD_AFFIRMATIVES):
        return True
    # No clear signal either way — also check the trailing 60 chars
    # for max-affirmative phrases that follow the value (e.g. "an
    # OD600 of up to 10").
    tail = (text or "")[span_start: span_start + 80].lower()
    return any(phrase in tail for phrase in _MAX_OD_AFFIRMATIVES)


def extract_growth_metrics(text: str) -> dict:
    """Return possibly-empty dict of the metrics found, with regex match
    spans suitable for later snippet selection."""
    m: dict = {}
    od_match = OD_RE.search(text or "") or OD_GENERIC_RE.search(text or "")
    if od_match and _is_max_od_context(text or "", od_match.start()):
        try:
            m["max_od600"] = float(od_match.group(1))
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


# ---------------- v2: perturbation / conditional-growth extraction ----------------

def _normalize_role(raw: str) -> str:
    r = raw.strip().lower()
    return {
        "carbon": "CARBON_SOURCE",
        "nitrogen": "NITROGEN_SOURCE",
        "sulfur": "SULFUR_SOURCE",
        "phosphate": "PHOSPHATE_SOURCE",
        "phosphorus": "PHOSPHATE_SOURCE",
        "electron": "ELECTRON_DONOR",
    }.get(r, "OTHER")


def _dedup_dicts(items: list[dict]) -> list[dict]:
    """Stable dedup of small dicts by their JSON repr (fields are scalar)."""
    seen: set[str] = set()
    out: list[dict] = []
    for d in items:
        key = json.dumps(d, sort_keys=True, default=str)
        if key in seen:
            continue
        seen.add(key)
        out.append(d)
    return out


def extract_strain_modifications(text: str) -> list[dict]:
    """Return a list of StrainModification candidate dicts."""
    if not text:
        return []
    out: list[dict] = []
    seen_targets: set[tuple[str, str]] = set()
    for pat, mod_type in _STRAIN_MOD_PATTERNS:
        for m in pat.finditer(text):
            tgt = (m.groupdict().get("target") or "").strip()
            if not tgt or len(tgt) < 2:
                continue
            # Skip very generic words masquerading as targets.
            if tgt.lower() in {"the", "a", "an", "and", "for", "with", "of", "in",
                               "strain", "mutant", "growth", "study"}:
                continue
            key = (mod_type, tgt.lower())
            if key in seen_targets:
                continue
            seen_targets.add(key)
            entry: dict = {
                "modification_type": mod_type,
                "target": tgt,
            }
            if mod_type == "KNOCKOUT":
                entry["ontology_term"] = "NCIT:C120956"
            out.append(entry)
    return out


def extract_perturbations(text: str) -> list[dict]:
    """Return a list of PerturbationContext candidate dicts.

    Detects chemical stress (heavy metals, oxidative agents, antibiotics),
    temperature stress, and growth-phase markers. Numeric levels and
    units are extracted when adjacent to the agent name.
    """
    if not text:
        return []
    out: list[dict] = []

    # Chemical stress — heavy metals (with quantitative level).
    # Try both orderings: "<agent> at <level> <unit>" and the chemistry-
    # paper-common reverse "<level> <unit> <agent>".
    for pat in (_HEAVY_METAL_RE, _HEAVY_METAL_REV_RE):
        for m in pat.finditer(text):
            agent = m.group("agent").strip()
            level = m.group("level")
            unit = (m.group("unit") or "").strip()
            # Normalize "mg L-1", "mg·L-1", "mg L 1", "mg/L" → "mg/L"
            unit_norm = re.sub(r"\s+", "", unit)
            unit_norm = unit_norm.replace("·", "/").replace("L-1", "/L")
            unit_norm = unit_norm.replace("L1", "/L")
            unit_norm = re.sub(r"/+", "/", unit_norm).rstrip("/")
            if unit_norm.lower() == "mgl":
                unit_norm = "mg/L"
            descriptor = f"{agent} at {level} {unit_norm}".strip()
            entry = {
                "perturbation_type": "CHEMICAL_STRESS",
                "descriptor": descriptor,
                "target": agent,
            }
            try:
                entry["level"] = float(level)
            except (ValueError, TypeError):
                pass
            if unit_norm:
                entry["level_unit"] = unit_norm
            out.append(entry)

    # Lite heavy-metal mention (no quantitative level extractable)
    if not any(p.get("perturbation_type") == "CHEMICAL_STRESS" for p in out):
        m = _HEAVY_METAL_LITE_RE.search(text)
        if m:
            agent = m.group("agent").strip()
            out.append({
                "perturbation_type": "CHEMICAL_STRESS",
                "descriptor": f"{agent} stress",
                "target": agent,
            })

    # Oxidative stress
    for m in _OXIDATIVE_RE.finditer(text):
        agent = m.group("agent").strip()
        out.append({
            "perturbation_type": "OXIDATIVE_STRESS",
            "descriptor": agent,
            "target": agent,
        })
        break  # one is sufficient

    # Antibiotics — chemical-stress class
    for m in _ANTIBIOTIC_RE.finditer(text):
        agent = m.group("agent").strip()
        entry = {
            "perturbation_type": "CHEMICAL_STRESS",
            "descriptor": agent,
            "target": agent,
        }
        level = m.group("level")
        unit = (m.group("unit") or "").strip() if m.group("unit") else ""
        if level:
            try:
                entry["level"] = float(level)
            except ValueError:
                pass
            if unit:
                entry["level_unit"] = unit
        out.append(entry)
        break

    # Temperature stress — affirmative cold/heat-shock context, OR "at N°C"
    # paired with a growth/cultivation verb. We flag when:
    #   (a) an affirmative shock/stress phrase is present, OR
    #   (b) the abstract reports growth at a low temperature (≤10°C) or
    #       a high temperature (≥45°C) tied to a growth verb — these
    #       are non-default for typical mesophilic curated organisms.
    # Avoids tagging routine "incubated at 37°C" mentions.
    text_l = text.lower()
    has_temp_affirmative = any(p in text_l for p in _TEMP_STRESS_AFFIRMATIVES)
    temp_match = None
    descriptor_phrase = None
    if has_temp_affirmative:
        temp_match = _TEMP_AND_GROWTH_RE.search(text) or _TEMP_RE.search(text)
        if temp_match:
            descriptor_phrase = next((p for p in _TEMP_STRESS_AFFIRMATIVES
                                      if p in text_l), "temperature stress")
    else:
        # Implicit cold/heat — growth verb paired with extreme temp.
        for m in _TEMP_AND_GROWTH_RE.finditer(text):
            try:
                t = float(m.group(1))
            except ValueError:
                continue
            if t <= 10.0:
                temp_match = m
                descriptor_phrase = f"cold growth at {m.group(1)}°C"
                break
            if t >= 45.0:
                temp_match = m
                descriptor_phrase = f"thermophilic growth at {m.group(1)}°C"
                break

    if temp_match is not None and descriptor_phrase is not None:
        level = temp_match.group(1)
        entry: dict = {
            "perturbation_type": "TEMPERATURE_STRESS",
            "descriptor": descriptor_phrase if "°C" in descriptor_phrase
                          else f"{descriptor_phrase} at {level}°C",
            "target": "temperature",
            "level_unit": "°C",
        }
        try:
            entry["level"] = float(level)
        except ValueError:
            pass
        out.append(entry)

    # Growth-phase — slow-growth / lag-phase markers as conditional context.
    # We *don't* treat plain "stationary phase" as a perturbation: a
    # max-OD measurement reported at stationary phase is the standard
    # max-attainment claim. We only flag explicit slow-growth / lag-phase
    # qualifiers, which the curator triages have actually rejected as
    # conditional kinetic claims (PMID:21097629 etc).
    slow_phrases = (
        "during slow growth", "slow-growth phase", "slow growth phase",
        "lag phase",
    )
    if any(phrase in text_l for phrase in slow_phrases):
        descriptor_phrase = next((p for p in slow_phrases if p in text_l),
                                 "slow growth")
        out.append({
            "perturbation_type": "GROWTH_PHASE",
            "descriptor": descriptor_phrase,
            "target": "growth phase",
        })

    return _dedup_dicts(out)


def extract_nutrient_overrides(text: str) -> list[dict]:
    """Return a list of NutrientOverride candidate dicts."""
    if not text:
        return []
    out: list[dict] = []
    for pat in (_SOLE_SOURCE_RE, _SOLE_SOURCE_ALT_RE, _WITH_SOURCE_RE):
        for m in pat.finditer(text):
            role_raw = m.group("role")
            source = (m.group("source") or "").strip(" ,.;:-")
            if not source or len(source) < 2:
                continue
            # Trim trailing prepositions / articles
            source = re.sub(
                r"\s+(when\s+used|when|as|in|for|of|the|a|an)$",
                "", source, flags=re.IGNORECASE,
            ).strip(" ,.;:-")
            # Trim leading prepositions / articles (".on L-phenylalanine")
            source = re.sub(
                r"^(?:on|with|in|using|the|a|an)\s+",
                "", source, flags=re.IGNORECASE,
            ).strip(" ,.;:-")
            if not source or len(source) < 2:
                continue
            entry = {
                "role": _normalize_role(role_raw),
                "source": source,
                "is_sole_source": True,
            }
            out.append(entry)
    return _dedup_dicts(out)


def extract_growth_mode(text: str) -> str | None:
    """Return a GrowthModeEnum value or None.

    Priority: non-batch modes (CHEMOSTAT, TURBIDOSTAT, FED_BATCH,
    CONTINUOUS_FLOW, BIOFILM) win over BATCH when both are mentioned —
    a paper that explicitly contrasts batch vs chemostat is reporting
    on the more-specific mode.
    """
    if not text:
        return None
    found_batch = False
    for pat, mode in _GROWTH_MODE_PATTERNS:
        if pat.search(text):
            if mode == "BATCH":
                found_batch = True
                continue
            return mode
    return "BATCH" if found_batch else None


def detect_max_attainment(text: str,
                          perturbations: list[dict],
                          strain_mods: list[dict],
                          nutrient_overrides: list[dict],
                          growth_mode: str | None) -> bool | None:
    """Return True/False/None for is_max_attainment.

    Heuristic order (matches the schema-doc's intent):
      1. If any perturbation/conditional marker is present (perturbations,
         strain_mods, nutrient_overrides, or non-BATCH growth_mode), the
         metric is conditional — return False.
      2. Else if affirmative max-attainment language is present, return True.
      3. Else None (curator decides).
    """
    if perturbations or strain_mods or nutrient_overrides:
        return False
    if growth_mode and growth_mode != "BATCH":
        return False
    if not text:
        return None
    text_l = text.lower()
    if any(m in text_l for m in _CONDITIONAL_MARKERS):
        return False
    if any(p in text_l for p in _MAX_ATTAINMENT_AFFIRMATIVES):
        return True
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

            # v2 schema additions: perturbation / conditional-growth context.
            strain_modifications = extract_strain_modifications(abstract)
            perturbations = extract_perturbations(abstract)
            nutrient_overrides = extract_nutrient_overrides(abstract)
            growth_mode = extract_growth_mode(abstract)
            is_max_attainment = detect_max_attainment(
                abstract, perturbations, strain_modifications,
                nutrient_overrides, growth_mode,
            )

            if not (metrics or genomes or organisms_in_abs):
                continue

            metric_snippet: str | None = None
            for needle in ("OD600", "doubling time", "growth rate", "optical density"):
                metric_snippet = find_snippet_for(abstract, needle)
                if metric_snippet:
                    break

            extracted: dict = {
                "organisms": organisms_in_abs,
                "strains": strains,
                "genome_assembly_ids": genomes,
                "growth_metrics": metrics,
            }
            # Only emit v2 fields when populated — keeps proposal YAMLs
            # tidy for non-perturbed papers.
            if strain_modifications:
                extracted["strain_modifications"] = strain_modifications
            if perturbations:
                extracted["perturbations"] = perturbations
            if nutrient_overrides:
                extracted["nutrient_overrides"] = nutrient_overrides
            if growth_mode is not None:
                extracted["growth_mode"] = growth_mode
            if is_max_attainment is not None:
                extracted["is_max_attainment"] = is_max_attainment

            candidates.append({
                "pmid": pmid,
                "title": data.get("title", ""),
                "year": data.get("year", ""),
                "query": q,
                "extracted": extracted,
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
