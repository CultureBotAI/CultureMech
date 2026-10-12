# Adversarial Review

## Resolved In This Repair

- **Stock versus medium basis:** the former flattened calcium, magnesium and
  iron entries did not describe the source's separately prepared stocks. The
  applied nine-record plan separates their source-explicit strengths and batch doses.
- **M17 lactose:** 8.0 g/L describes the finished medium, not the filtered stock.
  Its existing direct amount is retained with stage-specific evidence. No stock
  strength, stock volume or final-medium volume is invented.
- **Water percentages:** 990, 1000 and 950 ml water are batch inputs, not 990%,
  1000% or 950% v/v. Standalone water fields are corrected; missing medium water
  inputs are restored without implying final volume.
- **Iron carrier versus pH reagent:** 0.2 N H2SO4 belongs to the iron stock;
  4 N H2SO4 adjusts the base to pH 2.2. Neither reagent dose is quantified.
  Normalities remain source text because the unit enum cannot express them.
- **Preparation labels:** the entire 670 preparation must not be labeled
  filter-sterilized, nor static incubation labeled MIX. The full combined
  instruction remains under DISSOLVE; the incubation instruction moves to notes.
- **Historical migration coupling:** the old 670 migration tests read mutable
  live recipes, forcing a flat parent inventory after a valid stock repair.
  Tests now use five byte-preserved inputs from commit
  `f8af2562c3ae51d5f9ed01a484f4a2971b6cd80f`. The legacy mutator remains unchanged
  and a regression test confirms it refuses a stock-structured parent. This
  tests historical behavior, not the scientific correctness of its variants.

## Still Open

The official [670 recipe](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium670.pdf)
was text-inspected again for this repair. Its strain alternatives are not merely
pH changes. Current `for_dsm_9463.yaml`, `for_dsm_9466.yaml` and
`for_dsm_9467.yaml` retain base iron, while the source requires its omission and
different sulfur/glucose/yeast additions. The 9466 record also says pH 3.5 while
the current PDF says 3.0. All four linked strain records retain historical
`ingredients_curated` flags. These source/version and formulation conflicts need
an explicit variant follow-up, including the parent's relationship descriptions;
this base-medium correction does not endorse them or rewrite their history.

The pinned [KOMODO cohort plan](../20261007-komodo-media-2000-2500/plan.json)
also contains the original 670.3 mapping row with `3.5, H2SO4` and its link to
DSMZ 670. The pH difference therefore exists between the captured sources, not
just between a local YAML and a source. Preserve that disagreement when selecting
the formulation/version for the next repair; do not silently treat 3.5 as an
unsupported local typo. The newly hashed [PDF captures](next-variant-source-captures.json)
retain the exact 670, 673 and 266 page text for that investigation.

The inherited [673/266 conflict](../20261007-dsmz650-752-762-preparations/next-stock-candidates.md)
remains unresolved. No numerical correction to those three records is applied.

Full corpus coverage, actual-group merge retention, global merge/freshness gates
and bibliography validation remain separate requirements. Passing source and
schema checks is not publication approval. See the terminal validation artifacts
and README for actual results rather than inferring a pass from this review.
