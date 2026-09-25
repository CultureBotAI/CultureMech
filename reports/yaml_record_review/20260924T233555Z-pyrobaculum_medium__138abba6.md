# YAML Record Review: pyrobaculum_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/pyrobaculum_medium__138abba6.yaml
- Started UTC: 2026-09-24T23:34:46Z
- Finished UTC: 2026-09-24T23:36:11Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/pyrobaculum_medium__138abba6.yaml` as a generated `MediaRecipe` for `CultureMech:005172`, label `pyrobaculum_medium`, with `media_term` `komodo.medium:390`.

The merged YAML was generated from `data/normalized_yaml/archaea/KOMODO_390_PYROBACULUM_MEDIUM.yaml`, `data/normalized_yaml/archaea/pyrobaculum_medium.yaml`, and four `data/normalized_yaml/bacterial/for_dsm_*.yaml` KOMODO rows on 2026-08-06. It is generated output; future fixes belong in the normalized DSMZ/KOMODO owners and the merge generator, followed by regeneration of `data/merge_yaml/merged`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/pyrobaculum_medium__138abba6.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/pyrobaculum_medium__138abba6.yaml --out /private/tmp/pyrobaculum_medium__138abba6.strict.tsv --workers 1 --quiet` | Passed; 1 TSV line, header only, 0 error rows. |
| Internal references | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/pyrobaculum_medium__138abba6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks were configured for this record. |
| Term grounding | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/pyrobaculum_medium__138abba6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils/pkg_resources` warning. |
| Embedded history | `just validate-history` | Not checked: the available validator covers standalone `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

`komodo.medium:390`, `mediadive.medium:390`, DSMZ Medium 390, and the DSMZ PDF all identify `PYROBACULUM MEDIUM`. The source identity is therefore aligned for the base record, and the DSMZ/MediaDive source supports pH 6.0 for the base formulation.

An ignored-file-inclusive search across `data/normalized_yaml` and `data/merge_yaml/merged` for `CultureMech:005172`, `komodo.medium:390.1`, `komodo.medium:390.2`, `komodo.medium:390.4`, `mediadive.medium:390`, `KOMODO_390_PYROBACULUM_MEDIUM`, `DSMZ_Medium390`, and the full `138abba6e54d6729367ec43083a35cb9195787a3b07425f4e56369e360344a99` fingerprint found the expected KOMODO owner, the direct DSMZ owner, the four DSM-specific KOMODO children, and generated TOGO records that cite the same DSMZ PDF.

The merged record is stale relative to the 2026-09-13 repair in `data/normalized_yaml/archaea/KOMODO_390_PYROBACULUM_MEDIUM.yaml` and `data/normalized_yaml/archaea/pyrobaculum_medium.yaml`: the maintained files now model `komodo.medium:390.1`, `390.2`, `390.3`, and `390.4` as `STRAIN_SPECIFIC_VARIANT` children, while this generated artifact still lists them as `SOURCE_DUPLICATE` children and merges all four into the base `PYROBACULUM MEDIUM` fingerprint.

## Evidence

The DSMZ PDF and MediaDive REST record for medium 390 agree on the base main-solution amounts: 1.30 g `(NH4)2SO4`, 0.28 g `KH2PO4`, 0.25 g `MgSO4 x 7 H2O`, 0.07 g `CaCl2 x 2 H2O`, 0.02 g `FeCl3 x 6 H2O`, 10.00 ml `Allen's trace element solution`, 0.50 ml sodium resazurin 0.1% w/v, 0.50 g Trypticase peptone, 0.20 g yeast extract, 2.00 g `Na2S2O3 x 5 H2O`, 0.50 g `Na2S x 9 H2O`, and 1000.00 ml distilled water. The generated direct DSMZ/KOMODO record keeps the main salts and complex ingredients at the MediaDive `g_l` concentrations but drops both the 1000 ml water row and the 10 ml Allen's stock addition.

The generated ingredient rows for `MnCl2 x 4 H2O`, `Na2B4O7 x 10 H2O`, `ZnSO4 x 7 H2O`, `CuCl2 x 2 H2O`, `Na2MoO4 x 2 H2O`, `VOSO4 x 2 H2O`, and `CoSO4 x 7 H2O` are the 1 L stock concentrations from `Allen's trace element solution`, not final medium concentrations after adding 10 ml of that stock to the main solution.

The DSMZ PDF and MediaDive `steps` also support anaerobic preparation instructions: sparge the base medium with 100% N2 gas for at least 30 min, autoclave, add Trypticase peptone, yeast extract, thiosulfate, and sulfide from sterile anoxic stocks prepared under 100% N2 gas, filter-sterilize sodium thiosulfate, and re-adjust final pH to 6.0 before inoculation. This generated artifact has no `preparation_steps`.

The source PDF explicitly lists non-duplicate DSM modifications: DSM 4185 replaces thiosulfate with sulfur; DSM 13380 omits Trypticase peptone, increases yeast extract to 1 g/L, lowers thiosulfate to 1 g/L, and uses pH 7.0; DSM 13514 and DSM 103086 use pH 6.8. The four `for_dsm_*` KOMODO children should stay strain-specific rather than collapsing into this base source-duplicate merge.

## Completeness

Empty optional fields are not defects.

Consequential omissions:

- No row represents the 10 ml addition of `Allen's trace element solution`.
- No row represents 1000 ml distilled water in the main solution or in the Allen's stock solution.
- No nested `solutions` structure preserves the Allen's stock composition and its pH 2 HCl adjustment.
- No preparation step preserves the N2 sparging, staged sterile additions, sodium thiosulfate filtration, or final pH adjustment from DSMZ/MediaDive 390.

