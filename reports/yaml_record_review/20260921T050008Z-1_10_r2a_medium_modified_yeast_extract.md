# YAML Record Review: 1_10_r2a_medium_modified_yeast_extract

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml`
- Started UTC: 20260921T045903Z
- Finished UTC: 20260921T050008Z
- Verdict: needs curation

## Target

| Field | Observed value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:010448` |
| Label | `1_10_r2a_medium_modified_yeast_extract` |
| Original label | `1/10 R2A MEDIUM MODIFIED (+ Yeast Extract)` |
| Category | `fungal`, with generated `categories: [bacterial, fungal]` |
| Generated or maintained | Generated merge artifact under `data/merge_yaml/merged/`; future edits belong in `data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml`, `data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml`, merge rules, or merge regeneration |
| Merge owner | `merged_from: [1_10_r2a_medium_modified, 1_10_r2a_medium_modified_yeast_extract]` |
| Maintained owners | `data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml`; `data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml` |

This generated record is the Aug 6 merge of DSMZ Medium 1365 and DSMZ Medium 1365a.

## Validation

Repository `just` entrypoints were blocked before target-specific validation because the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`.

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml` | Pass |
| Closed schema / strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml --out /private/tmp/1_10_r2a_medium_modified_yeast_extract.strict.tsv --workers 1 --quiet` | Pass; 1 file scanned, 0 files with `ERROR`, TSV at `/private/tmp/1_10_r2a_medium_modified_yeast_extract.strict.tsv` |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 1 file validated, 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/1_10_r2a_medium_modified_yeast_extract.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone files under `history/` |

## Identity and Grounding

The generated record carries the DSMZ Medium 1365a ID and label but has the DSMZ Medium 1365 yeast-extract quantity:

- DSMZ Medium 1365 is `1/10 R2A MEDIUM MODIFIED` and uses 0.050 g yeast extract.
- DSMZ Medium 1365a is `1/10 R2A MEDIUM MODIFIED (+ Yeast Extract)` and uses 0.250 g yeast extract.
- The generated 1365a canonical has `Yeast extract` at 0.05 g/L and lists DSMZ 1365 as a synonym/source duplicate.

The other ingredient rows, pH range, agar, and preparation note agree between the two DSMZ PDFs.

## Evidence

Supported by inspected source text:

- The DSMZ 1365a source supports Proteose Peptone, Casamino acids, Glucose, Soluble starch, MgSO4 x 7 H2O, Agar, pH 4.5-5.0, alginic-acid adjustment before agar, boiling to dissolve agar, and autoclaving for 15 min at 121 degrees C.
- DSMZ 1365 and 1365a differ by the yeast-extract amount only.

Unsupported or malformed in the generated record:

- The 1365a canonical's 0.05 g/L yeast-extract amount is the DSMZ 1365 value, not the 1365a value.
- DSMZ 1365 is not a source duplicate of DSMZ 1365a.
- The 1000 ml distilled-water row is missing.
- The source's `Proteose Peptone (Difco no. 3)` qualifier is not represented.
- The DSMZ PDF URL is present only in free-text `notes`; there is no structured `references` block for `linkml-reference-validator` to resolve.

## Completeness

- The generated record has no `variant_children` block explaining its DSMZ 1365 sibling; it only has `synonyms` and `categories`, so the 0.20 g/L yeast-extract modification is erased.
- Empty growth-evidence slots are acceptable for these imported provider recipes because the DSMZ PDFs do not state organism-specific growth observations.
- A gitignore-independent `rg --no-ignore --hidden` search over `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:010448`, `mediadive.medium:1365a`, `mediadive.medium:1365`, `DSMZ_Medium1365a`, `DSMZ_Medium1365`, and the merge fingerprint found only the expected DSMZ 1365a owner, DSMZ 1365 owner, generated merge, and ID/catalog entries.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | DSMZ 1365 and 1365a are incorrectly merged as source duplicates. | DSMZ 1365 has 0.050 g yeast extract while DSMZ 1365a has 0.250 g; those are distinct source formulations. | `data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml`, `data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml`, merge rules, then regeneration. |
| Blocker | The generated 1365a record has the wrong yeast-extract concentration. | The target identifies DSMZ 1365a but stores `Yeast extract` as `0.05 G_PER_L`; DSMZ 1365a lists 0.250 g/L. | Split the two normalized records during merge regeneration so 1365a keeps its 0.25 g/L owner value. |
| Major | The DSMZ water row is missing. | Both DSMZ sources list 1000 ml distilled water; neither normalized owner nor the generated merge represents the final water row. | Both normalized owners or the MediaDive importer. |
| Minor | The Proteose Peptone supplier qualifier is dropped. | Both DSMZ sources qualify Proteose Peptone as Difco no. 3; the YAML stores only `Proteose peptone`. | Both normalized owners or the MediaDive importer. |
| Minor | Structured references are absent. | The DSMZ PDF URL is present only in `notes`; the generated file has no `references` block, so `linkml-reference-validator` performed zero checks. | Both normalized owners or their MediaDive import mapping. |

## Recommended Edits

1. Prevent DSMZ 1365 and 1365a from merging as source duplicates; model them as yeast-extract concentration variants if the corpus should retain an explicit relationship.
2. Regenerate `data/merge_yaml/merged/` so DSMZ 1365a carries 0.25 g/L yeast extract and DSMZ 1365 carries 0.05 g/L.
3. Add the 1000 ml distilled-water row or a final-volume convention to both normalized records.
4. Preserve `Difco no. 3` on the Proteose Peptone row.
5. Add structured DSMZ references to both normalized records.

## Follow-up Checks

- `just validate-strict data/normalized_yaml/fungal/1_10_r2a_medium_modified_yeast_extract.yaml data/normalized_yaml/bacterial/1_10_r2a_medium_modified.yaml` after normalized edits.
- `just validate-references` on both owners after adding structured references.
- `just verify-merges` to prove DSMZ 1365 and 1365a no longer collapse to one generated record.
- `just validate-strict` and `just validate-terms` on both regenerated DSMZ 1365/1365a merge artifacts.
- Manual comparison to DSMZ Medium 1365 and 1365a for yeast extract, water, pH, alginic-acid adjustment, agar, and autoclaving.

## Additional Notes

- `linkml-reference-validator` performed zero checks because the generated record has no `references` block.
