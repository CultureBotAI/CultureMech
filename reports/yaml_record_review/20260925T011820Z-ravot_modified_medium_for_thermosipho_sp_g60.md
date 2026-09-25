# YAML Record Review: RAVOT MODIFIED MEDIUM FOR THERMOSIPHO SP. G60

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/ravot_modified_medium_for_thermosipho_sp_g60.yaml`
- Started UTC: 2026-09-25T01:16:25Z
- Finished UTC: 2026-09-25T01:18:20Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:003071` |
| Name | `ravot_modified_medium_for_thermosipho_sp_g60` |
| Original name | `RAVOT MODIFIED MEDIUM FOR THERMOSIPHO SP. G60` |
| Category | `bacterial` |
| Source term | `mediadive.medium:J727`, label `RAVOT MODIFIED MEDIUM FOR THERMOSIPHO SP. G60` |
| Source URL in notes | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=727` |
| Merge fingerprint | `3246547a833d4aee6880484f9bbbd5a1451cd42a9073f63201c32de553386d96` |
| Generated from | `data/normalized_yaml/bacterial/ravot_modified_medium_for_fervidobacterium_sp_r8.yaml`, `data/normalized_yaml/bacterial/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml`, `data/normalized_yaml/bacterial/ravot_modified_medium_for_thermosipho_sp_g60.yaml` |

This is a generated merge artifact under `data/merge_yaml/merged/`. It incorrectly merges three direct JCM/MediaDive wrappers into the G60 canonical output.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/ravot_modified_medium_for_thermosipho_sp_g60.yaml` | Passed; exited 0 with no diagnostics. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/ravot_modified_medium_for_thermosipho_sp_g60.yaml --out /private/tmp/ravot_modified_medium_for_thermosipho_sp_g60.strict.tsv --workers 1 --quiet` | Passed; exit 0 and `/private/tmp/ravot_modified_medium_for_thermosipho_sp_g60.strict.tsv` has one header row and 0 error rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/ravot_modified_medium_for_thermosipho_sp_g60.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 total checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/ravot_modified_medium_for_thermosipho_sp_g60.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known `eutils` `pkg_resources` deprecation warning before `Validation passed`. |
| Embedded `curation_history` | Not run | Not checked: `just validate-history` validates standalone files under `history/`, not the embedded `MediaRecipe.curation_history` array in this merged YAML. |

## Identity and Grounding

JCM `GRMD=727` is `RAVOT MODIFIED MEDIUM FOR THERMOSIPHO SP. G60`; the live page says to use Medium No. 725 with 20.0 g/L NaCl and adjust pH to 7.0. The target's ID, name, pH 7.0, `mediadive.medium:J727` source term, and source URL all match that wrapper identity.

The generated record stops being identity-coherent after the merge layer. It also merges direct JCM 725 / `mediadive.medium:J725` R101 and direct JCM 726 / `mediadive.medium:J726` R8 into the same canonical G60 record, lists the R101 and R8 slugs as synonyms, and records both children as `SOURCE_DUPLICATE` variants. The live JCM pages show that they are not duplicates: JCM 725 is the R101 base medium, JCM 726 uses Medium 725 with 5.0 g/L NaCl at pH 6.3, and JCM 727 uses Medium 725 with 20.0 g/L NaCl at pH 7.0.

A gitignore-independent exact search over `data/normalized_yaml`, `data/merge_yaml`, and review/report files for `CultureMech:003071`, `mediadive.medium:J727`, `GRMD=727`, `TOGO:M750`, and `CultureMech:010156` found the direct J727 owner reviewed here and a separate, repaired TOGO M750 owner at `data/normalized_yaml/bacterial/TOGO_M750_Ravot_Modified_Medium_For_Thermosipho_SP._G60.yaml`. TOGO M750 now models G60 as a salinity variant of TOGO M748 with 20.0 g/L NaCl, pH 7.0, and a 1000 ml/L base-medium solution.

## Evidence

The inspected JCM 727 and TOGO M750 sources both support only a wrapper formula: prepared Medium 725 plus 20.0 g/L NaCl, adjusted to pH 7.0. The current generated record has `ph_value: 7.0` and a preparation string with that wrapper instruction, but no `NaCl` ingredient; therefore its defining G60 amendment is not machine-readable as composition.

The thirteen generated ingredient rows were copied from the direct JCM 725/R101 owner, not from JCM 727. Because the copied JCM 725 owner is itself malformed, the G60 merge inherited the same stock-addition errors: 4.3 ml of 7% KH2PO4, 4.3 ml of 7% K2HPO4, and 10 ml of 3% Na2S x 9 H2O are represented as 4.3, 4.3, and 10 `G_PER_L` direct ingredients.

The copied base rows also carry two inherited grounding defects:

- JCM 725 supplies sulfur powder, but the copied `Sulfur` row is grounded to `CHEBI:26833` / `sulfur atom`.
- JCM 725 supplies sodium acetate x 3 H2O, but the copied `Sodium acetate x 3 H2O` row is grounded to `CHEBI:32954` / `sodium acetate`.

The inspected JCM 726 source supports R8 as Medium 725 with 5.0 g/L NaCl and pH 6.3. Those source facts conflict with the generated merge's `SOURCE_DUPLICATE` treatment of the R8 and G60 owners.

## Completeness

The direct J727 owner is stale beside the repaired TOGO M750 owner. TOGO M750 retains just the 20.0 g/L NaCl amendment, points at TOGO M748 as the base, keeps `ph_value: 7.0`, represents the base as 1000 ml/L of `CultureMech:010153`, and records `SALINITY_VARIANT`; the direct J727 record instead materializes a stale copy of all direct J725 base ingredients and loses the 20.0 g/L NaCl from `ingredients`.

The generated record has no `references` array. The generated `notes` slot names the JCM 727 URL, so the source can be recovered, but the cleaner TOGO M750 owner already records explicit references to TOGO M750, JCM 727, TOGO M748, and JCM 725.

Empty `target_organisms` and growth-evidence fields are not flagged. JCM 727 and TOGO M750 are recipes, not growth studies for Thermosipho sp. G60.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The generated G60 record falsely merges distinct JCM 725, 726, and 727 recipes. | JCM 725 is the R101 base medium, JCM 726 is base plus 5.0 g/L NaCl at pH 6.3, and JCM 727 is base plus 20.0 g/L NaCl at pH 7.0; the generated record merges all three direct MediaDive owners and lists J725/J726 as G60 synonyms and `SOURCE_DUPLICATE` children. | `data/normalized_yaml/bacterial/ravot_modified_medium_for_thermosipho_sp_g60.yaml`; `data/normalized_yaml/bacterial/ravot_modified_medium_for_fervidobacterium_sp_r8.yaml`; `data/normalized_yaml/bacterial/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml`; merge equivalence rules |
| Major | The G60 composition omits its defining 20.0 g/L NaCl. | JCM 727 and TOGO M750 both state that G60 uses Medium 725 with 20.0 g/L NaCl, but the generated `ingredients` list has no `NaCl` row. | `data/normalized_yaml/bacterial/ravot_modified_medium_for_thermosipho_sp_g60.yaml` |
| Major | The copied JCM 725 base formula encodes three stock additions as bulk gram-per-liter ingredients. | The copied rows for `KH2PO4`, `K2HPO4`, and `Na2S x 9 H2O` come from 4.3 ml, 4.3 ml, and 10 ml JCM 725 solution additions; the generated rows say `4.3`, `4.3`, and `10` `G_PER_L`. | `data/normalized_yaml/bacterial/ravot_modified_medium_for_thermoanaerovibrio_sp_r101.yaml`; copy-referenced-compositions logic; `data/normalized_yaml/bacterial/ravot_modified_medium_for_thermosipho_sp_g60.yaml` |
| Major | Two copied base ingredients have wrong or too-broad ChEBI groundings. | Sulfur powder is grounded to `CHEBI:26833` / `sulfur atom`; sodium acetate x 3 H2O is grounded to `CHEBI:32954` / `sodium acetate`. | Direct J725 owner first, then direct J727 after the copy is corrected or replaced |

## Recommended Edits

1. Stop merging direct J725, J726, and J727 as `SOURCE_DUPLICATE` records. Model J727/G60 and J726/R8 as salinity variants of J725/R101, or retire the stale direct wrappers in favor of the repaired TOGO M749/M750 lineage.
2. In `data/normalized_yaml/bacterial/ravot_modified_medium_for_thermosipho_sp_g60.yaml`, add the JCM 727 20.0 g/L NaCl amendment and keep it distinct from the 5.0 g/L R8 amendment.
3. Replace the stale copied direct J725 formula in the direct J727 and J726 owners after the direct J725 stock-solution rows are fixed.
4. Re-ground the copied sulfur powder and sodium acetate trihydrate rows, or inherit the corrected base rows from a repaired J725 owner.
5. Regenerate `data/merge_yaml/merged/ravot_modified_medium_for_thermosipho_sp_g60.yaml` and verify that R101/R8 are no longer listed in `merged_from` or `synonyms`.

## Follow-up Checks

- Re-run the focused open-schema, strict, reference, and term validators on the repaired direct J727 owner and regenerated G60 artifact.
- Re-run the same validators on direct J725 and J726 if those wrappers are kept instead of being deprecated in favor of TOGO.
- Run the merge freshness/equivalence checks and verify that direct J725, J726, and J727 no longer share a merge fingerprint.
- Manually compare regenerated G60 against live JCM `GRMD=727` and repaired TOGO M750 to confirm that the record still says pH 7.0 and now has 20.0 g/L NaCl as a machine-readable amendment.

## Additional Notes

- A gitignore-independent `find` over `data/raw`, `data/normalized_yaml`, and `data/merge_yaml` for paths containing `Thermosipho` found the direct J727 and TOGO M750 owners plus unrelated Thermosipho media. It found no other local file path for JCM 727 or M750 in that bounded path search.
- The exact no-ignore search for `TOGO:M750` also found an older GAM Semisolid review note that mentioned `TOGO:M750` only as a neighboring false hit from that review's own broader `TOGO:M75` search. I did not use that older report as evidence.
