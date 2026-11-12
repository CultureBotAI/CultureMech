#!/usr/bin/env python3
"""Legal full-text access ladder for CultureMech curation (no gray-area sources).

Given a PMID or DOI, tries — in order of legality + cost — to locate an
openly/legally accessible full text, and if none is reachable, drafts an
author-request email. Routes (all legal; Sci-Hub etc. deliberately excluded):

  1. Local Zotero PDF        — local library (`$ZOTERO_DATA_DIR/zotero.sqlite` + `storage/`).
  2. Europe PMC OA full text — free, anonymous; JATS `fullTextXML` for the PMCID.
  3. OpenAlex OA location    — free, anonymous; OurResearch green/gold/hybrid OA index.
  4. bioRxiv / medRxiv       — free, anonymous; preprint full-text PDF for 10.1101 / 10.64898.
  5. DOE OSTI.gov            — free, anonymous; DOE/LBNL full-text technical reports & accepted MSS.
  6. LBNL Publisher TDM APIs — institutional full-text XML/PDF when API keys are set in env:
                               `$ELSEVIER_API_KEY` (10.1016/*),
                               `$SPRINGER_API_KEY` (10.1007/*, 10.1038/*, 10.1186/*),
                               `$WILEY_TDM_TOKEN`  (10.1002/*, 10.1111/*).
  7. CORE full text          — free for public-research orgs; needs `$CORE_API_KEY`.
  8. Author-request draft    — corresponding author + a templated email asking
                               for the Methods/cultivation section (legal, often effective).

All external API requests run anonymously without disclosing any user email
address in query parameters or `User-Agent` headers.

Usage:
    uv run python scripts/fulltext_access.py --pmid 41825563
    uv run python scripts/fulltext_access.py --doi 10.1016/j.biortech.2026.134417
"""

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sqlite3
import sys
import urllib.parse
import urllib.request
from contextlib import closing
from pathlib import Path

UA = {"User-Agent": "CultureMech-fulltext/1.0"}

DOI_RESOLVER_RE = re.compile(r"https?://(dx\.)?doi\.org/", re.IGNORECASE)


def _get_json(url: str, headers: dict | None = None):
    if not url.startswith("https://"):  # only fixed https API hosts are queried
        return None
    hdr = {**UA, **(headers or {})}
    req = urllib.request.Request(url, headers=hdr)  # noqa: S310
    try:
        with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310
            return json.load(r)
    except Exception:
        return None


def _get_text_prefix(url: str, headers: dict | None = None, max_bytes: int = 32768) -> str | None:
    if not url.startswith("https://"):
        return None
    hdr = {**UA, **(headers or {})}
    req = urllib.request.Request(url, headers=hdr)  # noqa: S310
    try:
        with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310
            if getattr(r, "status", 200) != 200:
                return None
            return r.read(max_bytes).decode("utf-8", errors="ignore")
    except Exception:
        return None


def _probe_binary_ok(url: str, headers: dict | None = None, min_bytes: int = 1024) -> bool:
    if not url.startswith("https://"):
        return False
    hdr = {**UA, **(headers or {})}
    req = urllib.request.Request(url, headers=hdr)  # noqa: S310
    try:
        with urllib.request.urlopen(req, timeout=30) as r:  # noqa: S310
            if getattr(r, "status", 200) != 200:
                return False
            chunk = r.read(min_bytes)
            return len(chunk) >= min_bytes
    except Exception:
        return False


def _clean_doi(doi: str | None) -> str | None:
    if not doi:
        return None
    cleaned = doi.strip()
    for prefix in ("https://doi.org/", "http://doi.org/", "https://dx.doi.org/", "doi:", "DOI:"):
        if cleaned.startswith(prefix):
            cleaned = cleaned[len(prefix) :].strip()
    return cleaned or None


def epmc_core(pmid: str | None, doi: str | None) -> dict:
    """Europe PMC core record: pmcid, OA status, DOI/PMID, title, corresponding author."""
    if pmid:
        q = f"EXT_ID:{pmid} AND SRC:MED"
    elif doi:
        q = f'DOI:"{doi}"'
    else:
        return {}
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode(
        {"query": q, "format": "json", "resultType": "core", "pageSize": "1"}
    )
    d = _get_json(url) or {}
    r = (d.get("resultList", {}).get("result") or [{}])[0]
    return r


