# YAML Record Review: minimal_seed_medium_liu_2004

- Repository: CultureMech
- Record: data/merge_yaml/merged/minimal_seed_medium_liu_2004.yaml
- Started UTC: 2026-09-24T07:27:46Z
- Finished UTC: 2026-09-24T07:28:13Z
- Verdict: pass with minor issues

## Target

- Generated record: `CultureMech:007284`
- Generated name: `minimal_seed_medium_liu_2004`
- Generated source file: `data/merge_yaml/merged/minimal_seed_medium_liu_2004.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/minimal_seed_medium_liu_2004.yaml`
- Upstream source: MediaDB medium `380`, `Minimal seed medium (liu 2004)`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/minimal_seed_medium_liu_2004.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with MediaDB medium `380`.
- The `media_term` points to `MEDIADB:380`.
- The eight ingredient quantities and millimolar units match MediaDB's tab-delimited medium 380 export.
- All eight ingredients have primary CHEBI terms after the pyridoxine hydrochloride re-grounding.
- `Nicotinate` lacks a `mediaingredientmech_chebi_term`, but it does have the primary CHEBI term `CHEBI:15940`.

## Evidence

- MediaDB medium `380` lists eight compounds: Biotin 4.093e-05 mM, Glucose 555.1 mM, Magnesium sulfate 3.246 mM, Nicotinate 0.03249 mM, Potassium dihydrogen phosphate 36.74 mM, Pyridoxine HCl 0.0004863 mM, Riboflavin 0.0001329 mM, and Thiamine HCl 4.447e-05 mM.
- The MediaDB `media_text/380` export contains the same eight compound/amount pairs and associates CHEBI IDs with Biotin, Nicotinate, Riboflavin, Glucose, Potassium dihydrogen phosphate, and Magnesium sulfate.
- MediaDB medium `380` links source `125`, `Liu lm et al, 2004`, with PMID `15242462`.
- The medium page links two growth-data records, both for `Candida glabrata`: CTCC M202019 at growth rate 0.059, pH 5.5, 30.0 C, and WSH-IP303 at growth rate 0.071, pH 5.5, 30.0 C.

## Completeness

- The formula is complete against MediaDB medium `380`.
- The generated `category` is `bacterial`, but the only MediaDB organisms listed for this medium are `Candida glabrata` yeast strains.
- The original label is malformed as `'''Minimal Seed Medium (Liu 2004`, and the `media_term` label carries the same leading apostrophes and missing close parenthesis.
- The `notes` field cites only the generic MediaDB reference URL, not the medium page, source page, or PMID.
- The generated preparation steps are generic MediaDB defaults and are not supported by the MediaDB 380 page.
- The MediaDB pH 5.5, 30.0 C, strain growth rates, and source 125 are not represented.
- The import `curation_history` names Mazumdar et al. 2014 as the reference even though MediaDB medium 380 links Liu et al. 2004.

## Findings

- Medium: The record is categorized and filed as `bacterial` even though MediaDB 380 is only linked to `Candida glabrata` growth data. It should be reclassified as fungal unless additional bacterial source evidence is added.
- Medium: The imported original label and `media_term` label are malformed with leading apostrophes and a missing close parenthesis.
- Low: The MediaDB source, PMID, organism growth data, pH, and temperature were not imported into structured or source-note fields.
- Low: The generated `preparation_steps` are generic and unsupported by the MediaDB medium page.
- Low: The import history references the wrong paper for this MediaDB medium.

## Recommended Edits

- Move the normalized record out of `data/normalized_yaml/bacterial/` or change its category to the repository's fungal category, then refresh any generated indexes that key off category paths.
- Repair `original_name` and the `media_term` label to `Minimal seed medium (liu 2004)`.
- Replace the generic source URL with a MediaDB 380 source note and preserve source 125 or PMID 15242462.
- Remove the generic preparation steps unless Liu et al. 2004 supplies matching sterilization details.
- Add the pH 5.5, 30.0 C, and two `Candida glabrata` growth records if the current model has a suitable location for MediaDB growth-data provenance.
- Correct the `mediadb-import` curation-history note so it no longer attributes medium 380 to Mazumdar et al. 2014.

## Follow-up Checks

- Re-fetch MediaDB `media_text/380` after curation and verify all eight compound rows still match.
- Re-fetch MediaDB growth data `744` and `745` and verify the curated category and growth-source details.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.
- The normalized-owner lookup used `rg --no-ignore --hidden`; repeat ignored-file-inclusive checks for exact owner and duplicate source paths after the edit.

## Additional Notes

- None found.
