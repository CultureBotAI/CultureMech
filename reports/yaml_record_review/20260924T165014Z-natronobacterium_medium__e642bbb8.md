# YAML Record Review: Natronobacterium Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronobacterium_medium__e642bbb8.yaml
- Started UTC: 2026-09-24T16:50:14Z
- Finished UTC: 2026-09-24T16:50:14Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:008909` for TOGO M2321, a DSMZ Medium 205 `Natronobacterium Medium` import.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to TOGO M2321 and its original DSMZ Medium 205 PDF.

An exact repository search including ignored and hidden files for `mediadive.medium:205`, `mediadive.medium:J166`, `TOGO:M2321`, `CultureMech:001304`, `CultureMech:002525`, `DSMZ_Medium205`, `natronobacterium_medium`, and `jcm_medium_no_166` found this TOGO M2321 generated record, its normalized TOGO owner, the active direct DSMZ/JCM source-duplicate merge for Medium 205 and JCM 166, and an active KOMODO DSMZ 205 projection.

The primary `MgSO4 x 7 H2O` term is correctly grounded to magnesium sulfate heptahydrate, but its `mediaingredientmech_chebi_term` still points at generic magnesium sulfate.

## Evidence

The TOGO API for M2321 points to the DSMZ Medium 205 PDF and carries pH 8.5.

DSMZ Medium 205 lists 15.0 g Casamino acids, 3.0 g Na3-citrate x 2 H2O, 2.5 g glutamic acid, 2.5 g MgSO4 x 7 H2O, 2.0 g KCl, 250.0 g NaCl, and 20.0 g agar per 1000.0 ml final volume.

DSMZ instructs adding distilled water to give a final volume of 1000.0 ml, dissolving agar by heating before adding sodium chloride, adjusting to pH 7.0 before autoclaving, and adjusting to pH 8.5 with sterile 5% Na2CO3 after heat sterilization.

The generated record has the correct DSMZ source accession, major ingredients, and `SOLID_AGAR` physical state.

## Completeness

The generated record lacks the DSMZ pH 8.5 final value and the pH 7.0 pre-autoclave adjustment.

The agar-before-NaCl instruction and post-sterilization sodium carbonate adjustment are absent.

## Findings

- Major: The DSMZ final volume was mis-unitized as a direct `Distilled water` row with `1000 G_PER_L`.
- Major: The final pH 8.5 and pH 7.0 pre-autoclave preparation condition are absent even though TOGO and DSMZ both expose the final pH.
- Major: The sterile 5% Na2CO3 post-sterilization adjustment was converted to a variable-concentration direct ingredient instead of a preparation reagent.
- Major: The agar-before-NaCl preparation step is absent.
- Major: TOGO M2321 is unlinked from the curated direct DSMZ/JCM Medium 205 merge and the active KOMODO Medium 205 projection.
- Minor: `MgSO4 x 7 H2O` retains a stale generic magnesium sulfate `mediaingredientmech_chebi_term`.

## Recommended Edits

- In `data/normalized_yaml/archaea/TOGO_M2321_Natronobacterium_Medium.yaml`, convert distilled water to a final 1000.0 ml volume instead of `1000 G_PER_L`.
- Add the DSMZ pH 7.0 before autoclaving and pH 8.5 after heat sterilization as structured preparation or pH data.
- Represent sterile 5% Na2CO3 as a post-sterilization pH-adjustment reagent rather than a variable direct ingredient.
- Restore the DSMZ instruction to dissolve agar by heating before adding sodium chloride.
- Collapse or link TOGO M2321 and the KOMODO Medium 205 projection with the curated DSMZ Medium 205 owner.
- Refresh the MediaIngredientMech CHEBI link for `MgSO4 x 7 H2O`.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natronobacterium_medium__e642bbb8.yaml` and verify the source water is not represented as `1000 G_PER_L`.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored and hidden files for `TOGO:M2321`, `mediadive.medium:205`, and `komodo.medium:205` to verify the duplicate family is linked or collapsed.

## Additional Notes

None found.
