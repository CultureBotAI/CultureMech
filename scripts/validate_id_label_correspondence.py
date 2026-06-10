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
    ADAPTER_ERROR       a CONFIGURED adapter failed to load                 (ERROR)
    SKIPPED_NO_ADAPTER  prefix has no configured OAK adapter (cas:, MIM:, …)
    SKIPPED_EMPTY_ADAPTER  configured adapter loaded but holds no terms (e.g. a
                        0-byte sqlite stub); db needs populating, data isn't wrong

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
# ADAPTER_ERROR is fatal: a configured adapter that fails to LOAD must never be
# silently downgraded to SKIPPED_NO_ADAPTER (which would let an enforce run pass
# while checking nothing).
_ERROR_VERDICTS = {"MISMATCH", "ID_NOT_FOUND", "EMPTY_LABEL", "ADAPTER_ERROR"}

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


# Sentinel returned by ``AdapterPool.get`` when a CONFIGURED adapter fails to
# load. Distinct from ``None`` (prefix not configured → legitimate skip) so the
# caller can raise a fatal ADAPTER_ERROR instead of a benign SKIPPED_NO_ADAPTER.
LOAD_FAILED = object()

# Sentinel for a CONFIGURED adapter that loads but contains no terms (e.g. a
# 0-byte ``~/.data/oaklib/micro.db`` stub that OAK opens happily but that yields
# ``label() == None`` for every id). Without this, every id under such a prefix
# would be reported as a false ``ID_NOT_FOUND``. Treated as a benign skip
# (``SKIPPED_EMPTY_ADAPTER``) — the db needs populating, the data isn't wrong.
EMPTY_ADAPTER = object()


class AdapterPool:
    """Lazily loads OAK adapters, but ONLY for prefixes in the allowlist.

    The allowlist (``adapters`` map in the config) is the safety boundary:
    prefixes without an entry (``cas:``, ``MIM:``, ``kgmicrobe.compound:``,
    ``DSMZ``, …) are never looked up — they are reported as
    ``SKIPPED_NO_ADAPTER`` instead of triggering a futile ontology download.

    Prefix matching is case-insensitive: data carries lowercase ``mesh:`` while
    the allowlist (and OAK's OBO CURIEs) use uppercase ``MESH:``. ``get`` keys
    on the canonical allowlist case, and callers can rewrite the CURIE prefix
    via ``canonical_prefix`` so the lookup actually resolves.

    ``get`` returns one of three things:

    * ``None``          — prefix is not in the allowlist (legitimate skip).
    * ``LOAD_FAILED``   — prefix IS configured but its adapter raised on load.
    * an OAK adapter    — ready to query.

    The ``LOAD_FAILED`` case is deliberately NOT collapsed into ``None`` so a
    broken-but-configured adapter surfaces as a fatal verdict rather than
    silently passing an enforce run.
    """

    def __init__(self, adapters: dict[str, str]):
        self._selectors = adapters
        # Case-insensitive prefix lookup: data carries lowercase `mesh:` while
        # the allowlist (and OAK's OBO CURIEs) use uppercase `MESH:`. Map any
        # casing of a data prefix back to its canonical allowlist key.
        self._canonical: dict[str, str] = {key.casefold(): key for key in adapters}
        self._cache: dict[str, Any] = {}

    def canonical_prefix(self, prefix: str | None) -> str | None:
        """Return the allowlist key matching ``prefix`` case-insensitively."""
        if not prefix:
            return None
        return self._canonical.get(prefix.casefold())

    def get(self, prefix: str | None):
        key = self.canonical_prefix(prefix)
        if key is None:
            return None
        if key not in self._cache:
            try:
                from oaklib import get_adapter

                adapter = get_adapter(self._selectors[key])
            except Exception as exc:  # pragma: no cover - environment dependent
                print(f"  ! failed to load adapter for {key}: {exc}", file=sys.stderr)
                self._cache[key] = LOAD_FAILED
            else:
                self._cache[key] = EMPTY_ADAPTER if self._is_empty(adapter, key) else adapter
        return self._cache[key]

    @staticmethod
    def _is_empty(adapter: Any, key: str) -> bool:
        """True if the adapter loaded but holds no terms (e.g. a 0-byte sqlite).

        Peeks a single entity (O(1)) rather than counting. Two empty shapes:
        a valid-but-termless db (``entities()`` yields nothing), and an
        uninitialized 0-byte sqlite stub whose tables don't exist yet
        (``entities()`` raises ``no such table`` — OAK's ``sqlite:obo:micro``
        points at exactly such a stub). Any *other* probe error is treated as
        non-empty so a genuinely broken adapter still surfaces per-id verdicts
        rather than being masked as an empty skip.
        """
        try:
            return next(iter(adapter.entities()), None) is None
        except Exception as exc:  # pragma: no cover - environment dependent
            if "no such table" in str(exc).lower():  # uninitialized/0-byte stub
                return True
            print(f"  ! emptiness probe failed for {key}: {exc}", file=sys.stderr)
            return False


