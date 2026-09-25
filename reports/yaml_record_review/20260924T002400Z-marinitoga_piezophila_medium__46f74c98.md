# YAML Record Review: marinitoga_piezophila_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/marinitoga_piezophila_medium__46f74c98.yaml`
- Started UTC: 2026-09-24T00:23:13Z
- Finished UTC: 2026-09-24T00:24:00Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002122` |
| Name | `marinitoga_piezophila_medium` |
| Original name | `MARINITOGA PIEZOPHILA MEDIUM` |
| Category | `bacterial` |
| Media term | `mediadive.medium:945` |
| Generated status | Generated merge output from 2026-08-06 |
| Merge fingerprint | `46f74c9836a530dd58540e24397c016cd533f986994547e1120e40fe9325eed1` |
| Maintained owners | `data/normalized_yaml/bacterial/marinitoga_piezophila_medium.yaml`, `data/normalized_yaml/bacterial/for_dsm_17373.yaml` |

The reviewed record is generated from a MediaDive DSMZ 945 import and a KOMODO 945.2 strain/pH variant that were merged as source duplicates. Fixes belong in the normalized variant graph and the direct MediaDive owner, followed by regeneration of `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marinitoga_piezophila_medium__46f74c98.yaml` | Passed with `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marinitoga_piezophila_medium__46f74c98.yaml --out /private/tmp/marinitoga_piezophila_medium__46f74c98.strict.tsv --workers 1 --quiet` | Passed. The strict TSV had only its header line, so there were 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marinitoga_piezophila_medium__46f74c98.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file scanned, 0 references checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marinitoga_piezophila_medium__46f74c98.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the standard `eutils` / `pkg_resources` warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/*.yaml`, not embedded `MediaRecipe.curation_history` blocks. |

