# YAML Record Review: methanogens_saline_water_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanogens_saline_water_medium__61ede417.yaml
- Started UTC: 2026-09-24T03:58:45Z
- Finished UTC: 2026-09-24T04:02:12Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:000286` / `methanogens_saline_water_medium`, produced from one normalized MediaDive import:

- `data/normalized_yaml/archaea/methanogens_saline_water_medium.yaml`
- `merged_from`: `methanogens_saline_water_medium`
- `merge_fingerprint`: `61ede417dc99df7c6fddc1d9052b852f3db39eb1e72094244f529a6318a5b3e4`
- Upstream identity: MediaDive/JCM medium `J1027`, `METHANOGENS SALINE WATER MEDIUM`

## Validation

- LinkML open validation: Passed; printed `No issues found`.
- Strict validation: Passed with 0 error rows in `/private/tmp/methanogens_saline_water_medium__61ede417.strict.tsv`.
- Reference validation: Passed; 0 checks.
- Term validation: Passed.
- Embedded history: Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The generated record keeps the expected CultureMech identifier, MediaDive `J1027` medium term, JCM source note, and single-source merge fingerprint. The normalized owner is identical to the generated ingredient and preparation payload except for generated merge history, so the stock-flattening defects described below need to be fixed in `data/normalized_yaml/archaea/methanogens_saline_water_medium.yaml` or in the MediaDive import path.

The MediaDive REST record for `J1027` resolves to source `JCM` with the name `METHANOGENS SALINE WATER MEDIUM`. Its main solution has volume 1033 ml and separately links `Trace mineral solution` solution `4825`, `Se/W solution` solution `4826`, and `Trace vitamins solution` solution `3979`; the old JCM `GRMD=1027` link stored in the YAML now returns "Nothing found".

## Evidence

- MediaDive `J1027` `Main sol. J1027` contains the base salts scaled over a 1033 ml final volume, with 1 ml Trace mineral solution, 1 ml Se/W solution, 1 ml Trace vitamins solution, 1 mg resazurin, 1000 ml distilled water, 10 ml 1 M trimethylamine, 10 ml 5% `L-Cysteine HCl x H2O`, and 10 ml 5% `Na2S x 9 H2O`.
- MediaDive solution `4825` defines the 1 L Trace mineral stock with `FeCl2 x 4 H2O`, `MnCl2 x 4 H2O`, `CoCl2 x 6 H2O`, `ZnCl2`, `CuCl2 x 2 H2O`, `H3BO3`, `Na2MoO4 x 2 H2O`, `NiCl2 x 6 H2O`, `AlCl3`, and distilled water.
- MediaDive solution `4826` defines the 1 L Se/W stock with `Na2SeO3 x 5 H2O`, `Na2WO4 x 2 H2O`, and distilled water.
- MediaDive solution `3979` defines the 1 L Trace vitamins stock with biotin, folic acid, pyridoxine hydrochloride, thiamine HCl, riboflavin, nicotinic acid, DL-calcium pantothenate, vitamin B12, p-aminobenzoic acid, lipoic acid, and distilled water.
- MediaDive keeps three preparation strings: first autoclave the dispensed base under `H2-CO2` 80:20 and stand overnight, then add the sterile anaerobic 1 M trimethylamine stock and the two 5% reducing solutions, and treat strains JCM 19935 and JCM 19936 as special variants with 100 kPa `H2-CO2` 80:20 pressurization.

## Completeness

The record preserves the MediaDive/JCM identity, main salt concentrations, final resazurin concentration, and source preparation text. It is incomplete as a reusable CultureMech recipe because all three referenced stocks and all three volumetric additions from those stocks were collapsed into flat ingredient rows, so stock identity, addition volume, stock strength, and final dilution are no longer recoverable from the YAML.

## Findings

- Stock components were imported at stock strength instead of final strength. For example, MediaDive adds 1 ml of Trace mineral solution to 1033 ml final medium, but the YAML stores `FeCl2 x 4 H2O` as `1.99 G_PER_L`, the concentration inside solution `4825`; the final contribution is approximately 0.00193 g/L before rounding. The same roughly 1000-fold inflation affects every trace-metal, Se/W, and vitamin component imported from solutions `4825`, `4826`, and `3979`.
- The importer changed liquid stock additions into 10 g/L base compounds. MediaDive lists 10 ml of 1 M trimethylamine, 10 ml of 5% `L-Cysteine HCl x H2O`, and 10 ml of 5% `Na2S x 9 H2O`; the YAML stores those as 10 g/L trimethylamine, cysteine salt, and sodium sulfide, losing both the 1 M or 5% stock concentration and the 10 ml/L addition semantics.
- The stock hierarchy was lost. The generated record has no `solutions` array and no cross-reference to MediaDive solution IDs `4825`, `4826`, or `3979`, even though the source exposes named formula blocks for all three stocks.
- Preparation actions are too coarse. The two steps that introduce trimethylamine and reducing solutions are post-autoclave anaerobic additions, but they are both represented with `action: AUTOCLAVE`; the record needs a representation that separates base autoclaving, filter-sterile trimethylamine addition under `N2`, and reducing-solution addition before inoculation.

## Recommended Edits

- Replace flattened trace-metal, Se/W, and vitamin rows with structured `Trace mineral solution`, `Se/W solution`, and `Trace vitamins solution` stock definitions, preserving MediaDive solution IDs `4825`, `4826`, and `3979` in notes or references.
- Preserve the three main-solution stock invocations as 1 ml/L trace mineral, 1 ml/L Se/W, 1 ml/L trace vitamins, 10 ml/L 1 M trimethylamine, 10 ml/L 5% cysteine hydrochloride monohydrate, and 10 ml/L 5% sodium sulfide nonahydrate.
- If flattened final concentrations are retained for search or comparison, compute them after dilution into the 1033 ml final volume and do not replace the source stock hierarchy with them.
- Recode the preparation steps so post-autoclave additions are not labeled as autoclave actions.
- Regenerate `data/merge_yaml/merged/methanogens_saline_water_medium__61ede417.yaml` from the curated normalized owner.

## Follow-up Checks

- Re-run open, strict, reference, and term validation after regeneration.
- Compare the regenerated YAML against MediaDive REST `/rest/medium/J1027` and verify that the named stock solutions, the 1033 ml final volume, and the 1 M/5% stock attributes are all still visible.
- Check whether the old JCM URL remains unavailable and keep MediaDive as the primary retrievable source if it still returns no medium formula.

## Additional Notes

The base MediaDive/JCM `J1027` recipe and the TOGO `M1090` `JCM_M1027-2` yeast-extract variant share preparation text but are not duplicates: `J1027` includes 10 ml 1 M trimethylamine, while `M1090` is a derived variant replacing that addition with yeast extract.