def accepted_labels(
    adapter: Any, curie: str, scope: str, *, include_synonyms: bool = True
) -> tuple[str | None, set[str], bool]:
    """Return (canonical_label, accepted_normalized_set, id_found).

    ``accepted_normalized_set`` always contains the canonical label; when
    ``include_synonyms`` is set it is widened via ``scope`` synonyms. Callers
    using a strict ``canonical`` policy never consult synonyms, so they pass
    ``include_synonyms=False`` to skip the (potentially expensive)
    ``entity_alias_map`` lookup entirely. ``id_found`` is False when the id is
    absent from the ontology.
    """
    try:
        canonical = adapter.label(curie)
    except Exception:
        canonical = None
    if canonical is None:
        return None, set(), False
    accepted = {normalize(canonical)}
    if include_synonyms:
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
    lookup_curie: str | None = None,
) -> dict[str, Any]:
    """Classify one (id, label) pair into a verdict dict.

    ``curie`` is reported verbatim; ``lookup_curie`` (when given) is the
    case-normalized CURIE actually passed to the adapter so that, e.g., a
    lowercase ``mesh:`` row resolves against OAK's uppercase ``MESH:`` ids.
    Synonyms are only built when the policy actually consults them.
    """
    include_synonyms = policy != "canonical"
    canonical, accepted, found = accepted_labels(
        adapter, lookup_curie or curie, scope, include_synonyms=include_synonyms
    )
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

def _read_tabular_rows(
    path: Path, fmt: str
) -> tuple[list[str], list[dict[str, str]], list[int]]:
    """Read a TSV/CSV, skipping ONLY the leading SSSOM ``#`` comment prelude.

    Returns ``(fieldnames, rows, data_line_numbers)`` where each entry of
    ``data_line_numbers`` is the TRUE 1-based physical file line where the
    corresponding data row begins, so locators stay accurate even after the
    prelude is removed. ``#`` lines that appear *after* the header are NOT
    stripped (only the contiguous top-of-file prelude is), matching the SSSOM
    convention where the metadata block precedes the table.

    The physical line numbers come from the original file, so a quoted
    multiline field could desync ``len(data_line_numbers)`` from ``len(rows)``;
    the caller falls back to a post-header ordinal in that case.
    """
    delim = "," if fmt == "csv" else "\t"
    with path.open(newline="", encoding="utf-8") as fh:
        raw = list(enumerate(fh, start=1))  # (physical_line_number, text)
    # Strip only the contiguous prelude of ``#`` lines at the top of the file.
    start = 0
    while start < len(raw) and raw[start][1].lstrip().startswith("#"):
        start += 1
    body = raw[start:]
    if not body:
        return [], [], []
    lines = [text for _, text in body]
    # body[0] is the header; data rows begin at the next physical line.
    data_line_numbers = [phys for phys, _ in body[1:]]
    reader = csv.DictReader(lines, delimiter=delim)
    return list(reader.fieldnames or []), list(reader), data_line_numbers


def iter_tabular(path: Path, fmt: str, pairs: list[list[str]]) -> Iterator[tuple[str, str, str]]:
    """Yield (locator, id, label) for each configured id/label column pair."""
    fields, rows, line_numbers = _read_tabular_rows(path, fmt)
    field_set = set(fields)
    # Keep any pair whose id column exists; a missing label column is allowed
    # so an id present without its label still gets an EMPTY_LABEL verdict
    # rather than being silently dropped.
    usable = [(i, l) for (i, l) in pairs if i in field_set]
    # RISK: a configured pair whose ID column is absent must NOT vanish silently.
    # Warn loudly when the file has rows but a configured pair can't be applied
    # at all. (A missing LABEL column alone is fine — it yields EMPTY_LABEL.)
    if rows:
        for (i, l) in pairs:
            if i not in field_set or l not in field_set:
                missing = [c for c in (i, l) if c not in field_set]
                print(
                    f"  ! {_safe_rel(path)}: configured id/label pair "
                    f"[{i}/{l}] — missing column(s) {missing}; "
                    f"present columns: {sorted(field_set)}",
                    file=sys.stderr,
                )
    for idx, row in enumerate(rows):
        # True physical line number when available (a quoted multiline field
        # could desync the count); else fall back to the post-header ordinal.
        line_no = line_numbers[idx] if idx < len(line_numbers) else idx + 2
        for id_col, label_col in usable:
            curie = (row.get(id_col) or "").strip()
            if not curie:
                continue
            label = (row.get(label_col) or "").strip()
            yield f"line {line_no} [{id_col}/{label_col}]", curie, label


