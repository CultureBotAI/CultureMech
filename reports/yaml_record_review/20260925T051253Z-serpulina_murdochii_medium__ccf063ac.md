# YAML Record Review: serpulina_murdochii_medium__ccf063ac

- Repository: CultureMech
- Record: data/merge_yaml/merged/serpulina_murdochii_medium__ccf063ac.yaml
- Started UTC: 2026-09-25T05:12:53Z
- Finished UTC: 2026-09-25T05:12:53Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009321`, `serpulina_murdochii_medium`, from `data/merge_yaml/merged/serpulina_murdochii_medium__ccf063ac.yaml`.

The target record merges TOGO Medium M2773 and TOGO Medium M2774 imports for the liquid Trypticase Soy Broth alternatives from DSMZ Medium 840.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO M2773/M2774 and DSMZ Medium 840.

TOGO M2773 is the 5 ml Hungate-tube formulation and TOGO M2774 is the 10 ml serum-bottle formulation. They share the same medium family but use different vessel-scale addition rows and should not be treated as exact duplicates.

## Evidence

DSMZ Medium 840 prepares Trypticase Soy Broth BBL 11774 under 80% N2 / 20% CO2 in either Hungate tubes with 5 ml per tube or 100 ml serum bottles with 10 ml per bottle.

After autoclaving and cooling, the Hungate-tube branch adds 0.30 ml sterile 10% w/v NaHCO3, 0.35 ml sterile bovine serum heat-inactivated at 56C for 45 min, 0.05 ml sterile 30% w/v glucose, and 0.5 ml air per tube.

The serum-bottle branch adds the same post-autoclave components at 0.60 ml, 0.70 ml, 0.10 ml, and 5.0 ml per bottle.

## Completeness

The generated record expands Trypticase Soy Broth into a generic TSB/TSA constituent list from a secondary product summary and even includes the TSA-only Agar component.

The source Trypticase Soy Broth BBL 11774 component is absent as an opaque product row.

The sterile NaHCO3 and glucose stock additions are empty `Unknown solution` stubs with `G_PER_L` units.

The bovine serum and air additions are represented as `G_PER_L` parent ingredients instead of ml additions scoped to the 5 ml tube or 10 ml bottle branch.

The generated M2773/M2774 merge keeps only the smaller 5 ml branch volumes and loses the 10 ml serum-bottle scale.

## Findings

The two vessel-scale source branches were merged as duplicates even though their air and addition volumes differ.

Opaque commercial Trypticase Soy Broth was replaced by inferred constituent rows.

Liquid stock additions and air volumes were converted to `G_PER_L`.

Source stock boundaries for sterile 10% NaHCO3 and sterile 30% glucose were lost.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/TOGO_M2773_Serpulina_Murdochii_Medium.yaml` and `data/normalized_yaml/bacterial/TOGO_M2774_Serpulina_Murdochii_Medium.yaml` so each keeps Trypticase Soy Broth BBL 11774 as an opaque 5 ml or 10 ml product component.

Represent sterile 10% w/v NaHCO3, sterile bovine serum, sterile 30% w/v glucose, and air as post-autoclave additions with source ml units.

Model M2773 and M2774 as vessel-scale variants of one DSMZ 840 liquid branch instead of exact duplicates, or keep both separate until their differing vessel scales can be represented without collapsing source quantities.

Remove the unsupported generic TSB/TSA constituent expansion from these TOGO source records.

Regenerate the merged YAML after the normalized TOGO sources are repaired.

## Follow-up Checks

Confirm the regenerated records contain no Agar row from the generic TSB/TSA expansion.

Confirm M2773 retains the 0.30 ml/0.35 ml/0.05 ml/0.5 ml post-autoclave additions and M2774 retains the 0.60 ml/0.70 ml/0.10 ml/5.0 ml additions.

Confirm the regenerated merge does not silently collapse M2773 and M2774 while discarding the serum-bottle branch volumes.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
