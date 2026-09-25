# YAML Record Review: nutrient_methanol_agar

- Repository: CultureMech
- Record: `data/merge_yaml/merged/nutrient_methanol_agar.yaml`
- Started UTC: 2026-09-24T18:47:06Z
- Finished UTC: 2026-09-24T18:47:44Z
- Verdict: needs curation

## Target

Generated bacterial record `CultureMech:009310`, `nutrient_methanol_agar`, a one-source TOGO M275 import of JCM Medium 281.

## Validation

Open LinkML validation passed with `No issues found`.

Strict validation passed; `/private/tmp/nutrient_methanol_agar.strict.tsv` contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: the history validator operates over standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The reviewed record is grounded to TOGO M275, which mirrors JCM Medium 281 `NUTRIENT-METHANOL AGAR`.

An exact ignored-inclusive, hidden-inclusive search for `TOGO:M275`, `GMDB:M275`, `M275`, `JCM_M281`, `GRMD=281`, `TOGO_M275_Nutrient-Methanol_Agar`, `nutrient_methanol_agar`, and `Nutrient-Methanol Agar` found this TOGO normalized owner and generated merge, a separate direct JCM/MediaDive normalized owner and generated merge for the same GRMD 281 source, source indexes, and unrelated records whose source notes contain `M275` for NBRC or another JCM medium.

## Evidence

TOGO M275 and the live JCM Medium 281 page agree on the recipe: 10 g Peptone, 10 g Beef extract, 5 g NaCl, 10 ml Methanol, 20 g Agar, and 1 L Distilled water. JCM also says to add Methanol aseptically to the autoclaved medium and mix well before dispensation.

The generated TOGO record preserves the 10 g/L Peptone, 10 g/L Beef extract, 5 g/L NaCl, and 20 g/L Agar values.

## Completeness

The generated record is incomplete as a preparation recipe because it drops the JCM instruction to add methanol aseptically after autoclaving.

The same JCM Medium 281 page is also represented by the direct `data/normalized_yaml/bacterial/nutrient_methanol_agar.yaml` import and the generated `data/merge_yaml/merged/nutrient_methanol_agar__0d3f9d47.yaml` artifact. Those direct-JCM records preserve the aseptic methanol-addition step, but they omit the 1 L water row and rescale the gram rows to 1010 ml final volume as 9.90099, 9.90099, 4.9505, and 19.802 g/L.

## Findings

Needs curation:

- `Distilled water` is encoded as `1 G_PER_L`; JCM Medium 281 lists 1 L Distilled water.
- `Methanol` is encoded as `10 G_PER_L`; JCM Medium 281 lists 10 ml Methanol.
- The aseptic post-autoclave methanol addition and mixing instruction is missing.
- The TOGO M275 import and direct JCM 281 import remain split into separate generated records for the same JCM source.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/TOGO_M275_Nutrient-Methanol_Agar.yaml` before regenerating this artifact:

- Convert `Distilled water` to `1000 ML_PER_L`.
- Convert `Methanol` to a 10 ml/L volume addition.
- Add a preparation step that autoclaves the base medium, then adds methanol aseptically and mixes before dispensation.
- Reconcile this TOGO M275 import with `data/normalized_yaml/bacterial/nutrient_methanol_agar.yaml` so one curated JCM Medium 281 recipe is generated.

During duplicate reconciliation, decide whether ingredient values should remain as source amounts per 1 L water or be normalized to the 1010 ml post-methanol final volume; do not keep both conventions as separate records for the same GRMD 281 source.

## Follow-up Checks

After repair, rerun open schema, strict, reference, and term validation on the normalized owner and regenerated merged YAML. Re-fetch TOGO M275 and JCM `GRMD=281`, then confirm the generated record has 1000 ml/L water, a volume-based methanol addition, the aseptic methanol preparation step, and no separate hash-suffixed direct-JCM duplicate.

## Additional Notes

None found.
