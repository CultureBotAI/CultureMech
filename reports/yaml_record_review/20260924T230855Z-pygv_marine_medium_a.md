# YAML Record Review: PYGV Marine Medium (A)

- Repository: CultureMech
- Record: data/merge_yaml/merged/pygv_marine_medium_a.yaml
- Started UTC: 2026-09-24T23:08:55Z
- Finished UTC: 2026-09-24T23:09:50Z
- Verdict: needs curation

## Target

- Generated file: data/merge_yaml/merged/pygv_marine_medium_a.yaml
- Stable ID: CultureMech:009516
- Maintained owner: data/normalized_yaml/bacterial/pygv_marine_medium_a.yaml
- Merge sources: pygv_marine_medium_a
- Merge fingerprint: d895831928a23ee49e934017dc59ade52cf4498e749de79fd0564567c8787905
- Source grounding: TOGO M299 / JCM Medium 304 PYGV Marine Medium (A)

## Validation

| Check | Result |
| --- | --- |
| LinkML open schema | Passed with `No issues found`. |
| Strict schema | Passed with 0 errors. `/private/tmp/pygv_marine_medium_a.strict.tsv` contains only the header line. |
| Reference validation | Passed 1 file with 0 reference checks. |
| Term validation | Passed after the known `eutils` / `pkg_resources` warning. |
| Embedded history validation | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The record is correctly identified as TOGO M299 / JCM Medium 304, PYGV Marine Medium (A). The source recipe is a main medium with 0.25 g Bacto peptone, 0.25 g Yeast extract, 20 ml Mineral salt solution, 10 ml 2.5% Glucose solution, 10 ml Vitamin solution, 15 g Agar, and 960 ml Artificial seawater. The final pH should be 7.5.

The source also defines nested Mineral salt solution, Vitamin solution, Artificial seawater, and Metals 44 stocks. The generated record flattened all stock contents into top-level ingredients and kept the four stock additions as empty top-level solution shells with `G_PER_L` concentrations of 10, 20, 10, and 50.

An exact ignored-file search for `TOGO:M299`, `gm_id=M299`, `GRMD=304`, `J304`, `mediadive.medium:J304`, and `pygv_marine_medium_a` under `data/normalized_yaml/bacterial`, `data/normalized_yaml/specialized_index.json`, and `data/merge_yaml/merged` found this TOGO M299 branch, the separate direct JCM J304 branch `data/merge_yaml/merged/pygv_marine_medium_a__405d6e69.yaml`, and expected references from repaired PYGV descendant recipes.

## Evidence

- TOGO M299 imports JCM Medium 304 and preserves pH 7.5.
- JCM Medium 304 lists 20 ml Mineral salt solution, 10 ml 2.5% Glucose solution, 10 ml Vitamin solution, 15 g Agar, and 960 ml Artificial seawater in the main liter.
- JCM Medium 304 lists the Mineral salt solution separately with 29.7 g MgSO4 x 7H2O, 10 g Nitrilotriacetic acid, 3.34 g CaCl2 x 2H2O, 99 mg FeSO4 x 7H2O, 13 mg Na2MoO4 x 2H2O, 50 ml Metals 44, and 950 ml water.
- JCM Medium 304 lists the Vitamin solution in 1 L water with Biotin 2 mg, Folic acid 2 mg, Pyridoxine HCl 10 mg, Riboflavin 5 mg, Thiamine HCl 5 mg, Nicotinamide 5 mg, Calcium pantothenate 5 mg, Vitamin B12 0.1 mg, and p-Aminobenzoic acid 5 mg.
- JCM Medium 304 lists Artificial seawater as a 1 L stock with NaCl, Na2SO4, MgCl2 x 6H2O, CaCl2 x 2H2O, NaHCO3 192 mg, KCl 664 mg, KBr 6 mg, H3BO3 26 mg, SrCl2 x 6H2O 24 mg, NaF 3 mg, and water.
- MediaDive J304 additionally expands Metals 44 as a 1 L stock with Na2-EDTA, ZnSO4 x 7H2O, FeSO4 x 7H2O, MnSO4 x n H2O, CuSO4 x 5H2O, Co(NO3)2 x 6H2O, Na2B4O7 x 10H2O, and water.
- `data/merge_yaml/merged/pygv_marine_medium_a.yaml` stores `Na2MoO4 x 2H2O: 13 G_PER_L`, `FeSO4 x 7H2O: 99 G_PER_L`, `Biotin: 2 G_PER_L`, `NaHCO3: 192 G_PER_L`, and `KCl: 664 G_PER_L`, showing that milligram source quantities were converted to grams per liter.
- The record omits the pH 7.5 value and the source preparation instructions for aseptic glucose/vitamin addition, pH adjustment, and Mineral salt solution preparation.

