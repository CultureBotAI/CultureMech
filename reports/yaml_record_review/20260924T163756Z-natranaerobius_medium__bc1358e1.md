# YAML Record Review: Natranaerobius Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/natranaerobius_medium__bc1358e1.yaml
- Started UTC: 2026-09-24T16:37:56Z
- Finished UTC: 2026-09-24T16:37:56Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:009108` for TOGO M2539, `Natranaerobius Medium`, sourced from DSMZ Medium 1095.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to the intended TOGO import of DSMZ Medium 1095.

An exact repository search including ignored files for `TOGO:M2539`, `CultureMech:009108`, `DSMZ_Medium1095`, and `natranaerobius_medium` found this TOGO owner and generated file plus the active direct DSMZ/KOMODO source-duplicate family for DSMZ Medium 1095. The direct DSMZ owner has already linked KOMODO 1095 as a source duplicate and KOMODO 1095.1 and 1095.2 as pH variants; the TOGO M2539 owner is still separate.

## Evidence

The DSMZ Medium 1095 PDF lists a main medium made with 1000 ml water, 100 g NaCl, 0.2 g KH2PO4, 0.1 g MgCl2, 0.5 g NH4Cl, 10 g OXOID yeast extract, 10 g BD Bacto tryptone, 1 ml Trace element solution SL-10, 68 g Na2CO3, 38 g NaHCO3, 0.7 g L-cysteine HCl x H2O, 1 ml Wolin's vitamin solution 10x, and 5 g sucrose.

The PDF preparation text dissolves ingredients except carbonates, cysteine, sucrose, and vitamins; sparges with 100% N2 for 30 to 45 min; adds carbonate, hydrogencarbonate, and cysteine; adjusts pH to 8.5; dispenses under 100% N2; autoclaves; and then adds sterile anoxic sucrose and vitamin stocks.

Trace element solution SL-10 is defined as 10 ml 25% HCl, 1.5 g FeCl2 x 4H2O, 70 mg ZnCl2, 100 mg MnCl2 x 4H2O, 6 mg H3BO3, 190 mg CoCl2 x 6H2O, 2 mg CuCl2 x 2H2O, 24 mg NiCl2 x 6H2O, 36 mg Na2MoO4 x 2H2O, and 990 ml water, made up to 1000 ml.

Wolin's vitamin solution 10x is defined per 1000 ml as 20 mg biotin, 20 mg folic acid, 100 mg pyridoxine hydrochloride, 50 mg thiamine HCl, 50 mg riboflavin, 50 mg nicotinic acid, 50 mg calcium D-(+)-pantothenate, 1 mg vitamin B12, 50 mg p-aminobenzoic acid, and 50 mg (DL)-alpha-lipoic acid.

The TOGO API for M2539 emits the source's `1 ml` Trace element solution SL-10 row as a cross-reference to M2539 itself and emits `10 ml` Vitamin solution, not the source PDF's 1 ml Wolin's vitamin solution 10x row.

## Completeness

The generated record flattens both internal subrecipes into the top-level final ingredient list. It is missing structured stock additions for Trace element solution SL-10 and Wolin's vitamin solution 10x.

It merges the main 1000 ml water, the SL-10 990 ml water, and the Wolin stock 1000 ml water into one impossible `2990.0 G_PER_L` row.

It omits the pH 8.5 value and both preparation steps from the DSMZ source, including the N2 sparging/autoclave sequence and the SL-10 FeCl2/HCl dissolution order.

## Findings

- Source stock internals are flattened as final top-level ingredients.
- SL-10 milligram values are promoted to gram-per-liter values: for example, 36 mg Na2MoO4 x 2H2O becomes `36 G_PER_L`, 6 mg H3BO3 becomes `6 G_PER_L`, and 70 mg ZnCl2 becomes `70 G_PER_L`.
- Wolin's vitamin 10x milligram values are also promoted to gram-per-liter values instead of remaining mg/L inside a 1 ml/L stock addition.
- The DSMZ 1 ml Wolin's vitamin solution 10x addition is represented by TOGO as a 10 ml `Vitamin solution` addition.
- The generated water row is an invalid merge of final-medium water and two stock-solution water rows.
- The active TOGO owner duplicates DSMZ Medium 1095 outside the direct DSMZ/KOMODO duplicate family.

## Recommended Edits

- Retire or link the TOGO M2539 owner to the curated DSMZ/KOMODO 1095 duplicate family.
- If retaining TOGO M2539, re-curate it from the DSMZ Medium 1095 PDF with nested SL-10 and Wolin's vitamin solution layers and mg quantities preserved as stock-local `MG_PER_L` values.
- Correct Wolin's vitamin solution to 1 ml/L, not 10 ml/L.
- Preserve the pH 8.5 and DSMZ preparation sequence.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natranaerobius_medium__bc1358e1.yaml` and verify no trace-metal or vitamin mg source row remains inflated 1000-fold.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored files for `DSMZ_Medium1095`, `TOGO:M2539`, `mediadive.medium:1095`, and `komodo.medium:1095` to verify there is one intentional source-duplicate family.

## Additional Notes

None found.
