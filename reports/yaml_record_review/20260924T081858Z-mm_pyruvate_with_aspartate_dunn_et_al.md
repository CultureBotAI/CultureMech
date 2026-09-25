# YAML Record Review: mm_pyruvate_with_aspartate_dunn_et_al

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mm_pyruvate_with_aspartate_dunn_et_al.yaml
- Started UTC: 2026-09-24T08:18:58Z
- Finished UTC: 2026-09-24T08:18:58Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/mm_pyruvate_with_aspartate_dunn_et_al.yaml`
- Class: `MediaRecipe`
- Record ID: `CultureMech:007039`
- Label: `mm_pyruvate_with_aspartate_dunn_et_al`
- Original label: `MM-Pyruvate with aspartate; Dunn et al`
- Source grounding: `MEDIADB:149`, labelled `MM-Pyruvate with aspartate; Dunn et al`
- Category: `bacterial`
- Generated status: generated merged record with `merge_fingerprint: 2eb1f3039b4eee3d7487d52b22f2861aaf8bdf4a3758db796e3b64e49de5db84`
- Maintained owner for future edits: `data/normalized_yaml/bacterial/mm_pyruvate_with_aspartate_dunn_et_al.yaml`

## Validation

- Open schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mm_pyruvate_with_aspartate_dunn_et_al.yaml`
  - Result: passed with `No issues found`.
- Strict schema validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mm_pyruvate_with_aspartate_dunn_et_al.yaml --out /private/tmp/mm_pyruvate_with_aspartate_dunn_et_al.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows. `/private/tmp/mm_pyruvate_with_aspartate_dunn_et_al.strict.tsv` has 1 line, the header only.
- LinkML reference validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mm_pyruvate_with_aspartate_dunn_et_al.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 reference checks, all validations passed.
- Term validation:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mm_pyruvate_with_aspartate_dunn_et_al.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed.
- Embedded history validation:
  - Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated merged YAML.

## Identity and Grounding

- The generated record identity matches MediaDB medium 149: the inspected MediaDB page and tab-delimited export both name `MM-Pyruvate with aspartate; Dunn et al`.
- The inspected MediaDB tab-delimited export supports the nine source ingredients and millimolar concentrations, including `L-Aspartate` at 1.0 mM and `Iron(III) chloride` at 0.123304 mM.
- The inspected MediaDB medium 149 page links source 50, `Dunn et al, 1996`, and source 50 identifies the expected Dunn publication, not Mazumdar.
- The generated record is stale relative to its maintained source: `data/normalized_yaml/bacterial/mm_pyruvate_with_aspartate_dunn_et_al.yaml` has `Iron(III) chloride`, a CHEBI term for `L-Aspartate`, and August 20 and August 31, 2026 curation events that are absent from this generated record.
- The maintained MediaDB source was found with an exact `rg --files --no-ignore --hidden` search under `data/normalized_yaml`; ignored files were included.

## Evidence

- Eight generated ingredient rows match MediaDB's text export for medium 149 by label and concentration: Pyruvate 10.0 mM, L-Aspartate 1.0 mM, Biotin 0.0000409316 mM, Calcium chloride anhydrous 0.360425 mM, Potassium dibasic phosphate 1.2629 mM, Thiamine HCl 0.000331323 mM, Magnesium sulfate 0.40572 mM, and Sodium Glutamate 6.50468 mM.
- The ninth MediaDB ingredient is `Iron(III) chloride` at 0.123304 mM. The generated record has the truncated preferred term `'''Iron(III` and no ontology term for that row; the maintained normalized source has already repaired the preferred term to `Iron(III) chloride`.
- The preparation steps in the generated YAML are not source-supported. An exact `rg --no-ignore --hidden` search for `Dissolve all ingredients`, `specified concentrations`, `ADJUST_PH`, `FILTER_STERILIZE`, and `0.22` found none of those strings in the inspected MediaDB medium page, tab-delimited export, or source 50 page; ignored files were included by the search.
- The generated `curation_history` says the import reference was `Mazumdar et al. (2014) PLOS One`. An exact `rg --no-ignore --hidden` search for `Mazumdar` across the inspected MediaDB medium page, tab-delimited export, and source 50 page returned no matches; ignored files were included by the search.

