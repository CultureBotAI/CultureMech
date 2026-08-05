#!/usr/bin/env python3
"""Scrape JCM growth-medium recipes from the RIKEN JCM GRMD database and
emit CultureMech-normalized YAML records.

Background
----------
CultureMech's existing JCM media were never scraped from JCM directly: they
arrived as derivative copies via MediaDive (``mediadive.medium:J<GRMD>``) and
the TOGO medium database (``TOGO M####``). Both aggregator snapshots lag the
live JCM catalogue, so recently-added JCM media (high GRMD numbers) are absent.
This importer talks to JCM directly so the gap can be closed and kept current.

Source
------
Each medium has a page at::

    https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=<N>

The CGI returns HTTP 200 for *every* number; a number with no medium yields a
tiny (~843-byte) "no medium" page with no ``<TABLE>``. Real media render the
name in a ``<FONT SIZE=3>`` heading followed by one or more bordered tables of
``component | amount | unit`` rows, with free-text preparation notes between
and after the tables.

What it extracts
----------------
- ``original_name`` / ``name`` (snake_case)
- ``ingredients`` (preferred_term + concentration value/unit); ``<sub>`` in
  chemical formulae is flattened (Na<sub>2</sub>CO<sub>3</sub> -> Na2CO3)
- ``physical_state`` (SOLID_AGAR if an agar component is present, else LIQUID)
- ``medium_type`` (COMPLEX if an undefined-rich component is present, else DEFINED)
- ``ph_value`` (parsed from preparation text when stated)
- ``preparation_steps`` (free-text prep paragraphs, lightly classified)
- ``media_term`` (``jcm.grmd:<N>``) and a provenance ``notes`` link

CHEBI / MediaIngredientMech enrichment and archaea-vs-bacterial recategorization
are intentionally LEFT to the existing downstream curators (chebi-enrichment,
mediaingredientmech-enrichment, manual review) — this script only does the
faithful first-pass capture, matching how the original aggregator imports
seeded bare ingredient lists.

Usage
-----
    # explicit GRMD numbers
    python scripts/import_jcm_grmd.py --grmd 1333 1334 1341 --dry-run

    # auto-detect every real JCM medium absent from data/normalized_yaml/
    python scripts/import_jcm_grmd.py --detect-missing --dry-run

    # write records + validate against MediaRecipe
    python scripts/import_jcm_grmd.py --grmd 1333 --out-dir data/normalized_yaml/bacterial --validate
"""
from __future__ import annotations

import argparse
import html
import re
import subprocess
import sys
import time
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from record_io import dump_record  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parents[1]
NORMALIZED_DIR = REPO_ROOT / "data" / "normalized_yaml"
GRMD_URL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD={}"
EMPTY_PAGE_MAX_BYTES = 1000  # real media pages are multi-KB; empty slots ~843 B

# Unit token (as printed by JCM) -> ConcentrationUnitEnum
UNIT_MAP = {
    "g": "G_PER_L",
    "mg": "MG_PER_L",
    "µg": "MICROG_PER_L",
    "ug": "MICROG_PER_L",
    "ml": "ML_PER_L",
    "l": "ML_PER_L",        # litres -> mL basis; value scaled ×1000 in _to_concentration
}

# Components that mark a medium COMPLEX (chemically undefined inputs).
COMPLEX_MARKERS = (
    "yeast extract", "peptone", "casamino", "tryptone", "trypticase",
    "meat extract", "beef extract", "blood", "brain heart", "serum",
    "casein", "rumen", "tryptose", "proteose", "lab-lemco", "malt extract",
    "soytone", "gelatin", "digest", "infusion",
)


def fetch(grmd: int, *, retries: int = 3) -> str | None:
    """Return page HTML for a GRMD number, or None on hard failure."""
    last = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(GRMD_URL.format(grmd),
                                         headers={"User-Agent": "curl/8"})
            return urllib.request.urlopen(req, timeout=30).read().decode("utf-8", "ignore")
        except Exception as e:  # noqa: BLE001 - network is best-effort
            last = e
            time.sleep(1.5 * (attempt + 1))
    print(f"  ! GRMD={grmd}: fetch failed after {retries} tries: {last}", file=sys.stderr)
    return None


def _clean(cell: str) -> str:
    """Strip tags, flatten <sub>/<sup>, unescape entities, collapse whitespace."""
    cell = re.sub(r"</?su[bp]>", "", cell, flags=re.I)  # Na<sub>2</sub> -> Na2
    cell = re.sub(r"<[^>]+>", " ", cell)
    cell = html.unescape(cell).replace("\xa0", " ")
    return re.sub(r"\s+", " ", cell).strip()


