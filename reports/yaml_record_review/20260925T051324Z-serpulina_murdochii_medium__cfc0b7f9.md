# YAML Record Review: serpulina_murdochii_medium__cfc0b7f9

- Repository: CultureMech
- Record: data/merge_yaml/merged/serpulina_murdochii_medium__cfc0b7f9.yaml
- Started UTC: 2026-09-25T05:13:24Z
- Finished UTC: 2026-09-25T05:13:24Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009319`, `serpulina_murdochii_medium`, from `data/merge_yaml/merged/serpulina_murdochii_medium__cfc0b7f9.yaml`.

The target record merges TOGO Medium M2771, the Trypticase Soy Agar sheep-blood plate option from DSMZ Medium 840, with JCM 278 `nam_agar`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

TOGO M2771 is correctly grounded to DSMZ Medium 840.

M2771 and NAM Agar share a Trypticase Soy Agar with 5% sheep blood base, but the NAM Agar source adds an N-acetylmuramic-acid disk workflow and should be modeled as a variant, not an exact source duplicate.

## Evidence

DSMZ Medium 840 lists `Trypticase Soy Agar (BBL 11043) with 5% defibrinated sheep blood` as one of the two solid-agar alternatives.

TOGO Medium M2771 isolates that same plate alternative as `Trypticase Soy Agar (BBL 11043)` plus 5% `defibrinated sheep blood`.

The NAM Agar source adds a filter-sterilized 1.5% NAM disk to Trypticase Soy Agar with 5% sheep blood and incubates under an H2-CO2-N2 gas mixture.

## Completeness

The generated record preserves the 5% defibrinated sheep blood row.

The generated record expands the source Trypticase Soy Agar product into a generic TSB/TSA constituent recipe instead of keeping BBL 11043 opaque.

The generated record merges M2771 with NAM Agar and therefore attaches the NAM Agar synonym and source ID to the DSMZ 840 plate option.

The generated record does not carry the NAM disk workflow from the NAM Agar branch, so the exact-duplicate merge loses the main feature that distinguishes NAM Agar from the unsupplemented sheep-blood TSA plate.

## Findings

Opaque commercial Trypticase Soy Agar was replaced by inferred constituent rows.

NAM Agar was merged as a `SOURCE_DUPLICATE` even though it contains an extra N-acetylmuramic-acid disk addition.

The generated merge hides the distinction between an unsupplemented Trypticase Soy Agar sheep-blood plate and a NAM-supplemented plate.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/TOGO_M2771_Serpulina_Murdochii_Medium.yaml` so it keeps `Trypticase Soy Agar (BBL 11043)` as an opaque product with 5% defibrinated sheep blood.

Remove the unsupported generic TSB/TSA constituent expansion from the TOGO M2771 source.

Change the NAM Agar relationship from `SOURCE_DUPLICATE` to a variant that adds the N-acetylmuramic-acid disk workflow to the same Trypticase Soy Agar with 5% sheep blood base.

Regenerate the merged YAML after the normalized sources are repaired.

## Follow-up Checks

Confirm the regenerated M2771 record has no Pancreatic digest of casein, Peptic digest of soybean meal, generic Glucose, Sodium chloride, Dipotassium phosphate, or Agar rows inferred from a secondary TSB/TSA summary.

Confirm the regenerated NAM Agar record remains discoverable as a NAM-supplemented variant rather than an exact duplicate.

Confirm the Serpulina M2771 record remains a solid agar record with 5% defibrinated sheep blood.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