The ignored-file-inclusive search described above was limited to `data/normalized_yaml` and `data/merge_yaml/merged` and found no newer generated merge of `CultureMech:005172`; the only generated `138abba6e54d6729367ec43083a35cb9195787a3b07425f4e56369e360344a99` fingerprint is this stale artifact.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | `Allen's trace element solution` has been flattened into final-medium ingredients at stock concentrations, and its 10 ml main-solution addition is absent. | DSMZ/MediaDive 390 add 10 ml of Allen's trace stock to the main recipe and define `MnCl2 x 4 H2O` through `CoSO4 x 7 H2O` in a separate 1 L stock. The record instead lists those stock rows directly at `0.18`, `0.45`, `0.022`, `0.005`, `0.003`, `0.003`, and `0.001` g/L. | `data/normalized_yaml/archaea/pyrobaculum_medium.yaml`; `data/normalized_yaml/archaea/KOMODO_390_PYROBACULUM_MEDIUM.yaml` |
| Major | The DSMZ/MediaDive preparation procedure is missing from the generated record. | The source requires sparging with 100% N2, adding several substrates from sterile anoxic stocks, filter-sterilizing thiosulfate, and adjusting the final medium to pH 6.0 before inoculation; none of these steps survive in the generated YAML. | `data/normalized_yaml/archaea/KOMODO_390_PYROBACULUM_MEDIUM.yaml`; `scripts/merge_recipes.py` or the merge path that chooses canonical duplicate fields |
| Major | The generated merge is stale and merges four KOMODO strain variants as source duplicates. | The generated `variant_children` and `merged_from` still include `for_dsm_4184`, `for_dsm_4185`, `for_dsm_13380`, and `for_dsm_13514` as exact duplicates, while the 2026-09-13 maintained KOMODO owner now marks them as `STRAIN_SPECIFIC_VARIANT`. DSMZ 390 documents real strain-specific pH and ingredient modifications. | `data/normalized_yaml/archaea/KOMODO_390_PYROBACULUM_MEDIUM.yaml`; merge regeneration for `data/merge_yaml/merged` |
| Major | `medium_type: DEFINED` and `composition_type: DEFINED` are stale and conflict with the complex base recipe. | The record contains Trypticase peptone and yeast extract; both normalized source owners now say `COMPLEX` and `UNDEFINED`. | `data/merge_yaml/merged` regeneration from `data/normalized_yaml/archaea/KOMODO_390_PYROBACULUM_MEDIUM.yaml` |
| Minor | The KOMODO import history timestamp is malformed. | `curation_history[0].timestamp` is `2026-01-27T01:15:02.fZ`, which is not an ISO timestamp even though the schema validators accept it as a string. | KOMODO normalized import cleanup for `data/normalized_yaml/archaea/KOMODO_390_PYROBACULUM_MEDIUM.yaml` and the four `for_dsm_*` KOMODO rows |

## Recommended Edits

1. In `data/normalized_yaml/archaea/pyrobaculum_medium.yaml` and `data/normalized_yaml/archaea/KOMODO_390_PYROBACULUM_MEDIUM.yaml`, rehydrate `Allen's trace element solution` as a 10 ml stock addition whose stock contains the seven trace salts in 1000 ml distilled water, and keep the stock pH adjustment attached to that stock instead of to the top-level final medium.

2. Preserve the DSMZ/MediaDive 390 main-solution preparation on both the direct DSMZ owner and the KOMODO duplicate, including N2 sparging, sterile anoxic additions, sodium thiosulfate filtration, and final pH 6.0 adjustment.

3. Regenerate `data/merge_yaml/merged` from the repaired normalized files so the 2026-09-13 `STRAIN_SPECIFIC_VARIANT` relationships replace the stale 2026-08-06 `SOURCE_DUPLICATE` merge of `for_dsm_4184`, `for_dsm_4185`, `for_dsm_13380`, and `for_dsm_13514`.

4. Let regenerated output carry `medium_type: COMPLEX` and `composition_type: UNDEFINED` for the base KOMODO/DSMZ duplicate.

5. Normalize the malformed KOMODO web-import timestamp on `KOMODO_390_PYROBACULUM_MEDIUM.yaml` and its `for_dsm_*` children.

## Follow-up Checks

- Re-run the focused schema, strict, reference, and term validators on the repaired normalized DSMZ/KOMODO owners and the regenerated `data/merge_yaml/merged/pyrobaculum_medium__*.yaml` outputs.
- Re-run an ignored-file-inclusive exact search for `komodo.medium:390.1`, `komodo.medium:390.2`, `komodo.medium:390.3`, `komodo.medium:390.4`, `CultureMech:005172`, and `mediadive.medium:390` across `data/normalized_yaml` and `data/merge_yaml/merged` to confirm that only the true KOMODO base and direct DSMZ owner are source duplicates.
- Manually compare the regenerated YAML against the live MediaDive REST payload and `DSMZ_Medium390.pdf` to confirm the 10 ml Allen's stock addition is no longer inflated into stock-strength final-medium rows.

## Additional Notes

The live MediaDive REST payload reports solution volume 1010 ml for the main solution because it adds the 1000 ml water base and the 10 ml Allen's trace solution. Existing MediaDive imports divide gram amounts by 1.01 and therefore record 1.28713 g/L ammonium sulfate instead of the DSMZ PDF's human-readable 1.30 g per 1000 ml base. That convention is internally consistent in this normalized owner; the material defect is the loss of the Allen's stock boundary, not that expected 1.01 normalization.
