# YAML Record Review: Ravot Modified Medium For Thermoanaerovibrio SP. R101

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml`
- Started UTC: 2026-09-25T01:14:16Z
- Finished UTC: 2026-09-25T01:16:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:010153` |
| Name | `ravot_modified_medium_for_thermoanaerovibrio_sp_r101` |
| Original name | `Ravot Modified Medium For Thermoanaerovibrio SP. R101` |
| Category | `bacterial` |
| Source term | `TOGO:M748`, label `Ravot Modified Medium For Thermoanaerovibrio SP. R101` |
| Original source | `JCM_M725`, URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=725` |
| Merge fingerprint | `8c3a0b8719a89df2f1624cbe00062fe907de454da11785d57de8409f1ad602ae` |
| Generated from | `data/normalized_yaml/bacterial/TOGO_M748_Ravot_Modified_Medium_For_Thermoanaerovibrio_SP._R101.yaml` |

This is a generated merge artifact under `data/merge_yaml/merged/`. Its only `merged_from` value is `TOGO_M748_Ravot_Modified_Medium_For_Thermoanaerovibrio_SP._R101`, so the maintained normalized TOGO owner currently controls the generated record.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml --out /private/tmp/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.strict.tsv --workers 1 --quiet` | Passed; exit 0 and `/private/tmp/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.strict.tsv` has one header row and 0 error rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; exited 0 with no diagnostics. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning before `Validation passed`. |
| Embedded `curation_history` | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not the embedded `MediaRecipe.curation_history` array in this merged YAML. |

## Identity and Grounding

The target denotes TOGO M748, which wraps JCM medium 725, `RAVOT MODIFIED MEDIUM FOR THERMOANAEROVIBRIO SP. R101`. The live TOGO M748 API payload resolves `original_media_id` `JCM_M725` to the same JCM `GRMD=725` URL stored in the YAML, and the live JCM page has the same medium number and title.

A gitignore-independent exact search over `data/normalized_yaml`, `data/merge_yaml`, `reports`, and `reports/yaml_record_review` for `CultureMech:010153`, `TOGO:M748`, `JCM_M725`, `GRMD=725`, and the R101 slug found this reviewed TOGO lineage, the direct MediaDive J725 owner at `data/normalized_yaml/bacterial/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml`, and TOGO M749/M750 child variants that correctly refer back to TOGO M748 as their parent.

The simple CaCl2 x 2 H2O, NH4Cl, MgCl2 x 6 H2O, KCl, PIPES, and sulfur powder groundings match the live TOGO labels closely enough for this review. `Sodium acetate x 3H2O` is hydrated in JCM and TOGO, but is grounded to `CHEBI:32954` / `sodium acetate`; hydration is identity-significant and the current grounding drops it.

## Evidence

The live JCM and TOGO records support the main ingredient table as 1 L distilled water; 5 g yeast extract; 0.1 g CaCl2 x 2 H2O; 1 g NH4Cl; 1 mg resazurin; 0.2 g MgCl2 x 6 H2O; 0.1 g KCl; 5 g sulfur powder; 3.45 g PIPES; 0.83 g sodium acetate x 3 H2O; and 5 g Trypticase peptone.

TOGO M748 records source pH `6.5`, and JCM has two pH instructions: adjust the base medium to pH 6.5 before autoclaving and readjust the medium to pH 6.5 after adding the phosphate stocks. The generated target has no `ph_value` and no `preparation_steps`, so both pH and the order of autoclaving, cooling, phosphate-stock addition, pH readjustment, sulfur steaming, N2 distribution, sealing, and Na2S x 9 H2O addition are lost.

The TOGO JSON correctly preserves the three later rows as solution additions, not bulk gram additions:

| Source addition | Source amount | Current generated row |
|---|---:|---|
| 7% K2HPO4 solution | 4.3 ml | `solutions[0]`, empty `composition`, `4.3` `G_PER_L`, `Unknown solution` |
| 7% KH2PO4 solution | 4.3 ml | `solutions[1]`, empty `composition`, `4.3` `G_PER_L`, `Unknown solution` |
| 3% Na2S x 9 H2O solution | 10 ml | `solutions[2]`, empty `composition`, `10` `G_PER_L`, `Unknown solution` |

The direct MediaDive J725 solution import at `data/normalized_yaml/bacterial/mediadive_4649_Main_sol_J725.yaml` shows the sibling MediaDive failure mode: it scales the base gram amounts to a reported `Original volume: 1019 mL`, then stores the 4.3 ml, 4.3 ml, and 10 ml stock additions as `PERCENT_V_V` component rows without their 7% and 3% stock strengths.

## Completeness

The target has four consequential representation gaps:

- It imports `Distilled water` as `1` `G_PER_L` even though the source row is 1 L.
- It imports `Resazurin` as `1` `G_PER_L` even though the source row is 1 mg.
- It leaves three stock solution additions empty and unit-wrong.
- It omits pH and all preparation text even though both are present in the live TOGO payload.

The `N2` ingredient is also an imported atmosphere artifact. JCM uses N2 to describe the autoclaving, storage, distribution, and stock handling atmosphere; it does not list N2 in the main component table. That is lower priority than the broken numeric rows and missing protocol, but it should be moved out of `ingredients` when the preparation is restored.

