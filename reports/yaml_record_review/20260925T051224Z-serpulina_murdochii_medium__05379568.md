# YAML Record Review: serpulina_murdochii_medium__05379568

- Repository: CultureMech
- Record: data/merge_yaml/merged/serpulina_murdochii_medium__05379568.yaml
- Started UTC: 2026-09-25T05:12:24Z
- Finished UTC: 2026-09-25T05:12:24Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009320`, `serpulina_murdochii_medium`, from `data/merge_yaml/merged/serpulina_murdochii_medium__05379568.yaml`.

The target record is a TOGO Medium M2772 import for the Columbia agar plate option from DSMZ Medium 840.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO Medium M2772 and DSMZ Medium 840.

M2772 is a Columbia Agar Plates with 5% sheep blood option from DSMZ 840, not the full DSMZ 840 liquid medium or its Trypticase Soy Agar plate option.

The repaired normalized source correctly links M2772 as a source duplicate of the canonical `columbia_agar_with_sheep_blood` product record.

## Evidence

DSMZ Medium 840 states that strains can grow on Trypticase Soy Agar with 5% defibrinated sheep blood or Columbia Agar Plates with 5% sheep blood.

TOGO Medium M2772 isolates the Columbia Agar Plates with 5% sheep blood (BBL 4354005) option as a single opaque ready-to-use product.

The current normalized M2772 source models that product as 1000 ml/L and ties it to `CultureMech:008653`, `columbia_agar_with_sheep_blood`.

## Completeness

The generated record preserves the correct BBL 4354005 Columbia agar with sheep blood product.

The generated merge layer is stale relative to the repaired normalized source: it still has a variable product concentration and lacks the 1000 ml/L ready-to-use-product row.

The generated record lacks the explicit product-use preparation step, CultureMech parent link, curated duplicate relationship, data-quality flags, and TOGO/DSMZ references that are already present in the normalized source.

## Findings

The generated M2772 record predates the September product repair.

The product row still uses a schema-defaulted `VARIABLE` concentration.

The generated record is missing the canonical Columbia agar with sheep blood source-duplicate relationship.

## Recommended Edits

Regenerate the merged YAML from `data/normalized_yaml/bacterial/TOGO_M2772_Serpulina_Murdochii_Medium.yaml`.

Keep the Columbia Agar Plates with 5% sheep blood product opaque; do not infer a recipe for the commercial plate.

Preserve the `SOURCE_DUPLICATE` relationship to `data/normalized_yaml/bacterial/columbia_agar_with_sheep_blood.yaml`.

## Follow-up Checks

Confirm the regenerated M2772 record carries a 1000 ml/L opaque Columbia agar with sheep blood product row instead of a variable concentration.

Confirm the regenerated record carries TOGO M2772 and DSMZ 840 references.

Confirm `columbia_agar_with_sheep_blood` remains the canonical parent for the BBL/BD-BBL Columbia agar with 5% sheep blood product.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
