# YAML Record Review: ANAEROBIOSPIRILLUM THOMASII MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml
- Started UTC: 2026-09-21T12:24:55Z
- Finished UTC: 2026-09-21T12:26:26Z
- Verdict: needs curation

## Target

- Reviewed record: `data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml`
- Class: `MediaRecipe`
- Stable ID: `CultureMech:001945`
- Label: `ANAEROBIOSPIRILLUM THOMASII MEDIUM`
- Category: `bacterial`
- Source identity: MediaDive `mediadive.medium:800`, source `DSMZ`, DSMZ medium `800`
- Generated status: generated merge record with fingerprint `8ca22612bc50f2f0ef4269b5db05a5cb8544e45db28b35973f8773d27b6e1516`
- Merge lineage: one source, `anaerobiospirillum_thomasii_medium`
- Maintained owner for future record edits: `data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml`

## Validation

- Open schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml`
  - Result: passed; no issues found
- Strict schema:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml --out /private/tmp/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.strict.tsv --workers 1 --quiet`
  - Result: passed; 1 file scanned, 0 files with errors, 0 total error rows
- Reference validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
  - Result: passed; 1 file validated, 0 total checks
- Term validator:
  - Command: `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
  - Result: passed
- Embedded curation history: Not checked. The documented `just validate-history` recipe validates standalone records under `history/`; I did not find a focused embedded `MediaRecipe.curation_history` validator for one merge file.

## Identity and Grounding

The record correctly denotes DSMZ/MediaDive medium 800. The inspected DSMZ PDF is `800. ANAEROBIOSPIRILLUM THOMASII MEDIUM`, matching the generated `original_name`, source accession, and PDF link.

The direct ingredient identities are not source-faithful. DSMZ 800 uses Wilkins Chalgrene Anaerobe Broth as a commercial base and then adds, per 10 ml, 0.5 ml 5 percent `NaHCO3`, 1.0 ml Fildes Enrichment, 0.1 ml 3 percent cysteine-HCl x H2O, and 0.1 ml 3 percent `Na2S x 9 H2O`. The generated record instead has direct `5-Aminovaleric acid`, `Fildes Enrichment`, and `3-Hydroxybenzoic acid` rows in `G_PER_L`; bicarbonate, cysteine, and sulfide are absent.

The pH is acceptable as a midpoint summary: DSMZ states that the completed medium should be pH 6.8 to 7.0 and the record stores `ph_value: 6.9`.

## Evidence

Supported:

- DSMZ 800 supports the medium number, title, Oxoid `CM 643` Wilkins Chalgrene Anaerobe Broth base, anaerobic preparation under 80 percent N2 and 20 percent CO2, post-autoclave cooling to room temperature, and addition of sterile anaerobic stock solutions per 10 ml.
- DSMZ 800 supports Fildes Enrichment as one post-autoclave volume addition and supports the completed-medium pH range of 6.8 to 7.0.
- DSMZ 800 supports Columbia sheep blood agar plates under an anaerobic atmosphere containing 5 to 10 percent CO2 as a separate agar option.

Unsupported or over-scoped:

- `5-Aminovaleric acid` is unsupported. DSMZ lists a 0.5 ml volume of 5 percent `NaHCO3` stock at that coordinate, not 0.5 g/L 5-aminovaleric acid.
- `3-Hydroxybenzoic acid` is unsupported. DSMZ lists two 0.1 ml stock additions: 3 percent cysteine-HCl x H2O and 3 percent `Na2S x 9 H2O`. Neither is 3-hydroxybenzoic acid.
- Fildes Enrichment is represented as `1 G_PER_L`, but the source amount is 1.0 ml per 10 ml.
- The 10 g/L amount for Wilkins Chalgrene Anaerobe Broth is not supported by the inspected DSMZ PDF, which names the Oxoid CM 643 product but does not state a powder mass.
- No structured source or evidence entry binds DSMZ Medium 800 to the imported formulation.

## Completeness

Consequential gaps:

- The record omits the four sterile anaerobic stock additions as solutions and cannot represent their per-10-ml volume basis.
- Bicarbonate, cysteine-HCl x H2O, and sodium sulfide nonahydrate are missing.
- The generated merge is stale relative to `data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml`: the normalized owner has a 2026-09-02 `repair_merged_duplicates.py` event that collapses the duplicated `3-Hydroxybenzoic acid` amount back to `0.1 G_PER_L`, while this generated file still shows a summed `0.2 G_PER_L`.
- The source PDF link appears only in `notes`; the record lacks structured `source_data` and `evidence`.

Correctly empty or not scored:

- `target_organisms`, `growth_metrics`, and variant links are empty. DSMZ Medium 800 is a recipe source, not primary growth evidence for Anaerobiospirillum thomasii.
- `high_metal` and `high_ree` are empty and not scored for this review.

Bounded searches:

- `find reports/yaml_record_review -maxdepth 1 -type f -name '*ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.md' -print` found no prior report for this generated record before the report was written; `find` included ignored report files.
- `rg --no-ignore --hidden -n "ANAEROBIOSPIRILLUM_THOMASII_MEDIUM|Anaerobiospirillum Thomasii|ANAEROBIOSPIRILLUM|Anaerobiospirillum" data . -g '*.yaml' -g '*.yml' -g '*.tsv' -g '*.csv' -g '*.md' -g '*.py'` covered tracked and ignored YAML/TSV/CSV/Markdown/Python files under `data` and `.`. It found the single normalized owner, this single generated merge, one organism-review candidate row, generated indexes, archived validation TSVs, and no adjacent duplicate generated record for the same medium.
- `rg --no-ignore --hidden -n "CultureMech:001945|mediadive.medium:800|DSMZ_Medium800|anaerobiospirillum_thomasii_medium|DSMZ_800_ANAEROBIOSPIRILLUM" data/curation data/normalized_yaml data/merge_yaml reports -g '*.yaml' -g '*.yml' -g '*.tsv' -g '*.csv' -g '*.json' -g '*.md'` found only the normalized owner, generated merge, generated indexes, organism-review candidate artifacts, and archived validation outputs for `CultureMech:001945`; ignored files were included.

## Findings

- **Major - bicarbonate, cysteine, and sulfide stock additions are misidentified.** The generated `5-Aminovaleric acid` and `3-Hydroxybenzoic acid` direct ingredients are unsupported substitutions for DSMZ's 5 percent `NaHCO3`, 3 percent cysteine-HCl x H2O, and 3 percent `Na2S x 9 H2O` stock additions. Future fix owner: `data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml`, with any reusable MediaDive/DSMZ percent-stock parser repair in the importer that produced the normalized record.
- **Major - volume additions were imported as mass concentrations.** DSMZ gives all four post-autoclave additions in ml per 10 ml, but `5-Aminovaleric acid`, `Fildes Enrichment`, and `3-Hydroxybenzoic acid` are stored as `G_PER_L` rows. Future fix owner: `data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml`.
- **Major - the generated merge is stale.** The authoritative normalized record collapsed the duplicated `3-Hydroxybenzoic acid` row to `0.1 G_PER_L` on 2026-09-02; the generated merge still has the pre-repair summed `0.2 G_PER_L`. Future fix owner: regenerate `data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml` after fixing the normalized owner.
- **Minor - source provenance is unstructured.** The DSMZ PDF is available only in prose `notes`, and the record has no evidence block tying DSMZ 800 to the base broth, stock-addition volumes, or pH range. Future fix owner: `data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml`.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml`, remove the unsupported `5-Aminovaleric acid` and `3-Hydroxybenzoic acid` rows.
2. Add explicit sterile anaerobic stock additions for 0.5 ml 5 percent `NaHCO3`, 1.0 ml Fildes Enrichment, 0.1 ml 3 percent cysteine-HCl x H2O, and 0.1 ml 3 percent `Na2S x 9 H2O` per 10 ml.
3. Keep Wilkins Chalgrene Anaerobe Broth as the Oxoid CM 643 commercial base, but verify or remove the unsupported `10 G_PER_L` amount unless MediaDive has a recoverable source for that powder concentration.
4. Add structured source provenance for DSMZ Medium 800 with narrow evidence snippets on the stock-addition table and completed-medium pH range.
5. Regenerate `data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml` so the generated layer reflects the September duplicate repair and the source-backed stock fixes.

## Follow-up Checks

- Rerun `just validate-schema data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml` and `just validate-strict data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml`.
- Rerun `just validate-terms data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml` to confirm bicarbonate, cysteine-HCl x H2O, and sodium sulfide nonahydrate grounding.
- Rerun `just validate-references data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml` if DSMZ PDF evidence is added.
- Rerun `just verify-merges` or the narrow merge-regeneration check that proves `data/merge_yaml/merged/ANAEROBIOSPIRILLUM_THOMASII_MEDIUM.yaml` is fresh from `data/normalized_yaml/bacterial/anaerobiospirillum_thomasii_medium.yaml`.
- Manually re-open DSMZ Medium 800 after curation and verify that every sterile stock addition remains modeled as ml per 10 ml, not as top-level dry grams per liter.

## Additional Notes

- The second preparation step preserves DSMZ's agar option, including the source typo `containig`; this is a source-text artifact rather than a curation defect.
- I did not rerun `just validate-schema`, `just validate-strict`, or `just validate-terms` directly because the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails before reaching these focused validators. The no-project Python 3.11 commands above exercised the same record-level LinkML, strict, reference, and term validators without installing the project.
