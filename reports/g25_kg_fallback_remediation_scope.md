# G25 — kg_fallback chebi_term remediation: scope

**Status:** scoped (not yet implemented)
**Source:** surfaced by `scripts/audit_chebi_consistency.py` (G23) during the
grounding audit.

## Problem

The `chebi_term` field carries a large low-confidence layer produced by an
automated KG-embedding matcher:

| `chebi_term.match_type` | fields | reliability |
|---|---|---|
| `exact_match` | 10,738 | trustworthy |
| `kg_fallback` | 21,146 | **low (≈0.7 conf), frequently wrong** |
| `synonym_match_ambiguous` | 2,746 | low |
| (none) | 106 | unknown |

The `kg_fallback` + ambiguous layer is **61% of all `chebi_term` fields** and is
often chemically wrong, e.g.:

- "Distilled water" → `CHEBI:6636` (**magnesium dichloride**), conf 0.7 — ×3,951
- "CaCl2 x 2 H2O" → `CHEBI:176843` (**Vitamin B12**) — ×1,439

The **primary `term` grounding is unaffected** (water's `term` is
`mediadive.compound:4`). But any downstream consumer reading `chebi_term`
(KG-Microbe, role/chemistry inference) is polluted.

## Scoping numbers (measured)

- Fallback/ambiguous fields to remediate: **23,998**
- **Distinct labels: 772** ← the real work unit (cache by label, not by field)
- Occurrences whose label **already has a reliable grounding elsewhere in the
  corpus**: **19,707 (82%)** → fixable with **zero external calls**
- Distinct labels needing an **external** lookup: **~326**

Top fallback labels are all common, well-grounded compounds (distilled water,
yeast extract, CaCl2·2H2O, KH2PO4, MgSO4·7H2O, agar, glucose, …) — so the
internal-borrow tier carries the bulk.

## Approach — 3-tier pipeline (cache keyed on normalised label)

Reuse the mature name-normaliser already in
`scripts/enrich_sssom_with_ols.py` (`normalize_ingredient_name`,
formula→name, greek letters, salt/hydrate notation) for every label key.

**Tier 1 — internal consensus borrow (82%, 0 API calls).**
For each fallback field, look up the label's *reliable* grounding(s) elsewhere
in the corpus (primary CHEBI `term` or `exact_match` chebi_term). If there is a
single consensus CHEBI for that label → replace the wrong `kg_fallback`
chebi_term with it (`match_type: corpus_consensus`). If the label maps to >1
reliable CHEBI (the G23 same-name-multiple-CHEBI cases), defer to Tier 2.

**Tier 2 — external grounding (~326 distinct labels).**
Resolve the label against CHEBI with a confidence gate:
- **OAK**, local & scalable: `get_adapter("sqlite:obo:chebi")` (downloads once,
  then offline — no rate limits; verified `basic_search` resolves). Take a hit
  only when the label exact- or exact-synonym-matches a single CHEBI.
- **OLS4 REST** (`https://www.ebi.ac.uk/ols4/api/search?ontology=chebi&exact=true`)
  as a cross-check / tie-breaker and for labels OAK's release misses (verified).
- Accept a remap only when OAK and OLS **agree** on an exact match; record
  `match_type: oak_exact` / `ols_exact` + the source. 326 labels × 2 services is
  trivial (seconds–minutes) thanks to the label cache.

**Tier 3 — de-ground the unresolved.**
If neither internal nor external lookup yields a confident exact match, **remove
the wrong low-confidence `chebi_term`** (the primary `term` is untouched) rather
than keep a known-bad id. Flag the de-grounded labels for curator review.

A `--dry-run` + per-tier change report + `CurationEvent` per file, PyYAML
round-trip (surgical diffs) — same pattern as `migrate_chebi_regrounding.py`.

## Why this avoids the MIM trap

G24 showed that trusting one curated source wholesale (MIM) is unsafe — MIM
itself mis-grounds glycerol/casamino. Here the authority is **CHEBI itself via
OAK + OLS with agreement required**, and the safe fallback is **de-ground, not
guess**. Tier 1 also anchors 82% to the corpus's own reliable consensus.

## Tooling (all present / verified)

- `oaklib` (dep) — OAK CHEBI adapter; `sqlite:obo:chebi` for offline scale.
- `requests` (dep) — OLS4 REST.
- `scripts/enrich_sssom_with_ols.py` — name normalisation to reuse.
- **`id-label-correspondence` skill** — complementary: validates every
  `term.{id,label}` against the canonical OAK label; run it after remediation to
  confirm `chebi_term` ids now carry correct labels.

## Validation / exit criteria

1. `just check-chebi-grounding`: `kg_fallback` + ambiguous count → ~0; lower the
   CI baseline (currently 102) toward the new floor.
2. `id-label-correspondence` skill: 0 wrong-label `chebi_term`s.
3. `just validate-strict`: still 0 ERROR rows.
4. Re-run the G23 probe; Signal A (same-name-multiple-CHEBI) materially down.

## Effort & phasing

- **Phase 1 (S, high value):** Tier 1 internal borrow — fixes ~82% with no
  network, low risk. Deliver as its own PR; re-baseline the G23 gate.
- **Phase 2 (M):** Tier 2 OAK+OLS for ~326 labels + Tier 3 de-ground; cache +
  agreement gate; curator-review list for the residue.
- **Phase 3 (S):** lower the CI baseline; optionally wire the
  `id-label-correspondence` check into CI alongside `check-chebi-grounding`.

## Risks

- A wrong Tier-1 *consensus* (if the corpus's reliable layer is itself wrong for
  a label) — mitigate by requiring a single consensus id and spot-checking the
  top-N labels by volume before applying.
- OAK first-run downloads the CHEBI sqlite (~hundreds of MB) — one-time; cache in
  CI or pin a release.
- Synonym ambiguity (e.g. glucose anomers, vitamer forms) — require exact match,
  defer ambiguous to the curator list rather than auto-picking.
