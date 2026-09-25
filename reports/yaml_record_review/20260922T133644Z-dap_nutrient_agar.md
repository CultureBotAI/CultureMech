# YAML Record Review: dap_nutrient_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/dap_nutrient_agar.yaml
- Started UTC: 2026-09-22T13:34:29Z
- Finished UTC: 2026-09-22T13:36:44Z
- Verdict: needs curation

## Target

Reviewed generated record `data/merge_yaml/merged/dap_nutrient_agar.yaml` with generated identifier `CultureMech:003910`, KOMODO media term `komodo.medium:118`, original name `DAP-NUTRIENT AGAR`, category `bacterial`, and two merged sources, `KOMODO_118_DAP-NUTRIENT_AGAR` and `dap_nutrient_agar`.

## Validation

- LinkML open-schema validation: passed.
- Strict validation: passed with 0 error rows in `/private/tmp/dap_nutrient_agar.strict.tsv`.
- Reference validation: passed with 0 references checked.
- Term validation: passed.
- Embedded curation history: not checked; `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` blocks.

## Identity and Grounding

The record is grounded to DSMZ Medium 118 through both normalized sources. `data/normalized_yaml/bacterial/dap_nutrient_agar.yaml` is the direct DSMZ/MediaDive import for `mediadive.medium:118`, and `data/normalized_yaml/bacterial/KOMODO_118_DAP-NUTRIENT_AGAR.yaml` explicitly maps KOMODO Medium 118 back to DSMZ Medium 118.

The generated source-duplicate merge is legitimate at the recipe level: both normalized sources have the same name, solid-agar physical state, pH 7.0, and local ingredient concentrations for peptone, meat extract, diaminopimelic acid, and agar.

An exact gitignore-independent search for `komodo.medium:118`, `mediadive.medium:118`, `DAP-NUTRIENT AGAR`, and `dap_nutrient_agar` across normalized YAML, merged YAML, and prior YAML record reviews found only the direct DSMZ source, the KOMODO source, and this generated merge for Medium 118. The search used a non-digit boundary around the numeric medium ID so DSMZ 1180-1189 records were not counted.

## Evidence

DSMZ Medium 118 is titled `DAP-NUTRIENT AGAR` and instructs curators to add 100 mg DL-diaminopimelic acid to DSMZ Medium 1. MediaDive's DSMZ Medium 118 expansion supplies the full 1 L formula used by the local records: 5 g peptone, 3 g meat extract, 100 mg diaminopimelic acid, 15 g agar with the `if necessary` condition, and 1000 ml distilled water, with adjustment to pH 7.0 and a Bacillus sporulation note recommending 10.0 mg MnSO4 x H2O.

## Completeness

The generated record captures the expanded nitrogen and solidifying components and the pH scalar. It does not capture the MediaDive `Distilled water` row, and the merge discarded the DSMZ input's `preparation_steps` text for the pH adjustment plus Bacillus sporulation recommendation.

## Findings

1. **Preparation instructions were lost during the duplicate merge.** The direct DSMZ normalized source includes `preparation_steps` with the MediaDive step, `Adjust pH to 7.0. For Bacillus strains the addition of 10.0 mg MnSO4 x H2O is recommended for sporulation.` The generated record merged that source with the KOMODO copy, retained only scalar `ph_value: 7.0`, and dropped the Bacillus-specific recommendation entirely.

2. **The solvent row is missing.** MediaDive's expanded DSMZ Medium 118 recipe includes 1000 ml distilled water, but neither the direct DSMZ normalized source nor the generated merge represents that row. This makes the generated formula less complete than the authoritative expansion.

## Recommended Edits

- Preserve the direct DSMZ source's preparation step when source-duplicate records are merged so the generated recipe retains both pH adjustment context and the Bacillus `MnSO4 x H2O` sporulation recommendation.
- Add the DSMZ/MediaDive 1000 ml distilled-water row to `data/normalized_yaml/bacterial/dap_nutrient_agar.yaml`, then regenerate the merged YAML.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating `data/merge_yaml/merged/dap_nutrient_agar.yaml`.
- Manually compare the regenerated record against MediaDive medium 118 and the DSMZ Medium 118 PDF to confirm the DAP supplement remains 0.1 g/L and the `if necessary` agar condition survives the merge.

## Additional Notes

The review used gitignore-independent `rg --no-ignore --hidden` searches for exact Medium 118 identifiers and record names so ignored files were included in the duplicate/source scan.