def crossref_meta(doi: str | None) -> dict:
    """Title + author string from CrossRef, for records not in Europe PMC (e.g. DOI-only)."""
    if not doi:
        return {}
    d = _get_json(f"https://api.crossref.org/works/{urllib.parse.quote(doi)}")
    m = (d or {}).get("message", {})
    if not m:
        return {}
    authors = ", ".join(
        " ".join(x for x in (a.get("given"), a.get("family")) if x) for a in m.get("author", [])[:6]
    )
    return {"title": (m.get("title") or [""])[0], "authorString": authors}


def try_zotero_local(pmid: str | None = None, doi: str | None = None) -> str | None:
    """Check local Zotero SQLite + storage directory for an already-synced PDF attachment."""
    clean_doi = _clean_doi(doi)
    clean_pmid = (pmid or "").strip()
    if not clean_doi and not clean_pmid:
        return None

    zotero_env = os.environ.get("ZOTERO_DATA_DIR", "").strip()
    if not zotero_env:
        return None
    zotero_dir = Path(zotero_env)
    db_path = zotero_dir / "zotero.sqlite"
    storage_dir = zotero_dir / "storage"
    if not db_path.is_file() or not storage_dir.is_dir():
        return None

    parent_ids: set[int] = set()
    try:
        uri = f"file:{db_path}?mode=ro&immutable=1"
        with closing(sqlite3.connect(uri, uri=True, timeout=5)) as conn:
            cur = conn.cursor()
            if clean_doi:
                low_doi = clean_doi.lower()
                cur.execute(
                    """
                    SELECT id.itemID
                    FROM itemData id
                    JOIN fields f ON id.fieldID = f.fieldID
                    JOIN itemDataValues v ON id.valueID = v.valueID
                    WHERE f.fieldName = 'DOI'
                      AND LOWER(TRIM(v.value)) IN (?, ?, ?)
                    """,
                    (low_doi, f"https://doi.org/{low_doi}", f"doi:{low_doi}"),
                )
                parent_ids.update(row[0] for row in cur.fetchall())

            if clean_pmid and not parent_ids:
                cur.execute(
                    """
                    SELECT id.itemID
                    FROM itemData id
                    JOIN fields f ON id.fieldID = f.fieldID
                    JOIN itemDataValues v ON id.valueID = v.valueID
                    WHERE f.fieldName = 'extra'
                      AND v.value LIKE ?
                    """,
                    (f"%PMID: {clean_pmid}%",),
                )
                parent_ids.update(row[0] for row in cur.fetchall())

            for parent_id in sorted(parent_ids):
                cur.execute(
                    """
                    SELECT i.key, ia.path
                    FROM itemAttachments ia
                    JOIN items i ON ia.itemID = i.itemID
                    WHERE ia.parentItemID = ?
                      AND ia.contentType = 'application/pdf'
                    """,
                    (parent_id,),
                )
                for att_key, att_path in cur.fetchall():
                    if not att_key or not att_path:
                        continue
                    if att_path.startswith("storage:"):
                        rel_name = att_path[len("storage:") :]
                        pdf_file = storage_dir / att_key / rel_name
                    else:
                        pdf_file = Path(att_path)
                    if pdf_file.is_file():
                        return f"file://{pdf_file.resolve()}"
    except Exception:
        return None
    return None


def try_europepmc(rec: dict) -> str | None:
    pmcid = rec.get("pmcid")
    if pmcid and rec.get("isOpenAccess") == "Y":
        return f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
    return None


def _non_doi_oa_url(loc: dict) -> str | None:
    """Return the best non-DOI-resolver URL from an OpenAlex/Unpaywall location dict."""
    pdf_url = loc.get("pdf_url") or loc.get("url_for_pdf")
    landing_url = loc.get("landing_page_url") or loc.get("url")
    for candidate in (pdf_url, landing_url):
        if candidate and not DOI_RESOLVER_RE.match(candidate):
            return candidate
    return None


