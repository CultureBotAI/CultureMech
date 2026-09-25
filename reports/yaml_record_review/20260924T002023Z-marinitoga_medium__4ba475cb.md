# YAML Record Review: marinitoga_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/marinitoga_medium__4ba475cb.yaml`
- Started UTC: 2026-09-24T00:19:49Z
- Finished UTC: 2026-09-24T00:20:23Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:007568` |
| Name | `marinitoga_medium` |
| Original name | `Marinitoga Medium` |
| Category | `bacterial` |
| Media term | `TOGO:M1052` |
| Generated status | Generated merge output from 2026-08-06 |
| Merge fingerprint | `4ba475cb8403a3e722a71c2502906f6403d36f0e65d0f9b677f41f009b3fcebe` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M1052_Marinitoga_Medium.yaml` |

The reviewed record is a generated single-source merge from the TOGO M1052 normalized YAML. Future corrections belong in `data/normalized_yaml/bacterial/TOGO_M1052_Marinitoga_Medium.yaml`, followed by regeneration of `data/merge_yaml/merged/marinitoga_medium__4ba475cb.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marinitoga_medium__4ba475cb.yaml` | Passed with `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marinitoga_medium__4ba475cb.yaml --out /private/tmp/marinitoga_medium__4ba475cb.strict.tsv --workers 1 --quiet` | Passed. The strict TSV had only its header line, so there were 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marinitoga_medium__4ba475cb.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file scanned, 0 references checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marinitoga_medium__4ba475cb.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the standard `eutils` / `pkg_resources` warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/*.yaml`, not embedded `MediaRecipe.curation_history` blocks. |

The regular `just` validation recipes were not used because this checkout currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools` before reaching record validation.

## Identity and Grounding

- The record identity is coherent: `CultureMech:007568`, `TOGO:M1052`, the `Marinitoga Medium` label, and the original `JCM_M997` source metadata all describe the JCM Marinitoga Medium imported through TOGO.
- The inspected TOGO M1052 API payload supports the listed major ingredients and confirms this is the PIPES / pH 7.0 Marinitoga Medium, not the MES / pH 6.0 Marinitoga Hydrogenitolerans Medium reviewed separately.
- The old JCM `GRMD=997` URL now returns `Nothing found`, so this review could not inspect the JCM page directly. The MediaDive/DSMZ 904 source was inspected as a cross-check and agrees with the TOGO formulation on PIPES, pH 7.0, the reducer amounts, and the anaerobic preparation outline.
- An exact gitignore-independent scan found `TOGO:M1052`, `JCM_M997`, and `CultureMech:007568` only in the reviewed generated file, `data/normalized_yaml/bacterial/TOGO_M1052_Marinitoga_Medium.yaml`, and the TOGO source index entries.

## Evidence

- TOGO M1052 supports the identity, JCM M997 provenance, water, resazurin, Na2S x 9H2O, sea salts, PIPES, glucose, yeast extract, tryptone, L-cysteine HCl H2O, and N2 claims.
- The generated record misrepresents two TOGO units: TOGO lists distilled water as 1 L and resazurin as 0.5 mg, but the generated target records both as `G_PER_L`.
- The generated record carries the correct 0.5 g/L Na2S x 9H2O, 30 g/L sea salts, 6 g/L PIPES, 2.5 g/L glucose, 1 g/L yeast extract, 1 g/L tryptone, and 0.5 g/L L-cysteine HCl H2O quantities.
- The generated record omits the TOGO preparation comment. That comment sets pH to 7.0, prepares the medium anaerobically under N2, dispenses into anaerobic vials, autoclaves, and adds sterile anoxic glucose, cysteine, and sulfide stocks under N2.
- `Microbial cultivation` is a reasonable generic application for a named JCM medium. The source does not assert a growth metric or target-organism result, and the generated target does not add one.

## Completeness

- A gitignore-independent exact field scan over the generated record, its TOGO owner, and the separate MediaDive DSMZ 904 owner found `ph_value` and `preparation_steps` only in `data/normalized_yaml/bacterial/marinitoga_medium.yaml`. It found no `sources`, `source_data`, `target_organisms`, `growth_metrics`, `parent_media`, `variant_children`, `variant_relationship`, `references`, or `sterilization` in the reviewed generated record or its exact TOGO owner.
- Missing `target_organisms` and `growth_metrics` are acceptable here because the inspected TOGO and DSMZ formulation sources establish the recipe rather than a specific organism growth claim.
- Missing `references`, `ph_value`, `preparation_steps`, and `sterilization` are consequential gaps. TOGO M1052 carries enough source information to represent pH 7.0 and the anaerobic autoclave workflow, and the maintained TOGO owner has not yet been upgraded.
- The separate `data/normalized_yaml/bacterial/marinitoga_medium.yaml` MediaDive DSMZ 904 record is a plausible duplicate source for this same PIPES / pH 7.0 recipe, but duplicate linkage should wait until the TOGO owner has been corrected and a source comparison is performed.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The normalized TOGO owner and generated merge preserve the TOGO volume and mass importer bug for water and resazurin. | TOGO M1052 lists 1 L distilled water and 0.5 mg resazurin; the reviewed YAML records `1 G_PER_L` water and `0.5 G_PER_L` resazurin. | Re-curate `data/normalized_yaml/bacterial/TOGO_M1052_Marinitoga_Medium.yaml`, then regenerate `data/merge_yaml/merged/marinitoga_medium__4ba475cb.yaml`. |
| Major | The TOGO preparation comment is absent from the maintained and generated records. | TOGO M1052 supplies a preparation comment with pH 7.0, 100% N2 atmosphere, anaerobic vials, autoclaving, and post-autoclave stock additions; neither the generated record nor its TOGO owner has `ph_value`, `preparation_steps`, or `sterilization`. | Add source-backed pH, preparation, and sterilization metadata to `data/normalized_yaml/bacterial/TOGO_M1052_Marinitoga_Medium.yaml`, then regenerate the merged YAML. |

No blocker findings: the YAML is valid and the record denotes the intended TOGO/JCM source medium.

No minor findings found.

## Recommended Edits

1. Change distilled water to 1 L and resazurin to 0.5 mg/L or another dimensionally faithful representation in `data/normalized_yaml/bacterial/TOGO_M1052_Marinitoga_Medium.yaml`.
2. Add `ph_value: 7.0`, a source-faithful anaerobic preparation sequence, and structured autoclave sterilization to the same TOGO owner.
3. Add `references` for TOGO M1052 and the original JCM URL. Record that the old JCM URL was checked and currently returns no formula if no better JCM endpoint can be recovered.
4. Compare the corrected TOGO M1052 record against `data/normalized_yaml/bacterial/marinitoga_medium.yaml` and decide whether the TOGO/JCM and MediaDive/DSMZ 904 copies should be linked as source duplicates.
5. Regenerate `data/merge_yaml/merged/marinitoga_medium__4ba475cb.yaml` from the corrected normalized source.

## Follow-up Checks

- Re-run TOGO M1052 retrieval and confirm the corrected YAML still matches every listed component, unit, and the preparation comment.
- Re-run open-schema, strict, term, and reference validation on the corrected normalized owner and the regenerated merged record.
- Run `just verify-merges` to prove the single-source generated record is in sync with `data/normalized_yaml/bacterial/TOGO_M1052_Marinitoga_Medium.yaml`.
- Compare the corrected TOGO M1052 copy with MediaDive/DSMZ 904 before adding any `SOURCE_DUPLICATE` relationship.

## Additional Notes

- The TOGO import and generated merge use the source form `L--Cysteine HCl H2O`; this review treated that spelling as a source-label artifact and did not require changing the ingredient label to decide the larger unit and preparation gaps.
- This record has no embedded source-level growth evidence; the absence of `target_organisms` and `growth_metrics` is not a defect by itself.
