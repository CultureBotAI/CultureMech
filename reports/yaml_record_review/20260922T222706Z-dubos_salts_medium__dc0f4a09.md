# YAML Record Review: Dubos Salts Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/dubos_salts_medium__dc0f4a09.yaml
- Started UTC: 2026-09-22T22:25:33Z
- Finished UTC: 2026-09-22T22:27:06Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` record `CultureMech:008012` at `data/merge_yaml/merged/dubos_salts_medium__dc0f4a09.yaml`.

- Label: `dubos_salts_medium`; original name: `Dubos Salts Medium`.
- Generated status: generated merge output with `merge_fingerprint` `dc0f4a091e001af63784b9feceb9d3355bfbace7cab9f61c76152037e5e29a72`.
- Maintained owner for direct record repair: `data/normalized_yaml/bacterial/TOGO_M146_Dubos_Salts_Medium.yaml`.
- Merge lineage: one source record, `TOGO_M146_Dubos_Salts_Medium`.
- Declared external source: `TOGO:M146`, imported by TOGO from JCM `GRMD=155`.
- Related local duplicate cluster: `data/merge_yaml/merged/DUBOS_SALTS_MEDIUM.yaml` merges `JCM_J155_DUBOS_SALTS_MEDIUM`, `KOMODO_1161_DUBOS_SALTS_MEDIUM`, and the DSMZ `dubos_salts_medium` canonical.

## Validation

Focused validation on `data/merge_yaml/merged/dubos_salts_medium__dc0f4a09.yaml`:

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/dubos_salts_medium__dc0f4a09.yaml` | Passed; `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/dubos_salts_medium__dc0f4a09.yaml --out /private/tmp/dubos_salts_medium__dc0f4a09.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned and 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/dubos_salts_medium__dc0f4a09.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated, 0 checks, all validations passed. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/dubos_salts_medium__dc0f4a09.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils` / `pkg_resources` warning. |
| Embedded curation history | `just validate-history` | Not checked: the available history gate validates standalone `history/` files, not embedded `MediaRecipe.curation_history` in one merged YAML. |

The validators pass even though source units and pH were not imported correctly.

## Identity and Grounding

The target is the TOGO wrapper for JCM Medium 155:

- TOGO `M146` identifies `Dubos Salts Medium`, has `original_media_id: JCM_M155`, and links to `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=155`.
- The live JCM page for `GRMD=155` is `DUBOS SALTS MEDIUM`.
- Local normalized records already contain the same JCM and DSMZ formulation as `JCM_J155_DUBOS_SALTS_MEDIUM.yaml`, `KOMODO_1161_DUBOS_SALTS_MEDIUM.yaml`, and `dubos_salts_medium.yaml`.

Primary chemical groundings for sodium nitrate, dipotassium hydrogen phosphate, magnesium sulfate heptahydrate, potassium chloride, iron(II) sulfate heptahydrate, and agar are suitable for the named ingredients.

## Evidence

Supported against TOGO, JCM, and MediaDive:

- JCM `GRMD=155` and TOGO `M146` both support `0.5 g` NaNO3, `1.0 g` K2HPO4, `0.5 g` MgSO4 x 7 H2O, `0.5 g` KCl, `10.0 mg` FeSO4 x 7 H2O, `15.0 g` agar, and `1.0 L` distilled water.
- TOGO `M146` and the JCM source support pH 7.2 and the instruction to adjust pH, autoclave, dispense into slopes, place sterile filter paper on the solidified agar surface, and inoculate onto the filter paper.
- MediaDive medium `1161` stores the same Dubos Salts Medium formula with 0.01 g/L FeSO4 x 7 H2O, pH 7.2, and the same slope/filter-paper preparation.

Unsupported in the generated TOGO record:

- `FeSO4 x 7 H2O` is `10 G_PER_L`, but TOGO and JCM both state `10 mg`; MediaDive converts the same amount to `0.01 G_PER_L`.
- `Distilled water` is `1 G_PER_L`, but TOGO and JCM state `1 L`.
- pH 7.2 and the preparation instructions are missing from the generated TOGO-only record.
- The generated record is typed as `COMPLEX` and `UNDEFINED`; the imported formulation contains only defined salts, water, and agar.

## Completeness

The record is a consequentially incomplete and numerically inaccurate TOGO import of an otherwise represented JCM recipe.

