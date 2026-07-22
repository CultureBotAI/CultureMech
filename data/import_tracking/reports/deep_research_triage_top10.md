# Deep-Research Triage — Top 10

Drafted from `deep_research_priority_top100.json` (regenerated after the archaeal
recategorization of #114; 15,496 candidates scored, already-researched records
filtered out).

Nine are **bacterial** and one is **archaeal** — #3 *Sulfolobus*, now correctly
filed under `archaea/` and scored with the archaeal multiplier (×0.95), which is
why it sits at 87.4 rather than at the top. All ten have **0 real target
organisms** (max information gain), carry **fully-quantified recipes** (every
ingredient has a concentration → clean recipe diff against the publication), and
are anchored to a citable source ID (TOGO / JCM). A homogeneous, high-confidence
batch — safe to run through phase-1.

| # | Score | Domain | Recipe | Source ID | Ingredients | Action |
|--:|------:|--------|--------|-----------|------------:|--------|
| 1 | 92.0 | bacterial | `wilkins_chalgren_anaerobe_broth_n2_co2_for_dsm_15567` | TOGO:M2735 | 15 | Run phase-1 |
| 2 | 89.0 | bacterial | `syntrophomonas_medium_for_syntrophospora_cellicola_19j_3` | mediadive.medium:J519 | 25 | Run phase-1 |
| 3 | 87.4 | archaea | `sulfolobus_medium_for_dsm_9790` | TOGO:M2323 | 16 | Run phase-1 |
| 4 | 87.0 | bacterial | `leuconostoc_oenos_medium` | TOGO:M1620 | 11 | Run phase-1 |
| 5 | 87.0 | bacterial | `clostridium_thermocellum_medium_d58_medium` | TOGO:M1766 | 14 | Run phase-1 |
| 6 | 87.0 | bacterial | `pelobacter_carbinolicus_medium` | TOGO:M1788 | 22 | Run phase-1 |
| 7 | 87.0 | bacterial | `medium_for_ectothiorhodospira` | TOGO:M1789 | 24 | Run phase-1 |
| 8 | 87.0 | bacterial | `pelobacter_acetylenicus_medium` | TOGO:M1791 | 22 | Run phase-1 |
| 9 | 87.0 | bacterial | `desulfovibrio_medium` | TOGO:M1796 | 13 | Run phase-1 |
| 10 | 87.0 | bacterial | `medium_for_strains_ja145_ja193_ja310_ja334_ja415_ja430_ja447_and_ja643` | TOGO:M1836 | 11 | Run phase-1 |

## Notes for the curator

- **#3 `sulfolobus_medium_for_dsm_9790` is the only archaeon** in this batch —
  recategorized to `archaea/` in #114 (it was mis-filed under `bacterial/`, which
  had put it artificially at #1 with the bacterial ×1.00 multiplier).
- **#2 is the richest recipe (25 ingredients, JCM-anchored).** Best single
  candidate for exercising the parent-child MediaVariant recipe-diff path.
- **#4 `Leuconostoc oenos`** is a reclassified name (now *Oenococcus oeni*) — the
  phase-2 follow-up should reconcile the current NCBITaxon.
- **#7 `medium_for_ectothiorhodospira`** names a *genus*, not a strain — slightly
  higher chance phase-1 returns multiple candidate organisms.
- **#6/#8 are both *Pelobacter*** (carbinolicus, acetylenicus) — run them together
  so the shared base recipe is diffed once.

## How to run

```bash
# Dry-run the top 5 first to audit phase-1 prompts:
just research-media-edison-batch \
    data/import_tracking/reports/deep_research_priority_top100.json \
    --limit 5 --dry-run

# Live phase-1 on the top 10:
just research-media-edison-batch \
    data/import_tracking/reports/deep_research_priority_top100.json \
    --limit 10

# Then invoke the deep-research-medium skill per result for phase-2.
```
