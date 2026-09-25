# YAML Record Review: Columbia blood agar (containing 10% bovine blood)

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_blood_agar_containing_10_bovine_blood.yaml`
- Started UTC: `2026-09-22T10:37:32Z`
- Finished UTC: `2026-09-22T10:42:47Z`
- Verdict: needs curation

## Target

Generated bacterial `MediaRecipe` record `CultureMech:009496` for TOGO Medium `M2973`, `Columbia blood agar (containing 10% bovine blood)`, generated from `data/normalized_yaml/bacterial/columbia_blood_agar_containing_10_bovine_blood.yaml` on merge fingerprint `167aaf42b3cbeab328565a5186ed5a09e008dab7da4bd43a4483d1fb9e32cf05`.

## Validation

- LinkML open schema validation: passed.
- Strict validation: passed with no errors in `/private/tmp/columbia_blood_agar_containing_10_bovine_blood.strict.tsv`.
- LinkML reference validation: passed; the validator reported 0 total checks.
- LinkML term validation: passed.
- Embedded `curation_history` entries: not checked by the standalone history validator.

## Identity and Grounding

The TOGO identity is coherent. TOGO `M2973` names the recipe `Columbia blood agar (containing 10% bovine blood)` and its structured API payload contains 10% bovine blood plus 1 L Columbia blood agar from Difco Laboratories.

The generated record is stale relative to the maintained normalized input. `data/normalized_yaml/bacterial/columbia_blood_agar_containing_10_bovine_blood.yaml` repairs the same TOGO payload to `Bovine blood` at `10 PERCENT_V_V`, grounds blood to `UBERON:0000178`, and models the Difco Columbia blood agar component as `1000 ML_PER_L`. The reviewed generated record still has the imported `10 PERCENT_W_V` and `1 G_PER_L` rows.

## Evidence

The TOGO API supports a volume-like 10% bovine-blood addition and a one-liter Columbia blood agar product row. It does not support interpreting the 1 L Columbia blood agar product as 1 g/L, and the source sentence is about Columbia blood agar containing 10% bovine blood rather than 10 g/L bovine blood.

The source payload's `src_url` field is empty and the comment cites only a numbered paper reference. Ignored-inclusive searches for the exact `H. somnus was grown on Columbia blood agar` source sentence and for `M2973` in `references_cache/` found no cached PMID, DOI, or other local bibliography record.

## Completeness

The generated file is missing the normalized record's ingredient `source` notes, blood ontology grounding, TOGO reference, `ingredients_curated` / `has_ontology_mappings` / `has_unmapped_ingredients` quality flags, and 2026-09-07 repair history.

No target organism or growth evidence is present. That is acceptable for a narrow TOGO recipe branch; the imported TOGO sentence mentions `H. somnus`, but the current maintained record only claims the source formulation.

## Findings

- Major: `Columbia blood agar (Difco Laboratories, Detroit, Mich.)` is represented as `1 G_PER_L`; the TOGO payload has `volume: 1`, `unit: L`, and the maintained input has already repaired it to `1000 ML_PER_L`.
- Major: `bovine blood` is represented as `10 PERCENT_W_V`; the TOGO payload lists a 10% blood supplement and the maintained input has already normalized it to `10 PERCENT_V_V`.
- Major: the generated output predates the maintained TOGO repair and is missing the curated source annotations, `UBERON:0000178` blood grounding, TOGO reference, and data-quality flags.

## Recommended Edits

- Regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/columbia_blood_agar_containing_10_bovine_blood.yaml` so the generated record carries `1000 ML_PER_L` Columbia blood agar and `10 PERCENT_V_V` bovine blood.
- Preserve the normalized blood grounding, ingredient-level `source` notes, `https://togomedium.org/medium/M2973` reference, data-quality flags, and 2026-09-07 repair history through the merge.
- Do not infer an `H. somnus` target-organism block from this TOGO recipe unless the original numbered paper reference is resolved and inspected.

## Follow-up Checks

- Validate the regenerated record with open schema, strict, reference, and term validators.
- Confirm no `1 G_PER_L` Columbia blood agar product row remains.
- Confirm no `PERCENT_W_V` bovine blood row remains.
- Confirm the regenerated record keeps the TOGO reference and blood grounding from the maintained normalized file.

## Additional Notes

The searches used to check for a local original-source bibliography included ignored files.