The regular `just` validators were not used because this checkout currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools` before reaching record validation.

## Identity and Grounding

- The representative DSMZ 945 identity is coherent: `CultureMech:002122`, `mediadive.medium:945`, `MARINITOGA PIEZOPHILA MEDIUM`, and pH 6.0 agree with the inspected MediaDive page and DSMZ Medium 945 PDF.
- The `SOURCE_DUPLICATE` merge with `data/normalized_yaml/bacterial/for_dsm_17373.yaml` is not source-supported. DSMZ Medium 945 treats DSM 17373 as a pH 5.5 variant with an 80% H2 / 20% CO2 post-inoculation gas phase, not as the same pH 6.0 base recipe.
- `for_dsm_17373.yaml` was partly repaired on 2026-09-13: it now points to `KOMODO_945_MARINITOGA_PIEZOPHILA_medium.yaml` as a `PH_VARIANT`. Its obsolete `variant_children` edge back to `marinitoga_piezophila_medium.yaml` still marks the pH 6.0 MediaDive record as a `SOURCE_DUPLICATE`, and that stale edge feeds the reviewed generated merge.
- An exact gitignore-independent scan found `CultureMech:002122` and exact `mediadive.medium:945` entries only in the reviewed generated record, `data/normalized_yaml/bacterial/marinitoga_piezophila_medium.yaml`, and the MediaDive index files. The exact `komodo.medium:945.2` scan resolved the pH 5.5 child to `data/normalized_yaml/bacterial/for_dsm_17373.yaml`.

## Evidence

- The generated representative carries the pH 6.0 DSMZ 945 ingredient list and preparation prose from the direct MediaDive import. These values match the DSMZ PDF for the base recipe: salts, Na-acetate, MES, yeast extract, Trypticase peptone, phosphate salts, sodium resazurin, sulfur, L-cysteine HCl x H2O, and Na2S x 9H2O.
- The source preparation is retained in prose and preserves the nonstandard sterilization requirement: medium plus sulfur is heated in boiling water for 2 - 3 hours on each of 3 successive days, rather than autoclaved.
- The source lists distilled water as 1000 ml, but neither the direct normalized owner nor the generated record represents water or final volume.
- The DSM 17373 note in the DSMZ PDF is over-scoped by the generated `SOURCE_DUPLICATE` edge. It changes pH and post-inoculation gas pressure; the generated pH 6.0 record collapses that variant into a synonym while dropping the pH 5.5 and 80% H2 / 20% CO2 gas modifications.
- The direct MediaDive owner also omits NaOH as an explicit variable pH-adjustment component even though the source says to adjust pH with NaOH. The preparation prose preserves the NaOH instruction, so this is secondary to the missing final volume and wrong duplicate merge.

## Completeness

- A gitignore-independent exact field scan over the generated record and both normalized `merged_from` owners found `ph_value`, `preparation_steps`, `parent_media`, and `variant_relationship`. It found no `sources`, `source_data`, `target_organisms`, `growth_metrics`, `references`, or `sterilization` in those exact files.
- Missing `target_organisms` and `growth_metrics` are acceptable for the base DSMZ recipe. DSMZ 945 names strain-specific preparation variants, but the reviewed base record does not claim a measured growth outcome.
- Missing structured `sterilization` is a consequential gap for this source. The preparation prose mentions the three-day boiling regimen, but the record has no structured sterilization object that can distinguish fractional boiling from ordinary autoclaving.
- The generated record's `synonyms` block is incomplete for its own duplicate claim because it only carries the KOMODO source row and loses the pH 5.5 / H2 / CO2 modifications that make DSM 17373 distinct.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated record merges a pH/gas variant into the DSMZ 945 base as a `SOURCE_DUPLICATE`. | The inspected DSMZ 945 PDF says DSM 17373 uses the complete medium at pH 5.5 and is pressurized after inoculation with 80% H2 / 20% CO2. `for_dsm_17373.yaml` now also records this as a `PH_VARIANT` of KOMODO 945, but still has a stale `variant_children` `SOURCE_DUPLICATE` edge to `CultureMech:002122`; the generated merge follows that stale duplicate edge. | Remove the obsolete duplicate edge between `data/normalized_yaml/bacterial/for_dsm_17373.yaml` and `data/normalized_yaml/bacterial/marinitoga_piezophila_medium.yaml`, then regenerate merged recipes. |
| Major | The MediaDive owner and generated record omit the explicit final-volume water component. | MediaDive/DSMZ 945 lists 1000 ml distilled water. The reviewed generated YAML and `data/normalized_yaml/bacterial/marinitoga_piezophila_medium.yaml` stop at Na2S x 9H2O and do not represent water or final volume. | Add the DSMZ-supported water/final-volume ingredient to `data/normalized_yaml/bacterial/marinitoga_piezophila_medium.yaml`, then regenerate. |

No blocker findings: the representative record still denotes DSMZ 945 and the YAML is valid.

No minor findings found.

## Recommended Edits

1. Delete the stale `SOURCE_DUPLICATE` link from `data/normalized_yaml/bacterial/for_dsm_17373.yaml` back to `data/normalized_yaml/bacterial/marinitoga_piezophila_medium.yaml`. DSM 17373 should remain a pH 5.5 variant of KOMODO 945, not a duplicate of the pH 6.0 MediaDive base.
2. Ensure the DSM 17373 variant records its 80% H2 / 20% CO2 post-inoculation gas modification from DSMZ 945.
3. Add 1000 ml distilled water, or another explicit final-volume representation, to `data/normalized_yaml/bacterial/marinitoga_piezophila_medium.yaml`.
4. Add NaOH as a variable pH-adjustment ingredient and add a structured sterilization representation for the three successive boiling-water treatments if the schema can represent it without losing source fidelity.
5. Regenerate `data/merge_yaml/merged/` and confirm the DSMZ 945 base is no longer merged with the DSM 17373 pH variant.

## Follow-up Checks

- Run `just validate-media-variant-links` after the stale source-duplicate edge is removed to confirm the normalized variant graph is internally consistent.
- Run `just verify-merges` after regeneration to prove `marinitoga_piezophila_medium__46f74c98.yaml` no longer combines the pH 6.0 base with the pH 5.5 DSM 17373 variant.
- Re-run open-schema, strict, term, and reference validation on the regenerated generated record.
- Compare the regenerated base and DSM 17373 child against the DSMZ 945 PDF to verify pH 6.0, pH 5.5, sulfur handling, boiling-water sterilization, and post-inoculation gas conditions.

## Additional Notes

- Fetching the DSMZ 945 PDF initially failed in the sandbox with a DNS resolution error and then succeeded when retried with the approved `curl -L` escalation.
- The separate KOMODO 945 base already lists `for_dsm_17373.yaml` as a `PH_VARIANT` child and `for_dsm_14283.yaml` as a `STRAIN_SPECIFIC_VARIANT` child. That topology is a better fit for the DSMZ 945 notes than the stale direct source-duplicate edge into the MediaDive 945 copy.
