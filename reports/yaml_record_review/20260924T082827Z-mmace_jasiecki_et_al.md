# YAML Record Review: mmace_jasiecki_et_al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mmace_jasiecki_et_al.yaml
- Started UTC: 2026-09-24T08:28:27Z
- Finished UTC: 2026-09-24T08:28:27Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/mmace_jasiecki_et_al.yaml`
- Class: `MediaRecipe`
- Record ID: `CultureMech:007031`
- Label: `mmace_jasiecki_et_al`
- Original label: `Mmace; jasiecki et al`
- Source grounding: `MEDIADB:141`, labelled `Mmace; jasiecki et al`
- Category: `bacterial`
- Generated status: generated merged record with `merge_fingerprint: 4bbcb57eebe8f67e0e5ca881d15aa56bb19fe557b60a21217e39eaf0d2b67b07`
- Maintained owner for future edits: `data/normalized_yaml/bacterial/mmace_jasiecki_et_al.yaml`

## Validation

- Open schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mmace_jasiecki_et_al.yaml`
  - Result: passed with `No issues found`.
- Strict schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mmace_jasiecki_et_al.yaml --out /private/tmp/mmace_jasiecki_et_al.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows. `/private/tmp/mmace_jasiecki_et_al.strict.tsv` has 1 line, the header only.
- LinkML reference validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mmace_jasiecki_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 reference checks, all validations passed.
- Term validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mmace_jasiecki_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed.
- Embedded history validation:
  - Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated merged YAML.

## Identity and Grounding

- The generated record identity matches MediaDB medium 141: the inspected MediaDB page and tab-delimited export both name `Mmace; jasiecki et al`.
- The inspected MediaDB tab-delimited export supports all ten source ingredients and millimolar concentrations.
- The inspected MediaDB medium 141 page links source 44, `Jasiecki et al, 2003`, and source 44 identifies the expected Jasiecki publication, not Mazumdar.
- The maintained MediaDB source was found with an exact `rg --files --no-ignore --hidden` search under `data/normalized_yaml`; ignored files were included.

## Evidence

- All ten generated ingredient rows match MediaDB's text export for medium 141 by label and concentration: Thiamine 0.037684 mM, Maleic acid 49.9698 mM, Tromethamine 49.5295 mM, Magnesium chloride 4.91859 mM, Sodium sulfate 0.929316 mM, Dibasic sodium phosphate 0.898939 mM, Sodium chloride 42.7789 mM, Potassium chloride 26.8272 mM, Sodium acetate 75.4518 mM, and Ammonium chloride 18.6947 mM.
- The `Magnesium chloride` row is source-supported by label and concentration, but the generated ontology grounding maps it to `CHEBI:86345`, `magnesium dichloride hexahydrate`; the MediaDB export labels the row `Magnesium chloride` and exports `6636` in its CHEBI column.
- The `Thiamine` row still has `mediaingredientmech_term: MediaIngredientMech:000898` in both the generated record and maintained normalized source even though the June 5, 2026 curation history says legacy links were replaced with `mediaingredientmech_chebi_term`.
- The preparation steps in the generated YAML are not source-supported. An exact `rg --no-ignore --hidden` search for `Dissolve all ingredients`, `specified concentrations`, `ADJUST_PH`, `FILTER_STERILIZE`, and `0.22` found none of those strings in the inspected MediaDB medium page, tab-delimited export, or source 44 page; ignored files were included by the search.
- The generated `curation_history` says the import reference was `Mazumdar et al. (2014) PLOS One`. An exact `rg --no-ignore --hidden` search for `Mazumdar` across the inspected MediaDB medium page, tab-delimited export, and source 44 page returned no matches; ignored files were included by the search.

## Completeness

- The ingredient list is complete against the MediaDB medium 141 tab-delimited export.
- The source provenance is incomplete and partly wrong: the record keeps a generic MediaDB landing-page note instead of the medium URL and names Mazumdar et al. in history where the inspected MediaDB page points to Jasiecki et al.
- The source does not expose pH or sterilization details, so the generated adjustment and filtration steps should not appear as asserted preparation instructions.
- The MediaIngredientMech migration is incomplete because one legacy `mediaingredientmech_term` remains.

## Findings

1. **major - generated preparation steps are unsupported by the inspected MediaDB source**
   - Evidence: the record asserts water dissolution, conditional pH adjustment, and 0.22 um filter sterilization steps. MediaDB medium 141, its tab-delimited export, and source 44 list ingredient, growth, and citation metadata but not those preparation instructions.
   - Maintained owner: `data/normalized_yaml/bacterial/mmace_jasiecki_et_al.yaml`, via the MediaDB importer that generated generic preparation text.
2. **minor - source provenance names the wrong paper in curation history**
   - Evidence: the MediaDB medium 141 page links source 44, `Jasiecki et al, 2003`; `curation_history` says `Reference: Mazumdar et al. (2014) PLOS One`.
   - Maintained owner: `data/normalized_yaml/bacterial/mmace_jasiecki_et_al.yaml`, via the MediaDB import provenance mapping.
3. **minor - Thiamine still carries a legacy MediaIngredientMech link**
   - Evidence: both maintained and generated YAML still have `mediaingredientmech_term: MediaIngredientMech:000898` for Thiamine even though the migration history says legacy links were replaced with CHEBI-keyed links.
   - Maintained owner: `data/normalized_yaml/bacterial/mmace_jasiecki_et_al.yaml`, via the MIM legacy migration.
4. **minor - magnesium chloride has a hydrate-specific ontology term not supported by the MediaDB label**
   - Evidence: the source export labels the row `Magnesium chloride`; the YAML grounds that row to `CHEBI:86345`, `magnesium dichloride hexahydrate`.
   - Maintained owner: `data/normalized_yaml/bacterial/mmace_jasiecki_et_al.yaml`, via the source ontology enrichment.

## Recommended Edits

1. Remove the generic preparation steps from `data/normalized_yaml/bacterial/mmace_jasiecki_et_al.yaml` unless Jasiecki source inspection provides exact pH or sterilization instructions.
2. Replace the Mazumdar import-history reference with MediaDB source 44 or the actual Jasiecki citation, and preserve the exact MediaDB medium 141 URL in provenance rather than only the MediaDB landing page.
3. Complete the MIM legacy migration for Thiamine by replacing `mediaingredientmech_term` with the corresponding `mediaingredientmech_chebi_term` or by deleting the stale legacy cross-reference.
4. Recheck and, if needed, correct the `Magnesium chloride` ontology grounding to a non-hydrate magnesium chloride term supported by MediaDB's compound row.
5. Regenerate `data/merge_yaml/merged/mmace_jasiecki_et_al.yaml` after source curation; do not patch the generated merged file directly.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/mmace_jasiecki_et_al.yaml`.
- Compare the regenerated ingredient rows against the MediaDB medium 141 tab-delimited export.
- Re-run exact ignored-inclusive `rg --no-ignore --hidden` checks for `MediaIngredientMech:000898`, `mediaingredientmech_term`, `Mazumdar`, `0.22`, `Jasiecki`, and `Magnesium chloride` against the maintained normalized owner and regenerated merge output.

## Additional Notes

- No generated-output staleness was found: the maintained normalized source and generated merge share the same ingredient and provenance defects, and the generated file only adds merge metadata.