def _walk_yaml(
    node: Any,
    pairs: list[tuple[str, str]],
    path: str,
    exclude_keys: frozenset[str] = frozenset(),
) -> Iterator[tuple[str, str, str]]:
    if isinstance(node, dict):
        for id_key, label_key in pairs:
            # An id present without its sibling label must still be checked
            # (yields EMPTY_LABEL), so we do NOT require label_key to exist.
            if id_key in node:
                curie = node.get(id_key)
                if isinstance(curie, str) and curie.strip():
                    label = node.get(label_key)
                    label = label if isinstance(label, str) else ""
                    yield f"{path}.{id_key}", curie.strip(), (label or "").strip()
        for k, v in node.items():
            # Skip excluded grounding blocks (e.g. mediaingredientmech_chebi_term,
            # whose label is intentionally MIM's preferred_term, not the OBO
            # canonical label, so a `canonical` policy would false-MISMATCH it).
            if k in exclude_keys:
                continue
            yield from _walk_yaml(v, pairs, f"{path}.{k}", exclude_keys)
    elif isinstance(node, list):
        for idx, item in enumerate(node):
            yield from _walk_yaml(item, pairs, f"{path}[{idx}]", exclude_keys)


def iter_yaml(
    path: Path, pairs: list[list[str]], exclude_keys: frozenset[str] = frozenset()
) -> Iterator[tuple[str, str, str]]:
    """Yield (locator, id, label) from a YAML doc by recursively finding dicts
    that carry an id key (and, when present, its sibling label key)."""
    try:
        doc = yaml.safe_load(path.read_text())
    except Exception as exc:  # pragma: no cover
        print(f"  ! failed to parse {path}: {exc}", file=sys.stderr)
        return
    yield from _walk_yaml(doc, [(a, b) for a, b in pairs], path.name, exclude_keys)


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
        exclude_keys = frozenset(target.get("exclude_keys", []) or [])
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
                pairs_iter = iter_yaml(path, pairs, exclude_keys)
            else:
                pairs_iter = iter_tabular(path, target.get("format", "tsv"), pairs)
            for locator, curie, label in pairs_iter:
                prefix = prefix_of(curie)
                adapter = pool.get(prefix)
                if adapter is None:
                    rec = {"id": curie, "label": label, "canonical": "",
                           "verdict": "SKIPPED_NO_ADAPTER"}
                elif adapter is LOAD_FAILED:
                    rec = {"id": curie, "label": label, "canonical": "",
                           "verdict": "ADAPTER_ERROR"}
                elif adapter is EMPTY_ADAPTER:
                    rec = {"id": curie, "label": label, "canonical": "",
                           "verdict": "SKIPPED_EMPTY_ADAPTER"}
                else:
                    # Rewrite the CURIE prefix to the canonical allowlist case
                    # (e.g. mesh: -> MESH:) so OAK, which keys on uppercase OBO
                    # prefixes, resolves the label instead of returning None.
                    canonical_prefix = pool.canonical_prefix(prefix)
                    lookup_curie = curie
                    if canonical_prefix and prefix != canonical_prefix:
                        lookup_curie = f"{canonical_prefix}:{curie.split(':', 1)[1]}"
                    rec = classify(
                        curie=curie, label=label, adapter=adapter, policy=policy,
                        scope=scope, lookup_curie=lookup_curie,
                    )
                counts[rec["verdict"]] = counts.get(rec["verdict"], 0) + 1
                if rec["verdict"] not in ("OK_CANONICAL", "OK_SYNONYM",
                                          "SKIPPED_NO_ADAPTER", "SKIPPED_EMPTY_ADAPTER"):
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
        "ADAPTER_ERROR",
        "SKIPPED_NO_ADAPTER",
        "SKIPPED_EMPTY_ADAPTER",
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
