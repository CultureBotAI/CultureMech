# YAML Record Review: mm_asparagine_fillinger_et_al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mm_asparagine_fillinger_et_al.yaml
- Started UTC: 2026-09-24T08:10:48Z
- Finished UTC: 2026-09-24T08:10:48Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/mm_asparagine_fillinger_et_al.yaml`
- Class: `MediaRecipe`
- Record ID: `CultureMech:007117`
- Label: `mm_asparagine_fillinger_et_al`
- Original label: `Mm-asparagine; fillinger et al`
- Source grounding: `MEDIADB:222`, labelled `Mm-asparagine; fillinger et al`
- Category: `bacterial`
- Generated status: generated merged record with `merge_fingerprint: bd1d99d4dc29102d180791d69ae101b28cc5fae1ddb94565ec7ac6ed64139f16`
- Maintained owner for future edits: `data/normalized_yaml/bacterial/mm_asparagine_fillinger_et_al.yaml`

## Validation

- Open schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mm_asparagine_fillinger_et_al.yaml`
  - Result: passed with `No issues found`.
- Strict schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mm_asparagine_fillinger_et_al.yaml --out /private/tmp/mm_asparagine_fillinger_et_al.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows. `/private/tmp/mm_asparagine_fillinger_et_al.strict.tsv` has 1 line, the header only.
- LinkML reference validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mm_asparagine_fillinger_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 reference checks, all validations passed.
- Term validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mm_asparagine_fillinger_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed.
- Embedded history validation:
  - Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated merged YAML.

## Identity and Grounding

- The generated record identity matches MediaDB medium 222: the inspected MediaDB page and tab-delimited export both name `Mm-asparagine; fillinger et al`.
- The inspected MediaDB tab-delimited export supports all seven imported ingredients and millimolar concentrations.
- The inspected MediaDB medium 222 page links source 79, `Fillinger et al, 2000`, and source 79 identifies the paper as a Fillinger paper about two glyceraldehyde-3-phosphate dehydrogenases.
- An exact gitignore-independent search with `rg --no-ignore --hidden` over `data/normalized_yaml` and this generated target found the maintained MediaDB source at `data/normalized_yaml/bacterial/mm_asparagine_fillinger_et_al.yaml`.

## Evidence

- The seven ingredient rows are supported by MediaDB's text export for medium 222: Tryptophan 0.244822 mM, Potassium dibasic phosphate 80.3673 mM, Asparagine 25.0 mM, Potassium dihydrogen phosphate 44.0898 mM, Magnesium sulfate 0.811458 mM, Ammonium sulfate 15.1355 mM, and Sodium citrate 3.4002 mM.
- The MediaDB medium page links three growth-data pages for Bacillus subtilis 168CA, GM1500, and GM1501 on this medium, but those inspected pages expose no non-empty growth-rate, growth-value, or growth-condition fields; they are not enough to support a precise `target_organisms` entry.
- The preparation steps in the generated YAML are not source-supported. An exact `rg --no-ignore --hidden` search for `preparation_steps:`, `0.22`, `FILTER_STERILIZE`, `Adjust pH if specified`, and `Dissolve all ingredients` found those strings only in `data/merge_yaml/merged/mm_asparagine_fillinger_et_al.yaml` and `data/normalized_yaml/bacterial/mm_asparagine_fillinger_et_al.yaml`, not in the inspected MediaDB page or text export; ignored files were included by the search.
- The generated `curation_history` says the import reference was `Mazumdar et al. (2014) PLOS One`. An exact `rg --no-ignore --hidden` search for `Mazumdar` across the inspected MediaDB medium page, tab-delimited export, and source 79 page returned no matches, with ignored files included by the search.

## Completeness

- The ingredient list is complete for MediaDB medium 222.
- The source provenance is incomplete and partly wrong: the record keeps a generic MediaDB landing-page note instead of the medium URL and names Mazumdar et al. in history where the inspected MediaDB page points to Fillinger et al.
- The source does not expose pH or sterilization details, so the generated adjustment and filtration steps should not appear as asserted preparation instructions.
- Empty optional pH and discussion fields are not defects here; the inspected MediaDB page does not expose pH or curator discussion data.

## Findings

1. **major - generated preparation steps are unsupported by the inspected MediaDB source**
   - Evidence: the record asserts water dissolution, conditional pH adjustment, and 0.22 um filter sterilization steps. MediaDB medium 222 and its tab-delimited export list ingredients and related growth/source links but not those preparation instructions.
   - Maintained owner: `data/normalized_yaml/bacterial/mm_asparagine_fillinger_et_al.yaml`, via the MediaDB importer that generated generic preparation text.
2. **minor - source provenance names the wrong paper in curation history**
   - Evidence: the MediaDB medium 222 page links source 79, `Fillinger et al, 2000`; the source 79 page describes a Fillinger paper, while `curation_history` says `Reference: Mazumdar et al. (2014) PLOS One`.
   - Maintained owner: `data/normalized_yaml/bacterial/mm_asparagine_fillinger_et_al.yaml`, via the MediaDB import provenance mapping.

## Recommended Edits

1. Remove the generic preparation steps from `data/normalized_yaml/bacterial/mm_asparagine_fillinger_et_al.yaml` unless a Fillinger source inspection provides exact pH or sterilization instructions.
2. Replace the Mazumdar import-history reference with MediaDB source 79 or the actual Fillinger citation, and preserve the exact MediaDB medium 222 URL in provenance rather than only the MediaDB landing page.
3. Regenerate `data/merge_yaml/merged/mm_asparagine_fillinger_et_al.yaml` after the normalized source and any importer fixes land; do not patch the generated merged file directly.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/mm_asparagine_fillinger_et_al.yaml`.
- Compare the regenerated ingredient rows against the MediaDB medium 222 tab-delimited export.
- Re-run exact ignored-inclusive `rg --no-ignore --hidden` checks for `Mazumdar`, `0.22`, and `Fillinger` against the maintained normalized owner and regenerated merge output.

## Additional Notes

- The inspected MediaDB growth-data pages for medium 222 had organism and medium labels but no non-empty quantitative growth fields, so this review did not treat absent `target_organisms` as a source-supported omission.
