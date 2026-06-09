#!/usr/bin/env python3
"""Validate that every ontology ID carries its correct ontology LABEL.

Shared, schema/config-driven id↔label correspondence checker. Vendored
**byte-identical** across the Mech repos (CultureMech / MIM / CommunityMech)
— the same convention as ``scripts/_edison_capture.py``. Verify with
``md5``; a fix here must be synced to all copies.

Why this exists
---------------
``linkml-term-validator validate-data --labels`` only checks that the
label of an ontology ID matches the ontology — and only for LinkML data
instances (YAML) whose schema declares a ``binding``. It does NOT cover
**data products**: SSSOM TSVs, mapping CSVs, KGX node tables, and review
TSVs all carry (id, label) columns that no LinkML tool reads. This script
closes that gap and also produces a single cross-surface drift report.

What it checks
--------------
For every (id, label) pair in the configured targets it resolves the
canonical label (and synonyms) from the same OAK sqlite adapters the
repos already use, and classifies the pair:

    OK_CANONICAL        label == canonical OBO label
    OK_SYNONYM          label is an accepted synonym (policy-dependent)
    MISMATCH            label is neither canonical nor an accepted synonym  (ERROR)
    ID_NOT_FOUND        id has an adapter but is absent from the ontology   (ERROR)
    EMPTY_LABEL         id present, label blank                             (ERROR)
    SKIPPED_NO_ADAPTER  prefix has no configured OAK adapter (cas:, MIM:, …)

Policy (per target, ``conf/id_label_targets.yaml``)
    ``canonical``            accept only the canonical OBO label (strict;
                             mirrors the linkml-term-validator schema gate).
    ``canonical_or_synonym`` accept canonical OR a synonym within
                             ``synonym_scope`` (exact | exact_related | all).

Modes
    ``--report PATH``  write a TSV of every non-OK pair and exit 0 (baseline).
    (default)          enforce: exit 2 if any ERROR-class pair is found.

Usage::

    python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
    python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml \\
        --report reports/label_drift.tsv
"""
from __future__ import annotations

import argparse
import csv
import re
import sys
from pathlib import Path
from typing import Any, Iterator

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent


def _safe_rel(path: Path) -> str:
    """``path`` relative to the repo when possible; else its absolute string."""
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


# Verdict classes that should fail an --enforce run.
_ERROR_VERDICTS = {"MISMATCH", "ID_NOT_FOUND", "EMPTY_LABEL"}

_CURIE_RE = re.compile(r"^([A-Za-z][A-Za-z0-9.]*):(.+)$")
_WS_RE = re.compile(r"\s+")

# OAK alias predicates by synonym scope (always includes label + exact).
_SYNONYM_PREDICATES = {
    "exact": ["oio:hasExactSynonym"],
    "exact_related": ["oio:hasExactSynonym", "oio:hasRelatedSynonym"],
    "all": [
        "oio:hasExactSynonym",
        "oio:hasRelatedSynonym",
        "oio:hasBroadSynonym",
        "oio:hasNarrowSynonym",
    ],
}


def normalize(text: str) -> str:
    """Casefold, strip, collapse internal whitespace — for label comparison."""
    return _WS_RE.sub(" ", str(text).strip()).casefold()


def prefix_of(curie: str) -> str | None:
    m = _CURIE_RE.match(str(curie).strip())
    return m.group(1) if m else None


class AdapterPool:
    """Lazily loads OAK adapters, but ONLY for prefixes in the allowlist.

    The allowlist (``adapters`` map in the config) is the safety boundary:
    prefixes without an entry (``cas:``, ``MIM:``, ``kgmicrobe.compound:``,
    ``DSMZ``, …) are never looked up — they are reported as
    ``SKIPPED_NO_ADAPTER`` instead of triggering a futile ontology download.
    """

    def __init__(self, adapters: dict[str, str]):
        self._selectors = adapters
        self._cache: dict[str, Any] = {}

    def get(self, prefix: str | None):
        if not prefix or prefix not in self._selectors:
            return None
        if prefix not in self._cache:
            try:
                from oaklib import get_adapter

                self._cache[prefix] = get_adapter(self._selectors[prefix])
            except Exception as exc:  # pragma: no cover - environment dependent
                print(f"  ! failed to load adapter for {prefix}: {exc}", file=sys.stderr)
                self._cache[prefix] = None
        return self._cache[prefix]


