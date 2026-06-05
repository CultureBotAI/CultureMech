# CHEBI grounding audit — ingredient term correctness

**Date:** 2026-06-05
**Trigger:** the MIM legacy→CHEBI migration emitted
`data/import_tracking/reports/mim_grounding_divergences.tsv` (500 CHEBI ids
where the CultureMech ingredient label and MIM's `preferred_term` /
`ontology_label` differ). This audit separates benign formatting differences
from **genuine mis-groundings** (a CHEBI id applied to a chemically *different*
compound) and quantifies their corpus impact.

## Headline

- **Instance validation (closed-mode, `just validate-strict`): 0 ERROR rows
  across 15,827 records.** The recent JCM ingestion, archaea recategorization,
  and the 120k-link MIM refresh introduced **no** schema-level instance errors.
- **Grounding correctness is a different, pre-existing problem.** ~2,300
  ingredient occurrences carry a CHEBI id that names a chemically different
  substance. These mappings predate this work (inherited from upstream
  MediaDive / source imports); the MIM divergence report is only the detector.

## Method

The divergence rows were filtered to drop benign classes — salt/hydrate/formula
variants (`NaCl`↔`Sodium Chloride`, `x 2 H2O`), spelling/i18n (`Cystein`,
`Biotine`, `glycerin`, `sulphate`), and established synonyms (`niacin`↔
`nicotinic acid`, `thioctic`↔`lipoic`). The residual was reviewed against the
authoritative CHEBI label (MIM `ontology_label`) using chemical knowledge, then
each confirmed mismatch was counted across `data/normalized_yaml/**` (`term`,
`chebi_term`, and the new `mediaingredientmech_chebi_term`).

## Confirmed mis-groundings

### Tier 1 — chemically wrong compound (high impact)

| CHEBI id | CHEBI actually denotes | Used in CultureMech for | Occurrences | Correct target |
|---|---|---|---|---|
| `CHEBI:78020` | heptacosanoate (C27 fatty acid) | **Casamino acids** (acid-hydrolysed casein) | ~822 | a mixture/`FOODON` term, not a single fatty-acid CHEBI |
| `CHEBI:131531` | pyridoxamine | **Pyridoxine·HCl** (different vitamin B6 vitamer) | 791 | pyridoxine hydrochloride (≠ pyridoxamine) |
| `CHEBI:15978` | *sn*-glycerol 3-phosphate | **Glycerol** | 140 | `CHEBI:17754` (glycerol) |
| `CHEBI:75211` | tannic acid | **MnSO₄·H₂O** (manganese(II) sulfate) | 128 | a manganese-sulfate CHEBI |
| `CHEBI:77732` | **cadmium** nitrate | **Ca(NO₃)₂** (calcium nitrate) | 52 | a calcium-nitrate CHEBI (wrong metal — toxicity-relevant) |

### Tier 2 — wrong species sharing an id / ambiguous

| CHEBI id | CHEBI denotes | Misused for | Occurrences | Note |
|---|---|---|---|---|
| `CHEBI:32149` | sodium sulfate (Na₂SO₄) | **Na₂SeO₄** (sodium **selenate**) | 216 (of 2,155; the other 1,939 Na₂SO₄ are correct) | selenate ≠ sulfate |
| `CHEBI:37583` | trisodium phosphate (Na₃PO₄) | "Sodium dihydrogen phosphate" (mono, 156) + "Sodium phosphate dibasic" (33) | 189 | three different sodium phosphates conflated on one id; MIM is also inconsistent here |
| `CHEBI:53258` | sodium citrate | a few "Citric acid" (free acid) entries | small | mostly correct (citrate salts); salt-vs-acid nuance |

**Total clearly-wrong ingredient occurrences: ~2,300** across Tiers 1–2.

## Why it matters

These feed KG-Microbe and any downstream chemistry/role inference. A medium
that lists "manganese sulfate" but resolves to *tannic acid*, or "calcium
nitrate" resolving to *cadmium nitrate*, will mislead trait/role analyses and
any toxicity- or metal-aware reasoning. The pyridoxine/pyridoxamine and
glycerol/glycerol-3-phosphate swaps are subtler but equally wrong biochemically.

## Recommended fixes

1. **Re-ground the Tier-1 ids** — these are unambiguous: remap the affected
   ingredients to the correct CHEBI (or, for Casamino acids, to a mixture term).
   A targeted `migrate_*` script keyed on `(term.id, preferred_term)` pairs is
   the right tool (idempotent, `--dry-run`, appends `CurationEvent`).
2. **Split shared ids** — for `CHEBI:32149` and `CHEBI:37583`, route by label:
   selenate→selenate CHEBI, mono/di/tri phosphate each to its own id.
3. **Add a grounding-consistency check** — flag any CHEBI id whose ingredient
   labels (after benign-normalisation) disagree with the CHEBI canonical name,
   as a recurring QC (extend `audit_schema.py` or a new `validate-terms` probe).
4. The upstream source (MediaDive compound→CHEBI table) likely carries the same
   errors; fixes here should be reported upstream to avoid re-import.

See `gap_fix_backlog.md` rows **G21–G23**.