def try_openalex_oa(doi: str | None, pmid: str | None = None) -> str | None:
    """Anonymous OpenAlex OA location lookup (OurResearch's anonymous successor to Unpaywall)."""
    clean_doi = _clean_doi(doi)
    clean_pmid = (pmid or "").strip()
    if clean_doi:
        api_url = f"https://api.openalex.org/works/https://doi.org/{urllib.parse.quote(clean_doi)}"
    elif clean_pmid:
        api_url = f"https://api.openalex.org/works/pmid:{urllib.parse.quote(clean_pmid)}"
    else:
        return None

    d = _get_json(api_url)
    if not isinstance(d, dict):
        return None
    oa = d.get("open_access") or {}
    if not oa.get("is_oa"):
        return None

    best = d.get("best_oa_location") or {}
    hit = _non_doi_oa_url(best)
    if hit:
        return hit

    oa_url = oa.get("oa_url")
    if oa_url and not DOI_RESOLVER_RE.match(oa_url):
        return oa_url

    for loc in d.get("locations") or []:
        if isinstance(loc, dict) and loc.get("is_oa"):
            hit = _non_doi_oa_url(loc)
            if hit:
                return hit
    return None


def try_unpaywall(doi: str | None) -> str | None:
    """Backward-compatible wrapper that queries OpenAlex OA anonymously (no email disclosure)."""
    return try_openalex_oa(doi)


def try_biorxiv(doi: str | None) -> str | None:
    """Check bioRxiv / medRxiv API for 10.1101 / 10.64898 preprint full-text PDFs."""
    clean_doi = _clean_doi(doi)
    if not clean_doi or not clean_doi.startswith(("10.1101/", "10.64898/")):
        return None
    quoted = urllib.parse.quote(clean_doi, safe="/")
    for server in ("biorxiv", "medrxiv"):
        d = _get_json(f"https://api.biorxiv.org/details/{server}/{quoted}/na/json")
        collection = (d or {}).get("collection") or []
        if collection:
            return f"https://www.{server}.org/content/{clean_doi}.full.pdf"
    return None


def try_osti(doi: str | None, title: str | None = None) -> str | None:
    """Check DOE OSTI.gov API for publicly accessible full-text reports or accepted manuscripts."""
    clean_doi = _clean_doi(doi)
    if not clean_doi:
        return None
    url = "https://www.osti.gov/api/v1/records?" + urllib.parse.urlencode({"doi": clean_doi})
    records = _get_json(url, headers={"Accept": "application/json"})
    if not isinstance(records, list):
        return None
    for rec in records:
        if not isinstance(rec, dict):
            continue
        for link in rec.get("links") or []:
            if isinstance(link, dict) and link.get("rel") == "fulltext" and link.get("href"):
                return link["href"]
    return None


def try_elsevier_tdm(doi: str | None) -> str | None:
    """Check Elsevier Article Retrieval API when $ELSEVIER_API_KEY is set."""
    key = os.environ.get("ELSEVIER_API_KEY", "").strip()
    clean_doi = _clean_doi(doi)
    if not key or not clean_doi or not clean_doi.startswith("10.1016/"):
        return None
    url = (
        f"https://api.elsevier.com/content/article/doi/"
        f"{urllib.parse.quote(clean_doi, safe='/')}?httpAccept=text/xml"
    )
    headers = {"X-ELS-APIKey": key, "Accept": "text/xml"}
    inst_token = os.environ.get("ELSEVIER_INST_TOKEN", "").strip()
    if inst_token:
        headers["X-ELS-Insttoken"] = inst_token
    xml_prefix = _get_text_prefix(url, headers=headers)
    if xml_prefix and any(tag in xml_prefix for tag in ("<body", "<ce:sections", "<rawtext>")):
        return url
    return None


def try_springer_tdm(doi: str | None) -> str | None:
    """Check Springer Nature JATS API when $SPRINGER_API_KEY is set (never leaks key in URL)."""
    key = os.environ.get("SPRINGER_API_KEY", "").strip()
    clean_doi = _clean_doi(doi)
    if not key or not clean_doi or not clean_doi.startswith(("10.1007/", "10.1038/", "10.1186/")):
        return None
    display_url = "https://api.springernature.com/openaccess/jats?" + urllib.parse.urlencode(
        {"q": f"doi:{clean_doi}"}
    )
    probe_url = display_url + "&" + urllib.parse.urlencode({"api_key": key})
    xml_prefix = _get_text_prefix(probe_url)
    if xml_prefix and "<body" in xml_prefix:
        return display_url
    return None


def try_wiley_tdm(doi: str | None) -> str | None:
    """Check Wiley TDM API v1 when $WILEY_TDM_TOKEN is set."""
    token = os.environ.get("WILEY_TDM_TOKEN", "").strip()
    clean_doi = _clean_doi(doi)
    if not token or not clean_doi or not clean_doi.startswith(("10.1002/", "10.1111/")):
        return None
    url = "https://api.wiley.com/onlinelibrary/tdm/v1/articles/" + urllib.parse.quote(
        clean_doi, safe=""
    )
    if _probe_binary_ok(url, headers={"Wiley-TDM-Client-Token": token}):
        return url
    return None


