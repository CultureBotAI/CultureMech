# YAML Record Review: flexibacter_canadensis_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/flexibacter_canadensis_medium__26f726a0.yaml
- Started UTC: 2026-09-23T03:27:45Z
- Finished UTC: 2026-09-23T03:29:10Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:009158` / `flexibacter_canadensis_medium`, the TOGO M2591 import for Flexibacter Canadensis Medium.
- Confirmed that this generated record comes from `data/normalized_yaml/bacterial/TOGO_M2591_Flexibacter_Canadensis_Medium.yaml`.
- Cross-checked TOGO M2591 against its cited DSMZ 357 PDF and the equivalent MediaDive REST payload for DSMZ medium 357.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; `/private/tmp/flexibacter_canadensis_medium_26f726a0.strict.tsv` contains only its header row.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The Togo identity is coherent: `media_term` is `TOGO:M2591`, the source note cites the TOGO M2591 page, and TOGO M2591 cites DSMZ medium 357 as its original URL.
- The record is not the same source as same-slug `data/normalized_yaml/bacterial/flexibacter_canadensis_medium.yaml`, which is the separate DSMZ 357 MediaDive import with CultureMech ID `CultureMech:001456`.
- `MgSO4 x 7 H2O` has the corrected primary heptahydrate CHEBI term, but its `mediaingredientmech_chebi_term` mirror still points to the generic magnesium sulfate `CHEBI:32599`.
- `KNO3` still has a legacy `mediaingredientmech_term` identifier rather than an id-safe CHEBI mirror.
- `Na-glycerophosphate`, `Glucose (sterilized separately)`, `Casamino acids`, and `HCl (25%; 7.7 M)` are ungrounded.

## Evidence

- TOGO M2591, DSMZ 357, and MediaDive 357 all support pH 7.5 and a main solid-agar recipe with MgSO4 x 7 H2O, KNO3, CaCl2 x 2 H2O, Na-glycerophosphate, Tris, Thiamine-HCl x 2 H2O, Casamino acids, Glucose, Vitamin B12, Agar, Distilled water, and a 1 ml/L Trace element solution SL-10 addition.
- The generated Togo record omits the source pH value and preparation comments.
- The generated Togo record keeps a Trace element solution SL-10 row under `solutions`, but records its 1 ml/L source addition as 1 `G_PER_L`.
- The generated Togo record also flattens SL-10 stock water and stock salts into top-level ingredients, producing 1990.0 `G_PER_L` water and stock-strength trace metal rows.
- Thiamine-HCl x 2 H2O should be 1 mg/L, represented as 0.001 g/L by the DSMZ MediaDive import; Vitamin B12 should be 1 ug/L, represented as 0.000001 g/L. The Togo record stores both as 1 g/L.

## Completeness

- Ingredients, solid-agar state, medium identity, and source URL are present.
- The source pH 7.5 and the pH-adjustment preparation instruction are absent from the generated Togo record.
- The SL-10 stock composition is partially present, but at the wrong level of the recipe hierarchy.

## Findings

- Needs curation: source pH 7.5 and the pH-adjustment instruction were dropped.
- Needs curation: Trace element solution SL-10 should be a 1 `ML_PER_L` addition, not a 1 `G_PER_L` addition.
- Needs curation: nested SL-10 stock water, HCl, and trace salts are incorrectly exposed as final-medium ingredients at stock strength.
- Needs curation: microgram and milligram vitamin units were converted as grams; Vitamin B12 and Thiamine-HCl x 2 H2O are each inflated by 1,000,000x and 1,000x respectively.
- Needs curation: the Togo M2591 record should be reconciled with the DSMZ 357 source duplicate so the better MediaDive ID and the repaired DSMZ/KOMODO topology are not left disconnected.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M2591_Flexibacter_Canadensis_Medium.yaml` or the TOGO import logic before regenerating this merge.
- Restore `ph_value: 7.5` and a preparation step equivalent to DSMZ's pH-adjustment instruction.
- Convert Thiamine-HCl x 2 H2O to 0.001 `G_PER_L` and Vitamin B12 to 0.000001 `G_PER_L`.
- Preserve Trace element solution SL-10 as a 1 `ML_PER_L` solution addition and remove all nested SL-10 components from top-level final `ingredients`.
- Reconcile this Togo M2591 source duplicate with the DSMZ 357 import rather than keeping two diverging `flexibacter_canadensis_medium` records.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated M2591 YAML.
- Confirm no top-level final ingredient row remains for SL-10-only HCl, FeCl2 x 4 H2O, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, or the SL-10 stock water.
- Confirm the repaired generated record does not contain 1990.0 `G_PER_L` water or `G_PER_L` trace solution.
- Confirm the MgSO4 x 7 H2O and KNO3 MediaIngredientMech mirrors are id-safe after curation.

## Additional Notes

- The generated file is derived data. The observed defects are present in the normalized Togo source and need to be fixed there or in the Togo importer.
