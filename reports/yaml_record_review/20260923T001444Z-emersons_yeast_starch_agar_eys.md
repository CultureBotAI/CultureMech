# YAML Record Review: EMERSON'S YEAST STARCH AGAR (EYS)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/emersons_yeast_starch_agar_eys.yaml
- Started UTC: 2026-09-23T00:11:00Z
- Finished UTC: 2026-09-23T00:14:44Z
- Verdict: pass with minor issues

## Target

- Reviewed record: `data/merge_yaml/merged/emersons_yeast_starch_agar_eys.yaml`
- Class: `MediaRecipe`
- ID: `CultureMech:006000`
- Name: `emersons_yeast_starch_agar_eys`
- Original label: `EMERSON'S YEAST STARCH AGAR (EYS)`
- Categories: `bacterial`, `fungal`
- Medium term in generated record: `komodo.medium:551`
- Generated status: generated merge record with fingerprint `8baea4f9a1237d2780214bb144be06741aa25379a92f23a43b4df1ec88724d9b`
- Maintained source records:
  - `data/normalized_yaml/bacterial/emersons_yeast_starch_agar_eys.yaml`
  - `data/normalized_yaml/fungal/emersons_yeast_starch_agar_eys.yaml`

The merge correctly detected duplicate bacterial KOMODO 551 and fungal DSMZ 551 records with the same ingredient signature.

## Validation

Focused validation was clean.

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/emersons_yeast_starch_agar_eys.yaml` | Passed; `No issues found`. |
| Strict schema wrapper | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/emersons_yeast_starch_agar_eys.yaml --out /private/tmp/emersons_yeast_starch_agar_eys.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/emersons_yeast_starch_agar_eys.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 reference checks, all validations passed. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/emersons_yeast_starch_agar_eys.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; the run emitted the expected `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` in merged YAML. |

## Identity and Grounding

The generated record denotes DSMZ Medium 551, `EMERSON'S YEAST STARCH AGAR (EYS)`. DSMZ Medium 551, MediaDive 551, KOMODO 551, and both normalized EYS records agree on the same formula, so the cross-category merge did not conflate this record with the distinct JCM 73 / TOGO M64 `emersons_yeast_starch_agar` records that use K2HPO4, magnesium sulfate heptahydrate, and a sodium carbonate pH adjustment.

The chemical groundings are correct for the displayed labels: starch, disodium hydrogen phosphate, magnesium sulfate, and agar all match the anhydrous DSMZ 551 rows.

## Evidence

DSMZ 551 lists a 1 L agar with 4.0 g yeast extract, 15.0 g soluble starch, 1.0 g Na2HPO4, 0.5 g MgSO4, 15.0 g agar, and pH 6.8. MediaDive 551 returns the same five g/L rows and the `pH 6.8` preparation note.

The reviewed record preserves all five ingredient identities and amounts. Its `ph_value: 6.8` preserves the source pH numerically.

Minor evidence loss remains:

- `Starch, soluble` is simplified to `Starch`.
- The fungal DSMZ owner has a `preparation_steps` entry for `pH 6.8`, but the generated merge loses that step.
- The generated `media_term` and `notes` favor the KOMODO copy and drop the direct `mediadive.medium:551` term and DSMZ PDF URL.
- The KOMODO note says `Aerobic: No`, but the inspected DSMZ 551 recipe does not specify an aerobic or anaerobic incubation atmosphere.

## Completeness

The record is complete enough to reconstruct DSMZ 551. Distilled water is correctly left out of the final nutrient ingredient table because all masses are already per liter.

Exact local discovery used `find`, which includes ignored files, and found the bacterial and fungal EYS owners plus distinct bacterial and fungal non-EYS Emerson records. No additional generated EYS file was found while enumerating the sorted corpus.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| minor | The source-specific `soluble` starch form is not preserved in the preferred term. | DSMZ and MediaDive list `Starch, soluble`; the generated record lists `Starch`. | `data/normalized_yaml/fungal/emersons_yeast_starch_agar_eys.yaml` |
| minor | Merge output drops the direct DSMZ term, DSMZ URL, and pH preparation note. | The fungal DSMZ owner has `mediadive.medium:551`, a DSMZ PDF URL, and a `pH 6.8` preparation step; the merge output keeps only the KOMODO term and numerical `ph_value`. | merge generation |
| minor | The KOMODO `Aerobic: No` note is not supported by the inspected DSMZ 551 recipe. | The DSMZ 551 PDF contains only ingredients, water, and pH 6.8, with no atmosphere condition. | `data/normalized_yaml/bacterial/emersons_yeast_starch_agar_eys.yaml` |

## Recommended Edits

1. Preserve `Starch, soluble` in the DSMZ owner, either as the `preferred_term` or in an ingredient-level source note.
2. Update merge generation so direct source terms and source URLs are not hidden when a KOMODO import merges with a direct DSMZ import.
3. Remove or qualify `Aerobic: No` on the KOMODO normalized owner unless a KOMODO-specific source can support it.
4. Regenerate merged YAML and downstream pages.

## Follow-up Checks

1. Rerun LinkML schema, strict schema, reference, and term validation on the regenerated `data/merge_yaml/merged/emersons_yeast_starch_agar_eys.yaml`.
2. Reopen DSMZ Medium 551 and MediaDive 551 and verify the five ingredient amounts, pH 6.8, and the soluble starch form.
3. Verify the generated page still shows both bacterial and fungal category membership without losing the direct DSMZ accession.

## Additional Notes

None found.