def accepted_labels(adapter: Any, curie: str, scope: str) -> tuple[str | None, set[str], bool]:
    """Return (canonical_label, accepted_normalized_set, id_found).

    ``accepted_normalized_set`` always contains the canonical label; with a
    non-``canonical`` policy the caller widens it via ``scope`` synonyms.
    ``id_found`` is False when the id is absent from the ontology.
    """
    try:
        canonical = adapter.label(curie)
    except Exception:
        canonical = None
    if canonical is None:
        return None, set(), False
    accepted = {normalize(canonical)}
    alias_map: dict[str, list[str]] = {}
    try:
        alias_map = adapter.entity_alias_map(curie) or {}
    except Exception:
        alias_map = {}
    for pred in _SYNONYM_PREDICATES.get(scope, _SYNONYM_PREDICATES["exact"]):
        for alias in alias_map.get(pred, []) or []:
            accepted.add(normalize(alias))
    return canonical, accepted, True


def classify(
    *,
    curie: str,
    label: str,
    adapter: Any,
    policy: str,
    scope: str,
) -> dict[str, Any]:
    """Classify one (id, label) pair into a verdict dict."""
    canonical, accepted, found = accepted_labels(adapter, curie, scope)
    base = {"id": curie, "label": label, "canonical": canonical or ""}
    if not found:
        return {**base, "verdict": "ID_NOT_FOUND"}
    if label is None or str(label).strip() == "":
        return {**base, "verdict": "EMPTY_LABEL"}
    norm_label = normalize(label)
    if canonical and norm_label == normalize(canonical):
        return {**base, "verdict": "OK_CANONICAL"}
    if policy == "canonical_or_synonym" and norm_label in accepted:
        return {**base, "verdict": "OK_SYNONYM"}
    return {**base, "verdict": "MISMATCH"}


# -- target readers -------------------------------------------------------

def _read_tabular_rows(path: Path, fmt: str) -> tuple[list[str], list[dict[str, str]]]:
    """Read a TSV/CSV, skipping SSSOM ``#`` comment-prelude lines."""
    delim = "," if fmt == "csv" else "\t"
    with path.open(newline="", encoding="utf-8") as fh:
        lines = [ln for ln in fh if not ln.lstrip().startswith("#")]
    if not lines:
        return [], []
    reader = csv.DictReader(lines, delimiter=delim)
    return list(reader.fieldnames or []), list(reader)


def iter_tabular(path: Path, fmt: str, pairs: list[list[str]]) -> Iterator[tuple[str, str, str]]:
    """Yield (locator, id, label) for each configured id/label column pair."""
    fields, rows = _read_tabular_rows(path, fmt)
    field_set = set(fields)
    usable = [(i, l) for (i, l) in pairs if i in field_set and l in field_set]
    for n, row in enumerate(rows, start=2):  # row 1 is the header
        for id_col, label_col in usable:
            curie = (row.get(id_col) or "").strip()
            if not curie:
                continue
            label = (row.get(label_col) or "").strip()
            yield f"row {n} [{id_col}/{label_col}]", curie, label


def _walk_yaml(node: Any, pairs: list[tuple[str, str]], path: str) -> Iterator[tuple[str, str, str]]:
    if isinstance(node, dict):
        for id_key, label_key in pairs:
            if id_key in node and label_key in node:
                curie = node.get(id_key)
                if isinstance(curie, str) and curie.strip():
                    label = node.get(label_key)
                    label = label if isinstance(label, str) else ""
                    yield f"{path}.{id_key}", curie.strip(), (label or "").strip()
        for k, v in node.items():
            yield from _walk_yaml(v, pairs, f"{path}.{k}")
    elif isinstance(node, list):
        for idx, item in enumerate(node):
            yield from _walk_yaml(item, pairs, f"{path}[{idx}]")


def iter_yaml(path: Path, pairs: list[list[str]]) -> Iterator[tuple[str, str, str]]:
    """Yield (locator, id, label) from a YAML doc by recursively finding dicts
    that carry BOTH an id key and its sibling label key."""
    try:
        doc = yaml.safe_load(path.read_text())
    except Exception as exc:  # pragma: no cover
        print(f"  ! failed to parse {path}: {exc}", file=sys.stderr)
        return
    yield from _walk_yaml(doc, [(a, b) for a, b in pairs], path.name)