def try_core(doi: str | None, title: str | None) -> str | None:
    key = os.environ.get("CORE_API_KEY")
    if not key or not (doi or title):
        return None
    q = f'doi:"{doi}"' if doi else f'title:"{title}"'
    url = "https://api.core.ac.uk/v3/search/works?" + urllib.parse.urlencode({"q": q, "limit": "1"})
    d = _get_json(url, headers={"Authorization": f"Bearer {key}"})
    for w in (d or {}).get("results", []) or []:
        for link in w.get("links", []) or []:
            if link.get("type") in ("download", "reader") and link.get("url"):
                return link["url"]
        if w.get("downloadUrl"):
            return w["downloadUrl"]
    return None


def try_acs_figshare_si(doi: str | None) -> str | None:
    """Resolve open-access ACS Supporting Information on Figshare (10.1021/<suffix>.s001)."""
    clean_doi = _clean_doi(doi)
    if not clean_doi or not clean_doi.startswith("10.1021/"):
        return None
    base_doi = re.sub(r"\.s\d{3}$", "", clean_doi, flags=re.IGNORECASE)
    for suffix in (".s001", ".s002"):
        si_doi = f"{base_doi}{suffix}"
        handle_url = "https://doi.org/api/handles/" + urllib.parse.quote(si_doi, safe="/")
        handle_data = _get_json(handle_url)
        if not isinstance(handle_data, dict) or handle_data.get("responseCode") != 1:
            continue
        target_url = None
        for val in handle_data.get("values") or []:
            if isinstance(val, dict) and val.get("type") == "URL":
                data_val = (val.get("data") or {}).get("value")
                if isinstance(data_val, str) and data_val.startswith("https://"):
                    target_url = data_val
                    break
        if not target_url:
            continue
        m = re.search(r"figshare\.com/articles/[^?#]+/(\d+)(?:[/?#]|$)", target_url, re.I)
        if m:
            article_id = m.group(1)
            meta = _get_json(f"https://api.figshare.com/v2/articles/{article_id}")
            if isinstance(meta, dict):
                files = [f for f in (meta.get("files") or []) if isinstance(f, dict)]
                for f in files:
                    dl = f.get("download_url")
                    name = str(f.get("name") or "").lower()
                    if isinstance(dl, str) and dl.startswith("https://") and name.endswith(".pdf"):
                        return dl
                for f in files:
                    dl = f.get("download_url")
                    if isinstance(dl, str) and dl.startswith("https://"):
                        return dl
        return target_url
    return None


def access_ladder(
    rec: dict,
    doi: str | None,
    title: str | None,
    pmid: str | None = None,
) -> tuple[str, str | None]:
    """Return (method, url) for the first legal full-text hit, or ('none', None)."""
    resolved_pmid = pmid or rec.get("pmid")
    resolved_doi = _clean_doi(doi or rec.get("doi"))
    for method, fn in (
        ("zotero_local", lambda: try_zotero_local(resolved_pmid, resolved_doi)),
        ("europepmc_oa", lambda: try_europepmc(rec)),
        ("openalex_oa", lambda: try_openalex_oa(resolved_doi, resolved_pmid)),
        ("biorxiv", lambda: try_biorxiv(resolved_doi)),
        ("osti_gov", lambda: try_osti(resolved_doi, title)),
        ("elsevier_tdm", lambda: try_elsevier_tdm(resolved_doi)),
        ("springer_tdm", lambda: try_springer_tdm(resolved_doi)),
        ("wiley_tdm", lambda: try_wiley_tdm(resolved_doi)),
        ("core", lambda: try_core(resolved_doi, title)),
        ("acs_figshare_si", lambda: try_acs_figshare_si(resolved_doi)),
    ):
        url = fn()
        if url:
            return method, url
    return "none", None


