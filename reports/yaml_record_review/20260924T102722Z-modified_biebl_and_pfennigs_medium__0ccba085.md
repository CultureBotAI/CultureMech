# YAML Record Review: Modified Biebl And Pfennig's Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__0ccba085.yaml
- Started UTC: 2026-09-24T10:27:22Z
- Finished UTC: 2026-09-24T10:27:22Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__0ccba085.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:009885` |
| Name | `modified_biebl_and_pfennigs_medium` |
| Original name | `Modified Biebl And Pfennig's Medium` |
| Category | `bacterial` |
| Medium source | TOGO `M497`, mirrored from JCM `496` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml` |
| Generated status | Stale generated copy of a flattened TOGO/JCM normalized record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__0ccba085.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__0ccba085.yaml --out /private/tmp/modified_biebl_and_pfennigs_medium__0ccba085.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_biebl_and_pfennigs_medium__0ccba085.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__0ccba085.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__0ccba085.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent at the source level: `CultureMech:009885` and `TOGO:M497` identify a TOGO mirror of JCM Medium 496, Modified Biebl And Pfennig's Medium.

An exact `find data/normalized_yaml -name TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml` search, which covers ignored files, found one maintained owner at `data/normalized_yaml/bacterial/TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml`.

## Evidence

TOGO `M497` and the live JCM `GRMD=496` page agree on the source medium.

| Source claim | Record representation | Review |
| --- | --- | --- |
| The source main recipe has 1 L distilled water plus MgSO4 x 7 H2O, NaCl, CaCl2 x 2 H2O, KH2PO4, NH4Cl, sorbitol, yeast extract from BD-Difco, and a 1 ml Trace element solution SL-12 addition after autoclaving. | The seven non-water main rows are present and the yeast-extract vendor is preserved, but the 1 ml SL-12 addition is modeled as an empty `1 G_PER_L` solution stub and pH 6.8 is absent. | Partial. |
| Trace element solution SL-12 has 1 L distilled water plus Na2MoO4 x 2 H2O, H3BO3, FeSO4 x 7 H2O, MnCl2 x 4 H2O, CoCl2 x 6 H2O, NiCl2 x 6 H2O, CuCl2 x 2 H2O, ZnCl2, and EDTA x 2Na. | The trace rows are all promoted to top-level final-medium ingredients; the milligram stock rows keep their numeric source values but are stored as `G_PER_L`, for example `Na2MoO4 x 2H2O` is `18 G_PER_L` instead of 18 mg in the 1 L stock. | Unsupported stock flattening and unit conversion. |
| The source has separate 1 L water rows for the main solution and SL-12. | The generated record has one `2.0 G_PER_L` water row; the maintained owner was later repaired to one `1.0 G_PER_L` row, but still does not preserve both compartments. | Stale generated output plus incomplete water repair upstream. |
| TOGO carries pH 6.8 and JCM lists "Adjust pH to 6.8" after the SL-12 table. | The generated record has no `ph_value` and no preparation step for pH adjustment. | Incomplete pH import. |
| TOGO carries comments to add the SL-12 component after autoclaving and to autoclave SL-12 separately. | The generated record has no preparation steps, and the SL-12 addition has no structured compartment to target. | Incomplete preparation import. |
| The source specifies CoCl2 x 6 H2O and NiCl2 x 6 H2O. | Those rows are grounded to generic `cobalt dichloride` and `nickel dichloride`, respectively. | Hydrate-specific source labels are not preserved in grounding. |

## Completeness

The generated record is incomplete because the defining Trace element solution SL-12 stock is flattened, the 1 ml/L post-autoclave addition is an empty solution stub with the wrong unit, pH and source comments are missing, and water is not scoped to the main and stock compartments.

Empty target-organism and growth-evidence fields were not treated as defects. TOGO `M497` and JCM 496 are medium formulation pages, not growth-evidence pages.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Trace element solution SL-12 is flattened into top-level final-medium ingredients with wrong units for milligram rows. | TOGO places those rows under an SL-12 stock; the generated record stores values such as `300 G_PER_L` H3BO3 and `190 G_PER_L` CoCl2 x 6 H2O directly in the final medium. | `data/normalized_yaml/bacterial/TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml`; TOGO stock migration. |
| major | The SL-12 addition is an empty solution stub with the wrong addition unit. | The source adds 1 ml after autoclaving; the record has `Trace element solution SL-12 (see below)` with `composition: []` and `1 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml`; solution migration. |
| major | Main and stock water rows were collapsed together. | The source has 1 L main water and 1 L SL-12 water; the generated record has a summed `2.0 G_PER_L` row, and the maintained owner has only a collapsed `1.0 G_PER_L` row after a 2026-09-02 repair. | `data/normalized_yaml/bacterial/TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml`; duplicate cleanup must preserve compartment boundaries. |
| major | pH 6.8 and preparation comments are missing. | TOGO carries pH 6.8 plus add-after-autoclaving, separate-autoclaving, and pH-adjustment comments; the record has no `ph_value` and no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml`; TOGO comments import. |
| major | Hexahydrate trace salts are grounded to generic anhydrous salts. | Source labels `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` are grounded to `cobalt dichloride` and `nickel dichloride`. | `data/normalized_yaml/bacterial/TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml`; CHEBI grounding. |
| minor | The generated record is stale relative to the 2026-09-02 duplicate-water repair. | The generated record still sums two identical `1.0` water rows to `2.0 G_PER_L`; the maintained owner now has one collapsed `1.0 G_PER_L` row. | Merge generation from `data/normalized_yaml/bacterial/TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml`. |

## Recommended Edits

1. Move the nine SL-12 rows under a structured `Trace element solution SL-12` in `data/normalized_yaml/bacterial/TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml`; convert milligram stock rows to stock-local gram-per-liter values and keep the 1 ml/L SL-12 final-medium addition.
2. Restore separate 1 L distilled-water rows for the main solution and SL-12 instead of collapsing them by label.
3. Correct the SL-12 solution stub from `1 G_PER_L` to a 1 ml/L addition and populate its composition.
4. Add pH 6.8 and the TOGO/JCM add-after-autoclaving, separate-autoclaving, and pH-adjustment comments as structured preparation steps.
5. Re-ground `CoCl2 x 6 H2O` and `NiCl2 x 6 H2O` to hydrate-specific CHEBI terms or leave them ungrounded until exact hydrate terms are available.
6. Regenerate `data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__0ccba085.yaml` after the normalized owner is corrected.

## Follow-up Checks

1. Run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/TOGO_M497_Modified_Biebl_And_Pfennig_s_Medium.yaml`.
2. Regenerate `data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__0ccba085.yaml` and re-run the same validators on the generated record.
3. Manually compare the regenerated output against TOGO `M497` and JCM `GRMD=496`, checking pH 6.8, the 1 ml/L SL-12 addition, separated water rows, milligram trace-stock conversions, and the three preparation comments.
4. Verify that the TOGO M497 output remains distinct from the MediaDive J496 output even though both mirror JCM Medium 496 with slightly different import normalizations.

## Additional Notes

The TOGO API for `M497` still resolves, and its `src_url` points to the live JCM `GRMD=496` page reviewed for the adjacent JCM-source record.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
