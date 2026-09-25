# YAML Record Review: ANAEROTIGNUM MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/anaerotignum_medium__bcb5094d.yaml
- Started UTC: 2026-09-21T12:51:45Z
- Finished UTC: 2026-09-21T12:53:03Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Path | `data/merge_yaml/merged/anaerotignum_medium__bcb5094d.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:001046` |
| Name | `anaerotignum_medium` |
| Source accession | `mediadive.medium:156` |
| Source label | `ANAEROTIGNUM MEDIUM` |
| Generated status | Generated merge from `anaerotignum_medium`, `clostridium_propionicum_medium`, and `medium_156_modified_for_dsm_6251` |

The reviewed file is the generated canonical merge for DSMZ / MediaDive Medium 156 and two KOMODO wrappers for the same DSMZ family. Its maintained owners are `data/normalized_yaml/bacterial/anaerotignum_medium.yaml`, `data/normalized_yaml/bacterial/clostridium_propionicum_medium.yaml`, and `data/normalized_yaml/bacterial/medium_156_modified_for_dsm_6251.yaml`.

The exact, gitignore-independent identity search used `rg --no-ignore --hidden` across `data/normalized_yaml`, `data/merge_yaml/merged`, `scripts`, `tests`, and `history` for `CultureMech:001046`, `CultureMech:004179`, `CultureMech:004178`, `medium_156_modified_for_dsm_6251`, `komodo.medium:156_6251`, `156_6251`, `DSM 6251`, and `clostridium_propionicum_medium`. It found the three maintained inputs, the generated merge, generated KOMODO, MediaDive, bacterial, and recipe indexes, and no exact `DSM 6251` occurrence outside the `MEDIUM 156 MODIFIED FOR DSM 6251` wrapper; ignored files were included.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/anaerotignum_medium__bcb5094d.yaml` | Passed with no issues reported |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/anaerotignum_medium__bcb5094d.yaml --out /private/tmp/anaerotignum_medium__bcb5094d.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/anaerotignum_medium__bcb5094d.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 reference checks were available |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/anaerotignum_medium__bcb5094d.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` recipe validates standalone `history/*.yaml` records, not embedded `MediaRecipe.curation_history` inside one generated merge |

The documented `just` wrappers still fail before focused validation in this checkout because project `uv` resolves with Python 3.13 and attempts to build `llvmlite==0.46.0`, whose setuptools build aborts with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`. The no-project Python 3.11 commands above validate the generated record without building the project.

## Identity and Grounding

The root record correctly identifies DSMZ / MediaDive Medium 156 by stable ID, source accession, label, category, and liquid complex-medium classification. The rendered DSMZ PDF is headed `156: ANAEROTIGNUM MEDIUM`, and the generated record keeps DSMZ's pH range and preparation text.

The two source-duplicate children are mixed. `clostridium_propionicum_medium` is KOMODO Medium 156 and plausibly denotes the same base DSMZ medium. `medium_156_modified_for_dsm_6251` is KOMODO Medium 156_6251 and its own label says `MEDIUM 156 MODIFIED FOR DSM 6251`; collapsing it as a source duplicate with an identical copied base formula erases whatever DSM 6251-specific modification the source intended.

Potassium phosphate buffer and calcium sulfate are not grounded or quantified to the source entities. DSMZ lists 5 ml of 1 M pH 7.1 potassium phosphate buffer and 2.5 ml of saturated aqueous calcium sulfate solution; the generated rows store `5 G_PER_L` buffer and `2.5 G_PER_L` plain calcium sulfate.

## Evidence

The generated record has no structured `references` or `source_data` block. I rendered `DSMZ_Medium156.pdf` directly with `mutool`.

DSMZ Medium 156 supports:

- the ten base rows from L-Alanine through 1000 ml distilled water;
- 18 mg ferrous sulfate heptahydrate, equivalent to 0.018 g/L;
- 0.5 ml 0.1% sodium resazurin solution, equivalent to 0.0005 g/L if represented as final resazurin;
- initial pH adjustment to 7.0;
- 30-45 minutes of 100% N2 sparging;
- bicarbonate and cysteine addition before dispensing;
- dispensing under 100% N2 into anoxic Hungate-type tubes or serum vials;
- autoclaving and conditional final pH 7.0-7.2 adjustment.

The exact source for the KOMODO 156_6251 modification is not represented in normalized YAML. An exhaustive exact search found only the copied wrapper and generated indexes, with no separate `DSM 6251` curation note, composition difference, or source text explaining why Medium 156_6251 is modified.

## Completeness

The base DSMZ preparation text, pH range, and milligram ferrous sulfate conversion are present.

The consequential gaps are:

- no retained 1000 ml water row;
- no true volume representation for 5 ml phosphate buffer;
- no true volume representation for 2.5 ml saturated calcium sulfate solution;
- no stable stock/solution identity for either of those two source solutions;
- no maintained representation of what changes in KOMODO Medium 156_6251 for DSM 6251.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | `medium_156_modified_for_dsm_6251` is probably not a true source duplicate. | The KOMODO child is named `MEDIUM 156 MODIFIED FOR DSM 6251` and uses accession `komodo.medium:156_6251`, but its maintained record says it has the same ingredient and concentration signature as base Medium 156. Exact ignored-inclusive search found no separate DSM 6251 evidence. | `data/normalized_yaml/bacterial/medium_156_modified_for_dsm_6251.yaml` plus the KOMODO 156_6251 source import |
| Major | Phosphate buffer and saturated calcium sulfate are modeled as mass concentrations. | DSMZ lists 5 ml potassium phosphate buffer and 2.5 ml saturated calcium sulfate solution. The generated rows store `5 G_PER_L` and `2.5 G_PER_L` as direct ingredients. | `data/normalized_yaml/bacterial/anaerotignum_medium.yaml` and the two KOMODO children |
| Minor | The source water row is absent. | DSMZ Medium 156 lists 1000 ml distilled water; the generated DSMZ/MediaDive merge has no water row. | Same maintained owner set |
| Minor | The sodium resazurin solution boundary is absent. | DSMZ lists 0.5 ml sodium resazurin solution. The generated final `0.0005 G_PER_L` resazurin amount is arithmetically plausible but no longer says the addition came from a 0.1% stock. | Same maintained owner set |

## Recommended Edits

1. Re-open the KOMODO source for `komodo.medium:156_6251` and curate the DSM 6251 modification into `data/normalized_yaml/bacterial/medium_156_modified_for_dsm_6251.yaml`; if it really is the base formula, replace the wrapper label or add evidence explaining why a modified source is identical.
2. Preserve the phosphate buffer and saturated calcium sulfate additions as milliliter solution additions in all three maintained Medium 156 inputs.
3. Restore the 1000 ml distilled-water row from DSMZ Medium 156.
4. Preserve the 0.5 ml sodium-resazurin stock boundary or add a note documenting the conversion to final resazurin mass.
5. Regenerate `data/merge_yaml/merged/anaerotignum_medium__bcb5094d.yaml` and verify the DSM 6251 wrapper is no longer emitted as an unqualified `SOURCE_DUPLICATE` unless source evidence supports that relationship.

## Follow-up Checks

1. Run `just validate-schema`, `just validate-strict`, `just validate-terms`, and `just validate-references` on all edited Medium 156 normalized records.
2. Run `just verify-merges` after regeneration.
3. Re-open the regenerated merge and verify phosphate buffer and calcium sulfate no longer appear as direct g/L masses.

## Additional Notes

The similarly named TOGO M2752 record is reviewed separately because it has a different stable ID and source lineage. Its TOGO import currently has more severe unit loss than this DSMZ / MediaDive merge.