BASE_REF_RE = re.compile(r"Medium No\.?\s*(\d+)", re.I)


def is_real_medium(page_html: str) -> bool:
    """A page is a real medium iff it carries a <FONT SIZE=3> name heading.

    Truly-unassigned GRMD numbers return a ~843-byte page with NO name
    heading. A *named* page with no ingredient table is still a real
    medium — it is a derivative definition ("Use Medium No. N with ...")
    whose composition is inherited from a base recipe.
    """
    return parse_name(page_html) is not None


def parse_name(page_html: str) -> str | None:
    m = re.search(r"<FONT SIZE=3>\s*(\d+)(?:&nbsp;|\s)+(.*?)</FONT>",
                  page_html, re.I | re.S)
    if not m:
        return None
    return _clean(m.group(2))


def parse_tables(page_html: str) -> list[dict]:
    """Parse the PRIMARY recipe <TABLE> into {name, amount, unit} ingredients.

    Only the first table is the medium's own recipe. JCM renders
    separately-prepared sub-solutions (e.g. "Ni-Se-W solution") in their own
    subsequent tables; flattening every table would merge those components into
    the medium's top-level ingredients and double-count them (the sub-solution
    is already listed by name + volume in the primary table). Parse the first
    table only.
    """
    rows: list[dict] = []
    tables = re.findall(r"<TABLE[^>]*>(.*?)</TABLE>", page_html, re.I | re.S)
    if not tables:
        return rows
    for tr in re.findall(r"<TR>(.*?)</TR>", tables[0], re.I | re.S):
        tds = re.findall(r"<TD[^>]*>(.*?)</TD>", tr, re.I | re.S)
        if len(tds) < 2:
            continue
        name = _clean(tds[0])
        amount = _clean(tds[1])
        unit = _clean(tds[2]) if len(tds) > 2 else ""
        if not name:
            continue
        rows.append({"name": name, "amount": amount, "unit": unit})
    return rows


def parse_prep_text(page_html: str) -> list[str]:
    """Free-text paragraphs outside tables (preparation instructions)."""
    body = re.split(r"<FONT SIZE=3>.*?</FONT></B></P>", page_html, flags=re.I | re.S)
    tail = body[-1] if len(body) > 1 else page_html
    tail = re.sub(r"<TABLE[^>]*>.*?</TABLE>", "\n", tail, flags=re.I | re.S)
    text = _clean(tail)
    # drop boilerplate + trailing navigation
    text = re.sub(r"Unless otherwise stated.*?15 min\.?", "", text, flags=re.I)
    parts = [p.strip() for p in re.split(r"(?<=[.])\s+(?=[A-Z0-9])", text) if p.strip()]
    skip = ("medium data", "search for medium", "back to", "copyright", "riken",
            "japan collection", "dataLayer", "gtag")
    return [p for p in parts if p and not any(s in p.lower() for s in skip) and len(p) > 4]


def _to_concentration(amount: str, unit: str) -> dict | None:
    amount = amount.strip()
    if not amount:
        return None
    unit = unit.strip()
    # JCM sometimes fuses the unit into the amount cell ("20g", "980mL")
    # and leaves the unit column blank. Recover the suffix when needed.
    if not unit:
        m_suf = re.search(r"([a-zA-Zµ]+)\s*$", amount)
        if m_suf:
            unit = m_suf.group(1)
    enum = UNIT_MAP.get(unit.lower())
    val = amount
    m = re.match(r"^[~<>]?\s*([0-9]*\.?[0-9]+)", amount)
    if m:
        val = m.group(1)
        # Litres are recorded on a per-litre (mL_PER_L) basis: a whole-litre
        # volume must be scaled ×1000 to mL, otherwise "1 l" would be emitted
        # as "1 ML_PER_L" — a 1000× under-count.
        if unit.lower() == "l":
            scaled = float(val) * 1000
            val = str(int(scaled)) if scaled.is_integer() else str(scaled)
    else:
        enum = enum or "VARIABLE"
    conc: dict = {"value": str(val), "unit": enum or "VARIABLE"}
    return conc


def classify(ingredients: list[dict], original_name: str = "") -> tuple[str, str]:
    names = " ".join(i["name"].lower() for i in ingredients) + " " + original_name.lower()
    physical = "SOLID_AGAR" if re.search(r"\bagar\b", names) else "LIQUID"
    if re.search(r"semi-?solid", original_name.lower()):
        physical = "SEMISOLID"
    medium_type = "COMPLEX" if any(mk in names for mk in COMPLEX_MARKERS) else "DEFINED"
    return physical, medium_type