def fetch_to_staging(method: str, url: str, dest: Path) -> Path:
    """Download or copy a resolved full-text payload to a staging path outside references_cache/."""
    resolved = dest.resolve()
    if "references_cache" in resolved.parts:
        raise ValueError(
            "Refusing to stage fulltext_access output directly into references_cache/; "
            "stage into .temp/ or workspace/ and use verified cache helpers for OA text."
        )
    resolved.parent.mkdir(parents=True, exist_ok=True)

    if url.startswith("file://"):
        src_path = Path(urllib.parse.unquote(urllib.parse.urlparse(url).path))
        shutil.copy2(src_path, resolved)
        return resolved

    if not url.startswith("https://"):
        raise ValueError(f"Unsupported URL scheme for staging fetch: {url}")

    headers = dict(UA)
    fetch_url = url
    if method == "elsevier_tdm":
        key = os.environ.get("ELSEVIER_API_KEY", "").strip()
        if key:
            headers["X-ELS-APIKey"] = key
        headers["Accept"] = "text/xml"
        inst_token = os.environ.get("ELSEVIER_INST_TOKEN", "").strip()
        if inst_token:
            headers["X-ELS-Insttoken"] = inst_token
    elif method == "springer_tdm":
        key = os.environ.get("SPRINGER_API_KEY", "").strip()
        if key and "api_key=" not in fetch_url:
            sep = "&" if "?" in fetch_url else "?"
            fetch_url = f"{fetch_url}{sep}{urllib.parse.urlencode({'api_key': key})}"
    elif method == "wiley_tdm":
        token = os.environ.get("WILEY_TDM_TOKEN", "").strip()
        if token:
            headers["Wiley-TDM-Client-Token"] = token
    elif method == "core":
        key = os.environ.get("CORE_API_KEY", "").strip()
        if key:
            headers["Authorization"] = f"Bearer {key}"

    req = urllib.request.Request(fetch_url, headers=headers)  # noqa: S310
    with urllib.request.urlopen(req, timeout=60) as r:  # noqa: S310
        payload = r.read()
    if not payload:
        raise RuntimeError(f"Empty payload returned from {method} ({url})")
    resolved.write_bytes(payload)
    return resolved


def author_request_draft(rec: dict, doi: str | None) -> str:
    title = re.sub(r"<[^>]+>", "", rec.get("title", "") or "").rstrip(".")
    authors = rec.get("authorString", "") or "the corresponding author"
    ref = f"doi:{doi}" if doi else f"PMID:{rec.get('pmid', '?')}"
    return (
        f"To: <corresponding author of: {authors}>\n"
        f"Subject: Request for Methods details — {title[:70]}\n\n"
        f"Dear Author,\n\n"
        f"I am curating an open, public microbial cultivation-media knowledge base and would like to "
        f'cite your paper "{title}" ({ref}). The abstract does not include the cultivation / '
        f"Methods details I need (medium formulation, concentrations, pH, temperature, atmosphere, "
        f"and strain identities). Could you share the relevant Methods/supplementary text, "
        f"or a PDF? The extracted, source-attributed data would be published openly with full "
        f"citation to your work.\n\nThank you,\nCultureMech curation team\n"
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--pmid")
    g.add_argument("--doi")
    p.add_argument("--title", help="fallback for CORE title search")
    p.add_argument(
        "--fetch-to",
        help="stage the resolved full text to this path (outside references_cache/) using method auth headers",
    )
    args = p.parse_args(argv)

    rec = epmc_core(args.pmid, args.doi)
    doi = args.doi or rec.get("doi")
    if not rec.get("title"):  # DOI-only / not in Europe PMC — fall back to CrossRef
        rec = {**crossref_meta(doi), **rec}
    title = args.title or re.sub(r"<[^>]+>", "", rec.get("title", "") or "")

    method, url = access_ladder(rec, doi, title, pmid=args.pmid)
    if url:
        print(f"ACCESS\t{method}\t{url}")
        if args.fetch_to:
            saved = fetch_to_staging(method, url, Path(args.fetch_to))
            print(f"SAVED\t{method}\t{saved}")
        return 0

    print(
        "NO_LEGAL_OA\t(paywalled; no full text via Zotero / Europe PMC / OpenAlex / OSTI / TDM / CORE)",
        file=sys.stderr,
    )
    missing_keys = [
        k
        for k in (
            "ZOTERO_DATA_DIR",
            "ELSEVIER_API_KEY",
            "SPRINGER_API_KEY",
            "WILEY_TDM_TOKEN",
            "CORE_API_KEY",
        )
        if not os.environ.get(k)
    ]
    if missing_keys:
        print(
            f"  (optional API keys not set: {', '.join(missing_keys)})",
            file=sys.stderr,
        )
    print("\n--- author-request draft ---")
    print(author_request_draft(rec, doi))
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
