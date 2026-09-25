# YAML Record Review: MODIFIED BIEBL AND PFENNIG'S MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__2dbff5b4.yaml
- Started UTC: 2026-09-24T10:28:35Z
- Finished UTC: 2026-09-24T10:28:35Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Record | `data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__2dbff5b4.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:003657` |
| Name | `modified_biebl_and_pfennigs_medium` |
| Original name | `MODIFIED BIEBL AND PFENNIG'S MEDIUM` |
| Category | `bacterial` |
| Medium source | KOMODO / DSMZ `1069` |
| Maintained owners | Eight normalized DSMZ/KOMODO duplicate-cluster inputs under `data/normalized_yaml/bacterial` |
| Generated status | Incorrectly merged output from a base DSMZ medium and strain-specific variants |

## Validation

| Check | Result |
| --- | --- |
| Open LinkML schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__2dbff5b4.yaml` | Passed; exited 0 with "No issues found". |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__2dbff5b4.yaml --out /private/tmp/modified_biebl_and_pfennigs_medium__2dbff5b4.strict.tsv --workers 1 --quiet` | Passed; 0 strict errors were reported and `/private/tmp/modified_biebl_and_pfennigs_medium__2dbff5b4.strict.tsv` contained only the header line. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__2dbff5b4.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the focused run completed with 0 reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__2dbff5b4.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not inline `MediaRecipe.curation_history` entries in a merged YAML record. |

## Identity and Grounding

The canonical identity is partly coherent: the top-level `CultureMech:003657`, `komodo.medium:1069`, and parent `mediadive.medium:1069` identify DSMZ Medium 1069, MODIFIED BIEBL AND PFENNIG'S MEDIUM.

The generated merge is overbroad. DSMZ Medium 1069 contains the base formulation and separate strain-specific variants for DSM 18064, DSM 18713 and 18859, DSM 19947 and 19784, DSM 18985, DSM 21808 and 21809, and DSM 24766. Those variant sections change final pH and add sodium pyruvate, vitamin B12, sulfide, thiosulfate, bicarbonate, or magnesium-sulfate changes. They should not all be marked `SOURCE_DUPLICATE` of the unmodified base record.

Exact `find data/normalized_yaml -name ...` searches, which cover ignored files, found all eight generated `merged_from` owners:

| Normalized file | Expected source role |
| --- | --- |
| `data/normalized_yaml/bacterial/KOMODO_1069_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml` | Base KOMODO/DSMZ 1069 record |
| `data/normalized_yaml/bacterial/modified_biebl_and_pfennigs_medium.yaml` | Base DSMZ 1069 record |
| `data/normalized_yaml/bacterial/for_dsm_18064.yaml` | DSM 18064 variant |
| `data/normalized_yaml/bacterial/for_dsm_18713_and_18859.yaml` | DSM 18713 and 18859 variant |
| `data/normalized_yaml/bacterial/for_dsm_18985.yaml` | DSM 18985 variant |
| `data/normalized_yaml/bacterial/for_dsm_19947_and_19784.yaml` | DSM 19947 and 19784 variant |
| `data/normalized_yaml/bacterial/for_dsm_21808_and_21809.yaml` | DSM 21808 and 21809 variant |
| `data/normalized_yaml/bacterial/for_dsm_24766.yaml` | DSM 24766 variant |

## Evidence

The DSMZ Medium 1069 PDF and MediaDive 1069 REST record support the base medium and show that the strain-specific sections are true recipe variants.

| Source claim | Record representation | Review |
| --- | --- | --- |
| The base medium has KH2PO4, CaCl2 x 2 H2O, MgSO4 x 7 H2O, NH4Cl, NaCl, yeast extract, 5 ml 0.1% ferric citrate, 1 ml Trace element solution SL-7, 1000 ml distilled water, and pH 7. | The base gram rows, ferric citrate final amount, and pH are present; the SL-7 addition is flattened and the main water row is absent. | Partial. |
| Trace element solution SL-7 contains 1 L water, 1 ml 25% HCl, and seven trace salts. | HCl and the trace salts are top-level final-medium ingredients at SL-7 stock concentrations. | Unsupported stock flattening. |
| The base recipe requires bubbling the medium with nitrogen gas and filling tubes under nitrogen gas. | No `preparation_steps` are present. | Incomplete anaerobic preparation. |
| The source gives multiple `For DSM ...` variant blocks with extra post-autoclave stocks and pH changes. | `for_dsm_*` normalized records are merged into the same generated record as source duplicates and appear as synonyms. | Unsupported variant collapse. |
| The source specifies NiCl2 x 6 H2O. | The nickel chloride hexahydrate row is grounded to generic `nickel dichloride`. | Hydrate-specific source label is not preserved in grounding. |

