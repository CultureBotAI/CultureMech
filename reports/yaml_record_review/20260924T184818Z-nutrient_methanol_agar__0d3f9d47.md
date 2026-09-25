# YAML Record Review: nutrient_methanol_agar__0d3f9d47

- Repository: CultureMech
- Record: `data/merge_yaml/merged/nutrient_methanol_agar__0d3f9d47.yaml`
- Started UTC: 2026-09-24T18:48:18Z
- Finished UTC: 2026-09-24T18:48:40Z
- Verdict: needs curation

## Target

Generated bacterial record `CultureMech:002639`, `nutrient_methanol_agar__0d3f9d47`, a one-source direct JCM/MediaDive import of JCM Medium 281.

## Validation

Open LinkML validation passed with `No issues found`.

Strict validation passed; `/private/tmp/nutrient_methanol_agar__0d3f9d47.strict.tsv` contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: the history validator operates over standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The reviewed record is grounded to JCM Medium 281, `NUTRIENT-METHANOL AGAR`, and points directly at the live `GRMD=281` source page.

An exact ignored-inclusive, hidden-inclusive search for `TOGO:M275`, `GMDB:M275`, `M275`, `JCM_M281`, `GRMD=281`, `TOGO_M275_Nutrient-Methanol_Agar`, `nutrient_methanol_agar`, and `Nutrient-Methanol Agar` found this direct JCM normalized owner and generated merge, the separate TOGO M275 normalized owner and generated merge for the same GRMD 281 source, source indexes, and unrelated records whose source notes contain `M275` for NBRC or another JCM medium.

## Evidence

The live JCM Medium 281 page and TOGO M275 agree on the recipe: 10 g Peptone, 10 g Beef extract, 5 g NaCl, 10 ml Methanol, 20 g Agar, and 1 L Distilled water. JCM also says to add Methanol aseptically to the autoclaved medium and mix well before dispensation.

This direct-JCM record preserves the aseptic methanol-addition instruction.

## Completeness

The direct-JCM formula is incomplete because the source 1 L Distilled water row is missing.

The importer also appears to have rescaled base ingredients over 1010 ml, producing 9.90099 g/L Peptone, 9.90099 g/L Beef extract, 4.9505 g/L NaCl, and 19.802 g/L Agar from source rows that are 10 g, 10 g, 5 g, and 20 g per 1 L Distilled water plus 10 ml Methanol. That representation is inconsistent with the TOGO branch, which preserves the gram amounts but corrupts the two volume rows.

## Findings

Needs curation:

- `Distilled water 1 L` is missing from the direct JCM import.
- `Methanol` is encoded as `10 G_PER_L`; JCM Medium 281 lists 10 ml Methanol as an aseptic post-autoclave addition.
- The Peptone, Beef extract, NaCl, and Agar concentrations are silently rescaled to a 1010 ml final volume instead of preserving the source 10 g, 10 g, 5 g, and 20 g rows.
- The direct JCM import and TOGO M275 import remain split into separate generated records for the same JCM source.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/nutrient_methanol_agar.yaml` before regenerating this artifact:

- Add the source `Distilled water` row.
- Convert `Methanol` to a 10 ml/L volume addition.
- Decide whether ingredient values should remain as source amounts per 1 L water or be normalized to the 1010 ml post-methanol final volume; whichever convention is chosen, use the same convention for the direct JCM and TOGO M275 imports.
- Reconcile this direct JCM import with `data/normalized_yaml/bacterial/TOGO_M275_Nutrient-Methanol_Agar.yaml` so one curated JCM Medium 281 recipe is generated.

## Follow-up Checks

After repair, rerun open schema, strict, reference, and term validation on the normalized owner and regenerated merged YAML. Re-fetch TOGO M275 and JCM `GRMD=281`, then confirm the generated record has a water row, a volume-based methanol addition, the aseptic methanol preparation step, and no separate unmerged TOGO duplicate.

## Additional Notes

None found.
