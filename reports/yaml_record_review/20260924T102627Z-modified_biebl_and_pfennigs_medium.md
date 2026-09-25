# YAML Record Review: MODIFIED BIEBL AND PFENNIG'S MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_biebl_and_pfennigs_medium.yaml
- Started UTC: 2026-09-24T10:26:27Z
- Finished UTC: 2026-09-24T10:26:27Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_biebl_and_pfennigs_medium.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:002847` |
| Name | `modified_biebl_and_pfennigs_medium` |
| Original name | `MODIFIED BIEBL AND PFENNIG'S MEDIUM` |
| Category | `bacterial` |
| Medium source | JCM / MediaDive `J496` |
| Maintained owner | `data/normalized_yaml/bacterial/JCM_J496_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml` |
| Generated status | Generated copy of a flattened MediaDive/JCM normalized record |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_biebl_and_pfennigs_medium.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_biebl_and_pfennigs_medium.yaml --out /private/tmp/modified_biebl_and_pfennigs_medium.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_biebl_and_pfennigs_medium.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_biebl_and_pfennigs_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_biebl_and_pfennigs_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The record identity is coherent: `CultureMech:002847`, `mediadive.medium:J496`, the label, the stored JCM URL, and pH 6.8 identify JCM Medium 496.

The filename slug is ambiguous because a separate DSMZ 1069 normalized record is also named `modified_biebl_and_pfennigs_medium`. Exact `find data/normalized_yaml -name ...` searches, which cover ignored files, resolved both relevant normalized records:

| Search | Result |
| --- | --- |
| `find data/normalized_yaml -name JCM_J496_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml` | `data/normalized_yaml/bacterial/JCM_J496_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml` |
| `find data/normalized_yaml -name modified_biebl_and_pfennigs_medium.yaml` | `data/normalized_yaml/bacterial/modified_biebl_and_pfennigs_medium.yaml`, a different DSMZ 1069 owner |
| `find data/normalized_yaml -name KOMODO_1069_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml` | `data/normalized_yaml/bacterial/KOMODO_1069_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml`, another DSMZ 1069 source copy |

## Evidence

The live JCM `GRMD=496` page and MediaDive `J496` agree on the JCM formulation.

| Source claim | Record representation | Review |
| --- | --- | --- |
| The main solution contains KH2PO4, CaCl2 x 2 H2O, MgSO4 x 7 H2O, NH4Cl, yeast extract from BD-Difco, NaCl, sorbitol, 1 L distilled water, and 1 ml Trace element solution SL-12 added after autoclaving. | The seven non-water main ingredients are present, but the water row is absent and the SL-12 addition is flattened into top-level trace rows. | Partial. |
| Trace element solution SL-12 contains Na2-EDTA, FeSO4 x 7 H2O, CoCl2 x 6 H2O, MnCl2 x 4 H2O, ZnCl2, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, H3BO3, CuCl2 x 2 H2O, and 1 L distilled water. | All nine non-water SL-12 rows are present as top-level final-medium ingredients at stock concentration; the stock water row is absent. | Unsupported stock flattening. |
| Trace element solution SL-12 is autoclaved separately and the main recipe adds 1 ml after autoclaving. | The record has generic preparation steps saying to add an unnamed component after autoclaving and autoclave separately, but no structured SL-12 solution carrying the 1 ml/L addition. | Incomplete solution ownership for preparation. |
| JCM and MediaDive specify NiCl2 x 6 H2O. | The nickel chloride hexahydrate row is grounded to generic `nickel dichloride`. | Hydrate-specific source label is not preserved in grounding. |
| MediaDive records the yeast extract attribute `BD-Difco`. | The generated row is plain `Yeast extract` with no vendor attribute. | Minor loss of source detail. |

## Completeness

The generated record is incomplete because the defining Trace element solution SL-12 compartment has been flattened into the final-medium ingredient list. Main-medium water, trace-stock water, the 1 ml/L post-autoclave addition, and stock-scoped preparation are absent or only partially preserved as unscoped prose steps.

Empty target-organism and growth-evidence fields were not treated as defects. JCM 496 and MediaDive `J496` are medium formulation pages, not growth-evidence pages.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Trace element solution SL-12 is flattened into top-level final-medium ingredients. | JCM and MediaDive define a 1 ml post-autoclave SL-12 addition; the generated record stores Na2-EDTA, FeSO4 x 7 H2O, CoCl2 x 6 H2O, MnCl2 x 4 H2O, ZnCl2, NiCl2 x 6 H2O, Na2MoO4 x 2 H2O, H3BO3, and CuCl2 x 2 H2O as direct ingredients. | `data/normalized_yaml/bacterial/JCM_J496_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml`; MediaDive stock migration. |
| major | Main and stock water rows are absent. | MediaDive J496 has 1000 ml distilled water in the Main sol. J496 and in Trace element solution SL-12; neither row appears in the generated record. | `data/normalized_yaml/bacterial/JCM_J496_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml`; MediaDive water import. |
| major | The post-autoclave SL-12 addition is only preserved as an unnamed prose fragment. | The preparation step says "Add the following component after autoclaving" but the record has no structured 1 ml/L Trace element solution SL-12 row for that instruction to target. | `data/normalized_yaml/bacterial/JCM_J496_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml`; MediaDive solution import. |
| major | NiCl2 x 6 H2O is grounded to anhydrous nickel dichloride. | The source specifies nickel chloride hexahydrate; the term is `CHEBI:34887` / `nickel dichloride`. | `data/normalized_yaml/bacterial/JCM_J496_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml`; CHEBI grounding. |
| minor | The yeast-extract vendor attribute was dropped. | MediaDive stores yeast extract with attribute `BD-Difco`; the record has only `Yeast extract`. | `data/normalized_yaml/bacterial/JCM_J496_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml`; MediaDive attribute import. |

## Recommended Edits

1. Move the nine SL-12 rows under a `Trace element solution SL-12` solution in `data/normalized_yaml/bacterial/JCM_J496_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml` and represent the source 1 ml/L addition as the final-medium ingredient.
2. Restore the 1000 ml distilled-water rows for Main sol. J496 and Trace element solution SL-12.
3. Scope `Autoclave separately` and `Adjust pH to 6.8` to SL-12 or preserve their original MediaDive/JCM ownership when the solution is nested.
4. Re-ground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term or leave it ungrounded until an exact term is available.
5. Preserve the `BD-Difco` attribute on the Yeast extract row if the schema has a suitable notes or attribute field.
6. Regenerate `data/merge_yaml/merged/modified_biebl_and_pfennigs_medium.yaml` after the normalized owner is corrected.

## Follow-up Checks

1. Run focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/JCM_J496_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml`.
2. Regenerate `data/merge_yaml/merged/modified_biebl_and_pfennigs_medium.yaml` and re-run the same validators on the generated record.
3. Manually compare the regenerated record against JCM `GRMD=496` and MediaDive `J496`, checking the 1 ml/L SL-12 addition, both water rows, pH 6.8, and the post-autoclave addition step.
4. Verify that the DSMZ 1069 normalized records with the same `modified_biebl_and_pfennigs_medium` slug remain separate from the JCM 496 recipe.

## Additional Notes

The JCM `GRMD=496` page still resolves. The MediaDive REST record for `J496` also resolves and matches the JCM formulation.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