## Completeness

The generated record is incomplete for the base DSMZ 1069 formulation because SL-7 is flattened, the water rows are absent, and the nitrogen-gas handling step is missing. It is also incomplete for the DSM-specific variants because the variant-normalized records were merged even though their defining source modifications are absent from structured composition.

Empty target-organism and growth-evidence fields were not treated as defects. DSMZ 1069, MediaDive 1069, and KOMODO 1069 are formulation sources, not growth-evidence pages.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| blocker | Strain-specific DSMZ 1069 variants were merged as exact source duplicates of the base medium. | The DSMZ PDF has distinct sections for DSM 18064, DSM 18713 and 18859, DSM 19947 and 19784, DSM 18985, DSM 21808 and 21809, and DSM 24766 with extra additives and pH changes; the generated record lists the corresponding `for_dsm_*` inputs as `SOURCE_DUPLICATE` children and synonyms. | Variant overlay curation for all `for_dsm_*` owners and duplicate-merge logic. |
| major | Trace element solution SL-7 is flattened into top-level final-medium ingredients. | MediaDive 1069 adds 1 ml SL-7 to the main solution; the record stores HCl, ZnCl2, MnCl2 x 4 H2O, H3BO3, CoCl2 x 6 H2O, CuCl2 x 2 H2O, NiCl2 x 6 H2O, and Na2MoO4 x 2 H2O as direct ingredients. | `data/normalized_yaml/bacterial/KOMODO_1069_MODIFIED_BIEBL_AND_PFENNIG_S_MEDIUM.yaml`; `data/normalized_yaml/bacterial/modified_biebl_and_pfennigs_medium.yaml`; copied duplicate sources. |
| major | Main and SL-7 water rows are absent. | DSMZ and MediaDive have 1000 ml distilled water in the main recipe and in SL-7; no water row is present in the generated base record. | DSMZ 1069 normalized owners and MediaDive water import. |
| major | The nitrogen-gas preparation step is absent. | DSMZ and MediaDive instruct bubbling the medium with nitrogen gas and filling 10 ml in 15 ml tubes under a nitrogen stream; the record has no `preparation_steps`. | DSMZ 1069 normalized owners and MediaDive step import. |
| major | NiCl2 x 6 H2O is grounded to anhydrous nickel dichloride. | The source specifies nickel chloride hexahydrate; the term is `CHEBI:34887` / `nickel dichloride`. | DSMZ 1069 normalized owners; CHEBI grounding. |

## Recommended Edits

1. Stop merging the `for_dsm_*` variant records as `SOURCE_DUPLICATE` children of the base DSMZ 1069 record; represent each DSM-specific section as a variant with its source pH and post-autoclave additions.
2. Re-curate DSMZ 1069 base owners so Trace element solution SL-7 remains a 1 ml/L stock addition with its water and trace rows nested under the solution.
3. Restore main-medium and SL-7 water rows.
4. Add the nitrogen-gas bubbling and tube-filling instruction as a preparation step on the base medium.
5. Re-ground `NiCl2 x 6 H2O` to a hydrate-specific CHEBI term or leave it ungrounded until an exact term is available.
6. Regenerate `data/merge_yaml/merged/modified_biebl_and_pfennigs_medium__2dbff5b4.yaml` after the base and variant owners are corrected.

## Follow-up Checks

1. Run focused open-schema, strict, reference, and term validators on each corrected normalized DSMZ 1069 owner.
2. Regenerate merge outputs and re-run the same validators on the base record and on each DSM-specific variant record.
3. Manually compare the base regenerated output against DSMZ Medium 1069 and MediaDive 1069 for pH 7, ferric citrate, the 1 ml SL-7 addition, SL-7 stock composition, water rows, and the nitrogen-gas instruction.
4. Manually compare each regenerated `for_dsm_*` variant against its DSMZ block, checking sodium pyruvate, vitamin B12, sulfide, thiosulfate, bicarbonate, MgSO4 x 7 H2O changes, and final pH as applicable.

## Additional Notes

The DSMZ Medium 1069 PDF at the MediaDive source URL still resolves. The MediaDive REST record for `1069` also resolves and matches the base section of the PDF.

The repository-level `just` validators were not used for this focused record review because the project currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The focused validators above were run with Python 3.11 and the offline uv cache.
