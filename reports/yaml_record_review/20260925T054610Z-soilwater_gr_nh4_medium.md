# YAML Record Review: soilwater_gr_nh4_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/soilwater_gr_nh4_medium.yaml
- Started UTC: 2026-09-25T05:46:10Z
- Finished UTC: 2026-09-25T05:46:10Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:000228`, `soilwater_gr_nh4_medium`, from `data/merge_yaml/merged/soilwater_gr_nh4_medium.yaml`.

The target record is anchored on the older UTEX `Soilwater: GR-/NH4 Medium` import, then merged with 28 unrelated algae recipes.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The generated canonical record is not cleanly grounded to one UTEX medium.

The `soilwater_gr_nh4_medium` normalized slug collides for UTEX `GR+/NH4` and `GR-/NH4`; an ignored-file-inclusive filename search found both the current lowercase `GR+/NH4` file and the older uppercase `Soilwater_GR-_NH4_Medium.yaml` `GR-/NH4` file.

The generated record's `merged_from` list also collapses many unrelated enriched seawater, Erdschreiber, BG-11, Bristol NaCl, Proteose, Spirulina, Volvocacean, and soilwater recipes.

## Evidence

The UTEX `Soilwater: GR-/NH4 Medium` page states that the 200 ml total recipe prepares `Soilwater: GR- Medium` and adds 1 mg NH4MgPO4 after pasteurizing.

The repaired `Soilwater_GR-_NH4_Medium.yaml` normalized source models that as 1000 ml/L prepared `Soilwater: GR- Medium` plus 0.04 mM NH4MgPO4.

The paired `Soilwater_GR-_Medium.yaml` parent models `Soilwater: GR- Medium` from Green House Soil and dH2O.

## Completeness

The generated record still has parser artifact ingredients named `1` and `2`.

The generated `1` row stores `Enriched Seawater Medium` as an original amount rather than representing `Soilwater: GR- Medium`.

The generated `2` row stores `sterile dH2O` as an original amount rather than representing 1 mg NH4MgPO4.

The generated record lacks the prepared-Soilwater parent relation, NH4MgPO4 concentration, Sigma catalog provenance, and pH 7.3 present in the repaired normalized `GR-/NH4` source.

The generated record falsely merges 29 distinct algae recipes under the `soilwater_gr_nh4_medium` canonical ID.

## Findings

The UTEX table row ordinal bug is still present in generated YAML.

The `GR-/NH4` record was merged with unrelated algae recipes that do not have the same composition or source identity.

The `GR+/NH4` and `GR-/NH4` filename collision needs explicit handling during merge.

## Recommended Edits

Keep `Soilwater: GR+/NH4 Medium` and `Soilwater: GR-/NH4 Medium` as distinct normalized records with distinct generated outputs.

Use `data/normalized_yaml/algae/Soilwater_GR-_NH4_Medium.yaml` as the repaired source for the `GR-/NH4` branch.

Represent `GR-/NH4` as 1000 ml/L prepared `Soilwater: GR- Medium` plus 0.04 mM NH4MgPO4.

Delete the generated 29-way false merge by correcting the merge fingerprint inputs or merge-blocking these UTEX prepared-media variants.

Regenerate the merged YAML after the UTEX slug collision and merge logic are repaired.

## Follow-up Checks

Confirm the regenerated `GR-/NH4` record has no ingredients named `1` or `2`.

Confirm `GR-/NH4` links to `Soilwater: GR- Medium`, while `GR+/NH4` links to `Soilwater: GR+ Medium`.

Confirm none of the Enriched Seawater, Erdschreiber, BG-11, Bristol NaCl, Proteose, Spirulina, Volvocacean, or unrelated soilwater recipes remain merged into `GR-/NH4`.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