def parse_ph(prep_steps: list[str]) -> float | None:
    for p in prep_steps:
        m = re.search(r"pH\s*(?:to|of|=|:)?\s*([0-9]+\.?[0-9]*)", p, re.I)
        if m:
            try:
                v = float(m.group(1))
                if 0 < v <= 14:
                    return v
            except ValueError:
                pass
    return None


def _snake(name: str) -> str:
    s = re.sub(r"[^a-z0-9]+", "_", name.lower()).strip("_")
    return s or "jcm_medium"


def build_record(grmd: int, page_html: str, cm_id: str) -> dict | None:
    name = parse_name(page_html)
    if not name:
        return None
    table_rows = parse_tables(page_html)
    prep_steps = parse_prep_text(page_html)

    # Derivative definition: a named medium with no composition table, e.g.
    # "Use Medium No. 1462 with 21.0 g/L NaCl". The schema requires >=1
    # ingredient, so inherit the base recipe's table (one level) and keep
    # the modification text verbatim for a curator to apply.
    inherited_from: int | None = None
    if not table_rows:
        m = BASE_REF_RE.search(" ".join(prep_steps))
        if m:
            base = int(m.group(1))
            base_page = fetch(base)
            if base_page and is_real_medium(base_page):
                base_rows = parse_tables(base_page)
                if base_rows:
                    table_rows = base_rows
                    inherited_from = base
        if not table_rows:
            print(f"  ! GRMD={grmd}: derivative medium with no resolvable base "
                  f"table -> skipped ({name!r})", file=sys.stderr)
            return None

    physical, medium_type = classify(table_rows, name)
    ph = parse_ph(prep_steps)

    ingredients = []
    for r in table_rows:
        ing: dict = {"preferred_term": r["name"]}
        conc = _to_concentration(r["amount"], r["unit"])
        if conc:
            ing["concentration"] = conc
        ingredients.append(ing)

    rec: dict = {
        "id": cm_id,
        "name": _snake(name),
        "original_name": name,
        "category": "bacterial",
        "medium_type": medium_type,
        "physical_state": physical,
    }
    if ph is not None:
        rec["ph_value"] = ph
    rec["media_term"] = {
        "preferred_term": f"JCM Medium J{grmd}",
        "term": {"id": f"jcm.grmd:{grmd}", "label": name},
    }
    note = f"Source: JCM | Link: {GRMD_URL.format(grmd)}"
    if inherited_from is not None:
        note += (f" | Derivative medium: ingredients inherited from JCM "
                 f"GRMD={inherited_from}; apply the stated modification "
                 f"(see preparation_steps) before use.")
    rec["notes"] = note
    if ingredients:
        rec["ingredients"] = ingredients
    if prep_steps:
        rec["preparation_steps"] = [
            {"step_number": i + 1, "action": "MIX", "description": s}
            for i, s in enumerate(prep_steps)
        ]
    rec["applications"] = ["Microbial cultivation"]
    rec["curation_history"] = [{
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "curator": "jcm-grmd-import",
        "action": "Scraped from JCM GRMD database",
        "notes": (f"Direct import from JCM GRMD={grmd}. "
                  + (f"Derivative of GRMD={inherited_from}: ingredients inherited "
                     "from the base medium, stated modification preserved in "
                     "preparation_steps and still to be applied. "
                     if inherited_from is not None else
                     "Ingredients captured verbatim. ")
                  + "CHEBI/MediaIngredientMech enrichment and category "
                  "(bacterial/archaea) review are downstream steps."),
    }]
    return rec


def ingested_grmd_numbers() -> set[int]:
    # Key on the media_term id (`jcm.grmd:NNN`), not `GRMD=NNN`. The latter also
    # appears in derivative records' notes when they inherit a base recipe
    # ("inherited from JCM GRMD=1462"), which would mark a base GRMD as already
    # ingested even when it has no record of its own (a false negative that
    # hides a genuinely missing medium from --detect-missing).
    out = subprocess.run(
        ["grep", "-rhoE", r"jcm\.grmd:[0-9]+", str(NORMALIZED_DIR)],
        capture_output=True, text=True,
    ).stdout
    return {int(x.split(":")[1]) for x in out.split()}


def next_id_start() -> int:
    out = subprocess.run(
        ["grep", "-rhoE", r"^id: CultureMech:[0-9]+", str(NORMALIZED_DIR)],
        capture_output=True, text=True,
    ).stdout
    nums = [int(re.search(r"(\d+)", line).group(1)) for line in out.splitlines()]
    return (max(nums) + 1) if nums else 1


