# YAML Record Review: postgate_j_rs_medium_c__f76663b6

- Repository: CultureMech
- Record: data/merge_yaml/merged/postgate_j_rs_medium_c__f76663b6.yaml
- Started UTC: 2026-09-24T21:30:50Z
- Finished UTC: 2026-09-24T21:30:50Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:003000
- Name: postgate_j_rs_medium_c
- Source import: postgate_j_rs_medium_c
- Primary external ID: mediadive.medium:J654
- Maintained input: data/normalized_yaml/bacterial/postgate_j_rs_medium_c.yaml

This generated record represents the direct JCM import of JCM Medium 654, POSTGATE J. R'S MEDIUM C.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/postgate_j_rs_medium_c__f76663b6.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct JCM GRMD=654 identity. Exact ignored-file searches across `data` for `GRMD=654`, `JCM_M654`, and `postgate_j_rs_medium_c` found this direct-JCM normalized recipe and generated merge, plus a TOGO M670 import of the same JCM 654 formulation that remains split into `postgate_j_rs_medium_c.yaml`.

The eight base salts and yeast extract rows agree with JCM 654, and FeSO4 x 7H2O is correctly converted from 4.0 mg/L to 0.004 G_PER_L. The direct import nevertheless omits the 900 ml distilled water row, imports the 100 ml 6.0% sodium lactate addition as top-level 100 G_PER_L sodium lactate, and keeps only a truncated generic autoclave step.

## Evidence

- JCM 654 lists 0.5 g KH2PO4, 1 g NH4Cl, 4.5 g Na2SO4, 0.06 g CaCl2 x 2H2O, 0.06 g MgSO4 x 7H2O, 1 g yeast extract, 4.0 mg FeSO4 x 7H2O, 0.3 g sodium citrate, and 900 ml distilled water.
- JCM 654 then says to mix and autoclave those components, add 100 ml of 6.0% filter-sterilized sodium lactate solution, and cultivate under an N2 atmosphere.
- TOGO M670 points to the same JCM GRMD=654 page and is present as `data/normalized_yaml/bacterial/TOGO_M670_Postgate_J._R_S_Medium_C.yaml`.

## Completeness

The direct-JCM generated record is incomplete as a source-faithful JCM 654 representation:

- The 900 ml distilled water row is missing.
- The sodium lactate entry does not preserve the 6.0% stock concentration or the 100 ml addition volume.
- The N2 cultivation atmosphere is present only as free text in a generic `MIX` preparation step.
- The direct JCM and TOGO imports from the same JCM 654 source remain split.

## Findings

1. Major: JCM 654's 900 ml distilled water row is absent from the direct JCM normalized source and generated merge. Future repair belongs in `data/normalized_yaml/bacterial/postgate_j_rs_medium_c.yaml` or the JCM/MediaDive import layer.
2. Major: The post-autoclave 6.0% sodium lactate solution addition was collapsed to 100 G_PER_L top-level sodium lactate. Future repair belongs in the direct JCM normalized source.
3. Major: The direct-JCM import and TOGO M670 import of the same JCM 654 medium remain split across `postgate_j_rs_medium_c__f76663b6.yaml` and `postgate_j_rs_medium_c.yaml`.

## Recommended Edits

- Rebuild the direct JCM 654 import with the 900 ml distilled water row, a post-autoclave 100 ml 6.0% sodium lactate stock addition, and a structured N2 atmosphere field.
- Reconcile `data/normalized_yaml/bacterial/postgate_j_rs_medium_c.yaml` with `data/normalized_yaml/bacterial/TOGO_M670_Postgate_J._R_S_Medium_C.yaml` so JCM 654 no longer generates two separate `postgate_j_rs_medium_c` records.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `GRMD=654`, `JCM_M654`, and `TOGO:M670` with ignored files included to verify the direct JCM and TOGO branches are reconciled or intentionally linked.
- Spot-check the rendered JCM 654 page to verify sodium lactate appears as a post-autoclave 6.0% solution addition and water appears as 900 ml, not as a missing row.

## Additional Notes

None found.
