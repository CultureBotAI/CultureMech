# YAML Record Review: starch_casein_agar_sca_ph_5_5
- Repository: CultureMech
- Record: data/merge_yaml/merged/starch_casein_agar_sca_ph_5_5.yaml
- Started UTC: 2026-09-25T07:20:45Z
- Finished UTC: 2026-09-25T07:22:47Z
- Verdict: needs curation

## Target
Reviewed the generated merged record `data/merge_yaml/merged/starch_casein_agar_sca_ph_5_5.yaml`, a single-source TOGO import from `data/normalized_yaml/bacterial/starch_casein_agar_sca_ph_5_5.yaml`.

The record is identified as TOGO Medium M1947, `Starch casein agar (SCA, pH 5.5)`, with original NBRC source `NBRC_M1220`.

## Validation
- LinkML schema validation: Passed with `No issues found`.
- Strict validation: Passed; scanned 1 file and reported 0 `ERROR` rows. The strict TSV contained the header only.
- Reference validation: Passed; 1 file was validated and 0 reference checks were available.
- Term validation: Passed after the known `eutils` `pkg_resources` deprecation warning.
- Embedded `curation_history`: Not checked. The available `just validate-history` target validates standalone `history/`, not `MediaRecipe.curation_history` inside merged YAML.

## Identity and Grounding
The media identity is correct. TOGO M1947 reports name `Starch casein agar (SCA, pH 5.5)`, original media id `NBRC_M1220`, original NBRC URL `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1220`, and pH 5.5.

An exact source/id search for `TOGO:M1947`, `NBRC_M1220`, `CultureMech:008526`, and `Starch casein agar (SCA, pH 5.5)` included ignored files and found only the expected normalized TOGO file, generated merged file, and index references under `data/normalized_yaml` and `data/merge_yaml/merged`.

## Evidence
TOGO and NBRC both list Soluble starch 10 g, K2HPO4 2 g, KNO3 2 g, NaCl 2 g, Casein 0.3 g, MgSO4.7H2O 0.05 g, CaCO3 0.02 g, FeSO4.7H2O 0.01 g, Agar 15 g, Distilled water 1 L, and pH 5.5.

The generated record preserves the nine non-water ingredient masses as gram-per-liter concentrations for the 1 L recipe.

## Completeness
No target organisms are present in the generated record; no source evidence in the reviewed TOGO/NBRC material names organism growth for this recipe, so that is not a defect.

The generated record does not include `ph_value: 5.5` or a preparation step for the explicit pH 5.5 source annotation.

## Findings
- High: The 1 L distilled-water row was imported as `1 G_PER_L`. That stores the source volume as if it were a gram mass.
- Medium: The explicit source pH 5.5 is present in the source name and TOGO `ph` metadata but is absent from the generated structured `ph_value` field and `preparation_steps`.
- Low: `KNO3` still has a legacy `mediaingredientmech_term` instead of a CHEBI-keyed `mediaingredientmech_chebi_term`, despite having a valid CHEBI primary term.

## Recommended Edits
- Fix TOGO `L` solvent import so 1 L water rows are modeled as solvent volume rows or omitted consistently instead of becoming `1 G_PER_L`.
- Populate `ph_value: 5.5` or a pH preparation step from TOGO's explicit `ph` metadata.
- Add or refresh the CHEBI-keyed MediaIngredientMech link for `KNO3`.
- Regenerate merged YAML after editing the normalized source or TOGO import; do not patch `data/merge_yaml/merged/starch_casein_agar_sca_ph_5_5.yaml` by hand.

## Follow-up Checks
- After regeneration, verify that the generated record no longer has `Distilled water: 1 G_PER_L` and that pH 5.5 is represented outside the record name.
- Re-run schema, strict, reference, and term validators on the regenerated merged record.

## Additional Notes
No non-water ingredient mass corrections are needed.
