# YAML Record Review: saline_tryptone_yeast_extract_broth__8f9f1a93

- Repository: CultureMech
- Record: data/merge_yaml/merged/saline_tryptone_yeast_extract_broth__8f9f1a93.yaml
- Started UTC: 2026-09-25T03:44:58Z
- Finished UTC: 2026-09-25T03:44:58Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:010546`, `saline_tryptone_yeast_extract_broth`, from `data/merge_yaml/merged/saline_tryptone_yeast_extract_broth__8f9f1a93.yaml`.

The record is a single-source MediaDive/JCM J668 import under the fungal category.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The recipe is correctly grounded to MediaDive J668 / `SALINE TRYPTONE-YEAST EXTRACT BROTH`.

The live JCM `GRMD=668` page currently returns "Nothing found", but MediaDive and TOGO both retain this source as JCM 668 / JCM_M668.

The generated record is a duplicate split from `saline_tryptone_yeast_extract_broth.yaml`, which is TOGO M686 for the same JCM_M668 medium.

## Evidence

MediaDive J668 lists a 1000 ml main solution with 5 g Tryptone, 3 g yeast extract, 2 g MgSO4 x 7 H2O, 100 g NaCl, 1000 ml distilled water, and an instruction to adjust pH to 7.0-7.2.

TOGO M686 carries the same medium name, original source `JCM_M668`, original `GRMD=668` URL, and the same component set with the same amounts.

## Completeness

The generated MediaDive record carries the four non-water ingredients, the pH 7.1 value, and the pH-adjustment step.

The 1000 ml distilled-water row from MediaDive is absent. This is a minor loss if the schema treats water as implicit make-up volume, but it is also the difference that kept this MediaDive import from merging with the TOGO M686 import.

## Findings

MediaDive J668 and TOGO M686 are two imports of the same original JCM 668 recipe, but the generated YAML keeps them as separate records. The split leaves duplicated `saline_tryptone_yeast_extract_broth` generated records with different CultureMech identifiers and categories.

The generated MediaDive copy drops the source water row, while the generated TOGO copy drops the pH step. Those importer differences appear to have changed the merge fingerprint even though the recipes should be coalesced.

## Recommended Edits

Repair the normalized JCM J668 and TOGO M686 inputs so they preserve the same water and pH semantics, then regenerate the merge layer and collapse the two Saline Tryptone-Yeast Extract Broth copies into one record with both `bacterial` and `fungal` categories.

Retain both source links in provenance: MediaDive `mediadive.medium:J668` and TOGO `TOGO:M686`.

## Follow-up Checks

After regeneration, confirm only one generated `saline_tryptone_yeast_extract_broth` record remains and that it carries tryptone, yeast extract, MgSO4 x 7 H2O, NaCl, make-up distilled water, and the 7.0-7.2 pH adjustment.

Recheck the JCM_M668 URL later; if JCM restores that page, compare it against both preserved imports before discarding either provenance trail.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
