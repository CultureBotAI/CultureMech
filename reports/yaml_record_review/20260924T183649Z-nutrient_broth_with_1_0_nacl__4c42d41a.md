# YAML Record Review: nutrient_broth_with_1_0_nacl__4c42d41a

- Repository: CultureMech
- Record: `data/merge_yaml/merged/nutrient_broth_with_1_0_nacl__4c42d41a.yaml`
- Started UTC: 2026-09-24T18:36:49Z
- Finished UTC: 2026-09-24T18:37:09Z
- Verdict: needs curation

## Target

Generated bacterial record `CultureMech:003145`, `nutrient_broth_with_1_0_nacl__4c42d41a`, merging direct JCM Medium 7 and JCM Medium 12 imports.

## Validation

Open LinkML validation passed with `No issues found`.

Strict validation passed; `/private/tmp/nutrient_broth_with_1_0_nacl__4c42d41a.strict.tsv` contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: the history validator operates over standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record keeps the ID, media term, name, source URL, and pH from the direct JCM Medium 7 1.0% NaCl import, but its 5 g/L NaCl ingredient value came from the direct JCM Medium 12 0.5% NaCl parent.

The normalized direct JCM records correctly annotate the pair as `SALINITY_VARIANT`, so JCM 7 and JCM 12 should not be merged as source duplicates.

An exact ignored-inclusive, hidden-inclusive search for the two nutrient-broth slugs, `GRMD=7`, `GRMD=12`, and the matching TOGO source identifiers found this direct-JCM generated artifact, the parallel TOGO generated artifact, both direct JCM normalized records, both TOGO normalized records, and expected source/deep-research index rows.

## Evidence

JCM Medium 7 lists 5 g Bacto peptone, 3 g Beef extract, 10 g NaCl, 1 L Distilled water, and pH 7.0.

JCM Medium 12 lists 5 g Bacto peptone, 3 g Beef extract, 5 g NaCl, 1 L Distilled water, and pH 7.0.

MediaDive 74 is DSMZ `THERMUS THERMOPHILUS MEDIUM`, with Yeast extract, Proteose peptone no. 3, 2 g/L NaCl, and Distilled water, so `kg_microbe_match: mediadive.medium:74` is unrelated to these JCM nutrient-broth variants.

## Completeness

The generated formula is internally inconsistent: the metadata denotes the 1.0% NaCl JCM Medium 7 source, while the NaCl ingredient is 5 g/L from JCM Medium 12. Both direct JCM normalized parents also omit the 1 L Distilled water row from their ingredient lists.

The generated record is stale relative to the maintained normalized JCM Medium 7 parent for Bacto peptone and Beef extract ontology grounding.

## Findings

Needs curation:

- JCM 7 and JCM 12 were merged into one generated record even though they differ by NaCl concentration and are only salinity variants.
- This 1.0% NaCl generated record carries the 0.5% parent concentration, `NaCl 5 G_PER_L`, instead of the JCM Medium 7 source value of 10 g/L.
- `Distilled water 1 L` is missing from both direct JCM imports and from the generated merge.
- `kg_microbe_match: mediadive.medium:74` falsely links both JCM records to DSMZ Thermus Thermophilus Medium.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/nutrient_broth_with_1_0_nacl.yaml` and `data/normalized_yaml/bacterial/nutrient_broth_with_0_5_nacl.yaml`:

- Add `Distilled water` at `1000 ML_PER_L` to both records.
- Remove or recompute `kg_microbe_match: mediadive.medium:74`.
- Keep JCM Medium 7 and JCM Medium 12 as separate records connected by `SALINITY_VARIANT`.
- Ensure regenerated JCM Medium 7 keeps 10 g/L NaCl and regenerated JCM Medium 12 keeps 5 g/L NaCl.

Then regenerate the merged YAML and reconcile direct JCM 7 with TOGO M3, and direct JCM 12 with TOGO M5, as source-equivalent imports without merging the 1.0% and 0.5% NaCl variants together.

## Follow-up Checks

After repair, rerun open schema, strict, reference, and term validation on regenerated direct-JCM and TOGO nutrient-broth variants. Confirm that no generated JCM 7 or JCM 12 artifact keeps `mediadive.medium:74`, that 1000 ml/L water is present, and that no 1.0% NaCl artifact has `NaCl 5 G_PER_L`.

## Additional Notes

None found.
