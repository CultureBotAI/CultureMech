# YAML Record Review: ferrovum_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/ferrovum_medium.yaml
- Started UTC: 2026-09-23T03:06:19Z
- Finished UTC: 2026-09-23T03:07:38Z
- Verdict: needs curation

## Target

CultureMech:010313 is the generated merged record for TOGO Medium M896, `Ferrovum  Medium`, from JCM Medium 860.

JCM 860 is not equivalent to TOGO M752 / JCM 729 `ACIDITHIOBACILLUS FERRIVORANS MEDIUM`. JCM 860 uses 50 ml Modified UBS solution, 12.32 g MgSO4 x 7 H2O, 920 ml water, 20 ml 1.0 M FeSO4 solution, and 10 ml trace elements from JCM 748. JCM 729 uses 100 ml UBS solution, 10 ml trace minerals, 10 ml Ni-Se-W solution, 845 ml water, 25 ml 0.1 M K2S4O6 solution, and 10 ml 10 mM FeSO4 solution.

## Validation

- LinkML open-schema validation: pass; `linkml-validate` reported `No issues found`.
- Strict schema validation: pass; `scripts/validate_strict.py` reported 0 files with errors and 0 total error rows.
- Reference validation: pass; the reference validator scanned the file and reported 0 checks.
- Term validation: pass; `linkml-term-validator` exited 0 and reported `Validation passed`.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded history entries in generated MediaRecipe YAML.

## Identity and Grounding

The generated record's `media_term`, notes, and primary ID point to Togo M896 / JCM 860, but the generated ingredient values are the Togo M752 / JCM 729 UBS stock values: 30 g ammonium sulfate, 14 g sodium sulfate, 1 g KCl, 5 g MgSO4 x 7 H2O, 0.5 g K2HPO4, and 0.14 g Ca(NO3)2 x 4 H2O.

The standalone normalized JCM J860 import has a different ingredient set that includes the 20 ml FeSO4 solution and JCM 748 trace-element chemistry. The generated M896 record retains the post-autoclave solution rows only as empty solution placeholders.

## Evidence

The merge combines `TOGO_M752_Acidithiobacillus_Ferrivorans_Medium` and `TOGO_M896_Ferrovum_Medium` on one fingerprint even though their JCM source pages define different formulae, post-autoclave additions, and stock sources.

The generated top-level recipe points to M896/JCM 860 but carries M752/JCM 729 UBS values. The M896-specific 12.32 g MgSO4 x 7 H2O basal ingredient is missing, the M896 20 ml 1.0 M FeSO4 solution is present only as an empty solution stub, and the M896 10 ml JCM 748 trace-element stock is likewise present only as an empty solution stub.

The M752-specific 25 ml 0.1 M K2S4O6 and 10 ml 10 mM FeSO4 post-autoclave additions are absent after merging. Togo M752 also cross-references trace-mineral and Ni-Se-W media as M142 and M236, while the linked JCM 729 page points those stocks to JCM 151 and JCM 244.

## Completeness

The generated record is not complete for M896/JCM 860 and is not complete for M752/JCM 729.

It also loses preparation text entirely, including the required pH adjustments and filter-sterilized post-autoclave additions for both source media.

## Findings

1. Two distinct JCM media were merged into one canonical record.
2. The canonical identity is M896/JCM 860, but the materialized top-level ingredients are from M752/JCM 729.
3. M896-specific FeSO4 and trace-element additions survive only as empty `solutions` entries with source volumes misrepresented as `G_PER_L`.
4. M752-specific tetrathionate, FeSO4, trace-mineral, and Ni-Se-W additions are dropped from the canonical recipe.
5. The Togo M752 cross-references for Trace minerals and Ni-Se-W solution disagree with the linked JCM 729 source page.

## Recommended Edits

1. Split Togo M752/JCM 729 and Togo M896/JCM 860 back into separate generated records.
2. Preserve each source's stock additions as nested solutions or expand them with correct final scaling.
3. Reconcile Togo M752 stock references against the linked JCM 729 page.
4. Add pH and preparation steps for both split records.
5. Add MediaIngredientMech CHEBI links for magnesium sulfate heptahydrate and calcium nitrate tetrahydrate in the Togo-derived records if corresponding ingredient records exist.

## Follow-up Checks

- Re-run open-schema, strict-schema, reference, and term validation after splitting and recurating the records.
- Confirm M896 retains 12.32 g MgSO4 x 7 H2O and the 20 ml 1.0 M FeSO4 stock addition.
- Confirm M752 retains the 25 ml 0.1 M K2S4O6 stock addition and the 10 ml 10 mM FeSO4 stock addition.

## Additional Notes

None found.
