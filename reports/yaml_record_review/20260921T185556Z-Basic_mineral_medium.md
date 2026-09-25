# YAML Record Review: Basic mineral medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/Basic_mineral_medium.yaml
- Started UTC: 2026-09-21T18:54:21Z
- Finished UTC: 2026-09-21T18:55:56Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path reviewed | `data/merge_yaml/merged/Basic_mineral_medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/basic_mineral_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:001096` |
| Name | `basic_mineral_medium` |
| Original name | `Basic mineral medium` |
| Source | DSMZ Medium 1615 via MediaDive |
| Merge status | Generated one-source merge from `basic_mineral_medium` |

## Validation

| Check | Result |
|---|---|
| Open schema | Passed with the no-project LinkML invocation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`, and the generated DSMZ 1615 merge. |
| Strict schema | Passed with the no-project invocation of `scripts/validate_strict.py`: 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validator | Passed with 0 reference checks because this MediaDive import has no populated `references` list or evidence objects. |
| Term validator | Passed with `linkml-term-validator validate-data` against the generated DSMZ 1615 merge. |
| Embedded curation history | Not checked: this repository documents `just validate-history` for the standalone `history/` tree, not a focused one-record `MediaRecipe.curation_history` check. |
| Project `just` wrappers | Not rerun here: direct `just validate-schema`, `just validate-strict`, and `just validate-terms` fail before target-specific validation in this checkout while the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13. The equivalent no-project Python 3.11 validators above exercised the target record. |

## Identity and Grounding

- The generated record denotes DSMZ Medium 1615, `Basic mineral medium`, and has the permanent ID `CultureMech:001096`.
- Exact gitignore-independent searches for `CultureMech:001096`, `mediadive.medium:1615`, and `DSMZ_Medium1615` covered `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`. They found the normalized owner, generated merge, generated indexes, registry rows, import reports, and source PDF URL, but no maintained local copy of the DSMZ PDF.
- The maintained normalized record and generated merge have the same scientific content; fixes belong in `data/normalized_yaml/bacterial/basic_mineral_medium.yaml`, followed by merge regeneration.
- Exact chemical grounding is mixed:
  - The major salts, acetate, phosphate buffer salts, methionine, EDTA, zinc sulfate, boric acid, cobalt chloride hexahydrate, sodium molybdate dihydrate, and the named vitamins with CHEBI terms are directionally consistent with the DSMZ names.
  - `Na-aspartate` and `B12` are still ungrounded.
  - `NiCl2 x 6 H2O` is grounded to `CHEBI:34887`, nickel dichloride, which drops the source hexahydrate.
  - `Thiamine` still carries a legacy `mediaingredientmech_term: MediaIngredientMech:000898` alongside its CHEBI term.

## Evidence

- The inspected DSMZ Medium 1615 PDF supports the record identity, final pH 7.0-7.2 for the K-P buffer, 1 mM MgSO4 x 7 H2O, 10 mM sodium acetate, 5% CaCl2 x 2 H2O added at 1 ml/L, 2 mM sodium aspartate, 50 uM L-methionine, a trace-element stock added at 1 ml/L, and a four-part vitamin mix.
- The generated final-medium rows for MgSO4 x 7 H2O, sodium acetate, CaCl2 x 2 H2O, Na-aspartate, L-methionine, K2HPO4, and KH2PO4 are consistent with the DSMZ stock volumes and molarities.
- The trace-element ingredients are stock-solution concentrations from a 1 L stock that should be dosed at 1 ml/L final medium. The generated record flattened EDTA, FeSO4 x 7 H2O, ZnSO4, MnCl2, H3BO3, CoCl2 x 6 H2O, CuCl2 x 5 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O at stock g/L values instead of final 1:1000 dilutions.
- The vitamin ingredients are concentrations inside four 100 ml vitamin stocks. The generated record flattened Thiamine, calcium pantothenate, biotin, PABA, nicotinic acid, pyridoxine, NaOH, folic acid, riboflavin, and B12 to top-level ingredient rows at stock values and lost the acidified, basic, neutral, and B12 sub-stock boundaries.
- Several preparation steps were imported as unscoped top-level operations. The record currently makes `Adjust pH to 3.0-4.0 with HCl` look like a final-medium instruction, but DSMZ scopes that pH only to the trace-element solution. The stock-solution filtration and vitamin mixing instructions likewise need to stay attached to their respective stocks.

## Completeness

- Consequential gaps:
  - The K-P buffer, trace-element solution, and four vitamin solutions are not modeled as stock solutions.
  - Nine trace-element rows and ten vitamin/basic-solution rows are not final-medium concentrations.
  - Water rows for the K-P buffer, trace-element stock, and vitamin stocks are absent.
  - Trace-element pH, 20 minute Schott-bottle sterilization, post-sterilization additions, methionine filter sterilization/neutralization, and vitamin stock filtration are not scoped to their source solution boundaries.
  - `NiCl2 x 6 H2O`, `B12`, `Na-aspartate`, and the legacy Thiamine MIM link need grounding review.
- Correctly empty optional slots:
  - `target_organisms`, `references`, and organism-growth evidence are empty because the inspected DSMZ formulation names no strain or growth outcome.
- Bounded negative searches:
  - Exact gitignore-independent searches found no local DSMZ 1615 PDF capture under `data`, `src`, `scripts`, `.claude`, `justfile`, and `CLAUDE.md`; the review fetched the PDF from the URL recorded in the YAML.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The trace-element stock was flattened into final medium at 1000x stock concentrations. | DSMZ says to add 1 ml/L Trace elements from a 1 L stock containing EDTA 5.00 g, FeSO4 x 7 H2O 2.00 g, ZnSO4 0.10 g, MnCl2 0.03 g, H3BO3 0.30 g, CoCl2 x 6 H2O 0.20 g, CuCl2 x 5 H2O 0.01 g, NiCl2 x 6 H2O 0.02 g, and Na2MoO4 x 2 H2O 0.02 g; the YAML uses those stock g/L values as top-level ingredient concentrations. | `data/normalized_yaml/bacterial/basic_mineral_medium.yaml`. |
| Major | The vitamin stocks were flattened into top-level ingredients at stock concentrations. | DSMZ defines four 100 ml vitamin stocks and instructs adding a mixed vitamin solution or 250 uL/L of each stock; the YAML imports Thiamine, calcium pantothenate, biotin, PABA, nicotinic acid, pyridoxine, NaOH, folic acid, riboflavin, and B12 as final `G_PER_L` ingredients. | `data/normalized_yaml/bacterial/basic_mineral_medium.yaml`. |
| Major | Stock preparation instructions are orphaned and over-scoped. | DSMZ pH 3.0-4.0 belongs to the trace-element solution, the pH-acidified and basic solvents belong to vitamin sub-stocks, and the filtration instruction belongs to vitamin stocks; the YAML stores these as top-level preparation steps. | `data/normalized_yaml/bacterial/basic_mineral_medium.yaml`. |
| Major | Exact ingredient identity is incomplete for several rows. | `NiCl2 x 6 H2O` is grounded only to nickel dichloride, `Na-aspartate` and `B12` are ungrounded, and Thiamine still carries a deprecated `MediaIngredientMech:000898` link instead of a CHEBI-keyed MIM link. | `data/normalized_yaml/bacterial/basic_mineral_medium.yaml`. |

## Recommended Edits

1. Move the trace-element stock into a nested `solutions` record with its 1 L recipe, final pH 3.0-4.0, and 1 ml/L final-medium addition.
2. Move the four vitamin stocks into nested solution records, preserve their acidified/basic/neutral solvent boundaries, and represent the final mixed-vitamin addition as 1.0 ml/L or 250 uL/L of each sub-stock.
3. Keep only final-medium additions at top level: the 20 mM K-P buffer, 1 mM MgSO4 x 7 H2O, 10 mM sodium acetate, the 1 ml/L 5% CaCl2 addition, 2 mM sodium aspartate, 1 ml/L trace elements, 0.5 to 1.0 ml/L vitamins as resolved from the DSMZ text, and 50 uM L-methionine.
4. Scope the 121 C for 20 minutes sterilization to the K-P buffer, the 121 C for 15 minutes autoclaving to any source stock where DSMZ says it applies, and the filter-sterilization instructions to methionine and vitamin stocks.
5. Review `NiCl2 x 6 H2O`, `Na-aspartate`, `B12`, and the Thiamine MIM link against exact CHEBI/MIM identity and leave unresolved salts explicit if no exact term is available.
6. Regenerate `data/merge_yaml/merged/Basic_mineral_medium.yaml` from the normalized owner.

## Follow-up Checks

- Rerun open-schema LinkML validation, `scripts/validate_strict.py`, `linkml-term-validator`, and the reference validator on `data/normalized_yaml/bacterial/basic_mineral_medium.yaml` after edits.
- Regenerate the generated merge and run `just verify-merges` plus `just audit-merge-freshness`.
- Re-fetch DSMZ Medium 1615 and manually recalculate the final concentrations for trace elements, vitamins, MgSO4, sodium acetate, CaCl2, sodium aspartate, L-methionine, K2HPO4, and KH2PO4 from the stock recipes and addition volumes.
- Re-run the concentration-plausibility report or a focused equivalent and confirm `CultureMech:001096` no longer emits the current trace-salt or vitamin unit-slip rows.

## Additional Notes

- `data/import_tracking/reports/concentration_plausibility.tsv` already flags FeSO4 x 7 H2O as a stock-magnitude trace salt and Pyridoxine as a likely 1000x vitamin unit slip in this record.
- Exact gitignore-independent searches included ignored files where present.
