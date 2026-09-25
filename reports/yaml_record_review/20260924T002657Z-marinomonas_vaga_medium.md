# YAML Record Review: marinomonas_vaga_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/marinomonas_vaga_medium.yaml`
- Started UTC: 2026-09-24T00:25:55Z
- Finished UTC: 2026-09-24T00:26:57Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:006109` |
| Name | `marinomonas_vaga_medium` |
| Original name | `MARINOMONAS VAGA medium` |
| Category | `bacterial` |
| Media term | `komodo.medium:617` |
| Generated status | Generated merge output from 2026-08-06 |
| Merge fingerprint | `81f6c5d1e83b8e380fb9c8c5a21d6e990ef9a1328cd05475fac79c94b00cddcc` |
| Maintained representative owner | `data/normalized_yaml/bacterial/KOMODO_617_MARINOMONAS_VAGA_medium.yaml` |
| Exact DSMZ source owner | `data/normalized_yaml/bacterial/marinomonas_vaga_medium.yaml` |

The reviewed record is a generated ten-source merge that now disagrees with the repaired normalized topology. Its representative should collapse only the KOMODO 617 and MediaDive DSMZ 617 source copies; the Blood Agar Base, TOGO Nutrient Agar, soil-extract, and NBRC NA records are distinct recipes or concentration variants.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marinomonas_vaga_medium.yaml` | Passed with `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marinomonas_vaga_medium.yaml --out /private/tmp/marinomonas_vaga_medium.strict.tsv --workers 1 --quiet` | Passed. The strict TSV had only its header line, so there were 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marinomonas_vaga_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file scanned, 0 references checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marinomonas_vaga_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the standard `eutils` / `pkg_resources` warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/*.yaml`, not embedded `MediaRecipe.curation_history` blocks. |

The regular `just` validators were not used because this checkout currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools` before reaching record validation.

## Identity and Grounding

- The representative identity for KOMODO 617 / DSMZ 617 is coherent: KOMODO 617, MediaDive 617, and the DSMZ Medium 617 PDF describe `MARINOMONAS VAGA MEDIUM` with 10 g/L beef extract, 10 g/L peptone, 30 g/L NaCl, 15 g/L agar, and 1000 ml tap water.
- The generated source set is not coherent. It merges DSMZ 617a Blood Agar Base with 5 g/L NaCl and pH 7.3, TOGO M15 with 5 g/L NaCl and pH 7.0-7.2, TOGO M16 with 1/10 nutrient concentrations, TOGO M17 with 1/100 nutrient concentrations, TOGO M405 with 50% soil extract and 5% NaCl, and NBRC NA medium with 3 g/L beef extract and pH 7.4-7.6 into the 30 g/L NaCl DSMZ 617 base.
- The maintained normalized graph has already moved several of those children away from DSMZ 617. `blood_agar_base_oxoid_cm55.yaml` now owns the KOMODO 617a duplicate and DSM 7232 strain-specific child, while `TOGO_M15_Nutrient_Agar_NO._2.yaml` now owns the M16 concentration variant.
- An exact gitignore-independent scan found `CultureMech:006109`, `komodo.medium:617`, and exact `mediadive.medium:617` only in the KOMODO 617 / MediaDive 617 owners, this generated merge, and their source indexes. Exact scans of the reviewed target plus each TOGO normalized owner confirmed that the M15, M16, M17, M405, and M2163 identifiers in this generated file only come from the obsolete `synonyms` block.

## Evidence

- DSMZ 617 / MediaDive 617 support the representative five-ingredient formula with 30 g/L NaCl.
- DSMZ 617a and MediaDive 617a support Blood Agar Base as a related but separate five-ingredient formula with 5 g/L NaCl and final pH 7.3. It should not be a source duplicate of DSMZ 617.
- DSMZ 617a also says the DSM 7232 variant uses 25 g agar instead of 15 g. `data/normalized_yaml/bacterial/for_dsm_7232.yaml` still has 15 g/L agar, so that child is still incomplete even after its September topology repair.
- TOGO M15, M16, M17, M405, and M2163 support multiple nutrient agar or NA formulations with different concentrations, pH comments, NBRC/JCM source identities, or a soil-extract solution. None of those inspected TOGO records support the generated claim that they are aliases of Marinomonas Vaga Medium / DSMZ 617.
- The representative and MediaDive 617 owner carry tap water as `1000 G_PER_L`. DSMZ 617 lists 1000 ml tap water, so that unit is a final volume rather than a mass concentration.

## Completeness

- A gitignore-independent exact field scan over the generated file and all ten `merged_from` normalized owners found variant topology fields, `solutions` only in the TOGO M405 owner, and `ph_value`, `preparation_steps`, and `data_quality_flags` only on the repaired Blood Agar Base branch. It found no `sources`, `source_data`, `target_organisms`, `growth_metrics`, `references`, or `sterilization` in the exact file set.
- Empty `target_organisms` and `growth_metrics` are acceptable for this generated record. The inspected media pages are recipes, not source-backed growth assays.
- The generated `synonyms` list is not a harmless alias list because it erases concentration differences and distinct source accessions. In particular, the 1/10, 1/100, 50 g/L NaCl, pH 7.3 Blood Agar Base, and NBRC NA variants would all disappear behind a DSMZ 617 representative if this generated record were published as-is.
- Missing `references` on the DSMZ 617 owner are secondary to the merge error but should be addressed during future curation.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated merge over-collapses ten distinct media into the DSMZ/KOMODO 617 representative. | Inspected DSMZ, TOGO, and normalized records show different source IDs, NaCl amounts of 0.5, 5, 30, and 50 g/L, 1/10 and 1/100 nutrient concentrations, a 50% soil-extract formulation, and a distinct NBRC NA recipe. | Regenerate from the repaired normalized topology; if `KOMODO_617a_BLOOD_AGAR_BASE_OXOID_CM55`, `for_dsm_7232`, `TOGO_M15`, `TOGO_M16`, `TOGO_M17`, `TOGO_M405`, or `na_medium` are still merged with KOMODO 617, fix the merge rule to account for concentrations and explicit variant edges. |
| Major | The DSMZ 617 representative and its MediaDive source duplicate model tap water with a mass-concentration unit. | MediaDive and DSMZ 617 list 1000 ml tap water, but `KOMODO_617_MARINOMONAS_VAGA_medium.yaml`, `marinomonas_vaga_medium.yaml`, and the generated target record `1000 G_PER_L` tap water. | Correct the tap-water unit in the exact DSMZ 617 owners, then regenerate. |
| Major | The DSM 7232 Blood Agar Base child still loses its source-specific agar change. | DSMZ 617a changes the DSM 7232 variant from 15 g agar to 25 g agar; `data/normalized_yaml/bacterial/for_dsm_7232.yaml` still has the 15 g/L parent value. | Curate `data/normalized_yaml/bacterial/for_dsm_7232.yaml` under the Blood Agar Base branch; keep it separate from the DSMZ 617 Marinomonas Vaga merge. |

No blocker findings: the generated representative formula still matches DSMZ 617 apart from the tap-water unit, and the YAML is valid.

No minor findings found.

## Recommended Edits

1. Regenerate merged recipes from the current normalized graph and confirm only `KOMODO_617_MARINOMONAS_VAGA_medium.yaml` and `marinomonas_vaga_medium.yaml` collapse into the DSMZ 617 representative.
2. If regeneration still produces this ten-source merge, change the merge algorithm so ingredient identity without matching concentrations never collapses concentration variants or source-specific strain variants.
3. Represent tap water as 1000 ml/L, 1 L, or an equivalent final-volume value in `data/normalized_yaml/bacterial/KOMODO_617_MARINOMONAS_VAGA_medium.yaml` and `data/normalized_yaml/bacterial/marinomonas_vaga_medium.yaml`.
4. Correct `data/normalized_yaml/bacterial/for_dsm_7232.yaml` to 25 g/L agar and retain it as a `STRAIN_SPECIFIC_VARIANT` under `data/normalized_yaml/bacterial/blood_agar_base_oxoid_cm55.yaml`.
5. Review the TOGO M15, M16, M17, M405, and M2163 records separately for source-unit repairs before linking them to any parent/child group.

## Follow-up Checks

- Run `just validate-media-variant-links` after variant-edge repairs to ensure the normalized Blood Agar Base and Nutrient Agar subgraphs remain bidirectional.
- Run `just verify-merges` and inspect the regenerated `data/merge_yaml/merged/marinomonas_vaga_medium.yaml` source list.
- Re-run open-schema, strict, term, and reference validation on the regenerated DSMZ 617 generated record.
- Re-fetch MediaDive 617, MediaDive 617a, TOGO M15/M16/M17/M405/M2163, and the NBRC NA source before accepting any future duplicate or concentration-variant link.

## Additional Notes

- Fetching the DSMZ 617 and 617a PDFs initially failed in the sandbox with DNS resolution errors and then succeeded with the approved `curl -L` escalation.
- An accidental broad exact search for `marinomonas_vaga_medium` included generated pages and report artifacts; this review did not rely on that output. All nonexistence and exact-ID claims above use later gitignore-independent searches scoped to exact generated or normalized files and source indexes.
