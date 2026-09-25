# YAML Record Review: marinitoga_hydrogenitolerans_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__8a96fdfa.yaml`
- Started UTC: 2026-09-24T00:17:37Z
- Finished UTC: 2026-09-24T00:19:01Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002072` |
| Name | `marinitoga_hydrogenitolerans_medium` |
| Original name | `MARINITOGA HYDROGENITOLERANS MEDIUM` |
| Category | `bacterial` |
| Media term | `mediadive.medium:904a` |
| Generated status | Generated merge output from 2026-08-06 |
| Merge fingerprint | `8a96fdfa8ab2e7bf0da1652e27a66495250f92e99ea0da6de82a23e2139d1f50` |
| Maintained owners | `data/normalized_yaml/bacterial/marinitoga_hydrogenitolerans_medium.yaml`, `data/normalized_yaml/bacterial/KOMODO_904_MARINITOGA_medium.yaml`, `data/normalized_yaml/bacterial/for_dsm_15518_dsm_15807_and_dsm_16785.yaml` |

The reviewed file is a generated merge of one MediaDive DSMZ 904a import and two KOMODO imports. Scientific corrections belong in those normalized inputs or in source-duplicate merge decisions, followed by regeneration of `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__8a96fdfa.yaml` | Passed with `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__8a96fdfa.yaml --out /private/tmp/marinitoga_hydrogenitolerans_medium__8a96fdfa.strict.tsv --workers 1 --quiet` | Passed. The strict TSV had only its header line, so there were 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__8a96fdfa.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file scanned, 0 references checked. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__8a96fdfa.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the standard `eutils` / `pkg_resources` warning. |
| Embedded history | Not run | Not checked: `just validate-history` validates standalone `history/*.yaml`, not embedded `MediaRecipe.curation_history` blocks. |

The regular `just` validators were not used because this checkout currently tries to build `llvmlite==0.46.0` under Python 3.13 and fails inside `setuptools` before reaching record validation.

## Identity and Grounding

- The representative source identity is coherent for DSMZ/MediaDive 904a: `CultureMech:002072`, `mediadive.medium:904a`, `MARINITOGA HYDROGENITOLERANS MEDIUM`, pH 6.0, and MES at 4 g/L agree with the inspected MediaDive REST payload and DSMZ Medium 904a PDF.
- The merge is not source-clean. `data/normalized_yaml/bacterial/KOMODO_904_MARINITOGA_medium.yaml` is linked as the `SOURCE_DUPLICATE` parent of the reviewed record, but its own note says KOMODO 904 maps to DSMZ Medium 904 / `mediadive.medium:904`. The inspected DSMZ 904 PDF and MediaDive 904 REST payload define MARINITOGA MEDIUM at pH 7.0 with 6 g/L PIPES, so DSMZ 904 is not a duplicate of DSMZ 904a.
- `data/normalized_yaml/bacterial/for_dsm_15518_dsm_15807_and_dsm_16785.yaml` has the DSMZ 904a ingredient signature but its provenance also names KOMODO 904.1 and DSMZ Medium 904. That makes its exact source identity unresolved until the KOMODO row is inspected or the import is reconciled against DSMZ 904 / 904a.
- An exact gitignore-independent scan for `mediadive.medium:904a` found the reviewed generated file and `data/normalized_yaml/bacterial/marinitoga_hydrogenitolerans_medium.yaml` as the only recipe records keyed to DSMZ 904a. A similarly bounded exact scan for `mediadive.medium:904` found `data/normalized_yaml/bacterial/marinitoga_medium.yaml` and `data/merge_yaml/merged/marinitoga_medium__6731fa1e.yaml` as the direct DSMZ 904 records.

## Evidence

- MediaDive and the DSMZ 904a PDF support the target pH 6.0 and eight non-water ingredients: 30 g sea salt, 4 g MES, 1 g yeast extract, 1 g tryptone, 0.5 ml of 0.1% w/v sodium resazurin, 2.5 g D-glucose, 0.5 g Na2S x 9 H2O, and 0.5 g L-cysteine HCl x H2O per 1000 ml final volume.
- The 0.5 ml 0.1% w/v sodium resazurin addition is correctly represented as 0.0005 g/L of sodium resazurin in the generated target.
- The preparation text is source-supported: the DSMZ 904a recipe dissolves all components except glucose, sulfide, and cysteine, adjusts to pH 6.0, sparges with 100% N2, dispenses under N2, autoclaves, and then adds glucose, sulfide, and cysteine from sterile anoxic stocks.
- The generated target omits the explicit final 1000 ml distilled water from the MediaDive 904a REST payload and DSMZ 904a PDF.
- The `parent_media` and `merged_from` evidence are over-scoped. Formula equality to the local KOMODO imports was not enough to prove that KOMODO 904 / 904.1 and DSMZ 904a denote the same medium, and the inspected DSMZ 904 source disproves equality for KOMODO 904 as currently described.

## Completeness

- A gitignore-independent exact field scan over the reviewed generated file and all three `merged_from` normalized owners found `parent_media`, `variant_relationship`, and `variant_children`; it found no `sources`, `source_data`, `target_organisms`, `growth_metrics`, `references`, `solutions`, or `sterilization` in those exact files.
- Missing `target_organisms` and `growth_metrics` are acceptable for this review. DSMZ Medium 904a defines a cultivation recipe, but the inspected formulation source does not itself provide a growth metric or a strain-specific outcome.
- The absent `solutions` field is acceptable for this source because DSMZ gives final medium masses for glucose, Na2S x 9 H2O, and L-cysteine HCl x H2O, not source stock concentrations. The anoxic stock-preparation boundary still belongs in structured preparation or sterilization metadata.
- The lack of an explicit `sterilization` block is a non-blocking completeness gap. Autoclaving is preserved in the preparation prose, but a structured sterilization object would make the source's autoclave step checkable.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The generated source-duplicate merge conflates DSMZ 904a with at least one DSMZ 904-derived KOMODO record. | `KOMODO_904_MARINITOGA_medium.yaml` is the `SOURCE_DUPLICATE` parent and claims KOMODO 904 / DSMZ 904 provenance. Inspected DSMZ Medium 904 is pH 7.0 with 6 g/L PIPES; inspected DSMZ Medium 904a is pH 6.0 with 4 g/L MES. | Re-curate `data/normalized_yaml/bacterial/KOMODO_904_MARINITOGA_medium.yaml` and its duplicate links to `data/normalized_yaml/bacterial/marinitoga_hydrogenitolerans_medium.yaml`; then rerun the source-duplicate merge. |
| Major | The target omits the source final-volume water component. | MediaDive 904a and the DSMZ 904a PDF both list distilled water at 1000 ml, but the MediaDive normalized owner and generated target stop at L-cysteine and never represent water or final volume. | Add the supported water/final-volume component to `data/normalized_yaml/bacterial/marinitoga_hydrogenitolerans_medium.yaml`; mirror it into `data/normalized_yaml/bacterial/for_dsm_15518_dsm_15807_and_dsm_16785.yaml` only after its exact KOMODO source identity is confirmed. |

No blocker findings: the generated representative still denotes DSMZ 904a rather than DSMZ 904, and the YAML is valid.

No minor findings found.

## Recommended Edits

1. Split or correct the source-duplicate relation between `data/normalized_yaml/bacterial/KOMODO_904_MARINITOGA_medium.yaml` and `data/normalized_yaml/bacterial/marinitoga_hydrogenitolerans_medium.yaml`. If KOMODO 904 is truly DSMZ 904, it should align with the existing MediaDive 904 record at `data/normalized_yaml/bacterial/marinitoga_medium.yaml`, not with DSMZ 904a.
2. Inspect the KOMODO 904.1 source row behind `data/normalized_yaml/bacterial/for_dsm_15518_dsm_15807_and_dsm_16785.yaml` and decide whether it is a DSMZ 904 subvariant, a DSMZ 904a copy, or a distinct child recipe. Keep its `SOURCE_DUPLICATE` edge only if the source identity really matches DSMZ 904a.
3. Add 1000 ml distilled water or equivalent final-volume representation to `data/normalized_yaml/bacterial/marinitoga_hydrogenitolerans_medium.yaml`, with provenance to DSMZ 904a / MediaDive 904a.
4. Add structured `sterilization` metadata for the autoclave step when the normalized owner is next edited.
5. Regenerate merged records so `data/merge_yaml/merged/marinitoga_hydrogenitolerans_medium__8a96fdfa.yaml` reflects the corrected source ownership and final-volume ingredient.

## Follow-up Checks

- Run the MediaDive REST and DSMZ PDF comparison for both 904 and 904a after the KOMODO records are recured; the fix is correct only if PIPES/pH 7.0 and MES/pH 6.0 remain separated.
- Run `just verify-merges` to prove the corrected source-duplicate graph no longer merges DSMZ 904 into the DSMZ 904a generated record.
- Re-run open-schema, strict, term, and reference validation on this generated record after regeneration.
- Check `data/merge_yaml/merged/marinitoga_medium__6731fa1e.yaml` to confirm the direct MediaDive DSMZ 904 record still remains a separate generated record.

## Additional Notes

- The direct MediaDive import for DSMZ 904, `data/normalized_yaml/bacterial/marinitoga_medium.yaml`, already has the expected pH 7.0 / PIPES formulation and is not merged into this target.
- This review did not inspect the upstream KOMODO website for IDs 904 and 904.1. It only verified that the local KOMODO records' claimed DSMZ 904 provenance conflicts with the inspected DSMZ 904 source when those records are merged into DSMZ 904a.
