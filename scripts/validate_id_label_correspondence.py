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
    OK_ID_ONLY          id resolves; label match WAIVED for this slot (the slot
                        carries a curator-intended formula/common name, e.g.
                        CHEBI:15377 "Distilled water" — see ``label_waived_keys``)
    OK_EXCEPTION        the exact (id, label) pair is on the target's
                        ``exceptions`` allow-list — a curator-accepted residual
                        (obsolete-no-successor, no clean term yet, or id absent
                        from the current ontology snapshot) carrying a documented
                        ``reason``. Overrides MISMATCH / ID_NOT_FOUND only; the
                        match is exact, so a different wrong label on the same id
                        still fails as MISMATCH.
    MISMATCH            label is neither canonical nor an accepted synonym  (ERROR)
    ID_NOT_FOUND        id has an adapter but is absent from the ontology   (ERROR)
    EMPTY_LABEL         id present, label blank                             (ERROR)
    MISSING_COLUMN      a CONFIGURED id/label column is absent from a       (ERROR)
                        tabular target that has data rows — without this the
                        pair silently drops and enforce false-greens on drift
    ADAPTER_ERROR       a CONFIGURED adapter failed to load                 (ERROR)
    UNKNOWN_PREFIX      CURIE prefix is neither a configured ontology       (ERROR)
                        adapter NOR an explicitly ``ignored_prefixes`` entry —
                        i.e. a typo (``CHBEI:``) or an unexpected new prefix.
                        Without this such ids silently fell through as
                        SKIPPED_NO_ADAPTER and enforce false-greened on them.
    SKIPPED_NO_ADAPTER  prefix is an explicitly ignored non-ontology prefix
                        (``cas:``, ``MIM:``, ``kgmicrobe.compound:`` …) or the
                        id has no CURIE prefix at all (e.g. ``UNMAPPED_0001``)
    SKIPPED_EMPTY_ADAPTER  configured adapter loaded but holds no terms (e.g. a
                        0-byte sqlite stub); db needs populating, data isn't wrong

Policy (per target, ``conf/id_label_targets.yaml``)
    ``canonical``            accept only the canonical OBO label (strict;
                             mirrors the linkml-term-validator schema gate).
    ``canonical_or_synonym`` accept canonical OR a synonym within
                             ``synonym_scope`` (exact | exact_related | all).

