# YAML Record Review: Succinate salt; Schaechter et al
- Repository: CultureMech
- Record: data/merge_yaml/merged/succinate_salt_schaechter_et_al.yaml
- Started UTC: 2026-09-25T07:38:13Z
- Finished UTC: 2026-09-25T07:38:13Z
- Verdict: pass with minor issues

## Target
Reviewed generated record `CultureMech:007124` / `succinate_salt_schaechter_et_al` from `data/merge_yaml/merged/succinate_salt_schaechter_et_al.yaml`.

The generated record has one source, MediaDB medium 229.

## Validation
- Schema validation: Passed; exited 0 with no diagnostics.
- Strict validation: Passed for 1 file with 0 total error rows.
- Reference validation: Passed for 1 file with 0 link checks and all validations passing.
- Term validation: Passed.
- Embedded curation history validation: Not checked; the standalone history validator does not target `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding
The generated record correctly preserves the MediaDB identity as `MEDIADB:229` and the name `Succinate salt; Schaechter et al`.

An exact local search found only the normalized source record, generated merged record, and indexes for `CultureMech:007124` / `MEDIADB:229`.

## Evidence
MediaDB medium 229 lists exactly six compounds and millimolar amounts: succinate 17.231 mM, citrate 5.20497 mM, dibasic sodium phosphate 28.0899 mM, potassium chloride 9.92605 mM, magnesium sulfate 0.405729 mM, and sodium ammonium phosphate 8.32187 mM.

The MediaDB tab-delimited export for medium 229 reports the same six rows and cross-references succinate, citrate, dibasic sodium phosphate, potassium chloride, and magnesium sulfate to KEGG, BiGG, ModelSEED, PubChem, and/or CHEBI where MediaDB has those fields.

The MediaDB medium page links source 84, `Schaechter et al, 1958`, and the source page identifies the article title, `Dependency on medium and temperature of cell size and chemical composition during balanced growth of salmonella typhimurium`, in Journal of General Microbiology. The medium page also associates this formulation with `Salmonella enterica Typhimurium LT2`.

## Completeness
The generated formula matches MediaDB medium 229: all six compounds are present, the millimolar concentrations are unchanged, and no extra compounds were introduced.

The imported CHEBI mappings are mostly reasonable, but `Sodium ammonium phosphate` remains ungrounded. MediaDB itself does not provide a CHEBI id for that row, so this is a curation gap rather than an import mismatch.

The generated `preparation_steps` are generic MediaDB-import placeholders. MediaDB does not provide instructions to adjust pH or filter-sterilize this medium, so those steps should either be removed or marked as inferred defaults rather than source evidence.

The curation history says `Reference: Mazumdar et al. (2014) PLOS One`, which is the MediaDB database paper, while the source-specific reference for medium 229 is Schaechter et al. 1958.

## Findings
- Formula contents and mM concentrations pass against MediaDB medium 229.
- `Sodium ammonium phosphate` lacks an ontology grounding.
- Placeholder pH-adjustment and 0.22 um filter-sterilization steps are not stated on the MediaDB medium page.
- The generated record does not retain the source organism `Salmonella enterica Typhimurium LT2`.
- Source-specific citation metadata should point to Schaechter et al. 1958, with Mazumdar et al. 2014 retained only as the MediaDB database citation if needed.

## Recommended Edits
- Keep the six-compound MediaDB 229 formula unchanged.
- Add a source-specific Schaechter et al. 1958 citation and PubMed link from MediaDB source 84.
- Add `Salmonella enterica Typhimurium LT2` as the target organism or as growth-evidence context if the schema supports it.
- Remove the generic preparation steps or annotate them as importer defaults that were not provided by MediaDB.
- Curate an ontology grounding for `Sodium ammonium phosphate` if an appropriate CHEBI term exists.

## Follow-up Checks
- Verify the regenerated record still has the same six MediaDB millimolar concentrations.
- Confirm no pH or sterilization requirement is presented as source text unless backed by a primary Schaechter source.
- Confirm `MEDIADB:229` remains the media term and Schaechter et al. 1958 is represented separately from the MediaDB database citation.
- Re-run schema, strict, reference, and term validators on any edited YAML.

## Additional Notes
The exact local search for `MEDIADB:229`, `CultureMech:007124`, `succinate_salt_schaechter_et_al`, and `Succinate salt; Schaechter et al` included ignored and hidden files under `data/normalized_yaml` and `data/merge_yaml/merged`.