- The ferric sulfate and water amounts need unit repair.
- The pH and preparation text from TOGO/JCM need to be retained.
- After repair, this TOGO source should be eligible for the same source-duplicate grouping as `DUBOS_SALTS_MEDIUM.yaml`; leaving it as a singleton generated output keeps the TOGO view out of sync with the curated JCM/DSMZ duplicate cluster.

An ignored-inclusive `find data -iname '*dubos_salts_medium*' -o -iname '*dubos*salts*'` search found the target generated YAML, `DUBOS_SALTS_MEDIUM.yaml`, and the four active normalized Dubos Salt source records under `data/normalized_yaml/bacterial/`. An ignored-inclusive `rg --no-ignore --hidden` search for the exact TOGO `M146`, JCM `GRMD=155`, `CultureMech:008012`, fingerprint, and source filename across the bacterial normalized records, merged records, and CultureMech registries found the same active TOGO source plus the existing JCM duplicate; it did not find a second active TOGO `M146` repair to reconcile.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The TOGO import inflated ferrous sulfate by 1000x. | TOGO `M146` and JCM `155` state `10 mg` FeSO4 x 7 H2O. The generated YAML stores `10 G_PER_L`; MediaDive `1161` confirms the same recipe's converted value is `0.01 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M146_Dubos_Salts_Medium.yaml`; the TOGO unit mapper if the milligram conversion is a reusable importer bug. |
| major | The 1 L water row was converted to `1 G_PER_L`. | TOGO and JCM both state `1 L` distilled water, while the generated record stores the water amount as a mass concentration. | `data/normalized_yaml/bacterial/TOGO_M146_Dubos_Salts_Medium.yaml`; the TOGO unit mapper if liter rows are systemically coerced to `G_PER_L`. |
| major | pH 7.2 and all preparation instructions were dropped. | TOGO `M146`, JCM `155`, and MediaDive `1161` all carry pH 7.2 and the slope/filter-paper autoclave instructions. The generated TOGO record has neither `ph_value` nor `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M146_Dubos_Salts_Medium.yaml`. |
| major | The bad TOGO source does not merge with the existing duplicate cluster. | The existing `DUBOS_SALTS_MEDIUM.yaml` generated record correctly merges JCM `155`, KOMODO `1161`, and DSMZ `1161` sources with `0.01 G_PER_L` FeSO4 x 7 H2O and pH 7.2. The TOGO source remains a singleton because its Fe and water rows differ. | `data/normalized_yaml/bacterial/TOGO_M146_Dubos_Salts_Medium.yaml`; rerun merge generation after repair. |

No blocker findings were found: the record still denotes Dubos Salts Medium from TOGO `M146`. No minor-only findings were separated from the import defects above.

## Recommended Edits

1. In `data/normalized_yaml/bacterial/TOGO_M146_Dubos_Salts_Medium.yaml`, correct `FeSO4 x 7 H2O` from `10 G_PER_L` to `0.01 G_PER_L`.
2. Repair or omit the `1 L` distilled-water row instead of representing it as `1 G_PER_L`.
3. Add `ph_value: 7.2` and preserve the JCM/TOGO autoclave, slope, filter-paper, and inoculation instructions as structured preparation.
4. Change `medium_type` and `composition_type` to `DEFINED` if the source type fields are curated manually rather than inferred by an importer.
5. Re-run merge generation so the repaired TOGO `M146` source merges with the existing `DUBOS_SALTS_MEDIUM.yaml` source-duplicate cluster.

## Follow-up Checks

- Re-run the focused LinkML, strict, reference, and term validators on the repaired normalized record and regenerated merged record.
- Re-run merge generation and verify there is no separate `dubos_salts_medium__dc0f4a09.yaml` singleton for TOGO `M146`.
- Compare the repaired source against both `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M146` and `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=155`, with special attention to the 10 mg FeSO4 x 7 H2O row and pH 7.2.
- Compare the regenerated Dubos merged record against MediaDive medium `1161` and confirm all four local sources carry the same final formulation.

## Additional Notes

The TOGO API and live JCM HTML agree on the source formula, so this is an import-unit defect rather than a source conflict. The existing three-source `DUBOS_SALTS_MEDIUM.yaml` merge demonstrates the intended local representation after the TOGO row is repaired.