# -- driver ---------------------------------------------------------------

def load_config(config_path: Path) -> dict[str, Any]:
    cfg = yaml.safe_load(config_path.read_text())
    if not isinstance(cfg, dict):
        raise SystemExit(f"Config is not a mapping: {config_path}")
    cfg.setdefault("adapters", {})
    cfg.setdefault("synonym_scope", "exact_related")
    cfg.setdefault("targets", [])
    return cfg


def run(config_path: Path, report_path: Path | None) -> int:
    cfg = load_config(config_path)
    pool = AdapterPool(cfg["adapters"])
    default_scope = cfg["synonym_scope"]

    findings: list[dict[str, Any]] = []
    counts: dict[str, int] = {}
    for target in cfg["targets"]:
        name = target.get("name", target.get("glob", "?"))
        kind = target.get("kind", "tabular")
        policy = target.get("policy", "canonical_or_synonym")
        scope = target.get("synonym_scope", default_scope)
        pairs = target.get("pairs", [])
        globs = target.get("glob")
        glob_list = globs if isinstance(globs, list) else [globs]
        paths: list[Path] = []
        for g in glob_list:
            paths.extend(sorted(REPO_ROOT.glob(g)))
        if not paths:
            print(f"  - {name}: no files match {glob_list}")
            continue
        for path in paths:
            rel = _safe_rel(path)
            if kind == "yaml":
                pairs_iter = iter_yaml(path, pairs)
            else:
                pairs_iter = iter_tabular(path, target.get("format", "tsv"), pairs)
            for locator, curie, label in pairs_iter:
                prefix = prefix_of(curie)
                adapter = pool.get(prefix)
                if adapter is None:
                    verdict = "SKIPPED_NO_ADAPTER"
                    rec = {"id": curie, "label": label, "canonical": "", "verdict": verdict}
                else:
                    rec = classify(
                        curie=curie, label=label, adapter=adapter, policy=policy, scope=scope
                    )
                counts[rec["verdict"]] = counts.get(rec["verdict"], 0) + 1
                if rec["verdict"] not in ("OK_CANONICAL", "OK_SYNONYM", "SKIPPED_NO_ADAPTER"):
                    findings.append({
                        "surface": name,
                        "file": str(rel),
                        "locator": locator,
                        "policy": policy,
                        **rec,
                    })

    # Summary
    print("\nid↔label correspondence summary:")
    for verdict in (
        "OK_CANONICAL",
        "OK_SYNONYM",
        "MISMATCH",
        "ID_NOT_FOUND",
        "EMPTY_LABEL",
        "SKIPPED_NO_ADAPTER",
    ):
        if verdict in counts:
            print(f"  {verdict:>20}: {counts[verdict]}")

    if report_path is not None:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with report_path.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, delimiter="\t")
            w.writerow(
                ["surface", "file", "locator", "id", "current_label",
                 "canonical_label", "verdict", "policy"]
            )
            for f in findings:
                w.writerow([
                    f["surface"], f["file"], f["locator"], f["id"],
                    f["label"], f["canonical"], f["verdict"], f["policy"],
                ])
        print(f"\nWrote {len(findings)} flagged pairs to {_safe_rel(report_path)}")
        return 0

    errors = [f for f in findings if f["verdict"] in _ERROR_VERDICTS]
    if errors:
        print(f"\n❌ {len(errors)} id↔label correspondence error(s):")
        for f in errors[:50]:
            print(f"  {f['verdict']}: {f['file']} {f['locator']} "
                  f"{f['id']} label='{f['label']}' canonical='{f['canonical']}'")
        if len(errors) > 50:
            print(f"  ... {len(errors) - 50} more")
        return 2
    print("\n✅ All id↔label pairs correspond.")
    return 0


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("-c", "--config", type=Path, default=REPO_ROOT / "conf" / "id_label_targets.yaml")
    ap.add_argument("--report", type=Path, default=None,
                    help="Write a drift TSV here and exit 0 (baseline mode).")
    args = ap.parse_args(argv)
    if not args.config.is_file():
        print(f"Config not found: {args.config}", file=sys.stderr)
        return 2
    return run(args.config, args.report)


if __name__ == "__main__":
    sys.exit(main())