Per-target knobs (in addition to ``policy``/``synonym_scope``/``pairs``)
    ``required: true``       fail enforce when the target's glob matches NO
                             files (an expected artifact, e.g. an SSSOM export,
                             wasn't built). Default false preserves the prior
                             "skip-with-exit-0" behaviour for optional targets.
    ``label_waived_keys``    slots that carry curator-intended labels (formula /
                             common names) and so are EXEMPT from canonical-label
                             matching but STILL id-existence checked (OK_ID_ONLY
                             when the id resolves, ID_NOT_FOUND when it doesn't).
                             For YAML targets the entries match the *parent key*
                             of the id/label dict (e.g. ``term``, ``chebi_term``);
                             for tabular targets they match the *id column name*
                             (e.g. ``ontology_id``). This implements the product
                             decision to KEEP labels like "D-glucose" / "NaCl"
                             rather than relabel them to the OBO canonical form.
                             Unlike ``exclude_keys`` (which prunes the whole
                             subtree and checks nothing), label-waived slots are
                             still validated for id existence.

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

# ``chem_formula`` is a sibling module in this same scripts/ directory. Import it
# by way of an explicit sys.path entry so the validator works both when run as a
# script (scripts/ already on sys.path) and when loaded by file path via
# importlib, as the tests do.
_SCRIPTS_DIR = Path(__file__).resolve().parent
if str(_SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS_DIR))

import chem_formula  # noqa: E402

REPO_ROOT = _SCRIPTS_DIR.parent


def _safe_rel(path: Path) -> str:
    """``path`` relative to the repo when possible; else its absolute string."""
    try:
        return str(path.resolve().relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


# Verdict classes that should fail an --enforce run.
# ADAPTER_ERROR is fatal: a configured adapter that fails to LOAD must never be
# silently downgraded to SKIPPED_NO_ADAPTER (which would let an enforce run pass
# while checking nothing). MISSING_COLUMN is likewise fatal: a configured
# id/label column that is absent from a populated tabular target used to be a
# stderr-only warning, so enforce exited 0 even though the pair was never
# checked (Engine-B false-green). MISSING_GLOB is emitted for a ``required: true``
# target whose glob matched no files (an expected artifact wasn't built).
_ERROR_VERDICTS = {
    "MISMATCH",
    "ID_NOT_FOUND",
    "EMPTY_LABEL",
    "MISSING_COLUMN",
    "MISSING_GLOB",
    "ADAPTER_ERROR",
    "UNKNOWN_PREFIX",
    # A waived (curator-intended) label that has no plausible relationship to
    # the term it grounds: element skeletons conflict, or no content word is
    # shared. This is the class the blanket waiver used to hide.
    "IMPLAUSIBLE_LABEL",
    # An unresolvable accession numerically beyond the ontology's real range —
    # a foreign identifier (typically a PubChem CID) wearing an OBO prefix.
    "ID_OUT_OF_RANGE",
}

# Reported, actionable, but NOT fatal: the grounding is correct and only the
# label lost its subscript glyphs upstream ("NaCO3" for Na2CO3). Repairing the
# name is a data-cleanup task, not a mapping error, so it must not fail enforce.
_WARN_VERDICTS = {"LABEL_SUBSCRIPTS_LOST"}

# Path segments under which a `term`/`chebi_term` label-waiver does NOT apply:
# organism (NCBITaxon) and environment (ENVO) groundings must carry the canonical
# ontology label. Everywhere else a waived key is an INGREDIENT grounding whose
# label is a curator formula/common-name (CHEBI "NaCl", FOODON "Yeast extract",
# UBERON "Calf brains") and stays waived regardless of ontology.
_CANONICAL_LABEL_CONTEXTS = (
    "target_organisms",
    "source_environment",
)

# Verdicts that are accepted (do NOT get recorded as findings and never fail
# enforce). OK_ID_ONLY is a pass: the id resolved and the slot's label was
# intentionally waived (curator-intended formula/common name). OK_EXCEPTION is a
# pass: the exact (id, label) pair is on the target's ``exceptions`` allow-list —
# a curator-accepted residual (obsolete-no-successor, no clean term yet, id
# absent from the current ontology snapshot) with a documented ``reason``.
_OK_VERDICTS = {"OK_CANONICAL", "OK_SYNONYM", "OK_ID_ONLY", "OK_EXCEPTION"}
# Benign skips: not OK (still surfaced in the report) but never fail enforce.
_SKIP_VERDICTS = {"SKIPPED_NO_ADAPTER", "SKIPPED_EMPTY_ADAPTER"}

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

        Peeks a single entity (O(1)) rather than counting.

        When ``entities()`` yields nothing the db is a clean empty (valid schema,
        no rows) and is treated as an empty stub. When ``entities()`` *raises*
        (e.g. ``no such table: node``) we do NOT trust the error text alone —
        a partially-migrated or corrupt LIVE ontology (real tables, one missing)
        raises the same way, and masking it as a benign skip would let real drift
        pass an enforce run (the exact false-pass this guards against). We only
        return True when ``_is_uninitialized_stub`` POSITIVELY confirms the
        backing sqlite is an uninitialized stub (0 bytes / 0 tables); otherwise
        return False so the prefix's rows surface as ID_NOT_FOUND/error verdicts.
        """
        try:
            return next(iter(adapter.entities()), None) is None
        except Exception as exc:  # pragma: no cover - environment dependent
            if AdapterPool._is_uninitialized_stub(adapter):
                return True
            print(f"  ! emptiness probe failed for {key}: {exc}", file=sys.stderr)
            return False

    @staticmethod
    def _is_uninitialized_stub(adapter: Any) -> bool:
        """Positively confirm the adapter's sqlite backing store is an
        uninitialized stub — a 0-byte file or a sqlite with NO tables at all.

        Anything that has tables is a real (possibly broken/partial) db, not a
        benign stub, and must not be masked. Returns False on any uncertainty
        (path unresolvable, non-sqlite backend, probe error) so the caller never
        silently downgrades a real defect to a skip.
        """
        url = getattr(getattr(adapter, "engine", None), "url", None)
        db_path = getattr(url, "database", None)
        if not db_path:
            return False  # not a resolvable sqlite file → don't risk masking
        try:
            p = Path(db_path)
            if not p.exists():
                return False
            if p.stat().st_size == 0:
                return True  # 0-byte stub (OAK's sqlite:obo:micro shape)
            import sqlite3

            con = sqlite3.connect(f"file:{p}?mode=ro", uri=True)
            try:
                n = con.execute(
                    "SELECT count(*) FROM sqlite_master WHERE type='table'"
                ).fetchone()[0]
            finally:
                con.close()
            return n == 0
        except Exception:  # pragma: no cover - environment dependent
            return False


_LABEL_CACHE: dict[tuple[int, str, str, bool], tuple[str | None, set[str], bool]] = {}
# One bulk-loaded formula lookup per adapter (see chem_formula.build_formula_lookup).
_FORMULA_LOOKUPS: dict[int, Any] = {}


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
    cache_key = (id(adapter), curie, scope, include_synonyms)
    if cache_key in _LABEL_CACHE:
        return _LABEL_CACHE[cache_key]
    try:
        canonical = adapter.label(curie)
    except Exception:
        canonical = None
    if canonical is None:
        _LABEL_CACHE[cache_key] = (None, set(), False)
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
    _LABEL_CACHE[cache_key] = (canonical, accepted, True)
    return canonical, accepted, True


def _plausibility_verdict(
    *,
    label: str,
    canonical: str | None,
    accepted: set[str],
    adapter: Any,
    lookup_curie: str,
    formula_lookup: Any = None,
) -> tuple[str, str]:
    """Decide whether a waived (curator-intended) label is *plausible* for its id.

    The waiver exists so curators can write "Distilled water" on CHEBI:15377 or
    "NaCl" on CHEBI:26710 without churn. It must not extend to a label that has
    nothing to do with the term — "MnCl .4H O" on 2-hydroxybenzoyl-AMP.

    Two independent ways to pass, either sufficient:
      * FORMULA — the label parses as a chemical formula whose element skeleton
        matches the term's molecular formula (hydration and lost subscripts
        tolerated; see ``chem_formula``).
      * LEXICAL — the label shares a content word with the canonical label or
        any accepted synonym.

    Returns (verdict, detail). Anything that parses as a formula and *conflicts*
    is rejected outright; a label we cannot judge at all is accepted, so the
    gate never fails on absent evidence.
    """
    if formula_lookup is None:
        akey = id(adapter)
        if akey not in _FORMULA_LOOKUPS:
            _FORMULA_LOOKUPS[akey] = chem_formula.build_formula_lookup(adapter)
        formula_lookup = _FORMULA_LOOKUPS[akey]
    formula = formula_lookup(lookup_curie) or ""


    if formula and chem_formula.looks_like_formula(label):
        cmp = chem_formula.compare_formulas(label, formula)
        if cmp in ("MATCH", "HYDRATE_RELAXED"):
            return "OK_ID_ONLY", f"formula {cmp.lower()}"
        if cmp == "SUBSCRIPTS_LOST":
            # Correct grounding, damaged label — flag for name repair, not as a
            # mapping error.
            return "LABEL_SUBSCRIPTS_LOST", f"same elements as {formula}, wrong counts"
        if cmp == "CONFLICT":
            return "IMPLAUSIBLE_LABEL", f"label elements conflict with {formula}"

    # Lexical fallback: any shared content word. Deliberately permissive —
    # tightening it (requiring two shared words or head-word agreement) was
    # measured at 26k false positives, because correct chemical names routinely
    # share only the stem: "L-Cysteine HCl x H2O" vs "L-cysteine hydrochloride
    # hydrate" shares just "cysteine". The cost is that a one-word overlap on a
    # wrong term slips through ("Magnesium citrate" on "magnesium dihydroxide");
    # that residue is left to curation rather than paid for 26k times over.
    label_words = {w for w in re.split(r"[^a-z0-9]+", normalize(label)) if len(w) > 2}
    if not label_words:
        # No comparable content (blank or purely numeric label). The id resolved,
        # and an absent label is EMPTY_LABEL's business, not plausibility's.
        return "OK_ID_ONLY", "no comparable label content"
    for candidate in {normalize(canonical or "")} | accepted:
        cand_words = {w for w in re.split(r"[^a-z0-9]+", candidate) if len(w) > 2}
        if label_words & cand_words:
            return "OK_ID_ONLY", "shares a term word"

    # No lexical support and no formula agreement. Formula evidence being
    # UNAVAILABLE is not innocence: a formula-shaped label grounded to a term
    # that publishes no formula (a polymer, a FOODON class) is unverifiable in
    # both directions, which is exactly how "ZnCl .6H O" sat undetected on
    # peptidoglycosaminoglycan. Flag it rather than wave it through.
    if chem_formula.looks_like_formula(label) and not formula:
        return ("IMPLAUSIBLE_LABEL",
                f"formula-style label, but '{canonical or ''}' publishes no "
                "molecular formula — grounding cannot be verified either way")
    return "IMPLAUSIBLE_LABEL", f"no word shared with '{canonical or ''}'"


def classify(
    *,
    curie: str,
    label: str,
    adapter: Any,
    policy: str,
    scope: str,
    lookup_curie: str | None = None,
    label_waived: bool = False,
    waiver_mode: str = "id_only",
    max_accession: int | None = None,
    formula_lookup: Any = None,
) -> dict[str, Any]:
    """Classify one (id, label) pair into a verdict dict.

    ``curie`` is reported verbatim; ``lookup_curie`` (when given) is the
    case-normalized CURIE actually passed to the adapter so that, e.g., a
    lowercase ``mesh:`` row resolves against OAK's uppercase ``MESH:`` ids.
    Synonyms are only built when the policy actually consults them.

    ``label_waived`` marks slots that carry curator-intended formula/common
    names (e.g. CHEBI:15377 "Distilled water"): id existence is still
    enforced (ID_NOT_FOUND fires for a bogus id) but the canonical-label
    match is skipped — a resolvable id yields OK_ID_ONLY regardless of label.
    """
    # A waived label under the `plausible` mode still needs synonyms — they are
    # what the lexical half of the plausibility check compares against.
    plausible_mode = label_waived and waiver_mode == "plausible"
    # Plausibility asks a different question from policy conformance: "is this
    # label related to this term at all?" Synonyms answer it, so they are loaded
    # even under `policy: canonical`, which otherwise skips them. Without this,
    # every legitimate common name ("Vitamin B12" for cyanocob(III)alamin,
    # "Tween 80" for polysorbate 80) is a false positive.
    include_synonyms = plausible_mode or (
        (policy != "canonical") and not label_waived
    )
    canonical, accepted, found = accepted_labels(
        adapter, lookup_curie or curie, scope, include_synonyms=include_synonyms
    )
    base = {"id": curie, "label": label, "canonical": canonical or ""}
    if not found:
        # An unresolvable accession above the ontology's real range is almost
        # always a foreign identifier wearing an OBO prefix (PubChem CIDs reach
        # 8 digits; CHEBI does not), which is a different repair from a dead
        # legacy accession — so report it distinctly.
        if max_accession is not None:
            local = (lookup_curie or curie).split(":", 1)[-1]
            if local.isdigit() and int(local) > max_accession:
                return {**base, "verdict": "ID_OUT_OF_RANGE"}
        return {**base, "verdict": "ID_NOT_FOUND"}
    if label_waived:
        if not plausible_mode:
            # Legacy behaviour: id resolved, curator label accepted as-is.
            return {**base, "verdict": "OK_ID_ONLY"}
        verdict, detail = _plausibility_verdict(
            label=label, canonical=canonical, accepted=accepted,
            adapter=adapter, lookup_curie=lookup_curie or curie,
            formula_lookup=formula_lookup,
        )
        return {**base, "verdict": verdict, "detail": detail}
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
    # body[0] is the header; data rows begin at the next physical line. Exclude
    # truly-empty lines: csv.DictReader skips them (yields no row), so counting
    # them here would shift every subsequent locator one line early. An
    # all-whitespace line is NOT skipped by DictReader, so it stays counted.
    data_line_numbers = [phys for phys, text in body[1:] if text.rstrip("\r\n") != ""]
    reader = csv.DictReader(lines, delimiter=delim)
    return list(reader.fieldnames or []), list(reader), data_line_numbers


def iter_tabular(
    path: Path,
    fmt: str,
    pairs: list[list[str]],
    label_waived_cols: frozenset[str] = frozenset(),
) -> Iterator[tuple[str, str, str, bool, str | None]]:
    """Yield (locator, id, label, label_waived, verdict_override) for each pair.

    ``verdict_override`` is normally ``None`` (the caller classifies the pair).
    For a configured id column that is ABSENT from a populated file it is
    ``"MISSING_COLUMN"`` — an ERROR-class verdict, so enforce no longer
    false-greens on column drift (it used to be a stderr-only warning that the
    caller never saw as a finding). ``label_waived`` is True when the pair's id
    column is listed in ``label_waived_cols`` (curator-intended label slot).
    """
    fields, rows, line_numbers = _read_tabular_rows(path, fmt)
    field_set = set(fields)
    # Keep any pair whose id column exists; a missing label column is allowed
    # so an id present without its label still gets an EMPTY_LABEL verdict
    # rather than being silently dropped.
    usable = [(i, l) for (i, l) in pairs if i in field_set]
    # RISK (fixed): a configured pair whose ID or LABEL column is absent must
    # NOT vanish silently. When the file has data rows, emit a MISSING_COLUMN
    # ERROR finding per absent column so an enforce run FAILS instead of
    # passing while checking nothing. (Still also warn to stderr for context.)
    if rows:
        for (i, l) in pairs:
            missing = [c for c in (i, l) if c not in field_set]
            if missing:
                print(
                    f"  ! {_safe_rel(path)}: configured id/label pair "
                    f"[{i}/{l}] — missing column(s) {missing}; "
                    f"present columns: {sorted(field_set)}",
                    file=sys.stderr,
                )
                yield (
                    f"columns [{i}/{l}]",
                    f"missing:{','.join(missing)}",
                    f"present:{sorted(field_set)}",
                    False,
                    "MISSING_COLUMN",
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
            waived = id_col in label_waived_cols
            yield f"line {line_no} [{id_col}/{label_col}]", curie, label, waived, None


def _walk_yaml(
    node: Any,
    pairs: list[tuple[str, str]],
    path: str,
    exclude_keys: frozenset[str] = frozenset(),
    label_waived_keys: frozenset[str] = frozenset(),
    waived: bool = False,
) -> Iterator[tuple[str, str, str, bool, str | None]]:
    if isinstance(node, dict):
        for id_key, label_key in pairs:
            # An id present without its sibling label must still be checked
            # (yields EMPTY_LABEL), so we do NOT require label_key to exist.
            if id_key in node:
                curie = node.get(id_key)
                if isinstance(curie, str) and curie.strip():
                    label = node.get(label_key)
                    label = label if isinstance(label, str) else ""
                    cur = curie.strip()
                    # Scope the label waiver to INGREDIENT groundings by context.
                    # The waiver exists for curator formula/common-name labels on
                    # ingredient terms (CHEBI "NaCl", FOODON "Yeast extract",
                    # UBERON "Calf brains"). The `term` key is reused on organism
                    # (target_organisms) and environment (source_environment)
                    # blocks, whose labels MUST stay canonical (per the skill
                    # spec) — so a `term`/`chebi_term` waiver does NOT apply when
                    # the term sits in an organism/environment context, even
                    # though the key name matches. Keying on context (not the id
                    # prefix) keeps curator ingredient labels of every ontology
                    # waived while still canonical-checking taxon/environment.
                    in_canonical_ctx = any(seg in path for seg in _CANONICAL_LABEL_CONTEXTS)
                    effective_waived = waived and not in_canonical_ctx
                    yield f"{path}.{id_key}", cur, (label or "").strip(), effective_waived, None
        for k, v in node.items():
            # Skip excluded grounding blocks entirely (no checks at all).
            if k in exclude_keys:
                continue
            # label_waived_keys: descend, but mark everything under this key as
            # label-waived so its id/label dicts get id-existence-only checking
            # (curator-intended formula/common names, e.g. CHEBI:15377
            # "Distilled water" under a `term:` block). ``waived`` is sticky
            # for the subtree so a nested id/label pair stays waived.
            child_waived = waived or (k in label_waived_keys)
            yield from _walk_yaml(
                v, pairs, f"{path}.{k}", exclude_keys, label_waived_keys, child_waived
            )
    elif isinstance(node, list):
        for idx, item in enumerate(node):
            yield from _walk_yaml(
                item, pairs, f"{path}[{idx}]", exclude_keys, label_waived_keys, waived
            )


def iter_yaml(
    path: Path,
    pairs: list[list[str]],
    exclude_keys: frozenset[str] = frozenset(),
    label_waived_keys: frozenset[str] = frozenset(),
) -> Iterator[tuple[str, str, str, bool, str | None]]:
    """Yield (locator, id, label, label_waived, verdict_override) from a YAML
    doc by recursively finding dicts that carry an id key (and, when present,
    its sibling label key)."""
    try:
        doc = yaml.safe_load(path.read_text())
    except Exception as exc:  # pragma: no cover
        print(f"  ! failed to parse {path}: {exc}", file=sys.stderr)
        return
    yield from _walk_yaml(
        doc, [(a, b) for a, b in pairs], path.name, exclude_keys, label_waived_keys
    )


# -- exceptions allow-list ------------------------------------------------

def load_exceptions(target: dict[str, Any]) -> set[tuple[str, str]]:
    """Return the (curie, normalized_label) pairs the target accepts as-is.

    The ``exceptions`` field on a target is a list of mappings, each with at
    least ``id`` and ``label``. Optional ``reason`` is documentation only;
    pairs are matched on (id, normalized(label)) so a missing or alternative
    casing for ``reason`` doesn't affect matching. A target with no
    ``exceptions`` key yields an empty set (no-op), so repos that don't use the
    allow-list are unaffected.
    """
    out: set[tuple[str, str]] = set()
    for entry in target.get("exceptions") or []:
        curie = str(entry.get("id", "")).strip()
        label = str(entry.get("label", ""))
        if curie:
            out.add((curie, normalize(label)))
    return out


# -- driver ---------------------------------------------------------------

def load_config(config_path: Path) -> dict[str, Any]:
    cfg = yaml.safe_load(config_path.read_text())
    if not isinstance(cfg, dict):
        raise SystemExit(f"Config is not a mapping: {config_path}")
    cfg.setdefault("adapters", {})
    cfg.setdefault("ignored_prefixes", [])
    cfg.setdefault("synonym_scope", "exact_related")
    cfg.setdefault("targets", [])
    cfg.setdefault("max_accession", {})
    cfg.setdefault("plausibility_severity", "warn")
    return cfg


def run(config_path: Path, report_path: Path | None) -> int:
    cfg = load_config(config_path)
    pool = AdapterPool(cfg["adapters"])
    default_scope = cfg["synonym_scope"]
    # Explicitly-ignored non-ontology prefixes (cas:, MIM:, kgmicrobe.compound: …).
    # A prefixed id whose prefix is neither a configured adapter NOR listed here
    # is a typo / unexpected prefix → UNKNOWN_PREFIX (ERROR), not a silent skip.
    ignored_prefixes_cf = {str(p).casefold() for p in cfg["ignored_prefixes"]}
    # Per-ontology numeric accession ceiling. An unresolvable id above the
    # ceiling is a foreign identifier wearing an OBO prefix (PubChem CIDs run to
    # 8 digits) rather than a retired accession — a different repair.
    max_accessions: dict[str, int] = {
        str(k): int(v) for k, v in (cfg.get("max_accession") or {}).items()
    }
    # Plausibility is a NEW gate over pre-existing data, so it defaults to
    # `warn`: reported in full, but not build-breaking. Flip to `error` once the
    # backlog it surfaces is cleared — the repo's standard report-then-enforce
    # rollout. ID_OUT_OF_RANGE stays fatal regardless: it is a strictly better
    # diagnosis of an id that already failed as ID_NOT_FOUND.
    severity = str(cfg.get("plausibility_severity", "warn")).lower()
    error_verdicts = set(_ERROR_VERDICTS)
    if severity != "error":
        error_verdicts.discard("IMPLAUSIBLE_LABEL")

    findings: list[dict[str, Any]] = []
    counts: dict[str, int] = {}
    for target in cfg["targets"]:
        name = target.get("name", target.get("glob", "?"))
        kind = target.get("kind", "tabular")
        policy = target.get("policy", "canonical_or_synonym")
        scope = target.get("synonym_scope", default_scope)
        pairs = target.get("pairs", [])
        exclude_keys = frozenset(target.get("exclude_keys", []) or [])
        label_waived_keys = frozenset(target.get("label_waived_keys", []) or [])
        # `id_only` (default) preserves the historical blanket waiver; set
        # `plausible` to additionally require that a waived label bear some
        # relationship to the term it grounds.
        waiver_mode = str(target.get("label_waiver_mode", "id_only"))
        # Per-target severity. Defaults to `error` (historical behaviour). A
        # NEWLY-ADDED target over pre-existing data can start at `warn` so its
        # backlog is reported without breaking the build, then be flipped once
        # cleared — the repo's standard report-then-enforce onboarding.
        target_severity = str(target.get("severity", "error")).lower()
        exceptions = load_exceptions(target)
        required = bool(target.get("required", False))
        globs = target.get("glob")
        glob_list = globs if isinstance(globs, list) else [globs]
        paths: list[Path] = []
        for g in glob_list:
            paths.extend(sorted(REPO_ROOT.glob(g)))
        if not paths:
            # RISK (fixed): a `required: true` target whose glob matches NO
            # files means an expected artifact (e.g. output/*.sssom.tsv) was
            # never built. That used to skip with exit 0, so validate-products
            # greened on a missing product. Emit a MISSING_GLOB ERROR finding.
            if required:
                print(f"  ! {name}: REQUIRED target — no files match {glob_list}")
                rec = {"id": ",".join(str(g) for g in glob_list), "label": "",
                       "canonical": "", "verdict": "MISSING_GLOB"}
                counts["MISSING_GLOB"] = counts.get("MISSING_GLOB", 0) + 1
                findings.append({
                    "surface": name, "file": "(no match)",
                    "locator": f"glob {glob_list}", "policy": policy, **rec,
                })
            else:
                print(f"  - {name}: no files match {glob_list}")
            continue
        for path in paths:
            rel = _safe_rel(path)
            if kind == "yaml":
                pairs_iter = iter_yaml(path, pairs, exclude_keys, label_waived_keys)
            else:
                pairs_iter = iter_tabular(
                    path, target.get("format", "tsv"), pairs, label_waived_keys
                )
            for locator, curie, label, label_waived, verdict_override in pairs_iter:
                if verdict_override is not None:
                    rec = {"id": curie, "label": label, "canonical": "",
                           "verdict": verdict_override}
                else:
                    prefix = prefix_of(curie)
                    adapter = pool.get(prefix)
                    if adapter is None:
                        # No configured adapter for this prefix. Distinguish an
                        # explicitly-ignored non-ontology prefix (benign skip)
                        # from an unexpected/typoed ontology prefix (ERROR). An
                        # id with no CURIE prefix at all (UNMAPPED_0001) stays a
                        # benign skip — it isn't claiming to be an ontology term.
                        if prefix is not None and prefix.casefold() not in ignored_prefixes_cf:
                            verdict = "UNKNOWN_PREFIX"
                        else:
                            verdict = "SKIPPED_NO_ADAPTER"
                        rec = {"id": curie, "label": label, "canonical": "",
                               "verdict": verdict}
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
                            label_waived=label_waived, waiver_mode=waiver_mode,
                            max_accession=max_accessions.get(prefix),
                        )
                # Curator-accepted residual: an EXACT (id, label) pair on the
                # target's ``exceptions`` allow-list is accepted as OK_EXCEPTION
                # (non-error, documented ``reason``). Applies ONLY to label/id
                # residuals (MISMATCH / ID_NOT_FOUND) — never to structural
                # errors (UNKNOWN_PREFIX, ADAPTER_ERROR, MISSING_COLUMN,
                # MISSING_GLOB, EMPTY_LABEL), which signal real defects rather
                # than a knowingly-accepted label. The match is exact, so a
                # different wrong label on the same id still fails as MISMATCH.
                # IMPLAUSIBLE_LABEL and LABEL_SUBSCRIPTS_LOST are label/id
                # residuals of exactly the kind the allow-list exists for — a
                # correct grounding the heuristic cannot see is correct
                # ("soy peptone" on FOODON "vegetable protein, hydrolyzed"
                # shares no word) — so they are waivable too. Structural errors
                # (UNKNOWN_PREFIX, ADAPTER_ERROR, MISSING_*) remain unwaivable.
                if rec["verdict"] in (
                    "MISMATCH", "ID_NOT_FOUND", "IMPLAUSIBLE_LABEL",
                    "LABEL_SUBSCRIPTS_LOST", "ID_OUT_OF_RANGE",
                ) and (curie, normalize(label)) in exceptions:
                    rec["verdict"] = "OK_EXCEPTION"
                counts[rec["verdict"]] = counts.get(rec["verdict"], 0) + 1
                if rec["verdict"] not in _OK_VERDICTS | _SKIP_VERDICTS:
                    findings.append({
                        "severity": target_severity,
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
        "OK_ID_ONLY",
        "OK_EXCEPTION",
        "MISMATCH",
        "ID_NOT_FOUND",
        "EMPTY_LABEL",
        "MISSING_COLUMN",
        "MISSING_GLOB",
        "ADAPTER_ERROR",
        "UNKNOWN_PREFIX",
        "IMPLAUSIBLE_LABEL",
        "ID_OUT_OF_RANGE",
        "LABEL_SUBSCRIPTS_LOST",
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
                 "canonical_label", "verdict", "severity", "policy", "detail"]
            )
            for f in findings:
                w.writerow([
                    f["surface"], f["file"], f["locator"], f["id"],
                    f["label"], f["canonical"], f["verdict"],
                    f.get("severity", "error"), f["policy"], f.get("detail", ""),
                ])
        print(f"\nWrote {len(findings)} flagged pairs to {_safe_rel(report_path)}")
        return 0

    errors = [f for f in findings
              if f["verdict"] in error_verdicts
              and f.get("severity", "error") == "error"]
    if errors:
        print(f"\n❌ {len(errors)} id↔label correspondence error(s):")
        for f in errors[:50]:
            print(f"  {f['verdict']}: {f['file']} {f['locator']} "
                  f"{f['id']} label='{f['label']}' canonical='{f['canonical']}'")
        if len(errors) > 50:
            print(f"  ... {len(errors) - 50} more")
        return 2
    warned = [f for f in findings
              if f["verdict"] in (_ERROR_VERDICTS | _WARN_VERDICTS)
              and not (f["verdict"] in error_verdicts
                       and f.get("severity", "error") == "error")]
    if warned:
        print(f"\n⚠️  {len(warned)} non-blocking id↔label warning(s) "
              f"(plausibility_severity={severity}); see the report for detail.")
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
