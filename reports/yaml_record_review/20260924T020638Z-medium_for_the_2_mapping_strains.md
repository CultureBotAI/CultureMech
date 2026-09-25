# YAML Record Review: Medium for the 2u Mapping Strains

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/medium_for_the_2_mapping_strains.yaml
- Started UTC: 2026-09-24T02:05:56Z
- Finished UTC: 2026-09-24T02:06:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:007975 |
| Record name | medium_for_the_2_mapping_strains |
| Original name | Medium for the 2u Mapping Strains |
| Generated path | data/merge_yaml/merged/medium_for_the_2_mapping_strains.yaml |
| Maintained owner | data/normalized_yaml/bacterial/medium_for_the_2_mapping_strains.yaml |
| Upstream source | TOGO:M1436, imported from NBRC_M114 |
| Upstream URL | https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=114 |

The reviewed YAML is generated from `data/normalized_yaml/bacterial/medium_for_the_2_mapping_strains.yaml`.
Future fixes for this generated record belong in that normalized TOGO M1436
owner.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/medium_for_the_2_mapping_strains.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/medium_for_the_2_mapping_strains.yaml --out /private/tmp/medium_for_the_2_mapping_strains.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with ERROR, 0 total ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/medium_for_the_2_mapping_strains.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/medium_for_the_2_mapping_strains.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in generated YAML. |

## Identity and Grounding

- The record identity matches the TOGO source: TOGO M1436 reports the same
  2u mapping-strains title, `original_media_id=NBRC_M114`, and the inspected
  NBRC Medium No. 114 page has the same title.
- The `SOLID_AGAR` physical state is supported by the 15 g/L agar row.
- The bacterial category is not supported by the inspected NBRC recipe. The
  source name and the Bacto-Yeast Nitrogen Base component both point to a yeast
  mapping-strain medium, so this import needs non-bacterial classification.
- An exact gitignore-independent search over `data/normalized_yaml` and
  `data/merge_yaml/merged` for the slug, M1436, NBRC_M114, and NBRC `NO=114`
  found this TOGO M1436 owner and generated record, plus a separate recovered
  NBRC Medium 114 owner at `data/normalized_yaml/bacterial/NBRC_116.yaml` and
  its stale generated output at `data/merge_yaml/merged/116.yaml`. Other hits
  from the same bounded search were unrelated records that share the numeric
  string `1436` or `1140`.

## Evidence

- NBRC and TOGO support Bacto-Yeast Nitrogen Base at 6.7 g, glucose at 20 g,
  distilled water at 1 L, and agar at 15 g.
- NBRC and TOGO list the four auxotrophic amino acids in milligrams, not grams:
  60 mg L-leucine, 20 mg L-histidine, 20 mg L-tryptophan, and 20 mg
  L-methionine. The reviewed YAML stores the same numeric values as
  `G_PER_L`, overstating each amino acid by 1000x.
- The separate recovered NBRC owner for Medium 114 represents the same four
  amino acids as `MG_PER_L`, confirming that the live NBRC page and a later
  in-repo NBRC recovery agree against this older TOGO import.
- No preparation, pH, gas, or stock-solution claims are present in TOGO M1436
  or the inspected NBRC Medium 114 page, so their absence is not a defect here.

## Completeness

- The four amino-acid units are materially incomplete because the unit scale is
  wrong.
- The record is missing an identity relationship or merge decision between the
  TOGO M1436 import and the recovered NBRC Medium 114 record.
- Empty target-organism growth assertions, solution lists, and preparation
  fields are acceptable for this source page.
- The exact gitignore-independent search included ignored files in normalized
  and merged YAML and found a direct NBRC duplicate for the same NBRC Medium
  114 source.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Four amino acids are off by 1000x because source milligrams were imported as grams per liter. | NBRC and TOGO list L-leucine at 60 mg and L-histidine, L-tryptophan, and L-methionine at 20 mg each; the reviewed YAML stores 60, 20, 20, and 20 as `G_PER_L`. | `data/normalized_yaml/bacterial/medium_for_the_2_mapping_strains.yaml` |
| Major | The record is classified as bacterial despite source evidence for a yeast mapping medium. | The title is for 2u mapping strains and the formulation uses Bacto-Yeast Nitrogen Base without amino acids. | `data/normalized_yaml/bacterial/medium_for_the_2_mapping_strains.yaml` |
| Major | NBRC Medium 114 has two maintained owners with different formula fidelity. | `NBRC_116.yaml` recovers the same NBRC 114 source with amino acids in `MG_PER_L`, while the TOGO M1436 owner keeps the older `G_PER_L` values. | `data/normalized_yaml/bacterial/medium_for_the_2_mapping_strains.yaml`; `data/normalized_yaml/bacterial/NBRC_116.yaml` |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/medium_for_the_2_mapping_strains.yaml`,
   change L-leucine to 60 mg/L and L-histidine, L-tryptophan, and L-methionine
   to 20 mg/L each.
2. Move this recipe out of bacterial classification or otherwise classify it as
   a yeast/fungal mapping medium according to the repository's supported
   categories.
3. Reconcile the TOGO M1436 record with the recovered NBRC Medium 114 record so
   the same NBRC page does not remain represented by two divergent maintained
   recipes.
4. Regenerate merged YAML and downstream pages after the normalized owner is
   repaired.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validators on
  `data/merge_yaml/merged/medium_for_the_2_mapping_strains.yaml`.
- Re-inspect TOGO M1436 and NBRC Medium 114 after regeneration and confirm that
  only the glucose, agar, and Bacto-Yeast Nitrogen Base rows remain in gram
  units.
- Repeat an exact gitignore-independent search for `TOGO:M1436`, `NBRC_M114`,
  `NO=114`, and `medium_for_the_2_mapping_strains` across normalized and
  merged YAML after duplicate-source reconciliation.

## Additional Notes

- Source fetches used the TOGO M1436 API and the live NBRC Medium 114 page.
- No record YAML was edited during this review.