def detect_missing(scan_max: int, delay: float = 0.0) -> dict[int, str]:
    """Real JCM media (within 1..scan_max) absent from the corpus.

    Returns a mapping of GRMD number -> fetched page HTML so the caller can
    reuse the already-downloaded pages instead of fetching them a second
    time. Honors ``delay`` (seconds) between network requests for politeness.
    """
    have = ingested_grmd_numbers()
    missing_candidates = [n for n in range(1, scan_max + 1) if n not in have]
    real: dict[int, str] = {}
    for i, n in enumerate(missing_candidates):
        page = fetch(n)
        if page and is_real_medium(page):
            real[n] = page
        if delay and i < len(missing_candidates) - 1:
            time.sleep(delay)
    return real


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    src = ap.add_mutually_exclusive_group(required=True)
    src.add_argument("--grmd", type=int, nargs="+", help="Explicit GRMD numbers.")
    src.add_argument("--detect-missing", action="store_true",
                     help="Scan for real JCM media absent from the corpus.")
    ap.add_argument("--scan-max", type=int, default=1500,
                    help="Upper GRMD bound for --detect-missing (default 1500).")
    ap.add_argument("--out-dir", type=Path, default=NORMALIZED_DIR / "bacterial")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print parsed records; do not write files.")
    ap.add_argument("--validate", action="store_true",
                    help="Run linkml-validate on each written record.")
    ap.add_argument("--delay", type=float, default=0.5,
                    help="Seconds between JCM requests (politeness).")
    args = ap.parse_args(argv)

    page_cache: dict[int, str] = {}
    if args.detect_missing:
        print(f"Scanning JCM 1..{args.scan_max} for media missing from the corpus...")
        page_cache = detect_missing(args.scan_max, args.delay)
        grmds = sorted(page_cache)
        print(f"Found {len(grmds)} real JCM media not yet ingested.")
    else:
        grmds = args.grmd

    next_id = next_id_start()
    written: list[Path] = []
    skipped: list[int] = []

    for grmd in grmds:
        # Reuse the page already fetched during --detect-missing; only hit the
        # network when we have no cached copy.
        page = page_cache.get(grmd)
        fetched = False
        if page is None:
            page = fetch(grmd)
            fetched = True
        if page is None:
            skipped.append(grmd)
            continue
        if not is_real_medium(page):
            print(f"  - GRMD={grmd}: empty/unassigned in JCM -> skipped")
            skipped.append(grmd)
            continue
        cm_id = f"CultureMech:{next_id:06d}"
        rec = build_record(grmd, page, cm_id)
        if rec is None:
            print(f"  ! GRMD={grmd}: could not parse a medium name -> skipped")
            skipped.append(grmd)
            continue
        next_id += 1

        fname = f"JCM_J{grmd}_{re.sub(r'[^A-Za-z0-9]+', '_', rec['original_name']).strip('_')[:80]}.yaml"
        out_path = args.out_dir / fname
        # Corpus convention is PyYAML's default width; width=100 created records
        # that every later curation pass would re-wrap (#141).
        yaml_text = dump_record(rec)

        if args.dry_run:
            print(f"\n[DRY RUN] GRMD={grmd} -> {out_path.relative_to(REPO_ROOT)}  "
                  f"({cm_id}, {len(rec.get('ingredients', []))} ingredients, "
                  f"{rec['physical_state']}, {rec['medium_type']}, "
                  f"pH={rec.get('ph_value', '-')})")
            print("    name:", rec["original_name"])
            continue

        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(yaml_text)
        written.append(out_path)
        print(f"  + {cm_id}  GRMD={grmd}  {rec['original_name'][:55]}  -> {out_path.name}")
        # Politeness sleep only when we actually made a network request here;
        # cached pages from --detect-missing already paid their delay.
        if fetched and args.delay:
            time.sleep(args.delay)

    if args.validate and written:
        print("\nValidating against MediaRecipe...")
        schema = REPO_ROOT / "src" / "culturemech" / "schema" / "culturemech.yaml"
        ok = 0
        for p in written:
            r = subprocess.run(
                ["uv", "run", "--extra", "dev", "linkml-validate",
                 "-s", str(schema), "-C", "MediaRecipe", str(p)],
                capture_output=True, text=True, cwd=REPO_ROOT,
            )
            status = "OK" if r.returncode == 0 else "FAIL"
            if r.returncode == 0:
                ok += 1
            else:
                print(f"  [FAIL] {p.name}\n{r.stdout}\n{r.stderr}")
        print(f"  validated {ok}/{len(written)} records")

    print(f"\nDone. written={len(written)} skipped={len(skipped)}"
          + (f"  skipped GRMD={skipped}" if skipped else ""))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