The record has `variant_children` links to TOGO M749 and TOGO M750. I checked the immediate child YAMLs in the exact search context; both point back to `CultureMech:010153` and cite JCM 725 as their base recipe, so those links are plausible and are not flagged here.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The TOGO owner lost pH 6.5 and all preparation steps. | Live TOGO M748 has `ph: 6.5` and three comment paragraphs for N2 autoclaving, phosphate-stock addition, pH readjustment, sulfur steaming, N2 distribution/sealing, and Na2S x 9 H2O addition; the generated record has no `ph_value` and no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M748_Ravot_Modified_Medium_For_Thermoanaerovibrio_SP._R101.yaml` |
| Major | Three stock-solution additions are present as empty, unit-wrong `solutions`. | JCM and TOGO both describe 4.3 ml of 7% K2HPO4 solution, 4.3 ml of 7% KH2PO4 solution, and 10 ml of 3% Na2S x 9 H2O solution; the generated target has three `Unknown solution` objects with empty `composition` arrays and `G_PER_L` values of 4.3, 4.3, and 10. | `data/normalized_yaml/bacterial/TOGO_M748_Ravot_Modified_Medium_For_Thermoanaerovibrio_SP._R101.yaml`; TOGO solution-migration/import logic |
| Major | The water and resazurin source units were converted to false gram-per-liter rows. | JCM and TOGO state 1 L distilled water and 1 mg resazurin, but the generated target stores `Distilled water` as `1` `G_PER_L` and `Resazurin` as `1` `G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M748_Ravot_Modified_Medium_For_Thermoanaerovibrio_SP._R101.yaml`; TOGO unit-normalization logic |
| Major | `Sodium acetate x 3H2O` is grounded to an anhydrous sodium acetate term. | The live JCM and TOGO sources name the trihydrate; the target's `term` uses `CHEBI:32954` / `sodium acetate`. | `data/normalized_yaml/bacterial/TOGO_M748_Ravot_Modified_Medium_For_Thermoanaerovibrio_SP._R101.yaml` |
| Major | A source-equivalent direct JCM 725 lineage is not harmonized with the TOGO M748 owner. | An exact gitignore-independent search found `data/normalized_yaml/bacterial/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml`, whose `mediadive.medium:J725` record names the same live JCM `GRMD=725` source as TOGO M748. | TOGO M748 owner, direct J725 owner, and merge/import equivalence rules |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M748_Ravot_Modified_Medium_For_Thermoanaerovibrio_SP._R101.yaml`, restore `ph_value: 6.5` and preparation steps for the source pH adjustment, anaerobic autoclaving, phosphate stock additions, pH readjustment, sulfur steaming, N2 distribution/sealing, and Na2S x 9 H2O addition.
2. Replace the three empty `Unknown solution` objects with reviewed stock-addition modeling that preserves the 7% K2HPO4, 7% KH2PO4, and 3% Na2S x 9 H2O strengths and their 4.3 ml, 4.3 ml, and 10 ml addition volumes.
3. Fix `Distilled water` and `Resazurin` so the TOGO import no longer treats source liters and milligrams as gram-per-liter masses.
4. Move `N2` from the ingredient list into preparation/atmosphere context, or leave it unresolved until the schema has a reviewed gas-atmosphere representation.
5. Re-ground `Sodium acetate x 3H2O` to an exact sodium acetate trihydrate term if one is available; otherwise leave the hydrated source string ungrounded and document that no exact ChEBI term was selected.
6. Reconcile the corrected TOGO M748 record with the direct MediaDive J725 lineage at `data/normalized_yaml/bacterial/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml` and prevent the MediaDive `Main sol. J725` import from flattening stock volumes into bulk component rows.
7. Regenerate `data/merge_yaml/merged/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml` after the maintained owner or importer is fixed.

## Follow-up Checks

- Re-run the focused open-schema, strict, reference, and term validators on the repaired TOGO M748 owner and regenerated merge artifact.
- Manually compare the regenerated formula to live JCM `GRMD=725` or TOGO M748 and verify that 1 mg resazurin, 1 L water, pH 6.5, all three preparation comments, and the three milliliter stock additions are preserved correctly.
- Re-run the merge freshness/equivalence checks after fixing TOGO M748 and direct J725, then verify that no generated page publishes JCM 725 under an incompatible Ravot variant.
- Re-check the TOGO M749 and M750 parent links after the M748 owner ID and formula are harmonized with the direct J725 source.

## Additional Notes

- The exact gitignore-independent search over `data/normalized_yaml`, `data/merge_yaml`, and `reports` was deliberately scoped to exact `TOGO:M748`, `mediadive.medium:J725`, `JCM_M725`, `GRMD=725`, and record-ID strings to avoid conflating this R101 record with the G60, R8, Marinitoga, and Thermoanaerovibrio DSMZ media.
- A gitignore-independent `find` over `data/raw`, `data/normalized_yaml`, and `data/merge_yaml` for local paths containing `Thermoanaerovibrio` found the TOGO M748/direct J725 owners discussed here and the separate DSMZ/KOMODO Thermoanaerovibrio Medium records; it found no additional local R101 owner in that bounded path search.