## Completeness

The source identity, agar state, main peptone, main yeast extract, and main agar are present. The rest of the source hierarchy is incomplete: glucose, mineral salts, vitamins, artificial seawater, and Metals 44 are all disconnected from their aliquot volumes; all water rows are merged into one top-level water ingredient; several duplicate chemicals from different stocks are summed together; and pH/preparation details are absent.

The equivalent direct JCM J304 import exists as `pygv_marine_medium_a__405d6e69` and also needs repair because it flattened the same stocks into top-level ingredients, but it preserved MediaDive's gram-normalized mg values more accurately than this TOGO branch.

## Findings

- Major: four stock additions are empty `solutions` rows with `G_PER_L` volume aliquots instead of 10 ml/L 2.5% Glucose, 20 ml/L Mineral salt solution, 10 ml/L Vitamin solution, and 50 ml/L Metals 44 nested under the Mineral salt solution.
- Major: the Mineral salt solution, Vitamin solution, Artificial seawater, and Metals 44 internals are flattened into top-level final-medium ingredients, losing source context and causing duplicate water, CaCl2, and FeSO4 rows to be merged across unrelated stocks.
- Major: source milligram quantities are represented as gram-per-liter values; FeSO4, Na2MoO4, all vitamins, H3BO3, KCl, NaHCO3, KBr, SrCl2, and NaF are each 1000x too high in the generated top-level list before aliquot scaling is even considered.
- Major: pH 7.5 and the source preparation instructions are missing.

## Recommended Edits

1. Re-resolve `data/normalized_yaml/bacterial/pygv_marine_medium_a.yaml` from TOGO M299 / JCM Medium 304.
2. Restore top-level ingredients to Bacto peptone, Yeast extract, Agar, 20 ml/L Mineral salt solution, 10 ml/L 2.5% Glucose solution, 10 ml/L Vitamin solution, 960 ml/L Artificial seawater, and variable KOH for final pH.
3. Move the mineral salts, vitamin ingredients, artificial seawater salts, and Metals 44 ingredients into nested source solutions with source-local units.
4. Keep same-named chemicals from different stocks separate unless they are in the same solution.
5. Restore pH 7.5 and the JCM preparation steps for boiling, autoclaving, cooling, aseptic glucose/vitamin addition, final KOH adjustment, and Mineral salt solution pH adjustment.
6. Regenerate and check whether TOGO M299 and direct JCM J304 can merge after both are repaired to the same nested structure.

## Follow-up Checks

- Re-run open, strict, reference, and term validators on regenerated `pygv_marine_medium_a` output.
- Compare the regenerated TOGO M299 branch against JCM Medium 304, TOGO M299, and MediaDive J304.
- Repeat the exact ignored-file search for `TOGO:M299`, `GRMD=304`, `J304`, and `mediadive.medium:J304` to confirm TOGO and JCM branches either merge or remain separated for a documented source difference.
- Confirm all hydrated salts retain specific hydrated CHEBI terms in nested solution compositions.

## Additional Notes

None.