## Completeness

- The maintained normalized record is complete for the MediaDB medium 149 ingredient list after its `L-Aspartate` grounding and `Iron(III) chloride` name repair.
- The generated merged record is stale and incomplete because it has not incorporated those maintained-source improvements.
- The source provenance is incomplete and partly wrong: the record keeps a generic MediaDB landing-page note instead of the medium URL and names Mazumdar et al. in history where the inspected MediaDB page points to Dunn et al.
- The source does not expose pH or sterilization details, so the generated adjustment and filtration steps should not appear as asserted preparation instructions.

## Findings

1. **major - generated output still contains a stale truncated MediaDB ingredient**
   - Evidence: MediaDB medium 149 lists `Iron(III) chloride` at 0.123304 mM, and the maintained normalized YAML has repaired that preferred term. The generated record still contains `'''Iron(III`.
   - Maintained owner: `data/normalized_yaml/bacterial/mm_pyruvate_with_aspartate_dunn_et_al.yaml` is already fixed; regenerate `data/merge_yaml/merged/` from it.
2. **major - generated preparation steps are unsupported by the inspected MediaDB source**
   - Evidence: the record asserts water dissolution, conditional pH adjustment, and 0.22 um filter sterilization steps. MediaDB medium 149, its tab-delimited export, and source 50 list ingredient, growth, and citation metadata but not those preparation instructions.
   - Maintained owner: `data/normalized_yaml/bacterial/mm_pyruvate_with_aspartate_dunn_et_al.yaml`, via the MediaDB importer that generated generic preparation text.
3. **minor - generated output is stale relative to the maintained `L-Aspartate` grounding**
   - Evidence: the maintained normalized YAML has an August 20, 2026 `apply_mim_groundings.py` event and maps `L-Aspartate` to `CHEBI:29991`; the generated row lacks that grounding.
   - Maintained owner: regenerate `data/merge_yaml/merged/` from `data/normalized_yaml/bacterial/mm_pyruvate_with_aspartate_dunn_et_al.yaml`.
4. **minor - source provenance names the wrong paper in curation history**
   - Evidence: the MediaDB medium 149 page links source 50, `Dunn et al, 1996`; `curation_history` says `Reference: Mazumdar et al. (2014) PLOS One`.
   - Maintained owner: `data/normalized_yaml/bacterial/mm_pyruvate_with_aspartate_dunn_et_al.yaml`, via the MediaDB import provenance mapping.

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/mm_pyruvate_with_aspartate_dunn_et_al.yaml` from the already repaired normalized source so `Iron(III) chloride` and the `L-Aspartate` grounding are carried into generated output.
2. Remove the generic preparation steps from `data/normalized_yaml/bacterial/mm_pyruvate_with_aspartate_dunn_et_al.yaml` unless Dunn source inspection provides exact pH or sterilization instructions.
3. Replace the Mazumdar import-history reference with MediaDB source 50 or the actual Dunn citation, and preserve the exact MediaDB medium 149 URL in provenance rather than only the MediaDB landing page.
4. Regenerate generated outputs after the normalized source and any importer fixes land; do not patch the generated merged file directly.

## Follow-up Checks

- Re-run open schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/mm_pyruvate_with_aspartate_dunn_et_al.yaml`.
- Compare the regenerated ingredient rows against the MediaDB medium 149 tab-delimited export.
- Re-run exact ignored-inclusive `rg --no-ignore --hidden` checks for `'''Iron`, `Iron(III) chloride`, `CHEBI:29991`, `Mazumdar`, `0.22`, and `Dunn` against the maintained normalized owner and regenerated merge output.

## Additional Notes

- The current generated output predates both the August 20, 2026 MIM grounding and the August 31, 2026 truncated-name repair in the normalized source; this is a generation staleness problem in addition to the underlying MediaDB importer provenance and generic-step defects.
