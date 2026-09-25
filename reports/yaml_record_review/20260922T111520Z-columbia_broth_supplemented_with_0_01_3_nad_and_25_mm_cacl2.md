# YAML Record Review: Columbia broth supplemented with 0.01% 3-NAD and 25 mM CaCl2

- Repository: CultureMech
- Record: `data/merge_yaml/merged/columbia_broth_supplemented_with_0_01_3_nad_and_25_mm_cacl2.yaml`
- Started UTC: 2026-09-22T11:13:00Z
- Finished UTC: 2026-09-22T11:15:20Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:008843`
- Normalized source: `data/normalized_yaml/bacterial/columbia_broth_supplemented_with_0_01_3_nad_and_25_mm_cacl2.yaml`
- Source identity: TOGO M2256, `Columbia broth supplemented with 0.01% 3-NAD and 25 mM CaCl2`
- Current generated merge: one source recipe, `columbia_broth_supplemented_with_0_01_3_nad_and_25_mm_cacl2`

## Validation

- Open schema validation: pass.
- Strict validation: pass.
- Reference validation: pass with 0 checks.
- Term validation: pass.
- Embedded `curation_history`: not checked by the standalone history validator.

## Identity and Grounding

- TOGO M2256 describes a one-liter final broth made from distilled water, 25 mM calcium chloride, 0.01% beta-NAD, and 35 g Columbia broth.
- The same TOGO payload separately expands the `Columbia broth` subcomponent into approximately 35 g of dry ingredients.
- The generated YAML flattens both the final mixture and the base subcomponent into a single peer ingredient list.

## Evidence

- TOGO API checked: `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M2256`.
- Local normalized owner checked: `data/normalized_yaml/bacterial/columbia_broth_supplemented_with_0_01_3_nad_and_25_mm_cacl2.yaml`.
- Gitignore-independent search over `data` found no additional TOGO M2256 or `CultureMech:008843` normalized YAML records.

## Completeness

- The bacterial category, complex undefined type, and liquid physical state are appropriate.
- Calcium chloride at 25 mM and beta-NAD at 0.01% are direct final-mixture supplements.
- The record needs a nested-base representation or an expanded-base representation, not both at the same level.

## Findings

1. The ingredient list double-counts Columbia broth: it includes `Columbia broth` at `35 G_PER_L` and also includes yeast extract, sodium chloride, dextrose, sodium carbonate, Tris, ferrous sulfate, magnesium sulfate, Tris HCl, proteose peptone, pancreatic digest of casein, L-cysteine HCl, and tryptic digest of beef heart from the same Columbia broth base.
2. `Distilled water` is stored as `1 G_PER_L`; TOGO encodes this as 1 L of solvent for the final medium.
3. The generated record carries one stale `MediaIngredientMech:000643` identifier on `Tris (Hydroxymethyl) Aminomethane`; the CHEBI migration did not replace that legacy key in this record.
4. Beta-NAD lacks an ontology term even though TOGO supplies GMO `GMO_001691` for this ingredient.

## Recommended Edits

1. Keep the four final-mixture ingredients and move the Columbia broth breakdown into a nested base description, or drop the opaque `Columbia broth` line if the expanded 35 g base is the chosen representation.
2. Convert the water entry away from `1 G_PER_L`; use the schema's source-preserving representation for 1 L solvent.
3. Replace the legacy Tris MediaIngredientMech identifier with a current ontology mapping.
4. Map beta-NAD to an appropriate chemical term while preserving the TOGO GMO identifier in evidence.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after changing the normalized owner and regenerating this file.
- Confirm the regenerated ingredient mass does not include both 35 g Columbia broth and its 35 g ingredient expansion.
- Re-query TOGO M2256 and verify the final-mixture supplements remain 25 mM calcium chloride and 0.01% beta-NAD.

## Additional Notes

- No source-catalogue duplicate or variant relationship was found for this medium.
- The TOGO source has no external `src_url`; the API payload itself is the checked source.
