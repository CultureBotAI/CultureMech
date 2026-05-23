#!/usr/bin/env python3
"""Enrich CultureMech OrganismDescriptors with NCBI genome accessions.

Phase E of the CultureMech literature-review pipeline (per
`/Users/marcin/.claude/plans/now-focus-on-culturemech-piped-shell.md`).

For every OrganismDescriptor under data/normalized_yaml/**/*.yaml that
has `term: NCBITaxon:N` but empty `genome_assembly_id`:

  1. Look up SAMN accessions in
     ../kg-microbe/kg_microbe/transform_utils/bakta/samn_to_ncbitaxon.tsv
     (local file, no network).
  2. Fall back to the NCBI Datasets API
     /genome/taxon/{taxid}/dataset_report
     for representative GCF_/GCA_ accessions.
  3. Cache lookups under workspace/cache/ncbi_genome_lookups.json so
     reruns are fast.

Default is dry-run (prints proposed assignments). `--apply` writes.

Usage:
    python3 scripts/enrich_genome_ids.py --limit 5
    python3 scripts/enrich_genome_ids.py --apply
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "data" / "normalized_yaml"

sys.path.insert(0, str(REPO_ROOT / "src"))
from culturemech.curate.curation_event import record_curation_event
CACHE_FILE = REPO_ROOT / "workspace" / "cache" / "ncbi_genome_lookups.json"
KG_MICROBE_ROOT = Path(os.environ.get(
    "KGMICROBE_ROOT",
    REPO_ROOT.parent / "kg-microbe",
))
SAMN_TSV = KG_MICROBE_ROOT / "kg_microbe" / "transform_utils" / "bakta" / "samn_to_ncbitaxon.tsv"

DATASETS_URL = "https://api.ncbi.nlm.nih.gov/datasets/v2alpha/genome/taxon/{taxid}/dataset_report"
DEFAULT_RATE = 3.0
UA = "CultureMech-genome-enricher/1.0"


# ---------- SAMN local table ----------

_SAMN_INDEX_CACHE: dict[str, list[str]] | None = None


def load_samn_index() -> dict[str, list[str]]:
    """Map ncbitaxon_id (str) -> list[SAMN ids]."""
    global _SAMN_INDEX_CACHE
    if _SAMN_INDEX_CACHE is not None:
        return _SAMN_INDEX_CACHE
    idx: dict[str, list[str]] = {}
    if not SAMN_TSV.is_file():
        print(f"warn: {SAMN_TSV} not found; SAMN lookup disabled", file=sys.stderr)
        _SAMN_INDEX_CACHE = idx
        return idx
    with open(SAMN_TSV) as f:
        header = f.readline().rstrip("\n").split("\t")
        try:
            samn_col = header.index("samn_id")
            tax_col = header.index("ncbitaxon_id")
        except ValueError:
            samn_col, tax_col = 0, 1
        for line in f:
            parts = line.rstrip("\n").split("\t")
            if len(parts) <= max(samn_col, tax_col):
                continue
            samn = parts[samn_col].strip()
            taxid = parts[tax_col].strip()
            if not samn or not taxid:
                continue
            idx.setdefault(taxid, []).append(samn)
    _SAMN_INDEX_CACHE = idx
    return idx


# ---------- NCBI Datasets API ----------

def fetch_assembly_accessions(taxid: str, rate: float) -> list[str]:
    url = DATASETS_URL.format(taxid=urllib.parse.quote(taxid))
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/json",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            data = json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return [f"_error:HTTP {e.code}"]
    except Exception as e:
        return [f"_error:{type(e).__name__}"]
    finally:
        time.sleep(1.0 / rate)
    accessions: list[str] = []
    for rep in data.get("reports") or []:
        acc = (rep.get("accession") or "").strip()
        if acc and (acc.startswith("GCF_") or acc.startswith("GCA_")):
            if acc not in accessions:
                accessions.append(acc)
    return accessions


# ---------- cache ----------

def load_cache() -> dict:
    if CACHE_FILE.is_file():
        try:
            return json.loads(CACHE_FILE.read_text())
        except Exception:
            return {}
    return {}


def save_cache(cache: dict) -> None:
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    CACHE_FILE.write_text(json.dumps(cache, indent=2, sort_keys=True))


# ---------- per-organism resolution ----------

def extract_taxid(term: dict | None) -> str | None:
    if not term or not isinstance(term, dict):
        return None
    tid = (term.get("id") or "").strip()
    if tid.startswith("NCBITaxon:"):
        return tid.split(":", 1)[1]
    return None


def resolve_genomes(taxid: str, samn_idx: dict[str, list[str]],
                    cache: dict, rate: float, prefer_api: bool) -> list[str]:
    if taxid in cache:
        return list(cache[taxid])
    samns = samn_idx.get(taxid, [])
    if samns and not prefer_api:
        cache[taxid] = list(samns)
        return list(samns)
    api_accs = fetch_assembly_accessions(taxid, rate)
    real = [a for a in api_accs if not a.startswith("_error:")]
    combined = list(samns) + [a for a in real if a not in samns]
    if combined:
        cache[taxid] = list(combined)
    else:
        cache[taxid] = []
    return list(combined)


# ---------- recipe walk ----------

def iter_recipes(limit: int | None) -> list[Path]:
    out: list[Path] = []
    if not DATA_DIR.is_dir():
        return out
    for p in sorted(DATA_DIR.rglob("*.yaml")):
        out.append(p)
        if limit is not None and len(out) >= limit:
            break
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    ap.add_argument("--apply", action="store_true",
                    help="write the enriched genome IDs (default: dry-run)")
    ap.add_argument("--limit", type=int, default=None,
                    help="max number of MediaRecipe YAMLs to scan")
    ap.add_argument("--rate", type=float, default=DEFAULT_RATE,
                    help="NCBI Datasets API req/s (default 3)")
    ap.add_argument("--prefer-api", action="store_true",
                    help="query the NCBI Datasets API even when SAMN already matches")
    args = ap.parse_args()

    samn_idx = load_samn_index()
    cache = load_cache()

    recipes = iter_recipes(args.limit)
    print(f"Recipes to scan: {len(recipes)}")
    print(f"Mode: {'APPLY (writing genome_assembly_id)' if args.apply else 'DRY-RUN'}")
    print(f"SAMN index: {sum(len(v) for v in samn_idx.values())} SAMN ids "
          f"across {len(samn_idx)} taxa")

    n_organisms = 0
    n_already_have = 0
    n_no_taxid = 0
    n_resolved = 0
    n_unresolved = 0
    n_recipes_modified = 0

    try:
        for p in recipes:
            try:
                with open(p) as f:
                    recipe = yaml.safe_load(f) or {}
            except Exception as e:
                print(f"  load error {p.name}: {e}", file=sys.stderr)
                continue
            organisms = recipe.get("target_organisms") or []
            modified = False
            for org in organisms:
                n_organisms += 1
                if org.get("genome_assembly_id"):
                    n_already_have += 1
                    continue
                taxid = extract_taxid(org.get("term"))
                if not taxid:
                    n_no_taxid += 1
                    continue
                accs = resolve_genomes(taxid, samn_idx, cache, args.rate, args.prefer_api)
                if not accs:
                    n_unresolved += 1
                    continue
                n_resolved += 1
                org_label = org.get("preferred_term") or org.get("term", {}).get("label", "")
                print(f"  {p.name} :: {org_label} (NCBITaxon:{taxid}) → {accs}")
                if args.apply:
                    org["genome_assembly_id"] = accs
                    modified = True
            if modified:
                record_curation_event(
                    recipe,
                    curator="enrich_genome_ids.py",
                    action="ENRICHED_GENOME_IDS",
                    notes=(
                        f"organisms_resolved={sum(1 for o in organisms if o.get('genome_assembly_id'))} "
                        f"of {len(organisms)}"
                    ),
                    source="NCBI Datasets API + samn_to_ncbitaxon.tsv",
                    skip_if_recent=True,
                )
                with open(p, "w") as f:
                    yaml.safe_dump(recipe, f, sort_keys=False, allow_unicode=True)
                n_recipes_modified += 1
    finally:
        save_cache(cache)

    print()
    print(f"Organisms scanned: {n_organisms}")
    print(f"  already had genome_assembly_id: {n_already_have}")
    print(f"  no NCBITaxon term: {n_no_taxid}")
    print(f"  newly resolved: {n_resolved}")
    print(f"  unresolved (no SAMN, no API hit): {n_unresolved}")
    if args.apply:
        print(f"Recipes modified: {n_recipes_modified}")
    else:
        print("(dry-run — pass --apply to write)")
    print(f"Cache: {CACHE_FILE.relative_to(REPO_ROOT)} "
          f"({len(cache)} taxids cached)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
