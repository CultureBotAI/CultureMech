# YAML Record Review: Pfennig's Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/pfennigs_medium.yaml
- Started UTC: 2026-09-24T20:48:38Z
- Finished UTC: 2026-09-24T20:48:38Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pfennigs_medium.yaml`, the merged TOGO-derived record for JCM medium 681 / Pfennig's Medium.

The merged recipe has a single source, `TOGO_M700_Pfennig_s_Medium`, and traces to TOGO `M700`, whose original source is JCM `JCM_M681`.

## Validation

- LinkML open validation: passed; no issues found.
- Strict schema validation: passed; `/private/tmp/pfennigs_medium.strict.tsv` has one header row and zero error rows.
- Reference validation: passed; 1 file validated, 0 checks configured.
- Term validation: passed.
- Embedded curation history validation: Not checked; the available `just validate-history` target validates standalone `history/` records rather than `MediaRecipe.curation_history` blocks inside merged YAML.

## Identity and Grounding

The record identity is correct: the target represents "PFENNIG'S MEDIUM" from JCM medium 681 as imported through TOGO medium M700.

Source grounding is not complete because the same JCM page also exists as the direct JCM-derived sibling `data/merge_yaml/merged/pfennigs_medium__4e5aaa08.yaml`. That sibling uses `mediadive.medium:J681` for the same source URL and same recipe, but it flattened the cross-referenced SL-10 trace element stock from JCM medium 433 into final ingredients. Once the stock-solution model is corrected, the TOGO and direct JCM imports should be reconciled into one source-backed record instead of remaining as two Pfennig's Medium records.

Most simple main-medium groundings are correct. `MgSO4.7H2O`, `CaCl2.2H2O`, `Na2S.9H2O`, `K2HPO4`, `NH4Cl`, `KCl`, `NaHCO3`, and vitamin B12 are grounded to the expected CHEBI concepts. The source rows for acetate and thiosulfate remain ungrounded despite TOGO supplying those rows as defined final concentrations.

## Evidence

- Fetched TOGO API record `M700`, which reports name "Pfennig's Medium", original medium `JCM_M681`, source URL `GRMD=681`, pH 7.2, 0.02 mg vitamin B12, and a 0.5 ml "Trace element solution SL--10 (see Medium [M433])" addition.
- Fetched JCM medium 681 directly and confirmed the same formula: six salts plus 1 L distilled water before autoclaving, then 0.5 ml Trace element solution SL-10 from medium 433, 0.3 g Na2S x 9 H2O, 1.5 g NaHCO3, 0.02 mg vitamin B12, 2 mM acetate, 10 mM thiosulfate, and pH 7.2.
- Fetched JCM medium 433 and TOGO medium M433 to verify that the referenced SL-10 row is a stock solution in medium 433, not a set of final Pfennig's Medium ingredient masses.
- Compared the normalized TOGO source record `data/normalized_yaml/bacterial/TOGO_M700_Pfennig_s_Medium.yaml` with the merged output and inspected the direct JCM sibling that failed to merge.

## Completeness

The core non-stock chemical list is mostly complete, but several source facts did not survive with the right units or structure:

- JCM/TOGO list 0.02 mg vitamin B12 per liter; the target stores `0.02 G_PER_L`.
- JCM/TOGO list 0.5 ml of SL-10 trace element solution per liter; the target stores the stock under `solutions` with `0.5 G_PER_L`.
- JCM/TOGO list the final pH as 7.2; the target has no `ph_value`.
- JCM/TOGO explicitly say to add the second block after autoclaving; the target has no preparation step for that block.
- JCM/TOGO encode 1 L distilled water as final volume context; the target stores it as `1 G_PER_L`.

## Findings

- The vitamin B12 concentration is off by a factor of 1000. The source gives 0.02 mg/L, equivalent to `0.00002 G_PER_L`; the record stores `0.02 G_PER_L`.
- The SL-10 trace element stock addition is represented with the wrong unit. The source calls for 0.5 ml/L of the stock, but the migrated `solutions` entry records `0.5 G_PER_L`, and its `name` is the generic `Unknown solution`.
- The pH 7.2 and after-autoclaving preparation instruction from JCM/TOGO are omitted.
- Distilled water is imported as `1 G_PER_L` even though the source row is 1 L final-volume solvent.
- Acetate and thiosulfate have correct final concentration values but no CHEBI term or MediaIngredientMech CHEBI link.
- The exact JCM 681 recipe is split across this TOGO-derived record and `pfennigs_medium__4e5aaa08`, whose direct JCM import captured pH and instructions but flattened JCM 433 stock rows into final medium ingredients.

## Recommended Edits

- Fix the TOGO M700 normalized source import to convert 0.02 mg vitamin B12 to `0.00002 G_PER_L`.
- Preserve the SL-10 stock as a 0.5 `ML_PER_L` stock addition, with a meaningful stock name and the `M433` cross-reference.
- Carry `ph_value: 7.2` and a preparation step noting that the SL-10 stock, Na2S x 9 H2O, NaHCO3, vitamin B12, acetate, and thiosulfate are added after autoclaving.
- Represent the 1 L distilled-water row as final-volume solvent context instead of `1 G_PER_L`.
- Ground acetate to `CHEBI:30089` and thiosulfate to `CHEBI:26977`, then add matching `mediaingredientmech_chebi_term` blocks.
- Re-run merge after fixing the direct JCM import so JCM 681 and TOGO M700 reconcile instead of remaining as two near-duplicate Pfennig's Medium records.

## Follow-up Checks

- Re-run LinkML open validation, strict validation, reference validation, and term validation on the regenerated merged record.
- Search with ignored files included for `GRMD=681`, `TOGO:M700`, and `JCM_M681` and confirm they converge on the intended normalized source records and one merged Pfennig's Medium recipe.
- Confirm the regenerated recipe keeps the SL-10 addition as an aliquot rather than importing JCM 433 stock component masses into the final medium.
- Confirm vitamin B12 appears at 0.00002 g/L, not 0.02 g/L.

## Additional Notes

Empty optional fields were not treated as defects. The direct JCM sibling was used only as corroborating evidence of a merge/import split; it was not the primary target of this report.
