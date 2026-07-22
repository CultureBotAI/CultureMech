# Deep-Research Triage — Top 10

Drafted from `deep_research_priority_top100.json` (regenerated 2026-07-21;
15,496 candidates scored, already-researched records filtered out).

All ten are **bacterial**, all have **0 real target organisms** (max
information gain), all carry **fully-quantified recipes** (every ingredient
has a concentration → clean recipe diff against the publication), and all are
anchored to a citable source ID (TOGO / JCM). This is a homogeneous, high-
confidence batch — safe to run straight through phase-1.

| # | Score | Recipe | Source ID | Ingredients | Action |
|--:|------:|--------|-----------|------------:|--------|
| 1 | 92.0 | `sulfolobus_medium_for_dsm_9790` | TOGO:M2323 | 16 | Run phase-1 |
| 2 | 92.0 | `wilkins_chalgren_anaerobe_broth_n2_co2_for_dsm_15567` | TOGO:M2735 | 15 | Run phase-1 |
| 3 | 89.0 | `syntrophomonas_medium_for_syntrophospora_cellicola_19j_3` | JCM J519 | 25 | Run phase-1 |
| 4 | 87.0 | `leuconostoc_oenos_medium` | TOGO:M1620 | 11 | Run phase-1 |
| 5 | 87.0 | `thermoproteus_neutrophilus_medium` | TOGO:M1633 | 21 | Run phase-1 |
| 6 | 87.0 | `clostridium_thermocellum_medium_d58_medium` | TOGO:M1766 | 14 | Run phase-1 |
| 7 | 87.0 | `pelobacter_carbinolicus_medium` | TOGO:M1788 | 22 | Run phase-1 |
| 8 | 87.0 | `medium_for_ectothiorhodospira` | TOGO:M1789 | 24 | Run phase-1 |
| 9 | 87.0 | `pelobacter_acetylenicus_medium` | TOGO:M1791 | 22 | Run phase-1 |
| 10 | 87.0 | `desulfovibrio_medium` | TOGO:M1796 | 13 | Run phase-1 |

## Notes for the curator

- **#1, #6 name the strain but score orgs=0.** `dsm_9790` and
  `clostridium_thermocellum` have the taxon in the *medium* name but no
  populated `target_organisms` — expect deep-research to confirm and formally
  attach the strain-level association.
- **#3 is the richest recipe (25 ingredients, JCM-anchored).** Best single
  candidate for exercising the parent-child MediaVariant recipe-diff path.
- **#4 `Leuconostoc oenos`** is a reclassified name (now *Oenococcus oeni*) —
  the phase-2 follow-up should reconcile the current NCBITaxon.
- **#8 `medium_for_ectothiorhodospira`** names a *genus*, not a strain —
  slightly higher chance phase-1 returns multiple candidate organisms.

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
