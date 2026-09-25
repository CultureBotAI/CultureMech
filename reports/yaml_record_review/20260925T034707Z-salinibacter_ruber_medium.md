# YAML Record Review: salinibacter_ruber_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/salinibacter_ruber_medium.yaml
- Started UTC: 2026-09-25T03:47:07Z
- Finished UTC: 2026-09-25T03:47:07Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:006858`, `salinibacter_ruber_medium`, from `data/merge_yaml/merged/salinibacter_ruber_medium.yaml`.

The generated record uses KOMODO Medium 936 as canonical and merges eight sources: KOMODO 1138, DSMZ/MediaDive 1138, KOMODO 936, DSMZ/MediaDive 936, JCM J797, JCM J620, JCM J1011, and JCM J546.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The canonical identity is Salinibacter ruber medium / DSMZ 936, but the generated ingredient rows are not DSMZ 936 rows.

DSMZ 936 and KOMODO 936 are true source duplicates of SALINIBACTER RUBER MEDIUM. DSMZ 1138 and KOMODO 1138 are true source duplicates of HALOPIGER MEDIUM. Those two DSMZ media differ in six concentrations and pH and should not share one merge fingerprint.

SW-10, SW-20, SW-7.5, and Halophile Yeast Extract Medium are separately named JCM recipes and should be evaluated as separate recipes or variants, not silently collapsed into the DSMZ 936 source-duplicate group.

## Evidence

DSMZ Medium 936 lists 195 g NaCl, 34.6 g MgCl2 x 6 H2O, 49.5 g MgSO4 x 7 H2O, 1.25 g CaCl2 x 2 H2O, 5 g KCl, 0.25 g NaHCO3, 0.625 g NaBr, 1 g yeast extract, 1000 ml distilled water, and final pH 7.2.

DSMZ Medium 1138 lists 195 g NaCl, 32.5 g MgCl2 x 6H2O, 50.8 g MgSO4 x 7H2O, 0.8 g CaCl2 x 2H2O, 5 g KCl, 0.16 g NaHCO3, 0.6 g NaBr, 5 g yeast extract, 1000 ml distilled water, and pH 8.0.

The normalized JCM imports for SW-10 and SW-20 carry lower salt concentrations and different pH and agar notes than the generated canonical recipe. The normalized SW-7.5 and Halophile Yeast Extract Medium sources are much closer to DSMZ 1138, but they still have their own source names and preparation context.

## Completeness

The generated record contains the DSMZ 1138 ingredient amounts, not the DSMZ 936 amounts.

The DSMZ 936 source water row is not represented, and the DSMZ 1138 pH 8.0 adjustment is not represented because the generated record retained DSMZ 936's 7.2 pH.

## Findings

The duplicate merge is over-broad. It collapsed Salinibacter ruber medium, Halopiger medium, SW-10, SW-20, SW-7.5, and Halophile Yeast Extract Medium into one source-duplicate record even though the source names, pH values, ingredients, and preparation notes are not all identical.

The generated `salinibacter_ruber_medium` formula is a cross-source hybrid: it kept the Salinibacter name and pH 7.2 while using the Halopiger/JCM J546 concentrations for MgCl2 x 6 H2O, MgSO4 x 7 H2O, CaCl2 x 2 H2O, NaHCO3, NaBr, and yeast extract.

The canonical generated record understates DSMZ 936 CaCl2, NaHCO3, NaBr, and MgCl2, overstates DSMZ 936 MgSO4 and yeast extract, and omits the 1000 ml distilled-water row from both DSMZ sources.

The generated synonyms make the SW media and Halophile Yeast Extract Medium look like names for Salinibacter ruber medium, which is not supported by their JCM identities.

## Recommended Edits

Split the merge group into at least a DSMZ/KOMODO 936 Salinibacter record and a DSMZ/KOMODO 1138 Halopiger record, then evaluate SW-10, SW-20, SW-7.5, and Halophile Yeast Extract Medium as variants or separate media with evidence from their JCM source pages.

Keep DSMZ 936 at 34.6 g/L MgCl2 x 6 H2O, 49.5 g/L MgSO4 x 7 H2O, 1.25 g/L CaCl2 x 2 H2O, 0.25 g/L NaHCO3, 0.625 g/L NaBr, 1 g/L yeast extract, and pH 7.2.

Keep DSMZ 1138 at 32.5 g/L MgCl2 x 6H2O, 50.8 g/L MgSO4 x 7H2O, 0.8 g/L CaCl2 x 2H2O, 0.16 g/L NaHCO3, 0.6 g/L NaBr, 5 g/L yeast extract, and pH 8.0.

## Follow-up Checks

After regenerating the merge layer, confirm `salinibacter_ruber_medium` no longer has SW-10, SW-20, SW-7.5, Halophile Yeast Extract Medium, or Halopiger entries in `synonyms` or `merged_from`.

Validate the regenerated Salinibacter, Halopiger, SW, and Halophile generated records independently and compare every salt concentration against its source.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
